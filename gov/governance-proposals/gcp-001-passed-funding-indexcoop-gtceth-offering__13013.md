---
id: 13013
title: "[GCP-001] - PASSED - Funding IndexCoop gtcETH offering"
slug: gcp-001-passed-funding-indexcoop-gtceth-offering
category: governance-proposals
url: https://gov.gitcoin.co/t/gcp-001-passed-funding-indexcoop-gtceth-offering/13013
created_at: 2023-02-20T16:02:33.727Z
last_posted_at: 2023-03-08T20:26:42.533Z
posts_count: 21
views: 4714
like_count: 86
---

# [GCP-001] - PASSED - Funding IndexCoop gtcETH offering

<https://gov.gitcoin.co/t/gcp-001-passed-funding-indexcoop-gtceth-offering/13013>
kyle | 2023-03-06 21:27:58 UTC | #1

# [Gitcoin Community Proposal] - Funding IndexCoop gtcETH offering

A HUGE thank you to @c-squared.eth, @funkmasterflex from the Index Coop community for drafting the majority of this GCP. You can find [the full details of the IIP](https://gov.indexcoop.com/t/iip-xyz-launch-the-gitcoin-staked-eth-index-gtceth/4508) (Index Improvement Protocol) on their forums.

## Summary

In partnership with Index Coop, we would like to propose the Gitcoin Staked ETH Index (gtcETH), which will provide diversified exposure to the top liquid staking tokens and share a portion of staking rewards with the DAO in support of public goods funding.

As part of this proposal, I am requesting we seed initial liquidity pool requirements to ensure this asset is available to those who would like to take advantage of it. That seed funding should come from the Matching Pool as the yield accrued will be used in the matching pool in the future (and we can always sell the LP position and recover our assets if we need them in the short term).

## Abstract

gtcETH will enable token holders to access the top ETH liquid staking tokens through a single token while simultaneously contributing to public goods funding. gtcETH will employ the [dsETH methodology](https://gov.indexcoop.com/t/iip-171-launch-the-diversified-staked-eth-index-dseth/4389#h-60-methodology-15), which promotes decentralization and competition amongst liquid staking protocols.

## Motivation

Public goods are an integral part of Ethereum’s past, present, and future. Ethereum itself is built on the premise that a wide variety of stakeholders can come together to build, and ultimately depend on, public goods that serve the collective interests of the community. No single organization embodies this mission as much as Gitcoin DAO. Since 2017, we have provided over [$50m](https://gitcoin.co/results) in grants and bounties funding to thousands of teams and developers. Raising funds for public goods, however, can be unpredictable and inconsistent because of the donation-dependent models in place today. DeFi–specifically liquid staking, streaming fees, and Index Coop–can help with this.

gtcETH gives token holders the ability to earn and share diversified staking rewards with the Gitcoin DAO by holding an index of the top liquid staking tokens and enabling a streaming fee. For gtcETH token holders, the annualized streaming fee of 2.00% (1.75% for the Gitcoin DAO and 0.25% for Index Coop) is collected in a passive fashion, so aside from buying and holding the token, gtcETH holders don’t have to do anything to earn staking rewards for themselves and fund public goods. For Gitcoin, gtcETH provides a consistent, subscription-like revenue stream for funding grants and/or bounties as well as a low-friction access point for contributions. gtcETH also provides a positive-sum option for those considering donations because token holders retain price exposure to ETH and earn some staking rewards while simultaneously donating to public goods (versus an outright donation where the user must forfeit their ETH).

gtcETH will utilize the dsETH methodology and technology, so users can effectively distribute their stake across the top liquid staking protocols and earn an aggregate staking return (minus the streaming fee). Rather than selecting a single liquid staking token and concentrating risk, gtcETH token holders benefit from its innate diversification - both at the asset and the protocol layer. The methodology is also weighted towards protocols with more node operators and balanced distribution of stake, with the objective of encouraging decentralization and competition in the on-chain liquid staking market.

## Specification

gtcETH will be built on Index Protocol and contain Rocket Pool, Lido, and StakeWise liquid staking tokens. Lido’s stETH will be wrapped in order to accommodate its rebasing nature, and StakeWise rewards will be reinvested on a periodic basis into sETH2.

Flash Minting (and Redeeming) will be enabled at launch, allowing users to deposit ETH or ERC20s and receive gtcETH tokens in return.

Though there are many different liquid staking tokens in the DeFi ecosystem today, there are no on-chain offerings that enable users to earn staking rewards and contribute to public goods simultaneously. However, this table presents the liquid staking tokens that will be present in gtcETH and their respective yields:

|token|Issuing Protocol|Protocol Fees|APR ([sources](https://www.rated.network/dseth?network=mainnet))|
| --- | --- | --- | --- |
|wstETH|Lido|10% of rewards|5.2%|
|rETH|Rocket Pool|15% of rewards|4.7%|
|sETH2|StakeWise|10% of rewards|5.3%|

As a result, the initial composition for gtcETH will yield a 2.99% Net APR after accounting for the streaming fee (2.00% in total). This is a simple projection, and it is worth noting that a variety of factors - percentage of ETH staked, network fees, fee burn - fundamentally affect reward rates (thus yield is subject to change over time).

## Example composition

dsETH will have the following composition at launch:

* Rocket Pool rETH: 43.9%
* Lido (w)stETH: 29.7%
* StakeWise sETH2: 26.4%

![|624x387](upload://noA9Ulx8bPwT5xY7QyYjhkIavbA.png)

Rewards earned by the underlying assets will gradually accrue to the token’s value and be realized in the form of price appreciation. The annualized streaming fee is captured block-by-block via inflation.

## Backtest results

![|624x387](upload://dJ4MK4i4YsmDZJjqquqrlAivBjr.png)

Backtest calculations are shown for March - August 2022. The former is the earliest date for which complete price history is available for all constituents. This plot is shown with dsEth, but gtcETH will be the same given its 1:1 pair with dsETH.

The green plot shows the price history of gtcETH in USD terms, the blue plot gtcETH spot price in ETH terms, and the red plot gtcETH “NAV” price in ETH terms. It is important to note that the gtcETH “NAV” price (red) assumes 1:1 exchangeability between the underlyings and ETH. The gtcETH spot price in ETH terms (blue) can decrease due to decoupling between the underlying staked ETH tokens and ETH; an example would be the discounted exchange rate for stETH relative to ETH. Historical data on node operators were not available so we assumed a uniform allocation across the constituents.

## Size of Opportunity

Over $50m has been donated to and distributed by Gitcoin since 2017 in support of public goods. The Gitcoin Grants program accounts for $32m of that sum, with a median value of $1.14 and an average value of $14.26. In simple terms, if a user were to hold 1 gtcETH token for a year and earn a 5% gross staking APR during that time, their gtcETH token would ≈ 1.03 ETH and they will have contributed ~0.0175 ETH to Gitcoin over that period; applying a constant ETH price of $1,700, that contribution would be worth $29.75, or double the average historical contribution.

Additionally, at a TVL of $1m, gtcETH would contribute ~$17,500 annually to Gitcoin Grants. On a quarterly basis, this would earn gtcETH a top ten spot in Gitcoin’s [Funders Leaderboard](https://gitcoin.co/leaderboard/payers?cadence=quarterly&keyword=&product=all) while also earning gtcETH holders the net staking rate themselves.

## Benefits

Given the size of the opportunity, and the simple rebalancing, this initiative would yield an always on source of funding for our Matching Pool. The product is based on the dsETH product and benefits from the security and contract audits to ensure users funds are secure and able to participate in the yield from the collection of underlying assets.

This is also Gitcoin’s first opportunity to partner with Index Coop on a novel mechanism for funding public goods. Index has been a leader in the index fund creation and management having created multiple index funds to enable exposure to a basket of tokens without requiring users to be experts in selecting those tokens. In our case, we receive the upside and knowledge of the product while offering users the ability to fund public goods in a way that grows the value of their investment, and our funding for public goods.

gtcETH will offer a funding option to those who dont always know which grants to select themselves. The yield from both the index, and the liquidity pool position will yield funding results for the DAO and the matching pool.

## Drawbacks

This product (gtcETH) will be tied hand in hand to dsETH – while this has many benefits, it also has the drawbacks that any negative outcomes of dsETH will also affect gtcETH. It is worth noting, that while the majority of fees for gtcETH will be going to public goods, not 100% of the fees will be going to public goods as Index Coop will retain their same 0.25% fee.

We will be withdrawing a modest amount of ETH to help seed the liquidity pool and ensure future gtcETH holders are able to swap into the position. This ETH is just sitting in our matching pool today, not “working” for us, but by moving it to an LP there is always the risk of impermanent loss.

## Vote

I am requesting a vote that will accomplish the following (a yes vote would do…):

1. Formalize the relationship between us and Index Coop and enable co-branding and marketing of the new gtcETH product (if it passes the Index Coop governance)
2. Move 100 ETH from the matching pool multi sig to fund two LP positions (50ETH each LP):
2.1 pair gtcETH against dsETH in a 1bp pool
 2.2 pair gtcETH against ETH in a 5bps pool
(The two pools ensure deeper liquidity and reduce swapping fees for moving into gtcETH while also ensuring arb opportunities exist between dsETH and gtcETH to ensure they stay near parity in price)

3. Work with Index Coop to rebalance the product on a ~quarterly/monthly cadence as needed.

A no vote would prevent us from funding the initial liquidity, but may not materially change Index Coop’s decision to build and launch the product for us.

## Revision history

[2022.02.20] Made some updates to the impact results Gitcoin has had. Thanks @umarkhaneth for the suggestions.

-------------------------

ceresstation | 2023-02-20 16:36:13 UTC | #2

I don't have a ton to add here right now but just wanted to say this is awesome to see, this initiative has been a long time coming with efforts across multiple workstreams including PGF / GPC.

Also, I like the idea of actually starting to use the GCP framework that Cooper and I drafted lol.

-------------------------

c-squared.eth | 2023-02-20 19:27:04 UTC | #3

Howdy :wave: long time supporter, first time commenter.

I wanted to share a couple of comments and express Index Coop's excitement for gtcETH!

[quote="kyle, post:1, topic:13013"]
This is also Gitcoin’s first opportunity to partner with Index Coop on a novel mechanism for funding public goods.
[/quote]

The streaming fee mechanism in place for gtcETH accrues on a block-by-block basis, creating a kind of real-time subscription revenue for the Gitcoin Grants program. Gitcoin can collect these fees at any time too!

In addition to the consistent stream of contributions, gtcETH enables a positive-sum donation path for token holders. Previously, contributors would have to part ways with their assets - every gwei given to Gitcoin was one less gwei kept by the contributor. For this reason, it can be difficult for potential contributors to part ways with their ETH (even though they would ultimately benefit from the proliferation of public goods). With gtcETH, contributors can...

1. keep their ETH and maintain price exposure
2. earn staking and execution layer rewards
3. contribute to Gitcoin Grants funding

... all by buying and holding the token. Because gtcETH uses the dsETH methodology, it also...

4. diversifies your portfolio with multiple liquid staking tokens
5. promotes decentralization within the liquid staking ecosystem

Next:
[quote="kyle, post:1, topic:13013"]
This product (gtcETH) will be tied hand in hand to dsETH – while this has many benefits, it also has the drawbacks that any negative outcomes of dsETH will also affect gtcETH.
[/quote]

Though gtcETH will utilize the dsETH methodology at launch, it is possible to deviate from that methodology if that is the community's preference. For example, if Gitcoin would like to expand or contract the current inclusion criteria to allow for more or less liquid staking tokens in the future, that could be enacted through the standard governance process.

Anyone can learn more about the dsETH methodology in the forum post cited above!

Overall, the Index Coop is very excited to bring this product to market and experiment with a new public goods funding mechanism! :owl:

-------------------------

0xDev | 2023-02-20 20:32:00 UTC | #5

Great job, @kyle! We (the Index Coop) really hope we can bring this idea to reality with Gitcoin - and that the product grows huge and throws off a nice revenue stream for Gitcoin.

-------------------------

tigress | 2023-02-21 11:20:45 UTC | #6

[quote="c-squared.eth, post:3, topic:13013"]
With gtcETH, contributors can…

1. keep their ETH and maintain price exposure
[/quote]

I have not fully understood the mechanics of this from a dumb user perspective. 

Could you possible point me towards a video which shows the flow / steps in the process of staking using dsETH? The [linked forum post](https://gov.indexcoop.com/t/iip-171-launch-the-diversified-staked-eth-index-dseth/4389#h-60-methodology-15) did not really inform me well so I can run through it in my brain.

Moreover I was wondering: With this product can I stake GTC and / or ETH and contribute towards Gitcoin Grants funding?

Thanks 🙏

-------------------------

DisruptionJoe | 2023-02-21 16:29:04 UTC | #7

I'm fully in support of the direction because I love the idea of continuous funding for public goods. It seems like a very positive sum idea. 

I would like to understand risks in rebalancing and other potential risks are in this proposal. 

I would vote yes today.

-------------------------

vikrant6661 | 2023-02-22 03:01:24 UTC | #8

Very well laid down proposal. I vote in favour.

-------------------------

kevin.olsen | 2023-02-22 07:47:13 UTC | #9

Amazing stuff. I'm supportive of this proposal.

-------------------------

shawn16400 | 2023-02-22 11:17:31 UTC | #10

[quote="kyle, post:1, topic:13013"]
Additionally, at a TVL of $1m, gtcETH would contribute ~$17,500 annually to Gitcoin Grants. On a quarterly basis, this would earn gtcETH a top ten spot in Gitcoin’s [Funders Leaderboard ](https://gitcoin.co/leaderboard/payers?cadence=quarterly&keyword=&product=all) while also earning gtcETH holders the net staking rate themselves.
[/quote]

hey @kyle can you help me understand this?

- Gitcoin is contributing 100ETH to the staked pool ($~160,000) 
- If the staked pool reaches $1M, Gitcoin Matching pool stands to receive ~ $17K annually 

Two questions:
1. Is my understanding correct on the annual income of $17K at $1M in the matching pool? 
2. How does the pool get to $1M? Will Index market this, does Gitcoin market this, will it happen automatically?

-------------------------

kindeagle | 2023-02-22 16:23:15 UTC | #11

Hi @tigress  -

Here's the video: https://twitter.com/indexcoop/status/1617932168428421121?s=20

gtcETH is an index of the top ETH liquid staking tokens, so it's accessible by purchasing on a DEX or minting via the Index Coop app. You don't have to stake anything yourself. The staking yield will automatically accrue and be reflected in an increasing price of the token vs. ETH.

And a lot more resources are available on our blog: 
https://indexcoop.com/blog/faq-the-diversified-staked-eth-index-dseth
https://indexcoop.com/blog/understanding-the-diversified-staked-eth-index-dseth

-------------------------

azeem | 2023-02-22 17:51:57 UTC | #12

Worked with Kyle on helping make this happen. Creating self sustaining funding for Gitcoin is one of the most imperative things for us to be working on and so I'm entirely in favor of this!

-------------------------

kyle | 2023-02-23 02:11:50 UTC | #13

[quote="shawn16400, post:10, topic:13013"]
Two questions:

1. Is my understanding correct on the annual income of $17K at $1M in the matching pool?
2. How does the pool get to $1M? Will Index market this, does Gitcoin market this, will it happen automatically?
[/quote]

Great questions!

1 - The index fund will need to have $1MM in total locked value for us the generate the $17k in revenue. That revenue will be emitted back to the matching pool.

2 - The current plan is to have both ecosystems market this product and encourage folks to earn a yield and fund public goods by buying gtcETH. If we can convince folks to buy and hold gtcETH (and lock up $1MM+ in TVL) we will realize the projection of $17k. Ideally we convince a few large Eth holders to swap in gtcETH. them swapping a few thousand Eth would be a terrific outcome for Gitcoin. But, we need a product available for them to take advantage of this :slight_smile:

[quote="azeem, post:12, topic:13013"]
Worked with Kyle on helping make this happen.
[/quote]

Yes! Azeem has been immensely valuable in making sure these GCP's come to fruition. Much respect and appreciation for the partnership on these :slight_smile:

-------------------------

epowell101 | 2023-02-23 15:17:14 UTC | #14

Seems like a great experiment.

It looks like there may be some operational and reputational risk as well, unless I'm missing something.

Operational:
- the nuts and bolts are being handled by Index - 
    - if somehow we are hacked or they are - this could impact our reputation w/ some of our largest supporters (the stakers)
- marketing -
    - we have a marketing team that, while large, seems to be fairly stretched
- general management
    - we only have so many cycles per day to consider something - c/d this distract us from other priorities

Reputation risk
- if this does not go well - not a hack but otherwise - would it somehow undermine the valuable Gitcoin brand?

Again, overall I'm very supportive of this sort of experimentation.  It reminds me of the Aqueduct idea which also seems to have a lot of potential (we are hoping to build it into some work the OpenData Community is doing in supporting projects for eg).  If we can have a range of ways to passively generate funds for the matching pool that build over time somewhat organically - amazing.

-------------------------

kyle | 2023-02-26 05:54:53 UTC | #15

Hey all I numbered this proposal, and moved it to the Proposals section given the quorum and five day duration.

I have also moved this to Snapshot! - https://snapshot.org/#/gitcoindao.eth/proposal/0x6f1fa6b220417aa52ad566cfeb83c7e820f146a02eb04c754389a615035502df 

I would love to have folks go vote. This will not need a vote on Tally as we will not be withdrawing funds from the Treasury, but the multi-sig instead.

-------------------------

lefterisjp | 2023-02-27 21:54:34 UTC | #16

Hey this seems like an interesting idea. Not totally sure it would work, as it seems to depend on enough people swapping their ETH for gtcETH to get to the 1MM. Do you guys have any commitments from any whales on this?

If it ends up not working would it affect Gitcoin in any way?

In general sounds like a nice experiment.

-------------------------

ccerv1 | 2023-02-28 13:30:00 UTC | #17

In general I'm in favor of novel funding mechanisms. This is a cool idea and a product that I would use. 

It has my vote.

That said, this also feels like an initiative in the "low impact / easy to implement" corner of the matrix. I hope it doesn't distract from more audacious initiatives to create sustaining funding for Gitcoin.

-------------------------

kyle | 2023-03-03 03:44:05 UTC | #18

We have not really marketed this yet, but we hope to encourage folks to do this once the pools and things are live. Every little bit of participation helps though!

-------------------------

jaxcoder | 2023-03-03 20:08:52 UTC | #19

Love to see these income systems getting proposed and put in place.

-------------------------

c-squared.eth | 2023-03-06 19:43:16 UTC | #20

The [Snapshot vote](https://snapshot.org/#/gitcoindao.eth/proposal/0x6f1fa6b220417aa52ad566cfeb83c7e820f146a02eb04c754389a615035502df) has passed in favor of funding the gtcETH pools!

![Screenshot 2023-03-06 at 2.41.25 PM|690x391](upload://1Vfdk8oQ20wM9a0SEPnNy8cFilD.png)

gtcETH coming soon to a DEX near you :wink:

-------------------------

kyle | 2023-03-07 20:55:08 UTC | #21

Hey all - This product is live! And the 100 Eth has been transferred. We now have the LP positions in the Grants Matching Pool. 
![Screenshot 2023-03-07 at 3.52.10 PM|653x500](upload://eOq9c4bvgxJjcxSTXkextaCRCxi.jpeg)

Definitely pumped for this product to be live and to offer folks the ability to continuously fund public goods with their Eth.

-------------------------

koday | 2023-03-08 20:26:42 UTC | #23

Love this idea and I'm glad the vote passed - excited to allocate some ETH into gtcETH. 

Can't wait to see more experiments with sustainable, regen-focused public good funding models!

-------------------------
