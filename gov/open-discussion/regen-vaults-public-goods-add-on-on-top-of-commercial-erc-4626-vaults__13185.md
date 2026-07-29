---
id: 13185
title: "Regen Vaults - Public Goods add-on on top of commercial ERC-4626 vaults"
slug: regen-vaults-public-goods-add-on-on-top-of-commercial-erc-4626-vaults
category: open-discussion
url: https://gov.gitcoin.co/t/regen-vaults-public-goods-add-on-on-top-of-commercial-erc-4626-vaults/13185
created_at: 2023-03-06T10:49:40.554Z
last_posted_at: 2023-03-09T15:03:59.619Z
posts_count: 6
views: 4602
like_count: 18
---

# Regen Vaults - Public Goods add-on on top of commercial ERC-4626 vaults

<https://gov.gitcoin.co/t/regen-vaults-public-goods-add-on-on-top-of-commercial-erc-4626-vaults/13185>
Kaimi | 2023-03-06 10:49:40 UTC | #1

# Summary

Regen Vaults' core idea is a Public Goods *add-on* on top of commercial ERC-4626 vaults. 
> Regen Vaults are a multi-tranche portolios configured with:
> 	1 or 2 **senior tranches donating interest**/partial interest to "Gitcoin Grants matching pool address" 

> and being protected by single **commercial tranche** 
> 	serving as first-loss capital, using senior tranching capital to leverage yield. 

Commercial Lenders are incentivised to invest into vaults that already have donating capital(APY boost). Donating capital is incentivised to lend into Senior Tranches because it is being offered additional protection.

On absence of donators willing to lend to senior tranches vaults behave like classic unitranche pool and still should make economical sense. 


# Abstract

"Regen Vaults" allow lenders to earn interest on their deposits while supporting public goods through one of two strategies: "donation of interest" or "protection of  donating capital".

Idea builds on top of [TrueFi protocol](https://docs.truefi.io/faq/truefi-protocol/for-developers/structured-credit-vaults) maintained by [Wallfacer]("https://wallfacer.io/"): all mechanics for implementation of this idea already is possible within the protocol and had been thoroughly audited by Chainsecurity  [(Report)](https://chainsecurity.com/security-audit/truefi-carbon/)

# Specification

-   A Regen Vault is a pool of funds that are lent out to a selected asset manager to invest in accordance with a predefined strategy.
- It is structured to allow for different exposure to risk and yield. 
- It is not strictly a Public Goods Funding only product but rather it is a composition of commercial and public incentives in one on-chain product. 

## Regen Vault Trust Model

Let's start with simplest possible usecase assuming only two-tranches setup which is useful for visualising the trust model:

![Screenshot 2023-03-06 at 17.25.50|436x500](upload://d7ka0j6U6916nKxyiIvZ7Nhzu7W.jpeg)



Some implications:

* all lending happens on-chain, control of liqudity for Asset Managers happens on-chain, waterfall and senior-to-subordinate rations are being enforced on-chain
* Asset Manager can disburse the funds - only to a certain Legal Custodian Address.
* From there funds are being deployed into RWA through the brokerage account
* Asset Manager signs with Lenders an MLA where Asset Manager commits to certain strategy - like only T-Bills through Community Bank's brokerage account 
* Managers are approved via TrueFi Protocol proposals, with their corresponding Custodian Ethereum Address that had been confirmed. 
* Managers are responsible for providing correct valuations and attesting for it. It can be verified by external parties.
* Manager cannot use any other address for disbursment of the capital. Only legally recognized custodians are allowed
* Manager has to have legal structures verified, traction and reputation to be approved by TrueFi DAO. Currently TrueFI is working with 3 potential Asset Managers.

## Tranching Mechanics Explanation
In another example:
-   The pool is divided into three tranches: 
	- Interest Donation Tranche, 
	- Partial Interest Donation Tranche
	- Commercial Tranche.

![Screenshot 2023-03-06 at 17.18.09|690x343](upload://uaO80SQnB1EPBvSI4osCnfMbdC1.png)


In the particular example:
-   The Interest Donation Tranche is a 3% yield tranche where lenders donate their funds to support public goods quadratic funding via interest earning. Full 3% is being donated.
-   The Partial Interest Donation Tranche is a 8% yield tranche where half of the interest earned is allocated to public goods quadratic funding and the other half is distributed to the lender.
-   The Commercial Tranche is an uncapped yield tranche where lenders can earn high returns with smaller contribution on a field of public goods: protecting "donating capital" 
- Commercial Tranche is a "liquidity engine" that allows PM to scale the vault - since this capital is locked till the end of Vault's maturity. Worst case scenario, if there is no demand on upper tranches - than the vault is an "UniTranche opportunity". If anyone though, is ready to "donate" some part of the yield, or all of the yield - they can choose upper tranches being additionally protected from Asset Manager mistakes:
	- Interest Donation Tranche capital is protected by Partial Donation Tranche and Commercial Tranche
	- Partial Donation Tranche is protected by Commercial Tranche

> TL;DR
> Upper / Donating Tranches get protection, 
> Commercial Tranche get higher APY on some additional risk.

## Funds Management

-   The Asset Credit Vault is managed by a selected asset manager* who will invest the funds according to a predefined strategy, signing Master Loan Agreement with lenders on deposit. 
-   Funds will be off-ramped only to a legal/confirmed custodian address and exchanged for fiat, then sent to the asset manager's brokerage account to invest in accordance with the predefined strategy.
-   At the end of the investment period, the funds are returned to the vault to be redistributed to the lenders.

#### Scenario Simulation

-   Let's assume each tranche has raised $1M each with a final vault performance of 6%, resulting in a final value of $3.18M (180k)
-   Interest Donation Tranche: $1M deposited with *0%* yield for LPs, 3% going to "public goods address": __$30k__
-   Partial Interest Donation Tranche: $1M deposited for 8% in total, half being *4%* - yield allocated to both Vault LPs and public goods, resulting in a __$40k__ contribution to public goods and a __$40k__ yield to the LP.
-   Commercial Tranche: $1M deposited for *7%* total final yield, resulting in a $70k return, __leveraging "on public goods financing__


## Motivation
Thought behind this idea is to find sort of symbiosis between yield seeking capital and public goods capital. Is it worth pursuing in your opinion? This post is an ask for feedback.

### Benefits of Regen Vaults

-  Overall in the above example, the Asset Credit Vault achieved a **7% yield donated to public goods**: matching funds - __$70k__ in total.
- **"Donating" capital is being prioritized** and getting some first loss guarantees
- "Fully Donating" capital might be offered liquidity windows. 
- Donators are presented with two levels of engagement into public goods founding, *donating all interest* or *splitting APY* between donation and earning. 
- for first loss capital, APY/risk ratio proposition can be very attractive if Public Goods Tranches are full.

-------------------------

kyle | 2023-03-06 18:10:45 UTC | #2

[quote="Kaimi, post:1, topic:13185"]
Is it worth pursuing in your opinion? This post is an ask for feedback.
[/quote]

I love the idea of continuing to find sustainable funding for our matching pool. I am not in expert in the vault management or strategy you proposed, and so I find it a bit harder to abstract the true value.

Do you have pool established somewhere to put this into context for me?

-------------------------

tylerw | 2023-03-07 00:58:03 UTC | #3

This specific product is new. The ERC-4626 credit vault contracts were deployed on TrueFi last month. @Kaimi and I are bringing this idea here because we believe Gitcoin could help us experiment and build impactful applications for this infrastructure. 

**More on the product:**
I've created a live demo of the described vault [here](https://app.truefi.io/structured-credit-portfolio/optimism-goerli/0x693d29e072021cf88f2a8149dc771853cf00a39c) on Optimism Goerli testnet. Additionally, you can watch a video walkthrough of this product [here](https://docs.truefi.io/faq/truefi-protocol/for-developers/structured-credit-vaults).

The TrueFi protocol has facilitated >$1.7bn in on-chain credit to crypto institutions and "real world asset" (RWA) borrowers since 2020.

**Ideas on potential applications:**
Inspired by recent ideas in [[GCP-001] - PASSED - Funding IndexCoop gtcETH offering](https://gov.gitcoin.co/t/gcp-001-passed-funding-indexcoop-gtceth-offering/13013) and [Proposal: Carbon-Neutral Policy at Gitcoin](https://gov.gitcoin.co/t/proposal-carbon-neutral-policy-at-gitcoin/10823/32?u=tylerw#vibes-3), Gitcoin could participate in this type of vault to help bring together on-chain financing of climate impact projects.

The structure could help attract both profit-oriented and public goods-oriented lenders, where (i) public goods lenders receive protection against credit defaults in return for donating a portion of interest generated to the Gitcoin matching pool, and (ii) profit-oriented lenders receive more upside through leveraged returns.

If there is interest in this type of pursuing these types of experiments, we would like work with TrueFi to bring together asset originators and lenders to make this possible.

-------------------------

Kaimi | 2023-03-07 16:09:21 UTC | #4

@kyle thanks for the quick reply. as Tyler mentioned:

> If there is interest in this type of pursuing these types of experiments, we would like to work with TrueFi to bring together asset originators and lenders to make this possible.

Structured Vaults is the newest TrueFi protocol that had been developed, deployed and audited. On the 'bizdev" side, we are in conversations with 4 asset managers at this point, but as you know, the environment for "onchain lending" got substantially worse during last couple of months so it is not an easy feat to get something up and running, but we're getting there :slight_smile: 

I am personally a big fan of Gitcoin (since the very beginning) so part of my 'product brain' was always looking for a solution to find a way to marry "commercial/yield seeking capital" with "public goods funding". 

Could you advise how do we get more feedback / more confirmations on this idea? Things that we might do after full initial validation:

* look for Asset Manager willing to add optional donating tranches to their vaults
* build customised controllers to support interest donation
* build support for Regen Vaults on the UI side of TrueFI
* design and configure first Regen Vault (e.g. "Treasury Bills Vault with Climate Impact Tranche")

Potentially, this is a sort of product that could be developed w/o a need for deep integration and heavy  coordination work on the Gitcoin side - funds would just flow into the "matching pool address" / split /etc.

-------------------------

divine-comedian | 2023-03-08 20:46:00 UTC | #5

Hey! I wanted to chime in here that I **love** this idea! I actually spend most of my time buidling for Giveth and we've been speccing out a product for the last few months that is extremely similar. 

I won't spend too much time shilling Giveth on Gitcoin's forum but if you're not familiar with us, [we are a donation platform and can be found here](https://giveth.io).  We started work on **GIVfi** around December 2022 which will encompass two products - **GIVsavings** and **GIVdaoments** - the former being focused on project owners while the latter focused on donors. 

### A short TL;DR

**GIVsavings** - will allow owners of for-good projects to earn a yield on their idle donations - effectively giving them a "savings account" and be able to autodeposit incoming donations into this account and deposit any other eligible types of funds they hold. 

**GIVdaoments** - very similar to what you outline above, big ticket donors can create an endowment, allowing them to invest capital into a vault and donate the yield to one or many different for-good project simultaneously. Other donors can join an existing GIVdaoment or launch their own with unique distribution settings. 

----

I also noticed the great work @kyle has done [getting gtcETH out the door](https://gov.gitcoin.co/t/gcp-001-passed-funding-indexcoop-gtceth-offering/13013) and have had the opportunity to meet the crew at FundPG who were some ETH Denver '23 hackathon finalists (winners?) building also a very similar product. Not to mention the work [Spirals](https://www.spirals.so/) on CELO has been up to for a while now... 


It seems like the ReFi world is all starting to coalesce around the idea of supporting public goods directly with DeFi yield. I wonder if there's a way we can collaborate to make a single amazing product rather than many competing ones. 

Happy to chat more on our ideas here and can provide more context on Giveth and GIVfi.

-------------------------

LucianoDeAngelo | 2023-03-09 15:03:59 UTC | #6

Hey all, funny enough we just launched a similar product at ETHDenver and won the hackathon!  FundPG allows individuals to allocate a percentage of their yield to funding public goods via the Gitcoin Matching Pool. 

Feel free to send me over any information to my Telegram @ LucianoDeAngelo. I would like to learn more about these structure credit vaults on Truefi and the current activity + vision. @Kaimi @tylerw

-------------------------
