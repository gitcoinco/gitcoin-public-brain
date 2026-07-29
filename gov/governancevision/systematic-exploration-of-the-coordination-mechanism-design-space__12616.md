---
id: 12616
title: "Systematic Exploration of the Coordination Mechanism Design Space"
slug: systematic-exploration-of-the-coordination-mechanism-design-space
category: governancevision
url: https://gov.gitcoin.co/t/systematic-exploration-of-the-coordination-mechanism-design-space/12616
created_at: 2023-01-21T03:18:02.364Z
last_posted_at: 2023-09-18T16:48:55.752Z
posts_count: 23
views: 9057
like_count: 68
---

# Systematic Exploration of the Coordination Mechanism Design Space

<https://gov.gitcoin.co/t/systematic-exploration-of-the-coordination-mechanism-design-space/12616>
shreyjaineth | 2023-01-21 03:23:15 UTC | #1

# Systematic Exploration of the Coordination Mechanism Design Space

Shrey Jain and Kevin Owocki 

Gitcoin recently released Grants Stack, which is a set of modular tools that act as the scaffolding for any capital allocation construction. It acts as a structure to modularize all components of grants into standardized open-source modules for any DAO. It is with this modularity that any Grants module can slip-n-out of any Grants program without hurting the rest of the funding stack. 

In traditional organizations, it is very challenging to replace governance mechanisms with new ones, even if the members that make up the organization desire a new tool. The modularity of governance mechanisms seen with the Gitcoin Grants stack enables iteration on such mechanisms that human coordination has never experienced. 

With all of these new tools, a question remains, what combination of modules is right for our community? 

Of course, Gitcoin is known for Quadratic Funding (specifically, pairwise Quadratic Funding), but what other coordination mechanisms could be built into Grants Stack.

This post aims at providing a pragmatic approach on how Gitcoin can run an experiment to better understand which mechanisms work for different types of communities. 

## **Hyperparameter sweep on coordination mechanisms**

In machine learning, a [hyperparameter sweep](https://en.wikipedia.org/wiki/Hyperparameter_optimization) is the process of training machine learning models with various different values of hyperparameters (learning rate, activation functions, training data size, etc.). For a given model, the calibration of one set of hyperparameters may work very well in one context but very poorly in another.

We want to apply this concept to figuring out what models of coordination mechanisms work best in a given community. There are many different types of mechanisms that can be used for resource allocation, some of which include: quadratic funding, MACI quadratic funding, cluster-wise quadratic funding, subscriptions, demurrage, dominant assurance contracts, ranked-choice voting, and much more.

Gitcoin founder Kevin Owocki and Giveth founder Griff Green recently did a podcast in which they discussed ~30 Coordination mechanisms [[link]](https://medium.com/giveth/coordination-mechanisms-notes-from-a-conversation-with-griff-green-kevin-owocki-af95f3e831b1). The mechanisms listed in this podcast could serve as a backlog of mechanisms that could be built into Grants Stack.

**![|265x372](upload://oNjuVHCW66CRUElfDRQBHSGHGYa.jpeg)**

A parameter sweep for coordination mechanisms would first require us to build all of the various different mechanisms that could be incorporated into an upcoming Grants round.

We could then run simulated rounds on each of these different combinations to see how capital is allocated and determine what mechanism is most optimal for a given setting.


![|624x321](upload://cCoHDihsrqtfngeI92Evc0ZAhfp.jpeg)


The creation of these simulated rounds and the testing of which ones meet the heuristic of funding our shared needs, is essentially exploring the fitness landscape within this search space.

Once the fitness landscape is mapped, we could then look for the global maxima of coordination mechanisms that help us meet the heuristic.

Of course, different communities will have different value sets so they will have different fitness landscapes. Part of the exploration of this design space will mean figuring out different types of communities and how they define their heuristics of what they want to fund.



![|624x348](upload://5gIZTPBqxxrCIcwN22q5cZHOvU4.jpeg)

Right now, we know that the fitness landscape for the Ethereum ecosystem (Grants v1 explored this design space) looks kind of like this:

![|624x347](upload://3NF0oCa9mH8S8tDlNJL1Wt3Un9u.jpeg)

# Future Work

If there is consensus that this is a direction of research that is worth exploring, then we recommend that

1. GitcoinDAO create a prioritized backlog of coordination mechanisms to be built
2. Gitcoin’s community of developers can build these coordination mechanisms
3. Simulated Rounds will be run on top of these coordination mechanisms
4. We will have started to traverse the design the design space of coordination mechanisms
5. (Repeat 1-4 in an [OODA loop](https://community.supermodular.xyz/t/ooda-loops-for-fun-profit/133) until we’ve fully traversed the design space)

In addition to the process we outline to determine a given social spaces coordination global maxima, we can reference the many tools created by https://metagov.org/ and https://www.radicalxchange.org/ along with what we can expect to see from https://supermodular.xyz/.

-------------------------

DisruptionJoe | 2023-01-21 14:05:56 UTC | #2

This is a great post. I think the most under-rated metric for the Grant Stack UI is number of permutations of a [Funding Stack](https://gov.gitcoin.co/t/the-grants-2-0-funding-stack-choose-your-own-algorithm/10770) available. 

This slide still represents the functions where I see opportunities for experimentation and DevRel focus. Keeping the protocol unopinionated, but easily compatible with unique funding stacks should be a high priority.

![Gitcoin Weekly Workstream update (4)|690x388](upload://szE7GfGggrPyMwwHoXFe9TzxwgJ.jpeg)

Each funding stack function has some tradeoffs. In experimentation, it will be important to recognize the consistency of the other functions. Simulation is a great way to do this.

Here are some of the tradeoffs I am aware of:

**Funding Mechanism**
- Taxation by fees vs Inflation
- DeSoc Incentivization of outgroup collaboration vs centralizing over time
- Sybil

**User Moderation**
- Universal (more errors, but economy of scale benefits) vs customized (pluralistic, but more costly) 
- Gating & weighting (Creates systemic inequality which compounds over time) vs squelching (This is giving a 0 weight coefficient AFTER the vote is cast) 
- Closed vs Open (Don't let the attackers know your secrets vs Kerckoffs principle) 

**Grant Moderation**
- Programmatic filtering on specific data points (universal)  vs community scoring using aggregated data points (pluralist) 
- Eligibility Reviews: Delegated authority (single point of failure, but cost efficient) vs intersubjective consensus (Like polis or ethelo). I HIGHLY believe that although delegated authority is more costly today, once a pluralistic review protocol is bootstrapped, it will provide minimum necessary decentralization for each community to trust the reviews at a lower cost per review. 
- Crowdsourcing disputes and appeals: Incentivized (consistent, but likely to be gamed) vs UX driven (altruistic, but may not decentralize enough to be incorruptible)
- Appeals: Delegated authority vs decentralized and/or intersubjective consensus
- Eligibility Policy Evolution: Does the appeals judge use letter of the law and an appeal must change the law to overturn a decision that wasn't an error in application of the law or a gray/novel interpretation? Or does the judge have freedom to judge the case as is and the legislation should consider legislative updates? 

**Grant & Round Discoverability**
- Capital based decisions for social consensus based decisions

-------------------------

epowell101 | 2023-01-21 18:17:37 UTC | #3

Thanks for this.  Extremely exciting to see the design space open up here enormously.  Actually running a permutation sweep seems like a great idea based on what I know as a way to learn - in the open - about these alternatives in action.  

@DisruptionJoe comment goes some way towards addressing the question I have concerning running something like a parameter sweep across the permutations - the importance of the humans in the communities being able to grok the alternatives would seem to put a significant burden on DevRel and other teams.

Joe from his work can immediately cite the key trade-offs -> however wouldn't we need to undertake or seed or otherwise support an extensive education effort so that something approaching this level of knowledge is much more widespread than it is today?

I guess I can imagine a lot of useful Green Pill episodes for example - much like @owocki helped many understand the inevitability of Sybils and the impossibility of solving them once and for all and much else - would you envision a similar series doubling down on the podcast w/ @griff ?

And that would need to just be a piece of a plan IMO to engage stakeholders and elevate everyone's understanding such that they can internalize and act upon the results of this parameter sweep.  

Anyway - seems like a great idea to me, assuming we can figure out how to wrap around the experiments excellent DevRel & explanations & more.  Thanks for thinking it through and writing it up!

-------------------------

owocki | 2023-01-21 19:22:14 UTC | #4

(hi from [supermodular](https://gov.gitcoin.co/t/supermodular-xyz-2023-roadmap/12263) - commenting here to explore the design space stimulated by @shreyjaineth 's comment at Pluralism summit to me "what if we did a hyperparameter sweep across all coordination mechanisms"? for data gathering purposes! )

[quote="DisruptionJoe, post:2, topic:12616"]
![Gitcoin Weekly Workstream update (4)](upload://szE7GfGggrPyMwwHoXFe9TzxwgJ)

Each funding stack function has some tradeoffs. In experimentation, it will be important to recognize the consistency of the other functions. Simulation is a great way to do this.
[/quote]

this is a great graphic.  @shreyjaineth joe's post makes me think the hyperparameter sweep of all coordination mechanisms could sweep all possible parameters (joe lists some important ones below) across **[funding mechanism] x [passport rules] x [grant eligibility ] x [ui discoverability]**.

one thing i think thatll be an important design criteria from the start is the "cost" of running a simulated round.

when you have low cost you can sweep parameters fast.  when you have high cost you sweep parameters very slowly and costlyly.  those who know me know i like to spin my [OODA loops](https://community.supermodular.xyz/t/ooda-loops-for-fun-profit/133/2) fast! 

i can see four types of rounds (one real + three simulated):

0. *[high level of effort]* - **live** - real humans doing their JTBDs
1. *[medium level of effort]* - **simulated + human action needed** - data created by real people, staffed by someone who wants experimental data results 
2. *[low level of effort]* - **simulated + computer agent action** - data created by simulated people, staffed by someone who wants experimental data results 
3.  *[very low level of effort]* - **simulated + data analysis** - takes data created by rounds types 1 and 2 and tries to derive new analytic insights from them. 


[quote="epowell101, post:3, topic:12616"]
- the importance of the humans in the communities being able to grok the alternatives would seem to put a significant burden on DevRel and other teams.
[/quote]

i'm just one node in the network, but if Grants Stack helping communities to reach the "Global Maximas" of Coordination is important to it's partners, or is important as a USP, then IMO it follows that articulating the value of all the permutations = articulating the value proposition of Grants Stack. 

insofar as anyone else who would be pursuing such a strategy (hopefully they'd just build on Grants Stack instead), no other web3-era grants software suite is going be such a swiss army knife.  .

i dont mean to push you in one way or another tho...

(hey - what is Grants Stacks USP by the way? USP = Unique Selling Proposition.  maybe @CoachJonathan and @Viriya know) 


[quote="epowell101, post:3, topic:12616"]
however wouldn’t we need to undertake or seed or otherwise support an extensive education effort so that something approaching this level of knowledge is much more widespread than it is today?
[/quote]

i think explaining Quadratic Funding is kind of complicated, so i have a lot of empathy for how hard it is to educate people about these mechanisms.  

over time i've learned to create [explainer videos](https://www.youtube.com/watch?v=HJljTtLnymE) or show live examples to people is one of the easiest way to explain the mechanisms.

but is the juice worth the squeeze?  i can't say, it's really up to MMM/GPC.  it probably deeply depends on the USP of Grants Stack.  some options i've heard flying around on twitter.
1. Is the USP for Grants Stack that its a grants program that grows with you?  
2. That Grants Stack =  the simplest way to administer grants?  
3. Is it Grants Stack = easy Quadratic Funding?  
3. Is it Grants Stack = easy Retroactive Public Good Funding?  
4. Or is Grants Stack more like Wordpress, a minimal tool with an active developer community around it and lots of plugins that can be built in to extend it?

assuming the juice is worth the squeeze @epowell101  , how do you think the educational efforts should differ from, or build upon, work like [this 2 hour](https://medium.com/giveth/coordination-mechanisms-notes-from-a-conversation-with-griff-green-kevin-owocki-af95f3e831b1) episode on coordination mechanisms @griff and i did (and the article the giveth team made shortly thereafter).  i know @ccerv1 had some ideas about how to organize that content too.

when Gitcoin first launched we launched [https://wtfisqf.com/](https://wtfisqf.com/), to show off the power of Quadratic Funding to people.  perhaps a microsite like that could be useful here too.

we've actually done a few greenpill episodes on collective intelligence / coordination mechanisms come to think of it.  this is primarily because i find the concepts of collective intelligence intellectual fascinating and think them to be one of the great promises of web3...    as the meme goes [its all coordination](https://www.youtube.com/watch?v=KpXPym_m_wA)..

if there are any coordination mechanism deep dives you think we should do, let me knew.  

pasting a few such episodes below

https://www.youtube.com/watch?v=qyd7mvQmn5I

https://www.youtube.com/watch?v=gQ4rEa9ULOo&list=PLmkdAgtxf3ah0Vmyy1B3OU8BPacX4_gVY&index=23

https://www.youtube.com/watch?v=L54lcwjUYzM&list=PLmkdAgtxf3ah0Vmyy1B3OU8BPacX4_gVY&index=5

https://www.youtube.com/watch?v=Bzpcrp3-dHU&list=PLmkdAgtxf3ah0Vmyy1B3OU8BPacX4_gVY&index=73

https://www.youtube.com/watch?v=2RSf2bRiieU&list=PLmkdAgtxf3ah0Vmyy1B3OU8BPacX4_gVY&index=63

-------------------------

DisruptionJoe | 2023-01-21 19:43:02 UTC | #5

[quote="owocki, post:4, topic:12616"]
i can see four types of rounds (one real + three simulated):

0. *[high level of effort]* - **live** - real humans doing their JTBDs
1. *[medium level of effort]* - **simulated + human action needed** - data created by real people, staffed by someone who wants experimental data results
2. *[low level of effort]* - **simulated + computer agent action** - data created by simulated people, staffed by someone who wants experimental data results
3. *[very low level of effort]* - **simulated + data analysis** - takes data created by rounds types 1 and 2 and tries to derive new analytic insights from them.
[/quote]

The prioritization through impact and feasibility here is great. I think the entire community can help and that this is likely something the Open Data Community will be perfectly set up to execute! 

I see the OODA loop your refer to involving the following pieces:

* Crafted experimentation using the Gitcoin Program - Based on business intelligence and understanding of optimal capital allocation
* Prioritized wish lists for DevRel to help get built - Based on business intelligence combining our highest impact levers and our program managers most pressing needs
* Simulation experimentation where funding mechanism code can basically be swapped from simulation to live round calculations with ease

I'm sure there are plenty of others. Exciting time to be building Supermodular on the Gitcoin ecosystem. 

I also just posted this [growth and revenue forecasting model](https://gov.gitcoin.co/t/an-interactive-model-for-gitcoin-revenue-growth-forecasting/12625).

![Image 2023-01-21 at 6.44.23 PM (1)|690x334](upload://5un5BXaQ7e1CySOWmaYBXyEKLNH.jpeg)

-------------------------

owocki | 2023-01-21 23:39:13 UTC | #6

[quote="DisruptionJoe, post:5, topic:12616"]
I see the OODA loop your refer to involving the following pieces:

* Crafted experimentation using the Gitcoin Program - Based on business intelligence and understanding of optimal capital allocation
* Prioritized wish lists for DevRel to help get built - Based on business intelligence combining our highest impact levers and our program managers most pressing needs
* Simulation experimentation where funding mechanism code can basically be swapped from simulation to live round calculations with ease
[/quote]

IMO the loop looks somewhat like the scientific method.

1. Someone has a testable hypothesis.
2. They run an experiment to validate the hypothesis. 
3. They gather the results.
4. They disseminate learnings.
4. (repeat with updated information)

Or put into an OODA loop language:

1. They **observe** a need in market
2. They **orient** about how Grants Stack + other money legos could meet that need.
3. They **decide** to run a test.
3. They **act** to execute the test.
4. (repeat)

I'm not sure how this jibes with your thought below, maybe like this?
1. the experimentation or simulation = decide/act.  
2. the business intelligence + prioritized wish list = orienting?

-------------------------

llllvvuu | 2023-01-22 02:31:46 UTC | #7

[quote="owocki, post:4, topic:12616"]
i think explaining Quadratic Funding is kind of complicated, so i have a lot of empathy for how hard it is to educate people about these mechanisms.

over time i’ve learned to create [explainer videos ](https://www.youtube.com/watch?v=HJljTtLnymE) or show live examples to people is one of the easiest way to explain the mechanisms.

but is the juice worth the squeeze?
[/quote]

My thoughts on education:

I don't think it's necessary to push users to learn a lot about the protocol, because most people just want to use it. In this regard, I think the way Alpha Round works right now is actually fine; it only namedrops QF once and I'm not even sure that's necessary - it could also easily say something to the effect of "sponsors will amplify your donation ([how does this work?](https://wtfisqf.com/?grant=&grant=&grant=&grant=&match=1000))".

Similarly, I don't feel like passports need to namedrop stuff like "Sybil attacks" and "voting power" - the concept of identity verification should be self-explanatory (there can be a link for "how can people cheat the system?" to learn more).

A barbell strategy could be good I think. For a minority of the population - the skeptics and power users - they should be able to see in excruciating detail and dryness documentation of all the rationale, math proofs, attack analyses, open problems and research directions, etc. This is because this small minority [can disproportionally drive](https://sloanreview.mit.edu/article/the-user-innovation-revolution) marketing, ideas, feedback, etc. But the average user doesn't need any of this. They don't even need to know what the word "quadratic" means.

-------------------------

DisruptionJoe | 2023-01-22 09:33:37 UTC | #8

[quote="owocki, post:6, topic:12616"]
Or put into an OODA loop language:

1. They **observe** a need in market
2. They **orient** about how Grants Stack + other money legos could meet that need.
3. They **decide** to run a test.
4. They **act** to execute the test.
5. (repeat)
[/quote]

Good question. All three are good starting points for sparking the fire. 

The first two are Orient stage. There will likely be multiple OODA loops running in parallel. Some will be within a workstream and some between.  

1. The Grants Program has the ability to **observe** and understand all the rounds, in and out, of the program with the help of business intelligence / Open Data. They can then **orient** around what tests might reveal a most impactful learning, **decide** on an experiment to run in the Gitcoin Program, and run the test (**action**). Most other programs aren't likely to have multiple rounds active, the technical ability to run a/b tests within and between rounds, or the deep understanding of the Gitcoin team. 

2. The wishlists for DevRel might be orientation derived from **observations** made primarily by program managers. It might be something like, "Reviewing grants at scale is costly and difficult to be consistent." DevRel can now include this in a backlog of cool things to build. At the same time, business intelligence might do an assessment of each backlog item's potential impact, thus **orienting** the decentralized community on what the top priority builds are. It is up to the community to **decide** what to build, but we are more likely to get useful builds (**action**) if the devs know what is needed, how much impact it could have, and support when they need it. 


3. This one is more about the simulation & hyperparameter sweeps. Lets say you keep all funding stack functions constant except for the funding mechanism. We generate synthetic data and run millions of simulations to better understand what mechanisms are directional good ideas. You might consider this the entire OODA loop, or maybe a sub-loop of a larger loop. This "sub-loop' is simply the process that orients in the larger loop which then goes and tests the finding in a live grants round. Containerizing the code with some standardization could allow for this larger OODA loop to run faster.

-------------------------

llllvvuu | 2023-01-23 09:21:49 UTC | #9

[quote="owocki, post:4, topic:12616"]
Or is Grants Stack more like Wordpress, a minimal tool with an active developer community around it and lots of plugins that can be built in to extend it?
[/quote]

This sounds right, unless Gitcoin wants to dedicate resources to building, testing, iterating on, and documenting ~30 coordination mechanisms in-house (and surely there will be more in the future). 

We could also reason that such a developer community would also be a user community and take a lot of the OODA loop into their own hands. (e.g. suppose a Grants Protocol user were to develop a "HyperCerts" plugin, they would likely have their own report of the data, insights, etc - with ODC tools and support). Of course, Gitcoin would still need to have a head of plugins, to lead SDK, curation, collaborations, etc. For "front-page" plugins we might even want to forward deploy resources to make sure they are very well polished and documented.

-------------------------

DisruptionJoe | 2023-01-23 13:15:11 UTC | #10

Yes. This is exactly on point with how I've been envisioning it. Not to say there aren't other correct ways, but the way I see is basically this with a subtraction mindset as a first principle. If there is a private business market that can sustain an effort, then Gitcoin shouldn't be the one doing it. Gitcoin should focus on the ecosystem's public goods - continually improving infrastructure, composability/compatibility, education, and extracting lore from the successes within the ecosystem. 

Mutual grant investments in spinouts from workstreams would let us capitalize on this and perhaps accelerate the rate at which sustainable businesses are available. It would be like Gitcoin building a city with roads, plumbing and electricity, but there are no grocery stores or gas stations. We could subsidize their path to sustainability and potentially invest in them, but when a new company comes around wanting to own gas stations and grocery stores, we would likely have to divest at that time. How would we set this community trigger? By GTC holders telling us when!!!

-------------------------

J9leger | 2023-01-23 21:11:50 UTC | #11

Appreciate the conversation here. These concepts of the possibilities of building on the protocol is what makes the Allo protocol so exciting and why we're working hard to launch it as soon as possible. 

[quote="owocki, post:4, topic:12616"]
insofar as anyone else who would be pursuing such a strategy (hopefully they’d just build on Grants Stack instead), no other web3-era grants software suite is going be such a swiss army knife.
[/quote]

GPC is actively working to build every module in a flexible way for people to easily see opportunities to build additional elements, such as alternative funding mechanisms or grant review processes etc. 

First, we're working toward having runbooks for QF rounds on the protocol and info for how to build on the protocol by March. 

Ideally then, as a step 2, everyone who wants to build can test the protocol whether diving in and running full QF rounds or going in and running a small "simulated round" similar to what [Gitcoin did in December](https://gov.gitcoin.co/t/grants-protocol-simulated-rounds-post-op-summary/12609) to learn about the grants stack flow. Dev's could run simulated rounds to get a sense of where there is opportunity to build, what mechanisms they are most excited about and want to build and go from there without Gitcoin prescribing what people should build and how. 

This means @owocki you can spin your OODA Loops as fast as you want and the broader community gets to benefit from it.

-------------------------

PaigeDAO | 2023-01-24 11:13:29 UTC | #12

Listening now. 
Thank you for all this informative content!

-------------------------

ceresstation | 2023-01-24 17:12:14 UTC | #13

> In machine learning, a [hyperparameter sweep](https://en.wikipedia.org/wiki/Hyperparameter_optimization) is the process of training machine learning models with various different values of hyperparameters (learning rate, activation functions, training data size, etc.). For a given model, the calibration of one set of hyperparameters may work very well in one context but very poorly in another.

Really love the idea of running an experiment like this, I've actually been talking to [Artizen](https://artizen.fund/) and a few others about participating in something like this.

One trade-off space I've been thinking a lot about is between fully centralized expert decision-making and fully decentralized community decision-making.  This work has already been started at a small scale by Vitalik in the context of his review of [retroPGF](https://vitalik.ca/general/2021/11/16/retro1.html), which does a good job outlining how the current pairwise QF model seems to find a greater breadth of projects in a given domain, but possibly with lower average relevance (as defined by some domain expert).

If we understand this space well then we can start to define how experts *interact* with community mechanisms in a way that helps us expand the boundary of how effective these mechanisms can be (which could pair well with existing work on [hypercerts](https://research.protocol.ai/publications/generalized-impact-evaluators/)). 

>Part of the exploration of this design space will mean figuring out different types of communities and how they define their heuristics of what they want to fund.

As @J9leger mentioned we're actively working to launch the protocol which means we can start to help source some of these heuristics and map out the spaces to run through in the simulated rounds. Let us know what the next steps / ideal timeline would look like to help on this front!

-------------------------

DisruptionJoe | 2023-01-25 10:56:59 UTC | #14

[quote="llllvvuu, post:9, topic:12616"]
This sounds right, unless Gitcoin wants to dedicate resources to building, testing, iterating on, and documenting ~30 coordination mechanisms in-house (and surely there will be more in the future).
[/quote]

This is an interesting discussion. I've recently been presented a viewpoint that no one wants to deal with this Wordpress like system. What works now are things like Medium, Substack, or maybe Mirror in web 3. Systems that just work. 

My counter was that in the timeline for democratization of INFORMATION, we needed a Wordpress for us to accelerate the evolutionary trials which eventually brought us to a state where we know what the best ways for communities to distribute information is. However, in the progression of democratization of VALUE, we still need the system that crowdsources the intelligence to speedrun the evolutionary process to find which systems work best for us. 

Now do I believe this? I don't even have strong opinions held loosely yet. I'm hoping to hear some good arguments either way here.

What are your thoughts on this?

-------------------------

llllvvuu | 2023-01-25 11:47:25 UTC | #15

[quote="DisruptionJoe, post:14, topic:12616"]
This is an interesting discussion. I’ve recently been presented a viewpoint that no one wants to deal with this Wordpress like system. What works now are things like Medium, Substack, or maybe Mirror in web 3. Systems that just work.
[/quote]

I'm sympathetic to this viewpoint. And I'm also sympathetic to the evolutionary argument you make further below. Maybe Gitcoin doesn't have to quite be Medium, because it's not as B2C. A middle ground could be investing heavily in DevRel or even forward deploying. So like suppose a Grants Protocol user wants to do an experiment on some variant of Hypercerts and there isn't a plug-in for it yet. Gitcoin could deploy a few engineering hours to help them build that out and then they could take over in terms of administering it and collecting and analyzing the data. And we can talk about how to make that sustainable (is it a bespoke thing Gitcoin charges for or is it already included in the support plan for paying protocol users).

-------------------------

octopus | 2023-02-05 01:52:55 UTC | #16

I would like to suggest a few possible ideas for this:

Overall, my concern is about too small a set of pre-selected mechanisms being explored, and computation/simulation being used where analysis gives more insight.

The paper that proves "QF is optimal" explicitly states that the assumption for the math problem is that unique identities are enforced, i.e. no sybils. Since that isn't the real world in which GitCoin operates, implementing QF has required a huge Sybil resistance cost. 

Here are a few ideas:

1. There are known sybil-resistant distribution mechanisms in literature; there's a recent paper that discusses them. Try incorporating some of these?

2. Having the community design a small test set of situations, which are of most interest. Human understanding/comfort are an important metric which can't show up in simulations. 

3. I'd like to suggest one concrete metrics for exploring the mechanism space.

Mechanism alpha: Suppose we have a funding mechanism F(x) that takes a vector x of contributions and returns a number (which is then used to determine funding allocations by taking the proportion of that number compared to other numbers). 

Let w be the vector (1.0/n) * np.ones(n).

One thing to look at would be F(w)/F((1.0,))

In other words, how much more does a project get for N contributions of 1.0/N, compared to a single contribution of 1.0?

For regular Quadratic Funding, this ratio grows like N, which makes sybils incredibly attractive. For 1Token1Vote (regular "total" voting), this ratio is constant, which gives no difference for popular support. Measuring this for a proposed metric shows how attractive making a larger Sybil would be.

-------------------------

griff | 2023-02-05 16:55:26 UTC | #17

I really like the concept of building in an interoperable way, that makes it easy to allocate funding to projects. The key pieces here are the Registry and Sybil protection. Getting those solid, and designing & documenting the interfaces well will be the keys to success IMO.

It shouldn't be on Gitcoin alone to build this stack, we should lock down our core pieces and then let the other open source devs go wild with using it! One issue tho.... the sybil protection is seemingly still very difficult to use.

For example, GM is developing [Pairwise](https://pairwise.generalmagic.io/) and I think once we solidify some funding integrating the registry and passport is a no brainer to be on the roadmap.... but how do we (and any other group) integrate the post-round sybil analysis?

How does a group get that done? What would/could/should that look like? Is it a paid service from GitcoinDAO... ?

-------------------------

dazzsherly | 2023-02-10 13:06:44 UTC | #18

Great stuff thanks for sharing

-------------------------

nikete | 2023-02-10 15:07:05 UTC | #19

One line of attack for exploring the mechanism design space around quadratic funding is how special is the quadratic really? So exploring the functional parametrization of the mechanism.  Since the underlying task seems like it can be cast as belief elicitation (where those beliefs are about preferred states of the world) I conjecture that you can replace the pairwise quadratic with any other proper scoring rule and get a mechanism that is better in some situations and worse in others (where different proper score rules correspond to different prior beliefs in some sense). For something with a related flavor, see https://arxiv.org/pdf/2302.00196v1.pdf

-------------------------

DisruptionJoe | 2023-02-14 00:29:30 UTC | #20

I really appreciate you taking the time to share your expertise here. Thank you. 

Here is an under visited thread with direct recommendations for others who are monitoring this thread: https://gov.gitcoin.co/t/tax-mechanisms-for-gitcoin-grants/12764?u=disruptionjoe

-------------------------

owocki | 2023-09-17 23:04:54 UTC | #21

Reviving this topic now that Allo Protocol v2 is approaching launch.

I wonder in what ways we might prioritize the creation of Allo Strategies for some of the ideas in this thread. 

Allo v1 uses Quadratic Funding to allocate capital. Allo v2 could use many different ones.. but which ones should we prioritize first?

I think it makes sense to prioritze the ones with the largest TAMs in web3 for now.  And especially the ones where there is an unmet need in the market.  

It may also make sense to weight simpler mechanisms first.  More complex mechanisms requiring oracles for examples, we might want to sequence in a later iteration.

-------------------------

jengajojo | 2023-09-18 06:46:30 UTC | #22

If the DAO is being conservative with it's capital, then it's best to prioritize those strategies which have the highest potential for usage immediately after deployment. Maybe there can be an initial market research with existing partners on which strategies maybe immediately relevant or which problems do we predict each of the strategies solve and cross reference those with the problems highlighted by the partner communities.

-------------------------

PaigeDAO | 2023-09-18 16:48:55 UTC | #23

This is probly not the correct thread to add this to (please advise) but wanted to respond to @jengajojo and also pick up on the note in today's newsletter by @gaoa97 about @owocki open to hearing about Gitcoin-related projects to dig his hands into for this next phase his participation. And would like to loop in @kyle and also @Viriya and @CoachJonathan ...

Janine mentions here above about Gitcoin being 'conservative with its capital'. 

This pipe dream/ proposal is an attempt to imagine RWA investments that could accrue value over time as well as diversify the DAO's / Foundation's holdings. 

It could also very well just be a pipe dream... 


**PROPOSAL: Gitcoin Schelling Point France** 

Firstly, let me say that this is not in any way a competition to Zuzalu. (afaik that's a different, and very cool, vision)


Gitcoin Schelling Point France can be a wholly Gitcoin community ecovillage. 

**WHAT:** In France there are whole villages for sale such as in the S. of France. Yes, they are dilapidated stone buildings and mostly isolated and in need of massive restoration and development. But contrast purchasing a 20 room chateau with the possibility to purchase an entire village for about 3 Million Euro. 

Another possibility would be to invest in a vineyard with its manor and outbuildings which would come with enough property to construct tiny homes across the fields. We could perhaps solicit co-branding for the tiny homes to gather development funds support. The vineyard could be functional and produce wine for the guests and residents. Gitcoiners and their families could reserve in advance to help with the 'vendange' (harvest) each year. 

Pipe dream? 

Perhaps... But @Viriya and I had a good time imagining such a scenario during our conversations at ETHCC in Paris this summer.  

I don't expect that we'd be as successful as, say, Jimmy Buffett's Margarataville resorts (valued at $1B today I believe). But we could work towards that direction. 

If we went towards the EcoVillage concept (not so much the vineyard and winery) then perhaps we could make strategic partnerships with tech companies that would use the village as a tech showcase for remote, self-sustainable autonomy without sacrificing quality of life. Services that come to mind are solar panels, internet connectivity, water purification, vertical gardens. 

I know I am getting carried away here with a Solar Punk vision. Maybe this is simply Gitcoin x Schelling Point France x Solar Punk? 

Like I said above, maybe this is just a pipe dream. But from an investment diversification standpoint, property holds its value, tourism (even if it's eco tourism just for our community of Gitcoiners) will not be affected by AI like other industries, and, hey, who doesn't want to spend time every year in the South of France picking grapes, eating French cheese and teaching your kids how to speak French on Duolinga? 

WDYT?

-------------------------
