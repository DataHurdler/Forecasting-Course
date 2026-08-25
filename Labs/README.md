# Labs

The third part of each class session. Your syllabus describes a class as three parts —
review the previous topic, learn the theory, then **try the new technique on the computer**.
These are that third part.

## Naming

One lab per lecture, matching the `Narration/` short-form convention:

```
Labs/Lecture01_lab.qmd
Labs/Lecture02_lab.qmd
...
```

## Format

Quarto `.qmd`, not `.py` or `.ipynb`:

- Students already write `.qmd` for homework — one format, not three
- It renders to HTML for the course site *and* executes, so one file is both the handout
  and the runnable notebook
- It diffs cleanly in git; notebooks rewrite output cells and metadata on every run

## What a lab is, and is not

A lab is **guided and completable in the room** — roughly 30–40 minutes, with the scaffolding
already written and the student filling in the interesting parts. Homework is the opposite:
longer, unscaffolded, and done alone.

The rule of thumb: if a student can get stuck for twenty minutes with no way forward, it
belongs in homework, not a lab.

## Convention

- Every lab runs end-to-end on the course dataset with no manual steps
- `random_state=42` wherever a result is quoted
- `TimeSeriesSplit`, never `KFold`
- Each lab ends with one question that has no code answer — something to argue about before
  the session closes

Start from `_TEMPLATE_lab.qmd`.

## Series map — avoid collisions

Labs run **before** the homework they precede, so a lab must not use the series the homework
asks about. Keep this table current when adding a lab.

| | Primary series | Contrast / second series |
|---|---|---|
| **Lab 1** (Week 1) | TX_1 HOUSEHOLD | TX_1 FOODS |
| **HW1 Parts 1–2** (due Wks 2–3) | CA_1 FOODS | CA_3 FOODS |
| **Lab 2** (Week 2) | CA_1 HOUSEHOLD | CA_1 FOODS *(Granger step only)* |

Lab 1 and Lab 2 are deliberately built so the *answer differs* from the homework's:

- **Lab 1**: TX_1 HOUSEHOLD shifts +15% in the test year, so seasonal naive carries a stale
  level and loses. HW1's CA_1 FOODS is stable within 3%, so the benchmark wins. Same code,
  opposite conclusion — that contrast is the lesson.
- **Lab 2**: CA_1 HOUSEHOLD gives a clean ADF verdict at every lag order. HW1 deliberately
  uses the messy series where the verdict flips, so students meet the clean case first.
