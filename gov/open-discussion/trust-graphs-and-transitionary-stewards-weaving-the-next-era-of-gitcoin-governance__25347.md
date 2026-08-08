---
id: 25347
title: "Trust graphs and transitionary stewards: weaving the next era of gitcoin governance"
slug: trust-graphs-and-transitionary-stewards-weaving-the-next-era-of-gitcoin-governance
category: open-discussion
url: https://gov.gitcoin.co/t/trust-graphs-and-transitionary-stewards-weaving-the-next-era-of-gitcoin-governance/25347
created_at: 2026-07-17T21:18:28.918Z
last_posted_at: 2026-08-07T16:08:24.633Z
posts_count: 4
views: 84
like_count: 4
---

# Trust graphs and transitionary stewards: weaving the next era of gitcoin governance

<https://gov.gitcoin.co/t/trust-graphs-and-transitionary-stewards-weaving-the-next-era-of-gitcoin-governance/25347>
owocki | 2026-08-04 18:29:33 UTC | #1

# trust graphs and transitionary stewards: weaving the next era of gitcoin governance

*a follow-up to the [transitionary stewards temp check](https://gov.gitcoin.co/t/temp-check-transitionary-stewards-cohort/25342). that post floated the ideas. this one puts dates on them. still pre-vote, still wanting feedback.*

## tl;dr

* two structures launching together: a **transitionary stewards cohort** (12 months) and a **trust graph** that will programmatically hold my delegated voting power
* the trust graph starts institutional on purpose. \~5 people i select, a barrier around it, weekly and monthly calls, a shared context window of common knowledge about governing gitcoin
* then the walls come down over time.
* the milestone that matters: the trust graph can outvote me

## the timeline

### july 2026: 0% extitutional (the baseline)

the july budget request runs through the old machinery. while i have no inside information, i predict my delegation will be influential in the vote, and the context needed to evaluate it (although disclosed on the forum) lives mostly in the 3.0 team’s heads. i’m naming that honestly: governance is 0% extitutional. this is the baseline we grade everything after this against.

also happening now: the transitionary stewards cohort gets finalized (see the [temp check](https://gov.gitcoin.co/t/temp-check-transitionary-stewards-cohort/25342) for shape, comp, and criteria), and the trust graph gets seeded with roughly 5 people.

one change from the temp check: it proposed a term of august through march. i’m considering extending to 12 months so the term covers the full arc to the 75% checkpoint.  push back below if 12 months is wrong.

### august to december 2026: build the context window

the cohort’s 12 months begin. we hold weekly and monthly calls where we onboard stewards into gitcoin’s governance: treasury state, live programs, any legal/complaince considerations, strategy, the stuff you need to actually govern rather than spectate.

the artifact of those calls is an active **context window of common knowledge** about governing gitcoin. think of it as a shared brain: what we know, what we’ve decided, what we’re worried about, kept current and legible.

this phase starts institutional, and that’s deliberate. there’s a barrier around the group. membership is a list i wrote. context accumulates inside the walls first, because you can’t hand off power to people who don’t yet have the context to wield it.

### december 2026: 25% extitutional

by end of year, the first walls come down:

* the trust graph holds real delegated voting power. a meaningful slice of the gtc i currently have influence upon (roughly 2m gtc, and theres also a multisig from the dao that has rouhgly 12.5m gtc in it, both which could move to graph-driven delegation, updating programmatically as the graph evolves
* parts of the context window get published to the forum instead of living inside the calls
* stewards are making some governance calls without me in the room

### july 2027: 75% extitutional

a year from now:

* the barrier to the trust graph is mostly gone. you join by earning trust from people already in the graph, not by being on my list
* the context window bleeds out. most of what the cohort knows about governing gitcoin is public and kept current in public
* my delegated weight follows the graph automatically. i don’t touch it
* **the trust graph can outvote me.** to be precise: i keep voting my own tokens as myself, but the weight the graph controls exceeds my personal vote. if the graph thinks i’m wrong, they win. that’s the torch passed, and it’s the point of the whole exercise
* possibly change the brand to something 2027 native, like [\* Ethereum Extitutional](https://gov.gitcoin.co/t/temp-check-ethereum-extitutional/25345)

## the details

### what “% extitutional” actually measures

institutions have walls. extitutions have networks. a governance structure is extitutional to the degree that:

1. **power**: voting power flows from the trust graph rather than from the founder’s delegation choices
2. **membership**: you can enter by earning trust, without anyone’s permission
3. **context**: the knowledge needed to govern is public, not held inside a walled group

the percentages are a rough weighted read across those three dials. i won’t pretend they’re precise. but they’re dated and falsifiable: at each checkpoint we can look at the three dials and argue about the number in public. that argument is itself extitutional behavior, so i win either way.

### the mechanism (how delegation actually moves)

* scopelift is upgrading gitcoin’s governor from bravo to the new openzeppelin governor, which we believe supports the delegation tooling this needs (confirming the exact mechanics with them now)
* the trust graph (building with jake hartnell on trustgraph, rather than vibe-coding a lesser version solo) syncs on a nightly cadence: it emits a map of addresses and weights, and my delegation updates to match
* the graph gets seeded from existing gitcoin data (years of grants, gov, and contribution signal) plus attestations generated in the cohort’s calls
* signals decay, so inactive members de-weight over time instead of squatting on power

### why a schedule and not vibes

every founder says they’ll decentralize eventually. “eventually” is doing a lot of work in that sentence. tranched steward payments (from the temp check) already give the community a recurring leash on the 3.0 team. the 25/75 schedule gives you a leash on me specifically. if december comes and the trust graph holds no real power, or next july comes and membership is still my list, say so on the forum and point at this post.

### failure modes i’m watching

* **the walled garden persists.** the context window is convenient to keep private. if publishing keeps slipping, the cohort became an advisory board, and the percentages are theater
* **the graph gets gamed.** trust graphs invite sybils and cliques. starting small and institutional is partly a defense; the open question is whether the graph stays honest as the barrier drops
* **rubber stamping.** if the stewards only ever agree with me, the graph outvoting me is a technicality. the cohort’s charter (keep the 3.0 team honest) has to be real

### what this means if you hold gtc

your tokens and your own delegation stay exactly as they are. my delegated weight is the thing that moves: over 12 months it migrates from “kevin’s wallet points at kevin” to “kevin’s weight follows a graph of earned trust that anyone can eventually enter.” if it works, gitcoin ends up with a 2026-era legitimacy structure, and we’d be among the first major daos to run programmatic trust-graph delegation in production.

## feedback wanted

1. are the 25% and 75% checkpoints too slow, too fast, or about right?
2. what would you want published first when the context window starts extitutionalising out?
3. what’s missing?

*Disclaimer: This post is for informative purposes only and is not financial advice. This post reflects my personal views ahead of the stewards’ review, not a decision or commitment by Gitcoin governance. Forward-looking items in it are targets, not commitments. The information in these posts is subject to change as we continue learning. This post may contain estimates, may contain errors, and is provided on a best-effort basis. DYOR, do not make any financial decisions based on these posts.*

---

Disclaimer: This post is for informative purposes only and is not financial advice. This post reflects my personal views, not a decision or commitment by Gitcoin governance. Forward-looking items in it are targets, not commitments. The information in these posts is subject to change as we continue learning. This post may contain estimates, may contain errors, and is provided on a best-effort basis. DYOR, do not make any financial decisions based on these posts.

-------------------------

MconnectDAO | 2026-07-19 01:55:41 UTC | #2

**Governance structure**

* How do you plan to make the “% extitutional” metric more data‑driven across power, membership, and context, rather than a rough weighted read?

* If the trust graph does not hold a meaningful slice of delegation by December 2026, what is the explicit fallback governance plan?

## Trust graph mechanics

* What concrete caps or guardrails will you use to mitigate sybil attacks, cliques, or cartelized behavior as the trust graph updates delegation nightly.

* When will the full rule‑set for signal decay (half‑life, thresholds, negative signals) be published so the graph does not operate as a black box?

## Transitionary stewards

* Since the cohort’s charter is to “keep the 3.0 team honest”, what measurable accountability metrics will you track to show this is happening in practice?

* What clear eligibility criteria will govern the shift from a founder‑selected list to “earned trust” membership in the trust graph and steward cohort?

## Transparency & timeline

* Which parts of the context window are guaranteed to be public, and will you commit to specific publishing SLAs for those artifacts?

* At the 25% (Dec 2026) and 75% (July 2027) checkpoints, what explicit levers do GTC holders have if the trust‑graph design under‑performs its goals? @owocki

-------------------------

owocki | 2026-08-04 18:29:37 UTC | #3

thanks for the questions

> How do you plan to make the “% extitutional” metric more data‑driven across power, membership, and context, rather than a rough weighted read?

you can read the trustgraph data onchain.  maybe someone will build a tool that makes it easier to do without technical skills! although arguably this is accessible to anyone with an LLM

> If the trust graph does not hold a meaningful slice of delegation by December 2026, what is the explicit fallback governance plan?

gtc holders continue to have the ability to vote on snapshot/tally, just like before.  the trustgraph is supportive of this structure, not competitive.

> What concrete caps or guardrails will you use to mitigate sybil attacks, cliques, or cartelized behavior as the trust graph updates delegation nightly.

sybil attacks are not a threat vector for trustgraph, as there is no bonus to generating new identity.

cliques, or cartelized behaviour => imo these are the kinds of questions that gitcoin stewards asked a lot all through 2021-2025, when we laboured to keep cliques and cartels out of gitcoin governance, and the end result was spending $25m on a product almost no one wanted (why did we focus so much on this in 2021-2025?  im not quite sure, i think it was part of some assumptions about dao governance at the time..). it turns out building great software is really hard and it needs pockets of contributors with high trust/context/enablement.  and no one cares about governing something thats a sinking ship.  this caused a downward spiral of irrelvance for gitcoin, and most of the people who worried about cartels in 2021 were long gone by 2025 (actually many stewards disengaged in that period).

i think that once gitcoin again has a product in market that people actually want, we can and should worry a lot about preventing cartels (and arguably trustgraph does a lot to provide the right foundations for that time, and will put us in a good position if were in a fortunate enough position that gitcoin has built a very valuable protocol to be governed by then). but until then, i think this is secondary in priority to building a product ppl actually want.

> When will the full rule‑set for signal decay (half‑life, thresholds, negative signals) be published so the graph does not operate as a black box?

i defer to @JakeHartnell on this

> Since the cohort’s charter is to “keep the 3.0 team honest”, what measurable accountability metrics will you track to show this is happening in practice?

the main thing that matters to me is my mandate as executive steward

[quote="owocki, post:1, topic:23352"]
Return Gitcoin to its former glory

* restore Gitcoin’s social, economic, and reputational standing

[/quote]

i dont know how to quantify this (yet).

but… gtc holders continue to have the ability to vote on snapshot/tally, just like before.  the trustgraph is supportive of this structure, not competitive.

> What clear eligibility criteria will govern the shift from a founder‑selected list to “earned trust” membership in the trust graph and steward cohort?

for the seed of my delegations in the trust graph, its “do you understand gitcoin past + proposed future? can i have an honest/constructive conversation with you? can you allocate 3 hours a month to gitcoin governance?  will you be direct with me, whether its good or bad?”

when someone in the trustgraph, makes their own endorsement of someone new, their eligbility criteria are up to them.

> Which parts of the context window are guaranteed to be public, and will you commit to specific publishing SLAs for those artifacts?

i was planning on publishing notes from the transitionary stewards context window under chattham house rules to the gov forum (which will show up in the gitcoin gov brain).

> At the 25% (Dec 2026) and 75% (July 2027) checkpoints, what explicit levers do GTC holders have if the trust‑graph design under‑performs its goals? @owocki

gtc holders continue to have the ability to vote on snapshot/tally, just like before.  the trustgraph is supportive of this structure, not comptetitive..

*Disclaimer: This post is for informative purposes only and is not financial advice. This post reflects my personal views ahead of the stewards’ review, not a decision or commitment by Gitcoin governance. Forward-looking items in it are targets, not commitments. The information in these posts is subject to change as we continue learning. This post may contain estimates, may contain errors, and is provided on a best-effort basis. DYOR, do not make any financial decisions based on these posts.*

---

Disclaimer: This post is for informative purposes only and is not financial advice. This post reflects my personal views, not a decision or commitment by Gitcoin governance. Forward-looking items in it are targets, not commitments. The information in these posts is subject to change as we continue learning. This post may contain estimates, may contain errors, and is provided on a best-effort basis. DYOR, do not make any financial decisions based on these posts.

-------------------------

cecilerx1 | 2026-08-07 16:08:24 UTC | #4

I measured something adjacent that might be useful here, and it cuts both ways on the sybil question.

I ran a simulation of an invitation-based redistribution network — 500 real participants, empty wallets added as an attack. Each empty wallet captured 1.7× what an average account would, and the ratio held constant from 1 to 1,000 fake accounts: no threshold, no minimum viable size, three addresses already return 1% of the pot. About 215 fake addresses were enough to divert half the redistribution away from 500 real users. Past a majority of accounts, the genuinely poorest fifth dropped from 67% to 3%.

But your point holds, and that's the interesting part: the attack disappeared entirely when I changed the destination. Once the allocation went to a vetted list of recipients rather than to accounts, an empty wallet captured nothing. The most severe flaw in my design vanished not because I fixed it, but because I changed who receives.

So "no bonus to generating identity" seems exactly right as a defence — with one caveat worth naming explicitly. It protects the money. It does nothing against the failure mode you already listed as cliques and cartels, because that's real people coordinating, not fake ones. Sybil resistance and cartel resistance are different problems, and only one of them is solved by having nothing to capture.

On your founder-seeded graph: I modelled invitation growth as R = k × p, invitations per member times acceptance rate. Below R = 1 the network freezes permanently at founders / (1 − R) — with 3 invitations and 25% acceptance you stop at 80 members forever, and no later effort recovers it. Worth watching early if you're starting from \~5 people.

Scripts and full measurements are open, happy to be contradicted on any of it.

-------------------------
