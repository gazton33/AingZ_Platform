import os
import json
from pathlib import Path

TARGETS = [
    "Prompt_Codex_Baseline_V4_Check.md",
    "rw_b_blueprint_v_4_extendido_2025_08_06.md",
    "rw_b_master_plan_v_4_extendido_2025_08_06.md",
    "core/rulset/RULE_CODING_COMPLIANCE_V4.md",
]

def sweep(root: Path) -> dict:
    paths = {t: None for t in TARGETS}
    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            rel_path = (Path(dirpath) / name).relative_to(root).as_posix()
            for target in TARGETS:
                if rel_path.endswith(target):
                    paths[target] = rel_path
    return paths

def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    found_paths = sweep(repo_root)
    cache_file = Path(__file__).with_name("paths_cache.json")
    cache_file.write_text(
        json.dumps(found_paths, indent=2, ensure_ascii=False) + "\n"
    )
    for target, path in found_paths.items():
        print(f"{target}: {path}")

if __name__ == "__main__":
    main()
