---
id: 16561
title: "RFC: AI Dashboard for Governance Proposals"
slug: rfc-ai-dashboard-for-governance-proposals
category: open-discussion
url: https://gov.gitcoin.co/t/rfc-ai-dashboard-for-governance-proposals/16561
created_at: 2023-09-24T20:38:45.749Z
last_posted_at: 2023-11-21T04:22:29.547Z
posts_count: 11
views: 4846
like_count: 27
---

# RFC: AI Dashboard for Governance Proposals

<https://gov.gitcoin.co/t/rfc-ai-dashboard-for-governance-proposals/16561>
skyfoxx | 2023-09-24 20:40:17 UTC | #1

## The problem of governance

We are a team of Web3 builders, working on ways to help DAOs make better decisions, *faster*.

One pattern we have found in different DAOs is that they are impacted by *excessive* *governance burden*, which comes from the need to:

* Moderate online forums (like discourse)
* Consume proposals easily (getting to the point)
* Differentiating proposals (the good from the bad)

## A Visual solution for governance burden

We are exploring ways of representing proposal information visually, so it can be consumed quickly & easily. We use a combination of AI customized specifically for DAOs, and other software libraries.

#### Visual Summaries

For example, the general sentiment of comments on a proposal can be presented visually, so that a quick glance (rather than a 10 minute read) will give the reader an idea of the receptivity of the proposal.

![image|688x213](upload://9o5bmwHBtDS2C23unmU7EQsvKIu.png)


*In this example, users strongly favor the proposal.*

#### Mind Maps

Another way that proposals can be distilled is through mind-maps, to help users quickly gauge the benefit of a proposal. The mind map below has been generated from: [[GCP-009] - Upgrading Gitcoin’s Governance Contracts](https://gov.gitcoin.co/t/gcp-009-upgrading-gitcoin-s-governance-contracts/14010)

![image|690x368](upload://lL1alypZfXNZOhajQRO1XSOVpbu.png)


#### Tables

Tables can also create a way for quick proposal consumption. The table below has been generated from: [[GCP-009] - Upgrading Gitcoin’s Governance Contracts](https://gov.gitcoin.co/t/gcp-009-upgrading-gitcoin-s-governance-contracts/14010)

![image|690x365](upload://cqYUKXmmx0xgIRaQX2LcVPvGqsj.png)


## Our offer

We are looking for DAOs to participate in our alpha version of our dashboard. By offering our service free to the first DAOs that sign up, we hope to:

1. Use live proposal data to generate dashboards for the participating DAO
2. Get feedback and iterate to give the DAO better proposal management tools

#### To Participate

To accomplish this, we need participating DAOs to provide a read-only API key of their discourse platform. This will allow us to pull proposal data and package it in a way that is easy to consume for DAO users.

In summary, we are offering:

1. A way to reduce the governance burden through AI digests of proposals
2. To participate, Gitcoin needs to provide a read-only key of the discourse platform
3. Being read-only, this is risk-free and allows us to provide a dashboard for easy AI digests
4. Feedback from the community will allow us to improve the AI digests
5. This service is offered free to Gitcoin DAO, as it helps us improve our product.

-------------------------

krrisis | 2023-09-25 14:22:25 UTC | #2

This looks great! 

@kyle and @deltajuliet are probably the people who could sign off on an experiment like this, not entirely in the loop on steward governance plans

-------------------------

CoachJonathan | 2023-09-25 18:03:59 UTC | #3

Hey @skyfoxx this looks great. Do you have any case studies of other DAOs using this kind of visualization and seeing tangible upticks either in participation or comprehension?

Also, would you be willing to do another example from another recent post, just to get a sense of some more visualizations? Maybe something that is not as comprehensive as GCP009 (since most posts are not very comprehensive and might not be as data rich).

I love the idea of visualizing more info in the gov forum (which is currently very text heavy).

-------------------------

kyle | 2023-09-26 01:18:18 UTC | #4

I am down to get a read-only API key out to you. Shoot me a DM :slight_smile:

-------------------------

carlosjmelgar | 2023-09-26 19:40:58 UTC | #5

This is really cool. Also interested in seeing other GCP examples and learn about other DAOs using it, or interested in using it. 

Do the visualizations sort or link to the responses they reflect? If I click on the heart eyes, or "Onchain governance expansion", will I be directed to the comments represented? 

[quote="skyfoxx, post:1, topic:16561"]
We use a combination of AI customized specifically for DAOs, and other software libraries.
[/quote]
Can you share more on what this combination looks like? 

Are users able to customize the visualizations? For example, the [Vince McMahon reaction meme](https://imgflip.com/memegenerator/127634487/Mr-McMahon-reaction) instead of the emoji faces? 

Very interesting. Would love to play with this.

Next week's community call is a wrap up of recent Gov Posts. Would you be interested in joining to share more about this? It's on Wednesday at noon EST.

-------------------------

skyfoxx | 2023-09-26 21:44:31 UTC | #6

Thanks for the feedback!
> Do you have any case studies of other DAOs using this kind of visualization

We are in early alpha so don't have any case studies yet. The idea is to build out the idea with some participating DAOs.

I ran the tool through this GloDollar proposal :slight_smile: 

https://gov.gitcoin.co/t/proposal-diversify-gitcoin-stablecoin-holdings-by-exchanging-usdc-for-glo-dollars/16398

A quick summary:
![image|690x185](upload://zXPC3rkrB8iBGLTnSRCD1VYCU1x.png)

![image|690x175](upload://6TPz5ZwMYZk35zjNsCos2p1woNL.png)

![image|690x389](upload://yYhFExuQ8jR7qjnmfxifNFZsfoO.png)

![image|690x371](upload://89OFDT8s7F6ykaxtLgUi0c3BX8T.png)


![image|690x299](upload://lOMOSYJAyEyGVa11FsKeltGo4Wh.png)

Note these are experiments we are working to improve on (based on feedback, of course)

-------------------------

skyfoxx | 2023-09-26 21:53:31 UTC | #7

dm'ing - note we are in early alpha but we want to work with DAOs so we can build with them itteratively.

-------------------------

skyfoxx | 2023-09-27 02:02:06 UTC | #8

> Can you share more on what this combination looks like?

Pretty straightforward, actually. Most of the lifting is done using [langchain](https://js.langchain.com/docs/get_started/introduction/). To simplify a proposal, several LLMs are chained together. E.g. one's job is is to fetch context online around a proposal, another one is to decide what context is needed to fetch, another one summarizes, another highlights, etc.

The prompts are specifically designed to work with proposals, so it's not something throwaway like: "summarize this". Each type of analysis (e.g. pros & cons of a proposal) will go through maybe 5 LLMs. After that, simple javascript libraries to convert generated markdown to html, or to a mindmap. Happy to share more details.

> Also interested in seeing other GCP examples

Here is one I just did

https://gov.gitcoin.co/t/rfc-ai-dashboard-for-governance-proposals/16561/6

> Do the visualizations sort or link to the responses they reflect? If I click on the heart eyes, or “Onchain governance expansion”, will I be directed to the comments represented? Are users able to customize the visualizations?

Actually really cool ideas. Right now, it's super alpha and rough so we want to get ideas from the DAOs and polish it up so it's good. (In weekly short sprints). Since we have the structure set up, should be super easy to polish up. It still makes occasionall mistakes for now.

> Next week’s community call is a wrap up of recent Gov Posts. Would you be interested in joining to share more about this? It’s on Wednesday at noon EST.

Would actually love to demo and get some feedback. How can we arrange a slot? Also, could you let me know if there are specific proposals you'd like me to run through the tool for then?

-------------------------

kyle | 2023-10-04 16:23:21 UTC | #9

I dont see a DM, but let me know if I missed something.

-------------------------

Adedipupo | 2023-10-05 21:30:47 UTC | #10

Good ideas. I like this Proposals actually I can see it's waiting for the approvement. and I support this teams. But let us having a conversation from our people here.

-------------------------

skyfoxx | 2023-11-21 04:22:29 UTC | #11

We're still working on something in the background, based on feedback we received - This was super appreciated. :pray:

-------------------------
