---
id: 17201
title: "Overall Learnings from GCP-004 and Gitcoin Citizens Round #2 Results"
slug: overall-learnings-from-gcp-004-and-gitcoin-citizens-round-2-results
category: open-discussion
url: https://gov.gitcoin.co/t/overall-learnings-from-gcp-004-and-gitcoin-citizens-round-2-results/17201
created_at: 2023-11-30T19:41:07.399Z
last_posted_at: 2024-02-13T17:19:18.511Z
posts_count: 6
views: 4399
like_count: 29
---

# Overall Learnings from GCP-004 and Gitcoin Citizens Round #2 Results

<https://gov.gitcoin.co/t/overall-learnings-from-gcp-004-and-gitcoin-citizens-round-2-results/17201>
umarkhaneth | 2023-12-06 16:04:33 UTC | #1

# GCP-004 Overall Learnings and Gitcoin Citizens Round #2 Results

Thank you to @krrisis for co-authoring this post with me and being my dependable partner in crime on the Gitcoin Citizens Round. Thank you also to @shawn16400 for helping us kick this off with the GCP and running round 1 and to @carlosjmelgar for stepping in to help run round 2. 

# TL;DR:

* We tested retroactive and proactive funding and felt more confident in the results of retroactive funding. We plan on sticking to this for future Citizens Rounds.
* We prefer funding individuals to projects because quadratic funding can be monopolized by big brand names with marketing reach.
* We saw massive growth in participating Citizens round-over-round as more people heard about the funding opportunity. Communities who wish to run similar rounds should try to plan to run two or more rounds from the get-go.

## Intro

Following the end of Gitcoin Citizens Round #2, we have concluded our [first GCP](https://gov.gitcoin.co/t/gcp-004-passed-gitcoin-citizens-round/13462) and are reporting back on our main results and learnings from the two rounds.

From the beginning, we set out to run an experiment. We wanted to understand:

- i) can quadratic funding be effectively used to build and support our own ecosystem?
- ii) can retroactive funding increase the effectiveness of quadratic funding?

The answer to both of these questions was a resounding yes, but not without deeper nuance. In this post we’ll briefly explore the lessons we learned from running two QF rounds for Gitcoin and the trade-offs we encountered.

## Round Results

Here’s a quick recap of how the rounds went.

Gitcoin Citizens Round 1 was the first retroQF round, the first Grants Stack round to run on an L2 (Optimism), and the most successful Gitcoin Round to date in terms of crowdfunding versus matching. The crowdfund quadrupled the 20k matching pool and the round distributed over $100k to Gitcoin Citizens. You can read more in this [case study](https://www.gitcoin.co/blog/citizens-round-a-case-study-retroactive-qf) and in our round 1 [results](https://gov.gitcoin.co/t/gitcoin-citizens-round-1-results/16302) post.

For Round 2 we invited our community to not only apply for retroactive funding but also submit planned work, as promised in our [initial GCP](https://gov.gitcoin.co/t/gcp-004-passed-gitcoin-citizens-round/13462). We also made Gitcoin history by distributing matching funding in our native token, GTC. We’re very happy with our [results](https://reportcards.gitcoin.co/424/0x7492a8c4ED29B1F1559888Bd832fAe5D33E10370): 64 projects received $14,692 in donations from 1350 unique donors. In the process, they decided how we would distribute a matching pool of 22,232 GTC. Big thanks to @owocki who increased the matching pool by 50% by donating 4.20 ETH.

## Can quadratic funding be effectively used to build and support our own ecosystem?

It is *surprisingly easy* to launch a QF round on Grants Stack in a few minutes. In the cGrants days (just 14 months ago), the only way to launch a QF round was to be a developer with backend access to our system. That is so different from today. Anyone can do it in a few clicks. Hats off to the incredible Allo team that lays the critical foundation and the Grants Stack team that makes it usable.

Now, on to the nuance.

### Did quadratic funding effectively identify what should be built and supported within our own ecosystem?

This is really subjective. Here’s our personal stance: mostly no in round 1 and mostly yes in round 2.

When we initially kicked off the Gitcoin Citizens Round, it was after observing that there were many members of our community who were doing fantastic work and did not have a pathway to being funded for this work. We wanted to create that for them and also for anyone else who may come along. Those individuals (who we even specified as great examples [in our proposal](https://gov.gitcoin.co/t/gcp-004-passed-gitcoin-citizens-round/13462) to run a Citizens Round) were: @jon-spark-eco, Carlos Melgar, and Carl Cervone. Unfortunately, they did not place close to the top of the Round 1 QF matching distribution.

|Rank|Round 1|Round 2|
| --- | --- | --- |
|1|[Karma](https://explorer.gitcoin.co/#/round/10/0x984e29dcb4286c2d9cbaa2c238afdd8a191eefbc/0x984e29dcb4286c2d9cbaa2c238afdd8a191eefbc-30)|[Gitcoin Grants Data Portal](https://explorer.gitcoin.co/#/round/424/0x7492a8c4ed29b1f1559888bd832fae5d33e10370/0x7492a8c4ed29b1f1559888bd832fae5d33e10370-85)|
|2|[Biteye](https://explorer.gitcoin.co/#/round/10/0x984e29dcb4286c2d9cbaa2c238afdd8a191eefbc/0x984e29dcb4286c2d9cbaa2c238afdd8a191eefbc-25)|[GITCOIN DIGEST](https://explorer.gitcoin.co/#/round/424/0x7492a8c4ed29b1f1559888bd832fae5d33e10370/0x7492a8c4ed29b1f1559888bd832fae5d33e10370-83)|
|3|[Bankless DAO's Gitcoin Citizens](https://explorer.gitcoin.co/#/round/10/0x984e29dcb4286c2d9cbaa2c238afdd8a191eefbc/0x984e29dcb4286c2d9cbaa2c238afdd8a191eefbc-32)|[Joel Miller - Next Gen QF](https://explorer.gitcoin.co/#/round/424/0x7492a8c4ed29b1f1559888bd832fae5d33e10370/0x7492a8c4ed29b1f1559888bd832fae5d33e10370-73)|
|4|[Bankless Academy](https://explorer.gitcoin.co/#/round/10/0x984e29dcb4286c2d9cbaa2c238afdd8a191eefbc/0x984e29dcb4286c2d9cbaa2c238afdd8a191eefbc-16)|[Kris' Work as Citizens Round Operator](https://explorer.gitcoin.co/#/round/424/0x7492a8c4ed29b1f1559888bd832fae5d33e10370/0x7492a8c4ed29b1f1559888bd832fae5d33e10370-112)|
|5|[Dune Dashboard - Proof Of Stake by Vitalik Buterin](https://explorer.gitcoin.co/#/round/10/0x984e29dcb4286c2d9cbaa2c238afdd8a191eefbc/0x984e29dcb4286c2d9cbaa2c238afdd8a191eefbc-39)|[Memes for Gitcoin](https://explorer.gitcoin.co/#/round/424/0x7492a8c4ed29b1f1559888bd832fae5d33e10370/0x7492a8c4ed29b1f1559888bd832fae5d33e10370-41)|

*Table 1: Top 5 projects by round*

Was this because the community didn’t find their work valuable? No, if you ask many of the people at Gitcoin who have the highest-context then the work they did was universally incredibly valuable. However, what’s at play are the two biggest weaknesses quadratic funding faces in correctly determining where funds should go:

* Farmers & Attackers
* Grantee Awareness

**Farmers & Attackers:** Citizens Round 1 was Gitcoin’s first retroactive funding round and it ran on Optimism. Airdrop farmers were so hopeful! It was still surprising just how many showed up. Of the over 17k donors we know more than half were airdrop farming. In the process of farming the round they donated a lot of funding to Gitcoin community members but they also skewed the matching distribution.

**Grantee Awareness:** Given QF’s democratic/populist nature it’s difficult for lone individuals to compete with projects that hold as much brand recognition, marketing reach, or monogamously loyal supporters as Bankless or Biteye.

We took these lessons from Round 1 and adapted our strategy for Round 2. It’s also worth celebrating that, now, Jon and Carlos are Gitcoin Core and Carl is our largest external steward (by tokens delegated).

Moving into Round 2, we took a different approach. **We decided to limit the eligibility to individual efforts and exclude team projects.** We hoped this would reduce the ability of large brands to monopolize funding and more directly compensate those creating value. This ended up working well. The top projects in Citizens Round 2 are not only high-quality but the value they’re creating for Gitcoin is extremely tangible: from developing better QF algorithms, to building open grants funding databases, crafting our newsletter, cooking our dank memes, and even running our Citizens Round.

Our goal was to fund the people that create value for the Gitcoin Ecosystem. While more specific and tailored eligibility criteria certainly helped with this, it’s worth noting the following:

- a) We had clear examples of the types of grants we wanted to fund (essential to improving eligibility criteria)
- b) Our second round was much less attacked than our first one (in fact our number of unique donors declined 90% to 1350 – much more reasonable)
- c) We utilized [cluster-matching QF](https://x.com/gitcoin/status/1717192595003097279?s=20) which greatly mitigated the effect of a number of sybils and PGN airdrop-hopefuls while boosting the grantees who had diverse support.

Further analysis of the donors after payouts determined there were still some sybil attackers/airdrop farmers who received matching on their donation. Continuing to improve how we determine which wallets receive matching is extremely important to funding the projects which have authentic support.

There is likely also room to experiment with different methods of improving the quadratic funding outcomes, such as by encouraging or incentivizing the participation of our highest-context community members. One such experiment could involve airdropping Gitcoin core members funding with the express purpose that they use it to donate to the round.

### Can quadratic funding be effectively used to build and support our own ecosystem?

One of the most telling indicators that the answer to this question is a yes is the increase we saw in builders. **We received and accepted almost twice as many applications in Round 2 while decreasing our acceptance rate.**

![|624x404](upload://mGgFSkPxuyjkzJZiwcAcGYzsl9I.png)

||Acceptances|Applications|Acceptance Rate|
| --- | --- | --- | --- |
|Round 1|33|60|0.55|
|Round 2|64|135|0.47|
|Percent Difference|93.94%|125.00%|-14.55%|

Table 2: Project Acceptances, Applications, & Acceptance Rate, Round 1 vs. Round 2

It’s captivating to see so much growth RoR. One grantee told us “I only heard about the Citizens Round after Round 1 had ended” and another said that when they found out about the Citizens Round “It was in the middle of donations last time and I decided I’d apply to the next one.” We believe that continuing to run more rounds will continue to increase the quantity and quality of builders in the Gitcoin ecosystem.

> One lesson for other communities is that you should probably try to run multiple rounds from the get-go. Your experience will likely be better because you’ll be able to iterate on eligibility criteria and more builders will be drawn to your ecosystem in round 2 after hearing about round 1.

It’s also worth noting the growth is accelerated by the diversity of acceptable contributions to our round. We did not limit the round to particular types of contributions such as open-source software or education. As a result, we were able to fund governance with Jengajojo, AI solutions such as Rohit with GrantsScope, community-building such as Cori at Regens Unite, and many more. We fund value creation for our ecosystem, whatever form it takes.

## Can retroactive funding increase the effectiveness of quadratic funding?

As we stated in our initial proposal, we planned on running an experiment with our first two rounds. One [fully retroactive round](https://gov.gitcoin.co/t/gitcoin-citizens-round-1-results/16302), with inspiration from Optimism’s RPGF, and one standard round.

Our first round, being retroactive, made it easy on us as reviewers to deny applications from those projects who hadn’t yet done anything.

We ran our standard round after our retroactive round. During this round, when reviewing both retroactive and proactive applications, **we felt much more confident when admitting applications that already had work completed**. We also felt much better about funding these submissions compared to those submissions that were requesting funding for work they *might* do.

One concern we had with retroactive funding and that drove us to also test a standard round was that not everyone can afford to work for free for an uncertain reward. Yet, [as @ccerv1 pointed out on twitter](https://twitter.com/carl_cervone/status/1725258994741395704): all funding is retroactive. All funding is based on work you’ve done before whether on this particular project or previous ones.

More practically, one way to lower the risk for builders would be to increase the cadence of the rounds. If someone works on something for three months and then does not receive adequate funding then this might really hurt them. On the other hand, if they work on it for 1 to 2 weeks and then receive a funding decision they can choose to keep working on it or move to something else. It’ll be important to test different cadences of rounds in the future. We believe there is a viable retroactive path for all.

Overall, for the above reasons, we plan on all future citizens rounds being fully retroactive. Further, given the market direction it may be worth it for the main Gitcoin Grants program to consider a shift to include one or more dedicated retroactive funding pools as well. This may then make it easier to raise funds for the matching pool due to the increase in funder confidence that they are funding impactful, valuable contributions to the ecosystem.

One notable memetic attractor in retroactive funding is ‘impact = profit’ which goes hand-in-hand with ‘fund the gap.’ In our Ccitizens Rround 2, we had individuals seeking retroactive funding for work that had been compensated previously. To adequately fund the gap, it’s essential that donors are paying attention to how much previous funding a grantee has received and that grantees are transparent about their prior funding. If Gitcoin doubles down on retroactive funding, then it’ll be important for us to consider how we surface the idea of funding the gap to voters (and draw attention to the necessary data). You can find some recommendations on this in our feedback to the product team in our [initial documentation](https://docs.google.com/document/d/1W5T9ETvXl_t5ukgTw4UeDhCSdq21DayrBdWsSTzqAwA/edit?usp=sharing) and more elaborately for [round 2](https://docs.google.com/document/d/1ZaoyEfZ0fqMS0V0LRD3shyQWHHhJYSI5PMcz14QFbV0/edit).

# Closing

Thanks for making it this far.

We were surprised by how good it felt to fund retroactively and we were surprised by how good it felt to fund individuals instead of projects. It allows the community to much more directly determine who is creating value and send funds directly to them. It also sends a message to each Citizen that you choose what you want to work on, you don’t have to commit to a particular project: the rest of us will fund you if we find it valuable. This creates autonomy, freedom and a flat organization.

We view the Citizens Rounds as a model for our DAO, fostering a bottom-up, skills-driven owner’s mentality, bringing us back to the essence of what being a DAO is about. Our second GCP is coming very soon, and we’ll continue to check in with our community on missing pieces to achieve our goals, with a high focus on impact through retroactive funding.

# Appendix

## A. Relevant links:

[Learnings product round 1](https://docs.google.com/document/d/1W5T9ETvXl_t5ukgTw4UeDhCSdq21DayrBdWsSTzqAwA/edit?usp=sharing) | [Learnings product round 2](https://docs.google.com/document/d/1ZaoyEfZ0fqMS0V0LRD3shyQWHHhJYSI5PMcz14QFbV0/edit)

[Results round #1](https://gov.gitcoin.co/t/gitcoin-citizens-round-1-results/16302) | [Results round #2](https://reportcards.gitcoin.co/424/0x7492a8c4ED29B1F1559888Bd832fAe5D33E10370)

[Results dashboard](http://gitcoin.co/grants-data)

[Round #1 link](https://explorer.gitcoin.co/#/round/10/0x984e29dcb4286c2d9cbaa2c238afdd8a191eefbc)

[Round #2 link ](https://explorer.gitcoin.co/#/round/424/0x7492a8c4ed29b1f1559888bd832fae5d33e10370)

## B. Survey Results

||Round 1|Round 2|
| --- | --- | --- |
|Total Participants|9|13|
|Fairness of Compensation (3 = fair, 5 = over, 1 = under)|3.11|2.62|
|Felt Informed|4.56|4.62|
|Round Operator Rating|4.56|5.00|
|Intuitive to Set Up Grant Page|3.56|4.23|
|Intuitive to Apply For The Round|4.11|4.54|
|Intuitive to Bridge|4.67|3.92|
|Overall Experience / Satisfaction|4.44|4.38|

*Table 3: Grantee Survey Results*

When comparing Round 1 and 2 here are the most notable changes:

* Overall grantees felt more undercompensated in Round 2
* The experience of creating a grant and applying to a round was much more intuitive in round 2
* Bridging was much more intuitive in round 1 (on OP) than in round 2 (on PGN)

Full Survey Questions can be found [here](https://forms.gle/WsJ69mjoLmPpDrgV6) and [here](https://forms.gle/y6fiZhHv8Y7tZG548)

## C. Testimonials

![|527x152](upload://yv73Ckx1REBWmGk1PnoFn2NCkDR.png)

![|527x141](upload://acXydlphPO5QTFxs06ArA5TnTC9.png)![|526x637](upload://mnWEPZI8Byzsaz8VQaMwNDK7V7F.png)

![|553x201](upload://iLcn2Kqfdt1UcFwV3j4dCYty5st.png)

![|400x351](upload://rGDvxP9c5h3ot06poOZXaxevffw.png)

![|402x278](upload://iEptURF8scvv0umLODbXs15XzAv.png)

-------------------------

KarlaGod | 2023-12-01 20:43:40 UTC | #2

It's so great to see the transparency and decisiveness the Gitcoin team supplies. I'm glad that I met the Gitcoin community, and I'm excited for GC3

-------------------------

PaulBurg | 2023-12-02 04:37:25 UTC | #3

Thank you, Umar for such analysis! And thank you all to participate and support Gitcoin Citizens activities 👏

As you pointed one of the factors that increase the impact was airdrop farmers. As I understand they are partly responsible for ~$60k extra

In this case, should we engage more with degens (airdropers here) to exploit their speculative approach 

Let’s say we will talk with them by their language. I understood that it might view as against value. But this is conversion act from degen to regen! They will just realized it after the act not before

-------------------------

umarkhaneth | 2023-12-03 23:26:31 UTC | #4



[quote="PaulBurg, post:3, topic:17201"]
As you pointed one of the factors that increase the impact was airdrop farmers. As I understand they are partly responsible for ~$60k extra

In this case, should we engage more with degens (airdropers here) to exploit their speculative approach
[/quote]

Hey Paul! Good question. basically: does the amount of funding airdrop farmers add to the round outweigh the cost of possibly skewing the QF distribution away from deserving grantees? 

I think there might not be a hard and fast answer to the above question and I can only give my opinion. When looking at Citizens Round 1 for example, it really brought in a lot of airdrop farmers who added funding to the round. Maybe they wanted some RetroPGF of their own. It's notable that they didn't come back to Round 2 the same way. To me this partly says: they're fickle, they may show up for a novel opportunity to make money but they won't stick around. They are not a funding source to rely on. 

But more importantly, in general as we scale QF I see the answer to this increasingly being: No the cost of skewing the QF distribution is too high. When the matching pool is significantly larger than the crowdfund amount then farmers who skew the distribution have an outsized negative impact on deserving projects. 

For example, if a $100k matching pool raises $20k in contributions then on average each $1 donated directs at least $5 (extremely handwavey). This is harmful in the case where there are particular projects in the round who draw in the airdrop farmers (perhaps because they are teasing a token one day). In that case the cost to *deserving projects* for each airdrop farmer donating $1 to the token-teasing project is about $5. To me, this is clearly not worth it and against our desire to fund where value is being created.

On the other hand, it would be interesting to set up more ways to donate to the matching pool where the funds grow the overall pot for everyone in equal measure. Hopefully [this app by supermodular](https://crowdfund-matchingpool.vercel.app/) could help.
[quote="PaulBurg, post:3, topic:17201"]
degen to regen! 
[/quote]
My favorite type of conversion :)

-------------------------

FractalVisions | 2023-12-09 00:06:27 UTC | #5

The citizens program is one ☝️ of the best experiments around & hearing about the shift to a fully retroactive rewards model is exciting.

We feel like many builders will be attracted to this type of ecosystem. Thank you so much for this write up. The innovation here is definitely breaking the ice for new opportunities such as building on public goods network.

Whenever the next round comes the participation will be sure to increase. For now it’s a very small group of folks who are passionate about working together. That’s something others will recognize and want to join in on throughout the future as the program scales upwards. 

We definitely agree with what @PaulBurg mentioned above ⬆️ relating towards the popularity of the grants program becoming another avenue for funding that anyone could attempt to extract value from. 

At the same time some of the safeguards already in place as well as a tight knit community of Gitizens along with proof of impact reports via KarmaHQ and the Grantee Accountability Protocol aka GAP also help to show who is aligned with the same values of the Gitcoin ecosystem. 
That does provide extra transparency and trust for returning applicants that can be utilized to curate the round of it becomes an issue in the future.

There are a few scenarios imaginable where veterans of the citizens program could gain priority to enter a round if there is a large amount of funding available to help filter out low effort, high noise influencers from tapping into funds other low visibility participants really deserve who do provide high impact initiatives & contribute to the education or growth of the ecosystems core components.

-------------------------

bshevchenko | 2024-02-13 17:19:18 UTC | #6

This is really exciting! Great job!

-------------------------
