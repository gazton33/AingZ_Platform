---

## file: core/doc/workbench/AINGZ\_V5\_Baselines\_Unificados\_v1\_4\_locked.md code: ARB\_AST name: AINGZ\_V5\_Baselines\_Unificados version: v1.4 date: 2025-08-16 owner: AingZ\_Platform · QMS status: locked refs: baseline\_prev: core/doc/workbench/AINGZ\_V5\_Baselines\_Unificados\_v1\_3\_locked.md glosario\_final: main/data\_base/core\_actv/data/semantics/glossary/GLOS\_AINGZ\_V5\_FULL\_v1\_0.md sem\_ruleset: main/data\_base/core\_actv/data/semantics/ruleset/SEM\_RULESET\_AINGZ\_V5\_v0\_1.md chkp: main/data\_base/core\_actv/data/guides/planin/chkp/CHKP\_2025\_08\_16\_GLOSv1\_0.md valog: main/log/validation/VALOG\_GLOS\_AINGZ\_V5\_FULL\_2025\_08\_16.md triggers: [TRG\_AUDIT\_TL, TRG\_CONSOLIDATE\_TL] chg: [CHG-2025-08-16-001, CHG-2025-08-16-002, CHG-2025-08-16-003, CHG-2025-08-16-004] chk: CHK#baseline\_lock\_v1\_4 notes: "Snapshot **LOCKED**: árbol + assets + alias\_final en EN; alineado 1:1 a GLOS v1.0 (MAPX PASS)."

# AingZ V5 — **Baselines Unificados v1.4 (LOCKED)**

> **Objeto**: congelar el **árbol de directorios** y los **assets** con sus *alias\_final* como **fuente de verdad** para la Fase 2. Incluye **rename** y **altas** aprobadas en CHKP.

---

## 0) Principios de este baseline

- Naming técnico en **idioma nativo** (SDK/API/PL), con \`\` en español (ver SEMR).
- **MAPX** 1:1 entre Glosario v1.0 y este árbol (sin órfanos).
- Cambios respecto a v1.3 documentados en **CHG-001..004**.

---

## 1) Árbol de directorios (v1.4)

```text
main/
  data_base/
    core_actv/
      docs/
        audio/
        image/
        video/
        library/
        onboard/
      data/
        semantics/
          glossary/
          dicts/
          code_dict/
          trigger_dict/
          app_dict/
          prompt_dict/
          ingest_prompts/
          vocabulary/
          ruleset/                 # SEM_RULESET_AINGZ_V5_v0_1.md
        ai_learn/
          learning/
          evaluation/
          insights/
          fine_tuning/
          few_shot/
          relevance/
          training/
          feedback/
        develop/
          ruleset/
          config/
          setup/
          customization/
          specs/
          preferences/
          connectors/
          orchestrator/
        out_template/
          mtx/
            matrix/
            table/
            record_sheet/
            mapping/
            relation/
            validation/
            comparison/
          docs/                    # DOCS (nuevo)
          workspaces/              # WSPC (nuevo)
          platform_arch/           # PARCH (nuevo)
          ai_tools/                # ATOOL (nuevo)
        guides/
          planin/
            mpln/
            brainstorm_crtv/
          run_control/             # RCNT (nuevo: START/STOP/RESUME/ROLLBACK)
          pipeline/
        wf_playbooks/              # rename desde wf_template/ (WFPB)
      log/
        changelog/
        validation/
        qms/
```

> **Nota**: Las carpetas marcadas como **(nuevo)**/rename provienen de **CHG-002..004**.

---

## 2) Alias\_final (EN) por bucket — extracto

| Bucket/Path                                                   | Alias\_final (ejemplos)                                                                                          |
| ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| docs/audio                                                    | audio\_notes, meetings, interviews, podcast, audio\_from\_video                                                  |
| docs/image                                                    | photos, images, graphics, schematics, diagrams, blueprints, exploded\_views                                      |
| docs/video                                                    | videos, youtube, animations, presentations                                                                       |
| docs/library                                                  | books, manuals, guides, articles, papers                                                                         |
| docs/onboard                                                  | notes, messages, observations                                                                                    |
| data/semantics/\*                                             | glossary, trigger\_dict, code\_dict, app\_dict, prompt\_dict, ingest\_prompts, vocabulary                        |
| data/ai\_learn/\*                                             | learning, evaluation, insights, fine\_tuning, few\_shot, relevance, training, feedback                           |
| data/develop/\*                                               | ruleset, config, setup, customization, specs, preferences, connectors, orchestrator                              |
| data/out\_template/mtx/\*                                     | matrix, table, record\_sheet, mapping, relation, validation, comparison                                          |
| data/out\_template/{docs,workspaces,platform\_arch,ai\_tools} | docs\_template, workspace\_template, platform\_arch\_template, ai\_tool\_template                                |
| guides/run\_control                                           | run\_control (START, STOP, RESUME, ROLLBACK)                                                                     |
| guides/pipeline/\*                                            | creator, relev, audit, consolidation, migration, update, cleanup, validation, test, literal\_work, report, clone |
| data/wf\_playbooks                                            | wf\_playbook                                                                                                     |
| log/{changelog,validation,qms}                                | change\_log, validation\_log, traceability, cross\_ref, versioning                                               |

---

## 3) Delta v1.3 → v1.4 (estructura)

```diff
- data/wf_template/
+ data/wf_playbooks/              # CHG-002
+ data/out_template/docs/         # CHG-003
+ data/out_template/workspaces/   # CHG-003
+ data/out_template/platform_arch/# CHG-003
+ data/out_template/ai_tools/     # CHG-003
+ guides/run_control/             # CHG-004
```

---

## 4) Garantías y alcance del baseline

- **Integridad MAPX**: validada en **VALOG 2025-08-16**.
- **Compatibilidad V2→V5**: deprecaciones consolidadas (`RWB/RWS`→`SPEC`; `wf_template`→`wf_playbooks`).
- **Owners**: ver propuesta en Glosario v1.0 §2A (asignar nombres propios antes de cambios de producción).

---

## 5) Checklist de cierre (LOCKED)

-

---

## 6) OutputTemplate (de este baseline)

```yaml
output_example:
  status: LOCKED
  id_asset: aingz_v5_baselines_unificados_v1_4
  generated_by: ai
  created_at: 2025-08-16T00:00:00-03:00
  params:
    - from: v1.3
    - chg: [002,003,004]
    - aligned_to: GLOS_AINGZ_V5_FULL_v1_0
  result:
    - tree: updated
    - alias_final: applied
    - mapx: pass
  log:
    - step1: apply_chg
    - step2: update_tree
    - step3: verify_mapx
    - step4: lock_baseline
```

