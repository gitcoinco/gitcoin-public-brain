---
id: 4255
title: "[Proposal - Akita] Liquidate AKITA for ETH"
slug: proposal-akita-liquidate-akita-for-eth
category: governance-proposals
url: https://gov.gitcoin.co/t/proposal-akita-liquidate-akita-for-eth/4255
created_at: 2021-05-30T21:28:15.490Z
last_posted_at: 2021-06-07T19:05:34.544Z
posts_count: 11
views: 4891
like_count: 13
---

# [Proposal - Akita] Liquidate AKITA for ETH

<https://gov.gitcoin.co/t/proposal-akita-liquidate-akita-for-eth/4255>
androolloyd | 2021-06-11 13:05:14 UTC | #1

I propose that we liquidate the Akita for ETH and look towards the DeFi Treasury Mgmt Workstream to better ascertain how we utilize the underlying capital.

How the ETH is used is not apart of this proposal.

=========================================

# Proposal Update #2 

After some conversations with the Akita community it has become clear that the best path to maximize our ETH outcome is to enable some form of participation with them.

Highlights:

There will be a buy back and burn program that funds the AKITA LBP, for every 1 akita purchased X will be burned(economics still being finalized). 

The ETH raised here will be put into the LBP with a time of completion set for 3 months.

Based on our conversations I propose the following:

Option 1:

We split the LP Tokens as follows:
40% to Gitcoin
40% to Akita (streamed over the length of the LBP through Sablier)
20% to a Charity (yet to be chosen) funds ETH raised will be delivered VIA Gitcoin, post sale.


Option 2: 

We split the LP Tokens as follows:
80% to Gitcoin
20% to a Charity (yet to be chosen) funds ETH raised will be delivered VIA Gitcoin, post sale.

Option 3:

We don't split the LP Tokens

We agree to burn more Akita via Sablier by streaming to the 0x000 address Y tokens for each X Akita in the LBP.

Without a serious burn or a share of the ETH being raised, AKITA is most likely to dump their token or fork us out entirely. 


[Snapshot vote](https://snapshot.org/#/gitcoindao.eth/proposal/QmQe6fHVDsvE91ShNagvFojetuWHu6xKn7izk46Dg2cQmK)


# Proposal Update #1

After today's [Spaces call](https://twitter.com/makoto_inoue/status/1400040076151771139) to discuss some of the proposals and based on some comments by [Alex Van de Sande](https://twitter.com/avsa/status/1399892313007083522)

With the help of [James Hancock](https://twitter.com/JHancock) we have adjusted my proposal to include a high level overview of the means by which the $AKITA would be liquidated to ETH. 

This process will be carried out by the DeFi Treasury Mgmt Workstream for ratification by the multi sig signers. 

## The what:

A balancer smart pool will be created that is setup to supply the $AKITA:ETH

**Better for Gitcoin**

*  more likely to get more capital for public goods. To liquidate now would get a ceiling of 2 million, done overtime in a less harsh matter is more likely to get more out of those tokens. 
* avoids negative PR around dumping a project 

**Better for the Akita Community**
- Day 1 nothing changes 
- It is usable liquidity for the duration of the pool. 
- Predictable: The Akita community will know predictability what is happening mitigating fears of the unknown. Discouraging a "run on the bank" of akita to get out before Gitcoin does. 



**Things to work out after the proposal.** 
* How to handle exposure to the token over the entire period. 
* Is it worth withdrawing the pair token, or building a Smart pool with some custom ability to handle this. 
* It would be best to avoid complete collapse if Akita went to zero in the middle of the transition.


At a ratio of 0.1%:99.9% ETH/AKITA shifting the weight linearly over time to 99.9%ETH/0.1% AKITA



[Snapshot Poll](https://snapshot.org/#/gitcoindao.eth/proposal/QmeGrN1bxYyt3RGqLkJL6v8XLpz3W2FyYSmpZxAiCxhF2m)

-------------------------

defidefidefi | 2021-05-31 03:28:30 UTC | #2

Also we should do this asap because AKITA is losing value and is probably going to zero.

-------------------------

lefterisjp | 2021-06-01 13:53:03 UTC | #3

I agree with the spirit, but I can't see how we can implement it in a way that makes sense. That's why I think the proposal to liquidate 10% and then slowly the other 90% over 2 years makes more sense: https://gov.gitcoin.co/t/proposal-akita-sell-10-akita-place-90-akita-in-2-year-sablier-contract/1663/17

-------------------------

Tevinprime | 2021-06-01 14:00:12 UTC | #4

Akita to the moon just like shiba inu to the moon

-------------------------

defidefidefi | 2021-06-02 11:24:29 UTC | #5

There will be no AKITA in 2 years

-------------------------

Pop | 2021-06-02 21:30:38 UTC | #6

I am up for this but with Balancer Pool over 1 year - you can't really start it at 0.1% so maybe sell 15% of the Akita - Send 10% to treasury, 5% to start a 95/5 pool

-------------------------

Alexang | 2021-06-03 08:20:08 UTC | #7

With the brilliant minds in Gitcoin, this is the best solution?

-------------------------

Toby | 2021-06-04 18:18:10 UTC | #8

This is getting popular in the rollup Snapshot poll of options, and I personally am favoring this proposal. I don't fancy gitcoin continuing to deal with this controversy over the next two years and I think it's important for us to set a better precedent than taking speculative positions on any tokens that happen to be sent to the multisig. **It seems like people who are voting for this are favoring the option to *dispose* of 100% of the tokens while capturing some of the value, in the shortest possible time**

However, if what Scott said in the other thread is true, it sounds like "dispose of 100% while capturing some value" would require us to still integrate some of the other proposal options. Correct me if I'm wrong here.

Scott says:
>  there doesn’t appear to be an efficient way to sell more than 10% even using a variety of methods due to liquidity constraints. So in some sense if you believe the community should vote to sell, for short term purposes (say in the next 3-6 months) a proposal to sell 10% is equivalent to a proposal to sell 100% just without removing the potential for future disposition.

As discussed in [that other thread](https://gov.gitcoin.co/t/snapshot-proposal-akita-tokens-a-path-forward/4462/8) it would be beneficial if we could talk through exactly how this liquidation happens. 

If it's only possible to liquidate 10% immediately, then what about using Simona's proposal to put the rest in a 5/95 pool and simply leave it? I'm looking for more specificity on how we accomplish this to give this proposal more credibility.

-------------------------

Cryptoguy | 2021-06-05 13:07:07 UTC | #9

It's amazing to see the lack of empathy for destroying an entire community while hiding behind the guise of "funding public goods". So apparently only the public goods deemed worthy by gitcoins leaders are what matters. You're in essence going to rug pull a very large community just to better help your own needs. Why would it not make more sense to help the community that allowed you to even receive these funds? Without the strength of the community that was built around Akita, those tokens would be worthless. So you're going to crush a community just to add liquidity to your guys projects. Seems like exactly the opposite thing you guys are trying to stand for. I can only see this negatively rippling through Gitcoins future and forever tarnishing your reputation. Gitcoin will fall just as rapidly as you will crush Akita. Eye for an eye as they say. 

Great job mates.

Cheers

-------------------------

vogue20033 | 2021-06-06 02:53:39 UTC | #10

Much more better to liquidate all at once.

-------------------------

KriptoHayat | 2021-06-07 19:05:34 UTC | #11

this is the best choice. Let 's do it

-------------------------
