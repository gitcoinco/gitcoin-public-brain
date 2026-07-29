---
id: 19333
title: "[GCP] Coordinape <> Allo RFP"
slug: gcp-coordinape-allo-rfp
category: open-discussion
url: https://gov.gitcoin.co/t/gcp-coordinape-allo-rfp/19333
created_at: 2024-09-09T18:27:43.359Z
last_posted_at: 2024-09-21T10:43:36.166Z
posts_count: 5
views: 2810
like_count: 15
---

# [GCP] Coordinape <> Allo RFP

<https://gov.gitcoin.co/t/gcp-coordinape-allo-rfp/19333>
Zemm | 2024-09-09 18:29:55 UTC | #1

Greetings!

Spanning this proposal out from some conversations with @owocki , I would like to propose an Allo Strategy research and development RFP, with the goal of crafting a new Allo Strategy template that allows Coordinape GIVE to become an onchain mapping for Allo distributions of tokens.

Coordinape GIVE is written onchain via an EAS schema, and we feel it is possible to use this data to now close the loop of GIVE-based allocation via Allo's onchain distribution mechanism, providing a new, decentralized layer of incentives management for web3 at large.  

## Proposal:

An Allo Strategy could be crafted that uses Coordinape data as a distribution mapping. This is performed by the Strategy interacting with Coordinape’s Ethereum Attestation Service (EAS) schema (The Social Oracle) on Base, an onchain data source which can manage Recipients and Allocation.

### Goal:

Using the GIVE data EAS schema, users of Allo could theoretically manage a strategy that processes transactions based on GIVE outcomes.

* Right now, EAS GIVE comes from Coordinape’s social apps and Farcaster, supporting the attestation of one user to another for any skill or tag.
* With 45,000+ attestations made for hundreds of skill tags, communities and ideas, this data can already suit a wide range of token distribution goals.
* In the future, we will also be able to port Coordinape Gift Circle outcomes to be published on EAS in the same schema, making it possible to allocate to specific DAO memberships and work histories in Gift Circles.
* Tens of millions of GIVE have been sent in Gift Circles since 2021, for tens of thousands of users, making it one of the most rich and well used work evaluation dapps in web3..
* The GIVE EAS schema is additionally outfitted with a placeholder field that will allow for GIVE to be weighted by a global Reputation coefficient, making it a potentially sybil resistant and flexible way to allocate resources to groups users.

### Who Can Build This?

* Gitcoin <> Coordinape will conduct an RFP process to find interested developers for the Allo strategy, with the help of @deltajuliet 
* All developers or teams with an interest in Allo Strategies, EAS, good solidity knowledge, and a track record of building, would be excellent candidates.
* Coordinape can also contribute PM resources to assist developers with scope and design of the project.

### Example Use:

A user wants to allocate a distribution of token funds to developers that are considered well versed or connected to Eigen Layer.

They can create an Allo strategy that finds wallets that are highly recognized by GIVE for their skills in Dev, as well as highly recognized for Eigen Layer tags. This strategy could take advantage of Coordinape’s reputation weighting, and use a date range to introduce more filtering.

Recipients = wallets with 10+ GIVE in Dev & 5+ GIVE in Eigen Layer

Allocation = the percentage of GIVE each member has of the total in the represented category.

### Example Use (future):

A user wants to allocation a distribution of funding to a specific work team using a Coordinape Gift Circle.

They can create an Allo strategy that finds wallets that received GIVE in this Gif Circle, for a specified Epoch, and distributes an allocation based on the percentage of GIVE received.

Recipients = wallets with GIVE tagged with the targeted Organization, Gift Circle and Epoch

Allocation = the percentage of GIVE each member has of the total in the represented category.

### Resources:

[The Social Oracle Co-op](https://coordinape.com/codao/social-oracle)

[Social Oracle EAS Schema (Base)](https://base.easscan.org/schema/view/0x82c2ec8ec89cf1d13022ff0867744f1cecf932faa4fe334aa1bb443edbfee3fa)

[Social Oracle Developer Docs](https://docs.coordinape.com/social-oracle-tm-give)

-------------------------

zippy1979 | 2024-09-11 14:49:19 UTC | #2

I think this is a good initiative. Like the way you guys are thinking. Have used CoordinAPE when I was working with Ocean Protocol, it's rather useful.

-------------------------

SkyDAO | 2024-09-11 21:21:59 UTC | #3

I'm a big fan of Gitcoin and Allo protocol (it's so smooth) and a big fan of Coordinape and GIVE (it's so valuable, useful and fun).

Bringing these two systems closer together seems like it would open doors to some really cool opportunities.  

Making it easier to identify, incentivize and reward the right community members is beneficial for all communities.  

Looking forward to seeing what can be done!

-------------------------

Sov | 2024-09-17 19:15:33 UTC | #4

Thank you for sharing this idea. In reading the proposal I can see some potential synergies with @owocki Allo Points concept: https://gov.gitcoin.co/t/temp-check-allo-points-devcon/19259/1

* Contribution Tracking: Combining Coordinape's GIVE data with Allo-specific metrics could provide a holistic view of platform user contributions.
* Reward Mechanisms: The proposed Allo Strategy could distribute rewards based on Coordinate GIVE and Allo Points.
* Sybil-Resistant Allocations: Using the GIVE EAS schema for allocations could address concerns about ensuring fair and accurate distributions.

I support exploring this idea further, especially if we can bring these two concepts closer together.

-------------------------

deltajuliet | 2024-09-21 10:43:36 UTC | #5

Thanks for much for this @Zemm - Agree w/ @Sov on the synergies between this and the Allo Points temp check. 

What is next on the roadmap? I believe you're looking for interested devs to scope this out further to make this a formal GCP w/ roadmap, milestones and cost estimates? How can we support you on fleshing this out further and validating within the community?

-------------------------
