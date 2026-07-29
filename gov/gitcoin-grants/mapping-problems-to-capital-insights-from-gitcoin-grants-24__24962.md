---
id: 24962
title: "Mapping Problems to Capital: Insights from Gitcoin Grants 24"
slug: mapping-problems-to-capital-insights-from-gitcoin-grants-24
category: gitcoin-grants
url: https://gov.gitcoin.co/t/mapping-problems-to-capital-insights-from-gitcoin-grants-24/24962
created_at: 2025-12-19T12:00:31.726Z
last_posted_at: 2025-12-19T12:00:31.871Z
posts_count: 1
views: 106
like_count: 2
---

# Mapping Problems to Capital: Insights from Gitcoin Grants 24

<https://gov.gitcoin.co/t/mapping-problems-to-capital-insights-from-gitcoin-grants-24/24962>
rohit | 2025-12-19 12:00:31 UTC | #1

(*With guidance and feedback from @ccerv1*)

**TL; DR: Who is this for?**

This analysis examines how funding in Gitcoin Grants Round 24 flowed from ecosystem problems to projects and whether community allocations aligned with priorities identified through domain sensemaking.

* **Domain allocators and operators:** Use this to see where capital allocation reliably reflects ecosystem priorities and where it structurally underfunds critical work, so you can adjust problem framing and mechanism choice in future rounds

* **Funders and institutional backers:** Use this to identify ecosystem-critical dependencies that crowdfunding does not cover well, and deploy capital upstream of donor sentiment to close structural gaps

* **Donors and community:** Use this to understand how individual donations aggregate at the problem level, and to donate more intentionally across visible projects and less legible but high-leverage infrastructure

* **Domain experts and stewards:** Use this as a shared evidence base to interrogate funding patterns, test assumptions, and guide deeper sensemaking, roadmap design, and curation discussions.

> Explore the full data and interactive visualisations on the **[GG24 Analysis Portal](https://gg24-analysis.fly.dev)**

## Why This Analysis Exists

Gitcoin Grants Round 24 (GG24) is Gitcoin’s largest experiment in problem-first public goods funding. Each domain utilised sensemaking to identify ecosystem-level gaps and the problems it aims to solve. This analysis assesses whether the funded projects addressed the most significant, pressing, and solvable problems identified through that process.

The analysis answers three questions:

* **What are Ethereum’s most important problems?** Defined through sensemaking by each domain (stakeholder interviews, ecosystem analysis, and domain expertise).

* **What projects are most relevant to those problems?** Each project’s context is evaluated by an LLM against the full problem catalogue for the round to assign one primary and one secondary problem alignment.

* **What does the crowd think is the optimal funding portfolio across those projects to achieve maximum impact?** Revealed through actual funding allocations.

The analysis visualises how GG24’s funds map to projects and their respective problems, providing evidence that Gitcoin’s sensemaking-driven model surfaced the right problems; however, quadratic funding alone does not reliably ensure coverage of ecosystem-critical work, particularly where impact is long-horizon, coordination-heavy, or difficult to narrate at the project level.

By tracking funding flows from problem areas to individual projects, and showing which problems received the most capital relative to project engagement, we can see whether community funding decisions are aligned with the strategic priorities identified through sensemaking.

> **This creates a feedback loop: did the problems we identified as most critical actually attract the funding needed to solve them?**

## What’s Included

The **[Alignment Dashboard](http://gg24-analysis.fly.dev/)** makes problems, projects, and capital legible in one place to enable ecosystem-level reasoning, not just round retrospectives.

For each GG24 round (with allocations completed), the analysis provides:

* **Problem definitions:** View full statements, solution shapes, and measurement rubrics that define the round’s priorities derived from sensemaking

* **Project Alignment & Funding Summary table:** Sort by funding amount to identify top-funded projects and their problem alignments

* **Problem Funding Distribution:** Compare project alignment vs. funding allocation across problems

* **Funding Flow:** Trace funding from problem areas to individual projects; use the problem filter to focus on specific areas

Cross-domain analysis:

* **Ethereum Problem Space Mapping:** Explore how round-specific problems map to broader ecosystem challenges in Ethereum

This analysis is an invitation to examine system-level patterns that emerge only when we zoom out. It is not:

* A critique of any domain, round, or project

* An evaluation of “deservingness”

## Invitation for Feedback and Ongoing Sensemaking

Some design choices in this analysis, such as translating domain sensemaking documents into round-specific problem catalogues and aligning projects to problems, rely on AI-assisted methods. We welcome feedback from round operators, domain SMEs, and project teams to refine problem definitions, improve project-to-problem mappings, and surface additional questions this analysis should explore. Feedback can be shared here on the forum or via the [data portal’s](https://gg24-analysis.fly.dev/) feedback form for specific observations.

## Key Findings

### Dev Tooling & Infrastructure (QF)

Overall, the round demonstrates that QF is highly effective at surfacing community preference and perceived usefulness, but less effective at ensuring coverage of ecosystem-critical work with delayed or indirect impact. This is not a failure of execution, but a signal that mechanism choice must track problem maturity and payoff timelines.

![Dev Tooling](upload://lfYimGhG36ie13vZqxCL4ICXt3J.png)

> The round shows QF performing well as a discovery layer for visible, risk-reducing tooling and a pressure valve for known OSS sustainability gaps. **It performs poorly as a primary mechanism for long-horizon protocol work and deep infrastructure maintenance at the ecosystem scale.**

[details="Click to review detailed findings for the round"]
1. **Funding concentrates on a small set of visible, end-user–facing tools**

A disproportionate share of total funding flowed to projects with strong brand recognition, clear user touchpoints, or obvious donor utility (e.g., wallets, explorers, user safety tools). These projects consistently reached or approached the matching cap, even when their scope was narrower than foundational infrastructure projects. This suggests that donor behaviour in QF continues to favour legibility and immediacy of impact over structural criticality.

2. **Core infrastructure and protocol-adjacent work remain under-rewarded**

Projects working on Ethereum’s foundational layers (clients, languages, protocol-adjacent tooling, and long-term maintenance) received significantly lower total funding relative to their ecosystem importance. This pattern reinforces a persistent gap between ecosystem necessity and crowdfunding outcomes.

3. **Developer experience improvements underperformed relative to expectations**

Several widely respected developer-experience projects landed well below the matching cap, despite:

* High dependency usage across the ecosystem

* Alignment with onboarding, usability, and productivity goals

* Strong endorsement from subject-matter experts

This indicates that incremental or infrastructural DX improvements struggle to compete with tools that offer direct, user-visible benefits, even when DX work compounds ecosystem capacity over time.

4. **Average donation size varies sharply by problem type**

Problem areas associated with long-term sustainability and core infrastructure show higher average donations but fewer participating donors, while UX-oriented or safety-focused categories attract broader participation with smaller individual contributions. This suggests two distinct donor profiles operating simultaneously:

* A smaller cohort of informed donors backing structural work

* A larger cohort responding to familiarity, narrative clarity, and personal utility

QF amplifies the latter more effectively than the former.

[/details]

### Interop Standards, Infrastructure & Analytics (QF)

The capital distribution suggests that the ecosystem broadly agrees on what matters, but not when and how to fund it. Crowdfunding efficiently supports observability, experimentation, and early validation. It struggles to underwrite the infrastructural commitments that must precede or outlast visible adoption milestones.

![Interop](upload://qkEG7PxsPqg8gmgHIobnksxtPLO.png)

> **Interop’s most critical dependencies, therefore, require complementary funding paths that operate upstream of donor sentiment.**

[details="Click to review detailed findings for the round"]
1. **Donors reward epistemic clarity more than coordination completeness**

Across the round, funding concentrates around problems that improve the ecosystem’s ability to see itself clearly (metrics, visibility, analytics), rather than those that improve its ability to act coherently (coordination infrastructure). This suggests that, in crowdfunding contexts, donors prioritise work that reduces uncertainty and improves legibility, even when downstream coordination depends on deeper, less visible infrastructure.

2. **Intent-based architectures attract conviction, not mass participation**

Work aligned with intent-based architectures exhibits strong donor confidence per contribution, but does not mobilise broad participation. This pattern indicates that intents are currently understood and supported by a relatively small, informed audience rather than the wider donor base. In practice, this positions intent adoption as a belief-led bet, not yet a community-wide consensus, despite its prominence in roadmap discussions.

3. **Standards work occupies a “necessary but insufficient” middle ground**

Interop standards neither strongly outperform nor collapse across funding dimensions. They receive steady support, but rarely decisive backing. This points to a structural issue: standards are widely acknowledged as important, yet struggle to generate urgency or differentiation in a donor-driven environment where impact is evaluated project-by-project rather than system-by-system.

4. **Coordination problems fragment capital rather than attract it**

Problems framed around coordination draw multiple project attempts but fail to concentrate funding behind shared primitives or approaches. This implies that donors recognise coordination as a challenge, but lack shared heuristics for evaluating which coordination solutions are credible. As a result, capital disperses across competing interpretations rather than reinforcing common infrastructure.

5. **Deep coordination infrastructure lacks narrative leverage**

The weakest funding outcomes occur where the work is both foundational and difficult to narrate in isolation. Multi-chain coordination infrastructure appears structurally disadvantaged, not due to lack of importance, but due to weak standalone narratives, limited donor familiarity, and long feedback loops. This is less a signal of donor disinterest and more a signal of mechanism mismatch.

[/details]

### Privacy

The ecosystem strongly signals support for “default privacy” as a goal, but funding patterns imply it is approached through applications, tooling, and UX, rather than sustained investment in the lower layers that would make default privacy cheap, composable, and universal. Crowdfunding struggles to underwrite the infrastructural commitments that must precede mass privacy by default.

![Privacy](upload://311ZU2UtY6klPM2LjiRmz4FN5dh.png)

> **This creates a structural risk: enthusiasm for privacy defaults without commensurate investment in the systems that must underwrite them.**

[details="Click to review detailed findings for the round"]
1. **Privacy funding rewards reach and translation more than cryptographic depth**

Capital concentrates around problem areas that translate privacy into accessible narratives (education, default privacy framing) rather than those that push the technical frontier (ZK primitives, identity systems). This suggests that, within participatory funding, privacy is valued primarily as a social capability to be understood and adopted, not yet as a technical substrate to be deeply invested in.

2. **ZK infrastructure sits in a credibility gap, not a relevance gap**

Zero-knowledge infrastructure attracts meaningful funding, but not decisively more than narrative-oriented categories. This suggests donors recognise ZK as necessary, but struggle to evaluate which ZK investments are foundational versus exploratory. The result is cautious support rather than concentrated conviction, reflecting an evaluation problem more than a prioritisation problem.

3. **Privacy applications face a classic adoption trap**

Application-level privacy work shows weak funding intensity relative to participation. This indicates a familiar tension: donors want privacy to be used, but are unconvinced by early applications that adoption will compound without upstream shifts in defaults, identity, or infrastructure. In effect, applications are penalised for ecosystem constraints they do not control.

4. **Identity and governance privacy remain structurally under-articulated**

Privacy-preserving identity and private governance attract modest support despite being prerequisites for credible onchain coordination, voting, and reputation. This suggests these problem areas suffer from diffuse ownership: they matter systemically, but lack a clear “who benefits first” narrative that motivates donor urgency.

5. **Education functions as the ecosystem’s risk-reduction mechanism**

Privacy education and field building perform disproportionately well because they reduce cognitive and social risk for donors. Funding education is a way to express support for privacy without having to take a stance on specific architectures, protocols, or threat models. In this sense, education absorbs uncertainty that the rest of the stack has not yet resolved.

[/details]

## Sensemaking Prompts for Domain Stakeholders

The prompts below are intended as focused prompts for domain stakeholders to examine patterns observed in the data. They are not conclusions or critiques. Each inquiry highlights areas where funding distribution appears counterintuitive and should be read as an invitation for deeper sensemaking:

### Dev Tooling (QF)

#### Prompt 1: Why Are Certain Problem Types Persistently Underfunded?

**Finding**
In this round, the problem category “Scalability & Protocol Evolution” received extremely low total funding, despite being a historically critical concern for Ethereum.

This category encompasses work on clients, languages, rollup tooling, data availability systems, statelessness, account abstraction, and protocol readiness. Even with limited competition within the category, donor engagement remained minimal.

[details="Click to see more details"]
**Why is this surprising?**
These problem areas are foundational to Ethereum’s long-term viability, yet they appear consistently deprioritised in QF outcomes.

**Follow-up questions**

* Are these problems implicitly perceived as “someone else’s responsibility” (e.g., Ethereum Foundation or core protocol teams)?

* Are these problem types structurally misaligned with QF’s strength in surfacing community sentiment and visible impact?

* Does long time-to-impact reduce donor willingness, even when strategic importance is high?

**Possible actions**

* Formally distinguish ecosystem-critical but low-visibility problem types from community-facing problems in a new sub-domain

* Route such categories toward alternative mechanisms

[/details]

#### Prompt 2: Why Did Foundational Developer Experience Projects Underperform the Matching Cap?

**Finding**
Viem, Argot Collective, and Scaffold-ETH Mobile each landed at well under 30% of the matching cap, despite sitting close to the daily workflow of Ethereum developers. These projects underpin core aspects of developer experience, from language tooling to application scaffolding and mobile onboarding.

[details="Click to see more details"]
**Why is this surprising?**
If developer experience is considered a strategic priority, tools that developers rely on daily would be expected to attract stronger funding signals.

**Follow-up questions**

* If widely used developer tools consistently underperform in QF, is this a signal about project quality, donor behaviour, or the limits of the mechanism itself?

* Are primary beneficiaries (developers) systematically less likely to donate compared to end-user or community-facing audiences?

* Should foundational DX projects be expected to actively market themselves, or does this select for the wrong behaviours?

**Possible actions**

* Treat foundational developer experience similarly to core infrastructure: less reliant on donor mobilisation, more on expert, usage-based, or operator-curated signals.

[/details]

### Interop Standards, Infrastructure & Analytics (QF)

#### Prompt 1: Why Does Funding Concentrate on Visibility Rather Than Coordination Infrastructure?

**Finding**
A disproportionate share of funding flowed to projects improving ecosystem visibility and measurement, such as L2Beat, GrowThePie, and other analytics- and dashboard-oriented efforts, while projects focused on multi-chain coordination infrastructure received materially lower funding.

By contrast, work aimed at shared coordination primitives and execution-layer infrastructure, such as cross-chain messaging, routing, or coordination frameworks, failed to attract comparable funding depth, despite being prerequisites for durable interoperability.

[details="Click to see more details"]
**Why is this surprising?**
Coordination infrastructure underpins standards adoption, intent execution, and composable multi-chain systems. Once its importance is broadly acknowledged, one would expect these layers to attract stronger collective backing rather than being consistently outperformed by observability tooling.

**Follow-up questions**

* Are donors using analytics and dashboards as a proxy for “making progress” on interoperability, even when coordination remains unresolved?

* Does QF structurally favour work that produces immediately inspectable outputs over systems whose value emerges only through widespread adoption?

* Are coordination problems underfunded because donors lack shared heuristics for evaluating success?

**Possible actions**

* Explicitly distinguish observability from coordination primitives in future problem framing.

* Pair coordination infrastructure with concrete downstream integrations or adoption commitments to improve evaluability.
[/details]

#### Inquiry 2: Why Do Intent-Based Architectures Attract High Conviction but Low Participation?

**Finding**
Projects aligned with intent-based architectures, such as work related to ERC-7683, Open Intents–adjacent tooling, and early intent execution frameworks, exhibited relatively high average donation sizes but limited overall donor participation.

This pattern suggests strong conviction among a narrow set of informed donors, rather than broad-based engagement from the wider contributor pool.

[details="Click to see more details"]
**Why is this surprising?**
Intent-based architectures feature prominently in Ethereum roadmap discussions and ecosystem narratives. Given this prominence, one might expect broader participation rather than reliance on a small cohort of high-conviction contributors.

**Follow-up questions**

* Is the concept of intents still too abstract for most donors to evaluate confidently?

* Does early-stage architectural work require endorsement signals beyond QF to unlock wider participation?

**Possible actions**

* Treat intent-aligned work as belief-stage infrastructure, complemented by operator or institutional funding.

* Invest in clearer system-level narratives that connect intents to tangible coordination and user outcomes.
[/details]

### Privacy

#### Prompt 1: Why Does Funding Concentrate on Education and Default Privacy Narratives Rather Than Core Privacy Infrastructure?

**Finding**
A substantial share of funding clustered around projects whose primary alignment is privacy education or default-privacy framing, most notably Dev3pack – Privacy Bootcamp and WORM. In contrast, projects whose primary alignment is foundational zero-knowledge infrastructure appeared less frequently as top-funded entries, even when they served as secondary dependencies for higher-funded education and default-privacy efforts.

[details="Click to see more details"]
**Why is this surprising?**
Education and default framing lower cognitive and social barriers, but durable privacy-by-default ultimately depends on sustained investment in cryptographic infrastructure that must precede large-scale adoption.

**Follow-up questions**

* Are donors expressing support for privacy primarily through narrative- and education-led projects rather than infrastructure commitments?

* Are infrastructure-level privacy projects disadvantaged by longer feedback loops and indirect attribution?

**Possible actions**

* Explicitly distinguish privacy education & adoption from privacy infrastructure in future problem framing.

* Pair infrastructure projects with visible downstream dependencies to improve donor evaluability.
[/details]

#### Prompt 2: Why Do ZK, Identity, and Private Governance Systems Receive Recognition Without Concentrated Conviction?

**Finding**
Projects addressing zero-knowledge, identity, and private governance received meaningful but fragmented funding across multiple problem areas. Examples include Privote, ZKPassport and Fluidkey. While these projects span governance, identity, and application layers, no single effort emerged as a dominant coordination focal point for donor conviction.

[details="Click to see more details"]
**Why is this surprising?**
Zero-knowledge proofs, private identity, and private governance are widely recognised as prerequisites for credible onchain coordination and privacy-preserving systems, yet funding signals remain dispersed across adjacent implementations rather than concentrated around shared primitives.

**Follow-up questions**

* Are donors struggling to distinguish between exploratory ZK work and infrastructure ready for ecosystem-level dependence?

* Does diffuse ownership across identity, governance, and application layers dilute perceived responsibility for funding?

**Possible actions**

* Frame ZK and identity funding around shared dependency layers rather than isolated implementations.

* Complement QF with curator or expert signals to help donors coordinate conviction.
[/details]

## Conclusion
GG24 is still in motion. This analysis should be read as a checkpoint rather than a verdict. It captures early signals about how capital is currently routing across domains, what types of work attract broad participation versus concentrated conviction, and where funding dynamics appear misaligned with long-term ecosystem dependencies. In that sense, its value is prospective as much as retrospective. 

As Gitcoin moves deeper into its 3.x roadmap, the challenge is no longer just transparency of allocation, but intentional composition of funding pathways: combining community signalling with operator judgment, institutional capital, and mechanisms designed for long-horizon coordination. This analysis offers an intermediate mirror for that transition, helping inform how the remaining rounds and future iterations can better balance discovery, stewardship, and ecosystem resilience.

-------------------------
