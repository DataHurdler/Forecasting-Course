#!/usr/bin/env python3
"""Compare Beamer frame titles against their Quarto mirror's slide headings."""
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

rows = []
for tex in sorted(pathlib.Path('Slides').glob('Lecture*.tex')):
    n = tex.stem
    qmd = pathlib.Path('Quarto') / f'{n}.qmd'
    ft = frame_titles(tex.read_text(encoding='utf-8'))
    if not qmd.exists():
        rows.append((n, len(ft), None, 'NO MIRROR')); continue
    qh = qmd_headings(qmd.read_text(encoding='utf-8'))
    ok = len(qh) == len(ft)
    rows.append((n, len(ft), len(qh), 'ok' if ok else f'MISMATCH (want {len(ft)})'))

print(f"{'deck':<34}{'frames':>7}{'slides':>8}  status")
for n, f, q, s in rows:
    print(f"{n:<34}{f:>7}{('-' if q is None else q):>8}  {s}")

if len(sys.argv) > 1:
    n = sys.argv[1]
    ft = frame_titles(pathlib.Path(f'Slides/{n}.tex').read_text(encoding='utf-8'))
    print(f"\n{n} frame titles:")
    for k, t in enumerate(ft, 1): print(f"  {k:>2}. {t}")
