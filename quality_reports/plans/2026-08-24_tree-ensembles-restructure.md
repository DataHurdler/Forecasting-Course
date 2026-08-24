# Plan: Merge Boosted Trees into Random Forests; Expand Regularization

**Date:** 2026-08-24
**Approved decisions:** boosting merges into L05; regularization expands to a full standalone L06 (mirrors ISLP Ch.6 / Ch.8 split); wire open-source readings into syllabus AND add missing citations to slides.

## Target structure (stays at 12 lectures, no renumbering)
- **L04** Decision Trees — unchanged content, citations added
- **L05** Tree Ensembles: Random Forests & Boosted Trees — RF (9 frames) + boosting (5 frames from L06)
- **L06** Regularization & Model Selection — expand 2 frames -> full lecture (ISLP Ch.6 shape)

## Steps
1. Beamer L05: append Gradient Boosting + XGBoost sections; rewrite outline, takeaways, title
2. Beamer L06: rewrite as Regularization & Model Selection (subset selection vs shrinkage, ridge,
   lasso, elastic net, regularization paths, choosing lambda by CV, sklearn)
3. Add \parencite calls: Breiman1996/2001, Chen2016, Molnar2022, James2021, Hastie2009,
   Tibshirani1996, Hoerl, ZouHastie2005 into L04/L05/L06
4. Mirror both into Quarto .qmd (Beamer is source of truth)
5. Syllabus: update reading map + weekly readings (ISLP Ch.8 for L4-L5, ISLP Ch.6 for L6,
   XGBoost tutorial, Molnar) and lecture titles
6. CLAUDE.md: update lecture table rows 5 and 6
7. Verify: 3-pass xelatex + bibtex both lectures; check overfull; re-render Quarto

## Verification gates
- Both PDFs compile clean, no Overfull \vbox > 5pt
- Beamer/Quarto frame parity maintained (qmd '## ' count == tex frames - 1)
- All new \parencite keys resolve against Bibliography_base.bib
