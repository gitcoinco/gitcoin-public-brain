---
id: 21070
title: "[DRAFT] Core Technology Investments for Gitcoin 3.0 (GG24 Edition)"
slug: draft-core-technology-investments-for-gitcoin-3-0-gg24-edition
category: open-discussion
url: https://gov.gitcoin.co/t/draft-core-technology-investments-for-gitcoin-3-0-gg24-edition/21070
created_at: 2025-06-18T20:12:12.601Z
last_posted_at: 2025-06-20T16:59:11.043Z
posts_count: 3
views: 1229
like_count: 10
---

# [DRAFT] Core Technology Investments for Gitcoin 3.0 (GG24 Edition)

<https://gov.gitcoin.co/t/draft-core-technology-investments-for-gitcoin-3-0-gg24-edition/21070>
owocki | 2025-06-18 20:17:49 UTC | #1

x-post: https://research.allo.capital/t/draft-core-technology-investments-for-gitcoin-3-0-gg24-edition/396

# **\[DRAFT\] Core Technology Investments for Gitcoin 3.0 (GG24 Edition)**  
*Version: June 2025*

## TL;DR:

To realize the vision for Gitcoin 3.0, we must prioritize infrastructure that standardizes grants data, tracks impact, supports Dedicated Domain Allocation (DDA), and facilitates decentralized round proposals. These tools will form the foundation of a modular, scalable, and competitive community-driven capital allocation network aimed at Ethereums biggest problems.

## Scope:

This document covers Gitcoin 3.0 stuff, as the Gitcoin 2.2 stuff is already covered by [the other vendor (OV) proposal](https://docs.google.com/document/d/1OUfqAvTMCJZ5vlQdC8c8MztuvoAhJSTs1r6usq-2Iy0/edit?tab=t.0#heading=h.mxb0d3mkrvl0). Together, they form an arena through which the carnival of Ethereum public goods funding occurs.

![|624x412](upload://l2e8SNaZpVZhhHnJw1V5IsBUoPl.jpeg)

## Strategic Objective: Build the 3.0 foundation first

Before diving into specific technologies, it's important to understand why Gitcoin 3.0 requires this technological evolution.  The current proposals are focused on Gitcoin 2.2 era problems (QF, Retro Funding).  If implemented without Gitcoin 3.0 era context, this grants infrastructure lacks standardization across different funding mechanisms, making it difficult to track impact, maintain quality standards, or create meaningful interoperability or competitiveness between different grant programs. Think of this like the early days of the internet, when different networks couldn't communicate with each other—Gitcoin 3.0 aims to create the equivalent of standardized protocols that allow different grant ecosystems to work together seamlessly.

The technology investments for GG24 address three fundamental challenges: establishing common standards, enabling transparent impact measurement, and creating scalable governance mechanisms that can grow with the ecosystem.

## Why not just go with the other vendor (OV) proposal?

Other vendors (OV) proposal

1. Lacks build vs buy evaluation.  
2. Lacks the grants registry \+ impact reporting interoperability standards at the foundation.  
3. Does not see the forest for the trees. Assumes a continuation of Gitcoin 2.2 era thinking.  
4. Not the right vendor \- Is built by mercenaries selling their time, not founders building a world class product in exchange for distribution. Was scoped by someone who is not on good terms with allo.capital.  
5. Is too expensive.

---

### **(Gitcoin 3.0) 1\. Grants Registry**

**Objective:** Establish a canonical data layer for all grants across Gitcoin to ensure interoperability, legibility, and composability across the broader ecosystem.

**Problems Solved:**

* Disconnected, inconsistent grant records  
* Fragmented off-chain grant metadata  
* Replacement for the clunky/expensive Gitcoin 2.0 indexer infrastructure.  
* Inability to compose grant information across domains

**Proposed Features:**

* A common interface for storing and indexing grant metadata  
* An easy way to view/manage/update grants \+ search/discover grants.   
* An a way to migrate your Gitcoin 2.0 grants to the system.  
* Eventually,  
  * Support for decentralized identity, verification, and attestations  
  * Integration with AI grant reviewers (e.g., [Checker](https://docs.google.com/document/d/16KV0ijhTeKH46LaFySIwk7cs7jqxvFLKGNN5gLsMhWg/edit?tab=t.0#heading=h.bk6eklyopc1l) tool)

**Build vs. Buy Options:**

* Roll our own registry (tailored but expensive)  
* Use third-party standards (e.g., EAS, Optimism Attestations, DAOStar Grant IP)  
* Leverage existing platforms (e.g., Karma)

**Recommendation:**  
 Lean toward DAOStar and Karma, with an AI assistant (e.g., [Checker](https://docs.google.com/document/d/16KV0ijhTeKH46LaFySIwk7cs7jqxvFLKGNN5gLsMhWg/edit?tab=t.0#heading=h.bk6eklyopc1l)) for scalable grant evaluation and enforcement of minimum standards.

---

### **(Gitcoin 3.0) 2\. Impact Reporting System**

**Objective:** Provide a standardized, onchain or offchain method to report and verify grantee outcomes—critical for both legitimacy and learning.

**Problems Solved:**

* Low signal around outcomes  
* Inability to track longitudinal impact  
* Manual, inconsistent reporting practices

**Proposed Features:**

* Structured formats for outcome submissions  
* Integration with impact attestations (e.g., Hypercerts, EAS)  
* Support for multiple data modalities for different domains: text, metrics, media

**Build vs. Buy Options:**

* Native Gitcoin-built reporting interface  
* KarmaGAAP (structured, web3-native GAAP for impact)  
* Hypercerts (modular, composable attestation protocol)

**Recommendation:**  
Adopt KarmaGAAP as the foundation, with OSO for data support \- optional Hypercert support for projects aligned with emerging impact cert markets.

---

### **(Gitcoin 3.0) 3\. Dedicated Domain Allocation (DDA)**

**Objective:** Enable communities to define strategic domains with funding priorities and run rounds specific to those domains.

**Problems Solved:**

* Lack of structured funding goals  
* Difficulty aligning capital with ecosystem priorities  
* Limited participation of domain experts

**Proposed Features:**

* Domain metadata: title, description, amount already funded, funding goals, experts, optional theory of change  
* Admin interface for domain creators  
* GTC staking as a signal layer for curation

**Build vs. Buy Options:**

* Build custom Gitcoin-native DDA tooling  
* Reuse from existing open-source tools: Questbook, Grant Ships, Snapshot

**Recommendation:**  
Prototype on Grant Ships or Questbook.  Snapshot proposals can be a fallback. Use this as a stepping stone toward the “[Allo Arenas](https://research.allo.capital/t/request-for-feedback-allo-arenas/338)” ecosystem envisioned for GG25, where DDA domains evolve into persistent capital allocation collectives.

---

### **(Gitcoin 3.0) 4\. Round Proposal System**

**Objective:** Create a permissionless, onchain-native way for communities to propose and vote on grant rounds tied to domains.

**Problems Solved:**

* Centralized coordination bottlenecks  
* Lack of bottom-up round creation  
* Hardcoded round structures

**Proposed Features:**

* Simple UX for round submission, voting, and approval  
* Composability with domain data and grant registries  
* Onchain or snapshot-based governance  
* [Fair Fees](https://ethresear.ch/t/fair-fees-a-dynamic-formula-for-balancing-dapp-value-creation-capture/22225) or similar for rewarding round operators.

**Build vs. Buy Options:**

* Use Grant Ships for round proposals  
* Use snapshot  
* Build something custom here.

**Recommendation:**  
Reuse Grant Ships for quick iteration (assuming cost isnt a barrier) in GG24. In the future, design architecture that scales into a DAO-native funding proposal layer over time.

### **(Gitcoin 2.2) 1\. Quadratic Funding Tools**

**Objective:** Evolve Gitcoin’s flagship mechanism into a minimalistic modular, tunable, and interoperable system.

**Problems Solved:**

* High maintenance costs  
* Need for localized QF params (matching caps, identity levels, vote weights)  
* Inability to easily integrate QF into custom mechanisms

**Key Features:**

* Simple Quadratic Funding tooling: Great checkout experience  
* Fiat checkout  
* Support for tunable QF (e.g., capped matching, diminishing returns)  
* COCM sybil resistance.

**Build vs. Buy Options:**

1. Giveth  
2. CLRFund  
3. Other vendor proposal.  
4. Build our own.

**Recommendation:**  
Develop a minimalistic Quadratic Funding platform with easy checkout. 

---

### **(Gitcoin 2.2) 2\. Retro Funding Tools**

**Objective:** Create tooling for retroactive funding experiments like RetroPGF, where allocation happens after measurable outcomes.

**Problems Solved:**

* Upfront funding bias  
* Misalignment between outcome and reward  
* Difficulty in coordinating credible assessors

**Key Features:**

* Integration with OSO for data impact tracking  
* Badgeholder voting UI for funding decisions  
* Results calculations

**Build vs. Buy Options:**

5. Agora  
6. Gitcoins Impact Funding Tool  
7. Other vendor proposal.  
8. Build our own.

**Recommendation:**  
Do Impact Retro Funding in Google Sheets/Dune to start.  Then build something on top of that.

---

**Conclusion:**  
Gitcoin 3.0 technology must unify grants data, impact metrics, domain expertise, and round logic into a coherent ecosystem. By building these four pillars—Grants Registry, Impact Reporting, DDA, and Round Proposals—we lay the groundwork for a regenerative, scalable, and modular capital allocation network capable of serving the next decade of public goods.

By creating an alternative to the expensive other vendor bid, we can firm up the Gitcoin 2.2 era technology (QF, Retro Funding).

**Next Steps:**

* Lock tech stack choices by the end of June 2025\.  
* Launch prototypes by September 1 2025\.  
* QA \+ test round by October 1 2025\.  
* Cost the proposals.  
* Evolve toward Gitcoin 3.0 (Q1 2026\) with Allo Arenas, GTC staking, and full decentralization of round creation and domain governance

-------------------------

wasabi | 2025-06-18 23:43:17 UTC | #2

This post is a great bucket of clarity for the community of builders and donors. The fact that there are multiple options for each pillar/initiative/problem is great, also that UX is being optimized over "shiny things"

[quote="owocki, post:1, topic:21070"]
Do Impact Retro Funding in Google Sheets/Dune to start. Then build something on top of that.
[/quote]

For this Sheets/Dune idea, what if [Fileverse Sheets](https://dsheets.new/) is used instead of Google, as this demonstrates an Ethereum-first approach and also brings blockchain data natively to the spreadsheet, with strong provenance and authority support

-------------------------

LuukDAO | 2025-06-20 16:59:28 UTC | #3

Reviewed, and also here - aligned on recommendations from my position as a co-funder, builder, and round operator. 

The combination of Karma + Grant Ships at the core, with lean QF and Retro tools for allocation calculations, seems like a solid next step. 

Happy to contribute the Kolektivo Labs design and dev resources to contribute to making the operator and grantee UX sexy.

-------------------------
