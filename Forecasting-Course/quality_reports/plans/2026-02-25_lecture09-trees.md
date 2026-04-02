# Plan: Lecture 09 — Tree-Based Methods
**Status:** APPROVED
**Date:** 2026-02-25

## Deliverables
- `Slides/Lecture09_Trees.tex` — ~28 slides
- `scripts/Lecture09_Trees.ipynb` — 9 sections

## New bib entries needed
- `Breiman2001` — Random Forests, Machine Learning 2001
- `Breiman1996` — Bagging predictors, Machine Learning 1996
- (Chen2016 already present)

## Slide sections (28 total)
1. Title + Outline (2)
2. Decision Trees: CART (sectionslide + 3)
3. Bagging and Random Forests (sectionslide + 4)
4. Gradient Boosting and XGBoost (sectionslide + 4)
5. Feature Importance (sectionslide + 2)
6. Hyperparameter Tuning (sectionslide + 2)
7. Application to Forecasting (sectionslide + 3)
8. Takeaways + References (2)

## Key compilation risks (pre-mitigated)
- TikZ tree diagram: use align=center in node styles (nodes have newlines)
- TikZ boosting flow: hardcoded coordinates, no pgfmathsetmacro
- lstlisting frames: mark [fragile]
- No orange colors: only unoblue/unored/unogray/unogreen + light variants
