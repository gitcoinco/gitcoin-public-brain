---
id: 204
title: "Workstream Suggestion: DeFi Treasury Management"
slug: workstream-suggestion-defi-treasury-management
category: open-discussion
url: https://gov.gitcoin.co/t/workstream-suggestion-defi-treasury-management/204
created_at: 2021-05-21T23:05:32.443Z
last_posted_at: 2021-07-01T01:30:07.843Z
posts_count: 17
views: 4700
like_count: 41
---

# Workstream Suggestion: DeFi Treasury Management

<https://gov.gitcoin.co/t/workstream-suggestion-defi-treasury-management/204>
androolloyd | 2022-05-28 15:39:23 UTC | #1

Hey Gitcoiners,

I suggest that we put together a Workstream around how to effectively manage the Gitcoin treasury. 

Using DeFi protocols we can extend the treasury's capital and maximize the impact of public goods funding. 


We have some heavy hitters of the DeFi space who have stood up to be Stewards so I am confident we can put together a good strategy to effectively tackle this.

This also happens to co-inside with some work we are doing at PleasrDAO.


I think having a strategy in effect in time for next Grants round's completion would be prudent.


Catch you in the Metaverse.

-------------------------

Yalor | 2021-05-23 00:27:56 UTC | #3

That is a great idea, there is actually an existing group consisting of Hudson Jameson, Anthony Sassano, David Hoffman and some others. They currently manage the Gitcoin Community treasury, so I wonder if we could expand that group a little bit via this workstream ?

-------------------------

ajbeal | 2021-05-27 22:01:27 UTC | #4

Hey Gitcoiners!

Below is a draft Treasury Management Proposal for the Grants Multi-sig, authored by @HelloShreyas, @ajbeal, and @AcceleratedCapital from [Llama](https://twitter.com/llamacommunity_?lang=en), which provides treasury management as a service to DAOs.

**Treasury Management Approach**

There are a variety of approaches to treasury management based on the goals and demands of the organization. The primary levers available to us are the *assets* and the *allocation*. 

We can distinguish different crypto assets based on market cap, liquidity, months since launch, volatility, return potential, and other factors. For purposes of this exercise, we have divided assets into three tranches:

![Screen Shot 2021-05-26 at 5.40.15 PM|690x484](upload://4muMOl8F9y5Yx5FUHyLstUG86WK.png)

Because funds in the Grants Matching Pool are needed for quarterly grant distributions, we are inclined to take a slightly more conservative approach. Below is the suggested allocation:

**Low Risk (40%)** - Allocated to stablecoins and interest bearing equivalents.
* An amount of these assets equal to at least the dollar amount of the last quarter of grants will sit idle in the Grants multi-sig and be available for immediate use.
* The remainder will be put to work across several lending and AMM platforms to earn passive yield. [We estimate 7-12% APY on these assets for the foreseeable future.]

**Medium Risk (50%)** - Allocated to large cap cryptocurrencies and DeFi tokens.
* This tranche will be held long, and may be put to work across several lending and AMM platforms.
* To the extent the asset can be staked for yield such as in the case of ETH2, we will commit 100% of the asset to staking, taking into consideration any lock up periods. There is a preference for a derivative asset that enjoys the staking yields without being subject to the lock up (ex: stETH on Lido), if available.
* Assets in this tranche may be used in conjunction with assets from the Low Risk tranche for yield generation purposes. Example - contributing an equal amount of WETH and USDC to the WETH/USDC liquidity pool on Uniswap.

**High Risk (10%)** - Allocated to smaller cap tokens
* This tranche will be held long, and may be put to work across several lending and AMM platforms.
* To the extent the asset can be staked for yield such as in the case of ETH2, we will commit 100% of the asset to staking, taking into consideration any lock up periods. There is a preference for a derivative asset that enjoys the staking yields without being subject to the lock up if available.
* Assets in this tranche may be used in conjunction with assets from the Low Risk tranche for yield generation purposes. Ex: contributing an equal amount of [small cap token] and USDC to the relevant liquidity pool on Uniswap.

**Implementation of Treasury Management**

Llama will work with Gitcoin on an ideal way to implement the strategic asset allocation that involves the community and allows for effective decision making. We will screen assets based on various criteria including market cap, liquidity, months since launch, volatility, return potential, and other factors. The Gitcoin community will approve broad guardrails: tokens, strategic allocation, and rebalancing frequency. We will help implement rebalancing within those guardrails. This should be done on-chain, transparently, and potentially programmatically via Set Protocol. We will also review the strategic asset allocation periodically and make proposals to the Gitcoin community for feedback.


We would love to hear any feedback and questions!

-------------------------

kyle | 2021-05-30 14:38:05 UTC | #5

This is awesome! Are there turn key solutions to helping us balance in this way? One problem with multisigs is that it's often hard to coordinate the signatures required to send funds within the time window needed.

I wonder if an index of sorts (like $DPI) could be created to manage and balance this? Does something like that exist?

-------------------------

e-gons | 2021-05-30 16:23:42 UTC | #6

Thank you for putting together such a thoughtful proposal. I would add a few points for your consideration:

### Is the 60/40 mix between stocks (medium + high risk cryptoassets) and bonds (stablecoin yield farming) the optimal asset allocation for the treasury? 
The issue with the 60/40 portfolio is a *de minimus* benefit from diversification due to the 60%-90% correlation between the assets in each bucket. 

Another asset allocation mix to consider is something akin to a leading endowment, such as Yale, who will include lower correlation asset classes such as [real estate, leveraged equities, and venture capital](https://static1.squarespace.com/static/55db7b87e4b0dca22fba2438/t/607e4da7bc999d01b4752ea2/1618890160689/2020+Yale+Endowment.pdf). The GTC treasury could re-create some of these asset classes via synths that track stock market ETFs for things like real estate, commodities, etc.

### Security Selection
I suggest we utilize indices (e.g. DPI) where possible, as it is unlikely that we will increase the returns of the portfolio through superior security selection (e.g. picking UNI over SUSHI, etc.). We can create our own indicies through the Set protocol, but this has its issues as well (see below).  

### Ethereum Tail Risk Exposure
By investing 100% of the treasury in Ethereum denominated assets, it leaves the treasury open to systemic risk and the unknown unknowns.

To make the treasury more anti-fragile, it is worth considering diversifying the portfolio (e.g. BTC not WBTC).

### Implementation with Set
I like the simplicity, transparency and automation that the Set Protocol brings to the table, but I worry about the ETH tail risk exposure mentioned above. The ETH network can get very congested during market volatility and de-leveraging events, which create forced sellers. These are exactly the events when you need to be active, and being 100% reliant on ETH's network makes that difficult at the moment.

### Automation
Should we consider using some of Yearn's infrastructure (e.g. Vaults, multi-sig management, transaction automation) to help manage the 40% fixed income allocation? It is battle-tested and has an ardent community supporting it.

-------------------------

androolloyd | 2021-05-30 20:24:48 UTC | #7

I will say that I believe a large focus of the treasury mgmt should be coordinated around 'no loss' protocols so that we may function more like an endowment than a fund. 

This isn't to say I am against holding large cap currencies(as long as its not bitcoin), I just believe there is more value to be captured through incentivized community participation in the creation of our capital engine.

-------------------------

e-gons | 2021-05-31 16:24:10 UTC | #8

You make an excellent point. The goal of the fund should be first and foremost to protect purchasing power such that the treasury can support the current and future needs of the DAO. I suggest we decide on maximum acceptable volatility for the treasury's portfolio and work backward from there into an asset allocation strategy. The asset allocation decision will have the [biggest impact on the treasury's overall performance](https://bookdown.org/Albert/finance-shiller/guest-speaker-david-swensen.html), so it is worthy of our deep and careful consideration.

-------------------------

haywyer | 2021-06-01 22:14:19 UTC | #9

I wonder to what extent stablecoins are truly stable if they are pegged to a fiat currency. Is there perhaps a coin that is pegged to inflation?

A diverse portfolio would also have a number of assets with negative correlation with general crypto markets... perhaps some kind of volatility products or physical asset-backed tokens could be beneficial?

-------------------------

androolloyd | 2021-06-01 22:25:55 UTC | #10

RAI is not pegged to fiat. It i s a free floating asset powered by a PID controller.

-------------------------

haywyer | 2021-06-02 00:38:09 UTC | #11

RAI definitely sounds interesting. thanks.

-------------------------

bobjiang | 2021-06-02 13:38:34 UTC | #12

love this idea, I am definitely interested in this workstream.

-------------------------

wyx | 2021-06-09 00:16:49 UTC | #13

As with any asset management service, they will take a few basis points off for management fees. 

How much is this fee and will Llama be the custodian of the funds?

Also, 7-12% APY seems generous, might have to revise that downwards as more money gets parked into the ecosystem.

-------------------------

ajbeal | 2021-06-09 02:26:52 UTC | #14

Yes, we will try to automate the allocation and any rebalancing as much as possible. Protocols to accomplish this include Set, Index Coop and potentially UMA.

-------------------------

ajbeal | 2021-06-09 02:37:00 UTC | #15

Great questions. 

1. Llama will NOT take custody of treasury funds.

2. We do anticipate fees to be a small percentage of the treasury. The specific amount is still being considered.

-------------------------

ajbeal | 2021-06-09 02:41:49 UTC | #16

These are all worthwhile considerations. 

1. Agree that to the extent possible, finding uncorrelated assets is ideal. 
2. We agree that indices are easier to manage and will look to leverage them where possible. 
3. We can certainly consider using Yearn's infrastructure.

-------------------------

meknab | 2021-06-30 01:30:35 UTC | #17

I know I am late to this thread but I agree with this approach

-------------------------

zyks678 | 2021-07-01 01:30:07 UTC | #18

A great idea, let's discuss it and implement it as soon as possible.

-------------------------
