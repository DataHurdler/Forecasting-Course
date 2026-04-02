---
paths:
  - "Slides/**/*.tex"
  - "Quarto/**/*.qmd"
  - "scripts/**/*.py"
  - "**/*.ipynb"
---

# Course Knowledge Base: BSAD 8310 — Business Forecasting

<!-- Claude reads this before creating or modifying any lecture content.
     Update tables as the course develops. -->

## Notation Registry

| Rule | Convention | Example | Anti-Pattern |
|------|-----------|---------|-------------|
| Forecast target | $y_t$ (lowercase, subscript t) | $y_t = \text{sales at time } t$ | $Y$, $y(t)$ |
| h-step-ahead forecast | $\hat{y}_{t+h\|t}$ | $\hat{y}_{t+1\|t}$ | $\hat{y}_{t+1}$, $y^*$ |
| Forecast error | $e_t = y_t - \hat{y}_{t\|t-1}$ | $e_5 = y_5 - \hat{y}_{5\|4}$ | $\epsilon_t$ (reserve for white noise) |
| White noise | $\epsilon_t \sim WN(0, \sigma^2)$ | — | $e_t$ (that's forecast error) |
| Lag operator | $L^k y_t = y_{t-k}$ | $Ly_t = y_{t-1}$ | $B$ (Box-Jenkins notation — note when used) |
| Differencing | $\Delta y_t = y_t - y_{t-1}$ | $\Delta^2 y_t$ for double diff | $\nabla$ (acceptable but note convention) |
| ARIMA order | $\text{ARIMA}(p,d,q)$ | $\text{ARIMA}(1,1,1)$ | ARIMA(1)(1)(1) |
| Information criteria | AIC, BIC (no subscript) | $\text{AIC} = -2\ell + 2k$ | Akaike, Bayes |
| Loss function | $L(\cdot)$ or MSE/MAE/MAPE spelled out | $\text{RMSE} = \sqrt{\text{MSE}}$ | $\mathcal{L}$ (reserve for log-likelihood) |

## Symbol Reference

| Symbol | Meaning | Introduced |
|--------|---------|------------|
| $y_t$ | Time series observation at time $t$ | Lecture 1 |
| $\hat{y}_{t+h\|t}$ | Optimal h-step-ahead forecast given info at $t$ | Lecture 1 |
| $e_t$ | Forecast error | Lecture 1 |
| $\alpha$ | Smoothing parameter (ETS) | Lecture 3 |
| $p, d, q$ | AR order, integration order, MA order | Lecture 4 |
| $\phi_i$ | AR coefficient(s) | Lecture 4 |
| $\theta_j$ | MA coefficient(s) | Lecture 4 |
| $\rho_k$ | Autocorrelation at lag $k$ | Lecture 4 |
| $\lambda$ | Regularization penalty | Lecture 8 |
| $h$ | Forecast horizon | Lecture 1 |

## Lecture Progression

| # | Title | Core Question | Key Notation | Key Method |
|---|-------|--------------|-------------|------------|
| 1 | Introduction to Forecasting | What is forecasting and why does it matter? | $y_t$, $\hat{y}_{t+h\|t}$, $e_t$ | Benchmark models (naïve, seasonal naïve, mean) |
| 2 | Regression-Based Forecasting | How do we forecast using predictors? | $\beta$, $\epsilon_t$, prediction interval | OLS, forecast intervals, spurious regression |
| 3 | Exponential Smoothing | How does adaptive averaging work? | $\alpha$, $S_t$, ETS | Simple, Holt, Holt-Winters |
| 4 | ARIMA Models | How do autocorrelations generate forecasts? | ACF, PACF, $p,d,q$, $\phi$, $\theta$ | Box-Jenkins identification/estimation/checking |
| 5 | Multivariate Methods | How do multiple series inform each other? | VAR, ARIMAX, Granger | Granger causality, impulse responses |
| 6 | Forecast Evaluation | How do we measure and compare forecast quality? | RMSE, MAE, MAPE, DM stat | Diebold-Mariano test, forecast combination |
| 7 | ML Introduction | When does ML outperform classical methods? | bias-variance tradeoff | Train/val/test split, time series CV |
| 8 | Regularization | How to select predictors from many candidates? | $\lambda$, LASSO path | `sklearn` Lasso, Ridge, ElasticNet |
| 9 | Tree-Based Methods | How do ensembles improve accuracy? | depth, n_estimators | Random Forests, XGBoost for time series |
| 10 | Neural Networks | Can deep learning forecast time series? | LSTM, attention | Keras/PyTorch sequence models |
| 11 | Feature Engineering | What lag/rolling features improve ML forecasts? | lags, rolling stats | Pipeline design, target encoding |
| 12 | Capstone & Applications | How does this all connect in practice? | full pipeline | Demand forecasting, financial forecasting |

## Business Applications

| Application | Context | Dataset | Lecture(s) | Purpose |
|------------|---------|---------|------------|---------|
| Retail demand forecasting | How much inventory to order? | TBD | 1, 6, 9 | Motivating example |
| Macroeconomic forecasting | GDP, unemployment, inflation | FRED | 2, 5 | Show real-world complexity |
| Financial returns | Stock prices, volatility | TBD | 4, 7 | Efficient markets, GARCH |
| Energy demand | Hourly/daily load | TBD | 3, 11 | Seasonality patterns |

## Design Principles

| Principle | Rationale | Lectures Applied |
|-----------|----------|-----------------|
| Always show benchmark first | Students must know what "good" means | 1, 6 |
| Derive before implement | Code only after math is clear on slide | All |
| Python code matches slides exactly | Lab reinforces theory; no "trust me" moments | All lab sessions |
| Both classical and ML perspectives | Course covers both halves equally | Throughout |

## Anti-Patterns (Don't Do This)

| Anti-Pattern | What Happened | Correction |
|-------------|---------------|-----------|
| Using standard KFold for time series | Future data leaks into training | Always use `TimeSeriesSplit` |
| Forecasting levels when series is non-stationary | Spurious accuracy metrics | Test for stationarity; difference before modeling |
| Reporting in-sample fit as forecast accuracy | Severe overfitting | Always evaluate on held-out test set |
| Mixing $e_t$ (forecast error) and $\epsilon_t$ (white noise) | Student confusion | Use notation registry consistently |

## Python Code Pitfalls

| Bug | Impact | Fix |
|-----|--------|-----|
| `KFold` instead of `TimeSeriesSplit` | Future leakage, inflated accuracy | Use `sklearn.model_selection.TimeSeriesSplit` |
| Fitting ARIMA on non-stationary series | Invalid inference | ADF/KPSS test first; set $d$ appropriately |
| `random_state` omitted from sklearn | Non-reproducible results | Always `random_state=42` |
| `scaler.fit()` on test set | Data leakage | Fit scaler on train only; `transform` on test |
| Hardcoded absolute paths | Breaks on other machines | Use `pathlib.Path` relative to repo root |
| Plotting with default matplotlib style | Unprofessional figures | Set `rcParams` with UNO palette at top of script |
