---
id: 17281
title: "GG19 Program Round Results"
slug: gg19-program-round-results
category: gitcoin-grants
url: https://gov.gitcoin.co/t/gg19-program-round-results/17281
created_at: 2023-12-15T22:46:01.143Z
last_posted_at: 2024-01-04T18:14:08.342Z
posts_count: 17
views: 6788
like_count: 108
---

# GG19 Program Round Results

<https://gov.gitcoin.co/t/gg19-program-round-results/17281>
umarkhaneth | 2023-12-15 23:08:58 UTC | #1

![image|690x153](upload://1zTwNaxfy4LPESs2UvZEUEujbjc.jpeg)

Hey all, GG19 program round matching results are live [here](https://docs.google.com/spreadsheets/d/1J-llvoR7dJ8tisZf5TFCUE_72_W9gjaHjcOmjBF2nbo/edit#gid=668799987)! We’ll have five days for review and feedback, then process payouts on 12/20. 

Thank you to @connor for co-authoring this post with me. Thank you ​​to @Joel_m, @ghostffcode, & @stefi_says for contributing to the post-round analysis results. Thank you to @M0nkeyFl0wer @Sov and others within the DAO for their thoughts and reviews.

# TL;DR

In GG19, we continue moving to a variant of QF that uses clustering to move sybil and collusion resistance natively inside the mechanism and reward projects with more diverse and pluralistic communities. GG19 will be the first round in years where we will not do any closed-source silencing of Sybils/donors. Instead, we’re solely relying on our mechanism and Gitcoin Passport.

For this round, we had a proactive [governance discussion](https://gov.gitcoin.co/t/gg19-matching-funds-proposal-for-discussion/16945) and a subsequent [snapshot vote](https://snapshot.org/#/gitcoindao.eth/proposal/0x28602986792817ae8bd51ac57775966a4d4bf101eb585011715a9cf64c94e9df) to approve the transfer of matching funds. Consequently, there will not be a formal vote to ratify these results; however, we will have five days for review and discussion on the forums.

# GG19 Overview

GG19 took [a few steps to evolve](https://gov.gitcoin.co/t/gg19-outline-and-strategy/16682) our program round strategy from prior rounds. This time we had 3 program rounds distribute $1,094,662 to 471 projects. Big thank you to the Dev Con team, Polygon, & Arbitrum for supporting Ethereum Infrastructure, Open Source Software, and Web3 Community Builders! 💚💜💙

We also had an amazing 9 community rounds and 9 independent rounds running at the same time! This broke a Gitcoin record for most concurrent rounds. Special gratitude goes to all our partners and especially to our community round runners at the Climate Coordination Network, Arbitrum Citizens, Metagov (Governance Research), Token Engineering Commons, OpenCivics, Mask Network (Web3 Social), Meta Pool, and 1inch.

|Round|Matching Pool|Matching Cap|Crowdfund|
| --- | --- | --- | --- |
|Open Source Software|$200,000.00|7.420%|$297,252|
|Ethereum Infrastructure|$200,000.00|10%|$58,723|
|Web3 Community & Education|$200,000.00|7.420%|$138,687|


Each Gitcoin round sees improvements over the last but this one feels like a turning point in many ways. Some of the new features and additions include:

* Passport Sliding Scale: Rather than having passport scores resolve to a binary “pass” or “fail” result to determine whether a donor gets matched, GG19 had a new feature where once scores were over a certain threshold(15), an increase in the score would result in an increased matching impact. 76.0% of wallets qualified for this round, an increase of 4% from last round.

* Matching Estimates: Donors could now see an estimate of their donation's impact on a project’s matching amount.

* Explorer Landing Page: [explorer.gitcoin.co](https://explorer.gitcoin.co/)'s beautiful redesign also improved search and sort functionality

* Collections: created a way for donors to delegate funding decisions
* Report Cards: provided round operators a new channel to communicate publicly about their round

* Passport UI Improvements: sleek new interface makes it easier to see how you can earn points to increase your unique humanity score.

* Passport Scoring Improvements: continuous adjustments to the stamp scoring models are adapting to sybil strategies, making it harder for them and easier for real humans

Read more here:
- https://gov.gitcoin.co/t/gg19-oss-round-review-reflections/17278/
- https://gov.gitcoin.co/t/gg19-web3-community-and-education-round-review-reflections/17279
- https://gov.gitcoin.co/t/gg19-eth-infra-round-review-reflections/17268

Kudos to everyone who worked hard to make this round a success! There are many people behind the scenes at Gitcoin whose work makes it possible to fund what matters. Thank you!!

# Round and Results Calculation Details

The complete list of final results & payout amounts can be found [here](https://docs.google.com/spreadsheets/d/1J-llvoR7dJ8tisZf5TFCUE_72_W9gjaHjcOmjBF2nbo/edit#gid=668799987). Below, we’ll cover how these results were calculated and other decisions.

Post-round mechanism selection had a $350k financial impact. This means $175k was reduced from projects that saw over-coordinated or sybil activity and given to other projects.


# Next Gen Quadratic Funding: Collusion-Resistance Inside The Mechanism

We introduced post-round sybil squelching a few years ago as part of our defense against the dark arts of sybil attackers and airdrop farmers. This process involves the Gitcoin team utilizing on and off-chain data, machine learning, and manual verification to find sybils and sockpuppet accounts to take them out of the matching distribution. Because our methods only worked so long as the attackers didn’t know how we found them, we had to be closed source. This round, with an improved mechanism, we found our closed-source solution only improved results by between 5 and 20%. That’s why we’re really glad to not use it at all. Instead, we’ll draw attention to the [open source code](https://github.com/Jmiller4/qf-variants/tree/main) we use to calculate quadratic funding results.

About a year ago, @joel_m, @GlenWeyl, and @erich published an innovative [paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4311507) in which they designed collusion-resistant methods for quadratic funding. Recently we began implementing their strategies and they’ve proven highly effective. We successfully reduced the match of the most suspicious projects by up to 85% and redirected those funds to other projects.

Quadratic funding helps us solve coordination failures by creating a way to allocate towards the projects a community believes should be funded. As a base case it assumes people are making independent decisions. However, this assumption can be exploited by colluding groups who align their funding choices to unfairly influence the distribution of matching funds.

Collusion-oriented cluster-matching (COCM) doesn’t make this assumption. Instead, it quantifies just how coordinated groups of donors are likely to be based on the social signals they have in common. Projects backed by more independent agents receive greater matching funds. Conversely, if a project’s support network shows higher levels of coordination, the matching funds are reduced, encouraging self-organized solutions within more coordinated groups.

One open area of research examines what data points make the best social signals. For this round we used the donation choices themselves as those signals. We also studied alternative options such as using passport stamp data and POAP data. If you’re interested in conversations on clustering data or mechanism developments, please join this [telegram group](https://t.me/+Of1AvIwXZAJjYmM5).

In addition, as an unintended side-effect of the COCM mechanism most projects get more funding. As an example, here is the chart of per-project funding for the Web3 Open Source Software round:

![|624x341](upload://iw2K8hkKp2C8U6dRg7llTqaHJ51.png)

We’re directing more of the funding to the long-tail of projects.

For more details about pluralistic QF methods, check out [this paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4311507) and/or [these](https://www.youtube.com/watch?v=Gi1madKCWWA) [podcasts](https://www.youtube.com/watch?v=ueQDnq-J2mY).

# Code of Conduct

As a reminder to all projects, [quid pro quo](https://support.gitcoin.co/gitcoin-knowledge-base/about-gitcoin/policy/understanding-potential-attack-vectors/bribery-quid-pro-quo) is explicitly against [our agreement](https://grants-portal.gitcoin.co/gitcoin-grants-grantee-portal/gg19-eligibility). Providing an incentive or reward for individuals to donate to specific projects can affect your ability to participate in future rounds. If you see someone engaging in this type of behavior, please [let us know. ](https://forms.gle/n3b5MDgHskehNQ7s8)

# Coordination Technology == Social Technology

For us to fund what matters, we need to use our collective voices. Let’s chat below on these results, the mechanism choice, and your experiences in the round. What did you see working well? What could be improved?


# Next Steps 
We plan to distribute matches before the holidays, by the end of next week. We are leaving 5 days of discussion on this post, and sans any major problems or issues found with these results, will process payouts shortly thereafter. But that doesn’t mean this conversation ends there! We want the conversation to continue to help us shape strategies and improvements for future rounds. Cheers!


![|624x351](upload://p4UkhFuRtCsOttdg2x1svICaPF5.jpeg)

-------------------------

connor | 2023-12-16 02:02:05 UTC | #2

Props to @umarkhaneth for putting in so much time and effort to get this across the finish line! Much of the work behind the scenes isn't obvious but there has been a lot of testing, experimentation, and fine-tuning with different QF mechanisms. I'm bullish on cluster mapping, moving towards more objective (and transparent) mechanisms and less subjective squelches/decisions. Awesome work!

-------------------------

ccerv1 | 2023-12-16 02:32:49 UTC | #3

Congrats! Well done @umarkhaneth and team. This felt like a classic Gitcoin Grants round.

I’d be curious to see any trends related to which projects seemed to attract a lot of clustering or other signs of Sybil attention. I’m also curious if you think the collections feature was helpful in giving any projects additional signal. 

👏👏👏

-------------------------

Sov | 2023-12-16 13:41:59 UTC | #4

Great work on this @umarkhaneth.  Looking forward to taking the lessons learned from here into GG20 and beyond.

-------------------------

Romko.eth | 2023-12-16 19:39:07 UTC | #5

Congrats! Great work @umarkhaneth and team. Happy Holidays to all team!

-------------------------

mars | 2023-12-16 23:07:54 UTC | #6

[quote="umarkhaneth, post:1, topic:17281"]
social signals they have in common
[/quote]

Does the algorithm allow to read stamps from Passport and then analyse social graph?

*(for example I connected Twitter / Facebook to get some points and then you read my data and the data of my frens)*

Or maybe "social signals" analysing on-chain history?

### Notable outlier:

`3.7x` more money
`8.5x` more people
Roughly the same matching

![image|690x444](upload://6BNAmGECJ2dFv4MRURprrzZjOyZ.png)

-------------------------

charlesfreeborn | 2023-12-18 19:14:31 UTC | #7

thumbs to the GitCoin team for an amazing work

-------------------------

KarlaGod | 2023-12-18 20:57:11 UTC | #8

This is great work, congratulations to all grantees, and thank you so much for the detailed report @umarkhaneth

-------------------------

smith | 2023-12-19 02:28:03 UTC | #9

> GG19 will be the first round in years where we will not do any closed-source silencing of Sybils/donors. Instead, we’re solely relying on our mechanism and Gitcoin Passport.

This is awesome news. Congratulations to the many folks who have worked so hard on improving this process. From a grantee perspective, this was the smoothest round so far. We love to see it!

-------------------------

gabriellamena | 2023-12-19 14:51:22 UTC | #10

GMGM guys, how are you doing? First of all, I would like to congratulate the Gitcoin team for the amazing work you have done! :people_hugging:

I was wondering if there is a possibility of bringing greater transparency to the data, especially in relation to the number of donors who had more than the necessary points on their passport and what was the % of the distribution in relation to the passport points. I believe this makes it easier to visualize the reason for the distributed values. If you could provide this information it would be amazing! :pray:

Also, I would like to know if anyone has any information about the 1inch round for Latam projects. I could not find the dates and how the distribution will be done. :frowning_face:

Thank you very much in advance for your attention guys! :heartpulse:

-------------------------

rohit | 2023-12-20 06:11:02 UTC | #11

[quote="umarkhaneth, post:1, topic:17281"]
For this round we used the donation choices themselves as those signals.
[/quote]

No other social signals were used in this round other than the contribution choices made by a donor.

-------------------------

adminrefimedellin | 2023-12-20 07:01:40 UTC | #12

Thanks to all the Gitcoin Team for the hard work done :raised_hands:, and thanks to  @umarkhaneth for this detailed post. :boom:

-------------------------

carlosjmelgar | 2023-12-20 19:02:36 UTC | #13

gm @gabriellamena , The LatAm round ran during the same dates as GG19. We're waiting for the contract to be funded and distribution will happen shortly after that. 

These are the voting results from the round. We'll update with matching amounts soon. 

![newplot (1)|690x336](upload://ujPw21sRvG1I9Gn59ICeaF0dHkt.png)

-------------------------

gabriellamena | 2023-12-20 19:28:48 UTC | #14

Thank you so much for the answer, Carlos! :grin:

-------------------------

umarkhaneth | 2023-12-20 20:42:11 UTC | #15

Thank you everyone for the warm wishes and congratulations! Finalizing the results was a big team effort and I'm grateful for  @Joel_m 's galaxy brain, @ghostffcode's stoic sureness,  @stefi_says data magic ,  @connor's process prudence and many more individuals within the DAO who gave review and feedback. 

On to some comments and questions.

[quote="ccerv1, post:3, topic:17281"]
I’d be curious to see any trends related to which projects seemed to attract a lot of clustering or other signs of Sybil attention.
[/quote]
Hey Carl, thank you for asking this! Overwhelmingly, I'm seeing these projects are the ones someone would donate to **in expectation of a future reward**. There are generally 3 kinds: 
- Projects which provide Airdrop Farming Guides or Investment Advice via content publication 
- Projects which guide the user to complete specific tasks/quests for rewards
- Projects which may do an Airdrop one day 

Although every round sees a difference in the matching distribution when switching to COCM, the biggest difference comes in the Community and Education Round which accounts for 55% of the  redistributed funds. OSS follows with 30% and Eth Infra 15%. We heavily curated the Eth Infra round as an invite-only round while the Community and Education round was more intended to allow quadratic funding to decide. 

By incentivizing an existing community of farmers and sybils to visit Gitcoin these rewards-based projects directly distort our matching outcomes. Cluster Matching reduced the match of these projects by up to 85% yet they are still able to draw thousands in funding. The place to solve for this is not in post-round analysis but in pre-round gating. 

For future rounds it's clear (imo) that we can draft explicit rules against allowing in projects whose primary output is advice/instruction on how to get airdrops or win rewards. While these have a place in Web3, it's probably not in our QF rounds.

[quote="ccerv1, post:3, topic:17281"]
I’m also curious if you think the collections feature was helpful in giving any projects additional signal.
[/quote]

The answer to this one isn't yet clear to me. I think there's some more analysis to be done to fully answer it. But, just to share some quick thinking: in this debut round it seems to have primarily helped add visibility to projects but did not yet drive bulk donations. I was a bit worried about the effect this cGrants fave would have on our clusterQF methods but the most popular collection (Stake From Home) saw 18 donors who donated to every project in the grant, while most were single digits. I think that's mainly because this feature launched this round and the bulk-add-grants-from-collection option may not have been available for the entire round. Def will keep an eye on and see if we can dig deeper into this in collaboration w the GS team.

[quote="mars, post:6, topic:17281"]
Does the algorithm allow to read stamps from Passport and then analyse social graph?

*(for example I connected Twitter / Facebook to get some points and then you read my data and the data of my frens)*

Or maybe “social signals” analysing on-chain history?
[/quote]
That’s an interesting idea! Like @rohit mentioned, we don’t do this and I'll add that we couldn’t even if we wanted to. Passport encrypts all your information. Gitcoin cannot look at your twitter or facebook friends/follower relationships.

[quote="gabriellamena, post:10, topic:17281"]
I was wondering if there is a possibility of bringing greater transparency to the data, especially in relation to the number of donors who had more than the necessary points on their passport and what was the % of the distribution in relation to the passport points. I believe this makes it easier to visualize the reason for the distributed values. If you could provide this information it would be amazing! :pray:
[/quote]
Hey Gabriella, thanks for asking this!
We had 76% of our 44.6k users reach a passport score of 15 or higher qualifying them for matching funds. See the distribution of scores below:
![Screen Shot 2023-12-20 at 3.21.36 PM|690x256](upload://tlHLmH5IWIEUnW8cNX58TGZlHWX.png)

-------------------------

gabriellamena | 2024-01-03 18:21:41 UTC | #16

Hey Carlos, how are you? Do u have any news about the 1inch Latam round? @carlosjmelgar

-------------------------

carlosjmelgar | 2024-01-04 18:14:08 UTC | #17

Hello. We're waiting on the matching Arbitrum funds. Sorry for the delay. We'll post an update when those have been received.

-------------------------
