---
id: 19698
title: "[PASSED - SGTM 002] Avantgarde x Gitcoin: Strategic Asset Management for the Matching Pool"
slug: passed-sgtm-002-avantgarde-x-gitcoin-strategic-asset-management-for-the-matching-pool
category: governance-proposals
url: https://gov.gitcoin.co/t/passed-sgtm-002-avantgarde-x-gitcoin-strategic-asset-management-for-the-matching-pool/19698
created_at: 2024-12-02T11:09:37.995Z
last_posted_at: 2025-05-05T19:46:39.250Z
posts_count: 16
views: 4460
like_count: 50
---

# [PASSED - SGTM 002] Avantgarde x Gitcoin: Strategic Asset Management for the Matching Pool

<https://gov.gitcoin.co/t/passed-sgtm-002-avantgarde-x-gitcoin-strategic-asset-management-for-the-matching-pool/19698>
Avantgarde | 2025-02-06 13:01:54 UTC | #1

# Avantgarde x Gitcoin: Strategic Asset Management for the Matching Pool

## Summary

As of today December 2nd, just under [$24m](https://etherscan.io/tokenholdings?a=0xde21f729137c5af1b01d73af1dc21effa2b8a0d6) worth of assets (mainly ETH and WETH) are sitting in the Gitcoin matching pool without a structured process around asset allocation and are currently in unproductive assets. Unlocking the potential of these assets is essential to support the program in expanding community funding capabilities and enabling Gitcoin’s ambition of reaching a $50 million Gross Marketplace Value through high-impact grants that catalyze ecosystem growth.

In this proposal, we put forward a path to making these assets productive and implementing a strategy that can support Gitcoin’s long-term goals.

## Intro

This proposal outlines a clear path for the Gitcoin community to enhance the productivity of the Matching Pool, providing:

* A recommended strategy for allocating assets between growth-oriented assets (e.g., ETH) and stable assets to support Gitcoin's long-term grant-making goals.
* A rationale for prioritizing the growth strategy (70% ETH / 30% Stablecoins) as the default allocation, given its potential to grow grant funding while maintaining flexibility to adapt over time.

The strategy will be implemented transparently and non-custodially, in collaboration with Avantgarde Finance, ensuring alignment with Gitcoin’s mission and adaptability to future market developments.

[Avantgarde](https://avantgarde.finance/) is a crypto native asset management firm that caters primarily to DAOs, foundations and protocols, specializing in natively run on-chain asset management, leveraging DeFi protocols and tools to build solutions for clients. Our company is headquartered in London with operations in the UAE, Bahamas and Panama.

Avantgarde has been active in DeFi since 2016, notably as co-founders of the onchain asset management protocol [Enzyme](https://enzyme.finance/), and brings decades of experience from reputable TradFi firms to help DAOs and Foundations optimize treasury management strategies, improve financial sustainability, and support long-term growth. Past and current clients include Uniswap, Arbitrum, Safe, Gitcoin, Nexus Mutual, amongst others.

## Strategic Asset Allocation (SAA)

Having a higher allocation to ETH and other growth assets can improve the average expected outcome, but also leads to more negative outcomes in the event crypto prices perform poorly over the holding period. The strategy asset allocation decision should trade off the need to preserve capital to meet near term grant spending versus the desire to grow the level of grant spending over the longer term.

## Current Position

Over 97% of the matching pool is currently in ETH, WETH, and other long tail assets including ENS, and memecoins such as AKITA INU.

### Options across the Risk Spectrum

The Strategic Asset Allocation (SAA) framework spans a range of approaches across the risk / return spectrum. Without a crystal ball, the optimal allocation depends on risk tolerance and the desired tradeoff between growth potential and potential worst case scenarios. Using historical data on ETH and stablecoin yields, the table below illustrates the potential distribution of 1-year returns across various market environments for allocations ranging from 0% ETH / 100% Stablecoins to 100% ETH / 0% Stablecoins.

We show that the median return increases with higher allocations to ETH in a bull market, with the bear cases all having an increasingly negative outcome with a higher allocation to growth assets.

![|624x257](upload://WtCzoLBIQVXs79zSBgNjuEnwcn.png)
*(Source: Avantgarde, CoinGecko, DeFiLlama)*

To provide a clear understanding of the spectrum, we categorize the SAA options as follows:

* **Conservative** (30% ETH / 70% Stablecoins): Prioritizes stability while incorporating some exposure to growth assets for modest upside potential.
* **Moderate** (50% ETH / 50% Stablecoins): Balances growth and stability, offering a middle-ground approach for those seeking a mix of risk and reward.
* **Growth** (70% ETH / 30% Stablecoins): Emphasizes growth while maintaining some stability to manage liquidity and downside risks.
* **Aggressive** (100% ETH / 0% Stablecoins): Fully allocates to growth assets for maximum upside potential but is highly vulnerable to market downturns.

The chart below illustrates the potential impact of price movements on the value of the matching pool for different allocation options across different market environments (note this does not take into account potential grant spending nor yield generated from market selection).

![|570x393](upload://kRwNNpdmVjzytPfLfLEk4VsyiQC.png)

## Market Selection (MS)

Given the pace at which DeFi evolves, we feel it is impractical to fix the exact portfolio of markets to allocate to within governance, as yields move quickly and require dynamic allocation. Instead, we propose return objectives for allocations within each category, battle-tested protocols for the most part, while retaining some flexibility for measured allocations to more dynamic opportunities in recognition that the opportunity set could change significantly over the course of the investment horizon. This approach ensures that the Matching Pool remains securely positioned while still able to take advantage of shifts in the market to optimize returns.

## Growth Assets Category

The soft objective for the growth asset category is to outperform ETH.

### Current Position

Roughly $15.5m of the total pool (~85%) is at the time of writing in ETH or WETH. Another $2.2m (12% of total) are in other long tail assets including ENS, and memecoins such as AKITA INU.

As discussed above, the majority of the return in this category will be driven by price movements. That said, we will also look to deploy strategies to enhance returns over and above the base performance of ETH.

### Proposed Solutions

For the core allocation within the growth assets category, we will look to allocate to staking ETH strategies, focusing on the larger and well established protocols. Though there are a number of innovations within ETH staking across the risk spectrum, as highlighted in the SAA section, levels of yield have been low relative to the price volatility of ETH. Hence we will run a lower risk approach focused on capital preservation for the majority of the ETH allocation.

However, depending on the opportunity set provided by the market environment, we will look to maintain flexibility within the growth assets category to allocate a proportion to higher yielding positions and/or to diversify ETH price risk, within the context of well established and battle tested protocols. This could include measured exposure to non-ETH tokens such as BTC and other bluechip projects within the Ethereum ecosystem, or strategies such as looping on liquid staking tokens.

## Stablecoins Category

The soft objective for the stablecoin category is to outperform USDC.

### Current Position

The Matching Pool currently only contains ~$470k in stablecoins, less than 2.6% of the total portfolio. The majority of these are not currently productive assets and not earning any revenue.

### Proposed Solutions

Allocate to the stablecoin pools across DeFi, focusing on the largest and most battle tested protocols whilst focusing on diversification, looking to earn a higher yield than sDAI (and/or sUSDS).

We believe this objective is achievable based on realised performance of strategies we have run in practice and also the observed opportunity set across large and well established DeFi protocols including: Aave, Compound, Curve, Ethena, Pendle, Maker, Morpho, Spark, and Uniswap.

![|624x455](upload://gI2lHlBJowQ4DjiZtWLdmCVmHLe.png)
*Source: Avantgarde, DeFiLlama*

As per the Strategic Asset Allocation section, we recognise that the primary roles for stablecoins are to reduce volatility and to provide a source of liquidity for funding grants in the near term. Therefore, we believe it is prudent to maintain a liquidity buffer of USDC (exact % dictated by the prevailing market environment) which is unallocated and not exposed to any smart contract risk within DeFi. The downside is that this will not earn additional revenues for the Matching Pool.

## Strategic Recommendation

**We recommend adopting the growth strategy (70% ETH / 30% Stablecoins) as the default allocation**. This strategy provides good potential for expanding the grant pool over time while maintaining flexibility to diversify into more conservative allocations as the market develops.

The growth strategy aligns with Gitcoin's goals of growing the grants program by leveraging potential upside in ETH, while still maintaining a prudent allocation to stablecoins for near-term liquidity needs and as a countercyclical buffer during periods of market weakness. Over time, as the matching pool evolves and market conditions change, we can periodically reassess and adapt the target allocations if deemed necessary by the community.

This iterative approach ensures that the allocation remains aligned with both Gitcoin's long-term ambitions and the evolving needs of the grants program.

## Infrastructure

We propose to keep the assets in the same multisig and add Avantgarde Finance as a signer on the multisig to line up transactions. In some cases, the use of the zodiac roles modifier might be used to embed smart contract roles & permissions to allow Avantgarde Finance to execute faster within a controlled environment.

## Reporting

Avantgarde Finance will provide monthly (written) reporting on the performance of assets. A quarterly community call will be organized too.

## Fees

We propose a performance fee of 10% subject to high water mark (resets whenever fees are payable), with no other management fee involved; where performance for any assets in the Growth category is measured against ETH, and assets in the Stablecoin category against USDC—though we remain flexible and open to feedback.

#### **Thank you for reading our proposal, and we look forward to hearing your feedback!**

-------------------------

Sov | 2024-12-02 12:58:05 UTC | #2

I support this partnership with Avantgarde Finance as their proposed strategy balances growth potential with risk management for Gitcoin's matching pool. Their approach, proven track, and performance-only fee structure demonstrate alignment with Gitcoin's goals of expanding grant funding while maintaining responsible asset management.

-------------------------

deltajuliet | 2024-12-02 18:01:02 UTC | #3

Thanks to the team @Avantgarde for putting this together, I'm looking forward to the future of a sustainable Matching Pool and expanding with the team further on the Foundation and Treasury resources. I'm excited to hear the community input on this proposal and am in favor of it. It's the intention of Gitcoin to monitor this relationship and returns closely as well as find ways to recreate successes with minimal risk to funds.

-------------------------

MathildaDV | 2024-12-05 18:27:16 UTC | #4

Very much in favor of this proposal. Thank you to @Avantgarde for this detailed proposal. I'm really excited about the future of the program and how this diversification will further enhance sustainability, and ultimately support the builders in the ecosystem. Also appreciate the low-risk approach.

-------------------------

meglister | 2024-12-12 02:41:31 UTC | #5

I'm supportive of this strategy to grow the matching pool and appreciate the aligned fee structure you're proposing!

-------------------------

gnomadic | 2024-12-13 17:48:51 UTC | #6

this makes sense and is a good use of the funds!  Avantgarde seems like a great partner to bring this together.

-------------------------

Avantgarde | 2024-12-19 13:59:42 UTC | #7

Thank you all for the positive feedback so far, we're very excited about the prospect of working closely with Gitcoin and very much appreciate your support!

If you're a Gitcoin Steward, we'd love to hear your thoughts as we're just one Steward away from moving this into the next phase.

-------------------------

cmurdock | 2024-12-19 15:53:56 UTC | #8

I am supportive of bringing on Avantgarde as a partner in this effort as collaborating on ways to sustainably manage Gitcoin's matching pool is of paramount importance to Gitcoin's future impact. Excited to see this work begin.

-------------------------

Avantgarde | 2024-12-24 11:20:41 UTC | #9

Thanks again all who've shown their support thus far - this proposal is now live for voting at https://v1.snapshot.box/#/gitcoindao.eth/proposal/0x8b698644c08b424f87709228caa0ee11af6a3a047d47032b0f45a7f971d15696.

We're very excited about the opportunity to work more closely with Gitcoin and would greatly appreciate your vote to help us reach quorum during this festive season!

Wishing you all a Merry Christmas and a Happy New Year! :snowman_with_snow: :sparkles:

-------------------------

cmurdock | 2025-01-07 20:18:31 UTC | #11

Note that this Proposal was sent to Snapshot over the holidays, but due to many citizens being offline over the holiday period, the proposal did not reach quorum. 

This proposal is now posted as a Revote proposal on Snapshot here:

https://v1.snapshot.box/#/gitcoindao.eth/proposal/0x524d7f51ea46bdc8fc461b999eff7a8da146386e5a49528b31d0a41293f0fe13

-------------------------

Gauntlet | 2025-01-08 19:09:32 UTC | #12

We want to propose a competitive process for managing the Gitcoin Matching Pool. As discussed with some existing stewards, Gauntlet believes that, along with Aera, we can provide a competitive and more performant offer to the Gitcoin DAO. We believe we can provide a more aggressive proposal by delivering benefits such as:

1. Completely on-chain, permissionless, and non-custodial tooling via the [Aera Protocol](https://www.aera.finance/).
2. Gauntlet and Aera will guarantee no fee for the first 12-months of engagement as the Strategic Asset Manager for Gitcoin Matching Pool. This would support Gitcoin’s joining the Aera ecosystem as an early adopter of the Aera Protocol alongside leading protocol teams and DAOs such as Morpho, Compound, Arbitrum, Euler, Xai, and Seamless. 
3. It’s unclear why the objective is only to outperform the base asset. Gauntlet and Aera believe they can provide more aggressive benchmarks while prioritizing security and risk management. Current Aera vaults are performing at the following annualized benchmarks:
   *  Stablecoins: 9.28%
   * ETH: 4.68%

You can read more about our Stablecoin strategies [here](https://gauntlet.notion.site/Aera-One-Pager-Stable-Coin-Strategy-a95f415e7d704efaae7f2e5896f76522?pvs=74). 

If this alternative is of interest, we can create a more comprehensive offer and meet with key delegates to discuss the benefits of on-chain, permissionless, and non-custodial asset management. We believe our approach would align closely with Gitcoin’s mission to build tools that enable communities to build, fund, and protect what matters to them. 

**About Aera**

Aera is an on-chain solution that optimizes DAO funds autonomously. It addresses the common pain point of inactive treasury management that often hinders a DAO’s ability to maintain a runway, cover liabilities, and benefit from market growth. Unlike traditional institutions that rely on nimble managers for fund allocation, DAOs face unique challenges, including governance and incentive alignment with external managers. To address these, Aera offers a unified solution for efficiently and transparently managing on-chain treasuries, grants, and incentive funds through customizable vaults. 

Aera vaults can hold stablecoins, native tokens, and other cryptocurrencies, with their objective functions tailored to each DAO’s needs. Guardians leverage off-chain logic to automate rebalancing decisions, ensuring the vaults meet their objectives across various market scenarios and time horizons. Gauntlet will be the initial Guardian of the Aera vault.

[Aera Vaults](https://app.aera.finance/) currently hold >$100M TVL, including vaults owned by Compound, Swell, Seamless, Morpho, Moonwell, Puffer, Threshold, and more. 

Below is an image of how Aera works:

![image|690x308](upload://2sgA91qk9ZS8M3NFYIVTKa0Ei1v.jpeg)

-------------------------

ccerv1 | 2025-01-08 21:00:41 UTC | #13

My two gwei:

- I'm not an expert in this domain, but think it is definitely worth comparing multiple options. 
- Gauntlet & Aera have a world class reputation; I've known one of the Aera founders for a long time and can certainly vouch for them.
- I see this proposal went to Snapshot vote yesterday, so not sure if this is too late to consider.

-------------------------

cmurdock | 2025-01-15 14:03:58 UTC | #14

Update that this proposal passed on Snapshot:
99.98% Yes. 
0.01% No
0.01% Abstain

https://snapshot.org/#/s:gitcoindao.eth/proposal/0x524d7f51ea46bdc8fc461b999eff7a8da146386e5a49528b31d0a41293f0fe13

@Avantgarde will update with next steps

-------------------------

Avantgarde | 2025-01-22 12:48:46 UTC | #15

**Thank you to everyone who voted in support of our proposal. We are very excited about this partnership and look forward to working with the Gitcoin community!**

As a next step, we are looking to set up role modifiers on the Matching Pool multisig that will maintain operational security whilst enabling sufficient flexibility for efficient treasury management. This will enable Avantgarde to perform certain treasury management actions autonomously within a pre-defined set of restrictions. We will discuss with the community and be posting a follow up proposal to this effect within the next week.

We will be using Zodiac Roles modifier v1 along with the Zodiac Pilot Chrome extension to interact through Zodiac roles. We will set the roles up so that the pre-agreed operations can be done through in a more flexible manner (without requiring all signers) to ensure a balance of sufficient oversight with efficient execution of time-sensitive operations. This includes the actual contract & methods of the protocols that we will interact with, and approval for certain tokens. 

**In the meantime, the Zodiac repo and audit can be found here:**

https://github.com/gnosisguild/zodiac-modifier-roles-v1

https://github.com/gnosisguild/zodiac-modifier-roles-v1/blob/main/packages/evm/docs/ZodiacRolesModifierJan2022.pdf

**We will follow up with a Snapshot proposal soon** to add a signer to the MP multisig, outlining addresses and all remaining details, including the protocols and tokens available to the strategy.

Any questions don't hesitate to ask!

-------------------------

deltajuliet | 2025-01-22 18:02:03 UTC | #16

Thanks @Avantgarde - Appreciate the followup. Will be looking to the community to weigh in here on the logistics but this all makes sense. 

@ccerv1 So you and the community are up to speed .. I'm chatting w/ Gauntlet - and have discussed options with a large handful of partners for various safes after posting the [OG post](https://gov.gitcoin.co/t/temp-check-sgtm-000-treasury-management-strategy-for-gitcoin-v1/18564) that led to this, def open to diversifying the diversification efforts! 

Based on our governance @Avantgarde's next step is the Snapshot proposal for the Zodiac role modifier on the MP to enact the proposed diversification and have asked them to outline everything that they would have permissions for/tokens affected/platforms used and of course the above audits. I'd welcome any further comments for those invested in Gitcoin's governance to weigh in here and in the next proposal - would be great to get this going!

-------------------------

ccerv1 | 2025-05-05 19:46:39 UTC | #17

Just to clarify my recent vote:
I meant to **abstain**, not vote against, and fat-fingered the wrong button. 
:melting_face:

-------------------------
