#!/usr/bin/env python3
"""Find (and optionally remove) redundant slide separators in RevealJS decks.

In a Quarto RevealJS deck both a `---` rule and a heading start a new slide. When a
`---` sits immediately before a level-1 heading, the rule opens a slide that the
section wrapper then immediately closes, and the deck renders a blank slide:

    <section class="slide level2">  </section>

Only level-1 headings are affected. A `---` before a `##` is harmless -- that heading
breaks the slide by itself -- and separators between prose blocks are doing real work.
Both are left alone.

Usage
-----
    python scripts/check_slide_separators.py            # report, exit 1 if any found
    python scripts/check_slide_separators.py --fix      # remove them, then report
    python scripts/check_slide_separators.py --fix Quarto/Lecture01_ETS_Eval.qmd

Exit status is 0 when no redundant separators remain, so this works as a gate.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

# A `---` line, then blank line(s), then a LEVEL-1 heading.
# Captures the heading so it can be kept while the rule is dropped.
#
# Level 1 only, and this is measured rather than assumed: with slide-level 2, a `##`
# already closes and opens a slide cleanly, so a `---` before it costs nothing. A `#`
# opens a *section* wrapper instead, and the preceding rule is left stranded as its own
# empty slide. Lecture 1 carried 20 separators before headings and rendered exactly 4
# blank slides -- one per `#`. Widening this to `#{1,6}` deletes 200+ harmless rules.
REDUNDANT = re.compile(r"^---[ \t]*\n\n+(# )", re.MULTILINE)

DEFAULT_GLOB = "Quarto/Lecture*.qmd"


def find(text: str) -> list[int]:
    """Line numbers (1-based) of redundant `---` rules."""
    return [text.count("\n", 0, m.start()) + 1 for m in REDUNDANT.finditer(text)]


def strip(text: str) -> tuple[str, int]:
    """Drop redundant rules, keeping the heading and one blank line before it."""
    return REDUNDANT.subn(r"\1", text)


def repo_root() -> pathlib.Path:
    here = pathlib.Path(__file__).resolve().parent
    return here.parent


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*", type=pathlib.Path,
                    help=f"files to check (default: {DEFAULT_GLOB} from the repo root)")
    ap.add_argument("--fix", action="store_true",
                    help="rewrite the files, removing redundant separators")
    args = ap.parse_args()

    paths = args.files or sorted(repo_root().glob(DEFAULT_GLOB))
    if not paths:
        print(f"no files matched {DEFAULT_GLOB}", file=sys.stderr)
        return 1

    total = 0
    changed = 0
    for p in paths:
        try:
            text = p.read_text(encoding="utf-8")
        except OSError as exc:
            print(f"  {p}: {exc}", file=sys.stderr)
            return 1

        lines = find(text)
        if not lines:
            continue
        total += len(lines)

        if args.fix:
            new, n = strip(text)
            # newline="\n" keeps LF endings regardless of platform
            with p.open("w", encoding="utf-8", newline="\n") as fh:
                fh.write(new)
            changed += 1
            print(f"  {p.name:<40} removed {n}")
        else:
            shown = ", ".join(str(n) for n in lines[:8])
            more = f" (+{len(lines) - 8} more)" if len(lines) > 8 else ""
            print(f"  {p.name:<40} {len(lines):>3} at lines {shown}{more}")

    if not total:
        print("  no redundant slide separators")
        return 0

    if args.fix:
        print(f"\n  removed {total} redundant separators from {changed} file(s)")
        print("  re-render the decks, then run check_mirror_parity.py")
        return 0

    print(f"\n  {total} redundant separators -- each renders as a blank slide")
    print("  fix with: python scripts/check_slide_separators.py --fix")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
