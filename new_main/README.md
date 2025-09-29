# AingZ Platform - Dir Tree & Templates Seed Pack

This bundle collects the minimal artifacts needed to keep standardizing the directory tree and master templates for the new platform in a clean repository.

## Key Contents
- `templates/architecture_interactive_forms/`
  - Forms, alignment plans, and legacy reference pool (includes `dir_tree_creator_form.md`, `dir_tree_alignment_plan.md`, `dir_tree_draft.excalidraw.md`).
- `templates/master_template_proposals/`
  - Orbit/Nexus/Spectrum proposals, reusable modules, context packs, and supporting docs.
- `templates/master_template_proposals/legacy_reference_pool/`
  - Audits, roadmaps, test harnesses, and validation suites for templates.
- `scripts/diagram_sync/`
  - Stub to automate Mermaid <-> YAML <-> Excalidraw regeneration.
- `templates/Untitled-2025-07-31-2043.excalidraw`
  - Companion canvas used in prior sessions.

## Suggested Next Steps
1. Copy the content of `new_main/` into the root of the new GitHub repository.
2. Implement scripts under `scripts/diagram_sync/` following the README tasks.
3. Update metadata (`dir_tree_source`, `dir_tree_last_sync`) when the Obsidian draft changes.
4. Fill in owners/states in the form matrix and publish required assets per folder.
5. Review the master template proposals and pick the baseline for the platform rollout.

