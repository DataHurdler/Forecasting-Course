# Make the public site UNO-agnostic

**Status:** APPROVED — in progress
**Date:** 2026-09-01

## The principle (instructional designer, agreed by the owner)

- Lecture videos live on **Canvas only**.
- Syllabus, assignments, project instructions and rubric have a **copy on Canvas**.
- The **public site carries all the materials and nothing UNO-specific**. A student arriving
  from Canvas is warned that policies, dates and grading live on Canvas, not here.

This also settles the fall/spring modality problem as a side effect: room, meeting time,
deadlines anchored to "before class begins", the industry panel and the in-class presentation
are all *enrollment* facts, so they move to Canvas and stop being a public-site concern.

## Owner decisions taken

- Keep the site **organized by week**, but with **no calendar dates**.
- The four (now five) orphaned syllabus items go to a **new public "About this course" page**.

## What changes

### 1. New page — `ABOUT.md` → `docs/files/about.html`

Holds the five things that exist nowhere but the syllabus, all modality-neutral:

| From the syllabus | Why it is course substance |
|---|---|
| Course goals (6 outcomes) | what the material claims to teach |
| Prerequisites | what it assumes you know |
| **Textbook discussion** | the landing page has a 4-row table; the *rationale* — why ISLP, why BMCP, the level note, the three further free resources — is syllabus-only |
| BMCP level note | "you are not responsible for the derivations" |
| Difficulty and pacing note | how to use the material |

### 2. Landing page — dates out, week structure kept

Driven from `scripts/site.yml`, so this is a data edit plus a template tweak.

| Element | Now | After |
|---|---|---|
| `date:` on 17 weeks | `Aug 27, 2026` … | removed |
| assignment line | `due Week 2 · Sep 3` | `due Week 2` |
| assignments table, Due column | `Sep 3`, `Sep 10` … | `Week 2`, `Week 3` … |
| due badges (12) | already date-free | unchanged |
| `Final Exam Week` label | dated `Dec 17` | `Week 17` |

Week notes, one by one:

| Week | Note | Verdict |
|---|---|---|
| 2 | industry panel, 6:00–7:30pm; Lab 2 self-paced | **Canvas** — a fall-section event |
| 5 | online/asynchronous, no in-person meeting, lecture posted as a recording | **Canvas** — section-specific, and the recording is Canvas-only by policy |
| 6 | "final project rubric distributed" | **drop** — the rubric is permanently on the site |
| 9 | "final project proposal due" | **keep** — a milestone in the sequence |
| 13 | "Not this: FPP Ch. 11 is reconciliation, not pooling" | **keep** — pure course substance |
| 16 | "No lab this week…bring your project and your questions" | **keep, reworded** — "no lab" is structure; "bring" is in-person |
| 17 | "Dec 18: final project report due" | **keep, undated** |

### 3. Strip term/modality language from the four other public documents

| File | Fix |
|---|---|
| `ECON8310_Project_Rubric.md` | drop "Fall 2026"; "described in the syllabus" → describe them here; "**In-Class** Presentation" → "Project presentation"; "Questions go to the Canvas discussion board" → neutral |
| `ECON8310_Datasets.md` | drop "Fall 2026"; "in-class demonstrations" → "lecture demonstrations" |
| `STUDENT_QUICKSTART.md` (student repo) | "in-class lab" → "lab" |
| landing page | keep the "(with AI)" title; add the Canvas banner (below) |

### 4. Remove `docs/files/syllabus.html` from the public site

`sync_to_docs.sh` stops rendering it; the landing page's document table swaps the syllabus row
for **About this course**. `ECON8310Syllabus2026Fall.md` stays in the repo — it is still the
source for the Canvas copy — it simply stops being published.

`check-site-index.py` enforces the rest: if the syllabus row is removed but the file is still
published, the gate fails as an orphan.

### 5. Canvas → public-site banner

One callout on the landing page: this site holds the course materials; dates, grading,
policies, recordings and submission live on Canvas for enrolled students.

## The break week — resolved

**Owner's technique, adopted:** the break week is **named, not numbered**, and the numbering
continues across it. That is what makes Canvas and the public site agree in both terms:

```
FALL, on Canvas          SPRING, on Canvas        PUBLIC SITE (both terms)
  Week 13 · L11 Pt 2       Week 8  · L8             Week 13 · Lecture 11 Part 2
  Thanksgiving Week        Spring Break             Week 14 · Lecture 12
  Week 14 · L12            Week 9  · L9 Pt 1        Week 15 · Lecture 13
  Week 15 · L13            …                        Week 16 · Presentations
  Week 16 · Presentations  Week 16 · Presentations
```

Because the break consumes no number, teaching-week numbers are continuous and term-independent:
Canvas's Week 14 is the site's Week 14 in both semesters, whatever the break is called and
wherever it falls. **The break card lives on Canvas only** — on the public site it would be the
one fall-specific fact we are removing, and wrong in name and position for spring.

Consequence here: the old Week 14 row is dropped and weeks 15/16/17 become **14/15/16**. The
`due Week 15` and `due Week 16` assignment references move with them. Each card also names its
lecture, so a card identifies itself even if a reader's calendar has drifted.

## Verification

- `python3 scripts/build_index.py && python3 scripts/check-site-index.py`
- `./scripts/backtest.sh` green
- `python3 scripts/check_links.py`
- grep the published `docs/` tree for `unomaha`, `Canvas`, `Fall 2026`, `in-class`, `Mammel`,
  and every month name — the result should be the banner and nothing else


---

## Executed 2026-09-01

- **`ECON8310_About.md` → `docs/files/about.html`** — course description, the six outcomes,
  prerequisites, the full textbook discussion (both editions, the Ch. 12 numbering trap, the
  Ch. 14/15 Python-only note, ISLP, BMCP, the level note, the three further resources), pacing,
  and how the material is organised.
- **Schedule** — 17 dated weeks → **16 undated teaching weeks**. The break row is gone; weeks
  15/16/17 renumbered to 14/15/16; every card now carries its **lecture name** where the date
  used to sit; assignment lines are `due Week N`; the assignments table's Due column is weeks,
  not dates. Notes split: industry panel and the Week 5 async note → Canvas; the Ch. 11
  reconciliation warning and "no lab in Week 16" kept; "rubric distributed" dropped.
- **Syllabus unpublished.** `check-site-index.py` caught the stale `docs/files/syllabus.html`
  on the first publish after the swap — the orphan check working as designed on its first real
  use. The `.md` stays in the repo as the Canvas source.
- **Canvas banner** on the landing page, plus a schedule preamble explaining that the week
  numbers are teaching weeks and that Canvas's numbering matches because the break is named,
  not numbered.
- **Rubric** — "Fall 2026" dropped, deliverable dates → week numbers, "In-Class Presentation" →
  "Project Presentation", and the two "see Canvas" pointers made **venue-neutral**: the file is
  published publicly *and* copied to Canvas, where "see Canvas" is circular. Owner raised this;
  it was a real defect.
- **Datasets guide** — "Fall 2026" dropped, "in-class demonstrations" → "lab demonstrations".
  Verified it needs no further change to publish on Canvas unaltered.
- **Quickstart** (student repo) — "in-class lab" → "lab".
- **Term stamp** — `· Fall 2026` removed from 26 source subtitles and from the landing page's
  term badge and footer. Institutional attribution kept (flagged to the owner as a judgement
  call, not a policy read).

Assignments needed no change — they carry no dates and no Canvas pointers.
