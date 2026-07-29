---
id: 17167
title: "What should Stewards vote on?"
slug: what-should-stewards-vote-on
category: governancevision
url: https://gov.gitcoin.co/t/what-should-stewards-vote-on/17167
created_at: 2023-11-22T13:14:06.245Z
last_posted_at: 2023-12-05T12:58:36.789Z
posts_count: 4
views: 4497
like_count: 14
---

# What should Stewards vote on?

<https://gov.gitcoin.co/t/what-should-stewards-vote-on/17167>
CoachJonathan | 2023-11-22 16:16:46 UTC | #1

It is currently not very clear (to me) what role GTC token holders (aka Stewards) should play at Gitcoin. In an attempt to make the implicit explicit, the question I cannot seem to find an answer to is: **What should token holders vote on and what shouldn't they vote on?**

## Existing documentation
There are two key pieces of documentation that elude to the answers to this question.

1. [Governance v3 Post](https://gov.gitcoin.co/t/gitcoin-dao-governance-process-v3/10358)

This is the last governance update that was posted to the forum and the basis for much of what is found in the [Governance Manual](https://manual.gitcoin.co/). Here is what the post has to say about the question:

[quote="kyle, post:1, topic:10358"]
### Voting

The Gitcoin community makes decisions by voting on proposals. Anyone who holds GTC is able to cast their vote themselves or delegate their voting power to a steward.

Typically, proposals will fall into one of three categories:

1. Funding proposals : A workstream requests funding from the Gitcoin DAO treasury.
2. Ratification proposals: The community or a workstream asks the community to approve something it wants to do, like issuing matching funds to Gitcoin Grantees at the end of a Grants round.
3. Governance proposals: The community is asked to ratify proposed changes to policy or procedures, like updating the Gitcoin Governance Process document, adopting the Foundation, etc. or the community is asked to vote on structural changes to how the DAO operates.
[/quote]

My takeaways:

* Stewards should have a say in funding requests across the board
* I'm unclear about "Ratification proposals" - what does need to be ratified and what doesn't? Decisions are made at the DAO everyday - what heuristic(s) do we want to use here?
* Governance proposals seems somewhat clear, though I think we can get specific about what policies and procedures need to go to a vote for GTC holders (ex: should our [partnership policy](https://gov.gitcoin.co/t/updated-partnership-processes-partnerships-comms-teams/16481) be ratified by token holders? What about our [Essential Intents](https://gov.gitcoin.co/t/discussion-community-feedback-on-gitcoin-s-essential-intents-for-2023-2024/16657)? What about the [DAO Cadence](https://gov.gitcoin.co/t/gitcoin-cadence-calendar/16643) - does any change to this need to be ratified through a vote, only specific ones, or maybe none at all?

2. [Introducing Steward Governance Post](https://gov.gitcoin.co/t/introducing-stewards-governance/41)

Similar to the post above, there are lots of ideas here though it is not a definitive list of "this is what Stewards *should and should not* vote on, in fact there is no mention of "voting" in the post, only what Stewards should get involved with.

## Looking at other orgs

Based on high-level preliminary research (and conversations with ChatGPT), many orgs use governance to help make decisions around governing their protocols. I found it quite difficult to find a definitive list of activities that token holders might vote on at other DAOs.

The Token House at Optimism does a good job of [making it clear what proposals token holders can expect to vote on](https://gov.gitcoin.co/t/introducing-stewards-governance/41) and the criteria around those proposals.

## Next Steps

In an attempt to make Gitcoin's governance more inclusive, I think it is important to create clear agreements around the roles and responsibilities of all parties involved in decisions at the DAO.

What I would love is for a discussion around what things token holders *should* be voting on (and we can safely assume that anything not mentioned are things they would not be voted on).

After some suggestions, I plan to make another proposal to ratify the [roles & responsibilities of Stewards at Gitcoin](https://manual.gitcoin.co/governance-roles/stewards) and the [proposals/voting processes](https://manual.gitcoin.co/governance-processes/governance-overview) in Gitcoin's governance.

-------------------------

jengajojo | 2023-11-24 08:07:18 UTC | #2

[quote="CoachJonathan, post:1, topic:17167"]
It is currently not very clear (to me) what role GTC token holders (aka Stewards) should play at Gitcoin.
[/quote]
I agree with you on this. As you have already identified, moving tokens from the DAO treasury (aka funding proposals) should have the token holders stepping in. But there is ambiguity for the other types of proposals partly because the needed clarity is lost in endless proposals which someone has to comb through in order to identify the current state of the DAO. 

This is exactly why I suggested in an earlier post to have a **shared source of truth** for the DAO (called **'constitution'** in some circles).  The main benefits are:

-  **Clarity and Transparency:** explicit guidelines on how decisions are made, what proposals are subject to voting, and the criteria for various types of proposals (funding, ratification, governance).

- **Decision-Making Heuristics:** defining the scope of decision-making for each group (CSDO/WGs/token-holders etc..) and the surface area for governance which can be as simple as token movements and updating the constitution

- **External Communication:** serves as a clear reference point for external parties interacting with the DAO, helping them understand the decision-making structure and principles and enhances the credibility of the DAO by showcasing a well-defined and organized governance structure.

-------------------------

CoachJonathan | 2023-11-24 14:05:34 UTC | #3

Great idea, @jengajojo. Do you have any examples of constitutions that describe this?

Looking at [Optimism's constitution](https://gov.optimism.io/t/working-constitution-of-the-optimism-collective/55), I'm only seeing this:

> * OP Holders may:
>   * Remove a director of the Optimism Foundation; and
>   * Veto changes to the founding documents of the Optimism Foundation, if those changes would reduce the rights of OP Holders in a material way.

The rest of the "types of proposals voted on" are all in the Operating Manual that I linked to in my post.

I also see that some DAOs do have constitutions like [Bankless](https://github.com/BanklessDAO/bankless-dao-constitution/blob/main/bdao-constitution.md) and [SafeDAO](https://forum.safe.global/t/sep-4-safedao-constitution/1749) and there are other DAOs with advanced governance models that don't have a constitution like [Uniswap](https://gov.uniswap.org/). And then there are orgs like ENS DAO and MakerDAO that have consistitutions that, tbh, I can't quite decipher whether or not they explicitly outline token holder responsibilities.

Suggestions and examples welcome. I'm game to have this embedded within a Gitcoin Governance Constitution. Just curious about what best practices are as to what to include/not to include in this document, and if any information is better listed within something like our [Governance Manual](https://manual.gitcoin.co) under "Steward Decision Rights" vs. a constitution.

-------------------------

CoachJonathan | 2023-12-05 12:59:50 UTC | #4

Reviving this thread, I want to drill down on a way forward.

### DAO Constitution
- I'd be game to draft this but I'm still not clear on how this is different than the Governance Manual
- If we do move forward with this, what are some high level ideas we'd want to include? How robust do we want this constitution to be? Like the [MakerDAO constitution](https://forum.makerdao.com/t/mip101-the-maker-constitution/19621) (which seems incredibly thorough and very difficult to understand imo), or something super simple like [Optimism](https://gov.optimism.io/t/working-constitution-of-the-optimism-collective/55) (that is more about outlining some fundamental agreements but doesn't necessarily have a ton of substance imo)

### What Token Holders Should Vote On

I think that there are only a few, very important matters that we currently should have Stewards voting on (this may change in the future).

**1. Gitcoin Treasury allocation**
- Stewards are the final safeguard for the DAO's treasury
- Any proposals and requests that would release funds from the treasury should require token holder approval
- This includes budget requests and GCPs

**2. Governance changes**
- Any change to our governance structure should be under review
- This should include changes to the Governance Manual
- If we create a constitution, this would be included as well

**3. Election of the Executive Director of the Foundation**
- This is how Stewards can hold the DAO accountable for decision makings
- Early 2024 we'll see some posts about an election for the role of ED of the Foundation
- Similar to how coops work - members elect the board, the board decides on the ED and holds them accountable, ED hires, manages and holds everyone in the org accountable
- The Foundation currently does have a board (different from the Steward Council) and I'm not personally clear on how members of the board are selected

-------------------------
