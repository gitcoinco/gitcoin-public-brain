---
id: 16525
title: "[GCP-015] - Sybil Attacker QF Round"
slug: gcp-015-sybil-attacker-qf-round
category: governance-proposals
url: https://gov.gitcoin.co/t/gcp-015-sybil-attacker-qf-round/16525
created_at: 2023-09-15T00:16:43.198Z
last_posted_at: 2023-11-07T16:37:04.254Z
posts_count: 15
views: 6274
like_count: 58
---

# [GCP-015] - Sybil Attacker QF Round

<https://gov.gitcoin.co/t/gcp-015-sybil-attacker-qf-round/16525>
umarkhaneth | 2023-11-07 16:35:31 UTC | #1

# GCP-015: Sybil Attacker QF Round


**Co-authors:**  @Jeremy & Umar

Thank you to @owocki , @meglister , @azeem , @MathildaDV , @CoachJonathan, @Sov , @connor , @M0nkeyFl0wer , @epowell101 for feedback on this GCP and/or conversations about the idea 
## This has been posted on [snapshot](https://snapshot.org/#/gitcoindao.eth/proposal/0xc8afbc5dcc6ee94434e5b828ff9c92ce020861a3a6604ed8090cb077d6b919ce)
## Summary:

Create a $5k quadratic funding round specifically for individuals with the skills to launch a sybil attack to come and claim the funding if they share information on how they do it.

## Abstract:

Sybil Defense is one of the largest problems facing Web3 and the reason for the existence of Gitcoin Passport. Sybil Resistance enables UBI, more effective airdrops, better quadratic funding, and much more.

Over the years, Sybil Attackers could have stolen millions of dollars from Gitcoin and the Ethereum ecosystem. Gitcoin’s unique position is similar to a bank holding funds on behalf of the ecosystem and every quarter we open the vault to give out money to the people placed in line by our community. Yet among those people there are some wearing disguises, impersonating honest actors, in order to steal from the bank.

While we’ve developed defense mechanisms against these robbers (such as asking to see their passport) we haven’t implemented one of the most common techniques banks use to defend against robbers both in-person and online. Trying to break into your own bank.

When you try to break in yourself you learn exactly where the weaknesses in the system are and can then design new methods to strengthen those locations. With this round, we’re offering an incentive for hackers to try to break into our system and tell us where our weaknesses are. Once we’ve shored them up we’ll then be in a better position to implement quadratic funding and aid the web3 ecosystem at large with sybil defense.

## Motivation:

“[In a red team/blue team exercise, the red team is made up of offensive security experts who try to attack an organization’s cybersecurity defenses. The blue team defends against and responds to the red team attack](https://www.crowdstrike.com/cybersecurity-101/red-team-vs-blue-team/).”

So far, Gitcoin and its community have played the role of the blue team. We defend from sybils and we often do so in an open-source way that reveals how we work to our adversary.

Our lack of knowledge about how the red team operates and attacks our system limits our ability to defend against them. Yet in our ecosystem we have people with the technical ability to break into our system who may have resisted doing so only because of their moral concerns. Let’s invite them to do what they’re good at and work with us.

The best part? No squelching.

## Specification:

Grants Stack makes it extremely easy to spin up a QF round. We will start one with the following rules:

* All non-offensive applications are accepted
* Grants must get at least 100 unique contributions above a 20 passport score to receive any matching payout
* Grants must share a detailed document on how they attacked the system via email before payouts and be available to answer questions (and preferably, but not required: hop on an anonymous voice call)
* 80% matching cap: if a single attacker drastically outcompetes the others they can claim up to $4k
* All donors will be labeled as Sybils in the Passport data sets and may not be able to receive scores or reuse credentials in the future

This will also require support from the MMM team to communicate about the round to draw in participants. This would involve:

* One design asset
* One or two emails
* Several tweets

Something similar to what Yearn did: 
https://twitter.com/yearnfi/status/1683892836393943048



## Benefits

* Insights into how sybil attacks are conducted
* Insights into how to improve our sybil defense
* Possibility to create new partnerships with proven experts

## Drawbacks

* Costs $5k
* Creates pressure to rapidly shore up our defenses after identifying key learnings

## Vote (tbd on Snapshot)

**Yes:** Pilot the Sybil Attacker QF Round and allocate $5k from the matching pool

**No:** Do not fund this work and do not move forward

**Abstain:** I am missing context or this proposal needs more refinement

## Temperature Check

[poll type=multiple results=always min=1 max=2 chartType=bar]
* Yes - Pilot the round for $5k
* No - Do not fund
* Abstain
[/poll]

-------------------------

Sov | 2023-09-15 00:55:42 UTC | #2

I support this proposal and the amazing work @umarkhaneth is doing here at Gitcoin.

-------------------------

owocki | 2023-09-15 03:25:29 UTC | #3

is gitcoin passport a cost center for gitcoin?  or is it a billion dollar opportunity to bootstrap an ecosystem of sybil resistent dapps that uniquely gitcoin can do?

if the former, then ppl likely will want to skimp on spending to improve this data set.  if the latter, then its worth doubling down on probably.

another point: i do worry that $5k is a pittance to the most sophisticated sybil attackers/red team people, who likely make millions of $$$ per year in yield farming operations.  i wonder if we might encourage the red team to cooperate instead of defect in other ways and/or increase the funding for these types of operations (this GCP, but also Upala style campaigns) in the future

-------------------------

Jeremy | 2023-09-15 21:04:49 UTC | #4

Good feedback @owocki.

> i do worry that $5k is a pittance to the most sophisticated sybil attackers/red team people, who likely make millions of $$$ per year in yield farming operations. 

I think it's OK to start small to see what value we can glean and make sure we have the full close loop in place before we ramp up the type of funding we'd put on the attacking side.

-------------------------

antonkulaga | 2023-09-16 20:33:32 UTC | #5

Gitcoin passport is the reason people hate Gitcoin. 3/4 of people who wanted to donate to our projects could not get enough points to donate as you made passport even more restrictive. Also, you agressively push your partners in a way that make users hate you (that is what some people told me). For example, at some point UI did't allow to make donations if the user didn't register brightid, even though often headache with brightid is higher than number of points you can get (unless it was a ui bug and it was not mandatory)Please, find a way to make gitcoin usable again!

-------------------------

umarkhaneth | 2023-09-18 17:38:04 UTC | #6



[quote="antonkulaga, post:5, topic:16525"]
Gitcoin passport is the reason people hate Gitcoin. 3/4 of people who wanted to donate to our projects could not get enough points to donate as you made passport even more restrictive.
[/quote]

3/4 wallets were able to reach a passport score >20 in GG18. There's a tension between making it hard for sybils and easy for humans that's still being explored on a relatively new product. That tension gets better with every round 


[quote="antonkulaga, post:5, topic:16525"]
For example, at some point UI did’t allow to make donations if the user didn’t register brightid,
[/quote]
When was this the case? Do you have any more specific information? 

Passport lets you have your choice of any stamps to verify with as long as you make it over 20. I know I'm not verified with BrightID and I'm well over a 20 passport score + able to make donations.

Your comments here are off-topic. If you wish to continue this convo, please dm me :]

-------------------------

carlosjmelgar | 2023-09-19 05:33:21 UTC | #7

[quote="umarkhaneth, post:1, topic:16525"]
## Benefits

* Insights into how sybil attacks are conducted
* Insights into how to improve our sybil defense
* Possibility to create new partnerships with proven experts

## Drawbacks

* Costs $5k
* Creates pressure to rapidly shore up our defenses after identifying key learnings
[/quote]

Voted yes, but also agree with @owocki on the matching amount. I'd like to see something closer to the minimum for featured rounds to motivate participation. $5K doesn't commensurate with the long term value this brings to Gitcoin.

-------------------------

0xZakk | 2023-09-22 18:12:46 UTC | #8

I'm very in support of this proposal. I think this will lead to a lot of interesting data for the Passport team. 

I'll also add concern that $5k might be too small to attract much attention from "professional" sybil attackers.

-------------------------

umarkhaneth | 2023-10-05 20:41:42 UTC | #9

I'm glad to hear all the support for this proposal and that people think we should actually be spending *more* on this. That's a rare thing to hear! 

In terms of incentive to attack the round, I think $5k will definitely be sufficient for some attackers. It feels like an iterative approach would be best here where we run a small, test round and if we find it valuable then we could scale to larger sums.

-------------------------

M0nkeyFl0wer | 2023-10-17 15:03:37 UTC | #10

Perhaps a bug bounty model would work for this?

I'm generally in favor of this idea. Might be more direct to just offer rewards to those who can help identify specific weaknesses in our processes and tools.

-------------------------

umarkhaneth | 2023-10-17 18:40:32 UTC | #11

This has been posted on [snapshot](https://snapshot.org/#/gitcoindao.eth/proposal/0x54016ff5337de45ee1fe8a36bb9cf332194b37022866610229a34b53e8e6d50f)

-------------------------

Donny_Jerri | 2023-10-22 16:43:40 UTC | #12

I think the Gitcoin passport system is a goldmine.  It is one of the most necessary features in the current environment and will only become more useful in the future.  I am currently working with projects to get them to utilize this asset for themselves and of course this onboards them into Gitcoin ecosystem.  This type of red team/blue team hacker idea is wonderful!  I am concerned the bounty is too small to get the “better” hackers to participate but this is a first iteration.  Let’s see what comes of it.

-------------------------

panpanpan | 2023-11-07 14:26:45 UTC | #13

Sybil defence is never going to be perfect when exchanges can essentially be used as giant mixers to obfuscate connections between addresses. Using on chain analysis on its own will not show this. Perhaps new rules need to be considered to ensure that projects are held accountable to a different standard once they have raised a substantial amount of funding. 

The Gitcoin Passport system is great for mitigating sybil attacks by individuals. As an effective barrier to individual collusion is raised however it shouldn't come as a surprise that other vectors emerge. 'Sybil attack' by individual projects that are collaborating for example. Bundles seem to be underrated as a means for ensuring that associated projects do not absorb more funding than they otherwise might if donors would see the connections between them especially when it comes to matching.

In a sense sybil resistance is meant to provide protection against greed - maybe it's more useful to frame it in this way.

-------------------------

FractalVisions | 2023-11-07 15:24:57 UTC | #14

[quote="panpanpan, post:13, topic:16525"]
Perhaps new rules need to be considered to ensure that projects are held accountable to a different standard once they have raised a substantial amount of funding.
[/quote]

Standards on accountability are beginning to form with [Karma GAP](https://gov.gitcoin.co/t/karma-gap-for-gitcoin-grantees/16936?u=fractalvisions) which is a Grantee Accountability Protocol. I would suggest this to be utilized as a way for future rounds to become curated with projects that have a strong track record for how the funds were allocated from their grant.

-------------------------

umarkhaneth | 2023-11-07 16:39:17 UTC | #15

Thank you to everyone who voted! This proposal [passed on snapshot](https://snapshot.org/#/gitcoindao.eth/proposal/0xc8afbc5dcc6ee94434e5b828ff9c92ce020861a3a6604ed8090cb077d6b919ce) and we will be running the round next month! Stay tuned :robot:

Metrics:
2,695 unique votes
~6.4M GTC tokens cast.

-------------------------
