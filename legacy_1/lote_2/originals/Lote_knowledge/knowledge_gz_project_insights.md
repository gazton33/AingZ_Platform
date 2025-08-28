# KNOWLEDGE BASE — Lecciones, aprendizajes y buenas prácticas

> Proyecto: **AingZ_Repo / ChatGPT Advanced Workflows**  
> Fecha última actualización: 2025-07-10  
> Autoría y edición: GZ + ChatGPT IA

---

## 1. Principios rectores y aprendizajes clave
- **Documentar siempre:** cada nueva matriz, workflow, prompt o croquis debe versionarse y dejar trazabilidad explícita (fecha, versión, autor/a, referencia).
- **Control cruzado y verificación exhaustiva:** cada matriz extendida debe mapear y cubrir el 100% de la funcionalidad de su matriz RAW/base. Usar controles automáticos/manuales de cobertura.
- **Mínima redundancia:** Evitar duplicación de features en múltiples archivos; usar referencias cruzadas y documentación modular.
- **Naming técnico y bilingüe:** Nombres de features y archivos en inglés técnico, explicaciones y contexto en español para onboarding local/global.
- **Privacidad y seguridad:** Preferir repos privados; nunca volcar datos personales o confidenciales no anonimizados.

## 2. Cosas que **sí** queremos repetir
- Validación iterativa: controles cruzados entre matrices, workflows y knowledge base antes de “congelar” versiones.
- Matrices con código, clase, naming nativo y abreviatura (siempre).  
- Documentar **qué NO debe hacerse** para evitar ciclos de error.
- Incorporar recomendaciones y aprendizajes en los archivos de conocimiento, no sólo en los prompts/workflows.

## 3. Cosas que **NO** queremos repetir
- Perder cobertura de features por falta de mapeo entre matrices.
- Cambiar nombres/abreviaturas entre releases sin migración y sin registro en el control de fuentes.
- Publicar archivos sin control de calidad o validación semántica.
- Olvidar la documentación viva: cada README debe decir para qué NO usar el archivo y cómo se versiona.

## 4. Best practices para expansión y onboarding
- Al sumar nuevas features, siempre agregar código único, clase y referencia de fuente.
- Si una feature deja de usarse, marcar como deprecated, no borrar; mantener trazabilidad histórica.
- Documentar errores y decisiones “fallidas” en la base para no repetirlos en el futuro.
- Usar README y knowledge base como puente con nuevos colaboradores.

## 5. Referencias clave
- [matriz_extendida_features_chatgpt_workflow.md](../knowledges/matriz_extendida_features_chatgpt_workflow.md)
- [control_trazabilidad_fuentes_chatgpt_workflow.md](../matrices/control_trazabilidad_fuentes_chatgpt_workflow.md)
- [croquis-mapeo-features-prompts.md](../doc/croquis-mapeo-features-prompts.md)
- [control-cruce-matriz-raw-vs-extendida.md](../matrices/control-cruce-matriz-raw-vs-extendida.md)

