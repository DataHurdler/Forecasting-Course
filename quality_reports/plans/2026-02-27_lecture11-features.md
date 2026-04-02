# Plan: Lecture 11 — Feature Engineering
**Status:** APPROVED
**Date:** 2026-02-27
**Session:** Lecture creation

---

## Deliverables
- `Slides/Lecture11_Features.tex` — 25 slides
- `scripts/Lecture11_Features.ipynb` — 9 sections

---

## New bib entries needed
- `Guyon2003` — "An Introduction to Variable and Feature Selection", JMLR 2003 (RFE)
- `Pedregosa2011` — "Scikit-learn: Machine Learning in Python", JMLR 2011 (Pipeline)
- `Molnar2022` — "Interpretable Machine Learning", 2nd ed. (permutation importance)
- (All other needed citations already in bib ✓)

---

## Slide sections (25 total)

| # | Slides | Content |
|---|--------|---------|
| 1–3 | 3 | Title + Outline + Motivation bridge (L10 RMSE → feature gap) |
| 4–6 | 3 | **Lag Features**: overview + ACF/PACF guidance + [fragile] leakage demo |
| 7–9 | 3 | **Rolling Statistics**: overview + rolling mean/std/min/max + EWM + importance preview TikZ |
| 10–12 | 3 | **Calendar and Structural Features**: overview + month dummies + when they help/hurt |
| 13–15 | 3 | **Interaction and Ratio Features**: overview + YoY/MoM formulas + extended make_features [fragile] |
| 16–18 | 3 | **Feature Selection**: overview + LASSO + permutation importance + RFECV [fragile] |
| 19–21 | 3 | **Pipeline Design**: overview + Pipeline flow TikZ + Pipeline code [fragile] |
| 22–23 | 2 | **Application**: section overview + leaderboard comparison (baseline 26f vs extended 36f) |
| 24–25 | 2 | **Takeaways** + **References** |

---

## TikZ diagrams (3 total — hardcoded coords, no foreach, no pgfmathsetmacro)

1. **ACF/PACF bar chart** (Slide 5): two panels (ACF top, PACF bottom); 12 bars each; explicit `\fill` statements; dashed confidence bands; lags 1, 2, 12 annotated; unolightblue bars for ACF, unoblue/unolightgreen for PACF spikes
2. **Permutation importance bar chart** (Slide 9): 8 horizontal bars; top 4 in unoblue, bottom 4 in gray!40; explicit `\fill` rectangles; feature labels as `\node`s; x-axis arrow
3. **Pipeline flow diagram** (Slide 20): 6 vertical stages with arrows; unolightblue for data/prediction stages, unolightgreen for transform stages, unolightred for model stage; all hardcoded y-coords

---

## Code frames ([fragile])
- **Slide 6**: two-column lag leakage demo (safe shift vs. lookahead bug)
- **Slide 15**: single wide-column `make_features_extended()` function
- **Slide 18**: left=RFECV definition box; right=RFECV code
- **Slide 21**: two-column Pipeline construction code

---

## Notebook sections (9)
1. Setup (UNO palette, sklearn/xgboost imports, rcParams)
2. Load RSXFS + `make_features_extended()` (36 features)
3. Feature visualization: ACF/PACF + rolling features time series → `lecture11_acf_pacf.png`, `lecture11_rolling_features.png`
4. Permutation importance ranking (RF on train, permutation on val) → `lecture11_permutation_importance.png`
5. Feature selection: LassoCV coefficients + RFECV curve → `lecture11_rfecv_curve.png`
6. Pipeline construction + CV leakage demonstration
7. Model comparison: baseline 26f vs extended 36f (RF + XGBoost) → `lecture11_feature_impact.png`
8. Full leaderboard update → `lecture11_leaderboard.png`
9. Forecast comparison plot → `lecture11_forecast_comparison.png`

---

## Illustrative RMSE values (consistent with L10)
| Model | RMSE (26f) | RMSE (36f) | Improvement |
|-------|------------|------------|-------------|
| Elastic Net | 2,540 | 2,410 | −130 |
| Random Forest | 2,380 | 2,210 | −170 |
| XGBoost | 2,250 | 2,050 | −200 |
| LSTM (med, 5 seeds) | 2,180 | 1,920 | −260 |

---

## Key compilation risks (pre-mitigated)
- `[fragile]` on all 4 code frames — MUST verify
- No `\foreach` in TikZ — all bars/nodes explicit
- No `\pgfmathsetmacro` in frame bodies
- No orange colors; no `unolightgray` (use `gray!25` or `gray!40`)
- `align=center` on TikZ multi-line nodes
- Max 2 colored boxes per slide — audit each slide
- Bib entries added BEFORE first compile
- Code lines ≤ 52 chars at `\tiny` in columns

---

## Implementation sequence
1. Add 3 bib entries to `Bibliography_base.bib`
2. Create `Slides/Lecture11_Features.tex`
3. Compile (3-pass XeLaTeX + bibtex): target 25pp, 0 errors, 0 overflows
4. Run proofreader + pedagogy reviewer (parallel)
5. Apply fixes; recompile
6. Create `scripts/Lecture11_Features.ipynb`
7. Write session log → `quality_reports/session_logs/2026-02-27_lecture11-features.md`
