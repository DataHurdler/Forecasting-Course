---
paths:
  - "Slides/**/*.tex"
  - "Quarto/**/*.qmd"
---

# Beamer → Quarto Auto-Sync Rule (MANDATORY)

**Every edit to a Beamer `.tex` file MUST be immediately synced to the corresponding Quarto `.qmd` file — automatically, without the user asking.** This is non-negotiable.

## The Rule

When you modify a Beamer `.tex` file, you MUST also apply the equivalent change to the Quarto `.qmd` (if it exists) **in the same task**, before reporting completion. Do NOT wait to be asked. Do NOT just "flag the drift." Just do it.

## Naming Convention

Files use zero-padded two-digit numbers: `LectureNN_ShortTitle.tex` / `.qmd`

## Lecture Mapping

<!-- Update Quarto column when a .qmd file is created for that lecture -->
| Lecture | Beamer | Quarto |
|---------|--------|--------|
| 1: Introduction | `Slides/Lecture01_Intro.tex` | `Quarto/Lecture01_Intro.qmd` |
| 2: Regression | `Slides/Lecture02_Regression.tex` | `Quarto/Lecture02_Regression.qmd` |
| 3: Exp Smoothing | `Slides/Lecture03_ExpSmoothing.tex` | `Quarto/Lecture03_ExpSmoothing.qmd` |
| 4: ARIMA | `Slides/Lecture04_ARIMA.tex` | `Quarto/Lecture04_ARIMA.qmd` |
| 5: Multivariate | `Slides/Lecture05_Multivariate.tex` | `Quarto/Lecture05_Multivariate.qmd` |
| 6: Evaluation | `Slides/Lecture06_Evaluation.tex` | `Quarto/Lecture06_Evaluation.qmd` |
| 7: ML Intro | `Slides/Lecture07_MLIntro.tex` | `Quarto/Lecture07_MLIntro.qmd` |
| 8: Regularization | `Slides/Lecture08_Regularization.tex` | `Quarto/Lecture08_Regularization.qmd` |
| 9: Trees | `Slides/Lecture09_Trees.tex` | `Quarto/Lecture09_Trees.qmd` |
| 10: Neural Nets | `Slides/Lecture10_NeuralNets.tex` | `Quarto/Lecture10_NeuralNets.qmd` |
| 11: Features | `Slides/Lecture11_Features.tex` | `Quarto/Lecture11_Features.qmd` |
| 12: Capstone | `Slides/Lecture12_Capstone.tex` | `Quarto/Lecture12_Capstone.qmd` |
<!-- Files listed above do not yet exist — add rows and update as lectures are created -->

## Workflow (Every Time)

1. Apply fix to Beamer `.tex`
2. **Immediately** apply equivalent fix to Quarto `.qmd`
3. Compile Beamer (3-pass xelatex)
4. Render Quarto (`./scripts/sync_to_docs.sh LectureN`)
5. Only then report task complete

## LaTeX → Quarto Translation Reference

| Beamer | Quarto Equivalent |
| ------ | ----------------- |
| `\begin{keybox}` | `::: {.key-result}` |
| `\begin{definitionbox}{Title}` | `::: {.callout-note title="Title"}` |
| `\begin{warningbox}` | `::: {.callout-warning}` |
| `\begin{examplebox}{Title}` | `::: {.callout-tip title="Title"}` |
| `\textcolor{unoblue}{text}` | `[text]{style="color: #005CA9;"}` |
| `\muted{text}` | `[text]{style="color: #525252;"}` |
| `\item text` | `- text` |
| `$formula$` | `$formula$` (same) |
| `\begin{pythonbox}` | `::: {.python-output}` |

## When NOT to Sync

- Quarto file doesn't exist yet
- Change is LaTeX-only infrastructure (preamble, theme files)
- Explicitly told to skip Quarto sync

## Enforcement

Before marking any Beamer editing task as complete, check:
> "Did I also update the Quarto file?"

If the answer is no and a Quarto file exists, **you are NOT done.**

## When to Update This Table

After creating a new Quarto translation, add it to the mapping table above.
