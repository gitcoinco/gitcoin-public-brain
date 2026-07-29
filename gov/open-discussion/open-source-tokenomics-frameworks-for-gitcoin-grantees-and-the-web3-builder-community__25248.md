---
id: 25248
title: "Open-Source Tokenomics Frameworks for Gitcoin Grantees and the Web3 Builder Community"
slug: open-source-tokenomics-frameworks-for-gitcoin-grantees-and-the-web3-builder-community
category: open-discussion
url: https://gov.gitcoin.co/t/open-source-tokenomics-frameworks-for-gitcoin-grantees-and-the-web3-builder-community/25248
created_at: 2026-04-29T21:14:41.689Z
last_posted_at: 2026-04-29T21:14:41.788Z
posts_count: 1
views: 27
like_count: 2
---

# Open-Source Tokenomics Frameworks for Gitcoin Grantees and the Web3 Builder Community

<https://gov.gitcoin.co/t/open-source-tokenomics-frameworks-for-gitcoin-grantees-and-the-web3-builder-community/25248>
robtg4 | 2026-04-29 21:14:41 UTC | #1

## Who I Am

I’m Robby Greenfield. I’ve been in crypto since 2011, worked at Goldman Sachs, then spent years as Head of Social Impact at ConsenSys — building humanitarian blockchain infrastructure with the World Food Programme, Red Cross, and Oxfam across 17 countries. I later co-founded the Devcon Scholars program and served on the EU Blockchain Observatory Expert Panel.

Then I built my own DeFi protocol. It failed. Cost me $200K. :frowning:

That failure led me to spend 1,212 days systematically analyzing what makes tokenomics work — and what makes them collapse. The result is the [Tokédex](https://tokedex.org): a 674-page reference covering 34 DeFi protocols across 10 categories, each analyzed through 25 proprietary frameworks.

## Why I’m Posting Here

Gitcoin has always been about funding public goods and equipping builders with the tools they need to ship meaningful work. One of the most persistent gaps I see in the ecosystem is tokenomics literacy — not the theory, but the practical analytical capacity to evaluate whether a protocol’s incentive structure will actually hold up under real market conditions.

This gap has real consequences. The recent rsETH/Kelp incident on Aave exposed how supply cap mechanisms interact with bridge trust assumptions in ways that most governance participants didn’t have frameworks to anticipate. I’ve been actively contributing analysis in Aave governance on this — specifically on [gnarvaja’s Automated Supply Cap Updater proposal](https://governance.aave.com/t/temp-check-automated-supply-cap-updater-restricting-short-term-supply-increases-in-aave-v3/24632/4), [my personal [TEMP CHECK] Post-rsETH Collateral Framework: Tier-Based LTV Reductions and Wrap-Depth Ineligibility Limits proposal](https://governance.aave.com/t/temp-check-post-rseth-collateral-framework-tier-based-ltv-reductions-and-wrap-depth-ineligibility-limits/24726) and [LlamaRisk’s post-incident cap recalibration](https://governance.aave.com/t/risk-stewards-supply-and-borrow-cap-adjustments-on-aave-v3-2026-04-24/24739/5) — using the same analytical frameworks from the Tokédex to break down why static caps failed, how adversarial feedback loops emerge between automated systems, and why siloed pooling with eligibility gating is more architecturally sound than trying to engineer safety through oracle layers that can’t operate in sub-block time.

**The point isn’t the book.** The point is that these frameworks should be accessible to every builder and governance participant in the ecosystem — not locked behind institutional research desks. In fact, I have since operationalized the frameworks so that they can be applied (and process) protocol and digital asset data to assess [systemic risks in DeFi](https://www.tokedex.org/assets). 

## What I’m Sharing (Free)

The analytical frameworks from the Tokédex are available for free at [tokedex.org](https://tokedex.org). These 25 frameworks include:

* Token Design & Incentive Frameworks — incentive alignment scoring, value accrual mechanics, stakeholder mapping, governance structure analysis, risk topology, token utility mapping, and more
* Protocol Category Taxonomies — structured breakdowns of how tokenomics function differently across lending, DEXs, derivatives, stablecoins, liquid staking, restaking, L1s, L2s, and bridges
* Failure Pattern Analysis — documented patterns from protocols that imploded (Olympus, Terra, Iron Finance) mapped against the structural characteristics of survivors (Aave, Curve, Uniswap, Lido)
* Governance Risk Evaluation — frameworks for assessing how governance token distribution creates concentration risks, voter apathy dynamics, and adversarial capture vectors

These aren’t theoretical models. They’re built from analyzing \~60 live protocols — what the docs say versus what actually happens under market pressure.

## How This Connects to Gitcoin

I see three direct applications for the Gitcoin community:

1. ⁠For Grantees building protocols: Tokenomics are usually the last thing builders think about and the first thing that kills a project. These 25 frameworks give teams a structured way to stress-test their token designs before shipping — the evaluation I wish I’d had before my own protocol failed.
2. ⁠For Governance participants: Whether you’re evaluating Gitcoin proposals, participating in partner protocol governance, or assessing grant applications that involve token mechanics, having a consistent analytical framework makes the difference between pattern-matching on vibes and making informed decisions.
3. ⁠For the broader public goods mission: Tokenomics literacy is a public good. The more builders who understand how incentive structures actually behave — not how they’re marketed — the fewer catastrophic failures we get, and the more trust the ecosystem retains. Every protocol collapse sets the whole space back.

## The Ask

No funding request. No grant proposal. I’m sharing this as a resource for the community. Ideally, we can work together to make this a decentrally authored and published book via GitHub someday :slight_smile: 

The digital edition of the Tokédex is free for research and educational use at [tokedex.org](https://tokedex.org). Physical hardcovers are available at [store.tokedex.org](https://store.tokedex.org) for anyone who prefers books they can hold.

If you’re a builder working on tokenomics, a governance participant trying to evaluate protocol risk, or an educator teaching the next wave of web3 developers — these frameworks are built for you.

Happy to answer questions, discuss specific protocol mechanics, or collaborate on making tokenomics education more accessible as a public good.

–– Robby Greenfield | [@robtg4](https://twitter.com/robtg4) | [tokedex.org](https://tokedex.org)

-------------------------
