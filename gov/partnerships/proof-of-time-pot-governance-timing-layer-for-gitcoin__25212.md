---
id: 25212
title: "Proof-of-Time (PoT) — Governance Timing Layer for Gitcoin"
slug: proof-of-time-pot-governance-timing-layer-for-gitcoin
category: partnerships
url: https://gov.gitcoin.co/t/proof-of-time-pot-governance-timing-layer-for-gitcoin/25212
created_at: 2026-03-30T02:05:30.147Z
last_posted_at: 2026-03-30T02:05:30.245Z
posts_count: 1
views: 62
like_count: 0
---

# Proof-of-Time (PoT) — Governance Timing Layer for Gitcoin

<https://gov.gitcoin.co/t/proof-of-time-pot-governance-timing-layer-for-gitcoin/25212>
Heime-Jorgen | 2026-03-30 02:05:30 UTC | #1

# Proof-of-Time (PoT) — Governance Timing Layer for Gitcoin

Category: Governance Tools
Author: OpenTTT Research Team (heime.jorgen@proton.me)
Relevant links:
∙	IETF draft-helmprotocol-tttps-00
∙	EIP-8201
∙	npm install openttt

---

**Summary**


Note (March 2026): Tally shut down last week, leaving 500+ DAOs without a governance frontend. PoTVotingStrategy.sol is OZ Governor-compatible and ready to deploy.


We are proposing the integration of Proof-of-Time (PoT) as an optional governance strategy for Gitcoin DAO. PoT cryptographically verifies when a vote was cast, making vote timing manipulation detectable and making Gitcoin’s governance record MiCA-compliant.

We’ve built PoTVotingStrategy.sol — a drop-in
extension for any OpenZeppelin Governor DAO that
cryptographically verifies *when* a vote was cast.

**Why now:**
Tally shut down last week. 500+ OZ Governor DAOs
need a new path. PoTVotingStrategy.sol is ready.

**What it does:**
— Binds Ed25519 timestamp to every vote
— ERC-1155 permanent on-chain anchor
— MiCA Q2 2026 compliance automatic
— Soft mode (90% weight) or Strict mode

**Background**


The ordering problem in blockchain — who gets to go first, and can that be proven? — has become an active research area in MEV. Mazorra, Schlegel, and Mamageishvili’s Timing Games paper proved that transaction spam is not a bug but a Nash equilibrium: rational actors should spam when V/c is large.

Our follow-up article, published in the Flashbots Collective and featured in MEV Letter #131, shows how PoT shifts that equilibrium by raising c structurally:

**Proof-of-Time: Completing the Timing Game**

https://collective.flashbots.net/t/proof-of-time-completing-the-timing-game/5633


The same mechanism that protects transaction ordering in DeFi applies directly to governance vote ordering. This proposal brings that primitive to Gitcoin DAO.

**The Problem**


Current DAO governance has a timing gap.
Snapshot records who voted and how much voting power they had. It does not cryptographically record when the vote was cast in a manipulation-resistant way. This matters in three scenarios:

1. **Flash-loan attacks on quorum timing**
   A whale can acquire tokens moments before a snapshot block, vote, and exit. Snapshot’s n-1 block mechanism helps, but does not prevent strategic timing across blocks.
2. **MEV-style vote ordering**
   In on-chain governance (Governor contracts), a sophisticated actor can observe a pending governance vote and front-run it with a larger stake. The ordering of votes, not just the count, affects which proposals reach quorum first.
3. **MiCA compliance (Q2 2026)**
   The EU’s MiCA framework requires DAOs with over €5M in assets to anchor off-chain votes on-chain by Q2 2026. Gitcoin’s treasury qualifies. PoT’s ERC-1155 anchoring satisfies this requirement automatically.

**What PoT Does**


PoT is a cryptographic primitive that binds a timestamp to a vote before it is cast.
The flow:
1.	Voter submits vote → OpenTTT network synthesizes timestamp from NIST, Cloudflare, Google NTP
2.	Ed25519 signature binds timestamp to (proposalId, voter, support, weight)
3.	PoTVotingStrategy.sol verifies on-chain
4.	ERC-1155 token minted as permanent anchor
5.	The Graph indexes for auditability
The verification happens before the vote is counted. A vote with an invalid or missing PoT proof is counted at 90% weight (soft mode) or rejected (strict mode — configurable by the DAO).

**What we’re offering Gitcoin:**
Free deployment on Base. 1 months.
Gitcoin listed as reference DAO implementation
in all future pitches.

**FAQ**


**Does this change how we vote?**
No. Voters use the same Snapshot interface. The PoT proof is fetched automatically by the SDK. The only visible change is an on-chain anchor token in your wallet after voting.


**What if the PoT oracle is down?**
Soft mode: vote still counts at 90% weight. Strict mode (not recommended initially): vote is rejected. Gitcoin can configure this.

**Status:**
— IETF draft-helmprotocol-tttps-00
— EIP-8201 (active editor review)

—Nature manuscript #2026-03 (under review)

If there’s interest, happy to present to
the core team and deploy on Base Sepolia first.

— Heime Jorgen | heime.jorgen@proton.me

-------------------------
