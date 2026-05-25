#!/usr/bin/env bash
# commit.sh — build the CV in pages/cv, then commit and push from the repo root.
# Run from the repo root: ./commit.sh
# If make fails (e.g. "bibliography not found"), the pCloud drive isn't mounted —
# start the pCloud app and retry. Nothing is committed on a failed build.

set -euo pipefail

# Resolve repo root as the directory this script lives in, so it works
# regardless of where you call it from.
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

# 1. Descend into pages/cv and build. set -e means a make failure aborts the script.
echo "Building CV..."
( cd pages/cv && make all )

# 2. Back at the root, stage everything and commit only if something changed.
cd "$ROOT"
git add -A

if git diff --staged --quiet; then
  echo "Nothing changed — no commit made."
  exit 0
fi

git commit -m "Update $(date +%Y-%m-%d)"
git push

echo "Done."