---
id: 19712
title: "Citizen Grants GCP - Impact Passports and Impact Quadratic Funding (ImpactQF)"
slug: citizen-grants-gcp-impact-passports-and-impact-quadratic-funding-impactqf
category: citizen-grants
url: https://gov.gitcoin.co/t/citizen-grants-gcp-impact-passports-and-impact-quadratic-funding-impactqf/19712
created_at: 2024-12-05T19:10:17.677Z
last_posted_at: 2025-08-16T14:35:35.315Z
posts_count: 8
views: 4783
like_count: 34
---

# Citizen Grants GCP - Impact Passports and Impact Quadratic Funding (ImpactQF)

<https://gov.gitcoin.co/t/citizen-grants-gcp-impact-passports-and-impact-quadratic-funding-impactqf/19712>
sharfy | 2024-12-05 19:15:26 UTC | #1

# Proposal Title

Baking Impact Into The Quadratic Funding Matching Formula (ImpactQF)

# Description

This proposal seeks funding to create an **Impact Passport framework**. We expect use of this passport to augment the Quadratic Funding mechanism, serve as training data for AI allocation agents, and other use cases as they arise.

Projects can collect passport stamps from a selection of Impact Evaluators to demonstrate the impact of their project. Examples of existing Impact Evaluators are Open Source Observer for software contributions, Karma GAP for output based evaluation, Metrics Garden for outcome based evaluation, or GainForest for climate projects.

The first application of impact passport that we would like to see is a new mechanism, Impact Quadratic Funding (ImpactQF), where we bake impact into the quadratic funding matching formula. Projects with a higher impact score will obtain a higher matching fund. Through these verified impact measurements, ImpactQF ensures that matching funds are efficiently allocated based on *outcomes* rather than a popularity contest.

We hope that Gitcoin will also integrate the Impact Passport and ImpactQF mechanism in its future funding rounds. Through this implementation, we aim to support Gitcoin in more efficient allocation of capital. It would also position Gitcoin as the centerstage for evaluation providers to be included as a stamp, similar to the role Gitcoin passport played for identity solutions.

# Motivation

*Based on the 2025 trends to watch by Gitcoin: https://gov.gitcoin.co/t/2025-trends-to-watch-gitcoin/19362*

“Grants are not dying, but they are entering their Reputation era.” There is a rising demand for verifiable impact. We need to quickly capture this market segment of efficiently allocating ecosystem incentives to the most impactful projects.

Currently, Gitcoin primarily allocates funds based on Quadratic Funding, which does not have an impact metric baked into its formula. As more matching funds are allocated to projects that have the most “votes", projects that invest a considerable amount of time and resources in community outreach and marketing tend to capture more matching funds than those creating genuine impact. One potential downside of this formula is that projects may be incentivized to value promotion over delivering real value. This creates a self-reinforcing cycle where funding is driven by community outreach rather than actual impact, ultimately incentivizing projects to prioritize promotion, or direct their funds into capturing more funds rather than doing work.

IQF addresses this by incorporating verified impact scores from specialized evaluators into the quadratic funding formula, creating an equitable mechanism that rewards actual outcomes across different domains of public goods.

It also positions Gitcoin as the central platform where every evaluator in the space tries to get included as a stamp. 

# Specifications

1. **Core Protocol Development**

* Implement the impact-weighted quadratic funding formula:![|567x232](upload://wDMYNQ18CujnW4F83Bgr5dvMU7O.png)
* Develop standardized impact verification framework
* Create impact passport system for project evaluation
* Build integration layer with existing QF infrastructure


2. **Impact Verification System**

* Design a three-layer verification architecture:
  * Layer 1: Data collection and submission protocols
  * Layer 2: Proof of claims verification
  * Layer 3: Automated impact monitoring
* Implement API endpoints for verification services
* Create standardized impact scoring mechanism


3. **Impact Passport Hub (Frontend)**

Our technical stack includes:

* Impact passport system for standardized project evaluation
* Integration with impact evaluators
* Hypercerts integration for impact claims
* Allo integration for automated matching fund distribution

# Roadmap and Milestones
### Project Plan

|Month|Phase|Deliverables|
| --- | --- | --- |
|Month 1|Technical Foundation|1. Adjust allo protocol to deploy the adjusted matching equation.   <br/>2. Create impact passport standard specification and technical documentation|
|Month 2|Creation of Impact Passport Hub|1. Launch alpha version of the Impact Passport Hub - a platform where projects can connect their wallet and track their impact.|
|Month 3-4|Integration & Testing|1. Integrate 3+ impact evaluators, such as (Metrics Garden, Open Source Observer, Karma Gap, etc) tracking into impact passport <br/> 2. Assign weightages to the different stamps<br/>3. Deploy automated impact scoring system|
|Month 5|Pilot Preparation and Launch|1. Onboard projects to Impact Passport<br/>2. Launch public interface for donors|

### Technical Integration Milestones

**1. Impact Verification System**

* Integration with Impact Evaluators such as Open Source Observer, Karma GAP, Metrics Garden, and more

**2. User Interface**

* Users can sign in with their project wallet, and have the ability to collect impact passport stamps.

**3. Documentation & Open Source**

* Technical specifications
* API documentation
* Code repository publication
* Integration guides
* Developer workshops focused on impact verification integration
* Monthly technical updates on Gitcoin Discord/Forum


**4. Education**
* Comprehensive technical whitepaper explaining IQF's solution to the QF marketing problem
* Open-source repository with detailed implementation guides


**5. Content & Knowledge Sharing:**

* Blog post series explaining:
  * IQF's mathematics and implementation
  * Impact verification methodology
  * Case studies from pilot projects
  * Integration guides for developers
* Live demo at Gitcoin-aligned events
* Virtual workshops with projects
* Regular progress updates on Gitcoin Forum
* Regular community calls demonstrating impact verification tools
* Community presentation showcasing IQF's first funding round results


We'll maintain continuous engagement through the full development cycle, ensuring the Gitcoin community understands both the technical innovation and practical impact of IQF.

# Benefits
**Impact Passport**

* Can be used in any mechanism, not just in Impact Quadratic Funding
* Reduces over-reliance in any one kind of metric, as different impact evaluators have different metrics that they evaluate for
* Positions Gitcoin as the central platform where every evaluator in the space tries to get included as a stamp

**Impact Quadratic Funding**

* Bakes in impact directly into the funding mechanism
* Allows donors or grant operators to measure the impact of their capital allocation
* Allocates ecosystem incentives to the most impactful projects


# Drawbacks

**Technical Challenges**

* Risk: Scalability issues with impact verification
Mitigation: Implementing batch processing and optimized data pipelines

* Risk: Smart contract limitations with Allo protocol
Mitigation: Working closely with Gitcoin/Allo team

**Adoption Challenges**

* Risk: Complex onboarding for projects
Mitigation: Creating simplified mobile-first interfaces and local language support

* Risk: Impact verification delays
Mitigation: Building redundant verification pathways and automated monitoring

**Market Challenges**

* Risk: Insufficient matching pool
* Risk: Project quality variation
Mitigation: Standardized impact metrics and tiered verification system



# Budget Overview

* Smart Contract Development: $10K
* Impact Passport Hub Platform: $10k
* Impact Passport Stamp Integrations: $10k
* Technical Documentation, Education, Community Building: $5k

Total budget requested: $35k

# **Measures of success and KPIs**
Success Criteria

* Technical
  * Successful processing of all impact verifications
* Impact
  * 10+ active projects
  * $10K+ in contributions processed
  * 3+ successful impact verification cycles
* Community
  * 4+ technical integrations
  * Published case studies from pilot projects

|Month|Phase|Success Metrics|
| --- | --- | --- |
|Month 1|Technical Foundation|* Documentation of impact verification API<br/>* Published technical specification for impact passport|
|Month 2|Creation of Impact Passport Hub|* Open-sourced Github Repo of our Impact Passport Hub<br/>* Users can sign in with their wallet, view their Gitcoin project on the portal, and view possible impact stamps to verify with|
|Month 3|Integration & Testing|* Successful processing of test transactions<br/>* Open-source repository with technical documentation|
|Month 4|Pilot Preparation|* 10 completed impact passports<br/>* Published API documentation<br/>* Completed UI/UX testing|
|Month 5|Launch & Validation|* Minimum $10K total contributions processed<br/>* Successfully executed matching calculations<br/>* 100% of funds distributed correctly<br/>* Published transparency report|

# The Team

David Dao (@[dwddao](https://x.com/dwddao))
Sejal (@[sejal_rekhan](https://x.com/sejal_rekhan)) (will not be paid due to conflict of interest)
Sharfy (@[sharfyae](https://x.com/sharfyae))
Shuhei (@[shutanaka_jp)
](https://x.com/shutanaka_jp)Devansh (@[TheDevanshMehta](https://x.com/TheDevanshMehta))
Carl Barrdahl ([@carlbarrdahl](https://x.com/carlbarrdahl))

# Advisors
LauNaMu | Metrics Garden (@[0xyNaMu](https://x.com/0xyNaMu))
Mahesh | Karma GAP (@[mvmurthy](https://x.com/mvmurthy))

-------------------------

owocki | 2024-12-05 21:06:59 UTC | #2

[quote="sharfy, post:1, topic:19712"]
**1. Impact Verification System**
[/quote]

i am curious what types of impact data we should be ingesting to start. i think this is coupled with the question of "what GG community round would be a good pilot for this campaign?"

perhaps OSS is the best place to start due to it (1) having heat, ppl care about it (2) lots of good data available for that.

wdyt @MathildaDV ?

[quote="sharfy, post:1, topic:19712"]
* Smart Contract Development: $10K
[/quote]

is there a component of this that will be built with smart contracts? most of the QF calcs are offchain, so wondering if we can reallocate this budget to something else.  personally i think marketing this mechanism and what makes it special would be a good use of funds.

-------------------------

Sov | 2024-12-05 21:13:37 UTC | #3

I support exploring this Impact Passport framework, particularly its potential to shift funding allocation from pure marketing effectiveness to verified impact. The multi-evaluator approach using established tools like Open Source Observer and Karma GAP could provide valuable signals for decision-making.

Two suggestions:

* Could you share a concrete mock-up showing how impact scores would be calculated and how the modified quadratic funding formula would work in practice?
* Consider structuring as 50% upfront for infrastructure and 50% retroactive based on specific success metrics like number of projects onboarded and funding allocated through ImpactQF.

-------------------------

umarkhaneth | 2024-12-06 07:44:01 UTC | #4


Hello!
- I think this is an interesting experiment to run and I'm in favor of this great team executing on it. 
- I'd be interested to see simulations of results based on past rounds data!
- I appreciate the reasonable budget as well.

-------------------------

ccerv1 | 2024-12-06 16:00:35 UTC | #5

Happy to see this proposal and can personally vouch for the team as being values-aligned, long-term oriented. Also appreciate the opportunity to integrate with OSO & KarmaGAP :saluting_face: 

Putting my steward hat on, I would say:

:white_check_mark: High caliber team
:white_check_mark: Budget is very reasonable
:white_check_mark: This feels like an important complement to Gitcoin's growth strategy
:question: Generally, I like to see teams come with a PoC or some traction **first** before getting funded (see my comments on [another recent GCP](https://gov.gitcoin.co/t/gcp-xxx-community-knowledge-base-for-llm/19523)). In this case, that could be accomplished via a simulation (mock data) or a very basic impact framework on a subset of historic project submissions. 

If this moves to a vote, I would likely abstain given OSO is a (indirect) dependency, but will hereby register my support for this in principle

-------------------------

meglister | 2024-12-12 02:55:16 UTC | #6

Appreciate the thought behind the proposal -- verifiable impact is a huge initiative for Gitcoin and for the grants space generally. Also love to see the collaboration with our friends/valued partners at OSO, Karma, Metrics Garden, etc.

I'll echo @Sov and @ccerv1 's comments around funding a brand-new initiative -- it's generally safe/nice to invest in teams with some proven traction. I'm also having a hard time conceptualizing the user journey for projects who participate in this... I'm worried it's a little onerous? One way to address this could be the simulations @ccerv1 mentioned or even some mockups / wireframes.

One thought-starter for you all: how should QF donors think of their role in allocating funding with this algorithm in place? What do they add to the equation that is not accounted for in the impact algorithm? And if the impact measurement efforts are successful, could donors actually have a negative impact on allocations?

-------------------------

owocki | 2025-01-06 00:51:40 UTC | #7

Is there a pilot identified for this product?  How big and for whom?  Id be more keen to vote yes if there is a pilot that will deliver some GMV/results in a real world scenario vs a building for a hypothetical end user.

-------------------------

DavidDAO | 2025-08-16 14:35:35 UTC | #8

***tl;dr** we just did it anyway :slight_smile:* 

Felt a need to provide a closing to this thread. ImpactQF has been successfully tested out in two rounds in GG23:

https://gov.gitcoin.co/t/gg23-hypercerts-for-nature-stewards-full-round-report/20975

https://gov.gitcoin.co/t/ai-impactqf-regen-coordination-global-gg23-retrospective/20385

**ImpactQF** has now evolved and future iterations focus especially on impact evaluation, which resulted in a research retreat on impact evaluation ([researchretreat.org](https://researchretreat.org)) and experimental funding mechanisms such as AI ImpactQF, [DeepGov](https://gov.gitcoin.co/t/deepgov-phase-3-the-ai-elections-are-live/20315) and it's newest iteration, [Simocracy](https://simocracy.org). 

I expect to see this ImpactQF evolve, likely dropping the ImpactQF with ImpactX (any mechanism with integrated scalable impact evaluation) and being adopted by current and future round operators such as [GainForest.Earth](https://gainforest.earth), [Recerts Journal](https://recerts.org) and [Regen Coordination](https://www.regencoordination.xyz/).

-------------------------
