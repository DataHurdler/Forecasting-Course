# pentatonicwoodwinds: remove music + purge history

**Status:** COMPLETED 2026-08-26. Both repos purged and force-pushed.

| Repo | Before | After |
|---|---|---|
| `pentatonicwoodwinds` | 35 commits, 33.40 MiB | 1 commit (`311bb71`), 7.27 MiB |
| `omahahulusi` | 88 commits, 45.18 MiB | 1 commit (`c328677`), 667 KiB |

**Residual exposure:** old commits remain reachable by SHA on GitHub until it garbage-collects
(`b846e96`, `cc17a28`, `2256fb1` all returned 200 after the force-push). Neither repo is a fork,
neither has forks, and neither has open or closed pull requests — so nothing structurally pins
the objects. Owner is emailing GitHub Support to request garbage collection.

## Why

The 25 sheet-music PDFs (+3 `.abc`, 1 `.mp3`) are **not** on the live site (404) but **are**
publicly downloadable from `raw.githubusercontent.com` right now, because the repo is public.
A private repo would not fix this — the published site is public regardless. Scores must be
distributed through an access-controlled channel outside git.

## Backup (already done, verified)

`~/Documents/PentatonicWoodwinds-SheetMusic` — 29/29 files, 49 MB. Outside the repo.

## The trap that nearly bit us

`git checkout --orphan` **carries the old index forward**. Deleting files from the working tree
does not remove them from that index, so a naive `git add` re-staged all 29 music files into the
supposedly-clean history. **Verify with `git ls-files --cached | grep -c sheetmusic` → must be 0
before committing.** This is the whole reason the purge is worth scripting rather than retyping.

## Steps (when the user is ready)

1. Confirm working tree is clean and content updates are committed/pushed as normal commits.
2. Run `scripts/purge-pentatonic.sh` (below) — it stops before the force-push.
3. Review the staged file list and the `sheetmusic` leak check.
4. Force-push as its **own** command: `git push --force-with-lease origin main`.
   (Chaining a push after a commit caused the commit to be silently skipped previously.)

## Open questions for the user

- `contract2026` / `rehearsal2026`: `docs/contract2026.html` and `docs/rehearsal2026.html` are
  tracked and linked from `member.qmd`. They 404 today only because Hostinger serves the site
  from elsewhere. **Migrating to GitHub Pages makes them live public URLs.** Keep, or remove?
- `Omaha!` (the dead staticrypt password in `encrypt.r`) — is it reused anywhere real? If so it
  needs changing independently of this purge; a history purge does not un-leak a password that
  was public for 29 commits.
- `omahahulusi` needs the same treatment (also public, also carries the Chi Zhang LICENSE).

## Files the purge removes

- `sheetmusic/` (29 files) — plus `.gitignore` entries so it can never be re-added
- `encrypt.r` — dead staticryptR script containing `password = "Omaha!"`
- `.staticrypt.json` — orphaned salt
- `default.php` — Hostinger artifact
- `.hugo_build.lock` — Hugo artifact; this is a Quarto site
- `notes.txt`, `.Rprofile` — leftovers from the forked repo
- `_extensions/` — unused third-party

## Files the purge rewrites

- `LICENSE` → MIT, © 2026 Zijun Luo (was "Copyright (c) 2022 Chi Zhang")
- `README.md` → new, with a credit line to `lianyujun/lianyujun.github.io` and a standing
  "no sheet music in this repo" note


## What actually happened, for the record

**The `--orphan` index trap fired twice, in two different disguises.**

1. `git checkout --orphan` carries the previous index forward. Deleting files from the working
   tree does not remove them from it, so a plain `git add` re-staged all 29 music files into the
   supposedly clean history. Caught by the leak check.
2. On the retry, `git ls-files | grep -v '^sheetmusic/'` looked correct but missed 22 entries —
   git quotes paths containing non-ASCII characters, so those lines begin with `"sheetmusic/`,
   not `sheetmusic/`. Rebuilding the list from disk (where the music had been deleted) avoided
   the quoting question entirely.

**Lesson:** verify the index, not the intent — `git ls-files --cached | grep -ci sheetmusic`
must be 0 before committing. Do not filter git's path output with anchored patterns when
non-ASCII filenames are possible.

**Also removed during the same pass** (not in the original plan): three photographs of the
template's original author, a stale `search.json`/`sitemap.xml` carrying his email, ORCID and
Google Scholar profile, commented-out personal links in `index.qmd`, and `readme.md` crediting
the template rather than the site. See each repo's single commit message.
