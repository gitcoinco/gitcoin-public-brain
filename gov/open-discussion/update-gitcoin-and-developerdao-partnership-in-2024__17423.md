---
id: 17423
title: "[UPDATE] Gitcoin and DeveloperDAO Partnership in 2024"
slug: update-gitcoin-and-developerdao-partnership-in-2024
category: open-discussion
url: https://gov.gitcoin.co/t/update-gitcoin-and-developerdao-partnership-in-2024/17423
created_at: 2024-01-16T18:27:30.229Z
last_posted_at: 2024-02-08T00:54:07.648Z
posts_count: 5
views: 3960
like_count: 27
---

# [UPDATE] Gitcoin and DeveloperDAO Partnership in 2024

<https://gov.gitcoin.co/t/update-gitcoin-and-developerdao-partnership-in-2024/17423>
deltajuliet | 2024-01-16 18:27:30 UTC | #1

As we move further into 2024, we're excited to provide an update on our [Partnership & Mutual Grant with Developer DAO](https://gov.gitcoin.co/t/proposal-partnership-mutual-grant-with-developer-dao/9217). This collaboration is an important step in uniting our communities and leveraging our combined strengths to support the growth of the web3 space.

Our partnership is rooted in a shared vision: facilitating the transition of web2 developers into the burgeoning world of web3. By combining Gitcoin's robust grant capabilities with Developer DAO's vibrant community of builders, we're creating a synergy that will accelerate growth and innovation in the web3 ecosystem.

## CODE Token Allocation and Governance

DeveloperDAO has allocated 500k CODE tokens to Gitcoin in line with our original agreement. These tokens are currently held in the Safe address (eth:0x426b5f29828A66aA014ED92E755fed3fd78f2D16), allowing Gitcoin to actively participate in DeveloperDAO's governance votes.

The Safe has two signers from DeveloperDAO (@kempsterrrr , @mannyornothing ) and three from Gitcoin (@CoachJonathan , @kyle , @deltajuliet ). CoachJ and Kyle will represent Gitcoin DAO as delegated members in DeveloperDAO Governance.

## Governance Considerations

While navigating this partnership, we've discussed methods to balance the impact on Developer DAO’s Governance. See overview of allocation vs voting history in below. 

|Item|Notes|
| --- | --- |
|Average Total Votes on Snapshot|Average total tokens voting on snapshot is 277,312.58 - 500k is almost double participating tokens|
|Largest Total Votes on Snapshot|Largest total tokens voting on snapshot is 401,855.10 - 500k would have swung this vote|
|Gitcoin allocation vs top 100|Gitcoin's allocation is as much as the next 8 allocations combined|
|Gitcoin allocation vs top 100 (excluding founding team and advisors)|Gitcoin's allocation is as much as the top 19 holders outside of founding team and advisors|
|Gitcoin share of circulating supply not including treasury|Gitcoin's allocation is equivalent to 14.78% of circulating supply excluding CODE in treasury|

## Governance Impact:

We are acutely aware of the potential impact of this allocation on DeveloperDAO’s governance. To address this, we have taken a thoughtful approach:
* The 500k CODE tokens have been split between two SAFEs. The 'Voting Safe' (0x426b…2D16) holds 5% of the circulating supply of CODE, with the excess moved to a 'Non-voting Safe'.
* Each quarter, the difference between the balance of the Voting Safe and 5% of the circulating supply will be transferred from the Non-voting Safe into the Voting Safe.


## Cross-Community Engagement

We are planning various cross-community activities, including Twitter Spaces, joint AMAs, and cross-forum engagements. These initiatives aim to foster interaction, knowledge exchange, and stronger ties between Gitcoin and DeveloperDAO members.

We invite members from both communities to propose project ideas that could benefit from our partnership. These proposals can range from leveraging Gitcoin’s grant system for DeveloperDAO-driven projects to collaborative efforts in tackling complex challenges in the web3 space.

We encourage participation in each other's governance discussions, project brainstorming sessions, and community events. This involvement will deepen our understanding of each other's strengths and foster effective collaboration.

-------------------------

jengajojo | 2024-01-17 09:53:57 UTC | #2

I am happy to see this collaboration going forward and excited to for the future of such partnerships for both entities. 
As I understand both entities will make separate grant requests for action items related to executing specific deliverables in this partnership. Hence, if the scope of exchanging tokens is limited to governance participation, delegating tokens via a [Franchiser](https://github.com/NoahZinsmeister/franchiser/blob/main/spec.md) contract (as was done recently in Uniswap DAO) would be an optimal solution for future use cases to minimize impact on the treasury for low liquidity tokens

-------------------------

kyle | 2024-01-17 13:53:41 UTC | #3

Thanks @deltajuliet for the udapte and details. I am also excited to see this come to fruition. It's been in the works for a while.

@jengajojo - the Franchise contracts are really pretty neat. It would be interesting to explore setting this up with a small test amount of GTC to confirm it works properly. Do you have experience deploying the contracts an configuring them?

-------------------------

jengajojo | 2024-01-18 08:08:21 UTC | #4

thanks @kyle The test would be helpful indeed. I personally don't have experience with deploying these, but https://twitter.com/eek637 from uniswap foundation has done this for their recent proposal

-------------------------

kempsterrrr | 2024-02-08 00:54:26 UTC | #5

Thanks @deltajuliet and @CoachJonathan @kyle for working with us to execute on this. Very happy to see it come together. (had this response in draft from the day this was posted 🙃 ).

Wanted to give a few quick updates on progress from our side:

**Governance Participation**
We've now delegated the GTC in our treasury to `devdao.eth` so we can vote in Gitcoin's governance for the first time. I'll be managing this delegation on behalf of DD and will endeavour to engage in discussion where I believe we can add value and share our voting intention and reasoning for every vote we participate in.

Our first vote was cast in favour of [[Proposal] Gitcoin’s Citizen Grants program](https://gov.gitcoin.co/t/proposal-gitcoin-s-citizen-grants-program/17470) and our reasoning is shared [here](https://gov.gitcoin.co/t/proposal-gitcoin-s-citizen-grants-program/17470/18?u=kempsterrrr). This is a new role for myself and DD, so we'd love to hear any feedback on how you would like too see us participate in Gitcoin's Governance.

Here to help @kyle and @CoachJonathan participate in ours 🤝

**Cross-community Engagement**
With the focus on Denver at the moment for us both, we're moving slowly on cross-community activities. Some initial low lift steps we're taking on our side:

1. Socialising opportunities for builders that come up from within Gitcoin and general updates we feel our community would find interesting via our newsletter
2. Re-posting relevant gitcoin openings onto DD job board - See [Principal Engineer](https://developer-dao.joineden.ai/jobs/65c22510e28e9e00073005be) and [DevRel](https://developer-dao.joineden.ai/jobs/65c2273ae28e9e0007300744) postings. The board is in beta and built by Eden, a project from DD that received funding in GR15 - awesome to see it come back full circle and contribute back to Gitcoin. Any and well feedback very welcome on this, iterating quickly.

-------------------------
