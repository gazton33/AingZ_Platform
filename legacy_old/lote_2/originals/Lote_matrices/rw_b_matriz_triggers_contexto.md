# [RwB] MATRIZ DE TRIGGERS — Archivo vs Contexto vs Procedimiento (v1)

> Esta matriz organiza los **triggers operativos del sistema RwB** según:
> - tipo de archivo involucrado (CAT)
> - contexto de uso (PR, CO, CL)
> - propósito o ciclo de ejecución

---

## 🧭 Leyenda
- ✅ Aplicación directa del trigger en ese contexto y tipo
- ⚠️ Aplicable con adaptaciones o revisión
- ⛔ No aplica (uso inválido o fuera de alcance)

---

## 📊 Matriz Triggers x CAT x Contexto

| Trigger             | MTR | SCR | WF  | DOC | LOG | NB  | CFG | TMP | CHK | IMG | KNS | PR  | CO  | CL  | Propósito / Notas Breves                                   |
|---------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|--------------------------------------------------------------|
| **CP**              | ✅  | ✅  | ✅  | ✅  | ⚠️  | ✅  | ⚠️  | ✅  | ✅  | ⛔  | ✅  | ✅  | ✅  | ✅  | Cierre de hilo o ciclo, genera acta o snapshot              |
| **AUD**             | ✅  | ✅  | ✅  | ⚠️  | ✅  | ⚠️  | ⚠️  | ✅  | ✅  | ⛔  | ✅  | ✅  | ✅  | ✅  | Auditoría completa de outputs y cobertura literal           |
| **MIG**             | ✅  | ✅  | ⚠️  | ⚠️  | ✅  | ⚠️  | ⚠️  | ⛔  | ⛔  | ⛔  | ✅  | ✅  | ⚠️  | ⚠️  | Migración legacy a estándar RwB                             |
| **REV**             | ✅  | ✅  | ✅  | ✅  | ✅  | ✅  | ✅  | ✅  | ✅  | ✅  | ✅  | ✅  | ✅  | ✅  | Marca revisión pendiente (manual, profunda, iterativa)     |
| **TMP tipo**        | ⚠️  | ✅  | ✅  | ✅  | ⛔  | ⛔  | ✅  | ⛔  | ✅  | ⛔  | ⚠️  | ✅  | ✅  | ⚠️  | Generación automática de plantilla por categoría            |
| **BARRIDO_LITERAL** | ✅  | ✅  | ✅  | ✅  | ✅  | ✅  | ⚠️  | ⚠️  | ⚠️  | ⛔  | ✅  | ✅  | ✅  | ✅  | Relevamiento sin interpretación (fase inicial o validación) |
| **ONB**             | ⚠️  | ⚠️  | ✅  | ✅  | ⛔  | ⛔  | ✅  | ✅  | ✅  | ⛔  | ⚠️  | ✅  | ✅  | ✅  | Onboarding de proyecto, sistema o usuario                   |
| **CLS**             | ✅  | ✅  | ✅  | ⚠️  | ⚠️  | ⚠️  | ✅  | ⚠️  | ✅  | ⛔  | ✅  | ✅  | ✅  | ✅  | Clasificación de outputs en batches o por naming            |
| **TUN**             | ⚠️  | ✅  | ✅  | ✅  | ⛔  | ✅  | ✅  | ⚠️  | ⚠️  | ⛔  | ✅  | ✅  | ✅  | ⚠️  | Ajuste iterativo por feedback o evolución de uso            |
| **VAL**             | ✅  | ✅  | ✅  | ⚠️  | ✅  | ⚠️  | ✅  | ⚠️  | ✅  | ⛔  | ✅  | ✅  | ✅  | ✅  | Validación técnica o estructural previa a cierre            |
| **TAG_x**           | ⚠️  | ⚠️  | ⚠️  | ⚠️  | ⚠️  | ⚠️  | ⚠️  | ⚠️  | ⚠️  | ⚠️  | ⚠️  | ✅  | ✅  | ✅  | Subtag extensible según propósito específico (IMG, TEST)    |

---

## 🧩 Notas adicionales:
- **Contexto PR** permite mayor libertad en naming y testing.
- **Contexto CL** requiere validación y plantilla explícita en todo archivo con `TMP`, `VAL`, `AUD`, `REV`.
- **BARRIDO_LITERAL** se recomienda en todo nuevo hilo/ciclo o migración.
- **ONB** debe siempre generar un LOG + CFG asociados.

---

**FIN MATRIZ v1**

