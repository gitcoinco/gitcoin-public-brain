---
id: 15460
title: "[Proposal] DeSci “recognized subDAO” framework development and implementation"
slug: proposal-desci-recognized-subdao-framework-development-and-implementation
category: open-discussion
url: https://gov.gitcoin.co/t/proposal-desci-recognized-subdao-framework-development-and-implementation/15460
created_at: 2023-06-19T17:23:54.620Z
last_posted_at: 2023-06-28T14:32:23.301Z
posts_count: 13
views: 3246
like_count: 17
---

# [Proposal] DeSci “recognized subDAO” framework development and implementation

<https://gov.gitcoin.co/t/proposal-desci-recognized-subdao-framework-development-and-implementation/15460>
borisdyakov | 2023-06-19 18:23:20 UTC | #1

# [Proposal] DeSci “recognized subDAO” framework development and implementation


**_Author:_**
[Boris Dyakov](https://twitter.com/BJ_Dyakov)
*PhD Candidate, The University of Toronto
S17 Trusted Contributor, PGF*

Estimated reading time: 10 minutes

## Summary (TL;DR)

This GCP is intended for me to continue my work as a trusted contributor to PGF in S17 where I established DeSci as the first [community-operated featured round](https://explorer.gitcoin.co/#/round/1/0x6e8dc2e623204d61b0e59e668702654ae336c9f7) within the new Gitcoin Grants Program.

It will cover: 

1. A summary of work achieved towards this in S17
2. How extending this to a more general “recognized affinity group (or _‘subDAO’_)” model for grant round operations and funding can enable Gitcoin to scale its impact without increasing costs
3. The work needed to ensure there is ongoing support for DeSci within the Gitcoin grants program, and what would be needed to establish DeSci as the first of several potential subDAOs within Gitcoin

Special thanks to @connor for extensive feedback and to @M0nkeyFl0wer, @ceresstation, @kyle, @CoachJonathan, @azeem, @Maxwell, @juanna, and @J9leger for review and general discussion. This is now being submitted for wider community feedback and consideration as a GCP.

## Background and S17 work

### Gitcoin Grants Program 2.0 and existing challenges

The recent Beta Round was the first iteration of a new model for the Gitcoin Grants Program, where a [community-chosen](https://gov.gitcoin.co/t/shaping-the-new-gitcoin-grants-program-with-community-engagement/12811/15) set of _core rounds_ were fundraised for and operated by PGF alongside a set of _featured rounds_ which were funded and operated by external parties.

There are three major functional dimensions to running grant rounds: 

* Operations (defining eligibility criteria and round parameters, screening applications, communication with grantees, support, fraud detection, matching calculations, processing payouts)
* Marketing (promoting rounds to prospective grantees and donors, ensuring that the community is active and engaged)
* Partnerships (raising funds for the matching pool)

PGF continues to manage core rounds, and in S17 established the [Grant Round Operators Guild (GR-OG)](https://gitcoin.notion.site/Grant-Round-Operators-Guild-Portal-2183a58be88347c6b65643070f9b0c13) to support featured round operators, and eventually self-serve operators in general. The GR-OG is a crucial step towards decentralizing operations/support for the Allo Protocol, and the MMM workstream is a crucial partner for bringing awareness to quarterly rounds. 

The question of how to efficiently raise matching funds on a quarterly basis remains to be answered.

Core round matching funds are raised on a quarterly basis by the PGF partnerships team. Matching funds for featured rounds are provided by the sponsoring organization or company who want to run a grant round to support their specific ecosystem. **A community-run featured round (_e.g._ DeSci) is however more similar to a core round in terms of how it should be funded, but _without_ the organizational infrastructure that the PGF partnerships team provides.**

### Decentralized Science as a community-run featured round

[DeSci](https://ethereum.org/en/desci/) is an emerging narrative within web3 that covers a broad range of topics, each with the potential to develop distinct verticals with large addressable markets (*e.g.* funding, publications/attributions, data, social). DeSci also creates an opportunity for onboarding a new set of users (scientists) into the space, and overall offers new ways of using blockchain technology to solve real-world problems that exist within society.

During the recent Beta Rounds, DeSci was the only_ featured_ round which was operated by a decentralized community instead of a specific sponsoring entity (via democratic election of four round managers/”stewards”, plus myself). Establishing this bottom-up community governance framework was intended to create a culture that could run recurring grant rounds without relying on a single individual (or group) to handle operations on a quarterly basis – and has so far been a successful experiment.

Building on the growing DeSci movement and the success of the [inaugural DeSci round in GR15](https://www.gitcoin.co/blog/gr15-results#cause), I launched a new telegram group and invited past grantees, donors, and community members to join and get involved in running the upcoming round. To elect round stewards to represent the community as managers for this round, I set up a lightweight governance structure to carry out an on-chain vote (full details in this [twitter thread](https://twitter.com/BJ_Dyakov/status/1647966892001460224?s=20)).

Despite the high gas fees and some UX hiccups, the 65 DeSci round grantees crowdfunded a total [$18,675 from 267 donors](https://gitcoin-grants.streamlit.app/), making us the 2nd most funded featured round after web3 social.

### S17 work towards DeSci as an “affinity group” or “recognized subDAO” within the Gitcoin Grants Program

This “DeSci x Gitcoin Community” proto-DAO now has the structure for this community to fund its shared needs in an open way, but the problem that remains to be solved is one that applies broadly to Gitcoin: **_“how do we sustainably fund these rounds, so we can continue to make an impact and support emerging ecosystems?”_**

The initial $50k “minimum viable round” matching pool came from Gnosis Chain’s contribution to DeSci GR15 (earmarked for the next DeSci round, which ended up being during the recent Beta Round). The matching pool grew by an additional $35k thanks to support from MoonDAO and Greenpill China, but it’s unclear where funds for subsequent rounds will come. This proposal describes work for the next two seasons which aims to solve these problems in a scalable and repeatable way through the creation of new social norms, incentives, and infrastructure within the DeSci and Gitcoin communities through a **_“recognized subDAO'' framework._**

In S17, I laid the groundwork for the DeSci community to develop into a recognized subDAO within Gitcoin. As a recognized subDAO, the DeSci x Gitcoin community would be capable of independently running future grant rounds as part of the Gitcoin Grants Program with minimal use of PGF workstream resources. 

To custody our treasury and matching funds, we created a [5/7 multisig](https://etherscan.io/address/0x1385754798d1f2c3a5eaa45c32999e57317d6bfd) controlled by myself, the four community-elected stewards, and two PGF workstream leads as trusted backup signers (Ben West and Connor O’Day). This was funded by the community [as its own project within the round](https://explorer.gitcoin.co/#/round/1/0x6e8dc2e623204d61b0e59e668702654ae336c9f7/0x6e8dc2e623204d61b0e59e668702654ae336c9f7-75), showing that we can cover operational costs (_i.e._ gas for round operations) – but also creates the potential to reward stewards for their work, thus creating new incentives that will sustain this subDAO round-over-round.

## Motivation, benefits, and strategic fit

The Gitcoin Grants Program is the heart of Gitcoin. Though the DAO is transitioning from being a successful impact DAO to being a protocol DAO, dogfooding the Grants Stack and Allo Protocol is still essential, and Gitcoin will continue to run its Grants Program for the foreseeable future.

Gitcoin is already scaling the Grants Program in two ways:

1. Launching a self-serve offering for anyone to run a grant round on their own terms (the protocol is already permissionless and open for anyone to use)
2. Offering organizations the chance to run a featured round during the quarterly Grants Program via a minimum matching fund and a % service fee for operations and marketing support (great value given the substantial network effects that Gitcoin’s community enables)

<span style="text-decoration:underline;">This proposal aims to develop a third approach</span>: a framework for decentralized communities (*e.g.* the Decentralized Science community) to establish and operate a “recognized subDAO'' with the explicit objective of running grant rounds **_within_** the Gitcoin Grants Program. This continues the growth of the Gitcoin ecosystem without investing significant resources into additional PGF contributors, and without the direct support from a clear sponsor.

Round/topic-specific **recognized subDAOs** within Gitcoin could help the DAO grow and maintain a diverse and high-quality grants program without increasing costs or relying on key individuals within PGF, while being flexible enough to expand into emerging themes and narratives. These subDAOs could also take on support and marketing responsibilities (as the DeSci community already did in the Beta Rounds), and contribute to product development driven by the needs of their community.

A set of topic-specific recognized subDAOs would benefit Gitcoin by:

* [Decentralizing Gitcoin’s Grants Program](https://gov.gitcoin.co/t/decentralizing-the-gitcoin-grants-program/12669), growing the GR-OG, and generally creating more users for grants stack/allo protocol/passport – without added governance overhead costs for Gitcoin itself.
* Creating new opportunities for grantees, donors, and community members to directly and indirectly participate in Gitcoin governance. As members of a recognized subDAO that is directly working to support their interests, they will have a stake in Gitcoin’s success and broader DAO governance decisions.
* Creating a population of subDAO members who are incentivized to utilize GTC to participate in broader Gitcoin DAO governance (especially if these governance decisions have an impact on the subDAO they are passionate about)
* Acting as a more personalized on-ramp for grantees who will become supporters and community members of Gitcoin
* Engaging new donors who want to support a specific emerging theme/topic, who then get exposed to the broader community and concurrent rounds
* Enabling experimentation around the grants program at a smaller scale (*e.g.* different QF models)

Gitcoin is an important partner for emerging community subDAOs because:

* Gitcoin’s brand reputation and credibility is important for raising matching funds
* Marketing support and network effects during grant rounds ensure visibility and donations to projects
* TBD, but: subDAOs would benefit from support in establishing some governance infrastructure. One idea is a mechanism for time-locked/vesting GTC as rewards for elected round stewards (voted on by that specific subDAO, and from funds raised by the subDAO – several possibilities exist and are being explored).
* In the context of this proposal: support for me to directly 1) continue developing this model with DeSci as the first example in S18/19, 2) ensuring the funding and operational needs are met so the next DeSci round can happen, and 3) help at least one other community adopt this affinity group/recognized subDAO model
* Future featured rounds are expected to incur a service fee for operational support provided by PGF – a necessary step for the DAO to achieve revenue. This service structure makes a lot of sense when the client is a company/protocol that receives major benefits from running a round alongside Gitcoin. In the case of a decentralized community, this only compounds the challenges in funding a round and incentivizing community members to take on the task of managing a round. **_I propose that this service fee be initially waived for community-run or “recognized subDAO” rounds – but expect this arrangement be discussed on a rolling basis as a hypothetical subDAO achieves its own sustainable funding._**

## Scope of work and objectives

**I would like to be clear that the primary focus of this work is to ensure that we have sustainable, ongoing support for DeSci grant rounds.** Thinking about how to achieve this has led to the realization that we must develop community infrastructure (socialware, and eventually [trustware](https://gov.gitcoin.co/t/knowledge-transfer-the-gitcoin-hyperstructure/11335)) lest we rely on specific individuals to make these rounds happen each quarter. The aim of this work is for the DeSci community and round to not require ongoing financial support from Gitcoin / PGF (*i.e.* by paying contributors to operate the round), but rather to operate as a partner to Gitcoin to ensure mutual success of the grants program and Allo Protocol / Grants Stack.
 
I believe this approach that I am proposing and implementing for the DeSci community could be useful and adopted more widely, and may have further-reaching benefits for Gitcoin. I recognize this is an experiment but I am committed to documenting and working with the broader community to develop and execute on this.

Funding for S18/19 will allow me to complete the following: 

* Completing documentation and retrospective review of DeSci Beta Round
    * Blog post(s) for Gitcoin describing this process and outlining the “recognized subDAO model” (after additional discussions and community feedback on a separate forum post). I would work with MMM to further explain this in a twitter thread and a community call.
* Defining and executing on phase 2 of the “DeSci recognized subDAO” experiment:
    * Continue to establish our governance structure and process alongside the community
        * Expand membership to include all DeSci Beta Round (and GR15) grantees and donors, as well as vetted community members
    * Design and execute on experimental incentive models for subDAO round managers and “partnerships team” to ensure sustainable round-to-round funding and operations
        * Potential _retroactive_ incentive model for round stewards (elected operators/manager): xx% of matching pool is awarded to round stewards as time-locked GTC (decided by the subDAO via QV or directly by QF on a “[grant round ops fund](https://explorer.gitcoin.co/#/round/1/0x6e8dc2e623204d61b0e59e668702654ae336c9f7/0x6e8dc2e623204d61b0e59e668702654ae336c9f7-75)” project in future rounds)
        * Potential _prospective_ incentive model for “subDAO partnerships”: Community-decided “commission” on closing matching fund contributions.
    * Personally ensuring we secure a minimum of 50k in funding for the next 6 DeSci rounds (opting-out of the potential commission model described above while having my work funded by Gitcoin, until the 300k funding threshold is met)
    * Define and ratify how a “recognized subDAO” can be formally recognized by Gitcoin
        * What benefits does the subDAO receive?
        * What commitments does the subDAO make to Gitcoin?
        * How is this governed?
* Begin planning and operations for the next DeSci round – ideally acting as an advisor to a newly-elected set of round stewards and “DeSci subDAO” operator.
* Help apply this “recognized subDAO model” to a different community within the next two rounds:
    * Some possibilities to explore include Climate Solutions, ReFi, DEI, Greater China, Arts and Culture
    * Any community that already has an active online space where community members could feasibly coordinate around operations for a grants round would be a good candidate
* Continuing various partnerships-related conversations for the benefit of Gitcoin more generally (philand.xyz, Scroll zkEVM, Little Atlas, and more..)

The work described in this proposal will require continued close coordination between myself, the PGF workstream, and the broader DAO. This would also require me to attend weekly PGF and DAO-wide meetings, functionally operating as a trusted part-time contributor to PGF (as per my S17 status). This is accounted for in the budget and hourly allocation described below. 

Though related to the work being undertaken by PGF, this is being submitted as a separate proposal as it falls outside of the workstream’s immediate strategic focus for S18/S19 and represents a new vision for how the Gitcoin DAO may be structured.

Note that this proposal and funding request is partially retroactive as it pertains to work I’ve been doing in May and June 2023 while not on the workstream payroll.

## Risk Assessment

A subDAO model could introduce new forms of competition within the Gitcoin ecosystem, where different subDAOs end up competing for the same sources of funding (whether externally or from a shared pool generated by PGF’s efforts). This creates the risk of emergent unforeseen negative consequences, but also creates new potential opportunities. Experimenting with and testing this model should thus be done in close collaboration with PGF and the Gitcoin DAO.

## Budget

I am requesting total funding in GTC equivalent to to $34,000 USD ($32,400 USD salary based on an 18 hour per week commitment for S18 and S19, plus a $1600 travel budget) 

The travel budget is to present this work at an upcoming conference. I have already been invited to speak at several conferences about my DeSci-related work with Gitcoin (DeSci Boston, DAO Montenegro (EDCON), BlockSplit (Split, Croatia), ETH Barcelona, and DeSci Paris) but will target the DeSci Berlin x Funding The Commons conference this September.

As a corollary to this being approved, my status as a trusted contributor to PGF would need to be kept such that I maintain access to notion and google workspace (boris@gitcoin.co)
 
 _Reference calculation:_ 
_(72 hours/month) * (6 months [S18+S19]) = 432 hours (note: partially retroactive as we are ~1.5 months into S18)_
_432 hours * $75 USD/hour = $32,400 USD + $1600 USD = $34,000 USD (approximately 35175 GTC based on token price as of 19 June 2023)_
_($75 USD/hour based on comparable GCP budget requests)_

## Timeline

The proposed work would take place during S18 and S19. 

Future proposals requesting subDAO-specific support from Gitcoin will be submitted by those subDAOs if/when they are needed and can be clearly defined.

## Vote

1. **Yes**: fund this proposal with the requested amount (GTC equivalent to $34,000 USD)
2. **No**: Do not fund this proposal
3. **Abstain**: I am missing context or this proposal needs more refinement

-------------------------

Viriya | 2023-06-20 19:23:17 UTC | #2

Thanks for putting this together @borisdyakov. I really like the direction you're taking this and I think the long-term benefits will be really impactful. Generally I'm very bullish on this direction and would like to see a strategy emerge on how we might empower grassroots communities to benefit from our tech and pooled funds (as you're proposing here). 

For me to officially vote 'yes' to this, I'd like to get a sense of how the program's strategy is evolving (given current conversations around DAO resourcing and future states of the program). Once a clearer picture emerges from those conversations, I will personally have a better idea of how the piece you've proposed fits into the overall puzzle.

-------------------------

jengajojo | 2023-06-30 07:46:37 UTC | #3

I personally really like the DeSci movement and would like to thank @borisdyakov and crew for stewarding the featured DeSci round so far :fire: The recognized subDAO framework seems like the right step towards structuring coordination for featured round and I am happy to help you develop the same if you need help :slight_smile: 

Could you please help us understand:

- How much GTC/USD has been spent on operational expenses so far (salaries, gas, etc)?
-  How many leads have been contacted for potential matching funds so far? and what is the general response?
-  Can you offer some insights on the teams' history of fund raising?

General question to the community:

- Given the fact that any community can independently run their own QF matching rounds on Grants Stack, does it still make sense to invest resources in featured rounds?

-------------------------

Jag | 2023-06-21 15:20:11 UTC | #4

Is Gitcoin a DAO or an Ecosystem? If DAO, then we'd have a DeSci subDAO; if Ecosystem, then a DeSci DAO would emerge. To the Nucleolus, the Nucleus is the Cell; and to the Nucleus, the Cell is where the boundary lies. But it's all contiguous at the of the day. 

Frameshift scalings of perspectives aside, I think the work you're doing is extremely valuable. **The Opportunity Cost of not doing this is very high**, particularly at this time, because Decentralized Science is poised to create tremendous value as it grows to draw in bright minds and intellectual capital to the web3 space. Additionally, there are moral and ethical reasons that DeSci should find a home in the Gitcoin Ecosystem because Science is a Public Good. Regarding the Risk Assessment - Conflict breeds Creativity, so this can be healthy.

At the risk of unintentionally shilling my work, I'd like to mention how insights from DeSci have illuminated the importance of Supply Elastic Digital Assets in Decentralized Finance. This work was done independently in another community, and the Neuroscience of Ethereum offered a complementary perspective on the behavior of these instruments - which resemble the Economy of Neurotransmitters. Elastic DeFi engineering principles can benefit Gitcoin as I have [presented here in this post](https://gov.gitcoin.co/t/insights-from-a-gitcoin-grants-citizens-round-project-archimedes-lever/15406/3?u=jag); *this is relevant in this context b/c the GTC price has increased by ~14% since the time of your calculations*. 

Elastic DeFi sector is likely to benefit Gitcoin - thanks to DeSci. 

Therefore: it's imperative for DeSci to continue in the Gitcoin Ecosystem/DAO. Stewards such as yourself should be funded to continue doing indispensable work.

-------------------------

seldamat | 2023-06-21 22:28:08 UTC | #5

Great write up Boris, very thorough with clear goals and a plan to get there. 

The success of the past few DeSci rounds have all been bootstrapped from a revolving door of community members. A firmware update to move the community to a trustware OS is likely required for the movement to be self sustaining. 

DeSci is unlike many of the other communities, organizations, and funding rounds in the GTC ecosystem:

- it is decentralized and isoformic without a set definition by nature
- it is a bridge to non-crypto organizations, communities, and builders
- is a super-category of public goods and global areas of impact 
- doesn't depend on crypto to continue to develop or succeed

Moving forward, having a formal sub-DAO in place as a point of contact with potential funders such as non-profits, government agencies, enterprises, and philanthropists will accelerate the growth of DeSci and make public goods funding easier down the road.

This is an opportunity for many funders that have never heard of GTC before to come into contact on familiar grounds (science research and infrastructure funding). 

The benefits are many, the risks are few and Boris is the right person for the job. wagmi,
S

-------------------------

borisdyakov | 2023-06-25 16:14:38 UTC | #6

gm and thank you to everyone who has taken the time to read this and comment so far – I appreciate the support and welcome any and all feedback :) 

So far it seems the biggest questions are around how my proposal fits into the broader Gitcoin Grants Program and its evolution:

[quote="Viriya, post:2, topic:15460"]
I’d like to get a sense of how the program’s strategy is evolving (given current conversations around DAO resourcing and future states of the program).
[/quote]

This is a topic I've discussed a bit with @connor; I'll leave it to him, @M0nkeyFl0wer, or @azeem to officially comment on PGF's position while I share my personal view here:

My understanding is that despite our transition to being a protocol DAO, the Gitcoin Grants Program should and will remain a strategic priority in the near term. As the largest user of Gitcoin's products and tech, the Grants Program crucially demonstrates to partners and other potential users what is possible with the Allo Protocol and Grants Stack.

The future state vision is that as adoption of the Allo Protocol and Grants Stack grows, there will be many communities and organizations running different grant programs with various funding mechanisms on different cadences – with the Gitcoin Grants Program eventually being a small portion of total usage (if we succeed!)

I see the DeSci community as being a sort of intermediary step in this process: independent power-users of this technology that demonstrate how a grassroots community can fund its shared needs, yet invested in the success of Gitcoin and active in the community (and having a good reason to participate in governance!) Simultaneously, it can be a smaller-scale testbed for governance and funding experiments that might be valuable for the broader DAO.

[quote="jengajojo, post:3, topic:15460"]
Given the fact that any community can independently run their own QF matching rounds on Grants Stack, does it still make sense to invest resources in featured rounds?
[/quote]

If we hope to see widespread adoption of the Grants Stack and Allo Protocol I think it's actually essential that we invest resources in ***non-core*** rounds. Though anybody can already run a QF round via the Grants Stack, I do believe there's still a significant amount of support needed for one to be successful. **This is why we have the GR-OG!** Resources allocated to the GR-OG ***are*** directly supporting featured and independent rounds.

The investment in DeSci that I'm proposing  is to ensure we have the right structures and incentives to guarantee its continued existence and success within the Gitcoin ecosystem. With our own internal experience as operators, we can act as mentors to other grassroots communities, and hopefully can be the first of many impact DAOs that work with Gitcoin to fund public goods.

Finally, to answer some operational questions from @jengajojo:

[quote="jengajojo, post:3, topic:15460"]
* How much GTC/USD has been spent on operational expenses so far (salaries, gas, etc)?
[/quote]

The elected round stewards assumed this role with no guarantee of compensation, but the consensus within our community is that we should figure out a way to incentivize/compensate this role in the future (many reasons why this is important). Establishing a system to do this in a fair way that produces the results we want to see is one of the key things I aim to figure out over the coming months.

Costs for the DeSci round have been tracked [here](https://www.notion.so/gitcoin/DeSci-Round-Operations-Audit-0a04ffd88e634c1ea48e2ad36ec0e163), but so far total 0.111740902 ETH (~$210 USD) + approx $10 USD worth of $MATIC for governance facilitation on Polygon via the [Jokerace](https://jokerace.xyz/) and Coinvise. Gas cost for round payout is TBD (we're still figuring out sybil analysis), but is estimated to be ~$30 (based on [the txn](https://etherscan.io/tx/0xb007664bff7f44ebc45d33349930570135fa7d7229d9e327e9e6ff6b84ba8599) for the Metacrisis round payout).

To cover these costs, we created a [DeSci Grant Round Ops Fund](https://explorer.gitcoin.co/#/round/1/0x6e8dc2e623204d61b0e59e668702654ae336c9f7/0x6e8dc2e623204d61b0e59e668702654ae336c9f7-75) project for the DeSci round. These holdings, after reimbursements for gas fees, were proposed to be used as a retroactive reward to round stewards. This will be decided by community vote, but in light of the support shown for [our entry in the ongoing Citizens round](https://explorer.gitcoin.co/#/round/10/0x984e29dcb4286c2d9cbaa2c238afdd8a191eefbc/0x984e29dcb4286c2d9cbaa2c238afdd8a191eefbc-48) by the Gitcoin community, I would personally vote that this be earmarked for future direct grants proposals or retroactive rewards to other community members who have been working to make our round successful.

I was paid a total of $6480 USD over 3 months as a part-time contributor to PGF in S16 with my primary focus being DeSci, but this did not account for all my time spent on Gitcoin-related work.

[quote="jengajojo, post:3, topic:15460"]
* How many leads have been contacted for potential matching funds so far? and what is the general response?
* Can you offer some insights on the teams’ history of fund raising?
[/quote]

I'm now starting to follow up on the many positive conversations I had over the past months to secure funding for future DeSci rounds. The response has been positive and there's a lot of interest around DeSci as a new narrative in web3.

Without dedicating time to this partnerships work during S16 (and instead focusing on operations for the beta round) I brought in an additional $35K for the matching pool to top off the preexisting $50K we had (earmarked for a future round from Gnosis Chain's donation to the DeSci round in GR15). I additionally brought in $25K for a core round.

The scope of this proposal includes me dedicating more time to securing funds for future DeSci rounds. More importantly, my goal is to use what I learned while contributing to PGF to establish a system that leverages our entire community's network to generate these matching pools – **a set of incentives that reliably funds a subset of public goods while minimizing fixed costs.**

The DeSci community includes founders, investors, and people with deep networks in crypto. DeSci OGs like @vincentweisser were instrumental in raising >$500K for the DeSci round during GR15 – and with the recent success of our Beta Round and high level of engagement in our community I'm confident we can present an even more compelling case for funding partners to support DeSci.

-------------------------

PaigeDAO | 2023-06-26 11:16:18 UTC | #7

As a Gitcoin steward and as a founder of one of the first DeSci DAOs (FrontierDAO) I'd like to ask for more clarification on this process you allude to, please: 
*(via democratic election of four round managers/”stewards”, plus myself.)*
I was theoretically a part of all discussions and did not see anything about 'elections'. Including the Tg chat group for Beta Round - DeSci.   Where did I miss this?  
Thank you

-------------------------

DisruptionJoe | 2023-06-26 13:43:35 UTC | #8

This whole post is well thought out and touches on some key issues. You are offering an elegant solution that seems to be in the spirit of a "crawl, walk, run" approach. Here are a few items I specifically like. Most are around giving explicit authority and autonomy to the "recognized subdao" entity. 

[quote="borisdyakov, post:1, topic:15460"]
Design and execute on experimental incentive models for subDAO round managers and “partnerships team” to ensure sustainable round-to-round funding and operations

* Potential *retroactive* incentive model for round stewards (elected operators/manager): xx% of matching pool is awarded to round stewards as time-locked GTC (decided by the subDAO via QV or directly by QF on a “[grant round ops fund](https://explorer.gitcoin.co/#/round/1/0x6e8dc2e623204d61b0e59e668702654ae336c9f7/0x6e8dc2e623204d61b0e59e668702654ae336c9f7-75)” project in future rounds)
* Potential *prospective* incentive model for “subDAO partnerships”: Community-decided “commission” on closing matching fund contributions.
[/quote]

[quote="borisdyakov, post:1, topic:15460"]
Personally ensuring we secure a minimum of 50k in funding for the next 6 DeSci rounds (opting-out of the potential commission model described above while having my work funded by Gitcoin, until the 300k funding threshold is met)
[/quote]

[quote="borisdyakov, post:1, topic:15460"]
Define and ratify how a “recognized subDAO” can be formally recognized by Gitcoin

* What benefits does the subDAO receive?
* What commitments does the subDAO make to Gitcoin?
* How is this governed?
[/quote]

These items are all non-trivial strategy work that is best done bottoms-up in a pluralistic way. You're suggestion on how we do it with DeSci having trust from the community already built is a great step forward. 

I truly hope the community understands the value of this work as beyond simply managing a round, but more in the domain of managing a program while explicitly accepting responsibility for deriving some useful innovation as a part of your KPI. This is very intelligent in that it sets a KPI for the community to understand what success looks like, while leaving white space for the innovation to happen. Very well written. 

You have my support.

-------------------------

Joel_m | 2023-06-26 15:42:50 UTC | #9

I see myself as a visitor to the community, so I hope everyone takes my opinion with a grain of salt. That being said, I love the idea of subDAOs. 

I'm new to DAOs but familiar with writing about decentralized governance in "real life" (e.g. Bookchin, Zibechi, Ocallan), and these authors tend to stress that decentralized governance is powerful precisely because it allows for flexibly recognizing sub-groups, overlappnig groups, etc. They argue that this type of flexibility ends up letting communities make better decisions (I think this is also a big theme of the recent buzz about [plurality](https://www.plurality.institute/)). So I'm very much in favor of trying to implement a framework for that type of flexible recognition. 

BTW, @borisdyakov, if you have time, I'd love to chat more about the DeSci rounds -- it might be very helpful for the [research I'm currently doing at Gitcoin](https://gov.gitcoin.co/t/gcp-010-evolving-gitcoin-grants-the-q-e-d-quadratic-experimentation-and-development-program/14174/12). I'll DM you on twitter.

-------------------------

borisdyakov | 2023-06-26 18:57:51 UTC | #10

Hi Paige, happy to clarify this, and will also share some context on how we've tried to bootstrap some sort of community governance for the DeSci round/program.

I spun up the [DeSci x Gitcoin Community telegram group](https://t.me/gitcoindesci) on March 1st to create space for the community to give input on how DeSci rounds should be run. I tried to reach as many of the online DeSci spaces as possible, inviting folks to join from all the existing DeSci telegram groups I could find, and also by sending out an invite link to all GR15 DeSci grantees by email.

Since DeSci was not voted in as a core round for the Beta Round, it seemed important to people that we have some sort of process for electing round managers (which we called DeSci round stewards) that we could trust to represent the values of our community and its wishes. [I proposed a way to do this](https://t.me/gitcoindesci/1/397) on March 31st, gave ample time for feedback, and people started nominating themselves as candidates.

I gave an overview of this in this [twitter thread](https://twitter.com/BJ_Dyakov/status/1647966892001460224?s=20) but admittedly need to sit down and do a more comprehensive writeup.

This was an experiment and a V1 of this community governance process but I think it was successful given the time constraints. I believe that some governance is better than no governance, and if anyone is really unhappy with how the stewards acted in running this round they are more than welcome to run for a steward position for the next round!

Anyone in the group at the time of me posting this process was eligible to vote or to run for a steward position. To get voting tokens for the on-chain vote, you just had to submit a wallet address so those could be airdropped. I also offered to provide some $MATIC to anyone who needed it for gas.

The election outcome sparked lots of discussion in the Governance topic in the telegram group, but we managed to elect a small team to move forward with time-critical work to get the round launched, and will be integrating all the feedback into how we govern going forward.

I'm working on getting a charmverse space set up so we can hold long-form forum-style discussions on "how we do things as a community". To evolve away from "being in the telegram group" as criteria for voting, I plan to leverage the on-chain data from the DeSci beta round and GR15 so active community members (grantees and donors) are the ones who get a vote. 

I'll be sharing more on this in the telegram group soon!

-------------------------

PaigeDAO | 2023-06-26 18:10:39 UTC | #11

HI Boris, thank you for your response.  Yes, I've been in the Tg Gitcoin DeSci group since the beginning and all the way through. However, somehow I missed that process/ announdement, though I did notice when people started referring to themselves as 'stewards.'   I guess my question then is, is this intended as a SubDao to Gitcoin or to VitaDAO/ Molecule?  I guess I'd be hoping for a response beyond simple semantics.   Thank you.

-------------------------

borisdyakov | 2023-06-26 18:31:40 UTC | #12

I'm proposing that this DeSci community, which **currently exists around the mission of managing a continuing DeSci grants program via Gitcoin's Grants Stack/Allo protocol**, evolve into becoming a subDAO to Gitcoin.

In theory, we could continue to run these rounds as a community completely independently from Gitcoin. But I think there are lots of benefits (for both Gitcoin and this DeSci community) from there being some formal partnership/association between the two.

I'm not sure where you're seeing this connection to VitaDAO/Molecule.

-------------------------

PaigeDAO | 2023-06-28 14:32:23 UTC | #13

Hi - 
Wanted to share my response and more reflections on this initiative.
 
First will respond to several points made above by @seldamat in order to illustrate why it's important to distinguish between DeSci and Open Science and allow for a place for both. 

Firstly, thinking more deeply on your desire to be funded by Gitcoin for a position to head up a SubDao called 'DeSci' here at Gitcoin, I'd like to counter propose that should that proceed that there be at least two co-Stewards responsible as leaders of the SubDAO. 

For anyone who is following the chat threads within the DeSci, Blockchain for Science and Open Science discussion groups and larger diaspora, it will not come as a surprise to you that DeSci has become bifurcated as a movement. 

'DeSci' (decentralized science) is built upon the Open Science movement. Open Science has been a movement for over a decade and is championed by huge institutions such as UNESCO and even the White House declared 2023 as the Year of Open Science. 

For 'DeSci' - the added element is DeFi as most people understand it. Though there is currently some community discussion around whether DeSci necessarily incorporates DeFi. 

For reasons of brevity, suffice it to say that in the current regulatory environment, esp. for those of us compliant with US law, there is strong rejection to most DeFi strategies as they might be applied to science, scientific data and STEM research. Specifically I am referring to tokens, IP NFTs and other 'tools' that some of the community embraces and have used effectively but that others vehemently disagree with. 

In my frequent and ongoing interactions with the larger Open Science community  - this includes UNESCO, US Govt agencies practicing Open Science, White House office of Science and Technology who recently held Listening Sessions on Open Science, NumFocus, Center for Open Science... and others - there is often a skepticism, to outright distaste, toward all things 'blockchain' and crypto. 

DeSci cannot disassociate itself from crypto and blockchain since that is how it defines itself. And most who self-identify as 'DeSciers' also fully embrace these ecosystems. 

Open Science, on the other hand, is simply embracing the principles of transparent, accessible, inclusive and reproducible science and research.  It could employ DLT but it doesn't, by definition, have to. 

Therefore, given the current climate on a regulatory front and also given the current larger community sentiments and bifurcation of how people are defining best practices when it comes to employing emerging technologies (as in blockchain, DLT, crypto) to scientific research, I propose that a broader, more inclusive approach be considered in regards to this initiative of a SubDAO that you are proposing. 

**IN sum:**  I suggest that if a SubDAO for Gitcoin is established that focuses on science, that it welcomes and is inclusive of Open Science, too. 

That if a science focused SubDAO is established by Gitcoin community/DAO that there be at least two co-stewards recognized as leaders with equal authority with at least one of them being representative of the Open Science (as opposed to DeSci) movement; And that we respect and are cognizant of the constraints imposed on US based STEM projects *vis-a-vis* the current regulatory (crypto) climate.

https://open.science.gov/

https://www.cos.io/timeline

-------------------------
