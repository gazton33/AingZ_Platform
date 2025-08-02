# Matriz de límites de ventana de contexto en modelos ChatGPT (jul‑2025)

[BARRIDO\_LITERAL]

| Modelo                    | Ventana de contexto (tokens) | \~Palabras | Máx tokens de salida | Estado           |
| ------------------------- | ---------------------------- | ---------- | -------------------- | ---------------- |
| text‑davinci‑003          | 2 049                        | \~1 537    | 2 049‑prompt         | Legacy           |
| gpt‑3.5‑turbo‑0613        | 4 096                        | \~3 072    | 4 096‑prompt         | Legacy           |
| gpt‑3.5‑turbo‑1106 / 0125 | 16 384                       | \~12 288   | 16 384‑prompt        | Activo (default) |
| gpt‑4‑0613                | 8 192                        | \~6 144    | 8 192‑prompt         | Legacy/UI        |
| gpt‑4‑turbo‑0125          | 128 000                      | \~96 000   | 4 096                | Activo API       |
| gpt‑4o (mini/std)         | 128 000                      | \~96 000   | 4 096 (16 k img)     | Activo           |
| o3                        | 200 000                      | \~150 000  | 100 000              | Activo           |
| o3‑mini                   | 200 000                      | \~150 000  | 100 000              | Activo           |
| gpt‑4.1 (std)             | 1 000 000                    | \~750 000  | 65 536               | Activo           |
|                           |                              |            |                      |                  |

| **o4‑mini**       | 512 000\* | \~384 000 | 8 192\*  | Anunciado (TBC) |
| ----------------- | --------- | --------- | -------- | --------------- |
| **o4‑mini‑high**  | 512 000\* | \~384 000 | 16 384\* | Anunciado (TBC) |
| **gpt‑4.5 (std)** | 256 000\* | \~192 000 | 8 192\*  | Rumor           |

\*Valores preliminares basados en roadmap; sujetos a cambio.

---

## Desglose típico de un contexto vivo en un hilo

```text
System / Dev / Tools      3‑10 %
Personalización / Memoria 1‑5 %
Adjuntos & Canvas         0‑60 % (según tamaño de archivos)
Historial Usuario         10‑30 %
Historial Asistente       10‑30 %
Respuesta actual          2‑5 % (max_tokens)
```

> **Nota:** asegúrate de que la suma de todos los componentes no supere la ventana de contexto del modelo. Conversión aproximada → palabras ≈ tokens × 0,75.

---

## Auditoría de tokens – Instrucciones de ejecución

### 1. Prompt rápido dentro de ChatGPT

> **Prompt**:\
> *«Eres un auditor de tokens. Analiza todo el historial presente ✅ y devuélveme un JSON con **`role`**, **`tokens`**, **`percent_of_context`** (suponiendo ventana = \<MODEL\_CONTEXT>) y totales. Usa el mismo tokenizador que el modelo.»*

- Cambia `<MODEL_CONTEXT>` por el límite de la tabla.
- El propio modelo devolverá un resumen sin código externo.

### 2. Auditoría reproducible vía script Python + OpenAI

Requisitos:

```bash
pip install tiktoken openai
```

Script base:

```python
import tiktoken, json, openai

MODEL       = "gpt-4o"          # o el que uses
CTX_LIMIT   = 128_000            # ajusta desde la matriz
chat_history = [                 # lista de dicts role/content
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."},
    # ...
]

enc   = tiktoken.encoding_for_model(MODEL)
rows  = []
total = 0

for m in chat_history:
    n = len(enc.encode(m["content"]))
    rows.append({"role": m["role"], "tokens": n})
    total += n

for r in rows:
    r["percent_of_context"] = round(100 * r["tokens"] / CTX_LIMIT, 3)

report = {
    "model": MODEL,
    "context_limit": CTX_LIMIT,
    "total_tokens": total,
    "percent_used": round(100 * total / CTX_LIMIT, 3),
    "details": rows,
}

print(json.dumps(report, indent=2, ensure_ascii=False))
```

**Pasos:**

1. Exporta tu historial a `chat_history` con los mensajes que quieras medir (incluye system, tool calls, etc.).
2. Ajusta `MODEL` y `CTX_LIMIT` con los valores de esta matriz.
3. Ejecuta. Obtendrás un JSON con tokens por rol y porcentaje de uso.

### 3. Buenas prácticas para no exceder contexto

1. **Chunking & resumen**: divide texto extenso y condensa antes de añadir.
2. **Function calling / JSON mode**: reduce tokens “decorativos”.
3. **Paginar**: si esperas salida > máx tokens, pide en lotes.
4. **Monitorear**: usa el script regularmente para prever errores `context_length_exceeded`.

---

[REVISION\_PENDING] Actualizar al publicarse límites oficiales definitivos de la serie o4 / o4‑mini‑high, gpt‑4.5 y futuros modelos. Mantener alineado el script con cambios de tokenizador o API.

