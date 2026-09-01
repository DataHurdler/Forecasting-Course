#!/usr/bin/env python3
"""check-site-index.py — the landing page is complete, current, and has no dead links.

Three questions, in the order a student meets them:

  1. STALE      — is docs/index.html what scripts/site.yml + the template produce?
                  (i.e. did someone hand-edit the generated page, or edit the sources
                  and forget to rebuild?)
  2. DEAD       — does every local href on the page resolve to a file under docs/?
  3. ORPHANED   — is every page published under docs/ reachable from the landing page?

(3) is the one that has no other gate. check-links.py verifies that what we link exists;
nothing verified that what exists is linked. That is the failure this file was written for:
a rendered lab, a new deck or a whole new book can sit in docs/, be served by GitHub Pages,
and be invisible to every student because nothing points at it. Both drifts on 2026-09-01
were of exactly that shape.

An artifact that genuinely should not be linked goes in site.yml's `unlinked:` list with a
reason. That makes the omission a decision on the record instead of an oversight.

    python3 scripts/check-site-index.py

Exit 0 = clean. Runs inside ./scripts/backtest.sh, so also on every commit.
"""
from __future__ import annotations

import pathlib
import re
import subprocess
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
INDEX = DOCS / "index.html"
MANIFEST = ROOT / "scripts" / "site.yml"

# Directories whose contents are a page's own assets, not pages in their own right.
ASSET_DIR = re.compile(r"(^|/)(Figures|site_libs|search\.json|.*_files)(/|$)")

# Sub-sites: the landing page links their entry point, and the entry point is
# responsible for its own chapters. Requiring a link to every chapter would put 40
# rows on the landing page and defeat the point of having a book.
SUBSITE_ROOTS = ("book/", "workbook/")


def published_pages() -> list[str]:
    """Everything under docs/ a student could be sent to, as docs-relative paths."""
    out = []
    for p in sorted(DOCS.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(DOCS).as_posix()
        if rel == "index.html" or ASSET_DIR.search(rel):
            continue
        if p.suffix.lower() not in {".html", ".css", ".pdf"}:
            continue
        if rel.startswith(SUBSITE_ROOTS) and not rel.endswith("/index.html"):
            continue  # a sub-site chapter; its own index covers it
        out.append(rel)
    return out


def page_hrefs(html: str) -> set[str]:
    hrefs = set()
    for h in re.findall(r'href="([^"]+)"', html):
        if h.startswith(("http://", "https://", "mailto:", "#")):
            continue
        hrefs.add(h.split("#")[0].split("?")[0])
    return hrefs


def main() -> int:
    problems: list[str] = []

    # ---- 1. stale ------------------------------------------------------------
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "build_index.py"), "--check"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        problems.append("docs/index.html is out of date with scripts/site.yml + the template")
        print(r.stdout.rstrip())

    if not INDEX.exists():
        print("check-site-index: docs/index.html does not exist")
        return 1

    html = INDEX.read_text(encoding="utf-8")
    hrefs = page_hrefs(html)

    # ---- 2. dead links -------------------------------------------------------
    dead = sorted(h for h in hrefs if not (DOCS / h).exists())
    for h in dead:
        problems.append(f"dead link on the landing page: {h}")

    # ---- 3. orphaned artifacts ----------------------------------------------
    site = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    declared = {u["path"]: u["why"] for u in (site.get("unlinked") or [])}

    orphans = [p for p in published_pages() if p not in hrefs and p not in declared]
    for p in orphans:
        problems.append(
            f"published but unreachable: docs/{p} — add it to scripts/site.yml, "
            f"or to its `unlinked:` list with a reason")

    # A stale `unlinked:` entry is its own small rot: it records a decision about a
    # file that is no longer there.
    for p in sorted(declared):
        if not (DOCS / p).exists():
            problems.append(f"site.yml lists `unlinked: {p}`, but no such file is published")

    # ---- report --------------------------------------------------------------
    if problems:
        print(f"check-site-index: {len(problems)} problem(s)\n")
        for p in problems:
            print(f"  {p}")
        return 1

    linked = len([h for h in hrefs if not h.startswith("files/docstyle")])
    print(f"check-site-index: landing page current; {linked} local links all resolve; "
          f"all {len(published_pages())} published pages are reachable "
          f"({len(declared)} deliberately unlinked)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
