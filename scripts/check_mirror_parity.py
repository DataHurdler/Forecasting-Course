#!/usr/bin/env python3
"""Compare a Beamer deck against its Quarto mirror — content slides AND sections.

Frame counts alone are not parity. Lecture 8's mirror merged two sections and
renamed a third; the deck kept five sections and the mirror had four, and this
gate reported `ok` for months because section slides are invisible to a frame
count on BOTH sides: in Beamer they are written `\\sectionslide{..}{..}`, a macro
rather than a literal `\\begin{frame}`, and in the mirror they are `# ` headings
rather than `## `. An entire structural layer went unchecked, so a rebuild driven
by "the mirror is two slides short" could merge sections and still come out level.

So this compares both layers, and compares section NAMES, not just how many.
"""
import re, sys, pathlib

def frame_titles(tex):
    out, i = [], 0
    for m in re.finditer(r'\\begin\{frame\}(\[[^\]]*\])?\s*\{', tex):
        j = m.end(); depth = 1; buf = []
        while j < len(tex) and depth:
            c = tex[j]
            if c == '{': depth += 1
            elif c == '}':
                depth -= 1
                if not depth: break
            buf.append(c); j += 1
        t = ''.join(buf)
        t = re.sub(r'\\(parencite|cite|textcite)\{[^}]*\}', '', t)
        t = re.sub(r'\\[a-zA-Z]+\s*', '', t).replace('---', '—')
        out.append(' '.join(t.split()))
    return out

def qmd_headings(q):
    return [' '.join(l[3:].split()) for l in q.splitlines() if l.startswith('## ')]

def tex_sections(tex):
    """Section slides, which are \\sectionslide{Title}{subtitle} not \\begin{frame}."""
    out = []
    for m in re.finditer(r'\\sectionslide\s*\{', tex):
        j, depth, buf = m.end(), 1, []
        while j < len(tex) and depth:
            c = tex[j]
            if c == '{': depth += 1
            elif c == '}':
                depth -= 1
                if not depth: break
            buf.append(c); j += 1
        t = re.sub(r'\\[a-zA-Z]+\s*', '', ''.join(buf)).replace('---', '—')
        out.append(' '.join(t.split()))
    return out

def qmd_sections(q):
    return [' '.join(l[2:].split()) for l in q.splitlines()
            if l.startswith('# ') and not l.startswith('## ')]

def norm(t):
    return re.sub(r'[^a-z0-9]+', '', t.lower())

rows = []
for tex in sorted(pathlib.Path('Slides').glob('Lecture*.tex')):
    n = tex.stem
    qmd = pathlib.Path('Quarto') / f'{n}.qmd'
    ft = frame_titles(tex.read_text(encoding='utf-8'))
    if not qmd.exists():
        rows.append((n, len(ft), None, 'NO MIRROR')); continue
    body = qmd.read_text(encoding='utf-8')
    qh = qmd_headings(body)
    ts, qs = tex_sections(tex.read_text(encoding='utf-8')), qmd_sections(body)
    problems = []
    if len(qh) != len(ft):
        problems.append(f'slides {len(qh)}, want {len(ft)}')
    if len(qs) != len(ts):
        problems.append(f'sections {len(qs)}, want {len(ts)}')
    else:
        drifted = [(a, b) for a, b in zip(ts, qs) if norm(a) != norm(b)]
        if drifted:
            problems.append('section renamed: ' + '; '.join(f'{a!r} -> {b!r}' for a, b in drifted))
    rows.append((n, len(ft), len(qh), 'ok' if not problems else 'MISMATCH — ' + ', '.join(problems)))

print(f"{'deck':<34}{'frames':>7}{'slides':>8}  status")
for n, f, q, s in rows:
    print(f"{n:<34}{f:>7}{('-' if q is None else q):>8}  {s}")

if len(sys.argv) > 1:
    n = sys.argv[1]
    ft = frame_titles(pathlib.Path(f'Slides/{n}.tex').read_text(encoding='utf-8'))
    print(f"\n{n} frame titles:")
    for k, t in enumerate(ft, 1): print(f"  {k:>2}. {t}")
