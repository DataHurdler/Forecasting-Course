---
paths:
  - "**/*.py"
  - "scripts/**/*.py"
  - "**/*.ipynb"
---

# Python Code Standards — BSAD 8310

**Standard:** Publication-ready lab scripts. Runs end-to-end with `python script.py` — no interactive-only steps.

---

## 1. Reproducibility

- `np.random.seed(42)` called **once at top** of every stochastic script
- `random_state=42` on **every** sklearn estimator that accepts it
- All packages imported at top (`import`, not buried mid-script)
- All paths via `pathlib.Path`, relative to repository root
- `requirements.txt` kept current; pin major versions

```python
from pathlib import Path
import numpy as np
import pandas as pd

np.random.seed(42)

ROOT = Path(__file__).parent.parent  # repo root
DATA_DIR = ROOT / "data"
FIG_DIR = ROOT / "Figures"
```

---

## 2. Code Style

- **PEP 8** throughout; line limit 100 characters (see math exception below)
- `snake_case` for variables and functions; `PascalCase` for classes
- Docstrings on all functions (NumPy style preferred)
- No magic numbers — use named constants at top of file
- Type hints on function signatures

```python
def compute_rmse(actual: np.ndarray, forecast: np.ndarray) -> float:
    """Compute Root Mean Squared Error.

    Parameters
    ----------
    actual : np.ndarray
        Realized values.
    forecast : np.ndarray
        Point forecasts.

    Returns
    -------
    float
        RMSE value.
    """
    return np.sqrt(np.mean((actual - forecast) ** 2))
```

**Math exception:** Lines may exceed 100 characters if breaking would harm readability of a formula.
Add an inline comment explaining the mathematical operation.

```python
# DM test statistic: Diebold-Mariano (1995) eq. 4 — standardized loss differential
dm_stat = loss_differential.mean() / np.sqrt(loss_differential.var() / n_obs)
```

---

## 3. Time Series Domain Correctness

**Data leakage prevention — this is the most common and most serious error:**

```python
# CORRECT: time-aware cross-validation
from sklearn.model_selection import TimeSeriesSplit
tscv = TimeSeriesSplit(n_splits=5)

# WRONG: leaks future data into training
from sklearn.model_selection import KFold  # NEVER use for time series
```

**Scaler leakage:**
```python
# CORRECT
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # transform only, NOT fit_transform

# WRONG
X_test_scaled = scaler.fit_transform(X_test)  # refitting on test leaks stats
```

**Stationarity:**
- Always run ADF or KPSS test before fitting ARIMA
- Document test results and chosen differencing order in script comments
- `statsmodels.tsa.stattools.adfuller` for ADF; `statsmodels.tsa.stattools.kpss` for KPSS

**statsmodels ARIMA interface:**
```python
from statsmodels.tsa.arima.model import ARIMA
model = ARIMA(endog=y_train, order=(p, d, q))  # order must match slides
result = model.fit()
# Forecast
forecast = result.forecast(steps=h)
conf_int = result.get_forecast(steps=h).conf_int(alpha=0.05)
```

---

## 4. Visual Identity

```python
# UNO Maverick color palette
UNO_BLUE   = "#005CA9"
UNO_RED    = "#E41C38"
GRAY       = "#525252"
GREEN      = "#15803d"

import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams.update({
    "font.family": "sans-serif",
    "axes.titlesize": 14,
    "axes.labelsize": 12,
    "axes.titleweight": "bold",
    "axes.titlecolor": UNO_BLUE,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "legend.frameon": False,
    "figure.dpi": 150,
})
```

**Figure conventions:**
- Always set `figsize` explicitly — never rely on defaults
- `plt.tight_layout()` before every `savefig`
- White background for HTML/Quarto: `fig.patch.set_facecolor("white")`
- Transparent background for Beamer: `plt.savefig(..., transparent=True)`
- All axis labels in plain English (not variable names like `y_hat`)

```python
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(dates, actual, color=UNO_BLUE, label="Actual")
ax.plot(dates, forecast, color=UNO_RED, linestyle="--", label="Forecast")
ax.set_xlabel("Date")
ax.set_ylabel("Value")
ax.set_title("12-Month Ahead Sales Forecast")
ax.legend()
plt.tight_layout()
fig.savefig(FIG_DIR / "lecture01_forecast.png", dpi=150, bbox_inches="tight")
plt.close(fig)
```

---

## 5. Notebook Conventions (`.ipynb`)

- **Linear execution:** Every notebook runs top-to-bottom with `Kernel → Restart & Run All`; no cell order dependencies
- **Markdown narrative:** Each code section is preceded by a markdown cell explaining what and why
- **Committed outputs:** Notebook outputs committed to repo for student reference
- **No interactive widgets** in lab notebooks (breaks reproducibility)
- Variable names in notebooks must match slide notation exactly (e.g., `y_hat` not `pred`)

---

## 6. Heavy Computations

**Pre-compute and cache with pickle/joblib for anything > 10 seconds:**

```python
import joblib

# Save
joblib.dump(model, FIG_DIR.parent / "models" / "arima_model.pkl")

# Load
model = joblib.load(FIG_DIR.parent / "models" / "arima_model.pkl")
```

Commit `.pkl` files only if small (< 10 MB). For large models, document the command to regenerate.

---

## 7. Common Pitfalls

| Pitfall | Impact | Fix |
|---------|--------|-----|
| `KFold` for time series | Future data leaks, inflated accuracy | Always `TimeSeriesSplit` |
| `scaler.fit_transform(X_test)` | Leaks test set statistics | `scaler.transform(X_test)` only |
| `random_state` omitted | Non-reproducible results | Set `random_state=42` everywhere |
| Hardcoded absolute paths | Breaks on other machines | Use `pathlib.Path` from `ROOT` |
| `plt.show()` in scripts | Blocks execution in lab | Use `plt.savefig()` + `plt.close()` |
| ARIMA on non-stationary series | Invalid inference | ADF/KPSS test first |
| Default matplotlib style | Unprofessional figures | Set `rcParams` with UNO palette |
| Variable names differ from slides | Student confusion in lab | Use exact slide notation |

---

## 8. Quality Checklist

```
[ ] np.random.seed(42) at top
[ ] random_state=42 on every sklearn estimator
[ ] All imports at top
[ ] All paths via pathlib.Path relative to ROOT
[ ] TimeSeriesSplit used (never KFold) for time series CV
[ ] Scaler fit only on train set
[ ] Stationarity tested before ARIMA
[ ] Figures: explicit figsize, tight_layout, savefig + close
[ ] Variable names match slide notation
[ ] Script runs end-to-end: python script.py
[ ] Notebook: Restart & Run All succeeds
```
