---
id: 23042
title: "Mechanism Builders Domain - GG24 Sensemaking Report"
slug: mechanism-builders-domain-gg24-sensemaking-report
category: gitcoin-sensemaking-szn
url: https://gov.gitcoin.co/t/mechanism-builders-domain-gg24-sensemaking-report/23042
created_at: 2025-08-16T09:41:53.377Z
last_posted_at: 2025-09-11T09:47:56.164Z
posts_count: 5
views: 1378
like_count: 5
---

# Mechanism Builders Domain - GG24 Sensemaking Report

<https://gov.gitcoin.co/t/mechanism-builders-domain-gg24-sensemaking-report/23042>
thedevanshmehta | 2025-08-19 22:52:56 UTC | #1

**Problem**

Ethereum as an onchain economy needs to solve its own public goods problem. Specifically, if a project or open source repo provides a value of $10 to 10 revenue generating organizations but requires $60 for its upkeep, it ends up getting underfunded despite a positive expected value of $40 to the ecosystem as a whole. No individual picking up the entire bill of $60 makes sense, but at the same time if the ecosystem supported the project everyone benefits more than if it was unsupported.

As we start to see the launch of more L2s and EVM based alt L1s, solving this coordination failure becomes paramount. If they each pay their share for ecosystem goods that make everyone better off, it starts a flywheel effect where more institutions join the party, solidifying Ethereum network effects and dominance.

Vitalik has written on the [general directio](https://balajis.com/p/credible-neutrality)n for solving these issues. He proposes working on credibly neutral funding mechanisms that have

1. mandatory indirection without specific people or institutions written into the mechanism itself (a feature that grant making bodies lack)

2. Open source and verifiable execution (such as quadratic funding)

3. Keeping it simple with minimal changes (like protocol guild)

We propose a domain around this theme both as a way of bringing together the small space of funding mechanism builders and also to create an incentive for more to join this niche. Eventually, we want all revenue generating organizations in Ethereum or EVM to put money into credibly neutral funding mechanisms that can auto-allocate to the network goods they depend on and that bring them a +EV

**Why Now?**

Gitcoin has shifted strategy, from relying upon mechanism builders in its grant rounds to leveraging the funding mechanism across the ecosystem. For this strategy to work, we need to incentivize good funding mechanisms that can be deployed across the various domains . So at a simple level, this domain will bring all mechanism builders onto one page and show the ecosystem the availability of various allocation mechanisms they can use for their specific domain.

In the recent [GreenPill podcast](https://www.youtube.com/watch?v=b81LXpCqunk), Vitalik mentioned that there is room for 5-8 credibly neutral funding mechanisms to support Ethereum’s growth. Thus far, we only have 3 piloted at scale: QF, RetroPGF, and Guilds. We need to dramatically accelerate the pace at which we build out such mechanisms to supercharge the Ethereum ecosystem. With Octant kickstarting its [Ethereum Sustainability Fund](https://x.com/OctantApp/status/1922391450056032713) & other [proposals](https://beta.fileverse.io/files/b6dfa2ad-f7a3-4a90-b937-82a22f9388f6) to route validator rewards towards such mechanisms, we need to grow the space so that it is already battle tested before we can entrust larger amounts to them.

This proposal will be a domain

* Restricted to those who build funding infrastructure only
* Amounts will be distributed at end of 6 month period instead of beginning

Allocations to each team will depend on actual value flowing through mechanisms, incentivizing adoption of their tech stack instead of rewarding those who  simply build tech or can better discipline their community

**Why GG24?**

Gitcoin has adopted a new role in the ecosystem: rather than competing with other mechanisms, it seeks to become a schelling point bringing all mechanisms together This domain would formalize the process by getting mechanism builders (such as gardens, hypercerts, butter, etc) into one domain. 

Simultaneously, as the allocation mechanism depends on actual business metrics (specifically, how much money has been entrusted for streaming through your protocol) it would incentivize actual adoption over simply building new mechanisms that may not receive any actual usage.

By proposing this formally as a GG24 domain, we hope to also gauge organic interest in the niche of building funding mechanisms.

**Satisfaction Test**

The money given under this domain will only be distributed after 6 months. The only criteria will be actual usage of the funding mechanism, ie, how much funding has been distributed through it? So we have a quantitative measure to show success in 6 months, that is, how many of the funding mechanism builders that applied under this domain actually had use in the 6 month period and in what amounts?
As a general note, retro funding works better when expectations are communicated much in advance, giving teams time to align around achieving them before funding is distributed. We would measure genuine impact through emergence of funding mechanisms that can be credibly recommended for GG25 as they have proven their stripes in this round.

Overall, we want more of the Ethereum ecosystem to move from grant allocations or committees towards credibly neutral funding mechanisms. We can measure whether the Ethereum community  is glad we funded this domain based on whether we start to see more adoption of this infra vs the regular grant making bodies at foundations deciding the teams that get funded and for how much.

**Implementation**

This domain is open to only those who are building or have deployed credibly neutral funding infrastructure. The actual allocation of funding to these domain builders would depend on total value that has flowed through their mechanism with a quadratic instead of proportional distribution.

Devansh Mehta is an expert in this area who will run this domain and ensure high quality applications. While we eventually eventually want to move to a version of streamed funding (such as superfluid) based on metrics achieved over time like funding flowing through the mechanism, for GG24 the following process will be followed;

* Accept applications until a cut off date
* Domain experts approve or reject applications
* Deployment period starts where successful applicants are encouraged to get as much funding flowing through their onchain mechanism as possible
* At end of deployment period, domain experts review amount flowing through the mechanisms of various applicants and disqualify those engaging in wash trading or other unethical behavior
* The overall funding in this pot is then distributed based on quadratic division of amount that was allocated via these mechanisms. For example, if drips is used to distribute $100,000 and hypercerts $25,000 in the 6 month period, we will not use a proportional 3:1 split for the funding pot but instead a quadratic split. If a mechanism is approved into the round but does not get any business testing it, they receive 0 funds from the pot.

There may be sub rounds for applicants. For example, while hypercerts as a whole might apply under the domain, there are many teams working on hypercerts. So the hypercerts team might pass on revenue earned to those builders depending on value flowing through their platform.

-------------------------

owocki | 2025-08-18 22:15:16 UTC | #2

# Draft Scorecard

## 2025/08/18 - Version 0.1.1

## By Owocki

## Prepared for Devansh Mehta re: "Mechanism Builders Domain - GG24 Sensemaking Report"

(vibe-researched-and-written by an LLM using [this prompt](https://github.com/owocki/gg24/blob/main/prompt_individual.txt), iterated on, + edited for accuracy quality and legibility by owocki himself.)

## Proposal Comprehension

TITLE
Mechanism Builders Domain - GG24 Sensemaking Report. 

AUTHOR
Devansh Mehta. 

URL
[https://gov.gitcoin.co/t/mechanism-builders-domain-gg24-sensemaking-report/23042](https://gov.gitcoin.co/t/mechanism-builders-domain-gg24-sensemaking-report/23042) ([Gitcoin Governance][1])

### TLDR

You propose a GG24 domain focused on funding mechanism builders. Teams apply, build or deploy credibly neutral allocation mechanisms, then after a 6-month deployment window the domain distributes funds retroactively based on actual usage measured by value routed through each mechanism, with a quadratic split rather than proportional to dampen concentration and an explicit review to disqualify wash trading. The goal is to accelerate adoption of a small portfolio of simple, verifiable, credibly neutral funding mechanisms across Ethereum. 

### Proposers

Devansh Mehta

EF Next Billion fellow and active contributor in public goods funding experiments, Gitcoin ecosystem contributor, AI x public goods focus.

### Domain Experts

not listed yet beyond Devansh as domain lead

Consider a small review panel drawn from neutral mechanism researchers and implementers to reduce single-point-of-failure and bias.

### Problem

Public goods that create ecosystem value are underfunded because benefiting institutions do not internalize shared costs. As more L2s and EVM L1s proliferate, Ethereum needs credibly neutral mechanisms that can route recurring, verifiable funding toward shared infrastructure without centralized committees.

### Solution

Create a dedicated domain for mechanism builders. Approve builders of credibly neutral mechanisms only. Run a 6-month deployment period. Allocate the pot retroactively by a quadratic function of dollars routed through each approved mechanism, subject to anti-wash reviews. Use the domain to make Gitcoin a schelling point that catalogs and validates mechanisms that other domains can adopt.

### Risks

1. metric gaming: “value routed” can be wash-traded, circularly streamed, or double-counted across integrations; mitigations need to be crisp and consistent. 
2) comparability: mechanisms differ in primitives, UX, and eligible flows, so a single metric may unfairly advantage certain designs. 
3) time to impact: a 6-month window means little evidence by October. 
4) governance load and neutrality: one lead approving and adjudicating wash trades concentrates discretion; needs a multi-expert rubric. 
5) fragmentation: too many micro-mechanisms can confuse domains unless the program emphasizes adoption and interoperability.

## Outside Funding

Not specified. You reference emerging co-funding vectors like Octant’s Ethereum Sustainability Fund and validator-rewards routing proposals, which could complement this domain if aligned, but they are not yet committed here.

## Why Gitcoin?

Gitcoin’s new role is convening and coordinating mechanisms rather than competing with them. The network, schelling power, and GG24 structure are well suited to run a domain that validates and routes attention to proven mechanisms, especially given the recent strategic shift away from operating Grants Stack as a product and toward funding what matters through community-operated domains. 

## Owockis scorecard

| # | Criterion                                                         | Score (0-2) | Notes                                                                                                                                       |
| - | ----------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Problem Focus – clearly frames a real problem, avoids solutionism | 2           | Core Ethereum problem, crisply framed around credibly neutral funding mechanisms.                                                           |
| 2 | Credible, high leverage, evidence-based approach                  | 1           | Retro pot keyed to adoption is promising, but metric design and anti-gaming plan need more specificity.   Also is retro the right funding mechanism? would a better route be to encourage angels/vcs to invest in these apps and make sure they make revenue so tehy are investable?                                    |
| 3 | Domain Expertise – active involvement from recognized experts     | 2           | Devansh has relevant track record. Add 2–3 independent reviewers to fortify neutrality.                   |
| 4 | Co-Funding – financial backing beyond Gitcoin                     | 0           | No confirmed co-funders yet. References to Octant and validator routing are directional only.                   |
| 5 | Fit-for-Purpose Capital Allocation Method                         | 2           | Usage-weighted retro makes sense for mechanisms, but single metric may bias results without normalization.                                  |
| 6 | Execution Readiness – can deliver meaningful results by October   | 2         | Six-month measurement means limited impact evidence by Oct. You can stand up the domain, but outcomes land later.  |
| 7 | Other – general vibe check                                        | 2           | Directionally strong and aligned with Gitcoin 3.0. Needs clearer guardrails and governance design.              |

### Score

Total Score: 11 / 14
Confidence in score: 70%

### Feedback:

#### Major

* tighten the metric: define exactly what counts as “value routed,” how to dedupe flows, and how to detect and penalize wash activity. Publish examples and edge cases up front.
* raise outside funding
* is retro the right funding mechanism? would a better route be to encourage angels/vcs to invest in these apps and make sure they make revenue so tehy are investable?

#### Minor

* diversify decision making: add an explicit, named review panel and a transparent rubric for approvals and for post-hoc disqualifications to preserve credible neutrality.
* normalization: consider normalizing by address count, unique funders, or integrator diversity so the quadratic split does not just reward one large whale sponsor.
* timeline fit: add an interim milestone by October with early adoption signals, even if the retro payout is six months out.
* interoperability: encourage common attestations or receipts across mechanisms so usage data is auditable and comparable.

### Steel man case for/against:

#### For

If Gitcoin convenes a neutral portfolio of mechanisms and rewards actual adoption, we shift the culture from “ship a demo” to “prove it in production.” A small set of simple, verifiable mechanisms can become default rails for domains, L2s, and foundations, compounding network effects for public goods.

#### Against

Usage-based retro allocation can be gamed or skewed toward mechanisms that are easier to inflate on-chain. Without rigorous metrics, cross-mechanism comparability, and independent oversight, the pot could reward the best marketers or the best gamers, not the mechanisms with the strongest long-term social surplus.

### Rose/ Bud/Thorn

rose
Clear, ecosystem-level intent. Retro allocation tied to adoption is aligned with incentives and could accelerate real usage if guardrails are tight.

thorn
Ambiguity in the “value routed” metric and in review governance. Single-lead discretion plus a 6-month lag creates execution and neutrality risks.

bud
If you publish a shared data schema for “funds routed,” standardized attestations, and a public dashboard, this domain could become the spine for future validator-revenue pilots and other co-funding programs.

## Feedback

Did I miss anything or get anything wrong? FF to let me know in the comments.

-------------------------

deltajuliet | 2025-08-19 22:52:37 UTC | #3

Thanks @thedevanshmehta for submitting this. I found this one tricky but agree w/ the theme of the proposal. 

Evaluated using [my steward scorecard](https://gov.gitcoin.co/t/gg24-domain-proposal-voting-scorecards/23016/5?u=deltajuliet) — reviewed and iterated manually for consistency, clarity, and alignment with GG24 criteria.

---

### ✅ Submission Compliance
- Format and structure are clear and tight  
- Sensemaking section exists, but doesn’t do what it’s supposed to: no data aggregation, no comparative analysis, no synthesis  
- No co-funding partners identified  
- Domain lead named and scoped; mechanism design is defined  
- Verdict: **Compliant, but barely** — technically hits the format, but misses depth in signal synthesis

---

### 📊 Scorecard Evaluation  
**Total Score: 11 / 16**

| Criteria | Score | Notes |
|----------|-------|-------|
| Problem Clarity | 2 | Frames underfunded mechanism infra as a real risk for Ethereum |
| Sensemaking Approach | 0 | No methodology or ecosystem mapping — thesis-only proposal |
| Gitcoin Fit | 2 | Gitcoin as coordination layer makes sense here |
| Fundraising Plan | 0 | No matchers or partners listed |
| Capital Allocation Design | 2 | Usage-weighted RF is simple and testable |
| Domain Expertise | 2 | Devansh is credible and the domain is scoped narrowly |
| Clarity & Completeness | 2 | Reads like a deployment plan, not a grant ask — which is a good thing here |
| Gitcoin Support Required | 1 | Metric validation and governance scaffolding would fall on Gitcoin unless a panel is named |

---

### 📌 Risks + Opportunities

**Where I agree with Owocki:**  
- You’ll need an external review panel to avoid centralizing discretion  
- “Value routed” as a metric is gameable unless you define it precisely  
- Co-funding would de-risk Gitcoin’s exposure, and none is named

**What I’d add:**  
- If this works, Gitcoin becomes the **indexer of credible funding rails** — not just an experimenter. That’s a useful role to play post-Grants Stack.
- If this fails, it fails quietly. Worst-case outcome is that no one uses the mechanisms and the domain pays out nothing — that’s a relatively safe bet from Gitcoin’s side.
- The ops layer here is under-explained. If this is running during GG24, who’s collecting usage metrics? Who handles disputes? This isn't high-touch, but it’s not no-touch either.

---


Would support if:
- A light sensemaking layer is added (even 5–6 sentences naming the state of mechanism design in Ethereum)  
- At least one reviewer or governance structure is confirmed  
- A public definition of “value routed” is published — with edge cases and disqualification guidelines

-------------------------

sepu85 | 2025-08-25 12:30:59 UTC | #4

Thanks for surfacing this **Mechanism Builders** domain — the idea of cultivating a dedicated space for mechanism design feels very aligned with Gitcoin’s broader vision.

In our [proposal](https://gov.gitcoin.co/t/gg24-sensemaking-report-at-pre-post-grant-coordination-from-allocation-to-alignment-accountability/21711), we didn’t propose a domain per se. Instead, we’re trying to validate whether **CollabBerry’s peer-based contributor allocation and post-grant accountability tools** could serve as a mechanism that cuts across domains.

What we see in your proposal is an emphasis on **expanding Gitcoin’s mechanism portfolio**. From our perspective, CollabBerry can be understood as exactly that: a mechanism for the “last mile” — once grants are distributed to projects, how do teams internally allocate funds, recognize contributions, and align incentives transparently?

We’d love to learn if this resonates with the Mechanism Builders community: would you consider contributor-level allocation tools like CollabBerry as part of the mechanism design landscape Gitcoin should be nurturing?

-------------------------

thedevanshmehta | 2025-09-11 09:47:56 UTC | #5

We would like to withdraw this domain for consideration in GG24, in light of the fair fees approach helping mechanism builders in addition to other domains centered around PGF tooling and research such as the ones proposed by @DavidDAO and @paul2

Overall, a performance based bonus for mechanism builders based on value flowing through their mechanism can move the space ahead in the long term. Currently, there is a higher value add in advising the ongoing domains in this area than managing our own

-------------------------
