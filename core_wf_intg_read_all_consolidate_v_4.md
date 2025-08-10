---

## file: core/wf/INTG\_ReadAll\_Consolidate\_V4.md code: INTG4 name: IntegracionLecturaConsolidacionV4 version: v4.0 date: 2025-08-09 owner: AingZ\_Platform · RwB status: active xrf: blueprint: RwB\_Blueprint\_V4 mplan: RwB\_MasterPlan\_V4 glossary: CODE\_Glossary\_v2 dictionary: CODE\_Triggers\_v2 triggers: [TRG\_CONSOLIDATE\_TL, TRG\_AUDIT\_TL, TRG\_LSWP, TRG\_PURGE\_AI] chg: CHG\_main.md#intg\_readall\_consolidate\_v4 chk: CHK\_root.md#intg\_readall\_consolidate\_v4

# WF — Integración, lectura total y consolidación V4 (sin pérdida de información)

## Objetivo

Integrar **todo el conocimiento** de la plataforma (README de cada bucket/asset, Blueprint V4, Master Plan V4, prompts y rulesets), **sin pérdida**, generando un **Corpus V4** único para análisis, detección de incoherencias y posterior purga/normalización. Salida **GPT‑5 / Codex‑ready**.

## Alcance

- Árbol completo: `core/`, `ops/`, `packages/`, `lifecycle/`, `snapshots_ctx/`, `library/`.
- Archivos foco: `README*.md`, `readme*.md`, `*_blueprint_*`, `*_master_plan_*`, `prompt_*`, `RULE_*`.

## Roles

- **Agent**: orquestación (workflows, harvest, diffs, PRs).
- **Codex**: tallado masivo/estandarización.
- **Usuario**: aprobaciones/merge y resolución de conflictos semánticos.

## Flujo (alto nivel)

1. **Tallado V4** de READMEs legacy → normalizar front‑matter + OutputTemplate.
2. **Crossref Fix** → rutas vivas, sin links rotos.
3. **Harvest** → indexar y consolidar todo en un **Corpus V4** (sin perder texto).
4. **Diff & Checks** → confirmar **0 pérdida** de líneas/secciones; listar incoherencias.
5. **Purga** → proponer merges/splits/renames con PRs atómicos.
6. **Endurecer CI** → bloquear regresiones.

## Entradas

- `ops/paths_cache.json` (mapeo nombre→ruta canónica).
- Reglas: `core/rulset/RULE_CODING_COMPLIANCE_V4.md`.

## Salidas (artefactos)

- `ops/data/index/knowledge_index.json` (índice completo).
- `ops/log/harvest_readmes.md` (inventario literal).
- `library/intg/Corpus_Platform_V4.md` (consolidado textual).
- `ops/log/diff_summary.md` + `ops/data/diff_report.json` (no‑regresión).
- PRs: *tallado*, *crossref-fix*, *cleanup*, *purga*.

---

## Procedimiento detallado (paso a paso)

### Paso A — Tallado (Codex‑ready)

- Ejecutar **AingZ Tallado READMEs V4** (ya en `.github/workflows/aingz_tallado_readmes.yml`).
- Asegura: campos V4 (`CODE, ID, VERSION, ROUTE, CROSSREF, AUTHOR, DATE`) + `## OutputTemplate`.

### Paso B — Crossref

- Ejecutar **AingZ Crossref Fix** (ya en `.github/workflows/aingz_crossref_fix.yml`).
- Reescribe referencias según `ops/paths_cache.json`.

### Paso C — Harvest (integración sin pérdida)

**Nuevo workflow propuesto**: `.github/workflows/aingz_harvest_knowledge.yml`\
Crea índice + corpus sin eliminar ni reescribir contenido.

```yaml
name: AingZ Harvest Knowledge
on:
  workflow_dispatch:
    inputs:
      reason:
        description: motivo
        required: true
        default: "harvest"
permissions:
  contents: write
  pull-requests: write
jobs:
  harvest:
    runs-on: ubuntu-latest
    steps:
      - name: App token
        id: app
        uses: tibdex/github-app-token@v2
        with:
          app_id: ${{ secrets.APP_ID }}
          installation_id: ${{ secrets.INSTALLATION_ID }}
          private_key: ${{ secrets.APP_PRIVATE_KEY }}
      - uses: actions/checkout@v4
        with: { token: ${{ steps.app.outputs.token }} }
      - name: Build index & corpus (no-loss)
        run: |
          python - <<'PY'
          from pathlib import Path
          import hashlib, json, re
          ROOT = Path('.')
          out_idx = ROOT/"ops/data/index/knowledge_index.json"
          out_inv = ROOT/"ops/log/harvest_readmes.md"
          out_cps = ROOT/"library/intg/Corpus_Platform_V4.md"
          out_idx.parent.mkdir(parents=True, exist_ok=True)
          out_inv.parent.mkdir(parents=True, exist_ok=True)
          out_cps.parent.mkdir(parents=True, exist_ok=True)

          def read(p): return p.read_text(encoding='utf-8', errors='ignore')
          def sha1(s): return hashlib.sha1(s.encode('utf-8')).hexdigest()
          def parse_fm(txt):
            if not txt.startswith('---\n'): return None, txt
            j = txt.find('\n---',4)
            if j==-1: return None, txt
            fm = txt[4:j]
            body = txt[j+4:].lstrip('\n')
            meta = {}
            for line in fm.splitlines():
              if ':' in line and not line.strip().startswith('#'):
                k,v = line.split(':',1)
                meta[k.strip()] = v.strip()
            return meta, body

          items=[]; inv_lines=["# Harvest — Inventario\n"]; corp=["# Corpus_Platform_V4\n"]
          targets = []
          for p in ROOT.rglob("*.md"):
            low = p.name.lower()
            if ('readme' in low) or ('blueprint' in low) or ('master_plan' in low) or ('prompt' in low) or low.startswith('rule_') or low.startswith('ruleset') or low.startswith('rule'):
              targets.append(p)
          # orden por bucket y ruta
          targets = sorted(targets, key=lambda q: q.as_posix())

          for p in targets:
            txt = read(p)
            meta, body = parse_fm(txt)
            h = sha1(txt)
            item = {
              'path': p.as_posix(),
              'sha1': h,
              'bytes': len(txt.encode('utf-8')),
              'has_front_matter': bool(meta),
              'meta': meta or {}
            }
            items.append(item)
            inv_lines.append(f"- {p.as_posix()} | sha1:{h} | fm:{bool(meta)}")
            # agregar al corpus SIN modificar el cuerpo
            corp.append(f"\n## {p.as_posix()}\n")
            corp.append(txt)

          out_idx.write_text(json.dumps(items, indent=2), encoding='utf-8')
          out_inv.write_text("\n".join(inv_lines)+"\n", encoding='utf-8')
          out_cps.write_text("\n".join(corp)+"\n", encoding='utf-8')
          print(f"Indexed {len(items)} files → {out_idx}")
          PY
      - name: Create PR
        uses: peter-evans/create-pull-request@v6
        with:
          token: ${{ steps.app.outputs.token }}
          commit-message: "AingZ Agent: harvest"
          branch: bot/aingz/harvest-${{ github.run_id }}
          title: "Agent: harvest knowledge"
          body: "Índice + corpus consolidado (sin pérdida). Ver ops/log/harvest_readmes.md y library/intg/Corpus_Platform_V4.md."
          base: main
          delete-branch: true
```

### Paso D — No‑regresión (no pérdida)

**Nuevo workflow propuesto**: `.github/workflows/aingz_diff_guard.yml`\
Compara conteo de líneas/secciones antes/después y genera reportes.

```yaml
name: AingZ Diff Guard
on:
  pull_request:
    paths:
      - "**/*.md"
permissions: { contents: read }
jobs:
  diff:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 0 }
      - name: No-loss check
        run: |
          base=$(git merge-base HEAD^ HEAD || echo HEAD^)
          git diff --unified=0 "$base" HEAD -- "**/*.md" > diff.patch || true
          added=$(grep -c '^\+' diff.patch || true)
          removed=$(grep -c '^-\' diff.patch || true)
          echo "added=$added removed=$removed"
          # criterio simple: no permitir más removals que additions cuando cambian READMEs
          if [ "$removed" -gt "$added" ]; then
            echo "Potential loss detected"; exit 1; fi
```

### Paso E — Purga / Cleanup (posterior a validación)

- Matriz de incoherencias (títulos repetidos, definiciones conflictivas).
- PRs atómicos de fusión/split/rename.
- Actualización `ops/paths_cache.json` + `AingZ Crossref Fix`.

---

## Estándar GPT‑5 / Codex‑ready (aplicable a TODOS los docs)

- **Lenguaje**: imperativo, inequívoco, trazable; evitar ambigüedad.
- **Estructura**: front‑matter V4 + secciones: *Objetivo, Inputs, Pasos, Salidas, Validación, Observaciones*.
- **Bloques**: código y YAML con parámetros explícitos; evitar prosa larga en tablas.
- **Triggers**: incluir `TRG_*` relevantes en front‑matter y referenciarlos en el flujo.
- **Conectores**: indicar `github/notion` cuando aplique; rutas exactas; formatos de salida (`.md`, `.json`).

---

## Aceptación

- `Corpus_Platform_V4.md` contiene **todo** lo cosechado (hash y conteos coinciden con el inventario).
- `diff_guard` en **verde**.
- `ci_audit.yml` en **verde**.
- PRs de purga aprobados.

---

## Plan inmediato (orden recomendado)

1. Cargar workflows **Harvest** y **Diff Guard** (los YAML de arriba).
2. Ejecutar: **Tallado** → **Crossref Fix** → **Harvest**.
3. Revisar `Corpus_Platform_V4.md` + `harvest_readmes.md`.
4. Ejecutar **PRs de purga** (si aparecen incoherencias).
5. Dejar `ci_audit.yml` y `diff_guard` como checks requeridos en rama protegida.

---

# OutputTemplate (obligatorio)

output\_example: status: OK id\_asset: intg\_readall\_consolidate\_v4 generated\_by: ai created\_at: 2025-08-09T00:00:00-03:00 params: - mode: full - preserve\_loss: true result: - indexed\_files: 0 - corpus\_path: library/intg/Corpus\_Platform\_V4.md - inventory\_path: ops/log/harvest\_readmes.md log: - step1: tallado - step2: crossref - step3: harvest - step4: diff\_guard

