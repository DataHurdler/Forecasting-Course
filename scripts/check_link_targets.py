#!/usr/bin/env python3
"""Ensure content links on the course landing page open in a new tab.

`docs/index.html` is hand-maintained, so links added later drift back to opening
in the same tab. That is mildly annoying for a document and genuinely annoying for
a RevealJS deck: the site is replaced by the deck, and getting back means hunting
for the Back button.

Links to slides, labs, homework, supporting documents, and external sites get
`target="_blank" rel="noopener"`. In-page anchors (`#section`) and any link that
already declares a target are left alone.

`rel="noopener"` is not optional: without it the opened page can reach back
through `window.opener`, and older browsers leak referrer information.

Usage
-----
    python scripts/check_link_targets.py            # report, exit 1 if any missing
    python scripts/check_link_targets.py --fix      # add the attributes
    python scripts/check_link_targets.py --fix docs/index.html

Exit status is 0 when every content link opens in a new tab, so this works as a gate.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

# Link prefixes whose targets are content the reader opens *alongside* the site.
CONTENT_PREFIXES = ("slides/", "labs/", "homework/", "files/", "http://", "https://")

# <a ...href="X"...>  -- capture the whole tag and the href value
ANCHOR = re.compile(r"<a\b([^>]*?)href=\"([^\"]+)\"([^>]*?)>", re.IGNORECASE)

DEFAULT_FILES = ("docs/index.html",)


def wants_new_tab(href: str) -> bool:
    return href.startswith(CONTENT_PREFIXES)


def scan(text: str) -> list[str]:
    """hrefs that should open in a new tab but do not yet."""
    missing = []
    for m in ANCHOR.finditer(text):
        pre, href, post = m.group(1), m.group(2), m.group(3)
        if not wants_new_tab(href):
            continue
        if "target=" in (pre + post).lower():
            continue
        missing.append(href)
    return missing


def apply(text: str) -> tuple[str, int]:
    count = 0

    def repl(m: re.Match) -> str:
        nonlocal count
        pre, href, post = m.group(1), m.group(2), m.group(3)
        if not wants_new_tab(href) or "target=" in (pre + post).lower():
            return m.group(0)
        count += 1
        return f'<a{pre}href="{href}"{post} target="_blank" rel="noopener">'

    return ANCHOR.sub(repl, text), count


def repo_root() -> pathlib.Path:
    return pathlib.Path(__file__).resolve().parent.parent


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*", type=pathlib.Path,
                    help=f"files to check (default: {', '.join(DEFAULT_FILES)})")
    ap.add_argument("--fix", action="store_true", help="add the missing attributes")
    args = ap.parse_args()

    root = repo_root()
    paths = args.files or [root / f for f in DEFAULT_FILES]

    total = 0
    for p in paths:
        if not p.exists():
            print(f"  {p}: not found", file=sys.stderr)
            return 1
        text = p.read_text(encoding="utf-8")
        missing = scan(text)
        if not missing:
            continue
        total += len(missing)

        if args.fix:
            new, n = apply(text)
            with p.open("w", encoding="utf-8", newline="\n") as fh:
                fh.write(new)
            print(f"  {p.name:<24} added target to {n} link(s)")
        else:
            kinds: dict[str, int] = {}
            for h in missing:
                key = h.split("/")[0] + "/" if "/" in h and not h.startswith("http") else "external"
                kinds[key] = kinds.get(key, 0) + 1
            summary = ", ".join(f"{v} {k}" for k, v in sorted(kinds.items()))
            print(f"  {p.name:<24} {len(missing)} link(s) open in the same tab: {summary}")

    if not total:
        print("  every content link opens in a new tab")
        return 0

    if args.fix:
        print(f"\n  updated {total} link(s)")
        return 0

    print(f"\n  {total} content link(s) would replace the site in the same tab")
    print("  fix with: python scripts/check_link_targets.py --fix")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
