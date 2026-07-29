---
id: 20334
title: "GG23 OSS Program Quadratic Funding Results"
slug: gg23-oss-program-quadratic-funding-results
category: gitcoin-grants
url: https://gov.gitcoin.co/t/gg23-oss-program-quadratic-funding-results/20334
created_at: 2025-04-25T14:45:11.239Z
last_posted_at: 2025-06-04T18:36:41.925Z
posts_count: 40
views: 6478
like_count: 86
---

# GG23 OSS Program Quadratic Funding Results

<https://gov.gitcoin.co/t/gg23-oss-program-quadratic-funding-results/20334>
MathildaDV | 2025-05-09 16:01:11 UTC | #1

# GG23 OSS Program Quadratic Funding Results

Our GG23 OSS Program Quadratic Funding results are [live](https://docs.google.com/spreadsheets/d/1v7eYS2MZtUZ4VeubQ4rN4ZNeWbFc2Os2xjNAmOOHcmg/edit?gid=0#gid=0)! We’ll have one week for review and feedback then, barring any major issues, will proceed with payouts by May 2, 2025.

*The **OSS Mature Builders Retro Funding** round results will be posted to the forum next week in a separate post.*

## TL;DR

* In GG23, we moved towards a deeper builder-centric approach in the way we fund public goods, focusing on supporting builders at every stage of growth through a new pluralistic, multi-mechanism design.
* We implemented the same two-pronged [sybil resistance strategy ](https://gov.gitcoin.co/t/our-sybil-resistance-strategy-for-gg20/18524)as we’ve been using since GG20. We used a [pluralistic variant of QF ](https://www.gitcoin.co/blog/leveling-the-field-how-connection-oriented-cluster-matching-strengthens-quadratic-funding)and we used Passport’s model based detection system. We did not do any closed-source silencing of sybils/donors. Instead, we’re solely relying on our mechanism and Gitcoin Passport.
* Discussion will be open for one week before payouts are concluded. A [GG23 pre-ratification proposal](https://gov.gitcoin.co/t/gg23-pre-ratification-proposal/20136) was passed through governance, speeding up the process of payouts to grantees.

[Full QF Matching Results](https://docs.google.com/spreadsheets/d/1v7eYS2MZtUZ4VeubQ4rN4ZNeWbFc2Os2xjNAmOOHcmg/edit?gid=0#gid=0)

## GG23 Overview

Every round sees new developments. Some of the most exciting in GG23 included:

* A multi-mechanism OSS Program, with early-stage projects participating in Quadratic Funding, and piloting Retro Funding for [GG’s Top 30 Mature Builders](https://www.gitcoin.co/blog/top-30-builders-in-gitcoins-retro-round-funding-proven-impact).
* 6+ Community Rounds. Read the [GG23 announcement post](https://www.gitcoin.co/blog/announcing-gitcoin-grants-round-23-gg23) for all the details.
* We introduced [Grant Ships](https://gg23.grantships.com/) as the new mechanism to host and support Community Round governance, including a new competitive model.
* Providing the same sybil resistance tooling we use for our rounds to every community using Grants Stack by creating a [cluster-matching calculator ](http://github.com/gitcoinco/qf-calculator)and integrating with [Passport’s model based detection](https://support.passport.xyz/passport-knowledge-base/stamps/guide-to-model-based-detection).
* Introduced a new [GTC Staking experiment.](https://gov.gitcoin.co/t/gtc-utility-experiment-for-gg23/20044)
* Consolidating all of our program rounds onto Arbitrum.

## OSS Program Quadratic Funding Rounds: Key Metrics

3 Program Rounds
$600k Matching
$95,278.16 Total Crowdfunded
9991 Unique Donors
235 Projects

## ![:bulb:|20x20](upload://bNudgaxRbqz4WF1KdbpGfTxjBaq.png ":bulb:") Round & Project Spotlight

Here are the top five projects by total matching funding (gleaned from the [overall matching results](https://docs.google.com/spreadsheets/d/1v7eYS2MZtUZ4VeubQ4rN4ZNeWbFc2Os2xjNAmOOHcmg/edit?gid=0#gid=0)). The projects on this list are the ones with the most diverse bases of support, regardless of the size of the base.

### GG23 OSS Developer Tooling & Libraries

View this round’s [report card here.](https://reportcards.gitcoin.co/42161/863)

![|502x400](upload://3PJiTSLCuhriWsw15IrAmbB8jae.png)

|Project Name|Matching Funds (USDC)|Matching Funds (USD)|
| --- | --- | --- |
|Human Passport (formerly Gitcoin Passport)|20000|$19,997.88|
|rekt.news - The dark web of DeFi journalism|20000|$19,997.88|
|growthepie 🥧📏|20000|$19,997.88|
|OpenZeppelin Contracts Library|20000|$19,997.88|
|Open Source Observer|20000|$19,997.88|

### GG23 OSS dApps & Apps

View this round’s [report card here.](https://reportcards.gitcoin.co/42161/867)

![|471x371](upload://inqTqZfbmSRruSMYPctfZFMMNSy.png)

|Project|Matching Funds (USDC)|Matching Funds (USD)|
|---|---|---|
|Karma GAP|10000|9999.76|
|GainForest|10000|9999.76|
|Treegens DAO🌳|10000|9999.76|
|Kolektivo Network|10000|9999.76|
|Greenpill Dev Guild|9144.7|9144.48|


### GG23 OSS Web3 Infrastructure

View this round’s [report card here. ](https://reportcards.gitcoin.co/42161/865)

![|499x396](upload://9T93tzVM7SQrIAcmblRXnFaStdi.png)

|Project|Matching Funds (USDC)|Matching Funds (USD)|
| --- | --- | --- |
|BrightID 🔆 Universal Proof of Uniqueness|20000|$19,997.88|
|Superchain Eco|20000|$19,997.88|
|ethOS|19148.79|$19,146.76|
|eth.limo|16004.09|$16,002.39|
|Deep Funding|12292.52|$12,291.22|

## ![:abacus:|20x20](upload://mkuUumpgcCNkv6O1f7MLCaNML3J.png ":abacus:") Round and Results Calculation Details

Before GG20 began, we proposed a two-pronged [sybil resistance strategy](https://gov.gitcoin.co/t/our-sybil-resistance-strategy-for-gg20/18524). To recap it briefly, we would continue to use COCM (Connection-Oriented Cluster Matching) as we had in GG20 & GG22.

As explained in the post, and the [paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4311507) which introduced this mechanism to the world, COCM is much less vulnerable to Sybil Attacks than ordinary QF because it reduces the matching of donors who look similar.

In addition, over the past few rounds, Passport’s Model-Based Detection system has yielded greater sybil resistance than the stamp-based system without any of the user friction. When used together, we believe these two tools produce the most sybil-resistant results we’ve ever had.

### Connection-Oriented Cluster Matching (COCM)

COCM is an approach within Gitcoin Grants that enhances Quadratic Funding by prioritizing projects with diverse support bases, helping to counteract sybil attacks and coordinated groups trying to unfairly influence funding distribution. Key elements include:

* Diversity Bonus: COCM increases matching funds for projects supported by a wide array of “tribes” or distinct groups, rewarding cross-group support and broad appeal.
* Markov Chain Enhancement: Recent updates to COCM use a Markov chain approach to gauge connection strength between users and projects, providing stronger sybil resistance by analyzing indirect connections.
* Funding Distribution: COCM’s design inherently shifts some funds from top projects to those in the “long tail,” enhancing the reach of smaller or niche projects.

### Gitcoin Passport’s Model-Based Detection System

The Gitcoin Passport team has implemented a model that evaluates on-chain activity to detect potential sybil accounts, enhancing funding fairness by:

* Address Probability Scoring: The model assigns each address a probability score, indicating whether it likely belongs to a genuine user or a sybil account.
* Continuous Improvement: While the model sometimes mistakenly flags new users with limited on-chain history, the team is refining the dataset and expanding to include Layer 2 networks, effectively reducing sybil influence on funding results.

These efforts together strengthen Gitcoin’s defenses against manipulation, helping to ensure fair distribution of funds to genuine community-supported projects.

## Code of Conduct Reminder

As a reminder to all projects, [quid pro quo ](https://support.gitcoin.co/gitcoin-knowledge-base/about-gitcoin/policy/understanding-potential-attack-vectors/bribery-quid-pro-quo)is explicitly against [our agreement](https://grants-portal.gitcoin.co/gitcoin-grants-grantee-portal/gg19-eligibility). Providing an incentive or reward for individuals to donate to specific projects can affect your ability to participate in future rounds. If you see someone engaging in this type of behavior, please [let us know.](https://forms.gle/gjnz7mtCcd6aRTFw6)

We have removed Pheasant Network & Vine Finance from matching due to the fact that both projects participated in quid pro quo during GG23.

## Next Steps

We plan to distribute the matching by May 2, 2025, after the [results](https://docs.google.com/spreadsheets/d/1v7eYS2MZtUZ4VeubQ4rN4ZNeWbFc2Os2xjNAmOOHcmg/edit?gid=0#gid=0) are open for discussion for one week.

It’s worth noting that GG23 [pre-approved the matching fund](https://gov.gitcoin.co/t/gg23-pre-ratification-proposal/20136) to be paid out before results were posted. This means that the payout process to grantees will occur faster, after this post has been left open for community input.

We are also hosting an internal retro in the following weeks and will publish further results and learnings. And as always, a detailed blog post will be published on the day that payouts are distributed.

If you know of any projects violating any of our agreements, please do let us know.

We’re also always looking for direct feedback from the community on which improvements would make GG24 even better. Please don’t hesitate to let us know!

-------------------------

Johnadek | 2025-04-25 15:25:50 UTC | #2

Awesome!
This is a very comprehensive report. Congratulations to all projects that came top in this round.
@MathildaDV when would results for Web3 for Universities round be out?

-------------------------

wasabi | 2025-04-25 15:54:15 UTC | #3

gm @Johnadek, you need to reach out to the Round Operators for the Web3 for Universities Round, as Community Rounds aren't managed by Gitcoin.

-------------------------

Johnadek | 2025-04-25 16:15:52 UTC | #4

Ah I see!
Thank you Wasabi. 🙏
@KarlaGod any update please?

-------------------------

CheatDetector | 2025-04-25 17:24:40 UTC | #5

Are projects who have intentionally colluded and participated in sybil attacks excluded? I picked a couple of receiving addresses from the QF calculator and ran them through Arkham. There is a clear intentional pattern of sending large amounts from the receiver address to other passported addresses through the across bridge 2 hops, who then go on to donate more than 99% of the funds forwarded back to the colluding receivers. There are even projects who both forward to the same users who go on to donate back to those projects and just dust a couple other projects.
Looking at the matched donors and amounts its impossible those donations have been ignored, given the full match amount is close to the total the project collected. Those projects are with very high gitcoin matching results and seem to have done a ton of recycling of funds through passported addresses?

-------------------------

wasabi | 2025-04-25 17:35:00 UTC | #6

gm @CheatDetector, please fill out this form with those findings https://forms.gle/gjnz7mtCcd6aRTFw6

-------------------------

KevinChibuoyim | 2025-04-25 19:55:57 UTC | #7

This is very detailed 

Great job here @MathildaDV

-------------------------

debuggingfuture | 2025-04-28 02:04:36 UTC | #8


Thanks for organizing and the detailed result report!

We are from [dDevKit](https://explorer.gitcoin.co/#/round/42161/863/47), this GG#23 dev tools round we ranked #5 by Most contributors (168) & #6 by Most donations at the end.

Seems we have mismatched expectations that per above results we end up ranking #22 with ~$1.8k matching funding. Understand the role of COCM, where we tried to attend shill space, mobilize our network and onboarded quite some donors new to gitcoin along the process.

A few things we wonder are
- did we miss out anything or any patterns we should avoid
- if dev activities/ contributing metrics of repo is part of the formula? before the round we changed our github repo name, not sure if there is implication. 
- thus we also created a new gitcoin project thus [past round](https://checker.gitcoin.co/public/project/show/geist) is not attached, will that affect the result?

Our project perhaps doesn't exists without gitcoin in the first place -- We’d appreciate it if someone could shed some light on this to help our understanding. We also wonder if gitcoin round is good for us to onboard users, not just rely on highly active wallets Web3 ecosystems in order to align with the formula.

-------------------------

thecryptonomad | 2025-04-26 12:57:20 UTC | #9

"We also wonder if gitcoin round is good for us to onboard users, not just rely on highly active wallets Web3 ecosystems in order to align with the formula."

I was about to ask the same. Thanks to raise it up. I look forward from any Gitcoin's team answer.

-------------------------

thecryptonomad | 2025-04-26 13:04:33 UTC | #10

Thank you for such an extensive report.

As PM at Animal Social Club this has been a first direct experience with Gitcoin QF. 

Traveling during the fundraising weeks impacted team's coordination and thus weakened our marketing approach, but still we're happy to have learned a lot and for any funds we'll receive.

Also, it's been amazing to see many friends met IRL at conferences running their QF campaigns and achieving some great results.

Happy for all. Congrats to Gitcoin. Appreciate for this growing opportunity 🙏

-------------------------

DeFiTeddy | 2025-04-27 02:51:33 UTC | #11

Thanks so much for the detailed report!

We're building Mini Bridge and ranked **#5** for both **Most Contributors** and **Most Donations** in the Infra round. But our matched result came out at **#11**, and we're trying to figure out why there’s such a big gap between the donation rank and matched rank.

Really appreciate your support for our project!

-------------------------

ShinHODLer | 2025-04-27 05:10:34 UTC | #12

**Hi Gitcoin Team,**

First of all, thank you for all the hard work in organizing GG23.
I have a quick question regarding the matching calculation under the COCM model.

I noticed a case where two projects have very different outcomes despite differing crowdfund amounts and number of contributors.
For example:

* ABI Ninja received **$79.68** in crowdfunds from **41 contributors**, and matched **$5,298**. 
* SuperUI received **$250.45** from **79 contributors**, but matched only **$356**. 

Could you help clarify how the diversity score or sybil resistance mechanism affected this result?
Is there anything we could do in the future to better optimize for matching outcomes, apart from increasing total crowdfunds or contributors?

Really appreciate your time and all the improvements made to the grants program. 🙏

-------------------------

Hydrapad | 2025-04-27 06:22:20 UTC | #13

I am sure they have logics and good reasoning. And I agree with you that Gitcoin has been supporting web3 community so long I can remember. Personally I don't really care about the amount/matching fund we have received. Community showed love and support. It's good enough knowing 1400+ people went to Gitcoin to show support for our project. :pray:

-------------------------

stellaachenbach | 2025-04-28 19:27:31 UTC | #14

Thank you for the detailed report @MathildaDV !
Can you help me understand where Unlock DAO is in all of this, or didn't we end up not making it at all? I knew only after that I should have applied for the Infrastructure round but well there is always something to learn ...

-------------------------

wasabi | 2025-04-29 13:03:09 UTC | #15

Check the tabs in the document.

-------------------------

MathildaDV | 2025-04-29 21:55:39 UTC | #16

Thanks for the comment @debuggingfuture. So, yes this is COCM in action. With traditional QF, your match would've looked different, but due to us using COCM (which is the most sybil-resistant), your match amount would look different. 

This is due to the fact that COCM favors projects that have a wider range of donors from various communities. So, if you have a donor base that only donates to your project and not other projects, this is where the difference comes in.

[quote="debuggingfuture, post:8, topic:20334"]
if dev activities/ contributing metrics of repo is part of the formula? before the round we changed our github repo name, not sure if there is implication.
[/quote]
No, COCM takes into account donor behaviour, and coupled with Passport's MBD (as outlined in this post), the onchain activity of the wallets donating!

Hope that clears things up for you!

-------------------------

MathildaDV | 2025-04-29 21:59:50 UTC | #17

Thanks @DeFiTeddy! Yes, the amount of donations is important in traditional QF, but in COCM having a wide range of donors is more important, so for this reason that's why you're seeing that gap. As outlined in this post, the two-pronged sybil resistance that we have ensures a fair distribution of funds. We always encourage projects to suggest to their donor base to not only donate to their project, but to others in the round as well! 

Hope that clears things up!

-------------------------

MathildaDV | 2025-04-29 22:00:49 UTC | #18

I see Unlock Protocol listed in dApps & Apps.

-------------------------

MathildaDV | 2025-04-29 23:09:12 UTC | #19

Thank you. This is being investigated, alongside all other reports that we have and that we may receive.

-------------------------

debuggingfuture | 2025-04-30 01:05:34 UTC | #20

Thank you for the response @MathildaDV it is helpful. 

We understand motivations of COCM and have the trust it is well designed & executed.
Thus I think we are aligned with COCM in principle, however we still find it challenging to understand how it actually play out given the algorithm complexity.

It will be great if some heruistic metrics/elaborations are published alongside the matching results  (besides on-chain [calculations as proposed](https://gov.gitcoin.co/t/gg23-pre-ratification-proposal/20136)), 
for examples we wonder, for each project

- how many donors are filtered in the first place (base on Passport MBD)? 
- % of donors donating to other projects?
- donor similarity for the project and how is that being calculated?
- visualized comparsion re diversity for projects?

In our case in last round with same COCM mechanism we were fortunately a top matched project (hackathon alumini). While this time similarily we raised donations from quite some different communities and with the large contributors count come organically, we are left feeling "yea we should be diverse with a valuable community" with COCM saying "no not actually diverse enough". 

Anyway just two cents from a project perspective, and we would love to communicate things clearly to our supporters as well. 
Still have to say, thank you Gitcoin!

-------------------------

MathildaDV | 2025-04-30 01:41:04 UTC | #21

I understand the need to understand these sybil-resistant mechanisms on a deeper level, but there's also a reason why we only release what we do -- so that the integrity of sybil resistance remains in tact, and that it protects future rounds from being gamed. 

Everything you need to know about COCM and how it works can be [found in this post!](https://www.gitcoin.co/blog/leveling-the-field-how-connection-oriented-cluster-matching-strengthens-quadratic-funding)

-------------------------

debuggingfuture | 2025-04-30 03:06:29 UTC | #22

Thanks -- Seems i misunderstood it is in the process of moving on chain.  Will appreciate any future discussions and materials on trade offs it made, such as on attributes related to [ethereum alginment](https://vitalik.eth.limo/general/2024/09/28/alignment.html) 

**Decentralization and security** - avoiding points of trust, minimizing censorship vulnerabilities, and minimizing centralized infrastructure dependency. The natural metrics are (i) **the walkaway test** : if your team and servers disappear tomorrow, will your application still be usable, and (ii) **the insider attack test** : if your team itself tries to attack the system, how much will break, and how much harm could you do

-------------------------

MathildaDV | 2025-05-02 15:49:05 UTC | #23

**UPDATE:** Due to our team actively investigation a few reports of violations, we will push finalization and payouts to next week when we have had the time to complete our due diligence.

-------------------------

Pjay | 2025-05-04 19:25:16 UTC | #25

hello @Johnadek i don't know if you've seen it yet, but the results for Web3 for universities are already out.

-------------------------

AndreyP55 | 2025-05-05 16:39:54 UTC | #26

Can you tell me when will be the results GG23 OSS - Web3 Infrastructure and awards for this stage? It's been quite a while, but the results have not been announced, and there are no awards.

-------------------------

owocki | 2025-05-05 17:22:59 UTC | #27


[quote="AndreyP55, post:26, topic:20334, full:true"]
Can you tell me when will be the results GG23 OSS - Web3 Infrastructure and awards for this stage? It’s been quite a while, but the results have not been announced, and there are no awards.
[/quote]

Please see the results in the post:


[quote="MathildaDV, post:1, topic:20334"]
[Full QF Matching Results](https://docs.google.com/spreadsheets/d/1v7eYS2MZtUZ4VeubQ4rN4ZNeWbFc2Os2xjNAmOOHcmg/edit?gid=0#gid=0)
[/quote]

-------------------------

AndreyP55 | 2025-05-05 18:46:35 UTC | #28

[quote="owocki, post:27, topic:20334"]
Please see the results in the post:
[/quote]

I have a question, I participated for the first time in tokenization of gitcoin token into projects in grants, will there be any rewards for the fact that I threw 50 gtc into each project that ended up in the top 3 projects?

-------------------------

owocki | 2025-05-05 18:50:36 UTC | #29

the rewards scheme was detailed on https://gov.gitcoin.co/t/gtc-utility-experiment-for-gg23/20044

@gnomadic might know when payouts are happening.

-------------------------

MathildaDV | 2025-05-06 22:15:58 UTC | #30

once the round is finalized, everyone will be able to unstake their GTC. please keep an eye out on communications from Gitcoin on this.

-------------------------

Johnadek | 2025-05-07 06:50:04 UTC | #31

Yeah buddy, seen.
Thank you :)

-------------------------

AndreyP55 | 2025-05-07 10:56:58 UTC | #32

That's the problem that the round is over long time ago, but my GTCs are not unlocked, and the branding of rewards on the page is also not there, all the waiting is going on

-------------------------

Hydrapad | 2025-05-07 11:27:44 UTC | #33

I think it would be great if users can unlock staked GTC and Gitcoin can take it's time to distribute matching funds later.

-------------------------

MathildaDV | 2025-05-08 23:09:36 UTC | #34

Please note that we have finalized our investigations, and matching distribution has been updated for dApps & Apps. All projects that participated in behaviour that violated our terms have been contacted directly.

Payouts will be processed by end of this week, latest early next week.

-------------------------

MathildaDV | 2025-05-09 22:45:41 UTC | #35

This round has been paid out and finalized.

-------------------------

Hydrapad | 2025-05-09 23:22:27 UTC | #36

Thanks for getting things done @MathildaDV :love_you_gesture:

-------------------------

Hydrapad | 2025-05-15 15:55:30 UTC | #37

@MathildaDV  we have received email from Gitcoin saying on 12th of May users can unstake GTC from Boosting projects. It seems still pending. Could you please explain why the delay, are the developers having difficulties or something ? Thanks.

-------------------------

wasabi | 2025-05-15 16:10:41 UTC | #38

From Gitcoin Grants Program Telegram 
> 
> Good news! 🤝 If you staked on a project during GG23, you are eligible for rewards! We are distributing your rewards directly to your wallet by Monday, May 19th. 🎉
> 
> 🌱Unstaking opens on Friday, May 16th.

-------------------------

AndreyP55 | 2025-06-04 17:52:08 UTC | #39

where and how can I withdraw my tokens? they are shown in the debank you can brand but where I can not find, please tell me

-------------------------

Tavernier | 2025-06-04 18:45:06 UTC | #40

Hey @AndreyP55 This forum is for governance discussions only. You should direct your question to the team: [Gitcoin Support]( [support@gitcoin.co](support@gitcoin.co))

-------------------------

MathildaDV | 2025-06-04 18:36:41 UTC | #41

Not sure what you're referring to, please reach out to support@gitcoin.co!

-------------------------
