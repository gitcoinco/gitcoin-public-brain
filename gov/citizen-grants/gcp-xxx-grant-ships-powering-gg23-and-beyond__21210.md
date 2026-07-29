---
id: 21210
title: "[GCP - XXX] Grant Ships - Powering GG23 and Beyond"
slug: gcp-xxx-grant-ships-powering-gg23-and-beyond
category: citizen-grants
url: https://gov.gitcoin.co/t/gcp-xxx-grant-ships-powering-gg23-and-beyond/21210
created_at: 2025-06-23T19:07:26.004Z
last_posted_at: 2025-07-21T15:36:55.195Z
posts_count: 10
views: 1816
like_count: 43
---

# [GCP - XXX] Grant Ships - Powering GG23 and Beyond

<https://gov.gitcoin.co/t/gcp-xxx-grant-ships-powering-gg23-and-beyond/21210>
UI369 | 2025-06-23 19:12:35 UTC | #1

## Proposal Title

Grant Ships - Powering GG23 and Beyond

## Proposal Description

> *A high-level overview of the proposal’s substance.*
> *Please include:*
> * Short summary of the proposal*
> * Impacted stakeholders & expected outcome*

---

### Who we are
DAO Masons is a full-service governance development shop for DAOs, specializing in core governance workflow design and implementation of supporting technology.

Our flagship product, [Grant Ships](https://rules.grantships.fun), is a gamified "evolutionary grants framework". It is designed to discover and advance best practices, promote transparency and provide accountability within grants programs.

See our [whitepaper](https://rules.grantships.fun/tech/whitepaper.html) and [pilot retrospective](https://rules.grantships.fun/pilotretro.pdf) for more information.

### Proposal Overview

In late Q3 2024, Gitcoin staff approached us and asked us to develop a custom implementation of Grant Ships for their Gitcoin Grants 23 Community Rounds. This integration would combine the battle-tested strategies of Gitcoin's community round program with the proven Grant Ships evolutionary mechanism to streamline program onboarding, selection and evaluation. We worked closely with Mathilda to define the requirements.

This proposal outlines the scope of work delivered, and the value provided to the Gitcoin ecosystem and plans for future development.

### The GG23 Implementation

A Grant Ships round includes 3 stages:  Onboarding, Performance and Assessment.  This build focused on stages 1 and 3, with stage 2 handled by the typical Gitcoin community round framework. 

#### Stage 1: Onboarding

The Onboarding stage is where participant programs (in this case, GG23 Community Rounds) are selected to become Ships. Top performers from previous rounds are automatically onboarded and receive boosts to amplify their impact in the following round. 

A key challenge in past GG rounds was the significant time and effort required to collect, organize, and fairly assess community round applications. Previously, applications were posted on forums, leaving assessors to individually review each submission without structured guidance.

For GG23, we transformed the existing Gitcoin Community Round application template from a Google document into a multi-page form submission tool. This streamlined system allows applicants to complete their submissions through a simple step-by-step process, with results displayed publicly and an option for community feedback.

We also developed and launched a novel Hats protocol NFT-gated, rubric-based voting system that enables Gitcoin's elected representatives to serve as judges in evaluating community round applicants across multiple criteria. These Hats NFTs can be transferred by Gitcoin when new representatives are selected, ensuring the system remains reusable.

The system allows each judge to provide detailed point-by-point assessments and numerical ratings for every section of each application. These numerical ratings are summed to create a public leaderboard where top applications rise to prominence. This mechanism was successfully implemented to onboard and evaluate community round applicants for GG23. 

The app is live at [https://gg23.grantships.com/ships
](https://gg23.grantships.com/ships)

#### Stage 2: Performance

The top six rated community rounds from Stage 1 became “Ships” and received $21,000 in matching funds. The 6 Ships ran their rounds on their own using a variety of approaches with grants.gitcoin.co serving as the dashboard. 

There was no new technical implementation for this stage.

#### Stage 3: Assessment
The Assessment phase involves community rating and ranking of Ships to determine which advance to the next round. A key challenge in previous community rounds has been helping participants understand the different programs and effectively signal which ones should continue in future iterations.

To address this challenge, we developed an AI-assisted voting tool for the post-GG23 assessment. The tool was trained on program summaries and key metrics including donations received and matching funds provided. Available to GTC holders with 100+ tokens, it allows voters to indicate their priorities using a 1-5 scale across various criteria such as "novel mechanisms are important" and "total unique donations received is important." Users can also provide subjective input through an open text field. Based on these preferences, the tool generates a recommended voting distribution with explanations and links to complete round reports for voters seeking additional details.

This mechanism enables voters with limited context to quickly identify high-performing programs that align with their values. Votes are logged, tallied, and used to rank Ships according to the total votes received. 

Top performers receive a "boost" to amplify their programs in subsequent rounds. For GG23, the Gitcoin team selected automatic entry to GG24 as the boost for the top three community rounds. In future rounds, additional funding or other added resources could also be provided to top proven performers to further amplify successful programs.

GG23 vote results can be seen at [https://gg23.grantships.com/vote
](https://gg23.grantships.com/vote)

#### Impacted Stakeholders

* GG Community Round applicants - streamlined and public application/evaluation process.
* Judges - streamlined and public rubric-based evaluation tooling
* Gitcoin staff - streamlined administrative processes for program management
* GTC Holders - incentivized to hold GTC above a certain threshold, enabling participation in Ship evaluations.

## Motivation

> Why you are submitting the proposal

Our aim is to create a community-curated system for "funding what matters." Grant Ships is designed to surface and amplify programs that effectively raise and distribute funds, deliver genuine user impact, and solve core problems. This approach enables more refined practices in domain selection, program selection, and assessment.

Grant Ships' evolutionary methodology aligns perfectly with Gitcoin's iterative grant-round structure. When Gitcoin invited us to implement Grant Ships for the GG23 community rounds, we recognized an exciting opportunity to contribute our expertise and demonstrate the mechanism's value within Gitcoin's ecosystem.

This implementation allows us to contribute our focus on clean user experience, smooth workflows, and evolutionary competitive mechanisms. We believe our contribution will be a vital component of the ecosystem's continued development.

## Conflicts
> Any conflicts of actual or anticipated conflicts of interest that you (as an individual, group, or entity) may have concerning the proposal

Grant Ships and other DAO Masons projects participate in Gitcoin Grants rounds and plan to continue doing so. Implementing Grant Ships as Gitcoin's governance layer may increase our visibility among round leaders, potentially creating perceptions that engaging with us offers advantages. While we have no direct influence over outcomes, we acknowledge this potential conflict and commit to transparent management of any perceived advantages.

## Why
> Why the Citizen Grants Program should adopt the proposal

### Benefits and Value Delivered

Grant Ships streamlines and standardizes the community round application and review process, significantly reducing administrative workload for Gitcoin staff while providing a consistent user experience for applicants.

The system creates powerful progressive feedback loops for the Gitcoin Grants program by integrating insights from community votes, judge and panel reviews, AI-powered rubric analysis, and direct metric feedback. Both the application and assessment systems can be iteratively improved across multiple grant rounds to better serve the Gitcoin community as it transitions to Gitcoin 3.0.

Grant Ships also adds utility to the GTC token. In this initial implementation, token holders can signal their preferences on community round performance to influence future Gitcoin Grants rounds.

The platform is designed for reusability and enables expansion for future needs. It could be deployed as-is for GG24, and with anticipated changes for Gitcoin 3.0 beginning with GG24, the existing foundation allows new features to be built more quickly and cost-effectively.

### Compensation Request

Gitcoin staff requested that our team create this custom Grant Ships implementation for GG23. At the time, we were informed that compensation would be available through the Citizens Retro Program. Since that program has been discontinued, we are requesting retroactive compensation for the work performed and value delivered.

## Specifications

> Scope of activities (description of the work breakdown involved in the proposal)

The Grant Ships for Gitcoin build was implemented across five phases:

* System Design
* Product Design
* UX/UI Design
* Contract Customization
* UI Implementation

Each phase is detailed in the [Technical Inventory](https://docs.google.com/document/d/1-g_iayGItvY2nuClj8A6WFZQIdw8_BoPvAkGeL6J290/edit?usp=sharing) document and summarized below.

### System Design Phase

Beginning in September 2024, we collaborated with Mathilda and her team to address a set of key questions. The [early planning document](https://docs.google.com/document/d/16pcS-tOWHhSxQM7HkkkRPTXUcx8vDMoT_YhpTkSsGNo/edit?tab=t.0#heading=h.mbo3so9si0l4) provides additional context for this phase.

### High Level Goals
Through this collaborative process, seven high-level goals emerged:

1. **Streamline the Process** - make applications and evaluations simple and straightforward
2. **Accelerate the Timeline** - reduce time requirements across all stages
3. **Clarity and Transparency** - ensure decision-making processes are visible to all participants
4. **Enable Decentralized Evolution** - support the continuous improvement of grants programs over time
5. **Rubric-based Voting** - provide judges with tools to evaluate applications using preset criteria
6. **Integrated Experience** - create a comprehensive platform for the entire process
7. **AI-powered Voting** - help voters with limited context make informed decisions

### Product Design Phase

The Grant Ships process is summarized pretty well in this tweet:

###
![|458x147](upload://tpkzvLiQfMIPhOxLMIQamUqYeFd.png)

The Gitcoin implementation used this underlying “game loop” and required customized interfaces for their unique use case.

A Grant Ships funding round can be considered in 3 phases — Onboarding, Performance, and Assessment. Each phase has a design space within it that we can tailor for an ecosystem’s specific needs and goals.

![|454x255](upload://vILRk9NVFtm6VZAbJzlrrTgHrj9.jpeg)

*Cyclical: These phases continually cycle, with outcomes from each phase shaping the starting conditions of the next.*

### UX/UI Design Phase

This application includes multiple user workflows. These began from conversations with Mathilda and her team and were scoped into screen flows in Figma then translated to frontend and contract code over the course of several months.

[Early requirements document](https://docs.google.com/document/d/1W8XggyGEmEfdTAdfl-Zp487qafIi9CerWaSZpCmmHAU/edit?tab=t.0#heading=h.6pxklsvon6h1)

#### Primary workflows

All screens and workflows can be viewed in the [design figma](https://www.figma.com/design/PWYZ4nK1gKOek4zAjXxiK0/GITCOIN?node-id=0-1&p=f&t=N9IgmL3mStr5CUrW-0).

**Onboarding Phase Workflows** 

* User creates a new application (includes edit and public comment)
  * Multi-page application w/links and profile image
  * [original provided application](https://docs.google.com/document/d/1nNxOuInLseavEXgoYvM3Rw76wJW0nuil-IxFIItC4OI/edit?tab=t.0) -> [video walkthrough of early implementation](https://vimeo.com/1052391465?share=copy)
  * User optionally edits application
* Community members optionally comment on applications
* Judges (Hats NFT Holders) assess each application using novel rubric-based onchain voting tool
  * Guided ‘stepper’ tool to walk judges through applicant evaluation
  * [Provided rubric](https://docs.google.com/document/d/1oGaP9LKBY6iqOSoc6RA8uo0CdBmzELs9J_5E4cZtJ7M/edit?tab=t.0#heading=h.5kev3fqmxyro)
* Applications leaderboard ranks judge-rated applications
  * Shows all judge scoring and identifies top 6 applicants


**Performance Phase Workflows**
* Community Rounds implement their grants programs as normal using grants.gitcoin.co
  * This season was the first "multi-mechanism" season so many programs were hosted offsite and linked from the gitcoin site
* After GG23 donations closed, Community Rounds submit a portfolio report to Grant Ships team for voters to consider in the Assessment phase
* Portfolio report is summarized and used as training data for AI tool in Assessment Phase

**Assessment Phase Workflows**

* Participant signs in with their wallet
* Participant clicks a button to initiate eligibility determination (Did this wallet have 100 GTC on L1 at program launch date?)
* GTC voter provides their personal preferences on various key aspects of GG programs, rated on a scale from 1 to 5
* GTC voter optionally provides freeform text on what they believe makes a successful grant program
* GTC Voter submits their preferences to the AI service
* GTC Voter preferences are processed by AI into a vote recommendation with a pre-filled vote spread, splitting a possibly 100 points across the 6 Ships
* GTC Voter can tweak and modify recommended votes by moving slider bars
* GTC Voter submits vote
* Application applies GTC Voter's vote to the total
* Application displays aggregate community vote results and individual votes



### Contract Customization Phase

The Grant Ships for GG23 build required contract customization for Chews rubric voting, Hats integration for permissions and voting modules for the public vote.

See [Technical Inventory](https://docs.google.com/document/d/1-g_iayGItvY2nuClj8A6WFZQIdw8_BoPvAkGeL6J290/edit?tab=t.0#heading=h.m7oah2kfze2k) for more detail including links to repositories with all applicable code. 

### UI Implementation Phase

The Grant Ships for GG23 UI was built using React and the Mantine components library. Our focus was on "simplicity at all costs". 

See [Figma Slides](https://www.figma.com/design/PWYZ4nK1gKOek4zAjXxiK0/GITCOIN?node-id=0-1&p=f&t=N9IgmL3mStr5CUrW-0) & [Live site](https://gg23.grantships.com)

## Implementation 

For the Gitcoin design, we focused on the Onboarding and Assessment phases, with the Performance phase handled by the existing Gitcoin Grants platform.



### Deliverables
> Deliverables and artifacts (outputs expected from the proposal)

### Onboarding Features

The initial round's Onboarding workflow for selecting Ships was implemented with the following features:

#### Judge Management System

* Judges (elected outside the Grant Ships platform) received Hats NFTs granting special permissions within the app
* Hats NFTs can be reassigned by the "Top Hat NFT" holder, making the system reusable and capture-resistant
* Future versions can integrate the election process directly into Grant Ships if desired

#### Application Process

* Community Round applicants completed application forms within the app ([Application Form](https://gg23.grantships.com/submit-application))
* Applications are displayed publicly with options for public comments ([Application List](https://gg23.grantships.com/applications),
[Application View w/comments in timeline](https://gg23.grantships.com/view-draft/0xd8c6a64b1287b9dd17f9305f087998a380e0d466720d8fcc72510ce3a75bd7d2-0))
* Applicants can edit their submissions after initial submission ([Application View Page w/edit in timeline](https://gg23.grantships.com/view-draft/0x559f71a3559444c0e12205b095cbecd784199ab4caa271fcddf67b293318eb0f-1))
* All applications include a comprehensive timeline of key events (submission, edits, comments, reviews) ([Application View Page w/Judge votes in timeline](https://gg23.grantships.com/view-draft/0xd18608a33ecfd6b9c08a6c8fd99fd934199dff54ae53515e159b195b2cce770c-0))

#### Evaluation System

* Judges used a custom rubric-based voting mechanism to rate and rank each applicant ([Sample Rubric Vote Result](https://gg23.grantships.com/review/vote-0x559f71a3559444c0e12205b095cbecd784199ab4caa271fcddf67b293318eb0f-0x3FB19771947072629C8EEE7995a2eF23B72d4C8A))
* Application ratings from all judges are summed to determine Ship leaderboard positions ([Ship Leaderboard & Judge Rubric Results](https://gg23.grantships.com/ships))
* The leaderboard displays current rankings and designates the top 6 applicants advancing to the next phase

### Performance Features

The Performance phase utilized Gitcoin's existing grants framework:

* Performance data is self-reported by community round staff and presented during the Assessment phase

### Assessment Features

The Assessment workflow includes these key components:

#### Data Presentation

* Portfolios and metrics from the Performance phase are presented within the Grant Ships app ([Ship page w/links to full reports & metrics](https://gg23.grantships.com/ship/0x559f71a3559444c0e12205b095cbecd784199ab4caa271fcddf67b293318eb0f))
* Ship data is provided by each team and imported by the Grant Ships development team

#### Voting Infrastructure

* A voting whitelist is generated using Merkle Tree cryptography for any GTC holder above the threshold (100 GTC) on L1, enabling voting on L2 contracts
* This complex operation required new Chews Protocol modules and offline scripts for whitelist generation

#### AI-Powered Voting

* Novel AI voting workflow that queries users for their preferences and intelligently prepopulates their votes ([Vote results and voter reviews](https://gg23.grantships.com/vote), [Video Walkthrough of AI voting feature](https://www.youtube.com/watch?v=w2kuK4E3n78))
* Top 3 Ships receive automatic entry to GG24

The [Technical Inventory](https://docs.google.com/document/d/1-g_iayGItvY2nuClj8A6WFZQIdw8_BoPvAkGeL6J290/edit?usp=sharing)  provides comprehensive implementation details for all system components.

#### Repositories
These are the repositories that contain the code for the Gitcoin/Grant Ships build. 



[Grant Ships Gitcoin](https://github.com/DAOmasons/grantships-gitcoin) - Front end React application (204 commits w/first commit Jan 6)
[Sayeth](https://github.com/DAOmasons/sayeth/commits/main/) - Messaging protocol for flexible onchain storage (20 commits)
[Ask Haus Envio](https://github.com/DAOmasons/ask-haus-envio) - Indexer platform for onchain voting (34 project commits since Dec)
[Chews Protocol](https://github.com/DAOmasons/stem-voting/tree/main) - Previously “Stem Protocol”, multipurpose voting framework (50 project commits)

See [Technical Inventory: Contracts](https://docs.google.com/document/d/1-g_iayGItvY2nuClj8A6WFZQIdw8_BoPvAkGeL6J290/edit?tab=t.0#bookmark=id.8wgveedme9pc) for more specifics on contract code created for this project.



## Roadmap and Milestones

> How the proposal would be implemented. If applicable, please include:

#### Development Timeline 
  * August - First Meeting: August 28th
  * September - November: Requirements meetings, internal design work
    * Most screens and workflows are laid out in Figma at this point
  * December - Finalize designs, begin application development
  * January - March: Continue development, first client demos, client feedback & refinement
  * May-June: AI Voting feature - questionnaire for voters asking them for their preferences in #### Timeline & Tweets

#### Launch Timeline
Feb 12: Grant Ships announced
[https://x.com/gitcoin/status/1889822947495567810](https://x.com/gitcoin/status/1889822947495567810)

Mar 7: Judge Rubric Vote announcement
[https://x.com/gitcoin/status/1898065287729012868](https://x.com/gitcoin/status/1898065287729012868)

Mar 17: Top 6 Ships announced
[https://x.com/gitcoin/status/1909653349768561064](https://x.com/gitcoin/status/1909653349768561064)

Apr 2: GG23 open for donations
[https://x.com/gitcoin/status/1907415280474530164](https://x.com/gitcoin/status/1907415280474530164)

Apr 16: GG23 donations close
[https://x.com/gitcoin/status/1912666366202769912](https://x.com/gitcoin/status/1912666366202769912)

May 22: Community Vote goes live
[https://x.com/grantships/status/1925613205977800986
](https://x.com/grantships/status/1925613205977800986)

June 3: Community Vote results announced
[https://x.com/grantships/status/1930036840700227896
](https://x.com/grantships/status/1930036840700227896)

#### Plan for communication and education to the community
  * Telegram help channel to answer questions
  * Grant Ships crew available to talk at select Gitcoin Twitter spaces
  * One (1) forum post per GG round from Grant Ships to give an overview and status update on current stage of development

## Benefits - Point out the core benefits of the proposal implementation

> Mention the amount requested. Proposals should demonstrate how they support at least one essential intent, which includes fostering community engagement, enhancing the network's effects, and ensuring the financial sustainability of the ecosystem.

### Grant Ships fosters community engagement through:

* A streamlined application process, reducing friction and insider knowledge required.
* Creating a clear pathway for participation, reducing uncertainty, friction and confusion for all community members
* Allowing community members to give feedback on Community Rounds through comments during the application process and through votes after the rounds complete.
* Creating a sense of continuity and history by providing a storehouse of records for past GG events
* Revealing the judging process and opening it to review and comment by the community
* Eliminating "back room decisions" for Community Round selections, creating a sense of fairness which encourages engagement
* Encouraging community members to signal their preferences on what constitutes a successful grants program (during the voting pocess), and logging those reflections in public for further review
* Directly incorporating community vote signal into results that propagate into future rounds in a transparent, accessible way
* A gamified model that creates a sense of reward and fun


### Grant Ships enhances the network’s effects by:

* Facilitating consistent, iterative assessment of Community Rounds performance
* Utilizing progressive feedback loops, resulting in improvement of Community Round performance
* Visibility and accountability will improve Community Round performance over time, each of which will provide improved network effects
* Providing a reusable application process for future rounds, creating consistency and historical records

### Grant Ships assists with financial sustainability of the ecosystem by:

* Reducing time and attention required for staff and volunteers to administer GG programs
* Providing additional utility for GTC tokens
* Reducing cost to implement this system again with minimal configuration changes for future GG rounds
* Providing accountability and transparency in grants programs, which aligns with fiscal responsibility
* Creating better record keeping for grant program results, providing learning material for the community, likely resulting in better financial decisions and improved fundraising in the future
*Allowing for expansions and integrations with anticipated changes for Gitcoin 3.0 to be built more quickly and at a reduced rate.

## Drawbacks
> Highlight any drawbacks to implementing the proposal

**Less Flexibility** - The existing process for Community Round applications using the Gitcoin forums is more flexible and freeform than a standalone app with stronger rails on the user experience. Adjusting workflow in an app is more work than doing the same with an editable forum post.

**Upfront Costs** – there is an upfront cost to implementation – continuing to use the forums and internal administrative processes may be cheaper in the short term.

**Dependence on external vendors** – changes to the service will likely require the assistance of the DAO Masons team through future iterations. The code will be open source and you could conceivably fork it if needed.

## Budget Overview
>How the funding amount was determined and how it will be allocated

> Mention the amount requested. Outline a clear allocation strategy, specifying how funds will be distributed across various project components to ensure efficient resource use and the achievement of project objectives.

### Compensation Framework

At project initiation, compensation was planned through the established Citizens Retro program. When that program was discontinued mid-development, the alternative approach became submitting a GCP proposal.

We tracked time spent directly on this project during the approximately six-month development period. The breakdown below shows these hours with corresponding fair market rates for this type of work. Our funding request represents a significant discount from the full market value, reflecting both our commitment to supporting the Gitcoin ecosystem and accommodation of budgetary considerations discussed with the Gitcoin team.

#### Project Effort

* **Total**: 860 hours team-wide across 6 months (excludes requirements gathering process)
* **Team Breakdown**:
  * **Jord** (Product & Engineering, System Design): 640 hours – System architecture, contracts, front-end and indexer implementation
  * **Sun** (Designer): 140 hours – UX/UI design
  * **Matt** (Operations/System Design): 80 hours – System architecture, Gitcoin collaboration, documentation

#### Fair Market Valuation

* **U.S. Market Rates**:
  * Product & Engineering: $125/hour (mid-to-high range of $100–$150/hour, up to $200+ for complex Web3 development)
  * Designer: $100/hour (includes Web3 UX premium)
  * Operations: $50/hour
  * System Design: $110/hour (governance workflow expertise)
* **Market Value Calculation**:
  * Product & Engineering (Jord): 640 hours × $125/hour = $80,000
  * Designer (Sun): 140 hours × $100/hour = $14,000
  * Operations (Matt): 60 hours × $50/hour = $3,000
  * System Design (Matt & Jord): 20 hours × $110/hour = $2,200
  * **Total Market Value**: $99,200

#### Funding Request

**Total: $40,000**

* This represents approximately 40% of fair market value for the scope and complexity of work delivered
* The request amount reflects our commitment to supporting Gitcoin's mission and accommodates current budgetary considerations

#### Project Summary

* **Duration**: 6 months of development (860 hours)
* **Deliverable**: Live platform at gg23.grantships.com, successfully deployed for GG23 Community Rounds with integrated blockchain governance tools

## Measures of success and KPIs
> Attributes to help the grants council measure progress and impact
> 
> This may include achieving project milestones, the quality and quantity of outputs compared to planned outputs, and the degree of achievement of the outcome(s). Other qualitative measures may include the novelty of approaches, the potential for scaling, user satisfaction

### **Quantitative**

With [Goodhart’s Law](https://en.wikipedia.org/wiki/Goodhart%27s_law) in mind, these values and others can be tracked over time to note improvement.

#### This round:

* Number of applications processed: (13)
* Number of judge votes registered: (55)
* GTC Votes registered: (39)

#### Over multiple rounds

* Key metrics progress
  * Donations Received: $66,645.37
  * Additional Funds Raised: $279,500
  * Total donations made: 5985
  * Projects registered: 178

#### Individual Ship Metrics

**Donations Received:**

* Regen Coordination Global: $10818.98
* Web3 for Universities: $4609.86
* Regen Rio de Janeiro: $1302.02
* Token Engineering the Superchain Retro Round: $0
* GoodDollar Builders Program: $24014.51
* Gitcoin Grants Garden: $25900

**Additional Funds Raised**

* Regen Coordination Global: $96000
* Web3 for Universities: $33000
* Regen Rio de Janeiro: $25000
* Token Engineering the Superchain Retro Round: $40000
* GoodDollar Builders Program: $51000
* Gitcoin Grants Garden: $34500

**Total Donations made:**

* Regen Coordination Global: 2368
* Web3 for Universities: 1973
* Regen Rio de Janeiro: 564
* Token Engineering the Superchain Retro Round: 0
* GoodDollar Builders Program: 1047
* Gitcoin Grants Garden: 33

**Projects Registered:**

* Regen Coordination Global: 50
* Web3 for Universities: 50
* Regen Rio de Janeiro: 21
* Token Engineering the Superchain Retro Round: 9
* GoodDollar Builders Program: 25
* Gitcoin Grants Garden: 23

### Qualitative

* Comprehensive GG23 [application process feedback](http://applicant/Judge/Voter%20feedback)
  * “GrantShips UI/UX was intuitive and made participation straightforward”
  * “The GrantShips platform added transparency to the process.”
* Time and energy saved by Gitcoin staff due to a streamlined solution providing “governance compression”
* Reduction in governance fatigue due to clear UX and easeful participation pipelines for community round applicants, judge reviews and community feedback voting - eliminate need for forum-based application process.
* A pathway toward a decentralized governance solution for managing community rounds.
* Adaptability to support DDA and Gitcoin 3.0
* Iterative improvement on community round quality & metrics
* Outcomes produced by supported projects

## Non-Financial Requirements - List any other resources or support needed from Gitcoin to accomplish the objectives

> Don't forget to tell us exactly what you need from the Gitcoin team to make your project successful. Whether it's resources, information, or anything else, being upfront about your needs helps us work together smoothly and successfully gets us all to the finish line.

Apart from thought partnership and insights on community particulars, these were the main deliverables:
* Details on application form and process
* Judge rubric
* List of all judges for permission NFTs
* Marketing and promotion
* assessment reward decisions

## Future Rounds: GG24 and Beyond

From the outset of the Gitcoin and Grant Ships collaboration, there has been mutual interest in providing services for future rounds. Given recent decisions regarding Gitcoin 3.0 and the commitment to a Dedicated Domain Allocation strategy, we're prepared to adapt and support these rounds in whatever configuration emerges. This build is designed for adaptability, with much of the foundational work remaining reusable should Gitcoin choose Grant Ships for future GG program iterations.

We plan to generate a comprehensive retrospective document capturing lessons learned from GG23 and are currently in discussions with Gitcoin staff to assess future round requirements. The Grant Ships model can be adapted to support domain allocation frameworks, additional rubric-based decision pathways, and more sophisticated assessment systems as needs evolve.

We recognize that our participation in future rounds will depend on alignment with Gitcoin's evolving needs and strategic direction. We remain committed to understanding the ecosystem's requirements and providing thoughtful proposals and designs as opportunities arise.

## Thank you!
Thank you for your consideration and we look forward to answering your questions and discussing details of this proposal!

#### Contact Information

To reach out to our team directly:

* **Discord**: https://discord.gg/2SYby64NBp
* **Telegram**:  https://t.me/grantships
* **Schedule a Meeting**: https://calendly.com/daomasons/30min

-------------------------

wasabi | 2025-06-24 19:12:53 UTC | #2

gm @UI369 thanks for putting together this amazing deep dive into the GG <> GS collaboration that took place during the past ~7 months, as a member of the OG Community Council I can say that the UX & UI of handling the community rounds using Grants Ships was an improvement in several angles like you outlined and created the foundational work to piggyback into the success of GG Rounds to continuously improve & iterate.

Now that I've read this forum proposal, I just want to congrats to everyone involved into this build and love to see the alignment between Gitcoin & Grants Ships.

LFG :rocket:

-------------------------

Sov | 2025-07-09 11:42:24 UTC | #3

Thanks @UI369 !

I am in favor of supporting the request for $ 40,000 in retroactive funding for this project.  We appreciate your contributions to the ecosystem and the work done to produce a successful build.

-------------------------

ivanmolto | 2025-07-09 18:05:29 UTC | #4

I’m also in favor of this budgeting — echoing what was already well said above.

I fully support the request for $40,000 in retroactive funding. I’d also like to highlight how responsive the team was during the GG23 Community Rounds voting period — they were quick to answer questions and respond to feedback about the voting module, even on weekends. That level of engagement and dedication is truly appreciated.

-------------------------

Oba-One | 2025-07-09 22:06:02 UTC | #5

Amazed by all the work the DAO Masons team has done with minimal funds and excited to see Grant Ships continued to be utilized for Gitcoin Grant Rounds. I support this proposal and looking forward to the vote.

-------------------------

MathildaDV | 2025-07-14 23:03:08 UTC | #6

Appreciate the proposal and the work that went into making GG23 a success. I am in favour of this proposal.

-------------------------

paul2 | 2025-07-16 20:13:22 UTC | #7

I support! Very happy with the work the Grant Ships team did on GG23, and $40k looks fair for the work :+1:

-------------------------

cauetomaz | 2025-07-16 20:32:10 UTC | #8

DAO masons have showed that they can deliver a lot of tangible impact with their buildings. I support the request for $40,000 in retroactive funding! Thanks for all the work for the ecosystem.

-------------------------

MathildaDV | 2025-07-17 22:18:17 UTC | #9

This proposal is now live on Snapshot for voting: https://snapshot.box/#/s:gitcoindao.eth/proposal/0x92a36f55042108a839328a18f23b64dfdf1610e37a9ae00fb4ea130e45ad1583

-------------------------

SEEDGov | 2025-07-21 15:36:55 UTC | #10

As part of Gitcoin's Governance Council, we've had the opportunity to use Grant Ships when assessing GG applicants. That's why we really value all the work done by DAO Masons. That being said, we support this proposal with our FOR vote and we expect to keep wroking with them in future GG rounds.

-------------------------
