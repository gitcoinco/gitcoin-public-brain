---
id: 11058
title: "[S15 Proposal] - Gitcoin Product Collective Workstream Proposal & Budget Request"
slug: s15-proposal-gitcoin-product-collective-workstream-proposal-budget-request
category: governance-proposals
url: https://gov.gitcoin.co/t/s15-proposal-gitcoin-product-collective-workstream-proposal-budget-request/11058
created_at: 2022-07-04T16:06:59.050Z
last_posted_at: 2022-08-02T18:36:29.533Z
posts_count: 22
views: 8252
like_count: 107
---

# [S15 Proposal] - Gitcoin Product Collective Workstream Proposal & Budget Request

<https://gov.gitcoin.co/t/s15-proposal-gitcoin-product-collective-workstream-proposal-budget-request/11058>
lthrift | 2022-07-04 16:06:59 UTC | #1

# Gitcoin Product Collective Workstream
## Season 15 Budget Proposal

This is an initial funding proposal for the Gitcoin Product Collective (GPC) Workstream requesting ratification as a structured workstream and budgetary funds for Season 15 (1 August 2022 through 31 October 2022).

## TL;DR

Gitcoin Product Collective is seeking to enter the DAO as a structured workstream in Season 15. We have been working in close collaboration with the DAO while residing in Gitcoin Holdings and are eager to fully integrate our work and operations. We will be bringing with us the foundational development of the Grants and Passport protocols and have ambitious goals to drive early adoption and validation of the designs in Season 15.

## Vision

As a collective, Gitcoin DAO has[ aligned itself with the purpose](https://gov.gitcoin.co/t/update-gitcoindaos-adopted-purpose-and-essential-intents/10984) to empower communities to fund their shared needs. In order to ensure progress towards achieving that purpose, one of our key essential intents is protocol adoption and growth, more specifically:

1. Build a widely adopted, modular Grants protocol that creates a flourishing ecosystem of funding mechanisms.
2. Build a widely adopted, modular Pluralism Passport protocol that creates a flourishing ecosystem of network effects around Decentralized Society.

The GPC workstream vision is to design and build these protocols while collaborating with other DAO workstreams to ensure they are distributed and adopted for our long-term success.

The Grants 2.0 protocol mission and vision in a nutshell is to build a suite of tools that enables a unified experience for grantees across multiple programs and provides an extensible foundation for any community looking to run a grant program to fund their shared needs. A more detailed overview can be viewed in [this recording](https://drive.google.com/file/d/1JkvYDjI1NVh9UZGE1QOHiJvR99AHzJrl/view?usp=sharing).

The Passport mission and vision is to build a collaborative and secure infrastructure for identity verification that gives individuals and communities the ability to verify the unique humanity and other attributes about their peers. This will serve as a critical building block to the security and efficacy of the Gitcoin Grants programs and others using quadratic funding with the Grants 2.0 protocol while also providing critical building blocks for social innovation across the ecosystem.

## Current State

The GPC team has been working within Gitcoin Holdings during prior seasons and has already begun the work to realize our DAO vision for protocol development. At this point we have achieved the following across the 3 protocol domains:

### Passport

An alpha release was successfully run during GR14. For [this release](https://passport.gitcoin.co/), the ability to generate a trust bonus score was switched to being powered by Passport. This meant that any new grants contributors or those who wanted to further boost their trust bonus now had to use Passport, rather than the previous Trust Bonus UI. Over 17,000 passports were created during Gitcoin Grants GR14 (there were 44,000 contributors to GR14).

### Grant Hub

Grant Hub has released an initial MVP of the product which allows project owners (formerly referred to as “grantees” or “grant owners”) to create their project profile which is then saved in an on-chain universal registry and enables a project owner to submit an application to a round run using the Round Manager protocol. The team is in the process of putting the final touches on a production release of this MVP to be deployed to Optimism.

### Round Manager

The Round Manager team is currently building their initial MVP. The MVP will allow a grants round operator to create a grants program on-chain, deploy a round contract, and review applications for participation in the round. With the MVP, round operators will calculate results and manage payouts manually. The MVP will be production tested with Optimism in running their second round of Retroactive Public Goods Funding later this summer.

## Season 15 Goals

For Season 15, GPC will be collectively focused on advancing protocol development to the point where grant rounds running end to end on the protocol suite enables half of core operations to be run programmatically rather than manually outside the protocol. This is an incremental step towards reaching the end state of being able to run large scale grant programs (Gitcoin Grants). We will also be focused on driving early adoption of the protocols through strategic partnership programs in order to have short feedback loops from production use and ensure we are building towards real needs.

### Shared Commitments

Across all 3 protocol domains, in Season 15 we will commit to:

* Enabling Moonshot Collective builders to be able to extend protocol functionality through developer documentation and on-going developer support
  * We expect this support to serve as early feedback on implementation of the protocols to ensure developers remain a first class citizen in the Grants 2.0 ecosystem.
* We will brand and name all of the protocol components in collaboration with MMM.
* GPC will work with DAO Support to develop Gitcoin’s knowledge base and evolve the support process, integrating the efforts to support existing products and onboarding new ones for support as they launch.
* Launch and run partner programs that drive a user centered approach to our protocol development and scale adoption over time.
  * The Round Manager Team, with support from the Grant Hub team, will collaborate with PGF on the Grants 2.0 Design Partner Program. Our goal is to use this program to test and validate design decisions for the protocol while also building up an initial Grant Program user base.
  * The Passport team will launch an Alpha Partner Program which targets 4-6 other application teams who have high interest in using Passport for identity verification.

### Passport

Passport has gone through an alpha launch during GR14 and served as the new path for grant funders to boost their matching percentage through an increased trust bonus score. During Season 15, the focus will be on solidifying our position for product-market fit through running an alpha partner program and hardening the Gitcoin Grants program through a more accurate Trust Bonus personhood score via Passport.

#### Commitments:

* Move over all GR15 contributors to Passport and decommission cGrants Trust Bonus entirely.
* Review the performance of the Passport’s technological architecture and interface, and the Trust Bonus in GR14, ship protocol and interface experience improvements for GR15.
* Improve the accuracy of Trust Bonus in GR15 by a measurable degree. The exact target for improvement and how to measure it will be determined in collaboration with GitcoinDAO Fraud Detection and Defense.
* Drive adoption of Passport by other dApps through an alpha partnership program.

### Grant Hub

Following Phase 1 of Grant Hub in Season 14, which will enable users to create projects on the decentralized project registry, the team will be focused on adding functionality to support project owners applying to grant rounds and tracking grant data, and will start to work towards a long-term vision of building project reputation.

#### Commitments:

* Build out Phase 2 of Grant Hub, which will enable project owners to apply to a round, view application status, track active grants, and view historical project data.
  * We will test Phase 2 of Grant Hub in partnership with Grants 2.0 Design Partners (i.e. Optimism’s RPGF round targeted for early August 2022)
* Expand Grant Hub project metadata to store verified fields, starting with verified spam and fraud signals
* Research how to further leverage Grant Hub project metadata to support building project reputation and niche curation. Long term, this enables more automated grant round eligibility curation.

### Round Manager

In Season 14, we will have built a foothold for the protocol by enabling Grants Round Operators to manage grant applications and review through the Round Manager dApp. In Season 15, we will focus on further expanding the Round Manager capabilities such that operators can run rounds end-to-end on the G2 protocol suite.

#### Commitments:

* Allow Round Manager to ingest verified spam and fraud signals from Grant Hub and filter projects based on those signals
* Allow Round Operators to select and configure a voting/contribution module from 2-4 options
* Design the Grant Explorer for Gitcoin rounds (i.e. interface for contributors to browse/vote) based on PGF partnership
  * Partner with PGF on the design of the future Gitcoin grants program
* Enable Round Manager to generate payout calculations based on the selected voting/contribution module and votes cast via a Contributor-facing front-end

## Season 15 Budget Requirements

|Budget Category|Description & Assumptions|Amt USD|Amt GTC|
| --- | --- | --- | --- |
|Contributor Compensation|Accounts for the compensation of all contributors to the workstream for 3 months.|$635,911|223,127|
|Contracting & Hiring Budget|Accounts for the cost of strategic consulting services & hiring to backfill the consulting roles.|$232,500|81,579|
|DevRel Expenses|Funding for Developer Relations across the protocol domains through hackathons and bounties.|$60,000|21,053|
|OpEx|This accounts for seeding the [DAO required budget](https://www.notion.so/gitcoin/Events-Policy-c80f5d08f99e4e3a89d45e04b16f395d) for contributors to take a once per year conference trip, covering travel for high impact in-person working time, covering costs associated with managing and issuing contributor payments, and providing contributors a small stipend for coworking space.|$55,018|19,305|
|Totals||$983,429|345,063|

#### Further Detail for Description & Assumptions

*Contributor Compensation* - We currently have a total of 13 core contributors (full-time) with a goal of getting to 16 core contributors by the end of the season. Generally, each domain will have 3 developers and 1 product manager. Supporting all 3 domains will be 2 workstream leads and 2 product designers. We will be filling the 3 open roles (2 developers and 1 designer) through the hiring and contracting budget below.

*Contracting & Hiring* - GPC has been engaging with [Focused Labs](https://focusedlabs.io/) for a strategic engagement that allowed us to more quickly ramp the team up on shipping MVPs of all protocol components. We are looking to hire 2 more developers by the end of the season to replace these contracting resources. Hiring these roles full-time will significantly reduce our on-going costs for these roles and we are doing so as quickly as possible without impacting delivery of the protocols.

We are also seeking one additional product designer to ensure we have enough support for design across all 3 development areas.

This budget is based on a maximum amount required to cover hiring at the top of the pay band for these roles. We will seek to be as conservative as possible with this spend and reduce whenever possible.

Finally, we have been contracting up to 30 hours a week with DAO contributor Nick Kammerdiener to provide DevOps services across all the teams. This engagement is slated to continue in Season 15 or until there is no more DevOps work to be done.

*DevRel Expenses* - At the end of Season 14, we began experimenting with building up a DevRel practice through the organization and funding of bounties and hackathons. Our goals with this approach were the following:

* road test our SDK, and documentation
* begin engaging with community builders in our discord
* discover if DevRel contributors could be sourced and further engaged for future DevRel work

The Passport hackathon has just ended and we plan to continue trying this approach with the rest of the development areas in Season 15.

#### Per Project Cost Allocations

Given the above structure of our budget it may be helpful to see the costing on a per team basis -this is broken down as follows:

* Gitcoin Passport: 22.95%
* Grant Hub: 35.03%
* Round Manager: 42.02%

These costs include the shared resources (design and workstream leads allocated ⅓ to each project)

The higher cost for Round Manager is primarily driven by the inclusion of Focused Labs, this cost will decrease over time as we hire into that team and roll off the external resources.

### Budget Ask

||USD|GTC|
| --- | --- | --- |
|Season 15 Total Need|$983,429|345,063|
|60 day reserves*|$462,085|162,135|
|Amount Requested from Treasury|$1,445,514|507,198|

**60 day reserves are calculated only against the contributor compensation and payroll related OpEx.*

Note: A denomination in dollar amount will be prioritized in budget proposals over GTC - if the spot price assumed at the time of posting ($2.85) this document on the forum changes between then and when the budget gets proposed on-chain, the GTC amount will be readjusted to reflect the USD amount above. GTC amounts are rounded values.

Current signers of the Gitcoin Product Collective Multisig will be Lindsey Thrift, Kevin Olsen, and Kyle Weiss. We are also working to identify two additional cross-functional workstream leaders to serve as signers and hold GPC accountable.

## Team Composition

In its initial season, the GPC will be composed of the team that has been operating in Gitcoin Holdings. All contributors are full-time.

#### Core Contributors
*Workstream Leads* - Lindsey Thrift & Kevin Olsen
*Software Developers* - Aditya Anand, Chiboutu Amadi, Graham Dixon, Gerald Iakobinya-Pich, Timothy Schultz, Andrea Franz, & Daniele Salatti
*Product Managers* - Nate Gosselin, Michelle Ma, & Leon Erichsen
*Product Designers* - Eduardo Tovar

## Conclusion

Thank you for taking the time to consider our proposal and the commitments we have put forth for Season 15. We look forward to answering any questions you may have and ensuring our work is closely aligned to the expectations of the collective DAO and stewardship.

-------------------------

krrisis | 2022-07-04 16:36:05 UTC | #2

I'm in full support of this proposal. As I've commented on the draft it is difficult to add a whole lot more, as all my feedback is already integrated :) 

Looking forward to see GPC landing fully within the DAO!

-------------------------

tjayrush | 2022-07-04 22:59:18 UTC | #3

I'll start the comments, I guess.

1. Very well done. Thorough, clear, detailed. Excellent job.

2. As I was reading this, I kept thinking to myself that I wanted to know who the people are -- their names -- who makes up this working group? I don't remember that being part of previous rounds' budget proposal. I'm very glad to see the list of names included, and I think every other budget proposal should included the names of the primary people on the team as well as information about how many contributors are involved (for easier calculations of how much people are being paid).

3. Again, as I was reading this, I kept thinking -- this is a lot of money -- but it's also a lot of work. I wondered how much of this work removes work from other work streams? In other words, is this proposal adding brand new money to the total budget or is this proposal moving money (and therefore work) from one work stream to another -- and if so, how much and from which work streams?

4. As I read this, I felt that this work stream has a broader mission than some others -- the comments about reaching out to MMM and Moonshot. It would be good if those referenced work streams (and others) noted this work stream's mission and co-ordinated to eliminate duplicative effort and would show a consciousness of the need to work together.

5. As has always been the case, I'm concerned about the comment that the budget is denominated in dollars and yet is paid out in GTC. I'm certain I don't need to explain what happens if the price of GTC goes in half. Not good. Also, if the price doubles, is the US dollar ask still prioritized? Also -- I probably don't need to point this out, but there are other reactions to a change in the exchange rate -- a lessening of the work load, for example.

All in all, a very well done proposal. And, as will always true for me, I reserve the right to make no further comments.

-------------------------

lthrift | 2022-07-05 14:28:58 UTC | #4

Thanks for taking the time to review and comment @tjayrush. Here are some answers to your questions:

[quote="tjayrush, post:3, topic:11058"]
is this proposal adding brand new money to the total budget or is this proposal moving money (and therefore work) from one work stream to another – and if so, how much and from which work streams?
[/quote]

There was previously a "Decentralize Gitcoin" work stream that built an early prototype of the Grants 2.0 protocols (referred to as dGrants), but that work was all merged together with the rest of the protocol and software development being done by the Holdings team to take a more comprehensive and aligned approach. There was no DAO budget in Season 14 that covered this work. Therefore, this is new work and budget for the DAO in Season 15. There are no other groups doing this work at this time. 

[quote="tjayrush, post:3, topic:11058"]
the comments about reaching out to MMM and Moonshot. It would be good if those referenced work streams (and others) noted this work stream’s mission and co-ordinated to eliminate duplicative effort and would show a consciousness of the need to work together.
[/quote]

Tagging @DisruptionJoe @GTChase @seanmac as workstream leads for FDD, Moonshot Collective, and MMM to see this comment from TJ, as well. These are conversations we've been having with these groups for multiple months now, so none of the referenced collaboration is a surprise and most work is already in progress. Alot of this is the result of the overall DAO aligning around essential intents, of which GPC's work is at the core of the protocol EIs. 

[quote="tjayrush, post:3, topic:11058"]
I’m concerned about the comment that the budget is denominated in dollars and yet is paid out in GTC.
[/quote]

This has been a CSDO decision as it enables the workstreams to plan according to the way contributors need to be compensated in order to retain them. There are efforts underway to diversify the treasury and address the pain points you've mentioned. I just want to highlight this denomination in the GPC budget request is not a unique decision on GPC's part.

-------------------------

kyle | 2022-07-05 17:45:25 UTC | #5

I am really excited to have GPC joint he DAO. This is a really robust proposal, with great insight into a team that has really started to fire on all cylinders. 

The Passport launch has been great to see, and I look forward to more protocol launches and development.

I am usually less worried about how much a team needs to accomplish their goals and more worried about the goals they are trying to accomplish. This holds true here and I am excited to see GPC make progress in the DAO. I am supportive and have appreciated having these workstreams leads partake in CSDO and other key aspects already.

-------------------------

lthrift | 2022-07-05 21:28:57 UTC | #6

@tjayrush I actually just did a quick look back to give a more complete look on this question

[quote="tjayrush, post:3, topic:11058"]
is this proposal adding brand new money to the total budget or is this proposal moving money (and therefore work) from one work stream to another – and if so, how much and from which work streams?
[/quote]

You can see the two Decentralize Gitcoin Workstream budget requests here: 
[August 2021](https://gov.gitcoin.co/t/decentralize-gitcoin-workstream-budget-request/8121) - Requested 41.3k GTC 
[October 2021](https://gov.gitcoin.co/t/proposal-decentralize-gitcoin-workstream-budget-request-q4-2021/8895) - Requested 127k GTC (total 138k GTC budget)

These requests do not denominate at all in USD or other stable coin to give an indication of how they got to these numbers, so a rough estimate of the potential spot price in each of these months would give you the following USD denominations: 

August 2021 - @ $9 USD spot price, $371,700 USD
![Screen Shot 2022-07-05 at 3.24.44 PM|690x412](upload://j4IjwK5xE1pFjmUiVF7jGIrXSKX.png)

October 2021 - @ $9 USD spot price, $1,143,000 requested of a budget of $1,242,000 
![Screen Shot 2022-07-05 at 3.26.14 PM|690x403](upload://A2cC4Q1rlnesOgCEZtuYEwJGJcF.png)

So, while there was no budget for this work in Season 14, Seasons 12 and 13 the DAO did shoulder budget for similar work.

-------------------------

Pop | 2022-07-06 14:48:16 UTC | #7

This is great historical context, @lthrift  - thank you for surfacing it and illustrating the pattern we saw for this work in prev seasons. 

I would also love to know if any of the budget from prev seasons remains at all? And if so, can it be moved across to this new workstream?

-------------------------

kyle | 2022-07-06 15:25:51 UTC | #8

The budget that remains is fairly small (Price has dropped 75% since funding). I don't think we should plan for moving that over, but I dont feel strongly. 

The current plan is to move those funds to the Foundation controlled Gnosis safe. We have used those funds for a few small expenses to date (paying for HubSpot migration, Steward compensation, etc.).

-------------------------

DisruptionJoe | 2022-07-07 17:47:42 UTC | #9

I highly in support of this budget. It is one of the most important things GitcoinDAO will do!

-------------------------

ZER8 | 2022-07-07 20:51:37 UTC | #10

Great 2 see this happening! Welcome to the DAO :robot: Our collective success depends on the success of Grants 2.0 and I'm sure that we will all contribute in making that happen.


Happy to help with anything I/we as the GIA can. Be it general info around grants, grant eligibility or anything else. I'm also very eager to try to find how the GIA will fit into this Grants 2.0 and Passport future. A simplistic vision would be a future in which we can be a sort off add-on to the round manager
. :robot:
 

[quote="lthrift, post:1, topic:11058"]
Research how to further leverage Grant Hub project metadata to support building project reputation and niche curation. Long term, this enables more automated grant round eligibility curation.
[/quote]

[quote="lthrift, post:1, topic:11058"]
Allow Round Manager to ingest verified spam and fraud signals from Grant Hub and filter projects based on those signals
[/quote]

These are the key areas that I would love to help in. Tagging @David_Dyor also.

-------------------------

Jodi_GitcoinDAO | 2022-07-07 23:28:10 UTC | #11

I'm supportive of this budget and thrilled to have the team driving our protocol development in the DAO.  I look forward to working with GPC on the User Support commitment shared above and other priorities.

-------------------------

epowell101 | 2022-07-10 16:40:17 UTC | #12

Thank you for the clear budget.  Very excited to see the continued progress on Grants 2.0!

I would second the comments about preferring to see yet more clarity in terms of overall impact to budget - I think your response as I understand it is that this was more or less net new work and as such we should not expect any offsetting reductions from other workstreams?  

Another question along similar lines - metrics - is there a way for interested observers to track typical development metrics so we can begin to get a feel as to the maturity of the process?  Typically I've seen these in burn-down charts and so on out of ye ole Jira.... I looked around in Discord however likely am not looking in the right spots.  

Lastly - you mention the importance of partnerships to provide feedback for all aspects and the interaction w/ the other work streams in this effort.  Can you shed more light on how these partnerships w/ potential users and other partners are being recruited, prioritized, and managed?  As a Wildfire representative, we are working in meta governance and related roles w/ 12+ web3 organizations - I'm wondering again whether we can learn more about this effort and potentially contribute if only by educating the other organizations w/ which we are working.  Is there a write-up or thread on this product partnership strategy you can point us towards?

Again - this was an extremely clear and encouraging budget request.  I hope the above few questions help shed further light on it.

-------------------------

linda | 2022-07-11 18:57:53 UTC | #13

Thanks for the detailed proposal, it was really helpful in understanding the purpose and scope of the workstream. 

While it is a significant amount of requested funding, I think this is important work for Gitcoin and I'm supportive of it. 

My only request given this large amount is in order to help make the DAO treasury long-term sustainable for all workstreams, where possible this season and future seasons to try to be conservative with spending on nice-to-have vs requirements along with leveraging work done by other workstreams as to not have duplicative work (as @tjayrush mentioned).

-------------------------

ceresstation | 2022-07-12 17:14:27 UTC | #14

Biased of course, but strongly in support of this proposal! Especially excited to find ways to collaborate around DevRel and to see how these tools enable utility across the Gitcoin ecosystem. 

As others have mentioned this is a high budget, but one that's absolutely critical to our success long term. Even in a bear market, we need to put energy and time towards the futures we want to see.

-------------------------

seanmac | 2022-07-12 22:26:24 UTC | #15

Highly supportive of this proposal, very well put together. On behalf of MMM we are super excited to have you all join the DAO and continue ramping up our protocol marketing team & efforts!

-------------------------

lthrift | 2022-07-13 01:29:12 UTC | #16

[quote="epowell101, post:12, topic:11058"]
I would second the comments about preferring to see yet more clarity in terms of overall impact to budget - I think your response as I understand it is that this was more or less net new work and as such we should not expect any offsetting reductions from other workstreams?
[/quote]

That's correct. There will be no offset from Season 14 budgets. 

[quote="epowell101, post:12, topic:11058"]
is there a way for interested observers to track typical development metrics so we can begin to get a feel as to the maturity of the process? Typically I’ve seen these in burn-down charts and so on out of ye ole Jira… I looked around in Discord however likely am not looking in the right spots.
[/quote]

You can follow along progress in the #gpc-demos channel. We are currently maintaining lean, single priority backlogs that drive towards outcomes rather than scrum style sprint commitments with burn down charts. We'll be adding a monthly public chat on the roadmap with progress reports and upcoming work starting the first week of August. 

[quote="epowell101, post:12, topic:11058"]
Can you shed more light on how these partnerships w/ potential users and other partners are being recruited, prioritized, and managed?
[/quote]

We have kicked off the design partnership program for Grants specifically with the PGF Partnerships team. Here is a [deck that outlines the program](https://docs.google.com/presentation/d/1EL6pFKLmCF-brrg2xbcMBnFjweOM0wvyRrMVwv-YJ6o/edit?usp=sharing). For Passport we are just shaping up the details and don't have anything public to share just yet. It will be focused on partners who are interested in integrating their dApps with Passport for sybil resistance and identity verification. I'm happy to [hop on a call](https://calendly.com/lindsey-thrift/15-minute-quick-sync) to answer questions you might have and see if there's a fit to work together on it.

-------------------------

lefterisjp | 2022-07-15 22:46:56 UTC | #17

Hey guys,

Thanks a lot for the proposal. I was expecting this at some point though as I wrote in discord, please ping us early enough for comments. 

The proposal is well written and structured.

The project is a must to have since gitcoin grants 2.0 is what will be built from this workgroup as I understand. This brings the obvious question to me. If GPC builds gitcoin grants then why do we need MoonShot collective and generally would GPC also pick up work from other workstreams? And if yes, which ones and what work?

With the addition of yet another workstream, and the market being the way it is I think we really need to ask hard questions and perhaps restructure the workstreams even further. I am pretty sure there will be overlaps, and as such we will end up wasting funds as a DAO. Let's try to frontrun this problem by thinking ahead. If we spend $1.5m on each workstream every 3 months, and we have 6 workstreams the money is gonna run out fast.

[quote="lthrift, post:1, topic:11058"]
In Season 14, we will have built a foothold for the protocol by enabling Grants Round Operators to manage grant applications and review through the Round Manager dApp.
[/quote]

Was that done in S14? Because from what I saw it was a bit chaotic with round managers not knowing who applied where.

[quote="lthrift, post:1, topic:11058"]
contributors to take a once per year conference trip,
[/quote]

This $55k is for how many contributors? And since this is for 3 months, are we to assume you need $220k for OpEx/travel expenses in a year? So for 16 people ~$13,750 for such expenses in a year? Isn't that very high for travel expenses and all the other things you mentioned per person in a year if you only do one trip per person?

[quote="lthrift, post:1, topic:11058"]
The Passport hackathon has just ended and we plan to continue trying this approach with the rest of the development areas in Season 15.
[/quote]

Hackathons and attracting talent to play with the SDK is a good thing. But do you have any ways to measure effectiveness of this budget? What are the KPIs with which you judge these were money well spent?

-------------------------

kevin.olsen | 2022-07-16 06:01:49 UTC | #18

Hey Lefteris thanks for jumping in with your questions!

[quote="lefterisjp, post:17, topic:11058"]
If GPC builds gitcoin grants then why do we need MoonShot collective and generally would GPC also pick up work from other workstreams? And if yes, which ones and what work?
[/quote]

We've already been engaging with moonshot, with our folks collaborating on some projects (passport had moonshot team members). We primarily see MC as evolving to be the first "3rd party" builders on top of the grants protocol. Their S15 roadmap is shaping up to have a few squads who will run out ahead of us, finding interesting problems they can solve on top of the core protocol we are shipping.

To the second part of your question, we certainly hope the grants protocol will alleviate some of the toil other groups in the DAO experience delivering our grant rounds, it's too early to set explicit targets for efficiency gains, but  there are conversations ongoing with PGF and FDD to find effective ways to automate work and scale their operations more effectively.

[quote="lefterisjp, post:17, topic:11058"]
Was that done in S14? Because from what I saw it was a bit chaotic with round managers not knowing who applied where.
[/quote]

GR14 was run with the same centralized platform, but the season (S14) is still ongoing and we have working MVPs for the grant hub, and the application flow to the round manager is under development now. I couldn't find the source for the original line you quoted in this post, but I would note that we have shifted some of our delivery targets to prioritize supportting our design partners (alpha users) to allow us to launch with and learn from some smaller scale grants programs before migrating the gitcoin rounds as first users of the protocol.

[quote="lefterisjp, post:17, topic:11058"]
This $55k is for how many contributors? And since this is for 3 months, are we to assume you need $220k for OpEx/travel expenses in a year? So for 16 people ~$13,750 for such expenses in a year? Isn’t that very high for travel expenses and all the other things you mentioned per person in a year if you only do one trip per person?
[/quote]

Good question, the travel portion of the request here is for half the annual travel budget (not a quarter) with an estimate of 5k per contributor (13 * 5k) / 2 = $32,500, the remainder of the requested budget should cover our payroll fees (utopia labs), a coworking stipend to help folks that have existing coworking arrangements in holdings to cover those fees in the DAO, and a small tech refresh stipend.

[quote="lefterisjp, post:17, topic:11058"]
Hackathons and attracting talent to play with the SDK is a good thing. But do you have any ways to measure effectiveness of this budget? What are the KPIs with which you judge these were money well spent?
[/quote]

Another good question, so far we've just concluded our first hackathon for the Gitcoin Passport, and saw some great contributions. Our hypothesis here was that we could bootstrap our devrel work first by engaging via a hackathon to receive quick feedback on our SDK and documentation. This so far looks like a success. Secondarily, we hypothesized that we might be able to source devrel talent that we could engage with outside the hackathon, we haven't had the chance to close the loop on this, but given some strong contributions I've got my fingers crossed. Lastly, we were pleasantly surprised that we also received some great open source contributions that could be used to extend our products and documentation. The results here are promising (4 new stamp integrations submitted, and some strong educational content). 

Given this was a first experiment that was run within holdings with holdings' budget we didn't have the request for KPIs, the experiment framing was sufficient to kick this off.

Going forward I'd be game to formalize some of these experiments, perhaps via the forum here, or in discord to help provide some goals and outcomes to the DAO as we progress the devrel function for the protocol and ensure we're using these funds effectively.

-------------------------

kevin.olsen | 2022-07-16 14:56:37 UTC | #19

The snapshot vote for this Budget Request is live here: [Snapshot Vote](https://snapshot.org/#/gitcoindao.eth/proposal/0xc6309348f43ba77bb488d2d5f154db3264f86a890b500fa8286fe089c6ddc9a0)

Thank you all for your participation in this process 🤖❤️

-------------------------

lefterisjp | 2022-07-21 09:22:43 UTC | #20

So I will vote a reluctant YES in this proposal.

It seems that GPC is the actual product arm of Gitcoin and it finally joins the DAO and if anything is to ever get funding it's this workstream. 

What I would like to see in the near future is to understand what each workstream should do because initially I thought moonshot would do dev stuff but now it seems that GPC is what will create the Gitcoin 2.0 grants.

We have too many workstreams and not all of it makes sense to keep being part of the DAO. Bear market is here and Gitcoin should not be a fat cash cow to be milked.

-------------------------

GTChase | 2022-07-21 12:52:46 UTC | #21

[quote="lefterisjp, post:17, topic:11058"]
his brings the obvious question to me. If GPC builds gitcoin grants then why do we need MoonShot collective
[/quote]

This question is one we have been expecting at Moonshot, and I think a fair one at that. I appreciate your willingness to ask these kinds of questions. 

@kevin.olsen's response was pretty spot on, but figured it wouldn't hurt to give some direct insight to MC's planning for s15.

It’s clear you see the importance of the Grants + Passport protocols. MC’s priority is to help GPC make these protocols more accessible by being the first community to build on top of them, i.e. dog fooding.  MC has a diverse community of builders to mobilize which enables us to provide rich feedback on the protocols. This allows GPC to quickly iterate on documentation/SDK's/features, which in return will provide confidence across the board that these protocols are indeed approachable and ready for primetime. 

The second value add here is, MC can expand the development opportunities for the protocols.  What MC builds on top of the protocols should be valuable solutions to key problems that have been identified/heard from key design partners. In fact, what you will see in our s15 budget proposal are items that were prioritized in collaboration with GPC and key stakeholders to ensure we are working on high impact items. Not only can we expand on the development opportunities, but also mobilize talent that can contribute directly to the teams and work of the core protocols. This is already happening today as we mobilized product and engineering help for Passport, and short term engineering help for Grants 2.0. 

TLDR: GPC = core protocol work / defined products. MC = Dogfooding + experimentation + innovation (aligned with EI’s)

[quote="lefterisjp, post:17, topic:11058"]
pick up work from other workstreams?
[/quote]

This is actually something MC is aiming to help with in future seasons as well, planning/strategy calls are happening on what this best looks like. Essentially becoming the trusted source of software development for the DAO workstreams that have a need for software outside of the protocols to solve key problems, but don't have devs or dev capacity. An example of this is working with the Public Goods Funding ws to help build partnerships or help build products that facilitate and scale their fundraising for public goods (aqueducts and fee swaps). To capture more of these opportunities we will roll out an idea/problem submission form for WS’s to submit areas they need help with and prioritize those against other problems/ideas that help achieve our EI’s.  

The reason that is coming in future seasons is we want to stay hyper focused on ensuring the protocols are approachable and are built with the needed solutions to be successful. We will continue to work with other WS’s to have a solid plan on what becoming this trusted source of development looks like and how we best scale that effort to ensure we are capturing those ideas and prioritizing them accordingly.

-------------------------

Fred | 2022-08-04 11:43:41 UTC | #22

![GPC_S15|928x1000](upload://3tHn8yv1Sr4zXjD19eA3TgGhexB.png)
Visualization of the budget request above. Please reach out if you have any questions or input.

-------------------------
