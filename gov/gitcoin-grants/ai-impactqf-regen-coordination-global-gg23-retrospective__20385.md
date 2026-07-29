---
id: 20385
title: "AI ImpactQF + Regen Coordination Global GG23 Retrospective"
slug: ai-impactqf-regen-coordination-global-gg23-retrospective
category: gitcoin-grants
url: https://gov.gitcoin.co/t/ai-impactqf-regen-coordination-global-gg23-retrospective/20385
created_at: 2025-05-09T18:53:31.963Z
last_posted_at: 2025-07-07T10:47:49.862Z
posts_count: 9
views: 4338
like_count: 37
---

# AI ImpactQF + Regen Coordination Global GG23 Retrospective

<https://gov.gitcoin.co/t/ai-impactqf-regen-coordination-global-gg23-retrospective/20385>
MontyMerlin | 2025-05-13 08:05:30 UTC | #1

![Regen Coordi-Nation Network Nation|690x388](upload://9StK52QsTIU5OEKt3WGgbfyiw0p.jpeg)

# Overview

The **Regen Coordination Global GG23** round has been our most ambitious and innovative experiment in regenerative funding to date. With a **$96,000 matching** pool raised, this round supported **50 projects** working at the intersection of ReFi, Ethereum, and local ecological, social, and economic regeneration.

> **Key Results** 
> 
> * **579 unique donors**
> 
> * **$10,817 in contributions**
> 
> * **$90,000 in matching funds distributed**, and further $6,000 to be allocated in partnership with [DeepGov](https://www.deepgov.org/) through further AI evaluation and allocation agents.
>
> See [Round Report Card](https://reportcards.gitcoin.co/42220/31) for more.

This global round ran in parallel with two regional partner rounds — [ReFi Mediterranean](https://explorer.gitcoin.co/#/round/42220/33) and [Regen Rio de Janeiro](https://explorer.gitcoin.co/#/round/42220/30) — as part of a coordinated effort to localize regenerative public goods funding and build momentum towards a cosmo-local network of ReFi grantmaking. Furthermore, we also launched the [Regen Coordination Digital Public Goods Round](https://explorer.gitcoin.co/#/round/42220/25) on Gitcoin, delivering $30k in direct grants to key supporting infrastructure projects, including [Karma GAP](https://explorer.gitcoin.co/#/round/42220/25/1),  [ Zazelenimo](https://explorer.gitcoin.co/#/round/42220/25/2), and the [Local ReFi Toolkit Funding Pool](https://explorer.gitcoin.co/#/round/42220/25/5).

Altogether, these rounds have ALLOcated **$159,732** in capital across programs so far in 2025. We’re deeply grateful to the ecosystem leaders, sponsors and partners who made these experiments possible → Gitcoin, Celo Public Goods, Ma Earth, Kevin Owocki, ReFi DAO, Greenpill Network and others.

Beyond the numbers, **GG23 served as the first pilot of the AI + ImpactQF methodology** — a system we believe could become one of the leading mechanisms for Web3 grant funding. This post will serve as a case study of the methodology we deployed, our key learnings and the future vision from here.

---

# Case Study: AI ImpactQF 🧪

For this round, we combined three powerful innovations:

1. **A Common Approach to Impact Measurement** (implemented through Karma GAP)

2. **AI-Enhanced Evaluation** (GPT-4o & Claude 3.7 + Coordination Council)

3. **ImpactQF** (Impact-Weighted Quadratic Funding)

This approach enables a scalable, transparent, and rigorous impact evaluation and funding system to complement quadratic funding by aligning matching allocations with demonstrated outcomes — not just marketing or social capital. Here’s how it worked 👇


### 1) Common Approach to Impact Measurement

**The [Common Approach](https://www.commonapproach.org/) to Impact Measurement** is a set of frameworks designed to support organisations and institutions in measuring, managing, and communicating impact in a way that is both rigorous and flexible. It addresses the tension between standardized metrics and context-specific approaches by creating interoperable and adaptable standards.

![|2048x463](upload://weaMgctPGShClKzwHYBxSBgw4U0.png)

[**CIDS (Common Impact Data Standard)**](https://www.commonapproach.org/common-impact-data-standard/) is a data ontology that enables structured, semantic, and machine-readable impact data. It enables:

* Flexible representation of any impact model (logic model, impact thesis, etc.)
* Interoperability between systems and standards (e.g. SDGs, IRIS+)
* Integration of the five Impact Management Project (IMP) dimensions: What, Who, How much, Contribution, and Risk
* Use by multiple software platforms for consistent and shareable data.

For anyone interested in exploring further, the [Common Approach Impact Ontology resource](https://www.commonapproach.org/impactontology/) offers detailed information.

![Regen Coordination Reporting Flows|690x285](upload://bhCLnaB8xDp8mYvGA2u0X5uZqmi.jpeg)

Regen Coordination has been directly supporting the integration of the Common Approach into the KarmaGAP platform, enabling more effective tracking and evaluation of project activities, outputs and impact. Furthermore, to support onboarding and context development, we also developed **templates, graphics and guides** to support projects in effectively understanding and using the system.

> [Impact Reporting Guidance | Regen Coordination 
> ](https://www.regencoordination.xyz/guidance-regen-coordination-impact-reporting)
[How to Use AI for Activity & Output Reporting](https://www.regencoordination.xyz/ai-for-activity-output-reporting)
> 
> We also translated materials into both 🇪🇸 [Spanish](https://www.regencoordination.xyz/Regen-Coordination-Global-GG23-ES-1be2e7251f2f80babfbef1cf223bd6cc) and 🇵🇹 [Portuguese](https://www.regencoordination.xyz/Regen-Coordination-Global-GG23-PT-1be2e7251f2f8010abc7d017c6ed443f). 

![Regen Coordiantion - Activity & Output reporting|690x218](upload://ddCfFjvm1JQqpB5tnkxpObJoALI.jpeg)

![Regen Coordiantion - Output Deliverables & Metrics|690x249](upload://6Db6xqAH5xJzsXSvfnlIS198Eb1.jpeg)

### 2) AI-Augmented Evaluation

To process and assess a high volume of data from 50 projects in the round with consistency, transparency, and speed, Regen Coordination used a **hybrid AI + human evaluation process.** This approach ensured each application was rigorously evaluated on its merits using both structured AI analysis and expert human judgment.

Analyzing the Gitcoin application + Karma GAP project data, we leveraged two leading models — **GPT-4o** (OpenAI) and **Claude 3.7** (Anthropic) — to generate detailed independent reports for every project in the round. These dual evaluations allowed us to cross-compare results and reduce model-specific bias — increasing robustness and confidence in our findings (see [Evaluation Comparison: Claude 3.7 vs GPT-4o](https://www.notion.so/celopg/Evaluation-Comparison-Claude-3-7-vs-GPT-4o-1dd2e7251f2f80da9106e4ca6dedee5d?pvs=24)).

In alignment with [Regen Coordination’s Core Mission and North Star Outcomes](https://www.regencoordination.xyz/Regen-Coordination-Mission-North-Stars-1c32e7251f2f8070897fc38b8375509f), the evaluations were structured around five key criteria:

> 🌟 Increase Awareness, Engagement, Adoption, and Development of ReFi Web3
> 
> 🌟 Increase Awareness, Adoption, Development, and Financial Activity on Celo, Ethereum, and the Ethereum-Aligned Ecosystem
> 
> 🌟 Directly Create or Catalyse Local Ecological, Social, and Economic Impact
> 
> 🌟 Resources, Maturity, and Past Funding Compared to Impact Delivered
> 
> 🌟 Active Goals, Plans, Milestones and Objectives

The AI Models scored each project on a 1–10 scale against each of these 5 criteria with the [detailed evaluation rubrics](https://www.notion.so/celopg/Regen-Coordination-Project-Evaluation-Methodology-1e42e7251f2f808fa404c759fecdb86a?pvs=4#1e42e7251f2f80c9b652fb189d5d8936) we developed to support rigorous and comparable assessment. Each model worked in a clean prompt environment, with no cross-contamination or prior context, ensuring clarity and impartiality.

All reports included detailed narrative evaluation of project impact and activities, scoring and rational across the five rubric areas, and highlights of strengths, risks, and areas for improvement.

> You can browse the full reports here:
> 
> * [ Evaluation Reports (GPT-4o)](https://www.notion.so/1dc2e7251f2f8098b047e71adddfccb5?pvs=21)
> * [ Evaluation Reports (Claude 3.7)](https://www.notion.so/1dd2e7251f2f808da942f25102cdb620?pvs=21)

These baseline AI evaluations were then reviewed by the [Coordination Council](https://www.notion.so/celopg/Regen-Coordination-Global-GG23-1972e7251f2f802b9c8ef0a29fa8e6e2?pvs=4#1b32e7251f2f805dbfe0da6fbc1728c1), made up of evaluators from ReFi DAO, Celo Public Goods, and Greenpill Network. Each project received at least three independent human reviews, with scores averaged and used as the final impact evaluation rating.

> This hybrid approach reflects the paradigm described by Vitalik Buterin:
> 
> *“AI as the engine, humans as the steering wheel."*
>
> [vitalik.eth.limo](https://vitalik.eth.limo/general/2025/02/28/aihumans.html )

AI provides the efficiency and structured analysis needed to scale, while human reviewers bring strategic judgment, contextual insight, and ethical oversight.

Further details on our process here: [Project Evaluation Methodology | Regen Coordination](https://www.regencoordination.xyz/project-evaluation-methodology)

---

### 3) ImpactQF (Impact-Weighted Quadratic Funding)

Once impact evaluations were completed, we integrated the final Coordination Council reviewed scores directly into the matching fund allocation. As such, this round represented the **first completed implementation of ‘ImpactQF'** — an idea [originally proposed](https://gov.gitcoin.co/t/citizen-grants-gcp-impact-passports-and-impact-quadratic-funding-impactqf/19712) by Sharfy and David Dao of GainForest to align quadratic funding with verified impact outcomes. The problem this model addresses is well-known: regular QF can become a popularity contest, over or under rewarding projects based on marketing skills and ability to mobilize donor networks rather than underlying impact.

For this round, we implemented a Hybrid ImpactQF Model — meaning that instead of modifying the quadratic formula itself, our method ran two evaluation tracks in parallel:

* **COCM Score** - 50% of matching was based on the default Gitcoin QF COCM results — reflecting the number of unique donors, donation clusters, and total contributions per project.

* **Impact Score** - 50% was based on the project’s final impact score — derived from the AI-generated reports and the reviews by human evaluators.

This model helped to balance crowdfunding signal with evidence-based evaluation to ensure that both community support and demonstrated outputs shaped funding allocation.

**Why the Hybrid Model?**

For our first implementation of ImpactQF, the Coordination Council voted for this hybrid model on the basis that it would be better suited for getting our community introduced and accustomed to the new methodology. See below for a detailed comparison of the mechanisms.

![|1520x1620](upload://sRxcBjWlM8bEiCRk2MEg0sd3xhB.jpeg)

In future rounds, we aim to shift toward a fully impact-embedded QF system where we internalise the impact score directly into the match formula. Until then, the Hybrid Model offers a practical and high-integrity stepping stone. Going forward, Regen Coordination is actively collaborating with Gitcoin, DeepGov, and others to explore these next-stage systems — and is committed to further evolving the ImpactQF landscape.

# 📊 Results & Analysis

> 👉 **Explore full results & reports**: [GG23 Results Sheet
> ](https://docs.google.com/spreadsheets/d/1QqHbFEXXSHUQv6m-sUJ5619mmyEGQevRBNQJRNdbWm0) (Includes: AI reports, scoring, final match allocations)

![GG23 Regen Coordination Global Results - ALL|500x1000](upload://pf56j9l3PMOyj2r4aXlKIMKBVjo.jpeg)

The final allocations reflect the success of the hybrid ImpactQF approach in balancing grassroots support and measurable regenerative outcomes. While traditional QF rounds have mostly favoured projects with large donor networks or slick promotion, this round ensured resources were allocated to impactful projects which may have otherwise been overlooked.

![|2048x970](upload://8h5zKNx6aDucQUJw9Y3IsTWlHIw.png)

**Key Trends:**

* Projects with strong **community backing and high impact** (e.g. Kokonut Network, Gainforest, Greenpill Dev Guild, Atlantis) received significant relative matching — confirming the power of aligned public and evaluator support.

* Several **high-impact but lower-donor** projects saw their matching significantly boosted through the process — helping re-balance outcomes that would otherwise have skewed toward popularity.

* A few projects that garnered **strong QF support but had low impact scores** saw their relative final allocations lowered accordingly — illustrating the effect of the hybrid model in prioritizing impact over popularity.

**Key observations:**

* **No extreme outliers**: The highest-matched project received under $4,000, and the drop-off is gradual across the entire dataset.

* **Healthy middle**: A substantial number of projects landed in the $2,000–$3,500 range, suggesting the hybrid model rewarded a broad set of contributors rather than concentrating funds.

* **Reduced tail effect**: The lower end of the distribution still received meaningful relative allocations (mostly >$1,000).  Funding is more evenly spread across the ecosystem — rewarding a wide diversity of approaches, regions, and organizational maturity levels.


### Testimonials

> *“A great round and amazing to receive the feedback after the evaluation. appreciate all the team and sponsors. massive job done in organizing this round from point A to point B”* 
>
> [@ReFiPhangan](https://x.com/ReFiPhangan/status/1919785605728276948)

> *“Quite exciting to see the way funds were allocated this time. Good to see it going beyond wisdom of the crowds”* 
>
>[@solarpunkmaxi](https://x.com/solarpunkmaxi/status/1920005642095341620)

> “*It was a well-documented program with all the resources for donors and grantees to make informed decisions every step of the process.*”
> 
> “*It was a very detailed process with multiple layers of evaluation, a balanced approach.*”
> 
> 
> [Anons from Feedback Form](https://tally.so/r/31xlKb)

### Learnings & Reflections

The Regen Coordination Global GG23 round was a bold and complex experiment — and like any pilot, it generated critical insights to help refine future iterations of the methodology. Here are a few of the key takeaways from the Coordination Council:

#### 1. Flattened Distribution = Greater Equity, But Less Variance

While the Hybrid ImpactQF model succeeded in avoiding the pitfalls of pure popularity contests, the resulting matching distribution was relatively flat and linear, with less differentiation between projects. This helped create a sense of fairness and broad inclusion — but may also have under-rewarded the most exceptional performers.

➡️ In future rounds — especially as impact data integrity and matching fund amounts increase — we may evolve toward Impact-Embedded QF, where impact scores directly influence match size inside the formula. This would allow greater reward variance and further sharpen incentives around impact outcomes, while maintaining the community voice at the heart of QF.

#### 2. Explore Differentiated Evaluation Tracks

While the evaluation rubric ensured consistency, it occasionally struggled to equally serve local on-the-ground regenerative communities and digital public goods /software teams (e.g. Atlantis, GainForest, Regen Atlas, Silvi). Each of these groups operate with different resources, visibility, and output patterns, making apples-to-apples scoring challenging.

➡️ In future rounds, we may introduce separate evaluation tracks or tailored rubrics — allowing software, infra, and digital tool builders to be assessed using more appropriate metrics (e.g., usage data, dev activity, integrations), while maintaining strong standards for place-based community work.

#### 3. Impact Reporting Infrastructure Is Maturing, But Still New

GG23 was the first usecase of Karma GAP’s new Common Impact Data Standard (CIDS) aligned reporting system, enabling structured activity and output tracking across all projects. While the foundation was strong, we encountered expected early-stage challenges around UX, data consistency, and reporting quality.

➡️ Looking forward, we aim to improve ease of use, deepen integrations with ReFi apps and onchain data sources, and automate more reporting processes — ultimately making impact evaluation easier and more useful for all stakeholders.

#### 4. AI-Enhanced Evaluation Is Ready

One of the most promising outcomes of this round was the successful deployment of a hybrid AI + human evaluation model. The dual-model approach (GPT-4o and Claude 3.7) produced consistent, high-quality reports that supported rigorous impact scoring and gave both human evaluators and grantees detailed, actionable feedback and insights. However, despite these strong results, the current processes were manual and time consuming to execute — requiring data scraping, detailed prompt design with iterative testing, cycling each project individually through multiple models, manual review of AI generated evaluations, and compiling scores into the final scoring spreadsheet.

➡️ Going forward, we will build on the foundations already established and iterate further — experimenting with more agent-based review flows, deeper prompt tuning, and the automation and productisation of the process with partners like KarmaGAP,[ DeepGov](https://www.deepgov.org/) and others. Ultimately we aim to significantly reduce friction, improve accuracy, and make it easier for other rounds to replicate and adopt the ImpactQF model.

#### 5. Increasing Cross Pollination and Collaboration

A deep insight from the evaluations was the high potential for collaboration between projects to strengthen ecosystem-wide outcomes. Throughout the review process, a clear pattern emerged: some projects demonstrated strong local impact but limited onchain or ReFi integration, while others excelled in ReFi/Web3 tooling but lacked grounded, community-based activity. This divergence is encouraging as it shows we have a complementary ecosystem where projects can support each other in progressing in their weaker dimensions.

➡️ As we design future rounds, we want to optimize for collaboration and cross-pollination as core evaluation and ecosystem principles. Potential directions include:

* Allowing projects to attribute shared impact across multiple collaborators.
* Introducing lightweight peer review and endorsement tools (e.g. DeVouch) to surface trust and relational signal.
* Hosting collaboration-focused workshops to foster intentional partnerships between grantees.
* Using the upcoming [Regen Coordination Hub](https://hub.greenpill.network/t/protocol-amendment-rebrand-the-greenpill-hub-into-the-regen-coordination-forum/203/3) to share ideas and cross pollinate

# Next Steps & Future Vision

Building on learnings from GG23, Regen Coordination will double down on its mission to support the growth and coordination of the **ReFi and Ethereum Localism** movements — and aim to act as a **dedicated domain expert** within Gitcoin 3.0 and beyond.

![Gitcoin Funding Festival Ideas|690x318](upload://b5t7XHEvCCOBWN9yjBgkdUWrjDw.png)

Here are some of the key next steps we will prioritize 👇

### 1) Strengthening Governance and Community Participation

Regen Coordination began as a partnership between Celo Public Goods, Greenpill Network, and ReFi DAO — and has since grown to include additional aligned communities. As we seek to scale further, establishing a more **transparent and participatory governance framework** is a top priority. This includes evolving the Greenpill forum into a Regen Coordination Hub, hosting regular coordination calls and workshops, and co-creating documentation to define council roles, processes, and fund allocation.

We want this process to be community driven, if you have thoughts to add or feedback on what is currently suggested please share.

### 2) Automating and Productizing the ImpactQF Stack

To scale the model implemented in this round we seek to evolve the ImpactQF methodology into a more automated, composable, and user-friendly system — making it easier for other communities and ecosystems to adopt. With the winding down of Gitcoin Grants Stack, we’re actively exploring what a new integrated ImpactQF tech stack could look like — combining best-in-class tools from across the ecosystem.

Some exciting possibilities include:

* **Karma GAP** as the core data layer — with all project profiles, impact metrics, and activity/output reports standardized using Common Impact Data Standard (CIDS), and added automation with further integrations with leading ReFi Web3 apps.

* **DeepGov** to power AI agent workflows and enable streamlined human evaluation interfaces — reducing friction in scoring, review, and aggregation.

* **Self.xyz** to provide secure, privacy-preserving identity verification — enabling sybil-resistant quadratic funding without compromising UX or accessibility.

* **Allo Protocol** as the underlying distribution and allocation smart contracts.

* **Mainstream payment integrations** (e.g. cards, PayPal, Apply Pay) to lower barriers for new donors and onboard fiat capital into onchain regenerative funding flows.

* **Prosperity Pass and Divvi.xyz** as mechanisms to track and incentivize adoption of key ReFi tools and behaviors, as well as measuring Total Value Flowed (TVF).

Together, these tools could form a modular, interoperable stack that enables communities anywhere to run their own ImpactQF rounds — from local regenerative hubs to global and bioregional networks. While still in early stages, these explorations point to a future where impact-embedded funding is easy to run, replicate, and trust at any scale.

### 3) Expanding a Global Network of Local Funding Rounds

Alongside the global round, community-led experiments in the Mediterranean and Rio de Janeiro successfully mobilized local donors and matched capital to grassroots regenerative projects. Looking ahead, Regen Coordination is exploring how this model could scale — evolving into a cosmo-local network of bioregional and community-driven funding rounds. Each round would be tailored to its unique context, yet aligned through shared values, methodologies, and infrastructure.

As part of **Gitcoin 3.0**’s shift toward **Dedicated Domain Allocation (DDA)**, Regen Coordination aspires to lead as a dedicated domain expert for ReFi and Ethereum Localism. We’re exploring whether a structure like a Regen Coordination [Grantship](https://rules.grantships.fun/) could serve as a coordination layer — offering technical, evaluative, and strategic support to local rounds while creating pathways for these communities to access matching funds. Over time, this could create healthy competition among communities to demonstrate regenerative outcomes and Total Value Flowed (TVF) within local Web3 economies.

To support this ecosystem, we continue to develop and refine the [Local ReFi Toolkit](https://www.notion.so/celopg/Local-ReFi-Toolkit-Drafting-1ba2e7251f2f808d95b9f6d9f21cf77c?pvs=4) — a practical, accessible resource to help communities launch and sustain regenerative economies using Web3 tools. The toolkit aims to lower entry barriers and empower communities to bring Ethereum Localism to life.

### 4) Cosmo-Local Capital Flows

To date, Celo Public Goods and Gitcoin have been Regen Coordination’s primary funding partners — providing essential early support for piloting regenerative funding infrastructure and methodologies like ImpactQF. Going forward, we see promising opportunities for “**matching-on-matching**” dynamics, not only with other crypto-native sources such as Ethereum, Octant, and ecosystem-aligned organisations, but also through systems that blend global Web3 infrastructure with local governance, public institutions, and place-based finance. This pathway could enable us to help unlock and de-risk additional capital from municipal governments, public agencies, philanthropic foundations, and institutional actors. If done well, this could dramatically expand the resources flowing into regenerative initiatives.

One live example is our partnership with [Zazelenimo](https://explorer.gitcoin.co/#/round/42220/25/2) — an urban greening initiative in Split, Croatia, which Regen Coordination is sponsoring and supporting. Their upcoming pilot will blend Ethereum-aligned participatory funding infrastructure with a 3:1 local municipal match, enabling citizen-led urban greening through a public–private–community capital stack. If successful, this model could be replicated globally — empowering cities to launch regenerative funding rounds, develop local currencies, and embed Web3 infrastructure into civic processes.

We’re also part of early discussions with [UNDP](https://www.undp.org/) and other institutional stakeholders, exploring how onchain tooling and regenerative methodologies could align with global sustainability frameworks. As these conversations progress, we believe Regen Coordination can serve as a bridge between Web3 innovation and real-world transformation — powering cosmo-local flows of capital that fund what matters for people and planet.

![Regen Coordination Flows - Powered by Ethereum|690x458](upload://hpz6GfX1UttrjSLwRRArwGXXbPF.jpeg)


## Vision

*‘What does it look like if Regen Coordination is maximally successful’*

If Regen Coordination succeeds at the highest level, regenerative communities across the globe are empowered with the infrastructure, capital, and coordination systems they need to grow, sustain, and thrive. Funding flows to those stewarding real impact — not through opaque legacy institutions, but through open-source, transparent, and community-governed mechanisms.

We unlock billions in Total Value Flowed (TVF) toward regenerative outcomes — circulating around local economies and institutional systems on Web3 rails. A global movement of place-based communities, open financial infrastructure, and AI-augmented capital allocators drives systemic change at every layer of our economies.

> [ The Path to $1 Trillion in TVF in the ReFi Web3 Movement by 2050](https://docs.google.com/document/d/10-eSBPgXEHzdYvt9z3tu6rX7-uvGX0L0TqPxcO8SrEA/edit)

**We reshape how capital flows, who it empowers, and what it values.** Funding becomes embedded in systems that reward verified impact and community stewardship. Bioregional capital networks flourish. Public institutions collaborate with DAOs. AI agents help route resources toward climate resilience, economic justice, and ecological repair — at planetary scale.


The Allo will flow ⛲️



> *If you are an [Allo Patron NFT](https://www.allo.capital/patron) holder you can support this vision and next steps by allocating some voting weight in the [Allo Capital Builders Fund gardens pool](https://app.gardens.fund/gardens/10/0x1eba7a6a72c894026cd654ac5cdcf83a46445b08/0xd3345828914b740fddd1b8ae4f4d2ce03d1e0960/123/0x4ceda4f34d3512900cc03c813e7eff4619ce5cfa-12). Thank you:)*

—
**Monty Merlin Bryant, Afolabi Aiyeloja, & the Regen Coordination Council**
On behalf of ReFi DAO, Greenpill Network, and Regen Coordination

![Ethereum Localism|690x460](upload://2um2JwMjyJ76wRL3NzeSJos7r70.jpeg)

-------------------------

luizfernando | 2025-05-12 22:44:57 UTC | #2

Thanks for sharing the retrospective and for all the effort in the round @MontyMerlin! It's been a pleasure to have been part of it 💫

Here's a retrospective on the parallel localized ReFi Mediterranean GG23 round, supported by Regen Coordination:

## Overview

The [ReFi Mediterranean GG23 Round](https://www.regencoordination.xyz/refi-mediterranean-gg23) was the first bioregional‑scale Quadratic Funding round supporting regenerative projects across the Mediterranean. A matching pool of **$10,000** was distributed using an **ImpactQF** approach that combined impact evaluation with traditional Quadratic Funding.

The round successfully engaged a diverse mix of Mediterranean initiatives — including local nodes, land‑based projects, and community hubs — many of which were new to Gitcoin and Web3.

![Gqu TEOW8AAC Be|400x500](upload://rtlLRLUmMHqqcDMQVPqVnmbFPb8.jpeg)

## Key Results
- **12 projects participating**
- **71 unique contributors**
- **206 donations made**
- **$1,064 donated to the projects**
- **$10,000 matching funds distributed**

## AI ImpactQF Implementation

Building on the Regen Coordination Global Round, the ReFi Mediterranean Round became the first localized, bioregional round to implement **AI‑driven ImpactQF**, embedding impact measurement (alongside the standard COCM QF) into fund allocation.

Implementation steps:

1. **Project reporting on Karma Gap**
   Projects documented their activities, deliverables, and metrics using the Common Approach to Impact Measurement.
2. **AI-Augmented Evaluation**
    AI evaluation reports + Round Operators evaluation
3. **ImpactQF matching**
   Impact and COCM scores were combined in the matching formula.

To ensure feasibility within tight timelines, we adopted key elements from the Regen Coordination Global Round:

- [**Regen Coordination’s Project Evaluation Methodology**](https://www.regencoordination.xyz/project-evaluation-methodology) - including evaluation criteria following the [Regen Coordination’s Core Mission and North Star Outcomes](https://www.regencoordination.xyz/Regen-Coordination-Mission-North-Stars-1c32e7251f2f8070897fc38b8375509f)
- **Hybrid model** for implementing ImpactQF:
    - **50% based on the Impact Score** - project’s final score, derived from the AI-generated reports and the reviews by human evaluators.
    - **50% based on COCM QF matching** - Gitcoin's default QF COCM results, reflecting the number of unique donors, wallet behaviors, and total contributions per project.

## Evaluations & Results

- [**Project pages & AI evaluation reports:**](https://www.regencoordination.xyz/ReFi-Med-GG23-Evaluations-1e72e7251f2f80b58783c7216d7bcb81)
    - Includes data from KarmaGap and Gitcoin (project pages) and both Claude 3.7 and GPT-o4-mini evaluation reports prepared for all projects.
- [**Evaluation spreadsheet:**](https://docs.google.com/spreadsheets/d/1yb9r5QwNnuaOUCSt1fCCCTmHPvRlgDkuesKxjxlLEg4/edit?usp=sharing)
    - Includes AI reports, human scores and final matching allocations.

### Key Trends & Observations

Compared with the Regen Coordination Global Round:

- **Activity & output reporting**
    - Lower quality of reporting.
    - Greater need for onboarding support for groups new to Gitcoin and Web3.

- **Evaluation methodology:**
    - Projects scored lower on criteria 1 and 2 (Web3/Ethereum alignment), so activity in these areas had a stronger effect on final scores.
    - A specific rubric for ReFi Mediterranean is needed to emphasize social and ecological impact over pure Web3 alignment.

- **Same trends as in the Regen Coordination Global Round:**
    - **Impact-first approach:** Projects with high QF support but low impact scores received reduced allocations, demonstrating the hybrid model's 
    - **Funding is more evenly spread** across the ecosystem — rewarding a wide diversity of approaches, regions, and organizational maturity levels.
    - **Healthy middle:** Most received between $500–$1,500.
    - **No extreme outliers:** The lower end of the distribution still received meaningful relative allocations, showing the model’s ability to lift smaller or emerging initiatives.

## Moving Forward

1. **Develop Mediterranean-specific evaluation criteria** that better reflect the region's unique needs - prioritizing ecological and social impact while appropriately weighting Web3 adoption criteria.

2. **Establish a Mediterranean impact measurement framework** that captures region-specific regenerative indicators relevant to Mediterranean ecosystems and communities.

3. **Enhance project onboarding and reporting support** with dedicated workshops, templates, and one-on-one assistance to improve both participation and impact documentation quality for new projects.

4. **Expand local engagement** by leveraging the successful projects from this round as ambassadors to bring more regional initiatives into the Web3 regenerative ecosystem.

5. **Consider adjusting the impact/COCM weighting** based on round learnings - potentially increasing the impact evaluation component for more established projects.

Thanks for all the sponsors (@owocki, Celo Public Goods, Ma Earth & ReFi Mediterranean), round operators (myself and Antonio @regenavocado, with good support from @MontyMerlin) and all the projects participating for making it happen! 💫

-------------------------

mmurthy | 2025-05-13 18:46:06 UTC | #3

Huge thanks to you @MontyMerlin for putting together such a comprehensive retro. I got to see the entire process along with evaluation first hand and I must say, you did an incredible job! And thank you for working so closely with our team at Karma GAP to help make it all work.

Seeing the Common Impact Data Standard come to life inside Karma GAP, and then plugged into an AI + human evaluation loop, is exactly the kind of composable, regenerative infrastructure we’ve all been dreaming about. It was great to see it in action. As you said, there's lot more to build but I feel we are moving in the right direction.

After closely following QF model for a long time, I felt this hybrid ImpactQF model struck a great balance, it uplifted high-impact projects that might’ve been missed in a traditional QF round while still honoring grassroots support. The results speak for themselves.

Can’t wait to keep building with you to make this stack more powerful, automated, and accessible for communities everywhere. Looking forward to continuing our collaboration and experimentation!

-------------------------

MontyMerlin | 2025-05-27 11:09:20 UTC | #4

https://gov.gitcoin.co/t/regen-rio-de-janeiro-gg23-full-program-report/20423

-------------------------

MontyMerlin | 2025-06-06 14:30:58 UTC | #5

Deepgov Allocations & Update --> https://hub.regencoordination.xyz/t/regen-coordination-x-ai-impactqf-gg23-deepgov-bonus-allocation-announced/241

As an **experimental final step** , Regen Coordination partnered with [**DeepGov**](https://allo.deepgov.org/) to allocate a **$6,000 bonus matching pool** using their new system of **AI Politicians** — autonomous agents designed to simulate capital allocation from different political and value-aligned perspectives.

Full results and analysis 👇

https://hub.regencoordination.xyz/t/regen-coordination-x-ai-impactqf-gg23-deepgov-bonus-allocation-announced/241

-------------------------

Donny_Jerri | 2025-06-06 15:46:11 UTC | #6

This is lovely.  Thank you for the informative and well structured report.  I have especially appreciated the AI integrations both for assessment and feedback.  I feel like this could be a huge unlock for funders and founders alike, giving concise information and analysis is often difficult. It can also be expensive, I know how much I charge for my time and advice.  This has the potential to accelerate many projects pointing out possible blind spots for builders, while giving an easier way to digest and assess for funders looking to fund what matters to them.  

Really well done!

-------------------------

AleVerde | 2025-06-16 14:36:34 UTC | #7

Thank you all for the incredibly thorough evaluation work you did during GG23. @ReFi_PACA participated in the ReFi Mediterranean round and from the results and feedback we can say that the depth and rigor of your assessment is honestly remarkable - it's clear how much effort and care went into providing such detailed, constructive feedback.

Getting this kind of comprehensive guidance is really helpful to level up our approach. Also, it's always such a good feeling to receive recognition for the foundation are building, while also getting clear recommendations for improvement. 

The insights provided are already shaping how we're planning our next steps at @ReFi_PACA to strengthen our role as connector between local PACA initiatives and the broader ReFi ecosystem.

Based on your feedback, we're moving forward with concrete actions aligned with Regen coordination Northstar: launching our Mediterranean regenerative actors mapping project to systematically identify and onboard local ecological initiatives into Web3, developing robust impact measurement frameworks for bioregional projects, and preparing DeFi4Nature , a side event during EthCC Cannes as our flagship event to increase awareness and adoption of web3 tools for ReFi and BioFi .

Your evaluation highlighted the importance of going beyond community building to measurable outcomes for each action- this is what we're aiming at through our structured roadmap for supporting 5+ local projects with Web3 tools by end of 2025. 

Thank you for helping us amplify our local, regional, and global impact with such strategic clarity, and in coherence with the global ReFi ecosystem!

-------------------------

dustyoldduke | 2025-06-30 04:43:25 UTC | #8

I fully support Gitcoin’s ambitious direction toward integrating AI with ImpactQF for regenerative funding. This innovative approach offers great potential in streamlining impact evaluation and aligning resources with measurable outcomes. However, upon reviewing the implementation, I believe there are several structural weaknesses in the current model that need to be addressed to ensure it delivers truly equitable and meaningful results.
1. Limitations in Measuring Impact

Issue:
The reliance on AI for evaluating projects introduces significant challenges in measuring qualitative impacts such as community cohesion or the preservation of indigenous culture. AI, by nature, struggles to quantify values that are not easily represented by numbers, thus potentially overlooking important aspects of a project’s influence.

Suggested Improvement:
To address this, I recommend introducing a multi-dimensional evaluation framework that combines both quantitative AI-driven analysis and qualitative community feedback. Local experts and community-driven insights should be integrated into the evaluation process to ensure the impact of social and cultural aspects is not overlooked. Incorporating these perspectives will allow us to capture a fuller picture of a project's impact.
2. AI Bias and Training Data Limitations

Issue:
The training datasets used for AI models tend to be heavily skewed towards Western-centric data, leading to biases when evaluating projects in the Global South. For instance, agricultural projects in Africa may be unfairly penalized for a lack of technological maturity, ignoring local context and challenges.

Suggested Improvement:
To mitigate this, region-specific evaluation criteria should be developed. AI models must be trained on a more diverse range of global contexts, and evaluations should incorporate local knowledge to ensure fairer assessments. Additionally, human evaluators with regional expertise should cross-check AI-generated results to ensure that local realities are properly accounted for in the final evaluation.
3. ImpactQF Funding Allocation Flaws

Issue:
The hybrid model of ImpactQF, while a step in the right direction, still skews resources toward projects with larger donor networks, potentially sidelining smaller initiatives with higher local or social impact. This creates a paradox where impactful grassroots projects receive less funding, even though they may be critical to achieving long-term systemic change.

Suggested Improvement:
To address this, I recommend differentiating funding allocation to ensure that small-scale innovation is not left behind. We need to create mechanisms that prioritize impact first, rather than merely rewarding projects based on the size of their donor network. Smaller projects should receive sufficient support to scale and make a difference. A flexible funding approach that allows for both large-scale and grassroots projects to thrive is essential.
4. Governance Vulnerabilities and Transparency

Issue:
The current lack of transparency around AI algorithms and their implementation creates a "black-box" scenario where the logic behind funding decisions is unclear. This opens the door for potential manipulation or biased decision-making, as well as diminishing community trust in the process.

Suggested Improvement:
To ensure fairness and transparency, the evaluation algorithms should be open-source and auditable. This will allow the community to verify the processes and ensure that AI is working within ethical boundaries. Moreover, a decentralized governance model should be developed where community members can review and challenge funding decisions, ensuring that human oversight is a fundamental part of the evaluation process.
5. Neglecting Regional Context

Issue:
AI-driven evaluation models are often based on standardized criteria that fail to account for local context and cultural differences. For example, a Mediterranean ecosystem restoration project may be evaluated against metrics designed for Northern European projects, leading to inaccurate assessments.

Suggested Improvement:
Incorporate contextual evaluations that reflect the unique challenges faced by projects in different regions. For example, localized evaluation rubrics that prioritize social and ecological impact over standard Web3 adoption criteria would better suit the diverse goals of regenerative projects across the world. Multilingual support and region-specific evaluation metrics should be integrated to ensure fair and accurate assessments.
Conclusion

While the AI ImpactQF model holds great promise, its current framework requires several critical adjustments to ensure that it addresses the complex, diverse, and decentralized nature of regenerative projects. By enhancing transparency, mitigating AI bias, and incorporating local expertise, we can create a more equitable, inclusive, and impactful funding model that aligns with the values of the Ethereum ecosystem and the global regenerative movement.

I believe these adjustments will ensure that Gitcoin continues to lead as a pioneering platform for funding public goods, while fostering a more inclusive, decentralized, and equitable ecosystem for all builders.

Final Thought:
The proposed changes are not about undermining the value of AI in funding allocation, but rather about enhancing the AI’s ability to make human-centric decisions that reflect the full complexity of social and ecological systems. By incorporating these changes, Gitcoin can stay ahead of the curve and continue to build a truly sustainable and impactful ecosystem for public goods funding.

-------------------------

MontyMerlin | 2025-07-07 10:53:35 UTC | #9

# Regen Coordination GG23 - Community Feedback Report

This feedback report synthesizes responses collected from participants and applicants across all three Regen Coordination GG23 rounds—Regen Coordination Global, ReFi Mediterranean, and Regen Rio de Janeiro. Feedback was gathered via a dedicated [Tally form](https://tally.so/r/31xlKb), where respondents were invited to rate their experiences regarding the application process, the fairness of outcomes, the quality of communication and support, and the overall program. In addition to quantitative ratings, the form solicited rich qualitative feedback, including reasons for their ratings, suggestions for improving the Gitcoin and Karma GAP experience, comments on impact reporting and evaluation processes, and any other ideas or reflections participants wished to share. This report aims to cluster and synthesize these insights to inform future improvements and highlight key themes emerging from the community’s experience.

## **Overview Summary**

### **Regen Coordination Global**

- **Number of responses:** 9
- **Average Score:** 4.65 / 5
- **Breakdown:**
-- **The application process:** 4.8
--  **The fairness of outcome:** 4.3
-- **The communication and support:** 4.7
--  **The overall program:** 4.8

Most participants rated the Regen Coordination Global round very highly across all categories, highlighting a well-documented program, clear communication, and strong support from organizers. Respondents appreciated the clarity of expectations and the resources provided for both donors and grantees. However, some concerns were raised about the fairness of outcomes, particularly regarding the COCM (Community of Communities Model) and Quadratic Funding mechanisms. One participant felt that these systems could be manipulated by coordinated groups or fake accounts, potentially disadvantaging genuine projects and creating “donor fatigue.” Despite this, the majority of feedback was positive, with participants noting the transparency, helpfulness, and overall effectiveness of the program.


### **ReFi Mediterranean**

- **Number of responses:** 1
- **Average Score:** 5 / 5

With only a single response, all aspects of the ReFi Mediterranean round received perfect scores. While this is a positive indicator, more responses would be needed to draw representative conclusions or identify specific themes.

### **Regen Rio de Janeiro**


- **Number of responses:** 5
- **Average Score:** 4.7 / 5
- **Breakdown:**
-- **The application process:** 4.6
--  **The fairness of outcome:** 4.6
-- **The communication and support:** 4.8
--  **The overall program:** 4.8

Participants in the Regen Rio de Janeiro round also gave high marks, especially for communication, support, and the overall program. Respondents described the experience as inspiring, with strong community engagement and effective support from organizers. The timely delivery of resources and the organization of follow-up activities were particularly appreciated. Some feedback pointed to areas for improvement, such as occasional confusion in the process, communication issues among round operators, and the need for better onboarding and security protocols for new users unfamiliar with Web3 wallets. Overall, the round was seen as transparent, fair, and impactful, with a few suggestions for enhancing clarity and user support in future rounds.

---

**Now moving on to deeper thematic analysis of the richer qualitative feedback also provided from respondents in the feedback form:**

## **1. Application Process & User Experience**

**Positive Feedback:**

- Many respondents found the application process clear, well-documented, and user-friendly.
> *“It was a well documented program with all the resources for donors and grantees to make informed decisions every sep of the process”*
> *“Overall very user friendly and great support!”*

**Areas for Improvement:**

- Some found the process confusing or inaccessible, especially for those less familiar with Web3 or digital tools.

>  *“I couldn’t quite figure any of that out which is one of the reason’s I didn’t apply… that and knowing that because our community doesn’t have that strong of a crypto presence… the amount of work required for the potential payout would just not make the numbers line up.”*

**Suggestions:**

- Improve onboarding, navigation, and language support (especially for non-English speakers).

> *“It’s still too early to say, but my feedback is mainly about making the platform more accessible to Portuguese-speaking users. I noticed that there is no support for Portuguese.” (translated)*

- Make the process more accessible for analog, global south, and non-Web3 native participants.

---

## **2. Fairness, Evaluation, and Outcome Perception**

**Positive Feedback:**

- The majority of participants felt the process was fair, transparent, and balanced.
> *“It was a very detailed process with multiple layers of evaluation, a balanced approach.”*
> *“The team organized multiple support rounds and were very efficient… really transparent, consistent and fair with the outcome.”*

**Critical Feedback:**

- Others expressed perceived bias or issues with the evaluation criteria.
> *“The current impact reporting and evaluation process doesn’t feel entirely fair. It often favors those who are more experienced in framing their work in technical or metrics-heavy language, rather than those actually creating meaningful on-the-ground impact.”*
> *“Rated a 2 in the fairness of outcome because of an expressed lack of faith in the COCM mechanism”*

**Concerns Raised:**

- The process may favor projects skilled in digital/metrics-heavy reporting over grassroots, analog, or less technical projects.
- Potential for conflicts of interest (e.g., council members with projects in their own rounds).
- Risk of competition and “popularity contest” dynamics, rather than true impact assessment.

**Suggestions:**

- Increase contextual understanding and diversity in evaluation panels.
- Separate governance and grantee/operator roles to avoid conflicts of interest
- Consider anonymizing projects during voting to reduce bias and focus on project qualities.

---

## **3. Karma GAP Platform & Impact Reporting**

**Positive Feedback:**

- Many found the platform useful for tracking and reporting impact.

> *“everything was clear and well articulated, no surprises what we were being judged on and our impact”*

**Critical Feedback:**

- Some found Karma GAP difficult to use and identified bugs in the software + difficulty in tracking non-digital or ecosystem work.
> *“Karma GAP needs significant improvements before it can be considered a mandatory tool. It is difficult to track ecosystem work outside the main GitHub or DAO tools.”
> *“Karma GAP was a bit clunky to fill out metrics. Also there were sometimes many similar indicators in the dropdown menu/autocomplete, which may or may not be suitable. A lack of consistency makes it hard to compare metrics like for like.”**
> *“Often it feels like it takes more time to prove impact than to make impact, which does not make sense. A new system should be created.”*

**Suggestions:**

- Improve UI/UX, onboarding, and navigation.
- Add features for better status updates and progress tracking for projects. 
- Automate impact proofs and reduce the reporting burden, especially for intangible or qualitative impact. 

---

## **4. Communication & Support**

**Positive Feedback:**

- Many praised the support and communication from organizers.
> *“The guys were always available to assist, if we had questions or needed help, the communication was as clear as daylight, especially as to how the money would be paid out.”*
> *“The team organized multiple support rounds and were very efficient of organizing everything.”*

**Areas for Improvement:**

- Some noted occasional confusion or communication breakdowns.
- “houve alguns ruidos na comunicação entre os operadores do Round que atrapalharam o entendimento geral.”

**Suggestions:**

- Provide more real-time updates and status tracking for projects and donors.

> *“Would be nice to keep donors better informed as the round progresses - not sure how we could automate round updates? For example, crowdfunding apps let you send emails to all your donors.”*

---

## **5. Inclusivity, Diversity, and Accessibility**

**Concerns:**

- The process may unintentionally exclude analog, grassroots, or global south projects, and those not engaging with AI or digital tools.

> *“I would recommend that you guys ensure that you have analog, global south participants when you decide how to frame future rounds and also that you provide some kind of parity for projects who are choosing not to engage with AI.”*

**Suggestions:**

- Broaden accessibility and support for non-digital, non-English, and less technical participants.
- Ensure evaluation criteria and processes are inclusive of diverse types of impact and project approaches.

---

## **6. Quadratic Funding, COCM Algorithm, and Voting Dynamics**

**Critical Feedback:**

- Concerns about the COCM algorithm and QF mechanisms leading to unintended consequences:

> *“Encouraging donors to vote for more projects creates the opposite effect of Gitcoin growth. It creates ‘Donor Fatigue’ making it harder for voters, making them put more money when they really do not want to, and discouragement of the more genuine, ethical and honest projects / stewards / donors.”*

**Suggestions:**

- Re-evaluate the goals and outcomes of the COCM system.
- Consider mechanisms to reduce gaming, donor fatigue, and to better align incentives with genuine impact.

---

## **7. Security, Resource Management, and Onboarding**

**Suggestions:**

- Provide security protocols and onboarding for new users, especially those unfamiliar with Web3 wallets and resource management.

> *“My suggestion is to create security protocols for the projects to follow as soon as they receive the resource, directing them to a possible off-ramp with security.”*

---

## **8. General Praise and Encouragement**

- Many respondents expressed gratitude, appreciation, and encouragement for the organizers and the process.
> *“Congrats for this beautiful work, is very important support who is invisible for the system, but do a great impact for every one.”*
> *“keep up the good work!”*

---

## **9. Meta-Reflection: Tensions and Trade-offs**

- There is a recurring tension between digital/metrics-based evaluation and the recognition of intangible, qualitative, or grassroots impact.
- The need for both transparency and inclusivity, and for systems that are robust against manipulation but not overly burdensome or exclusive.
- The challenge of scaling impact evaluation while maintaining trust, fairness, and community alignment.

---

# **Feedback Summary Table**

| Theme | Positive Feedback | Critical Feedback / Concerns | Suggestions / Requests |
| --- | --- | --- | --- |
| Application Process & UX | Clear, user-friendly for some | Confusing, inaccessible for others | Better onboarding, navigation, language support |
| Fairness & Evaluation | Transparent, balanced for some | Perceived bias, favoring digital/metrics | Diverse panels, anonymized voting, separate roles |
| Karma GAP & Impact Reporting | Useful for some | Buggy, unintuitive, hard for non-digital | UI/UX improvements, automation, easier editing |
| Communication & Support | Responsive, clear | Occasional confusion | More real-time updates, status tracking |
| Inclusivity & Accessibility | - | Excludes analog, non-English, grassroots | Broaden accessibility, inclusive criteria |
| QF/COCM & Voting | - | Manipulation, donor fatigue, misaligned incentives | Re-evaluate mechanisms, reduce gaming |
| Security & Onboarding | - | - | Security protocols, onboarding for new users |


# **Conclusion**

The feedback from GG23 Regen Coordination participants reveals a vibrant, committed community with a strong desire for fairness, inclusivity, and meaningful impact. While many aspects of the process are praised, there are clear calls for improvements in accessibility, evaluation fairness, platform usability, and the alignment of funding mechanisms with real-world impact. Addressing these themes will help strengthen trust, participation, and the overall effectiveness of future rounds.

-------------------------
