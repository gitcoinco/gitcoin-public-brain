---
id: 12612
title: "Refactoring Gitcoin DAO: Evolving the FDD"
slug: refactoring-gitcoin-dao-evolving-the-fdd
category: governancevision
url: https://gov.gitcoin.co/t/refactoring-gitcoin-dao-evolving-the-fdd/12612
created_at: 2023-01-20T11:35:32.380Z
last_posted_at: 2023-01-26T15:25:49.042Z
posts_count: 16
views: 5655
like_count: 45
---

# Refactoring Gitcoin DAO: Evolving the FDD

<https://gov.gitcoin.co/t/refactoring-gitcoin-dao-evolving-the-fdd/12612>
kevin.olsen | 2023-01-21 12:29:43 UTC | #1

*Continuing my series of posts, I’m going to take a risk and make a recommendation about restructuring a workstream that I do not run. I want to preface this with the statement that I love the contributors in these workstreams and think they are all amazing people. I worry very much about upsetting my peers in the DAO. I especially worry that my comments may create a sense of precarity for contributors in any of our workstreams. Still, I feel this conversation belongs in the forum, and I hope we can move through the tension to arrive at the best results for the DAO, the contributors in our workstreams, and our community*

# What comes after the FDD?

## Tension:

As it stands today, most of the FDD's historical operational responsibilities have moved into other workstreams or product teams:

* Grant Reviews by the FDD have ended entirely with the move to the protocols. These responsibilities lie with operational roles in the Grants Programs, aided by continuous improvements to the products in the Grants Stack.
* Sybil Hunting is no longer a contributor activity but programmatic, replaced by iterative improvements to Passport in collaboration with Data Science.

Reviewing the S16 budget for FDD: https://gov.gitcoin.co/t/s16-proposal-integrated-fdd-budget-request/11890 I see the following tensions around the FDD's current areas of work:
* Sybil Legos is still more concept than product IMO. The FDD has **not** demonstrated it can ship production software products (going back to the SAD pipelines and the Matrix efforts of past seasons). I believe this effort continues the pattern of the FDD incubating projects that are not likely to run in production or achieve product market fit.
* ODC is the future of what the FDD should be. Still, it is a relatively new concept that was incubated inside the workstream, and its goals, value, and accountabilities to the DAO are opaque.
* There has been some discussion of analysis services provided by the FDD or even a spin-out. I'm unclear if this is an ODC offering or what entity would be accountable for this.
* @DisruptionJoe 's recent engagement with the topic of workstream revenue, or profitable workstreams, demonstrates a significant divergence from the standard operating model of workstreams as cooperative budgeted teams that seek to achieve the DAO's EIs.

## Recommendation:

* End the FDD workstream, do not post a budget for the FDD in S17
* Create an ODC workstream with its own budget.
* The Sybil Analysis spin-out is broken out for further incubation as its own workstream OR Data science and Sybil Analysis move into the Passport 'customer' workstream and iterate within the context of a product delivery organization.
* Pause Sybil Legos until there is Product/Engineering leadership with a proven track record of delivering production software that can produce a project plan and budget that the DAO can review and approve.
* FDD contributors take some time to build a proposal for an investment and governance process (independently of the existing workstream process) that can be ratified and used to fund investable spin-out workstreams. @DisruptionJoe 's thoughts on this topic are in this recent comment: https://gov.gitcoin.co/t/discussion-gitcoin-2023-future-essential-intents-and-organization/12533/6 (corrected per Joe's response)

## Considerations:

* Given the urgency to launch our products and ensure their legitimacy in the market, is there a risk in ending the FDD WS? *In my opinion, no. The FDD is not operationally responsible for Fraud Detection and Defence at this point in time. There are analytics needs in products like Passport or the Grants Stack, and I would recommend staffing data science in those teams.*
* Sybil Legos sounds like a good idea. Where does this work go? *TBD, I am unconvinced that this project will achieve a production release. I think this effort needs to be re-evaluated outside of the FDD workstream umbrella and see if the DAO believes this effort should continue to consume resources or not.*
* Investible workstreams make sense. Let’s do that. *Agreed. Sounds super cool. But there’s no process for that, and this needs some dedicated effort to hammer out a process in collaboration with DAOOps and governance.*
* We don't have enough time to make this change. *The Research and Strategy line items in the FDD S16 budget would indicate to me the ODC, the Revenue, and Spinout ideas should be fairly evolved, and the FDD may be in a spot to implement these changes now. Either way, we cannot keep funding workstreams because of our inability to improve our budgeting process.*

## Conclusion:

FDD as a workstream has run its course, the original responsibilities have diffused through the DAO, and the day-to-day work belongs in new or different parts of the organization. I believe the ODC exemplifies the subtraction mindset and community building we want to take as a DAO, and I'm super supportive of this direction.

As a steward, I would support budgets for independent and accountable workstreams representing the current focus areas within the FDD (even one-off direct grants to accomplish a particular goal). I will not vote to fund another season of the FDD as it is currently organized.

-------------------------

DisruptionJoe | 2023-01-22 15:46:27 UTC | #2

[quote="kevin.olsen, post:1, topic:12612"]
I especially worry that my comments may create a sense of precarity for contributors in any of our workstreams. Still, I feel this conversation belongs in the forum, and I hope we can move through the tension to arrive at the best results for the DAO, the contributors in our workstreams, and our community
[/quote]

It does seem like this could be a tension you would bring up, discuss with or otherwise confront at some level prior to posting here. It is quite a shock to see you advocating for laying-off 10 people in 10 days. This doesn't present any consideration for the psychological safety of contributors in or out of FDD. 

[quote="kevin.olsen, post:1, topic:12612"]
Sybil Hunting is no longer a contributor activity but programmatic, replaced by iterative improvements to Passport in collaboration with Data Science.
[/quote]

## Iterative improvements to passport with data science is what FDD is currently doing.
We haven't done one test looking at the results of Passport Scoring as a Service (PSaaS) effectiveness during the Gitcoin Alpha round, the first round to use it.  PSaaS is an algorithm custom designed by FDD this season. We gave 3 other options including a cost of forgery model. The plan which we very clearly articulated at the beginning of the season is that a "one-score-to-rule-them-all" model could be iterated on over multiple uses, but by no means would be perfect from the start!

You get the benefit of talking with one analyst or data scientist from our team and assuming that they are doing all the work of FDD. Our team doesn't work this way. Most efforts of any single contributor are supported by others on the team. 

I personally recommended that you hire a data scientist onto the passport team to help transition both the Passport team and FDD to a post protocol launch future. We discussed this a few days ago. 

## The idea that there isn't a need for sybil defense is a mistake.
GPC informed us that there would be no need for our sybil defense work for the Unicef, Fantom, and Gitcoin Alpha round. I am not sure why they insisted this, but luckily we still performed these checks (as is our mandate) and uncovered substantial fraud in the Fantom round. Some of the same wallets which attacked the Fantom round are ALREADY attacking the main round. 

Our analysis of GR15 clearly showed that passport alone is NOT ready to be the only method for sybil defense. 

## There are ethical tradeoffs to using preventative vs reactive sybil mitigation techniques and for the protocol to be unopinionated we will need to offer both. 
For those who are not aware, both preventative (passport gating/weighting) and reactive (squelching - giving a user a 0 coefficient based on in round behavior) have ethical tradeoffs. 

Gating over multiple instances compound inequality building a privileged class. This is the fundamental problem with moving to meritocracy in a system where the players do not start at equal levels. Additionally, it leaves little room for new users to participate. 

Squelching is like removing ballots after the person voted. However, it opens the aperture for participation that is innocent until proven guilty. It would be quite assumptive of us to assume preventative sybil defense is the only ethical option when it is KNOWN to cause systemic problems. 

Are we sure we want to make the protocol opinionated in a way that seems more ethical today (not removing votes already cast) in favor of creating systemic inequality in the democratic fund distribution of public goods in web 3? Especially when the FDD answer is to instead provide transparency and reproducibility to any algorithms used for removing votes in a reactive way?

 

[quote="kevin.olsen, post:1, topic:12612"]
Sybil Legos is still more concept than product IMO. The FDD has **not** demonstrated it can ship production software products (going back to the SAD pipelines and the Matrix efforts of past seasons). I believe this effort continues the pattern of the FDD incubating projects that are not likely to run in production or achieve product market fit.
[/quote]

This is said as though you have a clear solution for solving sybil defense. As for the two items that you bring up:

SAD model - This was still in use in GR15. Instead of it being the ONLY model used to predict how likely an account is sybil, we instead made it one of multiple models. We did this because the SAD model was great when there were primarly web 3 devs supporting open source. When the cause rounds like Climate Change started, we suddenly saw a new wave of donors without a Github. 

Discovering new behaviors is part of the fraud detection effort. it is an iterative game. As old signals are deprecated, we find and validate new signals like the [onchain intersectionality](https://github.com/Fraud-Detection-and-Defense/onchain-trustscore-analysis) report. 

Matrix was an interesting case where we had an idea that would have massively helped the DAO at the point we are now imho. However, FDD was voted not to work on this and the contributor who intended to work on this moved on. It wasn't unreasonable to think we could build this simulation engine as here is one for [reward modeling for grant reviewers](https://github.com/Fraud-Detection-and-Defense/rewards-system-model). 

The problem we are supposed to solve is sybil defense. We are not shipping production software because it is an unsolved research problem. We need a solution prior to shipping software. The sybil scoring legos are an attempt to ship an MVP that pulls these past learnings together. 

1 - Crowdsourcing analysis is more efficient
2 - Contributors need a way to build on each others success and not "reinvent the wheel" every time a new analysts participates
3 - The scoring application needs a standardized format which can continually be updated with new analysis based on new behaviors to empower non-technical users

Lastly, I'll remind everyone that when the DAO started we were excited about being open and letting anyone participate. The goal for workstreams was not that we should be as efficient as possible and exceed our goals. We hoped this would happen, but at the time it was more important to be open to participation and still hit objectives. We did this. When the bear hit, the DAO took a transformational turn and we followed suit. 

[quote="kevin.olsen, post:1, topic:12612"]
ODC is the future of what the FDD should be. Still, it is a relatively new concept that was incubated inside the workstream, and its goals, value, and accountabilities to the DAO are opaque.
[/quote]

Mostly agree, but we aren't there yet. The bounties that FDD included in the hackathon needed to be created. The ODC can continue exploratory analysis to find new detection methods, but FDD will need to productize them to be used by program managers. 

Here is an early breakdown of how we might [split responsibilities between ODC & FDD](https://github.com/OpenDataforWeb3/Resources/wiki/Some-thoughts-about-ODC-&-FDD-(Gitcoin)-activities). 

[quote="kevin.olsen, post:1, topic:12612"]
There has been some discussion of analysis services provided by the FDD or even a spin-out. I’m unclear if this is an ODC offering or what entity would be accountable for this.
[/quote]

It is exactly that, a discussion. That discussion would be much better to have without the overtone of "I think we should fire this workstream". 

[quote="kevin.olsen, post:1, topic:12612"]
@DisruptionJoe 's recent engagement with the topic of workstream revenue, or profitable workstreams, demonstrates a significant divergence from the standard operating model of workstreams as cooperative budgeted teams that seek to achieve the DAO’s EIs.
[/quote]

Stewards are asking about sustainability. My response is to DISCUSS potential ideas. It seems that your understanding is that if people bring up discussions that you (or maybe your perception of the current DAO zeitgeist?) don't agree with, that is counter-productive to achieving our EIs? I don't think it is a good idea to set a precedent that we should defund any workstream that dares to have independent thoughts. 

To this logic, I think your post advocating for firing 10 people in another workstream 10 days from now demonstrates a significant divergence from the standard operating model of workstreams as cooperative budgeted teams that seek to achieve the DAO’s EIs - HOWEVER - I do not think we should defund your workstream. 

[quote="kevin.olsen, post:1, topic:12612"]
End the FDD workstream, do not post a budget for the FDD in S17
[/quote]

This is not going to happen. You are welcome to not vote for our budget. 

[quote="kevin.olsen, post:1, topic:12612"]
Create an ODC workstream with its own budget.
[/quote]

I would love to do this! It was my understanding that spinning out workstreams was seen as potential defection...

[quote="kevin.olsen, post:1, topic:12612"]
The Sybil Analysis spin-out is broken out for further incubation as its own workstream OR Data science and Sybil Analysis move into the Passport ‘customer’ workstream and iterate within the context of a product delivery organization.
[/quote]

As mentioned above, I do think Passport could potentially benefit from having a data scientist on their core team. I do not think that it makes sense to lose the FDD support for this person AT THIS TIME. 

Also, who is dynamically monitoring grant behavior for fraudulent actions if we move the data science and analysis into the Passport working group? 

We know sybil resistance needs more than just the preventative model offered by the passport. Your suggestion here is that although we have the agreement of multiple data analysts, data scientists, and also math, you still think that Passport alone is the answer. How do you resolve the ethical dilemma of bias compounding over time to create a privileged class? 

[quote="kevin.olsen, post:1, topic:12612"]
Pause Sybil Legos until there is Product/Engineering leadership with a proven track record of delivering production software that can produce a project plan and budget that the DAO can review and approve.
[/quote]

Why wouldn't we finish validating our prototypes to be used by an FDD Fraud Consultant and a PGF Round Operator during the beta rounds in April. Then, we might discuss moving the prototypes to the next phase of delivering production ready software. 

[quote="kevin.olsen, post:1, topic:12612"]
FDD contributors take some time to build a proposal for an investment and governance process (independently of the existing workstream process) that can be ratified and used to fund investable spin-out workstreams. @DisruptionJoe 's thoughts on this topic are in this recent comment: [[Discussion] Gitcoin 2023 - Future Essential Intents and Organization - #5 by epowell101](https://gov.gitcoin.co/t/discussion-gitcoin-2023-future-essential-intents-and-organization/12533/5)
[/quote]

Here are the thoughts you refer to:

[quote="DisruptionJoe, post:6, topic:12533"]
I’m very concerned that once we begin taking revenue, we will set our goals in ways that slowly eliminate our efforts for the public goods parts of our ecosystem. The best way to stop this from potentially being a problem is to design public, transparent, and ratified processes for Gitcoin to hold investment in workstreams which find a way to produce revenue. This would clearly set the line that GitcoinDAO treasury is ONLY funding public goods in our ecosystem.

However, if the experts in a workstream are the only viable option for providing services which are needed AND they are able to demonstrate the ability to collect revenue and forecast a profitable future, then Gitcoin should invest in that business with favorable conditions.
[/quote]

and

[quote="DisruptionJoe, post:6, topic:12533"]
We do have a session on updating the essential intents next week. I’d like to get to those results before entertaining a re-org of any type.
[/quote]

Additionally, why would you think FDD contributors should work unpaid to design governance processes for the DAO? This is a stretch from our mandate and common sense.

[quote="kevin.olsen, post:1, topic:12612"]
Given the urgency to launch our products and ensure their legitimacy in the market, is there a risk in ending the FDD WS? *In my opinion, no. The FDD is not operationally responsible for Fraud Detection and Defence at this point in time. There are analytics needs in products like Passport or the Grants Stack, and I would recommend staffing data science in those teams.*
[/quote]

**This is a blatantly false statement.** We found substantial fraud in the Fantom round and the same wallets are already hitting the Alpha round. I shared this at the Tuesday weekly and the CSDO meeting. 

[quote="kevin.olsen, post:1, topic:12612"]
Sybil Legos sounds like a good idea. Where does this work go? *TBD, I am unconvinced that this project will achieve a production release. I think this effort needs to be re-evaluated outside of the FDD workstream umbrella and see if the DAO believes this effort should continue to consume resources or not.*
[/quote]

You say this as though the DAO hasn't been evaluating our work and yours every three months. Yes, we would love to get more people to pay attention and care about sybil resistance and our solutions. It goes a little far imho, to call out the stewards who have been deep diving on our budget for not doing their jobs.

[quote="kevin.olsen, post:1, topic:12612"]
Investible workstreams make sense. Let’s do that. *Agreed. Sounds super cool. But there’s no process for that, and this needs some dedicated effort to hammer out a process in collaboration with DAOOps and governance.*
[/quote]

Exactly! This needs a process. That is why I am talking about it. I DO think FDD should likely become a smaller workstream with more direct support to ODC in the future. I don't think we should fire everyone in FDD 10 days from now AND think that would be a horrible precedent to set. 

[quote="kevin.olsen, post:1, topic:12612"]
We don’t have enough time to make this change. *The Research and Strategy line items in the FDD S16 budget would indicate to me the ODC, the Revenue, and Spinout ideas should be fairly evolved, and the FDD may be in a spot to implement these changes now. Either way, we cannot keep funding workstreams because of our inability to improve our budgeting process.*
[/quote]

The S16 budget was put together without knowing whether there would be a GR16. Additionally, we didn't know when which parts of the protocol would launch necessitating flexibility in our objectives. I have kept the stewards up to date with the changing tasks/projects we have prioritized as the season developed. GPC has done a great job of meeting the deadlines for product launches this season, but these deadlines were set AFTER the budgets were posted. 

Here is a [miro](https://miro.com/app/board/uXjVP0ptO3k=/?share_link_id=966113074605) with the latest updates as to what FDD has completed this season and what we won't do that was initially considered. This should not be surprising as you were one of the people who pushed for us to have "flat" (although most workstreams increased) budgets without much scrutiny on objectives. Please don't call FDD out for operating under the agreements you supported. 

We are funding the workstream because sybil defense is critical to Gitcoin's success AND WE KNOW that Passport is not enough at this time! We want to finish the job.

[quote="kevin.olsen, post:1, topic:12612"]
FDD as a workstream has run its course, the original responsibilities have diffused through the DAO, and the day-to-day work belongs in new or different parts of the organization. I believe the ODC exemplifies the subtraction mindset and community building we want to take as a DAO, and I’m super supportive of this direction.
[/quote]

I agree with most of this, but FDD has NOT run it's course and it's responsibilities are still numerous. 

[quote="kevin.olsen, post:1, topic:12612"]
As a steward, I would support budgets for independent and accountable workstreams representing the current focus areas within the FDD (even one-off direct grants to accomplish a particular goal). I will not vote to fund another season of the FDD as it is currently organized.
[/quote]

As a steward, I support your right to vote and campaign as you choose.

-------------------------

kevin.olsen | 2023-01-21 13:03:48 UTC | #3

Hey Joe, I've read this through this a few times, before I can respond there is one point that I want to clarify at this time.

You've mischaracterized this post several times as advocating for firing 10 people:

[quote="DisruptionJoe, post:2, topic:12612"]
advocating for laying-off 10 people
[/quote]

[quote="DisruptionJoe, post:2, topic:12612"]
“I think we should fire this workstream”
[/quote]

[quote="DisruptionJoe, post:2, topic:12612"]
fire everyone in FDD 10 days
[/quote]

My post doesn't advocate for any this, and it's painful for me to think of the FDD contributors seeing this post being mischaracterized this way.

This post is about refactoring our DAO to better map the work being done to the problems we are solving. I put forward a recommendation for how we plan to take apart our own workstream https://gov.gitcoin.co/t/refactoring-gitcoin-dao-the-next-gpc/12592 

I'll take some more time to see if I can come up with a more complete response, but will end this by reiterating the sentiment that I prefaced this post with:

[quote="kevin.olsen, post:1, topic:12612"]
I hope we can move through the tension to arrive at the best results for the DAO, **the contributors in our workstreams**, and our community
[/quote]

-------------------------

DisruptionJoe | 2023-01-22 16:55:35 UTC | #4

## Firing Assumption

Perhaps I did respond with the incorrect assumption that you are recommending firing everyone. You did suggest paying the ODC and potentially spinning out data science and maybe sybil analysis into Passport. 

I'm really hoping that we agree upon some appropriate level of psychological safety as a first principle for Gitcoin. Think of this post from the point of the contributors of FDD. 

1. Perhaps this would be received better if you listed the individuals and where they would go?
2. Who decides who stays and who goes? You? Other workstreams? (It is tough to say when the recommendation is putting them into the Passport team which you are a lead. You also suggest splitting GPC into two workstreams which you would be a co-lead of both?)
3. What about personnel decisions already in motion by FDD? Shouldn't we consider those?

Being transparent does not mean that we aren't allowed to have a discussion before you post something that will impact multiple people in this way. This courtesy was given to Moonshot before winding it down, so why not FDD?

## The Problems We Are Solving

Gr12-GR15 averaged over $500k in matching funds saved from misallocation by the work of FDD. This fraud is caused by around 25%-30% of the donors being sybil each round. The beta rounds coming up are  likely to continue this trend. 

Hopefully, Passport DOES fix a majority of it. This would mean FDD did a great job designing the algorithm! Let's say passport reduced the fraud to half it's previous volume. We might say that only 10% of matching is fraudulently allocated. Here is what the seasonal loss experienced by the ecosystem would look like using the forecasting model I shared here: https://gov.gitcoin.co/t/an-interactive-model-for-gitcoin-revenue-growth-forecasting/12625 

![Image 2023-01-22 at 5.22.59 PM|690x216](upload://d3QNWUHdcRbC96c94c77BRT4Mab.jpeg)

The columns in red are the SEASONAL amount lost to fraud! Not cumulative. The rows are seasonal loss based on a low, mid, and high growth rate over time (row 1 is the first season, row 6 is after 6 seasons). 

At the same time, the protocol itself is launching after EthDenver. This means we don't even know how many rounds will be run! 

The biggest problem with fraud is that the marginal value is too low for anyone to fund the solution. Sound familiar? This is the age old public goods funding problem. If there is a problem with the grants protocol that the DAO should solve, it is sybil resistance!

Yes, there is a potential opportunity to spin out profitable entities from workstreams, but I am not pushing for this because I'm excited about the business opportunity. It's because I think that Gitcoin should only consider protocol fees and/or UI fees for revenue but not services! The investment in worktreams recognizes a well known systems problem in cybernetics and offers a positive-sum solution. I'd rather FDD continue focus on solving sybil resistance and take mutual grants in the many businesses which might come from it's open source data and tools.

This also seems like a very optimistic and humane way to wind down a workstream as it solves it's core problem. 

## Refactoring the DAO

I agree that we should refactor around our core problems. If I was to just decide myself, Id say core problems are:

- How to increase the speed and satisfaction of Passport integrations to encourage growth?
- How to enable enough 1-click funding stack permutations on the Grants Stack UI to find product market fit and drive fee revenue?
- How to set best practices in program governance with the Gitcoin Grants Program?
- How to enable economies of scale learning across ecosystems using Allo (grants) protocol using open data to prevent capture at the data layer? (read: black box algorithms & single points of failure in data extraction)
- How to reduce DAO budgets and transition to dogfooding our protocol to fund Gitcoin ecosystem public goods while maintaining our core products?
- How to empower program managers by offering them a robust suite of tools and builders to help continually allocate capital better?

I'm guessing we are closer than farther apart on this. However, I would like to go through our essential intent exercise and then decide on a best way to refactor around our problems.

## How We Might Move Forward

Maybe we should discuss 1 on 1? Perhaps there is a more personal reason you might want a neutral third party present? I'm open to working together to find solutions.

-------------------------

Adebola | 2023-01-22 18:33:38 UTC | #6

With all due respect, given that your post highlighted FDD’s shortcomings, none of its successes and immediately advocated for it to not submit a budget for the upcoming season, it is very hard to not characterize your post as advocating that everyone be laid off.

-------------------------

Vega | 2023-01-23 00:47:35 UTC | #7

[quote="DisruptionJoe, post:4, topic:12612"]
I’m really hoping that we agree upon some appropriate level of psychological safety as a first principle for Gitcoin.
[/quote]

What is the basis of psychological safety at Gitcoin if the token (which funds 100% of operations) is going down all the time? 

The token (and by proxy, faith in Gitcoin as a whole), is prettymuch at an all time low.

@a33titude did a good job of providing some perspective on this [here](https://gov.gitcoin.co/t/discussion-should-workstreams-be-allowed-to-request-stables/12536/5).

[quote="a33titude, post:5, topic:12536"]
## What conclusions can we draw from this data?

GTC/USD is a very low liquidity market in between ETH/USD and GTC/ETH.

The upward price on GTC/USD is due to ETH/USD recovering.

The flat/downward price on GTC is a sign that people who are more deeply involved in the Ethereum Ecosystem (most of Gitcoin’s contributors, token holders, stewards) do not think that GTC is a better hold than ETH or other ETH-based assets.
[/quote]

In any sane organization, this would compel a shift in strategy and execution.  

In considering the debates on the re-org posts, I encourage people to consider "what is truly the best path for Gitcoin and GTC?"

Clearly workstream contributors are not "entitled" to the next batch of funding.  Especially if continuing to fund their workstream is not what is best for Gitcoin and GTC.  But if the DAO decides that's the way to go, then it should of course do it humanely.

-------------------------

kyle | 2023-01-23 01:06:09 UTC | #8

Thanks for posting this @kevin.olsen - I am in agreement with much of the post. And I too did not expect us to "fire 10 people" as @DisruptionJoe put it.

Many of these folks could continue work in other workstreams (Grants, Passport) and in the new ODC workstream. I am just really surprised and dismayed to see the hostility in your response both here and on Twitter. Its feels pretty immature and not one that has the dAO's best interest in mind but perhaps your own.

Let's frame what Olsen said in a different way:

**Given**
[quote="kevin.olsen, post:1, topic:12612"]
* Grant Reviews by the FDD have ended entirely with the move to the protocols. These responsibilities lie with operational roles in the Grants Programs, aided by continuous improvements to the products in the Grants Stack.
* Sybil Hunting is no longer a contributor activity but programmatic, replaced by iterative improvements to Passport in collaboration with Data Science.
[/quote]

**How might we**

[quote="kevin.olsen, post:1, topic:12612"]
Create an ODC workstream with its own budget.
[/quote]

**And ensure some of the great work FDD is doing can continue (perhaps in a different workstream**)? 

---
I am still just surprised at the rejection of Olsen's suggestion to:

[quote="kevin.olsen, post:1, topic:12612"]
FDD contributors take some time to build a proposal for an investment and governance process (independently of the existing workstream process) that can be ratified and used to fund investable spin-out workstreams.
[/quote]

You have been advocating for you own DAO for 6+mo's now. You'd have that chance?

As for the other contributors, I don't see this as "fire the workstream." I see this as a step to getting folks closer to tech. In the near future I could see myself proposing a similar "refactor MMM" where we move Product Marketing into the respective workstreams, Grants marketing into PGF and then build a new Brand Marketing workstream (and decide if merch is in that mandate).

-------------------------

llllvvuu | 2023-01-23 02:07:40 UTC | #9

Perhaps it would also be worth asking the fine folks who are putting their money at stake sponsoring these rounds if they would like to fund fraud defense or if they would be more comfortable with a $785k fraud cost and associated reputational damage. It would also fit the broader theme of giving the DAO a sustainable revenue model and aligning incentives with stakeholders to whom we are providing services (i.e. running their grant programs for them, currently for free, which may be too generous).

Definitely a split between "FDD Execution" (which includes manual and centralized execution; and realistically Gitcoin does not yet seem in a place to graduate from this yet, as it seems to be the broader public's understanding that Gitcoin is still supposed to provide these services) and "FDD Systemization" (which would aim to obsolete and eventually absorb the execution group, and includes ODC, but also realistically there needs to be Gitcoin full-time people who are coordinating the effort and deciding on standards/standard libraries/official guidance for protocol users). Certainly, a proposed re-definition of specific contributor roles would be a useful part of that, with input from said individual contributors.

One could propose that FDD service fees be negotiated directly between protocol users and FDD as a spun-out entity. Therefore you skip Gitcoin as a middleman and insurer. I would recommend in this case proceeding in two stages:
* Stage one: Switch to a new invoicing model in which "Fraud Defense Services" is an explicit line item offered to round owners, so that we have a separate revenue stream for FDD. FDD is responsible for the pitch directly to protocol users.
* Stage two: Spin out FDD, handing off the revenue stream to them. Let them participate in the Gitcoin brand and IP still.

I would recommend, if pursuing this option, to give an adequate transition period during stage one. In particular, the FDD needs to have adequate data on how much revenue it can expect when it eventually spins out (and so that any staffing adjustments can be made with much more due notice). Furthermore, round owners may need time to warm up to the idea of paying for services, since we have been subsidizing it for so long.

It can also be structured as a mutual grant where if Gitcoin runs a loss during stage one (pays FDD more than the FDD revenue stream brings in), the FDD spin out owes the difference after spinning out. The Gitcoin brand and IP can be used as collateral. One must be careful not to run afoul of securities law, though.

-------------------------

llllvvuu | 2023-01-23 03:01:36 UTC | #10

Let's also compare @kevin.olsen

> * Create an ODC workstream with its own budget.
> * The Sybil Analysis spin-out is broken out for further incubation as its own workstream OR Data science and Sybil Analysis move into the Passport ‘customer’ workstream and iterate within the context of a product delivery organization.
> * Pause Sybil Legos until there is Product/Engineering leadership with a proven track record of delivering production software that can produce a project plan and budget that the DAO can review and approve.

vs @DisruptionJoe vision:

> **ODC builds open source projects.**
> 
> * Exploratory Data Analysis
> * Analysis Legos
> * Data Extraction Infrastructure
> 
> **FDD maintains data infra & data products.**
> 
> * Open Source Scoring Applications
> * Ad Hoc Round Analysis
> * BI Tool Maintenance
> * Prioritization and Specifications for Fraud Defense Analysis & Builds from ODC/DevRel
> 
> **FDD Service Spin Out**
> 
> * Freemium Model Product
> * Consulting Services

The first obvious thing that stands out is that **they don't seem that different at a high-level**. The primary differences are:
* In @kevin.olsen version, "Analysis Legos" is gone
* "Sybil Analysis [...] its own workstream OR [...] move into the Passport ‘customer’ workstream" seems to be referring to what @DisruptionJoe calls "**FDD maintains data infra & data products.**". The "its own workstream" is identical, whereas the "move into the Passport ‘customer’ workstream" seems to be a contentious takeover play. Perhaps this can be fixed by simply removing the "OR [...]"

The part that seems not clear/potentially in disagreement is how much time should be given to FDD to complete its pivot to its final form. It doesn't sound like the thing quoted from @DisruptionJoe was meant as something that would be done this month. Is this an ultimatum to accelerate it?

Also, to be clear, would it also hold in this case that we "do move forward with splitting our workstream, implementing budgeting and payroll changes to establish two workstreams. But, we do not make any changes to the way contributors organize and work until after ETHDenver.", as was suggested in the [proposed GPC refactor](https://gov.gitcoin.co/t/refactoring-gitcoin-dao-the-next-gpc/12592)? That seems unnecessarily confusing for stewards. How would one "not make any changes to the way contributors organize and work until after ETHDenver" if one budget proposals can have a different voting outcome than the other?

Finally, I would add that what I see as an outside steward as being sensible for something like FDD is pretty similar to what I quoted from @DisruptionJoe, except "Ad Hoc Round Analysis" sounds like it belongs in the Spinout.

-------------------------

tigress | 2023-01-23 10:57:19 UTC | #11

[quote="kevin.olsen, post:1, topic:12612"]
I feel this conversation belongs in the forum
[/quote]

Help me understand why this goes straight to the forum without first consulting (or at least informing) affected workstream leads. 

Which of your values and priorities motivate you to choose this channel for communicating *about* your peers?

-------------------------

tigress | 2023-01-23 11:21:12 UTC | #12

[quote="Vega, post:7, topic:12612"]
In considering the debates on the re-org posts, I encourage people to consider “what is truly the best path for Gitcoin and GTC?”
[/quote]

Thank you @Vega for mentioning this here. 

Posts like this affect psychological safety. For sure this contributes to the deterioration of trust in the people and in GTC.

-------------------------

DisruptionJoe | 2023-01-23 11:59:17 UTC | #13

Kevin and I talked last night and realized (as we both likely suspected) that a conversation would help. We are meeting :::checks watch::: Now...  will post some thoughts after.

-------------------------

DisruptionJoe | 2023-01-23 21:35:39 UTC | #14

[quote="kyle, post:8, topic:12612"]
I am just really surprised and dismayed to see the hostility in your response both here and on Twitter. Its feels pretty immature and not one that has the dAO’s best interest in mind but perhaps your own.
[/quote]

I apologize if this came off as hostile. I attempted to keep it less hostile than this came across to me:  

[quote="kevin.olsen, post:1, topic:12612"]
End the FDD workstream, do not post a budget for the FDD in S17
[/quote]

Is some type of warning to me before posting this a reasonable expectation? 

Especially after sitting in the CSDO call and everyone agreeing that our budgets would remain flat for next season. Nothing was said to me then. 

On Wednesday, you and I had a conversation about when it would be appropriate to split up FDD. We discussed 6 months as an the earliest that we could potentially commit, but we would keep the conversation going.

I shared these pieces of information to the workstream. We were feeling good. We have a lot of work to do and we are excited to do it. 

Then this post comes on Friday afternoon. Do I call attention to it and ruin peoples weekends? Do I ignore it and have them upset that I said nothing? This put us in a difficult place that wasn't necessary imho.

[quote="kyle, post:8, topic:12612"]
Let’s frame what Olsen said in a different way:
[/quote]

1. This is a much better way of saying it. 

2. It does hold incorrect interpretations of Passport ability to provide sybil defense at this time. 

[quote="kyle, post:8, topic:12612"]
You have been advocating for you own DAO for 6+mo’s now. You’d have that chance?
[/quote]

Yes, and apparently I have not communicated my reasoning very well. I do feel as though I have stated these points many times including the exact comment that he referenced. 

* I'm not interested in FDD spinning out, i'm interested in FDD creating a new entity to spin out
* FDD can do this to model how it would work for the DAO (because I'm worried!)
* Once some service revenue comes in, people shift focus to the revenue generating thing. Services require people and before you know it your past the event horizon with an org that has an internal public goods funding problem. 
* We are planning on ODC spinning out. It is not ready. There are reasons for this. Let's explore them together. 

[quote="DisruptionJoe, post:6, topic:12533"]
I’m very concerned that once we begin taking revenue, we will set our goals in ways that slowly eliminate our efforts for the public goods parts of our ecosystem. The best way to stop this from potentially being a problem is to design public, transparent, and ratified processes for Gitcoin to hold investment in workstreams which find a way to produce revenue. This would clearly set the line that GitcoinDAO treasury is ONLY funding public goods in our ecosystem.
[/quote]

Additionally, I've been frustrated at our inability to have a conversation without it being a commitment. Let's talk about these possibilities. Let's talk about the potential. 

This is an attempt at a better conversation around revenue: https://gov.gitcoin.co/t/an-interactive-model-for-gitcoin-revenue-growth-forecasting/12625

[quote="kyle, post:8, topic:12612"]
As for the other contributors, I don’t see this as “fire the workstream.” I see this as a step to getting folks closer to tech. In the near future I could see myself proposing a similar “refactor MMM” where we move Product Marketing into the respective workstreams, Grants marketing into PGF and then build a new Brand Marketing workstream (and decide if merch is in that mandate).
[/quote]

I'm very ok with you posting this in the future. I'd be hard pressed to support it if you posted it before the next budget after we sat in the room and agreed on a course of action. It isn't that we can't change course, it is that we could offer some courtesy around discussing peoples lives. 

[quote="llllvvuu, post:9, topic:12612"]
erhaps it would also be worth asking the fine folks who are putting their money at stake sponsoring these rounds if they would like to fund fraud defense or if they would be more comfortable with a $785k fraud cost and associated reputational damage.
[/quote]

I've suggested this. Although the recommendation is to spin out FDD services, at this time there is an understanding that PGF is working on service agreements. I've gone along with this because we had no clue that anyone would want us to spin out this soon. 

[quote="llllvvuu, post:9, topic:12612"]
t would also fit the broader theme of giving the DAO a sustainable revenue model and aligning incentives with stakeholders to whom we are providing services (i.e. running their grant programs for them, currently for free, which may be too generous).
[/quote]

Yes. This is why I've been pushing the conversation. Program managers will have a need for more productized and professional commercial services. There is an OPPORUNITY worth discussing and shouldn't be considered as trying to defect or be independent. This is for the good of the WHOLE DAO. 

What we really need is space for strong contrarian opinions to be debated with a larger group than CSDO. 

[quote="llllvvuu, post:9, topic:12612"]
One could propose that FDD service fees be negotiated directly between protocol users and FDD as a spun-out entity.
[/quote]

Yes. This is a better solution than just dropping everyone performing in a workstream because they might be able to collect some revenue. Let's forecast, plan, and see if there is an opportunity the GTC community might be missing!

[quote="llllvvuu, post:10, topic:12612"]
The “its own workstream” is identical, whereas the “move into the Passport ‘customer’ workstream” seems to be a contentious takeover play.
[/quote]

This is an elephant in the room. CSDO has 2 reps from each workstream. In the GPC refactor post a couple days before, Kevin suggests that GPC become two workstreams with him a half lead for each. I honestly don't think this is a power play from Kevin. I do think his suggestion for GPC is a good one as is most of his suggestion. 

Additionally, I don't have any desire to remain a workstream lead unless there are people who depend on me or would like me to remain. Look at my steward introduction. I hoped to train someone and have them in the role by season 15. Unfortunately with bear market budget cuts, we had to refocus. I'm open to stepping down from FDD workstream lead representation at CSDO, but I would like a clear discussion around who follows and how they are elected, chosen, or other. This should happen PRIOR to a move to defund or split FDD which may have the side affect of the changing representation. 


# Moving Forward

FDD and other workstreams are sharing a first draft of budgets with CSDO tomorrow. Friday there is a 3 hour facilitated session for us to discuss and further align these budgets and make sure the workstreams agree on a path forward. Between Tuesday and Friday, I will share our FDD budget and future plan with Kevin to bring him into the process of co-creating a plan with FDD.

-------------------------

J9leger | 2023-01-24 00:16:23 UTC | #15

I appreciate these posts from @kevin.olsen. In general I think he's got some really level headed ideas that often we don't get time to hear. 

I empathize that as a workstream lead, this post would elicit more of a defensive reaction initially than an opener for a creative discussion around refactoring how we're organized. However, I think as much as possible, seeing each of these individual posts on workstreams across a broader vision to start with vs piecemeal could help avoid initial defensive reactions. 

That said, I'm 100p in alignment with @kevin.olsen that the more we can orient how we organize around our protocols and have lean teams of people close to the tech, the better. 

I do think FDD consolidation with Passport could be valuable. In addition the spin-out approach for Sybil and FRAUD detection is one to keep exploring. What I do wonder about the above and something I'm genuinely worried about is a simplified review process that easily detects fraudulent grants. We have not done any open rounds since GR15 and both grant reviews and those that were fraudulent was a real challenge for us to manage. If we don't prioritize building better moats between FDD and Passports work combined, we'll degrade the legitimacy of our protocols. All that to say, I'd love to see FDD doing more around the Passport protocol and pushing it to be a better product for sybil and fraud detection similar to how the PGF team is pushing forward the Allo Protocol (new name for Grants Protocol).

For this to be successful we have to see more of a team mindset between workstreams than one being out to get the other and we should be able to open these discussions and recognize it's not about killing workstreams and jobs, it's about reorganizing for long term DAO success. @tigress I don't think @kevin.olsen meant for

> Posts like this affect psychological safety. 

And I think it worth reflecting on what you'd like to see differently in someone expression their opinion before making such strong claims as the one below. 

>For sure this contributes to the deterioration of trust in the people and in GTC.

-------------------------

shawn16400 | 2023-01-24 10:43:13 UTC | #16

[quote="kevin.olsen, post:1, topic:12612"]
FDD contributors take some time to build a proposal for an investment and governance process (independently of the existing workstream process) that can be ratified and used to fund investable spin-out workstreams.
[/quote]

@krrisis I know DAOops season 17 plans are underway, but this looks like the kind of cross stream work DAOops might want to lean into. 

[quote="kevin.olsen, post:1, topic:12612"]
Either way, we cannot keep funding workstreams because of our inability to improve our budgeting process.
[/quote]

@krrisis I suspect this goes beyond budgeting to include the disconnect between EIs and budget deliverables.  From the Steward Council call yesterday https://youtu.be/95YooYceMyw?t=2470, to the timing of this post, and from what I perceive as the surprise from @DisruptionJoe, this gap is becoming clear to me.  Let's discuss how this impacts DAOops season 17. 

[quote="kevin.olsen, post:1, topic:12612"]
I will not vote to fund another season of the FDD as it is currently organized.
[/quote]
@krrisis Season 16 budgets received about 9-10M votes per budget on average.  Given  @kevin.olsen holds about 19% of the tokens normally cast in an election, this post is more than just one node in a network.  If I read into responses from @J9leger and @kyle as support for the proposal, that percentage moves to about 50% votes normally cast in a budget vote. 

@kyle, @J9leger, I am not presuming to know how you would vote, but I use this as an example to illustrate how concentrated voting power is at Gitcoin.  

Is this good or bad?  We as a DAO need to come to consensus.  If I were leading a workstream in Gitcoin - this post would compel me to ramp up my internal sensing to those top token holders to avoid being caught off guard.

I do not think this post and thread represents the best of Gitcoin.  @krrisis and @Jodi_GitcoinDAO in a perfect world with all the time and resources, DAOops would lead a post mortem and we would reflect on how we could have done this better and what updates we might make to our principles(?) to guide how we work.

And finally, I need to get off my butt and finish that post sitting in my draft folder titled "how to use the forum for maximum positive impact".

-------------------------

kevin.olsen | 2023-01-26 15:25:49 UTC | #17

A quick follow-up - I've been working with @DisruptionJoe this week and I'm finding our 1:1 dialogue to be productive. I'm optimistic that an integrated approach will be reflected in the budgets.

[quote="shawn16400, post:16, topic:12612"]
I do not think this post and thread represents the best of Gitcoin.
[/quote]

I agree with this 100%. And will be the first to admit that I'm learning, and in my efforts to bring difficult topics into public spaces, I can see room for improvement on my end.

I also hope that our community's requests for visibility into the work of the DAO are centered in any recommendations DAOOps makes. 

Lastly, I hope the process of affecting change and the work we do in public begins to reflect the thoughtfulness, candidness, and courtesy our 1:1 conversations have.

-------------------------
