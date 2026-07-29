---
id: 11171
title: "[Discussion] How might we think about budgeting - What should the DAO budget be?"
slug: discussion-how-might-we-think-about-budgeting-what-should-the-dao-budget-be
category: open-discussion
url: https://gov.gitcoin.co/t/discussion-how-might-we-think-about-budgeting-what-should-the-dao-budget-be/11171
created_at: 2022-07-26T14:39:19.293Z
last_posted_at: 2022-08-03T22:59:52.790Z
posts_count: 14
views: 4548
like_count: 85
---

# [Discussion] How might we think about budgeting - What should the DAO budget be?

<https://gov.gitcoin.co/t/discussion-how-might-we-think-about-budgeting-what-should-the-dao-budget-be/11171>
kyle | 2022-07-28 15:56:37 UTC | #1

When the Gitcoin DAO launched over a year ago, we were right in the first third of a crypto bull run. Interest in crypto was growing again, and the value of outside capital was much lower than it is today. This has meant for Gitcoin, lots of unchecked growth and a DAO that has seen only the sweet smell of summer. We didn’t have much of a fall season, we went from summer to brutal winter with drawdowns of nearly 80% within a very short time period.

As a DAO, we’ve grown permissionlessly – not without approval from Stewards, but often without first-principled, intentional decision-making. Contributor counts have increased, workstream budgets have ballooned, and yet we have workstreams that continue to struggle to actually be effective at building towards our (newly defined) Essential Intents. With this rapid growth, we have amassed a myriad of folks who are not in the right roles.

In S14 we saw a constructive reorientation with FDD; FDD was able to focus on the two core tenets of their mandate (Grants Approvals and Sybil detection), with some support for Analytics.This change has made it more clear what FDD is doing that’s essential and where it belongs in the DAO, more to come below.

It is common to have [roughly 60%](https://www.builtinchicago.org/blog/how-much-should-software-startup-budget-development-and-operations) of a [tech startup’s costs](https://about.crunchbase.com/blog/startup-product-spend/) borne from development (engineering, product, design). The remaining 40% of the budget is in supporting functions. While the right breakdown for Gitcoin may vary somewhat from this archetype, we should at least be in this ballpark. Taking the 60% figure as a starting point, if we assume GPC is at a quarterly budget of $1MM, that means the rest of the DAO should fit into $670K a quarter. Moonshot Collective likely has half of their team also supporting protocol development (in Passport, and in partnership with Optimism)... perhaps we include another $200k from their budget in GPC (TBD on how best to do this). 

One caveat to call out, we have a Grants program which delivers roughly $6MM in quarterly funding to the ecosystem and I want to ensure that stays intact. As a result, I could see us give some parts of PGF an immunity potion for this exercise. We also have a few roles that directly support the Grants execution function so perhaps they are immune - but not many.

Our burn as a DAO in S141 was [$2.9M](https://docs.google.com/spreadsheets/d/1A4lmRXnPH2KxbY84GxlHTDdupELBr7oU9b3i_L9e_uM/edit#gid=0), or ~$1M per month. This is about [3x the burn of a typical US-based startup](https://www.geekwire.com/2018/startups-spend-money-new-data-shows-burn-rates-differ-industry-region/) – and those startups are typically generating early revenue, which Gitcoin is not. In addition, as a DAO whose capital structure is pretty much all in our (highly volatile) governance token today, we don’t have sufficient runway in case of a rainy day. It is [generally recommended](https://medium.com/corl/how-long-is-your-startup-runway-6eed37962445) that startups have 12-18 months of runway on hand – today, the Gitcoin Timelock has no stablecoin-based runway to rely on whatsoever. We have line of sight to $5-10M with the Treasury Diversification efforts, which under today’s spending, would bring us to ~4-12 months of runway – still leaving the DAO in a precarious position in the event of a further downturn, even if we are able to execute on those efforts.

I can hear what you are thinking - “Kyle, this is insane, you are out for blood.” I don’t think I am out for blood, and in fact I am really focused on ensuring we operate as a healthy (decentralized and autonomous) organization. As we contract, we should take care of those who may not be with us during this next phase of our build cycle with severance and offer support in finding their next role. We should also honestly invite them to continue to be part of our community, and to help us grow funding for public goods.

@lthrift did all of the heavy lifting of visualizing how this might be possible. One of those options are diagramed below but it is not the only way to reduce our spend, thank you to those who are brainstorming with me (@annika, @ceresstation, @krrisis). 

I recognize this split may not be doable in S15 - it's worth having the conversation though:
![image|680x500](upload://kiMgUjbBft3jDBxCH7anSsIb39e.jpeg)


**What would need to be true to reach something like this? What do folks think of this split (60/40 with carveouts for Grants Ops)?**

-------------------------

annika | 2022-07-26 16:59:42 UTC | #2

Thanks for raising this @kyle .

I'm fully bought into the ethos of this conversation and having a DAO-wide figure, as well as rough breakdowns across WS, that we pre-emptively aim to track to.

From my perspective, we've always done almost exclusively bottoms-up budgeting and workstreams have been thinking far too much in isolation about their own budgets, versus us thinking from first principles at a DAO-wide level as to how much is reasonable to spend quarter-over-quarter and trying to make tradeoffs in a broader context than just at a workstream-level.

This is especially pertinent in a bear market.

Candidly, I'm not necessarily sure 60/40 will be exactly the right split (given our ImpactDAO roots, we might be closer to, say, 55/45? 50/50?) or that a $1.5M budget for S15 specifically is practically doable - but I am very in favour of starting this conversation and thinking structurally in this vein across workstreams.

-------------------------

safder | 2022-07-26 17:29:18 UTC | #3

I think this makes sense, given the bear market conditions and Gitcoin's current state as a non-revenue-generating Impact DAO shifting into a Protocol DAO.

However in order for us to reach these numbers (~70% reductions in each workstream's budget other than GPC) we need to envision what a lean Gitcoin DAO looks like, and I think this would require a pretty thorough restructuring of teams/roles/responsibilities and also a reframing of workstream autonomy. We are currently far from being lean, with each workstream designed to operate mostly self-sufficiently with their own ops/people ops/marketing/community "departments". This allows workstreams to be more autonomous, but also means we have a lot of repitition of labour and working in silos. It's painful to see, but there is very often a sense of unhealthy competition/almost animosity between workstreams (and even within workstreams, between "departments") instead of a sense of collaboration, especially when the topics of budgeting are raised. Everyone thinks the work they're doing is the most useful and should get the highest budget, because they often don't even know what other workstreams are working on. There is very little interdependence. 

Like Annika mentioned, I believe this also has a lot to do with our seasonal budget-approval process. These budgets are created collaboratively within each workstream, and briefly discussed across workstreams at CSDO, but there is so little context each workstream contributor has into what contributors at other workstreams are working on - at best, we're just making guesses at what the DAO needs based on our own personal context and skillset, and at worst, we're just creating work for ourselves regardless of the actual needs of the DAO.

I think we need less of a focus on workstream "autonomy" - we're already a decentralized organization and have a fairly robust governance process - and more of a focus on interdependence and skills+context-sharing across the DAO. I think budgets should be applied for and decided on as a DAO, instead of as workstreams, and I think we need to do this less often than every season (something I'm glad we're already having discussions on). We need to identify the distinct roles each contributor is playing and the unique value they are adding in service of the Purpose and Essential Intents *together as a DAO instead of in our workstreams*. And we need a process that conducts all of this in a truly unbiased/credibly-neutral way. Tall ask to do before Season 15, but I'm glad we're starting the conversation.

-------------------------

connor | 2022-07-26 20:36:45 UTC | #4

This is a hard post to make and I appreciate you putting it forward Kyle. I largely agree that reductions like this need to be made in order to deal with the current market conditions. Bear market + increased sell pressure on GTC + lower price could lead to a death spiral. We need to weather the storm for the next 6-12+ months.

I also think this is a wake up call to really double down on 1. GTC demand and utility within the platform, and 2. Revenue generation within the DAO. Right now we are a very services heavy "business", except the services we provide and programs we run are done for free with no captured value. I think we can change this sooner rather than later.

Finally, as @safder said, we likely need to dial down workstream autonomy to an extent. I feel as if workstreams are not well aligned on priorities, each workstream has its own focus, there is duplicate work being done, and not enough cross-stream alignment (and dare I say, not enough top down leadership). I hope we can work on this and focus next season on 1. scaling the existing grants program, and 2. launching the 2.0 protocol. This, along with token utility and revenue generation, should be the top priorities for all workstreams right now.

Thank you for starting this conversation!

-------------------------

tigress | 2022-07-27 13:00:51 UTC | #5

[quote="kyle, post:1, topic:11171"]
What would need to be true to reach something like this?
[/quote]


The new diet Gitcoin is facing and the culture that is being released on demand is, as it seems to me, most likely a consequence of 

* unchecked growth
* unprioritized work - lack of expression of WHAT needs to get in order to WHERE we intend to go
* lack of leadership: without first-principled, intentional decision-making

It boils down to this:

*In an organizational context, permissionless does not mean you can do whatever you want without seeking permission and expecting to be paid! Boundaries need to be consciously set in place to enable permissionlessness and autonomy.*

I tend to disagree with:

> With this rapid growth, we have amassed a myriad of folks who are not in the right roles.

An expression that I feel is more true in this context is: 

> We were overwhelmed by the growth*) - most likely. We lack(ed) prioritisation across the workstreams and did not set boundaries accordingly therefore we have amassed a myriad of folks who are here to contribute with good intentions, but who were not given the instructions of what this means in action.

Overall, I believe I can see where you are coming from and heading to and my concern simply is the way how this is going to be communicated. 

The question is not how to keep pushing harder and slimming budgets and workstreams.

> The question is: How can we become better at doing the right work (effectiveness!) and how can we improve the way we prioritize the work that we believe needs to get done (efficiency).

*)edit: Growth as in "No. of Contributors joining the DAO to work with and contribute to."

-------------------------

owocki | 2022-07-27 12:12:35 UTC | #6

[quote="tigress, post:5, topic:11171"]
We were overwhelmed by the growth
[/quote]

What kind of growth are you talking about here?  

Because `gitcoin.co/results` shows consistent a $6m/quarter (plus or minus $1m/quarter) moved through Gitcoin through the last 6 quarters.  From a GMV perspective, I'm not sure it can be claimed that the growth has been overwhelming. 


![Screen Shot 2022-07-27 at 6.07.48 AM|690x229](upload://NJHbvllYKOinOw2EywwZVs521K.png)
(There is one quarter that has $9m, but that's because the previous quarters match payments were rolled into that quarter.)

There maybe be other growth vectors tho.  The ones I'm aware of since the DAO launch:
1. 1 main QF round => 19 QF side rounds.
1. Gitcoin being worked on by 23 people => 300 people (according to the latest DAO Year in Review)
2. Growth in roadmap as Grants 2/Passport was launched.

-------------------------

tigress | 2022-07-27 13:00:40 UTC | #7

Growth as in "No. of Contributors joining the DAO to work with and contribute to".

-------------------------

Pop | 2022-07-28 12:33:08 UTC | #8

Thank you for your perspective, @kyle - a necessary call for efficiency in the face of market conditions and past spending patterns.

There are a lot of considerations here and I think a lot should have been done at the early stages of the DAO to ensure this "austerity" dynamic would not be needed:

 - Earlier, timely and actually efficient treasury diversification would have helped, particularly in the past year when the market conditions were auspicious. 
 - Standards in budget proposals, clear decision making flows vs rubberstamping just because "the going was good" should not have been encouraged. It always hurts when we're squeezed but good planning is done when we are comfortable and survival instincts are not activated and we make choices out of fear.

Austerity rarely works - there are countless economic crises that have been made worse by austerity - plenty of research and a great book I urge everyone to read  - Mark Blyth, Austerity: The History of a Dangerous Idea

I agree mindful spending is needed and because things were left unchecked, especially in the beginning, we are in a position where we must make tough decisions. I would, as always, err on the side of balance. 

This % ceiling on the cusp of S15 without prior consultation (aside the four individuals mentioned) feels very top down and corporate. I always invite discussion and even though we had floated this in the steward council, no proposal, in depth discussion or concrete plan was formed in consensus. Seems like this has been forming for a while, I wonder why it wasn't discussed in the previous council call since we were in effect discussing the new budget flow. 

I want Gitcoin DAO to be a beacon of transparency and best practices in how we evolve DAOs as organizations (and it may not be perfect) vs falling back on corporate reflexes. At least a hybrid of the two if not a purist approach. 

Saying all of this which I think is important to be highlighted and discussed - how may we use the NEW budget proposal flow to bring an evaluation of contributions and ensure we only focus on needs for the next 3 months - which in effect is what the new flow *SHOULD* be doing?

I urge this to be discussed in the next stewards council call for a much better diversity of perspective vs a distinct angle.

-------------------------

loietaylor | 2022-07-29 01:12:58 UTC | #9

Thanks for this discussion! @annika's comment strikes many of the chords I would touch, and I'll add a little more.

We certainly are not a software company - not in the way we've found market value, the way we've done our development, nor the values we hold in our world. So I'm wary of trying to mirror structures of a software company as you suggest with the 60/40 @kyle. Tech startups live in & reinforce the same world where open source software delivers billions in economic value on the backs of unpaid nights & weekends labor - the same world where more value is extracted/exploited from users than is created for them - the same world where people cannot work for the public good bc they would suffer tragedy of the commons so much that they wouldn't make rent. 

I do however worry sometimes that Gitcoin supports the public good a bit too much in all it's ways - we have been slow to reign in budgets, we've built DAO tools when it wasn't an essential part of our business plan, and we've offered services that certainly could generate revenue without charging ANYTHING to the users. I think that's all beautiful but as @connor says, we might do better to change *some* elements of this sooner than later. 
> Right now we are a very services heavy “business”, except the services we provide and programs we run are done for free with no captured value.

This point about burn is salient and I agree on shifting towards a top-down total budget number for the season. We can shift *towards* that while still staying agile to the information we have about what kind of spend is needed to accomplish our current goals. As Annika said we've been EXTREMELY bottoms up so far and I think even a mid point **in between** that and a totally steward-mandated top-down number would show a lot of improvement to our long term sustainability.
> Our burn as a DAO in S141 was $2.9M , or ~$1M per month. This is about 3x the burn of a typical US-based startup– and those startups are typically generating early revenue, which Gitcoin is not.

On the note of finding an in between, I've heard @kyle say this post was not meant to be as prescriptive for S15 as it is perhaps being perceived. It's a great convo to start and I'd like to see us make a plan this season that we take real steps towards for the next budget cycle.

I have a lot more to say about contributor health & maintaining quality work thru team morale & the right folks staying on board in the midst of these discussions, as well as more careful planning for RIF from a People Ops perspective but I'm gonna leave that comment for tomorrow!

-------------------------

kyle | 2022-07-29 02:26:22 UTC | #10

I appreciate the dialog here, and the opportunity I have had to start conversations with many people in the DAO as a result of this post. I have learned how I might have made this post without so much "sticker shock."

Thanks to @connor for offering thoughts on ways to improve the DAO treasury's position (ie, GTC Utility or charging for services) - I believe those are important in the right time. I personally don't believe we should start charging for running rounds... yet. But more importantly, I dont think it would change our need to lean down to a 50/50 split as proposed by @annika.

@safder pointed out some real challenges in how we are budgeting and one of my goals was to answer the request of "what type of budget numbers do stewards want to see?" My post was intended to be a discussion, not a mandate (as @loie pointed out) and I know this has caused a lot of hard reflection. Our ratified essential intents are now the rallying cry for us to work together as DAO to accomplish some bold goals. I think we all wish we had these to guide us sooner in the process and existence of the DAO.

I want to call out something @tigress specifically mentioned:
> The question is: How can we become better at doing the right work (effectiveness!) and how can we improve the way we prioritize the work that we believe needs to get done (efficiency).

This is spot on - I would STRONGLY advocate workstreams evaluate the work they are doing and slim down their commitments to only the items that support our Essential Intents. This naturally may offer guidance on how to slim down workstream budgets as well. I DO NOT want people to feel like they need work more in unhealthy ways.

One final note - This idea and 60/40 split formed and then was posted to the forums in a matter of 72 hours. I skipped the path of shopping it around privately with select people... I asked for an editorial review from two individuals, and then posted to the forum the next day after briefly mentioning this concept to each of the WS leads (except MMM as I didn't have a 1:1 with MMM leadership this week). As noted above, I want to do better as to not have the "sticker shock."

-------------------------

Fishbiscuit | 2022-07-31 02:25:58 UTC | #11

I'd like to chime in a bit while drinking some tea and being calm on a weekend.

Firstly, could we first recognise that it's not just Gitcoin that's down. The entire market is down and prices are just bad. Treasury diversification, a conversation that's started not long from when the DAO first started, wasn't executed in time and thus we are feeling it harder. **Either way, I don't think we should factor in prices too much into our decision-making because following this logical path, if prices are up we should spend freely (also not true).**

Secondly, that ultimately we **diversified sources of revenue**. Cutting costs without trying or even creating a path to revenue would just mean that talent would leave, projects would be closed, and eventually we won't even be able to support any program at all. That being said, simply cutting all workstreams that don't generate revenue also wouldn't make sense either.

Thirdly, echoing @loietaylor 's point, we aren't a software company. In fact, I think we're more like a foundation that helps other organisations (sometimes other foundations) disburse funds in a more democratic way without compromising on efficiency such as hiring a large grants team to manage through a software solution. I've been looking at [how charities operate](https://www.charitynavigator.org/index.cfm?bay=topten.detail&listid=505) and [what expenses might look like](https://warrenaverett.com/insights/nonprofit-ratios/) so that we might take a leaf from some of them. Perhaps looking at this would be a better way. But once again, we don't have revenue so it's practically impossible to use this. 

FYI:
*Total Contributions/Fundraising Expenses = Fundraising Efficiency Ratio, A lower ratio is considered better, and Charity Navigator gives its highest ratings to those organizations that spend less than $.10 for every dollar raised.*
Our spend for partnerships is 0.327M (budgeted cost) /3.4M (funds raised) = 0.09. Mad kudos to @ceresstation @vgk @azeem and every fundraiser working their ass off each quarter.

![image|634x500](upload://nz41bDYqoTONgokaP4bk9vlL4WD.png)

I'm going to try and answer **"What would need to be true to reach something like this? What do folks think of this split (60/40 with carveouts for Grants Ops)?"**


- we'll **need to have revenue** that can eventually cover this proposed budget of 2.25M/quarter (9M a year)
- some of us will need to help **shepherd the change and transition people into other roles** that serve the essential intents
- we might need to **split what we're doing into what's in service of the grants program and what's in service of improving it**. But that being said, it's pretty myopic because Gitcoin also has a strong overall community and is a reference point for many DAOs. However, as innovation work and operational work are very different in nature, splitting them and measuring separately will be fairer. eg. what's the program ratio for grants program. vs the innovation budget for Grants 2.0 (or other technology projects)
- we might have to **consolidate workstreams** into more specific goals to lower the overhead of cross-workstream coordination. (CSDO calls take up quite a few man-hours). This might mean a "Grants Program workstream" that has marketing, operational, sybil defence functions consolidated. Even if it isn't formalised as a workstream, we could calculate our budgets collectively and evaluate from there.

-------------------------

ZER8 | 2022-08-01 12:05:35 UTC | #12

Great post Fishbiscuit ! :smiley:

[quote="Fishbiscuit, post:11, topic:11171"]
we might have to **consolidate workstreams** into more specific goals to lower the overhead of cross-workstream coordination. (CSDO calls take up quite a few man-hours). This might mean a “Grants Program workstream” that has marketing, operational, sybil defence functions consolidated. Even if it isn’t formalised as a workstream, we could calculate our budgets collectively and evaluate from there.
[/quote]

Now this is a interesting idea, including everything about grants in a "Grant workstream" could be a big shift and could change the power structure, but could be more sustainable in the long term. 
As the present lead of Grant eligibility I have sometimes felt that my team worked a lot and always took the "bad hits" with the DAO even if we improved every round in almost every possible way in the past context of a not yet finalized DAO structure and the dynamism of the environment.

I'm just trying to imagine what a " Grant Program workstream" would look like and how it would be structured.

Maybe if the grants program is a completely separate entity it will be a lot easier to analyze performance, but the big issue is how the "Grants Program workstream" will be formed and structured to ensure that there is no friction between it's different initiatives and that the right people are in the right places. Nonetheless it's a cool and very progressive idea :fire:

-------------------------

michaelgreen06 | 2022-08-03 22:52:28 UTC | #13

@kyle , thank you so much for taking the time to write this post and bring up this delicate subject. I really appreciate you helping guide conversations (often tough) that help us find our way forward as a DAO. 

Thank you to everyone else who weighed in on this subject. Conversations like this are most fruitful when we have a variety of perspectives represented.  I resonate with many of your opinions and view this as an opportunity for growth as a DAO.
 
I agree that the DAO has been very eager to onboard, and that there is (or at least was) room for getting lean. I like the idea of having metrics to help shape our budget. I think this is essential if we want to operate as an effective organization. 

Unfortunately, I don’t currently have a better recommendation than the metrics you suggested. However, I propose we create our own custom metrics that are better suited for a [protocol sandwich DAO](https://gov.gitcoin.co/t/the-impactdao-protocoldao-sandwich/8944). There are a few things I think we should consider when creating our own custom metrics:

1. AFAIK we don’t have a business model, so comparing us to a web2 company that has a (likely extractive) business model feels off to me.  
2. Our biggest asset, our community, is likely not represented in the business models used to create the metrics you referenced. We definitely need to find a way to account for the value our community provides when creating our metrics. 
3. Perhaps we can find similar ratios/metrics for community focused/non profit businesses.

I’m looking forward to continuing progress on this conversation because I believe it is foundational to our success.

-------------------------

michaelgreen06 | 2022-08-03 22:59:52 UTC | #15

Great post @Fishbiscuit !!

I didn’t read it until after I posted mine.

Thanks for doing some of the work to address the points that I made!

-------------------------
