---
id: 12267
title: "Bringing Gitcoin Passport On-Chain [Request for Feedback]"
slug: bringing-gitcoin-passport-on-chain-request-for-feedback
category: open-discussion
url: https://gov.gitcoin.co/t/bringing-gitcoin-passport-on-chain-request-for-feedback/12267
created_at: 2022-12-08T17:57:08.697Z
last_posted_at: 2022-12-08T18:48:38.537Z
posts_count: 2
views: 2780
like_count: 14
---

# Bringing Gitcoin Passport On-Chain [Request for Feedback]

<https://gov.gitcoin.co/t/bringing-gitcoin-passport-on-chain-request-for-feedback/12267>
erich | 2022-12-08 19:52:37 UTC | #1

The Gitcoin Passport team is kicking off collaborative product research to make Passport more composable with blockchain applications. A critical benefit of blockchain-based identity solutions over an off-chain approach (like the current Passport architecture with the Ceramic Network) is more native composability with blockchain-native applications, also known as smart contracts.

Blockchain-native composability of identity certificates and smart contracts may enable apps that execute as programmed and protect Passport holder privacy and coercion and censorship resistance. Unfortunately, off-chain identity solutions (including Gitcoin Passport 🥲) cannot cohesively satisfy these goals because they heavily rely on trusted intermediaries to feed the identity data into the apps.

Through an internal hackathon, the Passport team has prototyped [different](https://github.com/gitcoinco/passport/issues/617#issuecomment-1285668189) [implementations](https://github.com/gitcoinco/passport/issues/618#issuecomment-1290046517) in these and adjacent directions. The outcome we are looking to achieve through our research is to more deeply understand the community’s needs to inform how we architect an on-chain Passport.

Areas the team is trying to gain a deeper understanding:
* The problems that can be solved by a blockchain-based Passport
* Importance of privacy-preserving capabilities (e.g., zero-knowledge proofs, designated verifier proofs) of on-chain Passports;
* Partner preferences around specific networks (Optimism, Ethereum, Arbitrum, and more)

Are you a Passport holder, (potential) integration partner, or Gitcoin community member interested in this work and want to guide our research? Then we'd love to hear your thoughts on this. Indeed, we’d encourage you to provide contextual feedback exclusively via 👉 **[Pol.is](https://pol.is/8fyrkbujac)** 👈 so we can get a more meaningful insight into the community sentiment. Feel free to post procedural / bureaucratic questions in this thread.


Sincerely,
@GTChase and Erich

PS: Here's the **[Pol.is](https://pol.is/8fyrkbujac)** link again.

-------------------------

owocki | 2022-12-08 18:48:38 UTC | #2

[quote="erich, post:1, topic:12267"]
Are you a Passport holder, (potential) integration partner, or Gitcoin community member interested in this work and want to guide our research?
[/quote]

hi from supermodular.xyz - we are considering building things on top of passport.  here is our 002 wei:

i would like to have a set of smart contract functions that allow me interact with the personhood scores of various identities

# modifier onlyPersonhoodScoreAbove(uint 256 above_score)

a smart contract modifier

```
modifier onlyPersonhoodScoreAbove(uint 256 above_score)
```

that only allows ppl with a personhood score above `above_score` to call a function and a second modifier:

# modifier onlyNtimes(uint 256 n_times, uint256 nonce)

```
modifier onlyNtimes(uint 256 n_times, uint256 nonce)
```

that allows a function to be called only `n_times` by a unique person for each `nonce` . (`n_times` will usually just be 1, eg 1 person 1 vote) it would also be useful to have a function:

# function getPersonhoodScore(address addr) returns uint 256

```
function getPersonhoodScore(address addr) returns uint 256
```

where i can pull the personhood score of a specific address. 

# summary / a comment on the level of abstraction i care about

youll note that exactly 0 of these functions care about which verifiable credentials an address has used. to me as a customer of this smart contract, i dont care about at all, the VCs are just an implementation detail. i just want them abstracted away by someone who has done the work to figure out how to translate them into a scare + i want to know who is a unique human + who is not. i trust passport + the scoring algorithm i've chosen to take care of the details.

my 002 wei as someone whos building above the protocol.

-------------------------
