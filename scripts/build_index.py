#!/usr/bin/env python3
"""build_index.py — generate docs/index.html from site.yml + a prose template.

The landing page was the last hand-maintained student surface in the repository.
Every other page under docs/ is rendered from a source file, so it cannot silently
disagree with the material; the landing page was typed by hand, and on 2026-09-01 it
drifted twice in one day (a book link, then a workbook link) with no gate noticing.

Now the schedule, the three tables and the "last updated" stamp come from
scripts/site.yml, and everything else — CSS, prose, callouts — from
scripts/templates/index.html.in. Run this after any publish:

    python3 scripts/build_index.py            # rebuild, stamped today
    python3 scripts/build_index.py --check    # exit 1 if the published page is stale

scripts/sync_to_docs.sh calls it at the end of every publish, and
scripts/check-site-index.py runs the --check plus the two link audits in the backtest.
"""
from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "scripts" / "site.yml"
TEMPLATE = ROOT / "scripts" / "templates" / "index.html.in"
OUT = ROOT / "docs" / "index.html"

# Every link on this page opens in a new tab: a student following a deck link and then
# hitting Back expected the schedule, and RevealJS ate the gesture (fixed in beed63a7).
TAB = ' target="_blank" rel="noopener"'


def a(href: str, text: str, extra: str = "") -> str:
    return f'<a href="{href}"{TAB}{extra}>{text}</a>'


def render_week(w: dict) -> str:
    head = [f'<span class="wnum">{w["label"]}</span>']
    if w.get("date"):
        head.append(f'<span class="wdate">{w["date"]}</span>')
    for d in w.get("due", []):
        head.append(f'<span class="due">{a(d["href"], d["text"])}</span>')

    out = ['<div class="week">', '  <div class="whead">' + "".join(head) + "</div>"]
    if w.get("title"):
        out.append(f'  <span class="wtitle">{w["title"]}</span>')
    if w.get("reading"):
        out.append(f'  <div class="wread"><strong>Reading:</strong> {w["reading"]}</div>')
    if w.get("links"):
        # Joined across newlines, not concatenated: .wlinks is not a flex row, so the
        # inter-element whitespace is the gap the separator sits in.
        links = '\n    <span class="sep">&middot;</span>'.join(
            a(l["href"], l["text"]) for l in w["links"])
        out += ['  <div class="wlinks">', "    " + links, "  </div>"]
    if w.get("assignment"):
        s = w["assignment"]
        out.append('  <div class="wassign">' + a(s["href"], s["text"])
                   + f'<span class="dueon"> &mdash; {s["dueon"]}</span></div>')
    for n in w.get("notes", []):
        out.append('  <div class="wread" style="margin-top:.5em;margin-bottom:0">'
                   + n + "</div>")
    out.append("</div>")
    return "\n".join(out)


def render_documents(rows: list[dict]) -> str:
    body = "\n".join(
        f'  <tr><td>{a(r["href"], r["text"])}</td>\n      <td>{r["covers"]}</td></tr>'
        for r in rows)
    return "<table>\n  <tr><th>Document</th><th>What it covers</th></tr>\n" + body + "\n</table>"


def render_textbooks(rows: list[dict]) -> str:
    body = "\n".join(
        f'  <tr>\n    <td>{r["book"]}</td>\n    <td>{r["used_for"]}</td>\n  </tr>'
        for r in rows)
    return "<table>\n  <tr><th>Book</th><th>Used for</th></tr>\n" + body + "\n</table>"


def render_assignments(rows: list[dict]) -> str:
    body = "\n".join(
        f'  <tr>\n    <td>{a(r["href"], r["text"])}</td>\n'
        f'    <td>{r["covers"]}</td>\n'
        f'    <td>{r["due"]}</td><td>{r["prompts"]}</td>\n  </tr>'
        for r in rows)
    return ("<table>\n  <tr><th>Assignment</th><th>Covers</th><th>Due</th><th>Prompts</th></tr>\n"
            + body + "\n</table>")


def build(stamp: str | None = None) -> str:
    site = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    page = TEMPLATE.read_text(encoding="utf-8")
    page = page.replace("{{DOCUMENTS_TABLE}}", render_documents(site["documents"]))
    page = page.replace("{{TEXTBOOKS_TABLE}}", render_textbooks(site["textbooks"]))
    page = page.replace("{{ASSIGNMENTS_TABLE}}", render_assignments(site["assignments"]))
    page = page.replace("{{SCHEDULE}}",
                        "\n\n".join(render_week(w) for w in site["weeks"]))
    # %-d is a GNU/BSD extension; both platforms this repo runs on have it.
    page = page.replace("{{UPDATED}}",
                        stamp or dt.date.today().strftime("%B %-d, %Y"))
    return page


def published_stamp() -> str | None:
    """The stamp on the page as published, so --check does not fail on the date alone."""
    if not OUT.exists():
        return None
    import re
    m = re.search(r'<span id="updated">Last updated: ([^<]*)</span>', OUT.read_text())
    return m.group(1) if m else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if docs/index.html differs from what the sources produce")
    args = ap.parse_args()

    if args.check:
        # Compare against the published page's OWN stamp. A rebuild on a later day
        # would otherwise report drift for the date alone, which is not drift — the
        # stamp is a fact about the last publish, and only a publish should move it.
        want = build(stamp=published_stamp())
        have = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if want == have:
            print("build_index: docs/index.html matches site.yml + template")
            return 0
        print("build_index: docs/index.html is STALE — it was hand-edited, or "
              "site.yml/the template changed without a rebuild.")
        print("  fix: python3 scripts/build_index.py")
        import difflib
        diff = list(difflib.unified_diff(have.splitlines(), want.splitlines(),
                                         "published", "generated", lineterm="", n=1))
        for line in diff[:40]:
            print("  " + line)
        if len(diff) > 40:
            print(f"  … {len(diff) - 40} more diff lines")
        return 1

    OUT.write_text(build(), encoding="utf-8")
    site = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    print(f"build_index: wrote {OUT.relative_to(ROOT)} — {len(site['weeks'])} weeks, "
          f"{len(site['assignments'])} assignments, {len(site['documents'])} documents")
    return 0


if __name__ == "__main__":
    sys.exit(main())
