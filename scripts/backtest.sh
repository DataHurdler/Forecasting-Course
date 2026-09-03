#!/usr/bin/env bash
# backtest.sh — prove the whole repo is internally consistent and currently true.
#
# Run this after ANY change. It is the difference between a maintained repo and
# one that merely looks maintained. Thirteen gates:
#
#   1. surface-sync        counts + enumerative tables match what is on disk
#   2. skill-integrity     frontmatter <-> body tool parity, anchors, flag parity
#   3. model-versions      no superseded model presented as current (internal
#                         consistency against the model SSoT; the EXPIRY on that
#                         SSoT is enforced by gate 6, staleness)
#   4. links               every relative link and heading anchor resolves
#   5. site-index         the published course site is complete: the landing page is
#                         what its sources produce, its links resolve, and — the part
#                         gate 4 is blind to — nothing is published under docs/ that
#                         the landing page fails to link
#   6. book-claims        the book's and workbook's prefaces are the only hand-written
#                         pages in two generated volumes; every claim they make is
#                         bound to its source (the Lecture 13 scoreboard, the chapter
#                         list, the labs and assignments on disk), and a claim
#                         reworded until it says nothing fails rather than skips
#   7. assignment-sync    the two copies of every assignment agree, AND the three
#                         student-repo documents this site publishes were built from
#                         their sources as they stand now. Assignments are authored in
#                         Homework/ and COPIED to the student repo; the setup guide, AI
#                         policy and quickstart are AUTHORED there and RENDERED here.
#                         Every other gate runs inside one repo, so both kinds of
#                         cross-repo drift are invisible to them by construction
#   8. spec-conformance    every skill obeys the Agent Skills spec
#   9. staleness           stale recommendations, source/render divergence, expired currency
#  10. repo-hygiene       no scratch-as-main, no root clutter, archives documented
#  11. derived-counts     enumerable claims (journals, patterns, phases, snippets)
#                         verified against their own source of truth
#  12. ledger-coverage    the qualification ledger and the checks that actually run
#                         agree in BOTH directions, and every hook in settings.json
#                         is wired to a file that exists (a mistyped path there
#                         disables a hook in silence)
#  13. hook-battery       the active guard hooks are driven with synthetic events
#                         and must still go red on the failure each one targets —
#                         gate 12 proves a hook is wired, this proves it still acts
#   +  findings-validator  smoke test, so a review run cannot fail at the last step
#
# Every gate runs to completion even if an earlier one fails — you get the whole
# picture in one pass. Exit code is the max of all gates.
#
# No `set -e`: it would abort after the first failure and hide the rest.
set -uo pipefail

DIR="$(cd "$(dirname "$0")" 2>/dev/null && pwd)"
if [ -z "$DIR" ] || [ ! -d "$DIR" ]; then
    echo "backtest: cannot resolve script directory" >&2; exit 2
fi

RC=0
run() {  # run <label> <command...>
    local label="$1"; shift
    echo ""
    echo "── $label ──"
    "$@"
    local rc=$?
    [ "$rc" -gt "$RC" ] && RC=$rc
    return 0
}

echo "═══ BACKTEST: is this repo internally consistent and currently true? ═══"

run "surface-sync"       python3 "$DIR/check-surface-sync.py"
run "skill-integrity"    python3 "$DIR/check-skill-integrity.py"
run "model-versions"     "$DIR/check-model-versions.sh"
run "links"              python3 "$DIR/check-links.py"
run "site-index"       python3 "$DIR/check-site-index.py"
run "book-claims"       python3 "$DIR/check-book-claims.py"
run "assignment-sync"  python3 "$DIR/check-assignment-sync.py"
run "spec-conformance"   python3 "$DIR/check-spec-conformance.py"
run "staleness"          python3 "$DIR/check-staleness.py"
run "repo-hygiene"       python3 "$DIR/check-repo-hygiene.py"
run "derived-counts"     python3 "$DIR/check-derived-counts.py"
run "ledger-coverage"    python3 "$DIR/check-ledger-coverage.py"
run "hook-battery"       bash "$DIR/hook-battery.sh"

echo ""
echo "── findings-validator smoke test ──"
echo '[]' | python3 "$DIR/validate-findings.py"
rc=$?; [ "$rc" -gt "$RC" ] && RC=$rc

echo ""
if [ "$RC" -eq 0 ]; then
    echo "═══ BACKTEST PASSED — repo is fresh and internally consistent ═══"
else
    echo "═══ BACKTEST FAILED (exit $RC) — fix before shipping ═══"
fi
exit "$RC"
