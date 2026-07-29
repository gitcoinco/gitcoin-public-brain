---
id: 25334
title: "The gitcoin gov brain"
slug: the-gitcoin-gov-brain
category: open-discussion
url: https://gov.gitcoin.co/t/the-gitcoin-gov-brain/25334
created_at: 2026-07-08T18:03:20.603Z
last_posted_at: 2026-07-15T13:23:48.447Z
posts_count: 3
views: 39
like_count: 4
---

# The gitcoin gov brain

<https://gov.gitcoin.co/t/the-gitcoin-gov-brain/25334>
owocki | 2026-07-08 18:04:23 UTC | #1

tl;dr: we put gitcoin’s entire governance record into a public github repo, cleaned up so a human can grep it and an llm can read it. it updates itself nightly. github.com/gitcoinco/gitcoin-public-brain.

## why this exists

gitcoin’s governance record is real and deep. hundreds of proposals, treasury debates, grant round retros, steward votes, years of it. all public, all on gov.gitcoin.co.

but it lives as a forum. a forum is good for posting and arguing. it’s bad for reasoning over the whole corpus at once.

try to answer “every time we’ve debated quorum, what did we decide and why” from the forum ui. you can’t, really. you click through 20 threads and reconstruct it in your head. the knowledge is public but it isn’t usable.

that’s the gap. the decisions are open. the ability to reason over them as one body of data is not.

## what it is

a mirror of gov.gitcoin.co as plain markdown, one file per thread, organized by category. 1,639 threads at launch. proposals, governance vision, citizen grants, partnerships, product, the sensemaking szn, all of it.

each file is the full thread in order, with light frontmatter (title, category, timestamps). no forum chrome, no javascript, no login. just the text, versioned in git.

a github action re-pulls the latest topics every night and commits the diff. incremental, so a thread only re-syncs when someone posts to it. the record stays live without anyone touching it.

## the deeper reason

i’ve been building on a thesis i keep coming back to: the strongest new orgs put an intelligence at the center and humans and agents at the edge. a shared context window everyone can query.

the gitcoin team already runs one internally. this is the move to give the same thing to the people the dao is actually accountable to. gtc holders, stewards, delegates. and increasingly, their agents.

if you hold gtc and you want to reason about how this dao has governed itself, you should have the record as data, not as 20 open tabs. if you delegate, your delegate’s homework should be greppable. if you’re pointing an agent at gitcoin, it should be able to read the governance history the way it reads a codebase.

transparency that you can’t compute over is just a filing cabinet. this makes it a corpus.

## how to use it

the whole point of this format is that you can point an ai at it and ask questions in plain english. no forum archaeology.

the fastest path: clone the repo and open claude in it.

```
git clone https://github.com/gitcoinco/gitcoin-public-brain
cd gitcoin-public-brain
claude
```

now the entire governance record is claude’s working context. ask it anything about how this dao has governed itself and it answers from the primary source, the actual threads, not something it half-remembers.

no terminal? drop the folder (or just the threads you care about) into claude.ai and ask the same questions there.

and because it’s versioned in git, you can ask claude what changed. “what moved in governance this week” is a real question it can answer off the commit history.

## what this is not

this is v0, and it’s deliberately the “green tier”: already-public sources only. nothing here that wasn’t already on the public forum. no private docs, no treasury internals, no half-finished plans.

it’s also not the canonical source. gov.gitcoin.co is. this is a convenience mirror for reading and reasoning. if you’re going to act on something, confirm it at the forum.

## what’s next

if this is useful, the obvious extensions are other already-public sources: the public writing, on-chain treasury snapshots, a redacted decision log. i’d rather ship the smallest useful thing first and let demand pull the rest.

if you want a source added, or you build something on top of it, reply here or open an issue on the repo.

## prompts to try

once claude is running in the repo, paste any of these:

* “i just started delegating gtc. catch me up on the 5 most important governance decisions of the last 18 months, and link the threads.”
* “walk me through every time gitcoin has debated quorum. what did we decide each time, and why?”
* “summarize the arguments for and against winding down Grants Stack, and who made each one.”
* “what treasury allocation decisions were made in 2021-2025? give me the amounts and the reasoning behind each.”
* “trace how the grants matching-pool mechanism changed over time, proposal by proposal.”
* “where did stewards disagree most in the most recent sensemaking season? steelman both sides.”
* “i want to write a proposal to change how we do X. first show me every prior thread that touched X so i don’t relitigate settled ground.”
* “what got decided in governance this month that i might have missed?”

the answers cite real threads. if one looks important, open it on gov.gitcoin.co and read the source.

-------------------------

Kaf | 2026-07-09 16:30:19 UTC | #2

Great initiative. I think most organizations will eventually have something similar: a public memory layer that makes it easier to understand past decisions and reason about what comes next. Clear example of a good use of AI for governance.

-------------------------

MconnectDAO | 2026-07-15 13:23:48 UTC | #3

This is a very strong initiative turning Gitcoin’s governance history into a machine‑readable “gov brain” is a huge unlock for research, meta‑governance, and funding mechanism analysis. @owocki

-------------------------
