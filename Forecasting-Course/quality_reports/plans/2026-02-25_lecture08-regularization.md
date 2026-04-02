# Plan: Lecture 08 — Regularization
**Status:** APPROVED
**Date:** 2026-02-25

## Deliverables
- `Slides/Lecture08_Regularization.tex` — ~28 slides
- `scripts/Lecture08_Regularization.ipynb` — 9 sections

## New bib entries needed
- `Tibshirani1996` — LASSO, JRSS-B 1996
- `ZouHastie2005` — Elastic Net, JRSS-B 2005
- `HoerlKennard1970` — Ridge regression, Technometrics 1970

## Slide sections (28 total)
1. Title + Outline (2)
2. Motivation: Why Regularization? (sectionslide + 3)
3. Ridge Regression L2 (sectionslide + 4)
4. LASSO Regression L1 (sectionslide + 4)
5. Elastic Net (sectionslide + 2)
6. Tuning λ via Cross-Validation (sectionslide + 3)
7. Application to Forecasting (sectionslide + 3)
8. Takeaways + References (2)

## Key compilation risks (pre-mitigated from [LEARN])
- Geometry constraint diagrams (Ridge circle, LASSO diamond): use hardcoded TikZ paths, no pgfmathsetmacro
- Python code listings: mark frames [fragile]
- TikZ nodes with newlines: always include align=center in style
- No orange colors: only unoblue/unored/unogray/unogreen + light variants
