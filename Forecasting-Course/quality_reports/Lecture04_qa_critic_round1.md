# QA Critic Report: Lecture04_ARIMA — Round 1
**Date:** 2026-03-06
**Beamer source:** `Slides/Lecture04_ARIMA.tex`
**Quarto source:** `Quarto/Lecture04_ARIMA.qmd`
**Reviewer:** quarto-critic agent

---

## Hard Gate Status

| Gate | Status | Notes |
|------|--------|-------|
| Overflow | PASS | No content cut off; SARIMA equation uses `.smaller` wrapper |
| Plot Quality | PASS | SVG charts faithful to TikZ originals; interactive HTML >= static PDF |
| Content Parity | PASS | All 26 Beamer frames represented in QMD |
| Visual Regression | PASS | SVG diagrams match Beamer concepts; Box-Jenkins flowchart reproduced |
| Slide Centering | PASS | `center: false` in YAML; no jumping |
| Notation Fidelity | PASS | All equations verbatim from Beamer (operator notation, SARIMA, ARMA, ARIMA) |

---

## Issues Found

### QA-01 — MINOR: Ellipsis in Seasonal ARIMA section divider
- **Location:** QMD line 547
- **Beamer:** `lags $m$, $2m$, $3m$,\ldots`
- **Quarto:** `lags $m$, $2m$, $3m$, ...`
- **Issue:** Literal `...` in Markdown text renders as three periods, not a proper typographic ellipsis. Should be `$\ldots$`.
- **Fix:** Replace `, ...` with `, $\ldots$`

### QA-02 — MINOR: ACF SVG — lower confidence bound partially overlaps x-tick labels
- **Location:** QMD lines 261–262 (ACF SVG)
- **Issue:** The lower dashed confidence bound is drawn at y=105; x-tick labels at y=102. The 3px gap causes slight visual overlap. The bound is present but slightly obscured.
- **Fix:** Shift lower bound to y=107 and x-tick labels to y=104 for clarity, or increase viewBox height to 115.

### QA-03 — MINOR: PACF SVG — small negative bars rendered above baseline
- **Location:** QMD lines 346–351 (PACF SVG, k=4,6,9)
- **Issue:** Negative PACF values (k=4,6,9) are shown in red (`#E41C38`) with `y` set 1px above baseline (y=99 for baseline at y=100). This means the bars appear to go upward (positive direction) in red, which is visually confusing — small negative bars should extend downward from the baseline.
- **Fix:** For negative bars, set `y=100` (baseline) and use positive `height` values so bars extend downward. E.g., `<rect x="122" y="100" width="7" height="2" fill="#E41C38"/>` for a small negative value at k=4.

### QA-04 — MINOR: Box-Jenkins SVG feedback label hyphen-break
- **Location:** QMD lines 512–513 (Box-Jenkins SVG)
- **Issue:** "Inadequate" is split as `"Inade-"` / `"quate"` across two SVG text elements due to space constraints. Beamer renders as a single word on one line.
- **Fix:** Use a narrower font-size (7px instead of 8px) and combine onto one line: `<text x="222" y="77" font-size="7" ...>Inadequate</text>`, removing the second text element.

### QA-05 — MINOR: Box-Jenkins citation: parenthetical vs. in-text
- **Location:** QMD line 473
- **Beamer:** `\textcite{BoxJenkins2015}` in frame title (renders as "Box and Jenkins (2015)")
- **Quarto:** `[@BoxJenkins2015]` in heading (renders as "(Box and Jenkins 2015)")
- **Issue:** Parenthetical vs. in-text citation in slide title. Low visual impact but inconsistent with Beamer intent.
- **Fix:** Change to `@BoxJenkins2015` (no brackets) for inline citation rendering.

---

## Summary

| Severity | Count |
|----------|-------|
| Critical | 0 |
| Major | 0 |
| Minor | 5 |

**Verdict: CONDITIONAL PASS.** No hard gate failures. Five minor issues to fix before final approval.

---

## Content Parity Detail

All 26 Beamer frames accounted for in QMD:
- Title slide: YAML front matter
- Outline, all 6 section dividers, all 18 content slides, References: all present
- All Socratic prompts: present with `.neutral .smaller` styling
- All keyboxes, definitionboxes, warningboxes, exampleboxes: present with correct CSS classes
- All tabular content (unit root table, KPSS table, ACF/PACF pattern table): present as Markdown tables

## Notation Fidelity Detail

Verified 9 major equations — all match Beamer verbatim:
- Weak stationarity conditions (3 equations)
- ADF regression
- Backshift operator expressions (first diff, seasonal diff)
- ACF definition
- ARMA, ARIMA, SARIMA operator equations
- Multi-step forecast recursion
- Random walk expanded (Quarto adds `\displaystyle` — minor enhancement)
