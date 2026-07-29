# gitcoin public brain

a public, machine-readable mirror of gitcoin's governance record, built for gtc holders, stewards, delegates, and any agent that wants to reason over gitcoin's decisions.

everything in here is already public. this repo just makes it greppable, versioned, and easy to feed into an llm or a second brain.

## what's in it

- **`gov/`** — every topic on [gov.gitcoin.co](https://gov.gitcoin.co), one markdown file per thread, organized by category:
  - `governance-proposals/`, `governancevision/`, `citizen-grants/`, `gitcoin-grants/`, `partnerships/`, `product/`, `open-discussion/`, `newscommunity/`, `pgn/`, `gitcoin-sensemaking-szn/`
  - each file is `<slug>__<topic-id>.md`: light frontmatter (title, category, timestamps) followed by every post in the thread, in order, prefixed with `username | timestamp | #N`.

that's it for v0. this is the "green tier" of a larger tokenholder brain: only already-public sources. more may be added over time.

## how it stays fresh

a github action ([`.github/workflows/sync-gov.yml`](.github/workflows/sync-gov.yml)) runs **nightly at 06:45 UTC**. it pulls the latest topics from gov.gitcoin.co's public discourse api and commits any changes. sync is incremental: a thread is only re-fetched when it has a newer post than the copy on disk.

run it yourself:

```bash
pip install -r scripts/requirements.txt
python scripts/sync_gov.py
```

tunables (env vars): `GOV_MAX_PAGES` (default 200), `GOV_MAX_TOPICS` (0 = no limit).

## use it

- **grep** the governance history: `grep -rl "quadratic funding" gov/`
- **feed it to an llm** as context for questions about gitcoin's decisions, treasury debates, or grant rounds
- **diff over time**: `git log` shows how the governance record changed, night over night

## source + license

content is mirrored from [gov.gitcoin.co](https://gov.gitcoin.co) and belongs to its original authors under the forum's terms. this repo is a convenience mirror, not the canonical source. for anything authoritative, go to the forum.
