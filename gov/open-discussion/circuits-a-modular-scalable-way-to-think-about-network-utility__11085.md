---
id: 11085
title: "Circuits - a Modular/Scalable Way to think about Network Utility"
slug: circuits-a-modular-scalable-way-to-think-about-network-utility
category: open-discussion
url: https://gov.gitcoin.co/t/circuits-a-modular-scalable-way-to-think-about-network-utility/11085
created_at: 2022-07-08T18:36:38.417Z
last_posted_at: 2022-07-13T16:27:24.006Z
posts_count: 6
views: 3368
like_count: 12
---

# Circuits - a Modular/Scalable Way to think about Network Utility

<https://gov.gitcoin.co/t/circuits-a-modular-scalable-way-to-think-about-network-utility/11085>
owocki | 2022-07-26 17:28:49 UTC | #1

In this post, I would like to articulate the way I think about the DAO building Network Utility.  I will not prescribe any particular mechanism, but I will try to build a vocabulary for thinking about these mechanisms. 

 By having visuals and by sharing a common vocabulary + a modular, composable, scalable way of thinking about network Utility, the DAO will have less of a coordination lift to build network utility + network Utility.

Post TLDR
1. Circuits are a composable way of connecting governance Utility to Network Utility in a positive sum way
2. Adapters are the primary mechanism within a circuit.
2. Circuits & Adaptors can be stacked modularly.
3. The remainder of the post explores stacking circuits in practice.

# Circuits

Per [https://gitcoin.co/results](https://gitcoin.co/results) we know that Gitcoin delivers $6m/quarter in financial network value & a ton of social value too to the ecosystem.

![9f170add-d30a-4f25-8c44-b66869c3ce43|690x423, 50%](upload://wMoXD3PhkU00xrTyL7gyKpxsBdL.gif)

Because Gitcoin is a double sided marketplace (grant owners <> funders), https://gov.gitcoin.co/t/the-network-effects-of-gitcoindaos-protocols/10973 (in theory) create an exponential growth in the network utility for both sides of the marketplace.

For the purposes of simplicity in this post, I will abstract this double sided marketplace into one node:

![5bb020f9-3e7f-4692-bf24-d8aa1da982a5|561x500, 50%](upload://pZwWVIeL3ZhBhr9aTuiDy7QkWLW.gif)

This post will articulate how the DAO might build a **circuit** that, when combined with an **adapter**, could create both more network utility and governanceUtility

![59f98726-840a-43af-9bef-3032abcdfa46|690x315, 75%](upload://HXcMKMmgTrjaqvVbfpFTLZZbXU.gif)

An **adapter** is a credibly neutral mechanism that connects the **network** (which is already creating utility for the ecosystem but has governance problems) to **GTC governance token** (which is held by people who have the context to govern Gitcoin, but has no utility).

In this circuit, the adapter exports governance to the parts of the circuit that needs governance, and utility to the part of the circuit that needs utility.

1. **GTC governance tokens** have little utility + a lot of ability to govern.
2. The **network** has a lot of utility + lots of governance problems
3.  An adapter bridges the two, creating more utility for governance (reducing governance problems) + also more utility.  At least in theory!

## More legitimacy - the first bonus feature

It gets better. Since the network  utility is now being governed better according to the preferences of its users (who bc of the retro airdrop have GTC), the end result is more legitimacy, which creates more utility.  The whole thing is even more positive sum.

[![187c925a-93b3-4d94-b645-22583781efec|690x324, 75%](upload://awGqLEwfGgKzyzTNrcAd7u1Zw4q.gif)](https://ncase.me/loopy/v1.1/?data=[[[1,527,391,0,%22GTC%2520Utility%22,4],[2,714,379,0,%22adapter%22,5],[3,966,379,0.16,%22network%2520utility%22,3]],[[2,1,73,1,0],[1,2,66,1,0],[2,3,33,1,0],[3,2,53,1,0],[2,2,126,1,21],[3,3,130,1,58]],[[745,276,%22more%2520legitimacy%2520%253D%253E%2520more%2520utility%22]],22%5D)


## Modularity - the second bonus feature

Know what else is cool about these circuits?  They can stack on top of each other fairly modularly!

Lets stack some circuits!  Heres what that could look like:
[![395c8aa3-3e8c-451c-92c5-c9aa6c81e5d8|690x286](upload://2FqX8PqlTPdNxoJ9wqwJmE3voPI.gif)](https://ncase.me/loopy/v1.1/?data=[[[1,527,391,0,%22circuit%2520GTC%2520Utility%22,4],[2,714,379,0,%22adapter%22,5],[3,966,379,0.16,%22circuit%2520network%2520utility%22,3],[15,723,534,0,%22adapter%22,5],[16,719,221,0,%22adapter%22,5],[17,533,220,0,%22circuit%2520GTC%2520Utility%22,4],[18,989,230,0.16,%22circuit%2520network%2520utility%22,3],[19,974,527,0.16,%22circuit%2520network%2520utility%22,3],[20,512,539,0,%22circuit%2520GTC%2520Utility%22,4],[21,249,390,0,%22total%2520GTC%2520Utility%22,4],[22,1194,396,0.5,%22total%2520network%2520utility%22,3]],[[2,1,73,1,0],[1,2,66,1,0],[2,3,33,1,0],[3,2,53,1,0],[3,22,-27,1,0],[22,3,-30,1,0],[22,18,-26,1,0],[18,22,-10,1,0],[19,22,-18,1,0],[22,19,59,1,0],[22,22,117,1,74],[18,16,9,1,0],[16,18,-19,1,0],[16,17,4,1,0],[17,16,22,1,0],[15,20,-30,1,0],[20,15,-30,1,0],[15,19,14,1,0],[19,15,57,1,0],[21,1,-16,1,0],[1,21,-21,1,0],[17,21,-18,1,0],[21,17,-59,1,0],[20,21,-9,1,0],[21,20,-49,1,0]],[],22%5D)

An aside: @kyle has sent me a great post about how NOT to do this [here](https://cobie.substack.com/p/apecoin-and-the-death-of-staking). Any such adapters should likely innovate so they are positive sum (past DAO staking tools have not really done this well)

Weee !  Bitcoiners stack sats.  At Gitcoin, we stack circuits

# Stacking Circuits in Practice

## Example 1 - Passport GTC Staking

One idea I've seen kicked around the DAO is the idea to add more total sybil resistance into the Gitcoin ecosystem + web3 ecosystem with Gitcoin passport by adding more stamps to the  system.  The post [Passport is our AWS](https://gov.gitcoin.co/t/passport-is-our-aws/10995) goes into this idea in depth.

One thing that could be done is to build an circuit that creates sybil resistance (network utility) with GTC.  Imagine an adapater is built that allows people to stake on each others identities to increase the sybil resistence of each user staked.  So for example,

1. I know @kyle is a real human, so I take $300 worth of GTC on him.  If his Gitcoin Passport ID had a cost of forgery of $50 before, he now has a $350 cost of forgery.
1. I know @linda is a real human, so I take $1000 worth of GTC on her.  If her Gitcoin Passport ID had a cost of forgery of $337 before, she now has a $1337 cost of forgery.
1. and so on.

Heres what I think this looks like:

![42597fc5-cc67-431e-b0f8-777bad2457b0|687x500, 75%](upload://fWDPOPVqCvShyXvZWNr9j4kzyNj.gif)

## Example 2 - Conviction Voting GTC Staking

Here's a circuit that is already built!  A [GTC conviction voting app](https://gov.gitcoin.co/t/gtc-conviction-voting-dapp-gtc-utility/10523)!

It consists of an adapter hosted at voting.gitcoin.co where anyone can go in and stake their GTC on which grants they think are higher quality than other grants.    This provides fairer starting conditions to the Gitcoin Grants rounds, so it does not become a horse race (where ppl get more contributions => higher matching => repeat)

Heres what I think this circuit looks like:

![b32b70e5-e95b-4b63-ad7c-eff89b1ddedf|690x469, 75%](upload://2VF77bi6D2ZeAKChpiD7tOHc4rY.gif)


## Example 3 - Mutual Grants

One thing that I think is fairly upside for Gitcoin could be [Mutual Grants](https://gov.gitcoin.co/t/constructing-a-mutual-grants-committee/10347) - which again, are already happening.

Mutual Grants allow Gitcoin to invite our partner ecosystems to participate in Gitcoin governance, which increases Gitcoin governance utility.

The same could be true in reverse (Gitcoin creating partner ecosystem utility).

For more on this idea, checkout updates from @ceresstation on this thread: https://gov.gitcoin.co/t/constructing-a-mutual-grants-committee/10347

Heres what I think this circuit looks like:


![20465a45-b42d-48af-966d-6560b62cc689|690x452, 75%](upload://gHGdvPbqrlz7DdAIrYvDB5DAwQj.gif)

## Stacking Circuits = SuperCircuit!

Here is a stacked circuit of these 3 circuits.  

[![5050ca94-80ab-4571-bbde-7c468a417f87|690x381](upload://bkwUOivejO5ZOT57isdiVGWfBQY.gif)](https://ncase.me/loopy/v1.1/?data=[[[1,473,212,0.16,%22Circuit%2520GTC%2520Utility%22,4],[2,669,203,0,%22adapter%22,5],[3,928,199,0.16,%22total%2520sybil%2520resistence%22,3],[4,1111,157,0.5,%22other%2520sybil%2520resistence%2520tools%22,1],[5,921,356,0.16,%22total%2520grants%2520GMV%22,3],[6,689,369,0,%22adapter%22,5],[7,522,376,0.16,%22Circuit%2520GTC%2520Utility%22,4],[8,316,366,0.16,%22Total%2520GTC%2520Utility%22,4],[9,1233,354,0.16,%22total%2520network%2520utility%22,3],[10,1193,522,0.66,%22other%2520grants%2520drivers%22,1],[11,526,511,0.16,%22Circuit%2520GTC%2520Utility%22,4],[12,697,514,0,%22adapter%22,5],[13,893,521,0,%22GTC%2520partner%2520ecosystem%2520utility%22,3],[14,1047,592,0.5,%22other%2520partner%2520ecosystem%2520utility%22,1]],[[2,1,94,-1,0],[1,2,89,1,0],[4,3,40,1,0],[2,3,20,1,0],[3,2,49,1,0],[3,9,23,1,0],[9,3,14,1,0],[5,9,12,1,0],[9,5,35,1,0],[6,5,38,1,0],[5,6,28,1,0],[6,7,-33,1,0],[7,6,-40,1,0],[7,8,-31,1,0],[8,7,-17,1,0],[8,1,-17,1,0],[1,8,-56,1,0],[10,5,14,1,0],[5,10,39,1,0],[3,4,14,1,0],[14,13,-15,1,0],[13,14,-30,1,0],[8,11,-2,1,0],[11,8,49,1,0],[11,12,26,1,0],[12,11,49,1,0],[12,13,34,1,0],[13,12,29,1,0],[13,9,26,1,0],[9,13,22,1,0]],[[465,138,%22Sybil%2520Resistence%2520Circuit%22],[530,317,%22Gitcoin%2520Grants%2520Circuit%22],[523,602,%22Mutual%2520Grants%2520Circuit%22]],14%5D)

Notice how once the circuits are setup correctlly (positive sum) utility flows around the supercircuit like water flowing downhill. 

Now that we've looked at the expanded version of this circuit, we could perhaps simplify. 

 This stack of circuits could be further simplified by looking at the circuits from the to down as opposed to stacked next to each other.  eg as follows:

[![1f3dce47-8eff-4ce3-9b8e-412a4d01d051|690x323](upload://ioAOeoGakCnbz0JML8zyQ3GAKLV.gif)](https://ncase.me/loopy/v1.1/?data=[[[6,654,389,0,%22many%2520adapters%22,5],[8,458,392,0.16,%22Total%2520GTC%2520Utility%22,4],[9,910,385,0.16,%22total%2520network%2520utility%22,3]],[[6,6,152,1,74],[9,6,-32,1,0],[6,9,-87,1,0],[6,8,-23,1,0],[8,6,-34,1,0],[9,9,173,1,73]],[[484,289,%22Simplified%2520SuperCircuit%22]],14%5D)


For those skilled at reading between the lines, the total Utility is bounded by

1. total network utility
2. how much of that utility is translated into governance utility by adapters.

Feedback welcome.

-------------------------

David_Dyor | 2022-07-11 20:20:17 UTC | #2

I appreciate this breakdown Kevin.  It is easy to follow.  

We've been kicking around the GTC-utility idea for a while in the FDD.  I like to think utility-concerns are appropriate to anyone interested in survival and health of the Dao...or basically every Dao member.

Gitcoin already has a grant 'Flagging' system by which any member-of-the-public can dispute a grant in the Gitcoin system.  In GR14 we saw increased use of the Flagging system for posting personal conflicts.  Somebody alleged plagiarism and someone else alleged financial fraud in GR14, which are examples of types of personal conflict that can be hard to manage through the Flagging system.  

There is no disincentive to prevent malicious use of the flagging system.  
There is no incentive to properly use the system beyond personal ethics and diverting funds from possible bad actors (which might change quadratic matching amounts).

I think this Flagging system can be modified into a simple circuit as you describe, plus increase Dao-efficiency by reducing spam flags.  There are really just 2 additional mechanisms needed:

1.  Gitcoin Dao require a small GTC deposit by a person to flag a grant.
2.  Flags that are found to be valid upon FDD assessment shall cause the deposit to get returned to sender (+ 1 GTC or a poap/passport stamp for incentive).  Invalid flags cause GTC deposit to get added to matching pool.

This would have the additional benefit of decreasing centralization-debt with regard to crowd-sourcing the anti-sybil hunt as we saw some other ecosystems experiment with recently.  I suggest this might be one of the low-hanging-fruits Gitcoin can use without needing to start from a blank slate.  I am unsure how Grants2.0 will affect the Flagging system.

-------------------------

owocki | 2022-07-11 20:30:41 UTC | #3

[quote="David_Dyor, post:2, topic:11085"]
* Gitcoin Dao require a small GTC deposit by a person to flag a grant.
[/quote]

yeah this could be powerful.

i could also see a circuit in grants 2.0 whereby someone must do a small GTC stake in order to get their grant into the review queue.  that GTC collateral would be burned if the grant owner is cheating or in violation of the rules in some way

-------------------------

GTChase | 2022-07-12 13:07:53 UTC | #4

This is such an awesome walk through of GTC utility, especially for someone like me who needs it broken down. 

This is one of the main reasons that im super bullish on the work that Moonshot is doing for staking GTC on ones Passport!

-------------------------

ZER8 | 2022-07-12 16:55:05 UTC | #5

Hello @David_Dyor and thank you @owocki for this post and ideas presented, I also read it and since then I'm ideating how to stake/bet GTC on a grants outcome.....still plotting on that.


The reason I jumped in here is to inform you that if we require a small GTC deposit to flag a grant we could actually loose valuable insights/info because of this. I don't think we should place a barrier for people that want to help us. 

BUT, maybe we switch that to **if you flag a grant and you are right** you could get a X return on the GTC you deposited.(5-20 GTC cap or more or with a different mechanism)  :robot: This could have vulnerabilities and could be gamed, but if designed correctly we could at least avoid some issues.

-------------------------

David_Dyor | 2022-07-13 16:31:12 UTC | #6

[quote="ZER8, post:5, topic:11085"]
if we require a small GTC deposit to flag a grant we could actually loose valuable insights/info because of this.
[/quote]

Great point Zer8.  I sense community interest in moving into a creative supportive direction versus a prohibitive policing direction.  Your suggestion completely aligns with this.  We need to ensure that whatever circuits are used in GTC-utility do not compromise on our regen solarpunk ethos.


Legitimate grant projects should have no hesitation to stake serious collateral as they should have full confidence in getting approved.  This might even provide new metrics which can help defend GC or determine optimal capital allocation.  Ofc it could be gamed like anything.

We could even prioritize grant-reviews in descending order of collateral staked, so that those weak projects without confidence don't consume valuable dao resources until we've served the probable-legit-grants first.  Just thinking out loud.

The system is not perfect and sometimes exploitive grants get approved and legit grants get denied.  For whatever reason.  If we start slashing stakes we may find ourselves in litigation.  It is less likely a denied Grantee will sue if they didn't lose anything.  Surely there is a workaround...

-------------------------
