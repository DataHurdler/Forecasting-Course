#!/usr/bin/env python3
"""check-assignment-sync.py — the two copies of every assignment agree.

Assignments are authored in `Homework/` here and **copied** to the student repo's
`assignments/`. Students read the copy. Nothing enforced that the two matched, and
on 2026-09-01 all eleven had drifted within a single day: the term stamp was
removed from every subtitle here, and the American-English pass corrected four
more, while the student repo kept the old text. Every gate in this repo runs
inside this repo, so cross-repo drift is invisible to all of them by construction.

That is the failure this closes. It is the same shape as the stale quickstart
reference found the same day: a fact stated in two places, checked in one.

    python3 scripts/check-assignment-sync.py

The student repo is located the way sync_to_docs.sh locates it — $STUDENT_REPO,
then a sibling `forecasting-env` or `Forecasting-Env`. When it is genuinely absent
(a fresh clone of this repo alone) the check reports that and passes, because a
missing peer is not drift. When it is present, every assignment must match
byte-for-byte.
"""
from __future__ import annotations

import glob
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def student_repo() -> str | None:
    for c in (os.environ.get("STUDENT_REPO"),
              os.path.join(ROOT, "..", "forecasting-env"),
              os.path.join(ROOT, "..", "Forecasting-Env")):
        if c and os.path.isfile(os.path.join(c, "QUARTO_GUIDE.md")):
            return os.path.abspath(c)
    return None


def main() -> int:
    sr = student_repo()
    if sr is None:
        print("check-assignment-sync: student repo not found — nothing to compare.")
        print("  (set STUDENT_REPO=/path/to/forecasting-env to enable this check)")
        return 0

    here = sorted(glob.glob(os.path.join(ROOT, "Homework", "HW*.qmd")))
    problems, checked = [], 0

    for src in here:
        name = os.path.basename(src)
        dst = os.path.join(sr, "assignments", name)
        if not os.path.exists(dst):
            problems.append(f"{name}: authored here, missing from the student repo's assignments/")
            continue
        checked += 1
        a = open(src, encoding="utf-8").read()
        b = open(dst, encoding="utf-8").read()
        if a != b:
            # Name the first differing line: "they differ" is not actionable.
            al, bl = a.splitlines(), b.splitlines()
            i = next((n for n in range(min(len(al), len(bl))) if al[n] != bl[n]),
                     min(len(al), len(bl)))
            problems.append(
                f"{name}: copies differ, first at line {i + 1}\n"
                f"        here:    {al[i][:96] if i < len(al) else '<end of file>'}\n"
                f"        student: {bl[i][:96] if i < len(bl) else '<end of file>'}")

    # The reverse direction: an assignment the students have and we do not.
    for dst in sorted(glob.glob(os.path.join(sr, "assignments", "HW*.qmd"))):
        name = os.path.basename(dst)
        if not os.path.exists(os.path.join(ROOT, "Homework", name)):
            problems.append(f"{name}: in the student repo but not authored in Homework/")

    if problems:
        print(f"check-assignment-sync: {len(problems)} problem(s)\n")
        for p in problems:
            print(f"  {p}")
        print("\n  fix: cp Homework/HW*.qmd <student repo>/assignments/")
        return 1

    print(f"check-assignment-sync: all {checked} assignments identical in both repos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
