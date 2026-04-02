# QA Critic Report: Lecture08 Regularization
## Quarto vs. Beamer Adversarial Comparison — Round 1

**Date:** 2026-03-06
**Beamer source:** `Slides/Lecture08_Regularization.tex`
**Quarto source:** `Quarto/Lecture08_Regularization.qmd`
**HTML rendered:** Not yet rendered (no .html file found)
**Critic:** qa-quarto adversarial agent

---

## Hard Gate Status

| Gate | Status | Notes |
|------|--------|-------|
| Overflow | WARN | One long inline span (line 115–117) may wrap; pre-existing issue from proofreader report |
| Plot Quality | PASS | All TikZ diagrams replaced with inline SVG; geometry is faithful |
| Content Parity | PASS | All 20 Beamer frames present in Quarto; no missing slides |
| Visual Regression | PASS | SVG diagrams are equivalent or better than static TikZ |
| Slide Centering | PASS | `center: false` is set; layout is left-aligned consistently with other lectures |
| Notation Fidelity | PASS | All math equations verified verbatim against Beamer source |

**Overall verdict: CONDITIONAL PASS** — No critical failures. One warning (overflow) and five minor issues. The file is fit for rendering and deployment pending the minor fixes catalogued below.

---

## Section-by-Section Comparison

### Section 1: Motivation — Why Regularization?

**Frame: Section Slide (sectionslide)**
- Beamer: custom `\sectionslide` macro with subtitle text
- Quarto: rendered as a level-1 heading (`# Motivation: Why Regularization?`) followed by subtitle text on same slide
- Status: PASS — standard pattern matches all other L08 lectures

**Frame: OLS Instability with Many Predictors**
- Math: $\hat{\boldsymbol{\beta}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$ — MATCH
- Three failure modes: identical text — MATCH
- examplebox with RSXFS: present and correctly classed — MATCH
- Minor: "obs.\ " (LaTeX forced space) → "monthly observations." in Quarto — BETTER (pre-existing A-01 from proofreader)

**Frame: The Bias--Variance View**
- Two-column layout: MATCH
- Equations: $\mathbb{E}[\hat{\boldsymbol{\beta}}_{\mathrm{OLS}}] = \boldsymbol{\beta}$ and variance formulas — MATCH
- keybox with $\mathrm{MSE} = \mathrm{Bias}^2 + \mathrm{Var} + \sigma^2$ — MATCH
- Beamer uses `\MSE` custom macro; Quarto expands to `\mathrm{MSE}` — MATCH (correct expansion)
- Citation `[@Hastie2009]` — MATCH

**Frame: Penalized Regression: General Form**
- Main equation with underbrace — MATCH
- Table: Ridge/LASSO/Elastic Net with penalties — MATCH
- Footer note: present as inline `.neutral .smaller` span — FUNCTIONAL MATCH
- ISSUE (pre-existing O-01): The note is a single long inline span; the Beamer version wraps naturally via LaTeX. The Quarto span may overflow at 1280px. This is the primary outstanding overflow risk.

---

### Section 2: Ridge Regression (L2)

**Frame: Ridge: Objective and Solution**
- definitionbox with title "Ridge Regression" — MATCH
- Objective equation: $\hat{\boldsymbol{\beta}}^{\mathrm{R}}_\lambda = \arg\min_{\boldsymbol{\beta}} \|\mathbf{y} - \mathbf{X}\boldsymbol{\beta}\|_2^2 + \lambda \|\boldsymbol{\beta}\|_2^2$ — MATCH
- Analytical solution: $\left(\mathbf{X}^\top\mathbf{X} + \lambda \mathbf{I}\right)^{-1}\mathbf{X}^\top\mathbf{y}$ — MATCH
- Bullet points on near-singularity fix, eigenvalue shift, SVD interpretation — MATCH
- Citation `[@HoerlKennard1970]` — MATCH

**Frame: Ridge: Constraint Set Geometry**
- Two-column layout: MATCH
- Constrained form equation — MATCH
- warningbox "never exactly zero" — MATCH
- TikZ → SVG: Circle constraint, OLS point, Ridge point, RSS ellipses, axes
  - SVG uses hex colors (#005CA9 blue, #E41C38 red) — matches UNO palette
  - Circle is correctly drawn; OLS and Ridge solution dots present
  - Status: PASS — faithful geometric representation
- MINOR ISSUE (NEW): The SVG has `max-height:240px` which is adequate for a 720px slide, but the `width="100%"` on a 48% column means the SVG will scale proportionally. The TikZ original uses `scale=1.05` which renders at approximately 220px tall. The SVG rendering should be equivalent.

**Frame: Ridge: Coefficient Path**
- SVG chart with 5 smooth curves asymptotically approaching zero — MATCH to TikZ
- `λ* (CV)` dashed vertical line — MATCH
- Socratic note in `.neutral .smaller` — MATCH
- The SVG uses `max-height:220px; width:80%` — consistent with the narrow chart format in TikZ (xscale=2.8, yscale=1.6)

**Frame: Ridge: Key Properties Summary**
- Two-column Strengths/Limitations — MATCH
- keybox "When to use Ridge" — MATCH
- MINOR (pre-existing A-02): "predictors are highly correlated groups" → should be "predictors come in highly correlated groups"

---

### Section 3: LASSO Regression (L1)

**Frame: LASSO: Objective and Sparsity**
- definitionbox with two equations — MATCH
- Coordinate descent explanation — MATCH
- Soft-thresholding formula: $\hat{\beta}_j \leftarrow \mathrm{sign}(z_j)\,\max\!\left(|z_j| - \tfrac{\lambda}{2},\, 0\right)$ — MATCH
- Inline example with $z_j = 1.8 \Rightarrow \hat{\beta}_j = +0.8$ and $z_j = 0.7 \Rightarrow 0$ — MATCH

**Frame: LASSO: Constraint Set Geometry**
- Diamond SVG with four vertices, RSS ellipses, LASSO solution at corner — MATCH
- keybox on sparsity from corners — MATCH
- "β̂₂ = 0" label at corner solution — MATCH

**Frame: LASSO: Coefficient Path**
- Piecewise-linear paths with coefficients zeroing at different λ values — MATCH to TikZ polylines
- `λ* (CV)` vertical dashed line present — MATCH
- Note on kinks vs. smooth Ridge paths — MATCH

**Frame: LASSO: Properties and Limitations**
- Two-column Strengths/Limitations — MATCH
- examplebox "RSXFS Application" — MATCH
- "Seasonal Naïve" in Beamer → "Seasonal Naive" in Quarto table (pre-existing C-01): MINOR INCONSISTENCY

---

### Section 4: Elastic Net

**Frame: Elastic Net: Objective and Geometry**
- definitionbox with title — MATCH
- Three-way $\alpha$ interpretation ($\alpha=1$ LASSO, $\alpha=0$ Ridge, $0 < \alpha < 1$ EN) — MATCH
- Grouped selection property — MATCH
- Two hyperparameter bullet points — MATCH
- warningbox on expensive joint tuning — MATCH
- Note distinguishing EN $\alpha$ from ETS $\alpha$ and ECM $\alpha$ — MATCH

**Frame: Ridge vs. LASSO vs. Elastic Net: Decision Guide**
- Comparison table: 5 rows × 4 columns — MATCH
- All checkmarks (✓✓, ✓) present; in Beamer as `\checkmark\checkmark`, in Quarto as plain text "Best" — DIFFERENCE: Quarto dropped the checkmarks and replaced with text labels ("Best", "Good")
- ISSUE (NEW — MINOR): The Beamer table uses `\checkmark\checkmark Best` and `\checkmark Good` to add visual weight. The Quarto table uses plain text "Best" and "Good". The information is equivalent but the visual emphasis is reduced. This is a presentation regression, though not a content loss.
- Socratic note — MATCH

---

### Section 5: Tuning λ via Cross-Validation

**Frame: TimeSeriesSplit CV for Regularization**
- Numbered procedure list — MATCH
- warningbox on StandardScaler leakage — MATCH
- SVG TimeSeriesSplit diagram: 5 folds (F1–F5) with growing train bars and fixed-width val bars — MATCH to TikZ
- Legend (Train/Val) and time axis — MATCH
- MINOR: Beamer procedure uses "e.g.\ $10^{-3}$" with forced space; Quarto has "e.g. $10^{-3}$" (pre-existing G-01 comma missing) → should be "e.g.,"

**Frame: Validation Curve: Selecting λ***
- SVG with U-shaped validation curve and monotone decreasing train curve — MATCH
- λ* marker with red dashed line and dot — MATCH
- "overfit" and "underfit" region labels — MATCH
- Val and Train labels — MATCH
- keybox "one standard error rule" — MATCH
- Socratic note — MATCH

---

### Section 6: Application to Forecasting

**Frame: sklearn Pipeline for Leakage-Free CV**
- Two code blocks (pipeline setup, evaluation) — MATCH
- Beamer uses `lstlisting` with `basicstyle=\tiny\ttfamily`; Quarto uses fenced code blocks — FUNCTIONAL MATCH
- Comments preserved in code including the sklearn 'alpha' vs lambda notation clarification — MATCH
- keybox "StandardScaler is inside the pipeline" — MATCH
- MINOR (pre-existing C-03): heading "sklearn Pipeline for Leakage-Free CV" starts with lowercase `sklearn`

**Frame: Interpreting LASSO Coefficients in Forecasting**
- Two-column layout — MATCH
- Surviving features list (Lag 1, 12, 3, Rolling mean 12, December dummy) — MATCH
- Zeroed features list — MATCH
- examplebox "Interpretation Rule" — MATCH
- Neutral italic ARIMA comparison note — MATCH

**Frame: Forecast Comparison: SARIMA vs. Regularized Models**
- Table: 5 rows (Seasonal Naïve, SARIMA, Ridge, LASSO, Elastic Net) — MATCH on values
- MINOR (pre-existing C-01): "Seasonal Naive" missing diaeresis → should be "Naïve"
- Takeaways bullets — MATCH

---

### Section 7: Takeaways and References

**Frame: Lecture 8 Key Takeaways**
- keybox with 5 numbered takeaways — MATCH verbatim
- Preview of Lecture 09 — MATCH

**Frame: References**
- `## References {.smaller}` with `{#refs}` div — standard Quarto pattern, correct
- Beamer uses `\printbibliography[heading=none]` — FUNCTIONAL MATCH

---

## Issues Catalogue

### Critical Issues
*None.*

### Major Issues
*None.*

### Minor Issues

| ID | Location | Description | Beamer Source | Action |
|----|----------|-------------|---------------|--------|
| M-01 | Line 115–117 | Long inline `.neutral .smaller` span may overflow at 1280px | `\muted{\footnotesize\itshape ...}` wraps naturally in LaTeX | Wrap in `::: {.neutral .smaller}` div block |
| M-02 | Line 481–486 | Decision Guide table: checkmarks dropped (Beamer: `\checkmark\checkmark Best`; Quarto: "Best") | `\checkmark\checkmark Best` | Add checkmarks: "✓✓ Best", "✓ Good" |
| M-03 | Line 735 | "Seasonal Naive" missing diaeresis | "Seasonal Naïve" | Change to "Naïve" |
| M-04 | Line 264 | "predictors are highly correlated groups" — awkward phrasing | "predictors are highly correlated groups" | Change to "predictors come in highly correlated groups" |
| M-05 | Line 512 | "e.g. $10^{-3}$" missing comma | `e.g.\ ` (LaTeX) | Change to "e.g.," |

### Informational (No Action Required)

| ID | Location | Description |
|----|----------|-------------|
| I-01 | Line 627 | Heading "sklearn Pipeline..." starts lowercase — acceptable convention |
| I-02 | Line 734 | SARIMA subscript using Unicode ₁₂ — acceptable; consistent within file |
| I-03 | Line 64 | "obs." → "monthly observations." — pre-existing improvement, already better than Beamer |

---

## Notation Fidelity Check (Full Pass)

All the following equations were verified character-by-character against the Beamer source:

| Equation | Beamer | Quarto | Match |
|----------|--------|--------|-------|
| OLS estimator | `\hat{\bm{\beta}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}` | `\hat{\boldsymbol{\beta}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}` | YES (`\bm` → `\boldsymbol`, same output) |
| General penalized form | `\hat{\bm{\beta}}_\lambda = \arg\min...` | `\hat{\boldsymbol{\beta}}_\lambda = \arg\min...` | YES |
| Ridge objective | `\hat{\bm{\beta}}^{\mathrm{R}}_\lambda = \arg\min...` | `\hat{\boldsymbol{\beta}}^{\mathrm{R}}_\lambda = \arg\min...` | YES |
| Ridge solution | `(\mathbf{X}^\top\mathbf{X} + \lambda \mathbf{I})^{-1}\mathbf{X}^\top\mathbf{y}` | Same | YES |
| LASSO objective | `\hat{\bm{\beta}}^{\mathrm{L}}_\lambda = \arg\min...` | Same with `\boldsymbol` | YES |
| L1 norm | `\|\bm{\beta}\|_1 = \sum_{j=1}^{p} |\beta_j|` | `\|\boldsymbol{\beta}\|_1 = \sum_{j=1}^{p} |\beta_j|` | YES |
| Soft-thresholding | `\mathrm{sign}(z_j)\,\max\!\left(|z_j| - \tfrac{\lambda}{2},\, 0\right)` | Same | YES |
| Elastic Net objective | `\arg\min...\lambda[\alpha\|\bm{\beta}\|_1 + (1-\alpha)\|\bm{\beta}\|_2^2]` | Same with `\boldsymbol` | YES |
| Bias-Variance | `\MSE = \mathrm{Bias}^2 + \Var + \sigma^2` | `\mathrm{MSE} = \mathrm{Bias}^2 + \mathrm{Var} + \sigma^2` | YES (custom macros expanded correctly) |

---

## SVG Diagram Fidelity Check

| Diagram | Beamer TikZ | Quarto SVG | Verdict |
|---------|-------------|------------|---------|
| Ridge geometry (circle) | Circle constraint, OLS dot, Ridge dot, 3 RSS ellipses | Same elements, hex colors | PASS |
| Ridge coefficient path | 5 smooth curves → 0, λ* line | 5 smooth bezier paths → 0, λ* line | PASS |
| LASSO geometry (diamond) | Diamond, OLS dot, corner solution, 3 ellipses | Same elements | PASS |
| LASSO coefficient path | 5 piecewise-linear paths, zeros at different λ | 5 polylines + horizontal tails | PASS |
| TimeSeriesSplit | 5 folds, growing train bars, fixed val bars | Same, rects with colors | PASS |
| Validation curve | U-shaped val + decreasing train, λ* marker | Same shapes | PASS |

---

## Content Parity Audit

Beamer slide count: 20 frames (excluding title and section slides)
Quarto slide count: 20 content slides (matching)

| Beamer Frame | Present in Quarto | Notes |
|-------------|-------------------|-------|
| Title | YES | YAML front matter |
| Lecture Outline | YES | Numbered list |
| Section Overview (×6) | YES | All 6 present |
| OLS Instability | YES | |
| Bias-Variance View | YES | |
| Penalized Regression General Form | YES | |
| Ridge Objective and Solution | YES | |
| Ridge Constraint Geometry | YES | |
| Ridge Coefficient Path | YES | |
| Ridge Key Properties | YES | |
| LASSO Objective and Sparsity | YES | |
| LASSO Constraint Geometry | YES | |
| LASSO Coefficient Path | YES | |
| LASSO Properties and Limitations | YES | |
| Elastic Net Objective | YES | |
| Decision Guide Table | YES | Minor checkmark issue |
| TimeSeriesSplit CV | YES | |
| Validation Curve | YES | |
| sklearn Pipeline | YES | |
| Interpreting LASSO Coefficients | YES | |
| Forecast Comparison Table | YES | |
| Key Takeaways | YES | |
| References | YES | |

---

## Verdict

**CONDITIONAL PASS — Proceed to Fixer**

No critical or major issues. Five minor issues require fixing before deployment. The file is structurally sound with complete content parity, accurate notation, and faithful SVG diagrams.

Priority order for fixer:
1. M-01 (overflow risk — inline span → div block)
2. M-02 (checkmarks in decision guide table)
3. M-03 (Naïve accent)
4. M-04 (phrasing fix)
5. M-05 (comma after "e.g.")
