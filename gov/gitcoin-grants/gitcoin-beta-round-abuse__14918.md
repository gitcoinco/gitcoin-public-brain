---
id: 14918
title: "Gitcoin Beta Round Abuse"
slug: gitcoin-beta-round-abuse
category: gitcoin-grants
url: https://gov.gitcoin.co/t/gitcoin-beta-round-abuse/14918
created_at: 2023-05-10T02:30:38.814Z
last_posted_at: 2023-05-11T12:54:08.685Z
posts_count: 4
views: 1680
like_count: 3
---

# Gitcoin Beta Round Abuse

<https://gov.gitcoin.co/t/gitcoin-beta-round-abuse/14918>
inplco | 2023-05-10 02:30:38 UTC | #1

Hi,

We saw that the funds donated during the Gitcoin Beta round are sent straight to the wallet address specified during contract deployment. What's stopping a few bad actors with Gitcoin passports from cycling the donations through a CEX and re-donating to themselves to maximise the matching pool? For example,

Donate $10 → Receive $10 → Cycle through a CEX → Donate the same $10 again → Rinse & Repeat

Is this possible?

-------------------------

bobjiang | 2023-05-10 11:51:11 UTC | #2

Hi @inplco 

It is **absolutely** forbidden action for funding (donating) to their own project. This is a sybil action, and would be identified and marked by anti-sybil check.

For more info, would like to invite gitcoin team to introduce.

-------------------------

inplco | 2023-05-11 11:55:27 UTC | #5

Hi, 

Can someone elaborate on what these anti-Sybil measures are? In particular, how can they catch the following scenario:

> Donate $10 → Receive $10 → Cycle through a CEX → Donate the same $10 again → Rinse & Repeat

Last I checked, anyone can donate multiple times to a project and there is no way to associate transactions across CEXs. For example, if I like a project a lot, I can donate 1000$ from my passport address to it, ask the team to send the 1000$ that they just received to a CEX (to my exchange address of course), send it from the CEX back to my passport address, donate the same 1000$ again. Repeat. Perhaps I wouldn't want to raise suspicion and only do it a few times. But a team can have access to multiple passport accounts and this can have an exaggerated effect.

-------------------------

Supreme | 2023-05-11 12:54:08 UTC | #6

I have also been trying to figure out what these antisybil measures are. I am unable to see any and I have found many instances throughout this last grant round.

-------------------------
