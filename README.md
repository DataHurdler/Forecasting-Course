# ECON 8310: Business Forecasting

Course materials for **ECON 8310 — Business Forecasting**, University of Nebraska at Omaha,
Fall 2026. Taught by [Zijun Luo](https://www.luozijun.com/).

Lecture slides are authored in Beamer and mirrored to RevealJS; both are published to
GitHub Pages from `docs/`. All course code is Python.

---

## What's Here

| Path | Contents |
|------|----------|
| `Slides/` | Beamer `.tex` sources and compiled PDFs — **authoritative** |
| `Quarto/` | RevealJS `.qmd` mirrors + `emory-clean.scss` theme |
| `Homework/` | 7 assignments as Quarto `.qmd` |
| `docs/` | Published GitHub Pages site (slides, homework, index) |
| `Preambles/header.tex` | Shared LaTeX preamble — UNO palette, custom boxes |
| `Bibliography_base.bib` | Centralized bibliography (46 entries) |
| `scripts/` | Build/sync utilities, data prep, repo gate checks |
| `quality_reports/` | Plans, session logs, merge reports |
| `.claude/` | Claude Code workflow: skills, agents, hooks, rules |
| `ECON8310Syllabus2026Fall.md` | Course syllabus |

---

## Lectures

| # | Topic |
|---|-------|
| 1 | Introduction, Exponential Smoothing & Forecast Evaluation |
| 2 | ARIMA, VAR & Multivariate Models |
| 3 | Generalized Additive Models |
| 4 | Decision Trees |
| 5 | Tree Ensembles: Random Forests & Boosted Trees |
| 6 | Regularization & Model Selection |
| 7 | Introduction to Neural Networks |
| 8 | CNN Architectures |
| 9 | RNNs, LSTMs & Transformers |
| 10 | Bayesian Statistics I — Foundations |
| 11 | Bayesian Statistics II — Time Series & Hierarchical Models |
| 12 | Bayesian Statistics III — Bayesian Linear Regression |

Textbooks (both free online): *Forecasting: Principles and Practice, the Pythonic Way*
([fpppy](https://otexts.com/fpppy/)) and *An Introduction to Statistical Learning with
Applications in Python* ([ISLP](https://www.statlearning.com/)) for Lectures 4–6.
The syllabus carries a full lecture-to-chapter reading map.

---

## Building

**Slides (Beamer, XeLaTeX only, 3 passes):**

```bash
cd Slides
TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode LectureNN_Title.tex
BIBINPUTS=..:$BIBINPUTS bibtex LectureNN_Title
TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode LectureNN_Title.tex
TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode LectureNN_Title.tex
```

**Quarto → GitHub Pages:**

```bash
./scripts/sync_to_docs.sh LectureNN_Title
```

**Homework data** (run once; requires the Rossmann Store Sales files in `data/raw/`):

```bash
python scripts/prep_rossmann.py
```

**Quality score:**

```bash
python scripts/quality_score.py Quarto/LectureNN_Title.qmd
```

---

## Conventions

- **Beamer is the single source of truth.** `Quarto/*.qmd` mirrors it; when they diverge,
  the `.tex` wins. Parity check: a lecture's `.qmd` should have exactly one fewer `##`
  slide than its `.tex` has `\begin{frame}` (the title frame).
- **Python-first.** `random_state=42` throughout.
- **Quality gates:** 80 to commit, 90 to deploy, 95 aspirational.
- **Plan first** for non-trivial work; plans live in `quality_reports/plans/`.

See [CLAUDE.md](CLAUDE.md) for the full working agreement and skill reference.

---

## Acknowledgements

The Claude Code workflow in `.claude/` — skills, agents, hooks, and rules — comes from
[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)
(v2.5.1), by Pedro H. C. Sant'Anna, used under the MIT License. Course content is the
instructor's own.
