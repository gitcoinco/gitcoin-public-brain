---
id: 11873
title: "[Discussion & Feedback Request] Grants Protocol Alpha Round Eligibility"
slug: discussion-feedback-request-grants-protocol-alpha-round-eligibility
category: gitcoin-grants
url: https://gov.gitcoin.co/t/discussion-feedback-request-grants-protocol-alpha-round-eligibility/11873
created_at: 2022-11-08T00:00:37.539Z
last_posted_at: 2023-01-10T07:53:43.817Z
posts_count: 12
views: 5175
like_count: 50
---

# [Discussion & Feedback Request] Grants Protocol Alpha Round Eligibility

<https://gov.gitcoin.co/t/discussion-feedback-request-grants-protocol-alpha-round-eligibility/11873>
connor | 2022-11-09 00:24:33 UTC | #1

Firstly, I want to say a big thank you to @j9leger and @M0nkeyFl0wer for co-authoring the below, @koday @umarkhaneth for helping with all the analysis, and @nategosselin for helping with all the analysis, and @nategosselin & the GPC team for helping bring these alpha rounds to life.

**TL;DR**

* Governance has approved the decision to sunset cGrants and transition to the Grants Protocol
* GR16 will not happen in December and instead we’ll run an Alpha Round on the protocol in January with the goal of testing the product while supporting established grantees
* The Alpha Round will consist of 3 separate matching pools: Open Source Software, Ethereum Infrastructure, and Climate Solutions
* These rounds will only be open to a subset of existing grantees with a goal to support about 300 projects in total
* We’ve considered many different options for which grantees to include and will invite 40 grantees in the climate round with 10 additional bundled projects, ~250 in the OSS round and ~30 in the Eth Infrastructure round
* We’ve included our analysis of how we came to a decision for the OSS and Eth Infra round structure for those interested and are open to feedback on the criteria we landed on

**Context**

As many of you know, the past few months have been filled with discussions and posts about the upcoming launch of the [Grants Protocol](https://go.gitcoin.co/blog/introduction-to-grants-protocol), the [Future of the Grants program](https://gov.gitcoin.co/t/discussion-series-future-of-the-grants-program/11252), and how the DAO can best enable the [Protocol Flywheel](https://gov.gitcoin.co/t/the-new-grants-protocol-flywheel/11769) to thrive.

After lengthy, productive discussions about [GR16 and the protocol transition](https://gov.gitcoin.co/t/request-for-feedback-proposed-future-for-the-grant-programs-and-gr16-as-we-transition-to-the-protocol/11624), a [new option](https://gov.gitcoin.co/t/request-for-feedback-proposed-future-for-the-grant-programs-and-gr16-as-we-transition-to-the-protocol/11624/42?u=connor) was crafted based on community feedback. The revised proposal replaces GR16 with a streamlined alpha round on the new protocol in January, focused on mission-aligned themes, and with a subset of existing grantees. This ensures core grantees still receive the funding they rely on, while allowing the DAO to focus on the full protocol launch in early Q2 with opportunities to iterate based on user feedback. As of last week the [Snapshot vote](https://snapshot.org/#/gitcoindao.eth/proposal/0xecc9736dc4f9e6eb954b67a0d7301ecbcc48bbd5ad31fbd28f1e74ade500c479) for this option passed almost unanimously; 99.98% in favor! [Bonus - See [Messari’s Governor Note](https://messari.io/report/governor-note-decentralizing-gitcoin) for a consolidated overview of this debate and proposal]

You heard that right - it’s finally time for cGrants (aka centralized grants, the QF platform we all know and love) to be retired, after almost 4 years since it launched. The first QF round on cGrants in February 2019 had a $25k matching pool, which inspired 200 donors to contribute an additional $13k, raising $38k total for Open Source Software. We’re now 15 rounds in and have facilitated $72 million in funding for OSS and public goods. Since the GitcoinDAO was formed, a primary mission has been to create a decentralized and modular Grants Protocol, and we’re finally taking the leap into this next iteration. That said, for grants that are still using cGrants for ongoing one-off donations, you’ll be able to do so for the foreseeable future.

Over the next few months we will focus on running alpha rounds to ensure that we continue to support early-stage builders as we transition to a decentralized, scalable solution that will support many more communities in funding their shared needs. This will include the January Gitcoin Program alpha rounds that we will run in lieu of GR16, smaller test rounds, along with various external rounds with design partners who will launch grants programs of their own to help test the protocol.

The Gitcoin Alpha rounds will be focused on Open Source Software, Ethereum Infrastructure, and Web3 Climate Solutions. We proposed these themes as they are our longest-standing Gitcoin rounds and are at the heart of the mission to fund public goods in our community. We used our [community discussion](https://gov.gitcoin.co/t/request-for-feedback-proposed-future-for-the-grant-programs-and-gr16-as-we-transition-to-the-protocol/11624) and [vote](https://snapshot.org/#/gitcoindao.eth/proposal/0xecc9736dc4f9e6eb954b67a0d7301ecbcc48bbd5ad31fbd28f1e74ade500c479) to help frame these rounds.

For more information on this decision and transition, see the latest blog post - [​​Announcing the decentralized future of Gitcoin Grants](https://go.gitcoin.co/blog/announcing-the-decentralized-future-of-gitcoin-grants).

Now that we’ve reached consensus on the high-level path to launching the protocol, it’s time to plan the specifics of what the Gitcoin Program alpha rounds will encompass.

**Round Structure:**

The governance debate and decision established a few key points:

* The substitute for GR16 will run on the protocol in January with a reduced scope
  * This enables the DAO to focus on purposeful onboarding and gathering user feedback, helping to make the protocol transition and launch a success
* The initial rounds we’ll focus on are Ethereum Infrastructure, Open Source Software, and Climate Solutions
  * Supporting Eth Infra and OSS have been core pillars of the Gitcoin mission and community since day 1
  * Climate Solutions has become the biggest and longest-running Cause Round, spearheading the effort to bring QF out of the Web3 niche. It is also an area where open-source blockchain-based tech is enabling cutting-edge opportunities to address this issue that threatens everyone worldwide
* These initial rounds will only be open to a subset of projects that have participated in previous Gitcoin Grants rounds
  * In recent rounds we’ve received a huge influx of new grant applications - a notable amount of which are fraudulent, Sybil attackers, or simply not a great fit
  * While we don’t mean to exclude legitimate new projects, to mitigate risks while testing our new product features, reducing the application review process to verified existing grants will help us prioritize a successful launch to support the broader community in subsequent rounds

**Determining Round Criteria:**

Participation will only be for a limited subset of existing grants from GR14 and GR15 to facilitate efficient onboarding and testing. Additionally, the three rounds will be independent with separate matching pools, where a grant will only be in allowed into one round (so Eth Infra and Climate projects won’t be able to also join the OSS round). This restriction is temporary, but for the January Alpha Rounds, we want to prioritize including as many unique grants as possible.

In an effort to provide more context on our decision making and the state of the protocol - another reason for the 1 round limit is that each round’s donations and CLR calculations will be fully independent from one another. On cGrants when a project was in multiple rounds concurrently, any donation would earn additional matching from every pool the grant was a part of. In the early protocol rounds this will not be the case; if a grant is in OSS and Infra, a donation can only be made in the context of one round or the other, since each round is a unique smart contract. This means a single donation will only increase matching from one of the two pools; to increase matching from both pools, 2 donations would have to be made, one within each of the 2 round contracts. While we are building the functionality to run “overlapping” or “meta” rounds where donations can earn matching from multiple pools at once, the January rounds will not have this feature.

**Climate Solutions Round Criteria**

The Climate Solutions round will include up to 40 individual blockchain-enabled climate solutions projects. We will also invite a range of grantees to be part of 10 bundles of projects grouped by use case and geographic location. This helps donors easily select areas to support in grants explorer and is a new experiment for how small grants can collaborate with one another to receive funding. These groups will likely be:

1. Renewable Energy financing and decentralized grids
2. Community Engagement (conferences, podcasts, arts, games, etc)
3. Carbon Markets
4. MRV and Oracles
5. Projects focused on Ocean, Forest, and Agriculture
6. Climate Research
7. Climate Advocacy and Activism,
8. Refi South
9. Projects on the African continent
10. Projects in Latin America

We will encourage & work to facilitate eligible Grantees to collaborate on shared projects and/or to set up fund-sharing “drips” to 5 or more Grantees or to one or more of the use-case bundles.

@M0nkeyFl0wer, our Cause Round lead has spent a lot of effort determining how to engage as many community members in the round as well as finding ways to include principles of diversity, equity, and inclusion in all cause round activities. Thoughts and feedback are welcome!

**The Eth Infra and OSS Rounds**

The Eth Infra & OSS rounds, however, will be more curated to limit the scale to a manageable capacity. We want to support as many grantees as possible while making this test successful so we can begin onboarding more rounds and grantees soon after.

After much consideration, we will run the two rounds separately without any grantee overlap (ie. those in the Eth Infra round won’t also be in the OSS round). **Both rounds would include grants that received over $1K total (donations + round-specific match) in GR14 or GR15, or grants that had at least 150 unique donors in GR14 or GR15.** This would include inviting ~30 grantees for the Eth Infra round and ~250 grantees for the OSS round.

We’re including our analysis that helped come to the above criteria below. If our analysis leads you to a different conclusion, we’d love to hear from you so we can consider alternative approaches.

Thanks for reading and we’re looking forward to hearing your thoughts!
__________________________________

**Grant Data Analysis**
The following analysis compares various cases trying to answer the core questions of

* How many grantees would be in each round if we’re keeping our alpha rounds to no more than 300 grantees max
* What is the best objective threshold for inclusion? (by either the amount raised by a grant in prior rounds OR the number of unique donors)

**Grantees in One Round Only:**

If we choose one round per grantee, then we can see how the number of grantees in the OSS and Eth Infra rounds changes as we adjust our thresholds. We haven’t included climate round analysis as the above criteria leads to an inclusive round for all blockchain based climate solution grantees.

We looked at both the amount raised (donations + match) and the number of unique contributors as meaningful metrics to consider (with the caveat that Sybil attacks/airdrop farming is not uncommon). While the amount raised seems like it should receive the most weight, the relative impact of funding can vary widely between grants based on the team size, geographic location, upkeep costs, etc. After reviewing the data shared below in detail, it does not appear that either option will result in a significantly different group of grants but we included both metrics for transparency.

**OSS Only Grantees in GR14/15 by Amount ($) Raised**
(Using crowdfund + main round match)

How many grants are in OSS only and over the $X threshold? (not in Eth Infra or Climate)

||Over $100|Over $250|Over $500|Over $1k|Over $2.5k|Over $5k|
| --- | --- | --- | --- | --- | --- | --- |
|GR15|377|293|220|147|77|43|
|GR14|428|310|235|167|105|69|
|14 OR 15|584|444|341|240|146|90|

![|574x336](upload://mhTa3xKz3TLowePQpNNdZNhJogT.png)

**OSS GR14/15 Unique Contributors**
How many OSS grants had over X unique contributors in GR14 and 15?

||Over 25|Over 50|Over 75|Over 100|Over 150|Over 200|Over 300|
| --- | --- | --- | --- | --- | --- | --- | --- |
|GR15|319|247|206|175|135|112|88|
|GR14|338|261|224|201|171|147|121|
|14 OR 15|461|360|307|271|224|192|154|

![|589x355](upload://h4HfQQtrdbfutZaUiK8fnXyNQcF.png)

**ETH Infra Grant Data Analysis**
How many ETH Infra grants are over $X threshold? (Using Amount Contributed + ETH Infra Match amount)

||Over $100|Over $250|Over $500|Over $1k|Over $2.5k|Over $5k|
| --- | --- | --- | --- | --- | --- | --- |
|GR15|34|33|30|28|25|23|
|GR14|29|28|28|26|20|17|
|14 OR 15|36|34|33|32|27|24|

![|516x311](upload://dwaEJEL72cHaF5hdrBylR8YIXma.png)

How many Eth Infra grants has over X unique contributors in GR 14 or GR15?

||Over 25|Over 50|Over 75|Over 100|Over 150|Over 200|Over 300|
| --- | --- | --- | --- | --- | --- | --- | --- |
|GR15|30|28|26|25|24|23|21|
|GR14|28|26|25|24|19|19|16|
|14 OR 15|34|31|30|28|26|25|23|

![|488x295](upload://645UioQukkRWJOACkyuaP1TotUm.png)

**Grantees in Multiple Rounds:**

How would allowing grantees in multiple rounds affect the outcome? The biggest difference would be the OSS round now includes grants from Eth Infra and Climate, however, the Eth Infra and Climate rounds would not be affected. For the purposes of this analysis, we can take the max-case and assume that all grantees in the Eth Infra and Climate round could be eligible for the OSS round. The likely number will then be a bit smaller than projected below as some Climate grantees would not qualify.

OSS (including Eth Infra and Climate Grantees) Combined Round Analysis:

||Over $100|Over $250|Over $500|Over $1k|Over $2.5k|Over $5k|
| --- | --- | --- | --- | --- | --- | --- |
|GR15|439|354|278|199|109|68|
|GR14|477|356|278|206|132|88|
|14 OR 15|648|506|402|298|184|117|

![|624x377](upload://4N5Sj5DOkWq6pVSLK2xmBPbWwd7.png)

The overall effect on the number of grantees in the OSS round if we allow grantees to be in multiple rounds can be seen in the below table and chart.

||Over $100|Over $250|Over $500|Over $1k|Over $2.5k|Over $5k|
| --- | --- | --- | --- | --- | --- | --- |
|OSS One Round Eligible|584|444|341|240|146|90|
|OSS Multi Round Eligible|648|506|402|298|184|117|
|Difference|64|62|61|58|38|27|

![|624x385](upload://dxv5BXjJRRR8JKKKd0tYFaMUyp2.png "Chart")

Our decision not to go this route is because we didn’t think it fair to include a subset of grantees in multiple rounds while others aren’t able to participate at all. Additionally, grants only in the OSS round would now have greater competition. Finally, with each round independently contained in a unique smart contract, a grant being in multiple rounds at once may not create the best UX until more features are deployed.

**Conclusion**

Thank you for reading this far! Keep in mind this is our analysis based on the data we’ve collected in recent rounds. If you believe we should consider changes to our approach, or have ideas of other areas where we should dig deeper into the data, please let us know. This is our tentative path forward as the round preparation has already begun, however this framework is still malleable. Your feedback is highly appreciated as we move closer to launching the Grants Protocol. Thanks in advance!

-------------------------

tjayrush | 2022-11-08 15:42:33 UTC | #2

This is really excellent. I'm very excited to finally have permissionless, not-rate-limited access to this system. 

I'm imagining that I will no longer have to ask GitCoin APIs for data about what's going on. I can read directly from the smart contracts -- permissionlessly. That's the true import of decentralization -- the ability analyze a system with no dependency on even the developers of the system.

Along those lines, please lean into it:

People on the outside (i.e. not the GitCoin developers) need the addresses of the core smart contracts. That's all we need, we can get the rest of the data from the smart contracts.

But this seems to be the one thing that many projects neglect to provide.

Publish the addresses (perhaps even on the interface) of the core smart contracts. Make them very obvious. Purposefully give people the ability to snoop.

-------------------------

krrisis | 2022-11-08 20:21:55 UTC | #3

Thanks for this great overview Connor & team! 

Very happy to see the biggest focus will be on OSS, bringing us back to our roots. 💪

A quick question while reading through this:

[quote="connor, post:1, topic:11873"]
We will also invite a range of grantees to be part of 10 bundles of projects grouped by use case and geographic location. This helps donors easily select areas to support in grants explorer and is a new experiment for how small grants can collaborate with one another to receive funding.
[/quote]

I think this is a great idea, but will probably trigger most of the questions, as a lot of projects will want to be a part of these bundles, do we already have any more information to share on how this will practically work? How many projects do you envision per bundle? And how can we avoid discussions within bundles about funding splits?

Once again thank you for the deep transparency towards the community in making these tough decisions.

-------------------------

connor | 2022-11-09 00:27:12 UTC | #4

@M0nkeyFl0wer can add more context on the bundles for you! I believe the plan would be to include grants not already in the round (individually) to join a bundle - as a way to include more projects, but keep the total number of grants lower

-------------------------

M0nkeyFl0wer | 2022-11-09 18:08:56 UTC | #5

Hey hey, good question! 

So we will be inviting projects to be part of these bundles and the funding will be split evenly with all participants. We are building on top of the collections that have been created in past round to highlight different climate solutions use cases enabled by blockchain technology as well as breaking projects down by under represented geographic areas (the global south, the african continent and Latin America). 

In terms of how these will be administered there will be a multi-sig set up for each bundle in advance of the round getting underway. We will be sending out invites for deeper discussions with each of the groups of potential grantees in each bundle. 

Our hope is this will provide a way for the vast majority of past grantees in this rapidly growing community to have some skin in the game for the alpha round and in the process keep them engaged and playing a role in helping to shape the future of the protocol and our grants program.

-------------------------

annika | 2022-11-17 19:27:35 UTC | #6

This is great, @connor - love the data-driven approach and think the inclusion criteria are very reasonable. This Alpha round sounds super intentional & clear overall.

Thinking out to post-Alpha round and the broader protocol launch, figured I'd share two things that come to mind upon reading this post for future consideration. To be clear, these are by no means feedback or distractions for 'right now' while you guys are heads down prepping the Alpha round -- just  a couple areas that pop into mind as the future of grants gets further defined.

1. **Longer-Term Eligibility**  - We've talked a lot about eligibility for the old 'Main Round' which probably erred on the side of too inclusive (a lot of not Public Goods stuff and not OSS stuff was ultimately in there), and for other curated rounds which were often on the other end of the spectrum -- too exclusive. The thresholds & frameworks laid out in this post work great for Alpha Rounds, but in the context of the Gitcoin-led program rounds (vs. externally-led protocol rounds) we still have the very big question of "what's in and what's out". I am excited to see how you all are thinking about that (probably in the new year!).

2. **ETH Infra vs. OSS Rounds**  - The venn diagram of grantees in these two rounds was highly overlapping in the past. It will be interesting to see who self-selects into which one in the Alpha round - I imagine it will likely be a function of number of grantees and pool size. e.g., if I am an ETH Infra grantee from the past, assuming equal round size, I'd *far* rather be in the ETH Infra round since I know the pool of 'competing' grants is smaller. I wonder how this will affect QF and how the effect might be handled longer-term.

-------------------------

connor | 2022-11-30 06:18:28 UTC | #7

[quote="annika, post:6, topic:11873"]
* **Longer-Term Eligibility** - We’ve talked a lot about eligibility for the old ‘Main Round’ which probably erred on the side of too inclusive (a lot of not Public Goods stuff and not OSS stuff was ultimately in there), and for other curated rounds which were often on the other end of the spectrum – too exclusive. The thresholds & frameworks laid out in this post work great for Alpha Rounds, but in the context of the Gitcoin-led program rounds (vs. externally-led protocol rounds) we still have the very big question of “what’s in and what’s out”. I am excited to see how you all are thinking about that (probably in the new year!).
[/quote]

We are working hard on the Gitcoin Program structure, including how we will engage governance more, feature up-and-coming rounds, and offer funding opportunities for these rounds the community can help distribute. More to come on this soon!

Also safe to say there will not be one overall "main round", however a few different larger rounds that encompass most existing projects from cGrants. OSS? Infra? Other thematic/cause rounds? TBD - the DAO will help decide :slight_smile: 

[quote="annika, post:6, topic:11873"]
1. **ETH Infra vs. OSS Rounds** - The venn diagram of grantees in these two rounds was highly overlapping in the past. It will be interesting to see who self-selects into which one in the Alpha round - I imagine it will likely be a function of number of grantees and pool size. e.g., if I am an ETH Infra grantee from the past, assuming equal round size, I’d *far* rather be in the ETH Infra round since I know the pool of ‘competing’ grants is smaller. I wonder how this will affect QF and how the effect might be handled longer-term.
[/quote]

Yes - in this case since we will not yet allow grants to be in multiple rounds at once (for this first Alpha test), the Eth Infra grants will be invited to join the Infra round but not the OSS round. We believe this will be advantageous to all Infra grants as the ratio of projects to matching pool will be in their favor.

This is also partially due to the protocol currently not supporting "Meta-round" functionality (this is the name I'm trying to make catch on for what we used to call "jet fuel QF") which I hope we can add soon. Quoting the explanation below, but essentially, I don't believe it will be a good UX with projects in multiple rounds when users will have to choose to donate in the context of one round or the other.

[quote="connor, post:1, topic:11873"]
In an effort to provide more context on our decision making and the state of the protocol - another reason for the 1 round limit is that each round’s donations and CLR calculations will be fully independent from one another. On cGrants when a project was in multiple rounds concurrently, any donation would earn additional matching from every pool the grant was a part of. In the early protocol rounds this will not be the case; if a grant is in OSS and Infra, a donation can only be made in the context of one round or the other, since each round is a unique smart contract. This means a single donation will only increase matching from one of the two pools; to increase matching from both pools, 2 donations would have to be made, one within each of the 2 round contracts. While we are building the functionality to run “overlapping” or “meta” rounds where donations can earn matching from multiple pools at once, the January rounds will not have this feature.
[/quote]

-------------------------

ccerv1 | 2022-12-21 04:54:34 UTC | #8

I am excited for the upcoming Alpha Rounds and especially that Gitcoin is going back to its roots with a focus on support for Eth Infra and OSS!

I had some thoughts on eligibility for Eth Infra and OSS, which I've been discussing with @koday and @M0nkeyFl0wer, and would like to share here.

First, let me say that I'm supportive of the initial criteria that Connor proposes below, which ensure that each grant is only eligible for only one round and does some filtering at the tail end of projects:

[quote="connor, post:1, topic:11873"]
**The Eth Infra and OSS Rounds**

The Eth Infra & OSS rounds, however, will be more curated to limit the scale to a manageable capacity. We want to support as many grantees as possible while making this test successful so we can begin onboarding more rounds and grantees soon after.

After much consideration, we will run the two rounds separately without any grantee overlap (ie. those in the Eth Infra round won’t also be in the OSS round). **Both rounds would include grants that received over $1K total (donations + round-specific match) in GR14 or GR15, or grants that had at least 150 unique donors in GR14 or GR15.** This would include inviting ~30 grantees for the Eth Infra round and ~250 grantees for the OSS round.

We’re including our analysis that helped come to the above criteria below. If our analysis leads you to a different conclusion, we’d love to hear from you so we can consider alternative approaches.
[/quote]

Second, I would like to propose some added eligibility criteria related:
1. The project should have a public Github repo; AND 
2. There being some "recent" activity in that repo (since the last round).

These criteria feel particularly relevant for the OSS round -- it's kinda hard to make the case that you are working on OSS if there's no open source software to show for it! Plus, don't we want to give special recognitions to projects that have been buidling steadily through the bear?

I wrote a script that looks at each project and analyzes its Github activity. (I also manually went through all projects that didn't have a Github listed in their profile and tried to find one on their website or grant application.)

Out of `251` shortlisted OSS projects with more than $1000 in funding, here are the results as of Dec 20:
- With commits in last 15 days:     90
- Last 30 days:     100
- Last 60 days:     124
- Last 90 days      128
- Last 180 days    153
- Ever: 180

This also means there are 71 projects with either no Github or that returned a 404 error.

**My proposal would be to limit eligibility to OSS projects that have some developer activity within the last 30 days -- in effect, 100 of the 251 shortlisted projects.**

Note: if we apply the same criteria for ETH Infra projects, then 28/32 have at least one commit in the last 30 days.

We should kick the tires on the methodology (and double check the findings), but here's my quick analysis of the types of projects that would no longer be eligible for the OSS alpha round if the DAO opts for this type of screening criteria:
- Projects that were previously active but have become inactive since GR14/15
- Worthy projects, but ones that aren't really OSS because they are more closely allied with other cause or ecosystem rounds, such as Community, Loot, DEI, Education, etc.
- Dubious projects that in retrospect look like Sybils or opportunists

Curious for feedback on the approach and happy to share my findings in detail with anyone who's interested.

-------------------------

koday | 2022-12-22 23:19:29 UTC | #9

[quote="ccerv1, post:8, topic:11873"]
My proposal would be to limit eligibility to OSS projects that have some developer activity within the last 30 days – in effect, 100 of the 251 shortlisted projects.
[/quote]

Thank you so much for this analysis Carl! 

I think these are super important metrics and I really like the suggestion of pruning the eligibility list down to the 100 projects in the OSS round and 28 in the ETH Infra round that have had provable OSS development activity within the last 30 days. This will leave us with a very solid group of grants for the Alpha rounds, ensuring we are allocating funds to the most active and engaged OSS projects. I've floated this by the grant ops team to get some more input - thanks again for sharing!

-------------------------

vegayp | 2023-01-05 04:39:19 UTC | #10

Hello there!

Thanks for putting up all this information.

I just wanted to follow up this post, and curious to know if there is an specific date for this to start, and secondly, if the option to submit candidate for this alpha of the Grants Protocol is closed to discussion. 

I think for many new open sources projects and more on the context of bear market, Gitcoin becomes a reliable source of continuity, and I was wondering if that was an option: to submit a new grant for this round. 

Thanks

-------------------------

griff | 2023-01-07 18:11:24 UTC | #11

In general its very hard to find which grants are eligible.

Is that already announced somewhere?

-------------------------

connor | 2023-01-10 07:53:43 UTC | #12

Thanks for the detailed analysis here! Very helpful.

We've done a pass of the grants in OSS and removed any that are very clearly not OSS or not legit. We've left some in that don't have public Githubs associated with their old Gitcoin grant, however, we're making it very clear that although these projects are **invited to apply**, they are not guaranteed approval unless they meet additional round criteria (like being active and OSS). 

We sent the first round of emails to Alpha Round grantees invited to apply last Friday.

The eligibility criteria for all 3 rounds and the program as a whole can be found here:
https://docs.google.com/document/d/1I4U3RA-q9ZW_Mtlz-EiFtj4YZTkPEwebQSKbEZlCfdY/edit?usp=sharing

We'd love community feedback on these eligibility rules and plan to change and iterate them after these initial test rounds. They are a starting point for community consensus.

We also anticipate only a % of all invited grantees to apply and from there only a % of applications to be approved.

[quote="vegayp, post:10, topic:11873"]
I just wanted to follow up this post, and curious to know if there is an specific date for this to start, and secondly, if the option to submit candidate for this alpha of the Grants Protocol is closed to discussion.
[/quote]

@vegayp unfortunately this round will only be open to existing grantees. Given the stage of the protocol,  we are not yet ready to open the floodgates to a big number of applications, and need to beef up Sybil and fraud resistance. That said, more and larger rounds are on the horizon! Thanks for your patience.

The round will officially begin Jan 17th.

[quote="griff, post:11, topic:11873, full:true"]
In general its very hard to find which grants are eligible.

Is that already announced somewhere?
[/quote]

@griff great point! the final list of grants invited to the OSS and Infra rounds can be found here:
https://docs.google.com/spreadsheets/d/1dD6NeofEKvSMMEXmqjU8dtDqS_pfEdiBpCcBpqIan5A/edit?usp=sharing

@koday will have a more detailed gov post going out soon with more details on the eligibility and list of grants soon!

Thanks all. Excited to kick off this round next week!

-------------------------
