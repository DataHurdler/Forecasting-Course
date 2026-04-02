# Session Log: Lecture 04 — Stationarity and ARIMA
**Date:** 2026-02-25
**Files:** `Slides/Lecture04_ARIMA.tex`, `scripts/Lecture04_ARIMA.ipynb`
**Status:** Complete — 25 pages, 0 errors, 0 overflows

---

## Goal
Create Lecture 04 covering Stationarity and ARIMA models, following the established
workflow: plan → implement → compile → dual quality review → fix all issues → clean recompile.

---

## Compilation History

| Pass | Pages | Errors | Overflows |
|------|-------|--------|-----------|
| Initial 3-pass | 25 | 0 | 1 (ACF slide, vbox 16.3pt) |
| After initial fix | 25 | 0 | 1 (ACF slide, vbox 5.6pt) |
| After quality fixes | 25 | 0 | 2 (ACF 5.6pt, ARIMA 48.7pt) |
| Final | 25 | 0 | 0 |

---

## Proofreader Findings and Fixes

### CRITICAL (2 fixed)
1. **Wrong "What's Next" slide** — pointed to Forecast Evaluation (Lecture 6), but
   Lecture 5 is Multivariate Methods. Fixed: frame title, body content, and "six" → "four"
   model families count.
2. **Forecasting keybox self-contradiction** — "unlike SES" but then said SES grows
   the same way; ARIMA(0,1,1) ≡ SES makes the contrast wrong. Fixed: rewritten to
   "ARIMA(0,1,1) ≡ SES shares this same growing uncertainty."

### MAJOR (5 fixed)
3. **"Behaviour" → "Behavior"** — British spelling in table header.
4. **Duplicate ADF citation** — `\parencite` in definitionbox title AND `\textcite`
   in body. Removed `\parencite` from title; kept narrative citation in body.
5. **PACF MA bullet** — "αk ≠ 0 for all k" is technically wrong (can be exactly zero
   by coincidence). Fixed to "φkk → 0 geometrically as k → ∞."
6. **ARMA error notation** — `\sim(0,σ²)` missing distributional family.
   Fixed to `\sim\mathcal{N}(0,σ²)` (consistent with Lecture 03).
7. **Exclamation mark** — "ARIMA(0,1,1): equivalent to SES!" informal.
   Replaced with `\parencite[][Ch.~9]{Hyndman2021}` citation.

### MINOR (3 fixed)
8. **Table header "$d$"** — not in math mode. Fixed to `$\boldsymbol{d}$`.
9. **"KPSS" unexpanded** — expanded to "Kwiatkowski--Phillips--Schmidt--Shin"
   on first use in the body text.
10. **"model combination" → "forecast combination"** (fixed as part of What's Next rewrite).

---

## Pedagogy Reviewer Findings and Fixes

### CRITICAL (1 fixed)
C1. **Mislabeled TikZ plots** — captions said "Stationary AR(1), φ₁ = 0.7" and
    "Random walk, φ₁ = 1" but the plots use deterministic trig functions.
    Fixed captions to "AR(1)-like series, φ₁ = 0.7 (simulated)" and
    "Random-walk-like series, φ₁ = 1 (simulated)."

### HIGH (4 fixed)
H1. **No worked example in ARIMA section** — added compact muted note at bottom
    of ARIMA(p,d,q) slide: "Example (ARIMA(1,1,0), φ̂₁=0.5, y₁₀₀=120, y₉₉=118):
    Δy₁₀₀=2 ⇒ ŷ₁₀₁|₁₀₀ = 120+0.5×2 = 121."
H2. **SARIMA notation overload** — six new symbols with no prior polynomial shorthand.
    Added bridge sentence defining φp(B) and θq(B) before the definitionbox.
H3. **No PACF visualization** — ACF had a TikZ bar chart; PACF had only text.
    Restructured PACF slide to two-column layout with AR(2) PACF bar chart
    (cuts off after lag 2) on the right column.
H4. **MA(q) component unmotivated** — added muted note: "MA terms arise naturally
    from aggregation and averaging — notably, ARIMA(0,1,1) ≡ SES."

### MEDIUM (4 fixed)
M1. **Over-differencing warning incomplete** — added "Re-apply ADF/KPSS after
    differencing; stop at d=1 if now stationary; over-differencing adds MA unit roots."
M2. **Invertibility unexplained** — added parenthetical "(unique MA representation;
    allows rewriting as AR(∞))."
M3. **Ljung-Box lacks decision rule** — added "test at L=min(10,T/5); p<0.05 signals
    residual autocorrelation — re-identify."
M4. **ADF Socratic too technical** — softened from requiring Phillips-Perron
    asymptotics knowledge to: "the ADF statistic doesn't follow a standard t-distribution
    even in large samples — what does this mean for standard p-values?"

### LOW (2 fixed)
L1. **αk → φkk** — changed PACF notation from αk (conflicts with SES smoothing
    parameter α from Lecture 03) to Box-Jenkins standard φkk.
L2. **"Practice rule" examplebox → warningbox** — content is a methodological warning,
    not a worked example. Changed box type accordingly.

---

## Overflow Fixes

1. **ACF slide (initial 16.3pt):** reduced TikZ height 2.8cm → 2.5cm, removed `\vspace{0.1cm}`.
2. **ACF slide (residual 5.6pt after quality fixes):** reduced TikZ height further 2.5cm → 2.2cm.
3. **ARIMA(p,d,q) slide (48.7pt):** examplebox (full tcolorbox + content + padding) was
   too tall. Replaced with compact single-line muted note.
4. **PACF slide (5.6pt from new PACF chart):** reduced TikZ height 3.0cm → 2.7cm.

---

## Design Decisions

- **PACF visualization:** AR(2) PACF coordinates `{(1,0.78)(2,0.25)(3,0.02)...}` are
  plausible but stylized (not computed from exact Yule-Walker equations). Consistent with
  the ACF visualization approach used for the AR(1) ACF plot.
- **SARIMA bridge:** Added polynomial shorthand definition before the definitionbox to
  reduce notation overload. Kept the bridge compact (one line with `\!` negative spaces).
- **Worked example:** Converted from examplebox to muted footnote to avoid overflow.
  The computation is correct: Δy₁₀₀ = 120-118 = 2, then ŷ₁₀₁|₁₀₀ = 120 + 0.5×2 = 121.
- **φkk notation:** Box-Jenkins standard (φkk from Yule-Walker). Avoids conflict with
  Lecture 03's smoothing parameter α.

---

## Final Slide Count by Section

| Section | Frames |
|---------|--------|
| Title + Outline | 2 |
| Stationarity | 3 |
| Unit Roots and Differencing | 4 |
| ACF and PACF | 4 |
| The ARIMA Model | 4 |
| Seasonal ARIMA | 2 |
| Key Takeaways and Roadmap | 4 (incl. References) |
| **Total** | **25** |

---

## Citations Used

| Key | Paper |
|-----|-------|
| `DickeyFuller1979` | Dickey & Fuller (1979), JASA 74(366):427–431 |
| `Kwiatkowski1992` | Kwiatkowski et al. (1992), JoE 54(1–3):159–178 |
| `BoxJenkins2015` | Box, Jenkins, Reinsel & Ljung (2015), 5th ed. |
| `Hyndman2021` | Hyndman & Athanasopoulos (2021), FPP3, Ch. 9 |

---

## Next Session

Lecture 05: Multivariate Methods — VAR models, ARIMAX, Granger causality tests.
