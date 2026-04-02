# Workflow Quick Reference

**Model:** Contractor (you direct, Claude orchestrates)

---

## The Loop

```
Your instruction
    ↓
[PLAN] (if multi-file or unclear) → Show plan → Your approval
    ↓
[EXECUTE] Implement, verify, done
    ↓
[REPORT] Summary + what's ready
    ↓
Repeat
```

---

## I Ask You When

- **Design forks:** "Option A (fast) vs. Option B (robust). Which?"
- **Code ambiguity:** "Spec unclear on X. Assume Y?"
- **Replication edge case:** "Just missed tolerance. Investigate?"
- **Scope question:** "Also refactor Y while here, or focus on X?"

---

## I Just Execute When

- Code fix is obvious (bug, pattern application)
- Verification (tolerance checks, tests, compilation)
- Documentation (logs, commits)
- Plotting (per established standards)
- Deployment (after you approve, I ship automatically)

---

## Quality Gates (No Exceptions)

| Score | Action |
|-------|--------|
| >= 80 | Ready to commit |
| < 80  | Fix blocking issues |

---

## Non-Negotiables

- **Path convention:** All paths relative to repo root; Python scripts use `pathlib.Path`
- **Seed convention:** `np.random.seed(42)` once at top; `random_state=42` on every sklearn estimator
- **Figure standards:** `figsize` always explicit; `plt.tight_layout()`; white bg for HTML/Quarto; transparent for Beamer; 150 DPI minimum
- **Color palette:** UNO Maverick Blue `#005CA9`, UNO Red `#E41C38`, neutral gray `#525252`, positive green `#15803d`
- **Lab scripts:** Must run end-to-end with `python script.py`; no interactive-only steps

---

## Preferences

**Visual:** Publication-ready. All axis labels in plain English (not variable names). Legends outside plot area when possible.
**Reporting:** Concise bullet summary first; full details available on request.
**Session logs:** Always (post-plan, incremental, end-of-session).
**Replication:** Lab scripts must be fully reproducible. Flag any non-determinism immediately.

---

## Exploration Mode

For experimental work, use the **Fast-Track** workflow:
- Work in `explorations/` folder
- 60/100 quality threshold (vs. 80/100 for production)
- No plan needed — just a research value check (2 min)
- See `.claude/rules/exploration-fast-track.md`

---

## Next Step

You provide task → I plan (if needed) → Your approval → Execute → Done.
