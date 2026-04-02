# Session Log: Lecture 07 — Machine Learning Introduction
**Date:** 2026-02-25
**Status:** COMPLETE
**Lecture:** `Slides/Lecture07_MLIntro.tex` + `scripts/Lecture07_MLIntro.ipynb`

---

## Goal

Create Lecture 07 (Machine Learning Introduction) as a full first draft — the bridge from classical forecasting (L01–L06) into the ML portion of the course (L07–L12).

---

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| Sections 5 & 6 are previews only (regularization, features) | Full treatments in L08 and L11; L07 establishes vocabulary and motivation without duplicating future content |
| Synthetic bias-variance illustration in notebook | RSXFS has no known ground truth; polynomial + sin example shows the U-curve cleanly with controlled σ² |
| Walk-forward evaluation AND TimeSeriesSplit CV in same notebook | L07 objective: distinguish "evaluation" (walk-forward, from L06) from "tuning" (TimeSeriesSplit CV, new in L07) |
| Validation color: `unogreen` (not orange) | `unoorange` not defined in header.tex; traffic-light convention: blue=train, green=val, red=test |
| `[fragile]` on frames with lstlisting | Required for verbatim environments inside Beamer frames |

---

## Compilation Issues Encountered and Resolved

### Issue 1: `\pgfmathsetmacro` inside Beamer frame
**Cause:** `\pgfmathsetmacro{\ybot}{(\fold-1)*0.7}` inside a `\foreach` loop fails
in Beamer because frames save and replay content.
**Fix:** Replaced with hardcoded y-coordinates for each of the 5 walk-forward folds.
**[LEARN:latex] Never use `\pgfmathsetmacro` inside Beamer frames — use hardcoded coordinates.**

### Issue 2: `unoorange`/`unolightorange` colors not defined
**Cause:** Validation band used `\unoorange` and `\unolightorange` which don't exist
in `header.tex`. Only blue, red, gray, green variants are defined.
**Fix:** Changed all validation colors to `unogreen` / `unolightgreen`.
**[LEARN:latex] header.tex palette: unoblue, unored, unogray, unogreen + light variants. No orange.**

### Issue 3: `lstlisting` inside `\column` without `[fragile]`
**Cause:** `lstlisting` is a verbatim environment; fails inside Beamer `columns`
unless the frame uses `[fragile]`.
**Fix:** Added `[fragile]` to both frames containing `lstlisting` blocks.
**[LEARN:latex] Any Beamer frame with verbatim/lstlisting must use `[fragile]`.**

### Issue 4: Overfull \hbox (55.27pt) on "Three Gaps" table
**Cause:** Three-column table with `\small` overflowed the left column (0.54\textwidth).
**Fix:** Switched to `\footnotesize` with explicit `p{...}` column widths and
shorter cell text.

### Issue 5: Overfull \vbox (5.3pt) on walk-forward CV frame
**Cause:** Frame content slightly too tall.
**Fix:** Reduced TikZ `yscale` from 0.72 to 0.60; increased `\vspace{-0.1cm}` to `\vspace{-0.3cm}`.

### Issue 6: `\end{frame}` unclosed — pipeline frame
**Cause:** TikZ `box/.style` was missing `align=center`; nodes with `\\` newlines
inside them triggered `! LaTeX Error: Not allowed in LR mode`.
**Fix:** Added `align=center` to `box/.style` in the pipeline TikZ.
**[LEARN:latex] TikZ node with `\\` newlines requires `align=center` in style.**

---

## Quality Review Findings and Fixes

### MAJOR
1. **`\log(\lambda)` ambiguous** — shrinkage path x-axis used `$\log(\lambda)$` but
   tick labels showed base-10 values. Fixed to `$\log_{10}(\lambda)$`.

### No CRITICAL issues found.

---

## New Bibliography Entries Added

```bibtex
Bergmeir2018  — Validity of CV for autoregressive TS prediction, CSDA 2018
Arlot2010     — Survey of cross-validation procedures, Statistics Surveys 2010
```

---

## Final State

| Item | Value |
|------|-------|
| PDF pages | 30 |
| Compilation errors | 0 |
| Overfull hboxes | 0 |
| Undefined citations | 0 |
| New bib entries | Bergmeir2018, Arlot2010 |
| Notebook sections | 9 |
| Notebook figures | lecture07_cv_tuning.png, lecture07_bias_variance.png, lecture07_horizon_profile.png, lecture07_lasso_path.png |

---

## [LEARN] Entries

- `[LEARN:latex] Never use \pgfmathsetmacro inside Beamer frames — Beamer's save/replay breaks it. Use hardcoded coordinates.`
- `[LEARN:latex] header.tex color palette: unoblue, unored, unogray, unogreen and light variants. No orange. Validation = unogreen.`
- `[LEARN:latex] Beamer frames with verbatim/lstlisting must use [fragile] option.`
- `[LEARN:latex] TikZ node styles with \\\\ newlines require align=center in the style definition.`

---

## Proofreader Review + Fixes (2026-02-28)

**Report:** `quality_reports/Lecture07_MLIntro_report.md`
**17 issues found (4 CRITICAL, 7 MAJOR, 6 MINOR)**

### Fixes Applied

| # | Severity | Fix |
|---|----------|-----|
| 1 | CRITICAL | Citation key `Zou2005` → `ZouHastie2005` (line 568) |
| 2 | CRITICAL | Frame title "Three Gaps ML Fills" → "Four Gaps ML Fills" (table has 4 rows) |
| 3 | CRITICAL | M4 sMAPE values corrected: ES-RNN 11.37 → 11.374; Theta 11.37 → 11.551; FFORMA 11.57 → 11.720 |
| 4 | CRITICAL | `Bibliography_base.bib` `James2021` entry: Python edition is 2023, 1st edition (not 2021, 2nd). Added Taylor as 5th author. |
| 5 | MAJOR | `p > T` → `k \gg T` to avoid clash with VAR lag-order notation from L05 |
| 6 | MAJOR | `\operatorname{Var}` → `\Var` macro in Key Takeaways keybox (line 794) |
| 7 | MAJOR | σ² bullet: "only better data can" → "neither better models nor additional observations can eliminate it" |
| 8 | MAJOR | `\hat{\beta}` → `\bhat` macro (line 561) |
| 9 | MAJOR | Test RMSE adjusted from $1{,}620$ to $1{,}810$ (now above CV RMSE $1{,}780$, consistent with CV-as-honest-estimator narrative) |
| 10 | MAJOR | "modelling" → "modeling" (American English, line 131) |
| 11 | MAJOR | "minimising" → "minimizing" (American English, line 529) |
| 12 | MINOR | `\parencite{Hastie2009}` moved from `definitionbox` title (line 136) to inline `\muted{\footnotesize}` at end of box |
| 13 | MINOR | `\parencite{Hastie2009}` moved from second `definitionbox` title (line 558) to `\hfill` at bottom of box |
| 14 | MINOR | `$k$-Fold` → `$k$-fold` in frame title (line 409) |
| 15 | MINOR | "Now we stress-test its assumptions." → "This lecture examines where its assumptions break down." (academic register) |

### Deferred
- Issues 6 (MINOR): Add `\label` on section declarations — low priority
- Student concerns: HAC gloss, Clark-West explanation, DM Python pointer — next pass
- `$k$-fold` vs `$k$-Fold` capitalization: one remaining instance in sectionslide subtitle — consistent now

**Final state (2026-02-28):** 30 pages, 0 errors, 0 overflows.

---

## Pedagogy Review + Fixes (2026-02-28)

**Report:** `quality_reports/Lecture07_MLIntro_pedagogy_report.md`
**11/13 patterns followed; 1 violated (HIGH); 1 partially applied (LOW)**

### Fixes Applied

| # | Priority | Fix |
|---|----------|-----|
| 1 | HIGH | Split "MSE Decomposition" into two slides: Slide 1 = formula + forward pointer; Slide 2 = term-by-term unpacking with example values ($\text{Bias}^2 \approx 0.42$, $\Var \approx 0.31$, $\sigma^2 = 0.07$) + keybox of two controllable levers |
| 2 | MEDIUM | Added hyperparameter definition sentence before enumerated CV procedure on "CV in Practice" slide (`\vspace{4pt}` used instead of `\\[4pt]` — latter causes "no line here to end" error) |
| 3 | MEDIUM | Added i.i.d. motivation sentence (muted) on "From Time Series to Feature Matrix" slide explaining why ML needs explicit features unlike ARIMA |
| 4 | LOW | Added EN α disambiguation note in right column of Regularization Preview slide (not ETS α from L03) |
| 5 | LOW | Added Socratic question on Data Leakage slide (shortened to fit — vbox overflow with full sentence) |

### Compilation Issues from Pedagogy Fixes
- `\\[4pt]` after `{\small...}` group → `"There's no line here to end"` — fixed with `\vspace{4pt}`
- Socratic question + `\vspace{0.1cm}` caused 16.26pt vbox overflow on Data Leakage frame — fixed by removing `\vspace` and shortening question text

**Final state (2026-02-28):** 31 pages (+1 from MSE Decomposition split), 0 errors, 0 overflows.

### [LEARN] from pedagogy
- `[LEARN:latex] After a closing brace of a group ({\small...}), use \\vspace{Xpt} not \\\\[Xpt] to add vertical space — the double-backslash needs a line to end and causes a LaTeX error outside tabular/align.`

### [LEARN] from proofreader
- `[LEARN:content] M4 Competition sMAPE (Makridakis et al. 2020, Table 1 overall): ES-RNN = 11.374, Theta = 11.551, FFORMA = 11.720. Theta did NOT tie with ES-RNN. Always transcribe from paper, not rounded values.`
- `[LEARN:bib] ISL textbook has two editions: ISLR2 (R, 2nd ed., 2021, James/Witten/Hastie/Tibshirani) and ISLP (Python, 1st ed., 2023, James/Witten/Hastie/Tibshirani/Taylor). They are different publications. James2021 key should use 2023 year + 1st edition for the Python version.`
- `[LEARN:content] σ² = Var[ε] is the irreducible noise variance. It cannot be reduced by more observations from the same DGP — "more data" does not help. Only a fundamentally different measurement process could lower it. Never say "only better data can reduce σ²".`
- `[LEARN:notation] In this course, p has three conflicting uses: VAR lag order (L05), regression parameter count (L07), and polynomial degree. When discussing "too many parameters" in L07, use k (parameter count) not p to avoid L05 collision.`

---

## Quarto Translation (2026-03-02)

**File created:** `Quarto/Lecture07_MLIntro.qmd`
**Translation completed by:** `/translate-to-quarto Lecture07_MLIntro`

### Translation Decisions

| Item | Decision |
|------|----------|
| TikZ diagrams | Converted to inline SVG using UNO brand colors (#005CA9, #E41C38, #525252, #15803d) |
| Custom environments | All 4 environments (keybox, definitionbox, warningbox, examplebox) use existing CSS classes in emory-clean.scss |
| `\textcite{Bergmeir2018}` | Rendered as `@Bergmeir2018` (inline citation, no brackets) to match author-year inline style |
| `\parencite{}` | Rendered as `[@...]` (parenthetical citation) |
| `\MSE`, `\Var`, `\bhat` macros | Expanded to `\text{MSE}`, `\text{Var}`, `\hat{\beta}` in QMD |
| `\negc{}` | Rendered as `[...]{.negative}` |
| `\muted{}` | Rendered as `[...]{.neutral}` |
| Code blocks (`lstlisting`) | Converted to fenced ` ```python ``` ` blocks |
| Outline | 7 items matching 7 `\section{}` commands in source |

### Slide Count
- H2 content slides: 22
- H1 section slides: 7
- Total: 29 slides (vs. Beamer 31 PDF pages — difference is title page + separate section slides)

### No Beamer source corrections required.
