---
id: 16555
title: "The Path to Allo v2"
slug: the-path-to-allo-v2
category: product
url: https://gov.gitcoin.co/t/the-path-to-allo-v2/16555
created_at: 2023-09-22T20:28:56.959Z
last_posted_at: 2023-09-25T15:27:59.090Z
posts_count: 5
views: 4188
like_count: 12
---

# The Path to Allo v2

<https://gov.gitcoin.co/t/the-path-to-allo-v2/16555>
nategosselin | 2023-09-25 16:00:06 UTC | #1

I’m happy to announce that the submission portion of our Allo v2 audit wrapped this past Wednesday, September 20th. It's the first major stage of our audit and we've been thrilled to see the responses so far. Getting here has been a tremendous effort from the Allo team (@0xZakk @thelostone-mc @jaxcoder@ @0xKurt ), and we’re excited to share a bit more about our path to this moment. This post will refresh on why we pursued Allo v2, share an overview of the protocol and process, and outline what’s coming next for builders.


If you rewind back to March 2022, Gitcoin had just wrapped GR13 and announced our plans for “Grants 2.0”. The decision to begin the move to a decentralized allocation protocol (and away from our centralized platform) was informed by a few key beliefs that we still hold today:
- Public goods funding will best be served by a vast palette of mechanisms, and we need an open design space to iterate on that meta problem
- Every community is different, and they need the freedom and flexibility to fit their capital allocation system to their specific needs
- A system that serves these needs should not have Gitcoin as a gatekeeper, and instead be open and permissionless


The [Grants 2.0 project kicked off](https://gov.gitcoin.co/t/gitcoin-grants-2-0/9981) in summer 2022 and at the same time the DAO published our [updated Essential Intents](https://gov.gitcoin.co/t/update-gitcoindaos-adopted-purpose-and-essential-intents/10984). We embedded our beliefs about the fledgling protocol in the first essential intent: 
> Build a widely adopted, modular Grants protocol that creates a flourishing ecosystem of funding mechanisms. 

By spring 2023, we had sprinted to support the Gitcoin Grants Program by running a set of alpha and beta rounds on the newly-christened Allo Protocol v1. Around this time we also began DevRel efforts to seed adoption. Unfortunately, discussions with our potential integrators surfaced that there were [key technical barriers to adoption](https://gov.gitcoin.co/t/allo-grants-stack-mid-season-update/15278) — especially around developing new allocation mechanisms. Given our intent of building a widely adopted protocol with a flourishing ecosystem of mechanisms, we opted to immediately shift into developing a v2 that could better serve a wider ecosystem of builders. While frustrating, this is [common territory in protocol development](https://x.com/transmissions11/status/1446293172519256064?s=20):

![](upload://sdR4zJtYSpw2PiEYCwn4tCooMcX.png)



To set ourselves up for v2 success we split out a separate protocol team, brought in a protocol expert as a consultant, and allowed ourselves to rethink the architecture from first principles. We essentially locked ourselves in a room and, once we deploy to mainnet in October, will have gone from a blank whiteboard to fully audited protocol in **four months**. This is a huge accomplishment for the team, as [fully-featured protocols often take up to a year of focused development](https://blog.uniswap.org/uniswap-history). What’s more, integration partners who have previewed v2 have been able to develop new mechanisms in a matter of **days**. 


Allo v2 consists of a few key concepts that provide a powerful foundation:
- **Pools** are the atomic unit. Single contracts (as opposed to 3 in v1) that hold funds and the rules for how they will be allocated. 
- **Allo Core** orchestrates the overall protocol. Builders are able to build virtually all of their interactions with this core contract, greatly simplifying their overall integration and surface area. 
- the **Registry** is a repository for profiles, which is every user’s pass for interacting with the protocol. It creates a simple, unique address for each profile, which allows Allo profiles to be compatible both with the world of DeFi and the burgeoning reputation space (SBTs, Hypercerts, EAS, and more).


Over the next few weeks we will be sharing more about Allo v2 and our plans for the future. In the meantime, we want to invite builders to begin playing on the new protocol! You can get involved by:
- Reading up on our [docs](https://docs.allo.gitcoin.co/)
- Joining our Allo Devs Telegram group and our bi-weekly Core Devs call (comment below if you want invites!)
- Building! We’ve begun [curating a list of community build ideas](https://docs.google.com/spreadsheets/d/1VqyyhEcYQUBRmcwbB9Qog81q4S5hSP_Ej14w4ohciqE/edit?usp=sharing) that are ripe for development

-------------------------

annika | 2023-09-22 22:28:44 UTC | #2

Awesome update — super clear rundown, extremely helpful context-wise for those of us who aren't in the day-to-day

(also excellent tweet reference 💯)

-------------------------

owocki | 2023-09-23 12:53:42 UTC | #3

[quote="nategosselin, post:1, topic:16555"]
What’s more, integration partners who have previewed v2 have been able to develop new mechanisms in a matter of **days**.
[/quote]

I think this is for development of smart contracts right?  I'd be interested in finding a way to get to a launch of usable webapps for Allo v2 mechanisms down as close to a matter of days as possible..

The faster we get the OODA loop spinning on the market testing of new mechanisms, the faster (and with more agility) we get to the local/global maximas of what each of these mechanisms can do.
![ooda_480x480|480x407](upload://6YSF6v9kmjyeUeoe8SzkDPoeZVn.webp)

-------------------------

owocki | 2023-09-23 12:56:38 UTC | #4

[quote="nategosselin, post:1, topic:16555"]
* Public goods funding will best be served by a vast palette of mechanisms, and we need an open design space to iterate on that meta problem
[/quote]

i think this post ( https://gov.gitcoin.co/t/systematic-exploration-of-the-coordination-mechanism-design-space/12616 ) is a good overview/refresher on this idea set.

-------------------------

nategosselin | 2023-09-25 15:59:47 UTC | #5

> I think this is for development of smart contracts right? I’d be interested in finding a way to get to a launch of usable webapps for Allo v2 mechanisms down as close to a matter of days as possible…

Yes that's right — and agreed! That's part of where we're trying to dig in now with Octant, Questbook, and Impact Stream. 

We've put together an [initial SDK here](https://github.com/allo-protocol/allo-v2-sdk), but I'm sure there's more functionality we can add.

cc: @0xZakk @thelostone-mc @jaxcoder @0xKurt

-------------------------
