---
id: 67
title: "Discussion: What should the gitcoin community multisig do with the donated AKITA"
slug: discussion-what-should-the-gitcoin-community-multisig-do-with-the-donated-akita
category: open-discussion
url: https://gov.gitcoin.co/t/discussion-what-should-the-gitcoin-community-multisig-do-with-the-donated-akita/67
created_at: 2021-05-12T20:16:30.273Z
last_posted_at: 2021-11-01T13:59:50.689Z
posts_count: 179
views: 17460
like_count: 625
---

# Discussion: What should the gitcoin community multisig do with the donated AKITA

<https://gov.gitcoin.co/t/discussion-what-should-the-gitcoin-community-multisig-do-with-the-donated-akita/67>
lefterisjp | 2022-05-28 15:38:58 UTC | #1

Context: https://twitter.com/owocki/status/1392542552880865280

$500m worth (at the time) of AKITA was donated to the gitcoin community multisig.

This is an illiquid token so market selling for the actual value is impossible. Little to nothing is known for the plans of the AKITA project (is it just a meme coin?) so holding for a longer period of time may lead to loss of all of its value.

- Would giving it back make sense?
- Market Sell with insane (~98%) slippage?
- Keep it?
- Something else?

What should the gitcoin community do with these funds? Remember. Gitcoin's purpose is to fund open source (and public goods).

-------------------------

Adamscochran | 2021-05-12 20:51:01 UTC | #2

1. Sell it OTC to an experienced market maker, you'll get pennies on the dollar but it might be better than the slippage? (likely slow)

2. Right now there is $5M of liquidity in Uniswap. Sell what gets you there (via a mev proof relayer or perhaps TWAP [likely not worth waiting]), keep the rest of the tokens in case they move up (unlikely)

Take the $XM ETH and set up ETH2.0 validators where 100% of the net income from the nodes goes into the public goods pool.

Any new meme coin from this bout that doesn't have top exchanges or anything beyond just a meme isn't going to go very far after a rugging like that. The harsh reality is that the damage has already been done and their holders are still in a position where they are holding to zero.

If Gitcoin doesn't sell on to them, then experienced market makers and bots will continue to do it, at least if Gitcoin does it the money can help create a sustainable public goods.

It's an awkward trolley problem, but only one side of the tracks has a good outcome for at least one party.

(FWIW it sucks. We've all been on the bad end of rugs. In this case spammy projects tried to use VB to shill vaporware and some of the biggest bag holders were early insiders. I'm not saying there is one clearly good outcome, it's messy, but post damage, there is only one path that also serves a net benefit for the community.)

-------------------------

timothyjcoulter | 2021-05-12 20:27:34 UTC | #3

TL;DR: Sell it slowly. 

Why? 

First, you don't want to assume ill-intent on the AKITA community. By rugging the token (market selling it) you suggest that community is worth dumping on, which is not the ethos of Gitcoin. That said, Gitcoin has a mission, which is to make the open source community better, and it's their job to execute on that mission, so ultimately they should sell it. To do right by the AKITA community and assume the best, while also staying true to their mission, Gitcoin should sell at periodic intervals no matter the price (e.g., price insensitive selling) and publicize the selling plan and specific timings. That way member of the AKITA community can responding accordingly, while giving everyone a chance to stay true to their values.

-------------------------

Adamscochran | 2021-05-12 20:34:07 UTC | #4

The rug component has really already taken place, if you try and adjust your actions to correct the past, all you end up with is a situation where AKITA dies anyway and Gitcoin gets no benefit from it.

I understand the sentiment, and could see some argument for a TWAP approach (although I'm skeptical) but any publicized detailed sell plan just gets front run to a lose-lose.

-------------------------

nemo | 2021-05-12 20:36:51 UTC | #5

I'll focus on after selling part (I think it should be sold, but can't say what's the best way to do it)

My proposal is to swap it for DAI
## Why DAI

Main idea would be to NOT be exposed to volatility. This is funding that should be there for ongoing support for builders in the ecosystem.

With DAI community can go in two directions:
## Yearn Vaults 
Directly Via Yearn where on a monthly basis part is used in gitcoin round

## Alchemix 
Supply DAI, get half in alUSD, use alUSD (or sell it for DAI), and supply for round funding.

What I like about Alchemix idea is that on a round basis we can constantly max out 50% dept in alUSD and use it in each round.

-------------------------

Adamscochran | 2021-05-12 20:49:21 UTC | #6

Good concepts on selling it to a diverse basket of assets. Something productive that can add on going sustenance to the Gitcoin treasury through other defi protocols is interesting.

**Edit:**

There may also be a way to take a snapshot of those effected in the pool.

Sell the dog token, and put it into productive assets like ETH validators or defi. Use the gains from that to airdrop DAI to the users up until a certain return (perhaps even whole value depending on how productive the assets end up being) and then after that future proceeds go to Gitcoin.

It would mean at least some comp for those impacted but still a longer term future benefit for Gitcoin.

-------------------------

owocki | 2021-05-12 20:48:29 UTC | #7

suggestion from [pioneerpat on twitter](https://twitter.com/pi0neerpat/status/1392577524144738310): 

> Make a proposal to create a lending market for AKITA on CREAM. Deposit and take a DAI loan instead of selling it. Market doesn't crash and you have working capital.

-------------------------

nickjohnson | 2021-05-12 21:06:11 UTC | #8

Why not sell it via a Gnosis auction? This is transparent and gives people warning (nobody is getting rugged) and allows the market to set a clearing price.

-------------------------

HelloShreyas | 2021-05-12 21:39:53 UTC | #9

Here are a few options on what we can do:

1. **Sell via OTC desk**: We'll get far less than the donated USD amount but we can get experienced market makers to execute this. OTC will be the quickest solution, however, it isn't on-chain and trustless.

2. **Gnosis auctions**: Gnosis [batch auctions](https://gnosis-auction.eth.link/#/) let you execute trades on-chain and trustlessly without getting sandwiched/front run. (See [article](https://blog.gnosis.pm/announcing-gnosis-auction-launch-390124d56248).) I think the largest trade executed so far is by Boson Protocol, which had >$50m of bids and ended up settling ~$26m. For the size of the AKITA position, we would need to do several auctions (10+ probably).

3. **Selling on DEX**: High slippage, low liquidity, chance of getting front run/sandwiched. Advantage: on-chain execution.

4. **Hold on for longer**: Solutions might emerge from the broader crypto community and/or the AKITA community. For example, @Crisgarner suggested token buybacks from AKITA as a potential solution. If we have confidence in the AKITA community, we can even decide to earmark these funds over a longer time horizon for Gitcoin grants. If we are selling large amounts of the tokens, we also need to time to understand if there are any legal implications from doing this. 

**Conclusion:** We should understand any legal implications of executing a large sale, especially when it seriously impacts price. We should discuss a partial token sale with OTC desks and the Gnosis team. And we should hold the rest of the tokens till we get more clarity on the points above.

I'm happy to help facilitate the discussion with Gnosis and/or OTC desks. I'm also helping the Crypto Relief team that received a $1B donation in $SHIB. We can coordinate efforts if needed.

-------------------------

nemo | 2021-05-12 21:10:11 UTC | #10

Not sure about this since then we are exposed to AKITA volatility and asset management due to volaitility 
> Make a proposal to create a lending market for AKITA on CREAM. Deposit and take a DAI loan instead of selling it. Market doesn’t crash and you have working capital.




I like that idea @nickjohnson and @HelloShreyas mentioned about either OTC or Gnosis auction

-------------------------

Crisgarner | 2021-05-12 21:20:54 UTC | #11

Talk with the AKITA community to see if they are interested in buybacks.

-------------------------

HelloShreyas | 2021-05-12 21:26:18 UTC | #12

This would be cool! Finding a solution with the AKITA community can be ideal

-------------------------

relic | 2021-05-12 23:51:13 UTC | #13

Hello guys, Im Relic , project lead for AKITA network. I'm going to leave a little bit about us so you might understand the magnitude of what has taken place for our community.
@relic22 on TG
https://t.me/akitatoken
Twitter: AKITA_network
Medium: https://akitanetwork.medium.com/ 


We never thought V would ever touch these tokens, and now it seems the fate of our project has been put into your hands. I'm sure our steward chose well.

We initially tweeted to VB to see if he wouldn't mind burning our tokens, but seeing them go to help humanitarian efforts is something we would never disagree with. I hope we can all figure out a way to help each other, all we ever wanted was to be involved.

I think we can all agree that Vitalik did not want the burden of having these tokens in his possession.

With that being said, I cant really argue that our fate does not deserve to be in anyone else's hands, since the entire genesis of the project was centered around that fact.

Ideally I'd love to collaborate both of our communities, and leverage all of our assets and connections into building. I don't think our goals are dissimilar.

-------------------------

Adamscochran | 2021-05-12 23:59:35 UTC | #14

Can you explain the justification for sending tokens to VB in the first place rather than a burn address?

Because you note that the goals of the communities are similar and seek collaboration, but, I can't help but have a healthy bit of skepticism towards that based on the decision to send tokens to VB in the first place.

Racking it over in my mind, I can't imagine in which that decision was not done simply as a marketing ploy, which doesn't bode well for any trust or good faith in collaborating.

While I have no interest in seeing individuals, who didn't know any better, getting hurt, there is a principle matter here in that the blockchain has no governing principles beyond the chain at the end of the day, and so if you sent them to VB you cannot then ask by social contract those tokens to not ever be used.

I think most in this community will want a more olive branch and less fire and brimstone approach than I'd advocate for, but I'm sure they would still be interested in understanding the background on that decision as they weigh up how to collaborate.

-------------------------

relic | 2021-05-13 00:10:35 UTC | #15

Not sure why a "fire and brimstone" approach would be even considered.

We cloned ourselves after SHIBA who originally sent tokens to VB. 

I personally had no involvement with the launching of the contract.

I was just there to pick up the pieces after the original contract owner pulled liquidity.

Intentions aside, a community was formed and a direction was taken.

So, in regards to justification, I cant really provide a good answer to that, I am just leading a community interested in being something more than a meme.

-------------------------

ericdorafactory | 2021-05-13 00:16:05 UTC | #16

Since @relic from AKITA has shown up, I think some/most of the tokens should go back to the AKITA Network, depending on your discussion with AKITA team.

If some tokens are left for GitCoin, a good way to put all tokens on auction is to use a bonding curve. The start price of the bonding curve could be set to a slightly lower than the market price, and the end price could be set to a higher price (e.g. 3x or 5x). The duration of the auction can be a long period of time (e.g. a few months). By using a bonding curve, you can obtain sustainable funding transparently without hurting the AKITA community.

A suggestion -- Curve Auction (a Dora Factory product) can help with the process, a curve of self-defined parameters can be created: https://curve.auction/#/issue. The bonding curve factory team will refund all costs generated from the auction to the GitCoin community.

The Dora team is sharing the vision of funding public goods with GitCoin, and we hope that the result of selling AKITA tokens can contribute to the global open source community development, but in the same time make sure it's not at the cost of AKITA holder community.

-------------------------

Adamscochran | 2021-05-13 00:21:22 UTC | #17

[quote="relic, post:15, topic:67"]
I am just leading a community interested in being something more than a meme.
[/quote]

And what is that 'something more' you are interested in being?

-------------------------

relic | 2021-05-13 00:21:33 UTC | #18

I willingly ask for you guys to keep 10% of the supply and work together with us to build a better decentralized future.

Vitalik has given you this, and you should benefit from that decision.

-------------------------

relic | 2021-05-13 00:27:04 UTC | #19

Our plan is to first enable governance for the project, since our token on eth is unable to be interacted with, we have decided on moving to Avalanche for governance.

The first goal was to establish funding, by creating a dex. 
Team is heading to BTC 2021 in miami to try and convince BTC maxis to bridge to our dex on avax.
Longer term, the realization of AKITA network, a truly decentralized social media platform. We want to implement a social media structure that is completely self governed while implementing defi mechanisms to pay users for activity, data and analytics. Instead of users data being hoarded, we intend to sell it via data marketplaces like ocean protocol and redistribute that back into our token liqudity.

-------------------------

ericdorafactory | 2021-05-13 00:53:28 UTC | #20

I'm from DoraHacks and Dora Factory team so I won't decide where the fund should go and how much it should be kept. However if GitCoin and AKITA community need us to set up a bonding curve, we are happy to help!

-------------------------

cupOjoseph | 2021-05-13 17:19:37 UTC | #21

Hello, it is I, cupojoseph. I have worked for gitcoin (back in 2018), contributed to the platform, spent tens of thousands of dollars donating to grants and funding work on the platform, and got my very first eth ever on Gitcoin shortly after it launched. I consider myself very involved, and the long term success of gitcoin is deeply important to me.

I hold these truths to be self evident:

1. Gitcoin community and the world of funding public goods + open source does not owe anything to the akita community. 0 of this was donated by the akita community, and 0 of it would have made it here if it were just up to them.
2. These funds were removed from liquidity before being sent to gitcoin, where the akita community thought they would stay to increase their ability to dump.
3. Gitcoin community will not benefit long term by becoming an akita connected product, which will likely happen if these funds are held for long.
4. The goal of the gitcoin community is to fund open source sustainably in a way that has never been possible before.
5. The goal of the akita community is a pyramid scheme to make token price increase as more people buy in... and memes
6. these goals have competing interests whether or not we are willing to admit it.


with these in mind, the goals of the gitcoin multisig wallet members should be to turn as much AKITA into ETH and DAI, in order to fund open source and public goods, as fast as possible while extracting as much value as possible. A 98% dump right now does not extract as much value as we can so that should be mostly ruled out. However, we the members of gitcoin ( who have been honestly building a more transparent financial system and other non-meme-pyramid-scheme based crypto projects on gitcoin for years now) **do not owe the akita community anything, and should not hold these coins for very long with the reasoning that dumping will hurt them somehow**.

One plan to extract as much value from this for open source and public good funding:
- dump some small percentage now, maybe not more than would crash the price by 10-20%
- create a lending pool on CREAM and lend as much as possible out for DAI and ETH
- use these funds to buy equity in Gitcoin the company (not the community) back from consensys and VCs
- sell in non-dex places where there may be less slippage: OTC, gnosis auctions, and back to akita community
- create akita yield farm to increase liquidly again and dump more over time
- Set hard goals of not holding any significant amount for more than 6 months

Edit: re Akita team members asking us to hold a percentage of the coins.
[quote="relic, post:15, topic:67"]
I am just leading a community interested in being something more than a meme.
[/quote]
This is just dishonest. Your project's website clearly describes itself as "inspired by elon musk, little brother of dogecoin, meme-based" 
I'm not against holding a small percentage in good faith. But **holding it so the price doesnt collapse to the advantage of akita holders, is directly disadvantaging open source projects for good we could be funding instead, which is my primary goal.**

-------------------------

Adamscochran | 2021-05-13 01:28:04 UTC | #22

Right, so puffery, buzzword nonsense and meme filled hopium that is just going to hurt people entering the crypto space.

That sounds like all the more reason for the Gitcoin team to dump the coin.

Maybe you'll work something out with them, but I personally have no patience for a project that peddles an unrealistic narrative on users who don't know any better.

You can be a memecoin, but if you are a meme coin without any tech (or even the tech knowledge to make a realistic pitch) then be honest about it as people deserve to know what they are buying. When there is a disconnect between what they are being sold and what they get, that doesn't do you any favors.

-------------------------

relic | 2021-05-13 01:36:53 UTC | #23

I think that its really irresponsible for you to talk in this context about our project which it is obvious you have no knowledge of. The community will decide what actions to take, hopefully they aren't as narrow minded.

Don't call our project a pyramid scheme. A lot of people are working very hard to bring utility.

Don't call me dishonest because the initial roots of the project have become something more.

If you find a wallet on the side of the road, you look and see if any money is in there sure, and then you make a decision.

Edit: you also talk about us wanting to have the ability to dump, while in the next sentence proposing how to dump (on us) "the actual community".

-------------------------

JimWarren | 2021-05-13 02:04:43 UTC | #25

I would say definitely give it back to Akita , but there should be something in return Akita can do for Gitcoin which should be discussed and decided.

-------------------------

Yalor | 2021-05-13 02:21:09 UTC | #26

Fascinating thread that has emerged here, I personally don't think any rash actions should be taken. Gitcoin is here to fund public goods, we will continue to do that with or without extravagant donations of dog based coins. 

"Dumping on a community" is not something I think Gitcoin will or should ever do. An eye for an eye makes a world full of blind doges 🐕‍🦺

I think the whole thing is kind of funny, honestly we should not be treating this as a real donation. We should ask the community AKITA and Gitcoin what they would like to see done with these funds to better Gitcoin ( besides just cash it out) I have seem projects come back from the ashes before and I would not put it past anyone to recreate themselves in a useful way if they so chose. 

Full disclosure I have **no clue** what AKITA is all about, but I'm gonna look into it. 

I would suggest that we don't take this *too seriously* though, and please be civil to one another. This is not the place to bring arguments and vitriol ✌🏼

-------------------------

steveny | 2021-05-13 02:21:42 UTC | #27

SELL HALF,KEEP HALF；because you will need the funds to build and selling to eth for investing and respect Vitalik; but keeping half could let the market stable,that's my opinion

-------------------------

Yalor | 2021-05-13 02:22:28 UTC | #28

Def don't agree with this AKITA sent it to VB and VB sent it to Gitcoin so we will decide what to do with it together.

-------------------------

planckmatt | 2021-05-13 10:42:59 UTC | #29

One way to think about this:

If the Akita community believed there was some surplus value in having Vitalik burn the tokens, then perhaps there is (additional?) surplus value in having Vitalik -> Gitcoin do the burn. If that narrative would help Akita then perhaps they would be willing to offer Gitcoin some funds for burning the tokens.

-------------------------

tjayrush | 2021-05-13 02:45:38 UTC | #30

Why not simply send the tokens back to the project and let them and their community sink or swim on their own. I see nothing but downside to GitCoin getting involved in this any deeper than they already are.

Another possibility is to send the tokens back to Vitalik with the implied message being "Thanks but no thanks."

Charities give back tainted money all the time, and this feels like tainted money to me.

-------------------------

Adamscochran | 2021-05-13 02:50:53 UTC | #31

At the end of the day, if you send someone tokens, they can decide what to do with it after that.

If they send it then to someone else, there is no social contract nor obligation on that third-party listening to what the first party wants done with the tokens.

Akita is a meme coin and already plummeting.

This isn't about if you fleece the community or not.

The fleece already took place when they bought the token.

This is like a game of musical chairs, the music has already stopped. The only question is who is sitting in the chair when it is all over. Will it be Gitcoin or will it be market makers and bots who eat Akita buyers alive?

Because a quick glance at the transactions for the Akita pool on Uniswap show that's already what is happening. The retail investors are getting destroyed because they were sold on a pipe dream meme token - and that sucks. But Gitcoin not selling doesn't change that.

The only scenario I see where Akita users get anything out of it is if after the selling the Ethereum is put to work and gains yield that gives them some pay back to a threshold.

Other than that, you can't save a sinking ship, it doesn't mean you need to go down with it though.

-------------------------

Yalor | 2021-05-13 02:50:55 UTC | #32

I'm not against this idea, it seems the most logical and rational way to deal with this extraordinary situation. 

I don't think it would serve Gitcoin to "cash out" on the misfortune of anyone, whether this project is a success of failure should really rest on their own shoulders. Taking an action one way or the other is kind of a signal we don't want to make....

-------------------------

relic | 2021-05-13 02:57:33 UTC | #33

A sinking ship that has steadily rose since inception.... I'm sorry man but your logic is way off. I just feel like you are looking at this in the context that we are just a meme coin. I'm not sure what project you work on or are invested in but I'm sure as hell you wouldn't want it written off by someone who didn't understand it. I'm also sure that had you been in AKITA a month ago you wouldn't feel that way.

-------------------------

planckmatt | 2021-05-13 03:01:18 UTC | #35

Hey relic, do you think there is a chance of an offer from Akita to Gitcoin in exchange for burning all of the tokens?

Potentially win-win. RE: post upthread “If the Akita community believed there was some surplus value in having Vitalik burn the tokens, then perhaps there is (additional?) surplus value in having Vitalik → Gitcoin burn the token. If that narrative would help Akita then perhaps they would be willing to offer Gitcoin some funds for burning the tokens.”

-------------------------

Yalor | 2021-05-13 03:01:40 UTC | #36

Got some information from the AKITA Telegram:

> " We are building a dex on Avalanche that will bridge to eth and btc, we will use this dex to fund other defi projects on avax, we also have a meme swapping, farming and staking platform launching in a few weeks. Our main project will be AKITA network which will be a decentralized social media platform. This platform would use AKITA as a utility token and be governed by our community governance token."

I think these are interesting experiments, at the least.

-------------------------

Adamscochran | 2021-05-13 03:13:50 UTC | #37

Come on Yalor, these are buzz words.

Earlier in this thread they talked about how they are going to Miami to convince BTC maxis to use their AVAX dex.

One moment they are talking about a dex, then they are talking about meme swapping (wtf is that?) farming and staking launching "in a few weeks" (which would mean they should already have EVM compatible smart contracts they can show)

Then in the next sentence they talk about a network that is a decentralized social media platform.

None of that is on a website, none of that has any indication there is any technical team with the capabilities to build those things, nor that those things really mean anything to begin with anyway.

It's like every 2017 buzzword project constantly pivoting to the next trope to keep up steam.

If they've got unique EVM compatible contracts I am happy to review them and then eat my hat. But, I'd put a healthy bet on the fact they don't.

-------------------------

relic | 2021-05-13 03:24:51 UTC | #38

Our smart contract for our dex is forked from pangolin with a custom bridge being built, were working with the avax team and chainsafe to get this done right. The AKITA governance token is based on makers model and our meme swap is forked from sushi for the LP but the rest is custom. OK, so were not the uniswap core team but come on, were out here trying to build!

Look, I get it, be skeptical. I would be too, but everyone who didn't get a few rounds of investments had to start somewhere small.

-------------------------

relic | 2021-05-13 03:27:11 UTC | #39

Yes, definitely willing to work with you guys on a good solution.

-------------------------

JimWarren | 2021-05-13 03:31:47 UTC | #40

I like planckmatt's idea of seeing what Akita can offer in exchange for burn so it's a win-win for both and sounds like Akita is willing to work together for something positive out of all of this.

-------------------------

Adamscochran | 2021-05-13 03:33:41 UTC | #41

Do you have a link to the repos?

Because so far it sounds like you have plans to fork somethings that you don't fully understand.

-------------------------

relic | 2021-05-13 03:35:11 UTC | #42

when my devs wake up ill make sure our repos are made public just for you sir

-------------------------

Dai | 2021-05-13 03:52:11 UTC | #43

I didn't realize GitCoin / community have so many people think of themselves as so "righteous" that they can label a project as they want and reck a community of token holders like nothing happens.

Indeed the tokens are in GitCoin wallet, you can do whatever you want. But please do not use your "fund public good" flag to do evil, that makes me disgusted. Let me put it in this way, you are a venture backed company that tries to pump your valuation in the capital market and one day get rich from building this company, you are NOT a non-profit organization.

Whatever AKITA is, there are thousands of retail investors bought the token. Now you think you can reck these people because you are doing something righteous, and label AKITA a useless meme or scam, sell tokens in exchange for YOUR OWN BENEFITS. Please stop talking about funding public good.

You even mentioned to use the blood money to buy back shares from Consensys and VCs?? And what? Take back control from the investors or what? Is it that if you say something politically correct then you can decide other people's fate?

Are you willing to disclose your identity? If not, I might even think you are a sent by the GitCoin team to test community tolerance. (Notably you said you worked for GitCoin but you didn't participate in any previous discussion, ONLY THIS ONE)

Do NOT talk about "funding public good" any more, I am disgusted.

So, community, what do you think?

-------------------------

Reader_kk | 2021-05-13 03:56:17 UTC | #44

[quote="lefterisjp, post:1, topic:67"]
Remember. Gitcoin’s purpose is to fund open source (and public goods)
[/quote]

Remember. Gitcoin’s purpose is to fund open source (and public goods)
gitcoin is for open source, 
Akita is a meme coin, (after a short read) which aims to move towards real use case, which is built upon open source.  in finance terms, there is a mechanism to have decentralized finance.  Therefore, defi and open source both in one meme token.  meme is their way to do marketing.  behind the curtain, there are hardcore technical coding from open source, possibility of improving to the next version.

i think we shouldn't bash each other like this.  we are both in the open source community.

and.....

a research on https://gov.gitcoin.co/u/Adamscochran which has been voicing out strongly against Akita, sounds like fudding, as this guy joined only 7 hours ago.  if you are not going to make constructive suggestion to the gitcoin community, please stay neutral.  

disclaimer:  I joined 10 minutes ago.  look at my statement and see if what i have said is right or wrong.

to properly handle this huge windfall given by vb, we should first think.  Has gitcoin been surviving with or without vb's contribution?  someone mentioned vb's contribution as tainted money (this guy joined 1 day ago) .  I would say I would like to throw back the tokens back to them or burn them off, solved all the headache. but that's not the right way to manage this situation.  JimWarren joined 1hr ago, so he might be coming from a perspective as Akita token holder. (sorry about that)

when suggesting to dump the token, it is akin to some manipulator in stock market with a huge holding dumping their stock and causing the price to crash.  in the real world, we have regulations to monitor these.  but in the decentralized world, are we going to do this?  I understand this is permissionless and trustless system, you can do what you can with what you have on your hands.  but that would create chaos.  that's why we need governance in blockchain, in cryptocurrency, there is a community voting system. 

planckmatt suggestion sounds good.  for Akita community to offer Gitcoin the same amount of funds if we are to sell Akita token now.  price would possible doubled BUT nobody will be willing to give their token up.  (Akita holders would love you for this)

my humble suggestion:  if we are to sell, for gitcoin to spread the selling over 3 years.  that means 50% of Akita tokens (what we have now) divided by (365*2) 1095.    that would amount to 0.0456% daily.  this percentage is calculated to be the no. 65 Akita holder (quite a big dent already).  These funds are not us to begin with.  even if we get a fraction of it, we could still do good with public goods funding.  and considering the humanity impact it will cause the holder of Akita tokens.  you could say most of them might be degen and moonboy but are we going to judge them and punish them like this?  who are we at gitcoin to do that?  we are not at the level to judge.

the other suggestion is to work with the this relic from Akita, (please confirm his identity by some means that he is the dev - sorry need to factual) to produce a passive income to have funding rolling in for the years to come.  we could say that this is our golden goose.  worse case, we get 1/3 of the funds (hopefully during the period of collaboration, funds rolls in weekly) after collaboration as project fails. 

remember what lefterisjp said: Gitcoin’s purpose is to fund open source (and public goods).  we are both in the open source and now Akita could be our evergreen funding wallet for years to come if we managed it properly.

-------------------------

Dai | 2021-05-13 04:02:27 UTC | #45

Who is this guy @cupOjoseph? 

@owocki Do you know him? If he worked for GitCoin.

-------------------------

Dai | 2021-05-13 04:07:42 UTC | #46

Also, can we stop talking about "funding public goods" for a moment here? It looks like you guys are using funding public goods as something to justify your decisions. Let's solve the problem first before you "fund public goods".

-------------------------

papa_raw | 2021-05-13 07:49:34 UTC | #47

So a few things here:

* Dumping the tokens will rightfully piss off the community that supports them, and it's ethically problematic to pretend that this community doesn't matter (I'm sort of ashamed by the long-timers whose instant gut reaction was to do this)

* We have a funding mechanism to distribute funding at scale. This mechanism has been used successfully with other ERC-20s, such as Panvala PAN token. If you look at PAN, it's not that different from SHIBA in terms of utility.

**Why not distribute SHIBA using the thoughtful and effective QF mechanism in a special SHIBA round?** Why should Gitcoin have to take the moral burden of arbitrating of what's right and wrong, here? My proposed compromise is to push these coins out to the "open-source community" and let them decide using the very same mechanism that's meant to mediate these types of moral distribution issues.

A related Tweet, to help ground our intent:

https://twitter.com/mikojava/status/1392701896238927873?s=20

-------------------------

Reader_kk | 2021-05-13 08:13:15 UTC | #48

another way is to progressively convert bit of Akita , for a start, say 2% out of the 50% to eth, then create a liquidity pool using this initial 2% (in ether) with 2% Akita token. if this solution is a welcome action by the akita community and people are drawn to akita token, thus boosting the demand for akita token, the liquidity pool which we have in 2% ether/ 2% akita will become full one sided 4% ether. 

then we remove liquidity and with our 4% in ether, we go on to add 4% akita to form the liquidity pool of 4% ether/ 4% akita.  this way, eventually we will get 25% ether/ 25% akita.  by that time, we are constantly earning liquidity fees of 1% (listed under exotic asset)

these can be done by bot to detect the full shift to near ether, then bot remove liquidity using uniswap api, then add liquidity as mentioned above, using up more akita until it is a balance of 25% ether/ 25% akita.  

win-win situation for both gitcoin and akita, "nonviolent and solely based on cultures of consent"[Miko Matsumura]

-------------------------

wschwab | 2021-05-13 08:55:25 UTC | #49

I'd like to just try to aggregate and summarize some ideas mentioned until now and add some opinions to them:

## Option 1: Use AKITA for funding

The basic premise of this option is using AKITA to fund the Grants pools. The question is how best to execute this. Communication with the AKITA community is likely something a public-goods group should do - Gitcoin does not have to let the AKITA community _decide_ how much of the funds should be used, nor how they should be used, but communicating with the community about it is likely beneficial. (Though it may require a large amount of patience and compassion.)

Similarly, dumping everything is unlikely to benefit anyone. A slow burn rate communicated clearly is likely to be more sustainable for the AKITA community, and seems more ethically in line with Gitcoin. A potential downside is if there is significant abandonment of AKITA (also called dumping) on this news, but I do not think Gitcoin's goals should be maximization of financial value.

tl;dr if Gitcoin would like to use the AKITA for funding public goods, it should be done on a schedule transparently, and at a burn rate that is more sustainable

## Option 2: Don't Touch It

Mainly inspired by @tjayrush , there is the option of not touching something antithetical to Gitcoin. In this option, Gitcoin should likely either burn the funds or pass the bag back to Vitalik. Finding an AKITA community steward seems an unlikely possibility unless there is overwhelming AKITA community support, which would be hard to gauge imho. Burning should not adversely affect AKITA holders, if anything, reducing supply should make the value of their holdings go up, but is still taking a direct financial choice with the funds. Sending them back would be the most pure way for Gitcoin to wash their hands of the funds.

I am a member of the Ethereum Cat Herders. If there is any way we can assist Gitcoin with whatever Gitcoin chooses, or in facilitating comms, feel free to reach out.

-------------------------

owocki | 2021-05-13 14:16:08 UTC | #50

Heads up - It sounds like PolyGon (who received SHIB tokens from Vitalik), is considering using Wintermute (or a similar market maker) to handle the donations by Vitalik on their side.

This community might want to *consider* engaging them as well.

https://twitter.com/sandeepnailwal/status/1392841766844338176

-------------------------

owocki | 2021-05-13 14:24:34 UTC | #51

Hi everyone, 

[quote="Dai, post:46, topic:67"]
Also, can we stop talking about “funding public goods” for a moment here? I
[/quote]

Just so you know funding public goods is Gitcoin's mission (gitcoin.co/mission) so thats why you're getting a lot of heat about that topic.

[quote="Dai, post:46, topic:67"]
Let’s solve the problem first before you “fund public goods”.
[/quote]

Curious how you'd frame the problem here?

I'm mindful that the Gitcoin community's problem (how do we solve public goods) might be different than the AKITA community (I'm only guessing here but I guess it might be : how do we not crash the market / destroy our pgoress?).  Protocol politics is the art of the possible, so my north star would be [coordinating](https://twitter.com/owocki/status/1392616161360056322) to find a path forward that meets both community's goals.

[quote="Dai, post:45, topic:67"]
@owocki Do you know him? If he worked for GitCoin.
[/quote]

Yes he worked for Gitcoin (the company) a few years ago but does not anymore.  

My 2c as a community member myself: I think it might be fruitful to come up with 3-5 paths forward and put them to a vote.

-------------------------

Root | 2021-05-13 14:33:54 UTC | #52

[Personal Opinion]

I don't have anything against AKITA community, however, I don't think AKITA has any technology to offer where there are tons of similar projects with possibly more added value to the world. 

I think having multiple approaches to vote on is a good idea, but at the same time spending any more time on this means less time on actual development and helping the public good. It might be a better approach to do the all as well:

- Burn 33% of the token help by Gitcoin community multisig
- Liquidate another 33% and distribute between active projects in Gitcoin ecosystem or start new grant programs to help under representative groups
- Send 33% back to the AKITA community (possibly with a year vesting)

![9009f423-0d5f-4d22-911d-f6bed773ca36|353x500, 50%](upload://umZaAmJLmc4McjHr9fuPUdtPGkl.jpeg)

-------------------------

omnianalytics | 2021-05-13 15:30:27 UTC | #53

The solution to this should include as much cross-collaboration with the AKITA community as feasibly possible and socially acceptable. The reality is, $5M isn’t going to create a self-sustaining Gitcoin, but $100M just might. To extract $100M or anything close to that amount, the AKITA community will need to not only mature, but grow large enough to engender market demand that can sustain the multiples of millions of dollars in liquidity Gitcoin would need to support the sale of their position. This reality links, and ultimately aligns, the two communities. Even though Gitcoin has been gifted AKITA’s treasury, the public goods community has something else to offer AKITA , legitimacy. Having a noble purpose to support open source projects takes AKITA beyond just being one of many DOGE-clones into a more sustainable status as the go to coin for those who want to meme and do good. I believe this is the way to maximize the potential of the opportunity given to Gitcoin.

From a practical perspective, after a few basic tweets are published stating that co-community opportunities are being explored and $AKITA holders can be confident there will be no short term dumping of the coin by Gitcoin, then some co-community building begin. This could include:

* A portion of the funds to be allocated for bounties that build and support the AKITA ecosystem.
* A special Round 10 sponsorship by the AKITA community where CLR Matching of $AKITA can be gamified so that AKITA community members have additional sway in the matching.
* Between-round funding initiatives supported by or promoted with AKITA. Considering there isn’t ever much action between funding rounds, this could add a bit of life to the platform during down times.
* Initiate partnerships with educational platforms like [rabbithole.gg](https://t.co/xvVt7SccHC?amp=1) to onboard the AKITA community into the broader Ethereum ecosystem.

**The grand irony in this is that the most valuable thing here isn’t the money, but the access to a large community that could potentially be evangelized and mobilized to work on behalf of open source and the overall public good.** If that’s successful, it literally unlocks a war chest that can be used to sustain Gitcoin in perpetuity. This approach is idealistic, sure, but offers the highest potential reward and since Gitcoin isn't struggling, why not shoot for the moon?

-------------------------

isaac | 2021-05-13 15:25:14 UTC | #54

I have been thinking about this all day, wondering if it is best to sell as much as possible, or to try energise the project (like how sushi devs rugged, before later redeeming themselves and actually contributing to the ecosystem).

The question I land on is why should Akita receive the support from this community to develop it into something meaningful and useful, when there are already so many underfunded, understaffed, and non-meme non-PnD projects out there that could do with the support? 

If we had been just handed cold cash, how would that have been invested? most likely put up as match funds for the grants rounds. We have this ball of energy, with which we can invigorate projects we (the gitcoin grants donors) think deserve it. Does Akita deserve this energy? Is there something more deserving of it?

If akita team is committed to their work then they can create a gitcoin grants profile, explain what they are doing, and be applying for the funding on the same level as all other projects in the space. 

My conclusion is sell as much as you can as soon as you can. There is no guilt here, the money will go into supporting community projects as gitcoin always does.

Even if you sell the 10% for the $5m, you'll still have 90% of the tokens left, you could airdrop them to gitcoin grants donors and then the community might see that as some incentive to do something with akita and give it a reason to have value. 

If the plan is to sell you should act swiftly.  If you wait around for a vote, then as soon as the vote leans towards selling the prices will collapse.

-------------------------

owocki | 2021-05-13 15:48:32 UTC | #55

been chatting a bit with [banteg](https://twitter.com/bantg);  who understand DeFi way more than me.  here are two of their suggestions (neither of which i specifically endorse, just communicating what i've heard)

1. you can also probably try making a limit order on [http://match.xyz](https://t.co/aKmTtXnYiH?amp=1)

2. Make a Gitcoin Endowment Convert them to something valuable using [https://gnosis-auction.eth.link](https://t.co/AAIV5y6iUh?amp=1) Then put it into Yearn and have all the future rounds secured by yield.    we used gnosis auction for token buyback and it was pretty scary because it seemed people don't understand how it works. but ultimately it cleared very close to the market, like 0.2% difference.

-------------------------

jpitts | 2021-05-13 16:02:54 UTC | #56

Selling scam tokens thrown on your doorstep is tricky. To immediately sell is not pragmatic, considering the slippage. To quietly sell a large holding of a meme coin (or possibly even any highly over-valued asset) is unethical; it takes advantage of people potentially being scammed. 

One key thing to remember though: Gicoin owes the token holders and community nothing. A sell operation to DAI should only be bounded by the market mechanics, our general ethical responsibility, and Gitcoin's mission.

It would be good to know from more experienced traders how to do this sell w/ the following constraints: 
1. simplicity
2. general transparency
2. unload it all within a few weeks

**With these in mind, I would propose making the operation public, and selling the AKITA token at regular intervals in blocks that keep getting larger.**

-------------------------

Adamscochran | 2021-05-13 16:51:58 UTC | #57

I think the challenge is that the simplicity, transparency and timeline here all counter act the effectiveness of the trade as the asset is so microcap that it is monopolized by bots, market makers and dark forest types.

Your options are really memory pool bypass swaps, or hoping an OTC market maker like Wintermute or Alameda would take it on for you. Unlike the SHIBA token, ATIKA doesn't have the major markets that those kinds of traders operate on and so I doubt you'd get much.

Since that leaves you on chain you get a MEV/dark forest issue, anything you publish gets front run either when its in the mempool, or manually when announced on a timeline.

I think the balance is to announce that you *are* selling the asset and the intention is clear, but not to announce the mechanic.

I think the social contract obligation of a large holder should be treated no differently than that of a small holder in this case, so I dispute the claim of it being unethical as it isn't Gitcoin who built the project or hyped it. But, I can see middle ground merit in making clear that they plan to sell the token and after that doing as they see best fit for Gitcoin.

The other problem baked into the assumption of many of the users (whom I'd guess are from the ATIKA community) is that they propose other models will work as those models assume ATIKA will be worth more (or anything) at future time X. While I disagree with that view, even then we'd have to consider that a bird in the hand is worth two in the bush.

-------------------------

relic | 2021-05-13 20:18:43 UTC | #58

Reading some of the recent posts I have to say I am mortified. Its literally a bunch of people telling each other how to most efficiently gut our project. This is the reality, every token you extract value from effectively takes it away from someone in our project. 

Our governance model relies on the tokens being out of circulation.


This project has been my life for the past four months.

So I'm just a little startled to see these kind of brutal ideas being thrown around so easily.
 
https://github.com/Polarfox-DEX

-------------------------

omnianalytics | 2021-05-13 20:22:17 UTC | #59

At this point in time, @relic, I think the best thing you can do is provide advice and ideas for Gitcoin x AKITA collaborations. From there, just be patient and let the conversation evolve. It's only been 24 hours, so no need to panic.

-------------------------

nickjohnson | 2021-05-13 23:24:17 UTC | #60

[quote="relic, post:58, topic:67"]
Our governance model relies on the tokens being out of circulation.
[/quote]

Then why did you give them to Vitalik?

-------------------------

castall | 2021-05-14 04:21:17 UTC | #61

[quote="cupOjoseph, post:21, topic:67"]
use these funds to buy equity in Gitcoin the company (not the community) back from consensys and VCs
[/quote]

I think this would be a great outcome if it's possible.  I bet the investors would be in a better position to deal with an asset like this.  I know you want the community to decide @owocki , but we would need your help executing it.  Is it possible in your estimation?

My other favorite option (using whatever is left over after the above) is the one by @papa_raw to **use QF**.  I don't think it needs to be a special round--just an additional matching pool (and additional multisig) with all the Akita in it.  We measure and report matching in terms of Dai, like always, and all the other normal considerations which you can [read about here](https://gitcoin.co/grants/12/gitcoin-grants-official-matching-pool-fund).  The Akita wouldn't be included in the UI estimations for matching--recipients can just consider it a special, unadvertised bonus.  We don't have to set any expectations about how much it will be worth or how recipients should use it.

**Update:**
After talking with @relic on telegram, I've come to learn that they are in the middle of setting up a community or ecosystem fund and that there will soon be ways to stake Akita, so in my opinion we should hold off distributing Akita tokens as part of a grants round until these options are in place.

-------------------------

Dai | 2021-05-14 06:46:02 UTC | #62

First of all, while the GitCoin community is talking about how you can extract value from the AKITA coins, thousands of AKITA holders have already been doomed. Do they deserve it just because they hold a meme token?

Funding public good is your business (every business creates some value, including yours), and you benefit from that. Maybe temporarily you don't benefit from revenue, but you benefit from growing your platform, which gives you higher valuation. So it's definitely not all about "doing good to the world", if I were you, I would think about using this money to secure the company's funding source too. But if the AKITA community is doomed because of you, you have blood on your hand. That's why I said, let's STOP talking about funding public goods for a moment. Communism murdered millions of people, but in the first place they had good cause -- to improve public goods too.

It looks like your community is talking about how you can use OTCs, Defis to extract value while trying to ignore the problem of AKITA community. When you are discussing it, they have already lost so much money.

Having said that, I do think there are some ways you can work with AKITA community. There are a few possibilities moving ahead.

1. dump the tokens and extract cash from it -- blood is on your hand.
2. work with @relic and AKITA team, come up with a common goal (including funding public goods of course), and make AKITA a token to support public goods. 
(Note that GitCoin team might want to issue token (or maybe not, who knows) but you don't have a good excuse to do it, it's an opportunity to convert a token that works for your goal, without having the burden to be a token issuer. But, you do need to design a token economics that actually works, so that it has some real utility)
3. If you can't work with AKITA team in the end, you should probably just return most of the tokens back to AKITA community and as @relic mentioned, they would like you to keep 10%, which is good enough for you guys to secure enough funding to "fund public goods", by whatever means (OTC, yield farming, Gonsis auction, bondingcurve, whatever) I see previously discussed.

After all, being sanctimonious is disgusting. But if you take care of the AKITA community FIRST, there are several path you can take to move forward.

-------------------------

isaac | 2021-05-14 09:16:17 UTC | #63

Part of the issue i see is that "working with akita community" doesn't just require us to do nothing, it means the gitcoin team and community now have to start working on this thing they never asked for. There are already hundreds of other projects in the web3 ecosystem which that energy could be put into supporting.

We have to ask, does akita as a project align with gitcoins aims? If we were to support akita what are we actually supporting? Has anyone read the contract code? Do we know anything about the token distribution or authors? Apparently it is a fork of shiba, so do the devs even code? Can they responsibly manage this project if it got bigger? 
What are the values of the project? because it looks like a meme token intended to try and pump and make some people rich, is that what gitcoin and the community want to support?  Is this the most deserving project for these funds? Or is it a big distraction that will sap a lot of time and energy?  

If we were to work with the akita community I would want to see them signal their intentions by having large token holders and devs place their tokens in a vesting contract locked up for a few years. We would need to see a plan of what they are working on and importantly understand if they are capable of delivering. We treat this like an investment and it is up to akita community to prove to us that they are worthy of this investment and can deliver real value (not just money) to the wider community. 

So far I am not convinced investing in akita is a better option than investing in all the other projects around that could do with the funds, the developers, the community energy. But I'd be very happy to be proven wrong, to see a clear roadmap, with beautiful intentions for society behind it, with the best developers and designers offering up their talents in support. If that doesn't happen soon then we should just sell the tokens and carry on with our work.

-------------------------

Dai | 2021-05-14 09:25:53 UTC | #64

If you don't work with AKITA community / team then you should NOT sell the token and you should return most of the tokens to AKITA community, and carry on your work.

Again, don't think of yourself so high that you can be the judge of another project. Maybe you are doing something you think worth a thing (oh, again, "funding public goods"), you do not decide another community's fate.

-------------------------

HelloShreyas | 2021-05-14 11:22:18 UTC | #65

> Convert them to something valuable using [https://gnosis-auction.eth.link](https://t.co/AAIV5y6iUh?amp=1) Then put it into Yearn and have all the future rounds secured by yield.

I like the idea of trying to sell at least a portion (~10%?) of the AKITA proceeds via Gnosis auctions. It should be straightforward to do. I'm in touch with the Gnosis auctions team and they'd be willing to help. The largest auction they've executed so far is for Boston Protocol, for which they ended up settling $26m. We will have to run multiple auctions to execute a larger trade.

Putting the proceeds of the Gnosis auction sale in a Yearn vault is an extra step - we can discuss this after completing the auction.

@Adamscochran brought up the point of being front run / sandwiched:
> I think the challenge is that the simplicity, transparency and timeline here all counter act the effectiveness of the trade as the asset is so microcap that it is monopolized by bots, market makers and dark forest types.

Batch auctions enable matching of limit orders of buyers and sellers with the same clearing price for all participants. So they are designed to reduce the risk of frontrunning, gas bidding wars, and lower the amount of extracted value from auctioneers and bidders.

-------------------------

makoto | 2021-05-14 12:22:50 UTC | #66

How about sending back to Akita community in exchange for receiving some amount of donation  (in other words, OTC trade back to Akita community)? I sort of agree with @tjayrush that it's tainted money and no need to maximise the profit just because Gitcoin posses these tokens. Having said that Akita community made a silly decision to send it to Vitalik as a burn address which they should pay a price for it as well as the marketing exposure they received through the incident (plus wasting all stewards time which should be spending more on more meaningful discussion).

-------------------------

personofnointerest | 2021-05-14 14:09:08 UTC | #67

The original dev sent 50% to VB as a burn, in line with all the other dog memes back in February. Relic and the rest of the Akita community involved since that dev left have picked up the pieces of a burnt out project and actually gave it some inherent value and have tried to work towards utility beyond the original meme and build a collective resonance along the way. The people involved in Akita now did not use the VB burn as a marketing ploy, we are simply living in the ramifications of something out of our control.

-------------------------

GarrettBlanche | 2021-05-14 14:43:50 UTC | #68

I am seeing a lot of discussion around dismissing AKITA as a legit project but using the funds anyway. The result will destroy the lives of 41,000 current holders of AKITA. What kind of hypocritical message does this send from Gitcoin as a community? For a community that serves the public good are we really going to destroy another one in order to do this? The means do not justify the end in this case. 
The solution is simple. Take a small percentage of the holdings and burn the rest. Release a statement corroborating this and acknowledging the AKITA community for their donation. Both Gitcoin and AKITA walk away happy.

-------------------------

Dai | 2021-05-14 16:12:05 UTC | #69

I think the GitCoin team and people close to them do have shown they want the money badly. If nobody brings the fact that AKITA community can be (and in fact has been) destroyed, they will most likely to cash out the tokens and feed themselves for "FUNDING PUBLIC GOODS".

The guy @relic offered 10%, obviously GitCoin wants more. They didn't even respond to it, only talking about how they can sell the tokens to maximize their interests, because they will use it righteously to "Fund PUBLIC GOODS".

We are living in a world if you say you "FUND PUBLIC GOODS", you can do anything.

-------------------------

tjayrush | 2021-05-14 16:16:11 UTC | #70

[quote="Dai, post:62, topic:67"]
But if the AKITA community is doomed because of you, you have blood on your hand.
[/quote]

As soon as the narrative begins to turn to this sort of sentiment, it becomes very clear to me that the best way to make sure GitCoin does not "have blood on their hands" is for them to wash their hands of this whole issue. Send the tokens back to Vitalik--not today--not tomorrow--yesterday.

(Just to be clear, I do not agree that GitCoin will have blood on its hands no matter what decision is made -- I'm making the point that the narrative is getting twisted and will only get worse.)

-------------------------

relic | 2021-05-14 16:27:03 UTC | #71

5% of our supply was burned on top of what was sent to Vitalik.

The way I see it is, if we stay within that 5% we can still keep a total of 50% of the supply burned as investors originally thought was the case. 

Our team has been self funded this entire time. We have picked, scraped and scrounged up what we could with what we have.

I'd humbly ask that we split this 5% in a fair way, I think 3% to the stewards and 2% to the AKITA network fund would be fair. 

Gitcoin recieves more because we are the hitchhikers here.

Burn the rest.

Get on with our days.

Just dont dump that 3%, help us grow as a community and you can see that 3% turn into alot more.

Memecoins are the trojan horse of the mainstream to web3.

-------------------------

owocki | 2021-05-14 16:51:23 UTC | #72

[quote="castall, post:61, topic:67"]
I know you want the community to decide @owocki , but we would need your help executing it. Is it possible in your estimation?
[/quote]

i'm not sure, but i chat with Mike Kriak (who is our board member who represents Consensys's interest in Gitcoin) next week + take his temperature.

Can you say more about why this is important? ( I think I know but just to hear it from you and @cupOjoseph  )

-------------------------

personofnointerest | 2021-05-14 18:00:17 UTC | #73

I see an element of truth in this. This is my first time coming across Gitcoin due to VB's transfer of Akita to your multisig and I can't help but think some of the people involved in this project have some very insidious outlooks that on paper go against the ethics of your objectives;

"Connect with the *community* developing digital public goods, creating financial freedom, and defining the future of the open web."

"Open source code meets open economies. Build resilient projects, better coordination, and *positive-sum outcomes*."

"Growing networks with aligned incentives towards the *wellbeing* of each participant and the system as a whole."

"Through distributed funding and organizations, we build together toward our *shared goals*."

To me, if ~40k holders (at the time of writing), experience severe detriment in order to fund Gitcoin's mission, is that mission, it objectives and the means of which it carries out to achieve those objectives, genuinely consistent with how Gitcoin publicly presents itself?

[quote="omnianalytics, post:53, topic:67"]
The grand irony in this is that the most valuable thing here isn’t the money, but the access to a large community that could potentially be evangelized and mobilized to work on behalf of open source and the overall public good.
[/quote]

I think this is quite an insightful and shrewd outlook. Money is a resource to leverage access to other tools – an audience that can be leveraged also has inherent value which produces its own ROI.

-------------------------

castall | 2021-05-14 19:29:28 UTC | #74

My main reasoning is that there are several exit scenarios that make investors happy, but the only scenario I like regarding Gitcoin is long-term sustainability. They may be quite excited about getting Akita tokens, whereas we seem to be divided about it.

-------------------------

Adamscochran | 2021-05-14 19:32:13 UTC | #75

I think one part I do agree with is that it would be ideal to try and find a way for the Akita holders, many of whom had no idea what they were getting into, to get some benefit out of the action (such as returns from any productive asset this results in)

I'm not sure how you do that gracefully, if it is a necessary recourse or if it helps good actors at a greater rate than bad actors.

You could also airdrop half of the amount proportionally to holders which would dampen a sale effect of the remainder but still be a logistics nightmare. If you were going to do that, it could also be done on a dampened curve so it helps the little guys more than the major holders.

The situation all around sucks, and I'm not sure there is an outcome that is of perfect benefit to both parties, in fact I don't know if there is an outcome that is perfect for either party. I think it might be just finding the ones that suck the least.

-------------------------

relic | 2021-05-14 20:43:02 UTC | #76

The perfect solution is the most simple one. 

You found our wallet, sorry we accidentally mailed it to the wrong address! (yes I understand it was intentional albeit not by the party in question).

Thank you for finding our wallet, here is your reward. Please keep more of it than we will keep for ourselves.

BUT, it is imperative that the investors of AKITA get back to having 50% of the supply burned.

We can only do this by staying within that 5% window.

If it comes down to it, we will continue self funding and gitcoin can keep the entire 5%, just please burn the rest.

I'd love a solution where our community becomes informed about the importance of public goods funding and chooses to fund it organically without being "forced".

That organic funding should come from this finders fee so to speak. Over time the funds can be liquidated and the AKITA community pays our way out of this mess by funding public goods.

-------------------------

calbear4life | 2021-05-14 20:49:00 UTC | #77

The worst thing you could do from all angles would be to sit on the decision. So much value destruction…

-------------------------

Dai | 2021-05-14 21:33:22 UTC | #78

It's weird that @owocki doesn't reply to your message. Why?

You do have a proposal, but no reply from GitCoin, not even a comment. What is GitCoin thinking?

Looks like your tokens have fallen into the hands of a mixed group of special interests, and GitCoin founder needs to consult with his BOARD MEMBERS and decide how they can deal with your funds. It looks like AKITA community does not have any priority here.

So it looks like there is a BOARD OF DIRECTORS behind the "FUNDING PUBLIC GOODS" scene. Let's see which is more important to the board -- GitCoin's valuation, or find out a solution that actually can help AKITA community. If they can put the interest of AKITA community before themselves, I'm sure they can find a solution that would greatly benefit GitCoin as well.

-------------------------

Mantarochen | 2021-05-14 21:55:46 UTC | #79

For the Akita investors as well as the Akita project team it would be just fair to leave them as much of their token supply as possible. It was supposed to be burned and gone forever and on that basis every investor took the decision to support the project. 

I respect that you are willing to use gitcoin to support public needs but endangering the investment of tenthousands of small people should not be the way.

-------------------------

relic | 2021-05-15 01:46:19 UTC | #80

Nah, I fully trust in the gitcoin founders and their decision making ability, I'm just posting here to publicly state what I think the best solution is going forward. 

They don't owe anything to us. Not even the time they are taking away from their lives to deal with the situation, I respect the hell out of these guys for their contributions in the space.

I have 100% confidence in the situation being resolved relatively quickly with minimal drawback for either side. I actually think we will both benefit from this weird/awkward situation.

-------------------------

SHUSKY | 2021-05-15 04:46:16 UTC | #81

⬆️ This is the best comparison I’ve read in regards to this. I can’t imagine finding a wallet with money in it and keeping it knowing that it would effect the owner(s) of it in a very negative way. 

Burn the rest of the tokens and accept the gracious offer made by relic. I trust the gitcoin community to do the right thing and not destroy 40,000 (mostly small investors)...we are real people from all over the world..moms, dads, college students etc. 

These investors are every day people like myself...who believed in Relic and his team to take over an abandoned “memecoin” and turn it into something of value and real life use. 

Why do you feel you get to decide our fate? Let our project speak for itself. I definitely wouldn’t want the bad karma on my hands if it were me in your position...please choose wisely.

-------------------------

Yalor | 2021-05-15 07:05:24 UTC | #82

This is the kind thing I've been wanting to see mentioned, I really appreciate thoughtful and dignified responses. 

I hope some of these new folks from the AKITA community know that our Team @ Gitcoin has an entire eco-system of actual public goods projects in motion. We are running hack-a-thons, accelerator programs, and an entire bounty network that cannot be put on hold will we deal with this AKITA situation. 

Secondarily no one has ever accused us of "Using Public Goods" to extract value from other communities or to harm anyone in any way. That being said we didn't ask for this responsibility, not @owocki , not the community, not me and I will not apologize for taking our sweet time to make the right decision that protects our community and ensures that we are taking the voices of others who might be affected into consideration as well. 

We have spoken with @relic and we are discussing various proposal's as we speak. I am impressed with the fervor that you guys bring to the table trying to get this thing done, but please DON'T COME TO OUR COMMUNITY FORUM AND START TALKING SHIT ABOUT OUR FOUNDERS !!!!! 

**That's all I will say about that.**

-------------------------

simonc | 2021-05-15 09:37:34 UTC | #83

As part of the Akita community I first of all want to say a big thank you to relic and his team that have worked so hard on our behalf both before and during these challenging times 

There is clearly a lot of fear felt by the Akita community at the moment that can lead to emotionally lead comments being made - however, I personally have faith that the team at Gitcoin will work alongside Relic and the team at Akita to find a solution that works for both sides and allows all to grow together in achieving our aims.

I want to thank all involved - both in Akita and GitHub - for taking time out in their lives to give this matter the attention and careful consideration that it requires.

🙏🏽

-------------------------

owocki | 2021-05-15 16:31:17 UTC | #84

Hi everyone,

Thank you all for posting your thoughts here.  I have mostly been listening + digesting the conversation, trying to prioritize the community voices - and be a voice that encourages digesting information + prioritizing deliberation over hasty decisions.  I've also been spending time getting to know AKITA core team and token holders, trying to understand what drives them and drives the project.  (It is our [mission](gitcoin.co/mission) at Gitcoin to help builders build/fund the open web, and unpacking this situation is kinda a part of that IMHO)   By understanding each other, we can understand if there is a foundation for a positive relationship between the two communities in the future.  

Maybe at some point I will write up a post that tries to synthesize what I've heard and/or laying out where/how to vote on this, but even if I do that I want to again emphasize that this is the community's choice, and not Gitcoin Holdings (the company).  I do not plan to put my finger on the scale, but I think one role I'm being asked to play by a few of you is helping create consensus on how we could get to a decision that has any finality (this discussion is our first big debate on this forum, so some precedent needs to be set).

In the meantime, a few people have asked me why Vitalik sent Gitcoin the tokens.  With his permission, I'm sharing a screencap of something he sent me the morning of the transfer.  I'm not sure if this adds to the discussion or not but a few of you have asked so figured I'd pass along (again, only with Vitaliks permission am I sharing this)

![1|356x246](upload://5MAL04cqw3nOprqwewIXKFCcfCa.jpeg)

[Remember to breathe](https://twitter.com/MrBUIDL/status/1326242643614044167) people, 
@owocki

-------------------------

Adamscochran | 2021-05-15 20:59:26 UTC | #85

As a separate and general rule, I think that the matching pools should always just be ETH or stables.

Using other tokens in matching is going to open up a can of worms where its seen as an indirect endorsement and you're going to have everyone donating newly minted coins for matching.

-------------------------

scco | 2021-05-15 23:19:19 UTC | #86

isnt vb solving the freerider problem with this move ? taking from speculators that totaly knew the risk - giving it to the people that build their wallets, exchanges, chains and favorite websites  ... 

im ok using these tokens for grands - as vb suggest with the donation - BUT it would be awesome to keep 1% to  ensure gitcoins bright future.

-------------------------

Reader_kk | 2021-05-16 16:22:34 UTC | #87

QUESTIONS we would like to ask ourselves:

1) why wouldn't vb sell the tokens to usdt and donate with usdt?  he got lots of people to help with systematic liquidation and slippage issue.
2) vb send over shiba token to covid-relief, with the situation that shiba is in binance listing, capable to stay afloat no matter how big the liquidation from covid-19 relief is.  there will be people doing future shorts on shiba and profit from it and using the profit to pump back to shiba to profit again.

OBSERVATIONS from vb action:

1) shiba and akita experiences sharp decline partly from these vb actions and doge decline.  Do take note that as our discussion drags, our value in Akita reduced by a great percentage.
2) a crypto group in twitter started an action against ethereum as retaliation for "rug pulling" shiba. gathering size is currently a small 883, compared to 124k shiba telegram channel members.  other group not monitored yet.

ACTIONS and possibly consequences:
1) - sell all, killing akita in the process, 
- hate group will be there waiting.  generating 43k of Akita holders as hater at an instand.  I hope they are not in our ecosystem, don't like to deal with sabotager popping up out of nowhere.
- we can forget about funding public goods, we have become a destroyer while we should be a creator.
- even if the akita hate group don't boycott us, our competitors with a better image will rise up. (but we have a huge injection of funds now) 
- our image tainted.

2) - part sell part hold.  
- systematically sell a portion of Akita token to get our fundings, over a few years.  Risk: if Akita crashed to zero in the next few months, we get near to nothing.  Reward: if Akita token value rises (need to consult reliable trader to get a sensing), we get a funding machine for a longer period (more years), or we can increase our systematic amount to sell, maintaining healthy trading chart.
- if we decide to sell, we should not broadcast our decision here.  it will cause panic and the result of it, before we can even sell a single Akita token, is that the value drops to worthless in 3-5 minutes.   to get a  sensing of crypto, I joined several telegram crypto channel and fud is a serious issue that spread like wild fire, having the ability to destroy 99% value in an instant.

3) - special funding segment : fund public goods in Akita tokens, telling them that this will be the currency in use and condition that it should not be cash out for the entire duration of sponsor by themselves.  big ticket items should be paid in Akita tokens and that vendor (furniture, computers.  advise to vendor Akita is currently illiquid and there are slippage, thereby a premium will be paid to vendor) are allowed to cash out by themselves (gitcoin->sponsor company->vendors).  payment of salary to employees should be time delayed/locked for a period of 6months (6 months for Akita to recover to pre-vb saga or crashed).  internally, company could pay employees 
82.5%cash/20%Akita (2.5% risk premium for employee's benefit)
65%cash/40%Akita (5% risk premium for employee's benefit)
47.5%cash/60%Akita (7.5% risk premium for employee's benefit)
30%cash/80%Akita (10% risk premium for employee's benefit)
12.5%cash/100%Akita (12.5% risk premium for employee's benefit)

of course these risk premium can be adjusted accordingly as their HR's preference to attract talent.

4) return all token 
- defeat the purpose of vb sending it to us in the first place, but
- if we do not want to deal with the "hands in the blood", we could send it all back to him, tell him it is difficult for us to deal with this matter and could he send us usdt instead.
	- if he don't send, we get on with our lives.  lost a great opportunity to regain our control of gitcoin from vc.  alternatively, he might send Akita tokens to covid-19 relief.  the other side has a mandate and noble reason to sell off shiba to cash for the emergency issue they are facing.  our side don't have that emergency urgency to liquidate Akita token to cash but we face the risk as mentioned above if Akita token crashed to zero in the next few months.

all eyes are seeing how we handle this issue.  how we can progress forward will depend on the vote.

another is to for both Gitcoin and Akita to request for binance listing.  listing might not be good for Akita as usually price will crash on the first minute, but we get to sell our token progressively without slippage.  The visibility from vb's action has propel both Shiba and Akita, therefore as head of Gitcoin and Akita, do have a talk with binance.  nothing to lose.

-------------------------

personofnointerest | 2021-05-16 22:54:13 UTC | #88

Well VB's recent move with the remaining Shiba in his possession is certainly interesting. https://etherscan.io/tx/0x7a69f558bdc4aaf1e6bab9473c84cb2fddbd1e419c44d5c22eb88bedeb09657c

I think this needs to be weighted in as part of a wider, yet highly relevant context, to the decision making. I'm personally all for seeing Akita playing a role in contributing to open web and a percentage of the supply acting as Gitcoin's funding machine (as suggested by @relic) ensuring that the value of Akita remains beneficial for current and long standing retail token holders and Gitcoin alike.

![E1ipsVIXEAUyljH|690x292](upload://tNqlUAHhK8V1qE8rh0d3xMM3sSY.png)

-------------------------

GarrettBlanche | 2021-05-16 23:10:54 UTC | #89

So Vitalik burned the rest of his SHIB supply and kept 5%. I believe this is similar to one of the proposals on here. This seems like a clear path forward to me.

-------------------------

sviss | 2021-05-17 02:10:48 UTC | #90

From owocki's screenshot of his conversation with VB, and VB's burning of the Shiba tokens today, VB's intent for the dog coin communities is undeniably clear. There was a ZERO-PERCENT chance VB was ever going to rug all those fresh entry-level retail investors on his own network. To those who thought this was probable, or even possible – please, get out of investing and finance – your judgement is nonexistent.

Like many others reading this thread, discussing amongst the other hundreds of thousands of members of these dog coin Telegram groups, we were appalled and horrified to read how casually and flippantly the idea of dumping on all of us was tossed around here. "Sanctimonious" is the correct word, as stated by another user in response to Adamscochran’s brutal half-baked proposals which were never an option, and would never have worked.

Adamscochran’s emotionally vacant “fire and brimstone” proposals were beyond “disgustingly sanctimonious”, as stated. They were truly sociopathic (lacking any semblance of actual empathy for the tens of thousands of innocent investors affected by his heinous plans, which he justified to himself through sheer mental gymnastics, stating that the victims were already victims for investing in an “inferior” asset, so why feel bad for going ahead and MAKING VICTIMS OUT OF THEM), hypocritical (“dumping is bad, we've all been rugged, but let’s dump $AKITA”), and completely antithetical to Gitcoin’s stated mission and purpose for existing (“we’re so good and great, let’s do something unimaginably evil to others to raise money to carry on with our work being so good and great”).

Indeed, patently **disgusting.** A textbook example of the ruthlessness of the powerful!

Back to the future of $AKITA and Gitcoin. Half of something worth nothing (and illiquid at that) is worth nothing. But a sizable majority portion of something with widespread popularity, adoption, and enormous value is worth a significant fortune. THIS is and was the only way forward for Gitcoin.

I am extremely relieved VB has finally broken radio silence on the matter, and I trust owocki and others I’ve heard from in the Telegram groups will follow suit disclosing the fantastic plan for Gitcoin’s $AKITA tokens which was communicated to relic, myself, and others.

For those of you who can’t yet see – these dog coins are an entry-portal into the world of DeFi, the systems you're building, and the future of money. It would be absolutely insane to discourage this in any way. You’ve got lightning in a bottle right now, and with proper INVESTMENT (vs. cashing out for a tiny fraction), you will have a very powerful source of funding for the foreseeable future, as intended by VB, and supported by the $AKITA community 100%.

-------------------------

Enrique | 2021-05-17 03:54:01 UTC | #91

I personally believe it's best to create some sort of participation incentive for the community. 500m worth is plenty and should be divided in ways where community members marketing can be rewarded, as well as community members who've never sold a token from their wallets. Whatever the case, we should separate those who only want to short the market, from those who have long vested interests. My reference is ampleforth and how they chose to airdrop their gov token.

-------------------------

calbear4life | 2021-05-17 03:55:45 UTC | #92

The way Akita is being framed is as just another meme coin and compared to the other donated coin is tragic to be honest, There is a strong community brewing with lofty goals with solid intentions and work ethic displayed by their team. It is a sad destruction of value, for zero reason.  What has been mentioned about the actual project pipeline? How has the community been engaged to spur and create ideas? The communities should be voting together as one.

-------------------------

Rust | 2021-05-17 07:39:01 UTC | #93

The events that have unfolded over the past couple of days all feel like one big social experiment that are pushing the limits of the Crypto community. I do not think this was Vitalik's intention, but regardless this is where we are now.

I think there is only one solution here and that is a solution that wouldn't benefit Akita directly nor would it benefit the Gitcoin community directly. The solution here would be to not cause any more harm to the Crypto community that has already been done and I believe that Vitalik sending the AKITA to Gitcoin was in line with his trust in the teams here that they would do the right thing with it and not be blinded by personal greed.

We are all in this space for the same reasons at the end of the day, whether you're from 1 end of the spectrum where you're gambling on memecoins or whether you're on the other end where you're trying to find elegant solutions to real world problems. Now is a time more than any other where we need to stick together and workout how we can leverage this sticky situation to our advantage.

There are already some positive things that have come out of it such as the exposure Gitcoin and Akita have both received. We need to double down on that and show the World that the crypto space, despite all the rug pulls, scams, hacks, and other malicious activities, there are some very reliable people in here with a good hearts and that movement can start with Gitcoin. 

At the end of the day the tokens are tokens, whatever is done with them is secondary to the intention of the man controlling what is done to them. 

My solution would be for Gitcoin to control these tokens as a sign of good faith but not to sell them. If AKITA can trust Vitalik with them, surely there is more re-assurance in keeping them with Gitcoin in a multisig rather than just keeping them in the hands of 1 man. 

**How does Akita benefit from this?** Holders would sleep well knowing that ~50% of the supply is being held by some of the most trustworthy and informed people in the crypto space. We can leverage this to our advantage by marketing "If Gitcoin is holding, I'm holding". 

**How does Gitcoin benefit from this?** The exposure as being the de-facto Governance over crypto projects. Hell, I had no idea what Gitcoin even was until this entire thing played out but I'm glad to have now seen that such a community does indeed exist. I can see a future where tokens launch and send tokens to Gitcoin's address instead of a burn address. Why? Sending a portion of their supply to a burn address is an irreversible action and with the progress that the Crypto industry makes every day there are always elegant solutions around the corner. Sending half your supply to a burn address is a fix today, but not necessarily the best solution in 2 years time. 

So why don't tokens just keep 50% of their supply in their team wallets? Simple, I'd trust the Gitcoin community easily over any project that launches and keeps the tokens with them. Having Gitcoin control 50% of the supply is an investment into the future of Crypto and not just the token in itself. 

**How does Crypto benefit from this?** This one is pretty self explanatory but by seeing these acts of kindness and a show of how different communities can come together as one, it would create a much stronger bond within the space and would make good publicity. 

Yes, Akita is a memecoin (Or at least started as one) but that doesn't mean we can disregard their  huge community and hurting them will only be doing damage to the greater sum of this space.

The only caveat I'd have with this solution is that 50% of the supply isn't necessary for Gitcoin to hold and doesn't really bring any inherent value over holding 25% of the supply for example. AKITA holders are hurting so a proposal would be to burn 25% and keep the remaining 25% within the Gitcoin multisig until a more elegant solution is minted.

Thank you for listening to my TED talk.

-------------------------

isaac | 2021-05-17 09:52:29 UTC | #94

[quote="Rust, post:93, topic:67"]
The exposure as being the de-facto Governance over crypto projects. Hell, I had no idea what Gitcoin even was until this entire thing played out but I’m glad to have now seen that such a community does indeed exist. **I can see a future where tokens launch and send tokens to Gitcoin’s address instead of a burn address.**
[/quote]

I dont think we should be encouraging that at all. We do not want more projects started sending half their supply, leaving us with a loaded gun pointed at their head. Its lunacy.

I do worry that if we start legitimising meme projects, especially out of some guilt trip, it could lead to more hurt than selling the tokens now. I can see the "its supported by gitcoin" comments in the PnD telegram chats.  We hear a lot about how we'd hurt akita holders, but the damage to gitcoins reputation could be much worse. 

being "kind" to the akita holders could have an upside of introducing them to gitcoin, bringing lots of new faces, that could be cool! 

But we could also be saying to them that meme tokens are valuable, having no plans can make you rich and happy. We would be saying that buying a token designed with no purpose and with half the distribution sent to one person, was a great idea! and is fully supported by the wider community. 
why would we do that? because its funny? is that good enough? what if we end up hurting more people in the long term?

-------------------------

sviss | 2021-05-17 19:05:24 UTC | #95

[quote="isaac, post:94, topic:67"]
what if we end up hurting more people in the long term?
[/quote]

This sort of top-down tyrannical paternalism is always folly.

"Paternalism: the policy or practice on the part of people in positions of authority of restricting the freedom and responsibilities of those subordinate to them in the subordinates' supposed best interest."

Is dumping the tokens in ANYONE'S best interest besides Gitcoin's?
No. So let's not pretend.

Destroying others in order for you to get ahead is what it has always been: robbery, looting, and pillaging at worst - parasitic vampirism at best.

Back to the folly of paternalism: It is not up to any one of us to censor the entire cryptoverse in the way in which we alone see fit. This sort of unilateral action (not supported by anyone but you) is myopic, tyrannical, and stifles innovation - everything Gitcoin is supposed to be against!

The whole reason the cryptosphere is so attractive to many is because it's a new frontier! It's freedom! 

In a world completely bogged down by overreaching big government and corrupt institutions - you actually propose that what crypto needs is our freedom to be restricted in these various ways you alone see fit? 

I am here to tell you, you could not pick a more assured losing strategy if you tried.

And to the point: No one is asking you, Gitcoin, or anyone to "legitimize" meme coins. They are already legitimate! Look at their widespread popularity! You can't argue with market forces. Supply will rise up to meet demand - period. All we are asking you to do is not destroy $AKITA. That's it. No straw man fallacy about legitimizing memes or leading the ignorant masses to their doom. That is not what's on the chopping block here. It's the future of $AKITA. Will you act as stewards, protecting and nurturing your windfall and our investment - or will you plunder us, at the expense of tens of thousands of innocent people?

No one - absolutely no one - views these sorts of high-volatility meme coins as assured pathways to everlasting wealth and happiness. Notwithstanding the fact that $AKITA has a real, actionable plan to become more than just a meme coin, and an extremely strong and passionate community to help assure that becomes a reality - these sorts of speculative coins are **fun.** Period. The ups and downs give you exits and entries, allowing newcomers with limited patience and risk tolerance to play the game within a timeframe that is acceptable to them. Without the volatility, the game would not be fun - and **no one** would be interested. You'd have a fraction of the newcomers you're seeing coming into crypto right now. And this would be a net-negative for Gitcoin and crypto as a whole.

Do you know how many people are still out there who have no idea that their life savings is being inflated away? And that the permanent, unstoppable upward trend of crypto asset values is as much the debasement of their fiat currency as it is the success of crypto? 

These people will open their eyes voluntarily, in their own time, as they are able to see more and more. You need to create as many doorways as possible to let them in. And you need to roll out the red carpet at each of these doorways and present crypto in a way that is appealing to the tastes of whichever individual may be walking by. This means variety. Yes you have your blue chip "investment grade" coins, and your idealistic utopia projects. But you also have fun things, interesting things, promising things, risky (exciting) things, etc.

Take it from a businessman: curb appeal matters. You have to have ways to draw new customers into your store. This is what the meme coins are doing.

If you want people to care about what you're doing, you need to attract them here in the first place.
You catch flies with honey, guys. Honey! Not vinegar.

Again, as a businessman, I am here to tell you that you can not fight market forces. Customer demand wants what it wants, and supply WILL rise to meet it - whether you're the supplier or not! Whether you agree with it, approve of it, or not!

If customers want cheeseburgers, it is not up to us to tell them that steaks are superior!
Our job, as businessmen, is to create value for the customer by solving their problem with the most affordable solution (the best cheeseburger for the money).

Meme coins are that. You can not argue with popularity. The market has spoken = the People have spoken. And let us not forget what happens when the people grow unhappy with those in authority.

It is not up to you, me, or anyone to try to steer the whole world of crypto to suit any one of our individual visions. This is no "guilt trip". The consequences here are as real as it gets. Please, have some reverence for the significant burden of responsibility placed upon you at the moment. The fate of tens of thousands is literally up in the air right now, waiting for your announcement. Look at what happened to $AKITA's price last night when the news of VB burning the Shiba tokens got out. We are all waiting with bated breath.

Will you act as good stewards, or will you plunder us?
The world wants to know. I hope you'll choose wisely.

-------------------------

Vega5 | 2021-05-17 19:46:04 UTC | #96

https://megalink.app/akita-inu

This shows  that Atika Inu is not just a meme coin - it is this belief that the investors have hit behind

I believe they should be allowed to fail or succeed off their own merits

-------------------------

isaac | 2021-05-17 20:20:44 UTC | #97

> Is dumping the tokens in ANYONE’S best interest besides Gitcoin’s?

yes, literally hundreds of projects could benefit from these funds in the next gitcoin grants round. Too many to list! https://gitcoin.co/grants/explorer/

Akita devs could participate in a grants round and compete for funding the same as everyone else, based on the quality of their work, that seems fair doesn't it? 

> The whole reason the cryptosphere is so attractive to many is because it’s a new frontier! It’s freedom!
> In a world completely bogged down by overreaching big government and corrupt institutions - you actually propose that what crypto needs is our freedom to be restricted in these various ways you alone see fit?

freedom to send half your supply to a single person. freedom to donate them towards a community funding public goods. freedom for that community to sell them, or do whatever it determines is the best use of those funds for itself. freedom to collaborate on ideas too, if anyone has any creative and novel suggestions.

> Notwithstanding the fact that $AKITA has a real, actionable plan to become more than just a meme coin

This is very important. What is that plan? Can anyone show anything to us? code? design documents? if we consider this an investment in a roadmap, then where is it? can we review it, critique it, improve it? are the devs dedicated enough to that vision to lock up their own tokens in a vesting contract? how about the community, will they lock up in a vesting contract? you seem dedicated, will you lockup your funds like you are asking gitcoin to do? are we assured devs are capable of managing a project with many millions of $ of gitcoins funds on the line? what is their track record like, can we trust them? Do they share the same values?

Vega5 posted a link whilst i was writing. Seems like they are making a dex on avalance? and one sentence about decentralized social media?
Details would be great... Looks like another uniswap fork? why is it called polarfox? Why is there a separate $fox token for governance, and how does it relate to akita? why is the git repo empty? why did you choose avalanche over other chains? 
I joined the discord but it seems people are only talking about the token price and exchange listings, as i kind of expected. I am surprised how little conversation there is about gitcoin being sent 50% of the supply... why hasn't an announcement been made to the community? honestly, it looks like the usual pnd token, like the hundreds of other cloned tokens. I really don't get why we should be supporting this.

> But you also have fun things, interesting things, promising things, risky (exciting) things, etc.

We can fund hundreds of projects, toys, hackathons, using the tokens that have been donated to us. Or we could fund akita? 
Just asking questions before we give up a lot of money for a meme.

> It is not up to you, me, or anyone to try to steer the whole world of crypto to suit any one of our individual visions.

Yes that is why we debate, and develop funding methods like QF to ensure that public funds are distributed in the way the public want. Maybe it would be best if we made use of the mechanisms we have available to distribute these funds, and the people can decide who should get them.

> Let us not forget what happens when the people grow unhappy with those in authority.

There is no authority but yourself :)

-------------------------

OliverS | 2021-05-17 22:59:53 UTC | #98

It's clear, based on the telegram chat, that most $AKITA holders have no idea what’s going on in the background. They see meme coins as an opportunity to make a quick buck and are more focused on getting the next listing than the real issue at hand. This is a shame but Isaac I think you've been in the space for too long and forgotten what it’s like to be the average person venturing into the unknown. Let me explain.

I started in a very similar way, not with a meme coin but with others. I made my first investment on Revolut and soon after on Binance without understanding the technology or knowing the fundamental drivers of each project. I've made some money along the way which I am very grateful for but 6 months later I have started to understand the potential and the real word applications. It is exciting and happy to be an early(ish) adopter.

Upon reflection I believe that most 'normal' people enter the market for the same reasons, they see it as an investment opportunity. This may not be the right reason, but it is a reason nonetheless, and it is one step closer to mainstream use. You’ve made it clear that you do not support meme coins and anyone who has been in a while knows the danger of the but before long I have no doubt new investors will have the same outlook at myself.

It seems pointless to ask the plan for $AKITA when it's clear it was not created to change the world. Ironically it is making changes in that the majority of holders appear to be new. Collapsing a coin with tens of thousands of new and small investors will not solve the issue.

The team at Gitcoin have a far better understanding than I and I'm sure will make the right decision, I just hope not at the expense of early investors who will not only loose money but also faith in crypto.

Just to clarify I am not an $AKITA holder, I'm just interested to see how events will unfold and what can be learned along the way. A key lesson is to not give away 50% of all supply!

-------------------------

cryptowanderer | 2021-05-18 21:01:37 UTC | #99

fwiw, I am with my good friend @tjayrush - burn it **all** and let us get back to better uses of our time than debating idiots, who will just bring the conversation down to their level and beat us with experience.

We do not currently have the tools or coordination here to handle elegantly any of the other options presented.

-------------------------

JTraversa | 2021-05-19 15:51:32 UTC | #100

“the fate of our project has been put into your hands.”

I don’t think thats really a rational way to put things, especially with no governance in place. Without governance, its just market capitalization that is in Gitcoin’s hands, the path of the project can be independent from the token’s price. Theres really no onus on Gitcoin here.

However on a separate topic, assuming funds are effectively liquidated, I think that there should be some consideration made towards establishing a MetaCartel style venture DAO that participates in the early funding of open-source projects coming out of Gitcoin Kernel.

Gitcoin has unique access to the best new talent and projects in web3, the previous two cohorts each with ~10-25 projects eventually funded. If the concern is the perpetual funding of open-source community goods, significant returns are required for this funding to mean anything on a long term basis.

With a venture DAO, Gitcoin’s community multisig (or whatever it becomes) would then have access to these potentially high r/r opportunities, have projects coming out of Kernel with aligned incentives, and without LP’s to pay out, have the ability to sustain this funding perpetually.

There would definitely be questions as to selection processes, etc., so I’m unsure how realistic this is in comparison to just throwing the funds into some protocol, however its clearly a step that would lead to growth across all of the web3 community, and leaves a clear route for open-source funding beyond hope for continued Gitcoin Round matching.

Edit: This took awhile to get approved/posted so apologies, conversation may have moved past it.

Edit 2: It had in fact moved past it, with the context of vitalik specifically saying this is meant to fund gitcoin grants rather than gitcoin's overall mission statement, I'd likely put my vote into throwing funds into yearn and perpetually funding grants that way.

Edit 3:
**If we go the yearn direction, I would STRONGLY add the suggestion that profit be calculated on an adjusted basis.** If the funds yield 15% APY, one should only be able to withdraw and contribute 10% of that 15% to gitcoin grants in order to ensure the value of funds are retained over time and not lost to inflation.

-------------------------

ceresstation | 2021-05-24 00:51:21 UTC | #101

There are some super interesting ideas in this thread so far, thank you all for helping guide us here.  :pray: 

Like @owocki I've been listening + digesting the conversation and trying to get a sense of all the options the community has in mind. I truly believe there's potential for a positive-sum outcome here as in all things crypto, and we should strive towards that.

So far from the discussion, I'm noticing a few key options that I want to try to distill down:

**1) Sell a fixed percentage of tokens and burn/hold the rest**

This option seems to be the most popular, but it seems like there's a lot of variance in how much people want to sell. Some folks like @cupOjoseph think we should sell everything while others like @relic want to keep the number closer to 5%.

On average, it seems like most people in the thread are on board with somewhere around 10-20%. As I think most people in the thread know by now, Vitalik ended up burning around 80% of his SHIB so there's some interesting precedent here but that doesn't mean it's necessarily the right decision.

In terms of how to sell, @HelloShreyas mentioned a few strong options above, for example finding an OTC provider, drip selling into the market, or setting up a Gnosis auction. Other folks like @Crisgarner have even suggested some kind of buyback program.

**2) Hold the tokens and use them in collaboration with the AKITA ecosystem**

@omnianalytics and @Enrique have both suggested that we simply keep the funds but dedicate them to bounties, and specific quadratic funding rounds that benefit the AKITA ecosystem, the idea being that the most valuable thing here isn't the money but the community. Others like @papa_raw and @castall have suggested that we could hold the tokens but distribute them as part of the matching amount to grantees.

All of this feels very positive sum, but as @isaac and others mentioned there are opportunity costs and maybe even potential risks to putting our energy behind AKITA. 

**3) Do nothing, send the funds back to Vitalik**

As always the empty set is a subset of every set. As @tjayrush and @cryptowanderer have suggested, we could simply send the funds back to Vitalik or burn them entirely to move on to other things. This would allow us to avoid taking a side, and minimize opportunity costs, but at the cost of funds that could go towards Ethereum public goods.

**A Suggestion on how to move forward**

I noticed that @coopahtroopa put together a great [template](https://gov.gitcoin.co/t/gitcoin-community-proposal-gcp-template/134). No matter which of the options above (or others) we want to move forward with, I think we need to really clearly articulate the reasons why and consider both the potential, the downside risk, the second order effects, and so on. 

Do we have any folks that would be willing to take a shot at drafting some proposals and posting the final drafts [here](https://gov.gitcoin.co/c/governance-proposals/5) for the community to review?

-------------------------

scco | 2021-05-20 22:54:07 UTC | #102

agree 100% on it isaac .

-------------------------
