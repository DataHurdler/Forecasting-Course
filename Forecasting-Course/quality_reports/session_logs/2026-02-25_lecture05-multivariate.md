# Session Log: Lecture 05 — Multivariate Methods
**Date:** 2026-02-25
**Files:** `Slides/Lecture05_Multivariate.tex`, `scripts/Lecture05_Multivariate.ipynb`
**Status:** Complete — 22 pages, 0 errors, 0 overflows

---

## Goal
Create Lecture 05 covering Multivariate Methods (VAR models, Granger causality,
ARIMAX, cointegration and ECM), following the established workflow:
plan → implement → compile → dual quality review → fix all issues → clean recompile.

---

## Compilation History

| Pass | Pages | Errors | Overflows |
|------|-------|--------|-----------|
| Initial 3-pass | 22 | 0 | 1 (Granger slide, vbox 1.15pt) |
| After initial fix | 22 | 0 | 0 |
| After quality fixes | 22 | 0 | 1 (IRF slide, vbox 1.53pt) |
| Final | 22 | 0 | 0 |

---

## Proofreader Findings and Fixes

### CRITICAL (2 fixed)
1. **BIC notation collision** — `p\ln T` where `p` = lag order (conflicts with
   L02 convention `(p+2)\ln T` where `p+2` = parameter count). Fixed: renamed
   penalty term to `\kappa\ln T` with inline note `\kappa = k^2p+k \text{ parameters}`.
2. **`\parencite` for in-sentence attribution** — Spurious Regression slide used
   `\parencite{GrangerNewbold1974}` inline. Fixed: changed to `\textcite{GrangerNewbold1974}`.

### MAJOR (6 fixed)
3. **`\textcite` inside frame title** — Granger Causality title had `\textcite{Granger1969}`;
   fragile in Beamer navigation. Fixed: changed to `\parencite{Granger1969}`.
4. **`\textcite` inside definitionbox title** — VAR(p) Model definition used
   `\textcite{Sims1980}`; fragile. Fixed: changed to `\parencite{Sims1980}`.
5. **"PIs" undefined abbreviation** — Fixed: expanded to "prediction intervals (PIs)"
   on first use in ARIMAX slide.
6. **`(\phi,\theta)` undefined locally** — ARIMAX bullet introduced the notation
   without a descriptor. Fixed: added "the ARIMA parameters $(\phi,\theta)$".
7. **Three colored boxes on Granger slide** (definitionbox + examplebox + warningbox).
   Fixed: converted examplebox to plain italic text `\textit{Lab 5 example:}`.
8. **FEVD unexpanded in table** — Fixed: added `$^\dagger$` marker and a muted
   footnote "FEVD = forecast error variance decomposition."

### MINOR (4 fixed)
9. **$a_{12,\ell}$ without range** — Added `($\ell = 1,\ldots,p$)` in H₀ statement.
10. **"ADF" unexpanded in cointegration section** — Fixed: expanded to
    "Augmented Dickey-Fuller (ADF)" in the Engle-Granger keybox.
11. **Missing Engle-Granger citation** — Added `\parencite[][Ch.~19]{Hamilton1994}`.
12. **CCF not defined on first substantive use** — The Distributed Lag keybox
    mentioned CCF; expanded to formal definition:
    $r_k = \mathrm{Corr}(x_t, y_{t+k})$, with significance threshold $\pm 1.96/\sqrt{T}$.

---

## Pedagogy Reviewer Findings and Fixes

### CRITICAL (1 fixed)
C1. **BIC notation inconsistency** (same as proofreader CRITICAL #1 — resolved above).

### HIGH (4 fixed)
H1. **Missing cointegration visual** — Plan specified a two-panel TikZ; not in
    initial draft. Fixed: replaced Spurious Regression slide content with two
    stacked pgfplots panels (height=1.6cm each):
    - Left panel (blue vs. red): two independent RWs diverging
    - Right panel (blue vs. red): two cointegrated series tracking together
    This required restructuring the slide (removing examplebox, reorganizing columns).
H2. **No ECM worked example** — Fixed: added muted footnote at bottom of ECM slide:
    "Example: α̂=−0.3, y_{t−1}−β̂x_{t−1}=+2.0 ⇒ ECM contributes −0.3×2.0=−0.6."
H3. **Three-box violation on Granger slide** — Fixed: see MAJOR #7 above.
H4. **CCF not defined or visualized** — Fixed: see MINOR #12 above (formal definition
    in the keybox on the Distributed Lag slide).

### MEDIUM (3 fixed)
M1. **IRF Cholesky scoping** — "ordering matters" was unspecific. Fixed: added
    "place the most exogenous variable first."
M2. **ECM parameters introduced simultaneously** — definitionbox listed α, γ₁, δ₁
    without glosses. Fixed: added "γ₁: own short-run lag; δ₁: cross short-run lag."
M3. **IRF simulation formula not linked to VAR** — muted note lacked connection
    to VAR coefficient. Fixed: added "($\rho^h$, here $\rho=0.85$)."

---

## Overflow Fixes

1. **Granger Causality slide (initial 1.15pt):** Condensed Granger definitionbox
   from 2-line definition to 1-line definition; reduced enumerate from 3 items
   to 2 items. Fixed to 0pt before quality reviews.
2. **IRF slide (1.53pt after quality fixes):** Adding the 3-line Cholesky note
   (vs. original 2-line) caused 1.53pt overflow. Fixed: removed `\vspace{0.1cm}`
   between definitionbox and Cholesky paragraph.

---

## Design Decisions

- **Cointegration TikZ:** Two stacked panels in a column (height=1.6cm each) keep
  the visual compact and allow the Engle-Granger keybox to occupy the right column.
  Coordinates are stylized (not computed from a real DGP), consistent with the
  ACF/PACF approach in Lecture 04.
- **ECM worked example:** Compact muted footnote instead of examplebox to avoid
  a third box on an already two-box slide. The numbers (α=−0.3, deviation=+2.0,
  ECM contribution=−0.6) are pedagogically clean.
- **BIC κ notation:** Introduced κ (Greek kappa) as a bridge between the scalar
  lag order p and the full parameter count k²p+k. This makes the formula both
  correct and interpretable.
- **FEVD footnote:** Single muted line after `\end{center}` (before the warningbox)
  expands the abbreviation without cluttering the table.
- **CCF formal definition:** Added in the Distributed Lag keybox rather than the
  Toolkit overview slide, because that is where CCF is used as a practical tool.

---

## Final Slide Count by Section

| Section | Frames |
|---------|--------|
| Title + Outline | 2 |
| Beyond Univariate Forecasting | 3 (sectionslide + 2) |
| Vector Autoregression (VAR) | 6 (sectionslide + 5) |
| ARIMAX Models | 5 (sectionslide + 4) |
| Cointegration and Error Correction | 3 (sectionslide + 2) |
| Key Takeaways and Roadmap | 3 (2 + References) |
| **Total** | **22** |

---

## Citations Used

| Key | Paper |
|-----|-------|
| `Granger1969` | Granger (1969), Econometrica 37(3):424–438 |
| `Sims1980` | Sims (1980), Econometrica 48(1):1–48 |
| `GrangerNewbold1974` | Granger & Newbold (1974), JoE 2(2):111–120 |
| `Hamilton1994` | Hamilton (1994), Time Series Analysis, Ch. 19 |
| `Diebold1995` | Diebold & Mariano (1995), JBES 13(3):253–263 (in What's Next) |

---

## Next Session

Lecture 06: Forecast Evaluation — walk-forward validation, Diebold-Mariano test,
forecast combination.
