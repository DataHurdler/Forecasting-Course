# Plan: Lecture 06 — Forecast Evaluation
**Status:** APPROVED (continuing established per-lecture workflow)
**Date:** 2026-02-25

---

## Scope

| Deliverable | File | Action |
|-------------|------|--------|
| Slides | `Slides/Lecture06_Evaluation.tex` | New (~26 slides) |
| Lab notebook | `scripts/Lecture06_Evaluation.ipynb` | New (9 sections) |
| Bibliography | `Bibliography_base.bib` | Add BatesGranger1969, StockWatson2004 |

---

## Slide Structure (~26 slides)

### Title + Outline (2 slides)

### Section 1: The Evaluation Problem (sectionslide + 2 slides)
- S1: The Single-Split Trap + What Good Evaluation Requires (combined)
- S2: The Model Zoo — 5 families, lightweight orientation table

### Section 2: Error Metrics — Decision-Oriented (sectionslide + 4 slides)
- S3: Metrics overview — compact table with formulas + "Use when..." column
- S4: RMSE vs. MAE trade-off — cost structure alignment (pgfplots histogram)
- S5: MAPE pitfalls and MASE
- S6: Horizon profiles — line chart (Naive vs. SARIMA vs. ETS over h=1..12)

### Section 3: Walk-Forward Validation (sectionslide + 4 slides)
- S7: The walk-forward idea — expanding vs. rolling window TikZ diagram
- S8: Rolling vs. Expanding — decision table
- S9: Walk-forward implementation recipe (numbered steps)
- S10: Walk-forward results table (all 5 models, h=1/3/12/MASE)

### Section 4: Diebold-Mariano Test (sectionslide + 3 slides)
- S11: DM test statistic (definitionbox) + motivation
- S12: Interpreting DM — loss differential plot (pgfplots bar chart)
- S13: DM caveats — Clark-West for nested models; decision table

### Section 5: Forecast Combination (sectionslide + 3 slides)
- S14: The combination intuition — BatesGranger1969 result
- S15: Three strategies (equal, RMSE-weighted, OLS) + the equal-weight puzzle
- S16: Combination results table + actionable decision rule

### Section 6: Key Takeaways and Roadmap (2 slides + References)
- S17: Key Takeaways keybox (5 points)
- S18: What's Next — Lecture 7 ML Introduction

---

## New Bibliography Entries

```bibtex
@article{BatesGranger1969,
  author  = {Bates, John M. and Granger, C. W. J.},
  title   = {The Combination of Forecasts},
  journal = {Operational Research Quarterly},
  volume  = {20},
  number  = {4},
  pages   = {451--468},
  year    = {1969}
}

@article{StockWatson2004,
  author  = {Stock, James H. and Watson, Mark W.},
  title   = {Combination Forecasts of Output Growth in a Seven-Country Data Set},
  journal = {Journal of Forecasting},
  volume  = {23},
  number  = {6},
  pages   = {405--430},
  year    = {2004}
}
```

---

## Key Design Choices

- **Metrics:** upgrade from L01 definitions to decision-context framing
- **Walk-forward TikZ:** two stacked panels (expanding vs. rolling) using filled rectangles
- **DM loss differential plot:** ycomb pgfplots chart, 36 origins, simulated
- **Combination puzzle:** equal weights win empirically — teach this counterintuition explicitly
- **No Clark-West derivation:** mention and cite only; focus on "when to use it"
- **Notation:** `d_t` for loss differential (new); `w_k` for combination weight (new)

---

## Verification

1. 3-pass XeLaTeX + BibTeX compile
2. Check log: 0 errors, 0 Overfull vbox
3. Execute notebook end-to-end
