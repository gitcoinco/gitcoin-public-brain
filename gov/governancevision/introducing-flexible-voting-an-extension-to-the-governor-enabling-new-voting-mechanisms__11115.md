---
id: 11115
title: "Introducing Flexible Voting: An extension to the Governor enabling new voting mechanisms"
slug: introducing-flexible-voting-an-extension-to-the-governor-enabling-new-voting-mechanisms
category: governancevision
url: https://gov.gitcoin.co/t/introducing-flexible-voting-an-extension-to-the-governor-enabling-new-voting-mechanisms/11115
created_at: 2022-07-14T17:25:12.783Z
last_posted_at: 2022-07-27T13:06:37.685Z
posts_count: 6
views: 3945
like_count: 8
---

# Introducing Flexible Voting: An extension to the Governor enabling new voting mechanisms

<https://gov.gitcoin.co/t/introducing-flexible-voting-an-extension-to-the-governor-enabling-new-voting-mechanisms/11115>
bendi | 2022-07-28 16:01:04 UTC | #1

### Intro

The purpose of this post is to introduce Flexible Voting and begin the discussion about its adoption by the Gitcoin DAO. Flexible Voting is an extension to the Governor contract. It allows for the construction of new mechanisms which make governance participation easier, cheaper, and more accessible for GTC holders.

Flexible Voting was developed by [ScopeLift](https://scopelift.co) as part of our grant from the [Uniswap Grants Program](https://twitter.com/uniswapgrants). Before explaining more about Flexible Voting, let me introduce ScopeLift for anyone whose not familiar with us.

### About ScopeLift

ScopeLift is a dev shop focused on crypto. We're a small technical team with many years of EVM engineering experience. We've had the pleasure of working with many great clients including Uniswap, Optimism, Cozy, Endaoment, POAP, and others.

ScopeLift is a long time friend friend of Gitcoin. W've had the privilege of contributing to Gitcoin in various ways over the last few years, including helping to build the cart based checkout experience, the bulk checkout smart contract, the BrightID integration, the integration with zkSync, and the first iteration of dGrants.

We're also the team behind [Umbra](https://app.umbra.cash/), a stealth address system developed with grant funding from the EF, MolochDAO, and of course Gitcoin :)

ScopeLift received a UGP grant earlier this year to work on Governance related projects. One of those projects is Flexible Voting, which is the subject of this post.

### About Flexible Voting

Flexible Voting is an extension to the Governor contracts that enables delegates to split their voting weight across For, Against, and Abstain on any given proposal. This capability is especially useful when a contract serves as the delegate.

By enabling arbitrary contract logic to roll up the voting weight of disparate parties into a single delegated vote, many possibilities are unlocked. Having a contract act as the delegate also means these mechanisms can be implemented without introducing new trust assumptions.

The inspiration for Flexible Voting came from cUNI (Compound UNI). When a UNI holder deposits their tokens into Compound, they lose the ability to participate in Governance. [Attempts](https://www.comp.xyz/t/setup-community-cuni-voting/440) to mitigate this required trust and were [gameable](https://www.comp.xyz/t/setup-community-cuni-voting/440/8). Any holder of GTC who wants to deploy their tokens in DeFi would experience the same issue.

Flexible Governance fixes this problem. A deposit contract like Compound can delegate its voting weight to another “voting” contract. That contract in turn can implement its own set of rules enabling DeFi depositors to vote on proposals.

![flex-voting-diagram|690x388](upload://t7GK8vdM1ieF2z0DR5VgjJPZbCt.png)

### Other Use Cases

In addition to allowing token holders to vote while their GTC is active in DeFi, Flexible Voting enables many more use cases, such as:

* Voting on L2 with bridged tokens

* Shielded voting (i.e. secret/private voting)

* Cheaper subsidized signature based voting

* Easier voting with tokens held by custodians

**For a much more in-depth introduction to Flexible Voting, how we built it, and what it enables, check out post on the [ScopeLift blog](https://www.scopelift.co/blog/introducing-flexible-voting).**

### Next Steps

Flexible Voting is implemented as an extension to the OpenZeppelin Governor contract. It is [open source](https://github.com/ScopeLift/flexible-voting). Adopting it would require a carefully crafted governance proposal to be submitted and voted on. Since the DAO is [actively considering](https://gov.gitcoin.co/t/upgrading-the-gitcoin-governance-contracts/10721) an upgrade to the OpenZeppelin Governor, now would be the perfect opportunity to adopt Flexible Voting, and ScopeLift is committed to helping should the DAO choose to do this.

We'd love to hear your feedback. If you're a member of the community and you'd like to help us move Flexible Voting forward for Gitcoin, please get in touch.

For our part, we're working to expand the system's capability by implementing some of the concrete use cases which Flexible Voting makes possible. We're working to see Flexible Voting, which is backwards compatible with existing Governor tooling, directly and fully supported. We're also proposing Flexible Voting to other DAOs, including Uniswap, which funded its initial development.

If you’d like to help us build it, fund it, or get it adopted by another community you’re a part of, reach out!

-------------------------

GTChase | 2022-07-15 14:07:51 UTC | #2

this is a really important problem space, one that raises itself here at Gitcoin.  its awesome to see Scopelift introducing a solution to the problem. 

I have a quick question as i consume this material a bit deeper.. Is the flexible voting extension available for OpenZepplin's governor alpha, bravo or just a select one?

-------------------------

bendi | 2022-07-15 21:43:59 UTC | #3

Hey @GTChase, good question! Flexible Voting is implemented as an extension to the OpenZeppelin Governor. The OZ Governor itself is Bravo compatible, but very modular in design. A given DAO, when creating/deploying the contract that will be their Governor, can choose to inherit from different extensions to get different features, including various levels of Bravo compatibility. It's a bit hard to explain without getting into the details of the code but the basic answer is that OZ Governor is Bravo compatible with lots of room for customization.

-------------------------

kyle | 2022-07-25 18:11:08 UTC | #4

[quote="bendi, post:1, topic:11115"]
Flexible Voting is implemented as an extension to the OpenZeppelin Governor contract. It is [open source](https://github.com/ScopeLift/flexible-voting). Adopting it would require a carefully crafted governance proposal to be submitted and voted on.
[/quote]

I would love to learn more! thanks for posting this @bendi.

Is Uniswap also considering an upgrade off of the Governor Bravo? I may be mistaken but I didnt think the Comp/Uni style Governor Bravo was the same as the Open Zepplin contracts. Am I off base there?

-------------------------

bendi | 2022-07-27 02:45:09 UTC | #5

Hey Kyle, good questions! It's hard to say what "Uniswap" as a DAO is "considering", but the short answer is that the UGP folks who pushed for this grant are definitely interested in seeing this upgrade, and we're doing our part to try to mobilize the community around an upgrade. So, yes! They're considering it as much as a whole DAO can consider anything :slight_smile: 

This down-in-the-weeds code stuff can be a bit hard to explain, and I'm oversimplifying a bit with this explanation, but the quick TL;DR is that OZ's Governor works like Bravo's out of the box, and our extension is written in a backwards compatible way— meaning it adds features without breaking the existing ones.

Here's a slightly longer explanation:

The OpenZeppelin Governor is basically a modular rewrite of Governor Bravo. Out of the box, it is compatible with Bravo, and is used by many DAO's these days, such as ENS, as one prominent example.

Because it's written in a modular manner, it allows for the developers deploying the DAO contracts to customize it by extending or writing extensions. This means if you want, you can definitely modify the OZ Governor to break that Bravo Compatibility to differing degrees, depending on how you choose to customize it.

Our extension is written to be backwards compatible with Bravo-style Governors. This means contract integrations or DAO tools made to work with Bravo should work out of the box with it, but it *also* enables the new fractional style voting that gives flexible voting all of its flexibility.

Let me know if this explanation isn't clear or if you have further questions!

-------------------------

kyle | 2022-07-27 13:06:37 UTC | #6

[quote="bendi, post:5, topic:11115"]
Because it’s written in a modular manner, it allows for the developers deploying the DAO contracts to customize it by extending or writing extensions. This means if you want, you can definitely modify the OZ Governor to break that Bravo Compatibility to differing degrees, depending on how you choose to customize it.

Our extension is written to be backwards compatible with Bravo-style Governors. This means contract integrations or DAO tools made to work with Bravo should work out of the box with it, but it *also* enables the new fractional style voting that gives flexible voting all of its flexibility.
[/quote]

This is super slick.
![Screen Shot 2022-07-27 at 9.05.28 AM|690x432](upload://mfXAtQFUQ543V38ZspVz9xAatUC.jpeg)

What is usually involved in upgrading the contractor? As I understand it, there is the need for a vote, to replace the governor contract (which means we also need to deploy the new contract). Once deployed, can it be upgraded without having to deploy a new smart contract (ie, change the contract address?)

-------------------------
