---
id: 11678
title: "FDD: some security & privacy issues in a protocol based grants system"
slug: fdd-some-security-privacy-issues-in-a-protocol-based-grants-system
category: open-discussion
url: https://gov.gitcoin.co/t/fdd-some-security-privacy-issues-in-a-protocol-based-grants-system/11678
created_at: 2022-10-18T15:09:10.517Z
last_posted_at: 2022-10-19T06:57:40.756Z
posts_count: 2
views: 2613
like_count: 7
---

# FDD: some security & privacy issues in a protocol based grants system

<https://gov.gitcoin.co/t/fdd-some-security-privacy-issues-in-a-protocol-based-grants-system/11678>
j-cook | 2022-10-18 15:09:10 UTC | #1

***this post is intended to summarize the discussions around privacy and security happenming in fdd, and to stimulate further discussion among the wider community***

Gitcoin currently reviews grants and defends against Sybils using a small set of highly trusted reviewers and analysts. However, Gitcoin is undergoing a process of decentralization that relies upon developing composable protocols that can be tuned and deployed by individual grant owners. Instead of being a centralized grant funding platform, Gitcoin will be a funding factory, doing R&D and manufacturing of grant management tools. The aim of this is to empower individual communities to take control of their own grant rounds and configure them to their own needs.

While this decentralized approach has the potential to level up the public goods funding landscape through real community ownership, it is not risk free. It is difficult to open a protocol to honest users without also opening it to adversaries. This post outlines some of the risks decentralization and composability introduce into Sybil defense and grant reviewing, how they are mitigated and what opportunities remain.


## What keeps grant owners honest?

Composable, configurable protocols give individual grant owners the power to tune their security to their needs. For example, a grant owner might decide the standard grant eligibility requirements are not fit for purpose for their grant - they have the freedom to amend them to something more fitting. Similarly, they might identify a particular vulnerability in their community to a certain type of Sybil (maybe some subcommunity finds a way to farm certain stamps, for example) and chooses to tune their Sybil defenses to down-regulate those stamps. This flexibility offers great strength because individual grants can defend their specific vulnerabilities rather than relying on generic defenses in a way that is not possible for a centralized system.

On the other hand, what happens if a grant owner chooses to deliberately weaken their own defenses, or is manipulated into doing so?

It is not hard to imagine a scenario where a grant owner is bribed, blackmailed, threatened or otherwise manipulated into allowing Sybil attacks that favour certain projects. There are many versions of this issue - the minimal example being legitimate projects applying some social pressure or subtle social engineering to gain some small edge through tuning the Sybil defenses or grant review configuration. The maximal example is an outright scam project pressuring a grant owner to tune down their defenses sufficiently to enable a pre-prepared Sybil attack that enriches some person or group who then walk away with the funds. Perhaps some certain combination of easily farmable stamps, known to attackers in advance, is given a "free-pass" to non-Sybil status. In effect, migrating to a composable protocol adds some risk in that now not only can adversaries devise new ways to circumvent the rules of the platform, the configuration of the rules themselves becomes a viable attack vector.

The plausible defenses against this include whistleblower rewards or "whitehat" bounty that rewards ethical hacks that are honestly disclosed. Alternatively, some form of heirarchical oversight or retroactive slashing system that requires users to collaterize their good behaviour with something of value (perhaps staked $GTC). The "slashed" funds could be used to reward the whistleblowers. Round manager are very important in this context. Round managers determine eligibility conditions, matching amounts, quadratic funding calculation details, trust scoring weightings etc to provide a configuration that is common across all grants in the round. The grant owners then have tools to fine-tune their security and monitor other grants in their round.

It seems like a combination of all of these might be necessary to strongly disincentivize dishonest behaviour. Perhaps some incentivized inter-grant reviewing could lead to crowd-sourced assurance that security meets some threshold, but it is hard to see how to defend against cartels forming that recycle incentives into payments to mutually turn blind eyes. Whistleblower rewards could be a powerful way to protect against grant-owner dishonesty, but only if the grant owner has something tangible to lose when the whistle is blown on them, and there is no inadvertent incentive to whistleblow on honest actors.

The transition to protocol-based grant-giving brings to mind [Kerckoff's principle](https://www.crypto-it.net/eng/theory/kerckhoffs.html) that a system should be secure even under the assumption that adversaries have complete knowledge of how it works and its dependencies. In an open-source environment this is a hard requirement as everyone has access to the source code and protocol rules by default. To satisfy this, the protocol must be secured without using secrets or private interactions between trusted individuals, but instead be secure because resilience emerges as a natural consequence of the way the protocol is designed. A composable system might come with security benefits in that each component should be a self-contained package that can be unit tested, pen-tested etc to identify vulnerabilities and fix them quickly. It could be that communities form around each component and domain experts emerge for each composable unit, and continuous testing could be a crowd-sourced effort (maybe even supported by gitcoin grants). On the other hand, integration and system testing can be very difficult because complete coverage of all the various configurations and combinations of composable units is probably out of reach. There are also social factors and vulnerabilities that are hard to test for such as perverse incentives that are not baked into the protocol but emerge from real-world usage, maybe even using apps and social structures emerging on top of the protocol.


## Privacy

The model of Sybil defense that is being built for the new composable grant system relies upon users creating a Gitcoin Passport in which stamps are collected and used as evidence of personhood. The idea is that these stamps are sufficiently costly in terms of time, effort and/or money that they are difficult to collect dishonestly and at scale. At the same time, a retrospective machine learning model aims to identify Sybils from their observed behaviours.

Anonymity is difficult to preserve in a system designed to look for evidence of personhood, because it is difficult to distinguish that an individual is a human without also revealing that they are a specific human. Proof of personhood is akin to evidence of uniqueness, and uniqueness is antithetical to anonymity. There is a risk that participation in a Gitcoin grant round could provide a portal into the personhood attached to a specific address. In the original Grants 1.0 system Gitcoin collected user's email addresses, Github usernames and ip addresses along with their Ethereum address in order to identify Sybil's. That data could reveal a lot of information about an individual, including their approximate physical location and the projects they had contributed to. In Grants 2.0 this data will no longer be needed because it is replaced by Gitcoin Passport stamps - a more provate way to participate in Gitcoin grant rounds.

At the moment, there are a limited set of credentials that can become Gitcoin Passport stamps (Google, Facebook, BrightID, ENS, Proof-of-Humanity) meaning many users will share the same combination of stamps. This mitigates any doxxing risk. However, when individual communities are able to define their own authenticators the number of potential stamps and therefore their potential possible combinations could explode, creating a scenario where it is possible to "fingerprint" a wallet by its unique combination of credentials. The risk is then that an adversary could track an individuals "participation history" along with the financial history that comes for free on the blockchain. There may be tricky balances to strike between specificity of stamp combinations and privacy, since a tightly defined, specific set of credentials would enable high fidelity community curation but potentially also have a negative externality in the form of fingerprinting.

Passports with stamps are actually just DIDs (Decentralized Identifiers) mapped to a specific wallet address and they are set to expire after a fixed time. The DiDs do not contain any personally identifying informtion whle they exist - they are just an attestation that some truested issuer has observed a connection between an address and some credential of interest. When they expire, the stamp ceases to exist and leaves no trace that could connect the address to the stamp. This means an individual can present their honest credentials to the world when they need to but not have them become indelible tattoos that reveal their past activities to the world. Making passports ephemeral mitigates the problem of unwanted digital footprints.


## Personhood <> Projecthood

One way to refactor the protocol in favour of security and privacy is to make projects, rather than grants, a fundamental unit of account. It would be expected that projects request multiple grants and they accrue a legacy of honest activity that benefits them in successive rounds. Project owners are incentivized to act honestly, defend robustly against Sybils, make effective and efficient use of composable grant reviewing tools and build a genuine user base because these factors can influence their reputation. The projecthood score, in turn, lowers the bar of proof required for successive funding because evidence of trustability accrues over time. The concepts developed for individual proof-of-personhood (i.e. stamps associated with an address) can be adapted for proof-of-projecthood. This promotes decentralized quality control for grants and might help stimulate a transition to a more composable, protocol based Gitcoin. It might also address some of the problems discussed earlier related to gameable incentives for grant owners - by making them project owners that accrue reputation and consequently more frictionless access to follow-on funds promotes integrity over the long term. This could be how project owners are incentivized to tune up their own Sybil defenses and review stringency. However, proof-of-projecthood is no silver bullet - there are vulnerabilities that adversaries could feasibly exploit. One example is generating copycat projects - fake projects mirroring the activities of honest projects in order to gather sufficient credentials to successfully attack in some future round. Defining the projecthood criteria might fall into the remit of a round manager.


## Attack surface

The transition to a decentralized, protocol-based grant system undoubtedly increases the system complexity and as a result expands the attack surface in ways that might be hard to detect in advance. We already mentioned the potential for composable Sybil defense and grant review configurations to be a new attack vector. There is also the risk of accidentally creating perverse incentives, especially if ideas such as $GTC staking are progressed further. It is hard to be precise about these kinds of risks in advance, especially when the protocol design is not finalized, but one could imagine a system where it might benefit adversaries to act honestly for multiple rounds until they cross some threshold of trust before launching an attack that is then much harder to defend, or perhaps investing in the trustability of individuals until they become grant owners, at which point they can game the protocol's composability in favour of a certain outcome. The more complex the system becomes the harder it is to anticipate edge cases and close all the possible exploits. It is harder, for a more complex system, to see in advance what unintended consequences might arise. This is especially true for Gitcoin because this is untrodden ground with few analogs to learn from.

The defense against this is basically to do lots of conceptual and numerical modelling in advance to be as well informed as possible, and have a strong social layer backing up the protocol. The counter-argument, of course, is that although new attack vectors may be exposed by the transition from platform to protocol, it is all in the service of closing a critical one: the centralized control over funding distribution that Gitcoin currently relies on.


## Unknown unknowns

There is a finite set of vulnerabilties and scenarios that can feasibly be identified and wargamed in advance. Like any software there will be unforeseen issues and potentially zero-day exploits that only come to light once the product is in the wild. In order to safely transition from centralized to decentralized public goods funding there should be an incremental wilding of the protocol that hands control over the protocol to the community incrementally - for example, it might be prudent to maintain some degree of centralized control over the source code for the composable tools until they have been deployed and demonstrated to be running well, in case a rapid response to a bug or exploit is required.

## Summary/outlook

The transition to Grants 2.0 - a composable, protocol for community ownersip of Gitcoin grants - is a huge opportunity to level up public goods funding in web3. However, this large upgrade brings with it a new set of attack vectors and privacy concerns that must be mitigated. Overall, increased security and privacy are the likely outcomes from the transition thanks to the removal of data from the protocol through the integration of Gitcoin Passport.

-------------------------

castall | 2022-10-19 06:57:40 UTC | #2

[quote="j-cook, post:1, topic:11678"]
What keeps grant owners honest?
[/quote]

I think the burden of sybil mitigation falls on the grant round creators, not the grant creators.

As a decentralized grant round creator, I'll start with the assumption that all recipients in my grant round are potential sybil attackers. I shouldn't rely on them to decide what sybil protection is appropriate for their grant. A grant may welcome or even create a sybil attack--it means more matching for them. It's my job as a round creator to exclude grants that are encouraging or creating sybil attacks, and stop sybil attacks on grants that are not complicit.

[quote="j-cook, post:1, topic:11678"]
it is difficult to distinguish that an individual is a human without also revealing that they are a specific human. Proof of personhood is akin to evidence of uniqueness, and uniqueness is antithetical to anonymity.
[/quote]

For BrightID's part, having a stamp in the passport reveals nothing except that the bearer is one of the many verified BrightID users. Google and Facebook can't do this, because although you could create a zero knowledge proof of set membership, Google and Facebook don't enforce uniqueness.

BrightID lives by the idea that to be verified as a unique human, you shouldn't have to reveal anything to anyone that doesn't already know it.  There is a way to leverage people's knowledge about phone numbers, addresses, twitter handles, email addresses, and other semi-private information without ever revealing it to someone who doesn't already know it, and especially without linking it to an app account (like a Gitcoin account or an eth address).

https://forum.brightid.org/t/fighting-small-scale-sybil-attacks-with-known-identifiers/503

By the way, Aura is now working (https://aura.brightid.org), and we're preparing to open the beta. Very briefly, to be verified by Aura, you have to find someone who is an Aura player that knows you, connect to them on BrightID and they will do the rest. (Or if that isn't possible yet, you can become an Aura player and connect to other Aura players.)

I think the idea that people should reveal personal data in order to be verified as unique stems from a history of the government being the trusted entity to keep track of people. It did this originally for taxes, then benefits, then drafts, and so-called national security. Because the government agent doesn't know you, you must share info with strangers. We have the technology now that we don't have to do this anymore.

I believe in the ability of grant round creators to set appropriate standards for the projects and donors they're hoping to attract that may include anonymous proof of membership in certain organizations.  For example, you may believe that GitcoinDAO isn't filled with scammers and bots, so that is one stamp you consider. When setting these, let's remember that OR generally makes the anonymity set larger, and AND generally makes it smaller.  So you can say GitcoinDAO OR BrightDAO OR GivethDAO OR, etc. without narrowing down who the holder is.  I want BrightID to be a useful AND in passport proofs because it's a very large set--our goal is that everyone should be able to get one--and it reveals nothing other than a stamp of uniqueness.

-------------------------
