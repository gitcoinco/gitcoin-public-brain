---
id: 10391
title: "GR14 Round Structure & Future of the Main Round"
slug: gr14-round-structure-future-of-the-main-round
category: open-discussion
url: https://gov.gitcoin.co/t/gr14-round-structure-future-of-the-main-round/10391
created_at: 2022-04-19T16:40:30.686Z
last_posted_at: 2022-04-21T16:24:56.749Z
posts_count: 2
views: 3457
like_count: 11
---

# GR14 Round Structure & Future of the Main Round

<https://gov.gitcoin.co/t/gr14-round-structure-future-of-the-main-round/10391>
annika | 2022-04-19 16:45:42 UTC | #1

# Introduction

In GR14, which will run in June, the PGF workstream wants to define & test a round structure that is more reflective of the world we will live in post-Grants 2.0. Starting intentionally on this now will set us up to iterate our way to a more steady optimal state throughout the remainder of 2022.

This post is not a proposal to be voted on; it is simply a pre-read to the more formal “GR14 Round Structure” post which will follow in the coming weeks to ratify the plan for the round.

## What’s top-of-mind for GR14

1. **Re-evaluating the main round**
A big focus area ahead of GR14 is re-evaluating what constitutes the Main Round, which is the primary focal point of this post. Up until GR13, every grant on the platform with an Ethereum payout address has been eligible for matching funds in the Main Round. As we move towards a Grants 2.0 future, wherein anyone can permissionlessly stand up their own Ecosystem or Cause round and can fund whatever types of projects they’d like, the question has been raised as to whether we should define a Gitcoin governance-owned Main Round that will intentionally fund specific domains of projects — public goods, ETH ecosystem, whatever the community defines – rather than serving as a catch-all for everything on the protocol. The Main Round has evolved substantially over the past several rounds, and we have an opportunity to start to re-define it ahead of the Grants 2.0 launch.

2. **Horizontally Scaling Ecosystem Rounds**
We are targeting running 15-20 ecosystem rounds in GR14, up from 9 in GR13. In addition, we want to stand up a Gitcoin-led ecosystem round [specifically focused on Ethereum Infrastructure](https://gov.gitcoin.co/t/can-gitcoin-be-doing-more-to-support-ethereum-protocol-devs/10151/8). Finally, we will make processes explicit operationally for ‘Solo’ (e.g., Uniswap) vs. ‘Collaborative’ (e.g., ZK Tech) ecosystem rounds.

3. **Vertically Scaling Cause Rounds**
We are targeting holding the number of cause rounds roughly constant in GR14, running 3-4 cause rounds in the round. We will focus on scaling up funding & grantees for each round, rather than scaling these rounds horizontally. We will also focus on more clearly defining roles & responsibilities (e.g., who defines eligibility?) for these rounds.

# Re-evaluating the Main Round

#### Background

While Quadratic Funding has remained the core mechanism for Gitcoin Grants throughout the life of the program, the structure of funding pools within a grants round has evolved substantially since GR1.

We have had a few different eras of grants rounds, which can be categorized broadly into:

* *GR1-GR3: Main round as one universal pool*

In the first few rounds, as Gitcoin Grants was getting off the ground, there was just one matching pool that would be distributed across all projects using the QF mechanism, regardless of type of project.

* *GR4-GR11: Main round, sub-divided into categories for specific areas*

In round 4, two separate categories were introduced to the $200K pool: there was a $125,000 matching pool for tech projects, and a $75,000 matching pool for "media" projects. This was the first delineation of specific pools of funding for specific types of projects.

This category-based approach would continue through GR11, with rounds having different categories spanning both domain areas & geographies that were assigned a specific percentage of the main round:

![|468x223](upload://nwGvugviQ03q8MOjKuVlIBgSIez.png)

These categories and their funding percentage allocations were decided upon centrally by the Gitcoin team in the pre-DAO era.

* *GR11-13: Main round + ecosystem / cause rounds for specific areas*

In round 11, the concept of ‘ecosystem rounds’ was first introduced. The idea was: in addition to having specific categories within the main round, a specific project – e.g., Uniswap – could stand up its own ecosystem round to support projects specifically building open source software relevant to their ecosystem, and could use these ecosystem rounds to build their communities.

In round 12, the community voted to do away with categories in the Main Round, instead having one sweeping round that all grants were eligible for with a 2.5% cap (i.e., no single grant could earn more than 2.5% of the total matching pool in the Main Round). Alongside the main round, we continued to build out ecosystem rounds and also introduced Cause Rounds, dedicated pools supporting specific social causes such as Climate, Blockchain Advocacy, and Human Longevity.

In round 13, we continued with the single Main Round approach and we saw increased interest in further building out Ecosystem & Cause Rounds.

## The main round today

As outlined above, over the past several rounds, Gitcoin Grants has grown substantially in scope. What started as a platform to fund open-source projects in the Ethereum ecosystem is now a much broader program, continuing to fund open-source in the Ethereum ecosystem but also now enabling funding for Cause Round grants – some of which have nothing to do with crypto – as well as funding for Web3 ecosystems that extend beyond just the Ethereum community.

This scope expansion has resulted in some ambiguity & frustration given that it is not clear to everyone what’s in and what’s out for the Main Round, as we haven’t explicitly re-defined the round as we have evolved. Is it just Ethereum grants? Is it just Web3? Is it all public goods?

In addition to this scope expansion, platform eligibility has come into question. We have historically said that we only allow ‘public goods’ on the platform. Today, the ‘what is a public good’ criteria is implemented by FDD currently based on the “whether or not a project has raised VC funding” and “whether or not a project has a token”. As evidenced by [the Bright ID appeal in GR13](https://gov.gitcoin.co/t/proposal-grants-policy-update-projects-with-tokens/10125/24), these two criteria aren’t necessarily perfect.

Further to all this existing complexity, when [Grants 2.0](https://gov.gitcoin.co/t/gitcoin-grants-2-0/9981) comes to life, anyone will be able to spin up their own Gitcoin Grants QF round permissionlessly – the DAO won’t have control over the scope of these rounds, and we likely won’t want to include every owner-created round to be included in the Gitcoin Main Round.

So, as we move towards Grants 2.0, we have an opportunity to re-establish what the Main Round is and to be super explicit with funders & grantees on what’s in and what’s out.

## The main round in the future

There are a few paths we could take with the Main Round.

**1. Remove the main round altogether**

Rather than encouraging funders to fund a Gitcoin-owned Main Round, we could instead encourage them to fund specific ecosystem or cause rounds. In this version of the world, Gitcoin would continue to operationally run the ecosystem & cause rounds for the foreseeable future, but we would move away from having a Main Round that is ratified by Gitcoin governance – all decision-making would be independently led by each round. In the long-term, Gitcoin would serve only as the protocol, enabling anyone to spin up, run, and market their own rounds.

We do not think removing the Main Round is the right course of action for a few reasons. First, we have a broad set of funders that want to give back to the community and fund public goods generally speaking, rather than being prescriptive about which pool(s) they fund. We worry that choice overload might become an issue. Second, we have a hypothesis that the market sees value in Gitcoin’s curation – many funders want to give back in a way that is broadly impactful, and trust that the DAO will continue to fund meaningful projects. Finally, removing the main round would strip the DAO of the ability to test QF at scale, and we believe that the main round remains an important testing ground for QF implementations.

**2. Keep the main round as is**

Another path is to keep the main round as is. This would mean we’d continue the status quo: all grants that are approved to the platform and have an ETH payout address, regardless of their project scope or the ecosystem/cause rounds they’re in, are eligible.

All types of public goods can continue to receive funding through the Gitcoin platform, and Gitcoin can truly expand beyond just Web3 public goods and into public goods as a whole.

The ‘for’ argument to keeping the main round as is:

* *It is more inclusive, and our scope has intentionally broadened*
Gitcoin is in the middle of a ReFi / regen renaissance, partly thanks to Owocki's memeing but also because of our willingness to YOLO things like the climate round which have kept us relevant in the face of increasing competitive pressures. Related, Vitalik and others have bought into the idea of Gitcoin as a project that is solving "global coordination problems" beyond web3 including problems in the "physical world" - and we want to make sure we remain a leader in this area (it is very possible for the ReFi movement to go on without us, despite Owocki's role in formulating it).

The ‘against’:

* *It dilutes our focus*
Funding a bit of everything, by definition, means that projects who would receive more funding under a more narrowly-defined pool will be diluted by the rest of what’s added.

* *It limits ecosystem rounds*
If we do not de-couple the main round, all grants on the platform – including partner-run ecosystem rounds – need to adhere to the platform-level ‘must be a public good’ requirement. This limits autonomy to our partners who may want to permissionlessly fund projects that do not meet the public goods criteria.

**3. Narrow the main round’s focus**

The final path is to narrow the main round’s focus – some have suggested that we might just focus the main round on projects building within the Ethereum ecosystem, thereby excluding some of the ‘physical world’ projects & cause rounds that Gitcoin has expanded into over the past few rounds. Similarly, others have suggested that we refine our focus around public goods and have Gitcoin more strictly define what constitutes a ‘public good’ – which would render many grants currently on the platform ineligible for matching.

The ‘for’ argument to narrowing the aperture:

* *We hone in our focus*
Recent rounds have been dominated by Cause Round grants, with the Cause Rounds distributing $1.2M in GR13 across 181 grants, vs. $1.2M in the Main Round across nearly 1,000 grants. Directing funding to these 181 grants in the Main Round, in addition to the $1.2M specifically dedicated to the Cause Rounds, results in other grantees receiving less funding.

* *We build towards Grants 2.0*
We will soon be living in a world wherein anyone can permissionlessly stand up a round to fund whatever they choose on the Gitcoin Grants protocol, so at that point we likely won’t want every single one of those grants to live on the Main Round. Limiting the scope of what’s in the Main Round is a likely inevitability as we move towards that world – and if we start now, we can test what that looks like.

The ‘against’ argument:

* *We become too exclusive in our scope*
We have intentionally expanded beyond just Web3 public goods, and we want to continue down that path. Reverting to an ‘Ethereum’ round would be counter to our evolved ethos of funding more than just Web3 projects, and more narrowly defining ‘public goods’ would prevent lots of great projects currently on the platform from receiving the funding they need.

If we were to implement any sort of narrowing criteria, we would need to very clearly define criteria (e.g., what constitutes “building within the Ethereum ecosystem?”) and build a process to identify & tag all grantees on both a retroactive and forward-looking basis. This would be a pretty significant undertaking.

There are also other ways we might creatively do this – for example, we could set specific criteria that universally get approved to the platform, and then leave it open for governance to ratify adding in different buckets of grants periodically.

# GR14 Recommendation

In the long-term, directionally, we likely want to move towards Option 3. We believe it is important we stay true to Gitcoin’s mission of funding public goods, and we want to create mechanisms for the public to continually define what ‘public goods’ on the Gitcoin platform truly entail. That said, as anyone who has deeply explored the definition of ‘public goods’ knows, coming to universal consensus on what is & isn’t a public good is a monumental task that has been debated by economists and philosophers for years – questions like “how do we define a ‘public’? when does something cross the line of becoming excludable or rivalrous?” make this quite a challenge.

Determining a process to collectively define public goods as a community is not something we take lightly and will be a long, evolving journey.

In the near-term, for GR14 specifically, the Public Goods Funding workstream is putting forth the following recommendation:

1. *Keep the Main Round as is, for now*
In the spirit of continuing Gitcoin’s expansion into public goods beyond just those in Web3 or in the Ethereum ecosystem, we will go with Option 2 and keep the Main Round as is: all grants on the platform with Ethereum payout addresses are eligible for the GR14 Main Round

2. *Spin up a Gitcoin-led [Ethereum Infrastructure Ecosystem Round](https://gov.gitcoin.co/t/can-gitcoin-be-doing-more-to-support-ethereum-protocol-devs/10151/17)*
In addition, we will spin up an Ethereum Infrastructure ecosystem round as a complement to our Main Round which is now more general-purpose.

3. *Have stewards ratify any Gitcoin-led rounds*
To ensure we are spending time on rounds that align with Gitcoin’s objectives, and not expanding too far into areas that are not relevant, we want to bring the scope of Gitcoin-led rounds under the grants governance surface area. We will include the list of Cause Rounds, as well as the ETH infra ecosystem round, for ratification in the GR14 structure proposal. External ecosystem rounds will continue to be outside the scope of governance.

4. *More clearly define platform eligibility & the appeals process*
We will work with FDD to build out clearer guidance around the platform eligibility criteria and how they are communicated, as well as the process for conducting platform-level appeals

## Next Steps

We want to solicit the community’s input on this structure & the long-term direction. Please share comments. We will follow this in the coming weeks with a GR14 Round Structure post for steward ratification.

-------------------------

DisruptionJoe | 2022-04-21 16:24:56 UTC | #2

Thank you for the detailed writeup. You have the commitment from FDD to execute on point #4.

-------------------------
