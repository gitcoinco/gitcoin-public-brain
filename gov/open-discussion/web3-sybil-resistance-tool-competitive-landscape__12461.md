---
id: 12461
title: "Web3 Sybil Resistance Tool Competitive Landscape"
slug: web3-sybil-resistance-tool-competitive-landscape
category: open-discussion
url: https://gov.gitcoin.co/t/web3-sybil-resistance-tool-competitive-landscape/12461
created_at: 2022-12-30T15:46:42.658Z
last_posted_at: 2023-01-04T10:51:56.082Z
posts_count: 5
views: 5050
like_count: 15
---

# Web3 Sybil Resistance Tool Competitive Landscape

<https://gov.gitcoin.co/t/web3-sybil-resistance-tool-competitive-landscape/12461>
a33titude | 2022-12-30 15:46:42 UTC | #1

Following the success of my post https://gov.gitcoin.co/t/web3-crowdfunding-tool-competitive-landscape/12266/1 post I have decided to do a similar one for Gitcoin Passport.

As I mentioned in my https://gov.gitcoin.co/t/a-bull-bear-case-for-gitcoin-gtc-in-2023/12442 post, the most positive outlook I can imagine for Gitcoin Passport is:

> Passport will be the foundation of a new sybil resistant economy in web3.

In order to understand if that is on track or not, I created this table of the competitive outlook. Here is the competitive landscape for Sybil Tools in web3:

|- | [Circles UBI](https://joincircles.net/) | [POAP](https://poap.xyz/) | [KYC-DAO](https://kycdao.xyz/)  | [Idena](https://www.idena.io/)  | [BrightID](https://www.brightid.org/)  | [Proof Of Humanity](https://proofofhumanity.xyz/)  | [Worldcoin](https://worldcoin.org/)  |  [Gitcoin Passport](https://passport.gitcoin.co/)  |
|---|---|---|---|---|---|---|---|---|
|Mechanism |Web of Trust |Web of Trust   | Nation State ID   |  Presence/Intelligence Testing | Web of Trust   |  Web of Trust | Biometric  | Aggregator of other mechanisms
| Traction | [100k users](https://twitter.com/koeppelmann/status/1563089304775061504)  | [1million wallets](https://dune.com/greywizard/sgc-work)  | Not launched  | 3k validated identities  | 65K+ sponsored users / 15 Apps Integrated  |  17k users  | 700k users | 100k users  |
| Notable Integrations | $CIRCLES  | ~ | ~  | ~  | Gitcoin, Rabbithole, Unitap, [& others](https://apps.brightid.org/)  | $UBI, easy on-chain integration  |  ~ | Snapshot, Gitcoin Grants
| Pros | ~| ~  | ~  | ~  |  ~ |  ~ |  Distribution worldwide, scale, simple mechanism | Integration with Gitcoin Grants, Pluralistic Approach
| Cons | ~ | Not specifically a sybil tool  |  Nation State IDs not likely to be seen as legitimate in blockchain communities. |   ~|  ~ |  ~ |  Brand  | Not clear if it actually solves for sybil resistence, how well it scales across identities,
| Comments | Backed by Gnosis| Not specifically a sybil resistance tool, but could be useful for sybil resistance  | ~ | ~ |  Backed by [Vitalik](https://twitter.com/VitalikButerin/status/1288545712343527425), [lengthy thread on Gitcoin/BrightID Aura here](https://gov.gitcoin.co/t/what-can-we-learn-from-brightids-aura-sybil-defense-software/11159) |   Forking Soon, Backed by [Vitalik](https://ubi-alliance.medium.com/vitalik-buterin-supporting-proof-of-humanity-16339af97104)  | Backed by Silicon Valley Luminaries | 

I was not able to find all information for all of the tools so please comment below if there is something I missed or got wrong.

Some trends I observed while doing this analysis:
1. The tools with good developer docs seemed to have more apps built on top of them.
2. The tools with built in economics (eg Passport & Gitcoin Grants, Proof of Humanity & UBI, Worldcoin & Worldcoin airdrop) seemed to have the most distribution.
3.  There are a lot of web of trust based tools.
4.  While many of these tools claimed to solve sybil resistance, none of them really had easy to use tools that allowed you to inspect whether it was working or not (except BrightID and their Aura tool)

I think that the web3 sybil resistance ecosystem is small but growing, with no clear winner yet.  It seems to me it's anyone's game to create an ecosystem that has exponential growth and runaway value.

It's possible that there will be multiple winners.   These are the scenarios I am considering:
1. There is 1 winner.
2. There is 1 winner for creating sybil resistant identities (user centered use cases) and another 1 winner for making those identities easy to use with things like Sign In With Ethereum (developer centric use case).
3. There are multiple winners in each of those categories.
4. Because of the composability of this space, "winner" is too zero-sum of a mentality.  All of these apps will rise and fall together.

---------------------

This is what I would like to see in 2023:

> Passport will be the foundation of a new sybil resistant economy in web3.

Is Gitcoin Passport on track for this outcome?  Why or why not?  Which projects in the above list should Gitcoin try to emulate or integrate with?

-------------------------

castall | 2022-12-30 21:30:35 UTC | #2

I love to see research like this.

More points of interest about BrightID/Aura

* There is a snapshot BrightID strategy.  SongADAO is using it.

* BrightID Aura has a [Soulbound Token standard](https://github.com/BrightID/BrightID-Soulbound-Token)
* BrightID & Aura are happy to be stamps in Gitcoin Passport .  BrightID has always positioned itself as a stamp, not a wallet or passport. 
* BrightID has social recovery which we'd like to bring to Gitcoin Passport.  Maybe Gitcoin Passport could help bring (decentralized) institutional recovery (e.g. recover with Gitcoin, Giveth, etc. -- like social recovery but with semi-trusted orgs).
* BrightID would like to bring its privacy tech to Gitcoin Passport so users can avoid cross-linking or doxxing. ([See this post.](https://gov.gitcoin.co/t/passport-scoring-as-a-service/12419/3))
* Aura at its core is a decentralized tool for experts appointing other experts. The experts can operate in any domain.  We'd like to add Gitcoin as an energy team to allow independent Sybil hunters to help Gitcoin and learn to use its legos.


I'm looking forward to much more collaboration between Gitcoin and BrightID in 2023.

-------------------------

DisruptionJoe | 2023-01-02 15:23:04 UTC | #3

[quote="a33titude, post:1, topic:12461"]
While many of these tools claimed to solve sybil resistance, none of them really had easy to use tools that allowed you to inspect whether it was working or not (except BrightID and their Aura tool)
[/quote]

Very true. This is where the sybil scoring legos we are building with FDD will come into play. Think of each individual analysis as having a boolean output. The exploratory analysis of these has primarily been done and funded by FDD/Gitcoin in the past. Now we have built up the Open Data Community to split this cost with other orgs. Our hackathon in October was 100% Gitcoin funded prizes. The upcoming one in January is 39% Gitcoin funded! 

We also clarified the specifications to include containerization and a boolean output. For more on the anti-sybil legos see the articles [here](https://gov.gitcoin.co/t/introducing-the-fdd-review/11095).

When you envision this productized where the interface for a fraud analyst or round operator can utilize the many legos beneath the surface, here are a few ways to think of it:

- As a fraud analyst, I want to be able to suggest  wallet/passport/grant and see how it relates to it's relevant sybil analysis legos. 
- As a fraud analyst, I want to be able to upload a list of wallets/passports/grants and get an output with the rows being the identifier and the columns being the boolean output of each lego. 
- As a fraud analyst, I want to be able to select which analysis legos are executed for my list to save on computation costs. 

We have a much more detailed article coming out this week really sharing the vision along with the start of the hackathon which have rewards for both the exploratory analysis discovering new analysis legos and the building of legos, contanerization/standardization of known analysis.

-------------------------

a33titude | 2023-01-04 04:40:14 UTC | #4

[quote="DisruptionJoe, post:3, topic:12461"]
Think of each individual analysis as having a boolean output
[/quote]

Am I correct in presuming the boolean output is whether the user is a sybil attacker or not?

[quote="DisruptionJoe, post:3, topic:12461"]
When you envision this productized where the interface for a fraud analyst or round operator can utilize the many legos beneath the surface, here are a few ways to think of it:
[/quote]

Is there any place I can read about the holistic 2023 roadmap for Passport?  Or see wireframes of what it will look like at the end of 2023?  I get bits and pieces here and there, it would be great to see something holistic.

-------------------------

DisruptionJoe | 2023-01-04 10:51:56 UTC | #5

[quote="a33titude, post:4, topic:12461"]
Am I correct in presuming the boolean output is whether the user is a sybil attacker or not?
[/quote]

We would be lucky to have that! Unfortunately, it turns out that there is no one analysis that says for sure that user is sybil. Instead, we have many of these "legos" that say a user is likely sybil via a combination of multiple signals. 
1. if a user is triggering specific known combinations 
2. If they pass a threshold score from an ML model.  The model looks at all these outputs against our "Thor & Loki" datasets (read: for sure not sybil & for sure sybil)  We then choose a threshold whereby we deem the users most likely sybil. This method aims to minimize false positives even over avoiding false negatives. 

Here is a comment from a past budget discussion where I explained how any one signal is not sufficient on its own. https://gov.gitcoin.co/t/proposal-fdd-season-14-budget-request/10658/12?u=disruptionjoe

[quote="a33titude, post:4, topic:12461"]
Is there any place I can read about the holistic 2023 roadmap for Passport? Or see wireframes of what it will look like at the end of 2023? I get bits and pieces here and there, it would be great to see something holistic.
[/quote]

My team at FDD is working with the GPC Passport team to do a few specific things. 
1. In November we provided 4 models for scoring they could use for preventative sybil defense. These one score to rule them all models aren't as good as customized scores per use case, but it is more scalable and we are studying how well it works. 
2. We performed analysis to estimate the effectiveness of the Snapshot & Bankless integrations and fine new "legos" specific to their use cases. 
3. We created a topology model and recommendations for which stamps to prioritize to solve sybil resistance. The GPC team is thinking about UX and has final say for what is prioritized. At this point, they seem to be leaning towards a steward voting model to determine which stamps are included. (I believe this is a mistake because the purpose of passport is to solve sybil resistance, not to be a popularity contest, but we hope stewards will take FDD recommendations.) 
4. We are documenting and building pipelines for best way to extract data from ceramic and join with other data such as onchain signals. 

Here is a view of priorities from the cross-functional passport pod priorities for this season. 

![Image 2023-01-04 at 11.47.08 AM|690x346](upload://oK7LratZxoJxeFSxogB9efaTZiT.jpeg)

-------------------------
