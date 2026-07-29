---
id: 12739
title: "[S17 Proposal] DRAFT Gitcoin Allo Budget Request"
slug: s17-proposal-draft-gitcoin-allo-budget-request
category: governance-proposals
url: https://gov.gitcoin.co/t/s17-proposal-draft-gitcoin-allo-budget-request/12739
created_at: 2023-01-31T20:00:36.945Z
last_posted_at: 2023-02-17T21:46:47.296Z
posts_count: 12
views: 2929
like_count: 30
---

# [S17 Proposal] DRAFT Gitcoin Allo Budget Request

<https://gov.gitcoin.co/t/s17-proposal-draft-gitcoin-allo-budget-request/12739>
nategosselin | 2023-01-31 20:00:37 UTC | #1

# Allo Protocol S17 Workstream Budget Proposal
During Season 17, the GPC workstream (Gitcoin Product Collective) has decided to split into two workstreams: **Gitcoin Allo** which is focused on the continued development of our Grants protocol and stack, and **[Gitcoin Passport](https://gov.gitcoin.co/t/s17-proposal-draft-gitcoin-passport-budget-request/12727)** which is focused on our Passport protocol and stack. Splitting GPC into two workstreams will allow for a more “complete” team structure in the future.  This will allow for a more "complete" team structure in the future. @nategosselin and @kevin.olsen will be workstream leads for this workstream (h/t to @kyle for his assistance getting this initial draft up and running).

## Essential Intents

We are focused on a number of the Essential Intents. Specifically the following two:
1) Protocol Adoption + Growth
2) Financial Sustainability


## TL;DR

This season the Allo workstream will be focused on transitioning from alpha to beta, with Eth Denver as a key milestone and inflection point. At a high level, we will be focused on three key themes:

1) **Finish Protocol v0** — finalize the payouts interface and build our first payout mechanism so that there is an end-to-end protocol flow
2) **Engage the developer community** — with the foundational protocol complete, we will ramp up our DevRel efforts and work on getting external teams building on Allo
3) **Productize QF on Grants Stack** — Enabling communities to run Quadratic Funding rounds is a major opportunity for protocol adoption and growth. We want to make running QF rounds to be truly self-serve for non-technical operators on Grants Strack. We received great feedback during our alpha rounds and will continue building solutions to that feedback this season. 

Based on what we learned in Season 16, we recognize the need to continue being nimble with our development roadmap so that we can quickly adapt to the needs of the market. This season's roadmap will likely change month-to-month as we get feedback, so our objectives read more as high-priority user needs than concrete features.


> 💡For more context regarding our vision, the current state of the workstream and more please refer to the [📄Workstream Notion Page](https://www.notion.so/gitcoin/Grants-Protocol-Round-Manager-b650b50c91d14e43adacae14f3f2bd53). This page has not been updated to reflect the new workstream structure at time of writing, but you can find details on our vision and what we are building towards. 

## Amount

Gitcoin Allo (GA) is requesting **$803,533** for S17. A breakdown of the budget can be found at the end.

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
As mentioned above, we are tracking three key themes for Season 17. Given the need to be nimble, we will primarily use a monthly roadmap for how we translate those themes into development work. In February we are focusing on three high-priority needs for launch (payouts, repo refactor, and application flow improvements). We will share an updated Season 17 roadmap in the coming weeks and update it on a monthly cadence as our plans crystallize.

*Note: at this stage of development we have yet to establish baseline metrics for our products. We plan to establish our core metric portfolio and begin measuring baselines this season. Our goal is to transition to metrics-lead objectives in future seasons. For now, we have left metrics blank and instead focused on likely focus areas.*


## List of S17 OKRs

|Initiative/Project|Layer|Metrics|Likely Efforts|
|---|---|---|---|
|**Finish Protocol v0**<br>Complete the payouts interface so that end-to-end funding programs can run on Allo Protocol.|Protocol|- |- Finalize payouts interface<br> - Build bulk payout mechanism
|**Engage the developer community**<br>Ramp up our DevRel efforts to begin getting developers building on the protocol.|Protocol|- |- Refactor repos into easy-to-use Allo repo<br>- Improve Documentation, Legibility, DX<br> - Partnership and Project Incubation (likely focused on allocation mechanisms + payouts)
|**Productize QF on Grants Stack**<br>Enabling communities to run QF rounds is a major adoption and growth opportunity for our products. We want to remain laser-focused on the feedback we heard during the Alpha rounds and build a first-class QF grants exerpeince. |Stack + Protocol|- |- General iteration on Alpha round feedback<br>- Improve Application experience for Operators + Grantees<br> - Improve project review flow for Operators<br>- Improve and enrich the explorer experience for donors<br>- Enable new verified credentials so that projects can accrue reputation (including KYC)



## Budget Breakdown
We have broken the budget down by staffing, contracting, devrel, opex as we feel like this gives fairly granular details into where the funding will be going. 

### View: USD per Category

|Gitcoin Allo denoted in USD||||||
|---|---|---|---|---|---|
|Staffing||**2023.02**|**2023.03**|**2023.04**|**S17 Total**|
||Core Contributors|181,201|180,868|180,868|542,937|
||Leadership / Ops|34,865|34,865|34,865|104,596|
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
|S16 Treasury Balance|||||645,628|
|**Total S17 Request**|||||**693,540**|

-------------------------

shawn16400 | 2023-02-01 09:57:37 UTC | #2

Heads up @griff  @azeem @farque65 @bobjiang and @annika 
This is the second budget to review from GPC.

-------------------------

michaelgreen06 | 2023-02-06 18:07:08 UTC | #3

Looks good. I'm eager to see the allo team make progress on all of these items in S17

-------------------------

bobjiang | 2023-02-08 00:52:17 UTC | #4

Excellent job, Nate!

Firstly I support GA budget request, some questions - 

would we keep the team size or grow in next season?
would we list the team size currently (FT and PT)?
if possible, list the contributors' name like GPC did.

so as a steward I would know that we have xx team members, and we have a goal/vision for next season, and then we would achieve it or partially achieve it with the team.

Actually the basis idea is, as a steward, I would know more details about team. (this is a black box for me now)

from the vision and product view, it's very clear.

-------------------------

lefterisjp | 2023-02-08 11:00:59 UTC | #5

Hey guys. For this gitcoin budget season I will be following a different approach. I am not happy with how many things have been going in gitcoin and the way budget reviews work so I will either be abstaining or voting No in most budget reviews.

Despite the budget cuts I still think the DAO is burning too much money and it needs to become more lean.

-------------------------

griff | 2023-02-08 21:31:51 UTC | #6

I am not excited about such a huge spend on passport and Allo this quarter, would prefer a slower ramp up of the reserves.


That said I’m, in general, supportive of this proposal, but I want to ask every workstream… what would happen if this proposal didn’t pass?

Not fear mongering, just a practical reality. This post clearly explains what “yes” looks like… What would “No” look like?

-------------------------

kevin.olsen | 2023-02-09 17:27:53 UTC | #7

Thanks Griff. 

[quote="griff, post:6, topic:12739"]
I am not excited about such a huge spend on passport and Allo this quarter, would prefer a slower ramp up of the reserves.
[/quote]

The Allo budget carries over the GPC Reserves which are in excess of the standard 60 day request, you'll see the total S17 request is less than the total budgeted spend as a result.

[quote="griff, post:6, topic:12739"]
That said I’m, in general, supportive of this proposal, but I want to ask every workstream… what would happen if this proposal didn’t pass?
[/quote]

I just responded on the Passport budget, but somewhat similar outlook here on the Allo side.

In the scenario where Passport is funded, and Allo is not, Allo would have 80% of the season funded from reserves. The choice would be to reduce spending by 20% to survive until S18 and put up another budget or spin down the workstream. It would be essential to receive direction from the Stewards and the rest of the DAO regarding the preferred path.

As in my hypothetical that I explored in my response on the passport budget: if neither budget passes, we would be required to spin down the work pretty quickly. The DAO would need to help produce a contingency plan for this, either sourcing a small team for maintenance and operations, rebuilding a team for in-house development, or finding a new home for the products outside the DAO.

Thanks for exploring the tougher topics here, and I hope that helps.

-------------------------

kyle | 2023-02-10 17:05:40 UTC | #8

I thought I would chime in with support of the budget here. There are five distinct products being built by this team (Explorer, Manager, Builder, Allo and Project protocol) so the team size seems appropriate given the initiatives scale. I will be voting yes to this one.

-------------------------

DisruptionJoe | 2023-02-10 18:44:27 UTC | #9

I am voting yes to this budget. Allo & Grantstack products are the most important work we have. I would hope all stewards know this as well. Even when we need to pull in the reigns on some of the "nice to have" work, this work needs to be funded for there to be a Gitcoin.

-------------------------

annika | 2023-02-11 03:07:27 UTC | #10

I echo @kyle's comments -- to me, this is actually the most reasonable of all the budget requests this season.

As with all workstreams, I think we should continue to seek opportunities for cost-cutting but given the scope of this team & the fact that it's all mission-critical work, I am supportive of the budget as described and will vote yes.

-------------------------

linda | 2023-02-16 23:16:48 UTC | #11

I voted yes on this proposal given the assigned steward reviews and that this work is a core focus of the DAO.

-------------------------

michaelgreen06 | 2023-02-17 21:46:47 UTC | #12

I am sharing a quick note about Allo’s S16 reserves here for full transparency so anyone can reference it in the future if it’s helpful. In our original S17 budget request (this request) we cited having $645,628 in reserves. When the S17 budget request went to snapshot we cited having $1,049,168 in reserves. As mentioned in our snapshot summary, the extra reserves are due to price increases from when the S16 budget was issued, absorbing the Moonshot Collective treasury, and strong diversification in S16.

The main reason we didn’t catch the discrepancy in our actual reserves amount when posting our initial S17 budget request was because a large amount of our reserves were held in the foundation’s coinbase (CB) account at the time. We partner with the foundation to diversify our GTC into USDC to pay contributors primarily in USDC. We realized we forgot to include these funds held on CB when the foundation sent us all of our diversified funds when clearing our trading balance for S16.

Another reason we have more reserves than expected is when we requested our S16 budget we assumed that we would have $0 in reserves from S15 due to the falling price of GTC at the time. When our S15 budget was issued we actually had ~$86.5k in USDC and 16k in GTC. Due to an oversight on our end we failed to update our budget request when it went to tally to reflect these reserves. This resulted in our workstream getting slightly overfunded for S16. I apologize for this oversight in calculating our S15 & S16 reserve amounts.

-------------------------
