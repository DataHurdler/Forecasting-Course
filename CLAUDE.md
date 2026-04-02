# CLAUDE.MD -- Academic Project Development with Claude Code

**Project:** BSAD 8310: Business Forecasting
**Institution:** University of Nebraska at Omaha
**Branch:** main

---

## Core Principles

- **Plan first** -- enter plan mode before non-trivial tasks; save plans to `quality_reports/plans/`
- **Verify after** -- compile/render and confirm output at the end of every task
- **Single source of truth** -- Beamer `.tex` is authoritative; Quarto `.qmd` derives from it
- **Quality gates** -- nothing ships below 80/100
- **[LEARN] tags** -- when corrected, save `[LEARN:category] wrong → right` to MEMORY.md
- **Python-first** -- lab scripts use Python (statsmodels, scikit-learn, matplotlib); `random_state=42`

---

## Folder Structure

```
bsad8310-forecasting/
├── CLAUDE.MD                    # This file
├── .claude/                     # Rules, skills, agents, hooks
├── Bibliography_base.bib        # Centralized bibliography
├── Figures/                     # Figures and images
├── Preambles/header.tex         # LaTeX headers
├── Slides/                      # Beamer .tex files (LectureNN_Title.tex)
├── Quarto/                      # RevealJS .qmd files + theme
├── docs/                        # GitHub Pages (auto-generated)
├── scripts/                     # Utility scripts + Python notebooks
├── quality_reports/             # Plans, session logs, merge reports
├── explorations/                # Research sandbox (see rules)
├── templates/                   # Session log, quality report templates
└── master_supporting_docs/      # Papers and existing slides
```

---

## Commands

```bash
# LaTeX (3-pass, XeLaTeX only)
cd Slides && TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode file.tex
BIBINPUTS=..:$BIBINPUTS bibtex file
TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode file.tex
TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode file.tex

# Deploy Quarto to GitHub Pages
./scripts/sync_to_docs.sh LectureNN_Title

# Quality score
python scripts/quality_score.py Quarto/LectureNN_Title.qmd

# Run Python lab script (must run end-to-end without interaction)
python scripts/LectureNN_lab.py
```

---

## Quality Thresholds

| Score | Gate | Meaning |
|-------|------|---------|
| 80 | Commit | Good enough to save |
| 90 | PR | Ready for deployment |
| 95 | Excellence | Aspirational |

---

## Skills Quick Reference

| Command | What It Does |
|---------|-------------|
| `/compile-latex [file]` | 3-pass XeLaTeX + bibtex |
| `/deploy [LectureNN_Title]` | Render Quarto + sync to docs/ |
| `/extract-tikz [LectureN]` | TikZ → PDF → SVG |
| `/proofread [file]` | Grammar/typo/overflow review |
| `/visual-audit [file]` | Slide layout audit |
| `/pedagogy-review [file]` | Narrative, notation, pacing review |
| `/review-r [file]` | R code quality review (R scripts only) |
| `/qa-quarto [LectureN]` | Adversarial Quarto vs Beamer QA |
| `/slide-excellence [file]` | Combined multi-agent review |
| `/translate-to-quarto [file]` | Beamer → Quarto translation |
| `/validate-bib` | Cross-reference citations |
| `/devils-advocate` | Challenge slide design |
| `/create-lecture` | Full lecture creation workflow |
| `/commit [msg]` | Stage, commit, PR, merge |
| `/lit-review [topic]` | Literature search + synthesis |
| `/research-ideation [topic]` | Research questions + strategies |
| `/interview-me [topic]` | Interactive research interview |
| `/review-paper [file]` | Manuscript review |
| `/data-analysis [dataset]` | End-to-end Python analysis (statsmodels/sklearn) |

---

## Beamer Custom Environments

| Environment         | Effect                      | Use Case                              |
|---------------------|-----------------------------|---------------------------------------|
| `keybox`            | UNO-blue highlighted box    | Key formulas, forecast accuracy rules |
| `definitionbox[T]`  | Blue-bordered titled box    | Formal definitions (stationarity etc) |
| `warningbox`        | Red-accent warning box      | Common pitfalls, assumption violations|
| `examplebox[T]`     | Green-accent titled box     | Worked examples, business applications|

## Quarto CSS Classes

| Class              | Effect                    | Use Case                           |
|--------------------|---------------------------|------------------------------------|
| `.keybox`          | Gold-bordered box         | Key formulas, rules (mirrors Beamer keybox) |
| `.definitionbox`   | Blue left-rule + title    | Formal definitions (use `.definitionbox-title` inner div for title) |
| `.warningbox`      | Red left-rule box         | Common pitfalls, assumption violations |
| `.examplebox`      | Green left-rule + title   | Worked examples (use `.examplebox-title` inner div for title) |
| `.key-result`      | Bold UNO-blue accent      | Key takeaways per slide            |
| `.interpretation`  | Indented italic           | Model interpretation callouts      |
| `.smaller`         | 85% font size             | Dense content / long equations     |
| `.python-output`   | Monospace gray box        | Code output / model results        |
| `.hi`              | Bold blue accent text     | Key terms inline                   |
| `.neutral`         | Gray muted text           | Asides, caveats, footnotes         |
| `.positive`        | Green bold text           | Pros, recommended use cases        |
| `.negative`        | Red bold text             | Cons, contraindicated use cases    |

---

## Current Project State

**Beamer status:** All 12 new lectures written (Spring 2026 redesign).
**Quarto status:** All 12 new lectures written.
**Note:** Old lecture files (Lecture01_Intro.tex through Lecture12_Capstone.tex) remain on disk but are superseded by the redesigned files below.

| Lecture | Beamer | Quarto | Key Content |
|---------|--------|--------|-------------|
| 1: Intro, ETS & Forecast Evaluation | `Lecture01_ETS_Eval.tex` ✓ | `Lecture01_ETS_Eval.qmd` ✓ | SES, Holt, Holt-Winters, ETS framework, RMSE/MAE/MAPE/MASE, walk-forward CV, DM test. |
| 2: ARIMA, VAR & Multivariate Models | `Lecture02_ARIMA_VAR.tex` ✓ | `Lecture02_ARIMA_VAR.qmd` ✓ | Stationarity, ARIMA/SARIMA, auto-ARIMA, VAR, Granger causality, ARIMAX. |
| 3: Generalized Additive Models | `Lecture03_GAMs.tex` ✓ | `Lecture03_GAMs.qmd` ✓ | GAM structure, smoothing penalty, splines, Prophet, pyGAM, partial dependence plots. |
| 4: Decision Trees | `Lecture04_DecisionTrees.tex` ✓ | `Lecture04_DecisionTrees.qmd` ✓ | Bias-variance tradeoff, CART, entropy/information gain, sklearn, feature importance. |
| 5: Random Forests | `Lecture05_RandomForests.tex` ✓ | `Lecture05_RandomForests.qmd` ✓ | Bagging, bootstrap aggregation, feature subsampling, OOB error, MDI vs permutation importance. |
| 6: Boosted Trees & Regularization | `Lecture06_BoostedTrees.tex` ✓ | `Lecture06_BoostedTrees.qmd` ✓ | Gradient boosting, XGBoost (Newton step, regularization, col subsampling), Ridge/LASSO/Elastic Net. |
| 7: Introduction to Neural Networks | `Lecture07_NeuralNets.tex` ✓ | `Lecture07_NeuralNets.qmd` ✓ | Neurons, activations, FFN layers, MSE loss, backprop, Adam, dropout, PyTorch Dataset/DataLoader/training loop. |
| 8: CNN Architectures | `Lecture08_CNNs.tex` ✓ | `Lecture08_CNNs.qmd` ✓ | Convolution, pooling, LeNet→VGG→Inception→ResNet, residual connections, 1D CNN for time series. |
| 9: RNNs, LSTMs & Transformers | `Lecture09_RNNTransformers.tex` ✓ | `Lecture09_RNNTransformers.qmd` ✓ | Vanilla RNN, LSTM gates (forget/input/output/cell), attention, scaled dot-product, Transformer encoder, PyTorch nn.LSTM/nn.TransformerEncoder. |
| 10: Bayesian Statistics I — Foundations | `Lecture10_BayesianI.tex` ✓ | `Lecture10_BayesianI.qmd` ✓ | Frequentist vs Bayesian, Bayes' theorem, priors (Beta/Normal/Exponential), MCMC/NUTS, PyMC, prior predictive checks. |
| 11: Bayesian Statistics II — TS & Hierarchical | `Lecture11_BayesianII.tex` ✓ | `Lecture11_BayesianII.qmd` ✓ | Bayesian structural TS, local linear trend, Fourier seasonality, partial pooling, hierarchical models in PyMC. |
| 12: Bayesian Statistics III — Linear Regression | `Lecture12_BayesianIII.tex` ✓ | `Lecture12_BayesianIII.qmd` ✓ | Bayesian linear regression, posterior coefficient distributions, HDI, DAGs, scenario analysis, course method map. |
