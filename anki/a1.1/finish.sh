#!/usr/bin/env bash
set -euo pipefail

DECK_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
# Resolve launcher symlinks: relocatable Python installs otherwise write an
# incorrect home into pyvenv.cfg and fail while bootstrapping ensurepip.
DECK_PYTHON="$(python3 -c 'import pathlib, sys; print(pathlib.Path(sys._base_executable).resolve())')"
if [[ -d "$DECK_ROOT/.venv" ]] && ! "$DECK_ROOT/.venv/bin/python" -m pip --version >/dev/null 2>&1; then
  echo "Rebuilding the incomplete Python environment..."
  "$DECK_PYTHON" -m venv --clear "$DECK_ROOT/.venv"
elif [[ ! -d "$DECK_ROOT/.venv" ]]; then
  "$DECK_PYTHON" -m venv "$DECK_ROOT/.venv"
fi
if [[ "${1:-}" == "--setup-only" ]]; then
  "$DECK_ROOT/.venv/bin/python" -m pip --version
  exit 0
fi
"$DECK_ROOT/.venv/bin/python" -m pip install -r "$DECK_ROOT/requirements.txt"
for step in prepare audio build verify; do
  "$DECK_ROOT/.venv/bin/python" "$DECK_ROOT/build.py" "$step"
done
