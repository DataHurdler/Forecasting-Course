# QA Critic Report: Lecture03_ETS — Round 1
**Date:** 2026-03-06
**Beamer source:** `Slides/Lecture03_ETS.tex`
**Quarto source:** `Quarto/Lecture03_ETS.qmd`
**Workflow:** Adversarial Quarto vs. Beamer QA (Phase 1 Critic)

---

## Hard Gate Summary

| Gate | Status | Notes |
|------|--------|-------|
| Overflow — no content cut off | PASS | No structural overflow identified |
| Plot Quality — interactive >= static | PASS | SVG hand-coded replaces TikZ diagram faithfully |
| Content Parity — no missing slides/equations/text | PASS | All 14 content slides present; all equations reproduced |
| Visual Regression — Quarto >= Beamer on all dimensions | PARTIAL FAIL | See Issues 1, 3, 4 |
| Slide Centering — no jumping | PASS | `center: false` + `top: 0 !important` consistent |
| Notation Fidelity — all math verbatim from Beamer | PASS (minor gap) | See Issue 2 |

**Overall verdict:** NOT APPROVED — 2 critical issues, 3 major issues, 4 minor issues.

---

## Slide-by-Slide Comparison

### Title / Outline slides
- Quarto YAML metadata matches Beamer metadata exactly (title, subtitle, author, institute, date). ✓
- Outline slide uses an ordered list matching Beamer `\tableofcontents` items. ✓
- Section slides (`# ...`) render as centered gradient slides matching `\sectionslide{}{}`. ✓
- Section subtitle text (the tagline below the title) appears as a paragraph below `#` heading in Quarto, which is correct behavior for level-1 slides. ✓

### The Equal-Weight Problem
- OLS formula reproduced verbatim. ✓
- `warningbox` and `examplebox` with title "Business context" reproduced faithfully. ✓

### The Exponential Weighting Idea
- Table alignment in Quarto: column 2 (Age) is `text-anchor: center` in Beamer but uses `:---:` in Quarto — OK. ✓
- Weights-sum-to-1 sentence preserved. ✓
- `keybox` content preserved. ✓
- **ISSUE:** In Beamer, the keybox reads `\textbf{$\alpha \approx 1$}`: almost all weight... and `\textbf{$\alpha \approx 0$}`: long memory. — formatted as two separate bold-prefixed sentences. In Quarto (line 77), both are concatenated into a single sentence with no line break: "$\alpha \approx 1$: almost all weight on the latest value. $\alpha \approx 0$: long memory." The Beamer version puts `\quad` between them, creating visual spacing; the Quarto version runs them together as a single paragraph. This is **minor** — content preserved but spacing slightly reduced.

### Simple Exponential Smoothing (SES)
- `definitionbox` with title "Simple Exponential Smoothing" reproduced correctly. ✓
- Level equation, recursive expansion, muted footnote all verbatim. ✓

### The Error-Correction Form
- Error-correction equation reproduced verbatim. ✓
- SES≡ARIMA(0,1,1) note present (neutral/smaller). ✓
- `keybox` content correct. ✓
- Two-column alpha comparison reproduced with proper `{.columns}` / `{.column}` divs. ✓

### Estimating α and the SES Forecast
- Minimization equation reproduced correctly. ✓
- Citation `[@Hyndman2021, Ch. 8]` matches `\parencite[][Ch.~8]{Hyndman2021}`. ✓
- `warningbox` and Socratic note correct. ✓

### SES in Context: Boundary Cases
- `examplebox` with title "US Retail Sales (RSXFS)" reproduced. ✓
- Boundary-case table reproduced. Beamer uses `Na\"{i}ve` (produces "Naïve"); Quarto has "Naïve" directly — equivalent. ✓
- `keybox` with "SES nests..." reproduced. ✓

### Holt's Linear Method: Level and Trend
- `definitionbox` with title "Holt's Linear Exponential Smoothing" reproduced. ✓
- Level and Trend equations reproduced verbatim. ✓
- Citation `[@Holt2004]` matches `\parencite{Holt2004}`. ✓
- Two-column layout with interpretation + h-step forecast reproduced. ✓
- Muted SES-nesting note reproduced. ✓

### The Damped Trend
- Damped-trend equation reproduced verbatim. ✓
- `keybox` with φ boundary cases reproduced, including bold "Use damped by default for h > 6." ✓
- **ISSUE (Critical):** Beamer uses a TikZ `tikzpicture` for the damped vs Holt trend chart. Quarto replaces this with a hand-crafted inline SVG (lines 243–265). The SVG is mathematically correct (correct asymptote at ~122.67, correct curve shape for φ=0.85). However:
  - The SVG uses fixed pixel coordinates (`width="100%"` but `viewBox="0 0 320 210"`). At the declared slide width of 1280px, the SVG column occupies ~47% ≈ 600px; the SVG's intrinsic viewBox is 320×210, so it will scale up. The polyline data points for the damped curve (`40,174 65,164 105,155 149,147 193,140 257,130 300,125`) have only 7 sample points and produce a noticeably angular approximation of the smooth exponential-approach curve. The TikZ version uses `samples=50`, giving a smooth curve. The SVG approximation is visible as a polygon rather than a smooth curve.
  - **Severity: CRITICAL** — the chart quality is visually inferior to the Beamer version (violates Plot Quality gate).

### Three-Component Decomposition
- Additive HW model equation reproduced verbatim. ✓
- `definitionbox` with title "Holt-Winters Additive Update Equations" reproduced. ✓
- All three update equations verbatim. ✓
- Muted seasonal-index note reproduced. ✓

### Additive vs. Multiplicative Seasonality
- Two-column forecast equations reproduced. ✓
- Table with Additive/Multiplicative variants reproduced. ✓
- `examplebox` "US Retail Sales (RSXFS)" reproduced. ✓

### Estimation and Initialization
- Parameters and initialization strategies reproduced. ✓
- `warningbox` with 2m requirement reproduced. ✓
- Socratic note reproduced. ✓

### ETS: Error × Trend × Seasonal
- ETS taxonomy table reproduced. ✓
- **ISSUE (Major):** In Beamer, Trend options column reads "N, A, A\textsubscript{d}" (subscript d using LaTeX command). In Quarto (line 365), this is rendered as "N, A, A~d~" which uses Pandoc subscript markup — correct in HTML. ✓ But ETS model mapping in the two-column section (lines 377, 384) uses "A~d~" inline. This is correct for Quarto but verify it renders as subscript "d" and not as tilde-d. This is a rendering concern, not a source error — flagged for verification.
- `@Hyndman2021` used as sentence subject (line 360) — correctly renders as "Hyndman et al. (2021)" without parentheses. In Beamer, `\textcite{Hyndman2021}` is used — equivalent. ✓
- Two-column ETS mapping reproduced. ✓

### State Space Representation
- Two equations reproduced verbatim. ✓
- `\mathbf{x}_t` notation preserved. ✓
- `\varepsilon_t \overset{\mathrm{iid}}{\sim}` — Quarto version at line 395 uses `\overset{\mathrm{iid}}{\sim}` verbatim. ✓
- Two-column additive/multiplicative error comparison reproduced. ✓
- `keybox` reproduced. ✓
- Muted innovation note reproduced. ✓

### Automatic Model Selection via AIC
- AIC formula reproduced verbatim: `\mathrm{AIC} = -2\hat{L} + 2p` using `\hat{L}`. ✓
  - Note: the prior proofreading report (Lecture03_ETS_report.md) flagged the Beamer version for using `\hat{\ell}` (notation collision), and recommended `\hat{L}`. The Quarto version already uses `\hat{L}` (line 429), which is the CORRECT form. The Beamer `.tex` at line 449 also uses `\hat{L}` in the current source. Both are consistent and correct.
- Three-row ETS table reproduced (including `A~d~` subscript notation). ✓
- `keybox` with M4 Competition note reproduced. ✓
- Muted Lab 3 note reproduced (Python import path verbatim). ✓

### Key Takeaways
- **ISSUE (Major):** Beamer uses `{\small \setlength{\itemsep}{1pt} \begin{enumerate} ... \end{enumerate}}` inside a keybox with tight spacing. Quarto uses `{.keybox}` + `{.smaller}` + numbered list. This is structurally correct, but the `.smaller` class (85% font size) is applied as an inner div inside `.keybox`. The SCSS rule at line 547 does include `.keybox` in the `.smaller` context selectors, so padding/margin is reduced — however the nested-div pattern `{.keybox} {.smaller}` in Quarto means `.smaller` is a child element of `.keybox`, which may not trigger the `.smaller .keybox` SCSS rule (which targets a `.keybox` _inside_ `.smaller`). The correct SCSS cascade applies `.smaller` styles to `.keybox` when `.keybox` is _descendant_ of `.smaller`, not when `.smaller` is _descendant_ of `.keybox`. **The `.smaller` wrapper is inside `.keybox` in the QMD source (lines 453-465), which is the wrong nesting order.** The outer div should be `.smaller`, inner `.keybox` — or else use `{.keybox .smaller}` as combined classes on one div.
- Content of all 5 takeaway items reproduced. ✓
- Muted error-correction note reproduced. ✓

### What's Next: Stationarity and ARIMA
- Three bullet points on ETS limitations reproduced. ✓
- `keybox` Lecture 4 preview reproduced. ✓
- Lab 3 note reproduced. ✓
- **ISSUE (Minor):** In Beamer (line 523), the Lab 3 note is inside `\begin{center}...\end{center}` with `\muted{\small ...}`. In Quarto (line 485), it uses `::: {.neutral .smaller}`. The centering is lost — the Quarto version is left-aligned where Beamer was centered. This is a minor layout divergence.

### References
- References slide uses `{.smaller}` class and `{#refs}` div. ✓
- Bibliography is linked via `bibliography: ../Bibliography_base.bib`. ✓

---

## Issue Register

### CRITICAL Issues

**C1: Damped Trend SVG — Low sample point density produces angular curve**
- **Slide:** The Damped Trend
- **Beamer:** TikZ `\addplot` with `samples=50` producing a smooth exponential-approach curve
- **Quarto:** Hand-drawn SVG polyline with only 7 sample points (h=0,1,2,3,4,6,8,10,12 — but actually 7 points in the code) producing a visually angular approximation
- **Fix:** Add more intermediate points to the SVG polyline for the damped curve, or use a JavaScript/SVG path with Bezier curves for a smoother appearance. Minimum 12 sample points covering h=0 through h=12 in steps of 1.
- **Impact:** Violates Plot Quality hard gate — interactive/static chart is visually inferior to Beamer

**C2: `.smaller` nested inside `.keybox` — wrong nesting order on Key Takeaways slide**
- **Slide:** Key Takeaways
- **Beamer:** Tight spacing inside keybox via `\setlength{\itemsep}{1pt}` and `{\small ...}`
- **Quarto:** `{.keybox}` contains inner `{.smaller}` div — the SCSS `.smaller .keybox` rule applies reduced padding to a `.keybox` inside `.smaller`, but here `.smaller` is INSIDE `.keybox`, so the rule does not fire. Result: the keybox content may not receive compact spacing, risking visual overflow on a slide with 5 numbered items.
- **Fix:** Restructure as either (a) a single div with combined classes `{.keybox .smaller}` using Quarto attribute syntax, or (b) move `.smaller` outside `.keybox`. The correct QMD pattern is:
  ````
  ::: {.keybox .smaller}
  1. ...
  :::
  ````
- **Impact:** Potential content overflow on Key Takeaways slide; styling regression vs Beamer

---

### MAJOR Issues

**M1: Keybox alpha description — two items run together without visual spacing**
- **Slide:** The Exponential Weighting Idea
- **Beamer:** `\quad \textbf{$\alpha \approx 1$}: almost all weight... \quad \textbf{$\alpha \approx 0$}: long memory.`
- **Quarto:** Single paragraph — "$\alpha \approx 1$: almost all weight on the latest value. $\alpha \approx 0$: long memory."
- **Fix:** Use a line break or two separate paragraphs to separate the two parameter descriptions:
  ```markdown
  $\alpha \approx 1$: almost all weight on the latest value.

  $\alpha \approx 0$: long memory.
  ```
- **Impact:** Reduced visual clarity relative to Beamer

**M2: ETS A~d~ subscript — verify rendering**
- **Slide:** ETS: Error × Trend × Seasonal; Automatic Model Selection via AIC
- **Beamer:** `A\textsubscript{d}` renders as proper subscript in PDF
- **Quarto:** `A~d~` uses Pandoc subscript markup — correct if rendered, but must verify no render environment drops subscripts
- **Fix:** No source change needed; document as requiring HTML render verification. If `~d~` does not render in the deployed HTML, use `A<sub>d</sub>` as a fallback.
- **Impact:** Notation fidelity risk

**M3: Lab 3 "What's Next" note is left-aligned in Quarto vs. centered in Beamer**
- **Slide:** What's Next: Stationarity and ARIMA
- **Beamer:** `\begin{center}...\end{center}` wrapping the lab note
- **Quarto:** `::: {.neutral .smaller}` with no centering
- **Fix:** Add `text-align: center` via an inline style or a `.center` utility class:
  ```markdown
  ::: {.neutral .smaller style="text-align: center;"}
  **Lab 3:** Fit SES, Holt, Holt-Winters...
  :::
  ```
- **Impact:** Minor layout divergence; content is present

---

### MINOR Issues

**m1: Missing `\sectionslide` equivalent for "Key Takeaways and Roadmap" section**
- **Beamer:** The proofreading report (Issue 1 in Lecture03_ETS_report.md) already flagged that the Beamer `.tex` is missing a `\sectionslide` for section 6. The Quarto QMD includes `# Key Takeaways and Roadmap` as a level-1 heading (line 445), which correctly renders as a section slide. **The Quarto is actually MORE correct than the Beamer on this point.**
- **Action:** No Quarto fix needed; flag for Beamer fix separately.

**m2: Keybox text contrast — alpha descriptions use plain text (fine)**
- The prior proofreading report flagged `\pos` (green) inside `keybox` (blue) as a contrast failure in Beamer. In Quarto, the keybox text is plain (no `.positive` class applied), so the contrast issue does NOT exist in Quarto. The Quarto is correct here.

**m3: CSS — `.keybox` does not set `color: white` on `h3` or `h4` elements**
- The SCSS at line 295 sets `p, li, span, .math { color: white !important; }` inside `.keybox`, but does NOT include `h3, h4`. If a `###` or `####` heading appears inside a keybox, it would render in `$primary-blue` (dark blue on dark blue background). Not triggered in Lecture03, but structural gap.

**m4: Table column alignment inconsistency**
- **Slide:** Exponential Weighting Idea table
- **Beamer:** Three columns with `lcc` alignment (left, center, center)
- **Quarto:** Uses `|:---|:---:|:---|` — first column left, second center, third left-aligned. The "Weight" column in Beamer is center-aligned (`c`), but in Quarto the Weight column header and cells are left-aligned (`:---|`). This is a minor aesthetic divergence.

---

## Structural Checks

| Check | Result |
|-------|--------|
| All Beamer sections present as `#` section slides | PASS — 6 sections + title |
| All content slides present | PASS — 14 content slides |
| No missing equations | PASS |
| All `keybox`/`warningbox`/`examplebox`/`definitionbox` environments translated | PASS |
| All citations translated (parencite → [@...], textcite → @...) | PASS |
| All Socratic prompts present | PASS — 4 socratic notes |
| TikZ diagram replaced with web-compatible equivalent | PASS (SVG present, but quality issue C1) |
| SCSS theme matches Beamer color palette | PASS |
| No inline LaTeX commands leaked into QMD | PASS |
| `\mathrm{iid}` rendered correctly | PASS — `\overset{\mathrm{iid}}{\sim}` preserved |
| Footer text correct | PASS — "BSAD 8310 | University of Nebraska at Omaha | Spring 2026" |

---

## Issue Summary Table

| ID | Slide | Issue | Severity |
|----|-------|-------|----------|
| C1 | The Damped Trend | SVG polyline has only 7 sample points; curve is angular vs. smooth TikZ | CRITICAL |
| C2 | Key Takeaways | `.smaller` nested inside `.keybox` — wrong CSS nesting; compact styling may not apply | CRITICAL |
| M1 | Exponential Weighting Idea | Two α descriptions run together in keybox without spacing | MAJOR |
| M2 | ETS taxonomy / AIC selection | A~d~ subscript requires HTML render verification | MAJOR |
| M3 | What's Next | Lab 3 note is left-aligned in Quarto, centered in Beamer | MAJOR |
| m1 | Key Takeaways | Quarto has correct section slide; Beamer is the one missing it (no Quarto fix) | INFO |
| m2 | Exponential Weighting Idea | Contrast issue from Beamer keybox does NOT exist in Quarto (Quarto is correct) | INFO |
| m3 | N/A | CSS gap: `.keybox` does not force white on `h3`/`h4` headings | MINOR |
| m4 | Exponential Weighting Idea | Weight column alignment: Beamer center, Quarto left | MINOR |

---

## Recommendation

**Proceed to Phase 2 (Fixer).** Two critical issues require fixing before approval:

1. **C1:** Smooth the damped-trend SVG curve by adding more sample points (target: 13 points, h=0 through h=12 in integer steps).
2. **C2:** Restructure Key Takeaways to use `{.keybox .smaller}` combined-class div.

Major issues M1 and M3 should also be fixed (layout parity). M2 is a verification item.
