# CLAUDE.MD -- Academic Project Development with Claude Code

**Project:** ECON 8310: Business Forecasting
**Institution:** University of Nebraska at Omaha
**Branch:** main

---

## Core Principles

- **Plan first** -- enter plan mode before non-trivial tasks; save plans to `quality_reports/plans/`
- **Verify after** -- compile/render and confirm output at the end of every task
- **Single source of truth** -- Beamer `.tex` is authoritative; Quarto `.qmd` derives from it
- **Quality gates** -- nothing ships below 80/100
- **[LEARN] tags** -- when corrected, save `[LEARN:category] wrong → right` to MEMORY.md
- **Python-first** -- labs and analysis use Python (statsmodels, scikit-learn, matplotlib); `random_state=42`

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
├── Labs/                        # In-class hands-on exercises (LectureNN_lab.qmd)
├── Narration/                   # Recording scripts (LectureNN_script.md)
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

# Render an in-class lab (must run end-to-end without interaction)
quarto render Labs/LectureNN_lab.qmd
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

The full workflow ships in `.claude/` (60 skills, 18 agents, 8 hooks, 30 rules), inherited
from the [claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)
template at v2.5.1. The ones that matter most for this course:

**Slides and lectures**

| Command | What It Does |
|---------|-------------|
| `/compile-latex [file]` | 3-pass XeLaTeX + bibtex |
| `/deploy [LectureNN_Title]` | Render Quarto + sync to docs/ |
| `/create-lecture` | Full lecture creation workflow |
| `/translate-to-quarto [file]` | Beamer → Quarto translation |
| `/qa-quarto [LectureN]` | Adversarial Quarto vs Beamer QA |
| `/extract-tikz [LectureN]` | TikZ → PDF → SVG |
| `/new-diagram` | Author a new TikZ diagram |
| `/slide-excellence [file]` | Combined multi-agent review |
| `/visual-audit [file]` | Slide layout audit |
| `/pedagogy-review [file]` | Narrative, notation, pacing review |
| `/proofread [file]` | Grammar/typo/overflow review |
| `/devils-advocate` | Challenge slide design |
| `/validate-bib` | Cross-reference citations |

**Teaching**

| Command | What It Does |
|---------|-------------|
| `/syllabus` | Draft or revise the syllabus |
| `/scaffold-exercises` | Generate problem sets / homework scaffolding |
| `/teach-from-paper [file]` | Turn a paper into teaching material |

**Analysis and code**

| Command | What It Does |
|---------|-------------|
| `/data-analysis [dataset]` | End-to-end Python analysis (statsmodels/sklearn) |
| `/review-r [file]` | R code quality review (R scripts only) |
| `/capture-environment` | Record the runtime environment |
| `/diagnose` | Debug a failing build or script |

**Research**

| Command | What It Does |
|---------|-------------|
| `/lit-review [topic]` | Literature search + synthesis |
| `/research-ideation [topic]` | Research questions + strategies |
| `/interview-me [topic]` | Interactive research interview |
| `/review-paper [file]` | Manuscript review |

**Session and repo**

| Command | What It Does |
|---------|-------------|
| `/commit [msg]` | Stage, commit, PR, merge |
| `/checkpoint` | Save a session checkpoint |
| `/context-status` | Report context usage |
| `/compress-session` | Compress the session log |
| `/learn` | Record a [LEARN] entry to MEMORY.md |
| `/verify-claims` | Check stated claims against reality |
| `/deep-audit` | Full repo audit |

Run `ls .claude/skills` for the complete list. Gate scripts live in `scripts/`
(`check-*.py`); `scripts/backtest.sh` runs them all, though several are
template-maintenance gates that this course repo does not satisfy.

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
**Note:** The pre-redesign lecture set (Lecture01_Intro through Lecture12_Capstone) was removed in the Fall 2026 cleanup; it remains recoverable from git history. Its lab notebooks (`scripts/Lecture*.ipynb`) and QA reports (`quality_reports/`) were deliberately kept — the notebooks are the only worked Python in the repo outside Homework/.

| Lecture | Beamer | Quarto | Key Content |
|---------|--------|--------|-------------|
| 1: Intro, ETS & Forecast Evaluation | `Lecture01_ETS_Eval.tex` ✓ | `Lecture01_ETS_Eval.qmd` ✓ | SES, Holt, Holt-Winters, ETS framework, RMSE/MAE/MAPE/MASE, walk-forward CV, DM test. |
| 2: ARIMA, VAR & Multivariate Models | `Lecture02_ARIMA_VAR.tex` ✓ | `Lecture02_ARIMA_VAR.qmd` ✓ | Stationarity, ARIMA/SARIMA, auto-ARIMA, VAR, Granger causality, ARIMAX. |
| 3: Generalized Additive Models | `Lecture03_GAMs.tex` ✓ | `Lecture03_GAMs.qmd` ✓ | GAM structure, smoothing penalty, splines, Prophet, pyGAM, partial dependence plots. |
| 4: Decision Trees | `Lecture04_DecisionTrees.tex` ✓ | `Lecture04_DecisionTrees.qmd` ✓ | Bias-variance tradeoff, CART, entropy/information gain, sklearn, feature importance. |
| 5: Tree Ensembles — RF & Boosted Trees | `Lecture05_RandomForests.tex` ✓ | `Lecture05_RandomForests.qmd` ✓ | Bagging, bootstrap aggregation, feature subsampling, OOB error, MDI vs permutation importance, gradient boosting, XGBoost (Newton step, col subsampling). |
| 6: Regularization & Model Selection | `Lecture06_BoostedTrees.tex` ✓ | `Lecture06_BoostedTrees.qmd` ✓ | Subset selection vs shrinkage, Ridge, LASSO, Elastic Net, l1/l2 geometry, regularization paths, choosing λ by walk-forward CV. |
| 7: Introduction to Neural Networks | `Lecture07_NeuralNets.tex` ✓ | `Lecture07_NeuralNets.qmd` ✓ | Neurons, activations, FFN layers, MSE loss, backprop, Adam, dropout, PyTorch Dataset/DataLoader/training loop. |
| 8: CNN Architectures | `Lecture08_CNNs.tex` ✓ | `Lecture08_CNNs.qmd` ✓ | Convolution, pooling, LeNet→VGG→Inception→ResNet, residual connections, 1D CNN for time series. |
| 9: RNNs, LSTMs & Transformers | `Lecture09_RNNTransformers.tex` ✓ | `Lecture09_RNNTransformers.qmd` ✓ | Vanilla RNN, LSTM gates (forget/input/output/cell), attention, scaled dot-product, Transformer encoder, PyTorch nn.LSTM/nn.TransformerEncoder. |
| 10: Bayesian Statistics I — Foundations | `Lecture10_BayesianI.tex` ✓ | `Lecture10_BayesianI.qmd` ✓ | Frequentist vs Bayesian, Bayes' theorem, priors (Beta/Normal/Exponential), MCMC/NUTS, PyMC, prior predictive checks. |
| 11: Bayesian Statistics II — TS & Hierarchical | `Lecture11_BayesianII.tex` ✓ | `Lecture11_BayesianII.qmd` ✓ | Bayesian structural TS, local linear trend, Fourier seasonality, partial pooling, hierarchical models in PyMC. |
| 12: Bayesian Statistics III — Linear Regression | `Lecture12_BayesianIII.tex` ✓ | `Lecture12_BayesianIII.qmd` ✓ | Bayesian linear regression, posterior coefficient distributions, HDI, DAGs, scenario analysis, course method map. |

---

## Homework Assignments

**Dataset decision pending migration:** see
[`quality_reports/decisions/ADR-0001-course-dataset-architecture.md`](quality_reports/decisions/ADR-0001-course-dataset-architecture.md).
The spine moves from Rossmann to **M5/Walmart**, supplemented by FRED (L02 VAR/Granger),
electricity demand (L03 multiple seasonality), and Favorita (Week 16 shock cameo + project seed).
Do not restructure HW02–HW07 before that migration.

**Status:** All 8 assignments written (Spring 2026).
**Dataset:** Rossmann Store Sales (Kaggle) — 30 stores, weekly aggregated.
**Data prep:** Run `python scripts/prep_rossmann.py` once to generate `data/processed/rossmann_weekly.csv` and `data/processed/rossmann_daily.csv`.
**Format:** Quarto `.qmd` (students render to HTML). Each assignment includes an initial Codex prompt and per-question prompt budgets.
**Student repo:** https://github.com/DataHurdler/Forecasting-Env (Codex workflows, submission structure, validation script).

| HW | File | Lectures | Dataset | Prompt Budget | Key Tasks |
|----|------|----------|---------|---------------|-----------|
| 1a | `HW01_Part1_ETS.qmd` ✓ | L01 | Weekly, Store 1 | 4 | ETS (SES/Holt/HW), held-out RMSE/MAE |
| 1b | `HW01_Part2_ARIMA_VAR.qmd` ✓ | L02 | Weekly, Store 1 + Store 2 | 8 | ARIMA walk-forward CV, VAR, Granger causality, method comparison |
| 2 | `HW02_GAMs.qmd` ✓ | L03 | Daily, Store 1 | 10 | Prophet components + regressors, pyGAM splines, model comparison |
| 3 | `HW03_Trees_RF.qmd` ✓ | L04 + L05 | Weekly, 30 stores | 12 | Decision tree visualization, RF + OOB error, MDI vs permutation importance, walk-forward CV |
| 4 | `HW04_XGBoost_Regularization.qmd` ✓ | L06 | Weekly, 30 stores | 12 | XGBoost tuning, LASSO regularization path, Elastic Net vs Ridge, cross-model CV comparison |
| 5 | `HW05_DeepLearning.qmd` ✓ | L07 + L08 + L09 | Weekly, 30 stores (window=26/52) | 15 | PyTorch Dataset/DataLoader, FFN, 1D CNN, LSTM, Transformer + positional encoding, full course comparison |
| 6 | `HW06_Bayesian_TS_Hierarchical.qmd` ✓ | L10 + L11 | Weekly, Store 1 + 30 stores | 15 | Beta-Binomial prior predictive, Bayesian TS (Fourier), hierarchical partial pooling, shrinkage plot |
| 7 | `HW07_Bayesian_Regression.qmd` ✓ | L12 | Weekly, 30 stores | 15 | DAG construction, OLS benchmark, Bayesian regression, ROPE analysis, conditional simulation |
