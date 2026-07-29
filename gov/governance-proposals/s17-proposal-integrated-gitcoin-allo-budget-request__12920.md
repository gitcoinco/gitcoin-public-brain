---
id: 12920
title: "[S17 Proposal] INTEGRATED Gitcoin Allo Budget Request"
slug: s17-proposal-integrated-gitcoin-allo-budget-request
category: governance-proposals
url: https://gov.gitcoin.co/t/s17-proposal-integrated-gitcoin-allo-budget-request/12920
created_at: 2023-02-13T15:49:03.556Z
last_posted_at: 2023-02-22T08:14:09.615Z
posts_count: 9
views: 3028
like_count: 12
---

# [S17 Proposal] INTEGRATED Gitcoin Allo Budget Request

<https://gov.gitcoin.co/t/s17-proposal-integrated-gitcoin-allo-budget-request/12920>
nategosselin | 2023-02-13 15:49:03 UTC | #1

# [S17 Proposal] INTEGRATED Gitcoin Allo Budget Request
***NOTE: This request is structurally the same as the draft budget, but with additional detail on our workstream's remit, strategy, and roadmap for this season.***

During Season 17, the GPC workstream (Gitcoin Product Collective) has decided to split into two workstreams: **Gitcoin Allo** (this workstream) and **[Gitcoin Passport](https://gov.gitcoin.co/t/s17-proposal-draft-gitcoin-passport-budget-request/12727)**, which is focused on our Passport protocol and stack. Splitting GPC into two workstreams will allow for a more “complete” team structure in the future. @nategosselin and @kevin.olsen will be leads for this workstream. 

It's worth taking a moment to clarify exactly what this workstream's remit will be. As outlined on our [workstream page](https://www.notion.so/gitcoin/Grants-Stack-Allo-b650b50c91d14e43adacae14f3f2bd53), our responsibility is *building* the Grants Stack suite of dApps and *incubating* the initial development of Allo Protocol. Why the distinction? The long-term vision for Allo Protocol is that it stabilizes and progressively decentralizes from workstream "ownership" to true DAO/community ownership. This team is responsible for shipping this first iteration, but we will work with the rest of the DAO to eventually establish true community governance of the protocol and its code. Over time, we expect this workstream will function more as a product development team for Grants Stack* exclusively, while also being prominent contributors to the decentralized Allo Protocol.

>*We've decided to call ourselves the Allo workstream despite a long-term focus on Grants Stack primarily for expediency reasons: it's a shorter name.



## Essential Intents

We are focused on a number of the Essential Intents. Specifically the following two:
1) Protocol Adoption + Growth
2) Financial Sustainability


## TL;DR

This season the Allo workstream will be focused on transitioning from alpha to beta, with Eth Denver / the April Gitcoin rounds as key milestones and inflection points. Our team is focusing on work for both Allo Protocol and Grants Stack, each with associated S17 outcomes: 

**Allo Protocol:**
The tl;dr for Allo this season is **finishing Protocol v0** and beginning to get builders working with the codebase. Our two Allo-focused outcomes are:
* **[Enable Payouts](https://www.notion.so/gitcoin/Protocol-Payouts-d6f14dd0463a4051bd618295c47155df)** — finalize the payouts interface and build our first payout mechanism so that there is an end-to-end protocol flow
* **Engage the developer community** — with the foundational protocol complete, we will ramp up our DevRel efforts and work on getting external teams building on Allo

**Grants Stack:**
The primary goal in S17 is **productizing QF rounds on Grants Stack**. We received great feedback during our alpha period and want to focus on addressing so both our Grants Program and self-serve customers can run successful QF rounds. Our outcomes are:

* **Improve the project application and review flow** - a major pain point for program managers is the time spent reviewing and managing applications. This outcome will focus on easing that process and providing some high-demand features from the applicant side.
* **Build a project reputation system** — another angle for improving the review process is enabling projects to build verified reputation so that programs can more easily vet applications. This season will focus on building out our MVP of this experience.
* **Provide an easy, intuitive QF round experience** — we want the "QF package" on Grants Stack to be simple from end-to-end, with an easy "Hello World" setting for programs new to QF and enough tooling that sophisticated users like our Grants Program can tune the system. This outcome will focus on making that a reality. 

Based on what we learned in Season 16, we recognize the need to continue being nimble with our development roadmap so that we can quickly adapt to the needs of the market. This season's roadmap will likely change month-to-month as we get feedback, so our outcomes are focused on key aspects of the platform that will receive the bulk of our iteration cycles. You can check the [roadmap section](https://www.notion.so/gitcoin/Grants-Stack-Allo-b650b50c91d14e43adacae14f3f2bd53?pvs=4#63b3b881119740bfabd0516642ef05c9) of our Notion page if you ever want to see what we're up to at a given moment.


## Amount

Gitcoin Allo (GA) is requesting **$803,533** for S17. We will also send some of the treasury to the Gitcoin Passport Workstream (assuming it's funded) to help split our reserves. A breakdown of the budget can be found at the end.

|Gitcoin Season|Season 15|Season 16|Season 17|
|---|---|---|---|
|Season Budget|$-- |$-- |$803,533|

***1)** The amount of GTC requested and the value of the reserves will be adjusted based on the current market value at the time this proposal is moved to Tally using the lower of the current price or the 20 day moving average, whichever is lower.*



# Objectives and Key Results


## Milestone Report for the past Season


**Legend**
🟢 Success / completed / shipped
🟡 Incomplete but will hit goal and/or priority changed for initial description
🔴 Incomplete, will not hit goal (see description for reasons why)
⚫️ Canceled (see description for reasons why)


|Initiative/Project|Always-on|Key Results<br>|
|---|---|---|
|Round Operators can run a Quadratic Funding round on the protocol|NO|🟢 Ran 5 Alpha rounds (UNICEF, Fantom, 3 Gitcoin Alphas) + 2 simulated quadratic funding rounds| |
|Round Operator can run a Quadratic Voting round on the protocol|NO|⚫️ The team did significant scoping and discovery but, in consultation with other workstreams, ultimately decided to deprioritize QV in favor of remaining focused on QF, Alpha round support, and payouts work  
|Round Operator can execute payouts on the protocol|NO|🟡 The team originally planned to have this completed by Eth Denver, despite including it as a milestone on our S16 budget. We are still on track to build this by the launch in Denver. |  |
|Donors can browse and assess the projects in a round|NO|🟢 All alpha rounds mentioned above used the Explorer front end designed for this experience. The Gitcoin Alpha rounds also included a first integration with Passport for Sybil Defense. | |
|Project Reputation |NO|🔴 Our workstream had multiple S16 milestones that were effectively the same problem: enabling project reputation. The Grants Hub team spent significant time exploring the problem area of users bringing project reputation to other protocols, but ultimately learned that this was not an immediate need. Given these learnings, we've refocused on an Allo-specific funding use case for project reputation and will be working on that area in S17.


## Objectives and Key Results
As mentioned above, we will primarily use a monthly roadmap for how we translate our themes into development work. In February we are focusing on three high-priority needs for launch (payouts, repo refactor, and application flow improvements). We will share an updated Season 17 roadmap in the coming weeks and update it on a monthly cadence as our plans crystallize.

*Note: at this stage of development we have yet to establish baseline metrics for our products. We plan to establish our core metric portfolio and begin measuring baselines this season. Our goal is to transition to metrics-lead objectives in future seasons. For now, we have left metrics blank and instead focused on likely projects.*


## List of S17 OKRs

|Layer|Initiative/Project|Metrics|Likely Efforts|
|---|---|---|---|
|Allo Protocol | Enable Payouts|- |- Finalize payouts interface<br> - Build bulk payout mechanism
|Allo Protocol |Engage the developer community|- |- Refactor repos into easy-to-use Allo repo<br>- Improve Documentation, Legibility, DX<br> - Partnership and Project Incubation (likely focused on allocation mechanisms + payouts)
|Grants Stack|Improve the project application and review flow |-|- Improve Application experience for Operators + Grantees<br> - Improve project review flow for Operators<br>|
|Grants Stack|Build project reputation system|-|- Enable new verified credentials so that projects can accrue reputation (including KYC)|
|Grants Stack|Provide an easy, intuitive QF round experience|-|- Improve and enrich the explorer experience for donors<br> - "Hello World" QF <br>-Improvements for Grants Program operational management<br>- General iteration on Alpha round feedback<br>|



## Budget Breakdown
We have broken the budget down by staffing, contracting, devrel, opex as we feel like this gives fairly granular details into where the funding will be going. 

### View: USD per Category

|Gitcoin Allo denoted in USD||||||
|---|---|---|---|---|---|
|Staffing||**2023.02**|**2023.03**|**2023.04**|**S17 Total**|
||Core Contributors (13)<br><br>- **Engineering (9)**: Aditya, Andrea, Bhargav, Daniele, Hans, Jason, Josef, Kurt, Mo<br> - **Design (2)**: Melissa, Will<br>- **Product (2)**: Michelle, TBH|181,201|180,868|180,868|542,937|
||Leadership / Ops (3) <br><br> - Kevin, Michael, Nate |34,865|34,865|34,865|104,596|
|**Total Staffing**||**216,066**|**215,733**|**215,733**|**647,533**|
|Contracting||||||
||DevOps|12,000|12,000|12,000|36,000|
|**Total Contracting**||**12,000**|**12,000**|**12,000**|**36,000**|
|DevRel||||||
||DevRel|15,000|15,000|15,000|45,000|
||Hackathons & Bounties|5,000|5,000|5,000|15,000|
|**Total DevRel**||**20,000**|**20,000**|**20,000**|**60,000**|
|OpEx||||||
||Saas Fees (AWS, Datadog, fleek, etc.)|20,000|20,000|20,000|60,000|
|**Total OpEx**||**20,000**|**20,000**|**20,000**|**60,000**|
|---|---|---|---|---|---|
|**Total GPC Budgeted Spend**||**268,066**|**267,733**|**267,733**|**803,533**|
|60 Day Reserves|||||**535,635**|
|S16 Treasury Balance**|||||645,628|
|**Total S17 Request**|||||**693,540**|

** *Note: final treasury balance will be updated in integrated proposal.*

-------------------------

Viriya | 2023-02-13 18:00:24 UTC | #2

I will be voting *yes* on this budget. 

I am excited that more PM support is being recruited. From what I observed last season, I think that resourcing ops and building skillset in that area would level us up tremendously. 

Here's to shipping season 🍻

-------------------------

JR-OKX | 2023-02-13 19:21:47 UTC | #3

Voting yes on this budget proposal! I am curious to learn and see how how KYC and AML can be reinforced in the new verified credentials system.

-------------------------

chaselb | 2023-02-14 02:13:07 UTC | #4

I'm going to abstain to this budget request since I have not dedicated the time to really review like the other stewards.

-------------------------

kevin.olsen | 2023-02-15 21:34:13 UTC | #5

The Vote for this budget has been posted and is now live on https://snapshot.org/#/gitcoindao.eth/proposal/0x555f90d3c76bd44ee4727b627b424d524a799b8dde9784991848c90b599e6562

-------------------------

GordonDr | 2023-02-16 06:51:34 UTC | #6

Guys, I don't understand, why it is impossible for me to participate in DAO voting on snapshot.
I have both GTC in my wallet and staked on ETH Mainnet both now and before snapshot block.

No article or info found on what's wrong anywhere.

Please share info with me.

-------------------------

shawn16400 | 2023-02-16 11:40:24 UTC | #7

Hi there @GordonDr 
You will need to delegate to yourself or to another address.  Here is a guide to help you - if you still have issues, reach out to me at shawn16400#5507 on discord. 
https://docs.google.com/presentation/d/1hwI0qhQUSiaZXGMcSsA5riZf1mV6PBFpcu6s0NS6FGA/edit?usp=sharing

-------------------------

lefterisjp | 2023-02-19 23:12:43 UTC | #8

Voted yes for this since if the actual amount requested is $290K as per the snapshot vote description this is good and the development of the product is the most important thing we need right now

-------------------------

shawn16400 | 2023-02-22 08:14:09 UTC | #9

This snapshot vote has passed with ~80% approval rate.
Metrics:
1162 unique votes
~10.3M GTC tokens cast.
Special thanks to the steward who volunteered to review:  @griff @azeem @farque65 @bobjiang and @annika 

https://snapshot.org/#/gitcoindao.eth/proposal/0x555f90d3c76bd44ee4727b627b424d524a799b8dde9784991848c90b599e6562

-------------------------
