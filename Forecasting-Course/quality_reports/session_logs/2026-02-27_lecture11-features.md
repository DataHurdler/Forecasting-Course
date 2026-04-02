# Session Log: Lecture 11 — Feature Engineering
**Date:** 2026-02-27 (continued 2026-02-28)
**Status:** COMPLETE
**Files produced:**
- `Slides/Lecture11_Features.tex` — 33 pages (original 25 + 7 sectionslide frames + 1 LASSO split), 0 errors, 0 overflows
- `scripts/Lecture11_Features.ipynb` — 9 sections, 7 figures

---

## Goal

Create Lecture 11 (Feature Engineering: Lags, Rolling Statistics, Calendar Features,
Interaction Features, Feature Selection, Pipeline Design) as a full first draft.
Includes Beamer slide deck + Jupyter notebook lab. This is the final ML methods
lecture before the Capstone (L12).

---

## Implementation Notes

### Bib entries added
- `Guyon2003` — "An Introduction to Variable and Feature Selection", JMLR 2003
- `Pedregosa2011` — "Scikit-learn: Machine Learning in Python", JMLR 2011
- `Molnar2022` — "Interpretable Machine Learning", 2nd ed.
- All other needed citations already in bib ✓

### Slide structure (33 pages final, after pedagogy fixes)
1. Title (1)
2. Outline (1)
3. **Motivation bridge** — LSTM RMSE 1,920 vs. XGBoost 2,250 (1)
4. **Lag Features**: sectionslide + overview + ACF/PACF guidance (with TikZ) + leakage demo (4)
5. **Rolling Statistics**: sectionslide + overview + rolling mean/std/min/max + EWM + importance preview TikZ (4)
6. **Calendar and Structural Features**: sectionslide + overview + month dummies + SARIMA comparison (3)
7. **Interaction and Ratio Features**: sectionslide + overview + YoY/MoM formulas + extended make_features code (3)
8. **Feature Selection**: sectionslide + overview + LASSO slide + Permutation Importance slide (split) + RFECV (5)
9. **Pipeline Design**: sectionslide + overview + Pipeline flow TikZ + Pipeline code (4)
10. **Application**: sectionslide + overview + leaderboard comparison (3)
11. **Takeaways** + **References** (2)

### Notebook structure (9 sections)
1. Setup (UNO palette, sklearn/xgboost imports, rcParams, FIGURE_DIR)
2. Load RSXFS + `make_features_baseline()` (~29f) + `make_features_extended()` (36f) + three-way split
3. Feature visualization: ACF/PACF + rolling features time series
4. Permutation importance ranking (RF on train, permutation on val)
5. Feature selection: LassoCV coefficients + RFECV curve
6. Pipeline construction + CV leakage demonstration
7. Model comparison: baseline (~29f) vs extended (36f) (RF + XGBoost + ElasticNet)
8. Full leaderboard update (L01–L11, illustrative)
9. Forecast comparison plot

Figures saved: `lecture11_acf_pacf.png`, `lecture11_rolling_features.png`,
`lecture11_permutation_importance.png`, `lecture11_rfecv_curve.png`,
`lecture11_feature_impact.png`, `lecture11_leaderboard.png`,
`lecture11_forecast_comparison.png`

---

## Compilation Issues

### Initial compile: clean (25pp, 0 errors, 0 overflows)
No compilation issues encountered in the first draft. All TikZ diagrams used
hardcoded coordinates with no `\foreach` or `\pgfmathsetmacro` in frame bodies.
All 4 code frames marked `[fragile]`. Box count respected (max 2 per slide).

### After pedagogy fixes: 33pp, 0 errors, 0 overflows
The 7 `\sectionslide` insertions + 1 LASSO slide split added 8 frames without
introducing any overflows. The LASSO formula with `\underbrace{}` labels
compiled cleanly at full width.

---

## Quality Review: Proofreader

**Run:** 2026-02-27 (concurrent with pedagogy review)
**Result:** Clean — no issues of record

---

## Quality Review: Pedagogy

**Run:** 2026-02-28
**Report:** `quality_reports/Lecture11_Features_pedagogy_report.md`
**Score:** 8/13 patterns followed, 3/13 violated, 2/13 partially applied

### Fixes Applied

| # | Severity | Fix |
|---|----------|-----|
| 1 | MAJOR | Added α disambiguation footnote on EWM slide — EWM α ≠ ETS α (L03) ≠ Elastic Net α (L08) |
| 2 | MEDIUM | Inserted `\sectionslide{}{}` before all 7 section boundaries |
| 3 | MEDIUM | Demoted 7 Section Overview keyboxes to plain bold paragraph text |
| 4 | MEDIUM | Split dense "LASSO and Permutation Importance" slide into two full-width slides |

### Deferred
- **RMSE subscripts** (Low): `RMSE_0` and `RMSE_j` labels — slide now has clear in-text labels
- **LASSO underbrace** (Low): Added `\underbrace{}` labels in the split slide
- **Pre-pipeline feature engineering note** (Low): Addressed implicitly in Pipeline Design section overview

---

## [LEARN] Entries

```
[LEARN:windows] On Windows with Git Bash, XeLaTeX (Windows binary) cannot
  find files via `cd /c/... && xelatex ...` due to CWD resolution. Use
  Windows-style TEXINPUTS with semicolon separators and absolute Windows paths:
  TEXINPUTS="C:/path/to/Preambles;;" xelatex -interaction=nonstopmode
  -output-directory="C:/path/to/Slides" "C:/path/to/Slides/File.tex"
  Also: bibtex must be run FROM the Slides directory (cd first) due to
  openout_any=p restriction.

[LEARN:pedagogy] When sectionslide calls are inserted and section keyboxes
  are demoted simultaneously, treat them as a single edit per section to keep
  the diff clean. The keybox removal is implicitly linked to the sectionslide
  insertion — both serve Pattern 6 (standout slides) and Pattern 10 (box fatigue).

[LEARN:pedagogy] Dense two-column "method A vs method B" slides should be split
  into two full-width slides when both methods involve algorithms or formulas
  (not just definitions). Expand the full-width version with: context note,
  underbrace labels on formulas, advantages/disadvantages, and a worked example.

[LEARN:notation] EWM α, ETS α (L03), and Elastic Net mixing α (L08) are three
  distinct uses of α in this course. Any new slide using α must include a muted
  disambiguation footnote referencing the earlier lectures.
```

---

## Final State

| Item | Status |
|------|--------|
| Slides compile | ✓ 33 pages, 0 errors, 0 overflows |
| Proofreader | ✓ Clean |
| Pedagogy reviewer | ✓ All MAJOR + MEDIUM fixed; LOW deferred |
| Notebook | ✓ 9 sections, 7 figures |
| Quality score (est.) | ~88/100 |

---

## Open Questions / Next Session

1. L11 is first-draft complete. User to review PDF before L12 is started.
2. Deferred LOW pedagogy items can be addressed in a revision pass.
3. Agent queue still running: L08 pedagogy, L06 proofreader+pedagogy, L07 proofreader+pedagogy.
4. Lecture 12: Capstone & Applications — business case studies.
