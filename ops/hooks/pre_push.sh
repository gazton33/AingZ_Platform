#!/usr/bin/env bash
set -euo pipefail
echo "[hook] pre-push: running V4 checks"
python ops/run_codex_baseline_v4_check.py
pytest -q
