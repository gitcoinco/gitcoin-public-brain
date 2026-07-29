---
id: 18658
title: "Cross-chain donation widget for Twitter by IDriss"
slug: cross-chain-donation-widget-for-twitter-by-idriss
category: open-discussion
url: https://gov.gitcoin.co/t/cross-chain-donation-widget-for-twitter-by-idriss/18658
created_at: 2024-04-23T14:26:27.996Z
last_posted_at: 2024-05-06T12:49:47.855Z
posts_count: 5
views: 3210
like_count: 22
---

# Cross-chain donation widget for Twitter by IDriss

<https://gov.gitcoin.co/t/cross-chain-donation-widget-for-twitter-by-idriss/18658>
geoist | 2024-04-23 18:09:40 UTC | #1

## TLDR

- IDriss is back with the Twitter donation widget for GG20, now enabling **cross-chain** donations.
- Donate from 6 major EVM chains in seconds, with a bridge fee as low as $0.05.
- We've proposed a technical solution to the Gitcoin team for including these donations in the matching calculations with minimal effort and no changes to the Allo protocol.

This post aims to document our work, share context with the broader community, and possibly spark a conversation about the composability of the Allo protocol with regard to matching donations made via frontends built by external dev teams.

## Context

During the Gitcoin GG18 round, we've [onboarded](https://twitter.com/IDriss_xyz/status/1692567346886455507)  grantees to receive donations via our browser extension for Twitter. A total of 377 unique donors made impressive 1,186 donations to 155 grantees. Take a look at the [Twitter love board](https://idriss.xyz/gg18) with reactions from grantees and [Dune dashboard](https://dune.com/idriss/pg-donations)  with stats.

![Donation widget for GG18](upload://nUlYwl22s2HqLUWiSAtabslyuZs.jpeg)



During ETHDenver 2024, we developed a prototype that expands the functionality of the donation widget and enables cross-chain Gitcoin donations, receiving [the first prize from the Across Protocol team](https://twitter.com/AcrossProtocol/status/1765054760577556589). Over the past two months, we've been focused on incorporating the prototype into the live product for GG20.

## Cross-chain widget for GG20

Today, we're happy to share that the cross-chain component powered by [Across Protocol](https://across.to/) is live, together with the the start of GG20. Watch the demo below, or check out the [announcement thread](https://twitter.com/IDriss_xyz/status/1782779173196701708).

https://www.youtube.com/watch?v=RKo4-tp5aE0

Specification:
- We support donations in ETH on 6 major EVM chains: Arbitrum, Base, Ethereum, Linea, Optimism, zkSync Era.
- The test round in the demo above is deployed on Optimism, so what you're seeing is an Arbitrum to Optimism cross-chain donation.
- The $0.24 you see on the demo is a fee necessary to perform the bridging operation. This fee varies, and it's often as low as $0.05. You can find more information about the bridge fees in the [Across Protocol's documentation](https://docs.across.to/reference/fees-in-the-system#relayer-fees).
- We didn't have to compromise on speed; it's comparable to regular transfers. Across has consistently maintained its reputation as the fastest and lowest-cost bridge for end-users. Their recent milestone of [crossing $7B in all-time volume](https://twitter.com/AcrossProtocol/status/1778770155218370694) attests to its reliability.
- We set a minimum donation amount of $1. This ensures that bridging relayers can process transactions smoothly, without significantly limiting donors (usually $1 was the minimum amount eligible for matching).
- If for any reason the bridge transaction cannot be processed (e.g. donation is sent just before the round end), the donor receives back their funds after 6 hours.

All the code is open-source and can be verified here: [browser extension](https://github.com/idriss-crypto/browser-extensions), [smart contract](https://github.com/idriss-crypto/contracts/blob/DonationWrapper/src/contracts/DonationWrapper.sol).  No user funds are stored, and there are no token approvals. The contract code has undergone a sanity check by an independent smart contract developer.

## Matching

The question that naturally comes to mind is: will these donations be matched?

Unlike the same-chain donations we built for GG18, where all the donations fell into the Gitcoin indexer pipeline and were therefore automatically included for matching and showed up in the history page, the cross-chain donation component required us to introduce a wrapper smart contract, consequently obfuscating the original donor.

We've developed and proposed a non-invasive solution for including these donations in the matching calculations with minimal effort and no changes to the Allo protocol. Donations made through our extension issue onchain attestations via the [Ethereum Attestation Service](https://twitter.com/eas_eth). These attestations are issued in a decentralized manner, making them immune to spoofing or alteration. You can read the complete technical explanation of the solution [here](https://github.com/idriss-crypto/browser-extensions/blob/master/CONTRACTS.md).

Knowing about the plans to make Allo the ultimate composable funding allocation protocol, we think this is something worth solving not only for GG20 but also for any future dev teams building independent frontends.

## About Us

For those of you who don't know us yet, you can follow our work on the channels listed below.

[Gitcoin Grant](https://www.idriss.xyz/gitcoin)  - [Website](https://www.idriss.xyz/)  -  [Twitter](https://twitter.com/IDriss_xyz)  -  [Farcaster](https://warpcast.com/idriss)  -  [Discord](https://discord.gg/RJhJKamjw5)  -  [Mirror Blog](https://idriss.mirror.xyz/)  -  [Docs](https://docs.idriss.xyz/)  -  [GitHub](https://github.com/idriss-crypto)

Feedback and ideas are very welcome. Tagging relevant folks for visibility: @meglister @sov @umarkhaneth @owocki @kyle @jeremy @carlosjmelgar @thedevanshmehta.

-------------------------

carlosjmelgar | 2024-04-23 14:48:42 UTC | #2

IDriss always brings rizz to Gitcoin Grants. You truly are public greats. I love that this pragmatic approach front runs the superchain, orbit and agg layer visions. 

Already looking forward to the GG21 alpha. 

If there's ever a plan to incubate Gitcoin ecosystem projects and help them GTM through the DAOs network, this is a great candidate.

-------------------------

Sov | 2024-04-23 22:00:20 UTC | #3

Amazing work, as always.  Appreciate the continued dedication to building!

-------------------------

thedevanshmehta | 2024-05-06 11:13:57 UTC | #4

Great to see this tool built! I see it as an important innovation for chain abstraction in general. It's also heartening to see the IDriss team respond to the [call](https://twitter.com/owocki/status/1727353788787261452) put out by @owocki after GG19 for having something exactly like this built out.

As Gitcoin has doubled down on Arbitrum as the chain to run GG20 on, we probably won't see much uptake in this round. I would like to hear from the team on whether it can be absorbed natively into the Gitcoin grants stack so that we can auction off round hosting to the highest sponsoring chain without having it affect the UX for donors.

-------------------------

ccerv1 | 2024-05-06 12:49:47 UTC | #5

I'd love to see a pilot of this, eg, for a community round that is less OSS focused. I this this is a cool experiment, although I am also nervous of things that could further amp up the "popularity contest" aspect of GG. (This is not a reason against, just something to be mindful of.)

-------------------------
