# Adversarial QA: Lecture07 Critic Report — Round 1
**File:** `Quarto/Lecture07_MLIntro.qmd` vs `Slides/Lecture07_MLIntro.tex`
**Reviewer:** quarto-critic agent
**Date:** 2026-03-06
**Method:** Static source-to-source comparison (Quarto not rendered — no HTML present)

---

## Hard Gate Status

| Gate | Status | Notes |
|------|--------|-------|
| Content Parity | PASS | All slides, sections, and key content present |
| Notation Fidelity | PASS (minor gap) | Math notation faithful; one minor delta noted |
| Visual Regression | PASS | All TikZ diagrams replaced with inline SVG |
| Slide Centering | PASS | Section slides use `level1` CSS; layout consistent |
| Overflow | CANNOT VERIFY | No rendered HTML available |
| Plot Quality | PASS | SVG replacements are faithful representations |

---

## Slide-by-Slide Audit

### Outline slide
- Beamer: `\tableofcontents` (auto-generated from `\section` declarations)
- QMD: Manual numbered list of 7 sections
- **Status:** PASS — content matches. Manual list is acceptable for RevealJS.

---

### Section slides (7 total)
- Beamer: `\sectionslide{Title}{Subtitle text}` — custom macro with gradient background
- QMD: `# Section Title` + subtitle paragraph on same slide
- **Status:** PASS — SCSS `.level1` rule applies centered gradient layout, matching Beamer visual. Subtitle text faithfully reproduced.

---

### "The Limits of Classical Forecasting"
- Left column bullet list: PASS — 5 bullets match exactly
- `warningbox` content: PASS — text matches, `.warningbox` class applied
- Socratic footnote: PASS — rendered as `[*...*]{.neutral .smaller}`
- **Status:** PASS

---

### "Four Gaps ML Fills"
- Table (4 rows): PASS — all rows and cell text match
- `keybox` content: PASS — text matches, `.keybox` class applied
- Citation `[@Hastie2009]`: PASS
- **Status:** PASS

---

### "Evidence: The M4 Competition"
- Table (5 rows, sMAPE values): PASS — values match current Beamer (11.374, 11.551, 11.720 — already corrected from earlier proofreading)
- `examplebox` with title "Business context": PASS — `.examplebox` + `.examplebox-title` applied
- **Status:** PASS

---

### "MSE Decomposition"
- `definitionbox` with title "Bias-Variance Decomposition": PASS
- Math equation:
  - Beamer: `\MSE(\hat{f}(x_0)) = \bigl(\operatorname{Bias}[\hat{f}(x_0)]\bigr)^2 + \Var[\hat{f}(x_0)] + \sigma^2`
  - QMD: `$$\text{MSE}(\hat{f}(x_0)) = \bigl(\text{Bias}[\hat{f}(x_0)]\bigr)^2 + \text{Var}[\hat{f}(x_0)] + \sigma^2$$`
  - **MINOR:** Beamer uses `\MSE` and `\Var` macros (defined in `header.tex`). QMD uses `\text{MSE}` and `\text{Var}`. These render identically in the browser via MathJax — notation fidelity is preserved in output, though QMD cannot use the custom macros. Acceptable.
- Citation `[[@Hastie2009]]` inside box: PASS
- Body text: PASS
- **Status:** PASS

---

### "MSE Decomposition: Each Term"
- Left column 3 bullet items with sub-bullets: PASS — content matches
- `keybox` "Two levers you control": PASS
  - Beamer uses `\hspace{0.5em}` for indentation; QMD uses `&nbsp;&nbsp;` — acceptable HTML equivalent
- `$\text{Bias}^2$`, `$\text{Var}$` notation: consistent with QMD convention
- **Status:** PASS

---

### "Bias and Variance in Plain Language"
- `examplebox` "High bias — underfitting": PASS
- `warningbox` "High variance — overfitting": PASS
- Closing text about tradeoff: PASS
- **Status:** PASS

---

### "The Complexity Curve"
- Beamer: TikZ `axis` environment with three curves (train error, test error, irreducible floor), zone labels, optimal marker, x-axis tick labels (AR(1), Ridge, RF, Deep NN)
- QMD: Custom inline SVG (raw HTML block) reproducing the same diagram
- **MAJOR:** The SVG test error curve does not achieve a visible U-shape minimum — it continues decreasing into the right side of the chart. The polyline endpoint at x=640,y=275 exits the plot boundary below the x-axis gridline. In the Beamer version, the U-shape clearly rises on the right. Students looking at the Quarto version will not see the "high variance" zone rising upward on the right side as they should.
  - Beamer formula: `{0.5*exp(-0.40*x) + 0.07 + 0.032*(x - 3.5)^2}` — clearly U-shaped with minimum at x=3.5
  - SVG path: `points="60,130 120,150 180,172 240,193 270,200 300,203 360,210 420,220 480,234 540,250 600,265 640,275"` — monotone decreasing all the way; the curve does not turn back up
- **MAJOR:** The SVG plot does not show "High bias" and "High variance" zone labels clearly distinguished — both are colored the same gray (#525252) whereas Beamer uses `\textbf{}` on both. The styling is acceptable but the label at x=580,y=80 ("High variance") is too close to the edge and may be clipped.
- **Status:** FAIL — test error U-shape is broken (monotone decreasing instead of U-shaped). This is a content-level error, not cosmetic.

---

### "Bias-Variance in the Forecasting Setting"
- Table (5 rows): PASS — content matches
- `keybox` "For short series": PASS
- Footnote about LASSO: PASS
- **Status:** PASS

---

### "The Three-Way Split"
- Beamer: TikZ diagram showing Train/Validation/Test bands with time arrow and purpose labels
- QMD: Inline SVG reproducing the same layout
- SVG colors match SCSS palette: `#B8D4EF` (lightblue), `#D4EDDA` (lightgreen), `#FDECEA` (lightred) — PASS
- Time arrow with labeled endpoints (1, T): PASS
- Purpose labels (Fit model parameters, Tune hyper-parameters, Final honest evaluation): PASS
- Two-column text with `warningbox` "time capsule": PASS
- **Status:** PASS

---

### "Data Leakage: Definition and Examples"
- `definitionbox` "Data Leakage": PASS
- Left column (Feature leakage, Temporal leakage bullets): PASS
- Right column `warningbox` + Socratic footnote: PASS
- **MINOR:** Beamer uses `i.i.d.\ data` (escaped space after period). QMD uses `i.i.d. data` (no escaped space). Renders identically in HTML — no issue.
- **Status:** PASS

---

### "Time-Series Rules for Train/Val/Test"
- 5-item numbered list: PASS — all rules match exactly
- `keybox` with code reference: PASS
- `train_test_split(shuffle=False)` and `TimeSeriesSplit` inline code: PASS
- **Status:** PASS

---

### "Why k-fold CV is Wrong for Time Series"
- Beamer: TikZ diagram showing 5-fold shuffled CV with non-chronological red test blocks
- QMD: Inline SVG showing 5 folds with randomly placed red test rectangles
- **MINOR:** The Beamer diagram uses a `\foreach` loop to place test blocks at positions (3-5, 1-3, 6-8, 8-10, 4-6). The QMD SVG places them at different relative positions. The visual intent is conveyed — random placement is random — but the exact fold patterns differ. This is acceptable.
- Right column failure modes bullets (3 items): PASS
- `warningbox` with `@Bergmeir2018` citation: PASS
- `[Wrong for time series:]{.negative}` annotation: PASS — uses `.negative` class correctly
- **Status:** PASS (minor visual difference acceptable)

---

### "Walk-Forward CV and TimeSeriesSplit"
- Beamer: TikZ diagram showing 5-fold expanding-window CV (F1–F5, growing blue train + fixed green val)
- QMD: Inline SVG showing same expanding-window pattern
- SVG fold dimensions: F1 train=140px, F2=180px, F3=220px, F4=260px, F5=300px — each grows by 40px, matching expanding-window concept. PASS
- Python code block: PASS — identical code rendered as fenced code block
- `keybox` about `gap` parameter: PASS
- Citation `[@Arlot2010]`: PASS
- **Status:** PASS

---

### "CV in Practice: Hyperparameter Tuning"
- 5-step numbered list: PASS — all steps match
- "Step 4 is critical" emphasis: PASS
- `examplebox` "LASSO on RSXFS": PASS
  - All RMSE values match current Beamer (1,780 optimal, 1,890 overfit, 2,140 underfit, 1,810 test) — consistent with proofreading fix of Issue 9
- **Status:** PASS

---

### "Ridge, LASSO, and Elastic Net"
- `definitionbox` "Penalized Regression": PASS
- Display equation with `\hat{\beta} = \arg\min_\beta...`:
  - Beamer uses `\bhat`; QMD uses `\hat{\beta}` — renders identically in HTML. Acceptable.
- Ridge/LASSO/EN penalty definitions on one line: PASS
- Citations `[@Tibshirani1996]`, `[@ZouHastie2005]`, `[@Hastie2009]`: PASS
- Bullet list (3 items) + right-column neutral text: PASS
- Note about EN `alpha` vs ETS `alpha`: PASS
- **Status:** PASS

---

### "Shrinkage as Complexity Control"
- Beamer: TikZ axis with 4 Ridge curves (smooth decay, blue solid) and 2 LASSO paths (reaching 0 at finite lambda, red dashed)
- QMD: Inline SVG reproducing same
- SVG Ridge paths (4 polylines, blue solid): PASS — converge toward y=108 (β=0)
- SVG LASSO paths (2 polylines, red dashed): PASS — reach y=108 at finite lambda
- Axis labels (log10(λ) x-axis, coefficient y-axis): PASS
- "Ridge" and "LASSO" labels inside plot: PASS
- `keybox` content: PASS
- Footnote about illustrative paths: PASS
- **Status:** PASS

---

### "From Time Series to Feature Matrix"
- Opening text: PASS
- Feature table (5 rows): PASS — all formulas and business meanings match
  - Beamer: `$\operatorname{std}(y_{t-w:t-1})$`; QMD: `$\text{std}(y_{t-w:t-1})$` — equivalent in MathJax
- `warningbox` about leakage: PASS
- Footnote about L11: PASS
- **Status:** PASS

---

### "Features + Leakage Prevention in Python"
- Left column Python code block: PASS — identical code
- Right column bullet annotations (3 items): PASS
- `keybox` about sklearn Pipeline: PASS
- **Status:** PASS

---

### "The End-to-End ML Forecasting Pipeline"
- Beamer: TikZ diagram with 6 blue rounded-rectangle boxes connected by arrows, with notes below each box
- QMD: Inline SVG with 6 matching blue boxes, arrows, and sub-labels
- All 6 box labels match: Raw series, Feature matrix, Split Tr/Va/Te, CV + model fit, Evaluate on test, Deploy + monitor. PASS
- All 6 note pairs match: RSXFS/FRED, lags/rolling/stats/calendar, chronological/gap=H, TimeSeriesSplit/Ridge/LASSO/RF, RMSE by h/DM test, retrain monthly/monitor drift. PASS
- `keybox` about sklearn.Pipeline: PASS
- Citation `[@James2021]`: PASS
- **Status:** PASS

---

### "Key Takeaways and the Road Ahead"
- `keybox` with 5-item numbered list: PASS — all 5 takeaways match
- Right column roadmap table (L08-L12): PASS
- Lab 7 footnote: PASS
- **Status:** PASS

---

### References slide
- Beamer: `\printbibliography[heading=none]`
- QMD: `## References {.smaller}` with `{#refs}` div
- **Status:** PASS — standard Quarto bibliography rendering

---

## Issue Summary

### MAJOR Issues (blocks approval)

**M1 — Complexity Curve SVG: Test error U-shape broken**
- Location: "The Complexity Curve" slide, SVG polyline for test error
- Problem: The SVG test error curve is monotone decreasing (enters bottom-right of chart) rather than U-shaped. The critical visual teaching point — that test error rises in the high-variance regime — is absent.
- Beamer: `{0.5*exp(-0.40*x) + 0.07 + 0.032*(x - 3.5)^2}` — parabolic term creates U-shape, minimum at x=3.5
- QMD SVG: `points="60,130 120,150 180,172 240,193 270,200 300,203 360,210 420,220 480,234 540,250 600,265 640,275"` — continuously falling y-coordinates
- Fix needed: Correct the SVG polyline so that test error turns back upward after x≈270px, matching the U-shape. Also: the last point (640,275) exits the chart below the x-axis (which is at y=260); clamp to y=260 or trim.

### MINOR Issues (should fix)

**m1 — Complexity Curve SVG: "High variance" label potentially clipped**
- Location: Same slide, SVG `<text x="580" y="80">`
- The label sits near the right edge of the 720px-wide viewBox at x=580. If the slide has any right padding, the text may be partially hidden.
- Fix: Move to x="560" or smaller.

**m2 — Complexity Curve SVG: Last test-error point exits y-axis bounds**
- Location: Same slide, last polyline point at y=275 vs x-axis at y=260
- Fix: Trim final point or clamp to y=260 to avoid drawing below the axis line.

**m3 — Notation: `\text{MSE}` vs `\MSE` macro (cosmetic)**
- Location: MSE Decomposition slide
- As noted: renders identically in MathJax. No fix required unless macro consistency is desired.

---

## Hard Gate Re-Assessment

| Gate | Status |
|------|--------|
| Content Parity | PASS |
| Notation Fidelity | PASS |
| Visual Regression | FAIL (M1: test error U-shape broken) |
| Slide Centering | PASS |
| Overflow | UNVERIFIED |
| Plot Quality | FAIL (M1 same) |

**Overall: NOT APPROVED — Round 1**
One MAJOR issue requires fix before approval: the Complexity Curve test error curve must be corrected to show a U-shape. All other slides pass parity checks.

---

## Recommended Fix

In `Quarto/Lecture07_MLIntro.qmd`, on the "The Complexity Curve" slide, replace the test error polyline:

**Current (broken — monotone decreasing):**
```
points="60,130 120,150 180,172 240,193 270,200 300,203 360,210 420,220 480,234 540,250 600,265 640,275"
```

**Replacement (U-shaped — rises in high-variance zone):**
```
points="60,130 120,150 180,172 240,193 270,200 300,203 360,197 420,188 480,178 540,165 600,150 640,140"
```

This ensures:
- Minimum at x≈270 (matching Beamer's optimal at x=3.5)
- Rising right arm creates visible high-variance zone
- No point exits the chart boundary
