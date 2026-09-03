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
import hashlib
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


# The three student-repo documents this site publishes. Their SOURCE lives there and
# their RENDER lives here, so check-staleness -- which pairs a source with its output
# inside one repository -- has no pair to compare and cannot see them go stale. That
# is exactly how the quickstart shipped stale on 2026-09-02: its source had moved to
# Canvas submission, the published page still told students to `git push`, and every
# gate was green. sync_to_docs.sh records each source's hash when it publishes; this
# compares the current sources against that record.
# The data-prep scripts live in BOTH repositories: the course repo authors them, the
# student repo is where students actually run them. `ECON8310_Datasets.md` tells
# students to run `python scripts/prep_favorita.py` from their clone, and on
# 2026-09-03 that script existed only here — the instruction pointed at a file they
# did not have. Same shape as the assignment drift, one directory over.
SHARED_SCRIPTS = "scripts/prep_*.py"

PUBLISHED_FROM_STUDENT_REPO = {
    "QUARTO_GUIDE.md": "docs/files/setup-guide.html",
    "AI_POLICY.md": "docs/files/ai-policy.html",
    "STUDENT_QUICKSTART.md": "docs/files/quickstart.html",
}
STAMP = os.path.join(ROOT, ".student-docs-stamp")


def short_hash(path: str) -> str:
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()[:16]


def check_shared_scripts(sr: str) -> list[str]:
    """Every prep script exists in both repos, byte-for-byte."""
    out = []
    here = {os.path.basename(f) for f in glob.glob(os.path.join(ROOT, SHARED_SCRIPTS))}
    there = {os.path.basename(f) for f in glob.glob(os.path.join(sr, SHARED_SCRIPTS))}
    for name in sorted(here - there):
        out.append(f"scripts/{name}: authored here, missing from the student repo — "
                   f"students are told to run it from their clone")
    for name in sorted(there - here):
        out.append(f"scripts/{name}: in the student repo but not authored here")
    for name in sorted(here & there):
        a = open(os.path.join(ROOT, "scripts", name), "rb").read()
        b = open(os.path.join(sr, "scripts", name), "rb").read()
        if a != b:
            out.append(f"scripts/{name}: the two copies differ — "
                       f"cp scripts/{name} <student repo>/scripts/")
    return out


def check_published_docs(sr: str) -> list[str]:
    """Is each published copy built from the source as it stands now?"""
    if not os.path.exists(STAMP):
        return ["no .student-docs-stamp — run ./scripts/sync_to_docs.sh docs"]
    with open(STAMP, encoding="utf-8") as fh:
        recorded = dict(l.split(":", 1) for l in fh.read().split("\n") if ":" in l)
    out = []
    for src, rendered in PUBLISHED_FROM_STUDENT_REPO.items():
        src_path = os.path.join(sr, src)
        if not os.path.exists(src_path):
            out.append(f"{src}: named as a published source but missing from the student repo")
            continue
        if not os.path.exists(os.path.join(ROOT, rendered)):
            out.append(f"{rendered}: not published, though {src} exists")
            continue
        now, then = short_hash(src_path), recorded.get(src, "").strip()
        if not then:
            out.append(f"{src}: not in .student-docs-stamp — re-publish to record it")
        elif now != then:
            out.append(
                f"{src} changed since {rendered} was built ({then} -> {now})\n"
                f"        the published page is STALE — students are reading the old text\n"
                f"        fix: ./scripts/sync_to_docs.sh docs")
    return out


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

    problems += check_shared_scripts(sr)
    problems += check_published_docs(sr)

    if problems:
        print(f"check-assignment-sync: {len(problems)} problem(s)\n")
        for p in problems:
            print(f"  {p}")
        print("\n  fix: cp Homework/HW*.qmd <student repo>/assignments/")
        return 1

    n_scripts = len(glob.glob(os.path.join(ROOT, SHARED_SCRIPTS)))
    print(f"check-assignment-sync: all {checked} assignments and {n_scripts} prep scripts "
          f"identical in both repos; {len(PUBLISHED_FROM_STUDENT_REPO)} published documents "
          f"built from current sources")
    return 0


if __name__ == "__main__":
    sys.exit(main())
