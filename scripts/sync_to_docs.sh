#!/bin/bash
# sync_to_docs.sh — render course materials and publish them to docs/ for GitHub Pages.
#
# Usage:
#   ./scripts/sync_to_docs.sh                 # everything (slides, labs, homework, documents)
#   ./scripts/sync_to_docs.sh slides          # RevealJS mirrors only (no PDFs -- see below)
#   ./scripts/sync_to_docs.sh labs            # labs only  (slow: several render for minutes)
#   ./scripts/sync_to_docs.sh homework        # homework only
#   ./scripts/sync_to_docs.sh docs            # syllabus / datasets / rubric only
#   ./scripts/sync_to_docs.sh Lecture07       # one lecture's mirror
#
# Everything is rendered with the project venv so package versions match the labs.

set -e
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DOCS="$REPO_ROOT/docs"
export PATH="$REPO_ROOT/.venv/bin:$PATH"
export QUARTO_PYTHON="$REPO_ROOT/.venv/bin/python"
PANDOC=/Applications/quarto/bin/tools/aarch64/pandoc
[ -x "$PANDOC" ] || PANDOC=$(command -v pandoc || echo "")

TARGET="${1:-all}"
mkdir -p "$DOCS/slides" "$DOCS/labs" "$DOCS/homework" "$DOCS/files"

sync_slides() {
  echo "=== Slides ==="
  cd "$REPO_ROOT/Quarto"
  for qmd in Lecture*.qmd; do
    [ -f "$qmd" ] || continue
    echo "  rendering $qmd"
    quarto render "$qmd" >/dev/null 2>&1 || { echo "    FAILED: $qmd"; continue; }
    cp "${qmd%.qmd}.html" "$DOCS/slides/"
  done
  # Beamer PDFs are deliberately NOT published: untagged LaTeX output is the format
  # screen readers handle worst. The RevealJS HTML is the accessible version.
}

sync_one() {   # one lecture mirror by prefix
  cd "$REPO_ROOT/Quarto"
  local m; m=$(ls ${1}*.qmd 2>/dev/null | head -1)
  [ -n "$m" ] || { echo "No Quarto file matching '${1}'"; exit 1; }
  quarto render "$m"
  cp "${m%.qmd}.html" "$DOCS/slides/"
}

sync_labs() {
  echo "=== Labs (several take minutes — they fit real models) ==="
  cd "$REPO_ROOT"
  for qmd in Labs/Lecture*_lab.qmd; do
    b=$(basename "$qmd" .qmd); s=$(date +%s)
    if quarto render "$qmd" --to html >/dev/null 2>&1; then
      cp "Labs/$b.html" "$DOCS/labs/"; echo "  OK   $b ($(( $(date +%s) - s ))s)"
    else
      echo "  FAIL $b"
    fi
  done
}

sync_homework() {
  echo "=== Homework ==="
  cd "$REPO_ROOT"
  for qmd in Homework/HW*.qmd; do
    b=$(basename "$qmd" .qmd)
    if quarto render "$qmd" --to html >/dev/null 2>&1; then
      cp "Homework/$b.html" "$DOCS/homework/"; echo "  OK   $b"
    else
      echo "  FAIL $b"
    fi
  done
}

# The student repository holds three documents that are course material rather than repo
# mechanics. They are rendered from there so there is only ever one copy to keep correct.
# Override the location with STUDENT_REPO=/path ./scripts/sync_to_docs.sh docs
find_student_repo() {
  for c in "$STUDENT_REPO" "$REPO_ROOT/../forecasting-env" "$REPO_ROOT/../Forecasting-Env"; do
    [ -n "$c" ] && [ -f "$c/QUARTO_GUIDE.md" ] && { echo "$c"; return; }
  done
}

sync_student_docs() {
  local SR; SR="$(find_student_repo)"
  if [ -z "$SR" ]; then
    echo "  student repo not found — skipping the setup guide, AI policy and quickstart."
    echo "  (set STUDENT_REPO=/path/to/forecasting-env to include them)"
    return
  fi
  echo "  student repo: $SR"
  [ -n "$PANDOC" ] || return
  "$PANDOC" "$SR/QUARTO_GUIDE.md" -s --toc --toc-depth=2 -c docstyle.css \
     --metadata title="ECON 8310 — Setup and Quarto Guide" -o "$DOCS/files/setup-guide.html"
  "$PANDOC" "$SR/AI_POLICY.md" -s --toc --toc-depth=2 -c docstyle.css \
     --metadata title="ECON 8310 — Using AI on Homework" -o "$DOCS/files/ai-policy.html"
  "$PANDOC" "$SR/STUDENT_QUICKSTART.md" -s --toc --toc-depth=2 -c docstyle.css \
     --metadata title="ECON 8310 — Homework Quickstart" -o "$DOCS/files/quickstart.html"
  echo "  OK   setup-guide, ai-policy, quickstart"
}

sync_documents() {
  echo "=== Syllabus, datasets, rubric ==="
  [ -n "$PANDOC" ] || { echo "  pandoc not found — skipping"; return; }
  cd "$REPO_ROOT"
  "$PANDOC" ECON8310Syllabus2026Fall.md -s --toc --toc-depth=2 -c docstyle.css \
     --metadata title="ECON 8310 Syllabus — Fall 2026" -o "$DOCS/files/syllabus.html"
  "$PANDOC" ECON8310_Datasets.md -s --toc --toc-depth=2 -c docstyle.css \
     --metadata title="ECON 8310 — Course Datasets" -o "$DOCS/files/datasets.html"
  "$PANDOC" ECON8310_Project_Rubric.md -s --toc --toc-depth=2 -c docstyle.css \
     --metadata title="ECON 8310 — Final Project Rubric" -o "$DOCS/files/project-rubric.html"
  echo "  OK   syllabus, datasets, project-rubric"
  sync_student_docs
}

sync_figures() {
  if command -v rsync >/dev/null; then rsync -a --delete "$REPO_ROOT/Figures/" "$DOCS/Figures/"
  else rm -rf "$DOCS/Figures"; cp -r "$REPO_ROOT/Figures" "$DOCS/Figures"; fi
}

case "$TARGET" in
  all)      sync_slides; sync_labs; sync_homework; sync_documents; sync_figures ;;
  slides)   sync_slides; sync_figures ;;
  labs)     sync_labs ;;
  homework) sync_homework ;;
  docs)     sync_documents ;;
  *)        sync_one "$TARGET" ;;
esac

echo ""
# Restamp the landing page's "Last updated". A hand-maintained date is a claim
# that rots; this makes it a fact about the last publish.
if [ -f "$DOCS/index.html" ]; then
  STAMP="$(date '+%B %-d, %Y')"
  python3 - "$DOCS/index.html" "$STAMP" <<'PY'
import re, sys
p, stamp = sys.argv[1], sys.argv[2]
s = open(p, encoding="utf-8").read()
# \g<1> not \1: a stamp beginning with a digit turns \1 into group 11.
s2 = re.sub(r'(<span id="updated">Last updated: )[^<]*(</span>)', lambda m: m.group(1) + stamp + m.group(2), s)
if s2 != s:
    open(p, "w", encoding="utf-8").write(s2)
PY
  echo "  landing page stamped: $STAMP"
fi

echo "=== Done. Published to $DOCS ==="
