---
id: 4717
title: "Akita Sale/Stream implementation: make it a scheduled liquidity pool!"
slug: akita-sale-stream-implementation-make-it-a-scheduled-liquidity-pool
category: governance-proposals
url: https://gov.gitcoin.co/t/akita-sale-stream-implementation-make-it-a-scheduled-liquidity-pool/4717
created_at: 2021-06-02T15:00:23.946Z
last_posted_at: 2021-06-09T12:59:15.043Z
posts_count: 10
views: 4361
like_count: 32
---

# Akita Sale/Stream implementation: make it a scheduled liquidity pool!

<https://gov.gitcoin.co/t/akita-sale-stream-implementation-make-it-a-scheduled-liquidity-pool/4717>
AvsA | 2021-06-02 15:00:24 UTC | #1


This proposal came too late to be one of the options in the *Akita, a path forward poll*, which at the moment is leading with "Sell 10%, stream 90%" and "Liquidate 100%" so I will propose it as a further discussion on the merits of how to implement it. This was posted on June 1st as a [twitter thread](https://twitter.com/avsa/status/1399892313007083522?s=21) and gathered some positive feedback from many of the community representatives.

## The issue with the two main proposals

* There's not enough market depth to liquidate all Akita tokens without losing a lot of value for Gitcoin. Even if there are serious doubts about the long term viability of the Akita community, we have a responsibility to maximize the value gained for Gitcoin.

* Locking Akita on Sablier doesn't put that capital to good use, and if the market crashes and recovers and crashes again during before the stream is over, then there was a missed opportunity.

## The Proposed Implementation

1) Sell 10% of Akita in any exchange, put it in the Gitcoin treasury

2) Sell yet another 10% into ETH.

3) Create a Scheduled Balancer pool with the 10% ETH obtained in step 2 and all the remaining Akita.

4) Set up the pool controller to programmatically change the ratio over a period P so that it inverts from a 10% ETH 90% AKITA into a 90% ETH and 10% AKITA

Those types of pools are usually called **Liquidity Bootstrapping Pools** and are often used to launch new tokens that don't have liquidity. In this case, the token has launched but it would still bootstrap the liquidity. You can read more about LBPs on this article about [Radicle](https://medium.com/balancer-protocol/radicles-new-record-lbp-sale-shows-that-lbps-are-here-to-stay-4c81e15a4d4d).

## The end result is that:

* At the end of the period, Gitcoin will have sold most of their Akita, at a fairer market price, similarly to a Dollar Cost Averaging strategy

* Akita community gets a much more liquid market, a "billion" dollars deep (emphasis on the air quotes). This will reduce the impact any single seller can have on the final price.

* All trades that are executed against this pool will earn fees for Gitcoin, so in periods of high volatility Gitcoin is leveraging its massive Akita Holdings to generate Yield

* There will be a constant sell pressure on Akita, but it's one that is scheduled and known

## Variants and Risks

Balancer Pools are quite flexible and we could do other options like having a pool that starts at 91% Akita, 3% GTC, 3% ETH and 3% DAI. Or we could add all the dog tokens into a big billion dollar pile of dog ~~poo~~ money.

Pools also don't necessarily need to be locked: we can add a smart controller so that Gitcoin DAO can accelerate the schedule at a later vote, or simply change it completely and use the **Pie DAO** so that ratios can be changed at the will of GTC holders. Also, at any point, Gitcoin could vote to take the liquidity out of its own pool and receive it in either token of the pool.

It's also important to note that **LBPs are different than just selling a token**: the pool wants to keep a constant ratio at all times to reach its target, be it 10%, 25% or 90%. So it means that *the pool will both sell and buy akita for ETH* to keep the target ratio–that's how AMMs work. A LBP changes that target ratio slowly over time, but it also is reacting to the market in real time. It means that, if akita drops to near 0, then the pool will automatically be buying akita with ETH until it reaches the desired balance, so almost ETH would be drained from the pool. But that ETH came from the Akita sale in the step 2, and the end result would be the same if the strategy was to stream or liquidate it anyway. On the other hand, if the market goes up again, that will mean the pool will start selling the cheap akita it bought back to ETH (plus the fees it got during the period) which is why pools make money from volatility.

Disclaimer: I work for Balancer labs, but if the community wants to they can use other solutions. Balancer also has a "LBP referral program" but I am perfectly willing to either not claim it or to donate the BAL gained to Gitcoin.

## Period P

This proposal leaves the P period open. The ending date of this poll is after the resolution of the "Akita - a path forward" poll so votes should take this in consideration.

1) Long stream: a LBP of duration of 2 years

2) Intermediary: make the LBP last 1 year

3) Liquidation: a short LBP over 1 week

4) LBP in another platform or other configuration

5) No LBP: just use sablier or dump it all in uniswap, depending on the results

-------------------------

ceresstation | 2021-06-02 15:29:06 UTC | #2

Thanks for writing this up @AvsA! By the way, if you haven't signed up already we'd love to have you formally as a steward :pray:

https://gov.gitcoin.co/t/introducing-stewards-governance/41

@HelloShreyas @androolloyd curious to get your thoughts on how these would intersect with your proposals!

-------------------------

linda | 2021-06-02 15:47:43 UTC | #3

Shared my thoughts on Twitter https://twitter.com/ljxie/status/1400116505581428743

> I like this approach a lot more than just liquidating or burning all of the tokens. It's up there for me along with @HelloShreyas' proposal. Definitely think it's worth putting into a formal proposal

-------------------------

lefterisjp | 2021-06-02 16:20:22 UTC | #4

I also like this proposal a lot. It is a more concrete plan on how we can sell 100% in a constructive way. With such an implementation I am also inclined to go for the sell 100% with the period being up for discussion.

https://twitter.com/LefterisJP/status/1400124946127462400

-------------------------

Mantarochen | 2021-06-02 17:42:09 UTC | #5

Here my reply from Twitter:

This approach would cause Akita to literally gain no more price increases until Gitcoins entire Akita amount is gone. It would make Akita almost a stablecoin until day X. 

As soon as all investors find out about this, they will leave the token instantly and dump the price right away.

Beside the fact that this approach would still severely damage the investment of 46,000+ holders who are not willing to start Daytrading EVEN if this idea worked... It would obviously dump Gitcoins Akitatokens as well instantly.

TL;DR it would not work anyways. The news would spread fast. The entire community already knows about Gitcoin and the current process of finalizing a decision.

-------------------------

Klemah | 2021-06-02 19:15:50 UTC | #6

Hello!

I am the lead dev for the AKITA community. I'd like to speak on behalf of my dear colleagues and all the members of our community who put their trust in us.

[quote="AvsA, post:1, topic:4717"]
Locking Akita on Sablier doesn’t put that capital to good use, and if the market crashes and recovers and crashes again during before the stream is over, then there was a missed opportunity.
[/quote]

I could not disagree with this more. You seem to completely forget about the fact that the market could also go up, increasing Gitcoin's gains significantly. AKITA has seen a big increase in price (20x +) twice in just five months. We are working hard on releasing products for AKITA, which are expected to go live at the beginning of July. I expect those releases to increase the price of AKITA again over the next months and years.

Although the sablier proposal is not the one we wanted originally and we still think other options are better (like Relic's proposal or Vitalik's original proposal), we are ready to accept a compromise there.

The reason why is because the sablier option does not kill our project.

Unless I misunderstood something - the scheduled balancer would kill AKITA. Just like @Mantarochen explained in his answer above, people will start selling as soon as news of this becomes public.

**This is bad for AKITA** - for obvious reasons. It might seem like a meme coin to you, but to us, it's a family of 45,000 holders.  It has been our lives for the past few months. This proposal would hurt all holders, many of whom would lose all their investments. We never asked to be a part of this and would like to seek a more peaceful solution.

**This is also bad for Gitcoin** - I understand your goal is to try to take as much money from our project as possible. I do not like it one bit - no point pretending I do. We find it extremely unfair. **SHIB's tokens were burned - why not ours?**

I can however put myself in your shoes, and I do not understand why you would go ahead with this proposal.
You would get a moderate sum of money from the initial sell - just like with @HelloShreyas's proposal - **but contrary to his proposal, yours just will not bring any money to Gitcoin whatsoever after that initial sell.**

---

Let me elaborate on this last point.

In the AKITA community, we have a pledge of trust, honesty and openness. We are open about everything we do, and always let the community know about where we are going.
**This means we will be honest with the community about the future of the coin.**

After a proposal is decided on, we will be issuing an official announcement in all our groups, letting people know about the decision that was made.

Try to put yourself in an AKITA holder's shoes. He or she will read something like this:

*If AKITA's value increases, a whale will automatically sell until it gets back to its old price. However, if AKITA's value decreases, the whale will certainly not buy to get it back to its old price.*

How could an investor not sell after reading this? This is a stablecoin but without the benefits of stability. **It will just never increase in value.**

**AKITA investors will dump massively if such a proposal were to pass.**

It would kill the AKITA project. The team is strong, and I trust we would be able to move on to another project together.

What worries me more is the 45,000 holders of our token who would lose a lot of their money for some and all of their money for most.

It would not give much money to Gitcoin either. I bet your scheduled liquidity pool will wait a long time with its trillions of AKITA tokens, waiting for the token, now dead, to go back up in value, which it never will.

---

I sincerely hope you will consider the concern I share with this message. This concern is shared by the whole AKITA team.

The AKITA community supports @HelloShreyas's proposal.

-------------------------

Velucxa | 2021-06-04 09:00:11 UTC | #7

This thread special for Akita Inu or other Akita?

-------------------------

ceresstation | 2021-06-07 00:30:46 UTC | #8

Now that we have a final decision to sell all of the AKITA the community holds, @AvsA I'd like to ask that you and @androolloyd try to take some time to put together the details of how the LBP will work.

Similar to what was mentioned on Twitter, I think a buyback program is the most sensible way to frame this, and with that framing in mind I think we should consider offering some good faith measures in how we sell such that price isn't crushed and True Akita Believers TM can participate in taking the project to where the core team ostensibly wants it to be.

Some options:

- Let Akita supply liquidity to the LBP and we will give them equivalent tokens to double what they provide in good faith (facilitates selling)
 
- Set a discount to market such that participants who help us help themselves 

- Offer some kind of intangible olive branch to any devs in their community to get involved in and educated on Ethereum cc @austingriffith 

Would love to hear any thoughts / feedback on whether these could be part of how participation in the LBP works!

-------------------------

FABSCO | 2021-06-07 09:17:54 UTC | #9

AGRRED, 100%. Whatever i get free , i should use it for for the betterment of those people who are the owner. not to destroy them.

-------------------------

AvsA | 2021-06-09 12:59:59 UTC | #10

[quote="Klemah, post:6, topic:4717"]
If AKITA’s value increases, a whale will automatically sell until it gets back to its old price. However, if AKITA’s value decreases, the whale will certainly not buy to get it back to its old price.
[/quote]

Just wanted to reply to @klemah's point here: this is the opposite of how a pool works. If the pool 90:10 pool has 1 million dollars in ether and 9 million in Akita, it means that if Akita starts going down, the pool will start buying Akita until the equilibrium is back at 9:1. In other words, a pool that has 1 million in the other token is one that is willing to use all that money to buy Akita as it drops down, and if Akita goes to 0 then so will the ether side.

That's the main difference between a smart pool and a stream: the latter only sells, while the former sells and buys.

-------------------------
