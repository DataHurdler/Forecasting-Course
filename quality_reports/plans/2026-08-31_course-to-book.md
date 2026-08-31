# Plan: turn the course into a book website

**Date:** 2026-08-31 · **Status:** DRAFT — awaiting owner decisions
**Model:** https://www.luozijun.com/Econ-ML-Book/ (owner's existing book; built with **bookdown**)
**Ask:** not a portal around the existing files — *write a book* from the materials and publish it.

---

## 1. What we already have

| Asset | Count | Words | Role in the book |
|---|---:|---:|---|
| Deck narration scripts | 15 | **56,421** | **The draft prose.** Already in the author's voice |
| Lab narration scripts | 10 (of 14) | 26,232 | Worked-example walkthroughs |
| Homework solution scripts | 5 | 6,394 | Exercise discussion |
| Beamer decks / Quarto mirrors | 15 / 15 | — | Chapter skeletons, figures, TikZ |
| Labs (`.qmd`, executable) | 14 | — | Runnable worked examples |
| Homework (`.qmd`) | 11 | — | End-of-chapter exercises |
| Student-facing docs | 8 | — | Front matter (setup, AI policy, syllabus) |

**The finding that shapes this plan:** the narration corpus is **~89,000 words** — already a
250–300 page book, already written in the author's voice, and already verified line-by-line
against measured output during the scripting pass. This is not a write-from-scratch project. It
is a **voice conversion and restructuring** project on an existing draft.

## 2. Tech stack — recommendation: **Quarto Book**

The reference site is bookdown. Quarto Book is its direct successor (same author, same company,
same visual family), and it is the right choice *here* specifically:

- The repo is **already Quarto**: 15 mirrors, 14 labs, 11 assignments. No new toolchain.
- The course is **Python-first**; bookdown would drag in R for no benefit.
- Native sidebar navigation, full-text search (bookdown's site has none), cross-references,
  `Bibliography_base.bib` citations, callout blocks matching the existing `.keybox` house style,
  and optional PDF/EPUB from the same source.
- Executable chapters with **`freeze: auto`**, which the build strategy below depends on.

Rejected: bookdown (R dependency), Jupyter Book (third toolchain, no gain), mkdocs/Hugo (no
executable code, no citation handling).

## 3. Proposed structure

Not 15 chapters mirroring 15 lectures — the reference book uses 6 chapters with 10–12 sections.

| Part | Chapters | Source |
|---|---|---|
| **Front** | Preface · How to use this book · Setup · Working with an AI assistant | README, QUARTO_GUIDE, STUDENT_QUICKSTART, AI_POLICY |
| **I. The forecasting problem** | Benchmarks and evaluation · Why the naive model is a real competitor | L01 |
| **II. Classical time series** | ETS · ARIMA, VAR, Granger | L01, L02 |
| **III. Flexible regression** | GAMs, Prophet, several seasons at once | L03 |
| **IV. Trees** | Single trees · Bagging, forests, boosting | L04, L05 |
| **V. Regularization** | Breaking OLS · Ridge, LASSO, elastic net, choosing λ | L06 |
| **VI. Neural networks** | Feedforward · Convolution · Recurrence · Attention | L07, L08, L09 Pt 1–2 |
| **VII. Bayesian methods** | Foundations · Structural time series · Hierarchy · Regression | L10, L11 Pt 1–2, L12 |
| **VIII. What the measurements taught** | The scoreboard · Silent failures · Choosing a method | L13 |
| **Back** | Exercises · Datasets · Reproducing every number | Homework, ECON8310_Datasets |

**The book's spine, and its selling point:** every method measured on *one* panel, with a running
scoreboard, and every counter-intuitive result explained from the data. Few textbooks report a
46-coefficient LASSO beating four neural architectures and then explain *why* with a variance
decomposition. That is the differentiator — see the standing audit in the memory note
`audit-counterintuitive-results-after-narrations`.

## 4. The central risk: a third copy

Beamer is authoritative, Quarto mirrors it (parity-checked by `check_mirror_parity.py`), and
narration is a third rendering. **Book chapters would be a fourth.** Today's RNN-vs-LSTM
correction had to be applied in eight places; at four renderings that becomes routine.

The drift is never in the prose — it is in **numbers and claims**. So the fix is not a style
rule, it is a single machine-readable source:

> **`results/measured.yml`** — every reported number (scoreboard RMSEs, parameter counts,
> convergence tables, diagnostics) with its provenance: which script produced it, at what seed,
> at what budget. Decks, labs, narration and book all cite it; a checker (`check_measured.py`,
> alongside `check_mirror_parity.py`) fails when a document quotes a number that is not in it or
> disagrees with it.

This is worth building **before** the book, because it retro-fixes the existing four-way drift.

Two options for the prose itself:

- **(a) Derive-and-freeze (recommended for v1).** The book is a per-term snapshot generated from
  decks + narration and not hand-edited afterwards. Cheap; the book cannot outgrow the course.
- **(b) Invert the source of truth.** The chapter becomes canonical and decks derive from it.
  Correct if the book is meant to outlive the course; a much larger change.

Recommend (a) now, with (b) as a documented promotion path.

## 5. Build and reproducibility

- `freeze: auto`, with `_freeze/` **committed**, so a rebuild does not re-execute torch/pymc and
  the site can build without the full environment.
- Full cold build ≈ **45–60 min** (Lab 8 ≈ 8, Lab 9 Pt 2 ≈ 6, the Bayesian labs are MCMC). Warm
  builds should be seconds.
- Labs are **included**, never copied: `{{< include ../Labs/LectureNN_lab.qmd >}}`.
- Slides embedded as iframes with a full-screen link, so the decks stay the decks.

## 6. Publishing

- Lives in `book/` inside this repo (shares `Bibliography_base.bib`, `Figures/`, `data/`).
- Renders to `docs/book/` → e.g. `https://www.luozijun.com/forecasting-book/`.
- **A second canonical URL.** `scripts/set_course_url.py` now spans two repos and one URL; a book
  URL needs the same treatment or it will drift exactly as the student repo did (2026-08-26 →
  2026-08-31).

## 7. Phasing

| Phase | Work | Gate |
|---|---|---|
| **0** | Owner decisions (§8); `_quarto.yml` skeleton; **one chapter end-to-end** — recommend Lecture 9 Part 1, the richest and freshest | Owner likes the chapter's voice and shape |
| **1** | `results/measured.yml` + `check_measured.py`; back-fill every existing number | Checker passes on decks, labs, narration |
| **2** | Narration → chapter prose, 15 lectures | Each chapter reviewed |
| **3** | Fold labs in as worked examples (include, not copy) | Warm build clean |
| **4** | Front and back matter; exercises; scoreboard appendix | Full cold build |
| **5** | Publish; link from the course site; extend the URL tooling | Links checked |

Phase 2 is the bulk: ~56k words of spoken-register prose to convert. Roughly one lecture per
working session.

## 8. Open decisions (owner)

1. **Identity** — course companion (assumes the syllabus, keeps "Homework 4 asks you to…"), or a
   standalone book that a stranger can read? This changes every cross-reference.
2. **Voice** — narration is second-person spoken with stage directions (`[pause]`,
   `*(Screen: …)*`). Convert to book prose (recommended), or keep a lecture-transcript register?
3. **Exercises** — do the 11 assignments appear in the book? They are graded, they live in the
   student repo, and the narration includes solution discussion. Publishing solutions to
   assignments still in use is a real hazard.
4. **URL** — `/forecasting-book/` beside the course site, or does the book replace the course
   site as the front door?

## 9. Opportunity worth naming

The **AI-use policy** — per-assignment prompt budgets, a required prompt log, "do not let the
assistant ghostwrite interpretations" — is unusual, road-tested material. A short chapter on
using an AI assistant on empirical work without laundering it would be one of the more
distinctive things in the book, and no forecasting textbook currently has one.

---

## 10. Owner ruling, 2026-08-31: the book must match the decks *exactly*

> "All the graphs, tables, and important statements should match exactly like the decks."

This is a hard constraint, and it **settles §4**: derive-and-freeze prose is not sufficient,
because a frozen copy drifts the moment a deck is corrected — as five files did today. Exactness
has to be structural, not editorial. Three consequences:

**Tables.** No table is retyped into a chapter. Every reported table is generated from
`results/measured.yml` (§4) and rendered into *both* the deck and the book from that one source.
Where a deck's table is currently hand-written LaTeX, it gets back-filled into the results file
first. This is now a prerequisite for the book, not an optional tidy-up.

**Graphs.** The book consumes the deck's own artifacts — the existing TikZ → PDF → SVG pipeline
(`/extract-tikz`), and for computed figures the same script that the lab runs. No redrawing, no
"equivalent" plot. If a figure exists only inside a deck, extract it to a shared asset first.

**Important statements.** Extend the parity idea from structure to substance. Today
`check_mirror_parity.py` compares frame counts; a claim-level checker should verify that a
statement quoting a number agrees with `results/measured.yml`, and that a claim carrying a
qualifier in the deck carries it in the book too. The RNN-vs-LSTM correction is the worked
example: the qualifier "at a fixed 30-epoch budget" had to reach eight files, and nothing but
grep would have caught a miss.

**Revised phasing.** Phase 1 (`results/measured.yml` + checker + figure extraction) is promoted
to a **blocking prerequisite** for Phase 2. Writing chapters before the shared-artifact layer
exists guarantees a fourth copy of every number.

---

## 11. Revision 2 — owner ruling, 2026-08-31 (supersedes §3, §4's (a)/(b) choice, and §7)

> "This book accompanies the course, so **chapter titles need to match exactly** too. The first
> version should just be **stitching all existing materials together in a logical and fluent
> way** — a perfect substitution for the course materials we have already built, just another
> format."

**This changes what v1 *is*.** §1–§2 stand (inventory, Quarto Book). The rest is rewritten below.

### 11.1 v1 is an assembly problem, not an authoring problem

The 56k-word voice-conversion pass in §7 Phase 2 is **out of scope for v1**. Nothing gets
rewritten. The book is the same material in book form, and its correctness requirement is
"identical to the deck," which is achievable only if we do not retype anything.

### 11.2 The structure is the course's structure

Chapters **are** lectures, titled **verbatim**, in course order — `Lecture01_ETS_Eval.tex`'s
title becomes the chapter title, character for character. Parts group them the way the syllabus
groups weeks. No thematic reorganization, no merging L09 Part 1 and Part 2, no renumbering.

```
Front    Syllabus · Setup and Quarto guide · Working with an AI assistant · How to use this book
Ch 1-15  One per lecture, title verbatim:
           N.1  The lecture     deck content + deck narration
           N.2  The lab         lab .qmd (included) + lab narration
           N.3  The assignment  homework .qmd (included), where one exists
Back     Datasets · Project rubric · The scoreboard · Reproducing every number
```

### 11.3 The stitch that makes it fluent — and it already exists

The deck narration is written **slide by slide**, with headings `# ▶ SLIDE n — Title` that match
the deck's frame titles; the Quarto mirror carries the same titles as `## Title`. **The two join
on the title.** So a chapter section is mechanically assemblable:

> the slide's own content (its table, figure, keybox — from the parity-checked mirror)
> **+** that slide's narration as the connecting prose.

This is why the result reads as a book rather than as slides pasted into a page: the narration is
already the explanatory text a reader needs between one exhibit and the next. It was written for
exactly this job, just for the ear instead of the eye.

The same join works for labs: lab narration uses `▶ STEP n — Title` matching the lab's own
`# Step n — Title`.

### 11.4 Therefore: build a generator, not chapters

**No chapter is hand-written or hand-edited.** `scripts/build_book.py` assembles
`book/chapters/*.qmd` from the four sources at build time, and the generated directory is
disposable. This is what satisfies §10's exactness ruling *structurally* rather than by
discipline: a figure, table or statement cannot drift from the deck because it is never copied —
it is read from the deck's own mirror on every build.

Transform rules the generator applies to narration (the only text processing in v1):

| Narration element | In the book |
|---|---|
| `**[pause]**`, `*(Screen: …)*`, `*(Point at …)*` | dropped |
| `**[STOP — learner works]**` | becomes a "Try it" callout |
| `# ▶ SLIDE n — Title` / `▶ STEP n — Title` | section heading, or dropped where the mirror supplies it |
| "How to use this document", "things to know before recording", correction notes | dropped — instructor-facing |
| Second-person spoken register | **kept** — v1 reads as a lecture in prose, which is the point |

### 11.5 Revised phasing

| Phase | Work | Gate |
|---|---|---|
| **0** | Finish the four outstanding lab narration scripts (11 Pt 1, 11 Pt 2, 12 — and 1–3 predate the current format, check them) | Narration complete for all 14 labs |
| **1** | `build_book.py` + `_quarto.yml`; **one chapter end-to-end** — Lecture 9 Part 1 | Owner approves the assembled chapter |
| **2** | Generate all 15 lecture chapters; fix the joins that do not line up | Every slide title matched to narration |
| **3** | Front and back matter from the existing documents | Cold build clean |
| **4** | Publish to `docs/book/`; extend the URL tooling | Links checked |

Phase 0 is **already in progress** — it is the current lab-narration work, which is now a
prerequisite for the book rather than a parallel task.

### 11.6 What this defers

`results/measured.yml` (§4, §10) is **not needed for v1**, because a generator that reads the
deck cannot disagree with the deck. It becomes necessary at v2, when chapters are edited by hand
and the guarantee moves from structural to checked. Recorded so the reasoning is not lost.
