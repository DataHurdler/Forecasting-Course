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
