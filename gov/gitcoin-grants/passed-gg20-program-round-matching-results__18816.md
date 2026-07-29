---
id: 18816
title: "[PASSED] GG20 Program Round Matching Results"
slug: passed-gg20-program-round-matching-results
category: gitcoin-grants
url: https://gov.gitcoin.co/t/passed-gg20-program-round-matching-results/18816
created_at: 2024-05-16T22:24:31.103Z
last_posted_at: 2024-07-09T18:13:32.940Z
posts_count: 40
views: 8589
like_count: 115
---

# [PASSED] GG20 Program Round Matching Results

<https://gov.gitcoin.co/t/passed-gg20-program-round-matching-results/18816>
umarkhaneth | 2024-05-28 15:32:33 UTC | #1

UPDATE: We ratified results [on snapshot](https://snapshot.org/#/gitcoindao.eth/proposal/0x3527cb7a0c0e2100fc508b3d3b95e255ab34b95a18fd5fe6ab41c928d8aa5901) on May 28th

Hey y’all, our GG20 OSS program round matching results are live [here](https://docs.google.com/spreadsheets/d/1rZ9JPldY1AjzMdGgfqpfRfxlUyQdGLoVAZJ90Eamxq4/edit#gid=1546480797)! We’ll have five days for review and feedback then, barring any major issues, will move to ratify on snapshot on May 22nd and payout on May 28th.

Special thanks to  @Joel_m, @MathildaDV, @sejalrekhan, @M0nkeyFl0wer, @Jeremy, @meglister, @owocki  and @deltajuliet for their eyes, comments, and feedback! 


# TL;DR

* GG20 saw a [number of exciting developments](https://www.gitcoin.co/blog/announcing-gg20) including a $1M OSS matching pool, the election of a grants council, an upgrade to our core protocol, and a deepened partnership with our friends at Arbitrum.
* We implemented a two-pronged [sybil resistance strategy](https://gov.gitcoin.co/t/our-sybil-resistance-strategy-for-gg20/18524). We used a [pluralistic variant of QF](https://gov.gitcoin.co/t/nerd-post-updates-to-cluster-mapping-matching/18705) and we used Passport's model based detection system. We did not do any closed-source silencing of sybils/donors. Instead, we’re solely relying on our mechanism and Gitcoin Passport.
* Discussion will be open for five days before moving to snapshot on May 22nd. 

# 🌎 GG20 Overview

Every round sees new developments. Some of the most exciting in GG20 included:
* Returning to our [Open Source Software](https://gov.gitcoin.co/t/gg20-project-charter/18307) roots, doubling the number of rounds, projects, and matching funding available since GG19.
* Initiating [Community Rounds Governance](https://gov.gitcoin.co/t/gg20-community-round-governance-a-retrospective/18766), electing a council to allocate matching funds for community-led QF rounds. Read [the retro](https://gov.gitcoin.co/t/gg20-community-round-governance-a-retrospective/18766) and see the [proposal to extend the council’s term](https://gov.gitcoin.co/t/proposal-extending-the-term-of-gg-community-council/18776).
* Upgrading our core protocol to enable more permissionless building, going from [allo v1 to allo v2](https://docs.allo.gitcoin.co/), with GG20 being the first rounds to run on our new protocol!
* Providing the same sybil resistance tooling we use for our rounds to every community using Grants Stack by creating a [cluster-matching calculator](http://github.com/gitcoinco/qf-calculator) and integrating with [Passport’s model based detection](https://support.passport.xyz/passport-knowledge-base/stamps/guide-to-model-based-detection).
* Expanding our collections feature, enabling more people to add their own grant collections.
* Seeing the proliferation of side-apps and tooling, following our [modular, unix philosophy](https://gov.gitcoin.co/t/gitcoin-could-embrace-the-unix-philosophy-to-create-exponential-innovation/18602). GG20 launches included [GG Wrapped](https://ggwrapped.gitcoin.co/), [Grants Scan](https://grantscan.gitcoin.co/), [IDriss cross-chain donations on Twitter](https://www.idriss.xyz/), [gitcoindonordata.xyz](http://gitcoindonordata.xyz), and [a QF calculator](http://github.com/gitcoinco/qf-calculator) for round managers.
* Consolidating all of our program rounds onto Arbitrum, partnering with [Arbitrum and Thrive Coin](https://gov.gitcoin.co/t/thriving-gg20-thank-arb-and-gitcoin/18565) to expand the matching pool and incentives for contributors and grantees.

## Key Metrics:

### Overall

* 11 Total Rounds
* $1.647M Matching Pool
* $633,431.29 Crowdfunded
* 35,109 Unique Donors
* 629 Projects
* More data [here](http://gitcoin.co/grants-data)

### OSS Program

* 4 Program Rounds
* $1.0M Matching Pool
* $484,487.00 Crowdfunded
* 28, 393 Unique Donors
* 327 Projects

# 🧮 Round and Results Calculation Details

Before GG20 began, we proposed a two-pronged [sybil resistance strategy](https://gov.gitcoin.co/t/our-sybil-resistance-strategy-for-gg20/18524). To recap it briefly, we would continue to use COCM (Connection-Oriented Cluster Matching) as we had in GG19 and we would additionally introduce passport’s model-based detection system.

As explained in the post, and the [paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4311507) which introduced this mechanism to the world, COCM is much less vulnerable to Sybil Attacks than ordinary QF because it reduces the matching of donors who look similar.

In addition, testing Passport’s model-based detection system (PMBDS) on GG19 donor data yielded greater sybil resistance than the stamp-based system without any of the user friction. When used together, we believe these two tools produce the most sybil-resistant results we’ve ever had.

We also continue the precedent we began in GG19 of not doing any black-box squelching of donor accounts. All of the code we used to calculate results is [available on GitHub](http://github.com/gitcoinco/qf-calculator). Turning off squelching has allowed us to increase transparency of matching result calculations and reduced our time to payouts. In addition, it enabled us to scale the same sybil resistance methods we use to our partners through integrations with Grants Stack.

## Recap of COCM: [Connection-Oriented Cluster Matching](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4311507)

Quadratic Funding empowers a decentralized network to prioritize the public goods that need funding most. In doing so, it amplifies the voices of those with less money, ensuring bigger crowds receive more matching funds than larger wallets. However, it can be exploited by sybils or colluding groups who align their funding choices to unfairly influence matching fund distribution.

[COCM](https://www.gitcoin.co/blog/wtf-is-cluster-matching-qf) is one of the tools we use to address this issue. It identifies projects with the most diverse bases of support and increases their matching funds. It offers a bridging bonus for projects that find common ground across different groups, rewarding cross-tribal support and broad reach. In this way, COCM values not only the number of voters supporting a project but also the diversity of tribes supporting it.

Recently, Joel upgraded the mechanism further with a [Markov chain approach](https://gov.gitcoin.co/t/nerd-post-updates-to-cluster-mapping-matching/18705), which assesses the likelihood of a user's connection to a project based on intermediate connections. In experiments, this provided more sybil resistance by a large margin.

As an unintended side effect, COCM also tends to distribute funding away from top projects and toward the long tail.

## Passport’s Model Based Detection System

The Gitcoin Passport team has recently introduced a Model-Based Detection System that analyzes the on-chain history of addresses, comparing them to known human and sybil addresses. The model assigns each address a probability of being a genuine human user.

In GG20, this model detected 42.39% of participating wallets as very likely belonging to sybils, and these wallets were excluded from matching. The unmatched wallets accounted for 22.55% of all crowdfunded dollars. 

While the model isn't perfect and sometimes mistakes new users or those with few mainnet transactions for sybils, the team is continuously improving the dataset and expanding the model to L2s. Overall, it effectively reduced the impact of sybil accounts on matching results.


# 💡 Project Spotlight

Here are the top five projects by total matching funding and per voter matching funding for each of our four rounds (gleaned from the [overall matching results](https://docs.google.com/spreadsheets/d/1rZ9JPldY1AjzMdGgfqpfRfxlUyQdGLoVAZJ90Eamxq4/edit#gid=1546480797)). The “total matching” list highlights those who received the most support overall, while the “matching per voter” list showcases those who received the most diverse support, benefiting from the use of COCM. The projects on this list are the ones with the most diverse bases of support, regardless of the size of the base.

### Developer Tooling & Libraries - Top 5 by Total Matching

| Rank | Project | Matching Funds |
|------|---------|----------------|
| 1    | [ethers.js](https://explorer.gitcoin.co/#/round/42161/27/3) | $29,637.50   |
| 2    | [OpenZeppelin Contracts](https://explorer.gitcoin.co/#/round/42161/27/41) | $23,281.82   |
| 3    | [Blockscout Block Explorer - Decentralized, Open-Source, Transparent Block Explorer for All Chains](https://explorer.gitcoin.co/#/round/42161/27/12) | $17,741.54   |
| 4    | [Swiss-Knife.xyz](https://explorer.gitcoin.co/#/round/42161/27/33) | $16,518.84   |
| 5    | [Wagmi](https://explorer.gitcoin.co/#/round/42161/27/30) | $16,243.91   |


### Developer Tooling & Libraries - Top 5 by Matching per Voter

| Rank | Project | Matching Per Voter (Avg) |
|------|-------------------------------------|--------------------------|
| 1    | [Swiss-Knife.xyz](https://explorer.gitcoin.co/#/round/42161/27/33) | $83.43   |
| 2    | [Viem](https://explorer.gitcoin.co/#/round/42161/27/20) | $64.28   |
| 3    | [Ape Framework](https://explorer.gitcoin.co/#/round/42161/27/15) | $60.40   |
| 4    | [ethui](https://explorer.gitcoin.co/#/round/42161/27/8) | $60.34   |
| 5    | [Pentacle](https://explorer.gitcoin.co/#/round/42161/27/35)  | $57.51   |


### Hackathon Alumni - Top 5 by Total Matching
| Rank | Project | Matching Funds |
|------|---------|----------------|
| 1    | [NFC wallet](https://explorer.gitcoin.co/#/round/42161/23/36) | $10,000.00   |
| 2    | [WalletX  A Gasless Smart Wallet](https://explorer.gitcoin.co/#/round/42161/23/0) | $7,592.87   |
| 3    | [Fluidpay](https://explorer.gitcoin.co/#/round/42161/23/27) | $7,228.21   |
| 4    | [RejuvenateAI](https://explorer.gitcoin.co/#/round/42161/23/32) | $6,121.22   |
| 5    | [Mosaic: Earn rewards for using your favorite web3 apps and protocols](https://explorer.gitcoin.co/#/round/42161/23/40) | $3,801.02   |


### Hackathon Alumni - Top 5 by Matching per Voter

| Rank | Project | Matching Per Voter (Avg) |
|------|---------|--------------------------|
| 1    | [hashlists](https://explorer.gitcoin.co/#/round/42161/23/48) | $69.02   |
| 2    | [Gnomish](https://explorer.gitcoin.co/#/round/42161/23/49) | $66.79   |
| 3    | [DeStealth](https://explorer.gitcoin.co/#/round/42161/23/34) | $63.23   |
| 4    | [Mosaic: Earn rewards for using your favorite web3 apps and protocols](https://explorer.gitcoin.co/#/round/42161/23/40) | $60.33   |
| 5    | [Margari](https://explorer.gitcoin.co/#/round/42161/23/2) | $60.23   |

### Web3 Infrastructure - Top 5 by Total Matching

| Rank | Project | Matching Funds |
|------|---------|----------------|
| 1    | [DefiLlama](https://explorer.gitcoin.co/#/round/42161/26/14) | $30,000.00   |
| 2    | [L2BEAT](https://explorer.gitcoin.co/#/round/42161/26/66) | $25,206.67   |
| 3    | [Umbra](https://explorer.gitcoin.co/#/round/42161/26/67) | $17,319.34   |
| 4    | [Dappnode](https://explorer.gitcoin.co/#/round/42161/26/48) | $16,165.74   |
| 5    | [Ethereum Attestation Service (EAS)](https://explorer.gitcoin.co/#/round/42161/26/42) | $16,022.61   |

### Web3 Infrastructure - Top 5 by Matching per Voter

| Rank | Project | Matching Per Voter (Avg) |
|------|---------|--------------------------|
| 1    | [Ethereum on ARM](https://explorer.gitcoin.co/#/round/42161/26/30) | $14.65   |
| 2    | [The Tor Project](https://explorer.gitcoin.co/#/round/42161/26/24) | $14.55   |
| 3    | [Lighthouse by Sigma Prime](https://explorer.gitcoin.co/#/round/42161/26/69) | $14.41   |
| 4    | [eth.limo](https://explorer.gitcoin.co/#/round/42161/26/9) | $10.69   |
| 5    | [libp2p General](https://explorer.gitcoin.co/#/round/42161/26/98) | $10.63   |
| HM | [Lodestar](https://explorer.gitcoin.co/#/round/42161/26/38) | $10.58

### dApps & Apps - Top 5 by Total Matching

| Rank | Project | Matching Funds |
|------|---------|----------------|
| 1    | [JediSwap](https://explorer.gitcoin.co/#/round/42161/25/96) | $15,000.00   |
| 2    | [IDriss - A more usable web3 for everyone](https://explorer.gitcoin.co/#/round/42161/25/92) | $15,000.00   |
| 3    | [Hey.xyz (formerly Lenster)](https://explorer.gitcoin.co/#/round/42161/25/1) | $15,000.00   |
| 4    | [Revoke.cash](https://explorer.gitcoin.co/#/round/42161/25/25) | $15,000.00   |
| 5    | [Event Horizon](https://explorer.gitcoin.co/#/round/42161/25/105) | $12,098.09   |

### dApps & Apps - Top 5 Matching per Voter

| Rank | Project | Matching Per Voter (Avg) |
|------|---------|--------------------------|
| 1    | [rotki](https://explorer.gitcoin.co/#/round/42161/25/8) | $27.93   |
| 2    | [Karma GAP](https://explorer.gitcoin.co/#/round/42161/25/83) | $26.87   |
| 3    | [Giveth](https://explorer.gitcoin.co/#/round/42161/25/55) | $25.94   |
| 4    | [Funding the Commons](https://explorer.gitcoin.co/#/round/42161/25/95) | $22.78   |
| 5    | [Glo Dollar](https://explorer.gitcoin.co/#/round/42161/25/51) | $22.06   |


# Code of Conduct

As a reminder to all projects, [quid pro quo](https://support.gitcoin.co/gitcoin-knowledge-base/about-gitcoin/policy/understanding-potential-attack-vectors/bribery-quid-pro-quo) is explicitly against [our agreement](https://grants-portal.gitcoin.co/gitcoin-grants-grantee-portal/gg19-eligibility). Providing an incentive or reward for individuals to donate to specific projects can affect your ability to participate in future rounds. If you see someone engaging in this type of behavior, please [let us know.](https://forms.gle/n3b5MDgHskehNQ7s8)

# Next Steps

We plan to distribute the matching by May 28th, after the [results](https://docs.google.com/spreadsheets/d/1rZ9JPldY1AjzMdGgfqpfRfxlUyQdGLoVAZJ90Eamxq4/edit#gid=1546480797) are ratified through governance. We are leaving five days of discussion on this post, and barring any major problems or issues found with these results, will proceed to a Snapshot vote that is open for five days.

It's worth noting that GG19 pre-approved the matching fund to be paid out before results were posted. This is a strong precedent and, if the community agrees, we could pass a policy that matching payouts for all future rounds not require ratification. 

We are also hosting an internal retro on May 20th and will publish further results and learnings. And as always, a detailed blog post will be published on the day that payouts are distributed.

We're also always looking for direct feedback from the community on which improvements would make GG21 even better. Please don't hesitate to let us know!

![|624x557](upload://rqT88fXJEsoViTuugd299v5m59p.jpeg)

-------------------------

georgedonnelly | 2024-05-16 23:24:28 UTC | #2

FYI The overall results Google Sheet seems to not have sharing access turned on.

-------------------------

umarkhaneth | 2024-05-16 23:37:59 UTC | #3

Thanks for the msg! Just updated that

-------------------------

DistributedDoge | 2024-05-17 02:55:32 UTC | #4

Overall I am happy with the improved process. Here is my initial feedback: 

1. As the calculation method is progressively getting more complex, matching results of GG20 are much harder to "eyeball" than those of previous rounds. Therefore, it is very much apperciated, that you published code used to obtain those results.
2. Results seem "noisy" in that project with smaller number of supporters and crowdfunding can do much better than project with twice as many supporters. I know I have to take into account sybils + distribution of votes + clusters but link between "did well during the round' -> "got money during matching" seems weaker than in previous rounds. Not a blocker, as I guess this is "diverse support" part of algorithm working as intended, but something to think about for GG21. 
3. I would be in favour of streamlining the ratification process 5 days + 5 days feels excessive for most situations where there are no important objections, beyond small tweaks. 
4. Having my account passively scanned by some third-party black-box model is much less hassle than manually collecting stamps, so overall, it is an improvement.


As for results themselves, I only took quick look, but I do not see anything obviously wrong with the spreadsheet, so at this moment my only question is:

 1) In `Web3 Infrastructure` round, `Facet` project was top 1 in crowdfunding but I do not see it appear in matching at all. What happened there?

-------------------------

umarkhaneth | 2024-05-17 03:48:32 UTC | #5

Thanks for the thoughtful feedback @DistributedDoge 

1. I'm glad to hear that! This is one of the ways we're trying to improve trust in the process. We're also looking for ways to make cluster matching even easier to understand, including visualizations, writings, apps, or videos. Would love to see more folks getting involved!

2. This is a good point and it's worth asking where the noise is coming from here. Due to sybils and airdrop farmers, many of the 'voters' or 'wallets' numbers make projects with less genuine support *seem* as if they have more than they do. I think this is where the noise comes from. If these are used as the barometer for what's doing well during the round it could even be misleading. Maybe we should start displaying different numbers like 'users passing passport' or 'clusters supporting project' or a 'diversity score.' I'm just thinking out loud here and responding to your thought. When looking at the average matching per voter, by project, I think the mechanism is finding the signal in the noise and correctly identifying projects with a diverse support base.

3. Good to know!

4. 😅

[quote="DistributedDoge, post:4, topic:18816"]
In `Web3 Infrastructure` round, `Facet` project was top 1 in crowdfunding but I do not see it appear in matching at all. What happened there?
[/quote]

It looks like this project is listed in my spreadsheet under the name Ethscriptions which is currently #6 by matching in the Web3 Infrastructure round. I think perhaps there's a mapping error here. The founder of both projects is the same and it might be that the Facet project overwrote the Ethscriptions project but the update didn't propagate everywhere. Rest assured, they're getting matching!

-------------------------

skilesare | 2024-05-17 03:22:39 UTC | #6

Is there some way to get at the underlying results and data?  As most of our community was coming from outside the ETH universe I wasn't expecting a huge match, but where we ended up is disappointing nonetheless.  I'd like to better understand what went wrong and what we can do better as a community in the next round.  I Do see some strange behavior on the address of our project on Arbitrum where there are a ton of donations of all the same amounts, but, if I'm understanding the data correctly, those look like someone was carpet-bombing a bunch of projects.  These seem to have really brought my per-donation average down.  Other projects out of our ecosystem that I would expect to have a large overlap in donor base got 2x multipliers in Dapps and 9x in Tooling...but their averages were much higher but with like 50 less donations.

I'm super happy with however people want to donate, but did this carpet bombing lower our score somehow? If it did, how would I tell?  At first I thought some degen in our community(we love them, but..you know) may have tired to get creative and was hoping it would be obvious and I could just do some finger waving for next round, but I'm not sure how to look at this now.

If I take out these 46 or so contributions that were part of a carpet bomb my average goes from about 1.5 to 9.1 per donor.  Maybe these carpet bombs are across the whole category? It seems these folks (or maybe it was one person over and over since the amounts were so similar) were dropping like 0.035 ETH to 100 projects at a time.  Maybe this was some meta contract or app splitting something up because it was pretty uniform and happening over a concentrated amount of time.

It looks like out of the there big rounds my project ended up with a 271st out of 274th multiplier and I'm just trying to figure out why. It seems that a higher average helped you more than a larger number of donors which I thought was supposed to be the opposite of how QF worked.  I was pretty intentional with my community(many of whom were pretty beat up by the bear) that just giving something was helpful.  Maybe some of them took that too literally?

It looks like that if I just sent back these 46 carpet bomb donations totaling about $46 getting me to the about $9/donation and the take the average of others that averaged between $8-$10 that I'd end up with around a 3x match vs a 0.3 match(again, this is irrelevant if everyone in my category got the same carpet bomb...i know at least 100 other projects did because these 46 transactions all look the same).  This is the difference in me trying to attract a developer to justify engaging in some significant work with $540 vs $1900. Neither is earth-shattering, but its a pretty big difference what kind of work we can pursue.

Also, maybe this is all batch and I'm seeing the output of some other contract or system somehow? Anyway....any insight into what went wrong would be helpful(again maybe it is as simple as our donators not having passports or much ETH address history as most had to ask me how to get eth and then bridge it and haven't been super active in the EVM ecosystem in a few years...but also the other project from our little corner did ok with matching.)

-------------------------

thedevanshmehta | 2024-05-17 05:07:24 UTC | #7

I quickly scanned the results of each round & am quite happy with the results. In most cases, the ratio of matching : crowdfunding is greater than 1, sometimes significantly so, which is breaking new ground for open source rounds (which has always had more participation than matching since the beta round)

I personally do like seeing the results first before voting on them but that might just be me . Its like shareholder meetings where the management wants their renewal approved at the start itself, but shareholders insist on doing it at the end to give the meeting some color.

Overall quite happy with how Sybil analysis has evolved since the beta round, good job ! I also do love how even smaller projects have seen many multiples over the amount crowdfunded

-------------------------

CryptoRohittt | 2024-05-17 05:28:45 UTC | #8

**Subject: Request to review Hackathon Alumni Round Ranking**

Hello Gitcoin team, I am from the WalletX team. We participated in the Hackathon Alumni Round in GG20 and were very active in joining Gitcoin's Twitter Spaces + engaging with Donors community!

At the end of the GG20, WalletX had the maximum number of donors (689) and maximum amount donated (~1.34k) in the Hackathon Alumni Round! We had worked very hard to connect with our friends in communities. We leveraged our relationships with KOLs and requested them to support us. We were running 2nd the whole time but on the last day of GG20, we finally acquired the leaderboard after some KOL friends decided to support us by sharing within their communities. We also Livestreamed our excitement when we finally saw ourselves 1st in the leaderboard on the last few hours! And with a HUGE margin!

But now when we got the email from Gitcoin, we are shocked to see that we are ranked 2nd? I cannot understand why! :slightly_frowning_face:

-------------------------

CryptoRohittt | 2024-05-17 06:29:34 UTC | #9

There is no way for us to know what was the Average Similarity Score of Donor's for each participating project OR to understand the clusters and donor connections. The QF reports are not shared by Gitcoin.

-------------------------

crypto_bob | 2024-05-17 07:42:15 UTC | #10

Why are Rotki and Giveth receiving so high matching, while having low number of unique donors & total amount raised. 300 votes and $1000 in donations seems too little for the 9th spot. I dare not say it, but maybe being good friends with the founder of Gitcoin has more to do it than we think.

-------------------------

ayush035 | 2024-05-17 09:09:43 UTC | #11

Hey  Gitcoin Team , I am from the Stogram team , Our project is in the hackathon alumni round. We received donations from 86 unique donors and secured our rank on the leaderboard on the 7th position . But in the matching results for the Hackahton alumni I can see projects with 30-33 unique contributors much ahead of out project , Like how's that possible that recieving donation 86 users receive less matching than the projects who received donation by 30 users , I appeal to the Gitcoin team to please look into the results and please help us out with this. 
Thankyou
Team Stogram

-------------------------

wasabi | 2024-05-17 12:17:19 UTC | #12

gm @crypto_bob, this article may be a good resource to understand how Cluster Matching works

https://www.gitcoin.co/blog/wtf-is-cluster-matching-qf

-------------------------

Kronosapiens | 2024-05-17 13:31:14 UTC | #13

One metric which I would like to see if possible is the average passport score of the donors for a given project. Knowing the number of donors and amount donated is insufficient to even intuitively try and guess what the match will be, as the average passport score acts as a confound. Average and standard deviation would be even better!

-------------------------

Joel_m | 2024-05-17 15:45:44 UTC | #14

[quote="DistributedDoge, post:4, topic:18816"]
Results seem “noisy” in that project with smaller number of supporters and crowdfunding can do much better than project with twice as many supporters. I know I have to take into account sybils + distribution of votes + clusters but link between "did well during the round’ → “got money during matching” seems weaker than in previous rounds. Not a blocker, as I guess this is “diverse support” part of algorithm working as intended, but something to think about for GG21.
[/quote]

You're totally right about this, Umar and I have been spending a lot of time discussing the way that COCM (as its currently tuned) gives a more flat funding distribution in most cases, compared to what standard QF would do. 

Aside from what Umar said on this, the other good news is that we always have the ability to tune COCM further. So if there's a push from the community to make the algorithm show a stronger link of "did well during the round’ → “got money during matching”, that's not too hard to do from a technical standpoint. It's just a balance between that and Sybil resistance + prioritizing plurality, but I don't think there's any "right" answer per se.

Actually, I'm leaning towards making a separate forum post and/or holding some kind of vote to get wider community feedback on this ahead of GG21.

-------------------------

Moeen | 2024-05-17 19:38:24 UTC | #15

Hello,

I’m Moeen from BerryLab. First, I’d like to express my appreciation for the early release of the GG20 OSS program round results and the opportunity for open discussion prior to the snapshot. It’s great to see this level of transparency and engagement.

However, I have a concern regarding the matching funds allocated to our participation in Dapp & Apps project. Despite being ranked 20th in both the number of contributions and the total amount contributed, we find ourselves ranked 46th in matching funds, receiving $147 less than our contributed amount. This discrepancy is particularly puzzling because I noticed projects with around $200 in contributed funds receiving the same matching amount as us, even though we have 5-10 times more contributors.

Could you please help me understand the rationale behind the allocation of matching funds in this case? Insights into the process will be invaluable for our future participation and ensure we align better with the intended outcomes of the program.

-------------------------

umarkhaneth | 2024-05-18 01:51:21 UTC | #16

[quote="skilesare, post:6, topic:18816"]
Is there some way to get at the underlying results and data?
[/quote]

Hi skilesare, you can always find voting data available via SQL in our metabase instance at [regendata](https://github.com/ufkhan97/regendata) or our Indexer's [GraphQL endpoint](https://github.com/gitcoinco/grants-stack-indexer?tab=readme-ov-file). For GG20 I also uploaded  CSVs [here](https://drive.google.com/drive/u/1/folders/1_FQdrNLiTPxJ7OHIJFULGDxOIuW3_vvt). 

[quote="skilesare, post:6, topic:18816"]
As most of our community was coming from outside the ETH universe I wasn’t expecting a huge match, but where we ended up is disappointing nonetheless. I’d like to better understand what went wrong and what we can do better as a community in the next round.
[/quote]

I understand ending up with less funding than you expected can be really disappointing. I also hear you that you want to better understand what happened and how results are calculated. In your shoes, I'd want the same thing. 

I looked into your project to see what's happening -- ICDevs right? I see that over 80% of your donors passed the Passport model as having sufficient ETH activity and qualified for matching. Instead, it may be the case that the community of individuals who supported your project are not as diverse in the projects they choose to support.  @Joel_m is adding his expertise here as an inventor of COCM and we can dig in some more!

---
On a related note,  I've updated the [results sheet](https://docs.google.com/spreadsheets/d/1rZ9JPldY1AjzMdGgfqpfRfxlUyQdGLoVAZJ90Eamxq4/edit#gid=1546480797) to include the number and percent of users passing passport for each project. I hope that addresses the request from @Kronosapiens as well. Let me know! 

---

One thing I'd like to emphasize is that these rounds are meant to serve our OSS community. It's ultimately up to the members of this community to decide how these rounds should be run. If something we're doing isn't working then we should change it. With that said, it's hard to get an accurate read on things sometimes. My personal bias says that the projects with high matching per voter are ones that should be getting boosted. It would be helpful to hear from more people.

Projects like Giveth and Rotki, for example, are not doing well because they are 'friends of the founders.'   Griff, Lefteris, their teams, and our co-founders have been active contributors to the Ethereum ecosystem for many years, consistently move the industry forward, and have earned meaningful support from people across the space. That support shows up in the donation record. If in doubt of any of this, I recommend instead of leaving a comment just check the [code](https://github.com/gitcoinco/qf-calculator) and [on-chain data](https://drive.google.com/drive/u/1/folders/1_FQdrNLiTPxJ7OHIJFULGDxOIuW3_vvt) for yourself. 

---
I know there are more comments to address and will be back soon! Thanks to all projects for your engagement and patience here

-------------------------

Joel_m | 2024-05-17 23:16:28 UTC | #17

[quote="CryptoRohittt, post:8, topic:18816"]
But now when we got the email from Gitcoin, we are shocked to see that we are ranked 2nd? I cannot understand why! :slightly_frowning_face:
[/quote]

Hey @CryptoRohittt  -- I can look into the data here this weekend, but as mentioned in the post, COCM tends to take more than raw donor numbers / donation amounts into account. I think that this almost certainly had something to do with it. In particular, in an effort to curb sybils, COCM gives a leg up to donors who donate do more than one project, and tends to give single-issue voters less sway. So a big push to rope in folks who weren't already GG donors may have had less impact if those people only donated to your project.

[quote="skilesare, post:6, topic:18816"]
If I take out these 46 or so contributions that were part of a carpet bomb my average goes from about 1.5 to 9.1 per donor.
[/quote]

Thanks for flagging this -- I'm not the best person to capture the whole picture of what happened here, since I only work on the QF side of things and not passport, but if it really is the case that *fewer* donations to your project would've yielded more matching, that's definitely something we want to look into. 

[quote="Moeen, post:15, topic:18816"]
Could you please help me understand the rationale behind the allocation of matching funds in this case? Insights into the process will be invaluable for our future participation and ensure we align better with the intended outcomes of the program.
[/quote]

Definitely, this is also something I can look into, but like above it may have something to do with donor diversity. 

In case it helps anyone out, I'm also going to share [a link to the COCM code written in a clearer way than what's in the public repository/ what we use in production.](https://colab.research.google.com/drive/1D_3h-Lvpvd5p2YUbyhV8pMRzCZmbFxbk?usp=sharing) This code is VERY slow and is only really there to look at, in case doing so makes it more clear what's going on in the algorithm. To run your own experiments, I suggest using the version of COCM in this [github repo](https://github.com/Jmiller4/qf-variants/blob/main/qf-variants.py) with the default arguments. 

I'm also going to share [the similarity scores as calculated by  COCM for all GG20 rounds](https://drive.google.com/drive/folders/1LpJjxLJCSwp5ACaKHN_BwftX0IqmTo88?usp=sharing). This is already a long post but there is information linked above that explains how we use these.

However you don't really need these if you want to replicate the round results, you can just plug in the data Umar shared above (after a little pre-processing). COCM doesn't take the similarity scores as input, it calculates them as a by-product, so this is just a way to examine the "guts" of the algorithm, should anyone want to.

We're also always trying to tune this algorithm to give better results. It's a careful three-way balancing act between 1) prioritizing popular projects, 2) not letting sybils have too much sway, and 3) reducing user friction (i.e. not requiring too much proof of humanity stuff). Thanks all

-------------------------

skilesare | 2024-05-18 00:24:27 UTC | #18

[quote="umarkhaneth, post:16, topic:18816"]
Hi skilesare, you can always find voting data available via SQL in our metabase instance at [regendata](https://github.com/ufkhan97/regendata) or our Indexer’s [GraphQL endpoint](https://github.com/gitcoinco/grants-stack-indexer?tab=readme-ov-file). For GG20 I also uploaded CSVs [here](https://drive.google.com/drive/u/1/folders/1_FQdrNLiTPxJ7OHIJFULGDxOIuW3_vvt).
[/quote]

Dumb question here, but in the csv, for raw score, is 100 good or bad?

What is the difference between amountUSD and startingAmountUSD?

I tried signing up for the SQL and the registration process was down.

-------------------------

skilesare | 2024-05-18 00:46:38 UTC | #19

[quote="Joel_m, post:17, topic:18816"]
Thanks for flagging this – I’m not the best person to capture the whole picture of what happened here, since I only work on the QF side of things and not passport, but if it really is the case that *fewer* donations to your project would’ve yielded more matching, that’s definitely something we want to look into.
[/quote]

I'm going to slice this a bit by the number of these that were 'carpet bomb' votes....but most of those got a 100 score:

![image|689x292](upload://4PzT8ccD3JfJ7v6VpNfqrq1hR6V.png)

Not sure if it is helpful or not.

-------------------------

Moeen | 2024-05-18 10:17:33 UTC | #20

[quote="Joel_m, post:17, topic:18816"]
Definitely, this is also something I can look into, but like above it may have something to do with donor diversity.

In case it helps anyone out, I’m also going to share [a link to the COCM code written in a clearer way than what’s in the public repository/ what we use in production.This code is VERY slow and is only really there to look at, in case doing so makes it more clear what’s going on in the algorithm. To run your own experiments, I suggest using the version of COCM in this [github repo] with the default arguments.

I’m also going to share [the similarity scores as calculated by COCM for all GG20 rounds. This is already a long post but there is information linked above that explains how we use these.

However you don’t really need these if you want to replicate the round results, you can just plug in the data Umar shared above (after a little pre-processing). COCM doesn’t take the similarity scores as input, it calculates them as a by-product, so this is just a way to examine the “guts” of the algorithm, should anyone want to.

We’re also always trying to tune this algorithm to give better results. It’s a careful three-way balancing act between 1) prioritizing popular projects, 2) not letting sybils have too much sway, and 3) reducing user friction (i.e. not requiring too much proof of humanity stuff). Thanks all
[/quote]

Thank you for the detailed follow-up and for providing additional resources to understand the COCM code and its application.

I’ve reviewed the available information, and while I understand the complexity of balancing donor diversity, project popularity, and sybil resistance, I’m still puzzled by some discrepancies in the matching funds. For instance, a project with approximately 90 contributions totaling $200 received a higher matching amount than our project, which had around 650 contributions totaling $1600.

-------------------------

rohit | 2024-05-19 20:34:28 UTC | #21

[quote="Moeen, post:20, topic:18816"]
For instance, a project with approximately 90 contributions totaling $200 received a higher matching amount than our project, which had around 650 contributions totaling $1600.
[/quote]

I was intrigued by this and thought of digging deeper into the data. I would like to think the following supports @Joel_m's assertion about donor diversity.  

I profiled BerryLab's top 50 donors compared to the other project (with fewer contributors/contributions, let's call it Project A). The top 50 donors of Project A collectively supported 152 out of the 153 projects in the dApps & Apps round, while the top 50 donors of BerryLab have contributed to 34 out of the 153 projects. In relative terms, the top contributors for Project A are likely to be part of more diverse clusters by a long shot. 

While this is not conclusive, it is a directionally indicative reason behind the difference. I have spot-checked this with 3 other projects with less than 100 unique voters contributing to less than $350 in crowdfunding but have received an average matching Per Voter > $15. In each case, their top 50 donors collectively support at least 120 or more projects in the round.

(Query to support this analysis is available in the Metabase instance of Regendata [here](https://app.regendata.xyz/question/249-total-projects-supported-by-top-donors-of-a-project-dapps-apps)).

-------------------------

gulliverz | 2024-05-20 15:36:10 UTC | #22

[quote="DistributedDoge, post:4, topic:18816"]
Having my account passively scanned by some third-party black-box model is much less hassle than manually collecting stamps, so overall, it is an improvement.
[/quote]

Nice way of thinking, I second to that :slightly_smiling_face:

-------------------------

skilesare | 2024-05-20 20:50:23 UTC | #23

[quote="skilesare, post:18, topic:18816"]
Dumb question here, but in the csv, for raw score, is 100 good or bad?
[/quote]

Just raising this again as it is blocking my analysis.😬

-------------------------

umarkhaneth | 2024-05-20 21:04:50 UTC | #24

Hey! 100 is good. We apply a sliding scale to donations based on the passport score. If your score is 0 you get no matching. If your score is 1 you get 50% matching, and this increases linearly until a score of 25 at which point you get 100% matching. The amountUSD is the value after this scale is applied while the startingAmountUSD is the original donation. 

I'm looking into the bug in the registration process. If you DM me a good email address I can add you manually for now. I'm @umarkhaneth on tg

-------------------------

Joel_m | 2024-05-20 21:28:53 UTC | #25

Ok, here are some graphs that may help @Moeen , @CryptoRohittt , and @ayush035 understand their funding outcomes. 

We've mentioned above and in other communications how COCM prioritizes projects with diverse sets of donors. The charts below give one way of visualizing that on GG20 data. 

Each dot on these scatterplots is one project. The X axis is the average diversity of that project's donors, and the Y axis shows the amount that project benefited from moving from standard QF to COCM. 

In more detail: to calculate the X axis number, we looked at all pairs of donors to a project. For each pair, we found the number of other projects that just *one* person out of the pair donated to, and averaged all those numbers. To calculate the Y axis number, we found the percent of the matching pool that project got under COCM, and divided that by the percent they would've captured under standard QF. Also, since the DApps round was so big, we used 10k randomly sampled pairs instead of all pairs, per project.

![Untitled|571x492](upload://d8JqsQcKKJ778N1fbQN3KT28uDB.png)

![Untitled-1|562x492](upload://px6VEkbq9chuEEH7i2Ne9OcY6Tj.png)

These scatterplots show a correlation between this particular measure of donor diversity and project success. They might also help to explain why BerryLab, WalletX, and Stogram performed less well than expected: in regards to this measure, they're on the lower end of the distribution, coming in at  9.57, 4.97, and 10.64 respectively. 

Hopefully these charts can be helpful to everyone trying to understand why funding results look the way they did, and can help all of us in the Gitcoin community understand how we want to align the algorithm in the future. I would love everyone's feedback on whether or not this is the type of behavior we want out of the algorithm, and why or why not that's the case.

-------------------------

Moeen | 2024-05-20 22:02:14 UTC | #26

Thank you for providing this data and taking the time to explain all the details. I think it might be beneficial to exclude the outliers for each project. This could help to eliminate any potential bias if a random wallet only donated to one project.

-------------------------

ayush035 | 2024-05-20 22:05:28 UTC | #27

Got it , I appreciate your efforts for helping us understand COMC  ,things makes much more sense now.

-------------------------

Joel_m | 2024-05-21 05:07:38 UTC | #28

Hi @skilesare -- could you send me the addresses of the 46 carpet bombers you mention? Email is the best way -- joel@gitcoin.co

-------------------------

solarpunkmaxi | 2024-05-22 15:53:19 UTC | #29

hey @umarkhaneth , since $EARTH was rejected initially and then we got through after making the necessary changes for the OSS round, there were 2 grants LIVE - the one that got rejected and the one with which we reapplied. 

Have been given to believe that votes given to only of the 2 live are getting counted. 

Any particular reason not to include votes to both ?

-------------------------

umarkhaneth | 2024-05-22 22:44:29 UTC | #30

Hey @solarpunkmaxi, our program automatically pulls data on accepted projects and calculates the matching results. Including the votes from a rejected project and/or combining votes on two projects means a manual intervention.

With that said, we've gone ahead and processed this for $EARTH in the Dapps round and for DSPYT (who reached out via telegram and also had a duplicate project situation) in the Hackathon round.

The updated results are live in the results sheet.

-------------------------

CODEX | 2024-05-22 23:37:36 UTC | #31

To confirm: there are still no donations in the wallets connected to the #GG20 grant until the QF has been calculated?

-------------------------

umarkhaneth | 2024-05-23 16:21:07 UTC | #32

The [vote to ratify the GG20 results](https://snapshot.org/#/gitcoindao.eth/proposal/0x3527cb7a0c0e2100fc508b3d3b95e255ab34b95a18fd5fe6ab41c928d8aa5901) is now live on snapshot and running until May 28th! Please go vote! 🗳

-------------------------

umarkhaneth | 2024-05-23 16:44:47 UTC | #33

[quote="CODEX, post:31, topic:18816, full:true"]
To confirm: there are still no donations in the wallets connected to the #GG20 grant until the QF has been calculated?
[/quote]
No all crowdfunded donations are already in grantee wallets. If you're having issues pls dm me on telegram @umarkhaneth

-------------------------

CryptoRohittt | 2024-05-24 04:19:09 UTC | #34

[quote="Joel_m, post:17, topic:18816"]
I think that this almost certainly had something to do with it.
[/quote]

Why speculate? just share the data with us!

-------------------------

umarkhaneth | 2024-05-24 17:50:52 UTC | #35

reposting these links from above

[quote="umarkhaneth, post:16, topic:18816"]
you can always find voting data available via SQL in our metabase instance at [regendata ](https://github.com/ufkhan97/regendata) or our Indexer’s [GraphQL endpoint ](https://github.com/gitcoinco/grants-stack-indexer?tab=readme-ov-file). For GG20 I also uploaded CSVs [here](https://drive.google.com/drive/u/1/folders/1_FQdrNLiTPxJ7OHIJFULGDxOIuW3_vvt).
[/quote]

-------------------------

skilesare | 2024-05-28 15:02:04 UTC | #36

Sent the list last week but just noticed my message didn't post. Did you receive it via email?

-------------------------

umarkhaneth | 2024-05-28 15:15:42 UTC | #37

This [snapshot has closed](https://snapshot.org/#/gitcoindao.eth/proposal/0x3527cb7a0c0e2100fc508b3d3b95e255ab34b95a18fd5fe6ab41c928d8aa5901) and option to “Ratify the round results” has won.

Metrics:
1,635 unique wallets voted
~4.9M GTC tokens cast.

Thank you to all who voted!

-------------------------

skilesare | 2024-06-03 12:38:02 UTC | #38

@Joel_m Did you ever have a chance to look at that list?  Still trying to figure out what went wrong and how I can do better next round.

-------------------------

Joel_m | 2024-06-13 18:31:18 UTC | #39

Hi @skilesare, sorry for the delay here. 

I re-ran the results with the "carpet bombers" you indicated removed from the donor pool. Removing them doesn't seem to significantly change outcomes -- in particular, your project does get more matching, but only an additional 0.00000027 of the funding pool. 

I also tried stress-testing the results by adding in up to five thousand more fake carpet bombers, to see if this can become a viable attack with many such accounts. With 5k carpet bombers added in, your project's share of the matching pool does decrease, but only by a fraction of 0.0000021 (compared to the world with all carpet bombers removed). 

That being said, these seem to be very different results than what you noted in your original post. If you're comfortable emailing me with further information about what numbers you crunched to get the results you did, please shoot me another email.

-------------------------

skilesare | 2024-07-09 18:13:32 UTC | #40

Joel...I think this is just a case of most of my contributions being at opposite ends of the spectrum. Most of my donors were coming from outside the ETH ecosystem. Hopefully they are more established now and will get better scores in the next go around. We'll just have to build it up over time. 

We do have a cool demo of bringing passport over to our community now, so hopefully I can get better engagement with it in the future: https://kristoferlund.se/blog/240703-verifiable-credentials

I'm also lobbying to get ckGTC enababled, but we likely need a good use case first. :slight_smile: https://github.com/dfinity/ic/blob/master/rs/ethereum/cketh/docs/ckerc20.adoc

-------------------------
