# Plan: Lecture 07 — Machine Learning Introduction
**Status:** APPROVED
**Date:** 2026-02-25

## Deliverables
- `Slides/Lecture07_MLIntro.tex` — ~28 slides
- `scripts/Lecture07_MLIntro.ipynb` — 9 sections

## New bib entries needed
- `Bergmeir2018` — validity of CV for autoregressive TS prediction
- `Arlot2010` — survey of cross-validation procedures

## Slide sections (28 total)
1. Title + Outline (2)
2. Why ML for Forecasting? (sectionslide + 3)
3. Bias-Variance Tradeoff (sectionslide + 4)
4. Train/Val/Test Discipline (sectionslide + 3)
5. Cross-Validation for Time Series (sectionslide + 3)
6. Regularization Preview (sectionslide + 2)
7. Feature Engineering Preview (sectionslide + 2)
8. ML Forecasting Pipeline (sectionslide + 2)
9. Takeaways + References (2)

## Key compilation risks
- pgfplots U-curve: use shifted parabola `{0.5*exp(-0.4*x) + 0.05 + 0.03*(x-4)^2}`
- tcolorbox comma escaping: use `title={...}` with curly braces
- TikZ pipeline diagram: use xscale=0.82, tiny annotations
- lstlisting for Python code (not minted)
