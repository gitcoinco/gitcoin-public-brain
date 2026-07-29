---
id: 12511
title: "Using Kleros in the appeals and dispute resolution of the Gitcoin Grants Protocol"
slug: using-kleros-in-the-appeals-and-dispute-resolution-of-the-gitcoin-grants-protocol
category: gitcoin-grants
url: https://gov.gitcoin.co/t/using-kleros-in-the-appeals-and-dispute-resolution-of-the-gitcoin-grants-protocol/12511
created_at: 2023-01-06T15:42:59.867Z
last_posted_at: 2023-02-13T20:00:56.834Z
posts_count: 10
views: 3785
like_count: 16
---

# Using Kleros in the appeals and dispute resolution of the Gitcoin Grants Protocol

<https://gov.gitcoin.co/t/using-kleros-in-the-appeals-and-dispute-resolution-of-the-gitcoin-grants-protocol/12511>
gmkung | 2023-01-06 16:09:41 UTC | #1

As Gitcoin moves ahead with the Grants Protocol this month, I'd like to propose a solution for the decentralization of the dispute and appeal resolution processes (which are now primarily carried out by the FDD). 

Kleros has served as a reliable [independent judiciary](https://blog.kleros.io/independent-judiciaries-for-sovereign-daos/) for DAOs and decentralized communities since 2017, serving more than a [hundred different projects](https://kleros.world/), including Uniswap, 1Inch,  Ledger, Gnosis, Galxe, Lens Protocol and Panther Protocol.

Managing grant approval, dispute and appeals is a highly subjective process that is challenging to decentralize, and finding a robust solution for it is therefore ever more pertinent. I'm proposing to have [Kleros Court](https://kleros.io/) serve as one of the (primary) options for the decentralized handling of disputes and appeals. 
In this setup, the FDD will serve as the legislators and custodians of the process, curating and managing the ruleset that will be used by the Kleros jury to arbitrate on each dispute. This presents not only a credibly neutral dispute resolution solution for Gitcoin's community, but also greatly increases the scalability of the operations of the protocol by leveraging the wisdom of a crowd-sourced jury.

I welcome feedback from the community and the FDD on this proposal before diving into more details for a potential integration.

-------------------------

ludoviko.poh | 2023-01-06 19:59:10 UTC | #2

Hi, I am was a lurker of gitcoin forums but this post made me sign up for the forum to write a reply. 
I do not have much time to give an exhaustive reply at the moment, but I will write one in the relative near future. 
In my opinion, which I think it is shared with some others in the space, Kleros would be the worst Organization to hand over the dispute resolution. Their principle of decentralized justice is perfect in its design, but in reality the protocol is highly concentrated and the conflict resolutions are biased towards whales in their system, some of the whales directly associated with one of the founders (proof upon request, cannot post URLs now) to protect their interests. 

In Proof of Humanity, a DAO that I am a member and a highly-voted author, we are struggling with Kleros and its tactics since the beginning, just to obtain a minimum degree of autonomy and sovereignty. We are in the process of splitting the DAO precisely due to this conflict. 

Handing this power to Kleros would be handling the power to a limited amount of actors. I would research the PNK token distribution, and the governance manipulation tactics they have done in PoH before moving any further.

-------------------------

gmkung | 2023-01-07 05:21:36 UTC | #3

Thank you for showing interest in this thread, Luis.

I think the points you raised are very important in the selection process for a dispute resolution system, especially for a project as important as Gitcoin.

The mechanism design of Kleros Court follows the principles of [Credible Neutrality mentioned by Vitalik](https://nakamoto.com/credible-neutrality/), in which "just by looking at the mechanism’s design, it is easy to see that the mechanism does not discriminate for or against any specific people". This is a point that has been largely acknowledged thus far in this thread.

To address a side topic so we hopefully concentrate on the topic at hand: Kleros have been stalwarts of decentralization since the beginning and [Proof of Humanity DAO was designed by Kleros](https://blog.kleros.io/proof-of-humanity-building-the-internet-of-humans/) with a one-person-one-vote voting system. The decision to separate the Kleros tokens (the PNK) from the PoH DAO governance was conscious and intentional.

Regarding the fork in PoH DAO: Kleros acknowledged the presence of differing and irreconcilable opinions in the community and actually initiated [the peaceful fork](https://snapshot.org/#/poh.eth/proposal/0xe23fa2fc78fe95c9b904e6197eb88135dff859956f4474d13f5c622ec2188da5), a move that would have been unnecessary if Kleros Cooperative indeed had dominance over the DAO.

With that aside, I'd like to ask for comments from other members of the Gitcoin community to discuss this proposal for the next step in Gitcoin's progressive decentralization.

-------------------------

kevin.olsen | 2023-01-07 16:03:39 UTC | #4

I'm not super deep on this topic, but @owocki was a big proponent of forking Kleros to run on GTC and having that as the arbitration mechanism for the protocol. I believe the concerns that @ludoviko.poh raises were the driver for this recommendation.

Curious what folks think of this direction...

-------------------------

gmkung | 2023-01-07 16:28:06 UTC | #5

Hi @kevin.olsen on this topic, the usage of a DAO's own token for arbitration in a Kleros-style court is intuitive, but can be problematic as it tends to interfere with the original tokenomics of the DAO's token (e.g. GTC). 

One situation in which this can become problematic is when the DAO's token is used for other activities such as staking or voting in other parts of the DAO. As Kleros-style courts require jurors' tokens to be immobilised in the court they choose to stake in, these tokens become unavailable in other activities of the DAO. 
Likewise, if it is desirable to have large components of the DAO's token be directed towards voting/staking in DAO governance, they become unavailable to secure the arbitration Court.

A purpose-specific token (i.e. meant only for arbitration) is therefore desirable, and the most efficient way to build the value and community around such a token and court system is if it is used for as many dApps and projects as possible (i.e. not project specific), allowing the community expertise, experience and token liquidity to be pooled together.

-------------------------

griff | 2023-01-07 18:00:59 UTC | #6

Which chains is Kleros on? How easy is it to resolve disputes on a less popular EVM chain, like Celo, for instance?

-------------------------

gmkung | 2023-01-07 18:21:24 UTC | #7

Kleros is on Ethereum and Gnosis chain at the moment, but we will be announcing the roadmap for bridging to other EVM chains in the near future. 

Kleros can theoretically solve disputes in any environment or chain (even off-chain ones like [this one in Mexico](https://blog.kleros.io/how-to-enforce-blockchain-dispute-resolution-in-court-the-kleros-case-in-mexico/)), though trustless enforcement of rulings will require either the grant payout contracts to be on the same chain as Kleros Court, or on a chain where Kleros Court has a bridge to.

-------------------------

ludoviko.poh | 2023-01-07 19:07:26 UTC | #8

[quote="gmkung, post:3, topic:12511"]
The mechanism design of Kleros Court follows the principles of Credible Neutrality mentioned by Vitalik, in which “just by looking at the mechanism’s design, it is easy to see that the mechanism does not discriminate for or against any specific people”. This is a point that has been largely acknowledged thus far in this thread.
[/quote]

Again, things that are on paper are nice, but in practice the facade of ideal mechanisms falls pretty rapidly. Vitalik himself questioned how is it possible that credible neutrality and I quote him directly from his blog post "DAOs are not corporations", where he speaks directly about Kleros:

> Whether through a more widely distributed token supply, or through more use of non-token-driven governance, a more credibly decentralized form of governance could help Kleros avoid such concerns entirely.

I beg to differ, then, that Kleros represent a credible neutralty.

[quote="gmkung, post:3, topic:12511"]
To address a side topic so we hopefully concentrate on the topic at hand: Kleros have been stalwarts of decentralization since the beginning and Proof of Humanity DAO was designed by Kleros with a one-person-one-vote voting system. The decision to separate the Kleros tokens (the PNK) from the PoH DAO governance was conscious and intentional.
[/quote]

Kleros designed PoH so that it never becomes an independent DAO, and has used dirty tactics to attack whoever tries to reach some level of DAO sovereignty, so I am very doubtful of that claim. Kleros exploited peoples' innocence during the registry mechanism so that it bloated it's base dispute numbers, which up to the creation of PoH was failing to reach some credible amount.  
In terms of decentralization, Clement Lesaege campaigned to remove the Proof of Humanity's Mission Board, hours after he was removed due to an accumulations of dictatorial behaviour, such as hacking the one-person-one-vote mechanism by mass recruiting vulnerable people in Myanmar, creating his own Hermit Kingdom of people that pre-delegated their vote to him, without letting them know of the alternatives (proof on request). 

These are the sort of anti-values that Kleros represents: the opposite of everything Gitcoin tries to build on web3. It would be a huge mistake to cede a critical aspect of GTC.

-------------------------

kevin.olsen | 2023-01-08 15:38:17 UTC | #9

Thank you for sharing. I'd heard there was drama but hadn't been able to learn more about this yet.

What alternatives would you recommend we look at for dispute-resolution systems as we investigate this space?

-------------------------

M0nkeyFl0wer | 2023-02-15 21:07:20 UTC | #10

Would love to dig into this discussion more with along Shawn and allies. 

This is such an important part of the DAO space and all of our work and there are a lot of options and lessons learned from the digital democracy space in general. 

Full disclosure I'm a fan of multi attribute decision making and tools focused on fairness tied to roles as opposed to models that strictly attribute more voting power to those with more tokens (or staked tokens). 

Cheers

-------------------------
