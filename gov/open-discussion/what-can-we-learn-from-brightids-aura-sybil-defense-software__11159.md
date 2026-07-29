---
id: 11159
title: "What can we learn from BrightID's Aura Sybil Defense Software?"
slug: what-can-we-learn-from-brightids-aura-sybil-defense-software
category: open-discussion
url: https://gov.gitcoin.co/t/what-can-we-learn-from-brightids-aura-sybil-defense-software/11159
created_at: 2022-07-24T21:22:10.003Z
last_posted_at: 2022-11-29T11:46:58.846Z
posts_count: 19
views: 8795
like_count: 63
---

# What can we learn from BrightID's Aura Sybil Defense Software?

<https://gov.gitcoin.co/t/what-can-we-learn-from-brightids-aura-sybil-defense-software/11159>
owocki | 2022-07-25 00:36:59 UTC | #1

I think it's interesting how BrightID has designed their Fraud Defense ecosystem, and think there are some things that are worth learning from as Gitcoin [moves more into Grants 2.0 and into Passport](https://gov.gitcoin.co/t/passport-is-our-aws/10995).

BrightID has designed [Aura](https://forum.brightid.org/t/aura-a-new-verification-for-brightid/393), a scalable and decentralized fraud defense software system that rewards users who traverse the BrightID graph and look for sybil attackers.  

Aura is a Sybil battleground game.  This game creates sybil resistence for BrightID.  It's a place where the best motivated, best equipped, and most capable sybil defenders are found and enabled to help the system find sybil attackors.

Here's how it works:
1. BrightID founders and other high trust users designate users who they think are "honest" (this is the trusted seed).
2. Those honest users then get a unit of currency called "Energy".
   - Anyone can create their own system of "trust" and it can be retroactively empowered with energy from these users too.  This enables great ideas and great sybil hunters to come from anywhere.
2. Those users are then able to traverse the BrightID social graph (pictured below) either via the app or via the API and get rewarded with more energy for finding sybil attackors.
3. For example, a user who found the below sybil attackor would receive a lot of energy.

![57b4c815df89342b646257d90c1124df6638e77d|690x335](upload://cvSRuadyrbXivWvE3Sq3caW3Yfz.jpeg)
(Yellow nodes represent a sybil attack. Green nodes represent seeds, which help to identify the honest part of the graph (blue nodes).)

Here's what the App UI looks like.  In the app (or using the API), you can mark ay user as sybil or trusted.
![f7c7eb69345ce1437c56e338c92bd4e62952ef9b_2_1248x1000|624x500](upload://d5w65ycmmsMOArlXUnN5463yCRv.jpeg)

What I find most striking about Aura is how *scalable* and *decentralized* and *modular* it is.  As Gitcoin Grants moves from 1.0 to 2.0, it will be interesting to see if the DAO is able to come up with less centralized, more effective, and more scalable ways of finding & routing sybil attackers.

[Read more about Aura here](https://forum.brightid.org/t/aura-a-new-verification-for-brightid/393).

-------------------------

kyle | 2022-07-25 17:51:25 UTC | #2

I love this. It's so much of what we have been talking about wanting to see from an anti sybil solution. I wonder how they are incentivizing folks to participate. ie, does Energy get turned into a real world reward?

Also, can this tech be used for multiple graphs? (ie, Gitcoin's donation graph)? Here is a snippet of the last month (not include GR14):
![Screen Shot 2022-07-25 at 1.50.06 PM|690x396](upload://bQqoiFxwCgwb0JiarFQU7LOLv40.jpeg)

Identifying Sybils in this graph, and the comparing to "similar" account by Grants donated to, would be really interesting.

-------------------------

owocki | 2022-07-25 18:23:26 UTC | #3

[quote="kyle, post:2, topic:11159"]
Identifying Sybils in this graph, and the comparing to “similar” account by Grants donated to, would be really interesting.
[/quote]

IMO the big opportunity is to decentralize the analysis + gamify the creation of results.  

eg instead of having one large, monolithic, fraud analysis team doing the analysis, the DAO could release the data publicly and let different teams of data analyst's compete to do the best analysis.  the plurality of all of the data analysis's creates a stronger result, the system avoids capture by one group of analysts, and there is permissionless and transparent innovation coming from the crowd.

[Numerai](https://numer.ai/) has been really successful with this approach to doing data analysis (but in a very different context).

i am not clued into the latest approaches by the FDD and GPC, but i wonder what they think.

-------------------------

ccerv1 | 2022-07-25 19:43:29 UTC | #4

[quote="owocki, post:3, topic:11159"]

IMO the big opportunity is to decentralize the analysis + gamify the creation of results.  
[/quote]


:100:
This could be accomplished by exposing a grants subgraph that shows contributions from each wallet address and the desoc data associated with that wallet.

For example:

```
query {
  donors(
    where: {
      grantRound_in: ["GR14"]
    }
  ) {
    id
    contributions {
      grant
      amount
    }
    desoc {
      credentials {
        name
        verificationDate
      }
      nfts {
        id
        mintDate
      }
      poaps {
        id
        mintDate
      }
      lens {
        numFollowers
        numFollowing
      }
      poh {
        profileCreatedDate
      }
    }
  }
}
```

Critically, the API does not show an actual score, just the underlying data needed to build a scoring model.

Developers in the community could create their own scoring algorithms from this data, resulting in a common output, eg, `{​"wallet": "0x..", "sybilScore": 0.87, "squelch":  true}` for a list of wallets.

Developers could also complement the Gitcoin graph with other desoc data from on-chain sources. For example, verses.xyz signatures on Arweave.

FDD could backcheck a proportion of the cases where community algorithms do not achieve consensus. This may require some calibration of the `sybilScore` threshold that triggers a squelch, eg, a more promiscuous algorithm might squelch only 1% of accounts, whereas a tougher one might squelch 10%.

The community's actual Sybil scores + data from past rounds could be exposed (perhaps hiding wallet addresses) for Kaggle style competitions. This would be a great way for data scientists to learn about the shape of the data and test the performance of their models against others.

FWIW, I'm doing some work with FDD on this at the moment. It's a fun dataset and there are some pretty clear signals. For example, the chart below shows a cluster of grants that are strongly preferred by wallets that have no on-chain credentials.

![image|689x375](upload://6tMhqTykjCQiXUFzAQylBb34XbO.png)

-------------------------

castall | 2022-07-25 23:32:43 UTC | #5

[quote="kyle, post:2, topic:11159"]
I wonder how they are incentivizing folks to participate. ie, does Energy get turned into a real world reward?
[/quote]

So far there are no monetary incentives, but the energy overlay allows anyone who wants to reward helpful behavior to identify whom to reward and how much. For example, an app that uses BrightID/Aura to verify uniqueness could periodically drop rewards to any Aura player who helps verify its users.

**More on "Energy"**

Energy is a measure of a sybil hunter / human verifier's effectiveness as judged by other Aura players.  Energy also determines the capacity of an Aura player to provide expert help: i.e. verify regular BrightID users. The more energy someone has, the more verification power they have.

BrightID has long had "seed groups" (pre-trusted people in the graph), but the current process of seed group selection is slow and clunky and done by a seed DAO that hasn't changed much over the years.

Aura will speed this up and make it more resilient to corruption through the use of energy "flavors."  If an energy team (the source of an energy flavor) is found by the public to be corrupt, apps will naturally stop using that energy flavor.  At the same time, new energy teams can form and create new flavors without centralized control.  They just need to convince Aura players to use their energy.  (Each Aura players can pick at most five energy flavors to receive and pass on.) If a flavor needs to be discontinued, Aura falls back on other flavors and continues to operate.

We haven't nailed down any specific incentive model, but you can imagine that energy flavors can be branded and receive sponsorships from apps that use them. The best sybil hunters will receive large amounts of energy in elite flavors. If apps are generous and willing to pay back the value they receive from Aura to energy holders, we hope it will be enough that the best sybil hunters can do it professionally.

[quote="kyle, post:2, topic:11159"]
Also, can this tech be used for multiple graphs?
[/quote]

Yes.  Aura has its own internal graph which is the energy graph.  The nodes in this graph are all Aura players.  The Aura toolbox then provides tools to analyze the BrightID graph and provide assessments about whether its nodes are unique people or sybils.  Right now, the BrightID connection graph is the subject of analysis, and the research tools allow an Aura player to privately and anonymously check facts with other players, but the same Aura game and graph could be used with other graphs or data sets (such as Gitcoin grants data), as long as collaborative fact checking is possible, and Aura players can judge other Aura players' effectiveness.

I want Aura to grow its toolset to include specialized tools to work with a variety of data sets.  An Aura player could be a BrightID specialist, or a Gitcoin grants specialist, or both.

In fact, I think the Aura game could be used for fact-checking in other domains (besides sybil hunting) where experts help to determine who else is an expert in a decentralized manner.

BrightID is useful as a tool to create the expert graph (experts vouching for experts) that is at the core of Aura, but a separate question is what will the experts research?  The BrightID graph itself forms the first subject of research.  Gitcoin grants data could be the second.

-------------------------

gmkung | 2022-07-26 08:38:54 UTC | #6

Interesting idea, but I do wonder if the incentives in Aura are strong enough to incentivise people to take out Sybil attackers in a short enough amount of time. Also if the malicious accounts are dormant (not exhibiting suspicious activities) it can be hard to 'prosecute' them, allowing them to ambush airdrops/governance votes in the future when it is already too late to stop them.

-------------------------

DisruptionJoe | 2022-07-27 09:43:01 UTC | #7

[quote="castall, post:5, topic:11159"]
We haven’t nailed down any specific incentive model, but you can imagine that energy flavors can be branded and receive sponsorships from apps that use them. The best sybil hunters will receive large amounts of energy in elite flavors. If apps are generous and willing to pay back the value they receive from Aura to energy holders, we hope it will be enough that the best sybil hunters can do it professionally.
[/quote]

Short Term - Season 15

Perhaps we could put a small amount of our sybil hunting budget towards "retroactive rewards" for top energy groups or players. 

Long Term - Project to complete for the full launch of Grants 2

This incentive model outlined by @octopus & @j-cook could be a good starting point, but it would need to be specifically optimized to generate trusted outcomes for Aura participation. It could then be used to reward sybil hunters. 

A "Review Protocol" could allow for any community to reward reviewers by paying a minimal amount per epoch and simply "turn the knob" up and down to fine tune the system to the optimal decentralization needed to maintain credible neutrality. 

[quote="castall, post:5, topic:11159"]
Right now, the BrightID connection graph is the subject of analysis, and the research tools allow an Aura player to privately and anonymously check facts with other players, but the same Aura game and graph could be used with other graphs or data sets (such as Gitcoin grants data), as long as collaborative fact checking is possible, and Aura players can judge other Aura players’ effectiveness.
[/quote]

How might we define "collaborative fact checking"? 

[quote="castall, post:5, topic:11159"]
I want Aura to grow its toolset to include specialized tools to work with a variety of data sets. An Aura player could be a BrightID specialist, or a Gitcoin grants specialist, or both.
[/quote]

Would these be different energies or just different games? 

Another way to phrase this might be "Would aura be a review tool which gives an interface for users to review a specific question and the system would provide a trusted outcome?"

OR

"Does aura have any math proofs giving reasonable probalistic guarantees of a trusted outcome with minimal reasonable assumptions?" (if not, could we define some that would get us there?)

[quote="castall, post:5, topic:11159"]
I want Aura to grow its toolset to include specialized tools to work with a variety of data sets. An Aura player could be a BrightID specialist, or a Gitcoin grants specialist, or both.
[/quote]

Do you have a backlog of the tools which need to be built?

## Here are some quick win starting points I see: 


***I think there is a lot of value in combining the aura game mechanics with the reward modeling work we have done.*** 

***There are a few things we could do this season. Would it be better to set deliverables for the BrightID/Aura team to build a grants graph (maybe in collaboration) or should FDD build it?***

***What data could we look at to get an understanding of how well the system is working now?***

I'd really love some quick feedback here from @erich @brent @lthrift @kevin.olsen  @Sirlupinwatson @kishoraditya @omnianalytics @ccerv1 in addition to those mentioned above

## A Review Protocol

Allows a community to retroactively reward the reviewers who participated in a review round if they exceed a certain accuracy/consensus threshold. Scoring may include "gold stars" & "poison pills". ([Rewards Modeling](https://gov.gitcoin.co/t/gia-rewards-okr-report/10438)) 

Gamifies participation in a way that changes the optimal incentive structure in a way that attempting to attack any one round would be less advantageous than being continued to be invited back to play. (Aura)

Allows anyone to create a scoring system for how trusted a reviewer is. Similar to passport and reader. (FDD can be a first "vendor" of a scoring mechanism) 

[quote="castall, post:5, topic:11159"]
In fact, I think the Aura game could be used for fact-checking in other domains (besides sybil hunting) where experts help to determine who else is an expert in a decentralized manner.
[/quote]

Another use case could be grant reviews. Our collaboration with Ethelo tool provided a probabilistic score as an output. This can be used to predetermine eligibility or to provide community reviews of whether or not they are effective with the grants they have received. Grant round owners could elect to show these scores (or others!) and/or use them to programmatically filter grants for eligibility.

A continued partnership with Ethelo could use this gamification and trust model to scale and decentralize execution of grant application reviews for any community-curated grant round*, but would have to build out the ability to dynamically change the weighting applied to each of the reviewers based on a stamp, NFT, or token they hold.

-------------------------

tjayrush | 2022-07-27 18:01:41 UTC | #8

[quote="owocki, post:3, topic:11159"]
instead of having one large, monolithic, fraud analysis team doing the analysis,
[/quote]

This is exactly right. There should not be one large monolithic fraud analysis team.

[quote]
the DAO could release the data publicly
[/quote]

If the data is on-chain, there does not need to be any "releasing..." Yes the cost of smart contracts is high, but is it higher than building an off-chain solution. I think the answer is no if the smart contract system is designed on purpose to be a bit less gas-efficient and a bit more data-exposing.

<hr>
A meager effort to expose and encourage "community data access", is here: https://gitcoin.tokenomics.io/.

Of particular interest is the neighbors column where every address appearing in the same transactions as any of the grants has been extracted. If there's sybil happening, it's happening in that list of addresses.

-------------------------

kishoraditya | 2022-07-28 16:30:43 UTC | #9

[quote="DisruptionJoe, post:7, topic:11159"]
I think there is a lot of value in combining the aura game mechanics with the reward modeling work we have done
[/quote]
This is really interesting, we will be distributing the power of authority into the hands of the community(ies) and in turn, taking it out of the procedural flow and rewarding it! I think more than unit Sybil authentication, this can be a better cluster Sybil level detection!

Just a couple of thoughts/questions: 
1. Instead of open sourcing data at this point, we can create competitive analysis flow through grants itself, rewarding top Sybil hunters with say 0.01 or 0.1% of all the allocated funds in the round. Ecosystems will be happy to do it because it helps them reduce Sybils, their "policies" can act as multiple "energies" in our case. For starters, we can provide datasets through anonymization data protocol to maintain transparency and privacy as we understand it more and improvise it later. The scoring methods by gitcoinDAO itself can be open to all to give a head start whereas data analysts can create on top of it. (top of the mind experimental thoughts) 
2. 

[quote="gmkung, post:6, topic:11159"]
if the malicious accounts are dormant
[/quote]

[quote="kyle, post:2, topic:11159"]
can this tech be used for multiple graphs?
[/quote]

Will this system indirectly create lower average social distancing between the oldest and newest members? I think it will create a range for us, that helps us understand Sybil and non-Sybil associations and emergence in all social clusters. This, IMO, should be a solution for dormant malicious accounts. And associating the reward to grant rounds itself should also create a balance between which system should Sybil try to trick for maximum output for them with the least resources and capital. To be honest more than actual monetary rewards, the gamification part brings in a wider scope of reinforced learning, if planned accordingly.
3. 
[quote="DisruptionJoe, post:7, topic:11159"]
What data could we look at to get an understanding of how well the system is working now?
[/quote]
I am seeing this more as an "aura score (or score as a stamp for passport) " instead of as a whole system because this flow makes it necessary to grow socially for any user, which is a possibility for non-sybil users as well. and such different scores should show a pattern when compared against known and unknown sybils. We can actually input intentional sybils for the betterment of system flow in the experimental flow.
The best points will be to run initially across older datasets or probabilistic outcomes vs experimental outputs.

-------------------------

castall | 2022-07-28 19:50:05 UTC | #10

[quote="gmkung, post:6, topic:11159"]
Also if the malicious accounts are dormant (not exhibiting suspicious activities) it can be hard to ‘prosecute’ them, allowing them to ambush airdrops/governance votes in the future when it is already too late to stop them.
[/quote]

This is a good point.  The main thing that comes to mind here is gating participation on having an Aura verification BrightID passport stamp. This type of verification is harder to get than the basic "meets" verification stamp currently used in Gitcoin Passport.

Aura research can take time.  (It can take longer for someone to be Aura verified rather than meets verified, for example.)  Even if the research couldn't provide evidence quickly enough to stop an attack in progress, Aura could be used to identify which set of experts has "first response" defensive powers to be able to stop such an attack (shut off a grant, etc.)

[quote="DisruptionJoe, post:7, topic:11159"]
How might we define “collaborative fact checking”?
[/quote]

I'm not sure exactly how it might look for Gitcoin grants data, but a vague example would be: an Aura player provides an interpretation of the data, and other Aura players update how much energy they allocate to that player based on how they view the usefulness and correctness of that interpretation.

A more concrete example from BrightID graph analysis in Aura is:  an Aura player already knows the phone number of a person they're researching (and that person's BrightID, since they've connected with them).  The Aura player anonymously checks (using [the known identifiers Aura tool](https://forum.brightid.org/t/fighting-small-scale-sybil-attacks-with-known-identifiers/503#known-identifiers-tool-7)) that the other Aura players that know that phone number are associating it with same BrightID--in a way that doesn't reveal the BrightID (or phone number) to anyone that doesn't already know it.  This makes small-scale sybil attacks getting different BrightIDs verified with different Aura players very hard to pull off.

Basically what we're looking for are ways to compare answers with other Aura players.

-------------------------

bitsikka | 2022-07-29 06:36:40 UTC | #11

[quote="gmkung, post:6, topic:11159"]
Also if the malicious accounts are dormant
[/quote]

Not sure whether it is unintentionally ignored but one of the recurring pattern about most sybil resistant solution efforts known so far, is, by default, assuming ***static*** binary sybil/not-sybil character of agents.

It is obvious that being non-sybil implies that the limited number of key(s) used by the agent will characteristically have a good liveliness or heart-beat, and that the liveliness is essential to be accounted for in a good sybil resistant system.

It is not enough that the key(s) used by agent is old.

It is clear that one of the patterns that a good Aura player will look for in determining whether an agent is sybil is to look for pattern of usage of the agent's key(s).

- A fresh key with hardly any txn is obviously to be rated low
- A key with "natural" history of txn with "reasonable" characteristics of txn, preferably recent, to be rated higher
- A key with natural history but dormant for a long time is to be rated with suspicion especially if the sybil resistant system is only accounting for singular key. If multi-keys are allowed, there must be other keys that are livelier.

Aside:
If we take the dynamic/emergent nature of agent's sociality as one of the key design principles of sybil resistant solution, then:
- to scale, it has to be decentralized in the manner BrightID/Aura and FDD aspires.
- it affords agents the autonomy to freely use multiple keys for them to be safe(to the extent pseudonymity can provide) from global/external legibility.

-------------------------

castall | 2022-07-30 16:30:03 UTC | #12

[quote="DisruptionJoe, post:7, topic:11159"]
Perhaps we could put a small amount of our sybil hunting budget towards “retroactive rewards” for top energy groups or players.
[/quote]

I don't think Aura is ready for this.  I think we should wait for it to exit closed beta first.  I think if Gitcoin FDD (or others reading this) joined the [Aura discord](https://discord.gg/e2ShH4kN3S) and the beta, that could be beneficial later on.

[quote="DisruptionJoe, post:7, topic:11159"]
Would it be better to set deliverables for the BrightID/Aura team to build a grants graph (maybe in collaboration) or should FDD build it?
[/quote]

I think FDD should build it, but Aura can be used to analyze any set of data.  Aura identifies experts and gives them tools to compare answers about a set of data.  The first use case happens to involve a graph of connections (i.e. the BrightID graph), but Gitcoin grants data doesn't have to be in the form of a graph--just in a form (or multiple forms) that allows experts (Aura players) to compare answers.

I like where you're going with your outline for [A Review Protocol](https://gov.gitcoin.co/t/what-can-we-learn-from-brightids-aura-sybil-defense-software/11159/7#a-review-protocol-2) @DisruptionJoe .

[quote="DisruptionJoe, post:7, topic:11159"]
What data could we look at to get an understanding of how well the system is working now?
[/quote]
I would say that it isn't working well yet. We have a closed group of players who are mostly there to give feedback about the interface. We haven't yet built tools like this one [(known identifiers tool)](https://forum.brightid.org/t/fighting-small-scale-sybil-attacks-with-known-identifiers/503) that allow Aura players to justify their actions to other Aura players. (By the way, we would want to use a different set of tools for Gitcoin data than for BrightID graph analysis.)

Anyone reading this is welcome to join the Aura beta ([through our discord](https://discord.gg/e2ShH4kN3S)) and try it out.

-------------------------

DisruptionJoe | 2022-08-01 08:18:26 UTC | #13

[quote="castall, post:12, topic:11159"]
I don’t think Aura is ready for this. I think we should wait for it to exit closed beta first. I think if Gitcoin FDD (or others reading this) joined the [Aura discord](https://discord.gg/e2ShH4kN3S) and the beta, that could be beneficial later on.
[/quote]

Sounds good. We will get two of our sybil hunters to join.

[quote="castall, post:12, topic:11159"]
I like where you’re going with your outline for [A Review Protocol](https://gov.gitcoin.co/t/what-can-we-learn-from-brightids-aura-sybil-defense-software/11159/7#a-review-protocol-2) @DisruptionJoe
[/quote]

I'm shocked that I'm only now understanding the specific roles of each system to build a greater whole! The intuition was there, but the articulation is forming now. I'm in awe of the Aura design. Nice work. 

[quote="castall, post:12, topic:11159"]
We haven’t yet built tools like this one [(known identifiers tool)](https://forum.brightid.org/t/fighting-small-scale-sybil-attacks-with-known-identifiers/503) that allow Aura players to justify their actions to other Aura players.
[/quote]

Joining now!

-------------------------

owocki | 2022-08-15 17:12:13 UTC | #14

if anyone wants to checkout the aura software that brightid uses, this greenpill episode (which just aired last week) is a good tour of it https://www.youtube.com/watch?v=82SNLVQk_KA

-------------------------

castall | 2022-10-19 07:15:06 UTC | #15

Aura had a big update last week and is now usable by apps as a verification tool.

We're not publicizing the beta until we've created some better guides for new users, but if you'd like to join our discord and try it out, I think there are enough people there that can help walk you through it.

Discord:  https://discord.gg/e2ShH4kN3S
Guide (in progress): https://brightid.gitbook.io/aura

-------------------------

castall | 2022-10-28 23:10:54 UTC | #16

[quote="DisruptionJoe, post:16, topic:11235, full:true"]
The current implementation of aura uses graph analysis. Would it be possible to use other types of analysis in the future?
[/quote]

Yes.

At its core Aura is a way for experts to designate other experts in a decentralized way that is resilient to failures like corruption and collusion.

Aura players send each other "energy" (that represents how good they are at the game, aka their expertise).  This forms the inner graph.

In the case of BrightID verification, the outer graph is the last hop where Aura players rate the honesty of BrightID users.

You can see the current graph of [Aura here](https://explorer.brightid.org?aura=aura), with some explanation in [the documentation](https://brightid.gitbook.io/aura) that is still being improved.

Right now there is only one energy team which produces an energy "flavor" that selects experts at verifying people in BrightID. The data they see in Aura is tailored for BrightID verification. Other energy teams can join to increase resilience. If the original energy team's "flavor" of energy becomes flawed or corrupt, the other energy flavors will continue to work and Aura will continue to function.  Apps consuming verifications and individual Aura players decide which energy flavors to use.

What I would like to see are energy teams that look at other sources of information than the BrightID graph.  There will be some tools that help only with BrightID; some that help only with Gitcoin, and some that help with both (not to mention other applications that generate evidence of sybil attacks).

Gitcoin's "outer graph" of verified projects and users could look much different than BrightID and that's great.

Just like there should be more than one energy team analyzing BrightID data, there should be more than one energy team analyzing Gitcoin data.  Aura players can adjust their team affiliations: each player can choose up to 5 energy flavors to send and receive and change this choice as needed.

-------------------------

tkgshn | 2022-11-13 01:28:58 UTC | #17

I wrote about this
https://gov.gitcoin.co/t/decentralized-social-graph-as-an-oracle-powered-by-the-wisdom-of-the-crowd-for-the-era-of-plurality/11927

-------------------------

castall | 2022-11-24 05:14:59 UTC | #18

[quote="DisruptionJoe, post:7, topic:11159"]
Do you have a backlog of the tools which need to be built?
[/quote]

I really want the known identifier tool

https://forum.brightid.org/t/fighting-small-scale-sybil-attacks-with-known-identifiers/503

We've recently created a graph labeling tool where you can draw a lasso around any number of nodes in a graph and leave a comment (and other people can respond to your comment).  Try [going to the aura graph explorer](https://explorer.brightid.org/?aura=aura) and holding down the shift key and drawing a region with your mouse.  You will need energy in Aura to be able to leave a comment.

-------------------------

DisruptionJoe | 2022-11-29 11:46:58 UTC | #19

@Adebola @kishoraditya Let's make sure this is on backlog, not sure how to prioritize, but it should be on there.

-------------------------
