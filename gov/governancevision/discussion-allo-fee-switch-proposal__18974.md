---
id: 18974
title: "[Discussion] Allo Fee Switch Proposal"
slug: discussion-allo-fee-switch-proposal
category: governancevision
url: https://gov.gitcoin.co/t/discussion-allo-fee-switch-proposal/18974
created_at: 2024-06-10T22:27:17.404Z
last_posted_at: 2024-07-24T12:43:01.126Z
posts_count: 8
views: 3448
like_count: 19
---

# [Discussion] Allo Fee Switch Proposal

<https://gov.gitcoin.co/t/discussion-allo-fee-switch-proposal/18974>
James | 2024-06-10 22:27:17 UTC | #1

# Allo Fee Switch Proposal

## Abstract & Background

Fire Eyes DAO has been working towards creating a roadmap for [GTC Value Accrual](https://gov.gitcoin.co/t/gtc-value-accrual-intro/18380)  as well as driving more clear sustainability and value to the GitcoinDAO.

As mentioned in the [GTC Value Accrual Intro](https://gov.gitcoin.co/t/gtc-value-accrual-intro/18380) forum post, introducing a fee switch to the Allo Protocol is a straightforward decision that can allow us to begin this journey.

**This forum post aims to ignite initial discussion on an Allo fee switch, not be a ‘ready to vote’ proposal.**

## Motivation

Allo protocol v2 (and its predecessors) have had $60m+ in combined volume. The introduction of a fee to Allo would create a new revenue stream which would be passed back into the DAO treasury.

Uniswaps previous discussion on the activation of their fee switch provides some guidance around the process involved in making this change, and valuable insight into the wider community response to such a change.

Although Gitcoin is a different protocol to Uniswap, the foundation of these decisions should follow the same logical course. **Protocols cannot sustain being public goods indefinitely and leaning into value accrual as a protocol is important.**

## Specification

This initial pre-proposal discussion centres around two decisions that need to be made before we move forward: 
- Firstly (1.) if the fee is added to Gitcoin’s deployment of Allo protocol **or** (2.) to all deployments of Allo protocol. 
- Secondly if this fee was to be added, what percentage of volume the fee would take.

**Firstly:**

1. The fee switch could added to the Allo Protocol but only be enacted via the official Gitcoin deployment, not at the overall contract level.
    * This allows others to fork the contracts and deploy their own instance without the fee if they wish to.

2. The fee switch could be implemented at the contract level, meaning that all deployments would include the switch unless it was removed from the contract itself.
    * This more strongly encourages anyone using the allo contracts to contribute to the funding of public goods via GitcoinDAO.

**Secondly:** The fee level is an open question - we invite community feedback and discussion but envision the fee sitting at one of the following levels:

- 0.5%
- 1%
- 3%

For context, looking at these fee levels retroactively gives us an idea of how impactful a fee could be over time:

#### GG20:

- 0.5% of total GG20 donations = $3165
- 1% of total GG20 donations = $6330
- 3% of total GG20 donations = $18,990

#### All time:

- 0.5% of total Grants distributions to date = ~$300k
- 1% of total Grants distributions to date = ~$600k
- 3% of total Grants distributions to date = ~$1.8m

These numbers show value flows that could be directed towards sustainability.

**It is important to note that the proceeds of this fee will be deposited back into the Gitcoin DAO treasury,** to be directed into funding both the development of Gitcoin infrastructure, and the commons more broadly. As such, it makes sense for the fee to be higher than average and that most users would be accepting of this given that the fee exists purely to sustain the provision of Allo and related public goods.

*FireEyes would recommend that the switch be implemented at the Allo contract level with a fee of 1%. This is because it provides a clear value proposition to GitcoinDAO’s sustainability whilst remaining reasonably unobtrusive to users donating via the Allo protocol. It is obviously still possible to remove or reduce this fee switch, but this would need to be an explicit decision to exclude by anyone deploying.*

## Drawbacks / Risks

There are reasonable discussion points that this type of fee switch could damage Gitcoin's public goods reputation, here’s how we feel that we could mitigate this if deemed necessary by the community:

- Start with the checkout process having an optional donation/fee to Gitcoin DAO.
- Only enact the fee switch on the official Gitcoin frontend, and let others deploy their own frontends without fee switches.

Allo has established itself as a credible tool for capital allocation, projects with large sums of capital have two incentives to use Allo with a fee switch.

- It has pre-existing infrastructure which is easy to use, making the fee worthwhile.
- Using Allo (with a fee) also means that you are also contributing to public goods inherently by contributing to the sustainability of public goods infrastructure.

## Conclusion

We hope to foster community discussion around both the introduction of this mechanism and its finer details, as well as more broadly around sustainability for the GitcoinDAO and it's infrastructure. 

We realise this is a controversial topic to introduce to a public goods focused community like Gitcoin however starting this conversation is an important step towards ensuring that we can continue sustainably building public goods infrastructure for years to come!

Please share your thoughts and feedback in this forum post 🤖

-------------------------

DistributedDoge | 2024-06-11 00:38:12 UTC | #2

Allo v2 smart-contract suite, as it is deployed, already has a mechanism to extract fee from any *matching pool* (i.e. money submitted by sponsors/round managers) but not from donations.

Taking a quick look at stats in your example taking 3% fee *from round sponsors/managers* is a much better deal than skimming 3% *from donations*, let's take a look at money moved in GG20:

* $1.647M Sponsored matching pools
* $633,431.29 Donations

I think proposal to activate fee switch on donations as well is worth considering, but from pragmatic perspective it might be easier to start by working with functionality that is already deployed. 

The functionality that is already deployed enables two kinds of fees:

- `BaseFee` - round manager pays fixed amount (e.g. 40DAI) to deploy a round.
- `PercentageFee` - when round manager funds matching pool, fixed percentage of that (e.g. 3%) goes to Gitcoin

Both of those fees are currently set to 0 on every major chain I checked, but DAO is able to change them if willing to do so.

To the best of my knowledge, there is currently no mechanism to be selective with fees. If fee starts being enforced on protocol-level, it means every round (on a given chain) created within Allo V2 would need to pay such fee. 

You can look at Allo contract code to see how this works under the hood:

https://optimistic.etherscan.io/address/0xB087535DB0df98fC4327136e897A5985E5Cfbd66#code

**My personal conclusions:**

- I think having a small fee that is enforced on protocol level is a good idea!
- Since functionality for collecting fees on matching pools already exists, I would be in favour of asking DAO to activate existing `PercentageFee` switch at `1%` or similar (could be done on single chain to test the idea first?). 
- Gitcoin has no realistic way to enforce what happens inside third-party deployments of Allo Protocol but I pretty much agree with your recomendations at the end of *Specification* section.

-------------------------

owocki | 2024-06-11 15:18:12 UTC | #3

@Sov i'd be curious if you think that adding a Fee Switch would create an impediment to adoption, and if so what you make of that feedback. 

I'm also curious to hear if alternatives to fee switches (optional but default donations in checkout flow, having Gitcoin in each round as a project to fund, perhaps token staking schemes) would be more viable in your opinion.

-------------------------

Sov | 2024-06-11 16:29:06 UTC | #4

Projects could be amenable to this, but (as with everything), the devil would be in the details (how much, when applied, etc.).  

I'm sure I am biased, but I think the ecosystem being built on Allo could justify a fee switch both in the current app stack and what is sure to come.  With this, Gitcoin would need to make what is being built much more accessible to any network where Allo is deployed.

-------------------------

jengajojo | 2024-06-12 11:23:08 UTC | #5

Thanks for initiating this discussion @James I generally support sustainable development of protocols and the conversation around the fee switch. However, I'd like us to consider the consequences of switching it on too early! There is always a risk that the protocol doesn't have sufficient lindy yet and a competitor with 0 fees or even negative fees (backed by investors) can take huge chunks of marketshare if implemented too early. A deep analysis of the competitor landscape should be conducted before switching on fees imo. 

On the other hand, there maybe some benefits to selectively charging fees. Eg:

**Case A:** Fees are inversely proportional to a minimum donation threshold and 0 fees above that threshold. This can incentivize wallets to donate minimum amounts.

**Case B:** Fees are inversely proportional to amount of GTC staked and 0 fees if the stake is above this threshold

-------------------------

kyle | 2024-07-03 18:08:50 UTC | #6

Hey @James - Thanks for this. FWIW, I think turning on a fee switch for the protocol is not great at our current stage. ie, we are still too small to turn on a fee switch, it will deter adoption and create more problems for us... I had one idea that may be worth exploring though. It offers value for us and for our ecosystem as a whole:

I wonder if we could create an attestation for contributions to grants rounds as part of the checkout flow? Here are a few details - As part of the checkout flow, you mint an attestation (on the checkout network). This attestation details the contribution, expected match, and round details, etc. Ideally it includes information that only we would know (expected match amount, etc.), and then serves as an onchain proof for all contributors.

We start to build an attestation network (via the Gitcoin Grants EAS schema) that can be used for any number of things (reputation, airdrops, etc.) But then you also capture $1 per attestation, or $2 per attestation. We can turn Gitcoin into one of the largest attestors of funding sources and the projects that receive that funding. Ideally we deploy a smart contract to each network (like Passport has done) that enables easy, on chain querying of info. There by enabling gating on contributions, etc. I can share more details on this if this isn't well understood.

Gitcoin is often asked "who contributed to XXX round or YYY project" - now users have incentive to mint the attestation as they might be included in airdrops that target this info in the future AND because its onchain, we can look up details on who is minting, versus who isnt, etc.

This attestation (and the revenue to Gitcoin) is on the donor, optional, and has value to them as a credibility builder (or airdrop farmer). This also can serve as a proof to issue a hypercert in the future (or the contributions themselves to the project's wallet).

At 400k transactions per grants round, let's say 80% do it.. Gitcoin is making nearly $300k - $600k a round, collected in Eth. These attestations also provide more value to the ecosystem (and L2s). which means we can drive more grant funding from OP and others for providing interesting and valuable attestation data on chain (ie, filling block space).

Would love thoughts. I think the level of effort is fairly small given the knowledge, contracts and attestations Passport has done too.

-------------------------

umarkhaneth | 2024-07-18 21:54:07 UTC | #7

Hey, just wanted to quickly add some data on the amount Gitcoin stands to make per round. These are some numbers on unique_checkouts over the last ~2 years of Gitcoin Grants. 

If we look at ~50k average unique checkouts at 80% participation and $2 per attestation then an average GG could bring in close to $80k. In the bull case if we get back to ~100k unique checkouts per GG then this could be ~$160k per round.
Over one year of running four similar rounds, we could see around $320k-$640k annual recurring revenue.

![Screen Shot 2024-07-18 at 5.47.09 PM|398x500](upload://QOGNikuRI6yMkp1VTol99fByJz.png)

-------------------------

kyle | 2024-07-24 12:43:01 UTC | #8

Thanks, Umar - this is really helpful. We could play with the mint fee as well (2-4?) to determine if there is a trend in which we see less attestation minting based on fee amount.

One item of note. I would enable this for all rounds run on the platform, not just our GG rounds. These attestations become public goods, and a strong funding signal for communities to leverage. As something that is totally optional, turning it on for all community & ecosystem rounds seems low downside.

-------------------------
