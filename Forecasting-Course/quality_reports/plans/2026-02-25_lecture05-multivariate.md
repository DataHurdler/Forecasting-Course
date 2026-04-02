# Plan: Lecture 05 — Multivariate Methods
**Status:** APPROVED (continuing established per-lecture workflow)
**Date:** 2026-02-25

---

## Scope

| Deliverable | File | Action |
|-------------|------|--------|
| Slides | `Slides/Lecture05_Multivariate.tex` | New (~25 slides) |
| Lab notebook | `scripts/Lecture05_Multivariate.ipynb` | New (9 sections) |

Bibliography: all needed citations already in `Bibliography_base.bib`
(Granger1969, Sims1980, GrangerNewbold1974, Hamilton1994).

---

## Slide Structure (~25 slides)

### Section 1: Beyond Univariate Forecasting (sectionslide + 2 slides)
- S1: The univariate limitation — past of y only; what if other series help?
  Business example: consumer sentiment → retail sales
- S2: The multivariate toolkit overview — VAR vs. ARIMAX vs. cointegration

### Section 2: Vector Autoregression (sectionslide + 5 slides)
- S3: VAR(1) definition — 2-equation system (explicit, not abstract matrix)
- S4: VAR(p) order selection — AIC/BIC, equation-by-equation OLS
- S5: Granger causality — definition, F-test, H₀/H₁, warning on causal interpretation
- S6: Impulse Response Functions — pgfplots IRF visualization (2 series, 12 horizons)
- S7: Forecasting with VAR — recursive h-step formula, parameter count warning

### Section 3: ARIMAX Models (sectionslide + 4 slides)
- S8: Regression with ARIMA errors — model, why OLS fails with autocorrelated residuals
- S9: Dynamic regression — contemporaneous vs. distributed lag effects
- S10: Practical implementation — SARIMAX, differencing rule for I(1) regressors
- S11: VAR vs. ARIMAX comparison — when to use each

### Section 4: Cointegration (sectionslide + 2 slides)
- S12: Spurious regression revisited — connect to GrangerNewbold1974 from L02
- S13: Cointegration and Error Correction — long-run equilibrium, ECM formula

### Section 5: Key Takeaways and Roadmap (2 slides)
- S14: Key Takeaways keybox (5 points)
- S15: What's Next — Lecture 6: Forecast Evaluation (RMSE/MAE/MAPE, DM test, combinations)

---

## Notebook Structure (9 sections)

1. Setup (imports, UNO palette, rcParams, random_state=42)
2. Load FRED data: RSXFS (retail) + UMCSENT (consumer sentiment), fallback to macrodata
3. Exploratory: correlation, cross-correlation function (CCF) plot
4. Unit root tests on both series (ADF + KPSS)
5. Granger causality test (statsmodels grangercausalitytests)
6. VAR(p) fit + BIC order selection + IRF plot
7. ARIMAX: SARIMAX with UMCSENT as exogenous regressor
8. Forecast comparison: ARIMA vs. VAR vs. ARIMAX vs. naive
9. Forecast plot with 95% PI, save to Figures/

---

## Key Design Choices

- **VAR notation:** write out the 2-equation system explicitly (not full matrix form)
  to be accessible to business students; add matrix form as compact muted note
- **Granger causality:** stress that G-causality ≠ structural causality (warningbox)
- **ARIMAX vs. VAR:** ARIMAX when causal direction is clear; VAR when symmetric
- **Cointegration:** conceptual only (2 slides); full treatment is graduate econometrics
- **TikZ visuals:** (1) IRF bar/line plot, (2) cointegration series comparison plot

---

## Verification

1. 3-pass XeLaTeX + BibTeX compile
2. Check log: 0 errors, 0 Overfull vbox
3. Execute notebook end-to-end
