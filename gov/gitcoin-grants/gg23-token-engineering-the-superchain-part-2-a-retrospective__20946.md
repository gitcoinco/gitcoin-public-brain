---
id: 20946
title: "[GG23] Token Engineering the Superchain (Part 2): A Retrospective"
slug: gg23-token-engineering-the-superchain-part-2-a-retrospective
category: gitcoin-grants
url: https://gov.gitcoin.co/t/gg23-token-engineering-the-superchain-part-2-a-retrospective/20946
created_at: 2025-06-14T23:17:17.002Z
last_posted_at: 2025-06-14T23:17:17.122Z
posts_count: 1
views: 1077
like_count: 3
---

# [GG23] Token Engineering the Superchain (Part 2): A Retrospective

<https://gov.gitcoin.co/t/gg23-token-engineering-the-superchain-part-2-a-retrospective/20946>
natesuits | 2025-06-15 06:54:01 UTC | #1

# Introduction & Overview:

At the Token Engineering Commons (TEC), we take an iterative approach towards the development of our grants program. We wanted to take a proven mechanism like Gitcoin’s Quadratic Funding and build our development goals to enhance it in two different ways - (1) introduce a new method of anti-sybil resistance while incorporating subject matter expertise into the allocation process, and (2) to develop accountability methods to keep grantees committed to executing on their publicly stated intentions. In our combined GG21 and GG23 Token Engineering the Superchain rounds we executed on these goals through a QF round that was linked to a Retroactive Funding round.

**Goal #1: Expand Subject Matter Expertise (SME) beyond Token Engineering (TE) Credentials in GG21**

The insertion of SME is important because we want to make sure that the signals we are receiving in QF rounds from the support of donors are also aligned with the goals of the grant program and informed by those who have the best perspective on what those goals should be.

In order to incorporate SME, we developed Tunable Quadratic Funding (TQF); a sybil mitigation mechanism that boosts the influence of donors in the round who possess specific onchain signals that are aligned with the goals of the grant program for that specific round. We incorporated TQF into Gitcoins QF Calculator as a feature that can be used by other community rounds in addition to COCM and Passport.

TQF is an incredibly powerful tool that can be customized for any grant program or governance structure by adding and removing specific onchain signals that are relevant to the goals of the grant program and assigning their weight of influence.

In GG21, we facilitated the first phase of our Token Engineering the Superchain grant round, where we put TQF to the test within the Optimism ecosystem by extending OP’s governance infrastructure to influence the allocation of external capital resources. The goal was not only to fund TE projects, but to fund TE projects that were specifically building on the OP Superchain. It served as a method to extend OP’s governance infrastructure (Badgeholders and Delegates) and allow them to influence the allocation of funds through our grant program.

This targeted approach ensures that external capital can flow to projects with strong potential to drive innovation and adoption of token engineering principles while satisfying the needs of the Optimism ecosystem.

In practice, TQF facilitates both initial project selection through quadratic funding rounds and sustained support via retroactive funding rounds, creating a powerful incentive structure for high-impact projects to deliver tangible outcomes. By weighting OP delegate and badgeholder donations more heavily, TQF ensures that funding decisions reflect both technical merit and strategic alignment with Optimism’s vision.

This mechanism has already proven effective, with the GG21 grant round focused on Token Engineering the Superchain, as we achieved substantial engagement from the OP community, supported a group of diverse projects building on OP, and provided funding for practical applications that are used frequently within Optimism governance.

Through this experiment, TEC and Optimism are setting a new standard for community-driven, expertise-aligned capital allocation, helping to build a more decentralized and impact-focused capital allocation mechanism that extends OP’s governance structure beyond the activities of the Token House and Citizen House.

**Goal #2: Keeping grantees accountable to their publicly stated intentions.**

One of the biggest challenges with issuing onchain grants is that it is cumbersome for grant-round operators to facilitate multiple distributions in the form of performance based funding. Additionally, its very difficult to gauge whether or not projects received sufficient funding in the first place to execute on their goals as each project has different prior funding levels, different organizational capacities, and are at different stages in their development. Creating a method for grantees to set their own goals which are aligned with the grant program and incentivizing them to follow through with their intentions becomes a fundamental prerequisite for achieving the outcomes that this public funding seeks to facilitate.

This was the focus of our recent combined grant round (GG21: TQF, GG23: Retro), where we established a Retroactive Funding round as a method for incentivizing projects participating in the initial QF round to execute on their self-declared milestones.

The GG23 Retro Round was open to each project participating in the GG21 QF round. Once the round was completed, we asked each project to create their own milestones that aligned with the purpose of the Grant Round (TE on the OP Superchain) based on their own intentions and the outcomes they thought would be achievable.

Due to the short time period between GG21 and GG22, we decided to not participate in GG22, opting to provide our grantees with sufficient time to accomplish their milestones. Our goals were to reward those who kept moving forward in a good-will attempt to execute on their intentions for the original grant allocation in GG21.

# Projects Participating & Grant Funds Allocated (GG21 & GG23)
&nbsp;

**GG21: Token Engineering the Superchain TQF Round [Part 1] (50k Matching)**


|Grant name|Total Funding (DAI)|
| --- | --- |
|Pairwise: Simplifying Choices, Amplifying Voices|9000.00|
|Inverter Network|8928.09|
|Superchain.Eco Initiatives|8239.55|
|Bonding Curve Research Group (BCRG)|5227.51|
|Token Swaps as a Mechanism for Superchain alignment|4445.47|
|Treegens DAO|3732.94|
|Valueverse Labs|3600.49|
|TPRO Network|3090.28|
|Flow State (Streaming Quadratic Funding)|2963.42|
|GovGraph|2285.61|
|EVMcrispr|2159.55|
|Breadchain Cooperative|1749.53|
|1Hive Gardens|1398.04|
|Change Code: Permissionless Results-Based Fund|930.92|
|Super DCA: The Time-Weighted Average Market Ma…|841.54|
|Simplicity Group|574.94|
|Regen Atlas|501.28|
|Eisodos Multimodal|330.86|

&nbsp;

**GG23: Token Engineering the Superchain Retro Round [Part 2] (40k Distribution)**

|Grant name|Total Funding (DAI)|
| --- | --- |
|Superchain.Eco Initiatives|5,474.53|
|1Hive Gardens|5,354.65|
|Gov Graph|4,795.21|
|Super DCA|4,595.21|
|Flow State (Streaming Quadratic Funding)|4,355.65|
|Valueverse Labs|4,115.89|
|Regen Atlas|4,075.93|
|Token Swaps as a Mechanism for Superchain alignment|3,796.21|
|Breadchain Cooperative|3,436.57|
|Pairwise: Simplifying Choices, Amplifying Voices|0 (DNP)|
|EVMcrispr|0 (DNP)|
|Inverter Network|0 (DNP)|
|Bonding Curve Research Group (BCRG)|0 (DNP)|
|Change Code: Permissionless Results-Based Fund|0 (DNP)|
|Treegens DAO|0 (DNP)|
|Simplicity Group|0 (DNP)|
|TPRO Network|0 (DNP)|
|Eisodos Multimodal|0 (DNP)|

&nbsp;
# GG23 Retro Round Process

**Application Process:** All projects participating in the GG21 QF Round were qualified to participate in the GG23 Retroactive Funding Round.

**KarmaGAP Milestones:** To qualify for the round, projects simply needed to provide a set of finalized milestones within KarmaGAP and verification links to those completed milestones.

**Retroactive Scorecard & Review:** The TEC invited several OP Delegates and Badgeholders to serve alongside known Token Engineers on the GG23 Evaluation Board. In total, we had 10 members on this board who were charged with evaluating each project participating in the GG23 Retro Round. We developed an evaluation scorecard and an evaluation tool that had 12 different evaluation categories.

![Screenshot 2025-06-14 at 2.11.56 PM|690x371](upload://jEwbm8Qg46zyQRZQjzkVtBe5J8Y.png)

Each evaluator was allowed to set their own weights for each of the scoring categories that were broad enough to evaluate the unique milestones provided by each project.  Once the reviewer established their weights, we developed a TEC AI Agent that utilized the informational infrastructure for the combined grant round, and all of the KarmaGAP profiles, online platforms, and public information related to each participating grantee in GG23.  

We asked each evaluator to insert 2 prompts into the AI Agent that defined each of the 12 evaluation categories above and scored them based on our defined parameters.  Examples: 

![Screenshot 2025-06-14 at 2.21.14 PM|690x472](upload://5zZizh5xDghhZkoIH7n2xD4pZ8Q.png)
&nbsp;

![Screenshot 2025-06-14 at 2.27.33 PM|558x500](upload://9gW6BQKXwegaqr3FAd6M4MWEpR1.png)


![Screenshot 2025-06-14 at 2.28.46 PM|690x180](upload://wwFBJGX1v3CX6L8aXl7FDr3ziNv.png)

The AI Agent would produce a CSV ready result that scored each project according to the milestones they established, the verification of those milestones, and the weighted priorities set by each evaluator.  

The purpose of utilizing the AI Agent during the evaluation process was to limit the influence of any type of bias that evaluators may have for one project or another while incorporating the outcome and impact priorities of each evaluator based on the categories provided.  Each evaluation came with a justification statement for why the AI Agent produced the score for each project within each category.  In addition, the AI agent proposed a set of unique strategies that could be utilized to translate those scores into vote allocations as required by the Retro Funding platform on Gitcoin.  

Once the AI produced the scores, it was the responsibility of the evaluators to review the justification statements and the evaluation scorecard and either adjust the score based on their subjective disagreements or notify the board on mistakes made by the AI or other considerations that should be made collectively.  

**Final Votes:** Once the evaluators were done with their scorecards, they were required to insert their votes into the Retro Funding platform on Gitcoin for finalization, and grant distribution.



# Reflections on the Combined Round

The GG21 and GG23 Rounds marked an important evolution in how funding and accountability are structured within the TE Grant Program.  

All projects that participated in the GG21 QF round were automatically qualified for Retroactive Funding. Each grantee was required to submit an initial set of milestones prior to the GG21 round as part of the application process, and once the round was over, had the ability to alter their milestones at will, provided they were in alignment with the goals of the round.  All projects seeking to participate in the GG23 Retro Round were required to post their milestones to KarmaGAP for evaluation.  

The time between GG21 and GG23 was a period of 6 months!  So projects had plenty of time to weigh their decision on a number of issues that included whether or not this was in fact the direction they wanted to take with their project, and if it was, what were realistic milestones they could set to prove their impact?


Even if they failed to ask these questions, or take their QF grant allocation seriously (in alignment with the grant program goals), the time between grant rounds eliminated any type of excuse for not building in alignment or executing toward their stated intentions. There is a financial incentive if you do, but you will risk not qualifying if you don’t.  

As you can see, of the 18 projects who participated in the GG21 QF Round, only 9 applied for the GG23 Retro Funding Round.  Of the 9 projects NOT participating in the round, 6 of them reached out prior to the round to notify us they would not be participating due to changes in priority.  Some had in fact made progress on their projects and milestones but did not focus their impact within the Superchain ecosystem.  One project stated they wouldn’t feel right taking money away from those who actually made an impact in alignment with the Grant Programs goals.  

For us, this was a great outcome.  Six projects who would have loved to be considered for Retro Funding, but opted out because they didn’t feel like they created the impact they set out to accomplish. 

The two round system has clear benefits in this regard, as it keeps those who weren’t accountable for pushing forward the goals of the Grant Round from participating at all. They could attempt to fake it, act like they did it, or come up with abstract impact statements and milestones, but it’s hard to take a project seriously when there is a public record of you participating in a Retro Round with nothing to show for it when you previously stated your intentions publicly.  

This linked round process creates a filter for projects seeking funding and allocates capital toward projects that achieve outcomes aligned with the goals of the grant program, while still allowing for discoverability and early-stage funding through the QF round.  


# Critiques & Improvements for GG23

**Program Focus:** During this combined round, we focused entirely on the OP Superchain which was a shift from previous rounds which focused strictly on Token Engineering projects regardless of where it was being built and for what purpose.  This focus prevented some grantees in GG21 from participating in the Retro Round simply because making an impact on the OP Superchain either wasn’t a priority or the milestones they set for the OP Superchain were not as important compared to other areas of project development they established during that 6 month period.  While the round was great at rewarding projects who achieved their milestones in alignment with the OP Superchain, it was not sufficient enough to incentivize a change in direction or priorities for projects that focused more on the fundamentals of what they were building outside of those desired impacts.

**Milestone Development:** While each grantee was responsible for updating their own milestones, we did not implement a set pattern for review or checking-in with grantees on their milestones status.  Many projects altered their milestones several times prior to their final declaration and verification process.  Having established milestone reviews and deadlines ahead of time could have improved clarity in milestone goals and how projects focus their impact.  This would also allow the TEC to offer more value outside of financial rewards to help projects become more connected with other OP Superchain projects, assist in networking opportunities, etc.  

**Evaluation Process:** The evaluation framework and use of the TEC AI Agent as an internal evaluation tool was a new frontier for us.  While the approach was sufficient in maintaining objectivity for the evaluation, many of the evaluators found the use of the AI agent to be more complicated than evaluating each project individually with their own subjective scoring methods.  Improvements on the process are needed as it requires running the prompts for each grantee individually and takes up more time than desired.

# Next Steps: Ideas for Future Iterations

We plan on continuing the use of the combined QF + Retro Round format as a method to create discoverability and reward completion of grantee milestones.  In future rounds, we may consider having a minimal amount of funding in the matching pool for the QF round and make the Retro Round a much larger reward pool for grantees while incorporating a much more concentrated milestone management process.



# Conclusion
This round has shown that combining Quadratic Funding with Retroactive Funding presents an exciting opportunity for incentivizing long-term, milestone oriented impact. We are committed to refining our approach and ensuring alignment with grantees and our grant program goals.

We look forward to future combined rounds, where we will continue this journey of funding impactful projects and rewarding meaningful outcomes.


&nbsp;
&nbsp;
I want to give a special thanks to all the TEC core team members who made this round possible:
@Moni_boo @0xJade @bear100

-------------------------
