# Plan: Lecture 02 — Regression-Based Forecasting
**Status:** APPROVED (continuing series)
**Date:** 2026-02-24

## Scope
- `Slides/Lecture02_Regression.tex` — full first draft, ~32–35 slides
- `scripts/Lecture02_Regression.ipynb` — 9-section lab notebook

## Slide Structure (~33 slides)

### Section 1: From Benchmarks to Regression (3 slides)
- sectionslide
- Limits of benchmark models
- What regression adds: leading indicators, structural relationships

### Section 2: The Regression Model for Forecasting (5 slides)
- sectionslide
- General setup: y_t = x_t'β + ε_t
- OLS estimation: β̂ = (X'X)⁻¹X'y (Gauss-Markov)
- Predictor types: deterministic, lagged, external
- The forecast formula: ŷ_{T+h|T} = x_{T+h}'β̂

### Section 3: Trend and Seasonality as Regressors (5 slides)
- sectionslide
- Linear trend: y_t = β₀ + β₁t + ε_t
- Seasonal dummy variables (dummy trap warning)
- Combined trend + seasonality
- Example: US retail sales decomposition

### Section 4: Prediction Intervals (3 slides)
- Point vs. interval forecast
- 95% PI formula and assumptions
- What happens when assumptions are violated

### Section 5: Autoregressive Models (5 slides)
- sectionslide
- AR(1): y_t = φ₀ + φ₁y_{t-1} + ε_t — regression with lagged y
- AR(p): lag selection via AIC/BIC
- Recursive multi-step forecast
- Residual ACF diagnostics

### Section 6: Pitfalls (4 slides)
- sectionslide
- Spurious regression (I(1) series)
- Overfitting: many predictors → good in-sample, bad OOS
- The forecasting regressor problem (no contemporaneous X)

### Section 7: Takeaways + Roadmap (2 slides)
- Key takeaways (keybox)
- What's next: Exponential Smoothing

## Lab Notebook Structure (9 sections)
1. Setup (UNO palette, seed, paths)
2. Load FRED RSXFS (same as Lab 01, continuity)
3. Train/test split H=24
4. Model 1: Linear trend regression
5. Model 2: Trend + seasonal dummies
6. Model 3: AR(p) with BIC lag selection
7. Metrics: all models vs. Lab 01 benchmarks
8. Prediction intervals (95% PI for trend model)
9. Residual diagnostics (ACF of residuals)
