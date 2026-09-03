#!/usr/bin/env python3
"""Check every external link in the student-facing documents.

    python scripts/check_links.py

Only checks links a student can actually see — text inside <!-- --> is skipped, because a dead
link in a commented-out block harms nobody and reporting it trains you to ignore the output.

Some hosts refuse automated requests. Those are reported as CHECK rather than BROKEN; open them
in a browser before believing them dead.
"""
import re, sys, pathlib, urllib.request, urllib.error, ssl

DOCS = ["syllabi/ECON8310_2026Fall.md", "ECON8310_About.md",
        "ECON8310_Datasets.md", "ECON8310_Project_Rubric.md",
        "ECON8310_Troubleshooting.md"]
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"

# Hosts that block automated requests to their web pages while serving data normally.
# Verified reachable by other means; reported as ok with a note rather than as a problem.
KNOWN_BOT_BLOCKERS = {
    "fred.stlouisfed.org": "blocks non-browser clients; the CSV endpoint used by "
                           "scripts/prep_fred.py returns 200",
}
ROOT = pathlib.Path(__file__).resolve().parent.parent

def visible_links(path: pathlib.Path):
    raw = path.read_text(encoding="utf-8", errors="ignore")
    raw = re.sub(r"<!--.*?-->", "", raw, flags=re.S)          # student-visible text only
    return [u.rstrip(".,;)") for u in re.findall(r"https?://[^\s\)\]<>\"]+", raw)]

def check(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, timeout=20, context=ctx) as r:
            return r.status, ""
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:
        return None, type(e).__name__

def main() -> int:
    seen, broken, unclear = {}, [], []
    for d in DOCS:
        p = ROOT / d
        if not p.exists():
            continue
        for u in visible_links(p):
            seen.setdefault(u, set()).add(d)

    print(f"Checking {len(seen)} unique links across {len(DOCS)} documents\n")
    for u in sorted(seen):
        code, err = check(u)
        if code and 200 <= code < 400:
            print(f"  ok    {code}  {u}")
        elif code in (403, 429):
            print(f"  CHECK {code}  {u}   (host blocks automation — verify in a browser)")
            unclear.append(u)
        elif code is None:
            host = re.sub(r"^https?://([^/]+).*", r"\1", u)
            note = KNOWN_BOT_BLOCKERS.get(host)
            if note:
                print(f"  ok     --   {u}   (known: {note})")
            else:
                print(f"  CHECK  --   {u}   ({err} — verify in a browser)")
                unclear.append(u)
        else:
            print(f"  BROKEN {code} {u}   in: {', '.join(sorted(seen[u]))}")
            broken.append(u)

    print(f"\n  {len(broken)} broken, {len(unclear)} to verify manually")
    return 1 if broken else 0

if __name__ == "__main__":
    sys.exit(main())
