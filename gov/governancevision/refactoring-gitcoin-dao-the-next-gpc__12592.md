---
id: 12592
title: "Refactoring Gitcoin DAO: The Next GPC"
slug: refactoring-gitcoin-dao-the-next-gpc
category: governancevision
url: https://gov.gitcoin.co/t/refactoring-gitcoin-dao-the-next-gpc/12592
created_at: 2023-01-18T09:06:11.192Z
last_posted_at: 2023-02-08T07:50:56.110Z
posts_count: 12
views: 3305
like_count: 40
---

# Refactoring Gitcoin DAO: The Next GPC

<https://gov.gitcoin.co/t/refactoring-gitcoin-dao-the-next-gpc/12592>
kevin.olsen | 2023-01-20 10:09:01 UTC | #1

*As part of the ongoing wave of strategy posts, I’ve opted to release a series of short posts with concrete recommendations I believe we should make to the workstreams in the GitcoinDAO. I see these proposals as refactorings - changes made to a system that keeps the public API (the essential intents / the DAO's contract with the outside world) of a system the same.* 

# The Next GPC: Gitcoin Grants Stack and Gitcoin Passport

## Tension:

GPC was set up as a functional silo: product, engineering, and design contributors in one workstream tasked to build all the DAO’s new products and maintain the legacy products. Our budgets and outcomes often drive goals across the DAO (evidenced in recent requests that GPC produces a budget that other workstreams respond to). But, it is this interdependence with other workstreams that makes determining GPC effectiveness difficult and, in turn, makes it difficult to hold the workstream accountable.

## Recommendation:

End the GPC, and split it into two independent budgeted workstreams. In addition to splitting the GPC, I would advocate that we make these end to end accountable as much as possible, bringing dedicated contributors into the workstream that were previously part of our cross-stream pod experiment.

* Gitcoin Grants Stack (estimated budget 300k / mo) WS Leads Nate and ½ Kevin
  * Combine the Product, Design, and Engineering teams from Round Manager (Grant Protocol) and Grant Hub (Project Protocol).
  * Continue to build the Grants Stack products, and the (newly named) Allo Protocol
  * Include dedicated part-time or full-time Marketing, DevRel, and Support contributors

* Gitcoin Passport (estimated budget 150k / mo) WS Leads Kyle and ½ Kevin
  * Encapsulate the Passport Pod into a single budgeted workstream
  * Keep the Product, Design, and Engineering team from Passport the same
  * Include dedicated part-time or full-time Marketing, DevRel, Support, and Data Science contributors

## Considerations:

* Maintaining high standards, best practices, and a common culture for the Product, Design, and Engineering disciplines that are now split between workstreams. 
*I would hope to see communities of practice grow up around each of our disciplines, spanning workstreams, and to continue a culture of inter-team rotation.*
* Maintaining high standards, context, and community for the non-GPC Marketing, DevRel, Data Scientists, and Support team members that will be joining these workstreams. 
*Similarly to the point above, I hope to see internal communities forming organically around disciplines, and that these communities foster the environment for the development and dissemination of best practices.*
* Partial allocations to workstreams - Workstreams may not require a full-time team member for a given specialization. 
*I believe it is the workstream’s choice to find the right resource to fill these roles and should have the option to work with existing DAO contributors (sourcing with WS/CSDO help) or to look outside the DAO.*
* Further refactorings. The Grants Stack and the Gitcoin Protocol (name TBD) may have diverging metrics/goals and be better served as two independent teams. 
*This is being discussed, and I could see a recommendation for further defining these teams as workstreams coming forward during 2023 as our protocol integration footprint grows.*
* Payroll and Operational complexity have been a source of pushback in the past from DAOOps to the creation of new workstreams. 
*I would first acknowledge that I hold the opinion that the value of independent, thin, and outcome-oriented workstreams will be a net benefit over any operational efficiency that monolithic workstreams claim in the current DAO structure.
Tactically, I believe that these new workstreams can solve this through part-time allocations of GPC’s existing operational roles.* 


## Conclusion:

We have a lot of moving pieces in the GPC, and our responsibilities and focus are to ship the Stack/Protocol/Passport projects for the alpha rounds and prepare for launch at ETHDenver. Given that, I would recommend we **do** move forward with splitting our workstream, implementing budgeting and payroll changes to establish two workstreams. But, we **do not** make any changes to the way contributors organize and work until after ETHDenver.

As a steward and a workstream lead, I believe this is safe enough to try, and propose we move forward with splitting the GPC in the next budget cycle for S17.

-------------------------

safder | 2023-01-19 00:32:58 UTC | #2

I'm generally fully in favour of thinner/more fluid workstreams and fractionalized roles spanning across workstreams. Loved the thinking around the Pods experiment and I think it's the right direction to be heading with workstream design as well. 

In practice, the operational complexity you've alluded to here feels like not a simple hurdle to cross. The main problem imo is that there are large variations in how workstreams operate - documentation, meetings, tools, workflow, compensation, etc. Currently, having a contributor contributing part-time to, say, MMM and part-time to 1-2 other workstreams isn't simply a matter of working with new teammates, but also context-switching in all these other areas. Working in MMM currently looks and feels nothing like working in GPC or any other workstream. How would you plan to reduce the friction this causes and ensure that this change makes contributors more, rather than less effective at their jobs? 

One potential solution is for the DAO Operations team to really be trusted to operationalize across the DAO, and develop consistency in operations. I think if we want thin workstreams to be successful where contributors are contributing to multiple workstreams, they need to have very similar OS's to minimize friction between them. In the past, this has been met with resistance due to the possible "centralization"/dependency to DAO Ops it could cause, which is why currently every workstream also has their own operational resources. While this works well with our current overly-independent work structure, I would suggest rethinking this if we were to move to thinner workstreams.  

Or alternatively, we move away from having a core-team of full-time contributors to more fractional/part-time roles. This is something I've brought up before [here in more detail](https://gitcoin.notion.site/web3-ifying-DAO-Hiring-4a5f8a736f144699b9c6cc7e60df4b6f) but would probably be a slow, long-term process with a number of other design challenges. No shortage of hard problems to solve haha.

-------------------------

CoachJonathan | 2023-01-19 14:24:33 UTC | #3

I'm generally in favour of this, though I think we'll want to discuss the logistics of this.

My experience of GPC is that they're focused on a having individuals fill "positions" whereas MMM has been working on filling "roles". Many members of our team have multiple roles, and the work we do and support each other with is quite fluid (and works very, very well imo).

One method is not better than the other, it is just different.

**Passport**

Having a FT marketing person (@garysheng) on the team has some implications.

A few considerations from my end:
- Though Passport execution is being led by Gary, there is a strategic component that involves other players on the MMM team that should be kept intact.
- Gary also supports MMM from a content strategy and ad-hoc perspective - ideally we would be able to keep this arrangement in place.

**Grants Stack**

We currently don't have 1 single individual assigned to this, and with limited functionality beyond running QF rounds (we can't currently serve a Direct Grants audience), I don't think we need 1 single person working on this at this point (in fact, I think it will be wasteful and detrimental to our overall marketing efforts).

***
My reco is that GPC proceed with this *without* a marketing function (maybe Passport only) and then we relook at this in S18 once Grants Stack (and our products in general) have matured more.

-------------------------

CoachJonathan | 2023-01-19 14:30:21 UTC | #4

Also, just noticed that your post is timing agnostic. My post above was assuming this would be enacted for S17. With more agnostic timing, we have much more flexibility in our discussion.

-------------------------

michaelgreen06 | 2023-01-19 19:28:32 UTC | #5

Thanks for writing this post @kevin.olsen ! I am generally in favor of this move to split GPC into two separate workstreams to gain the accountability benefits you mentioned.
 
I also agree w/ @safder that we should reconsider how we approach operations if we plan to have more thin workstreams as a DAO. This is something I [previously proposed](https://gov.gitcoin.co/t/discussion-gitcoin-2023-future-essential-intents-and-organization/12533/9) in @kyle's future essential intents & organization post. I see more disadvantages than advantages in having decentralized operations. Decentralization of certain things like holding power, is essential, but I don’t think we should decentralize everything w/o considering the pros and cons of doing so. If we centralize workstream operations to DAO Ops, or some other to be created workstream, a key feature needs to be the ability for workstreams to opt out of that structure if it doesn’t fit their needs. 

@safder also mentions another option for solving the operational challenge posed by having more thin workstreams.

[quote="safder, post:2, topic:12592"]
we move away from having a core-team of full-time contributors to more fractional/part-time roles
[/quote]

IMO, a both and approach, not one or the other, is the best way for us to evolve operations as a DAO. We need to have core teams working on hard problems and we need to continually experiment with having bounties/composable scopes of work (CSOW) to augment those teams and to solve one off problems. As @Viriya [mentions here](https://gov.gitcoin.co/t/discussion-gitcoin-2023-future-essential-intents-and-organization/12533/3) under the **Brand, Design & Creative section**, there are certain scenarios where a core team of contributors is very important and much more effective than taking the bounty/CSOW approach. I agree w/ @safder that the bounty/CSOW approach is full of challenges and think it will take a long time for us to perfect this approach. I believe we need to focus on streamlining operations in the thinner workstream paradigm while also running experiments in the bounty/CSOW approach so we can continuously improve at involving our community in the work we are doing. 

Finally, I want to call out that one big operational pain point, that is felt by all workstreams, will not be solved by any of these proposed operational changes. Seasonal budgeting is a very involved process that any workstream has to undertake regardless of how thin or fat it is. Thinner workstreams will likely be the most negatively impacted by the budgeting process, because a higher percentage of the workstream’s contributors will have to be dedicated to the process. Hopefully the [budgeting work](https://gov.gitcoin.co/t/proposal-gitcoin-dao-budgeting-process-redesign/12493) that is already happening can address this problem.

-------------------------

kevin.olsen | 2023-01-20 08:42:54 UTC | #6

First, thank you for your thoughtful comments.

@CoachJonathan I am actually advocating for making this change to GPC in the next budget cycle.  As for how the cross-workstream allocations work, I think this is real work this next season.

I'm seeing two tensions being expressed - increased ops overhead and contributor experience.

First, on ops overhead, what are we talking about here: 
1. financial - payroll and expenses
2. contributor experience - people ops (onboarding, benefits, career development)
3. workstream budgeting - reviewing past seasons, setting targets for next season, determining costs to achieve those targets, and constructing budgets.

I think for 1. and 3. in the case of GPC splitting, this is basically the same workload as before. I don't see much impact here for the WS Leads or the contributors. (thanks to @michaelgreen06 for being awesome at workstream ops), and the budgeting work is pretty aligned with our product road mapping work.

For 2. We are in the same boat as before for the core GPC contributors. I think we might actually be in a better position, as this creates some upward mobility as @nategosselin steps up into a WS lead role, and we could see the same for other GPC'ers as we continue refactoring our teams.

Where 2. get's tricky and where the real unresolved tension in the above comments comes in is what about the partial allocations? The folks that were in MMM, FDD, or Ops who would be a direct full or part-time member of Passport or Grants Stack? 

I think you have two ways of thinking about contributor experience in a thin workstream future version of our DAO:
1. Atomised individual contributors. Pretty purist freelancer view of labor.
2. Skill-based guilds. Re-orient the current workstreams as incubators or stores of context and talent for the work to be done in the DAO.

I think the tendency is to fall back to 1, it's in some ways the most familiar (outside of direct employment). But this is the precarious employment future I think most of us DON'T want - where everyone is a free agent, and everyone is spending half their time lining up their next job while executing on their current. 

I think a better construction for our DAO is 2. In some way, I hear @CoachJonathan 's comments around roles as MMM already functioning as 2. but instead of those roles being defined and owned by end-to-end accountable workstreams (like in my proposal) they are identified in consultation with the other workstreams, and are then prioritized and staffed internally to MMM. This feels like an agency model where MMM is 'hired' by all the workstreams to do their marketing.

Where these ideas meet is in letting the Passport and Grants Stack streams own the outcomes of these roles, and rely on MMM as a skill-based guild to staff and manage these specialist functions that are embedded in the outcome-oriented streams.

Where this all really comes together as a decision point: should Passport and Grants Stack budget for these roles (with MMM, Ops, etc staffing and cross-charging?), or should we continue with our normal cross-workstream collaboration as before and have MMM, Ops, etc. budget for all cross workstream needs of the to two new workstreams?

-------------------------

epowell101 | 2023-01-22 04:17:28 UTC | #7

A lot of good points made in the thread however -> the entire thread seems to be a bit insular - it’s mostly about what would be best for leading the workstreams and so forth.

For me the considerations though valid and well stated are mostly moot.

Perhaps what should be determinate is what will better fulfill our essential intents; to map back from those intents to the correct structure of the DAO we need alignment on strategy and positioning. As mentioned elsewhere - a strategy and positioning exercise may reveal that to best serve the needs of user segments we need to be more integrated - or less - and also could suggest the most natural business models for current and future users.  In short - we should think outside in, not vise versa.  

Secondly - just a reminder that no matter how we collectively decide to organize ourselves once hopefully we are really thinking outside in -> *it all comes down to people*. In the end all we are is a bunch of people that need a trusting, challenging, fun, rewarding environment to do our best.  Discussing how and when to change everyone’s work teams w/ immediate effect (season 17 starts in 11 days) feels like it could undermine our culture and lead to zero sum thinking and other reactions that occur when humans are under stress.  

I suggest that gitcoin does some collective sense making during s17 to arrive at a couple of potential reorg approaches.  Even if the work streams decide more or less to go their own way, to become even more autonomous, this transition will impact how gitcoin serves users and the work life of every contributor.  As such we may want to proceed carefully and as collaboratively as possible.

-------------------------

Vega | 2023-01-22 05:36:03 UTC | #8

[quote="epowell101, post:7, topic:12592"]
when humans are under stress.
[/quote]

GTC is at an all time low.  Stress is the right response to the current situation.

[quote="epowell101, post:7, topic:12592"]
Even if the work streams decide more or less to go their own way, to become even more autonomous,
[/quote]

This isn't up to the workstreams, is it?  It's up to governance.

[quote="epowell101, post:7, topic:12592"]
I suggest that gitcoin does some collective sense making during s17 to arrive at a couple of potential reorg approaches.
[/quote]

By "gitcoin does some collective sense making" do you mean insiders?    Or do you mean the governance process?  

Sorry insiders, but governance is where important decisions should be made.  So I'm in favor of having these proposals discussed in the open on the forums and voted on on snapshot.

-------------------------

kevin.olsen | 2023-01-22 13:39:46 UTC | #9

Thanks @epowell101 

I see a lot of parallel efforts to do precisely what you're recommending - re-mapping our EIs to structures, positioning our products, etc. I posted this assuming an awareness of that common background work, but I recognize that it's not explicit in this post.

Going back to the tension stated at the top of the post, the goal motivating this and other recommendations I'm putting forward is to create better control surfaces for the DAO to steer and hold the workstreams accountable. This is not in lieu of the strategic work that's happening, but in parallel to it. I'm focusing on one issue that has consistently been raised for the last four budget cycles: that workstreams are monolithic, opaque, and impossible to hold accountable through our current governance structures. 

I feel like your recommendations here are all kicking the can down the road. We've done this so many times now, we're overdue for doing the hard things. Making our workstreams legible, accountable, and governable should be our top priority as we go into the budget process, doing this during the budget process is far more painful from what I've seen.

-------------------------

epowell101 | 2023-01-23 15:22:47 UTC | #10

Thanks @Vega 

You are right, of course.  Strategic decisions should be up to governance.  I'm sorry if I implied otherwise.  

We should of course also keep in mind that the organizations and "workstreams" we discuss are just groups of people.  All (or at least most) of the value of the organization can choose not to log-on tomorrow and we won't have any more chess pieces to debate moving around.  So being cognizant of the impact of our debates on the Gitcoin contributors isn't IMO an example of insider self dealing - it's good sense as well as ethical.  

Just as an example - a few years ago we decided to spin out a part of the company I was leading at the time.  We did that in a way that gave the people involved at least 6 months of runway and a plan for their organization; part of that was due to ethical concerns and because we were teammates with those people, however a lot of it was based on the recognition that they all could go elsewhere and leave us with nothing of value.  Being a good place to work and contribute is also good business.  

IF we decide to spin out a workstream or split them - I would argue we should only do so if we can do so when that workstream has some plan and some funding or a split of the treasury or similar.  Right now Gitcoin itself isn't clear on it's positioning and potential revenue models - so it is unlikely that any workstream would have that sort of perspective though not impossible.

Nonetheless - I agree with the need for urgency.  I would be supportive of a date certain such as the end of the upcoming season by which time we would have multiple scenarios to vote on.  Top of mind these might include (and a [MECE](https://en.wikipedia.org/wiki/MECE_principle) approach may be called for here):
- big bang - every workstream goes largely its own way, they are supplied w/ for example 6 months of funding, and have a standard separation path; I think @griff has suggested as much in a prior post (I may not be remembering correctly)  
- status quo improved - with a unified revenue plan - the workstreams align around a set of offerings and that plan includes a path to sustainability
- 1-2 mixed scenarios - perhaps the split of GPC, the launch of a commercial entity by or with FDD and perhaps others, or something similar

All of these scenarios can be grounded by a view into how best to serve the stakeholders - the so-called triple sided market that has been discussed elsewhere, comprised of grant operators, donors, and gratnees.

-------------------------

kyle | 2023-02-01 17:04:00 UTC | #11

I appreciate the comments and feedback on the thinking here.

We are moving forward with splitting the workstream into two workstreams. We look forward to the review and support on those two budgets.

-------------------------

griff | 2023-02-08 08:09:03 UTC | #12

I think building teams around products as opposed to around job descriptions is a WAY better dynamic.

I would also like to see elections for Product Owners/Product direction on a regular basis, not just budget, but direction + budget. One of the options could be "wind down this work stream"

FDD did some of this work in season 14 or 15 i think... that was a lot better then the current system where voting no almost doesnt make sense...

Going full product focused work streams and then making sure that the comms, ops & admin people from each group are either the same people or are working closely together. would give a lot of benefits IMO.

I would be cool with some one off projects too: Gitcoin Rebrand, Token Utility projects, etc... but these things should be one offs and probably be coordinated by an elected product work stream leader.

Random thought here... not attached to this as a final outcome, but it does seem like this forum post could take the DAO this direction, and I would love to see that!

-------------------------
