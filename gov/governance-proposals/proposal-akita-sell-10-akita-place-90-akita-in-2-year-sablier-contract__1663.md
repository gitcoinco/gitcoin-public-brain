---
id: 1663
title: "[Proposal - Akita] Sell 10% AKITA & Place 90% AKITA in 2-year Sablier Contract"
slug: proposal-akita-sell-10-akita-place-90-akita-in-2-year-sablier-contract
category: governance-proposals
url: https://gov.gitcoin.co/t/proposal-akita-sell-10-akita-place-90-akita-in-2-year-sablier-contract/1663
created_at: 2021-05-26T02:47:15.652Z
last_posted_at: 2021-11-29T11:17:56.586Z
posts_count: 33
views: 9143
like_count: 87
---

# [Proposal - Akita] Sell 10% AKITA & Place 90% AKITA in 2-year Sablier Contract

<https://gov.gitcoin.co/t/proposal-akita-sell-10-akita-place-90-akita-in-2-year-sablier-contract/1663>
HelloShreyas | 2021-05-27 16:36:00 UTC | #1

Authored by @HelloShreyas, @ajbeal, and @AcceleratedCapital from [Llama](https://twitter.com/llamacommunity_), which provides treasury management as a service to DAOs.

**Summary**

We propose that Gitcoin **sell 10% of its AKITA balance and place 90% of its AKITA balance in a Sablier contract unlocked over 2 years**.

* Sell 10% of AKITA balance
  * Sell 7% of AKITA balance via a market maker. This is 3.5 trillion AKITA worth $9m.
  * Sell 3% of AKITA balance via Gnosis Auctions. This is 1.5 trillion AKITA worth $4m.

* Allocate 90% of AKITA balance to Sablier contract unlocked over 2 years
  * 45% of AKITA balance will be unlocked to Gitcoin’s treasury over 2 years to fund quadratic rounds. This is 22.2 trillion AKITA worth $59m.
  * 45% of AKITA balance will be unlocked to AKITA’s treasury over 2 years fund AKITA development or public goods. This is 22.2 trillion AKITA worth $59m.

This proposal is inspired by Vitalik’s [recommendation](https://gov.gitcoin.co/t/discussion-what-should-the-gitcoin-community-multisig-do-with-the-donated-akita/67/126). We want this donation to fund important public goods and support the development of both Gitcoin and AKITA.

*Note that dollar amounts stated are as of May 26, 2021.*

**Abstract**

Gitcoin’s [treasury](https://etherscan.io/address/0xde21F729137C5Af1b01d73aF1dC21eFfa2B8a0d6) currently has about $131m worth AKITA or 49 trillion AKITA tokens. This is about half of AKITA’s total circulating supply. This proposal provides practical next steps for how Gitcoin should deal with the AKITA donation.

![|597x232](upload://mf78Iz2Rjxv07A6zQxMlH9zQjhl.png)

AKITA’s total liquidity on [Uniswap](https://v2.info.uniswap.org/token/0x3301ee63fb29f863f2333bd4466acb46cd8323e6) is $2.5m. AKITA is not listed on many exchanges, which makes a liquidation difficult. We have had conversations with teams from [Wintermute](https://www.wintermute.com/) (market maker) and Gnosis Auctions to evaluate a realistic amount we can sell. Despite this, given current market conditions, we might be able to sell less than what we plan or take longer to execute it.

The AKITA donation is substantial. We cannot decide everything now so have decided to take a piecemeal approach. We want to maximize the value of the donation to further Gitcoin’s goal of funding public goods. We also want to avoid causing significant harm to AKITA’s project. Based on these goals, we recommend placing 90% of the AKITA donation in a 2-year Sablier contract that helps fund critical development that the Gitcoin and AKITA communities independently deem valuable.

**I. a) Sell 7% of AKITA Balance via Market Maker**

We recommend selling 7% of the AKITA balance via a market maker. The market maker will sell AKITA via exchanges and attempt to get the best execution for Gitcoin. They will also try to sell tokens via OTC but OTC buyers are unlikely.

We recommend using [Wintermute](https://www.wintermute.com/) as the market maker. Wintermute has been effective with the sale of SHIB tokens donated by Vitalik to the [CryptoRelief](https://cryptorelief.in/) fund. They have sold $140m worth SHIB so far. Unlike SHIB, AKITA is not listed on many exchanges and is far more illiquid so we cannot expect similar outcomes.

**Benefits**

* Quick execution with an effective market maker
* Tried and tested method

**Drawbacks**

* Not trustless: we will have to transfer AKITA to market maker to execute the trade
* Market maker will charge a fee, whereas Gnosis Auctions is free

**Implementation**

* KYC for Gitcoin multisig wallet signers
* Enter into agreement with Wintermute to execute sale over 1 week
* Transfer AKITA to Wintermute
* Wintermute will sell AKITA via exchanges (and, possibly, OTC)
* Wintermute will transfer ETH/USDC/DAI/USDT from sale to Gitcoin treasury

**I. b) Sell 3% of AKITA Balance via Gnosis Auctions**

[Gnosis batch auctions](https://gnosis-auction.eth.link/#/) let you execute trades on-chain and trustlessly. [Batch auctions](https://blog.gnosis.pm/announcing-gnosis-auction-launch-390124d56248) enable matching of limit orders of buyers and sellers with the same clearing price for all participants. They are designed to reduce the risk of frontrunning, gas bidding wars, and lower the amount of extracted value from auctioneers and bidders. The largest auction executed so far is by Boson Protocol, which had >$50m of bids and ended up settling ~$26m.

**Benefits:**

* Fully on-chain and trustless
* Batch auctions help prevent getting front run or sandwiched
* Good precedent for the Gitcoin treasury; auctions are transparent and don't privilege any particular players
* Gnosis does not charge a fee for batch auctions

**Drawbacks:**

* Can be a slower process than selling via market maker
* Execution could be worse than market maker

**Implementation**

* Set up Gnosis Auctions via Gnosis safe app by following [these](https://gnosis-auction.eth.link/#/docs/starting-an-auction-with-safe#topAnchor) steps
* Enter parameters including but not limited to:
  * Token address we plan to auction
  * Token address we accept for bidding
  * Amount of tokens we plan to auction
  * Limit price we are willing to accept for tokens
* Finalize bid and receive ETH or stablecoins

Note that we have the option of KYC’ing bidders. However, this will make the process longer and reduce demand.

**II. Place 90% of AKITA Balance in a 2-year Sablier Contract**

We recommend placing 90% of the AKITA balance in a Sablier contract unlocked over 2 years. 45% of the total AKITA balance will accrue to the Gitcoin treasury over 2 years to fund quadratic rounds. 45% of the total AKITA balance will accrue to the AKITA treasury over 2 years to fund AKITA development. The Gitcoin and AKITA community will independently control how funds streamed to them are spent.

**Why place this amount in a 2-year Sablier contract instead of selling it?**

* Liquidity is thin and attempting to sell this balance will be difficult in current market conditions
* A sale does not maximize the amount of public goods that can be funded with this substantial donation
* A 2-year contract gives confidence to AKITA that the token won’t be sold at once

**Why place this amount in a 2-year Sablier contract instead of burning it?**

* 90% of the AKITA balance is a substantial amount that could be used to fund public goods; burning all of this could mean important projects miss out on funding
* Placing this amount in a 2-year Sablier contract helps Gitcoin and AKITA take more time to decide the best course of action and get the most value out of this donation
* 2 years is a long enough time horizon to help both Gitcoin and AKITA to think longer-term about funding development that matters

**Drawbacks**

* A substantial portion of AKITA’s token supply will be held in the Sablier contract
* There could be immediate benefits from a sale that Gitcoin isn’t realizing
* Although minimal, this might necessitate some coordination between Gitcoin and AKITA that both communities may or may not want

**Conclusion**

We recommend selling 10% of the AKITA balance and placing 90% of the AKITA balance in a 2-year Sablier contract. There is no perfect way to deal with the AKITA donation. However, given the goals of Gitcoin (funding public goods), the risks involved (reputational and headline risks), and current market conditions (low liquidity for the token), we believe this proposal is the best out of the possible options. 

We would love to hear any feedback and questions! We plan to set up a Snapshot vote on this proposal later this week.

-------------------------

wl790879704 | 2021-05-26 04:13:57 UTC | #2

[Discussion: What should the gitcoin community multisig do with the donated AKITA](https://gov.gitcoin.co/t/discussion-what-should-the-gitcoin-community-multisig-do-with-the-donated-akita/67)

-------------------------

personofnointerest | 2021-05-26 07:47:55 UTC | #3

You won't be extracting much value if its only locked for 2 years – that 45% at $59m won't be the case when it comes round to it, especially in a bear market. Ironically, retail will probably dump on you by then and that'll probably be catalysed by the immediate 10% sell. People will lose faith, Akita will lose value.

I see logic in the whole original '20 year' suggestion – a marathon not a race.

-------------------------

HelloShreyas | 2021-05-26 11:00:17 UTC | #4

2 crypto years is like 10+ normal world years! Things change so rapidly in crypto and there can be bull and bear market cycles even within two years. Given the crypto context, a 2 year schedule should give confidence to AKITA. Also, this amount will be streamed via a Sablier contract. So AKITA and Gitcoin will each receive about 11% of the AKITA token balance after 6 months. Both communities can use these amounts to fund public goods and development.

-------------------------

trent | 2021-05-26 22:07:28 UTC | #5

I can't find it in the documentation, but does Sablier take a % of each stream?

Edit: confirmed by Paul that it doesn't!

-------------------------

andyt | 2021-05-26 17:13:54 UTC | #6

I agree with this proposal. Interested to see what the results will be and how much $ from the market.

-------------------------

HelloShreyas | 2021-05-26 17:35:34 UTC | #7

> I can’t find it in the documentation, but does Sablier take a % of each stream?

No, Sablier is free!

-------------------------

hihoo | 2021-05-26 19:46:10 UTC | #8

I agree with this proposal.

-------------------------

paulrberg | 2021-05-26 21:50:21 UTC | #9

[quote="trent, post:5, topic:1663, full:true"]
I can’t find it in the documentation, but does Sablier take a % of each stream?
[/quote]

No, we don't. And we don't have the power to turn on any fee. The protocol is completely free to use.

-------------------------

remix | 2021-05-26 22:51:42 UTC | #10

出售10％AKITA并将90％AKITA放置在2年Sablier合同中 :+1:

-------------------------

James | 2021-05-27 01:54:48 UTC | #11

Hey all,

Just posting on behalf of 🔥_ 🔥 in support of @HelloShreyas proposal. Currently there are ~4 proposals that have been posted regarding AKITA;

[This proposal](https://gov.gitcoin.co/t/sell-10-akita-place-90-akita-in-2-year-sablier-contract/1663/8); outlining a short/medium/long term strategy for how the Gitcoin community can collaborate with the AKITA community as well as use some portion of tokens to continue to drive forward public goods funding.

[Proposal](https://gov.gitcoin.co/t/fund-public-goods-with-akita-via-quadratic-funding/185) from @castall proposing the Gitcoin community use AKITA as part of the next quadratic matching pool. Where ‘A smart contract for distributing Akita will be funded at the end of a round once the multisig owners approve of the contract’s particulars’. AKITA is distributed according to matching pool distributions.

[Proposal](https://gov.gitcoin.co/t/proposal-to-gitcoin-community-from-akita/218) from @relic to ‘burn everything that VB sent except for 5%. Leave 5% to stimulate progress between both communities’.

[Proposal](https://gov.gitcoin.co/t/return-akita-tokens-to-its-source/199) from @tjayrush proposing the Gitcoin community return the AKITA funds to their source (Vitaliks sending address).

There has also been a significant amount of discussion on @lefterisjp's [thread](https://gov.gitcoin.co/t/discussion-what-should-the-gitcoin-community-multisig-do-with-the-donated-akita/67) introducing the idea to the Gitcoin community.

This reply aims to summarize the majority of AKITA proposals from the Gitcoin community, **we’re proposing a snapshot vote which will allow the community to compare the current four proposals and ultimately make a decision on what to do with the AKITA held by Gitcoin.**

-------------------------

castall | 2021-05-27 02:11:42 UTC | #12

[quote="James, post:11, topic:1663"]
[Proposal](https://gov.gitcoin.co/t/fund-public-goods-with-akita-via-quadratic-funding/185) from @castall proposing the Gitcoin community use AKITA as part of the next quadratic matching pool. Where ‘A smart contract for distributing Akita will be funded at the end of a round once the multisig owners approve of the contract’s particulars’. AKITA is distributed according to matching pool distributions.
[/quote]

Just to clarify, I'm still trying to decide an appropriate length of time in which Akita could be used as matching funds.  I'm not suggesting to blow it all in one round

[quote="vbuterin, post:126, topic:67"]
Put the coins into a Sablier contract that unlocks them over the course of some long period of time (eg. 20 years).
[/quote]

Vitalik threw out 20 years as a time frame.  I'm thinking something shorter than that, but one that still feels long, like 5 years (i.e. 20 rounds).  If you have feedback, please [add to the post](https://gov.gitcoin.co/t/fund-public-goods-with-akita-via-quadratic-funding/185).

-------------------------

fu58889 | 2021-05-27 02:15:26 UTC | #13

将硬币放入Sablier合约中，该合约会在很长一段时间（例如20年）内将其解锁

-------------------------

relic | 2021-05-27 02:16:24 UTC | #14

I like the idea of using the sablier contract to distribute, but we should do that with the 5% and still burn the 45%. This is the safest way back to normal and instills confidence back into the retail investor. 

We will still have a lot of tokens coming to us while making sure that the AKITA community, who are the reason that this is possible, gets back to the original tokenomics of the project.

-------------------------

Reader_kk | 2021-05-28 18:23:17 UTC | #15

in trading and investor wise, one of the highest possibility would be that the moment this proposal is approval and accepted, the price of Akita would crashed to near zero as investor pull out their funds.  it's like 1929 where people withdraw their money from banks as soon as they know the situation. 

so instead of the few hundreds of millions dollars gitcoin would like to extract when they approach liquidating akita in any form.  It is too easy for these meme token to crash.  there are similar crash in other tokens when adverts information is released.  

**Any proposal to liquidate in any form, no matter the duration**
current price: $0.000002106
crash price: $0.0000000002 (estimated)
worth at crash price: $2millions
presume gitcoin 50% liquidation take home value : $1million

**relic proposal and price goes back to ath**
back to ath price: $0.00003346
worth at ath price: $3,346,000,000 ($3.3billions)
relic proposal of burning 45% and keeping 5% : $3.3billions* 5% = $167millions

**relic proposal and price goes back to midpoint**
back to midpoint price: ($0.00003346 - 0.000002106)/2 + 0.000002106 = 0.000017783
worth at midpoint price: $1,778,300,000 ($1.7billions)
relic proposal of burning 45% and keeping 5% : $1.7billions* 5% = $88millions

-------------------------

linda | 2021-05-28 21:59:42 UTC | #16

I mostly agree with the goal of this proposal. Thanks for putting it together!

- I don’t think it’s ideal to hurt the AKITA community by selling all of the tokens at once given how that will impact price. While we aren't beholden to AKITA, the idea of negatively impacting a community doesn't seem in line with the ethos of Gitcoin 
- I like the idea of selling 10% of the balance using a reputable market maker (provided that Gitcoin multisig signers are comfortable with the KYC) and the rest with Gnosis Auctions
- I think it makes sense to use Sablier to stream the rest over a period of time (2 years sounds reasonable) but it’s not really clear to me why 45% of the total AKITA balance will accrue to the AKITA treasury since Gitcoin’s mission is to fund open source public goods, not specifically fund the AKITA community. Perhaps if 2 years is too short and selling the rest in 2 years would harm the AKITA community, the time period can be lengthened

-------------------------

relic | 2021-05-29 04:44:35 UTC | #17

Without funding the AKITA community, you would effectively be liquidating the AKITA community  to fund Gitcoin grants. The tokens that Vitalik "donated" to gitcoin, were assumed burned by our community (not an actual burn but more of a DE circulation). Those tokens were one half of our supply. What would happen if half of the GTC supply was "donated" to UNICEF and UNICEF decided that world health was more important to fund than "public goods". Its a sticky situation.

If Gitcoin chooses to proceed in any way toward liquidation without including the AKITA community, then I don't believe it will be possible to salvage the situation or reach a positive outcome for both parties.

The results would be Gitcoin liquidating the position for minimal value and the rest of the AKITA community following suit, this is not just including retail investors but exchanges as well. This type of mass liquidation event is of no help to anyone and would only result in one outcome.

 The Gitcoin community would receive some funding from the initial liquidation, yet would also receive a ton of negative feedback/PR, and *NO* source of long term funding.

Where as, if we choose to work together on a solution beneficial to both parties, both communities could leverage each others respective "specialties".

The term "complimentary opposites" comes to mind although in this context it means something a bit different.

Although Gitcoin and the AKITA communities started in much different fashions, I do not think our long term goals are dissimilar (We too want our community empowered through a decentralized internet) and I do whole heartedly believe that these communities can be mutually beneficial to each other short and long term.

Its a delicate situation, trying to extract value efficiently without causing any collateral damage in the process.

I stand by my point that we should take care of the place that this value accrued from in the first place, which is the AKITA community. Thus far we have proven that even without funding, or paid advertising, that building a decentralized community project *IS* possible.

-------------------------

relic | 2021-05-29 01:09:28 UTC | #18

![image|690x379](upload://c5ZWI5RNA82Y9qJ3pi6FWAmjXAv.png)

-------------------------

relic | 2021-05-29 02:26:27 UTC | #19

This actually becomes the classic scenario that is zero-sum. Both entities control half of the supply, both entities have the power to nuke eachother, the only possible solution that doesnt result in nuking,is by cooperation. Funny to think that the [fundamental problem with Ethereum](https://medium.com/@danrobinson/ethereum-is-a-dark-forest-ecc5f0505dff) at the blockchain level is the same ZERO sum game being played at the social level. Interesting.

-------------------------

Edunwa18 | 2021-05-30 08:54:03 UTC | #20

I support your proposal, originally the tokens sent to VB was taken as burnt..i think it's against all good coincidence to dump it back against the Akita Community, I support burning, dumping is against the maxim of equity and natural justice

-------------------------

blcold | 2021-05-30 07:28:25 UTC | #21

I agree with the goal of this proposal.

-------------------------

wschwab | 2021-05-31 09:44:11 UTC | #22

I'm a bit confused by your posts in this thread @relic . @HelloShreyas is clearly trying to sell the tokens in a way which is sustainable for the AKITA community, by assuring that the rate of sale is low. I would've even read your comments here as being in support of the proposal if it wasn't for the occasional zero-sum comment.

If you are unhappy with this proposal, what is it that you would like to see Gitcoin do with their AKITA? I see you write multiple times that it should "benefit the AKITA community", but that isn't a concrete plan. I would strongly recommend coming up with a detailed proposal (along with the AKITA community), and writing it up in a new thread. It should include a plan for where whichever amount of AKITA should go where, as @HelloShreyas did here. There are already multiple threads with solutions. We would love to hear what positive-sum games you can come up with!

-------------------------

airtwothree | 2021-05-31 12:10:11 UTC | #23

The more proposals I see about AKITA , the more I get scared to become a holder. Can you guys give it a rest? Gitcoin isn't going to sell your meme coin. They have their own coin and you guys are acting like babies while their ICO is literally happening. Great timing guys.

-------------------------

androolloyd | 2021-05-31 12:31:15 UTC | #24

I think this is a bad proposal, 2 years is forever in crypto, if the akita project disbands in a month we'll be kicking ourselves for not acting rationally.

-------------------------

relic | 2021-05-31 20:51:12 UTC | #25

Great timing? How is that our fault? How can you say they aren't going to sell our token when every single proposal and vote made is how to sell our token..

Shreyas is the only person making strides toward a logical scenario.

Everyone else commenting and making snapshot votes is just kicking the hornets nest.

-------------------------

airtwothree | 2021-05-31 22:14:30 UTC | #26

They aren't selling AKITA. They literally have an ICO going on and the AKITA community wants Gitcoin to stop and focus on a mistake. Why couldn't this wait till after $GTC is well distributed ? These proposals seem like you guys are trying to sabotage Gitcoin when Gitcoin can have so much potential to grow right now. Just put it behind yall and let Gitcoin carry on doing something great this week.

-------------------------

wijuwiju | 2021-06-01 07:21:04 UTC | #27

hello guys,

imho I have no idea why everyone is so worried about committing to singleish strategy of getting rude of entire $AKITA holdings in one swift move, whether that's a liquidation, burn, sending back to VB, airdropping to GTC holders proportionally to GTC drop, whatever you can come up with

I mean, I understand the reasoning behind getting hands clean asap, but not sure whether that's the best solution

So that's said I was thinking of maybe suggesting to diverge discussion into a different stream, not stop keep coming up with the proposals on what to do with entire $AKITA in our treasury and trying to execute it asap, but rather how we in long term and in a sustainable fashion can actually use those funds to do public good. 

For example if there is need for additional liquidity to be raised for next matching grants round we can vote to liquidate whatever about of akita (e.g 3%) to fund it, maybe use some of those funds to educate $AKITA people on how our governance works (because from what I see, many don't even understand that by swapping their akita for gtc they can vote on what to do with the treasury)

Again, I'm not suggesting anything here, just some random ideas, but what I'm saying is that I don't see a real urge to rush into getting rude of all $AKITA straight, since it causes so much division and solving one problem at time makes a lot more sense to me

In the end we are all here kinda together

wijuwiju.eth

-------------------------

souptacular | 2021-06-01 23:22:15 UTC | #28

I just voted on Snapshot in favor of this proposal. Great job ya'll! Here are my thoughts I put on Twitter (https://twitter.com/hudsonjameson/status/1399868787579625480?s=20).

> I have been reading forum posts on https://gov.gitcoin.co/ regarding what to do about the AKITA tokens Vitalik donated:
> 
> https://gitcoin.co/blog/announcement-gitcoin-community-receives-generous-gift-from-vitalik-buterin/
> 
> I just voted for the proposal that sells 10% AKITA & places 90% AKITA in a 2-year Sablier Contract
> 
> Thread on my thinking 👇
> 
> It is a common tactic for a projects to send a portion of their token supply to Vitalik's public Ethereum address for publicity reasons. I've heard different reasons for why the AKITA team did this: publicity, as a "burn" address, as a gift to Ethereum's creator. Akita's creator sent roughly half of their supply (500 million tokens) to Vitalik's address. Now that Vitalik has donated much of the 500 million to the Gitcoin community multi-sig we all need to decide what to do with those tokens.  To me this decision hinges on the collective opinion of the viability of the AKITA community. The AKITA coin started "as joke coin without a team or project" by it's own admission, that is now trying to find use cases to no longer be a joke coin (see: https://akita.network/faq).
> 
> I've seen a proposals that distributes or locks in other ways the token over a period of 2 years. What are the chances that the AKITA team, community, and token are viable in that time? What's unique about their token? What if we slowly distribute over 2 years, but the team disappears and the price/liquidity tank? I don't think the token and team will last 2 years and I don't see any evidence on their site (plans, etc.) to convince me otherwise. So does that mean we should liquidate all of the tokens and get it over with?
> 
> As much as I would like to think positively about AKITA, I was starting to lean towards a more pragmatic approach of selling all of the tokens for maximum profit and avoid the risks and overhead of dealing with the tokens any longer. That was my thinking until I read this: https://gov.gitcoin.co/t/discussion-what-should-the-gitcoin-community-multisig-do-with-the-donated-akita/67/126
> 
> Vitalik's reply seems to indicate he believes there are better ways to handle this than pure liquidation of all of the tokens. His words should hold some weight as he is the donor of the tokens and generally a smart dude. Thinking/reading on the forum more brought up a few other points. A point that resonated most with me is that it is bad optics/not in the ethos of Gitcoin to wreck a token/community, even if the origins of the project or viability of the project are in question. If we can help both AKITA and Gitcoin that is the best. So my "pragmatic" approach of liquidating the token completely is now in the trash can somewhat. However, I can be convinced to support a proposal that liquidates some of the tokens so Gitcoin can benefit now.
> 
> Specifically, the proposal that "sells 10% of its AKITA balance and place 90% of its AKITA balance in a Sablier contract unlocked over 2 years" is intriguing. https://gov.gitcoin.co/t/proposal-akita-sell-10-akita-place-90-akita-in-2-year-sablier-contract/1663
> 
> I will be voting on this proposal since it seems to be balanced and looking out for both communities to maximize value.
> 
> If you have GTC and want to delegate your coins to me check out this thread! I appreciate everyone who has delegated so far :)
> 
> https://twitter.com/hudsonjameson/status/1399853366847717379?s=20

-------------------------

wschwab | 2021-06-06 12:13:25 UTC | #29

> if the akita project disbands in a month we’ll be kicking ourselves for not acting rationally

I respectfully disagree. While you're right that deliberation may cause de-optimization of the amount of financial value Gitcoin can extract, I think there are things even more important than the finances at stake here. I'll explain what I mean.

When we look at Gitcoin's mission of supporting public goods, I personally (this is an opinion) see it as a mission that should last long into the future. i think everyone here would see Gitcoin as a success if it is still supporting public goods a hundred years in the future. I think many would see it as a failure of sorts if it fails within the next couple of years (there have been many successes, but alas, they weren't sustainable). I think we need to realize that the actions around AKITA can possibly affect the "life expectancy" of Gitcoin. Gitcoin does also succeed based on reputation, and has moral legitimacy to contemplate. As strange as this may sound, this could be worth more than the instant millions in the long run.

It is true that this money wouldn't even be for Gitcoin, but rather to support projects now. Even so, if there is resulting damage to Gitcoin's reputation or worse, I do not think the burst of funding in the short term will be worth it. I think we need to be very careful with overly economics-based definitions of rationality here.

-------------------------

hisefly | 2021-06-07 05:17:33 UTC | #31

I fully agree with this proposal, which is conducive to the better development of gitcoin. I wish you all the best

-------------------------

wschwab | 2021-06-13 07:39:12 UTC | #32

um, I think you might want to read that again - I was the one arguing _not_ to do the "rug pull", for pretty much the same reason you mentioned :rofl:

**update**: this was originally written as a reply to a post which argued against my previous post, that post has either been updated or removed now

-------------------------

JAKP162 | 2021-06-12 11:11:46 UTC | #33

It's a very good initiative since it will help solve the problem at hand

-------------------------

munky | 2021-11-29 11:17:56 UTC | #36

Create value through **shared** truths. 

From what I understand,  the way this started, a community of people pumping a meme coin decided:
**put coins in Vitalik's wallet, 
    wen moon?**.  
Just as stupid as the rest of the dog strategies that worked.
However well meaning it may have been, it was extremely speculative, and involved putting somebody in a situation to make a really hard decision against their will.  It wasn't an investment into their community, they literally placed the value of the community into another parties hands and hoped for the best. 

I think our communities deserve to be responsible for the outcomes of the decisions that we make, because in that process of failing or making a wrong prediction, we are able to see the ways to avoid or move through that better in the future.  

Putting the future of their community into another communities hands wasn't a way to add value to anything.  I haven't had enough time to read about this yet, but I think whatever we decide should not be influenced by trying to rescue the AKITA community from something they decided they could benefit from if it worked, without worrying about any risk or what problems it might cause for the people they involved if it backfired.

I ultimately just want everybody to be friends, but I don't think its fair to plop this all onto another person or community and expect it to work out in your favor.  

We should reward those who collaborate in shared truths with **consent** from the party they are collaborating with.

-------------------------
