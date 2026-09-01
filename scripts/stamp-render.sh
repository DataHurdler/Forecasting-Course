#!/usr/bin/env bash
# Record which source produced the current rendered artifacts — and what those
# artifacts were, byte-for-byte, at stamp time.
#
# git does not preserve mtimes, so currency cannot be answered by timestamps.
# And a source-only stamp is not enough either (Codex, PR #140 round 2): if you
# render guide/ but forget to sync docs/, or hand-edit an HTML file, a stamp
# that records only the source hash still matches. So each line binds an output
# path to BOTH the source fingerprint and that output's own fingerprint.
#
# Run after: quarto render + cp guide/workflow-guide.html docs/workflow-guide.html
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"      # resolved BEFORE any cd
SRC="$ROOT/guide/workflow-guide.qmd"
G="$ROOT/guide/workflow-guide.html"
D="$ROOT/docs/workflow-guide.html"
for f in "$SRC" "$G"; do
    [ -f "$f" ] || { echo "stamp-render: missing $f" >&2; exit 2; }
done
# The docs/ copy is OPTIONAL: the workflow guide was unpublished from the course
# site in aea188b6, so on this repo there is nothing at docs/workflow-guide.html
# to stamp. Requiring it made the script unrunnable — which surfaced on
# 2026-09-01 as a staleness failure with no way to clear it. check-staleness
# skips a pair whose output is absent, so an unstamped absent file is not a gap.
# Where the copy DOES exist the old invariant is unchanged: docs/ is a copy of
# guide/, and a divergent pair is refused rather than stamped.
if [ -f "$D" ] && ! cmp -s "$G" "$D"; then
    echo "stamp-render: REFUSING — guide/ and docs/ HTML differ." >&2
    echo "  sync first:  cp guide/workflow-guide.html docs/workflow-guide.html" >&2
    exit 1
fi
fp() { local h; h="$(shasum -a 256 "$1" 2>/dev/null | cut -c1-16)"; 
       [ -n "$h" ] || { echo "stamp-render: fingerprint failed for $1 (shasum missing?)" >&2; exit 2; };
       printf '%s' "$h"; }
SH="$(fp "$SRC")" || exit 2
GH="$(fp "$G")"   || exit 2
{
  echo "guide/workflow-guide.html:$SH:$GH"
  if [ -f "$D" ]; then
    DH="$(fp "$D")" || exit 2
    echo "docs/workflow-guide.html:$SH:$DH"
  fi
} > "$ROOT/.render-stamp"
if [ -f "$D" ]; then
  echo "stamp-render: source=$SH output=$GH (guide/docs identical, both stamped)"
else
  echo "stamp-render: source=$SH output=$GH (guide/ stamped; docs/ copy not published here)"
fi
