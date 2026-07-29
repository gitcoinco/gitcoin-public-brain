---
id: 8925
title: "Your Input wanted - Multisig Keyholders Rotation"
slug: your-input-wanted-multisig-keyholders-rotation
category: governancevision
url: https://gov.gitcoin.co/t/your-input-wanted-multisig-keyholders-rotation/8925
created_at: 2021-11-01T17:04:53.190Z
last_posted_at: 2021-11-04T22:14:36.402Z
posts_count: 17
views: 2704
like_count: 30
---

# Your Input wanted - Multisig Keyholders Rotation

<https://gov.gitcoin.co/t/your-input-wanted-multisig-keyholders-rotation/8925>
owocki | 2021-11-01 17:32:57 UTC | #1

Hey all,

The [Gitcoin multisig](https://etherscan.io/address/0xde21f729137c5af1b01d73af1dc21effa2b8a0d6) was [created in August 2020](https://etherscan.io/tx/0x296fe57c2c227b7b37c3901844607e22633d2c12c98f8430727bfbed56d27de2), before the GitcoinDAO launch.

It has the following keyholders:
- myself
- David Hoffman
- Sassal
- Hudson Jameson
- Eric Coner
- Kyle Weiss

As we got around to paying out GR11, we realized that things have evolved a lot since we created this multisig.  Particularly, 
1. We now have formal governance of GitcoinDAO via the [Gitcoin Stewards](https://withtally.com/governance/gitcoin).
2. Things have shifted in the ecosystem, and many of the keyholders are now busy with other projects.

As a result, we started to have a conversation about what it would look like to have a "changing of the guard" here.  Specifically, David Hoffman, Sassal, and Eric Conner have all told me that they are interested in rolling off the multisig.  There are two directions we could go.  

1. Rotate the multisig keyholders to be [top GitcoinDAO stewards](https://withtally.com/governance/gitcoin), which are currently Trent, Austin, Linda, Lefteris - on a case by case basis if they want it.
2. Transfer all of the assets in the multisig to the [Timelock](https://etherscan.io/address/0x57a8865cfb1ecef7253c27da6b4bc3daee5be518).

I would like to hear which way the community would like us to go.

One consideration that you should know about  if you consider doing (2) is that right now the only way to rebalance tokens into DAI (which is what the Grants Rounds are paid out with) is to do a trade on uniswap/1inch or any other DEX.  We've found that if there is a long lag between when those txns are proposed and executed on chain, that the transaction will fail - presumably due to slippage.  If the community decides to go with (2) we will need a workaround that allows governance to rebalance the treasury within the structure of the 2 day Timelock.

What do ppl want to see? 
[poll type=regular results=always chartType=bar]
* 1. Rotate the Multisig Keyholders to top Stewards
* 2. Move all tokens into the GitcoinDAO Timelock
* 3. Other (pls comment below)
[/poll]

-------------------------

TrustlessState0x | 2021-11-01 17:26:10 UTC | #2

Hey all, 

Yes indeed, I think it might be in the best interest of the DAO to replace me with someone a bit more responsive towards what's specifically going on in Gitcoin. 

Cheers!

-------------------------

econoar | 2021-11-01 18:10:00 UTC | #3

I echo David’s comment for myself.

-------------------------

linda | 2021-11-01 19:43:10 UTC | #4

I'm supportive of rotating the multisig keyholders to top Stewards and I'm happy to be a signer.

-------------------------

kyle | 2021-11-01 20:52:24 UTC | #5

I am also supportive of rotating and ensuring we can take actions in a timely manner :slight_smile: 

One future goal will be to rebalance the multisig and this requires real time and work from folks to make happen on a regular cadence.

-------------------------

sassal | 2021-11-02 00:24:31 UTC | #6

Echoing what David says here - it's especially difficult for me to be involved because of time-zone differences (I'm usually sleeping when critical Gitcoin governance things are happening).

-------------------------

disruptionjoe1 | 2021-11-02 02:29:16 UTC | #7

Another option would be to leave it in the multisig but use a Zodiac module to initiate governance control. @auryn would probably be best to explain.

-------------------------

trent | 2021-11-02 13:28:23 UTC | #8

I've been asked if I would be able to help with this, I can definitely be a part of moving Gitcoin forward.

-------------------------

auryn | 2021-11-02 19:24:46 UTC | #9

[quote="owocki, post:1, topic:8925"]
We’ve found that if there is a long lag between when those txns are proposed and executed on chain, that the transaction will fail - presumably due to slippage. If the community decides to go with (2) we will need a workaround that allows governance to rebalance the treasury within the structure of the 2 day Timelock.
[/quote]

Whether it's the DAO or the multi-sig controlling the funds, it should absolutely use Cowswap for trades to avoid MEV or transaction failing due to falling outside of the slippage tolerance.

[quote="disruptionjoe1, post:7, topic:8925, full:true"]
Another option would be to leave it in the multisig but use a Zodiac module to initiate governance control. @auryn would probably be best to explain.
[/quote]
Absolutely! There is no need to move funds from the safe, the GitcoinDAO's timelock can be enabled as a module on the Gnosis Safe, giving it full control over the funds.

The nice thing with this is that both the DAO and the multisig members can control the safe in parallel. If we want to get real crazy, we could even use a scope guard to limit the scope of what the multisig members are allowed to do. So maybe they are only allowed to do swaps on cowswap, but anything else requires DAO proposal.

-------------------------

thelostone-mc | 2021-11-03 17:03:42 UTC | #10

Agreed on this.
I found myself being slowed down on getting the stuff setup for payout.
Having a rotating list would help would help make us get through this process quicker

-------------------------

owocki | 2021-11-03 18:36:23 UTC | #11

this idea seems like an intriguing "best of both worlds" scenario.

how might we explore Zodiac for GitcoinDAO in a way that respects governance + sets the right fine grained controls for the multisig?

-------------------------

austingriffith | 2021-11-04 17:34:08 UTC | #12

I support rotating in stewards and happy to help! 🏄

-------------------------

lefterisjp | 2021-11-04 17:44:54 UTC | #13

I am happy to help too. Been already doing a lot for Gitcoin DAO so this would be a good fit.

But I think I would like to echo @auryn and @DisruptionJoe that we could use a module in the multisig and do it directly from the safe.

If my (or anyone else's) availability changes then we can always rotate out.

-------------------------

DisruptionJoe | 2021-11-04 18:47:03 UTC | #14

Yeah. I didn't mention here yet, but definitely agree that this is a perfect use case for Zodiac.

-------------------------

griff | 2021-11-04 19:42:40 UTC | #15

+1 on Zodiac... seems like a nice high profile opportunity to give a nod to the great work Gnosis is doing with Cowswap and Zodiac

-------------------------

auryn | 2021-11-04 19:55:38 UTC | #16

[quote="owocki, post:11, topic:8925"]
how might we explore Zodiac for GitcoinDAO in a way that respects governance + sets the right fine grained controls for the multisig?
[/quote]

The setup could look something like this.

```
Gitcoin Gnosis Safe
  ⬑ Multisig
    ⬑Scope guard (optional)
  ⬑ GitcoinDAO timelock
  ⬑ Reality Module
    ⬑ GitcoinDAO Snapshot
      ⬑Scope guard (optional)
```

Essentially, the safe would be controlled by three mechanisms in parallel, the multisig, the compound timelock, and the Snapshot (via the [Reality module](https://github.com/gnosis/zodiac-module-reality)).  Optionally, the multisig and/or the Reality module could be restricted with a [Scope Guard](https://github.com/gnosis/zodiac-guard-scope/), which let's us define the addresses and function signatures with which they interact.

-------------------------

owocki | 2021-11-04 22:14:36 UTC | #17

Setting up some time next week with @auryn to talk through Gnosis Zodiac setup details.

-------------------------
