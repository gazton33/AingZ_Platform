#!/usr/bin/env python3
"""CLI to execute Codex baseline v4 check and generate trigger report."""

import argparse
import json
from pathlib import Path


def parse_dictionary(md_path: Path) -> list[dict]:
    """Parse markdown table of CODE_TRIGGERS dictionary."""
    entries: list[dict] = []
    lines = md_path.read_text(encoding="utf-8").splitlines()
    table_started = False
    for line in lines:
        if line.strip().startswith("| ID "):
            table_started = True
            continue
        if table_started:
            if not line.strip().startswith("|"):
                break
            parts = [p.strip() for p in line.strip().split("|")[1:-1]]
            if len(parts) >= 7:
                entries.append(
                    {
                        "ID": parts[0],
                        "CODE": parts[1],
                        "Name": parts[2],
                        "Prompt": parts[3],
                        "CAT": parts[4],
                        "TYP": parts[5],
                        "FileRef": parts[6],
                    }
                )
    return entries


def find_codes(text: str, codes: list[str]) -> list[str]:
    return sorted({code for code in codes if code in text})


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Codex baseline v4 check")
    parser.add_argument(
        "--repo-root",
        default=str(Path(__file__).resolve().parents[1]),
        help="Path to repository root",
    )
    args = parser.parse_args()
    repo_root = Path(args.repo_root)

    prompt_path = repo_root / "platform_v_4_0" / "main" / "prompt_codex_baseline_v_4_check.md"
    dict_path = repo_root / "core" / "rw_b_diccionario_code_triggers_v_2_20250729.md"

    print(f"Loading prompt from {prompt_path}")
    try:
        prompt_text = prompt_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print("Prompt file not found")
        return

    entries = parse_dictionary(dict_path)
    codes = [e["CODE"] for e in entries]
    used_codes = find_codes(prompt_text, codes)
    report = [e for e in entries if e["CODE"] in used_codes]

    report_path = repo_root / "ops" / "trigger_report.json"
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Trigger report written to {report_path}")


if __name__ == "__main__":
    main()
