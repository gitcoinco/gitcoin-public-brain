---
id: 17534
title: "ETH Staking for Public Goods Funding"
slug: eth-staking-for-public-goods-funding
category: open-discussion
url: https://gov.gitcoin.co/t/eth-staking-for-public-goods-funding/17534
created_at: 2024-02-01T18:43:56.383Z
last_posted_at: 2024-02-08T13:29:13.083Z
posts_count: 7
views: 3408
like_count: 18
---

# ETH Staking for Public Goods Funding

<https://gov.gitcoin.co/t/eth-staking-for-public-goods-funding/17534>
Jstar | 2024-02-01 18:55:19 UTC | #1

## Introduction

The utilization of ETH staking for public goods funding is heavily neglected. This proposal looks to resolve this by proposing a framework for a staking solution that enables stakers (incl. the Gitcoin treasury) to delegate their assets and pass on a % of their staking yield over to the Gitcoin Grants Program.

Depending on the structure of this solution, Gitcoin DAO approval may or may not be required, but I welcome everyone to provide their opinions/feedback to finalize the structure of this offering. This proposal uses [StakeWise](https://www.stakewise.io/), a white-label ETH staking solution that allows any entity to launch a fully comprehensive, non-custodial staking solution in a permissionless manner. Think of this as creating a public goods version of Lido, where the Gitcoin community can configure the entire solution to best suit Gitcoin’s needs. An overview of the StakeWise protocol is provided at the bottom should you wish to dive deeper.

## Gitcoin ETH Staking Solution (Example)

## ![|907x423](upload://1EvUfsAvY4NAWd0SlR91llVq8uV.png)

Gitcoin launches a Public Goods Staking Pool in partnership with node operators of its choosing. This example specifically highlights a partnership with NodeSet - a collection of 100s of Home Stakers who will stake the capital on behalf of the Pool.

The Pool’s staking fee is set to 50%, split 80/20 between Gitcoin Grants and NodeSet, and its distribution is automatically handled by the Pool smart contract. Note, the StakeWise infrastructure is free to use and consequently 100% of this staking fee is passed onto Gitcoin and the node operators. 

Gitcoin stakes its own treasury into the Pool, earning 50% of the staking yield and automatically sending the other 50% towards funding grants on its platform. As a public staking pool, anyone can delegate capital in a permissionless manner and use their ETH staking returns to contribute to public goods funding.

No development work is required by Gitcoin. The deployment of the staking pool takes minutes and Gitcoin’s operator partner(s) handles the daily staking operations. Stakers can utilize the StakeWise UI to stake and unstake.

Due to the nature of the StakeWise platform, any stakers in this pool would also be able to mint the main StakeWise liquid staking token, osETH, to access DeFi with their staked capital. Care must be taken however, as the large pool staking fee could impact staker’s ability to mint and use osETH in the long-term.

## Requested Feedback

Please provide your general feedback to this proposal. There are lots of parameters that can be configured in this solution, such as what MEV relays are used and whether the pool issues stakers with an ERC20 token or not. Most importantly though, I would like to hear your thoughts on the following 3 topics to help structure the key features of the solution:

1. Who should Gitcoin partner with as the node operators for this solution? 
This could be commercial operators, solo stakers, or a mixture of both. The NodeSet solution was used as an example as I believe it aligns with the ethos of Gitcoin and would ensure the Gitcoin ETH staking solution contributes to the decentralization of the Ethereum network.

2. What percentage of staking rewards would stakers be happy to assign to public goods funding? 
50% was used in the example, but this can range from 0% to 100%. Just bear in mind the node operators will likely also require payment for servicing the staking pool. Gitcoin is free to negotiate with node operators on their fee to make this solution as cost effective for stakers and maximize the public goods funding potential.

3. Should Gitcoin set this solution up itself or have a 3rd party, such as StakeWise, create the solution instead? If the latter, would Gitcoin be comfortable with the staking pool still being branded as Gitcoin? This is where the DAO would likely need to vote for approval.


[details="StakeWise Deep Dive"]
## StakeWise Deep Dive

StakeWise was the first non-custodial liquid staking protocol on Ethereum, live since early 2021. Launched in November 2023, the V3 upgrade white-labelled the protocol's architecture, allowing any entity to create its own fully customized staking solution in a matter of minutes and allow their stakers to access DeFi through a liquid staking token, osETH. The StakeWise V3 protocol consists of two layers:

1. **Vaults** - A comprehensive toolkit enabling anyone to launch and run their own staking pool.
2. **osETH** - Liquid staking token and single layer of fungibility across the StakeWise ecosystem.

![|1200.2649681528662x676.0366521582692](upload://fgqHT3AoVGA7j1HPa9LAT543fw6.jpeg)![|1207.544416243655x676.806671764044](upload://kvVJjVB8jAei8qztaXJEt5grUe.jpeg)
[StakeWise Docs](https://docs.stakewise.io/)
[/details]

-------------------------

owocki | 2024-02-02 15:31:16 UTC | #2

Interesting proposal.  Kind of feels like a "roll your own Octant" as a service.

The number one question on my mind is how many node operators + how much capital is interested in doing this, and how do we reach those folks?

-------------------------

thedevanshmehta | 2024-02-02 20:45:27 UTC | #3

I do believe octant is also coming onchain soon

Super interested to know about your liquid staking solutions for earning yield on eth. Do you guys use geth or a minority client ?

-------------------------

Jstar | 2024-02-05 08:17:48 UTC | #4

Great questions! 

Re node operators - ultimately, if there is capital to be staked, any node operator would be willing to get involved. It all depends on which operators Gitcoin would want to use and how much of a % cut those node operators get. I do believe that the NodeSet offering would suit very well given they are a group of 100s of solo/home stakers (many from Rocket Pool). I've spoken to them and they are keen to help.

Re attracting capital - this is where I think it is important that Gitcoin takes an active role in 'showcasing' this solution, whether or not it wants to launch it/brand it as Gitcoin. Gitcoin staking some of its treasury would be a great start and bring exposure (just like how Octant has done the same). Highlighting how much capital is raised for each Grants Program via this offering is another. I also genuinely think that capital will come from word of mouth - people sharing their plans to stake for public goods funding and others following suit. This is a pooled staking solution, allowing people to stake <32 ETH, so anyone can get involved.

-------------------------

Jstar | 2024-02-05 08:21:48 UTC | #5

[quote="thedevanshmehta, post:3, topic:17534"]
Do you guys use geth or a minority client ?
[/quote]

As the StakeWise platform allows any entity to launch their own non-custodial staking solution, it essentially creates an open marketplace for staking services. Within this marketplace, you can specifically choose to stake with operators that use minority clients, a few examples are: 
[Serenita](https://app.stakewise.io/vault/0xb36fc5e542cb4fc562a624912f55da2758998113) and [Stakesaurus](https://app.stakewise.io/vault/0x649955f4189c3921df60e25f58cb1e81070fedb0).

-------------------------

kyle | 2024-02-07 14:58:28 UTC | #6

This is great. With the rise in LRSTs, solutions like this feel like a great option ton continue to explore the landscape.

In this scenario, you mention Gitcoin may not be needed to roll this out. BUT - there may also value in us participating by staking maybe 150-250 Eth to explore the tech and take advantage of the yield generated?

A couple of questions:
1 - What is needed from Gitcoin to support this? is it just a request of marketing and some amount of Eth to participate?
2 - What timeline do you have in mind? how long does it usually take to set up something like this?
3 - Why might we do this versus just hold rEth with the Eth Gitcoin has? with a 50% fee back to the stakers, the yield will likely be pretty small compared to other options.

-------------------------

Jstar | 2024-02-08 13:29:13 UTC | #7

Thanks for such a positive response @kyle! Please see answers below to your Qs:

[quote="kyle, post:6, topic:17534"]
1 - What is needed from Gitcoin to support this? is it just a request of marketing and some amount of Eth to participate?
[/quote]

Technically nothing is needed to get the solution up and running per se, although it might struggle to attract capital unless there is support from Gitcoin itself. Marketing would be a great starting point and if Gitcoin did deploy some of its own capital then that would be a great signal for the community to get involved. Gitcoin can also decide whether it wants to deploy the solution itself or let StakeWise handle that side of things (the latter is probably simpler). Either way, it would be good to get Gitcoin's approval to include some Gitcoin related branding :)

[quote="kyle, post:6, topic:17534"]
2 - What timeline do you have in mind? how long does it usually take to set up something like this?
[/quote]

Once there is a decision on the parameters for the solution (node operators, fees, etc...), getting this set up shouldn't take any more than 1-2 days providing the node operators are familiar with the StakeWise platform (which many are). 

From that point onwards, the solution will be live and ready to accept deposits via the Gitcoin page on the StakeWise UI. Gitcoin can then decide whether it wants to offer this via its own UI and do the necessary development work there (certainly not mandatory, but could be nice if this ends up being a core driver of grants funding).

[quote="kyle, post:6, topic:17534"]
3 - Why might we do this versus just hold rEth with the Eth Gitcoin has? with a 50% fee back to the stakers, the yield will likely be pretty small compared to other options.
[/quote]

Great question - there are a few things that are worth highlighting:
* Using rETH wouldn't automate the distribution of funds (i.e. you would need to sell rETH periodically and then send the capital on to the Grants Program). This is not so much of a problem when staking the Gitcoin treasury in isolation, but if we want to get hundreds/thousands of stakers involved then it becomes problematic. Having a smart contract that automatically splits the staking rewards of all stakers makes this much more feasible. 
* Gitcoin has more control to customize its solution and brand it specifically to attract capital for public goods, without any dev lift. Don't get me wrong, the fact that rETH has a decentralized node operator set is great, but this is why I think using NodeSet could be a great fit here as it would still allow for Gitcoin to have 100s of node operators (way more decentralized than Lido for example), most of which are Rocket Pool operators anyway. 
* Another benefit is to lower Gitcoin's staking fees vs rETH (which historically have been around 13-15%) so more staking yield can be used for public goods funding. I would like to think node operators would be willing to charge more like 5-10% for a public goods funding solution like this.

On the topic of staking fees - the wording in my initial post is probably not optimal as a '50% Staking Fee' doesn't look/sound great. To be clear, this 'Fee' is what would be split between both Gitcoin Grants and the node operator(s). 50% was just a suggestion and it ultimately all depends how much of their staking yield stakers would want to pass on to Gitcoin. Maybe 50% is too high and something like 25-30% is more reasonable - it would be good to get more opinions on this area.

-------------------------
