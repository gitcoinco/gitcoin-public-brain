---
id: 11704
title: "Streamlining Budgeting with Utopia"
slug: streamlining-budgeting-with-utopia
category: partnerships
url: https://gov.gitcoin.co/t/streamlining-budgeting-with-utopia/11704
created_at: 2022-10-20T15:39:27.123Z
last_posted_at: 2022-11-16T18:53:09.963Z
posts_count: 4
views: 3202
like_count: 13
---

# Streamlining Budgeting with Utopia

<https://gov.gitcoin.co/t/streamlining-budgeting-with-utopia/11704>
scatterbrained | 2022-10-20 15:45:00 UTC | #1

**Hello from Utopia**
Hey Gitcoin, Utopia Labs’ Product team here! 👋 For those we haven’t met yet, we are a startup focused on enabling operational excellence for DAOs. We've been working with many of you to help streamline contributor payments and multi-sig management, and today we want to explore how we might also support Gitcoin’s seasonal budgeting process.

**Context:**
Many DAOs have been exploring budgeting as a means of scaling operations while maintaining decentralization. We believe Gitcoin is one of the furthest along in defining exactly what that process can look like, though we also think there may be an opportunity to help streamline that experience and relieve some of the manual work involved.

In this post, we want to share our understanding of the budget approval process and explore some ideas for how we might streamline a few aspects of it. We'd love community feedback, especially as it pertains to a couple questions:

1. What do you think is working well?
2. What have we failed to consider or misunderstood?

---

**Our Understanding:**
The Gitcoin forums have helped us develop an understanding of the budgeting process, in particular the [Workstream Accountability Flow](https://gov.gitcoin.co/t/gitcoin-dao-workstream-accountability-flow/9644) and [Budgeting Proposal Process v2](https://gov.gitcoin.co/t/budget-proposal-process-for-gitcoin-dao-v2/11168) posts. We’ve begun to think of a "budget lifecycle" as encompassing four general phases: planning, approval, execution, and evaluation.

![|602x25](upload://k9GnrxiqNq3H1aa1MJpQemW2RJ.png)

1. Planning Phase – New budget proposals are informally debated, per the DRAFT and INTEGRATED stages of the proposal process.
2. Approval Phase – Budget proposals are moved to Snapshot and Tally, and ultimately approved or denied. Budgets in the ACTIVE, RATIFIED, and DENIED stages map to this phase of the larger budgeting process.
3. Execution Phase – Where budgets live upon funding. This is when workstreams are actively spending against their budget, which includes work required to categorize spend against budget items.
4. Evaluation Phase – Finally, at the end of the season, budgets and milestones are reviewed.

The phases above take place across various surfaces and involve a range of tools such as Discord, Snapshot, Tally, Gnosis, Utopia, Google Sheets, etc.

**A Potential Solution:**
We believe the process can be streamlined by creating a live representation of a budget that reflects its health and status at all phases of the lifecycle. We’ll use [Moonshot Collective’s S14 Budget Request](https://gov.gitcoin.co/t/s14-proposal-amended-moonshot-collective-budget-request/10446) to demonstrate what this could look like:

*Planning: Drafting the Budget*
First, workstream operators can draft their budget proposal in Utopia and use our custom categories to outline individual budget items. If a budget is approved, we’ll automatically track spending against those categories to monitor budget health—more on that later.

![|602x428](upload://dVOL0XybdKlz4nAAfELeEuPzy1.jpeg)

Here’s what Moonshot Collective’s initial S14 budget could look like in Utopia:

![|602x428](upload://xVAbT2efciqR2LohW3GI6leRXM3.jpeg)
Once this draft has been created, we imagine it could be embedded or shared as a live preview anywhere the budget needs to be discussed. As the budget changes during planning, the live preview could automatically update to reflect the most recent proposal.

![|602x429](upload://x1sQjwye1O3LCmrwPG0p1IBjSLY.jpeg)

*Approval: Funding the Budget*
Once a budget has been approved through governance, a workstream operator can “Request Funds” from the DAO Ops Safe. We imagine a future where funds might be requested from any safe, but for now we’ll assume the DAO Ops Safe is funding all workstream budgets.

![|602x428](upload://cBBq19NMq9tTeRKHCOfhE5O2OcZ.jpeg)![|602x428](upload://90J4RXUwv1JIE7q6nhf8Hz2T5nZ.jpeg)
Now let’s switch to the DAO Ops Safe Utopia account, where we can see this budget funding request alongside S14 requests from other workstreams.

![|602x428](upload://tb2IkmbmvdtfhZ650yY8UeRdE7u.png)

Since this budget has passed the Snapshot governance vote, we’ll go ahead and create a transaction to fund the budget from the Dao Ops Safe.

![|602x428](upload://mXdJthtGqXRJn42sZ7hSIPKcGsk.jpeg)

*Execution: Spending the Budget*
If we switch back to the Moonshot Collective Safe, we can see that this budget was successfully funded. We’re now in the execution stage of the budget.

S14 has begun, and the workstream is executing its objectives and spending funds as necessary.

![|602x428](upload://ewR7oqm4Gz5AZdsj17VLrkoRwxr.png)

When workstream members create new payments in the Moonshot Collective Safe, they are prompted to categorize those payments. Note that these categories are the same ones we used to define our budget items, enabling us to seamlessly track real-time spend against each budget category.

![|602x428](upload://5ni6AJNAREct0rVGFZrSKRyHXqm.jpeg)

Because this budget is now live, Moonshot Collective members can track the budget health in real-time from their payments page in Utopia. This is an easy way to understand how we’ve spent the budget and if we’re at risk of going over-budget in any given category. In the example below, we’re over-budget in the OP Partnership Initiative budget item.

![|602x428](upload://jxCDwtigSiig8nZYqktrV4jqJhz.jpeg)

*Evaluation: Monitoring the Budget*
But wait, there’s more. Because the DAO Ops workstream funded this budget from their Utopia account, they’re also able to monitor the health of the budget from their account in real-time. Their Budgets page in Utopia becomes an easy way to monitor real-time budget health of all workstreams, as determined by the payment categories used in those workstreams.

![|602x428](upload://w4kcfStjPxSsjAIpSsbF8aOfswt.jpeg)

From here, there’s a ton of data visualization we can do to help you draw insights about budget spend. Budget forecasting and variance analysis would be relatively easy to report in real-time. At Utopia, we are passionate about treasury transparency and community accountability and we see this as a step forward in making it easy for DAO members to understand how the treasury is being spent in real-time.

---

**Next Steps**

Right now, this work is purely conceptual, and we’re looking for feedback from Gitcoin and others on whether productizing the budget process like this would be valuable. As far as we can tell, this process is already happening manually in spreadsheets, and our hope is to streamline the process and reduce the administrative burden on operators.

We'd love to get a conversation going here to help inform our thinking. What about this is working well? What have we failed to consider or misunderstood?

-------------------------

DisruptionJoe | 2022-10-21 12:52:56 UTC | #2

Very well written and helpful post. Thank you for taking the time to share this.

-------------------------

krrisis | 2022-11-16 14:19:11 UTC | #3

Hey, thank you so much for sharing your thoughts here on how Utopia could help make our lives easier! Apologies for the late reply, some thoughts while reading this through again, as we are now - post budgeting for S16 looking into reporting solutions. 

[quote="scatterbrained, post:1, topic:11704"]
The Gitcoin forums have helped us develop an understanding of the budgeting process, in particular the [Workstream Accountability Flow ](https://gov.gitcoin.co/t/gitcoin-dao-workstream-accountability-flow/9644) and [Budgeting Proposal Process v2 ](https://gov.gitcoin.co/t/budget-proposal-process-for-gitcoin-dao-v2/11168) posts. We’ve begun to think of a “budget lifecycle” as encompassing four general phases: planning, approval, execution, and evaluation.
[/quote]

This is indeed how we do this, although we do not spend enough time as a team on evaluation and reporting of past budget spent, and we'd like to improve here in the future.  Some thoughts on where I think you could help out in our process: 

**Planning:** 
I think we will not immediately move away from the planning phase outside of Google docs, because we have a lot of back and forths on these between workstreams and with Stewards. Updating an embedded budget live during planning is a nice to have, but as it lives on the forum and amounts are referenced elsewhere, this could cause more confusion than really bring useful solutions. 

**Approval:** 
This would add another step in our process (as we now send funds directly via Tally to the workstreams' multisig), so not sure if this is an improvement. 
But I do see the added value in being able to have a unified overview on spending. I wonder if this could be simplified by just having one Utopia account that can get 'view only' access to all of the details of spending of the various other multisigs for evaluation? 

**Execution**: 
No doubts here, this is super valuable for us. 

**Evaluation**: 
See above, this is really useful. Note, this would indeed be people in the DAO Ops workstream focusing on this but we might do this from a separate CSDO/DAO Ops accounting dashboard, which we'd like to make available cross-workstream, and potentially even to other whitelisted addresses (=our stewards), for increased transparency. We'd give it a separate name to avoid confusion, in the sense that DAO Ops also has its own budget. 

We could probably use a number of other visualizations here, on eg how much is spent on expenses vs contributors, how much vs previous season on that budget line (if existing) etc etc. 

These are just some thoughts that pop up, but to be discussed further, looking into solutions for deeper reporting solutions with my colleagues @shawn16400 & @Jodi_GitcoinDAO at the moment, so this post is super timely and very much appreciated!

One extra Q, what would be the timing to develop such dashboards? Would this be a heavy lift? (especially knowing we probably only need part of the suggestions offered here at this moment)

-------------------------

Jodi_GitcoinDAO | 2022-11-16 18:53:09 UTC | #4

[quote="krrisis, post:3, topic:11704"]
One extra Q, what would be the timing to develop such dashboards? Would this be a heavy lift? (especially knowing we probably only need part of the suggestions offered here at this moment)
[/quote]

There isn't a timeline. Utopia's offer is to design a solution with us as partners. I can loop you with Josiah and catch you up on our last converation.

-------------------------
