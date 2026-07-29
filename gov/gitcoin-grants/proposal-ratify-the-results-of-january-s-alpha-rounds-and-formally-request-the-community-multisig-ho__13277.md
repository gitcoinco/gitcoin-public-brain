---
id: 13277
title: "[Proposal] Ratify the Results of January’s Alpha Rounds and Formally Request the Community Multisig Holders to Payout Matching Allocations"
slug: proposal-ratify-the-results-of-january-s-alpha-rounds-and-formally-request-the-community-multisig-holders-to-payout-matching-allocations
category: gitcoin-grants
url: https://gov.gitcoin.co/t/proposal-ratify-the-results-of-january-s-alpha-rounds-and-formally-request-the-community-multisig-holders-to-payout-matching-allocations/13277
created_at: 2023-03-15T21:41:41.823Z
last_posted_at: 2023-08-13T00:33:50.695Z
posts_count: 20
views: 6018
like_count: 64
---

# [Proposal] Ratify the Results of January’s Alpha Rounds and Formally Request the Community Multisig Holders to Payout Matching Allocations

<https://gov.gitcoin.co/t/proposal-ratify-the-results-of-january-s-alpha-rounds-and-formally-request-the-community-multisig-holders-to-payout-matching-allocations/13277>
connor | 2023-03-31 09:07:15 UTC | #1

Edit: Snapshot vote is now [ratified](https://snapshot.org/#/gitcoindao.eth/proposal/0x921899e842c8a3f43026e0817b3a06b8117d1a23166ef192db275fb11af9ac7b)!

TLDR: Alpha Round final results are live [here](https://docs.google.com/spreadsheets/d/1Oq5Fp3y9z5Ffv4ipx1zAiw3YL6FBPMh2PtyyG6apmfQ/edit?usp=sharing)! We propose 5 days for discussion and review followed by a 5-day snapshot vote to ratify, before processing final payouts.

**Background**

First, we’d like to thank the community and the grantees for all of the patience everyone has shown as we fine-tune our “canon” QF implementation for the Allo protocol, passport scoring, and end-of-round analysis. We understand the results (and subsequent payouts) for this round have taken longer than usual and we look forward to accelerating this process in future rounds. Additionally, thanks to @AlexK @nategosselin @umarkhaneth @koday @kyle @M0nkeyFl0wer @zen @baoki and many other amazing contributors in the Gitcoin DAO for all the work that went into making this round successful and getting us to these final results.

The first Gitcoin Program Alpha QF rounds on Allo Protocol ran from January 17th to January 31st and included a subset of established grantees from past rounds. $1 million in matching was available between 3 distinct rounds (and correspondingly 3 smart contracts), with 333,333 DAI pools for the following categories:

1. Web3 Open Source Software [[Explorer](https://grant-explorer.gitcoin.co/#/round/1/0xd95a1969c41112cee9a2c931e849bcef36a16f4c) | [Contract](https://etherscan.io/address/0xd95a1969c41112cee9a2c931e849bcef36a16f4c)]
2. Ethereum Infrastructure [[Explorer](https://grant-explorer.gitcoin.co/#/round/1/0xe575282b376e3c9886779a841a2510f1dd8c2ce4) | [Contract](https://etherscan.io/address/0xe575282b376e3c9886779a841a2510f1dd8c2ce4)]
3. Climate Solutions [[Explorer](https://grant-explorer.gitcoin.co/#/round/1/0x1b165fe4da6bc58ab8370ddc763d367d29f50ef0) | [Contract](https://etherscan.io/address/0x1b165fe4da6bc58ab8370ddc763d367d29f50ef0)]

You can learn more about how these rounds were planned and structured here:
https://gov.gitcoin.co/t/discussion-feedback-request-grants-protocol-alpha-round-eligibility/11873

https://gov.gitcoin.co/t/gitcoin-program-alpha-round-grantee-invite-lists-eligibility-criteria/12538

https://go.gitcoin.co/blog/announcing-the-gitcoin-alpha-round

**Results & Ratification**

The full list of **final results & payout amounts can be found [here](https://docs.google.com/spreadsheets/d/1Oq5Fp3y9z5Ffv4ipx1zAiw3YL6FBPMh2PtyyG6apmfQ/edit?usp=sharing).** Below we’ll cover how these results were calculated and what decisions were made (given this is the first round integrating Gitcoin Passport and the first large-scale round on Allo, it was a new process and one we’d like to get community feedback and iterate on).

We ask our Community Stewards to ratify the Alpha Round payout amounts as being correct, fair, and abiding by community norms, including the implementation of Passport scoring as well as judgments and sanctions made by the Fraud Detection & Defense workstream.

**If stewards and the community approve after this discussion, we would like to suggest voting on Snapshot to run from Monday, March 20th to Friday, March 25th, in advance of payouts being processed the last week of March.**

**Options to vote on:**

*1. Ratify the round results*

You ratify the results as reported by the Public Goods Funding & Fraud Detection & Defense workstreams and request the keyholders of the community multisig to payout funds according to the Alpha Round final payout amounts.

*2. Request further deliberation*

You do not ratify the results and request keyholders of the community multi-sig wallet to delay payment until further notice.

**Round and Results Calculation Details**

To summarize:

* The Gitcoin Program Alpha Round was conducted on the new protocol from January 17-31, 2023
* It consisted of 3 curated rounds with their own matching pool: Web3 Open Source Software, Ethereum Infrastructure, and Climate Solutions
* There were 159 returning grants split between the rounds invited based on funding criteria from GR14 and GR15
* A total of $667k was donated from 30,893 unique wallets

![|624x352](upload://t8KAi8XW28DuveXYk1f8sL0zkug.jpeg)

**Matching Calculation Approach**

The final results shared here stray from the “pure QF” calculations after treatment for supporter eligibility. Our eligibility controls were:

* Sufficient passport score
* Non-arbitrary donation minimum
* Removal of sybil-attackers
* Support amounts totaling to matching cap limit in place per round

**Passport scores**: Gitcoin Passport ran into some issues that we’re glad to have ironed out - some donors were unable to verify their unique identity for most of the round due to infrastructure instability, and some passport stamps were reset at times. As a result, donors were given 2 extra weeks after the round concluded to reverify their passports and stamps. Given the 2-week grace period, we are happy with the final outcome of verified passports:

![|624x123](upload://vSG07pMaK0lKSekCV3shtEetwMg.png)

Only ~10% of attempted passports failed, and ~10% of donors did not have any passport at all. Only donors with a passport and sufficient score were counted for matching calculations.

You can find more about Passport’s round issues, lessons learned, and future mitigation plans in Erich’s [post](https://gov.gitcoin.co/t/lessons-learned-a-look-at-gitcoin-allo-alpha-rounds-and-the-path-forward-with-gitcoin-passport/13011).

**Donation minimum**: In past cGrants rounds the donation minimum was $1. For the Alpha Rounds, we instead went with a cutoff of a certain bottom percentile of donations, which all ended up at about $.50, but varied between 30% and 60% of total donations depending on the round:

![|624x347](upload://oSUiZyiRDdnsWPF7uWLr281cWYH.jpeg)

These lower boundary limits were selected based on examining statistical anomalies across projects in aggregate for each round, along with time-series analysis to identify botted behavior. Whether a cohort of airdrop farmers was found to act as a group of isolated, unique individuals, or as a sybil-network, this limit neutralized the impact of such speculation on the disbursement of matching funds and we found that Passport did a good job of limiting the prevalence of unsophisticated sybil network in our alpha rounds.

**Advanced sybil attackers**: As with most QF Rounds, we saw some more sophisticated Sybil Attack patterns which were not stopped by Passport (yet!), as well as donations from addresses which were known to be attackers of prior rounds. After on-chain data analysis and a manual sampling process, donations from addresses that were associated with these types of behaviors were excluded for the purposes of matching calculations. Moving forward, more of this analysis process will be automated and executed in near real-time with the help of on-chain data called within Passport.

**Matching caps**: Matching caps were introduced many rounds ago on cGrants, where there is a maximum percent of the total matching pool any one grant can capture. Once they hit this cap, they will not earn more, and any excess is redistributed to all other grants. Alpha Round caps were:

* 5% for OSS
* 10% for Climate
* 10% for Eth Infra

These amounts were selected based on the number of grants invited/expected to be in each round.

*Please note:* in an effort to create a transparent minimum viable product of QF formula, *simple* quadratic voting has been deployed here. In the future, we will offer pairwise matching as an option for possible customizations that will be set and published on-chain at the time of grant program creation.

**Prior Estimated Results & Takeaways**

Multiple DAO contributors have already shared detailed analyses, statistics, and takeaways from the Alpha Rounds. You can find those governance posts here:

https://gov.gitcoin.co/t/gitcoin-program-alpha-rounds-data-findings/13045

https://gov.gitcoin.co/t/gitcoin-program-alpha-round-post-op-writeup/13043

https://gov.gitcoin.co/t/lessons-learned-a-look-at-gitcoin-allo-alpha-rounds-and-the-path-forward-with-gitcoin-passport/13011

Again, we thank everyone for your patience and participation in the Alpha Rounds. We’re excited for the Beta Program launch the last week of April (details coming soon) as we reignite the Gitcoin Program on the Allo protocol and support many other organizations to host their own programs and rounds.

For questions, comments, or concerns on any of the above, please comment below or join the [Gitcoin Discord](https://discord.gg/cD6RKWjZ6g).

-------------------------

lefterisjp | 2023-03-15 23:05:39 UTC | #2

Hey @connor! Thank you for posting the results.

I don't see anything against the pre-stated rules so I would vote for this.

But I do have some very serious comments to take into account for future iterations.
1. We need smaller caps, as we had introduced into the old grants. We see the currently most popular pojects hoarding biggest % of the votes. Exactly the reason the caps were introduced before. Imo the point of these rounds is to make as much impact as help as much as possible across a wide array of projects. Not the most popular one.

2. We should limit projects per entity, especially if they are applying across multiple categories. I like the lammas and use their stuff, but I don't find it okay to see them apply in both OSS and infra categories with separate projects, ran by the same team. Especially with chainlist being just a list of rpcs, forked by another project.
It feels like a way to participate in both rounds, and utilize their fans to max out matching funds in both rounds. I believe this should be discouraged, otherwise other projects will follow suit in order to game the system if some rules are not set.

-------------------------

bobjiang | 2023-03-15 23:54:57 UTC | #3

Thank a lot @connor for your summary!
I would say "yes" for this proposal.

Also I have the same concerns with @lefterisjp about one grants within multiple rounds.
This must be a bit complex situations for dGrant. e.g

- one grant could be in multiple rounds (no limitations)
- one grant could be in limited rounds (e.g N)

but if we limit the number of rounds one grant could be in, what is the number? 1,2,or more?

I can understand lefteris concerns, which are that grantees farmed the rounds.

-------------------------

caifukk | 2023-03-16 00:55:23 UTC | #4

As a donor, the money is used where it should be used, and not being scammed by malicious projects is the best result. It is doing very well so far, everyone has worked hard

-------------------------

connor | 2023-03-16 03:09:33 UTC | #5

Thanks for the quick reply!

For the April Beta rounds, which will be larger scale, @koday will be sharing the first draft of the eligibility criteria and other rules on the gov forum soon, hopefully by this Friday. From there we'd love to get significant community and steward input on how we structure the rules for this upcoming round and in the future. That will be the perfect place to raise points like this and ensure they are enacted where the majority agrees

-------------------------

jengajojo | 2023-03-16 09:16:37 UTC | #6

Thanks for the summary @connor 

First I want to thank everyone involved for their contribution. Considering many other alpha stage products perform way below the output we have here, I am in favor of ' *Ratify the round results*'

[quote="connor, post:1, topic:13277"]
Only ~10% of attempted passports failed, and ~10% of donors did not have any passport at all.
[/quote]

Are there any conversation on having a fail-safe backup for passport incase the service doesn't work? If i understand the text below accurately, 20% donors were never factored into the calculation which seems like a high number?

[quote="connor, post:1, topic:13277"]
**Advanced sybil attackers**: 
[/quote]

Do we know what % of address/donors fall in this category? Is it possible that advanced sybils maybe able to learn and route around automations, which means that we'd need to perpetually fund creation of new filters?

[quote="connor, post:1, topic:13277"]
pairwise matching as an option for possible customizations that will be set and published on-chain at the time of grant program creation.
[/quote]
+1

-------------------------

ccerv1 | 2023-03-16 21:11:19 UTC | #7

I agree with these points -- and in general that Gitcoin should be more opinionated in how it runs its own rounds. (This can also help mitigate Sybil attacks.)

I am also excited about the near-future when anyone can be a Round Manager and thereby toggle those parameters however they see fit.

31K unique donors + 74% passport completion is no small feat! Congrats everyone!

-------------------------

azeem | 2023-03-17 15:13:19 UTC | #9

After taking a look, I'd say "yes" to this proposal. Appreciate you taking the time to put together so comprehensive.

-------------------------

babytiger | 2023-03-17 23:26:17 UTC | #10

good stuff i like how gitcoin is moving things and getting the community involve

-------------------------

M0nkeyFl0wer | 2023-03-20 17:26:13 UTC | #11

Thanks for all the work done on this y'all and the detailed explanation.

-------------------------

ale.k | 2023-03-20 18:00:09 UTC | #12

Really excited for the learnings unearthed from this round and looking forward to keep iterating for beta rounds! I'm in support of these matching amounts- and congratulations to everyone who participated with amazing projects around the space!

-------------------------

DisruptionJoe | 2023-03-20 18:47:30 UTC | #13

Thanks for the work here. Congrats to a successful Alpha Round. It looks like we have plenty of steward comments to legitimately move this forward to a Snapshot vote.

-------------------------

krrisis | 2023-03-20 22:00:38 UTC | #14

Thanks Connor for the great and detailed overview, I will vote yes here.

-------------------------

shawn16400 | 2023-03-21 09:45:52 UTC | #15

Stewards and GTC holders, 
Following the standard process, this proposal has been moved to a snapshot vote and can be found here.  The vote closes on Monday, March 27.  Please cast your vote!

https://snapshot.org/#/gitcoindao.eth/proposal/0x921899e842c8a3f43026e0817b3a06b8117d1a23166ef192db275fb11af9ac7b

-------------------------

Alex07UP | 2023-03-21 15:35:05 UTC | #16

Unfortunately, there was little information on some projects, especially on the website. I hope Gitcoin was accurate to the selection.

-------------------------

lefterisjp | 2023-03-21 20:34:45 UTC | #17

voted yes as per my initial post here: https://gov.gitcoin.co/t/proposal-ratify-the-results-of-january-s-alpha-rounds-and-formally-request-the-community-multisig-holders-to-payout-matching-allocations/13277/2?u=lefterisjp

-------------------------

epowell101 | 2023-03-21 21:25:17 UTC | #18

Good ideas IMO @bobjiang and @lefterisjp 

Fwiw one of the projects emerging out of the OpenData Community looks specifically at grants both to screen (proactive like Passport) and within the round (for eg seeing which grants are receiving lots of Sybils to vote for them).  

Hopefully this will be helpful to all future round operators to make their own determination.

-------------------------

smartionet | 2023-03-24 02:59:11 UTC | #19

I agree. :grinning:
Nice to be with you in this round.
Yours JJ

-------------------------

connor | 2023-03-28 06:29:28 UTC | #22

Quick update - the ratification vote has passed! https://snapshot.org/#/gitcoindao.eth/proposal/0x921899e842c8a3f43026e0817b3a06b8117d1a23166ef192db275fb11af9ac7b

We hope to process payouts by the end of this week. Stay tuned :slight_smile:

-------------------------

Digijoe7 | 2023-08-13 00:33:50 UTC | #24

@Alex07UP I agree. There was definitely not enough info

-------------------------
