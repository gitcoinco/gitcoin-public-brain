---
id: 19645
title: "GG22 OSS Program Matching Results"
slug: gg22-oss-program-matching-results
category: gitcoin-grants
url: https://gov.gitcoin.co/t/gg22-oss-program-matching-results/19645
created_at: 2024-11-12T15:17:36.063Z
last_posted_at: 2025-10-10T15:03:37.555Z
posts_count: 13
views: 4187
like_count: 33
---

# GG22 OSS Program Matching Results

<https://gov.gitcoin.co/t/gg22-oss-program-matching-results/19645>
MathildaDV | 2024-11-12 15:22:40 UTC | #1

Our GG22 OSS program round matching results are live [here](https://docs.google.com/spreadsheets/d/1WMFW6YrLIodpKoGcE79Vgf9vgBXXnC-JXw2w1Veds8s/edit?gid=1613004131#gid=1613004131)! We’ll have five days for review and feedback then, barring any major issues, will proceed with payouts by November 22.

Special thanks to @umarkhaneth for your partnership in crafting this post.

## TLDR

* GG22 saw a number of exciting new product features, such as Quick Bridge and [Mint Attestations](https://www.gitcoin.co/blog/mint-attestations-capturing-your-impact).
* We implemented the same two-pronged [sybil resistance strategy](https://gov.gitcoin.co/t/our-sybil-resistance-strategy-for-gg20/18524) as we’ve been using since GG20. We used a [pluralistic variant of QF](https://www.gitcoin.co/blog/leveling-the-field-how-connection-oriented-cluster-matching-strengthens-quadratic-funding) and we used Passport’s model based detection system. We did not do any closed-source silencing of sybils/donors. Instead, we’re solely relying on our mechanism and Gitcoin Passport.
* Discussion will be open for five days before payouts are concluded next week. A [GG22 pre-ratification](https://gov.gitcoin.co/t/proposal-gg22-pre-ratification/19501) was passed through governance, speeding up the process of payouts to grantees.

[Full Matching Results](https://docs.google.com/spreadsheets/d/1WMFW6YrLIodpKoGcE79Vgf9vgBXXnC-JXw2w1Veds8s/edit?gid=982062096#gid=982062096)

## Round Overview

Every round sees new developments. Some of the most exciting in GG22 included:

* Returning to our Open Source Software Program after GG21 was a fully [community-led round.](https://www.gitcoin.co/blog/gg21-results-retrospective)
* 7 Community Rounds. Read the [GG22 announcement post](https://gov.gitcoin.co/t/gg22-community-rounds-announced/19450) for those selected to run during this round.
* Providing the same sybil resistance tooling we use for our rounds to every community using Grants Stack by creating a [cluster-matching calculator ](http://github.com/gitcoinco/qf-calculator)and integrating with [Passport’s model based detection](https://support.passport.xyz/passport-knowledge-base/stamps/guide-to-model-based-detection).
* Expanding our product features to include Quick Bridge and Mint Attestations.
* Consolidating all of our program rounds onto Arbitrum.

## Key Metrics

### Overall

![|624x291](upload://5opg4n33SkzDHGnULNEYZ6iCoXN.png)

### OSS Program

4 Program Rounds
$1M Matching
$215k Total Crowdfunded
25,688 Unique Donors
283 Projects

## ![:bulb:|20x20](upload://bNudgaxRbqz4WF1KdbpGfTxjBaq.png ":bulb:") Project Spotlight

Here are the top five projects by total matching funding (gleaned from the [overall matching results](https://docs.google.com/spreadsheets/d/1WMFW6YrLIodpKoGcE79Vgf9vgBXXnC-JXw2w1Veds8s/edit?gid=982062096#gid=982062096)). The projects on this list are the ones with the most diverse bases of support, regardless of the size of the base.

### GG22 OSS Developer Tooling & Libraries

|Project Name|Matching Funds (USDC)|Matching Funds (USD)|
| --- | --- | --- |
|DefiLlama|$30,000|$29,862.54|
|Passport XYZ (formerly Gitcoin Passport)|$30,000|$29,862.54|
|Blockscout Open-Source Block Explorer|$27,280.78|$27,155.78|
|ethers.js|$18,686.91|$18,601.28|
|Viem|$17,077.67|$16,999.42|

### GG22 OSS dApps & Apps

|Project Name|Matching Funds (USDC)|Matching Funds (USD)|
| --- | --- | --- |
|Revoke.cash|$15,000|$14,931.27|
|Superchain Eco dApps|$15,000|$14,931.27|
|Hey.xyz (formerly Lenster)|$15,000|$14,931.27|
|The Tor Project|$15,000|$14,931.27|
|Giveth|$15,000|$14,931.27|

### GG22 Hackathon Alumni

Here’s an overview of additional projects that received matching funds in this round:

|Project Name|Matching Funds (USDC)|Matching Funds (USD)|
| --- | --- | --- |
|Geist dApp Kit|$10,000|$9,954.18|
|Warp Ads|$10,000|$9,954.18|
|UpStore🛡️|$10,000|$9,954.18|
|Realize It|$10,000|$9,954.18|
|Postino|$10,000|$9,954.18|

### GG22 OSS Web3 Infrastructure

Here’s an overview of more projects that received significant matching funds this round:

|Project Name|Matching Funds (USDC)|Matching Funds (USD)|
| --- | --- | --- |
|L2BEAT|$30,000|$29,862.54|
|eth.limo|$30,000|$29,862.54|
|Dappnode|$30,000|$29,862.54|
|Ethereum Attestation Service (EAS)|$30,000|$29,862.54|
|EthStaker|$25,711.66|$25,593.85|

## ![:abacus:|20x20](upload://mkuUumpgcCNkv6O1f7MLCaNML3J.png ":abacus:") Round and Results Calculation Details

Before GG20 began, we proposed a two-pronged [sybil resistance strategy](https://gov.gitcoin.co/t/our-sybil-resistance-strategy-for-gg20/18524). To recap it briefly, we would continue to use COCM (Connection-Oriented Cluster Matching) as we had in GG20 & GG22.

As explained in the post, and the [paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4311507) which introduced this mechanism to the world, COCM is much less vulnerable to Sybil Attacks than ordinary QF because it reduces the matching of donors who look similar.

In addition, over the past few rounds, Passport’s Model-Based Detection system has yielded greater sybil resistance than the stamp-based system without any of the user friction. When used together, we believe these two tools produce the most sybil-resistant results we’ve ever had.

There were some major updates made to Passport’s MBD system, which you can read more about [here](https://docs.passport.xyz/building-with-passport/model-based-detection/available-models).

### Connection-Oriented Cluster Matching (COCM)

COCM is an approach within Gitcoin Grants that enhances Quadratic Funding by prioritizing projects with diverse support bases, helping to counteract sybil attacks and coordinated groups trying to unfairly influence funding distribution. Key elements include:

* Diversity Bonus: COCM increases matching funds for projects supported by a wide array of "tribes" or distinct groups, rewarding cross-group support and broad appeal.
* Markov Chain Enhancement: Recent updates to COCM use a Markov chain approach to gauge connection strength between users and projects, providing stronger sybil resistance by analyzing indirect connections.
* Funding Distribution: COCM’s design inherently shifts some funds from top projects to those in the "long tail," enhancing the reach of smaller or niche projects.

### Gitcoin Passport’s Model-Based Detection System

The Gitcoin Passport team has implemented a model that evaluates on-chain activity to detect potential sybil accounts, enhancing funding fairness by:

* Address Probability Scoring: The model assigns each address a probability score, indicating whether it likely belongs to a genuine user or a sybil account.
* Continuous Improvement: While the model sometimes mistakenly flags new users with limited on-chain history, the team is refining the dataset and expanding to include Layer 2 networks, effectively reducing sybil influence on funding results.

These efforts together strengthen Gitcoin’s defenses against manipulation, helping to ensure fair distribution of funds to genuine community-supported projects.

## Code of Conduct Reminder

As a reminder to all projects, [quid pro quo ](https://support.gitcoin.co/gitcoin-knowledge-base/about-gitcoin/policy/understanding-potential-attack-vectors/bribery-quid-pro-quo)is explicitly against [our agreement](https://grants-portal.gitcoin.co/gitcoin-grants-grantee-portal/gg19-eligibility). Providing an incentive or reward for individuals to donate to specific projects can affect your ability to participate in future rounds. If you see someone engaging in this type of behavior, please [let us know.](https://forms.gle/gjnz7mtCcd6aRTFw6)

*We have removed Pheasant Network from matching distribution calculations, as this project clearly participated in Quid Pro Quo.*

## Next Steps

We plan to distribute the matching by November 22, after the [results](https://docs.google.com/spreadsheets/d/1WMFW6YrLIodpKoGcE79Vgf9vgBXXnC-JXw2w1Veds8s/edit?gid=1613004131#gid=1613004131) are open for discussion for five days.

It’s worth noting that GG22 [pre-approved the matching fund](https://gov.gitcoin.co/t/proposal-gg22-pre-ratification/19501) to be paid out before results were posted. This means that the payout process to grantees will occur faster, after this post has been left open for community input.

We are also hosting an internal retro in the following weeks and will publish further results and learnings. And as always, a detailed blog post will be published on the day that payouts are distributed.

We’re also always looking for direct feedback from the community on which improvements would make GG23 even better. Please don’t hesitate to let us know!

-------------------------

free2ride19 | 2024-11-12 15:36:20 UTC | #2

Hi MathildaDV,

Thanks for sharing the GG22 OSS Program Matching Results! I've reviewed the updates on Quick Bridge, Mint Attestations, and the sybil resistance strategy. Impressive work!

Appreciate the transparency on using a pluralistic variant of QF and Passport's model-based detection system. The open-source approach to sybil resistance is commendable.

Looking forward to the discussion over the next five days. The governance pre-ratification approval should indeed expedite the payout process.

Best regards,
@free2ride19

-------------------------

KMLLC | 2024-11-12 17:22:35 UTC | #3

Hi @MathildaDV,

Thanks for sharing the results. Hopefully these matched funds will aid in the effort of making these projects sustainable through time. Gitcoin product team definitely listens to community feedback and executes timely to address challenges, as is evident with every subsequent iteration to streamline the user experience.

One query I would have as a Gitcoin Steward, is there a simplified compare and contrast with these results & GG20 since both focused on OSS rounds?

If not no stress, just a nicety for an apples to apples comparison.

All my best,

Will T
Founder @KMLLC

-------------------------

MathildaDV | 2024-11-13 01:55:25 UTC | #4

Hey Will T! Thanks for your feedback. Regarding your question, you can view the results of GG20 [here](https://gov.gitcoin.co/t/passed-gg20-program-round-matching-results/18816). We generally don't do comparisons ourselves, but ff to have a look yourself! Curious though, would comparisons be helpful (and if so, why?)

-------------------------

ValentineCodes | 2024-11-13 04:42:02 UTC | #5

Hi! @MathildaDV 

Great results and fairly distributed!. Thanks for aiding the growth of Scaffold-ETH-Mobile!

🤝

-------------------------

chain_l | 2024-11-13 07:15:06 UTC | #6

Hi @MathildaDV 

Congratulations on one more successful round!

Can we learn about the calculation sheet that concluded the final matching funds? I see Hackathon Alumni Category has most % of approved projects being allotted 0 Matching funds. I would love dive deep and understand with the data, if it is accessible. 

Thanks.

-------------------------

KMLLC | 2024-11-13 14:45:56 UTC | #7

In a former life as a business strategist, I always found cycle over cycle comparisons useful. Typically when they can be visualized side by side and charted, it can lead to some learnings of opportunities. Might just be me, but I would find value in having this type of analytical view.

-------------------------

CeciSakura | 2024-11-13 15:32:50 UTC | #8

Hello @MathildaDV!
Thank you for such an amazing recap of the GG22 round and its results. The level of transparency you bring to all of Gitcoin’s work is simply outstanding!  :clap: :clap: :clap:

I think it would be incredibly insightful to see a comparative data analysis spanning rounds GG20 through GG22, especially focusing on donor behavior and trends in the OSS rounds. It would be fascinating to look at things like which types of projects attracted the most donations, how donation amounts have evolved across rounds, and any shifts in project categories that are gaining interest. Plus, examining whether donor participation has increased or decreased over time would give a clearer picture of community engagement.

This kind of analysis could give both the Gitcoin team and the community a richer understanding of the dynamics within OSS funding and how it’s growing or changing with each round. Just some ideas that could shed light on how we’re collectively making an impact over time!

Best regards,
@CeciSakura

-------------------------

MathildaDV | 2024-11-15 02:57:40 UTC | #9

Hi @chain_l! Thank you for your comment. There are a few reasons why matching is 0:

- minimum donation amount not reached
- donors only donated to their project
- not enough activity on their wallets

-------------------------

MathildaDV | 2024-11-21 18:02:08 UTC | #10

[UPDATE]: This post has been open for community feedback for 5+ days, and due to no conflicts with results, and the pre-ratification of the matching pool funds, we will proceed to payouts by end of this week. 

Thank you all for all your efforts making this round successful!

-------------------------

Maaz | 2024-11-23 03:14:30 UTC | #11

Do you mean the payouts will start from Monday? @MathildaDV

-------------------------

MathildaDV | 2024-11-25 12:42:26 UTC | #12

Yes! We are busy processing payouts rn but we are encountering a slight delay (comms were sent out end of last week). Apologies about that -- will process as soon as possible, latest tomorrow.

-------------------------

ajonathan007 | 2025-10-10 15:03:37 UTC | #13

best results until now i‘m proud of you

-------------------------
