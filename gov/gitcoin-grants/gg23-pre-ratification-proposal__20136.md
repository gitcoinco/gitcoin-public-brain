---
id: 20136
title: "GG23 Pre-Ratification Proposal"
slug: gg23-pre-ratification-proposal
category: gitcoin-grants
url: https://gov.gitcoin.co/t/gg23-pre-ratification-proposal/20136
created_at: 2025-03-11T19:49:48.106Z
last_posted_at: 2025-04-19T15:26:32.847Z
posts_count: 15
views: 4038
like_count: 40
---

# GG23 Pre-Ratification Proposal

<https://gov.gitcoin.co/t/gg23-pre-ratification-proposal/20136>
MathildaDV | 2025-03-25 23:30:54 UTC | #1

## GG23 Pre-Ratification Proposal

We propose to set the matching funds for GG23 as follows: **$1.348M** total from the Gitcoin.eth multisig. This proposal is to pre-ratify the allocation of funds to expedite the process and ensure a smooth and efficient round execution.

After the post-round review, we will post the round results on the governance forum, allowing the community one week for discussion and feedback before payouts are made.

## Proposed Matching Fund Allocation

The proposed matching funds of $1.2M will be distributed across the following OSS Program Rounds:

### Quadratic Funding

* Web3 Infrastructure Round: $200k (matching cap: 10%)
* dApps & Apps: $200k (matching cap: 5%)
* Developer Tooling & Libraries: $200k (matching cap: 10%)

#### GG23 Sybil Analysis and Matching Calculation Strategy
In GG20, we introduced a two-pronged sybil analysis strategy, outlined in detail [in this post.](https://gov.gitcoin.co/t/our-sybil-resistance-strategy-for-gg20/18524) It has shown to be incredibly effective as a strong strategy in our Quadratic Funding rounds. We will continue to drive forward with this strategy for GG23, finalizing each of the above rounds using the calculator that uses the approach of combining Passport's Model Based Detection and COCM.

**TL;DR:** 
**Passport's MBD:** 
This system analyzes the on-chain history of addresses and compares it to the historical data of known human and sybil addresses. Based on this comparison, the model assigns each address a score ranging from 0 to 100, where a score closer to 0 indicates a higher likelihood of the address being a sybil, and a score closer to 100 suggests a higher probability of the address belonging to a genuine human user.

**COCM:**
COCM takes Quadratic Funding (QF) to the next level by tackling its biggest challenge—manipulation through fake accounts and coordinated groups. By analyzing how connected donors are, COCM ensures that projects with genuine, diverse community support get the most matching funds. This method not only promotes fairness but also reflects the true values of the community, giving round operators more accurate insights into what their network really supports. [Read this blog post](https://www.gitcoin.co/blog/leveling-the-field-how-connection-oriented-cluster-matching-strengthens-quadratic-funding) for more in-depth information.

*We are exploring potential updates to Passport's engagement with GG23, which we will post on the forum if we go ahead with it.*

Calculations occur directly after the round has been completed, posted to the forum in roughly a week after donations end. The results will be posted to the forum and open for comments for a week.

### Retro Funding

$600k towards a curated round of 30 top OSS projects.

More details on the OSS Program eligibility can be found [here](https://gov.gitcoin.co/t/gg23-oss-program-eligibility-criteria/20072).

The Retro Funding round for GG23 was designed to support high-impact, mature projects based on their historical contributions to Gitcoin Grants and OSS.

For this round, a curated selection of 30 projects was identified using a force-ranked Elo rating system. This ranking was based on matching amounts received across at least 3 OSS rounds between GG18 and GG22. The goal was to recognize projects with sustained impact and strong community support over time.

This is a metrics-based round, so once the voting has been concluded, we will work closely with Open Source Observer to finalize the results, equally posting these to the forum for community input before conducting payouts.


### Community Rounds

The proposed matching funds of $130k will be distributed across the [selected Community Rounds](https://gov.gitcoin.co/t/gg23-community-rounds-announced/20127).

### Experimentation

We are equally requesting an additional $18k for a [GTC Utility experiment](https://gov.gitcoin.co/t/gtc-utility-experiment-for-gg23/20044).

### Current Matching Pool Status

The Matching Pool is heavily denominated in ETH, which has experienced significant volatility over the past year. We are actively working with Avantgarde to improve financial sustainability while managing market impacts.

Moving forward, our strategy includes increasing our stablecoin allocation to reduce volatility, generate revenue on idle assets, and maintain upside potential through strategic ETH exposure, all while ensuring we can meet our dollar-denominated spending commitments.

**Proposal for Community Vote**
We request the community to vote on the following options:

* Yes, approve the pre-ratified matching fund amounts from the multisig for GG23, totaling **$1.348M**.
* No, do not approve.
* No, follow the traditional process of ratification after the round.
* Abstain

Please share your thoughts and vote in the comments below.

*Thank you for your continued support and participation in Gitcoin Grants governance.*

-------------------------

owocki | 2025-03-12 16:05:18 UTC | #2

Copying these comments from @umarkhaneth on the [GG22 pre-ratification](https://gov.gitcoin.co/t/proposal-gg22-pre-ratification/19501/11).

[quote="umarkhaneth, post:12, topic:19501, full:true"]
In the future, I think it would be amazing if:

* in addition to ratifying the matching pool size gitcoin ratifies the process for calculating the results (e.g everyone agrees to the rules: COCM + Passport, or QF + Allowlist, or hypotheticaloption 3)
* that calculation process is completely onchain and has no offchain components
* there is an easy way for funders who see the ratified process and projects in the round to add to the matching pool

this increases trust in the system, removes centralization points, and could result in more allo GMV
[/quote]

I happen to agree with the above!

But I support this proposal regardless.

-------------------------

ivanmolto | 2025-03-14 08:03:52 UTC | #3

I endorse this pre-ratification proposal for GG23. 
And I would also appreciate a proposal about the process for calculating the results.

-------------------------

wasabi | 2025-03-17 22:58:43 UTC | #4

I'm in support for pre-ratification of the process and I would also echo @ivanmolto, the ratification vote should include the QF Sybil Strategy for GG23 which is COCM + Retro Round mechanics (metrics criteria for selection of the 30 OSS Projects)

[quote="MathildaDV, post:1, topic:20072"]
#### How we’re quantifying mature builders:

* The list is based on grantees participating in OSS rounds in GG18, GG19, GG20, and GG22, with criteria applied to participation in more than two rounds at a minimum.
* The grantees are force-ranked on their Elo Rating - a score based on their GMV normalized for differences across round sizes and competition.
* To exclude projects that have not been recently active, the list filters out grantees that have less than one commit a week over the last 6 months (or less than 25 commits over 6 months).
[/quote]

-------------------------

SEEDGov | 2025-03-18 20:09:54 UTC | #5

We support the pre-ratification proposal for GG23 since its allocation of matching funds seems reasonable to have a successful execution round. The breakdown looks pretty solid, and the balance between the traditional Quadratic Funding rounds and the newer Retro Funding approach seems also accurate.

However, we tend to share the concerns raised by @owocki and @umarkhaneth about the calculation process. For future rounds, we believe it would be good to include in the pre-ratification proposal not just the matching pool size but also the complete process for calculating the results. In this sense, we support the idea of moving towards a fully on-chain calculation process without off-chain components, alongside creating easier pathways for funders to contribute to the matching pool once they see the ratified process and projects.

We believe that with these minor tweaks, everyone can have better visibility into the grant distribution process. Despite these suggestions, we vote to support the pre-ratified matching fund amounts for GG23.

-------------------------

MathildaDV | 2025-03-18 23:46:06 UTC | #6

Thank you for your comments and I appreciate @ivanmolto @wasabi and @SEEDGov echoing this sentiment. I have updated the post to reflect our calculation strategy as well as how we're quantifying the Retro Funding round.

-------------------------

Sov | 2025-03-19 02:22:02 UTC | #7

I support the proposal but agree with the past recommendations of @umarkhaneth and believe establishing these guidelines will add further clarity and streamline the process moving forward.

-------------------------

ccerv1 | 2025-03-19 11:43:14 UTC | #8

Support the proposal and agree with other comments about ratifying the "rules of the game" at the same time

-------------------------

meglister | 2025-03-19 13:09:37 UTC | #9

To echo others, I'm in support of the proposal and ratifying methdology for post-round analysis. Might be good to include a challenge mechanism for the latter, but that feels like an optimization vs gating factor!

-------------------------

Tane | 2025-03-19 14:12:19 UTC | #10

We appreciate the thoughtful proposal and have several points we'd like to clarify and provide feedback on.

Regarding OSS Program Rounds,
- Could you please provide additional details on the Elo Rating mentioned in the [GG23 OSS Program Eligibility Criteria](https://gov.gitcoin.co/t/gg23-oss-program-eligibility-criteria/20072)? Specifically, we would love to know what metrics contribute to this score and how exactly these metrics reflect the impact of previously funded projects. Given that the Retro Round offers a valuable opportunity to measure the real impact and success of past projects, we believe clear understanding and transparency about this rating system is essential.
- For the dApps & Apps category, we note that projects within this category may typically have greater potential for generating financial returns compared to other categories, making them more attractive for venture capital funding. Therefore, could you elaborate on the justification for maintaining similar grant funding levels in this category relative to others?
- We find the funding allocation for Web3 Infrastructure and Developer Tooling & Libraries to be appropriate based on historical context and performance.

As for the Community Rounds, [we have already evaluated them before](https://gov.gitcoin.co/t/gg23-community-rounds-announced), and we keep supporting them.

We also agree with the direction of exploring and validating the utility of GTC tokens through experimentation and fully support pursuing this approach. However, while we support moving forward with the experiment, we have some concerns regarding the design and its effectiveness, such as the fact that the current proposal may heavily rely on the Gitcoin DAO’s existing resources, potentially limiting its scalability or sustainability given the current Gitcoin DAO's financial status. We feel further discussion and deeper research will be needed to address these concerns.

-------------------------

PGov | 2025-03-19 14:46:31 UTC | #11

This is a comprehensive and well-thought-out proposal. We are particularly impressed by the clear structure and thorough attention to details, especially regarding budget allocation and community engagement plans.

The emphasis on transparency and accountability through periodic reporting is appreciated and should be replicated across to build trust within the community. Appreciate the team involving diverse stakeholders early in the planning process.

Overall, we fully support this proposal moving forward to ratification and am excited to see its positive impact on the Gitcoin ecosystem. Great work to all involved!

-------------------------

MathildaDV | 2025-03-25 23:30:03 UTC | #12

Thank you to everyone for your valuable input. Please see https://gov.gitcoin.co/t/gitcoin-grants-23-setup-evaluation-process/20208 for an outline of the process and due diligence we will follow. We will ensure that we include this in each pre-ratification process moving forward to ensure further transparency and enhancement of our processes! 

[quote="Tane, post:10, topic:20136"]
Could you please provide additional details on the Elo Rating mentioned in the [GG23 OSS Program Eligibility Criteria ](https://gov.gitcoin.co/t/gg23-oss-program-eligibility-criteria/20072)? Specifically, we would love to know what metrics contribute to this score and how exactly these metrics reflect the impact of previously funded projects. Given that the Retro Round offers a valuable opportunity to measure the real impact and success of past projects, we believe clear understanding and transparency about this rating system is essential.
[/quote]

More in-depth information on this will be posted on Thursday by our partners for GG23, Open Source Observer! 

[quote="Tane, post:10, topic:20136"]
For the dApps & Apps category, we note that projects within this category may typically have greater potential for generating financial returns compared to other categories, making them more attractive for venture capital funding. Therefore, could you elaborate on the justification for maintaining similar grant funding levels in this category relative to others?
[/quote]
Thank you for bringing this to the surface! As outlined in the process post I just shared above, the matching cap for this round is always lower compared to the rest of the rounds to ensure fairer funding distribution. Also, due to a lot of large established projects entering into the Retro Round in GG23, we believe it will even out well. But of course we may further adjust in GG24.

[quote="Tane, post:10, topic:20136"]
However, while we support moving forward with the experiment, we have some concerns regarding the design and its effectiveness, such as the fact that the current proposal may heavily rely on the Gitcoin DAO’s existing resources, potentially limiting its scalability or sustainability given the current Gitcoin DAO’s financial status.
[/quote]

I will let @gnomadic weigh in here!

-------------------------

MathildaDV | 2025-03-26 14:11:01 UTC | #13

This proposal is now live on [Snapshot](https://snapshot.box/#/s:gitcoindao.eth/proposal/0x143291bab99a740eba64c18101a6203bd2d9c81bbcdef1b4c8cbc9b6a5973007).

-------------------------

Tane | 2025-04-02 04:38:44 UTC | #14

We voted **for** the proposal.

Regarding the Community Rounds and the GTC Utility experiment, as per our previous comments, we see no outstanding issues.
https://gov.gitcoin.co/t/gg23-pre-ratification-proposal/20136/10

For the OSS Quadratic Funding rounds, we acknowledge that appropriate modification has been made on the dApps & Apps category, specifically limiting the matching cap to 5%.

Concerning the Retroactive Funding metrics, we recognize that important ecosystem indicators are covered to a reasonable extent. 
https://gov.gitcoin.co/t/gg23-how-were-powering-retroactive-funding-metrics-that-matter/20216
However, we believe it would be beneficial to measure aspects closer to actual outcomes in the future – for example, (purely as an illustration) considering metrics like GitHub repository stars for the tooling category. We are keen to contribute to developing these aspects further.

-------------------------

ehsan68bad | 2025-04-19 15:26:32 UTC | #15

GM financial services are available from the same thing about

-------------------------
