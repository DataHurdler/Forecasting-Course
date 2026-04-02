# Session Log: Lecture 12 — Capstone & Applications
**Date:** 2026-03-02
**Branch:** main
**Goal:** Create Lecture 12 (Capstone & Applications), compile, generate companion notebook, review, and fix.

---

## Work Completed

### 1. Created `Slides/Lecture12_Capstone.tex`
Full 24-frame Beamer deck covering:
- **Course Synthesis:** Two-part toolkit map (L01–L11), five-question Decision Framework, five failure modes
- **Combining and Testing:** Equal-weight combination result (RMSE = 2,080), DM pairwise significance matrix
- **RSXFS Final Leaderboard:** All 11 methods table, DM interpretation, 2-model deployment pipeline
- **Case Study (RESGAS):** Utility demand forecasting, framework application, domain transfer analysis
- **Communication & Deployment:** Stakeholder summary, monitoring four-check procedure
- **Takeaways:** Six capstone takeaways with full citations

### 2. Compiled (3-pass XeLaTeX)
- 24 pages, zero overfull hbox warnings, all citations resolved
- Windows-specific compilation command required: `cmd //c "cd /d Slides && xelatex -interaction=nonstopmode FULL_PATH_TO_FILE.tex"` — the bash `cd` does not change the Windows working directory for xelatex

### 3. Created `scripts/Lecture12_Capstone.ipynb`
Python notebook covering the two case studies:
- **Section 1:** RSXFS final leaderboard (11-model comparison)
- **Section 2:** Forecast combination + DM test
- **Section 3:** RESGAS utility demand study
- **Section 4:** Decision framework applied to both datasets
- **Section 5:** Communication — stakeholder summary + monitoring

### 4. Proofreader review — 12 issues found
Reports saved to `quality_reports/Lecture12_Capstone_report.md`.

Critical issues fixed:
- Factual error: "combination beats XGBoost on MAE" was false (1,530 > 1,510)
- 2-model vs 3-model combination inconsistency in pipeline slide

Major issues fixed:
- "30-unit RMSE gain" → 160-unit corrected to reflect LSTM vs. combination delta
- `\hat{y}` → `\yhat` macro
- "Synthesising" → "Synthesizing" (British → American English)
- Undefined symbol $m$ → added "(the seasonal period, $m = 12$)" gloss

Minor issues fixed:
- "auto-AIC" → "auto-AICc"
- "adversarial" → "demanding"
- "Weekly"/"Monthly" → "Weekly refit"/"Monthly refit" (clarifies cadence vs. series frequency)
- Lowercase sentence-start in failure modes enumerate
- "within 8%" → "within 9%" (8.33% rounds up)

### 5. Pedagogy review — 3 patterns violated
Report saved to `quality_reports/Lecture12_Capstone_pedagogy_report.md`.

Key pedagogy fixes applied:
- **Socratic questions (Pattern 11 violation):** Added two questions:
  - Slide 5 (Decision Framework): Refit cadence question
  - Slide 17 (RESGAS leaderboard): COVID test-period question
- **DM formula recall (Pattern 7 partial):** Added two-line formula reminder at top of DM matrix slide
- **Forward pointer:** Added link from leaderboard slide to DM interpretation slide

Remaining items (minor, tracked in report but not blocking):
- Zero TikZ figures (below visual target, but capstone text density is appropriate)
- keybox count 62% vs 50% target (borderline, no action taken)
- Prediction interval construction method not shown (noted for future reference)

### 6. Recompile after fixes
- 3-pass XeLaTeX: clean, 24 pages, no warnings

---

## Key Technical Decision: Pipeline Combination Clarification
The original draft had an internal inconsistency: slide 8 described a 3-model combination (SARIMA + XGBoost + LSTM, RMSE = 2,080), but slide 13's deployment pipeline formula used only 2 models (SARIMA + XGBoost). Resolution: added a preamble sentence to slide 13 explicitly stating the production pipeline drops LSTM for operational simplicity, and rewrote the muted note to give the correct RMSE comparison (LSTM alone at 1,920 beats combination by 160 units, not 30).

---

## Compilation Workaround (Windows)
**Problem:** `cd Slides && TEXINPUTS=../Preambles:$TEXINPUTS xelatex file.tex` fails in Git Bash because xelatex (a Windows executable) doesn't use the bash working directory.

**Solution:**
```bash
# Pass 1
cmd //c "cd /d C:\path\to\Slides && xelatex -interaction=nonstopmode C:\path\to\Slides\file.tex"

# BibTeX (needs to cd first; do NOT override BIBINPUTS — .aux already has ../Bibliography_base)
cmd //c "cd /d C:\path\to\Slides && bibtex file"

# Passes 2 and 3 (same as pass 1)
```

---

## Open Questions / Future Work
- No TikZ fan chart for prediction intervals (L11 promise of "presentation-ready visualizations" partially unfulfilled)
- Lecture 12 is the only deck with a perfect `\sectionslide` record — retroactive application to L09–L11 would improve those decks
- The RESGAS case study notes that Holt-Winters was omitted without explanation; a future revision could add a sentence

---

## Quality Assessment
| Metric | Result |
|--------|--------|
| Compilation | Clean (24 pages, 0 warnings) |
| Proofreader critical fixes | 2 of 2 resolved |
| Proofreader major fixes | 4 of 4 resolved |
| Pedagogy violations fixed | 1/3 fully (Socratic), 1/3 partial (DM recall) |
| Estimated quality score | ~87/100 |
