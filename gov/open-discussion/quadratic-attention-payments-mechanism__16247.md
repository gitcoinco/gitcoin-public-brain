---
id: 16247
title: "Quadratic Attention Payments Mechanism"
slug: quadratic-attention-payments-mechanism
category: open-discussion
url: https://gov.gitcoin.co/t/quadratic-attention-payments-mechanism/16247
created_at: 2023-08-12T09:30:33.928Z
last_posted_at: 2023-09-28T16:08:18.031Z
posts_count: 8
views: 4152
like_count: 18
---

# Quadratic Attention Payments Mechanism

<https://gov.gitcoin.co/t/quadratic-attention-payments-mechanism/16247>
bernardovic | 2023-08-12 09:32:40 UTC | #1

I've been developing a mechanism around the Quadratic Attention Payments (QAP) concept, which aims to rethink public advertising in important ways. By leveraging quadratic voting principles, this mechanism empowers users to influence the ads they view, incentivizes advertisers to produce higher-quality and more relevant content, offers more accurate — but private — data for publishers, and boosts revenue and rewards for all parties.

### Genesis

For greater context into its origin, the initial idea was proposed by Vitalik Buterin on his essay *Quadratic Payments: A Primer*. In it, he argues that public ads, as a subsector of public goods, are a non-optimal good as the public does not have an efficient way to coordinate in selecting the ads that interest them. Consequently, we end up with a lot of ads we actually don’t want to see.

This is the problem this mechanism tries to solve. Across several iterations, including with Vitalik’s direct feedback, I have matured the mechanism to its current version.

### How QAP Can Work

This mechanism empowers:

- **Users** to upvote or downvote ads by how many degrees of preference (*D*) they want. The fee required for voting is equal to *D^2*, thus quadratic. Users benefit from the gradual improvement in relevance of and better content in ads they see, and earn rewards for their voting participation.

- **Advertisers** submit their ads and pool an initial deposit (*ID*) for their campaign spend. Based on the % of user downvotes on their ad and the quadratic fees (*QF*), their reimbursement would be calculated as:
    
![Image 12-08-2023 at 10.22|690x57](upload://6AnRAyHnPd6nIKoQfDcwK9794nm.jpeg)

   Therefore, the actual campaign cost (or amount that stays locked) would be:
    
![Image 12-08-2023 at 10.23|690x59](upload://qk5a07hZseS418kJCtShDU5P1WC.jpeg)
    
Or:
    
![Image 12-08-2023 at 10.23|690x56](upload://dDFrEQ2vMrEklKb8tFrL8qBdyTQ.jpeg)
    
Out of the *Final Campaign Cost* effectively paid by Advertisers, the platform that implements this mechanism can derive a % for itself and another to be rewarded to participating users. In this system, the monetary and engagement value advertisers get is increased for the same ad expenditure.

    
- **Publishers** collect the users' degrees of preference recorded. This helps them assess the users that the ads most resonated with, and, as a result, how to better instruct Advertisers on how and which users to tailor subsequent ads to. The more efficient the Advertisers’ ads are at generating sustained user attention, the greater the Publishers's revenue likely becomes.


At the end of the Advertiser’s campaign and after all the user preferences recorded, the ad gets extended or reduced according to the sum of the degrees of preference (*D*) — positive for upvotes, negative for downvotes:

![Image 12-08-2023 at 10.26|690x53](upload://6ResD52ZwZHscdJA2HLoz0dT8lo.jpeg)

Looking at the example below, the original duration of Advertiser A’s ad was 60 seconds and the *Ad Duration Variance* = +10, therefore A’s ad gets extended to a total of 70 seconds.

![Image 07-08-2023 at 00.59|690x282](upload://iKEOaH8ExQaplSsB9BesDXrKMHS.jpeg)

Users will get to see more of the ads that they value most and advertisers become incentivized to put up better and more valuable ads. The public good is improved through effective public coordination.

**Future Roadmap**

Experimenting with auction-related Harberger taxation systems, funds pooling and redeeming mechanism, and ZK proofs for secure and unique voting submissions.

### In sum

In essence, the Quadratic Attention Payment's public coordination and compensation system centers around an improved advertising experience for all stakeholders, whilst furthering a user-centric ethos. Particular use cases can include decentralized social networks and platforms with ad-driven products, like the Brave browser.

-------------------------

quaylawn | 2023-09-01 16:15:13 UTC | #2

[quote="bernardovic, post:1, topic:16247"]
In essence, the Quadratic Attention Payment’s public coordination and compensation system centers around an improved advertising experience for all stakeholders, whilst furthering a user-centric ethos. Particular use cases can include decentralized social networks and platforms with ad-driven products, like the Brave browser.
[/quote]

Love this idea :) what does moving this forward look like?

-------------------------

bernardovic | 2023-09-01 17:33:53 UTC | #3

Something interesting could be done on the Brave Ads/BAT ecosystem level. Drafting it up.
Also Lens' Fee Collect feature looks promising, from a glance.

-------------------------

quaylawn | 2023-09-01 18:51:55 UTC | #4

defo keep us updated! I'd be keen to see this go live at some stage

-------------------------

thelostone-mc | 2023-09-26 09:24:53 UTC | #5

Ah just read though the post!
This is def something which can be easily built as an Allo v2 Strategy.

Just going through the post, it looks like 

- We'd have 1 pool
- Publishers can create a profile on registry
- Publishers can register to the pool 
- Publishers would be able submit ads for duration (during which they pay the initial deposit )
- Users could then upvote/downvote based on a specific AD token ( like BAT )
- Once the ad duration ends, the publisher can withdraw the reimbursed amount.

This makes sense and I think new strategy would need some logic to handle the 
- submit ads
- update the reimbursed amount based on downvotes

Everything else we requires is already in base interface \m/

@bernardovic Would love to hear your thoughts on
How would we incentivize the user to participate? 
Is it as simple as the ads campaign cost is distributed to all the voters proportionally?

-------------------------

bernardovic | 2023-09-28 10:22:50 UTC | #6

The main value proposition on users’ side is the improvement in ad content being shown and better rewards vs. the quadratic fees they’ve submitted.

My first hunch was proportionately based on the number of users that voted, but based on the weight of quadratic fees submitted per user would make more sense, actually. A reputation system, more down the line, could be useful to implement as well, where we’d reward for loyalty and/or activity.

There’s also been a slight correction to the mechanism where additional funds would be at the disposal of the pool to do whatever interesting; open question right now.

-------------------------

thelostone-mc | 2023-09-28 10:42:25 UTC | #7

Ah okie this makes sense ! 
A use case different from the grant ecosystem!
Would love to see this implementation on allo and have some run a pool with this

-------------------------

Decentralizedceo | 2023-09-28 16:08:18 UTC | #8

Off Prima Facie, I would think that QAPM is similar to a Web2 algorithms now, until I read further. Instead of pushing out ads via popular demand and persuading, QAPM allows the individual the free will to go towards their own interests. That is an illuminated way to satisfy all parties involved. Great BM!
As we are building  a platform called SoundView, we have been looking for ways to reward engaged users and I think this could be easily implemented. I would like to read more on the "Auction-related Harberger taxation System."

-------------------------
