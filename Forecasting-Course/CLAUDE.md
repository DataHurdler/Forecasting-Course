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

**Beamer status:** All 12 lectures complete, reviewed, and compiled (0 errors).
**Quarto status:** All 12 lectures translated.

| Lecture | Beamer | Quarto | Key Content |
|---------|--------|--------|-------------|
| 1: Introduction to Forecasting | `Lecture01_Intro.tex` ✓ | `Lecture01_Intro.qmd` ✓ | Point/interval/density forecasts, benchmark models, evaluation setup. |
| 2: Regression-Based Forecasting | `Lecture02_Regression.tex` ✓ | `Lecture02_Regression.qmd` ✓ | OLS forecasting, prediction intervals, AR models, pitfalls. |
| 3: Exponential Smoothing | `Lecture03_ETS.tex` ✓ | `Lecture03_ETS.qmd` ✓ | SES, Holt, Holt-Winters, ETS taxonomy, AIC selection. |
| 4: ARIMA Models | `Lecture04_ARIMA.tex` ✓ | `Lecture04_ARIMA.qmd` ✓ | Stationarity, unit roots, ADF/KPSS, ACF/PACF, ARIMA/SARIMA, auto-ARIMA. |
| 5: Multivariate Methods | `Lecture05_Multivariate.tex` ✓ | `Lecture05_Multivariate.qmd` ✓ | VAR, ARIMAX, Granger causality, cointegration, ECM. |
| 6: Forecast Evaluation | `Lecture06_Evaluation.tex` ✓ | `Lecture06_Evaluation.qmd` ✓ | RMSE/MAE/MAPE/MASE, walk-forward CV, DM test, combination. |
| 7: ML Introduction | `Lecture07_MLIntro.tex` ✓ | `Lecture07_MLIntro.qmd` ✓ | Bias-variance, train/val/test, TimeSeriesSplit CV, pipeline. |
| 8: Regularization | `Lecture08_Regularization.tex` ✓ | `Lecture08_Regularization.qmd` ✓ | Ridge, LASSO, Elastic Net, coordinate descent, validation curve. |
| 9: Tree-Based Methods | `Lecture09_Trees.tex` ✓ | `Lecture09_Trees.qmd` ✓ | CART, Random Forests, XGBoost, feature importance. |
| 10: Neural Networks | `Lecture10_NeuralNets.tex` ✓ | `Lecture10_NeuralNets.qmd` ✓ | FFN, RNN, LSTM gates, vanishing gradient, attention, Keras implementation. |
| 11: Feature Engineering | `Lecture11_Features.tex` ✓ | `Lecture11_Features.qmd` ✓ | Lag features, rolling stats, leakage-free pipeline, LASSO importance. |
| 12: Capstone & Applications | `Lecture12_Capstone.tex` ✓ | `Lecture12_Capstone.qmd` ✓ | Decision framework, RSXFS leaderboard, RESGAS case study, deployment. |

<!-- Update Quarto column as lectures are translated -->
