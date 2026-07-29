---
id: 19423
title: "Web3 Funding Fatigue: a growing problem"
slug: web3-funding-fatigue-a-growing-problem
category: open-discussion
url: https://gov.gitcoin.co/t/web3-funding-fatigue-a-growing-problem/19423
created_at: 2024-09-24T17:33:27.604Z
last_posted_at: 2024-10-28T14:23:38.308Z
posts_count: 15
views: 4251
like_count: 35
---

# Web3 Funding Fatigue: a growing problem

<https://gov.gitcoin.co/t/web3-funding-fatigue-a-growing-problem/19423>
owocki | 2024-09-24 17:41:24 UTC | #1

**Web3 Funding Fatigue: a growing problem**
*Investigating the funding fatigue in supply and demand side web3 public goods.*
Authors: Vengist + Owocki

# TLDR

"Funding fatigue" is a growing issue in Web3 public goods funding.

Grantees experience fatigue from maintaining and promoting multiple grants across platforms, while funders face overwhelming requests and high attention costs in evaluating numerous proposals. The system's complexity is a barrier for both sides.

Proposed solutions:

* **Aggregation**: Aggregating labour supply and demand.
* **Mechanisms**: Introducing a "common app" for grantees, interoperable registry protocols, weighted lists for funding, and tools like Drips, 0xsplits, and Protocol Guild Forks to streamline the process.

# Introduction

Public goods funding in Web3 is essential but increasingly strained by "funding fatigue."

Grantees are overwhelmed by managing and promoting multiple grants across fragmented platforms, while funders struggle with an influx of proposals and high computational costs in evaluating them. This imbalance between supply and demand complicates the funding process.

Grantees face visibility challenges, needing constant promotion, while funders must navigate numerous deserving projects with limited resources. The system’s complexity worsens these issues.

Our proposed solution is aggregation. By formalizing grantee applications and funding decisions through tools like a “common app,” registry protocols, and guilds, the process can be simplified, reducing strain on both funders and grantees. Protopian increase in probabilities that desired public goods are realized.

# Problems:

## Grantee fatigue: supply-side

Grantees have to maintain grants on many diff platforms, across (often) multiple grants. And for QF they have to shill each of them. This is causing grantee fatigue.

Combating the matthew’s effect: intensive effort to become visible in the distributed, complicated public goods funding ecosystem.

## Supply fatigue: demand-side

There are DAOs that are overwhelmed with requests for funding from multiple worthy (but attention consuming to validate) causes.

Computational overhead:: observing, orienting, deciding, acting all take too much computation currently for a funder to navigate the public goods funding ecosystem, mismatch of supply and demand. The system is currently very complicated, instead of complex.

# Solution

# Aggregation of Supply

**Grantee Common App** - a webapp that allows you to apply to multiple grant programs at once.

**Registry Protocol Interop** - build an a way to push/pull grants from one registry to another.

# Aggregation of Demand

One solution may be Weighted Lists of causes that share sales/marketing/governance responsibilities.

One important primitive here is the self-curating registry (SCRs), popularized by protocol guild. SCRS (and nested SCRS of SCRS) could self to aggregate demand to navigate the funding of the commons.

Useful tools: Drips, 0xsplits, Protocol Guild Forks

Computation savings: Aggregated guilds act as high level strategies that funders can more easily navigate. Each guild serves as specialized tactics down stream of high level strategies. The low governance overhead of the SCRs, simply maintenance of the registry’s weights, allows for low-cost formation and operation of guild-like entities.

Ex. A self-curating registry of ethereum public goods

Because SCRs are just a simple address with governance + splitting logic, they can be chained and nested together in a number of interesting ways.

Let's imagine creating an SCR to represent Ethereum Public Goods. Instead of individual contributors, we can just add various guilds with reputable contributions to public goods. We would only need to determine the orgs, and the funding flows directly through to their contributors, based on the logic local to their context.

![|316x314](upload://mc9cvdG5l4Xme8CLkKTsVM25M6i.png)

Lets envision what funding flows look like before and after this fatigue issue is solved.

![|624x335](upload://twWik5hkpkKljlD6Vuebmn3gl3i.png)

![|666x365](upload://yVFSan8YCIwlzGWgs7fdQ0fgJCq.png)

# Conclusion

Addressing "funding fatigue" in Web3 public goods funding is critical to ensuring a sustainable ecosystem. The current system overwhelms both grantees and funders, leading to inefficiencies and missed opportunities. By focusing on solutions that aggregate supply and demand locally, both sides can operate with more efficiency and legitimacy. Tools like a "common app" for grantees and funding guilds for funders could reduce complexity, lower computational overhead, and improve the overall flow of funding. Simplifying these processes is key to maintaining the health and vitality of the Web3 public goods ecosystem.

-------------------------

jon-spark-eco | 2024-09-25 00:31:12 UTC | #2

I like the way this streamlines funding. Checking my understanding:

- In this scenario the Guilds do the shilling and the down stream public goods do the building. This solves the fatigue for the public goods builders but doesn't it just shift the fatigue to the Guilds? 
- How does this solve the Funder fatigue? Aren't the Guilds going to be shilling to the funding sources regularly to keep funds flowing?

-------------------------

magentaceiba | 2024-09-25 14:57:38 UTC | #3

In case the guilds approach doesn't take root, another detail piece I've seen could be helpful is a portable profiles app/protocol for projects. So it's easy for projects to own their grant listing and be able to easily pull it in to the specific grants program they're applying to and make modifications necessary for the specific grant. Ideally that listing could be available across platforms, for example across Gitcoin, Charmverse, Giveth, Octant, etc. 

Description of the problem: As the # of Gitcoin rounds has proliferated, when a project is eligible for multiple increasingly specific grant parameters there, they've had to write multiple different applications (just Gitcoin rounds, not talking about all the other Web3 grants programs). If there was a way for a project to keep a stored core of what their project does, and add details specific to a specific funding team's ask, that could streamline efforts from the project's side.

The reason I think this might be more helpful for a project than say, a Google or Hackmd file with the project's description, is that it also allows more flexibility when it comes to assigning streaming/drips, and also for any dashboard like apps like allow funders to see across different platforms and filter by stage, scale, focus vertical, region, any other common params.

The UI/api port for the project listing in any funding app would look like "Enter your core project description here or pull in from [The Protocol].

-------------------------

owocki | 2024-09-25 17:00:16 UTC | #4

[quote="jon-spark-eco, post:2, topic:19423"]
* In this scenario the Guilds do the shilling and the down stream public goods do the building. This solves the fatigue for the public goods builders but doesn’t it just shift the fatigue to the Guilds?
[/quote]

anyone can do the shilling.  but there is an opportunity to pool bd/shilling resources at the guild level, so not every project needs a shiller/salesperson.

[quote="jon-spark-eco, post:2, topic:19423"]
* How does this solve the Funder fatigue? Aren’t the Guilds going to be shilling to the funding sources regularly to keep funds flowing?
[/quote]

it makes it easy for anyone to fund an entire category of public goods, instead of having to pick every little project themselves.

-------------------------

owocki | 2024-09-25 17:01:20 UTC | #5

[quote="magentaceiba, post:3, topic:19423"]
In case the guilds approach doesn’t take root, another detail piece I’ve seen could be helpful is a portable profiles app/protocol for projects.
[/quote]

yes portable profiles are definitely a key piece of the puzzle!  i want to fund a "Common App" that can make it easy to transport grant profiles across registries.  eventually ill get my life together and write an RFP for this

-------------------------

1a35e1 | 2024-09-25 23:00:59 UTC | #6

Its an interesting solution but I think the current problems will just get transferred to the guilds who have less of an incentive to allocate effectively.

That said: 

* Curated Registries are 🤌
* Self service is with agency on the builder sider is good.
* Building on chain reputation by consistently delivering to spec 🤌

In an ideal world:
* Grantees can publish initiatives they are looking to get funded. 
* Initiatives map to macro themes set by Guild/Network
* Discovery is facilitated by theme
* Multiple Funding sources may fund themes or Initiatives
* Funding sources evaluate delivery
* Everything is on-chain.

-------------------------

mmurthy | 2024-09-26 16:55:23 UTC | #7

[quote="owocki, post:5, topic:19423"]
yes portable profiles are definitely a key piece of the puzzle! i want to fund a “Common App” that can make it easy to transport grant profiles across registries. eventually ill get my life together and write an RFP for this
[/quote]

We are trying to solve the portable profile problem at Karma by helping project owners aggregate all their grants, milestones, progress updates and roadmap in one place and onchain (as EAS attestations). [See Example here](https://gap.karmahq.xyz/project/viaprize-2). We have about 3k project profiles and we see hundreds of projects posting updates on a weekly basis and keeping their project/grant updated. I am very interested in building this Common App given lot of the data is already in project's GAP profile and this is a logical extension of it. Infact, multiple common apps can be built given that this data is all onchain and in clear structured format. Getting all the platforms onboard is the most challenging problem imho.

-------------------------

arunmaharajan | 2024-09-30 07:51:43 UTC | #8

At UNICEF we are looking to build a "marketplace" for Digital Public Goods to be able to find funding. We would immensely benefit from this common app, to be linked through APIs to our marketplace. The marketplace is still in ideation / design stage, so would be quite open to take part in any such discussions to collaborate or influence or get influenced.

-------------------------

owocki | 2024-09-30 15:39:12 UTC | #9

[quote="arunmaharajan, post:8, topic:19423"]
The marketplace is still in ideation / design stage, so would be quite open to take part in any such discussions to collaborate or influence or get influenced.
[/quote]

would love to chat.  DM me on telegram or twitter: I'm owocki in both places

-------------------------

owocki | 2024-09-30 18:30:55 UTC | #10

Just published another post about guilding :) https://gov.gitcoin.co/t/guild-guild-a-locus-of-coordination-for-guilding/19452

-------------------------

Kronosapiens | 2024-10-01 20:59:47 UTC | #11

Regarding the demand-side fatigue of evaluating projects, I'd highly encourage folks to look into the **pairwise-preference based approaches** that have been developed over the last few years. They've gotten less attention than QF-based approaches but have a lot to recommend them from the perspective of cognitive overload.

The big lift is that they simplify the evaluation process: instead of evaluating every project in *absolute* terms, funders can make *relative* choices between projects -- much easier to do at scale.

These techniques were first (to my knowledge) developed by Colony with their [BudgetBox](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3317445) mechanism, which was picked up by General Magic with [Pairwise](https://www.pairwise.vote/), and by dOrg with [Pairdrop](https://pairdrop.daodrops.io/), so at this point there are multiple working implementations to play with.

-------------------------

arunmaharajan | 2024-10-09 13:35:01 UTC | #12

[quote="owocki, post:9, topic:19423"]
owocki
[/quote]

Pinged you on Telegram. I am @arunmaharajan

-------------------------

1a35e1 | 2024-10-23 16:31:04 UTC | #13

I just put out an RFC for a new method to potentially address this problem. DMs always open.

https://x.com/1a35e1/status/1849084464028131503

```
TL;DR
- We introduce "initiatives" as a term to refer to ideation/macro planning in on-chain orgs (not proposals)
- Members create initiatives by locking gov tokens [some amount * some interval]
- The length of a lock boosts weight; Weight decays to the initial lock amount
- DAO sets an proposal/acceptance threshold (configurable)
- Anyone can "contribute" towards an Initiative (with on-chain clauses eg. None or Accepted before timestamp)
Outcomes
- Gov tokens removed from voting supply while locked
- Smaller token holders can lock for longer periods (boosted voice)
- A dynamic ranked on-chain priority board
- Incentives (contributions split eg. [ (5/30/65), (fee/supporters/treasury) ])
- Inverted capital allocation ( External committees can fund projects directly via this mechanism) 
- Issue bonds for locked token on an AMM to achieve a secondary.
```

-------------------------

Kronosapiens | 2024-10-28 01:16:09 UTC | #14

Following up on my [earlier comment](https://gov.gitcoin.co/t/web3-funding-fatigue-a-growing-problem/19423/11?u=kronosapiens), here's a deeper analysis contrasting Quadratic Funding with Pairwise Preference, with focus on the attentional dimension of the mechanisms. Should be relevant to this discussion.

https://blog.zaratan.world/p/quadratic-v-pairwise

-------------------------

owocki | 2024-10-28 14:23:38 UTC | #15

This article is fascinating.  Thanks for sharing.

Id be interested to play with a pairwise funding pilot sometime.  I wonder if this is something we could consider in 2025 for citizens @MathildaDV

-------------------------
