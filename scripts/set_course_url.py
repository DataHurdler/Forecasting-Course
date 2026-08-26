#!/usr/bin/env python3
"""Change the published course URL everywhere it appears, in one command.

    python scripts/set_course_url.py                       # show current + where it appears
    python scripts/set_course_url.py https://luozijun.com/Forecasting-Course/

The canonical URL lives in scripts/course_url.txt. Student-facing documents keep the real
URL in their source — no placeholder tokens — so the markdown reads correctly if someone
opens it raw or it is distributed as a PDF. This script is what keeps them in sync.

Session logs and quality reports are deliberately NOT rewritten: they are a historical
record of what was true when written.
"""
import pathlib, sys, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONF = ROOT / "scripts" / "course_url.txt"

# Student-facing documents that carry the live URL.
TARGETS = [
    "ECON8310Syllabus2026Fall.md",
    "ECON8310_Datasets.md",
    "ECON8310_Project_Rubric.md",
]

def current() -> str:
    return CONF.read_text(encoding="utf-8").strip()

def occurrences(url: str):
    base = url.rstrip("/")
    found = []
    for rel in TARGETS:
        p = ROOT / rel
        if not p.exists():
            found.append((rel, None)); continue
        found.append((rel, p.read_text(encoding="utf-8").count(base)))
    return found

def main():
    old = current()
    if len(sys.argv) == 1:
        print(f"current course URL: {old}\n")
        for rel, n in occurrences(old):
            print(f"  {rel:<34} {'(missing)' if n is None else f'{n} occurrence(s)'}")
        print("\nto change:  python scripts/set_course_url.py <new-url>")
        return 0

    new = sys.argv[1].strip()
    if not re.match(r"^https?://", new):
        print(f"error: '{new}' does not look like a URL"); return 1
    if not new.endswith("/"):
        new += "/"
    old_base, new_base = old.rstrip("/"), new.rstrip("/")
    if old_base == new_base:
        print("no change: that is already the current URL"); return 0

    total = 0
    for rel in TARGETS:
        p = ROOT / rel
        if not p.exists():
            print(f"  SKIP {rel} (missing)"); continue
        raw = p.read_bytes()
        crlf = raw.count(b"\r\n")
        text = raw.decode("utf-8")
        n = text.count(old_base)
        if n:
            text = text.replace(old_base, new_base)
            out = text.encode("utf-8")
            # preserve the file's original line-ending convention
            if crlf and out.count(b"\r\n") != crlf:
                out = out.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
            p.write_bytes(out)
            total += n
        print(f"  {rel:<34} {n} replaced")

    CONF.write_text(new + "\n", encoding="utf-8")
    print(f"\n{total} occurrence(s) updated; scripts/course_url.txt now reads {new}")
    print("next: ./scripts/sync_to_docs.sh docs   (re-render the three pages)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
