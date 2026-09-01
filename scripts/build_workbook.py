#!/usr/bin/env python3
"""Assemble the workbook: the labs and the assignments, as students meet them.

    python scripts/build_workbook.py

Separate from the book on purpose. The book is read; the workbook is *worked*,
open beside an editor. They also have different build physics — the labs execute,
and Lab 8 alone takes eight minutes — so folding them into the book would make
every rebuild of the prose cost forty-five minutes and require torch, pymc and the
prepared data. Here the code is shown, not run (`eval: false`); the executable
originals stay at docs/labs/.

Chapters are generated. Edit the lab, the assignment or the narration — never a
chapter. Solution keys live in a private repository and never enter this build.
"""
import re, sys, pathlib, difflib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT  = ROOT / "workbook" / "chapters"
sys.path.insert(0, str(ROOT / "scripts"))
from importlib import import_module
_bb = import_module("build_book")
clean_narration, merge_beats, norm_title = _bb.clean_narration, _bb.merge_beats, _bb.norm_title

# Instructor-facing scaffolding in a recording script. None of it belongs to a student.
_DROP_SECTIONS = re.compile(
    r'^#{1,3}\s+(how to use this|.*things to know before recording|'
    r'in-room language.*|.*correction.*|nothing needed correcting.*|'
    r'a defect this script found.*|this lab was restructured.*|'
    r'one number to settle.*|numbers carried in.*|one thing to fix.*)', re.I)

def strip_instructor(md: str) -> str:
    out, skip = [], False
    for block in re.split(r'(?m)^(?=#)', md):
        head = block.split("\n", 1)[0]
        if _DROP_SECTIONS.match(head):
            skip = True; continue
        if head.startswith("# "):
            skip = False
        if not skip:
            out.append(block)
    return "".join(out)

def lab_steps(md: str):
    """[(title, body)] for '# Step n — Title', plus the lead-in under 'What we are doing'."""
    parts, cur = [], None
    for line in md.split("\n"):
        m = re.match(r'^#\s+(.+?)\s*$', line)
        if m:
            if cur: parts.append(cur)
            cur = [m.group(1).strip(), []]
        elif cur:
            cur[1].append(line)
    if cur: parts.append(cur)
    return [(t, "\n".join(b).strip()) for t, b in parts]

def narration_steps(path: pathlib.Path):
    if not path.exists(): return {}
    md = strip_instructor(path.read_text(encoding="utf-8"))
    out = {}
    for b in re.split(r'^#\s+▶\s+', md, flags=re.M)[1:]:
        title, _, rest = b.partition("\n")
        title = re.sub(r'^(STEP|SLIDE)\s+\d+\s*[—-]\s*', '', title.strip(), flags=re.I)
        # Stop at the next top-level heading that is NOT a ▶ marker. Without this
        # the final ▶ section swallows everything after it — the appendix and its
        # "N things to know before recording" trailer, which is instructor-only.
        rest = re.split(r'^#\s+(?!▶)', rest, maxsplit=1, flags=re.M)[0]
        out[norm_title(title)] = merge_beats(clean_narration(rest))
    return out

def expected_output(path: pathlib.Path) -> str:
    """The appendix table — what a student's own run should produce — without the
    recording notes that follow it."""
    if not path.exists(): return ""
    md = path.read_text(encoding="utf-8")
    m = re.search(r'^#\s+Appendix[^\n]*\n(.*)', md, re.S | re.M)
    if not m: return ""
    body = re.split(r'\*\*\w+ things to know before recording\.\*\*', m.group(1))[0]
    return body.strip()

def frontmatter_title(p: pathlib.Path) -> str:
    m = re.search(r'^title:\s*"(.+?)"', p.read_text(encoding="utf-8"), re.M)
    return m.group(1) if m else p.stem

def build_lab(lab: pathlib.Path) -> pathlib.Path:
    stem = lab.stem                                    # Lecture09_Part1_lab
    nar  = ROOT / "Narration" / f"{stem.replace('_lab','')}_lab_script.md"
    body = re.sub(r'^---\n.*?\n---\n', '', lab.read_text(encoding="utf-8"), count=1, flags=re.S)
    said = narration_steps(nar)
    lines = [f"# {frontmatter_title(lab)}", "",
             f"*Run this one live: [the executable lab](../../labs/{stem}.html).*", ""]
    used = 0
    for title, content in lab_steps(body):
        lines += [f"## {title}", ""]
        if content: lines += [content, ""]
        key = norm_title(re.sub(r'^Step\s+\d+\s*[—-]\s*', '', title))
        prose = said.get(key)
        if prose is None:
            near = difflib.get_close_matches(key, list(said), n=1, cutoff=0.80)
            prose = said[near[0]] if near else None
        if prose:
            used += 1
            lines += ["::: {.callout-note collapse=\"true\"}\n## Walkthrough", "", prose, "", ":::", ""]
    exp = expected_output(nar)
    if exp:
        lines += ["## What your run should produce", "",
                  "Your numbers will differ where a model is stochastic; these are the values this "
                  "lab produces on the pinned environment.", "", exp, ""]
    out = OUT / f"{stem}.qmd"
    out.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return out, used

def build_assignment(hw: pathlib.Path) -> pathlib.Path:
    body = re.sub(r'^---\n.*?\n---\n', '', hw.read_text(encoding="utf-8"), count=1, flags=re.S)
    out = OUT / f"{hw.stem}.qmd"
    out.write_text(f"# {frontmatter_title(hw)}\n\n{body.strip()}\n", encoding="utf-8")
    return out

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    print("Assembling the workbook (generated — do not edit):")
    labs = sorted((ROOT / "Labs").glob("Lecture*_lab.qmd"))
    for lab in labs:
        p, used = build_lab(lab)
        print(f"  {p.name:<32} {used} step(s) with a walkthrough")
    for hw in sorted((ROOT / "Homework").glob("HW*.qmd")):
        print(f"  {build_assignment(hw).name}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
