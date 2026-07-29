---
id: 25055
title: "[Passed]: Disengagement of Avantgarde from Matching Pool Asset Management & Strategy Reset"
slug: passed-disengagement-of-avantgarde-from-matching-pool-asset-management-strategy-reset
category: governance-proposals
url: https://gov.gitcoin.co/t/passed-disengagement-of-avantgarde-from-matching-pool-asset-management-strategy-reset/25055
created_at: 2026-01-13T16:29:37.920Z
last_posted_at: 2026-02-11T19:14:19.551Z
posts_count: 8
views: 214
like_count: 8
---

# [Passed]: Disengagement of Avantgarde from Matching Pool Asset Management & Strategy Reset

<https://gov.gitcoin.co/t/passed-disengagement-of-avantgarde-from-matching-pool-asset-management-strategy-reset/25055>
owocki | 2026-02-11 19:13:39 UTC | #1

**Summary**

This proposal recommends formally ending Avantgarde Finance’s role as asset manager for the Gitcoin Matching Pool and transitioning away from the externally managed strategy approved under the prior [Matching Pool asset management proposal](https://gov.gitcoin.co/t/passed-sgtm-002-avantgarde-x-gitcoin-strategic-asset-management-for-the-matching-pool/19698).

While the original proposal was well-intentioned and appropriate for its time, the DAO’s strategy, tooling, and governance priorities have evolved. The Matching Pool will now be managed through DAO-controlled, non-intermediated approaches, with any yield generation explicitly supporting future grant matching.

### **Context**

The original Matching Pool proposal approved Avantgarde to:

* Introduce a structured asset allocation framework for the Matching Pool

* Actively manage ETH and stablecoin positions

* Generate yield to grow the Matching Pool over time

* Provide professionalized reporting and operational execution

At the time, this approach aimed to:

* Reduce idle capital

* Improve capital efficiency

* Extend the long-term sustainability of Gitcoin grants

The DAO recognizes that these goals were reasonable and the managed engagement was a success, given the Matching Pool’s size and the ecosystem context at the time of approval.

### **Why the Strategy Shift**

The Matching Pool exists to:

* Fund grants

* Maintain donor and community trust

* Be maximally legible to tokenholders and contributors

#### **1. Intermediated Management Adds Governance and Continuity Risk**

The Avantgarde model requires:

* Ongoing delegation of execution authority

* Reliance on specific personnel and reporting practices

* Governance abstraction that makes it difficult for non-specialists to understand current state

This has proven misaligned with the DAO’s preference for:

* Simpler control surfaces

* Clear, on-chain legibility

* Reduced dependency on third-party operators

#### **2. Reporting and Transparency Are Insufficient for Tokenholders**

Despite being “on-chain auditable,” the current reporting experience has proven inadequate in practice:

* It is laborious for DAO participants to determine current positions and exposures

* Treasury state is not easily legible to tokenholders without specialist tooling

* Governance participants cannot quickly answer basic questions like “where is the money right now?”

#### **3. Loss of Operational Continuity**

The original point of contact and relationship owner on the Avantgarde side has moved on. Given the complexity and sensitivity of treasury management, this materially weakens continuity and increases coordination risk.

Rather than re-establishing context under a changed team structure, the DAO prefers to reset its approach.

#### **4. Yield Can Be Generated Without Delegated Asset Managers**

The ecosystem has matured to the point where:

* Conservative yield strategies can be executed directly by DAO-controlled infrastructure

* Capital can remain non-custodial and fully under governance control

* Reporting can be simplified to “what is deployed, where, and how it affects matching”

As a result, the marginal benefit of an external asset manager no longer justifies the added complexity for the Matching Pool.

#### **5. Strategic Reset for 2026-Era Grants Infrastructure**

Gitcoin is intentionally resetting how it thinks about funding infrastructure:

* Fewer intermediaries

* Tighter coupling between capital deployment and matching outcomes

This includes retaining the ability to experiment with newer funding primitives and vault-based systems (e.g., limited experiments with Octant), without outsourcing overall Matching Pool management.

### **Proposal Actions**

1. **Formally disengage Avantgarde Finance** from managing Matching Pool assets

2. **Unwind the existing Matching Pool management setup** and return assets to DAO-controlled wallets or governance-approved contracts

3. **Sunset the original Matching Pool asset management mandate**, acknowledging it has been superseded by a new strategic direction

4. **Adopt a DAO-native Matching Pool strategy**, where:

   * Capital remains under direct governance control

   * Yield generation is optional, simple, and transparent

   * All yield is explicitly earmarked for future matching rounds

5. **Permit bounded experimentation** with protocol-native yield mechanisms where appropriate, without appointing a delegated asset manager

We want to thank Avantgarde Finance for their engagement. Ending the mandate for the Matching Pool is a strategic evolution toward simpler, more legible, and more mission-aligned infrastructure better suited to Gitcoin’s next phase of grants and public-goods funding.

### **Decision**

Yes - remove Avantgarde Finance as asset managers for the Matching Pool and return all funds to the DAO

No - keep Avantgarde Finance as asset managers for the Matching Pool

Abstain - choose not to vote on the proposal

-------------------------

ccerv1 | 2026-01-13 17:15:19 UTC | #2

I’m supportive; see also my comments on [this](https://gov.gitcoin.co/t/proposal-disengagement-of-avantgarde-as-treasury-asset-manager/25054/2?u=ccerv1) related proposal.

-------------------------

LuukDAO | 2026-01-14 00:03:58 UTC | #3

In favor, as I believe the DAO has the capacity to manage this properly.

Let’s make sure that the basic tasks, such as holding dashboards and regular finance reporting, are executed by Gitcoin contributors + ensure we have some expert oversight when making treasury allocations and yield decisions.

-------------------------

MathildaDV | 2026-01-16 18:14:27 UTC | #4

I appreciate the work that we’ve done with Avantgarde up to this point. I agree that we can restructure the MP assets in a way that is more favourable to our own strategies. I’m excited about the proposal to experiment with Octant yield in 2026! 

I’m in favour of this proposal.

-------------------------

kyle | 2026-01-19 16:09:05 UTC | #5

I’m also supportive. I wonder if we have alternatives identified yet (for yield generation), or if that will come later?

-------------------------

deltajuliet | 2026-01-21 13:33:25 UTC | #6

I’ve already commented on the Treasury post ([voting no, as it stands](https://gov.gitcoin.co/t/proposal-disengagement-of-avantgarde-as-treasury-asset-manager/25054/6)) and the same sentiment applies here. AG is managing $11 million of our funds, and we are dedicating (currently) $1M of that to the Octant pilot. 

The Matching Pool is pretty sacred, and I’m totally fine to disengage w/ AG if the last 2 FT DAO contributors prefer another relationship, however much like the Treasury, without a plan with what do do with these funds, I will be voting no.

-------------------------

owocki | 2026-01-21 22:15:26 UTC | #7

[quote="deltajuliet, post:6, topic:25055"]
without a plan with what do do with these funds, I will be voting no.

[/quote]

there is a plan - put the funds back in the timelock where everyone can see them and track them onchain without going through a labyrinth of trusted intermediaries.

-------------------------

MathildaDV | 2026-02-11 19:14:19 UTC | #8

This proposal has passed: https://snapshot.org/#/s:gitcoindao.eth/proposal/0x1c2875456a8696d35c8bf0ec1477500efcaa6f710e3ee1207832899d99941b0b

-------------------------
