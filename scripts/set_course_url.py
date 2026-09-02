#!/usr/bin/env python3
"""Change the published course URL everywhere it appears, in one command.

    python scripts/set_course_url.py                       # show current + where it appears
    python scripts/set_course_url.py https://luozijun.com/Forecasting-Course/

The canonical URL lives in scripts/course_url.txt. Student-facing documents keep the real
URL in their source — no placeholder tokens — so the markdown reads correctly if someone
opens it raw or it is distributed as a PDF. This script is what keeps them in sync.

**Two repositories carry this URL.** This one, and the student homework repo
(`forecasting-env`), whose README and quickstart are the first links a student clicks. The
student repo is a separate checkout, so it is located by:

    1. $FORECASTING_ENV_REPO, if set; otherwise
    2. a sibling directory named Forecasting-Env / forecasting-env beside this repo.

If neither is found the script says so loudly and names the files it could not reach —
it does not skip them silently. (Skipping silently is exactly how the student repo sat on a
dead github.io URL from 2026-08-26 until 2026-08-31.)

Session logs and quality reports are deliberately NOT rewritten: they are a historical
record of what was true when written.
"""
import os, pathlib, sys, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONF = ROOT / "scripts" / "course_url.txt"

# Student-facing documents in THIS repo that carry the live URL.
TARGETS = [
    "syllabi/ECON8310_2026Fall.md",
    "ECON8310_Datasets.md",
    "ECON8310_Project_Rubric.md",
    "ECON8310_About.md",
]

# Documents in the STUDENT repo that carry it.
ENV_TARGETS = [
    "README.md",
    "assignments/README.md",
    "STUDENT_QUICKSTART.md",
]


def env_root():
    """Locate the student repo. Returns (path_or_None, how_we_looked, explicitly_configured)."""
    override = os.environ.get("FORECASTING_ENV_REPO")
    if override:
        p = pathlib.Path(override).expanduser()
        return (p if p.is_dir() else None), f"$FORECASTING_ENV_REPO={override}", True
    for name in ("Forecasting-Env", "forecasting-env"):
        p = ROOT.parent / name
        if p.is_dir():
            return p, f"sibling directory {p}", False
    return None, f"no sibling Forecasting-Env beside {ROOT}", False


def targets():
    """[(label, Path)] across both repos, plus a note about the student repo."""
    items = [(rel, ROOT / rel) for rel in TARGETS]
    er, how, explicit = env_root()
    if er is not None:
        items += [(f"{er.name}/{rel}", er / rel) for rel in ENV_TARGETS]
    return items, er, how, explicit


def warn_missing_env(how, explicit):
    print("\n  !! STUDENT REPO NOT UPDATED")
    print(f"     Looked for it: {how}")
    print("     These files carry the course URL and were NOT touched:")
    for rel in ENV_TARGETS:
        print(f"       forecasting-env/{rel}")
    print("     Fix: set FORECASTING_ENV_REPO=/path/to/forecasting-env and re-run,")
    print("          or edit those three files by hand.")
    return 1 if explicit else 0

def current() -> str:
    return CONF.read_text(encoding="utf-8").strip()

def occurrences(url: str):
    base = url.rstrip("/")
    items, _er, _how, _x = targets()
    found = []
    for label, p in items:
        if not p.exists():
            found.append((label, None)); continue
        found.append((label, p.read_text(encoding="utf-8").count(base)))
    return found

def main():
    old = current()
    if len(sys.argv) == 1:
        print(f"current course URL: {old}\n")
        for rel, n in occurrences(old):
            print(f"  {rel:<38} {'(missing)' if n is None else f'{n} occurrence(s)'}")
        _items, er, how, explicit = targets()
        if er is None:
            warn_missing_env(how, explicit)
        print("\nto change:  python scripts/set_course_url.py <new-url>")
        return 0

    new = sys.argv[1].strip()
    if not re.match(r"^https?://", new):
        print(f"error: '{new}' does not look like a URL"); return 1
    if not new.endswith("/"):
        new += "/"
    old_base, new_base = old.rstrip("/"), new.rstrip("/")
    if old_base == new_base:
        print("no change: that is already the current URL"); return 0

    total = 0
    items, er, how, explicit = targets()
    for rel, p in items:
        if not p.exists():
            print(f"  SKIP {rel} (missing)"); continue
        raw = p.read_bytes()
        crlf = raw.count(b"\r\n")
        text = raw.decode("utf-8")
        n = text.count(old_base)
        if n:
            text = text.replace(old_base, new_base)
            out = text.encode("utf-8")
            # preserve the file's original line-ending convention
            if crlf and out.count(b"\r\n") != crlf:
                out = out.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
            p.write_bytes(out)
            total += n
        print(f"  {rel:<38} {n} replaced")

    CONF.write_text(new + "\n", encoding="utf-8")
    print(f"\n{total} occurrence(s) updated; scripts/course_url.txt now reads {new}")
    rc = 0
    if er is None:
        rc = warn_missing_env(how, explicit)
    else:
        print(f"student repo: {er}")
    print("next: ./scripts/sync_to_docs.sh docs   (re-render the three course pages)")
    print("      the student-repo files are plain markdown — commit them in that repo")
    return rc

if __name__ == "__main__":
    sys.exit(main())
