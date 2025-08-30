#!/usr/bin/env bash
# Apply or preview directory creation/removal plans.

set -euo pipefail

MODE="dry-run"
if [[ ${1:-} == "--apply" ]]; then
  MODE="apply"
  shift
elif [[ ${1:-} == "--dry-run" ]]; then
  shift
fi

PLAN=${1:-}
if [[ -z "$PLAN" ]]; then
  echo "Usage: $0 [--dry-run|--apply] PLAN.yaml" >&2
  exit 1
fi

read_plan() {
  local section="$1"
  awk -v section="$section" '
    $0 ~ "^"section":" {flag=1; next}
    /^[a-z]/ {flag=0}
    flag && /^  -/ {print $2}
  ' "$PLAN"
}

create_dirs=$(read_plan create)
remove_dirs=$(read_plan remove)

for d in $create_dirs; do
  if [[ $MODE == "apply" ]]; then
    mkdir -p "$d"
    echo "Created $d"
  else
    echo "[DRY-RUN] Would create $d"
  fi
done

for d in $remove_dirs; do
  if [[ $MODE == "apply" ]]; then
    rm -rf "$d"
    echo "Removed $d"
  else
    echo "[DRY-RUN] Would remove $d"
  fi
done
