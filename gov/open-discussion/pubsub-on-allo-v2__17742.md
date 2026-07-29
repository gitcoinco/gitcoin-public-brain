---
id: 17742
title: "PubSub On Allo V2"
slug: pubsub-on-allo-v2
category: open-discussion
url: https://gov.gitcoin.co/t/pubsub-on-allo-v2/17742
created_at: 2024-02-12T19:02:20.029Z
last_posted_at: 2024-08-13T18:52:01.145Z
posts_count: 3
views: 3656
like_count: 4
---

# PubSub On Allo V2

<https://gov.gitcoin.co/t/pubsub-on-allo-v2/17742>
owocki | 2024-02-12 19:07:26 UTC | #1

Thanks to @jaxcoder for the feedback on this idea.

# Tldr

This document proposes building pubsub (publish subscribe) into Allo protocol V2 in Q1/Q2 2024.

Pub/Sub is short for Publish/Subscribe. PubSub is a standard way of thinking about data models on the web, having been used for many open source projects [as a design pattern pattern](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern).

Pub/Sub in the context of Allo protocol means being able to publish Allo grants to other registries. And subscribe from other registries.

Pub/Sub would be of great strategic importance to Gitcoin. Implementing Pub/Sub in H1 2024 would enhance Gitcoin’s network effects greatly by allowing Allo Protocol to be used on every Grant Platform in the ecosystem. It would also make Gitcoin’s Builder tool into a very valuable tool for every Grant hunter in the ecosystem. and could work to further solidify Allo as THE library for capital allocation in web3.

# Essential intent

![|211x259](upload://eNcgbf393Lev39HMnnsYstHJD1s.jpeg)

# Problem

## 1. Lack of Adoption of Allo Registry

Right now, there are several prominent Grants standards created by Gitcoin (5% market share by 2023 ETH public goods funding GMV) Optimism (90% market share) Giveth (2%) CLRFund (1%), Hypercerts (1%) and more (1%).

Allo v1 tried to standardize them on Allo, but that didn’t work.

It’s almost like there is a pattern to how standards proliferate.

![|624x356](upload://4d5kNwyKXu2D9rgGbj4zOSp84Qx.jpeg)

## 2. Cold start problem

Network effects of these tools are reflexible. The more people use the Allo registry, the more people use the Allo registry, the more people use the Allo registry, and so on…

Tools that are trying to boostrap network effects have what we call the [cold start problem](https://www.nfx.com/post/19-marketplace-tactics-for-overcoming-the-chicken-or-egg-problem).

If we were still the top market leader in EVM based grants, we could bootstrap it with our dominance. But after the rise of Protocol Guild + Optimism Retro PGF, we are not the dominant market leader anymore.

![|299x271](upload://qNMh5SvMIVtRBNWPnDQMYyH7aHh.png)

We need to solve this cold start problem.

# Solution

Owocki/Jaxcoder propose the following solution: Pub/Sub For Allo v2.

High level this would be two things

1. **Publish**: The ability to publish your Gitcoin Grant to any major registry.
2. **Subscribe**: the ability to subscribe to any grants registry and import it into Allo.

## Subscribe

We could effectively solve Gitcoin’s cold start problem by importing other registries into Allo v2.

![|624x255](upload://uTigZdZQlBeDQoQ2zOUzuV1kBXZ.png)

Once this has hit scale, there is much more value in building things on top of Allo v2 (reputation, impact attestations, etc..) because all grants in the ecosystem are on the same registry.

## Publish

In college applications in the United States, students can fill out a “common app”. One college application that allows them to apply to hundreds of schools.

This is a killer app for college applicants who want to make multiple bets + have their time respected while doing so.

We should build a “common app for web3 grants” that allows grant owners to build / manage their grant in one place, then publish it to other registries.

![|624x312](upload://72KrgHp0WV2QwdiHuJ6A3HXZk1k.png)


# Conclusion

Implementing Pub/Sub into Allo protocol would enhance Gitcoin’s network effects greatly by allowing Allo Protocol to be used on every Grant Platform in the ecosystem. It would also make Gitcoin’s Builder tool into a must-use tool for every Grant hunter in the ecosystem. It would solidify Allo as THE library for capital allocation.

# Appendix A - Implementation Details

Thanks @jaxcoder for authoring this part of the post.

### Implementation

Subscribers typically receive only a subset of the total messages published. There are two common forms of filtering: topic-based and content-based. I think we could also add a third and possibly a fourth, or more, filter method.

We could start out with simple pub/sub options.

1.  Add a IRegistryWrapper interface - this will allow the user/developer to use the wrapper instead of the IRegistry (the wrapper will inherit this) which will contain the EAS functions.
2.  Add a RegistryManager contract - this will allow the user/developer to subscribe to any registry within the protocol and allo registries to publish ‘profiles’ and any other relevant information.

Current Problems:

* Cross-chain registry synchronization
* Wrapping each other registry “profile” into IRegistry for consumption
   * How do we define the interface(s)?
* EAS uses a registry specifically for attestations, to me this means we will still need a layer on top of EAS to map the UID (this is returned when an attestation is made) to a profileId (this profileId can exist on any registry that the RegistryManager has subscribed to and may even be called something different).
* Registries leveraging other registry data.

Solution(s):

* Use a [hybrid](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern#:~:text=In%20a%20topic,or%20more%20topics.) pub/sub system where the user's profile publishes the attestations via the registry or registries they subscribe to using the registry manager.
* To allow for a mapping from a profileId to a UID we need a contract layer to handle this and the other features we want to build out for managing multiple registries in one place.
* The user can then start to include many features provided by other registries within Allo by using the IRegistryWrapper interface. This will include all functions previously offered by the Allo IRegistry interface plus additional plug-and-play features that a user can turn on and off. One of the key features will be the PubSub model of providing profile and registry data.
* A flag that can be used to include EAS by default.
* [Diagram](https://excalidraw.com/#room=0c9d1eb62ff432c4aebc,O-QrXh4xoGYU1LkYrACt-g) currently representing the idea of having a RegistryManager and IRegistryWrapper interface.

-------------------------

owocki | 2024-07-15 12:45:04 UTC | #2

Had a good discussion with @launaumau about this idea at ethcc and posting some notes here

1. Is friction of submitting grants a feature or a bug?  I think that this brief considers it a bug.. but there are lots of grants managers who want more friction to weed out bad applicants.

2. How do fields translate across registries?  Sometimes this will be obvious but in others it will not be obvious.

-------------------------

skilesare | 2024-08-13 18:52:01 UTC | #3

Hello,

We've decided to make this the focus of our GG21 raise for ICDevs.  

https://explorer.gitcoin.co/?utm_source=grants.gitcoin.co&utm_medium=internal_link&utm_campaign=gg19&utm_content=community-rounds#/round/42161/385/35

The general idea is to use the Internet Computer as a trustless router that can sync data across chains. Bonus points if we can make it governable via an existing staking mechanism via GTC.

We'll likely need a few resources to dial it in. Any suggestions or insight would be welcome.

The largest challenge will be funding the gas fees to relay the messages, but perhaps that is raisable via grants themselves once it is up and running.

-------------------------
