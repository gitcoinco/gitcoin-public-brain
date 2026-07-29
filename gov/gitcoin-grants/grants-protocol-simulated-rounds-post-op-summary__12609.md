---
id: 12609
title: "Grants Protocol Simulated Rounds Post-Op Summary"
slug: grants-protocol-simulated-rounds-post-op-summary
category: gitcoin-grants
url: https://gov.gitcoin.co/t/grants-protocol-simulated-rounds-post-op-summary/12609
created_at: 2023-01-20T06:28:26.217Z
last_posted_at: 2023-02-08T01:39:55.057Z
posts_count: 7
views: 2670
like_count: 19
---

# Grants Protocol Simulated Rounds Post-Op Summary

<https://gov.gitcoin.co/t/grants-protocol-simulated-rounds-post-op-summary/12609>
koday | 2023-01-20 06:34:52 UTC | #1

**TL;DR**

Two simulated grants rounds were conducted on the protocol in December - one on Ethereum mainnet and one on Optimism. There were 17 grants split between the rounds selected based on prior engagement with the Grant Ops team and the mainnet results can be seen [here](https://dune.com/umarkhaneth/gitcoin-simulated-mainnet-round)*. Grantees provided candid feedback during onboarding through the end of the round. They were also surveyed after the round end date and provided both Grant Ops and GPC with valuable feedback that is currently being used to improve the Grants Protocol.

*Optimism results are still pending.


**Background + Objectives**

Prior to the [Grants Protocol Alpha Round](https://gov.gitcoin.co/t/discussion-feedback-request-grants-protocol-alpha-round-eligibility/11873), Grant Ops conducted two simulated (test) rounds. The primary objective of these rounds was for the Gitcoin team to learn how the Grants Protocol works and togather valuable data and feedback on the Grants Protocol from a small subset of highly engaged grantees and donors. This data would then be used to identify pain points, adjust Alpha Round preparations, improve the protocol where needed, and overall help the team prepare for the beta launch in March.


**Structure & Details**

The simulated rounds were structured as two separate rounds featuring Gitcoin grantees who participated in GR15.

The first simulated round was deployed on the Ethereum Mainnet and had 9 grants in the round. This round ran for 4 days from December 13-16.

![|624x344](upload://1aVKBrvio6ILw5tU5zTscKNYLur.jpeg)

The 2nd round was deployed on Optimism and had 8 grants in the round. This round ran for 5 days from December 15-19.

![|624x332](upload://nGg1kREw1JxGd6Vio5dhrzYP2Vn.jpeg)

The reason for deploying two separate rounds was to test the protocol using both Ethereum mainnet and Optimism to see what the differences were in gas costs, transaction times, general UI/UX for round managers, grantees and donors, bugs, etc. The plan was initially to run these rounds simultaneously to “practice” running multiple rounds at the same time, however an error on my end when creating the first Optimism round delayed the deployment for a few days and the rounds ran one after the other.

The grantees were primarily selected based on previous engagement with Gitcoin DAO contributors. For example, over half of the grantees were invited because they completed a voluntary interview with @madison after GR15 and gave valuable feedback regarding their experience and suggested improvements. We wanted to make sure the grantees helping us to test the protocol were not only interested in Gitcoin’s mission but also highly engaged and trustworthy.


**Ethereum Mainnet vs. Optimism**

Gas Costs:

* Creating a program in round manager: ~$18 on ETH, ~$0.21 on OP

* Creating a round: 3 smart contracts, ~$30 on ETH, ~$4 on OP

* Accepting grant applications: ~$2-3 on ETH, ~$0.10 on OP

As expected, the gas costs when using Optimism were significantly cheaper than Ethereum mainnet. Across the board, the exact same transactions using Optimism were ~90% cheaper than mainnet. This will likely lead to some strong upfront incentives for future Round Managers to run their rounds on Optimism instead of Mainnet.

On the flip side the layer 2 solution was more of a challenge for grantees and donors to navigate - it was not clear that they had to create their grant on Optimism in Grants Hub before applying to the Optimism-specific round. Only a few grantees had this issue, but with such a small sample size this could very easily scale up into a headache for round managers and grantees in a bigger round. I imagine this would be even more difficult when running a round with fewer crypto-native grantees who don’t already have an optimism wallet set up. It’s already a tall order to explain how to set up a wallet, fund it with DAI and ETH, and apply to a round on mainnet, but explaining a layer 2 solution like Optimism and how to convert assets into OP-ETH and OP-DAI adds a whole additional layer of complexity to the process.

Lastly, based on the donor data from these simulated rounds and the findings from the UNICEF Round, it appears that the majority of donors will still donate on Ethereum mainnet - likely because they don’t have a funded Optimism wallet handy or simply due to the familiarity of Ethereum regardless of the higher gas fees.


**Data Collection**

A strong emphasis was placed on gathering as much useful data as possible from these simulated rounds. The data came from:

* 1-on-1 walkthrough onboarding calls
* Grantee Telegram group
* Post-round grantee survey
* On-chain transactions


**Mainnet Round Dune Dashboard:**

A big shoutout goes to @umarkhaneth for his work in creating a [Dune dashboard](https://dune.com/umarkhaneth/gitcoin-simulated-mainnet-round) to show the stats from the mainnet simulated round. The results can be seen below:

![|624x393](upload://46DXhs3CRnCzWE1NUZKuYVU1rLj.jpeg)

In summary, 19 unique donors made 108 donations for a total USD value of $459.13 spread across 9 projects. This was also a great exercise in using Dune to dive into the on-chain analytics of a grant round on the protocol and will be invaluable for all rounds moving forward.

***Note: We are currently working through an issue in calculating the Optimism donation and matching fund totals, so those results have been omitted for the time being.


**Live Feedback/Product Improvements**

Overall, the rounds went pretty well considering it was a pre-alpha test of the protocol! There were some bugs and UI/UX issues but finding them was one of the goals of these test rounds. GPC has been great with addressing bugs as they come up and were able to fix a few things on the fly - huge shoutout to all of the GPC contributors for taking feedback in stride and working hard to make sure the protocol development continues and gets better and better with each iteration. If you have feedback for protocol improvements, please share it here: [https://forms.gle/um3JbjCuReTectcj7
](https://forms.gle/um3JbjCuReTectcj7)

Lastly, the Gitcoin Program Alpha Round is now live and running until January 31. please donate here: gitcoin.info/alpha


**Survey Results**

In full transparency, we wanted to share anonymous feedback from the grantees who responded to our survey after being onboarding to the round - the detailed responses can be found [here](https://docs.google.com/document/d/1ceatboeHfBVyNSbSt8RXOB4IR06OozfilSawqXrPEIE/edit?usp=sharing) and a TL;DR of the questions and results are summarized below:

Grantees were asked the following quantitative questions where 1 = Very easy and 5 = Very difficult. Each question was followed with a short answer prompt where we asked the grantees to elaborate on their experience. The last two questions were focused on overall impression of the round and any features they wanted to see added before the protocol beta launch.

![Forms response chart. Question title: On a scale of 1-5 how easy or difficult was it to set up your grant on the protocol? . Number of responses: 15 responses.|624x297](upload://tNWzmiiU3TdWz343kYGkSepymHw.png "On a scale of 1-5 how easy or difficult was it to set up your grant on the protocol? ")

*Please elaborate on your experience of setting up a grant:*

TL;DR - Most answers said creating a grant in Grants Hub was fairly easy and intuitive. There were some difficulties with Optimism with grantees requesting more info on how to use Optimism and bridge assets. Two other common themes throughout the responses were the troubles with verifying Twitter/Github (which GPC has already fixed!) and the lack of formatting/rich text ability in the grant description.

![Forms response chart. Question title: On a scale of 1-5 how easy or difficult was it to join the round and navigate the protocol?. Number of responses: 15 responses.|624x297](upload://1esaRab3VWOzOXGpgkzITtpIpJw.png "On a scale of 1-5 how easy or difficult was it to join the round and navigate the protocol?")

*Please elaborate on your experience of joining the round and navigating the protocol as a grantee:*

**TL;DR** - Grantees found it easy to join the round and navigate the protocol, although some mentioned that the UI did not have much detail and was slower than cGrants.

![Forms response chart. Question title: On a scale of 1-5 how easy was it to check out other grants and donate on the protocol?. Number of responses: 15 responses.|624x297](upload://f3nnkGM0J5TQps3TplB3QqMfghd.png "On a scale of 1-5 how easy was it to check out other grants and donate on the protocol?")

*Please elaborate on your experience of checking out grants and donating:*

**TL;DR** - This step did not go as well as the previous two for grantees. Some had issues with the checkout flow, others had txn errors they had to work through, and a few struggled to donate on Optimism for various reasons.

*How satisfied are you with your overall experience in the simulated round? What went well and what didn't?*

**TL;DR** - Most grantees said they had a positive experience helping us test the protocol with these simulated rounds. Many stated they want to see improvements in UI/UX, especially with adding rich text and images to grant descriptions and seeing live donation stats.

*What features you would like to see the product team focus on before the protocol beta launch in the Spring?*

**TL;DR** - Similar to the above question, the common requests were improvements to formatting for grant descriptions and adding functionality to see donation and matching stats live as the round is being run. Other interesting feature requests included language translation, support for more blockchains, grant sorting functionality, and load time improvements.

Thanks for reading and be sure to donate to grants in the [Alpha Rounds](http://gitcoin.info/alpha)!

-------------------------

J9leger | 2023-01-20 23:09:40 UTC | #2

Thanks for sharing about the Simulated rounds @koday. Well documented. This was a great low risk way for us to learn  about how the grants stack works and reduce any anxiety about the lift to run a round. I think there are two opportunities here for others to learn from starting in March: 
1) It would be awesome for partners interested in running their own rounds but unsure how to do so, to start by using this "simulated round" approach to learn by experience before deploying a large round 
2) For devs who want to build on allo/grants protocol but don't know how to or where to start, run a full round as small as $100 with 2-3 grantees to understand what we already have, what is missing and what to build. This is something Supermodular could even suggest for devs in their ecosystem.

-------------------------

Ministry888 | 2023-01-24 10:07:11 UTC | #3

[quote="koday, post:1, topic:12609"]
Two simulated grants rounds were conducted on the protocol in December - one on Ethereum mainnet and one on Optimism. There were 17 grants split between the rounds selected based on prior engagement with the Grant Ops team and the mainnet results can be seen [here ](https://dune.com/umarkhaneth/gitcoin-simulated-mainnet-round)*. Grantees provided candid feedback during onboarding through the end of the round. They were also surveyed after the round end date and provided both Grant Ops and GPC with valuable feedback that is currently being used to improve the Grants Protocol.

*Optimism results are still pending.

**Background + Objectives**

Prior to the [Grants Protocol Alpha Round](https://gov.gitcoin.co/t/discussion-feedback-request-grants-protocol-alpha-round-eligibility/11873), Grant Ops conducted two simulated (test) rounds. The primary objective of these rounds was for the Gitcoin team to learn how the Grants Protocol works and togather valuable data and feedback on the Grants Protocol from a small subset of highly engaged grantees and donors. This data would then be used to identify pain points, adjust Alpha Round preparations, improve the protocol where needed, and overall help the team prepare for the beta launch in March.
[/quote]
Thank you for the detailed article

-------------------------

PaigeDAO | 2023-01-24 10:59:02 UTC | #4

great suggestions. thank you @J9leger

-------------------------

PaigeDAO | 2023-01-24 11:01:09 UTC | #5

@koday appreciate the detail in this article. after I was invited to set up my sim grant, I was sort of left wondering how it all went? good to see that donations did come through... Am enjoying the Alpha Round now (Climate)

-------------------------

ceresstation | 2023-01-24 16:25:59 UTC | #6

This is fantastic work @koday, I don't have much to add but I appreciate that we're sharing these results and learning from them in public. The more experiments we run the better the protocol will be.

-------------------------

koday | 2023-02-08 01:39:55 UTC | #7

Thanks to @umarkhaneth we also have a Dune dashboard for the simulated round that ran on Optimism! https://dune.com/umarkhaneth/gitcoin-simulated-optimism-round

Even though the donor numbers were low while testing it's nice to have all the data in one place and prepare for reporting on larger rounds.

-------------------------
