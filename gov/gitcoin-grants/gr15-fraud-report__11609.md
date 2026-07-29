---
id: 11609
title: "GR15 Fraud Report"
slug: gr15-fraud-report
category: gitcoin-grants
url: https://gov.gitcoin.co/t/gr15-fraud-report/11609
created_at: 2022-10-05T16:35:17.112Z
last_posted_at: 2022-11-18T13:05:40.821Z
posts_count: 4
views: 4062
like_count: 10
---

# GR15 Fraud Report

<https://gov.gitcoin.co/t/gr15-fraud-report/11609>
DisruptionJoe | 2022-10-06 00:09:31 UTC | #1

The Fraud Detection & Defense workstream (FDD) aims to minimize the impact of fraud on our community. In this post, we highlight the quantitative data behind GR15 and the qualitative decisions made. We also link to reasoning behind any subjective judgments along with making recommendations to the Grants Operations team and Stewards for new policy revisions to match changing circumstances.

# TL:DR

* Contributor Fraud (Sybil Donations) Prevented
  * Fraud Tax (Squelched) = $285k
    * Contributors = 23% (9,176 / 39,758)
    * Contributions = 33.46% (155,683 / 465267)
    * $ Value of Sybil Donations = 17.5% ($225k / $1.3m)
  * Trust Bonus Analysis & Identity Staking Analysis
    * Deep Dive coming to DAOvibes on 10/19
* Grant Fraud (FDD is responsible for Platform & Main Round Eligibility)
  * New Applications
    * Total Applications = 1150
      * Platform approved = 700
      * Main Round approved = 300
    * Total Disputes = 70
    * Total Appeals = 32
  * Grant Investigations
    * GO Sybil Ring = 33 Grants / 250k $ in total matching
    * Other Disputes = 37 Grants / >250k $ in total matching
    * Over $700k in “FALSE” transactions. These are testnet transactions
      * Is there a reason for them?
  * Main Round Policy Update Recommendations
    * Need clarity on Quid Pro Quo including Discord Roles & SBTs
    * Need clarity on “Has Token” or “NFT sales” as automatic disqualification
      * Surge Women’s group / Lobby3DAO and Pooly NFTs were given exemptions by FDD in judgment of disputes for being public goods
* Other Insights
  * New QF attack vulnerability
  * Sybil Scoring Legos replaced Blockscience SAD model
  * Grant side fraud mitigation

# Contributor Fraud (Sybil Donations)

Sybil defense for Gitcoin consists of prevention, detection & mitigation. Our best possible detection can be used to guide passport development (trust bonus preventative mitigation) in addition to “squelching” (retroactive mitigation). More can be learned about these two techniques in our FDD Review article on “Closing the Gap”.

## Squelching (Reactive Mitigation)

Overall

||GR11|GR12|GR13|GR14|GR15|
| --- | --- | --- | --- | --- | --- |
|Total Sybil Donors Squelched|853|8100|2071|16073|9176|
|Total Donors|16597|27260|16651|44736|39758|
|% of total Donors Squelched|5.14%|29.71%|12.44%|35.93%|23.08%|
|Total Sybil Donations|29300|115000|23,951|167988|155683|
|Total Donations|441644|482293|306898|600869|465267|
|% of donations that are sybil|6.63%|23.84%|7.80%|27.96%|33.46%|
|$ Value of Sybil Donations||$710,139|$68,060|$337,143|$225,380|
|Total $ Value of all Donations|$1,620,800|$3,214,587|$1,462,659|$1,735,349|$1,306,724|
|% of total donation $ from sybil|0.00%|22.09%|4.65%|19.43%|17.25%|

After squelching, we can see a clear pattern in the distribution and histogram of the delta (or change in funding the grants will receive). Here are some key takeaways:

* The vast majority will only see a change of -$6 to $195.
* There are fewer grants which are negatively affected than positively
* A large number of positively impacted grants see substantial change, some are even close to doubling their match amount!

![|306x182](upload://uUElX5cByL1C8Gs2ylaF2vL8lSZ.jpeg)![|293x175](upload://4sQaBxDAVd2KifyMg7kbQlb7ynl.jpeg)

When we look at the grants that lost the most or the least, we can see that only a few grants are impacted for more than $1,000.

* 26 Grants lost > $1,000
* 33 Grants lost $100 > $1,000
* 68 Grants gained > $1,000
* 168 Grans gained $100 > $1,000

This is consistent with the hypothesis that a few bad actors divert funds from many grants.

## Trust Bonus (Proactive Mitigation)

The trust bonus analysis will require a much deeper analysis which we will be presenting at our DAOvibes call on Wednesday, 10/19. Here are some highlights on what will be included:

![|624x351](upload://tTQec3yzneyW13e0ezPOPkhyGAW.jpeg)

# Grant Fraud & Eligibility

FDD’s Grants Intelligence Agency (GIA) squadThe GIA handles all operations & execution of tasks relating to PLATFORM & MAIN ROUND eligibility except for policy. All aspects of the ecosystem and cause rounds belong to the Grants Operations squad.

GIA responsibilities include:

* New grant application assessment for Platform & Main Round eligibility
* Disputes - Re-reviewing grants flagged by the community
* Appeals - Re-reviewing grants denied eligibility and escalating when appropriate
* Policy - Identifying gray areas and novel situations & recommending policy review
* Investigations - Deep dives into suspicious grants to document types of fraud

These responsibilities ensure that grants on the platform are not in violation of codes of conduct, policy, and or set precedents and norms.

When the stewards ratify the round results, they are also approving the sanctions adjudicated by the FDD workstream.

Full transparency to the community* is available at:

* [Grant Approvals](https://www.notion.so/gitcoin/3940c8762a304e8c9630a05418ebd2a1?v=8fd78e98993e4dc29fd40a5b12a9ea75) - When new grant applications are received
* [Grant Disputes](https://www.notion.so/gitcoin/e79f1dd9e5074a1d986ee3f91b12943e?v=74372375b4ba42ebb269be219f2c452d) - When a grant is “flagged” by a user
* [Grant Appeals](https://www.notion.so/gitcoin/5627564cce204a0f8ae5af463873bb3d?v=2510b1a2634b4a0ea24cf2b81241d13a) - When a grant denied eligibility argues an incorrect judgment

*User Actions & Reviews is currently in “open review” allowing for select participation to stewards due to sensitive Personal Identifiable Information (PII) data and potential vulnerability to counter-attacks.

Additional transparency for all flags is provided at [@gitcoindisputes](https://twitter.com/GitcoinDisputes) Twitter.

## ![|317x294](upload://pXu4tDVbR3EG13bepv8KbaThu5u.jpeg)

### Platform Eligibility

**New Grant Applications**: ~1150

**Disputes**: 42 of 48 total disputes were found ineligible for the platform.

**Appeals**: 24 total, 9 denied, 13 approved

**Policy**: A clear understanding that sybil behavior, quid pro quo, and other behaviors not eligible for Main Round inclusion are NOT platform violations. Stricter or better defined policy around OS code or necessity of an MVP may help.

**Investigations**: Streamline approval of grants before the round begins. Ensure brand ownership verification programmatically. Suggestion for GR16: Grant creators that can’t verify twitter on Gitcoin should DM us at GitcoinDisputes directly.

### Main Round Eligibility

**New Grant Applications**: ~300

**Disputes**: 5 of 10 main round grants that were disputed were removed. (Not including the platform disputes which are ineligible for all rounds)

**Appeals**: 12 out of 32 appeals were denied main round

**Policy**: Stricter policy around OS code and MVP is needed. The main round decided to open up the criteria from the previous Ethereum/OSS community rules to allow all the ecosystem and cause round grants to be included. This could present a vulnerability if side rounds do not review grants with the same scrutiny as FDD historically did for the main round. While the technical decoupling of the main round and the platform eligibility offered more options, the decision made by Grants Operations created a main round with wider scope (and vulnerabilities) and removed a Gitcoin Community governed Ethereum & Open Source round.

**Investigations**: We removed over 10 main round grants that all raised maximum matching <$120k

### Cause Round Eligibility

Execution of these reviews was transferred to Grants Operations.

**New Grant Applications**: ~250

**Disputes**: 1 of 5 grants that were disputed were removed

**Appeals**: 1 appeal transferred out of FDD jurisdiction

**Policy**: We need to clearly communicate that cause/ecosystem rounds are not subjected to main round eligibility, but are subject to platform eligibility. There is a tendency for grants in Climate round to also be included in DeSci, while the argument that climate work is also DeSci, we recommend evaluating whether grants should choose which cause round best represents their work. Alternatively, the DeSci round may want to narrow their eligibility from anything tangentially related to science, to groups specifically building the rails for DeSci to function.

**Investigations**: Many grants which were removed were receiving matching from multiple rounds, even hitting caps.

### Ecosystem Round Eligibility

Execution of these reviews was transferred to Grants Operations.

**New Grant Applications**: ~600

**Disputes**: 6 of 27 grants that were disputed were removed

**Appeals**: 1 of 7 grants that appealed were not eligible

**Policy**: We need to clearly communicate that cause/ecosystem rounds are not subjected to main round eligibility, but are subject to platform eligibility. The ecosystem round owners will need to own more of the policy decisions which land in gray areas including disputes and appeals. They are the only ones who can decide how to evolve their community’s policy.

**Investigations**: We investigated and removed multiple grants that received maximum matching from multiple ecosystem rounds.

## Grants Review Metrics
Grants were reviewed by FDD for platform and main round eligibility in a timely manner before and during the round. The total volume of grant applications was larger this season, but more evenly distributed.

We had an average of 60 grants/day during the round and an average of 10 grants per day before the round started. In GR15, we had one person who served as an experienced reviewer that ensured platform and main round eligibility met QA standards. Two experienced reviewers assisted when the new applications were at the highest (see red zones in the chart).

![|624x157](upload://bmoxKL9dWLElvFaOw8Kb0wStD6K.png)
Grants submitted between 24 June and 25 September(after GR14 until the end of GR15)

A birds eye view of the progress in grant reviews:

GR15

* One main reviewer/approver + 2 assistants for platform/main round
* Reviewed over 1150 Grants for platform eligibility
* Resolved over 30 appeals and over 70 disputes
* Appeals/disputes were solved ASAP during the round. At the end of the round FDD + Gops closed all the open disputes.
* Investigations saved over 150k in main round matching + another 100k in side round matching
* Ensured brand ownership verification for over 300 grants
* Started Ethelo Deep Data

## Appeal & Dispute Process Improvement Needs

The most time consuming part of the appeals is accumulating enough FDD votes to gain a clear signal. In the future, we will strive to grow/decentralize the group evaluating appeal requests. GR15 showed us the public will benefit from increased Grantee communication about the appeal process.

The appeal process offered to Grantees has become efficient, credibly neutral and it happens in real time. Appeals are processed as soon as they are submitted. Voting still requires 1-2 days for a total processing time of up to 1 week in the longest cases. We are still researching and evaluating the best way to process appeals based on Novel Situations that will not require a Steward vote.

![|435x251](upload://527N0ZWDH20dYS5w6xYsHdIKQCk.png)

Here are some takeaways that will help us create better and safer rounds overall:

* Mandatory twitter verification eliminates over 30% of bad actors and grants
* Clearer policy will alleviate any double standards and also solve some vulnerabilities caused by eligibility
* Our community is an invaluable resource of intelligence. Appeals/disputes/investigations should be community driven in an optimal protocol future.
* The red team is continuing to evolve their strategies every round

-------------------------

ccerv1 | 2022-10-05 23:16:07 UTC | #2

Thanks so much for the summary @DisruptionJoe !! There's a lot to learn from FDD's experiences in GR15. A few quick thoughts on where the DAO can focus.

- **Have a hard deadline for grant submissions *at least several days before* the start of a round.** As shown in your exhibit, there was a huge influx of grant applications in the final days before the round -- and eligibility decisions were still being made once the round went live. In the short term, creating a hard cutoff can reduce the likelihood that FDD and Grants Ops get bottlenecked in making eligibility decisions and resolving appeals. Once the round starts, these teams have bigger fish to fry. In the longer term, I'd expect both matching round funders and grantees to appreciate knowing who is in their round before it goes live.

- **Encourage communities to come up with credibly neutral eligibility criteria for their rounds.** Imagine an [OSS round](https://twitter.com/LefterisJP/status/1568983643632320512?s=20&t=0C6YpY6LpSm1Um5y1z9PPA) that uses [GitPOAP](https://www.gitpoap.io/) to determine if a project is eligible: eg, the project needs to have at least one core contributor with a GitPOAP from a critical OSS project, like [this one](https://www.gitpoap.io/gp/486). This not only decentralizes eligibility decisions but also gives communities more autonomy to signal the types of contributions they'd like to see more of.

- **Engage the community in creating early warning systems for Sybil attacks.** As [we learned](https://gov.gitcoin.co/t/fileverse-grant-deactivation/11505) in GR15, it is important to identify Sybil attack vectors as early as possible in a round so as to minimize their impact on the QF allocation. In the short run, FDD should spend the first days of a round screening for Sybil attacks and doing exploratory data analysis, so that any suspicious activity around specific grants can be flagged and the grantee can be warned or delisted. In the medium term, I'd like to see the outputs of such analysis made visible to grantees and the wider community so they can self-report and take action. (This could be metrics on the grants/donation page or a separate dashboard.) In the long run, I'd like to see an incentivized community of Sybil defendooors doing the work of FDD and flagging suspicious grants. Like [this contribution](https://gov.gitcoin.co/t/sybil-attacks-on-gitcoin-and-grant-owners/11611) by @Momonosukke .

- **Assume all Sybil detection mechanisms have a half-life.** "Sybil Scoring Legos replaced Blockscience SAD model." This is a really important finding! I believe the ~~end game~~ infinite game of Sybil detection will be a stack of Sybil detection mechanisms, with each mechanism trained to combat a specific attack vector. (Sidenote: Sybil detection doesn't strike me as a neural network problem, as the rules and dimensions of the game are always changing.) @omnianalytics's Sybil Scoring Legos provide a preview of what this can look like: it enabled FDD to input a username and view a handful of independently derived Sybil probability scores. We should work from an assumption that, like SAD, each detection method will become less useful round to round and eventually be fully deprecated. IMO, this just underscores the need to engage the community in the analysis (rather than build up a bench of ML scientists continually churning out new scoring algorithms).

I'm looking forward to the Trust Bonus / Passport / Identity presentation on 10/19, where I expect some of these themes will resurface... the Sybil problem, the Trusted Contributor problem, and the Grant Eligibility problem are all just different flavors of the Identity problem... which is one of [THE problems](https://gov.gitcoin.co/t/passport-is-our-aws/10995) we need to crack to open the gates of a regenerative society :slight_smile: 

![image|690x387](upload://bRYSoai0xaHnNa9kOHe91qVhSAQ.jpeg)

-------------------------

tjayrush | 2022-11-17 20:48:51 UTC | #3

This is an idea that I just thought of now reading the above. I'll drop it here in the hopes that some happy traveller one day stumbles upon it and it becomes useful.

What if, in addition to all the specific measures used to find sibyls, there was the idea of "canneries in the coal mine," that is, projects that are deemed with high certainty to not be sibyls.

If a particular "solution" or "technique" or "system" incorrectly identified even a single "cannery" as sibyl, then back to the drawing board.

In other words, removing real sibyls from the system is as important as keeping known non-sibyls in the system. In both cases, the percentage of good projects is increased.

-------------------------

DisruptionJoe | 2022-11-18 13:06:23 UTC | #4

We actually have this now. Our "Thor" set is a data set with known non-sybil users. This is used for the purpose you describe and/or for regression modeling and other data science techniques. 

During season 16, our specific task or project related to this is to *document the QA process used to ensure the integrity of the Thor (and Loki) data sets.*

-------------------------
