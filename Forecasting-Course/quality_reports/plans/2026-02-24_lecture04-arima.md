# Plan: Lecture 04 — Stationarity and ARIMA
**Status:** APPROVED (continuing series)
**Date:** 2026-02-24

## Scope
- `Slides/Lecture04_ARIMA.tex` — full first draft, ~26 slides
- `scripts/Lecture04_ARIMA.ipynb` — 9-section lab notebook

## Slide Structure (~26 slides)

### Section 1: Stationarity (3 slides)
- sectionslide: "All classical forecasting methods implicitly assume stationarity."
- Weak stationarity: constant mean, constant variance, ACF depends only on lag
- Visual: stationary (AR(1), φ=0.7) vs. non-stationary (random walk) — pgfplots

### Section 2: Unit Roots and Differencing (5 slides)
- sectionslide: "A random walk has a unit root — its shocks never die out."
- The unit root: AR(1) with φ₁ = 1 vs. |φ₁| < 1
- ADF test (null = unit root, reject = stationary)
- First difference Δy_t = y_t − y_{t-1} + seasonal differencing
- KPSS as complementary test (null = stationary)

### Section 3: ACF and PACF (4 slides)
- sectionslide: "The ACF is the fingerprint of a time series."
- ACF definition + 95% confidence bounds
- PACF definition
- Pattern recognition table: AR(p) vs. MA(q) vs. ARMA + pgfplots theoretical ACF

### Section 4: The ARIMA Model (5 slides)
- sectionslide: "ARIMA = differencing + ARMA."
- ARMA(p,q): combining AR and MA terms
- ARIMA(p,d,q): applying ARMA to d-th differenced series (backshift notation)
- Box-Jenkins methodology: identify → estimate → diagnose
- Forecasting with ARIMA: recursive multi-step + uncertainty growth

### Section 5: Seasonal ARIMA (3 slides)
- sectionslide: "Retail and economic data show seasonal autocorrelation — ARIMA needs seasonal terms."
- Seasonal differencing + SARIMA(p,d,q)(P,D,Q)[m] notation
- Auto-ARIMA selection (AIC/BIC); example on RSXFS

### Section 6: Takeaways + Roadmap (2 slides)
- Key takeaways (keybox)
- What's next: Forecast Evaluation + Model Comparison (Lecture 5)

## Lab Notebook Structure (9 sections)
1. Setup (UNO palette, seed, paths)
2. Load FRED RSXFS
3. Stationarity tests: ADF + KPSS + interpretation
4. ACF/PACF plots (raw, first-differenced, seasonally differenced)
5. First + seasonal differencing
6. Manual ARIMA: select (p,d,q) from ACF/PACF; fit + residual check
7. Auto-ARIMA (pmdarima auto_arima or SARIMAX grid search)
8. Metrics: ARIMA vs. Lectures 1–3 benchmarks
9. Residual diagnostics (Ljung-Box test + ACF of residuals)

## Bibliography entries to add
- `DickeyFuller1979` — Dickey & Fuller (1979) ADF test
- `Kwiatkowski1992` — KPSS test (Kwiatkowski, Phillips, Schmidt, Shin)
