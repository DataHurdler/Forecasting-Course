# Session Log: Lecture 06 — Forecast Evaluation
**Date:** 2026-02-25
**Status:** COMPLETE
**Lecture:** `Slides/Lecture06_Evaluation.tex` + `scripts/Lecture06_Evaluation.ipynb`

---

## Goal

Create Lecture 06 (Forecast Evaluation) as a full first draft:
- Beamer slides (~27 pages): evaluation problem, error metrics, walk-forward validation,
  Diebold-Mariano test, forecast combination, takeaways
- Jupyter notebook (9 sections): walk-forward on RSXFS, DM test, combination strategies

---

## Key Decisions

| Decision | Rationale |
|----------|-----------|
| Metrics overview slide uses 2-column layout (definitionbox + keybox) instead of tabular in definitionbox | Prior L06 session revealed that tabular inside tcolorbox definitionbox leaves math mode open, causing `\"` accent errors downstream. Avoid tabulars inside colored boxes. |
| `e_{t,h}` notation (double-subscript) for walk-forward, `e_{T+h}` for metrics | Both are standard; bridge note added explaining equivalence |
| Combination puzzle treated as a "surprising" takeaway | Empirically robust finding; creates memorable "Aha" moment for students |
| DM notebook uses manual Newey-West HAC | More transparent for pedagogy than statsmodels HAC wrappers |
| Equal-weight combo highlighted (bold) as the practical recommendation | Consistent with combination puzzle: estimated weights often underperform |

---

## Compilation Issues Encountered and Resolved

### Issue 1: `! Missing $ inserted` + `Command \" invalid in math mode`
**Cause:** Original metrics slide used a `tabular` inside a `definitionbox` tcolorbox.
The `tabular` left math mode open; subsequent `na\"{i}ve` was processed in math mode.
**Fix:** Rewrote metrics slide to use two-column layout: `definitionbox` with `\hfill` formatting
(no tabular), `keybox` on the right. Removed `na\"{i}ve` from inside the definitionbox.

### Issue 2: `Overfull \hbox (27.87pt)` — TimeSeriesSplit
**Cause:** `\texttt{sklearn.model_selection.TimeSeriesSplit}` too wide for column.
**Fix:** Split into `\texttt{TimeSeriesSplit} in \texttt{sklearn.model\_selection}`.

---

## Quality Review Findings and Fixes Applied

### CRITICAL
1. **Duplicate Socratic question** — the same question ("RMSE(A) < RMSE(B) but MASE(A) > MASE(B)...")
   appeared verbatim on both the Metrics Overview slide and the MAPE/MASE slide.
   **Fix:** Replaced the MAPE/MASE slide Socratic with a distinct MASE-specific prompt
   (new product launch, $y_1=0$, which metric fails?).

### MAJOR
2. **`$\rho$` used as a verb** — Line 554: `"SARIMA errors $\rho$ ETS errors $\approx 0.72$"`.
   **Fix:** `"SARIMA--ETS error correlation $\approx 0.72$ on RSXFS"`.

3. **Missing notation bridge** — metrics slide uses `$e_{T+h}$` (fixed origin);
   walk-forward recipe uses `$e_{t,h}$` (varying origin). Students may not see these as the same.
   **Fix:** Added muted note to walk-forward recipe:
   `"$e_{t,h}$ generalizes $e_{T+h}$ from Section 2 to multiple origins $t$;
   the metric formulas are the same, averaged over $t$."`

4. **Frame title duplicates section title** — Frame "The Diebold-Mariano Test" repeated
   section name exactly.
   **Fix:** Renamed frame to "DM Statistic and Mechanics".

### MINOR
5. **MAPE decision guide entry unclear** — `"MAPE: cross-series ($y_t \gg 0$)"` ambiguous.
   **Fix:** `"MAPE: only when $y_t \gg 0$"`.

---

## Final State

| Item | Value |
|------|-------|
| PDF pages | 27 |
| Compilation errors | 0 |
| Overfull hboxes | 0 |
| Undefined citations | 0 |
| New bib entries | BatesGranger1969, StockWatson2004, Harvey1997 |
| Notebook sections | 9 |
| Notebook figures | lecture06_horizon_profile.png, lecture06_dm_plot.png, lecture06_forecasts.png |

---

## Bibliography Entries Added This Session

```bibtex
BatesGranger1969  — The Combination of Forecasts, ORQ 1969
StockWatson2004   — Combination Forecasts of Output Growth, JoF 2004
Harvey1997        — Testing Equality of Prediction MSE, IJF 1997
```

---

## Open Issues

- None blocking. Lecture 06 is first-draft complete.
- Lectures 07–12 remain to be created (one at a time, with review between).

---

## [LEARN] Entries

- `[LEARN:latex] Avoid tabular inside tcolorbox definitionbox — leaves math mode open,
  causing downstream \"{} accent errors in XeLaTeX.`
- `[LEARN:pedagogy] Duplicate Socratic questions across adjacent slides: always diff-check
  footnotes when copying slide templates.`

---

## Proofreader Review + Fixes (2026-02-28)

**Report:** `quality_reports/Lecture06_Evaluation_report.md`
**15 issues found (2 CRITICAL, 5 MAJOR, 8 MINOR)**

### Fixes Applied

| # | Severity | Fix |
|---|----------|-----|
| 1 | CRITICAL | Combination variance formula: `2ρσ₁₂` → `2ρσ₁σ₂` (line 541) |
| 2 | CRITICAL | MAPE asymmetry description reversed — rewrote to correctly state under-forecasts are bounded at 100%, over-forecasts are unbounded (lines 189-191) |
| 3 | MAJOR | Defined `e^+` and `e^-` in-line: `\max(e,0)` and `\max(-e,0)` (lines 172-173) |
| 4 | MAJOR | "Section~2" cross-reference → "the Error Metrics section" (line 379) |
| 5 | MAJOR | "consistently outperform" → "generally outperform" for BatesGranger1969 (lines 546-548) |
| 6 | MAJOR | `naive` → `na\"{i}ve` in keybox (line 127) |
| 7 | MAJOR | Added `\newcommand{\MASE}{\operatorname{MASE}}` to `Preambles/header.tex` |

### Deferred
- Issues 8-15 (MINOR): `n_h` formula, "fail to reject" phrasing, citation in title bar, missing \sectionslide for final section, missing \label on sections, ML assumptions, `e^{+}` brace encoding, walk-forward subtitle — low priority, deferred to next revision pass.

**Final state (2026-02-28):** 27 pages, 0 errors, 0 overflows.

### [LEARN] from this fix pass
- `[LEARN:math] Combination variance Var(½e₁+½e₂): correlation form is ¼(σ₁²+2ρσ₁σ₂+σ₂²), NOT ¼(σ₁²+2ρσ₁₂+σ₂²). The covariance σ₁₂ already absorbs the product σ₁σ₂; ρ is the normalized (dimensionless) correlation.`
- `[LEARN:content] MAPE asymmetry: UNDER-forecasts are BOUNDED at 100% (when ŷ=0, |e/y|=1). OVER-forecasts are UNBOUNDED above. MAPE penalizes over-forecasts more, biasing toward under-forecasting models.`

---

## Pedagogy Review + Fixes (2026-02-28)

**Report:** `quality_reports/Lecture06_Evaluation_pedagogy_report.md`
**Score:** 8/13 followed, 3/13 violated, 2/13 partially applied

### Fixes Applied

| # | Severity | Fix |
|---|----------|-----|
| 1 | HIGH | Split "DM Statistic and Mechanics" into two slides: "DM Test: Loss Differentials" (defines $d_t$, numeric example $d_1 = 3.2^2 - 2.8^2 = +2.40$, introduces $\bar{d}$) + "DM Test: The Statistic" (full formula with footnote labels, HAC columns, warningbox) |
| 2 | MEDIUM | Added `\sectionslide{Key Takeaways and Roadmap}{...}` before final section frame |
| 3 | MEDIUM | Demoted 3 low-value keyboxes to plain bold italic: "Always report accuracy by horizon" (horizon profile slide), "Walk-forward errors...track record" (recipe slide), "If two models have equal accuracy..." (combination slide) |
| 4 | MEDIUM | ML bridge table: "Minimal" → "Fewer formal (stationarity helpful)"; "High (regularize!)" → "High (mitigated by CV)" |

### Deferred
- Pattern 2 (notation): one-sentence horizon/n clarifier before metrics formulas — low priority
- Notation bridge note for RMSE formula (single-origin vs multi-origin) — low priority
- Student concerns (HAC gloss, DM Python pointer, Clark-West explanation, combination theory note) — next revision pass

**Final state (2026-02-28):** 29 pages (+2 from DM split + sectionslide), 0 errors, 0 overflows.

### [LEARN] from pedagogy review
- `[LEARN:pedagogy] DM test "Statistic and Mechanics" frame had 5 elements: loss differential, formula, asymptotic distribution, H₀, HAC. Two-slide split: Slide 1 = d_t definition + numeric example; Slide 2 = full statistic with labels + HAC columns.`
- `[LEARN:pedagogy] Box fatigue threshold: >50% of content slides carrying a keybox is over the ceiling. Demote motivational prose keyboxes to bold italic; reserve keybox for formal key results.`
