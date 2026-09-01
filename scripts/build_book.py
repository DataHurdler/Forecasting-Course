#!/usr/bin/env python3
"""Assemble book chapters from the course materials that already exist.

    python scripts/build_book.py                 # all configured chapters
    python scripts/build_book.py Lecture09_Part1 # one

**Nothing here is hand-written.** A chapter is generated from the parity-checked
Quarto mirror (its tables, figures and boxes) joined to the deck narration (the
prose that explains them), on the slide title they share. book/chapters/ is
disposable output; edit the deck or the narration, never the chapter.

That is what makes the book exact by construction rather than by discipline: a
figure or a number cannot drift from the deck, because it is never copied — it is
read from the deck's own mirror on every build.
"""
import re, sys, pathlib, difflib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT  = ROOT / "book" / "chapters"

CHAPTERS = [
    ("Lecture01_ETS_Eval",            "Lecture01_script.md"),
    ("Lecture02_ARIMA_VAR",           "Lecture02_script.md"),
    ("Lecture03_GAMs",                "Lecture03_script.md"),
    ("Lecture04_DecisionTrees",       "Lecture04_script.md"),
    ("Lecture05_TreeEnsembles",       "Lecture05_script.md"),
    ("Lecture06_Regularization",      "Lecture06_script.md"),
    ("Lecture07_NeuralNets",          "Lecture07_script.md"),
    ("Lecture08_CNNs",                "Lecture08_script.md"),
    ("Lecture09_Part1_RNN_LSTM",      "Lecture09_Part1_script.md"),
    ("Lecture09_Part2_Transformers",  "Lecture09_Part2_script.md"),
    ("Lecture10_BayesianFoundations", "Lecture10_script.md"),
    ("Lecture11_Part1_BayesianTS",    "Lecture11_Part1_script.md"),
    ("Lecture11_Part2_Hierarchical",  "Lecture11_Part2_script.md"),
    ("Lecture12_BayesianRegression",  "Lecture12_script.md"),
    ("Lecture13_Synthesis",           "Lecture13_script.md"),
]

# --- narration cleaning -------------------------------------------------------
STAGE = re.compile(r'^\s*\*\([^)]*\)\*\s*$')          # *(Screen: run the cell.)*
PAUSE = re.compile(r'^\s*\*\*\[pause\]\*\*.*$', re.I) # **[pause]** — *let it sit*
STOP  = re.compile(r'^\s*\*\*\[STOP[^\]]*\]\*\*(.*)$', re.I)
RULE  = re.compile(r'^\s*---\s*$')

def clean_narration(block: str) -> str:
    """Strip what only makes sense to a person holding a microphone."""
    out, in_try = [], False
    for line in block.split("\n"):
        if STAGE.match(line) or PAUSE.match(line) or RULE.match(line):
            continue
        m = STOP.match(line)
        if m:
            if in_try:
                out.append(":::")
            out.append('::: {.callout-tip}\n## Try it')
            in_try = True
            trailing = re.sub(r'^\s*—\s*\*\(.*?\)\*\s*', '', m.group(1)).strip()
            if trailing:
                out.append(trailing)
            continue
        # a stage direction sharing a line with prose: drop the parenthetical
        line = re.sub(r'\*\([^)]*\)\*', '', line).rstrip()
        if in_try and line.strip() == "":
            out.append(":::")
            in_try = False
        out.append(line)
    if in_try:
        out.append(":::")
    text = "\n".join(out)
    return re.sub(r'\n{3,}', '\n\n', text).strip()

# --- parsing ------------------------------------------------------------------
# --- title matching ------------------------------------------------------------
# A deck title is LaTeX-flavoured markdown ("Ridge Regression ($\\ell_2$)",
# "XGBoost: Three Advances [@Chen2016]", "Bias--Variance"); the narration says the
# same title in plain speech ("ridge regression (ℓ₂)", "xgboost: three advances",
# "bias–variance"). Exact matching loses 13 of 208 headings across the course to
# nothing but notation, so normalise before comparing, and fall back to a high
# fuzzy threshold. Anything still unmatched is REPORTED, never dropped quietly —
# a chapter missing its prose should be loud.
_CITE = re.compile(r'\s*\[@[^\]]+\]')
_MATHY = str.maketrans({'$': '', '\\': '', '—': '-', '–': '-', 'ℓ': 'l',
                        '₀': '0', '₁': '1', '₂': '2', 'λ': 'lambda', 'α': 'alpha'})

def norm_title(t: str) -> str:
    t = _CITE.sub('', t).lower()
    t = t.replace('---', '-').replace('--', '-')
    t = re.sub(r'\([^)]*\)', '', t)      # "(OOB)", "(Regression)" — spoken titles drop them
    t = t.translate(_MATHY)
    t = re.sub(r'\bell_?(\d)\b', r'l\1', t)
    t = re.sub(r'[^a-z0-9]+', '', t)
    return t

def parse_mirror(path: pathlib.Path):
    """[(level, title, body)] for every '# ' and '## ' heading, in order."""
    body = path.read_text(encoding="utf-8")
    body = re.sub(r'^---\n.*?\n---\n', '', body, count=1, flags=re.S)   # frontmatter
    parts, cur = [], None
    for line in body.split("\n"):
        m = re.match(r'^(#{1,2})\s+(.+?)\s*$', line)
        if m and not line.startswith("###"):
            if cur: parts.append(cur)
            cur = [len(m.group(1)), m.group(2).strip(), []]
        elif cur:
            cur[2].append(line)
    if cur: parts.append(cur)
    cleaned = []
    for lv, t, b in parts:
        # Drop the slide-separating horizontal rules; they are RevealJS pagination,
        # not content, and in running prose they read as section breaks.
        body = "\n".join(l for l in b if not re.match(r'^\s*---\s*$', l)).strip()
        cleaned.append((lv, t, body))
    return cleaned

def parse_narration(path: pathlib.Path):
    """{normalised title: prose} from '# ▶ SLIDE n — Title' blocks."""
    text = path.read_text(encoding="utf-8")
    blocks = re.split(r'^#\s+▶\s+SLIDE\s+\d+\s+—\s+', text, flags=re.M)[1:]
    out = {}
    for b in blocks:
        title, _, rest = b.partition("\n")
        key = norm_title(title.strip().replace("Section divider: ", ""))
        out[key] = clean_narration(rest)
    return out

def deck_title(path: pathlib.Path) -> str:
    m = re.search(r'^title:\s*"(.+?)"', path.read_text(encoding="utf-8"), re.M)
    return m.group(1) if m else path.stem

# --- assembly -----------------------------------------------------------------
def build(stem: str, narration_name: str) -> pathlib.Path:
    mirror = ROOT / "Quarto" / f"{stem}.qmd"
    narr   = ROOT / "Narration" / narration_name
    parts  = parse_mirror(mirror)
    prose  = parse_narration(narr)

    lines = [f"# {deck_title(mirror)}", ""]
    used = 0
    fuzzy, missing = [], []
    seen_section = False
    for level, title, body in parts:
        if level == 1:
            seen_section = True
        # Slides before the first section divider (the outline) are chapter-level.
        depth = "## " if level == 1 or not seen_section else "### "
        lines.append(depth + title)
        lines.append("")
        if body:
            lines += [body, ""]
        said = prose.get(norm_title(title))
        if said is None:
            key = norm_title(title)
            # A spoken title is often the deck's title shortened: the subtitle
            # after a colon is dropped ("Out-of-Bag (OOB) Error: Free
            # Cross-Validation" is said as "Out-of-Bag Error"), or a parenthetical
            # goes ("The CART Algorithm (Regression)"). Accept a narration key
            # that is a prefix of the deck's, when it is long enough to be
            # unambiguous.
            prefixes = [k for k in prose if len(k) >= 5 and key.startswith(k)]
            if prefixes:
                said = prose[max(prefixes, key=len)]
                fuzzy.append(title)
            else:
                near = difflib.get_close_matches(key, list(prose), n=1, cutoff=0.80)
                if near:
                    said = prose[near[0]]
                    fuzzy.append(title)
                else:
                    missing.append(title)
        if said:
            # A section divider's slide body is its one-line subtitle, which the
            # narration then says again. Keep it once.
            if body and said.startswith(body):
                said = said[len(body):].lstrip()
            used += 1
            if said:
                lines += [said, ""]
    out = OUT / f"{stem}.qmd"
    out.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    note = f"  {out.relative_to(ROOT)}  —  {len(parts)} headings, {used} with narration"
    if fuzzy:
        note += f", {len(fuzzy)} matched on normalised title"
    print(note)
    for t in missing:
        print(f"      !! no narration for: {t}")
    return out

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    want = sys.argv[1] if len(sys.argv) > 1 else None
    todo = [c for c in CHAPTERS if want is None or c[0].startswith(want)]
    if not todo:
        print(f"no chapter matching {want!r}"); return 1
    print("Assembling chapters (generated — do not edit):")
    for stem, narration in todo:
        build(stem, narration)
    return 0

if __name__ == "__main__":
    sys.exit(main())
