---
id: 25346
title: "TEMP CHECK - trustgraph x transitionary stewards"
slug: temp-check-trustgraph-x-transitionary-stewards
category: open-discussion
url: https://gov.gitcoin.co/t/temp-check-trustgraph-x-transitionary-stewards/25346
created_at: 2026-07-17T14:35:32.306Z
last_posted_at: 2026-07-17T14:35:32.362Z
posts_count: 1
views: 9
like_count: 0
---

# TEMP CHECK - trustgraph x transitionary stewards

<https://gov.gitcoin.co/t/temp-check-trustgraph-x-transitionary-stewards/25346>
owocki | 2026-07-17 21:16:09 UTC | #1

# **TEMP CHECK - trustgraph x transitionary stewards**

## **tldr in 1(ish) sentence**

Kevin thinks [web of trusts are super powerful](https://gov.gitcoin.co/t/the-impact-web-of-trust-could-change-everything/17635).

he is working with [Jake Hartnell](https://x.com/JakeHartnell) to seed a trust graph with the gtc voting power he influences, so that delegation updates programmatically and founder power disperses as the graph matures.

## **tldr in 2 paragraphs**

**the mechanism**: stewards and community members attest to each other, the graph computes trust scores, and it outputs a delegation map that syncs regularly into gitcoin’s new openzeppelin governor. the graph gets pre-seeded from existing gitcoin data (gov history, grants participation, kevin’s archives) rather than asking anyone to perform new rituals, and influence decays if you go inactive. past contributors can reclaim their weight, but only by showing up and agreeing to a new social contract.

**status**: it’s a volunteer handshake between kevin and jake right now, with a simple proof of concept as the first milestone and the transitionary stewards cohort as a candidate pilot group. the big open questions are legitimacy of the initial seed, whether gitcoin and the [ethereum extitutional](http://extitution.io) effort share one graph or two, and whether the scope grows enough to need funding. feedback from stewards welcome.

## **the problem this solves**

gitcoin’s governance has a legitimacy gap. a large share of gtc voting power is currently delegated to kevin

he doesn’t want to be the permanent power broker of gitcoin. the goal is to disperse that power deliberately, before it becomes a crisis.

deliberately means that the care, give a shit, context, organizational history that kevin holds as founder is dispersed - not just power.

## **the idea**

seed a trust graph with the GTC voting power currently delegated to kevin. no tokens change hands, only delegation.

stewards and community members attest to each other. the graph aggregates those attestations into trust scores. delegation then updates programmatically as the graph evolves, with the explicit goal that founder influence shrinks as the graph matures.

the transitionary stewards cohort (aug 2026 through march 2027, per the[ temp check post](https://gov.gitcoin.co/t/temp-check-transitionary-stewards-cohort/25342)) is one of two candidate pilot groups, the other being the [ethereum extitutional](http://extitution.io) effort. instead of kevin hand-picking wallets and delegating to individuals, the cohort builds its own pockets of power emergently, and can eventually stand up to him.

## **who jake is**

Jake Hartnell led the development of TrustGraph (attestation-based governance, open source) last year. He’s also building adjacent primitives: “commitments” (self-enforcing agreements for sharing risk and reward) and Ainima (an agentic “Stigmergic Organization” experiment). Those are context, not part of this scope.

the engagement is currently a volunteer handshake.

## **how it works mechanically**

* scopelift is already upgrading gitcoin from governor bravo to the new openzeppelin governor (modular, compound-style).

* the likely delegation plumbing is the franchiser pattern: kevin delegates to a smart contract, which subdelegates out per the graph. subdelegates never custody anything, and the root can recall at any time. that’s the safety valve while trust is being established.

* the trust graph outputs a simple map of {address: delegation amount}, synced nightly, so delegations shift automatically as the graph evolves. no manual updating.

* kevin’s take: if this ships, gitcoin would be the first major DAO to run delegation through a computed trust graph.

## **seeding and data**

both kevin and jake agreed: don’t start from zero, and don’t invent new rituals people won’t do.

* bootstrap from existing gitcoin data: gov forum history, grants/QF participation, and kevin’s mirror mirror archive (3 years of gov posts, email, transcripts) queried for “who has clout at gitcoin right now.”

* decaying signal (jake calls it demurrage): influence fades if you’re inactive. someone who did great work 4 years ago and left doesn’t get to silently govern.

* past contributors can claim their influence, but only by showing up and agreeing to a new social contract.

* possible ongoing signal: attestations captured from the monthly steward calls themselves (gratitude/appreciation on calls becomes graph input).

## **design principles**

* gall’s law: start with a simple, pre-seeded proof of concept that works, and evolve it.

* the one thing that must be designed well up front is how the graph upgrades its own computation. if the graph can vote to change its own scoring, the shitty first version is fine.

* feedback loops matter: stewards who do good or bad should see that behavior positively or negatively reinforced through the graph. jake sees trustgraph as one way to keep those incentives from goodharting.

## **status as of jul 17**

* kevin is connecting jake with ben difrancisco / scopelift to dial in the governor integration; jake is getting access to the governor-upgrade work in progress.

* jake is exploring which gitcoin datasets (graphql, indexes) give the best trust signals.

* handshake proposal expected from jake by end of week.

* kevin and jake are discussing presenting trustgraph at an upcoming call with target users, and possibly co-authoring a one-page gov post. the story: extitutions and trust games, moving away from kevin as the trust center.

## **open questions**

1. **Which of these two designs do we want to do?**

   1. • SubDAO (does it’s own thing with whatever powers / budget it’s given). It’s separate from the main GitCoin governance.

   2. • TrustPool gets delegations and participates in main GitCoin governance DAO directly.

* 

*Disclaimer: This post is for informative purposes only and is not financial advice.* *This post reflects my personal views ahead of the stewards’ review, not a decision or commitment by Gitcoin governance. Forward-looking items in it, like the october node zero timing, are targets, not commitments.* *The information in these posts is subject to change as we continue learning. This post may contain estimates, may contain errors, and is provided on a best-effort basis. DYOR, do not make any financial decisions based on these posts.*

-------------------------
