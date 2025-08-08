import json
from pathlib import Path

import ops.update_crossrefs as uc


def test_update_file_handles_rename_and_case(tmp_path, monkeypatch):
    cache = tmp_path / "paths_cache.json"
    cache.write_text(json.dumps({"blueprint_old.md": "new/BLUEPRINT_NEW.md"}))

    mappings = uc.load_paths_cache(cache)
    crossref = uc.load_crossref_fields(mappings)

    readme = tmp_path / "README.md"
    readme.write_text(
        "see BLUEPRINT_OLD.md\n" "crossref_blueprint: BLUEPRINT_OLD.md\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(uc, "ROOT", tmp_path)
    updates = uc.update_file(readme, mappings, crossref)

    content = readme.read_text()
    assert "new/BLUEPRINT_NEW.md" in content
    assert "crossref_blueprint: new/BLUEPRINT_NEW.md" in content
    assert ("README.md", "blueprint_old.md", "new/BLUEPRINT_NEW.md") in updates


def test_update_file_missing_replaces_with_null(tmp_path, monkeypatch):
    cache = tmp_path / "paths_cache.json"
    cache.write_text(json.dumps({"master_plan_missing.md": None}))

    mappings = uc.load_paths_cache(cache)
    crossref = uc.load_crossref_fields(mappings)

    readme = tmp_path / "README.md"
    readme.write_text(
        "crossref_masterplan: master_plan_missing.md\n", encoding="utf-8"
    )

    monkeypatch.setattr(uc, "ROOT", tmp_path)
    uc.update_file(readme, mappings, crossref)

    assert "crossref_masterplan: null" in readme.read_text()
