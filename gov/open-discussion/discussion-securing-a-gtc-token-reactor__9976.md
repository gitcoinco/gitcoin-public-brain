---
id: 9976
title: "Discussion: Securing a GTC Token Reactor"
slug: discussion-securing-a-gtc-token-reactor
category: open-discussion
url: https://gov.gitcoin.co/t/discussion-securing-a-gtc-token-reactor/9976
created_at: 2022-03-01T05:44:10.550Z
last_posted_at: 2022-04-08T20:04:32.128Z
posts_count: 3
views: 3003
like_count: 2
---

# Discussion: Securing a GTC Token Reactor

<https://gov.gitcoin.co/t/discussion-securing-a-gtc-token-reactor/9976>
Willy | 2022-05-28 15:40:54 UTC | #1

The goal of this thread is to introduce the concept of [Tokemak](https://tokemak.xyz)'s token reactors and to discuss the merit of campaigning for a GTC Reactor in the next election, dubbed C.o.R.E.3 (Collateralization of Reactors).

If you're not familiar with Tokemak, I encourage you to read this [Introduction](https://docs.tokemak.xyz/). The tl;dr is that Tokemak is a novel protocol designed to generate deep, sustainable liquidity for tokens. Token holders deposit Tokens in exchange for tTokens and earn TOKE. TOKE holders can then stake their TOKE to direct staked liquidity, both by voting on which reactors to allocate TOKE rewards to as well as which DEXs to LP the tokens staked in reactors. 

![image|690x218](upload://koQ3v7nhRfqas18TCYlQozrqiEC.png)

This provides 2 major benefits to tokens:
1. deeper liquidity on DEXs without liquidity mining
2. yield for token stakers

Furthermore, the DAO can stake tokens from its own treasury to earn TOKE rewards. ShapeShift DAO (where I spend most of my time) was fortunate enough to secure a FOX Token Reactor in C.o.R.E.2, and subsequently staked 50M FOX from its treasury. We're so happy with our reactor, we're now working on a new contract, [FOXy](https://forum.shapeshift.com/t/bounty-120-000-300-000-fox-for-foxy-aka-sfox-by-mar-22nd/984), which evolves traditional staking contracts that share DAO or protocol revenues with token stakers (ie. xSUSHI) by depositing FOX staked in the FOXy contract into the tokemak reactor to both boost yield while also enabling otherwise idle tokens to be put to work to deepen liquidity. If Gitcoin secures a reactor and is interested, we'd be happy to help you deploy your own GTCy.

Token Reactors are pretty cool, and as a result the demand for them is strong. In CoRE2, 45 projects entered, but only the top 5 projects with the most TOKE votes left with token reactors. The details of CoRE3 haven't been announced yet, but if anything I expect it to be even more competitive now that more projects caught wind. In a world of lengthy governance cycles and juggling priorities, being prepared is a huge advantage.

Things to consider:
Does Gitcoin DAO want to secure a token reactor?
If no, we can end the convo here :)
If yes...
Should we give everyone who votes for GTC a sweet poap? (this one is a no-brainer)
Should Gitcoin DAO allocate GTC from the treasury as a bribe using [votemak.com](https://votemak.com/)?
Should @owocki write a letter to the Tokemak community like [Erik Voorhees did](https://twitter.com/ErikVoorhees/status/1458825043283111949?s=20&t=D5HLGYsqw-bXKyZ-q7vhhA)? 
What other creative ideas can we come up with to secure the bag? 

Excited to hear your thoughts

Details on the last CoRE:
[CoRE2](https://medium.com/tokemak/c-o-r-e-2-begins-tuesday-november-9th-f52ca43f0770)
[CoRE2 Conclusion](https://medium.com/tokemak/c-o-r-e-2-conclusion-introducing-the-second-round-of-reactors-e38b207f2e0)

-------------------------

kyle | 2022-04-07 19:40:31 UTC | #2

@Willy - Thanks a bunch for he thoughts here! I would love to understand a bit more, but I likely need an ELI5.

[quote="Willy, post:1, topic:9976"]
Tokemak is a novel protocol designed to generate deep, sustainable liquidity for tokens.
[/quote]
This sounds great and like something every project is likely looking for!

[quote="Willy, post:1, topic:9976"]
Token holders deposit Tokens in exchange for tTokens and earn TOKE. TOKE holders can then stake their TOKE to direct staked liquidity, both by voting on which reactors to allocate TOKE rewards to as well as which DEXs to LP the tokens staked in reactors.
[/quote]
- Can you break this part down more? Let's use GTC in this example. So people trade GTC for tGTC and then can stake that tGTC into a staking pool that returns TOKE?  
- Can tGTC be unwrapped for GTC any time? 
- Are tGTC holders relying on the TOKE price to increase?
-- ie, TOKE has value as more people want to create Token reactors, and that drives up the price of the yield token tGTC holders are farming for?

[quote="Willy, post:1, topic:9976"]
deeper liquidity on DEXs without liquidity mining
[/quote]
Can you also explain how this work?

- I can imagine that this mechanism creates an incentive for people to stake their tokens in the reactor instead of market selling, but does it actually **increase** liquidity in a DEX somehow?

I want to note this from the tokemak's site:

> *Liquidity Directors* stake TOKE into individual Token Reactors and vote how that liquidity gets paired from the Genesis Pools and to what exchange venue it gets directed. They too earn yield in the form of TOKE.

Playing devils advocate, what happens if people move on from token reactors and decide they don't really care or need to create one with Tokemak, or lose interest in directing the the liquidity? Does the demand for TOKE dry up and then subsequently the yield (in TOKE from the staked tGTC... from staking GTC) become worthless?

This kind of feels like a ponzi a bit where we want to create fomo in the reactors, to keep demand high of TOKE so that our staked tGTC continues to have value. I feel like I am missing the points on "deep liquidity" and how that works though.

Thanks again so much for the outline here! I love the conversation and discussion.

-------------------------

Willy | 2022-04-08 20:05:50 UTC | #3

> * Can you break this part down more? Let’s use GTC in this example. So people trade GTC for tGTC and then can stake that tGTC into a staking pool that returns TOKE?

Basically GTC holders can stake GTC to receive tGTC 1:1. No additional staking step required to start earning TOKE (and notably, gas cost for staking is relatively cheap)

> * Can tGTC be unwrapped for GTC any time?

You can only withdraw at the end of the cycle, but as a result of getting a reactor, TOKE holders can vote to allocate staked GTC to a tGTC/GTC curve pool, enabling instant withdrawals for a small fee.

> * Are tGTC holders relying on the TOKE price to increase? – ie, TOKE has value as more people want to create Token reactors, and that drives up the price of the yield token tGTC holders are farming for?

If the TOKE price goes down, then the reactor is definitely less valuable, and vice versa. If TOKE achieves their vision of disrupting/replacing liquidity mining, that should create sustainable demand for TOKE, but TBD ofc.

> * I can imagine that this mechanism creates an incentive for people to stake their tokens in the reactor instead of market selling, but does it actually **increase** liquidity in a DEX somehow?

This is what makes tokemak so cool! TOKE holders can vote on which DEX to deploy tokens staked in reactors. ETH or Stables from the other reactors are paired with GTC to LP. Here's an example of what this looks like currently for the FOX reactor:

![image|690x316](upload://1FGuVpHOClPJFO2J5E4fOpdZZoz.png)


Thanks for the questions! Hope these answers help, please keep the good q's comin!

-------------------------
