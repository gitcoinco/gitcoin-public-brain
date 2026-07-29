---
id: 21951
title: "[GG24 DDA] Exit-to-Community"
slug: gg24-dda-exit-to-community
category: gitcoin-sensemaking-szn
url: https://gov.gitcoin.co/t/gg24-dda-exit-to-community/21951
created_at: 2025-07-16T23:59:47.069Z
last_posted_at: 2025-08-21T22:17:05.992Z
posts_count: 5
views: 2270
like_count: 14
---

# [GG24 DDA] Exit-to-Community

<https://gov.gitcoin.co/t/gg24-dda-exit-to-community/21951>
paul2 | 2025-08-21 22:27:23 UTC | #1

*This is a draft of a dedicated domain application for sensemaking created by the previous Round Operators of the Gitcoin Grants Garden: @paul2 @Oba-One @cauetomaz*

### **Problem & Impact**

One of the greatest strengths of Ethereum is its ability to help groups of people with a shared vision coordinate resources towards a common goal.

**On a macro scale,** Ethereum aims to solve global issues connected to the poor management and chronic underfunding of our shared resources, caused by our inadequate monopolistic public goods providers (governments) and their financial institutions. To do this, Ethereum first needs to build better systems for resource allocation and collective intelligence for its own ecosystem.

**On a micro scale,** communities in every realm of coordination are creating enormous amounts of value with goods and services that don't have a viable business model - i.e. "Public Goods". These organizations often struggle to resource their work, which could be far more valuable for the world with proper investment.

**This problem is exacerbated in the digital space where open source software is prolific, enormously valuable, and inherently free.**  People and organizations often depend on software that lacks the resourcing and support to grow to be as valuable as it could.

The infamous [xkcd comic](https://xkcd.com/2347/) says it all:

![dependency|385x489](upload://gth0laviVET6lI7Qj2Ew0wsKsBB.png)


To date, much of the work on solving this problem has been focused on helping funders identify critical infrastructure at the ecosystem level so they can fund it appropriately. Projects like Tea Protocol (https://tea.xyz/), Deep Funding (https://www.deepfunding.org/), and Drips (https://www.drips.network/) are all working on this approach.

However, most underserved public goods and [open source software](https://vitalik.eth.limo/general/2025/03/29/pubos.html) are *already very well known by their communities*, and are simply missing an organizational structure that lets them support their infrastructure themselves. What they really need is a viable [exit-to-community](https://hackernoon.com/startups-need-a-new-option-exit-to-community-ig12v2z73) path (made popular by @ntnsndr). A structure, with basic capabilities to accrue and hold value, that gives control of the platform and its resource allocation to its most avid users. 

**This DDA aims to address the critical gaps currently missing from the web3 open source software funding, which are projects with traction and happy users that struggle to lock down the support and resources they need for ongoing maintenance and key upgrades.**

To identify these gaps, we first considered other well-functioning funding programs in web3:

### **Proven routes for small, early stage projects**

- **Quadratic Funding / Incentivized Donation events** - Gitcoin GG1-GG23, Giveth QF, Octant
- **Hackathons** - like on [Buidlbox](https://app.buidlbox.io/) and [Devpost](https://devpost.com/hackathons)
- **Ecosystem/Protocol Grants/Fellowship Programs** - Ethereum Foundation, Protocol Guild, network ecosystem grants

### **Proven routes for large, late stage projects**

- **Tokenization** - projects with a large, passionate userbase can raise money by distributing community ownership through governance tokens. These projects can often convert this into a treasury that sustainably funds the project through yield and healthy treasury management.
- **Fees** - projects with large TVL, volume, and/or userbase can sustain themselves on fees, i.e. a freemium model, or fees small enough to be negligible for users.

### **Proven route at all stages of growth**

- **Whale Sponsorship** - altruistic contributions from the wealthiest members of the community.
    
    Drawbacks:
    
    - Requires the existence of altruistic whales in the community and centralizes control of the platform to these sponsors, creating a single points of failure for the project.
- **Privatizing -** projects that restrict access to their product to high-paying users (and upside to select investors) can join accelerator programs, get traditional Angel / VC funding, and continue raising private capital until they either fail or reach late stage growth.
    
    Drawbacks:
    
    - For many goods and services, the so-called “public goods,” this route is not an option - either because the costs related to supporting the good/service are far greater than the potential private revenue streams, or because restricting access to only users who can afford these costs significantly decreases the total value it creates for the world. 
    For example - imagine building public transportation for a city from scratch. For a private org to buy the land, build the infrastructure, and operate & maintain such a system, they’d need to charge customers way more than anyone would ever be willing to pay.

### **Existing proven models for projects within our Problem Area Scope**

- **Retroactive Public Goods Funding (RetroPGF)** - Optimism's proven model of rewarding past impact
    
    Drawbacks:
    
    - only funds past work, making it unsuitable as an investment in future builds, where a large upfront cost needs to be made with the risk of failure.
    - typically seasonal, with changing criteria each season making it hard for builders to rely on.
- **Octant -** Golem Foundation’s dedicated 100k ETH for sustainable public goods funding, which can sustainably fund projects in perpetuity.
    
    Drawbacks:
    
    - only works because Golem Foundation raised 100k ETH for another product in a time of irrational exuberance - this model can’t be reliably replicated by other projects.
- **Ongoing Ecosystem Grants / Funding proposals -** projects that show value for a specific network or ecosystem can usually go back to these organizations for more funding.
    
    Drawbacks:
    
    - centralized ecosystem grants:  fosters project dependence on the funding organization, which can decrease the quality of the projects that get funded. Grant admin also become bottlenecks for public goods growth, and often lack the direct context of the problems being solved to make good funding decisions.
    - decentralized ecosystem grants:  historically rife with abuse, gaming, and low quality decision-making.

### Sensemaking Analysis

The Greenpill Dev Guild, led by @afo and in collaboration with the Allo Alliance, has led our research in this space and have aggregated their findings in a series of articles:

- Pioneering the Regenerative Stack: https://paragraph.com/@greenpilldevguild/pioneering-a-regenerative-stack
- Capital Formation: https://paragraph.com/@greenpilldevguild/capital-formation-turning-impact-into-sustainable-revenue
- Validating the Regenerative Stack: https://paragraph.com/@greenpilldevguild/validating-the-regenerative-stack

Collectively these paint a picture of strong, diverse, growing ecosystem of mechanisms that span capital formation, capital allocation, reputation, accountability, and organizational infrastructure - all optimized for the growth of public goods organizations. 

Our key resource in this Sensemaking has been the Allo Alliance, a collection of mechanism builders embedded in these issues, sharing information and working together on solutions to common pitfalls in the space. 

You can read more about the Allo Alliance and its work here: https://paragraph.com/@greenpilldevguild/the-allo-alliance-innovating-capital-allocation-on-chain

We’ve taken our sensemaking beyond research as well, piloting an exit-to-community real world experiment for the Gardens platform using a combination of mechanisms including [Juicebox](https://juicebox.money/v4/op:34), [Flows](https://flows.wtf/gardens), [Gardens v2](https://app.gardens.fund/gardens/10/0x8b2f706cd2bc0df6679218177c56e72c5241de9b/0x59c47c30da2a0ca7359590f023da0284fef83e73), [Karma GAP](https://gap.karmahq.xyz/community/gardens-community), and [DeVouch](https://devouch.xyz/?source=gardens): https://x.com/gardens_fund/status/1929594004632752319

And over the next 2 months the Gardens team plans to experiment with other potential integrations including [Hats Protocol](https://www.hatsprotocol.xyz/), [Flow State](https://flowstate.network/), [Mezzanine](https://app.mezzanine.xyz/), [Collabberry](https://beta.collabberry.xyz/), and other mechanisms in the [Allo.Capital](http://Allo.Capital) ecosystem. 

The results of these experiments will be critical in identifying a round process with the greatest probability of success for the greatest number of projects.

### Gitcoin’s Unique Role & Fundraising

Over the last year the web3 infrastructure supporting this type of organization has improved by orders of magnitude, including:

- **Capital Formation:** Juicebox, Revnets
- **Capital Allocation:** Gardens, Flow State, Flows.wtf, Grant Ships
- **Decentralized Permissions:** Hats Protocol, Zodiac Roles, Prosperity Pass, DeVouch
- **Impact Reporting:** KarmaGAP, Bloom Network, Impact Miners

The existing network of open source software projects in the Gitcoin ecosystem, combined with Gitcoin’s shift towards a multi-mechanism ecosystem growth strategy make this the ideal problem area for Gitcoin to address.

We expect to be able to raise between $50-100k from the various organizations connected to this problem set, including our previous community round sponsors 1Hive and Celo Public Goods, and from partners and relevant mechanism funders like Allo.Capital, Juicebox, and Public Nouns.

### Success Measurement & Reflection

Impact metrics for this category:

- Quantitative:
    - Amount of funding raised + deployed
    - Project developer activity on Github
    - Project traction: DAU/MAU, TVL, transactions, etc
- Qualitative:
    - do project builders and users feel the project has become more valuable for them?
    - what other routes did they try or consider?
    - do they plan to keep using the solutions implemented?

In our previous GG23 round we found it effective to combine a [Dune Dashboard](https://dune.com/gardens_fund/gitcoin-grants-garden) and [Karma GAP](https://gap.karmahq.xyz/community/gardens-community) funding profile for quantitative impact tracking, with surveys and direct communication with participants on Telegram for qualitative impact. 

Our retrospective is available here: https://gov.gitcoin.co/t/gitcoin-grants-garden-gg23-retrospective/20720

-------------------------

jrocki.eth | 2025-07-18 01:34:14 UTC | #2

Thank you for writing this up.. this is actually the first time I have ever heard the term "Exit to Community". Very interesting.

-------------------------

MontyMerlin | 2025-08-13 11:41:24 UTC | #3

Some cool ideas in here, nice write up. I can also see some alignment with the [[GG24] Sensemaking Report: Pre & Post-Grant Coordination | From Allocation to Alignment & Accountability](https://gov.gitcoin.co/t/gg24-sensemaking-report-at-pre-post-grant-coordination-from-allocation-to-alignment-accountability/21711) sensemaking from @sepu85 

That said, I’m not entirely sure “Exit-to-Community” is the best framing for a domain in the context of Ethereum's greatest challenges. While it’s a powerful mechanism in itself, it feels a bit narrower than the broader category of challenges and opportunities this report begins to touch on.

Personally, I think a **“Web3 Capital Allocation”** domain could be really compelling. A domain focused on strengthening Ethereum’s ability to design, coordinate, and measure capital flows to high-impact projects. This could go beyond just core allocation mechanism innovation (QF, Retro, Streaming etc..) and also include the surrounding tooling, methodologies, and processes that can make web3 capital allocation ever more *effective*. This could encompass pre- and post-grant coordination systems, impact measurement and accountability tooling, capital formation models, capital routing infrastructure, and ecosystem intelligence for better funding decisions. By combining mechanism innovation with the operational and analytical layers that support it, this domain could help Ethereum move from fragmented and reactive funding toward a more intentional, data-informed, and outcomes-driven capital allocation ecosystem.

That framing might have even stronger alignment with “Ethereum’s biggest challenges” as identified in the sensemaking process, and could create a natural synergy with Gitcoin’s mission and the work Allo Capital is doing. Maybe Allo Capital could even co-fund this domain for GG24? @owocki 👀

Curious to hear others thoughts on this also:)

-------------------------

MontyMerlin | 2025-08-18 10:14:28 UTC | #4

ah, looks like @DavidDAO has gone for it!

https://gov.gitcoin.co/t/metafunding-fund-pgf-mechanisms-research-gitcoin-3-0-sensemaking-report/23024

@paul2 @Oba-One @cauetomaz could be scope for a team up?

-------------------------

deltajuliet | 2025-08-21 22:17:05 UTC | #5

### 📝 Scorecard: [Exit-to-Community – GG24 DDA Proposal](https://gov.gitcoin.co/t/gg24-dda-exit-to-community/23031)

Thanks @paul2 and team for this submission. Here's my evaluation using my [GG24 rubric](https://gov.gitcoin.co/t/gg24-domain-proposal-voting-scorecards/23016/5):

---

### ✅ Submission Compliance Check

| Criteria                     | Pass? | Notes                                                                 |
|------------------------------|-------|-----------------------------------------------------------------------|
| Word count                   | ✅    | Meets full template expectations                                      |
| Problem & Impact             | ✅    | Clear, compelling, and ecosystem-aligned                              |
| Sensemaking Analysis         | ✅    | Draws on Greenpill Dev Guild, Allo Alliance, and multiple case studies |
| Gitcoin Fit & Fundraising    | ✅    | Good fit with Gitcoin’s evolving ecosystem orientation                |
| Success Metrics & Reflection | ✅    | Mix of quant + qual; uses KarmaGAP, Dune, surveys                     |
| Domain Info                  | ⚠️    | Structured as a domain, but reads more like a multi-mechanism testbed |
| DRIs Named                   | ⚠️    | Garden team cited, but no specific operators for GG24 proposed        |


---

### 📊 Scorecard Evaluation  
**Total Score: 9 / 16**

| #  | Criteria                                             | Score | Notes |
|----|------------------------------------------------------|-------|-------|
| 1  | Problem Clarity & Relevance                          | 2     | Clearly articulates a real challenge faced by OSS and public goods teams |
| 2  | Sensemaking Approach                                 | 2     | Good grounding in the Allo Alliance, Greenpill research, real pilots     |
| 3  | Gitcoin Fit & Uniqueness                             | 2     | Tight alignment with Gitcoin 3.0 goals around modular, multi-mech funding |
| 4  | Fundraising Plan                                     | 1     | Early signals (1Hive, Celo PG, Juicebox), but no firm commitments yet    |
| 5  | Capital Allocation Design                            | 1     | Uses Juicebox, FlowState, Karma GAP, DeVouch — but details are diffuse   |
| 6  | Domain Expertise & Execution Team                    | 0     | No DRIs or ops team confirmed for GG24 round execution                   |
| 7  | Clarity & Completeness                               | 1     | Clear problem, but muddled as a domain vs coordination experiment        |
| 8  | Gitcoin Infra Support Required                       | 0     | Not clear how much infra or coordination Gitcoin would need to provide  |


---

### 🧠 Key Strengths

- A unique blend of philosophical framing (“Exit to Community”) and infrastructure experimentation.
- Embedded in the Gitcoin ecosystem and builds directly on previous round learnings.
- Deeply aware of tooling gaps, dependencies, and the ecosystem’s historical pain points.
- Strong alignment with Gitcoin’s *multi-mechanism*, *public goods*, and *capital innovation* focus.

---


---

### 🟡 Recommendation
**Mark as: Eligible — with reservations**

- If this moves forward, the proposers should:
- Clarify DRIs and execution responsibilities for GG24  
- Publish a minimal roadmap of October deliverables  
- Tighten scope around 1–2 testable capital allocation flows  

---

### 📝 Notes
- This could become a valuable coordination experiment for Gitcoin’s broader capital allocation ecosystem, especially when paired with the MetaFunding domain.
- Eligibility could shift if the domain framing becomes too diffuse or overlaps significantly with MetaFunding or Mechanism Builders.
- While this meets the structural criteria of a domain proposal, it frames itself around a *mechanism* ("Exit-to-Community") rather than a clear *problem domain*. It overlaps significantly with stronger proposals like **Metafunding** and **Mechanism Builders**, and may be better positioned as a subdomain, coordination experiment, or part of a broader capital allocation strategy. Eligible, but not strategically differentiated.

-------------------------
