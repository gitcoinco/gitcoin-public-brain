---
id: 20378
title: "[GITCOIN 3.0] Signals Protocol for sensemaking"
slug: gitcoin-3-0-signals-protocol-for-sensemaking
category: open-discussion
url: https://gov.gitcoin.co/t/gitcoin-3-0-signals-protocol-for-sensemaking/20378
created_at: 2025-05-08T14:39:16.086Z
last_posted_at: 2025-06-10T23:37:39.418Z
posts_count: 3
views: 1525
like_count: 7
---

# [GITCOIN 3.0] Signals Protocol for sensemaking

<https://gov.gitcoin.co/t/gitcoin-3-0-signals-protocol-for-sensemaking/20378>
jkm.eth | 2025-05-09 18:21:06 UTC | #1

Hi everyone, this is James from the Lighthouse team.

@owocki recently presented his vision for Gitcoin 3.0, where he discussed sensemaking and mechanisms for capital allocation. We have been working on a new onchain protocol for surfacing community sentiment, which we think could be a good solution for the sensemaking piece of the puzzle.

## Background

We first started building the Signals protocol during the Arbitrum x RnDAO collabtech hackathon, where our MVP won first place. We continued iterating on it during the Uniswap Hooks Incubator, in which we won top prizes from Arbitrum and Uniswap Foundation.

We were inspired to design this protocol having experienced **the difficulty of exposing honest opinions and priorities from DAO members**. As they say, “talk is cheap,” and we believe onchain indications of sentiment with an economic model attached is much more powerful than forum posts or upvotes.

## How it works

Our protocol allows community members to post initiatives that they think are important, and then other participants can lock up their **existing governance tokens** in support of the initiatives they agree with. Locking tokens for a longer period of time gives greater support, at the cost of having those tokens unavailable for longer. In many situations users may be forced to make a choice between which initiatives to support, which further increases the value of the signal as it is no longer feasible to support everything.

Support for initiatives algorithmically decays over time, which keeps the indicators timely. Initiatives that have the most support rise to the top of the dashboard, creating **a realtime view of what matters most** to DAO participants.

Once an initiative reaches a preconfigured threshold of support, it can be “actioned” by the DAO, in which case **all the locked tokens are immediately returned to their owners** and the initiative can be considered an official priority. Unpopular initiatives will also have their tokens unlocked, eventually, but the length of lockups means participants are further encouraged to only support initiatives they truly believe in.

We have also implemented some additional features which I won’t get into now:

* An incentives mechanism, to reward those who participate in supporting an initiative
* Lockups issued as NFTs, enabling a secondary market for locked support
* Additional criteria for submitting initiatives or actioning them (e.g. requiring endorsement from pre-vetted delegates, etc)

## Current state

Our MVP is live, complete with factory deployments and web app dashboard. We are currently looking for funding to improve the contracts, do a full audit, and run a pilot program to validate and refine the model. Everything is open source.

Signals github: https://github.com/0xLighthouse/signals

Live demo: https://signals.capstone.lighthouse.cx/

## About us

I (**jkm.eth**) have been in crypto for 13 years, having previously worked at Coinbase, Kraken, and C-level at Breadwallet (acquired by Coinbase).

My cofounder Arnold (**1a35e1.eth**) has been in the technology development space for 15 years, having built and scaled multiple enterprise products and teams.

## The ask

We think Signals could be the perfect tool for sensemaking. It doesn’t cost anything for users to participate (other than their tokens being unavailable for a time), and in fact they could even earn rewards for participating.

We want to know what you think about this idea and how it could be useful to Gitcoin!

-------------------------

owocki | 2025-06-08 13:45:30 UTC | #2

@jkm.eth hi -  we just launched some [basic gitcoin 3.0 timeline](https://gov.gitcoin.co/t/gitcoin-3-0-the-road-to-gg24/20723) on the gov forum . one detail that may be important:  we are standardizing all partnership evaluations in one place/process, mind filling out this form for signals protocol?  https://docs.google.com/forms/d/e/1FAIpQLSdjl1Jzm-FP875G5tXaWSQTktrsC36xsdWJQwSlyS4Wo3ecSA/viewform

-------------------------

jkm.eth | 2025-06-10 23:37:39 UTC | #3

Thanks for the ping. We've submitted the form.

As a quick update on Signals, we've published a short-but-sweet overview of how it works: https://mirror.xyz/lighthousegov.eth/yOY3vgiiE5HfPbUNLSbYUpjICDA3SrcJkQVEjTPiQR4

We've also put out a follow-up article about mechanisms we've designed to incentivize participation:  https://mirror.xyz/lighthousegov.eth/mEZhb9Nwav_ZpwrvOAKCxzmJFbsez-jow9t2b4mjc2k

-------------------------
