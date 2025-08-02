# AingZ_Platform_main — README v1

> **STATUS:** `UPDATED`
> **Last update:** 2025-08-02 | Author: ChatGPT

---

## 1. Summary
Root bucket that organizes the platform's main modules.

## 2. Backups / Context
- Related backup folder: [BACKUP/](BACKUP/)
- Links to relevant versions or AI backups: [backup/](backup/)

## 3. Cross‑references and Mapping
- **Upward reference:** `[../]`
- **Lateral references:** [./.git/], [./.pytest_cache/], [./BACKUP/], [./__pycache__/], [./apps/], [./backup/], [./connectors/], [./core/], [./infra/], [./legacy/], [./legacy_old/], [./log/], [./mig/], [./packages/], [./scripts/], [./tmp_staging/]
- **Typical destination buckets:** `[../DESTINATION/]`
- **Central crossref:** [Global Map](core/data/crossref_mapping_buckets_aingz_platform_v_1_20250731.md)
- **Relevant pipelines:** [infra/pipelines/README.md](infra/pipelines/README.md)

## 4. Directory Tree Precedence
```text
AingZ_Platform_main/
```

## 4.1 Directory Tree Origin
```text
AingZ_Platform_main/
├── .git/
├── .pytest_cache/
├── BACKUP/
├── __pycache__/
├── apps/
├── backup/
├── connectors/
├── core/
├── infra/
├── legacy/
├── legacy_old/
├── log/
├── mig/
├── packages/
├── scripts/
└── tmp_staging/
```

## 5. Pipeline and Workflows (Lifecycle)
Describes key steps in the lifecycle for the files in this bucket:
1. **Input / LEGACY or TMP:** [legacy/](legacy/) or [tmp_staging/](tmp_staging/)
2. **Staging / MIG:** [mig/](mig/)
3. **Consolidation / CORE:** [core/](core/)
4. **Backup / Deletion:** [backup/](backup/) and/or [BACKUP/](BACKUP/)

Adjust links according to the official pipeline and stages of `LEGACY→TMP→MIG→CORE→BACKUP`.

---

Fill all fields with active links once the real structure is created.

## Terminology
- [Bucket](core/kns/glossary/rw_b_glosario_code_v_2_20250729.md#buck-bucket)
- [Pipeline](core/kns/glossary/rw_b_glosario_code_v_2_20250729.md#pipe-pipeline)
- [Workflow](core/kns/glossary/rw_b_glosario_code_v_2_20250729.md#wf-workflow)
- [Migration](core/kns/glossary/rw_b_glosario_code_v_2_20250729.md#mig-migration)
- [Backup](core/kns/glossary/rw_b_glosario_code_v_2_20250729.md#bk-backup)
