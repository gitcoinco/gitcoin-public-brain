---
id: 10725
title: "Improve GTC Liquidity with Tokemak"
slug: improve-gtc-liquidity-with-tokemak
category: governancevision
url: https://gov.gitcoin.co/t/improve-gtc-liquidity-with-tokemak/10725
created_at: 2022-05-26T17:26:33.978Z
last_posted_at: 2025-08-10T07:33:26.382Z
posts_count: 14
views: 5820
like_count: 33
---

# Improve GTC Liquidity with Tokemak

<https://gov.gitcoin.co/t/improve-gtc-liquidity-with-tokemak/10725>
schlabach | 2022-06-04 11:18:32 UTC | #1

Authors: @schlabach, @HelloShreyas from [Llama](http://llama.xyz)

## Gitcoin’s Current Liquidity Situation

Gitcoin’s current volume is around $5m/day, mostly on off-chain CEXs (most notably Binance) [1]. At the time of writing, there is $680k (GTC @ $2.64) worth of TVL in the [Uniswap v3 pool](https://info.uniswap.org/#/tokens/0xde30da39c46104798bb5aa3fe8b9e0e1f348163f). Gitcoin does not pay liquidity mining rewards.

## Overview of Tokemak

Tokemak is a novel protocol designed to generate deep, sustainable liquidity for DeFi and future tokenized applications that will arise throughout the growth and evolution of web3.

An example of how Gitcoin can use a Tokemak reactor:

* Gitcoin creates a Tokemak reactor.
* Gitcoin deposits GTC in the reactor in exchange for tGTC.
  * This tGTC can only be withdrawn at the end of the cycle [2]. However, smaller depositors in the pool will be able to swap tGTC for regular GTC at any time on a normal DEX (assuming a liquidity pool is created).
* Gitcoin will earn TOKE, which it can stake and then use to 1) direct TOKE rewards to the pool and 2) direct GTC liquidity to different exchanges.
* Other TOKE holders (Liquidity Directors) are incentivized to direct GTC liquidity to the appropriate exchanges.

![image|690x286](upload://uO1TZyDzUdPJjlZnHIRR5qDqU1H.png)

@Willy and @kyle had a [discussion](https://gov.gitcoin.co/t/discussion-securing-a-gtc-token-reactor/9976) in March exploring setting up a Tokemak reactor. We would like to take this discussion to the next stage of execution.

### Benefits of Gitcoin using Tokemak:
* Provide liquidity for GTC
  * Gitcoin can ensure that GTC has plenty of liquidity without relying on any costly liquidity mining incentives.
  * No need to provide USDC or ETH (as those come from Tokemak).
  * Allow GTC holders to become LPs without having to manage a complex LP position or take on risk of impermanent loss. [3]
  * Sustainable, deep liquidity (avoid mercenary capital).
  * Platform/DEX agnostic; Tokemak sits above the exchange layer and can seamlessly route liquidity wherever it’s needed.
* Earn revenue for the DAO
  * Gitcoin DAO will earn TOKE rewards, which they can either sell or use to direct liquidity on Tokemak. As the Tokemak protocol becomes more widely used, it will have a large treasury of [Protocol Controlled Assets](https://docs.tokemak.xyz/protocol-information/key-terminology), making it strategically valuable to hold TOKE.
  * Allows Gitcoin to take advantage of its un-utilized GTC
* Allow the Gitcoin team & community to focus on their core competencies instead of managing GTC liquidity on DEXs
* Philosophically, it would be best for Gitcoin (with its focus on driving public goods) to have liquidity for its token available on-chain as opposed to on CEXs.

### Process of setting up a token reactor
Gitcoin will need to enter and win a token reactor through Tokemak’s [Collateralization of Reactors Event (C.o.R.E)](https://www.tokemak.xyz/core). In a C.o.R.E., different DeFi projects compete with one another to secure one of five token reactors. The projects with the most TOKE votes are rewarded with a reactor for their token.

In C.o.R.E. 2, there were 45 candidates and 5 were selected, so the process is competitive. C.o.R.E. 3 saw 5/52 candidates selected for reactors. Even well-recognized names like Aave and Curve did not win reactors in the last two C.o.R.E.s.

In the last C.o.R.E., Gitcoin would have needed 6,717,153.36 votes to win (if the original LUNA vote is counted). Voting power is different depending on which token is used:

* 1 liquid staked TOKE = 6 votes
* 1 staked LP token = 69 votes
* 1 locked (vesting) TOKE = 1 vote

Tokemak’s introduction of the vote-locked token model might make it more difficult to win a reactor, as token holders may lock their tokens in exchange for boosted voting power.

We can also improve Gitcoin’s odds by bribing voters on [Hidden Hand](https://hiddenhand.finance/tokemak), though it can be quite expensive to purchase votes, and there’s no guarantee that we’d win.

![image|690x248](upload://oVWH7KYo1aXUGMpkwwPWqfjNkdW.jpeg)


C.o.R.E.s last 1 week. The next C.o.R.E., C.o.R.E. 4 will begin in the next ~1.5 months.

While it will be challenging to secure a reactor through C.o.R.E., winning a reactor would be hugely beneficial to Gitcoin and the liquidity of GTC. 

Llama will work to secure a reactor by advocating on behalf of Gitcoin, securing votes for the GTC reactor, managing any technical requirements needed to enter C.o.R.E. or spin up a reactor, and evaluating any terms of using Tokemak (e.g. a mutual grant for TOKE).

### Ongoing Maintenance

Once Gitcoin has won a reactor, Gitcoin will need to deposit GTC into the reactor. There won’t be ongoing maintenance (other than directing liquidity with TOKE, which Llama can handle, or selling earned TOKE).

## About Llama

Llama is building economic infrastructure for DAOs. We have worked with some of the leading DAOs, including Aave, Uniswap, dYdX, Gitcoin, Radicle, PoolTogether, FWB, Harvest Finance, and Fei Protocol, among others. Llama has implemented on-chain proposals, constructed treasury strategies, designed liquidity incentive programs and on-chain indices, and built analytics dashboards and financial reports. Llama’s 45 contributors are among the most active in the DeFi and DAO ecosystem and include engineers, DeFi strategists, data analysts, quants, and accountants.

---

*[1] - Source: [CoinGecko](https://www.coingecko.com/en/coins/gitcoin)*
*[2] - [Cycles](https://docs.tokemak.xyz/protocol-information/cycles) now last 7 days, ending every Wednesday.*
*[3] - Read more on Tokemak’s approach to impermanent loss [here](https://docs.tokemak.xyz/mechanics-and-functionality/guardrails-and-impermanent-loss-mitigation).*

-------------------------

kyle | 2022-05-26 18:32:32 UTC | #2

Yasss!

I am a big fan of this and would love to see us explore this for the CoRE4 season. We (a couple of the Tokemak leaders and I) tried to get this together for CoRE3 but couldn't pull it off in a way that respected the desire to bring the community along with us.

This is a great overview on how token reactors work, and as mentioned you can read up on some of the ELI5 questions I had [here](https://gov.gitcoin.co/t/discussion-securing-a-gtc-token-reactor/9976). I love the idea of Llama helping us direct the TOKE tokens (in both votes and treasury management).

I could see us contributing the max amount of GTC ($1-$5M worth) to the reactor to deepen liquidity, but also offer a larger sum to generate swap fees. We have a pretty active pool and so there are opportunities to harvest from the swap fees. 

Huge thanks to Llama for leading here and helping us partner with the folks at Tokemak. The tokemech pilots are great and I am interested in getting closer to that community!

-------------------------

Lunacat | 2022-05-27 13:38:36 UTC | #3

Fantastic proposal!  This is first I've learned of Tokemak and looking into it more.  But just curious -- @schlabach how would you assess trade-offs of setting up a token reactor against leveraging something like Fei's [liquidity-as-a-service](https://medium.com/fei-protocol/if-you-are-part-of-a-dao-or-protocol-that-wants-to-create-liquidity-for-your-token-without-f49a01f02863)?

One other thought -- it would be fantastic if there was a way for contributors and stewards to be able to add liquidity to the pool/reactor without sacrificing their governance rights.  Just a separate consideration in broader context of [DAO Compensation Stability thread](https://gov.gitcoin.co/t/dao-compensation-sustainability/10604/8?u=lunacat).

-------------------------

schlabach | 2022-05-27 18:05:38 UTC | #4

Hi @Lunacat - thanks for the question.

There are a few ways to think about the tradeoffs. [This article](https://medium.com/fei-protocol/new-approaches-to-liquidity-in-defi-624f2e50937b) does a nice job of encapsulating the differences, and it includes this chart:
![image|690x381, 75%](upload://cQU8Bt10O1u8nEWykWtwUuTlAFO.png)

I would note that, while the Tokemak option doesn't allow Gitcoin to earn trading fees directly from the liquidity pools, it *does* allow Gitcoin to earn revenue through the form of TOKE; arguably this is better than simple LP fee revenue as it has the ability to direct TOKE rewards to Gitcoin reactors/direct GTC liquidity and has governance power over the Tokemak protocol.

I think one of the most important benefits of the Tokemak model is the impermanent loss (IL) protection it provides, which LaaS does not. There are a couple of llamas who are active in PoolTogether's treasury group, which ran LaaS; PT did end up suffering from IL and had to bear those costs as part of the program. You can read more about that on [PoolTogether's forum](https://gov.pooltogether.com/t/ptip-68-otc-settlement-for-ondo-fei-laas-program/2164).

You can read more about Tokemak's impermanent loss protection [here](https://docs.tokemak.xyz/mechanics-and-functionality/guardrails-and-impermanent-loss-mitigation).

On your second point, I agree; we can do more work on the feasibility of this from the technical side, but this would require GitcoinDAO's governance framework to allow voting from both GTC as well as tGTC.

-------------------------

kyle | 2022-05-27 19:32:46 UTC | #5

[quote="Lunacat, post:3, topic:10725"]
One other thought – it would be fantastic if there was a way for contributors and stewards to be able to add liquidity to the pool/reactor without sacrificing their governance rights. Just a separate consideration in broader context of [DAO Compensation Stability thread](https://gov.gitcoin.co/t/dao-compensation-sustainability/10604/8).
[/quote]

The governor we use looks at GTC in LPs (on Uni and Balancer today) - its a nifty voting strategy that Snapshot supports at least. I suspect this is straight forward to extend to a Token Reactor too (once it's set up).

-------------------------

Lunacat | 2022-06-02 22:43:01 UTC | #6

Thank you both for replies, @schlabach and @kyle !  Agreed that impermanent loss is strong selling point for Tokemak, although there are clear tradeoffs with Fei's use of matching in setting up LaaS pools.  If Tokemak is more naturally suited to address some of the governance rights ideas that have sprouted, that is also a big selling point, imo.  

Bumping overall discussion to see if any others chime in :slightly_smiling_face:

-------------------------

schlabach | 2022-06-03 14:20:06 UTC | #7

Hey @Lunacat - can you say a little more about this? Want to make sure I'm understanding your point properly. For both Tokemak/LaaS, the pair assets (ETH/stables) would be provided by another party (either Tokemak LPs or Fei).

> although there are clear tradeoffs with Fei’s use of matching in setting up LaaS pools

-------------------------

Lunacat | 2022-06-03 20:59:59 UTC | #8

Looks like i misread Tokemak's documentation - I had thought that pools would be with TOKE, not a stable/eth.  I do have reservations on how Tokemak is able to source that stable liquidity to support new pairs, and how sustainable that process may be.  Fei having direct control over its own stable is a strong selling point, imo, and inherently reduces operational risk.  But I am still familiarizing myself with Tokemak and do not want to give impression of endorsing one over the other at this point.

-------------------------

keneeze.eth | 2022-06-06 12:09:27 UTC | #9

I am in support of this initiative!

Token liquidity is very important for any project that has a token, considering the good work that Gitcoin is doing, leveraging Tokenmak, Gitcoin will be able to build deep liquidity for the token, I advise that the treasury management team look into this as soon as possible.
It is important to note that upon further research, Tokenmak may not be the best protocol for Gitcoin DAO to start building deep liquidity with, but definitely this is a starting point for much deeper research and analysis.
However in the search for liquidity it is important for the Gitcoin team to decide on these two things before seeking to build deeper liquidity.

1. How much is Gitcoin willing to pay for liquidity? I believe this answer will determine the protocol that Gitcoin would partner with, and the strategy that will be used for capturing this liquidity.

2. How much liquidity does Gitcoin really need? Being able to Cap the Total Value needed on any protocol chosen for liquidity building is important, by defining a target the team will have definite goals that ensure that Gitcoin does not end up overpaying for more liquidity that the GTC token needs.

keneeze.eth 🔥_🌱 (Wildfire, Public Goods Operator)

-------------------------

schlabach | 2022-06-14 22:25:54 UTC | #10

Hi everyone, just to provide a quick update here:

We've spoken with the Tokemak team and have confirmed that GTC will be entered into the upcoming C.o.R.E. 4. There are no updates on timing of C.o.R.E. 4 at the moment, but we expect it to come within the next 1-2 months.

-------------------------

epowell101 | 2022-07-01 21:31:20 UTC | #11

Is there anything we can do as small holders & friends to be helpful?

-------------------------

schlabach | 2022-07-02 00:11:27 UTC | #12

Nothing immediate for now other than voting for Gitcoin in C.o.R.E. 4 and wrangling as many votes as you can!

-------------------------

shin-malphur37 | 2025-08-10 07:31:26 UTC | #13

Very interesting and i will definitely 🙂 do an in depth lok into this protocol.

-------------------------

shin-malphur37 | 2025-08-10 07:33:26 UTC | #14

Did the documentation get moved to a new link?

-------------------------
