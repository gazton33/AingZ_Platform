#!/usr/bin/env python3
"""
Script RwB: Procesamiento masivo de PDFs y auditoría genérica
Versión: v1
Requerimientos: PyPDF2, openai, jinja2
"""
import os
import argparse
from PyPDF2 import PdfReader
from datetime import date
import openai
from jinja2 import Template

# Configurar tu API key de OpenAI como variable de entorno: OPENAI_API_KEY


def list_pdfs(directory):
    """Listar todos los archivos .pdf en el directorio dado."""
    return [f for f in os.listdir(directory) if f.lower().endswith('.pdf')]


def extract_title(pdf_path):
    """Extraer título del PDF desde metadata o primera página."""
    reader = PdfReader(pdf_path)
    meta = reader.metadata
    if meta and meta.title:
        return meta.title
    first_page = reader.pages[0]
    text = first_page.extract_text() or ""
    return text.strip().splitlines()[0]


def sanitize_filename(name):
    """Convertir nombre a minúsculas y reemplazar espacios por guiones bajos."""
    return name.strip().lower().replace(' ', '_')


def analyze_pdf(pdf_path, model="gpt-4"):  
    """Realiza un barrido literal usando la API de OpenAI y devuelve snapshots por página."""
    reader = PdfReader(pdf_path)
    snapshots = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        if not text.strip():
            continue
        # Preparar mensaje
        messages = [
            {"role": "system", "content": "Eres un asistente especializado en extraer extractos literales relevantes del texto dado."},
            {"role": "user", "content": f"Extrae el extracto literal más relevante de la siguiente sección del PDF (página {i+1}). Responde solo con el extracto sin explicaciones:\n'''{text}'''"}
        ]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            max_tokens=300
        )
        extract = response.choices[0].message.content.strip()
        total_tokens = response.usage.total_tokens if hasattr(response.usage, 'total_tokens') else None
        snapshots.append({"page": i+1, "extract": extract, "tokens": total_tokens})
    return snapshots


def generate_audit_markdown(pdf_name, output_path, metadata, snapshots):
    """Generar archivo markdown de auditoría con snapshots y metadata."""
    template_str = '''# [AUDITORÍA_LITERAL_RAW_V1] — Relevamiento completo {{ metadata['archivo'] }}

**Archivo:** {{ metadata['archivo'] }}  
**Título extraído:** {{ metadata['titulo'] }}  
**Fecha auditoría:** {{ metadata['fecha'] }}  
**Modelo:** GPT-4  
**Tokens utilizados:** {{ metadata['tokens'] or 'N/A' }}  
**Cobertura:** 100%  

---

## 1. Snapshots chunked (extractos clave)
| Chunk # | Página(s) | Extracto literal | Tokens |
|---------|-----------|------------------|--------|
{% for snap in snapshots %}| {{ loop.index }} | {{ snap.page }} | {{ snap.extract }} | {{ snap.tokens or 'N/A' }} |
{% endfor %}

---

## 2. Insights preliminares
- (Revisar extracts para temáticas generales)

---

## 3. Metadatos adicionales
- Estado auditoría: [RAW]
- Comentarios: 

---
'''  # Extender según necesidades
    tpl = Template(template_str)
    rendered = tpl.render(metadata=metadata, snapshots=snapshots)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(rendered)


def main():
    parser = argparse.ArgumentParser(
        description='Procesamiento masivo de PDFs y auditoría genérica (etapa 1)'
    )
    parser.add_argument(
        '-d', '--directory', default='.', help='Directorio con archivos PDF'
    )
    args = parser.parse_args()

    pdfs = list_pdfs(args.directory)
    if not pdfs:
        print('No se encontraron archivos PDF en', args.directory)
        return

    print('Archivos PDF disponibles:')
    for i, pdf in enumerate(pdfs, 1):
        print(f" {i}. {pdf}")

    sel = input('Selecciona archivos (números separados por coma) o "all": ')
    indices = []
    if sel.strip().lower() == 'all':
        indices = list(range(1, len(pdfs)+1))
    else:
        for part in sel.split(','):
            try:
                idx = int(part)
                if 1 <= idx <= len(pdfs):
                    indices.append(idx)
            except ValueError:
                pass

    for idx in indices:
        original_pdf = pdfs[idx-1]
        full_path = os.path.join(args.directory, original_pdf)
        print(f'\nProcesando: {original_pdf}')

        # Extraer título
        titulo = extract_title(full_path)
        print(f' Título detectado: {titulo}')

        # Propuesta de nuevo naming
        suggested = sanitize_filename(titulo)
        print(f' Nombre sugerido (base): {suggested}')

        # Ingreso manual de nombre
        user_input = input(f'Introduce nuevo nombre base o presiona Enter para usar "{suggested}": ')
        final_base = sanitize_filename(user_input) if user_input.strip() else suggested
        new_pdf_name = f"{final_base}.pdf"
        print(f' Nombre final aplicado: {new_pdf_name}')

        # Renombrar archivo
        new_path = os.path.join(args.directory, new_pdf_name)
        os.rename(full_path, new_path)
        full_path = new_path

        # Metadata inicial
        metadata = {
            'archivo': new_pdf_name,
            'titulo': titulo,
            'fecha': date.today().isoformat(),
            'tokens': None,
        }

        # Análisis con OpenAI
        print(' Iniciando análisis con OpenAI...')
        snapshots = analyze_pdf(full_path)
        metadata['tokens'] = sum(snap['tokens'] for snap in snapshots if snap['tokens'])

        # Generar auditoría Markdown
        md_name = f"{os.path.splitext(new_pdf_name)[0]}_auditoria.md"
        md_path = os.path.join(args.directory, md_name)
        generate_audit_markdown(new_pdf_name, md_path, metadata, snapshots)
        print(' Auditoría generada en', md_path)

if __name__ == '__main__':
    main()
