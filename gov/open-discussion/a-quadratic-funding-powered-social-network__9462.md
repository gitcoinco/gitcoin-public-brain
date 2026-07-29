---
id: 9462
title: "A Quadratic Funding Powered Social Network"
slug: a-quadratic-funding-powered-social-network
category: open-discussion
url: https://gov.gitcoin.co/t/a-quadratic-funding-powered-social-network/9462
created_at: 2021-12-18T22:24:19.943Z
last_posted_at: 2023-01-26T11:16:37.920Z
posts_count: 19
views: 7493
like_count: 35
---

# A Quadratic Funding Powered Social Network

<https://gov.gitcoin.co/t/a-quadratic-funding-powered-social-network/9462>
owocki | 2023-01-17 16:24:50 UTC | #1

*Note: This post assumes the reader is already familiar with what makes Quadratic Funding Powerful.  If that is not you, please checkout [https://wtfisqf.com/](https://wtfisqf.com/) first!*

## The Quest for a better social network.

In [July 2021](https://www.youtube.com/watch?v=oLsb7clrXMQ) Ethereum Founder Vitalik Buterin shared a [list of things that matter in Ethereum past Defi](https://www.youtube.com/watch?v=oLsb7clrXMQ), which listed the following

> Sign in with Ethereum,  Social Networks, Public Goods

Yesterday at the [RadXChange Denver 2021 Conference](https://www.radicalxchange.org/2021-conference/denver/), during the "Regenerative CryptoEconomics" breakout, we explored the problems with web2-era social networks, and what a web3-era social network that was more regenerative to the ecosystem it served might look like.

These two experiences have inspired me to write up a document detailing an experiment that I spearheaded at Gitcoin in early 2020 involving *public goods + social networks*.

## The Experiment

### The Social Network

One problem that novel social networks have is how to bootstrap their network effects.

Before you have any users on your social network, you won't have any utility for people who join.  Before there is any utility for people who join, there won't be any users on a network.  It's a vicious cycle.

![social-media-3846597_1280-1|690x435, 50%](upload://wGWytPo3PvGPNAPdFPU1QK0ieOM.png)

Gitcoin didn't have that problem at all, because 

1. Gitcoin Grants were growing rapidly during the bear market.
2. Gitcoin Hackathons was too.
2. [In early 2020](https://web.archive.org/web/20200406173347/https://gitcoin.co/results), we we had 20k active users and had already delivered about $4mm to OSS developers.  

### The Gitcoin Activity Feeds

With this growing usage, we were trying to figure out a few things:

1. How could we make Gitcoin feel more like a community?  Give it a shared space where you could have chance encounters just by showing up.
2. How do we surface novel/interesting ways ton show the activity of the network?
1. People would come to Gitcoin once or twice a quarter to contribute to a hack or grant, how could we get them coming back more to partcipate in [our mission](https://gitcoin.co/mission) often?

In 2020, we had been experimenting with building a handful of ways to solve these problems, and [Gitcoin's Townsquare](https://gitcoin.co/townsquare) was one of them.  

It was place where we could aggregate all of the interesting happenings across Gitcoin into one place.  After all, lots of interesting public goods funding was happening on Gitcoin, and stepping into the 'Townsquare' would be a novel way to navigate that, right?

The idea ended up looking something like this:
![Screen Shot 2021-12-18 at 2.20.20 PM|382x500](upload://9a1ufys225WObSw4V4BCwyj31j1.png)

Looks like a standard newsfeed, right?

It is.

And just like that, we stumbled into building a web 2.5-era social network.  The ux felt like web2, but it was web3 enabled, so we playfully call this era of Gitcoin web 2.5. :)

### Let's not zuck it up!

The problems with web2 social networks are well documented elsewhere.  They aren't forkable, they create polarity, they're like battle royales where nasty arguments can develop.   

We were determined to leverage our web3-ness to mitigate some of these problems and create something novel.

We were also interested in using this town square tool to solve the problems of people who were already on Gitcoin.  Members would share lots of different types of things on their Gitcoin newsfeeds.
1. They'd promote their grant.
2. They'd try to hire people.
2. They'd ask how Gitcoin worked.
3. They'd ask for customer support.
4. They'd share memes.

One of the consistent themes I'd seen was that when people had a job to be done, they'd come to the newsfeed + ask for help from the community.

But we weren't seeing many people show up to answer questions, to explain how things work, or to give thoughtful feedback.

So we started experimenting with ways to solve this problem.

### Tipping

In order to create incentives for people to help each other, and to [build in public](https://www.buildinpublic.xyz/) on a web3 primitive, I built the ability to tip other users in the newsfeed.

Here's what it looks like:

![Screen Shot 2021-12-18 at 2.36.50 PM|690x166](upload://Ab3yjTAWB1K6n4AejChipHEwnxp.png)
You can send a tip by clicking on the little Ether symbol on the newsfeed.

![Screen Shot 2021-12-18 at 2.35.06 PM|690x291](upload://oNOekDcipDJ4RfMWIRc2OdCxpTU.png)
and decide how much to send in the next dialogue.

#### Tips > Likes

**Likes are the ultimate shitcoin!**  They're infinite supply, you can't spend them on anything.  They're like little ephemeral dopamine rushes to consume, but they leave the creators who receive them feeling empty!

One of the things we wanted to prove here was that it was possible to build a social network on *something more web3-native than likes*.  

I wanted to provide something more valuable to our users than likes.  It felt intuitively like a micro-tip was a better measure of whether a piece of content was actually truly valued or not.  

People *like something* when it creates a visceral reaction.  People *tip someone* when they feel like they've truly been provided value.  

There is a subtle but important difference there.

#### .. but who cares about earning 30cents?

At the time of this experiment, 0.001 ETH was about 30c.  And gas fees on the Ethereum mainnet were low enough that you could send a 30c transaction without worrying about gas.  Ahh those were the days!

One thing that we saw when we launched tips was that people weren't really using it.  And when we asked them why they weren't using it, the answer us [unequivocally](https://twitter.com/owocki/status/1224042348335644672) "meh, 30c, who really cares?"

So we tried an experiment.  We took the biggest, most powerful mechanism we know of, [Quadratic Funding](https://wtfisqf.com/), and pointed it at the problem.

### Mini Quadratic Funding 🚀

In early 2020, I [quietly launched](https://github.com/gitcoinco/web/pull/5942) a thing we called "Mini Quadratic Funding" Rounds.  

It was a $200 per week subsidy to those who were providing helpful commentary to the platform.  Here's how it looked:

Every  week we put 200 DAI into a matching pool, and we loudly advertised to the users that if they received tips they would receive quadratic matches (just like they already did in Gitcoin Grants).

Here's a module that advertised the leaderboard of the Mini CLR Rounds
![75190350-1dded680-571e-11ea-8d14-eb1cf2881f1d|419x357](upload://xNIIMsU36wQ9310o8oRj7nSItRE.png)

### We have a hit!


Over the next few months, people sent 100s of tips:

![Screen Shot 2021-12-18 at 2.41.26 PM|690x377](upload://miaXfxvToJ37wQfCVZQ4ZYU6jQW.png)

The median tip amount was the default amount, 0.001 ETH ($0.30 at the time), but the median match amount was 0.005ETH ($1.50) at the time.

Here was the distribution of tip amounts by num tips:

![Screen Shot 2021-12-18 at 2.43.42 PM|690x137](upload://ziTQDM9wyllOXrBDId0jCHesbYC.png)

Over the subsequent  weeks, we ran 14 successive Mini QF Rounds, with 2,348 contributions resulting in 1,085 matching payouts/

![Screen Shot 2021-12-18 at 2.17.44 PM|532x499](upload://4J06WhHPJcswa5m5kZytlbI7FyZ.png)

### Behavior Change

Most importantly, we saw a large behaviour change in the participants. 

1. DAUs went up.
1. Community members seemed to really care about climbing the leaderboard.  
1. They went from passively ignoring each others help requests, and more actively helping to problem solve - directing support requests to the relevant Knoweldege Base entries, answering questions about the network.  

Effectively, this experiment it created a class of community member that earned by being helpful + providing value.

I [tweeted](https://twitter.com/owocki/status/1230633929280933888) about the behaviour change we saw:

![Screen Shot 2021-12-18 at 3.01.01 PM|253x500](upload://1OdlARZHTPj8mD7AmDTDGBvnVWm.jpeg)

### A Sybil Resistance Honeypot

![virtual-honey-pot-sized|650x400, 50%](upload://w04ZGO4o78AcZTd7QTx0NuxiH1M.jpeg)


One other benefit of the Mini QF experiment was that it allowed us to speed run the sybil resistence tools we were quietly building for use in the main Gitcoin Grants rounds.  

The main Grants rounds were 1x/quarter, and having a [honeypot](https://blog.24by7security.com/honeypots-and-how-they-can-secure-your-network?https://www.24by7security.com/cmmc) 1x/week QF round meant that we could see how attackers were attacking the system and learn about how to mitigate it even better.

Some of those insights endure as a major part of our [sybil resistance strategy today](https://gitcoin.co/blog/a-community-based-roadmap-for-sybil-detection-across-web-3/).

### Overcome by events.

Unfortunately, circumstances turned against the experiment:
1. gas fees on the eth mainnet went up in summer 2020 (colloquially known as DEFI summer)
2. we moved onto other things, like integrating ZKSync into Gitcoin Grants or adding a [bulk checkout](https://twitter.com/owocki/status/1279092094720598017) on Gitcoin Grants, or trying to figure out what GitcoinDAO would look like. Or the move towards creating a new landing page & navigation structure for Gitcoin, so people could get around easier.  Or the [imminent spinout from Consensys](https://decrypt.co/66541/ethereum-gitcoin-raises-11-million-spins-out-consensys)

Because of those events, we had to abandon the mini QF experiment and refocus on our core - Gitcoin Grants.

But I continue to think there is the KERNEL of a great idea here.  What if we replaced likes with micro-tip subsidies all across social media?  Would we close the asymmetry between value created and value captured for creators on social media, and realize Vitalik's dream of web3 social media?

These are big ideas.  I hope that I have played a small part in validating them.  I continue to be focused on building Gitcoin Grants. 

If anyone wants to take up this mechanism, please reach out.  I'd love to support you.

## example posts

edit; 12/19/2021, i'm attaching a few examples of posts here that got a lot of tips from 2020, so give a sense of what kind of posts this mechanism optimized for..
 
![Screen Shot 2021-12-19 at 5.50.28 PM|690x494](upload://tUNEvOWqpNcTDOq6eLGddMglnnj.jpeg)
![Screen Shot 2021-12-19 at 5.49.56 PM|690x495](upload://a8OnlM76pvsNi153gXxygsY9rlk.jpeg)
![Screen Shot 2021-12-19 at 5.49.36 PM|690x493](upload://yfbWNx6ql6M57i3zpTFstTnxDOb.png)
![Screen Shot 2021-12-19 at 5.49.19 PM|690x429](upload://ueEafzcCwHiW8xM0qOX9ZpBJwk5.jpeg)
![Screen Shot 2021-12-19 at 5.49.01 PM|690x463](upload://xHO46CJXhG2VwZPoyAH8uHV3gSq.png)

-------------------------

auryn | 2021-12-18 23:15:34 UTC | #2

I really dig this concept and explored a tangentially similar idea in burn signal, which ultimately suffered from the same gas price issues (along with some other questionable assumptions)

I've often wondered about using Medium-like claps for QV / QF in the context of a publishing or social media platform. @anneconnelly's Quadratic Trust was a really nice experiment in this direction. CLR.fund is going to leverage some version of this for recipient curation at some point.

-------------------------

owocki | 2021-12-18 23:54:26 UTC | #3

Yes Quadratic Trust deserves it's own retrospective post :slight_smile: 

> which ultimately suffered from the same gas price issues

I'm kicking myself for not just biting the bullet + migrating this to a L2 so it could live on ....

-------------------------

auryn | 2021-12-19 00:29:46 UTC | #4

[quote="owocki, post:3, topic:9462"]
I’m kicking myself for not just biting the bullet + migrating this to a L2 so it could live on
[/quote]

The L2 ecosystem is in a much better place to make this a reality now though.

Since you mentioned web 2.5, I'd love to explore how to push the town hall / feed feature to full web3. One option could be to use a shared data layer via something like [Poster](https://github.com/onposter/contract) on a cheap L2/sidechain.

-------------------------

ntnsndr | 2021-12-19 00:52:20 UTC | #5

Might it be worth considering integrating this idea with ethereum.world?

Nice to see you at RxC:)

-------------------------

tjayrush | 2021-12-19 01:31:30 UTC | #6

This is a really nice idea -- mini-grants / tips.

What would be super cool would be a javascript code snippet that people could drop into a website. Copy and paste tips.

-------------------------

socal434 | 2021-12-19 11:37:45 UTC | #7

I think the tips>likes is great. Instead of mindlessly smashing like you really put thought into who earned that commendation. Using Brave browser it is already kind of baked into it with $BAT on some social media sites and I think twitter is doing its own native thing with tips too (if I remember correctly). I think it should be moved to an L2 and revived because it would help to foster quality content in my opinion.

-------------------------

owocki | 2021-12-20 00:51:24 UTC | #8

attaching a few examples of posts that got a lot of tips from 2020, so give a sense of what kind of posts this mechanism optimized for..
 
![Screen Shot 2021-12-19 at 5.50.28 PM|690x494](upload://tUNEvOWqpNcTDOq6eLGddMglnnj.jpeg)
![Screen Shot 2021-12-19 at 5.49.56 PM|690x495](upload://a8OnlM76pvsNi153gXxygsY9rlk.jpeg)
![Screen Shot 2021-12-19 at 5.49.36 PM|690x493](upload://yfbWNx6ql6M57i3zpTFstTnxDOb.png)
![Screen Shot 2021-12-19 at 5.49.19 PM|690x429](upload://ueEafzcCwHiW8xM0qOX9ZpBJwk5.jpeg)
![Screen Shot 2021-12-19 at 5.49.01 PM|690x463](upload://xHO46CJXhG2VwZPoyAH8uHV3gSq.png)

-------------------------

Lunacat | 2021-12-20 15:35:32 UTC | #9

This is a fantastic idea.  I'd be more inclined to try and build this idea into something that already exists as opposed to creating something completely new.  Competing decentralized social media apps will run risk of fragmenting "liquidity" of user bases, similar to all the competing liquidity pools and L2s that are starting to consolidate.  Peepeth is still alive and kicking and shares much of the above ethos, and they have a tip feature that people were pretty actively using when it first launched; if a quadratic matching pool could be funded and tipping/likes moved to an L2, I could see that gaining some traction.  Might be a way to leverage what they (or someone else) has already built?  Granted, Peepeth specifically is focused on Twitter model while you've laid out a Facebook one, just using them as an example of possible "synergies" out there..

-------------------------

farmerxt | 2021-12-22 10:52:39 UTC | #10

its a module and can potentially be integrated into minds/com
//question!!

-------------------------

ManuAlzuru | 2021-12-29 00:25:21 UTC | #11

Amazing experiment, thanks again for sharing your learnings @owocki. I would love to learn more about Quadratic Trust that @auryn mentioned by @anneconnelly. Where can I learn more?

-------------------------

auryn | 2021-12-29 00:36:50 UTC | #12

[quote="ManuAlzuru, post:11, topic:9462"]
Where can I learn more?
[/quote]

You can find it at http://quadratictrust.com

-------------------------

anneconnelly | 2022-02-07 04:07:07 UTC | #13

I'll be presenting on it at Schelling Point in Denver and you can also check out this blog: https://anneconnelly.medium.com/quadratic-trust-339e3569475d

-------------------------

bestape | 2022-11-04 16:50:20 UTC | #14

Experimenting with tips in LexDAO Clinic right now. Thanks for this. Really like the idea of QF boosting tips.

-------------------------

ZER8 | 2022-11-05 21:09:55 UTC | #15

[quote="owocki, post:1, topic:9462"]
How could we make Gitcoin feel more like a community? Give it a shared space where you could have chance encounters just by showing up.
[/quote]

This is a great post. It's always amazing to see that the level of experimentation in Gitcoin is always mooning.

As a member of the community that worked for the DAO and joined organically and Stewards I sometimes feel that the community would need more than a space and could highly benefit from QV. This could be an area in which 1H1V could make a huge difference. Maybe until or during the next bull the DAO could experiment with 1H1V and enable the creation of organic pods in a bottoms up way. They would organize around common goals that would apply for funding via grants. They could even compete for the same goals/outcomes, but not in a winner takes all fashion.

-------------------------

monk2525 | 2022-11-07 14:10:10 UTC | #16

This is a really nice idea – mini-grants / tips.

-------------------------

guoliu | 2022-11-16 17:10:07 UTC | #17

We have been using micro-tipping (USDT on Polygon) on Matter.News for users to curate content, and are now starting to do donation-matching: exactly the same idea described here! So glad I found this post.

The biggest challenge we had was how to rank content based on tipping. If we use tipping times and amounts directly, people can easily create different accounts and tip each other, and occupy everyone's attention.

-------------------------

KazanderDad | 2023-01-26 02:11:14 UTC | #18

Folks,

Check out [GoodMicroGrants](https://www.goodmicrogrants.com/), currently in proof of concept. A quadratic matching site for any tipping transactions and/or purchase transactions. As long as they are between real humans it counts. Not a pure play social tipping protocol, but tipping is encouraged and certainly counts towards your "microgrants".

Tweet and share if you can.

-------------------------

DisruptionJoe | 2023-01-26 11:16:37 UTC | #19

How do you know if they are real humans or not?

-------------------------
