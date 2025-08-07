# Ops Scripts

This directory contains operational scripts for AingZ Platform.

## baseline_codex_v4.py

Generates a baseline report for `platform_v_4_0/main`.

### Usage

```bash
python ops/scripts/baseline_codex_v4.py [--root PATH] [--format json|yaml] [--log PATH]
```

### Parameters

- `--root`: Repository root path. Defaults to project root.
- `--format`: Output format (`json` or `yaml`). Defaults to `json`.
- `--log`: Destination log file. Defaults to `ops/log/baseline_codex_v4.log`.

The script prints the baseline to stdout and writes the same content to the log file.
