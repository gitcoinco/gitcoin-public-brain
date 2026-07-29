---
id: 16553
title: "[Proposal] Ratify the Results of GG18 and Formally Request the Community Multisig Holders to Payout Matching Allocations"
slug: proposal-ratify-the-results-of-gg18-and-formally-request-the-community-multisig-holders-to-payout-matching-allocations
category: gitcoin-grants
url: https://gov.gitcoin.co/t/proposal-ratify-the-results-of-gg18-and-formally-request-the-community-multisig-holders-to-payout-matching-allocations/16553
created_at: 2023-09-22T18:42:49.951Z
last_posted_at: 2023-10-15T02:35:27.224Z
posts_count: 81
views: 16069
like_count: 362
---

# [Proposal] Ratify the Results of GG18 and Formally Request the Community Multisig Holders to Payout Matching Allocations

<https://gov.gitcoin.co/t/proposal-ratify-the-results-of-gg18-and-formally-request-the-community-multisig-holders-to-payout-matching-allocations/16553>
umarkhaneth | 2023-10-10 18:23:54 UTC | #1

Thank you ​​to @Joel_m, @ghostffcode, @gerald, @jeremy, @owocki, @Sov, @M0nkeyFl0wer, and @Connor for getting us to final round results!

**Payments have now gone out!** 

This proposal has passed on [snapshot](https://snapshot.org/#/gitcoindao.eth/proposal/0xf4f44efa6c9a2968c8fba8fd664b7ba03a03b876eb033c09dd088d62877eb2fa)

# TL;DR

GG18 matching results are live [here](https://docs.google.com/spreadsheets/d/133eTg4V0iSsK0Id3iBMV1eHRogeWhJm91H2t0fWL0WE/edit#gid=1644179427)! We propose five days for discussion and review followed by a 5-day snapshot vote to ratify before processing final payouts. In GG18, we move to a variant of QF that uses cluster-matching to introduce sybil and collusion resistance natively into the mechanism and reward projects with more diverse and pluralistic communities.

Edit: Results have been updated. 
[Version 2 detailed](https://docs.google.com/spreadsheets/d/133eTg4V0iSsK0Id3iBMV1eHRogeWhJm91H2t0fWL0WE/edit#gid=1644179427)
[Version 2](https://docs.google.com/spreadsheets/d/1Qm8fLGPEoxzmioi42bgiaEZiyStfbxQ8H4Be9ysGANU/edit?usp=sharing) 
[Version 1](https://docs.google.com/spreadsheets/d/1HXhxuG8ElPF99Xs_q9_MY7-kV_S3GSf5jCyRSXp465s/edit#gid=1426584490)

# Round Results

This round saw increased crowdfunded contributions above the previous two rounds on Grants Stack & Allo – making it the biggest ever on the new decentralized tech stack.

* With $680k crowdfunded, we saw a 12% increase from the Beta round 🎉
* With 328k contributions, we saw a 65% increase from the Alpha round 🎉

This round also saw the Grants Stack team make significant improvements to the product, including Multi Round Checkout, which makes it easy to donate across rounds *and chains.*

Every core round was also on an L2, including the first round on the new Public Goods Network. This round, fittingly, funded Ethereum Infrastructure. It ended up being the second-largest round of the season by crowdfunding despite having the smallest matching fund and fewest grantees of the four core rounds. This is a testament to the ease of bridging and the focused interests of our community.

Kudos to everyone who worked hard to make this round a success!

# Round and Results Calculation Details

The complete list of matching results & payout amounts can be found [here](https://docs.google.com/spreadsheets/d/133eTg4V0iSsK0Id3iBMV1eHRogeWhJm91H2t0fWL0WE/edit#gid=1644179427). Below, we’ll cover how these results were calculated and other decisions.

Post-round analysis had a $300k financial impact. This means $150k was reduced from projects that saw sybil or collusive activity and given to other projects.

## Core Rounds:

|Round|Matching Pool|Matching Cap|
| --- | --- | --- |
|Open Source Software|$300,000.00|5%|
|Ethereum Infrastructure|$200,000.00 or 106.9 ETH|10%|
|Web3 Community & Education|$250,000.00|6%|
|Climate|$350,000.00|10%|

In the climate round grantees were given the option to opt-in to an extra $100k of matching funding from Shell. Over 64% of projects chose to opt-in to this funding.

# Next Gen Quadratic Funding

In theory, quadratic funding combines democracy and markets to create an optimal mechanism for communities to fund what matters. Under this mechanism, a project with many different supporters contributing some amount will receive much more funding than another project that gets the same total contribution from a single “whale.” However, Quadratic Funding’s optimality relies on assumptions that don’t hold in the real world.

It assumes that each donor is entirely different from every other and perfectly rational when deciding what projects will create the most value for them. However, we have users who will produce hundreds or even thousands of fake wallets to support themself. We also know users who will conspire to vote a particular way based on others voting the same way. Further, we’re not all completely distinct; many are members of the same social circles or communities.

[Cluster-Match Quadratic Funding](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4311507) takes a step toward solving the sybil and collusion problems by embracing the meaning of our social connections. It was developed by [Joel](https://gov.gitcoin.co/u/joel_m/summary) (who joined Gitcoin as part of the [QED](https://gov.gitcoin.co/t/gcp-010-evolving-gitcoin-grants-the-q-e-d-quadratic-experimentation-and-development-program/14174) program), [E. Glen Weyl](https://gov.gitcoin.co/u/glenweyl/summary) (who co-authored the original QF paper with Vitalik), and our very own Erich (who has been working on pluralism since at least 2019 and most recently on Gitcoin Passport).

Cluster-Match QF takes the projects you vote for as signals of the communities you belong to. It then calculates matching amounts for each supporter and unique community combination. This method provides more significant matching funding to projects that receive support from more diverse communities.

The outcome is clear: sybils and colluders receive fewer matching funds, while grants that create value for the broadest range of communities receive the most. By implementing this method, we reduced the match of the most suspicious projects by up to 70% and redirected those funds to other projects.

For more details about pluralistic QF methods, check out [this paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4311507) and/or [this podcast](https://open.spotify.com/episode/2Z0u8x4SQtK9LABzAuQteR).


# Sybil Detection

The primary anti-sybil mechanism for this round is Gitcoin Passport. Passport aggregates identity signals from across web2 and web3 to understand the likelihood of an individual being a unique human. If an individual’s score is below a set threshold, then they’re less likely to be a real human because they don’t have all the identity signals a real human typically would. Individual donations have previously received multipliers of anywhere from 2 to 25x, and this means our system is a target for bad actors that’s worth making it hard to get into.

73.2% of wallets that donated reached a score of 20 or higher.

As with most QF Rounds, we saw some sophisticated Sybil attack patterns that still needed to be stopped by Passport (yet!). We can learn from these attack patterns and modify the stamp scoring mechanism to make it impossible for Sybils to get in the same way again.

We were able to detect these sybil attacks through programmatic analysis built specifically for Anti-sybil. We leveraged the new [regendata](https://gov.gitcoin.co/t/regendata-xyz-our-sybil-resistant-future-q3-2023-and-beyond/16474) database to build new python-based tools for finding Sybils. These tools can continue to be used and iterated on such that every round sees them get better.

After our on-chain data analysis, donations from addresses associated with these behaviors were excluded from match calculations. This includes the following:

* Enhanced analysis of passport stamps to flag evidence of abuse between different wallets
* ​​Flagging known sybil networks/addresses from our 40k address blacklist
* Suspected bot activity based on anomalies detected in transaction patterns
* Suspected bot activity based on anomalies detected in donation patterns


# Vote

We ask our Community Stewards to ratify the GG18 payout amounts as being correct, fair, and abiding by community norms, including the implementation of Passport scoring as well as Sybil/Fraud judgments, squelching, and quadratic funding parameters made by the Public Goods Funding workstream.

If stewards and the community approve after this discussion, we suggest voting on Snapshot from Wednesday, September 26th to Sunday, October 1st. If the vote passes, the multisig signers can then approve a transaction to fund the round contracts, the results will be finalized on-chain, and payouts will be processed promptly after

Options to vote on:

**1. Ratify the round results**

You ratify the results as reported by the Public Goods Funding workstream and request the keyholders of the community multisig to payout funds according to the GG18 final payout amounts.

**2. Request further deliberation**

You wait to ratify the results and request keyholders of the community multi-sig wallet to delay payment until further notice.

Lastly:

![|447x421](upload://fTNC06FjVgRhJGoMgzIqt79y6bX.png) meme credit to @McKennedy

-------------------------

M0nkeyFl0wer | 2023-09-22 21:44:02 UTC | #3

You ser are a gift to this community. Thank you!

-------------------------

annika | 2023-09-22 22:36:12 UTC | #4

Congrats on a successful round!

One idea, process-wise here for the future: 

I always found it unintuitive that we have the community ratify results & approve payouts for something that it really makes more sense for core team members to validate. Those of us outside of the weeds just don't have the context/process required to say "yes these results adhere to the intent laid out for the round" or "no they don't".

- Maybe in the future this gets excluded from governance surface area? (i.e., the stewards agree that this is something dedicated DAO contributors can decide on themselves — and we get an FYI on what the end payout amounts were, rather than having to formally ratify them)

- Better yet, perhaps there's a low-fi "dual control" type process that a handful of stewards could run to say "yes this looks good"? (e.g., spot checks that there are no projects above matching cap thresholds, etc)

Just food for thought!

-------------------------

DistributedDoge | 2023-09-23 02:34:11 UTC | #5

Fully agreed with previous post. I see zero way to reproduce any of this without being led behind the curtain by someone. In ideal world report would be crafted in a way that gives confidence in matching calculations while obscuring details of sybil defense.

I understand algorithm is new and link between raw donations and matching results may be more muddled, but is something preventing you from sharing algorithm-agnostic information that used to be present in past reports:

- how many distinct non-sybil donations were made for each grant? 
- how much "valid, non-sybil" money was donated to each grant (before matching calculations). 

This is information only Gitcoin may know, so it is especially valuable when looking at results. 

Since you did the counting I assume you have actual implementation of novel algorithm on-hand, not just paper so why not share it? That way we could at least see what kind of results the algorithm is producing when run on example data and see if matching results look plausible in light of that. 

Past reports (Alpha/Beta round) gave opportunity to stewards, donors, voters, anyone to look at results and intervene if they spotted something strange in data presented. This gave some extra credibility to vote counting process which current single-column spreadsheet does not provide especially when coupled with new method of counting votes.

-------------------------

umarkhaneth | 2023-09-23 07:48:52 UTC | #6

[quote="annika, post:4, topic:16553"]
I always found it unintuitive that we have the community ratify results & approve payouts for something that it really makes more sense for core team members to validate.
[/quote]

Thanks for sharing your perspective from leading PGF Annika! I really agree with this especially given that this process slows down payouts by 10 days. In an ideal world I think we have payouts be nearly instant after the round ends and all sybil defense either handed by passport or automated.


[quote="DistributedDoge, post:5, topic:16553"]
In ideal world report would be crafted in a way that gives confidence in matching calculations while obscuring details of sybil defense.
[/quote]
I hear you. We really want to move this to a transparent mechanism without giving away the game to sybils.

We could and should share more high-level information that sheds more light on what we do for those community members interested in the details. 

Let me get some sleep and then pull together + share the following:

* Code/formula used for cluster match QF 
* Pre / Post Sybil Analysis Donor #s and Donation $'s 
* Pre/ Post Cluster-Match QF Matching $'s

If anyone from DAO core has objections to the above information being shared please let me know!

-------------------------

rohit | 2023-09-23 05:13:47 UTC | #7

As social centrality comes into focus, cluster-match QF is going to break some online friendships for the greater good (jk...😅).

Kudos and gratitude to the entire team and the supporting community crew for this analysis and protecting the funds for public goods!

-------------------------

BearMarco | 2023-09-23 07:42:12 UTC | #8

Thank you for all the work and for showing the extensive details about how they were calculated.

Love to see the dedication to transparency and fairness in the process. Kudos to everyone involved in making this round a success.

-------------------------

krrisis | 2023-09-23 12:49:11 UTC | #9

Thanks for all the work on this Umar <3 

Will be voting yes on this + agree with annika's comments.

-------------------------

charlesfreeborn | 2023-09-23 15:35:59 UTC | #10

Congratulations to the team and all the projects on GG18.

It's a vote of yes for me!

However, I observed that the results didn't show the number of contributions for each projects and the amounts contributed. What is shown in the results is just the matching amount.

-------------------------

M0nkeyFl0wer | 2023-09-23 15:53:59 UTC | #11

I am intending to bring a proposal to ratify the round structure and release the funds pre round moving forward. This would speed up the payouts dramatically. 

I do think its good to share the process and details of Sybil defense. Hopefully we can do that in more details as a WIP as the process unfolds so folks can provide context and feedback sooner after the end of the round. @umarkhaneth has built some fantastic tools along with others on the team and in the community which should speed this process up and increase credible neutrality.

-------------------------

M0nkeyFl0wer | 2023-09-23 15:55:51 UTC | #12

Good point, perhaps that should be changed. We will discuss how best to do this so people understand how cluster match QF and the rules of the round are applied and are represented in the results.

-------------------------

Yazdani | 2023-09-23 18:01:45 UTC | #13

@owocki
Hey, it's Yazdani from Unitap. When the previous round got finished we were in 10th place and now we're in 17th place. And honestly it's really weird to us cause we didn't do anything suspicious, we did only one or two announcements.

-------------------------

deltajuliet | 2023-09-23 19:21:16 UTC | #14

Thanks @Yazdani - @owocki wouldn't be able to answer right now but I'm sure the team on the ground could. 

@M0nkeyFl0wer are there logistics that come into play after the round closes that the community needs to account for? 

I suspect @Yazdani that the results you were seeing (10) - dropped you down due to the manual work that the Gitcoin crew did after round close - resulting in a lower score (17) @connor I'm making things up, can you speak to why? 

I could be WAYYY off base here but want to continue the convo... cc @umarkhaneth @Sov 

We would love to hear more on how that's not an optimal user flow but will also let the team talk about processes that I'm (literally) assuming at this point. This is how we backlog improvements to Governance. Thanks!

-------------------------

M0nkeyFl0wer | 2023-09-23 19:41:23 UTC | #15

Hey happy to help. Sucks that this can be confusing. Sounds like we are talking about a drop from the previous round to this round? There are any number of factors in terms of the level of support one grantee gets compared to the rest within a given round and from one round to the next. Happy to take a look but it doesn't seem unusual to me that a grantee would move a fair amount from one round to the next with all the changes in other grantees in the round as well as in the market overall. 

If we are talking about "standings" at the end of the this round compared to now that first depending on what dashboard you were looking at the result. Its likely this wouldn't take into account how many of the supporters had passport scores that qualified them to count towards matching fees or if they had donated at least the minimum amount to be considered (generally at least a dollar). Finally it wouldn't account for any squelching of sybil attacks,

Hope that helps. Apologies for any confusion.

-------------------------

priyank | 2023-09-24 11:37:00 UTC | #16

Hi, this is Priyank from Nawonmesh. We were in the Climate Round. 

I am super perplexed about Nawonmesh's matching amount calculations. It seems to be way off from our expectations. 

Two questions -

1) We had 300 votes as per our gitcoin grants page. And 240 passport votes as per the ChainEye dashboard. Considering this, the matching amount for us is too low compared to the others in the Climate round. Want to understand the reasons for this huge gap.

2) I am very sure we opted into the Shell funding while filling the grant application. I even dropped an (unresponded) msg to Jon post-GG18 to check if our email id shared with the Gitcoin team is correct because we were expecting the Shell KYC email. But I don't see Nawonmesh in the Shell funding list. Was it really a silly miss on our end or did something else go into the decision making of who all are eligible for that?

I raised these concerns to @M0nkeyFl0wer and he told me to post them here.

Regards.

-------------------------

DistributedDoge | 2023-09-24 15:53:23 UTC | #17

Any follow-up on efforts to deliver updated columns? 

* Code/formula used for cluster match QF
* Pre / Post Sybil Analysis Donor #s and Donation $'s
* Pre/ Post Cluster-Match QF Matching $'s

Community dashboards and on-chain information is insufficient to correctly compare donations against matchings as they do not account for manual interventions done by Gitcoin team. 

I believe that explaining what happened to @priyank and @Yazdani would be clearer, more persuasive and more quantitative if they were given access to dataset containing grant-level information promised by @umarkhaneth.

From voter/grantee perspective it is impossible to analyse what exactly influenced final matching without knowing the starting point. "How much money was donated to this particular grant (that actually counts for purposes of matching)?" feels like a question deserving a clear non-ambigious and quantitiative answer.

-------------------------

Yazdani | 2023-09-24 17:39:44 UTC | #18

Hey, thanks for your answer. My question was about our place at the end of this round compared to now. So now it's clear, and as a product manager/designer, I would say that Gitcoin should make it way more clear for users so they know the rule. I know that they can find the rule but we can't see them highlighted in the user flow.

And it's so simple to highlight them cause there are only 2 rules:
1. Minimum amount
2. Minimum GP score

-------------------------

ale.k | 2023-09-24 20:02:01 UTC | #19

To this point, I wonder if these result posts could continue the precedent of sharing high-level "rules" that the sybil defense is based off of (i.e. logic + ideally code snippets used to surface related accounts, minimum donation definition, etc.) Then if a particular project has additional questions about the rules/logic that their community triggered- this can be addressed in greater detail for their instance. 

Since sybil action shouldn't be conflated with self-attack- I think it would be helpful for groups like @yazdini and @priyank who might want more info on the silencing, and then can verify for themselves the donors who were hitting these rules.

Overall though- I support ratifying these results. In line with expectations and past rounds' sybil-rates.

-------------------------

RB1610 | 2023-09-25 05:49:05 UTC | #20

Just wanted to express my best wishes to the team behind GG18, what a great round this was! Thank you to @M0nkeyFl0wer @umarkhaneth @jon-spark-eco @MathildaDV and the rest for making sure to support the community whenever and however possible throughout those two weeks :slight_smile:

-------------------------

umarkhaneth | 2023-09-25 05:51:11 UTC | #21

Delivering here on my promise to share more details. 

## How to Calculate Cluster Match QF:

* First, a quick review of simple QF:
  * Sum the square roots of each individual’s contribution to a project
  * Square that sum to get a per-project value
  * Distribute the matching fund proportional to the relative size of each projects square  (and enforce a matching cap so that no project takes too much of the pool by itself)



* Next, cluster-match QF.  Cluster-match QF orients matching funds around communities rather than individuals. This is mainly the same overall process however *before* we square root contributions we cluster them together. 
  * Cluster based on the donation profile of a donor. A donation profile is defined as the set of decisions you made on each project: donate or don't donate. Donors who made all the same decisions are clustered together
  * The contributions to a project by the same cluster are added together as if they were the same voting bloc. Then their square root is taken.
  * After that the process is the same: sum the square roots of all clusters grouped by project, square the sums, and payout the matching fund proportionally.

## In Code:
Thank you to @Joel_m for writing this python function:


```
def donation_profile_clustermatch(donation_df):
  # run cluster match, using donation profiles as the clusters
  # i.e., everyone who donated to the same set of projects gets put under the same square root.

  # donation_df is expected to be a pandas Dataframe where rows are unique donors, columns are projects, 
  # and entry i,j denote user i's total donation to project j 

  # we'll store donation profiles as binary strings.
  # i.e. say there are four projects total. if an agent donated to project 0, project 1, and project 3, they will be put in cluster "1101".
  # here the indices 0,1,2,3 refer to the ordering in the input list of projects.

  projects = donation_df.columns

  clusters = {} # a dictionary that will map clusters to the total donation amounts coming from those clusters.

  # build up the cluster donation amounts
  for (wallet, donations) in donation_df.iterrows():

    # figure out what cluster the current user is in
    c = ''.join('1' if donations[p] > 0 else '0' for p in projects)

    # now update that cluster's donation amounts (or initialize new donation amounts if this is the first donor from that cluster)
    if c in clusters.keys():
      for p in projects:
        clusters[c][p] += donations[p]
    else:
      clusters[c] = {p: donations[p] for p in projects}

  # now do QF on the clustered donations.
  funding = {p: sum(sqrt(clusters[c][p]) for c in clusters.keys()) ** 2 for p in projects}

  return funding
```

## More Numbers
[Here](https://docs.google.com/spreadsheets/d/133eTg4V0iSsK0Id3iBMV1eHRogeWhJm91H2t0fWL0WE/edit?usp=sharing) are the calculation details including both matching formulas and pre/post squelching voter numbers and donation amounts. 

The 'base' totals are the numbers after applying our basic rules: have a passport score over 20 and donate at least $1. 

The 'eligible' totals are the numbers after applying our sybil squelching based on the rules stated above: 

[quote="umarkhaneth, post:1, topic:16553"]
After our on-chain data analysis, donations from addresses associated with these behaviors were excluded from match calculations. This includes the following:

* Enhanced analysis of passport stamps to flag evidence of abuse between different wallets
* ​​Flagging known sybil networks/addresses from our 40k address blacklist
* Suspected bot activity based on anomalies detected in transaction patterns
* Suspected bot activity based on anomalies detected in donation patterns
[/quote]

I'll note that while pulling this data together I found a bug in how my data was being aggregated. I fixed this and it affected the results. To me this underscored the necessary importance of transparency. We need to rapidly move toward turning off post-round squelching and relying only on passport + better QF.

-------------------------

umarkhaneth | 2023-09-25 06:11:51 UTC | #22

[quote="priyank, post:16, topic:16553"]
We had 300 votes as per our gitcoin grants page. And 240 passport votes as per the ChainEye dashboard. Considering this, the matching amount for us is too low compared to the others in the Climate round. Want to understand the reasons for this huge gap.
[/quote]
Hi Priyank, thanks for your question. I can see how this would be confusing at first. 

Looking at your data, I agree that your matching seems low when comparing your number of voters to the number of voters of projects who receive similar matching. Digging deeper into your data, I see this is because of how identical your voters are. Of your 187 eligible voters, 151 (over 80%) of them supported only Nawonmesh. 

Under Cluster-Match QF, your results are different from what they would be under Simple QF. While Simple QF places great importance on the number of individuals supporting a project, Cluster-Match QF places importance on the number of communities in support. Why is this a good thing?

It means a single special-interest community can't dominate the matching pool. QF is meant to allocate funding to public goods based on the breadth of support for those goods. This means it would be wrong to allow a single community to dominate just because it has many people. For example, if enough people from my hometown on Long Island decided we needed to improve our parks and we could quickly each give $1 to a gitcoin grant then we would outvote everyone else to claim a lions share of the matching pool by ourselves. This would be unfortunate for every other community who does not benefit from our project. On the other hand, if the same number of people from all across the world supported us (perhaps our parks are growing medical herbs) then Cluster-Match QF would allocate much more funding. I hope this gives the intuition behind the math.  

The other benefit of this QF implementation is that it means sybil attackers have to also donate to other projects in order to earn more matching for their own project, raising more money for public goods.

In the long-run, we can continue to improve our QF implementations and imo this is a big step in the right direction. I do see how it can be confusing. Especially given that we did not announce we would switch to Cluster-Match QF before the round began. I still think now is the right time to do so because it means we can right away begin improving how we are allocating funding.

[quote="priyank, post:16, topic:16553"]
I don’t see Nawonmesh in the Shell funding list. Was it really a silly miss on our end or did something else go into the decision making of who all are eligible for that?
[/quote]
This was probably just a simple miss. Imo your message here is sufficient to opt-in. I am adding Nawonmesh to the list!

-------------------------

DistributedDoge | 2023-09-25 06:52:31 UTC | #23

Thank you and rest of Gitcoin team for publishing updated results. This, in my eye, is most informative and logically organized matching report that Gitcoin has produced so far. This greatly increases my confidence in both sybil defense and algorithm presented.

Based on @Joel_m reply to my questions in [QED program post](https://gov.gitcoin.co/t/q-e-d-program-update-two-experiments-on-the-vote-to-choose-beta-core-rounds/15991/2) post, I can understand rationale for decision to swap algorithms without announcing it first.

> Naively clustering by donation profile is only really possible if you don’t tell people you’re going to do it before hand (or if you’re not too worried about people strategizing).

I will attempt to sanity-check `base` amounts later, but at the moment I find round data plausible and no longer have any reservations against final report or the process itself.

-------------------------

jengajojo | 2023-09-25 07:07:35 UTC | #24

Thank you @umarkhaneth and squad for sharing the results as well as the rationale on calculations. Cluster matching is definitely a game changer!

I vote to **Ratify the round results**

As feedback, maybe there can be a zkproof attached to the results so folks can confirm the calculations match the logic provided. That being said I understand that you cannot reveal all the strategies used to identify the red team but I hope we can strike a healthy middle ground. 

I'd like to ask what the time distribution looks for producing these results? are there any specific leverage points which could reduce the time to output significantly?

-------------------------

umarkhaneth | 2023-09-25 08:38:57 UTC | #25

[quote="ale.k, post:19, topic:16553"]
if a particular project has additional questions about the rules/logic that their community triggered- this can be addressed in greater detail for their instance.

Since sybil action shouldn’t be conflated with self-attack- I think it would be helpful for groups like @yazdini and @priyank 
[/quote]

Great nuanced points here  as expected from @ale.k , especially about how hard it can be to tell the actor behind sybil action. Also thank you for sanity-checking the results.

[quote="DistributedDoge, post:23, topic:16553"]
Thank you and rest of Gitcoin team for publishing updated results.
[/quote]
Thank you for being so engaged and asking for more transparency. This doesn't happen without that! Please keep doing it :saluting_face:

[quote="jengajojo, post:24, topic:16553"]
As feedback, maybe there can be a zkproof attached to the results so folks can confirm the calculations match the logic provided.
[/quote]

Interesting, I don't know enough about zkproofs to know if this is possible but would be quite cool if so. 

[quote="jengajojo, post:24, topic:16553"]
I’d like to ask what the time distribution looks for producing these results? are there any specific leverage points which could reduce the time to output significantly?
[/quote]
One of the big improvements this round was having [regendata](https://gov.gitcoin.co/t/regendata-xyz-our-sybil-resistant-future-q3-2023-and-beyond/16474) which makes it *much* easier to access clean data sets from grants stack, passport, and onchain. I can't think of other specific leverage points besides having more/better detection methods ready to go in advance of the round ending

-------------------------

gulliverz | 2023-09-25 09:44:49 UTC | #26

[quote="umarkhaneth, post:1, topic:16553"]
![|447x421](upload://fTNC06FjVgRhJGoMgzIqt79y6bX) meme cred
[/quote]

:sweat_smile: :rofl: :joy:
It took me couple of seconds to understand the meme :laughing:

-------------------------

rohit | 2023-09-25 11:00:53 UTC | #27

[quote="umarkhaneth, post:21, topic:16553"]
Cluster-match QF orients matching funds around communities rather than individuals.
[/quote]

I am unsure if I am using the right vocab, but is it fair to assume that clusters are unique to each core round? i.e., the clusters created for allocating the pool for Eth Infra are mutually exclusive from those created for allocations in Climate. Or are clusters agnostic of core rounds and reflective of decisions made on all projects across all core rounds?

-------------------------

priyank | 2023-09-25 11:25:36 UTC | #28

Hi Umar, 

Appreciate the detailed explanation. I now understand the reasoning behind the Cluster-Match QF. While that seems like an approach in the right direction, I wanted to highlight few concerns on this, citing Nawonmesh as an example.

1) In my opinion, urgent climate action needs a bottom-up approach through the formation of many grassroots organizations focused on building local climate resilience by solving local challenges, not just globally appealing projects like medical herbs. In such cases, funding support will have to come primarily from their local communities as these projects might not appeal to global donors, although local climate efforts also contribute to global GHG reduction. Cluster-Match QF seems to be incentivising the opposite approach i.e. a top-down approach and makes Gitcoin unsuitable as a funding source for grassroots climate orgs having only local appeal.

2) The logic of crowdfunding is to get initial social proof from the existing community of the project owners before the larger community jumps in to donate. That is how any web2 crowdfunding platform also works. Now, if that existing community is supposed to prove their legitimacy by also donating to other projects (who they know nothing about), it just creates lot of unnecessary donor friction.

3) Two-third of India survives in less than $2/day. Nawonmesh is a grassroots project operational in one of the most backward regions of rural India. You can imagine the financial capabilities of the immediate and extended communities Nawonmesh serves. Convincing these people to (a) resonate with a project having no immediate benefits to them and (b) DONATE $1, that too in CRYPTO, was itself very very difficult. Expecting them to give more to unrelated projects is completely unrealistic. If I had asked them to also donate to other projects, they would not have donated to Nawonmesh too as it would have been an overkill for them.

Also, ChainEye dashboard had 240 passport votes for us. but you have mentioned 187 eligible voters. I am unable to understand this gap.

[quote="umarkhaneth, post:22, topic:16553"]
This was probably just a simple miss. Imo your message here is sufficient to opt-in. I am adding Nawonmesh to the list!
[/quote]

Thanks a lot. Appreciate it man.

-------------------------

sejalrekhan | 2023-09-25 15:13:09 UTC | #29

Thanks so much for sharing this @umarkhaneth . Really appreciate your time and effort for this. Something similar happened to one of the projects I am associated with >  Impact Stream. 
Despite the number of votes, the matching amount for us is $10?

I echo @priyank , Cluster-Match QF is defeating the purpose of empowering grassroot level organizations to raise funding from Gitcoin as the only support they can get is from their local community. How will that happen? How will we onboard local orgs solving for challenges on local level? Please excuse my ignorance but would like to learn about this.

-------------------------

owocki | 2023-09-25 17:06:39 UTC | #30

from someone who is an ETH core dev:

> https://twitter.com/owocki/status/1706341408452554992?s=46
>  I don’t know who to flag this to but “iron wallet” is not core Ethereum haha it’s in the name 😛 cc @Owocki
> same with INTMAX

maybe worth digging in on how they got in the round?

-------------------------

umarkhaneth | 2023-09-25 18:39:19 UTC | #31


[quote="rohit, post:27, topic:16553"]
I am unsure if I am using the right vocab, but is it fair to assume that clusters are unique to each core round?
[/quote]
Hey Rohit, that's right on the money. We cluster based on the donations only within a single core round at a time.  It'd be a cool experiment to try clustering based on donations to all core rounds and seeing if this gives better results. 

[quote="priyank, post:28, topic:16553"]
funding support will have to come primarily from their local communities as these projects might not appeal to global donors, although local climate efforts also contribute to global GHG reduction.
[/quote]

Hey Priyank! If our goal is the greatest global GHG reduction then shouldn't we be searching for projects which most reduce global GHGs and funding those, regardless of if they're local or not? Climate knowledge is not my forte and I'll defer to @M0nkeyFl0wer for his opinion on this.

[quote="priyank, post:28, topic:16553"]
Cluster-Match QF seems to be incentivising the opposite approach i.e. a top-down approach and makes Gitcoin unsuitable as a funding source for grassroots climate orgs having only local appeal.
[/quote]
Cluster-Match QF is very bottoms-up however rather than trying to fund the largest single community it focuses on funding those who serve the most communities. You're right that this may make it unsuitable for orgs with only local appeal (like parks on Long Island). There may be better funding sources out there for local orgs imo. Gitcoin has always been digital-first. 

[quote="priyank, post:28, topic:16553"]
if that existing community is supposed to prove their legitimacy by also donating to other projects (who they know nothing about), it just creates lot of unnecessary donor friction.
[/quote]

[quote="priyank, post:28, topic:16553"]
Expecting them to give more to unrelated projects is completely unrealistic.
[/quote]

I agree! That's not the answer I would seek. Instead, if I'm participating in a global funding round I'd ask what the appeal of my project is to people outside my local community and how I can create value for a more diverse supporter base. The behavior we want to reward is *cooperation across differences*. If a project is supported by people who are very different then that is a strong signal.

[quote="priyank, post:28, topic:16553"]
Also, ChainEye dashboard had 240 passport votes for us. but you have mentioned 187 eligible voters. I am unable to understand this gap.
[/quote]
I can't speak to how the ChainEye dashboard was built. If it's just based on passport score then they're missing the post-round squelching we do as [described here.](https://gov.gitcoin.co/t/proposal-ratify-the-results-of-gg18-and-formally-request-the-community-multisig-holders-to-payout-matching-allocations/16553/21?u=umarkhaneth)

[quote="sejalrekhan, post:29, topic:16553"]
Something similar happened to one of the projects I am associated with > Impact Stream.
Despite the number of votes, the matching amount for us is $10?
[/quote]
Hi Sejal! Thanks for posting on our forum. Did you see the [detailed spreadsheet?](https://docs.google.com/spreadsheets/d/133eTg4V0iSsK0Id3iBMV1eHRogeWhJm91H2t0fWL0WE/edit#gid=1644179427) Impact Stream's matching *increased* when going to Cluster Match QF. 

[quote="sejalrekhan, post:29, topic:16553"]
Cluster-Match QF is defeating the purpose of empowering grassroot level organizations to raise funding from Gitcoin as the only support they can get is from their local community
[/quote]
This mechanism disempowers uniform, established monoliths and actually empowers grassroots organizations if they're made of diverse, different members. For example, in the Web3 Community and Education round greenpill network with it's global, distributed chapters saw an increase in matching funding of $3,787.93 when going to cluster match QF

[quote="owocki, post:30, topic:16553"]
maybe worth digging in on how they got in the round?
[/quote]

Hey Owocki! thanks for sharing -- will take a look

-------------------------

smith | 2023-09-26 02:57:40 UTC | #32

Thank you to everyone who puts their effort into to making Gitcoin and Quadratic Funding a meaningful way to fund public goods and projects. Every time the Tor Project participates in these funding rounds, I am impressed by the amount of collective effort goes into making them run, communicating clearly with the community, and improving over time.

> Cluster-Match QF takes the projects you vote for as signals of the communities you belong to. It then calculates matching amounts for each supporter and unique community combination. This method provides more significant matching funding to projects that receive support from more diverse communities.

Awesome. Thank you for making it clear the evolution of QF and the reasoning behind the changes.

Congrats to all the grantees!

-------------------------

rohit | 2023-09-26 05:30:50 UTC | #33

[quote="umarkhaneth, post:31, topic:16553"]
You’re right that this may make it unsuitable for orgs with only local appeal (like parks on Long Island).
[/quote]

There might be one possibility with cluster-matching QF that could benefit local communities. The new algorithm increases the total cost for Sybil attackers and tilts the scale for the system to be "cheaper to defend than attack." It might be a worthwhile exercise (possibly a prospectively funded project in Citizens Round if anyone is interested) to evaluate if we can lower the requirement for Passport Score in the frontend with cluster-matching QF as an additional rear-guard mechanism to nullify Sybil contributions.

To validate this, someone would need to rerun the squelching with one or two lower passport scores and analyze the impact on the final distribution. If the data supports this hypothesis, a lower score will reduce some friction local communities have in onboarding contributors to Gitcoin Grants.

Here is some background in the 2-minute snippet from @owocki's conversation with Joel Miller:
https://share.snipd.com/snip/45ba651f-bca0-43c4-9212-7ad728180211

-------------------------

solarpunkmaxi | 2023-09-26 07:29:58 UTC | #34

hey @umarkhaneth, cluster QF def feels like a step in the right direction.

Just trying to wrap my head around whats happening - Cluster QF filters donors having voted for multiple projects and counts them for QF , so does it also exclude a few donors that projects might have had that have just donated to that single project or that figure needs to cross a certain threshold?

Post Cluster sybil analysis the QF formula applied is the same and you are not tweaking the matching multiple depending on multiplicity of votes from a donor yet?

The difference between base and eligible voters represents the no of votes that projects rcvd from donors just voting for that particular project?

-------------------------

DeFiTeddy | 2023-09-26 10:26:13 UTC | #35

[quote="umarkhaneth, post:21, topic:16553"]
Next, cluster-match QF. Cluster-match QF orients matching funds around communities rather than individuals. This is mainly the same overall process however *before* we square root contributions we cluster them together.

* Cluster based on the donation profile of a donor. A donation profile is defined as the set of decisions you made on each project: donate or don’t donate. Donors who made all the same decisions are clustered together
* The contributions to a project by the same cluster are added together as if they were the same voting bloc. Then their square root is taken.
* After that the process is the same: sum the square roots of all clusters grouped by project, square the sums, and payout the matching fund proportionally.
[/quote]

First, Thanks for the hard work done for doing the cluster match QF :slight_smile: 

I just have a question: " the same cluster are added together as if they were the same voting bloc", I do not quite understand it. Say if one cluster/community has 100 voters, it is considered as one voter?

I understand that the votes from the same cluster should be given less weight, but treating them as from one voter is not quite fair especially for some local communities.

-------------------------

priyank | 2023-09-26 13:58:56 UTC | #36

[quote="umarkhaneth, post:31, topic:16553"]
If our goal is the greatest global GHG reduction then shouldn’t we be searching for projects which most reduce global GHGs and funding those, regardless of if they’re local or not?
[/quote]

Hi Umar, I agree 100% with your statement. But as of today, none of the climate projects write their GHG reduction potential on their gitcoin grant pages. The simple reason for this is that it is something very difficult to quantify accurately at the early stage of the projects. Due to that, the global appeal of a project does not mean that it has the highest GHG reduction potential. It might just be due to an interesting product, eg. medicinal herbs, or the likability of the founder on twitter interactions. Many grassroots orgs like Nawonmesh work on not-so-interesting things like local regeneration. And are run by senior citizens who are non-digital savvy and non-native English speaker, so spending time on Twitter spaces to showcase their charisma is not their forte (The main reason I am representing Nawonmesh in all the online interactions). It is much easier for them to interact with their local community for support.

[quote="umarkhaneth, post:31, topic:16553"]
There may be better funding sources out there for local orgs imo.
[/quote]

Unfortunately, the experience of Nawonmesh's founder says that the fundraising opportunities for regenerative activities are limited in their region.

[quote="umarkhaneth, post:31, topic:16553"]
The behavior we want to reward is *cooperation across differences*. If a project is supported by people who are very different then that is a strong signal.
[/quote]

Fair logic.

I also feel that we need to increase the donor base of the whole climate round. Compared to the other core rounds, the amount donated and unique donors are way less for the climate round. One of the easy ways to achieve that could have been to let climate projects onboard their communities and then few members from a particular project's community would have started cross-funding other projects too in subsequent rounds. Imagine if 100 climate projects could bring in just 50 new people, it would have almost doubled the 'unique donors' count for the climate round. But, due to Cluster-Match QF, the strategy of onboarding new communities has been somewhat disincentivized.

[quote="umarkhaneth, post:1, topic:16553"]
Version 2 detailed
[/quote]

Why are the "Eligible Voters" numbers different for the same project in the "Climate" and "Climate - Shell" sheets in the updated results?

-------------------------

thedevanshmehta | 2023-09-26 16:01:39 UTC | #37

Thanks to @umarkhaneth and team for all the great work! Here's some quick comments on the discussion going on

[quote="annika, post:4, topic:16553"]
I always found it unintuitive that we have the community ratify results & approve payouts for something that it really makes more sense for core team members to validate. Those of us outside of the weeds just don’t have the context/process required to say “yes these results adhere to the intent laid out for the round” or “no they don’t”.
[/quote]

I am against automation of the payout process that @umarkhaneth , @M0nkeyFl0wer & @annika are in favor of.

it's not just a mathematical formula but a social consensus on the best way to leverage the wisdom of the crowds. And the post analysis, pre-payout period is when some of the most active discussions take place. it would be tragic to let go of this tradition.

My main concern with this rounds distribution is just how closely it mirrors the 'winner take all' approach of the real world. Consider this chart i [found](https://x.com/timdaub/status/1706278967848628274?s=20) showing the distribution in the open source round, the inequality is worse than any capitalistic nation. 

![gitcoin matching|690x422](upload://xxJUiAvnZXUm9s5TMKKmdffP6Rj.png)

I wonder if we could develop a gini coefficient or some such metric capturing inequality among projects as a 1st step to possibly reducing it in future rounds. Here's some interesting research on progressive taxation in quadratic funding systems from DoraHacks thats worth exploring

[https://research.dorahacks.io/2021/06/16/reduce-quadratic-funding-inequality-with-a-progressive-tax-system/](https://research.dorahacks.io/2021/06/16/reduce-quadratic-funding-inequality-with-a-progressive-tax-system/)

I also don't know how much were following the gitcoin beta round squelching, but the difference that my project received from the 1st spreadsheet to the last was over 30%. These window periods are valuable for getting the community's assistance in identifying sybil attackers, such as how [mini meadows](https://gov.gitcoin.co/t/discussion-proposal-ratify-the-results-of-gitcoin-s-beta-round-and-formally-request-the-community-multisig-holders-to-payout-matching-allocations/15166/27?u=thedevanshmehta) & some others got caught last round in this window period.

[quote="sejalrekhan, post:29, topic:16553"]
I echo @priyank , Cluster-Match QF is defeating the purpose of empowering grassroot level organizations to raise funding from Gitcoin as the only support they can get is from their local community. How will that happen? How will we onboard local orgs solving for challenges on local level?
[/quote]

I will say that contrary to my expectations, the teams active on gitcoin radio have performed better under cluster QF. Maybe because we each gave to so many different projects that it increased the value of our vote. So while it won't initially help local convergence, it is certainly helping digital coordination!

[quote="priyank, post:28, topic:16553"]
Two-third of India survives in less than $2/day. Nawonmesh is a grassroots project operational in one of the most backward regions of rural India. You can imagine the financial capabilities of the immediate and extended communities Nawonmesh serves. Convincing these people to (a) resonate with a project having no immediate benefits to them and (b) DONATE $1, that too in CRYPTO, was itself very very difficult. Expecting them to give more to unrelated projects is completely unrealistic.
[/quote]

I agree with this point, I urge the team to consider making 10 cents the minimum vote for matching. $1 while living in the west is very different from $1 in the global south. Also, 20-35% of my project votes came from those giving less than a dollar, sometimes 10 cents and tragically even a few 95 cents :frowning_face:

Finally, I request the team to not publicly list the payout address of projects as many operate in hostile environments where this information could be used against them

-------------------------

berksohto | 2023-09-27 12:14:24 UTC | #38

Following some email exchanges with ben , he made me realize it would be more beneficial for us to shift our discussions to the government forums to embrace a "build in public" approach.

We also see some similar points as @priyank 's regarding our project.

1. After extensive internal discussions, we made the decision to participate in the Climate-Shell round, so we were opted-in during the application. However, we have noticed that our project is not listed in the Excel file.

2. @umarkhaneth  would you also please kindly look for our project again as numbers show some unfairness I can't comphrend ?

* Marked our Earthist - Decentralize the Seeds project with a magenta color in the climate round, and just to understand the numbers in comparison:
We have the second-highest number of eligible voters and eligible crowdfunding yet our match rating is lowest on below example sheet. While the average contribution for our project is $1.66.

We are eager to gain a better understanding of the situation for such low matchmaking even with high passport granted supporters. Your guidance and support in this matter would be greatly appreciated.

![image|690x218](upload://2zt8G706i1jD2gXp565wlYyNzYM.png)

![image|690x71](upload://s4BLpLLJ9DeWukOqO46G1gbwzJ0.png)

-------------------------

carlosjmelgar | 2023-09-26 19:06:02 UTC | #39

Thanks for all the hard work that went into this @umarkhaneth and other contributors. Seeing QF continue evolving is a beautiful thing. It's important to consider that the red team is always one step ahead. This requires continues action from the blue team. [I saw this topic discussed on the Green Pill Podcast, but seeing it in action hits different](https://youtu.be/ueQDnq-J2mY?si=oyWJ4UKhJfdcPVjV).

[quote="annika, post:4, topic:16553"]
I always found it unintuitive that we have the community ratify results & approve payouts for something that it really makes more sense for core team members to validate. Those of us outside of the weeds just don’t have the context/process required to say “yes these results adhere to the intent laid out for the round” or “no they don’t”.
[/quote]
Fully in support of this statement. This can help reduce the turnaround time in payouts.

[quote="priyank, post:28, topic:16553"]
Two-third of India survives in less than $2/day. Nawonmesh is a grassroots project operational in one of the most backward regions of rural India. You can imagine the financial capabilities of the immediate and extended communities Nawonmesh serves. Convincing these people to (a) resonate with a project having no immediate benefits to them and (b) DONATE $1, that too in CRYPTO, was itself very very difficult. Expecting them to give more to unrelated projects is completely unrealistic. If I had asked them to also donate to other projects, they would not have donated to Nawonmesh too as it would have been an overkill for them.
[/quote]

I can relate to these challenges faced in the global south. I'd like to highlight a Climate Solutions project that has been working extremely hard in a country where [minimum wage is $5 and a family needs 108 minimum wages](https://english.elpais.com/international/2023-03-07/venezuelans-struggle-to-survive-on-the-lowest-minimum-wage-in-latin-america.html) to sustain a family of 4 with basic needs. [Mi Costa de Oro](https://twitter.com/CostaOro80489) has spent months onboarding their community members to web3 tools ([snapshot voting](https://twitter.com/CostaOro80489/status/1690700407239057408), [paying for basic needs with crypto](https://twitter.com/CostaOro80489/status/1689088330753769472), [sending/ receiving tokens when compensated for beach clean ups](https://twitter.com/CostaOro80489/status/1703809485037322260), minting mirror articles, etc). Despite all their hard work since April, not one of them is able to obtain a Gitcoin Passport score that enables matching. This means they didn't even attempt to vote in the round. They were able to create impressive results this round by providing constant and transparent proof of their work and work incredibly hard to promote their grant during the Shill spaces. None of their contributors speak English. This means they mustered up the courage to participate in English speaking spaces, request the mic, shill their project in Spanish and hope people understood or someone present could translate for them.  I'm pointing this out because your project can take a page from their playbook. 100% of the images published by the Nawonmesh twitter account are AI generated.  almost all AI generated images. This looks pretty compared to the low quality images published by Mi Costa de Oro, but they don't do a great job showing the work and impact being pitched in the grant application. 

I'm really interested in learning how you were able to get the contributors to achieve passport scores above 20 points because it has been a huge barrier for the communities I work with. I haven't been able to get a single contributors in these communities above 8 points. 

[quote="sejalrekhan, post:29, topic:16553"]
echo @priyank , Cluster-Match QF is defeating the purpose of empowering grassroot level organizations to raise funding from Gitcoin as the only support they can get is from their local community. How will that happen? How will we onboard local orgs solving for challenges on local level? Please excuse my ignorance but would like to learn about this.
[/quote]

I can understand the frustration with this, but I also think it's healthy for the ecosystem. It creates a pluralistic and regenerative environment where people looking to be funded also take the time to become immersed in the ecosystem, learn more about other projects and potentially collaborate or copy pasta some of their work to benefit their local efforts.

[quote="thedevanshmehta, post:37, topic:16553"]
I am against automation of the payout process that @umarkhaneth , @M0nkeyFl0wer & @annika are in favor of.

it’s not just a mathematical formula but a social consensus on the best way to leverage the wisdom of the crowds. And the post analysis, pre-payout period is when some of the most active discussions take place. it would be tragic to let go of this tradition.
[/quote]

I'm in favor of these conversations happening in between rounds in an attempt to establish a structure that doens't require debate after every round. It's important to consider that many of the smaller projects are living day to day. Continuously delaying payouts for the sake of big brain back and forth seems like torture to many of these projects. Let's come up with a more streamlined process and stick to it until something serious breaks and needs fixing. 

[quote="thedevanshmehta, post:37, topic:16553"]
My main concern with this rounds distribution is just how closely it mirrors the ‘winner take all’ approach of the real world. Consider this chart i [found](https://x.com/timdaub/status/1706278967848628274?s=20) showing the distribution in the open source round, the inequality is worse than any capitalistic nation.
[/quote]
I'd be interested in seeing how this correlates to userbase. For example - Do Lenster, revoke, JediSwap have a much bigger userbase or transactional volume than projects on the lower end of match funding? If yes, I think this pays out fairly. I don't know those figures, but my gut tells me the funding received reflects the size of their userbase as well. It would be really interesting to identify projects that didn't perform well, but house big userbases. 

[quote="thedevanshmehta, post:37, topic:16553"]
Also, 20-35% of my project votes came from those giving less than a dollar, sometimes 10 cents and tragically even a few 95 cents
[/quote]
These might be bot donors. It was something that also occurred in the C grants platform, even between rounds. It always confused grantees. I don't think this is a case of donors giving 95 cents, or less than $1 because that's all they could afford. 

My big question looking ahead is - Wen Cluster Match + trust bonus based on passport score?

-------------------------

Joel_m | 2023-09-26 21:34:06 UTC | #40

[quote="priyank, post:28, topic:16553"]
Cluster-Match QF seems to be incentivising the opposite approach i.e. a top-down approach and makes Gitcoin unsuitable as a funding source for grassroots climate orgs having only local appeal.
[/quote]

Hey @priyank , I really appreciate you sharing your unique perspective. As we have these discussions about what funding allocations should look like, I want to give my interpretation of the problem QF was originally designed to solve, which I think is different from the problem you're pointing out. 

QF was designed to solve the problem of public goods funding under imperfect coordination. The first iteration of QF solves this problem in a world where people are maximally uncoordinated (i.e. everyone is completely selfish and isolated). In contrast, if everyone was perfectly coordinated, we wouldn't need QF at all. 

But the real world has a mix of coordination and isolation. We have local communities with internal communication channels (coordination), but people in different communities may still be isolated from each other. So the new algorithms like Cluster Match try to make funding work in this world by giving less money to projects supported by just one community, and instead favoring projects with diverse bases of support. If a project only has local support from one community, Cluster Match assumes that project doesn't need as much extra funding, since the people in that community should be able to figure out how much to fund it on their own.

Correct me if I'm wrong, but I think you're pointing out that this isn't the whole picture. It may be the case that a local community knows how much money a project *should* get, but doesn't have the cash to fund it. IMO this is kind of an orthogonal issue which is important to address, but needs different tools and different analysis. Of course, it's important to be aware of a case where trying to be more optimal along one axis (accounting for coordination) may have been less optimal along another axis (accounting for differences in ability to pay). But I think being clear about the microeconomic foundations of what's going on here can help us move forward in the best way. 

For what it's worth though, I think the picture around how Cluster Match impacts communities with differences in ability to pay isn't so simple. I actually think that with all else held equal, switching to Cluster Match tends to help communities with less ability to pay. But this post is already too long so I'll leave out that explanation for now.

-------------------------

KarlaGod | 2023-09-27 05:07:51 UTC | #41

Thank you for the work you do to get these results and thanks to Gitcoin for the transparency, this is excellent work and the fact that not everything is automated shows the level of dedication the team put in, thanks a lot.

I have a question regarding the Eligible Crowd Funding, Simple QF Match, Matching difference, and the rest, I wanted to know if they sum up to what a project would receive. I've had these questions from some of my community members, and I'm unsure how to respond.

-------------------------

connor | 2023-09-27 07:35:16 UTC | #42

I want to give a huge shoutout to @umarkhaneth for driving this and everyone else who helped detect Sybils and implement cluster mapping QF.

I am personally very excited about (and bullish on) cluster mapping and other varieties of QF that can effectively dampen collusion and Sybil attacks across the board in an objective fashion. The old cGrants platform had been using pairwise QF for years (a similar modification to cluster mapping, with similar impact/results). This was first tried in GR5, through GR15 (so almost 3 years from 2020 - 2023). We only went back to "traditional QF" for the Alpha and Beta rounds. 

Most users probably weren't even aware of this and there wasn't a push to publish the match differences between pure QF and pairwise, it was just the method found to work best. Similarly, while I'm glad Umar shared matching calcs for both methods in this case, given it's the first time it's being tried, I don't think it's productive to publicize all alternatives every round. If we calculated results with pure QF, pairwise, cluster mapping, Sybil or no Sybil squelching, and shared them all to compare, almost everyone would be able to find a scenario where they would get more funding and thus would not be happy. 

I do trust the team doing deep data analysis on Sybils, passports, voting patterns, etc, to find and use the best method to prevent collusion across the board (objectively without manual subjective judgments). We should absolutely be as transparent as possible though about the methods used and decisions made, and I believe we're only getting better in that regard compared to prior rounds.

So all that said, I really appreciate the hard work and hours that went into this from many people, and although not everyone is happy with the outcome, I am in favor of moving forward to a snapshot vote to ratify these results.

-------------------------

rohit | 2023-09-27 10:13:13 UTC | #43

[quote="connor, post:42, topic:16553"]
If we calculated results with pure QF, pairwise, cluster mapping, Sybil or no Sybil squelching, and shared them all to compare, almost everyone would be able to find a scenario where they would get more funding and thus would not be happy.
[/quote]

Strongly agree. We should debate and discuss the methods and their trade-offs, along with which ones are suitable for the current scale of Gitcoin Grants and which we should run low-stake experiments for the future. I am certain Cluster-Matching QF too shall outrun its utility at some point, and we will need to keep evolving. Tethering to outcomes of a single round to cherry-pick design choices will add to fragility.

Ideally, I would love to see more feature rounds operating variations of QF (and other allocation mechanisms) and sharing their learnings across the community. However, there is no one allocation mechanism "to rule them all".

![Screenshot 2023-09-27 at 3.41.10 PM|485x500, 100%](upload://vLl62UGig1JBQRhaE0yJacXVzs6.jpeg)

-------------------------

jayashree | 2023-09-27 10:48:42 UTC | #44

Hi @umarkhaneth 

We at Pollen Buzz Initiative had 'opted in' via email for the additional matching funds from Shell on the 21st of August, but we do not see our projects name in the Shell's matching round results.

-------------------------

rohit | 2023-09-27 11:24:58 UTC | #45

[quote="thedevanshmehta, post:37, topic:16553"]
https://research.dorahacks.io/2021/06/16/reduce-quadratic-funding-inequality-with-a-progressive-tax-system/
[/quote]

I, too, would like to see a less steeper curve. I am not in favor of any form of taxation, yet. This likely deserves a separate thread since it is independent of GG18 results.

My concern with a direct intervention like taxation is that it leaves endemic issues driving inequity unaddressed and dampens the effectiveness of taxation. Moreover, there is a risk that taxation diminishes input signals that are performance-based, such as grantees who show up round after round sharing their impact and raising support from the community will have a disproportionate share of the funding for the right reasons.  

Viewing the allocation of the funding pool in the context of respective eligible crowdfunding contributions adds more to the picture. The top 15 projects in the web3 OSS round received a share of 67.5% of eligible contributions and were allocated 70.3% of the funding pool.

![Screenshot 2023-09-27 at 4.42.00 PM|690x241](upload://6ozfubTubO2DMBZTICWwpG2UCmJ.png)

However, I would still support the case for a less steeper curve. Here are not-so-exhaustive measures, which if they don't make a dent, make the case for taxation stronger.
- Improve discoverability of grantees on the platform who may not have as strong a marketing muscle as larger projects (a lot is happening in this direction [already](https://x.com/grantsstack/status/1704182039258558854?s=20), also shameless self plug for AI-driven discoverability is [here](https://gov.gitcoin.co/t/gg18-grantee-discovery-using-llm-enabled-conversations/16192))

- Find ecosystem partners who can pool funds to run dedicated feature rounds exclusively for smaller projects (based on consensus on definition) similar to opportunities that accelerators and seed-stage funding offer to young start-ups.

- Run QF with weighted votes for subject matter expertise so smaller projects making large strides can see the gains in allocation based on curation from people in-the-know (Token Engineering Commons already did this in a feature round [here](https://medium.com/token-engineering-commons/expertise-and-quadratic-funding-bd4f0c5c3e23)).

- Integrate with a protocol like Hypercerts where firstly, the proof of impact, and then, evaluations, help divert dollars where the action is (food for thought [here](https://gov.gitcoin.co/t/better-impact-funding-the-greenpill-hypercerts-gitcoin-combo-move/16477))

Unfortunately, none of these are silver bullets that will change things overnight, but I am hopeful that ease of discoverability can make an impact in the near term.

-------------------------

littertoken | 2023-09-27 13:47:05 UTC | #47

The funding dashboard & our Grants page showed 990 votes but the final results are showing only 177 base voters. Obvi a pretty big gap. Would appreciate if you can take a look @umarkhaneth - would that be possible?

We can assure you that only 3 people from our community voted, so the vast majority of those votes were from people who genuinely supported our project.

-------------------------

littertoken | 2023-09-27 13:49:10 UTC | #48

Our vote is to not ratify this decision yet. We only received credit for 18% of the votes we received and we worked extremely hard on this last Grant round so it's disheartening for us.

-------------------------

umarkhaneth | 2023-09-27 15:43:08 UTC | #49

[quote="rohit, post:33, topic:16553"]
The new algorithm increases the total cost for Sybil attackers and tilts the scale for the system to be “cheaper to defend than attack.” It might be a worthwhile exercise (possibly a prospectively funded project in Citizens Round if anyone is interested) to evaluate if we can lower the requirement for Passport Score in the frontend with cluster-matching QF as an additional rear-guard mechanism to nullify Sybil contributions.
[/quote]
Tipping the scales to make it more expensive to defend than attack is definitely one of the properties we like about it a lot. Down to run this test you mention as well! 


[quote="solarpunkmaxi, post:34, topic:16553"]
Just trying to wrap my head around whats happening - Cluster QF filters donors having voted for multiple projects and counts them for QF , so does it also exclude a few donors that projects might have had that have just donated to that single project or that figure needs to cross a certain threshold?
[/quote]

Hey solarpunkmaxi! This can be a little confusing but Cluster QF doesn't filter any donors out. Instead, it groups together donors who vote identically (who support the same projects and don't support the same projects) and treats them as a community. Then, each community gets matched instead of each individual. 

[quote="solarpunkmaxi, post:34, topic:16553"]
The difference between base and eligible voters represents the no of votes that projects rcvd from donors just voting for that particular project?
[/quote]

Not quite -- the difference is due to our sybil squelching. Does this quick diagram help? 


![Screen Shot 2023-09-27 at 11.42.38 AM|690x271](upload://RMOyyMwZxL0IUWhff45Q0Bfijy.jpeg)

-------------------------

ASTRO-HSU | 2023-09-27 16:17:20 UTC | #51

This diagram is quite helpful, thanks !

-------------------------

duckdegen | 2023-09-27 19:28:00 UTC | #52

We're at day 5 so in the interest of moving forward I for one vote in favor of ratification of the results.

-------------------------

duckdegen | 2023-09-27 19:35:47 UTC | #53

Dear sir, I have made a dune dashboard back in the days, where even my most basic of analysis shows that there are far less donations above 1 USD than the total count.

Please look here:
dune [com] /queries/2946938

Specifically, for your project my dune query tallies 135 donors that gave more than 1USD, but keep in mind that i dont work for gitcoin and my data may be off.
What is evident from this is that there was a huge amount of airdrop farming going on from donors who dusted a bunch of grantees, and sadly the UI reflected this total tally even if it didnt qualify.

I hope that seeing this data will convince you that the problem is not with the matching, rather with the fact that legit donors were far less than what the UI showed.

It is good to keep in mind that the UI's purpose per se isnt to show filtered, cleaned and refined data, but rather to just show a total of transactions that came in. 
Its good to note that this is a process, and tooling will be improved, but ultimately the data was there to look at even from within your recipient wallet, and considering that the criteria of minimum 1 USD was defined from the start this specific outcome could have been seen from the raw data itself.

hope this helps you gain clarity on this topic

-------------------------

connor | 2023-09-27 23:52:43 UTC | #54

Hey all, the GG18 ratification snapshot vote is now live!

https://snapshot.org/#/gitcoindao.eth/proposal/0xf4f44efa6c9a2968c8fba8fd664b7ba03a03b876eb033c09dd088d62877eb2fa

Thank you everyone for the thoughtful comments, feedback, and debate in here :pray:

-------------------------

littertoken | 2023-09-28 16:08:57 UTC | #55

[quote="duckdegen, post:53, topic:16553"]
dune [com] /queries/2946938
[/quote]

Thanks for looking into it. It's just such a massive drop off that the other top 3 projects (Silvi & Earthist) did not seem to experience (at least not to as severe a degree). It doesn't make sense that "airdrop farmers" would have chosen to disproportionately focus on our project.

I would also call into question the minimum 1 USD donation criteria. Can someone remind me of the logic behind this criteria? Why should people & projects be penalized for giving less than 1 USD? This is especially relevant for projects like ours that focus on the Global South.

-------------------------

FractalVisions | 2023-09-28 16:16:07 UTC | #56

Time to vote 🗳️… Some amazing discussions have been made above ⬆️ and after observing the results along with the sentiment of participants it appears that a significant improvement can be made to this system.

It’s obvious that the projects with a stronger following on social media from past grant rounds that were successful and who have more capital allocated up front were able to drive donations to their projects with ease in order to achieve the highest ranks possible for matching funds. They have large teams allowing for low effort campaigns which are not intertwined with the rest of the community & seem to be out of touch with the smaller teams and projects who are participating completely.

My commentary suggestion about hosting spaces to highlight other projects to one team I don’t want to mention here was completely ignored on social media when they made a post about how they could help other projects during this last round.

I do NOT see the camaraderie that one another offers when participating in each round in order to help shill it forward for other impact makers in the round. 

The competition between the larger projects to overtake the entire round without some sort of system put into place for checks and balances will continue to hinder the overall growth and evolution of the regenerative movement that has sparked the flame of many passionate individuals who have joined Gitcoin.

Meanwhile the projects with low visibility yet have a ton of impactful potential are not able to campaign without putting in a massive amount of effort, energy, and time which could be used for development work during the round.

It is important to keep in mind that the pie 🥧 will not continue to grow larger if a majority of it is consumed by one entity. The math is simple and plain. No one else will be able to sustain themselves, their projects developments will dwindle, and builders ideas will continue to struggle to survive along with their livelihood. Every last drop of energy put into a project then becomes a waste.
Questions will be made as to why they didn’t do more in between rounds with what little funding they were given from the previous round. Scrutinizing smaller teams during the intake filter is also a concern because they are questioned more heavily than a large establishment is about their proof of impact.

I am curious 👀… Where is the proof of impact threads 🧵 with onchain data 📊 for the biggest projects that have received the most funds in the BETA round?

Do we have any updates from any of the projects that received QF showing their impact onchain ?

-------------------------

Kronosapiens | 2023-09-28 16:39:25 UTC | #57

I'll share a different experience... I've self-funded my project for the last three years, and submitted it for a grant hoping to get a little funding to help offset the costs. The project doesn't have a huge community or a lot of marketing capacity, but based on the organic traffic to the GG18 round alone I was able to raise a very meaningful amount of money.

While I can't speak to what extent large active communities and coordinated marketing efforts may have allowed some projects to secure significant grants in the round, I can say that at least in my case the process worked as intended, where organic traffic chose to support a project that seemed promising.

-------------------------

jon-spark-eco | 2023-09-28 17:40:44 UTC | #58

First, I want to give a big thanks to @umarkhaneth and the rest of the team who worked tirelessly to evaluate GG18. I believe the new tools you deployed along with utilizing cluster matching provided solid results and I have voted to ratify them.

[quote="littertoken, post:55, topic:16553"]
Thanks for looking into it. It’s just such a massive drop off that the other top 3 projects (Silvi & Earthist) did not seem to experience (at least not to as severe a degree). It doesn’t make sense that “airdrop farmers” would have chosen to disproportionately focus on our project.

I would also call into question the minimum 1 USD donation criteria. Can someone remind me of the logic behind this criteria? Why should people & projects be penalized for giving less than 1 USD? This is especially relevant for projects like ours that focus on the Global South.
[/quote]

In watching the round progress Silvi & Earthist received support earlier in the round, and then your project gained significant donations a bit later. This would lead me to believe that your donors were different donors than the other two projects. This is likely why they were squelched less than you, as their donors had different behaviors. Most of the donations your project received were less than $1, which is often an indication of a sybil attack or airdrop farming (though I am not suggesting it was you or your community that attacked). Since the Red team is not transparent about what they do and why they do it, I cannot tell you why your project was chosen by these donors.

Regarding the $1 minimum, this is another sybil protection. Our goal is always to make it more expensive for the Red team to attack and cheaper for us the Blue team to defend. This minimum allows us to remove some of the sybil attackers or airdrop farmers from the start because it forces them to pay more for their vote to count towards matching. I do hear you with regard to communities in the global south that this can be a gating factor. As our passport system continues to improve there may be a point where we can rely more on it and remove this barrier. For now this has been a part of our criteria for many rounds. 

[quote="FractalVisions, post:56, topic:16553"]
The competition between the larger projects to overtake the entire round without some sort of system put into place for checks and balances will continue to hinder the overall growth and evolution of the regenerative movement that has sparked the flame of many passionate individuals who have joined Gitcoin.
[/quote]

Since you participated in the Community & Education round, I will speak specifically about that round though some of what I write may apply to other rounds. In this round that focuses on community, I would say the objective of the projects in this round is to grow community, educate community or be a resource to community, and if the project is successful, that community will fund what matters to them during a round. I would also say that several of the top projects are run by small teams. The fact that they are at the top tells me they are fulfilling the objective of projects in the round (grow community, educate community or be a resource to community). 

On the flip side, it is difficult for QF mechanisms not to become popularity contests, and I think that may be what you are pointing at. I think cluster matching helps with this but does not completely solve it. In that respect, you are right the system will continue to evolve to be fairer over time. Even the authors of the cluster matching research paper do not believe this is the final evolution of this funding mechanism.

[quote="FractalVisions, post:56, topic:16553"]
It is important to keep in mind that the pie :pie: will not continue to grow larger if a majority of it is consumed by one entity. The math is simple and plain. No one else will be able to sustain themselves, their projects developments will dwindle, and builders ideas will continue to struggle to survive along with their livelihood.
[/quote]

To this point, the round has a 6% matching cap, so a project can't earn more than 6% of the pie or $15k. If you assume these projects participate quarterly, that is $60k to support a project that, for most projects, is not sustainable and likely doesn't support their livelihood. We could reduce the %, but given the size of the matching pool, I am not sure that would be the right direction to go if we want to fund what matters to the community. We could make the eligibility requirements stricter, but I suspect this would not make the community happy. In general, it isn't easy running a grants program, and in the end, you can never make everyone happy.

[quote="FractalVisions, post:56, topic:16553"]
I am curious :eyes:… Where is the proof of impact threads :thread: with onchain data :bar_chart: for the biggest projects that have received the most funds in the BETA round?
[/quote]

Impact is clearly an area where all of web3 is struggling. It is something we are always discussing internally, and something I am passionate about and working on outside of gitcoin. We hope to see more review and impact tools emerge to track impact on-chain. For now, I would suggest that of the top 5 projects in the community round, I think there is likely significant on-chain activity to back up the work they are doing, but I leave it to you to do that research.

-------------------------

cyrusclarke | 2023-09-28 18:44:07 UTC | #59

I appreciate the thinking and work around cluster matching. But seeing the length of replies to this idea brings me to 2 very succinct points:

1. Isn't this adding even more to the issue of "over-engineering the solution to the problem" which Gitcoin seems to be obsessed with i.e. preventing Sybil vs. just encouraging more donations/votes?

2. Why wasn't this communicated before the round so that voters knew the rules of the game? Retroactively doing just punishes projects who encouraged people to get out and vote/donate for them. 

I **would not vote to ratify** this result mostly based on point 2 and request further deliberation.
I would also encourage more discussion about where attention is placed based on 1.

-------------------------

FractalVisions | 2023-09-28 20:39:57 UTC | #60

[quote="jon-spark-eco, post:58, topic:16553"]
On the flip side, it is difficult for QF mechanisms not to become popularity contests, and I think that may be what you are pointing at.
[/quote]

Jon thanks 🙏 for taking your time to respond to us today. Yes. I think it’s a positive sign to see the space that was held today with security experts who were joining together. 
That was a great example of how the energy can be laser focused on initiatives and security is definitely number one.

[quote="jon-spark-eco, post:58, topic:16553"]
We could make the eligibility requirements stricter, but I suspect this would not make the community happy. In general, it isn’t easy running a grants program, and in the end, you can never make everyone happy.
[/quote]

On this note 📝 I definitely 💯 understand what you mean & respect everyone for their hard work during or in between rounds. It’s truly amazing. I assume the passport is constantly being improved upon for matching fund eligibility slowly over the course of the future.

Has there been any proposals from projects that have offered to pay back a portion of their donations into the matching pools at the end of the round if they received “x” amount of funding in round ? This is an idea that I think would be interesting to experiment with if builders who are heavily committed to the grants stack are also willing to turn around and help spread the distribution more evenly.

Dashboards for analytics research are great a way for anyone to learn more about blockchain in general. We will do our best to add value to the GTC ecosystem by doing our own research.

-------------------------

PouPou | 2023-09-28 20:49:02 UTC | #61

Thank you, @umarkhaneth, and the entire team for your efforts and for providing clarity. Would it be possible for you to add a column indicating the initial number of votes?
From my rapid calculations based on the OSS round data, it appears that 58% of the base votes were not considered. How much does this compare to previous rounds?

[quote="ale.k, post:19, topic:16553"]
Overall though- I support ratifying these results. In line with expectations and past rounds’ sybil-rates.
[/quote]

In my opinion, these numbers are staggering. Additionally, considering that 73% didn't surpass the passport score, how many total voters and votes does this account for? It seems that fewer than a third of the votes are getting counted. Is that an accurate estimation? Does this also represent a third of the unique voters?

I also have some questions regarding the cluster QF. Do you consolidate votes from a single donor before the clustering process? For instance, if a donor votes multiple times within a round, are all their donations counted as one? If this isn't the case, I imagine the results might vary, especially as voters familiarize themselves with new projects and subsequently vote for them during the round.

-------------------------

robioreefeco | 2023-09-28 20:53:26 UTC | #62

Thank you for all the people and contributors that made this possible!!

-------------------------

Yoshi420 | 2023-09-29 04:09:09 UTC | #63

I love the concept but have multiple concerns. Does the product have any potential risk for labeling people on the spectrum as bots? We tend to be more robotic in our movements. 
Does the product have issues with IPhone? I’ve struggled to get it to work, it won’t recognize my social media, or Google I’m not getting credit for much of any activity on the chain. It’s disappointing.

-------------------------

ASTRO-HSU | 2023-09-29 07:13:53 UTC | #64

I wanted to share an insightful piece written by [Blocktrend](https://blocktrend.substack.com/), a leading blockchain media in Taiwan. The article provides a detailed analysis of  Gitcoin Grants 18 results. Originally intended for Blocktrend's readers, the piece offers a comprehensive review of how Gitcoin identifies "voting troops" and addresses the issue of "wrongful accusations".

The article delves into the specifics of the Quadratic Funding mechanism, the concept of community importance, and the challenges faced by projects in attracting diverse supporters. It also highlights the potential of Gitcoin Grants as a sustainable funding model for small to medium-sized projects in the blockchain space.

We believe that this article could serve as a valuable resource for the Gitcoin community as well. Here is the link to the article:

* English version: [Analysis of GG18 Results: How Gitcoin Identifies Voting Troops and Wrongly Accuses the Innocent](https://blocktrendintl.substack.com/p/gg18-results-analysis)
* Chinese version: [平方募資結果分析：Gitcoin 如何揪出投票部隊、錯殺無辜](https://blocktrend.substack.com/p/565)


Feel free to share it with others who might find it informative. We appreciate your time and look forward to hearing your thoughts on the piece.

-------------------------

charlesfreeborn | 2023-09-29 09:08:54 UTC | #65

What next? Are we proceeding with payouts or ratification of the results?

-------------------------

giri | 2023-09-29 13:19:49 UTC | #66

I'm flagging this :black_flag:because few things are not proper in a certain manner :slightly_smiling_face:

-------------------------

giri | 2023-09-29 13:22:25 UTC | #67

The word "SYBIL" is enough to bring create a panic sensation in market :grin:

-------------------------

FractalVisions | 2023-09-29 15:51:16 UTC | #68

“ For example, EtherScore, which is ranked first in the table, had an original voter count of 2,941, but the final number of eligible voters was only 643. In other words, nearly 80% of the voters for this project were determined to be voting troops. ”


![IMG_3644|690x230](upload://hbtSdKPGy9ce4Pew4zAiXlv27sf.png)

I don’t think 💭 they understand how this works because the 643 voters were the ones with matching funds. There were not any voters who were removed. They simply didn’t have their Gitcoin passport score higher than 20 points for the matching funds.

So the article is misleading.

-------------------------

FractalVisions | 2023-09-29 15:59:09 UTC | #69

The vote 🗳️ will conclude in a few days which is already overwhelmingly for the approval of funds being distributed. That will take place afterwards.

-------------------------

ASTRO-HSU | 2023-09-29 16:22:25 UTC | #70

![截圖 2023-09-29 下午11.56.28|690x280](upload://sJN953SmvDU01ufh4UYnoS0TyKn.png)

Thank you for your response and clarification. I understand your concern, but I believe there may be some misunderstanding. The diagram provided explains the difference between Base Voters and Eligible Voters. 

As mentioned, voters must have a Gitcoin passport score higher than 20 and donation over $1 to become Base Voters. These Base Voters then undergo additional screening to ensure they are not sybils, bots, or duplicate accounts before becoming Eligible Voters. The final results are determined through simpleQF and cluster-matching QF separately.

-------------------------

FractalVisions | 2023-09-29 16:32:19 UTC | #71

You are correct ✅.. I am wrong 😑…

I see the difference here on the original contributions which makes more sense. It’s just not included in the article and that’s why I felt it was misleading.

![IMG_3645|230x500](upload://mauYid7YihinFHheYMyr4zKVZjk.jpeg)

-------------------------

littertoken | 2023-09-29 17:23:55 UTC | #72

Thanks Jon for the response & explanation. We'll try to do better next round.

-------------------------

realsahabia | 2023-10-08 00:27:56 UTC | #73

Hello everyone. 

Thanks to @umarkhaneth and the team for your efforts.

On behalf of our team at **DeFi Africa**, I would like to know when the payouts will be carried out? 

We had a planned to host a workshop in this October, which has already been announced and registration is full. We're just left with some few days away to the workshop and funds are yet to be released. 

I would like to know when it's planned to release so we can  reschedule our event.

-------------------------

umarkhaneth | 2023-10-08 08:41:03 UTC | #74

Hey @realsahabia thanks for your message and you have my apologies for this taking so long that you're considering rescheduling your event. Payouts should go out early this upcoming week. Could you dm me on telegram and we can figure out how to support your event in the meantime? I'm umarkhaneth on there as well.

-------------------------

adminrefimedellin | 2023-10-09 10:43:36 UTC | #75

Thanks to all Gitcoin Team for the hardwrok. :herb:

-------------------------

TiarnachEsq | 2023-10-09 13:14:33 UTC | #76

[quote="jon-spark-eco, post:58, topic:16553"]
To this point, the round has a 6% matching cap, so a project can’t earn more than 6% of the pie or $15k.
[/quote]

There are five projects in the climate round that received more than $15,000 - why has the matching cap not been enforced in these instances?

-------------------------

umarkhaneth | 2023-10-09 13:26:52 UTC | #77

[quote="TiarnachEsq, post:76, topic:16553"]
There are five projects in the climate round that received more than $15,000 - why has the matching cap not been enforced in these instances?
[/quote]
The matching cap is different by round. Climate has a 10% cap on the $250,000 in the main climate pool for a $25k cap


[quote="umarkhaneth, post:1, topic:16553"]
## Core Rounds:

|Round|Matching Pool|Matching Cap|
| --- | --- | --- |
|Open Source Software|$300,000.00|5%|
|Ethereum Infrastructure|$200,000.00 or 106.9 ETH|10%|
|Web3 Community & Education|$250,000.00|6%|
|Climate|$350,000.00|10%|
[/quote]

-------------------------

realsahabia | 2023-10-10 07:22:30 UTC | #78

Hey @umarkhaneth thanks for your response. Please find my message on your telegram inbox.

-------------------------

umarkhaneth | 2023-10-10 18:17:52 UTC | #79

All core rounds have now been paid out!! 🎉🎉🎉  (with the exception of shell's 100k side pool for climate)

If you have any questions please reach out on telegram: umarkhaneth

-------------------------

pcfreak30 | 2023-10-11 02:42:51 UTC | #80

I was told somewhere that the gitcoin rule of no VC funding was revoked. I am not sure if that is true, but I think it is a mistake if so.

My view as a small project is that I feel much of Gitcoin is a popularity contest that benefits established projects way more than early ones? For me at-least, I would need to rank in the top 50, probably the top 30 minimum to survive if I did not have community funding from my primary tribe.

While I cannot confirm it, I also feel like some of the projects in the top ranks may not fully qualify, or may be violating the VC funding, aka double-dipping.

I checked some and one that stands out is `DefiLab.xyz` whos domain points to a for sale page...

Another that is a name that stands out is `4EVERLAND` who IIRC has made VC biz dev deals and operates as a .Inc (meaning they have big fish investors more cases then not).

Some of these names I recognize as legit projects providing a valuable service like `revoke.cash`.

I feel a lot more vetting is needed on funding so that projects that actually need the money get it. I am fortunate to have a community funding source outside of Gitcoin, but if I did not, frankly the work I'm doing for the space would never exist and I would be working as a consultant again. But I do hope as *my* project grows, I can rely on Gitcoin more than getting a few hundred USD a quarter.

Unrelated to who gets what, some general product feedback is that the on/off ramps need solving. All the L2 stuff just fragments things and makes it more painful than cGrants ever was such only the most dedicated supporter will go though the BS needed to donate.

The batch donating is a good thing but we need to have a unified means of donating across grant pools, a unified profile for all grants on gitcoin.co, and a frictionless way to go from USD to X crypto to donate, KYC or not.

Overall I echo a lot of the criticism @lefterisjp left on Twitter. Im also glad to see someone helped his project outside Gitcoin :)

Kudos.

-------------------------

FractalVisions | 2023-10-11 03:45:27 UTC | #81

[quote="pcfreak30, post:80, topic:16553"]
I checked some and one that stands out is `DefiLab.xyz` whos domain points to a for sale page…
[/quote]

Can confirm the site goes here.
![IMG_3710|230x500](upload://351LRqctMyXxGlJ1xayYptlalYe.jpeg)

The actual site is here. It doesn’t look like it’s been updated since 2021…

https://defi-lab.xyz/

![IMG_3713|230x500](upload://kWn4bEPtIDWEKXroUlUzXBvlngK.jpeg)

Twitter is unfortunately not as active as one ☝️ might hope.

I only see one post about Gitcoin from the Alpha round so this is definitely a bit suspicious.

![IMG_3715|230x500](upload://x0ChiFb0GA4mjQoPg9p2GBndwgU.jpeg)


![IMG_3712|279x500](upload://zXIvKmm11t3e1TjOEFgCIggxW4i.jpeg)

The one ☝️ thing that does raise a bit of a red flag 🚩 is the number of donations. I can’t tell if these are legitimate donations or not based on their campaign activity on social media.

It’s also very hard to imagine 2370 individual donations being made when we all spent two weeks straight in Gitcoin radio 📻 fighting to get over 100 donations. Maybe we are missing something here but something definitely doesn’t add up.
![IMG_3711|230x500](upload://sIHoJGxl1hwdPcc6QzD1FNNFiX.png)

-------------------------

ZER8 | 2023-10-11 14:25:33 UTC | #82

The results overall look great, I'm personally very happy to see some of my favorite regen projects make it to the top in the Climate round!

-------------------------

RedAce7 | 2023-10-13 13:41:30 UTC | #83

Well done Guys , Looking forward to help the community in upcoming rounds as well .

-------------------------

raybankless | 2023-10-15 02:37:56 UTC | #84

Hello, 
[quote="umarkhaneth, post:31, topic:16553"]
This mechanism disempowers uniform, established monoliths and actually empowers grassroots organizations if they’re made of diverse, different members.
[/quote]
From what i read, as far as gitcoin concerned the top 2 projects that joined this climate round, are uniform, established monoliths. Since they have been slashed enormous percentages, that means the decision of their uniformness and monolithness is made.

and also, from the recent round operator lesson, i learned that 
![Screenshot 2023-10-15 at 03.42.12|690x306, 75%](upload://ou74GMLbIsk5J5gdAIRLblITwFS.png)

Seems like we are also doing suspicious activity.

Projects like us are not accepted to the round by just clicking the "submit" button. There was an election process. Our projects were reviewed by Gitcoin. But now, we are called suspicious monoliths by the same Gitcoin.

Either the language is wrong, or there is a much bigger problem here. Because what gitcoin gave me as an explanation to the %74 percent cut, was that we were either suspicious, or a uniform monolith.

Or our donators donated only to us and no one else. 
[quote="umarkhaneth, post:22, topic:16553"]
Looking at your data, I agree that your matching seems low when comparing your number of voters to the number of voters of projects who receive similar matching. Digging deeper into your data, I see this is because of how identical your voters are. Of your 187 eligible voters, 151 (over 80%) of them supported only Nawonmesh.
[/quote]
What is wrong with they voted only for us? That means our community has moved, they used gitcoin and donated $1 to us, we should not get a cut for that imo. We can not go check who voted for how many projects and find the ones that voted only for us then warn them about "no you can not just vote for us, you have to vote random amounts of $$ to random number of projects or it is fraudulent" 

We should do that before the round. This video is made by greenpill.network, i translated it to Turkish and shared from BanklessDAO Turkish YT. The video explains QF but there is no explanation of Cluster Matching, it just says "which ever project gets more number of people donating to them regardless of the amount of asset they donated, that project will get more from the matching pool". 

https://youtu.be/EjoiCWg9-r4?si=DcCxHDFgAYg_w1K9

That means we should update all our QF content ASAP until GG19, because it is missing the most important part of Gitcoin rounds. Since it caused us, %74 percent, there is nothing more important then knowing how CM works. There is no importance of what QF is for Nawonmesh, because %86 of their funds would have come from Cluster Matching.

We were the slashed side of the CM, how about the gainers?
[quote="umarkhaneth, post:22, topic:16553"]
For example, if enough people from my hometown on Long Island decided we needed to improve our parks and we could quickly each give $1 to a gitcoin grant then we would outvote everyone else to claim a lions share of the matching pool by ourselves.
[/quote]
If you mean you can get %80 percent of the pool by shear numbers, you can't, because there is a cap. I assume you already know about the cap thus by saying lions share you meant the cap.

Then how come Atlantis is eligible for the lions share of $23,876 with average number of backers?

Cluster Matching just got dismissed of QF in my experience.

-------------------------
