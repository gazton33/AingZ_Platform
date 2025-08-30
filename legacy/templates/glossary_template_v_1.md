---

file: templates/glossary/Glossary\_Template\_v1\_1\_linked.md code: GTPL11 name: GlossaryTemplateV1\_1Linked version: v1.1.0 date: 2025-08-18 owner: AingZ\_Platform · RwB status: template referencias: [DTT11] triggers: [TRG\_GLOSSARY] cambios:

- 2025-08-18: Añade namespaces, política anti-archivo y formato de IDs. checks:
- IDs únicos `GLOS::<ID>` (3–8 alfanum mayúscula)
- Refs sólo a `DIR::`
- Sin rutas de archivos ni anclas

---

# Glosario — Plantilla v1.1 enlazada

**Contrato**: Término → Definición → Refs a buckets `DIR::`. Sin enlaces a archivos.

## Namespaces y políticas

```yaml
namespaces: { dir: "DIR::", glos: "GLOS::" }
policies: { no_file_refs: true }
```

## Tabla (rellenar)

| ID (GLOS::) | Término    | Definición breve      | Refs (DIR::)         | Sinónimos | Tags      |
| ----------- | ---------- | --------------------- | -------------------- | --------- | --------- |
| GLOS::      | \<término> | \<definición concisa> | [[DIR::]], [[DIR::]] |           | #glosario |

## Reglas mínimas

1. `ID` estable y único. No reutilizar.
2. Definición ≤ 25 palabras. Sin dependencias tecnológicas.
3. Refs sólo a buckets `DIR::`. Cero rutas absolutas/relativas.
4. Términos con impacto crean ADR.

## Checklist

-

## OutputTemplate

```yaml
output_example:
  status: GLOSSARY_TEMPLATE_READY
  created_at: 2025-08-18T00:00:00-03:00
  result:
    - terms_defined: <n>
  log:
    - step1: author
    - step2: link_dirs
    - step3: validate
```

