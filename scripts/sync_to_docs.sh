#!/bin/bash
# sync_to_docs.sh — render course materials and publish them to docs/ for GitHub Pages.
#
# Usage:
#   ./scripts/sync_to_docs.sh                 # everything (slides, labs, homework, documents, books)
#   ./scripts/sync_to_docs.sh slides          # RevealJS mirrors only (no PDFs -- see below)
#   ./scripts/sync_to_docs.sh labs            # labs only  (slow: several render for minutes)
#   ./scripts/sync_to_docs.sh homework        # homework only
#   ./scripts/sync_to_docs.sh docs            # about / datasets / rubric / troubleshooting only
#   ./scripts/sync_to_docs.sh books           # the book and the workbook only
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
  # Record which SOURCE each of these three renders came from. Their sources live in
  # the student repository and their renders live here, so check-staleness -- which
  # compares a source to its output inside one repo -- has no pair to compare and is
  # structurally blind to them. That is how the quickstart shipped stale on
  # 2026-09-02, still telling students to `git push` a day after the source said
  # Canvas. The stamp is written HERE, by the publish step, so it cannot be forgotten
  # the way a separate stamping command can.
  {
    for f in QUARTO_GUIDE.md AI_POLICY.md STUDENT_QUICKSTART.md; do
      printf '%s:%s\n' "$f" "$(shasum -a 256 "$SR/$f" | cut -c1-16)"
    done
  } > "$REPO_ROOT/.student-docs-stamp"
  echo "  OK   setup-guide, ai-policy, quickstart"
}

sync_documents() {
  echo "=== Syllabus, datasets, rubric ==="
  [ -n "$PANDOC" ] || { echo "  pandoc not found — skipping"; return; }
  cd "$REPO_ROOT"
  # The SYLLABUS is deliberately not published. It is UNO- and term-specific — room,
  # meeting time, grade scale, integrity policy, the academic calendar — and by the
  # instructional designer's model it belongs on Canvas, which carries the copy every
  # enrolled student reads. What a public visitor needs from it lives in About.
  "$PANDOC" ECON8310_About.md -s --toc --toc-depth=2 -c docstyle.css \
     --metadata title="ECON 8310 — About This Course" -o "$DOCS/files/about.html"
  "$PANDOC" ECON8310_Datasets.md -s --toc --toc-depth=2 -c docstyle.css \
     --metadata title="ECON 8310 — Course Datasets" -o "$DOCS/files/datasets.html"
  "$PANDOC" ECON8310_Project_Rubric.md -s --toc --toc-depth=2 -c docstyle.css \
     --metadata title="ECON 8310 — Final Project Rubric" -o "$DOCS/files/project-rubric.html"
  # ECON8310_Troubleshooting.md, NOT TROUBLESHOOTING.md. The latter is the workflow
  # template's own troubleshooting -- `claude: command not found`, xelatex, pdf2svg,
  # the peer-review pipeline -- and three gates depend on it, so it stays. It was
  # published to students until 2026-09-03, which meant a student hitting a kernel
  # error read instructions for installing Claude Code.
  "$PANDOC" ECON8310_Troubleshooting.md -s --toc --toc-depth=2 -c docstyle.css \
     --metadata title="ECON 8310 — Troubleshooting" -o "$DOCS/files/troubleshooting.html"
  echo "  OK   about, datasets, project-rubric, troubleshooting"
  sync_student_docs
}

# The book and the workbook are ASSEMBLED from the decks, labs, assignments and
# narration, so an edit to any of those leaves them stale until they are rebuilt.
# They were absent from `all` until 2026-09-01, and it showed: a repo-wide spelling
# pass corrected 50 source files, `all` republished every deck, lab and assignment,
# and the book still carried the old prose because nothing here rebuilt it.
sync_books() {
  echo "=== Book and workbook ==="
  cd "$REPO_ROOT"
  python3 scripts/build_book.py     >/dev/null || { echo "  FAIL build_book.py";     return 1; }
  python3 scripts/build_workbook.py >/dev/null || { echo "  FAIL build_workbook.py"; return 1; }
  (cd book     && quarto render >/dev/null 2>&1) && echo "  OK   book"     || echo "  FAIL book render"
  (cd workbook && quarto render >/dev/null 2>&1) && echo "  OK   workbook" || echo "  FAIL workbook render"
}

sync_figures() {
  if command -v rsync >/dev/null; then rsync -a --delete "$REPO_ROOT/Figures/" "$DOCS/Figures/"
  else rm -rf "$DOCS/Figures"; cp -r "$REPO_ROOT/Figures" "$DOCS/Figures"; fi
}

case "$TARGET" in
  all)      sync_slides; sync_labs; sync_homework; sync_documents; sync_books; sync_figures ;;
  books)    sync_books ;;
  slides)   sync_slides; sync_figures ;;
  labs)     sync_labs ;;
  homework) sync_homework ;;
  docs)     sync_documents ;;
  *)        sync_one "$TARGET" ;;
esac

echo ""
# Regenerate the landing page. It used to be hand-maintained and restamped in place,
# which meant a newly published artifact appeared under docs/ with nothing linking to
# it — invisible to students, and invisible to every gate. It is now built from
# scripts/site.yml, and scripts/check-site-index.py fails the backtest if a published
# page is not reachable from it.
python3 "$REPO_ROOT/scripts/build_index.py"
python3 "$REPO_ROOT/scripts/check-site-index.py" || {
  echo ""
  echo "  ^ the landing page does not cover everything just published."
  echo "    Add the new material to scripts/site.yml and re-run."
  exit 1
}

echo "=== Done. Published to $DOCS ==="
