---
id: 22989
title: "Gitcoin Grants 24: Submission of Problem Briefs"
slug: gitcoin-grants-24-submission-of-problem-briefs
category: gitcoin-grants
url: https://gov.gitcoin.co/t/gitcoin-grants-24-submission-of-problem-briefs/22989
created_at: 2025-08-14T20:05:46.110Z
last_posted_at: 2025-08-14T20:05:46.219Z
posts_count: 1
views: 897
like_count: 1
---

# Gitcoin Grants 24: Submission of Problem Briefs

<https://gov.gitcoin.co/t/gitcoin-grants-24-submission-of-problem-briefs/22989>
devmaster | 2025-08-14 20:07:46 UTC | #1

## 1. Problem & Impact

**The Problem:**
Ethereum’s scaling strategy via Layer-2 (L2) rollups has created a rich ecosystem — but also severe **fragmentation**. Each L2 functions as an isolated environment with its own liquidity pools, dApps, and user base. Moving assets between L2s is often slow, costly, and inconvenient: the most common route involves bridging to L1, then re-depositing to another L2, taking hours or even days.

This has two major effects:

* **Liquidity fragmentation**: Liquidity providers must split funds across chains, leading to shallow pools, higher slippage, and worse user experience.
* **Loss of composability**: dApps can’t easily interact across L2s, breaking the “one big Ethereum” user experience.

**Evidence & Urgency:**

* Vitalik Buterin warned in 2023: without cheap, seamless L2 transactions, Ethereum risks losing users to centralized, high-throughput chains.
* Despite record DeFi TVL, rival chains like Solana have surpassed Ethereum in active DEX users (2025 data, Artemis & DefiLlama).
* Research by L2Beat and LI FI (2024) highlights bridging delays and liquidity isolation as critical obstacles to scaling adoption.
* DEX liquidity across L2s is highly uneven — small L2 pools often rely on slow, manual bridging from large L2s for rebalancing.

**Why This Matters Deeply:**
This is not hype-driven — it is **core infrastructure**. Both users and developers are directly affected:

* **Users** face higher costs, long wait times, and missed opportunities (e.g., in DeFi arbitrage).
* **Developers** must maintain multiple deployments, fragmenting their user base and liquidity.

**Impact of Solving This:**

* Unified liquidity across L2s → deeper pools, better prices, more active DeFi.
* Faster, cheaper cross-L2 transfers → improved UX and onboarding.
* Stronger Ethereum network effects → retaining users and developers.

## 2. Sensemaking Analysis

**Tools Used:**

* **Ecosystem Mapping:** Surveyed L2 rollups, existing bridges, and shared liquidity solutions.
* **Gap Analysis:** Compared current cross-chain infrastructure to Ethereum’s composability ideals.
* **On-chain Data Review:** Used DefiLlama, L2Beat, and Artemis data to identify liquidity distribution and transaction patterns.

**Sources:**

* Vitalik Buterin’s blog posts on scaling & decentralization trade-offs.
* Reports from L2Beat, LI.FI, and Chainlink on interoperability challenges.
* Gitcoin Grants history showing strong community support for infra/tooling rounds (GG18–GG23).
* Discussions from Ethereum Magicians, ETHResearch forums, and recent Devconnect panels.

**Aggregation Method:**

* Clustered pain points into **liquidity fragmentation**, **slow/unsafe bridging**, and **lack of shared standards**.
* Identified potential interventions: fast trust-minimized bridges, shared sequencers, cross-chain messaging protocols, and liquidity aggregation layers.
* Cross-referenced with past Gitcoin-funded infra successes to validate feasibility.


## 3. Gitcoin’s Unique Role & Fundraising

**Gitcoin’s Advantage:**

* Proven track record funding critical Ethereum infra (ethers.js, WalletConnect, Scaffold-ETH).
* Community governance ensures solutions remain **open-source public goods** rather than proprietary products.
* Quadratic Funding draws diverse stakeholder support, not just single-entity dominance.

**Why a Network Beats a Hierarchy:**

* L2 fragmentation affects many actors differently; only a decentralized network of builders can create widely adopted, chain-agnostic standards.
* Centralized actors (VC-funded infra) may prioritize chain-specific or closed solutions.

**Funding Reality:**

* **Target:** $50K+ matching pool is realistic.
* **Likely Sponsors:** Optimism, Arbitrum, Base, Polygon, StarkWare, zkSync, Uniswap, Curve, Aave, Chainlink, Connext.
* **Commitments:** Early soft interest from interoperability protocol teams and L2 foundations in supporting public-good bridges and liquidity layers.


## 4. Success Measurement & Reflection

**6-Month Success Outcomes:**

* 2+ open-source fast-bridge or shared liquidity prototypes deployed to mainnet.
* 5+ major DeFi protocols integrate funded interoperability solutions.
* 20% average reduction in bridging times between top L2 pairs.

**Impact Measurement Beyond Activity:**

* **Adoption Metrics:** Volume of assets moved using funded tools.
* **Developer Integration:** Count of dApps and wallets enabling cross-L2 swaps.
* **User Feedback:** Net Impact Score > 7/10 on UX improvement surveys.

**Satisfaction Test:**
The Ethereum community will celebrate if:

* Cross-L2 movement becomes **near-instant and trust-minimized**.
* Liquidity across L2s feels as unified as a single chain.
* DeFi, gaming, and NFT projects can scale without fragmenting users.


## 5. Domain Information

* **Proposing a Domain for GG24:** Yes — “Ethereum L2 Interoperability & Liquidity Unification.”
* **Domain Experts:** L2Beat researchers, Connext team, LI FI engineers, Chainlink CCIP team, leading DeFi protocol devs.
* **Mechanisms:** Quadratic Funding for early-stage infra, Retro Funding for proven adoption, Community Rounds for ecosystem-wide experiments.
* **Possible Sub-Rounds:**
  * Fast-Bridge Infrastructure
  * Shared Liquidity Layers
  * Cross-Chain Standards & Messaging

-------------------------
