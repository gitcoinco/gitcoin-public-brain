---
id: 10161
title: "DevRel @ GitcoinDAO"
slug: devrel-gitcoindao
category: governancevision
url: https://gov.gitcoin.co/t/devrel-gitcoindao/10161
created_at: 2022-03-22T15:00:18.630Z
last_posted_at: 2022-03-31T07:35:39.322Z
posts_count: 14
views: 4253
like_count: 33
---

# DevRel @ GitcoinDAO

<https://gov.gitcoin.co/t/devrel-gitcoindao/10161>
owocki | 2022-03-22 15:05:28 UTC | #1

I think there is so much potential in investing developer relations at Gitcoin.

This is informed by [my experience as an Software Developer](https://github.com/owocki) who has heavily relied on Open Source packages through the years.

The objective of this thread is to start a conversation. What should the developer relations practice at Gitcoin look like?

Here are the projects that need developer relations I’m aware of at GitcoinDAO 2022.

* Proof of Personhood Passport
* Grants 2.0
* (any other GitcoinDAO software products on the roadmap which need a thriving developer ecosystem)
* *I’d welcome corrections from any workstream leads on the above list. The above is just my best approximation of the products on the roadmap as they currently stand in the DAO.*

I know that in Grants 1.0, our documentation was quite paltry - it was hard to find, we did not invest a lot in making sure it was updated, and there is generally not a very thriving developer ecosystem built around Gitcoin’s APIs & open source code (though the gitcoin.co product does have plenty of active users, many of them are developers).

We have an opportunity to reset this as we transition from company to DAO, from Grants 1.0 to Grants 2.0. So here is my prompt to you:

* What does good documentation look like?
* How can we make developers first class citizens of Grants 2.0?
* How can we enable a thriving ecosystem built on top of GitcoinDAO’s products?

As we all know from the [Grants 2.0 post](https://gov.gitcoin.co/t/gitcoin-grants-2-0/9981), “Once grants 2.0 is launched, we will have created an environment where the community can test different public goods funding mechanisms on top of a deeply liquid registry of grants.”. What will that community look like? Where will we find them? How will they be enabled? How will they be incentivized? What kinds of tools will they build? What kinds of new innovation will be unleashed in mechanism design by this ecosystem.

I’d be curious if people in the community would be interested in putting forward a proposal to the DAO to formalize a developer relations practice at GitcoinDAO (which currently resides in multiple different groups at varying levels of coordination)

One area I think there is possibly an opportunity is to form an area of practice around Developer Relations which spans across different proucts/workstreams.

![Screen Shot 2022-03-15 at 3.58.14 PM|345x224](upload://5xfyQVRBNefgcShwr6RGQJnxPWf.jpeg)

-------------------------

thelostone-mc | 2022-03-23 14:06:42 UTC | #2

While this deviates a bit from this post -> Since we talk about documentation 

Having an index of all research stories -> not just how the product works but also decisions relating to 
- tech stack
- architecture 
to be documented and shared.

The purpose being a lot of this material could provide context to other workstreams if they had to make a similar problem to solve. Something as trivial as what's the most reliable network to deploy on / web3 service provider to complex decisions like where to dStorage would be helpful 

While regular project / product documenting is required / helpful.
Having this information shared within the DAO -> would enable other projects to take advantage as opposed to re-inventing the wheel.

-------------------------

erich | 2022-03-23 14:41:02 UTC | #3

I agree with the public research and development process, @thelostone-mc! The way @timbeiko [documents](https://github.com/ethereum/pm) the Ethereum core research and development updates might be a good role model as we build [Grants 2.0](https://gov.gitcoin.co/t/gitcoin-grants-2-0/9981?u=leone).

That level of transparency might be super valuable in onboarding new Gitcoin and partner engineers to contribute to and build on top of Grants 2.0.

-------------------------

owocki | 2022-03-23 15:26:52 UTC | #4

[quote="erich, post:3, topic:10161"]
The way @timbeiko [documents](https://github.com/ethereum/pm) the Ethereum core research and development updates might be a good role model as we build [Grants 2.0](https://gov.gitcoin.co/t/gitcoin-grants-2-0/9981).
[/quote]

are you talking about the weekly ACD updates? this? https://hackmd.io/@timbeiko/acd/

cc @nategosselin

-------------------------

erich | 2022-03-23 17:16:02 UTC | #5

The [AllCoreDevs project management repository](https://github.com/ethereum/pm) and the [AllCoreDevs updates](https://hackmd.io/@timbeiko/acd/https%3A%2F%2Ftim.mirror.xyz%2FRXwf30VB-Lr4_56w7Kbe-CVXi-L5DuN0Vpfr06Ww5Cs%3Fdisplay%3Diframe) are different documents but capture similar content.
- The AllCoreDevs project management repository captures the agendas, notes, and recordings of all the AllCoreDevs meetings.
- The AllCoreDevs updates seem less consistent in publication cadence, summarizing vital insights from the AllCoreDevs work.

I think both formats might be valuable as we build Grants 2.0.

-------------------------

timbeiko | 2022-03-23 17:30:52 UTC | #6

Chiming in because I was tagged! I think for ACD specifically, having multiple "resolution" helps different parts of the community follow the process. 

Depending on how much attention you want to give, you can:

* Spend every day in the R&D discord following the latest changes (mostly client devs + researchers)
* Attend/listen to ACD calls in full or read the entire transcript (forthnightly)
* Read my Tweet thread summaries of the calls every (forthnightly)
* Read my or Danny's blog updates about things (every 1-3 months)
* Wait for official network upgrade announcements on the EF blog (1-2x per year)

While these might not map perfectly to your context, I think having a couple different "resolutions" aimed at people with different levels of engagement is a good overall approach if the overhead isn't prohibitive.

-------------------------

erich | 2022-03-23 17:41:27 UTC | #7

Many thanks, Tim — this overview is super helpful!

I'd be delighted to walk you, @kevin.olsen and @lthrift, and the Grants 2.0 team through this map and showcase examples of the different Ethereum AllCoreDevs "resolutions" for our consideration.

-------------------------

schultztimothy | 2022-03-23 22:15:50 UTC | #8

[quote="owocki, post:1, topic:10161"]
I’d be curious if people in the community would be interested in putting forward a proposal to the DAO to formalize a developer relations practice at GitcoinDAO (which currently resides in multiple different groups at varying levels of coordination)
[/quote]
I think this would be great!

[quote="owocki, post:1, topic:10161"]
* What does good documentation look like?
* How can we make developers first class citizens of Grants 2.0?
* How can we enable a thriving ecosystem built on top of GitcoinDAO’s products?
[/quote]
I've always found a codebase/library more approachable when a strongly typed language was used to develop it. I feel like type hinting can act as a form of built in documentation.

I also feel like simple [tutorials](https://docs.uniswap.org/sdk/guides/liquidity/minting) outlining use cases can make projects more approachable to all levels of developers

-------------------------

developerkunal | 2022-03-24 08:58:05 UTC | #9

I think its gonna look like more good if you do like this


Your Full Name

Your Status on Project 

**Project Name**

4th September 20XX

# OVERVIEW

Please write a brief overview of the project including

* Vision of the project in a sentence or two
* Key performance indicators as a list
* Risks and threats to project success

# Target Audience

Clearly define your target audience

# Objectives

1. Obj 1
2. Obj 2

# Why this project

Tell us why is this project important to you

# What will you do

Tell us in detail what this project is about and what the success of this project looks like.

# How will you do it

Tell us how are you going to implement this project

# MILESTONES-

## Milestone 1

Share tangible milestones, it can be qualitative or quantitative both

## Milestone 2

Share tangible milestones, it can be qualitative or quantitative both

# Team

Tell us about your current team if any or future team roles that you may require

# Key Assumptions

Tell us about your key assumption that you have taken into account to ensure the success of this project

# Why will this fail

Tell us the reasons and factors which will lead to the failure of this project

# Project Roadmap after the fellowship

What happens to the project and target audience after your fellowship ends

# Compensation 

What are your expectations of compensation for your work?

-------------------------

ivanmolto | 2022-03-24 11:36:26 UTC | #10

[quote="owocki, post:1, topic:10161"]
How can we enable a thriving ecosystem built on top of GitcoinDAO’s products?
[/quote]

Thank you for sharing your insights, Kevin.
And sorry if my answers deviate from what you are looking for, but I wanted to add some suggestions.

How can we make developers first-class citizens of Grants 2.0?
I think that giving the possibility to fund grants with developers hours could be helpful:
- As a developer, I want to fund a grant with X hours per week for Y months.
- As a donor, I want to purchase hours from a developer to fund a grant.

How can we enable a thriving ecosystem built on top of GitcoinDAO’s products?
Arranging a hackathon around some products with workshops from the teams, and ideation sessions could be a good start.

-------------------------

erich | 2022-03-24 12:23:58 UTC | #11

Indeed, hackathons seem like a natural fit to engage developers with Grants 2.0. Something like the GitcoinDAO Hackathon, which I proposed a while back, might be a good framework for judging and rewards: https://gov.gitcoin.co/t/gitcoindao-hackathon-2022/9405?u=leone.

Relatedly, @brent brought up "Moonshot Collective speed hackathons.“

Besides hackathons, I could also see Grants 2.0 specific quadratic funding grant programs to fund related development work.

🐕🐩🦮🐕‍🦺 dogg fooooodin‘

-------------------------

nategosselin | 2022-03-25 20:43:35 UTC | #12

[quote="timbeiko, post:6, topic:10161"]
Chiming in because I was tagged! I think for ACD specifically, having multiple “resolution” helps different parts of the community follow the process.
[/quote]

:point_up: very much agree with this point — I think really good documentation is nested in a way that enables people to easily skim OR drill into the details. I like to use the 1 sentence, 1 paragraph, 1 page framework for this: does the reader need the one-sentence summary of the idea you're communicating, or do they need a page's worth of detail?

-------------------------

gloria | 2022-03-30 17:56:51 UTC | #13

I really enjoyed this discussion about the importance of DevRel in the Web3 space. It happened this morning. https://twitter.com/i/spaces/1LyxBoBdYmkKN?s=20.  I can definitely see the need for this position at Gitcoin.

-------------------------

thelostone-mc | 2022-03-31 07:35:39 UTC | #14

Oh if you record / throw in an invite whenever that happens. I'd love to listen in as well

-------------------------
