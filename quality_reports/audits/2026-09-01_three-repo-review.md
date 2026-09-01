# Three-repository review — 2026-09-01

Requested: inconsistencies; anything questionable to wrong; anything that may affect student
learning in a **fully online** setting.

Scope: `forecasting-course` (public), `forecasting-env` (public, student homework),
`forecasting-instructor` (private, keys). Evidence gathered by inspection and by running the
repositories' own checks.

**Four false alarms of my own — two found while writing this, two found while acting on it.** See §1.1 and §2.1, both retracted. The pattern in all four is the same: I trusted an extraction instead of reading the source.  A first pass reported
prompt-budget mismatches across all eleven assignments and a missing due date for Homework 6
Part 1. Both were bugs in my extraction, not in the course: the budgets agree in all three places
and all eleven due dates match. Where this document says something is clean, it was checked.

---

## 1. Inconsistencies

### 1.1 ~~The intake meeting is called two different lengths~~ — **WRONG, retracted 2026-09-01**

**This finding was mine and it was false.** The only "10-minute" text in the syllabus sat inside a
commented-out block — the superseded Calendly paragraph, replaced by the Google Sheet sign-up that
is actually live. I read commented-out text as live text. The live section never contradicted its
heading; it simply stated no duration at all, which has now been fixed to say twenty minutes.

Original finding, preserved:

`ECON8310Syllabus2026Fall.md`

```
line  39   ## 20-Minute In-Person Meeting
line  46   Each student is required to sign up for a 10-minute meeting ...
line  47   https://calendly.com/luozijun/fall-2026-10-minute-meeting
```

The body and the booking link agree on ten minutes; only the heading says twenty. A student
reads the heading, books ten minutes, and does not know which is true. The heading is the
outlier and is the thing to change.

### 1.2 `TROUBLESHOOTING.md` is reachable from nowhere — **confirmed**

278 lines of setup and error guidance, linked from **zero** of: the course website, the syllabus,
the student repository's `STUDENT_QUICKSTART.md`, its `README.md`. A student finds it only by
browsing the course repository, which they are never told to clone. See §3.6 — for a remote
student this is the most costly item in this document.

### 1.3 A commented-out line sits in the syllabus source — **confirmed**

```
line 156   - Ask questions <!-- - Email me a link to a drone video for three extra points -->
```

Invisible in the rendered HTML, plainly visible in the raw Markdown on GitHub, which is a link the
syllabus itself hands out. Either restore it or delete it.

### Checked and clean

| Checked | Result |
|---|---|
| Prompt budgets: assignment text vs `policy/homework_limits.json` vs `CLAUDE.md` | all 11 agree |
| Homework due dates: syllabus vs website table | all 11 agree |
| Project points: 5 + 20 + 25 + 50; course total 300 + 100 | 100 and 400, correct |
| Course URL across both public repos | 6 sites, all current |
| Scoreboard values (744, 781, 805, 899, 1 032, 2 152, 1 589, 127) across decks, mirrors, labs, homework, narration, book | consistent |
| Beamer ↔ Quarto parity, slides **and** sections | 15/15 pass |
| Internal links and anchors | 169 files, 0 broken |
| External links in student documents | 0 broken |
| Workbook → executable-lab links | resolve |
| Instructor repository | 24 files, 11 keys, 11 scripts, no rendered HTML, nothing student-facing |

---

## 2. Questionable to wrong

### 2.1 ~~Week 17 is graded but not scheduled~~ — **WRONG, retracted 2026-09-01**

**Also mine, also false.** The week was in the schedule as **"Final Exam Week · Dec 17 — Final
project presentations (5:30-7:30pm)"**. It was named differently from the grading table's "Week
17", not absent. My check grepped for `^\*\*Week 17` and concluded absence from a naming
difference. The two now agree.

Original finding, preserved:

The grading table has `| In-class presentation | Week 17 (Dec. 17) | 25 |`, and the final report is
due Dec 18. The weekly schedule ends at **Week 16 · Dec 10**. Nothing in the schedule tells a
student what happens in the week that carries 25 of their 100 project points. Finals week is
presumably intended; it should be written down.

### 2.2 Two systems hold the same course, and only one is public

All fourteen labs end with *"Solutions posted to Canvas after class."* The labs themselves are
public on the course site; their solutions are on Canvas. A student who finds the lab through the
website has no route to the solution and no way to know when "after class" was. This is defensible
for graded work — it is the reason the keys are private — but the sentence should say **when** and
**where**, because as written it is an instruction a student cannot act on.

### 2.3 `docs/index.html` is hand-maintained while everything around it is generated

It drifted twice in a single day: it kept the old "Codex, Copilot, ChatGPT…" AI wording after the
syllabus, the AI policy and all eleven assignments were corrected, and it needed manual edits to
link the book and the workbook. Every other student-facing surface is either generated or covered
by a gate. This page is the one that will silently fall behind again.

### 2.4 The book's preface is the only hand-written page in a generated book

It makes claims about the course's own history. It has already been corrected once for a stale
count. It is worth deciding whether that paragraph is maintained deliberately or removed.

---

## 3. Fully online delivery

The syllabus currently describes a course that meets in person, with **one** asynchronous week
(Week 5). Everything below is what would need attention if the whole course ran online.

### 3.1 A required **in-person** meeting — blocker

*"Each student is required to sign up for a 10-minute meeting"*, under a heading reading
**In-Person**, booked through Calendly in the first two weeks. A remote student cannot comply. The
requirement is good practice; the modality needs an alternative.

### 3.2 Office hours discourage the only remote channel — blocker

> Designated hours: Tuesday, 1-3pm · Outside designated hours: Email me for appointments ·
> **Zoom possible but not encouraged**

For an online student Zoom is not a fallback, it is the only door. As written the syllabus tells
them the door is discouraged.

### 3.3 A 25-point in-class presentation with no stated alternative

25 of the project's 100 points. No asynchronous equivalent — recorded presentation, live session,
written defence — is described anywhere.

### 3.4 Three labs instruct the student to talk to a neighbour

| Lab | Line |
|---|---|
| Lab 1 | "**Discuss with the person next to you, before reading on:** did any model beat the benchmark?" |
| Lab 2 | "Say it out loud to the person next to you before you fit anything." |
| Lab 4 | "**Read the root split aloud to the person next to you**, in business language" |

Dead instructions for a student working alone. The recording scripts already solved this for the
video versions, replacing each with a *"pause the video and do this"* prompt; the labs themselves
were never updated. The fix is small and the wording already exists.

### 3.5 Labs are budgeted for a 40-minute supervised slot

Each lab states "~40 minutes" and assumes someone is present to unblock a stuck student. The new
workbook mitigates this — every step now carries a collapsible walkthrough and every lab ends with
the output a correct run produces — but the time estimates still describe a classroom.

### 3.6 The troubleshooting guide is invisible

Repeating §1.2 because the consequence differs online. In a classroom a stuck student raises a
hand. Online they hit `import xgboost` failing on macOS without `libomp`, and the 278-line document
that answers it is linked from nowhere they will look.

### 3.7 Recordings are implied but never located

Fifteen lecture scripts, fourteen lab scripts and eleven solution scripts exist — the course is
clearly built to be recorded. Yet "recording" appears in the syllabus only for Week 5's
asynchronous session, and the website never says where recordings live. A fully online course needs
one canonical place, stated once.

### What already works well online

- Slides publish as **HTML, not PDF** — real headings, alt text, table headers, readable maths.
- The **book** and **workbook** now cover the lectures and the labs in searchable form.
- Prepared data is **committed**, so a failed download never blocks an assignment.
- The AI policy is **tool-agnostic** and now states that ChatGPT Edu here excludes Codex.
- Every assignment carries its own initial prompt, budget, and submission checklist, and
  `check_my_submission.py` lets a student verify their work before pushing without asking anyone.

---

## Suggested order

1. §3.1 and §3.2 — the two hard blockers, and both are a sentence each.
2. §1.2 / §3.6 — link `TROUBLESHOOTING.md` from the website, the syllabus and the quickstart.
3. §1.1 and §1.3 — heading, and the commented-out line.
4. §2.1 — put Week 17 in the schedule.
5. §3.4 — three lab lines; the replacement wording exists in the recording scripts.
6. §3.3 and §3.7 — need a decision from you, not an edit.
