---
id: 10523
title: "GTC Conviction Voting dApp => Network Utility"
slug: gtc-conviction-voting-dapp-network-utility
category: governancevision
url: https://gov.gitcoin.co/t/gtc-conviction-voting-dapp-network-utility/10523
created_at: 2022-05-06T21:09:52.264Z
last_posted_at: 2022-10-05T14:57:17.077Z
posts_count: 40
views: 6475
like_count: 70
---

# GTC Conviction Voting dApp => Network Utility

<https://gov.gitcoin.co/t/gtc-conviction-voting-dapp-network-utility/10523>
owocki | 2022-07-26 17:23:19 UTC | #1

I wanted to share a dApp prototype that @austingriffith & two of the BuidlGuidl builders built (Viraz + 0xDarni).

This is a dApp that allows a user to stake GTC on Gitcoin Grants based on the Grant quality using [Conviction Voting](https://medium.com/giveth/conviction-voting-a-novel-continuous-decision-making-alternative-to-governance-aa746cfb9475).   From there, Gitcoin Grants 1.0 (or 2.0) could then adjust the sort algorithm of the grants based on what grants GTC holders think is most valuable.

Problems this dApp solves:
1. Allow GTC Holders to have governance utility with their GTC.
2. Provide fairer starting conditions to the Gitcoin Grants rounds, so it does not become a horse race (where ppl get more contributions => higher matching => repeat)

Check out the demo of this conviction voting dapp.  It allows people to trustlessly stake GTC on their favorite grants, signaling their conviction about which grants are quality.

https://www.youtube.com/watch?v=vHwUs9m45sA

# Roadmap from here
1. Audit the smart contracts
2. Deploy on Optimism L2
3. Simplify the UX
4. (If governance decides to) Adopt this data as part of the sorting algorithm on Gitcoin Grants.

# Links:
1. Play with the demo yourself: https://gtc.v37.io/
2. Checkout [the Github](https://github.com/0xDarni/scaffold-eth/tree/conviction-voting-gitcoin)
3. [Demo video](https://www.youtube.com/watch?v=vHwUs9m45sA)
4. [What is conviction voting?](https://medium.com/giveth/conviction-voting-a-novel-continuous-decision-making-alternative-to-governance-aa746cfb9475)

# This was built in 3 days!

## What can we learn from this?

What I think is incredible about this prototype is that Austin + crew conceived + built this in 3 days!

They didnt hire any fancy consultants.  They aren't spending $200k-300k/mo on software development.  This was just someone who cares about Gitcoin who chose to work backwards from an outcome + ship the software (and will probably be rewarded retroactively from Build Gulid/Gitcoin if/once this ships).  It's really inspiring to me!

What can we learn from this type of rapid prototyping?  Can we sprinkle some of this culture in the Moonshot Collective + Gitcoin Product Group so that we can ship [Grants 2.0 well before the overton window closes](https://gov.gitcoin.co/t/the-overton-window-for-grants-2-0/10461)?

IMO its existential to solve our software dev velocity problems.  We cannot continue to plow hundreds of thousands of dollars into software development that is neither [fast, cheap, nor good](https://fastgood.cheap/).  Questions about priorities are only existential when it takes us 2-6 months to ship any new module.  If we could quickly ship slim MVPs it would be less of a zero sum "my priority vs yours" between leaders.

I am a strong advocate of focusing on [minimum shippable increments](https://gov.gitcoin.co/t/minimum-shippable-increments/10140).  This GTC Conviction Voting dApp is a great emergent example of that.


# Prompts

1. How can we get more rapid prototyping juju (build guild culture) into MSC/GPG?  Daniele showed here that a steel thread for a small dApp takes 2-3 days if you have the right builder on a project/focused on outcomes.
2. Do we want to support this conviction voting app as part of grants 2.0 roadmap?

-------------------------

DanieleSalatti | 2022-05-06 23:01:40 UTC | #2

Hello Gitcoin! 🖖

I'm 0xDarni, aka Daniele

If you want to play with the demo as @owocki suggested, first you need to mint some test-GTC on Rinkeby.

Looks like I cannot post links, so here is the contract address: 0x961D0F9a9519434DF0F950c191bE5010bcCe177b

**Edit:** I just got permissions to post links, so here's the [contract](https://rinkeby.etherscan.io/address/0x961D0F9a9519434DF0F950c191bE5010bcCe177b#writeContract)!

We created a simple ERC-20 just for this with a public mint method, etherscan on Rinkeby is all you need 😃

-------------------------

iSpeakNerd | 2022-05-10 17:18:34 UTC | #3

My first time minting from etherscan, thanks! Love using test networks to learn, why does no one teach how to use them??!?

-------------------------

DanieleSalatti | 2022-05-14 02:57:34 UTC | #4

Just a note that we have redeployed a new version of the contracts!

We are iterating quickly right now, I will wait to post new contract addresses until they are closer to the final state :slight_smile:

-------------------------

griff | 2022-05-14 22:16:22 UTC | #5

I love CV (I have been helping to push it forward, and the first time the concept was explained was on Giveth's blog :-D ) 

but this is not CV. 

But I do agree with Darni and Viraz's approach! In fact, it's very similar to GIVpower! (please don't call it CV).

Funny I read this after shilling GIVpower in another forum post: 
https://gov.gitcoin.co/t/roadmap-to-gtc-utility/10546/7?u=griff

The hardest part is parameterizing it and communicating the impact of staking for longer to the user... 

In summary tho, that's why we came up with the idea of GIVpower... if you stake 100 GIV for 2 weeks... you get 100 GIVpower,  if you stake for 8 weeks = 200 GIVpower, if you stake for 128 weeks = 800 GIVpower, 200 weeks = 1000 GIVpower (scaling quadratically of course) 

Also, mStable had a similar approach and then THEY CHANGED IT!!! :scream: I interviewed them about why (1 day of research will save 6 months of testing in prod):
https://www.youtube.com/watch?v=j7HxR8-uHso

Anyway, we have a bunch of designs and thoughts about how to do this... @0xDarni any interest in a sync? I just found you on Twitter and DM'd ;-D

-------------------------

griff | 2022-05-14 22:17:22 UTC | #6

Also... if this does go out, I would give people who stake extra voting power on snapshot

-------------------------

DanieleSalatti | 2022-05-14 23:09:29 UTC | #7

It's more "inspired by CV" I'd say - but I have no idea how to call it 😃

[quote="griff, post:5, topic:10523"]
The hardest part is parameterizing it and communicating the impact of staking for longer to the user…
[/quote]

Very true, and these are the two major things missing right now. I have a couple of ideas to improve the UX and communication, but defining the parameters will be trickier - especially if we want to make it somewhat sybil resistant.

[quote="griff, post:5, topic:10523"]
Anyway, we have a bunch of designs and thoughts about how to do this… @0xDarni any interest in a sync? I just found you on Twitter and DM’d ;-D
[/quote]

Absolutely! Would love to chat!

PS: 0xDarni was my old profile - from a time when I wanted to be pseudonymous 🙂 - I deleted it to avoid confusion since I don't need it anymore. I'm here now: https://gitcoin.co/danielesalatti

-------------------------

DanieleSalatti | 2022-05-15 14:32:57 UTC | #8

Little update for those who are following this thread and want to play with the test version.

* The repository has been renamed. It is now [here](https://github.com/DanieleSalatti/gitcoin-grants-conviction) (the link from the OP will redirect anyway). Still temporary, but communicates a bit better what project the repo is about.
* The ERC-20 contract you need to mint some test tokens on Rinkeby is [here](https://rinkeby.etherscan.io/address/0x67775cBe9e73aa255Fc8e6A992Ed340e3b28D926#writeContract).
* The app is still at [gtc.v37.io](https://gtc.v37.io/).

This is a demo of the new UX that I sent to @owocki and @austingriffith, it'll show you what to expect:

https://www.youtube.com/watch?v=wjz-v7dwA9s

Any feedback (on UX, concept or anything else) is welcome :slight_smile:
What did you find easy? What did you find hard or non obvious?

-------------------------

owocki | 2022-05-15 17:02:27 UTC | #9

Looks really nice!  Some notes:

- on the cart page it still says "Remember: you will not be able to unstake your tokens until the set time!"  but IIRC there is no set time anymore.
- i agree that it would make sense to show the user how much voting power their GTC is worth.
- is it easy to write a python script to get the voting power per grant?  if so id love to get a snippet of code that does this so i can automatically import these weight numbers into the cGrants DB on a regular interval.
- id love to know what other gitcoin product leaders (@kyle @lthrift @kevin.olsen ) want to see here to be comfortable using this dApp to create a user signal to rank grants.
- id love to know if we can cross-pollinate how you build with the GPG.  you move so fast, maybe the GPG could learn something from you?

-------------------------

DanieleSalatti | 2022-05-15 19:23:13 UTC | #10

[quote="owocki, post:9, topic:10523"]
on the cart page it still says “Remember: you will not be able to unstake your tokens until the set time!” but IIRC there is no set time anymore.
[/quote]

Fixed!

[quote="owocki, post:9, topic:10523"]
is it easy to write a python script to get the voting power per grant? if so id love to get a snippet of code that does this so i can automatically import these weight numbers into the cGrants DB on a regular interval.
[/quote]

I quickly changed the schema and mappings, and redeployed the subgraph so now we have an additional entity - which makes querying for that easier.

I'm outside and running out of battery, but [this repo](https://github.com/DanieleSalatti/gtc-data-fetcher/) should be a good starting point to get to the data you want. It gets the first 100 grants and the related votes and releases, it's missing the logic to actually calculate the voting power. I can get to that sometime this week :slight_smile: 

[quote="owocki, post:9, topic:10523"]
id love to know if we can cross-pollinate how you build with the GPG. you move so fast, maybe the GPG could learn something from you?
[/quote]

Yes, I'd love to sync with you guys :slight_smile:

-------------------------

DanieleSalatti | 2022-05-17 14:48:59 UTC | #11

@owocki what kind of growth do we want the voting power to have over time: linear, exponential, logarithmic...? And how fast do we want it to grow?

Once we know that we can start showing it to the user and tweak the Python script to calculate it.

-------------------------

DisruptionJoe | 2022-05-17 21:56:06 UTC | #12

I'd guess from @griff comments that exponential (quadratic) must be the best. Awesome to see this project moving forward FAST. I'd also advise changing the name from Conviction Voting to not confuse people.

-------------------------

ZER8 | 2022-05-18 11:47:22 UTC | #13

It's great to see another dApp being build around conviction voting. Conviction voting brought me to web 3 in 2019 :smiley:  Thanks to 1Hive :honeybee:

From a Grants perspective this will be a very useful signaling tool for our community. Would be curious what can be build on top of it or in continuation

-------------------------

owocki | 2022-05-18 23:23:39 UTC | #14

[quote="DanieleSalatti, post:11, topic:10523"]
@owocki what kind of growth do we want the voting power to have over time: linear, exponential, logarithmic…? And how fast do we want it to grow?
[/quote]

i would like to defer to the experts (like @griff)

[quote="DisruptionJoe, post:12, topic:10523"]
Awesome to see this project moving forward FAST
[/quote]

Yes, I agree.  There is something to be learnt here about how to do software development in DAOs.

-------------------------

DanieleSalatti | 2022-05-19 16:08:55 UTC | #15

[quote="owocki, post:14, topic:10523"]
i would like to defer to the experts (like @griff)
[/quote]

I had a call with him a couple of days ago - it was really interesting, he gave me material to read and showed me this: https://config.tecommons.org/config/4

His suggestion (@griff correct me if I missed something) is to replace the spending limit percentage in that model with a fixed multiplier, and make it go from 0 to the max in a pretty long amount of time.

E.g. you can get max 50x after 6 months, so:

1. you stake 5 GTC on a grant - on day one your voting power is worth 0

2. over time your voting power grows, and after e.g. 15 days it is now worth the full 5 GTC

3. after 6 months it reaches 250 (50x) - and it stops growing

At that point if you leave your tokens in, your voting power stays at 250 for that grant. If you un-stake there's a decay function so it doesn't go to 0 immediately.

The multiplier and the duration we should decide.

I have another call with him next week. I'm on a trip in NY at the moment - back on Monday - but in the meantime I handed over a couple of optimisations in the subgraph model to @Viraz.

Voting power will be calculated off-chain, so we will deploy to Mainnet soon :slight_smile:

-------------------------

DanieleSalatti | 2022-05-23 01:22:31 UTC | #16

[quote="DanieleSalatti, post:15, topic:10523"]
I’m on a trip in NY at the moment
[/quote]

I'm back :slight_smile: 

We deployed to Mainnet.

The next step is adding a visual indicator of the voting power to the dashboard.

-------------------------

owocki | 2022-05-23 01:40:44 UTC | #17

[quote="DanieleSalatti, post:16, topic:10523"]
We deployed to Mainnet.
[/quote]

is the final place for this tool mainnet or a L2?

-------------------------

DanieleSalatti | 2022-05-23 03:51:22 UTC | #18

[quote="owocki, post:17, topic:10523"]
is the final place for this tool mainnet or a L2?
[/quote]

Wherever it makes sense :slight_smile:
Is the DAO planning on moving GTC to an L2, even partially?

If you ask me, then I'd say long term an L2. Short term we could do L2, it just requires some work on the UX.

The reason we went for Mainnet is that @austingriffith tried bridging to Optimism and it cost him 41 USD to transfer 1 GTC:

![](upload://zRtfvkrffsUJxW9R1Cq7RWYFTrM.png)

Presumably you'd have to transfer back to L1 if you want to use the tokens for something else.

On top of that right now the UX is not great - this thread explains what Austin had to do:

https://twitter.com/austingriffith/status/1522671054308610048?s=20&t=jrp1o2jiuc-GNBtv-ZtXjQ

Nothing that can't be solved: we can quickly build a UI to let people bridge GTC to Optimism in a few clicks from the dApp, or we can use a different L2.

We can do anything :slight_smile:

I think the decision in the end should be coming from you / the DAO. I am not aware of what the long term plans are for the token and L2 adoption.

-------------------------

erich | 2022-05-23 10:19:50 UTC | #19

In what values do you ground these prescriptions for increasing voting power over time? Indeed, it seems pretty off to me to formally punish deliberation in the staking process as you prescribe.

Deliberation is key to plural forms of social organization!

-------------------------

kevin.olsen | 2022-05-23 12:25:18 UTC | #20

Does the 250GTC max apply universally? If I'm a whale and I drop 250GTC is my voting power maxed out at 15 days or does it really grow to 12500 GTC in 6 months?

-------------------------

kevin.olsen | 2022-05-23 12:31:49 UTC | #21

Another question, why would we want a decay when someone unstakes? It feels like a clear signal that a person has lost 'conviction' in the project, and the boost should go to 0.

-------------------------

owocki | 2022-05-23 14:10:55 UTC | #22

[quote="DanieleSalatti, post:18, topic:10523"]
I think the decision in the end should be coming from you / the DAO. I am not aware of what the long term plans are for the token and L2 adoption.
[/quote]

idk how to ratify this decision without going through the whole DAO voting process, but here is what i think: [ethereum has a rollup-centric scaling solution](https://ethereum-magicians.org/t/a-rollup-centric-ethereum-roadmap/4698), therefore i think this dapp should be hosted on a rollup.

-------------------------

DanieleSalatti | 2022-05-23 15:08:55 UTC | #23

[quote="kevin.olsen, post:20, topic:10523, full:true"]
Does the 250GTC max apply universally? If I’m a whale and I drop 250GTC is my voting power maxed out at 15 days or does it really grow to 12500 GTC in 6 months?
[/quote]

With the numbers in that example it would grow to 12500 in 6 months (50x multiplier).

[quote="erich, post:19, topic:10523, full:true"]
In what values do you ground these prescriptions for increasing voting power over time? Indeed, it seems pretty off to me to formally punish deliberation in the staking process as you prescribe.

Deliberation is key to plural forms of social organization!
[/quote]

[quote="kevin.olsen, post:21, topic:10523, full:true"]
Another question, why would we want a decay when someone unstakes? It feels like a clear signal that a person has lost ‘conviction’ in the project, and the boost should go to 0.
[/quote]

I'll let @griff and others with more experience on CV answer these. If they don't I'll give it a shot.

-------------------------

DanieleSalatti | 2022-05-23 18:14:25 UTC | #24

[quote="owocki, post:22, topic:10523"]
idk how to ratify this decision without going through the whole DAO voting process, but here is what i think: [ethereum has a rollup-centric scaling solution](https://ethereum-magicians.org/t/a-rollup-centric-ethereum-roadmap/4698), therefore i think this dapp should be hosted on a rollup.
[/quote]

~~I'll get to building the UI/UX for bridging to Optimism then :slight_smile:~~

~~I'll make it so the network can be feature-switched and the bridging UI hidden, in case the decision from the DAO is to stay on Mainnet.~~

Turns out there isn’t a GTC token on Optimism - I’ll work on refining the UX for now then, and as soon as we decide for an L2 I will deploy there.

-------------------------

owocki | 2022-05-23 18:28:58 UTC | #25

[quote="DanieleSalatti, post:24, topic:10523"]
Turns out there isn’t a GTC token on Optimism - I’ll work on refining the UX for now then, and as soon as we decide for an L2 I will deploy there.
[/quote]

i thought @austingriffith found a bridge? https://twitter.com/austingriffith/status/1522671723937550337?s=20&t=-5R9Lwpb8qR99SyzCQSQdw

if not we should get one over there.  idk if you've had any luck @gtcchase?

-------------------------

DanieleSalatti | 2022-05-23 19:44:16 UTC | #26

Yeah sorry. I am trying to piece together bits and pieces from here and a couple of chat rooms, and I'm doing a poor job at it...

-------------------------

gtcsameerth | 2022-05-23 20:06:41 UTC | #27

Hey there Daniele! MoonshotCollective has bridged GTC to Optimism. Here is the contract address and token view. We're currently waiting on folks over at Optimism to merge our PR so GTC can be easily selected from their bridge (https://app.optimism.io/bridge)!

GTC Optimism Contract Address:

[0x1eba7a6a72c894026cd654ac5cdcf83a46445b08](https://optimistic.etherscan.io/address/0x1eba7a6a72c894026cd654ac5cdcf83a46445b08)

GTC Optimism Token View:

https://optimistic.etherscan.io/token/0x1eba7a6a72c894026cd654ac5cdcf83a46445b08

Let me know if that was helpful or if you had any more question!

-------------------------

DanieleSalatti | 2022-05-25 15:30:10 UTC | #28

That helps!

Thanks @gtcsameerth!

-------------------------

DanieleSalatti | 2022-05-30 01:53:36 UTC | #29

We redeployed on Mainnet, and now that the Optimism bridge supports GTC we will work to support both networks :slight_smile: 

![Schermata 2022-05-29 alle 18.52.16|444x500](upload://s42sTEhc3YuCc1eK36bGFl5MAM6.jpeg)

-------------------------

DanieleSalatti | 2022-06-04 02:33:20 UTC | #30

We launched:

https://voting.gitcoin.co/

-------------------------

owocki | 2022-06-06 15:52:42 UTC | #31

heads up this is live now

how to use GTC to stake on the gitcoin grants you believe in 3 easy steps 

1. go to [http://voting.gitcoin.co](https://t.co/4BOxC4aFcz) 
2. stake your GTC on either mainnet or optimism 
3. browse to [http://gitcoin.co/grants](https://t.co/8P0WRpB1pF) and select "GTC Conviction Voting" as your sort order

itll look like this:

![FUkyT8NUUAAZkHK|690x436](upload://zxzHuMg2sujPO9ylMWwR4qIGZhX.png)

-------------------------

lefterisjp | 2022-06-06 16:55:46 UTC | #32

I was asked to post here and not only Twitter :sweat_smile:

So I think this is a good idea in the long run! But not for GR14. And such a last minute change should go through governance.

https://twitter.com/LefterisJP/status/1533821810260824065

As it stands I would not support it because:
1. No time for conviction part to work.
2. Unaudited contract + counterparty risk
3. Potential tax
4. Staking breaks delegation
5. Lack of time for (1) -> plutocracy


We would need to solve all these to have proper conviction voting,

-------------------------

jdonmoyer | 2022-06-17 18:07:39 UTC | #33

I'm also very much interested in the 'answer' to this question... I'm not currently a GTC holder, but I want to be and I would like to acquire it/keep it on the chain where it has the most utility.

-------------------------

owocki | 2022-07-11 20:29:16 UTC | #34

@DanieleSalatti @austingriffith do u gents have any data on how this experiment went?  would you call iteration 1 a success?  is there another iteration planned for GR15?

-------------------------

DanieleSalatti | 2022-07-24 08:31:06 UTC | #35

@owocki good question.

There's a lot that we cannot measure, for example I would love to know how often the new sorting was used on gitcoin.co while the round was going.

That said, we think it worked great. 

Some numbers:

* 23232 GTC still staked on Mainnet
* 4760 GTC still staked on Optimism [about about 60% of the total](https://optimistic.etherscan.io/token/0x1eba7a6a72c894026cd654ac5cdcf83a46445b08#balances)  as of now
* Highest amount staked was about 50K GTC on Mainnet - Optimism has been stable
* 54 unique stakers across the two networks

So let me turn the question back to you, @owocki, and to the DAO: what would have to be true for us to use conviction voting as the default sorting method for next round?

-------------------------

owocki | 2022-07-24 18:20:10 UTC | #36

[quote="DanieleSalatti, post:35, topic:10523"]
what would have to be true for us to use conviction voting as the default sorting method for next round?
[/quote]

perhaps @annika this is something to include in the convo about GR15 structure?

if not, it would probably be its own proposal?

-------------------------

Fred | 2022-07-31 07:32:23 UTC | #37

Is the 23232+4760 GTC that's still being staked continuing to accrue conviction bonus for upcoming rounds, or are these reset prior to each GR?

If the bonus carries over into GR15, will new staker be able to catch up in time for launch without a considerably larger amount of GTC? Or phrased differently; What percentage of their maximum conviction bonus have the GR14 stakers accumulated?

-------------------------

DisruptionJoe | 2022-08-08 10:35:15 UTC | #38

[quote="DanieleSalatti, post:35, topic:10523"]
what would have to be true for us to use conviction voting as the default sorting method for next round?
[/quote]

I'd really like to see some strategizing around how we can ensure that this mechanism isn't turning the game into an unfair rich get richer system BEFORE putting it as a default sort!

-------------------------

griff | 2022-10-03 17:01:59 UTC | #39

Giveth is going to be launching GIVpower, which is something very similar to the work being done here. The first part of it, the staking and locking, rolls out is tomorrow.

There should be lots of interesting Comms around it on our twitter and it might be fun to check it out.

https://twitter.com/Givethio

-------------------------

ZER8 | 2022-10-05 14:57:17 UTC | #40

Wow, Give is the give that keeps on giving. Thank you for the heads up :blue_heart:

-------------------------
