---

file: templates/\_baselines/glossary/Glossary\_Template\_Baseline\_v1\_1\_locked.md code: GTBL name: GlossaryTemplateBaselineV1\_1 version: v1.1.0 date: 2025-08-18 owner: AingZ\_Platform · RwB status: locked referencias: [GTPL11, DTT11, PCTRL] triggers: [TRG\_BASELINE\_LOCK, TRG\_GLOSSARY] cambios:

- 2025-08-18: Congelada la plantilla enlazada del glosario. checks:
- IDs únicos `GLOS::<ID>` (3–8 alfanum mayúscula)
- Refs sólo `DIR::`
- `no_file_refs: true`

---

# Glosario — Plantilla (Baseline v1.1 bloqueado)

**Objetivo**: registrar definiciones canónicas y sus referencias a buckets.

**Notas**: definiciones ≤ 25 palabras; IDs estables; cambios con impacto → ADR.

## Namespaces y políticas

```yaml
namespaces: { dir: "DIR::", glos: "GLOS::" }
policies: { no_file_refs: true }
```

## Tabla (plantilla)

| ID (GLOS::) | Término    | Definición breve      | Refs (DIR::)         | Sinónimos | Tags      |
| ----------- | ---------- | --------------------- | -------------------- | --------- | --------- |
| GLOS::      | \<término> | \<definición concisa> | [[DIR::]], [[DIR::]] |           | #glosario |

## Reglas mínimas

1. `ID` estable y único.
2. Refs sólo a `DIR::`.
3. Sin anclas ni rutas.

## Checklist

-

## OutputTemplate

```yaml
output_example:
  status: GLOSSARY_TEMPLATE_BASELINE_LOCKED
  created_at: 2025-08-18T00:00:00-03:00
  result:
    - constraints: { id_len: 3-8, refs: DIR:: }
  log:
    - step1: author
    - step2: validate
    - step3: freeze
```

