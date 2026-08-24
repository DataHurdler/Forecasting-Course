# Project Memory

Corrections and learned facts that persist across sessions.
When a mistake is corrected, append a `[LEARN:category]` entry below.

---

<!-- Append new entries below. Most recent at bottom. -->

## Workflow Patterns

[LEARN:workflow] Requirements specification phase catches ambiguity before planning → reduces rework 30-50%. Use spec-then-plan for complex/ambiguous tasks (>1 hour or >3 files).

[LEARN:workflow] Spec-then-plan protocol: AskUserQuestion (3-5 questions) → create `quality_reports/specs/YYYY-MM-DD_description.md` with MUST/SHOULD/MAY requirements → declare clarity status (CLEAR/ASSUMED/BLOCKED) → get approval → then draft plan.

[LEARN:workflow] Context survival before compression: (1) Update MEMORY.md with [LEARN] entries, (2) Ensure session log current (last 10 min), (3) Active plan saved to disk, (4) Open questions documented. The pre-compact hook displays checklist.

[LEARN:workflow] Plans, specs, and session logs must live on disk (not just in conversation) to survive compression and session boundaries. Quality reports only at merge time.

## Documentation Standards

[LEARN:documentation] When adding new features, update BOTH README and guide immediately to prevent documentation drift. Stale docs break user trust.

[LEARN:documentation] Always document new templates in README's "What's Included" section with purpose description. Template inventory must be complete and accurate.

[LEARN:documentation] Guide must be generic (framework-oriented) not prescriptive. Provide templates with examples for multiple workflows (LaTeX, R, Python, Jupyter), let users customize. No "thou shalt" rules.

[LEARN:documentation] Date fields in frontmatter and README must reflect latest significant changes. Users check dates to assess currency.

## Design Philosophy

[LEARN:design] Framework-oriented > Prescriptive rules. Constitutional governance works as a TEMPLATE with examples users customize to their domain. Same for requirements specs.

[LEARN:design] Quality standard for guide additions: useful + pedagogically strong + drives usage + leaves great impression + improves upon starting fresh + no redundancy + not slow. All 7 criteria must hold.

[LEARN:design] Generic means working for any academic workflow: pure LaTeX (no Quarto), pure R (no LaTeX), Python/Jupyter, any domain (not just econometrics). Test recommendations across use cases.

## File Organization

[LEARN:files] Specifications go in `quality_reports/specs/YYYY-MM-DD_description.md`, not scattered in root or other directories. Maintains structure.

[LEARN:files] Templates belong in `templates/` directory with descriptive names. Currently have: session-log.md, quality-report.md, exploration-readme.md, archive-readme.md, requirements-spec.md, constitutional-governance.md.

## Constitutional Governance

[LEARN:governance] Constitutional articles distinguish immutable principles (non-negotiable for quality/reproducibility) from flexible user preferences. Keep to 3-7 articles max.

[LEARN:governance] Example articles: Primary Artifact (which file is authoritative), Plan-First Threshold (when to plan), Quality Gate (minimum score), Verification Standard (what must pass), File Organization (where files live).

[LEARN:governance] Amendment process: Ask user if deviating from article is "amending Article X (permanent)" or "overriding for this task (one-time exception)". Preserves institutional memory.

## Skill Creation

[LEARN:skills] Effective skill descriptions use trigger phrases users actually say: "check citations", "format results", "validate protocol" → Claude knows when to load skill.

[LEARN:skills] Skills need 3 sections minimum: Instructions (step-by-step), Examples (concrete scenarios), Troubleshooting (common errors) → users can debug independently.

[LEARN:skills] Domain-specific examples beat generic ones: citation checker (psychology), protocol validator (biology), regression formatter (economics) → shows adaptability.

## Memory System

[LEARN:memory] Two-tier memory solves template vs working project tension: MEMORY.md (generic patterns, committed), personal-memory.md (machine-specific, gitignored) → cross-machine sync + local privacy.

[LEARN:memory] Post-merge hooks prompt reflection, don't auto-append → user maintains control while building habit.

## Meta-Governance

[LEARN:meta] Repository dual nature requires explicit governance: what's generic (commit) vs specific (gitignore) → prevents template pollution.

[LEARN:meta] Dogfooding principles must be enforced: plan-first, spec-then-plan, quality gates, session logs → we follow our own guide.

[LEARN:meta] Template development work (building infrastructure, docs) doesn't create session logs in quality_reports/ → those are for user work (slides, analysis), not meta-work. Keeps template clean for users who fork.

## LaTeX on Windows

[LEARN:latex] On Windows (Git Bash), TEXINPUTS path separator is `;` (semicolon), not `:` (colon). Use `TEXINPUTS="C:/path/to/Preambles;;"` — the trailing `;;` appends the standard search path. Unix-style `:` is only for Linux/macOS.

[LEARN:latex] On Windows, xelatex cannot use `cd && xelatex file.tex` pattern reliably. Use absolute paths: `xelatex -output-directory="C:/abs/path/Slides" "C:/abs/path/Slides/file.tex"`.

[LEARN:latex] Beamer `\useoutertheme{infolines}` causes `Overfull \hbox (70.75pt)` on every slide with `[aspectratio=169]`. Fix: remove `infolines` and define a custom `\setbeamertemplate{footline}` with three explicit `beamercolorbox` blocks at `.33/.34/.33\paperwidth`.

[LEARN:latex] Beamer `\newcommand{\neg}` conflicts with LaTeX's built-in `\neg` operator. Use `\negc` instead for colored negative annotation commands.

[LEARN:latex] tcolorbox `\newtcolorbox{envname}[1]{title=#1,...}` fails when titles contain commas (e.g., `Monthly data, $m=12$`) — pgfkeys treats comma as option separator. Fix: use `title={#1}` (curly braces protect comma). Affects `definitionbox` and `examplebox` in header.tex.

[LEARN:beamer] Socratic questions at bottom of dense slides: use `\muted{\footnotesize\itshape question text}` (no preceding `\vspace`) to minimize height impact while preserving pedagogical intent.

[LEARN:beamer] `\small` inside tcolorbox enumerate/itemize: wrap as `{\small \begin{enumerate}...\end{enumerate}}` — reduces the content block by ~8pt, useful for tight slides with definitionbox + columns.

[LEARN:latex] On Windows (Git Bash), the ONLY reliable xelatex+bibtex compile pattern is via `cmd //c`:
- Pass 1/2/3: `cmd //c "set TEXINPUTS=C:\path\Preambles;; && cd /d C:\path\Slides && xelatex -interaction=nonstopmode C:\path\Slides\file.tex"`
- BibTeX: `cmd //c "cd /d C:\path\Slides && bibtex file"` (NO BIBINPUTS override needed — .aux has `../Bibliography_base` already)
TEXINPUTS is required because all lectures use `\input{header}` (no path), so xelatex must search Preambles/ for header.tex. Separator is `;` (Windows); trailing `;;` appends the standard TEXMF path. BibTeX does NOT need TEXINPUTS. Do NOT override BIBINPUTS.

[LEARN:pedagogy] `\sectionslide{}{}` macro must be called at every major section boundary in all lectures. It is defined in `Preambles/header.tex` (lines 230-241). When demoting section-overview keyboxes, keep the prose content as a plain paragraph in the section overview frame immediately after the `\sectionslide` call.

[LEARN:pedagogy] When splitting a dense two-column "method A vs method B" slide into two full-width slides, expand each side with: (1) `\underbrace{}` labels on formulas, (2) a muted footnote about standardization/prerequisites, (3) a worked numeric example or RSXFS finding.

[LEARN:notation] In this course, `\alpha` has multiple incompatible meanings across lectures: ETS level-smoothing (L03), ECM speed-of-adjustment (L05), EN mixing parameter (L08), EWM decay weight (L11). Any new slide using α must explicitly disambiguate from the others. The L11 EWM slide provides the gold-standard disambiguation footnote format.

[LEARN:notation] sklearn's `Ridge(alpha=...)` parameter is the PENALTY STRENGTH (what we call `lambda`). sklearn's `ElasticNet(alpha=...)` is ALSO the penalty strength. The EN mixing parameter is `l1_ratio` in sklearn, not `alpha`. Always comment: `# sklearn 'alpha' = our lambda (penalty strength)`.

[LEARN:citation] Hamilton (1994) "Time Series Analysis": Ch. 8 = OLS/Gauss-Markov (BLUE). Ch. 10 = Vector Autoregressions. Never cite Ch. 10 for OLS/BLUE results.

[LEARN:content] M4 Competition sMAPE (Makridakis et al. 2020, Table 1 overall): ES-RNN = 11.374, Theta = 11.551, FFORMA = 11.720. Theta did NOT tie with ES-RNN. Always transcribe exact values from the paper.

[LEARN:bib] ISL textbook exists in two distinct editions: ISLR2 (Applications in R, 2nd ed., 2021, 4 authors) and ISLP (Applications in Python, 1st ed., 2023, 5 authors incl. Taylor). Never mix year/edition/subtitle. For Python courses: James2021 key should use 2023, 1st ed., Python, 5 authors.

[LEARN:content] σ² = Var[ε] is irreducible noise variance. It cannot be reduced by collecting more observations from the same DGP. Never say "only better data can reduce σ²" — the irreducible floor is fixed by the data-generating process.

[LEARN:notation] In this course, p has conflicting uses: VAR lag order (L05), regression parameter count (general), polynomial degree. When discussing "too many predictors" in L07+ context, use k (parameter count) to avoid collision with L05 VAR notation.

[LEARN:pedagogy] DM test "Statistic and Mechanics" had 5 elements on one slide (d_t def, formula, asymptotic dist, H₀, HAC). Two-slide split: Slide 1 = d_t definition + numeric example; Slide 2 = full statistic with inline labels + HAC columns + warningbox.

[LEARN:pedagogy] Box fatigue ceiling: >50% of content slides with a keybox is over the ceiling. Demote motivational prose keyboxes ("always do X", "this is the closest thing to Y") to bold italic text. Reserve keybox for formal key results and decision rules.

[LEARN:latex] After a closing brace of a group (e.g., `{\small...}`), use `\vspace{Xpt}` not `\\[Xpt]` to add vertical space — the double-backslash requires a line to end and causes "There's no line here to end" error when used after a closing group brace.

[LEARN:beamer] When adding a Socratic question below a warningbox in a two-column slide: remove `\vspace{0.1cm}` before the muted question, and shorten the question text — even a single added `\vspace` + full sentence can cause vbox overflow if the column is already near capacity.

[LEARN:latex] British spelling recurring authoring pattern: "regularised/regularisation/penalised/minimises" appear in drafts. Always grep for `-ised`, `-isation`, `-ising`, `minimises`, `penalises` before finalising any lecture. Course uses American English throughout.

[LEARN:notation] `\alpha` disambiguation must appear at FIRST USE in each lecture, not deferred to later sections. Course has 4 conflicting uses: ETS smoothing (L03), ECM adjustment (L05), EN mixing (L08), attention weights (L10). Pattern: `\muted{\footnotesize\itshape $\alpha$ here = [this use] --- distinct from [L03 use], [L05 use], [L08 use].}`

[LEARN:citation] `\parencite` inside tcolorbox titles (definitionbox/examplebox) and `\sectionslide` arguments is fragile (biblatex/hyperref interaction). Always put citations in box bodies as `\muted{\footnotesize\parencite{key}}`. For `\sectionslide`, citations already appear in the subsequent content slide.

[LEARN:beamer] Moving an inline `\frac{}{}` to display math (`\[...\]`) can cause 40pt+ vbox overflow on a dense Beamer slide. Fix: use `\tfrac` instead of `\frac` in display mode, add `\vspace{-6pt}` before and after the equation, and set `\footnotesize` on the enclosing box/column content.

[LEARN:pedagogy] Section overview keybox frames should ALWAYS be replaced with `\sectionslide{Title}{Subtitle}` (defined in header.tex). The subtitle captures the section's core thesis. Removing 6-7 section-overview keyboxes can drop deck-level keybox density from ~54% to ~29%, resolving Pattern 10 (box fatigue) simultaneously.

[LEARN:content] Equal-weight forecast combination does NOT guarantee beating the best individual model on every metric. The combination reduces variance but the mean is a weighted average: if SARIMA (weak) is included, the combination RMSE/MAE can exceed XGBoost or LSTM individually. Always verify combination vs individual comparisons against the actual leaderboard table — never assert "combination beats X" without checking.

---

<!-- Sections below inherited from the claude-code-my-workflow template (v2.5.1).
     Template-maintenance cycle logs were not carried over; see CHANGELOG.md. -->

## Drift Prevention

[LEARN:drift] `replace_all` on one phrasing (e.g., `"26 skills"`) misses sibling phrasings — `"26 skills, and 21 rules"` (extra "and"), `"26 slash commands"`, `"template's 26"`, `"N skills on day one"` (prose). Count drift hit us 3 times in v1.5.x (PRs #70, #76, #78). Solution: `scripts/check-surface-sync.py` with compound regex patterns as a pre-commit gate. Adding a new phrasing to documentation requires adding a matching regex to the script, otherwise it won't be caught.

[LEARN:drift] Guard against false positives when scanning for template counts: `"3 parallel agents"`, `"17 specialized agents"` (clo-author attribution), `"start with 2-3 skills"` are all legitimate non-template uses of `N + category` phrases. Use compound patterns requiring multiple template-specific tokens on the same line.

## Claude Code Hooks

[LEARN:hooks] Stop-hook block protocol has TWO valid forms: (a) legacy — `exit 2` + reason on stderr; (b) modern — `exit 0` + JSON `{"decision":"block","reason":"..."}` on stdout. `log-reminder.py` uses the modern form. Audit agents unfamiliar with the modern protocol will flag this as "should exit 2" — false alarm. Documented in `/deep-audit` skill's false-alarm list.

[LEARN:hooks] `initialPermissionMode` in VSCode settings only fires at **session start**. Mid-session mode toggles (via `Shift+Tab` or `/permission-mode`) override the file settings until session end. The 6-tier permission stack: VSCode user / workspace / CLI user / project / project-local / in-session runtime — the last is authoritative. "Prompts fire despite bypass config" is almost always a stale session, not a settings bug.

## Plan→Bypass Framing

[LEARN:safety] Do NOT frame Plan→Bypass as a "safety boundary" or "safety guarantee." Plan approval gives you a chance to review the APPROACH before execution, but exiting plan mode returns the session to `defaultMode` (bypassPermissions), at which point any tool call runs under the full allowlist. Frame as "review-before-execute convenience." If a user needs a real enforcement boundary, they should keep `defaultMode: "default"` and approve each high-risk tool individually.

## Privacy in Diagnostic Skills

[LEARN:privacy] Diagnostic skills that read host-global config (e.g., `~/.claude/`, VSCode user settings) must require **explicit user confirmation** before crossing the repo boundary — especially in template repos that get forked. Phase the skill: repo-local auto, host-global opt-in with key redaction. Codex correctly flagged this pattern as a template-adopter privacy risk in PR #75.

## Claim-vs-Reality Framing

[LEARN:framing] **The orchestrator became a real runtime in v2.0.0 (2026-06-09)** (fan-out → reduce → judge + hallucination gate → loop-until-dry), superseding its earlier "pattern, not a runtime" framing, retired 2026-08-21. What holds regardless: there is **no daemon and no post-plan-approval trigger** — the loop is always user- or skill-initiated, a documented non-goal. Any doc claiming it "activates automatically after plan approval" is wrong.

[LEARN:framing] **A gate is only as enforced as its installation.** v2.0.0 replaced the "quality gates" claim (then enforced only inside `/commit`) with a real pre-commit hook — but it is live only **after the user runs `./scripts/install-hooks.sh`**, and `SKIP_QUALITY_GATE=1` / `--no-verify` bypass it. Docs must say "enforced once installed", never "always enforced". *(v2.0.0; retired the older framing 2026-08-21.)*

[LEARN:framing] Cross-artifact review is **pattern-based detection**, not universal auto-invocation. If the manuscript has no `\input{scripts/...}` signals, no cross-artifact work happens even without `--no-cross-artifact`. Document detection signals explicitly.

## Verification Architecture (three complementary patterns)

[LEARN:pattern] Verification here operates at three architectural levels, each addressing a different failure mode. Do NOT collapse them — they are complementary, not redundant:

1. **Critic-fixer loop** (`/qa-quarto`, `/review-paper --adversarial`) — **two agents, serial** — one flags issues, the other applies fixes; loop until APPROVED. Best for **presentation + structural** bugs (Beamer↔Quarto parity, manuscript completeness). Both see the full artifact; the tension comes from role assignment.

2. **Cross-artifact review** (`/review-paper` + `/review-r` + `/audit-reproducibility`) — **horizontal dependency traversal** — a manuscript's claims depend on scripts' outputs, so the paper reviewer spawns script reviewers and reproducibility checkers alongside it. Best for **paper ↔ code consistency** (ATTs, coefficients, N match the outputs that produced them).

3. **Post-Flight Verification / CoVe** (`/verify-claims` + `claim-verifier` agent, v1.7.0) — **single agent, fresh-context fork** — the verifier has never seen the draft; it answers verification questions from the source material alone, using `context: fork` to architecturally enforce independence. Best for **factual hallucination** (fabricated citations, wrong dataset fields, misattributed findings). Adapted from Dhuliawala et al. 2023 ([arXiv:2309.11495](https://arxiv.org/abs/2309.11495)).

The key insight: each enforces independence differently — role tension, dependency-graph traversal, context isolation. A skill needing all three (e.g. `/review-paper --peer`) invokes them at different phases.

[LEARN:pattern] Post-Flight Reports (v1.7.0) are the output-side twin of Pre-Flight Reports (v1.6.0). Pre-Flight proves inputs were read, Post-Flight proves claims hold, and both use structured output blocks, fail-closed fallbacks, and explicit opt-outs. With summary-parity (v1.6.1) they form the **discipline-pattern trilogy** — input, framing, output discipline. Ask of a new text-generating skill: does it need all three?

[LEARN:audit] **Skill frontmatter `allowed-tools` must cover every tool the body invokes** — easy to miss, because the body reads as English ("spawn the verifier via Agent") while the frontmatter reads as a bureaucratic array. Four skills promised a tool in prose their `allowed-tools` omitted (PR #92, flagged by two external reviewers); the runtime failure is a permission error or a silent bypass. Sibling check: if rule X's `paths:` names skill Y, confirm Y actually implements X — rule-vs-implementation drift is the same bug one layer up.

[LEARN:audit] Deterministic bug classes (field exists, anchor resolves, count matches disk) belong in mechanical scripts — agent attention drifts, scripts don't. Reserve audit agents for judgment calls. `check-skill-integrity.py` ships the mechanical batch; `audit-pet-peeves.md` catalogues the judgment classes.

[LEARN:audit] When writing a parity-check regex, always strip inline code spans (` `` `) and fenced code blocks (` ``` `) before pattern-matching. Docs use example syntax like `[text](path#anchor)` inside backticks to illustrate; a naive regex treats those as real links. Replace matched code with spaces (preserving line numbers) before running the rest of the check.

[LEARN:audit] Audit-scope ATROPHY: audit agents only check what their prompt scopes, so any new code directory bypasses audit by default (6 bot-caught bugs in unscoped `scripts/`). **When adding a code location, expand audit scope first** — audit-debt accumulates silently.

## Scheduling Autonomous Work

[LEARN:scheduling] `CronCreate` is session-only in practice — it dies with the REPL (hit 2026-04-16 via a rate-limit termination). Work that must survive session death uses **Routines** (cloud-side). CronCreate is fine for short polling inside a live session, not "run this in an hour".

[LEARN:hooks] PreCompact hooks can BLOCK (modern protocol), which is how `pre-compact.py` can hold compaction while a plan is still DRAFT. Any such block must be opt-in, must fire at most once, and must fail open — a guard that can wedge a session is worse than the context it saves.
