---
id: 10016
title: "Quadratic Funding x Effective Altruism"
slug: quadratic-funding-x-effective-altruism
category: governancevision
url: https://gov.gitcoin.co/t/quadratic-funding-x-effective-altruism/10016
created_at: 2022-03-06T21:07:50.202Z
last_posted_at: 2022-06-06T15:51:36.453Z
posts_count: 12
views: 6514
like_count: 30
---

# Quadratic Funding x Effective Altruism

<https://gov.gitcoin.co/t/quadratic-funding-x-effective-altruism/10016>
owocki | 2022-06-06 15:52:52 UTC | #1


# Abstract

In this post, I explore the intersection of Effective Altruism and web3.0. I explore a proposed extension to [Gitcoin Grants 2.0](https://gov.gitcoin.co/t/gitcoin-grants-2-0/9981) such that [Gitcoin Grants Results](https://gitcoin.co/results) are increasingly steered towards the most effective causes via (1) the introduction of a data layer that allows for the aggregation of attestations of effectiveness & (2) the introduction of social norms introduced by Effective Altruism.

# Effective Altruism

I’ve been learning about & increasingly getting excited about Effective Altruism.

> Effective altruism (EA) is a philosophical and social movement that advocates "using evidence and reason to figure out how to benefit others as much as possible, and taking action on that basis". [[Wikipedia]](https://en.wikipedia.org/wiki/Effective_altruism)

The primary thing that appeals to me about Effective Altruism is how evidence based it is.

The giver in me is deeply excited that when giving to a cause based in effective altruism, the evidence-driven-basis for the giving means that one is doing the most good possible per dollar spent. It is not going to administrative overhead. It’s not going to dead-end-initiatives. That is deeply cool & profoundly impactful.

The scientist in me is deeply excited about the idea of having an evidence based approach to giving. Science and the scientific method is deeply based in the seeking of relevant evidence to prove or disprove various hypotheses.

The web3 builder in me is excited about the intersection of these ideas with the [data set we have at Gitcoin](https://docs.google.com/spreadsheets/d/1OsJ_nmN9mN-i_9h3Yj2mDfjvtsP1qvv3B1zcpER62dk/edit#gid=1223173410). Imagine if we could measure the impacts each Gitcoin Grant had on the world, across all [8 forms of capital](http://www.appleseedpermaculture.com/8-forms-of-capital/), and provided that information via the [Grants 2.0 protocol](https://gov.gitcoin.co/t/gitcoin-grants-2-0/9981), so that people across the world could easily make better-informed decisions about which grants were the most effective when funding them!

## Measuring Impact

The devil is in the details. How does one measure which projects are doing the most good? Back to [Wikipedia](https://en.wikipedia.org/wiki/Effective_altruism):

### Cost-effectiveness

> Some charities are far more effective than others, as charities may spend different amounts of money to achieve the same goal, and some charities may not achieve the goal at all.

> Effective altruists seek to identify charities that are highly cost-effective.

> For example, health interventions are selected based on their impact as measured by lives extended per dollar, quality-adjusted life years (QALY) added per dollar, or disability-adjusted life years (DALY) reduced per dollar.

We have now quantified the impact for health-based outcomes into a KPI: quality-adjusted life years (QALY)

### Room for more funding

Another important criteria is room for more funding. Back to [Wikipedia](https://en.wikipedia.org/wiki/Effective_altruism):

> Effective altruist organizations consider the expected impact of a funding increase rather than evaluating the average value of all donations to the charity. This avoids donations to organizations that lack "room" for more funding because they face bottlenecks other than lack of money. For example, a medical charity might not be able to hire enough doctors or nurses to distribute more medical supplies, or it might already be serving all of the potential patients in its market

## Learn more about Effective Altruism

I plan to use the rest of this post to talk about the intersection of Effective Altruism x web3.

You can learn more about [Effective Altruism in this handbook](https://forum.effectivealtruism.org/posts/cN9Zu7dowefAfmNnH/the-effective-altruism-handbook).

# Effective DAOltruism = Effective Altruism x web3

I would like to explore how we could bring more of an Effective Altruist mindset to Gitcoin Grants.

This means bringing more evidence of effectiveness into the Gitcoin Grants dataset.

For those of you reading this post who may be new to Gitcoin: [Gitcoin Grants](https://gitcoin.co/grants) is a project oriented around our [mission](https://gitcoin.co/mission) of building & funding digital public goods. So far [we’ve funded $52mm](https://gitcoin.co/results) worth of public goods, mostly using [a matching formula called Quadratic Funding](https://wtfisqf.com/).

Every quarter, about 500k transactions happen on Gitcoin Grants to allocate about $6mm/quarter to various projects. The data for last quarter looks like this:

[![|624x275](upload://2rbxNrwvD3d4HMthXR4mQTB9gKb.jpeg)](https://docs.google.com/spreadsheets/d/1OsJ_nmN9mN-i_9h3Yj2mDfjvtsP1qvv3B1zcpER62dk/edit#gid=1223173410)

The decisions on Gitcoin Grants are based upon the preferences of a community of 30k funders. There are 500k transactions per quarter, which constitute an expression of support for 1k different projects in the ecosystem.

When these funders make a decision about which projects to fund, they are given the following data:

1. Grant name
2. Grant Description [(see this example)](https://gitcoin.co/grants/1668/coin-center-is-educating-policy-makers-about-publ)
3. What geographical region they are from.
4. Their website
5. Their twitter
6. Who their team is

What is deeply interesting to me is starting to take Effective Altruist data and co-mingling it with the above data. Imagine if you could browse each grant + see its impact on the world right next to the above information about the grant.

What if you could see attestations about this grants impact, placed & quantified on each of the following vectors, as you browsed the grants registry?

![|624x391](upload://ywatn67gj8e8Nzgsyug85u0x5V3.png)

I imagine that the data layer of the system could look something like this

![|432x321](upload://qaD1wFS2NIqMALHYtMZhZsUqUOH.png)

How would it change the Gitcoin Grants experience to be able to browse/filter grants by their impact? What if you could choose Grants that have the most total impact? What if you could filter grant based on those who have attestations from people you yourself trust? How would you filter out spam? How can governance create consensus about which attestations are legitimate?

On a systemic level, how would the introduction of such a dataset change the preference map of each grants round?

Here is what the preference map for Gitcoin Grants Round 12 looked like. Each node in the network is a user or a grant, and each edge is a transaction.

![|380x250](upload://ttcbvHY4KruPlI9wwUPxJvPK6TG.gif)

If we were to introduce Effective Altruist data layer into Gitcoin Grants, would each individual agent in the system make more-informed decisions? If so, how does that change what the dataset in aggregate looks like for each Grants round? How would that change the [Quadratic Funding](https://wtfisqf.com/) results?

Right now there are more questions than answers, but I am deeply excited about the questions that are coming up when I think about Effective DAOtruism.

If you are too, I’d love to hear about it. Leave a comment below.

-------------------------

owocki | 2022-03-07 01:07:44 UTC | #2

One thing I think would be interesting to discover in the data of a hypothetical Effective Altruist Grants experiment would be to map the the preferences of communities utilizing that Grants program across multiple different types of capital.

For example, one could imagine a world in which blockchain-based grants programs optimize for Financial & Intellectual capital, but never meaningfully have a positive impact on other vectors.

![Screen Shot 2022-03-06 at 5.56.53 PM|690x385](upload://fRggJkiZaw6GJkntBvJ4AgyAiHv.png)
(*X axis: the preferences of 10 people*, *Y axis: the 8 forms of capital* 
*each cell is how much person X cares about Y form of capital.
all data is random + for demonstration purposes only*)

Personally I'd rather live in a world where the consensus of at least some of our grants programs is on creating positive impact on Material Capital (causes like climate change + biodiversity loss are deeply disheartening to me. 

A world where the community preferences look a bit more like this would give me more comfort.

![Screen Shot 2022-03-06 at 5.57.21 PM|690x421](upload://qXOtLnfPxWM9d2OD64jLnjdTiqr.png)

If we chop off the individaul preferences, and just look at the aggregated preferences:

![Screen Shot 2022-03-06 at 6.01.14 PM|690x164, 75%](upload://iSJuQny1iBZZvtOuPOKx1k8AjCb.png)

Here are a few more randomly generate preference maps.  I invite you to ponder what the communities underneath them would be like:

# a community that cares about social, material, & intellectual capital
![Screen Shot 2022-03-06 at 6.02.26 PM|690x208, 50%](upload://twH1cnjaBNPyTSUjxxUuRz2o0K6.png)
# a community that cares about social & experiential capital
![Screen Shot 2022-03-06 at 6.02.22 PM|690x213, 50%](upload://tk2bHA6HC7JplIcvkQMjn69w5Zw.png)
# a community that cares about material & experiential capital
![Screen Shot 2022-03-06 at 6.02.18 PM|690x211, 50%](upload://6uhWGYghZzY0MHUom87wXnReTBb.png)
# a community that cares about financial, intellectual capital
![Screen Shot 2022-03-06 at 6.02.08 PM|690x215, 50%](upload://oUJPZLwbTbNzhnGkTXuRECiwNGd.png)
# a community that doesnt care about much of anything at all except financial capital
![Screen Shot 2022-03-06 at 6.07.23 PM|690x207, 50%](upload://1lZuZuw464hdse7UyvDeFslvzH.png)

-------------------------

lthrift | 2022-03-08 05:21:01 UTC | #3

Thanks for surfacing Effective Altruism, Owocki. I haven't gone so far as to read the linked handbook yet, but look forward to doing so. 

In working on the vision and strategy for Grants 2.0, it is apparent that grants who come back round after round for on-going funding are on a spectrum of being able to avoid accountability for how they are using the money they raise to completely missing the opportunity to showcase their impact for increased funding and community support over time. Effective Altruism seems to hold some foundational theory for building a mechanism for showcasing impact delivered. 

Conversely from the potential significantly positive impact, I wonder if this model would negatively impact projects who are just getting started. Maybe the mechanism could be designed to account for the lifecycle of a project - expecting that the impact of a project should increase with age and maturity of a project? What about accounting for steadiness of impact versus volatility of impact?

-------------------------

pandeyanujk | 2022-03-09 07:44:39 UTC | #4

This is super interesting. I am enjoying this post and holding some of these questions. Oversimplifying a bit, it seems that the tradeoff is - how to optimize between *the popular projects* & the project that may *yield a high outcome to impact ratio* regardless of it's popularity/presence. Would be curious to put a list of projects that did great in the past grant rounds (were popular) but didn't meet the expected outcome to impact.

-------------------------

lthrift | 2022-03-10 22:27:30 UTC | #5

This is a really interesting idea @pandeyanujk! We don't currently collect impact metrics, but what you've outlined could be the basis of an initial experiment in doing so off-platform for grantees who were open to it.

-------------------------

erich | 2022-03-11 10:33:49 UTC | #6

The Effective Altruism community is highly rationalist and somewhat contrarian to collaborative, bottoms-up governance as in Gitcoin Grants. Therefore, we should be careful in sorting / prioritizing grants and nudging the community given some technocratic metrics of GPG or other centralized entities.

Many critical contexts can't be formalized and simplified into one or two metrics. So how would we measure "impact" really in a reasonably universal manner?

Here are some interesting thoughts on the issues of technocracy and the Effective Altruism movement: https://www.radicalxchange.org/media/blog/2019-08-19-bv61r6/.

-------------------------

tigress | 2022-03-11 14:42:26 UTC | #7

The preference maps and what is meant by Effective Altruism are interesting to study and contemplate. With my post here I d like to offer an additional perspective that may complement the 8 forms of capital very well.

To me, I d prefer to focus on a well-balanced preference map, because I feel like all 8 forms of capital are equally important to make my life and the life of others truly better. Based on the samples it would mean that each type of capital could be no less than ~ 60 and no more than ~70 to achieve balance. 

In addition.... I'd zoom out a little bit and ask: 
1. Given Grants 2.0 what is **the bigger change we intend to facilitate**? From where ... to where ... do we want to move? 

2. What could be meant when we intended to focus on "**regenerative decision making**" and therefore **doing good better** in this context?

One answer may be this: I would look into these scales based on developmental frameworks or Levels of Consciousness. In essence, there is several of these frameworks out there and they all converge to very similar developmental stages and tiers. Only their authors, naming and colours differentiate. Spiral Dynamics by Beck/Cowan based on Graves' work, Ken Wilber and Robert Kegan... just to name a few.

![Levels of Consciousness|690x434, 75%](upload://r0VjFJ8OHBGWg3JxdnrwhmlfQY6.jpeg)

So, my personal opinion would be:

> *YES, I think I would be **doing good better** if 30% or more of the projects I were to found would contribute to help more people like us make the move from the 1st Tier to the 2nd Tier.*

That is from orange/green to yellow/teal colours according to Spiral Dynamics (... which is fortunately mentioned in GreenPilled :-) on page 75 )

![image|398x500](upload://7waSeIl6EylNh4Qa7vANRrhCh9u.jpeg)


According to several studies by Loevinger or Wilber the population of the 1st tier make up roughly 85%. 

This idea, that "**regeneration**" can also be seen and understood as an increase in the Level of Consciousness of the population would change Quadratic Funding in a way that may look like this

* Current: *Number of contributors* matters more than *amount funded* .

* Future: *Number of contributors* multiplied by ***Regenerative Factor*** matters more than *amount funded*.

I hope I was able to explain this very abstract idea and make it understandable.

Thanks for the inspiration to think about this, connect the dots and come up with this work.

-------------------------

fleurdelys | 2022-03-12 04:14:36 UTC | #8

1. How to define effectiveness (a set of standards or matrix, weighting)
2. Who will evaluate?
3. Once the standards are set, who will continue to check whether the set is effective, i.e. achieve the original proposed goal?

-------------------------

pandeyanujk | 2022-03-14 06:00:09 UTC | #9

Yes! Thinking a bit more on the metrics governance & orchestration - this may also tie well into the impact DAOs project:

* A framework of metrics to measure the impact.

* A reference architecture for upcoming DAOs to measure their *outcome to impact*.

Happy to setup brainstorming sessions to list out the possibilities. Exciting stuff!

-------------------------

Colton | 2022-03-21 05:26:58 UTC | #10

Wow I’m late to the party but I can’t miss the opportunity to comment on this thread.

I took the Giving What We Can pledge (effective altruism) a year and a half ago after hearing Sam Harris’s conversations with Will MacAskill. Seeing EA talked about here makes me very happy. 

Leon and fleurdelys bring up a good point: Who gets to decide what is considered effective?

A good data set to start with would be how well projects do based on the goals they outline in their grants. 

But going a step further, it may be true that the EA movement is not fully appreciating the 8 forms of capital mentioned in Owocki’s post. Two ways we could shift the conversation toward this more holistic view of societal wealth:

1. Web3 may allow us to more accurately price in capital like Cultural, Social, Experiential

2. This may be a place for Gitcoin’s lore to play a role in shifting consciousness towards valuing more than money. 

So glad to see this conversation taking place <3

-------------------------

upper-left-k | 2022-04-27 04:15:27 UTC | #11

@owocki thanks for leaving such an interesting trail of ideas. I’m new here and have an idea on how web3 tech could be applied to make the Fair Trade system more effective.  My background comes from hands on experience with international trade and sustainable manufacturing. 

Is there a way I could connect with someone who is coming at this from a tech background to discuss?

-------------------------

owocki | 2022-06-06 15:51:36 UTC | #12

Heads up there is some action in the EA forums about this topic!

https://forum.effectivealtruism.org/posts/9kcMNim6R2Lvh4FAf/optimizing-public-goods-funding-with-blockchain-tech-and

-------------------------
