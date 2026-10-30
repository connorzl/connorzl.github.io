#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
source_dir="${HUGO_SOURCE_DIR:-$root/hugo}"
hugo_bin="${HUGO_BIN:-hugo-0.55.6}"

if ! command -v "$hugo_bin" >/dev/null 2>&1; then
  echo "Missing Hugo 0.55.6 extended. See README.md for installation instructions." >&2
  exit 1
fi
if [[ "$("$hugo_bin" version)" != *"v0.55.6-"*"/extended"* ]]; then
  echo "This theme requires Hugo 0.55.6 extended; set HUGO_BIN to that executable." >&2
  exit 1
fi
if [[ ! -f "$source_dir/config/_default/config.toml" || ! -f "$source_dir/themes/academic/theme.toml" ]]; then
  echo "Missing source or theme at $source_dir. See README.md." >&2
  exit 1
fi

export HUGO_RESOURCEDIR="$root/.hugo-resources"
exec "$hugo_bin" --source "$source_dir" --destination "$root/.hugo-build" "$@"
