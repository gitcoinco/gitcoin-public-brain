---
id: 22966
title: "GG24 Sensemaking Report: DeFi Transparency and Decentralization Assessment"
slug: gg24-sensemaking-report-defi-transparency-and-decentralization-assessment
category: gitcoin-sensemaking-szn
url: https://gov.gitcoin.co/t/gg24-sensemaking-report-defi-transparency-and-decentralization-assessment/22966
created_at: 2025-08-14T11:32:46.798Z
last_posted_at: 2025-09-16T05:54:29.378Z
posts_count: 6
views: 2305
like_count: 9
---

# GG24 Sensemaking Report: DeFi Transparency and Decentralization Assessment

<https://gov.gitcoin.co/t/gg24-sensemaking-report-defi-transparency-and-decentralization-assessment/22966>
MarcVlad | 2025-08-19 23:55:54 UTC | #1

**TL;DR:** This sensemaking report proposes a Gitcoin GG24 domain, "DeFi Transparency & Decentralization Assessment" (or "DeFi Curation"), to fund open-source tools, standards, and education for evaluating DeFi protocol maturity and risks via quadratic/retroactive funding, sub-rounds, and expert involvement from DeFiScan, L2Beat, and more /decentrlization/cybersecurity researchers. It addresses the "decentralization illusion" in DeFi—where protocols claim decentralization but harbor hidden central risks like admin keys and unverified contracts.

**Problem & Impact** 

The specific Ethereum problem we are addressing is the lack of a standardized, verifiable framework for assessing decentralization and maturity levels of DeFi protocols.

Many DeFi applications claim to be "decentralized," but in reality, they often rely on centralized components such as admin keys, points of failure in governance, oracles, collaterals, or opaque smart contract implementations. This creates a "decentralization illusion," where users believe they benefit from censorship-resistance and other decentralization advantages, but are actually exposed to hidden risks, such as centralized custody, unverified contracts, or a lack of protection against unwanted upgrades.

This issue is becoming increasingly important over time due to the explosive growth of DeFi on Ethereum and its ecosystems. As of August 2025, DeFi's total value locked (TVL) has reached approximately $150 billion. Decentralized finance is experiencing significant growth and is a particularly innovative sector, but the decentralized aspect has been overlooked. This could be mitigated or avoided through proactive decentralization assessments, as these tools highlight hidden central points of centralization. For instance, protocols with upgradable contracts or oracle dependencies often fail visibility checks, contributing to billions in avoidable losses over time.

Most community members who are not here for speculation have similar concerns. Vitalik warned us in [Cannes](https://www.youtube.com/watch?v=zo72TWXrc3Y) (and many times elsewhere) that [Ethereum risks failure if decentralization becomes merely a catchphrase without concrete guarantees](https://www.coindesk.com/tech/2025/07/02/the-protocol-ethereum-s-vitalik-buterin-says-the-ecosystem-is-at-risk-if-decentralization-is-just-a-catchphrase). KPMG also [reports](https://kpmg.com/xx/en/our-insights/regulatory-insights/defi-and-the-decentralisation-illusion.html) that DeFi's "decentralization illusion" amplifies risks in areas like smart contract security, questioning the true extent of decentralization in many protocols.

**Meaning Check:** This matters deeply to users because it directly impacts their financial security and trust in the ecosystem. People lose funds in exploits, leading to real-world consequences like lost savings or halted innovation. Users aren't just chasing yields; they seek reliable, verifiable systems where decentralization isn't a marketing term but a protective mechanism against censorship and traditional finance flaws. Without it, participation in DeFi feels like gambling, deterring long-term adoption and contradicting Ethereum's ethos of empowerment through transparency and censorship-resistance.

“Misnaming things is contributing to the world’s despair” – Albert Camus.


**Sensemaking Analysis** 

The sensemaking process draws from diverse methodologies to differentiate genuinely decentralized DeFi protocols from those with hidden centralized permissions and dependencies.

Our main inspirations come from L2Beat's [methods](https://forum.l2beat.com/c/methodology-and-framework/5) for decentralization assessments about Layer 2s, Anticapture's frameworks for capture-resistant governance, DeFi Safety's protocol ratings, or [Bluechip.org](http://bluechip.org), which is a stablecoin rating agency. These inspirations led to the development of the DeFiScan [methodology](https://www.defiscan.info/learn-more).,
.
These assessments focus on key metrics collected via permission scanners, documentation dissection by researchers, chain explorers, and tools like Tenderly.

Data is aggregated via API pulls and dashboards, synthesized from reports/documentations, tweets, and blogs, and validated through GitHub and Discord feedback. Furthermore, DeFiScan's framework and website are under MIT license, meaning this is an open-source tool that anyone can use and change.


**Gitcoin's Unique Role & Fundraising**

DeFiScan uses a bounty system to encourage people to create protocol reviews. Those bounties can go from $1,000 to $2,000, considering that a long codebase, a large number of permissions, or a large number of external dependencies mean higher payouts.
This bounty system is mandatory because creating a protocol review can take several weeks and requires a high level of technical expertise. This is where Gitcoin plays a unique role.

Gitcoin funding would enable DeFiScan and other domain participants to create many more decentralization / transparency reviews and significantly improve DeFi coverage. In addition, since the launch of DeFiScan, we have received numerous suggestions for improving the framework, and Gitcoin would be a great place to peer-review it.

Gitcoin can uniquely help solve this problem by channeling decentralization-aligned participants to fund and operate open-source tools and frameworks like DeFiScan, L2Beat, Anticapture, and Bluechip dashboards and scanners, amplifying community-driven transparency initiatives under MIT licenses. This fosters verifiable assessments of centralization risks, proposes a community-based standard for what DeFi apps should try to be, and directly addresses the decentralization illusion.

**Fundraising Reality Check:** Yes, raising $50K+ for this domain is feasible, given DeFi's scale and stakeholder interest.
DeFiScan has already raised over $100K since October 2024 from sponsors including the Ethereum Foundation, Octant, Giveth, Devcon, and various DeFi protocols, as evidenced by our Gitcoin, Octant, and Giveth campaigns. Likely additional sponsors include security firms, risk agencies, and protocols seeking audited transparency.


**Success Measurement & Reflection**

We assess success with various metrics:

- % TVL Reviewed

- Growth of TVL in highly decentralized protocols.

- Number of Changes Made: Track 10+ protocol upgrades (e.g., reduced centralization risks, verified contracts, integrated standards in multisig, exit windows, and frontends.

- Important accounts following/mentioning decentralization and transparency framework through social media, official reports, and GitHub contributions.

Our main goal is to cover 90% of DeFi’s total TVL by November 2025. Currently, more than [80% of total TVL is already reviewed](https://www.defiscan.info/), and some protocols have already been acted upon following our reviews. For example, Uniswap V3 on Arbitrum has three unverified contracts before the review, and two of them were verified after it was published.

**Genuine impact** will be measured according to the measures DeFi protocols are taking to improve their decentralization.

**Satisfaction Test:** The Ethereum community will be genuinely glad we funded this domain long-term if it leads to safer, more transparent DeFi standards, solidifying Ethereum as the financial layer of the internet.


**Domain Information**

Yes, we are proposing a domain for GG24:

"DeFi Transparency and Decentralization Assessment." or “DeFi Curation”

This domain will focus on funding projects that build verifiable tools for evaluating protocol maturity, risks, and decentralization stages.

 **Domain experts** could include the DeFiScan team, L2Beat contributors, and security/decentralization researchers from EVM and cybersecurity ecosystems adhering to the scientific method, public good funding, and the open source attitude.

We pitch a mix of **mechanisms**: quadratic funding for broad community input, retroactive funding for proven impacts, and governance tokens to influence DAO programs targeting DeFi users.

We foresee multiple **sub-rounds**: one for assessment tools (e.g., dashboards, permission scanners, APIs); one for education and standards (e.g., framework updates, conference participation, integrations with academic/private curricula and DAO ecosystems like L2s and DeFi apps). This ensures funding what truly matters, aligning capital with meaning in a cyberpunk, public-good mindset.

Thanks for reading all this! We are eager to discuss this potential "DeFi curation" domain and set a standard with the Gitcoin community!

-------------------------

owocki | 2025-08-18 20:42:47 UTC | #2

# Draft Scorecard

## 2025/08/18 - Version 0.1.1

## By Owocki

## Prepared for MarcVlad re: "GG24 Sensemaking Report: DeFi Transparency and Decentralization Assessment"

(vibe-researched-and-written by an LLM using [this prompt](https://github.com/owocki/gg24/blob/main/prompt_individual.txt), iterated on, + edited for accuracy quality and legibility by owocki himself.)

## Proposal Comprehension

TITLE
GG24 Sensemaking Report: DeFi Transparency and Decentralization Assessment

AUTHOR
MarcVlad

URL
[https://gov.gitcoin.co/t/gg24-sensemaking-report-defi-transparency-and-decentralization-assessment/22966](https://gov.gitcoin.co/t/gg24-sensemaking-report-defi-transparency-and-decentralization-assessment/22966)

### TLDR

You propose a GG24 domain focused on DeFi transparency and decentralization assessment (aka DeFi curation). The domain would fund open source tools, standards, and education that evaluate protocol maturity and centralization risk. Mechanisms include quadratic funding for broad input, retroactive funding for proven impact, and sub rounds for tools and for education. You expect collaboration with DeFiScan, L2Beat, security and decentralization researchers, and related initiatives. The intent is to chip away at the decentralization illusion in DeFi by making risks visible and incentivizing concrete improvements.

### Proposers

Proposer
MarcVlad

Their credentials
Driving DeFiScan’s open source framework and bounties for protocol reviews. Claims prior fundraising from EF, Octant, Giveth, Devcon, and various DeFi protocols. Familiar with adjacent efforts like L2Beat, Anticapture, DeFi Safety, and Bluechip.

### Domain Experts

Proposed experts
DeFiScan team, L2Beat contributors, EVM security and decentralization researchers, risk agencies.

Their credentials
Track records in public goods transparency tooling, security research, and protocol risk analysis. Not all named individuals appear to be confirmed yet in this thread, which matters for execution.

### Problem

There is no common, verifiable framework to assess how decentralized a DeFi protocol really is. Marketing often overstates decentralization while admin keys, upgradeability, oracles, unverified contracts, or opaque governance hide central points of failure. Users and allocators lack an easy way to compare risk and maturity.

### Solution

Fund open source assessment frameworks, scanners, dashboards, and documentation to surface decentralization risks and standards. Use bounties to scale rigorous protocol reviews. Run sub rounds for tool builders and for education and standards. Measure success by share of TVL reviewed, protocol changes prompted by reviews, and growth in usage of more decentralized options.

### Risks

Execution risks
• Reviewer supply and rigor. Recruiting enough technically strong, conflict free reviewers and maintaining consistent methodology is hard, especially at scale.
• Conflicts of interest. If protocols fund reviews, you need clear COI policies and public disclosures.
• Method drift and disagreement. Aligning on definitions of “decentralized enough,” weighting of dimensions, and updating the framework as tech evolves will be contentious.
• Duplication and ecosystem fit. This must complement, not fragment, adjacent efforts from L2Beat, DeFi Safety, Bluechip, and security firms.
• Metrics integrity. “% TVL reviewed” and “TVL growth of highly decentralized protocols” can be confounded by market cycles, incentives, and chain migrations.
• Timeline. Meaningful protocol changes by October require already lined up targets, reviewers, and bounty ops.
• Legal and reputational friction. Negative findings can create pressure. You will need strong editorial independence and clear process.

## Outside Funding

Yes. DeFiScan claims more than \$100k raised since Oct 2024 from EF, Octant, Giveth, Devcon, and various protocols. Security firms and risk agencies are listed as likely sponsors. Clarity on which parts are committed versus prospective would strengthen the case.

## Why Gitcoin?

Gitcoin can convene aligned contributors, distribute bounties at scale, and run plural mechanisms that reward both early signal and proven impact. The public goods ethos, community reach, and round ops make Gitcoin a uniquely good fit to steward an open, verifiable standard rather than a walled product.

## Owockis scorecard

| # | Criterion                                                                                                        | Score (0-2) | Notes                                                                                                                                                           |
| - | ---------------------------------------------------------------------------------------------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Problem Focus – Clearly frames a real problem (one that is a priority), avoids solutionism                       | 2           | Clear articulation of the decentralization illusion and user risk. Directly relevant to Ethereum’s credibility and safety.                                      |
| 2 | Credible, High leverage, Evidence-Based Approach – Solutions are high leverage and grounded in credible research | 1           | Builds on known frameworks and open methods. Bounties to scale reviews, plus standards and education. High leverage if executed rigorously.   Might be trying to go too broad by proposing qf/retro/others at once.                    |
| 3 | Domain Expertise – Proposal has active involvement from recognized experts                                       | 1           | Strong ecosystem signals, but expert commitments are implied rather than confirmed by name in the thread. Locking named reviewers and advisors would earn a 2.  |
| 4 | Co-Funding – Has financial backing beyond just Gitcoin                                                           | 1           | Prior fundraising noted and plausible additional sponsors. Would benefit from explicit letters of intent or MOUs.                                               |
| 5 | Fit-for-Purpose Capital Allocation Method – Methodology matches the epistemology of the domain                   | 1           | QF plus retro is maybe too broad? Maybe just focus on one mechanism?  |
| 6 | Execution Readiness – Can deliver meaningful results by October                                                  | 1           | Bounties and reviews can start quickly, but “meaningful results” requires named collaborations, a review backlog, and process tooling ready now.                |
| 7 | Other – vibe check and anything missed                                                                           | 2           | Open source, verifiability, and community standards are the right north star. The tone is collaborative and public good aligned. Ensure independence and rigor. |

### Score

Total Score: 9 / 14
Confidence in score: 75%

### Feedback:

#### Major

• Confirm named expert partners and a reviewer pool with CVs, time commitments, COI disclosures, and pay bands. This is the difference between a good idea and reliable signal.
• Confirm outside funders
• narrow to one mechanism

#### Minor

• Define a minimal, comparable “decentralization grade” per protocol plus a checklist that everyday users can grasp.
• Pre announce 5 to 10 target protocol reviews for September to prove pace and depth, then scale.
• Align with L2Beat, DeFi Safety, Bluechip to prevent duplication. 

### Steel man case for/against:

#### For

This targets a first order Ethereum priority: credible decentralization. Open assessments nudge protocols to remove central points of failure, improve contract verification, add exit windows, and harden governance. With Gitcoin’s mechanisms and DeFiScan’s momentum, the domain can produce verifiable public goods that compound over time.

#### Against

Assessment quality is fragile. Without named experts, strong COI policies, and a rigorous, transparent rubric, outputs risk becoming noise or capture. If adjacent efforts are not coordinated, we fragment attention and dilute signal. Metrics like “% TVL reviewed” can overstate safety and become a vanity target.

### Rose/ Bud/Thorn

Rose
Open source, verifiable assessments that push protocols to fix centralization risks. Strong alignment with Ethereum’s ethos and Gitcoin’s public goods mission.

Thorn
Rigor and neutrality are hard. Without locked in experts, COI rules, and a transparent rubric, outputs could be questioned or gamed. Coordination with existing orgs is essential to avoid duplicative reviews.

Bud
If you ship a credible rubric, shared data schema, and a cross org reviewer network, this could grow into the canonical decentralization standard that wallets, explorers, and treasuries rely on at allocation time.

## Feedback

Did I miss anything or get anything wrong? Feel free to reply in the thread and I will iterate quickly.

# Research Notes

I relied on the proposal thread for details about scope, mechanisms, experts, and funding. Open questions I would like to verify next:
• Which specific experts are committed and for how many reviews per month.
• Reviewer pipeline, training, and QA process, including second reviewer checks and appeals.
• COI policy when a protocol or its investors sponsor a review.
• Shared data formats with L2Beat, DeFi Safety, and Bluechip, and any formal coordination plan.
• Evidence behind the “80 percent TVL already reviewed” claim and examples of protocol changes prompted by reviews, with links to diffs and commits.
• A September to October milestone plan with 5 to 10 named protocol reviews, acceptance criteria, and budget per deliverable.

-------------------------

deltajuliet | 2025-08-19 23:55:31 UTC | #3

Welcome back @MarcVlad. 

Evaluated using [my steward scorecard](https://gov.gitcoin.co/t/gg24-domain-proposal-voting-scorecards/23016/5?u=deltajuliet) — reviewed and iterated manually for clarity and alignment with GG24 criteria.  

---

### ✅ Submission Compliance
- Problem, sensemaking, domain info, fundraising, and metrics are all included  
- References active prior funding ($100K+ from EF, Octant, Giveth, Devcon, protocols)  
- Experts listed as “DeFiScan team, L2Beat, decentralization/security researchers” but not individually confirmed  
- Mechanisms (QF + retro) are listed but execution structure feels broad and under-specified  
- Verdict: **Compliant but expert commitments + mechanism clarity are weak spots**

---

### 📊 Scorecard Evaluation  
**Total Score: 9 / 16**

| Criteria | Score | Notes |
|----------|-------|-------|
| Problem Clarity | 2 | Frames the “decentralization illusion” crisply; directly tied to Ethereum credibility and user safety |
| Sensemaking Approach | 1 | Builds on frameworks like L2Beat, DeFi Safety, Bluechip; but doesn’t show rigorous comparative synthesis or adoption plan |
| Gitcoin Fit | 2 | Strong fit — Gitcoin can convene bounties, plural mechanisms, and community standards |
| Fundraising Plan | 1 | Prior funding noted ($100K+), but GG24 round-specific anchors not yet committed |
| Capital Allocation Design | 1 | QF + retro + bounties is overbroad; could benefit from focusing on one fit-for-purpose mechanism |
| Domain Expertise | 1 | DeFiScan credible, but no confirmed independent reviewers/advisors named in-thread |
| Clarity & Completeness | 1 | Proposal is structured but risks “method drift” without clear rubric or reviewer pipeline |
| Gitcoin Support Required | 0 | Would require significant Gitcoin scaffolding: reviewer pool, COI rules, governance clarity |

---

### 📌 Feedback for Improvement

**Where I agree with Owocki:**  
- Need **named experts and reviewer commitments** with bios, availability, and COI disclosures.  
- Outside funders should be confirmed with at least one LOI before launch.  
- Mechanism mix is overstuffed — narrowing to one (bounties with QF, or retro) would help with focus and credibility.  

**What I’d add:**  
- Define a **minimum viable rubric**: e.g., checklist of contract verification, key management, governance openness, oracle dependencies.  
- Publish **5–10 named protocol reviews for October** as early deliverables — “90% TVL reviewed” is aspirational but too fuzzy.  
- Consider partnering formally with **L2Beat, Bluechip, DeFi Safety** to avoid fragmentation — shared data schema + reviewer pool could make this the canonical standard.  
- Plan for **legal/reputational pressure** — protocols may push back if flagged as centralized; editorial independence matters.  

---

### 🟡 Conditional Support
I would support this if:  
- At least 2–3 independent expert reviewers are confirmed with disclosed roles  
- One anchor co-funder signs on (security firm, EF, or major DeFi protocol)  
- October deliverables are locked (published reviews, rubric, public dashboard)  

Without these, the risk is producing noise or duplicative work that doesn’t land as a credible Ethereum-wide standard. With them, this domain could become the reference framework for decentralization in DeFi, pushing protocols toward real neutrality and safety.

-------------------------

sepu85 | 2025-08-25 12:44:59 UTC | #4

Thanks for this proposal on **DeFi Transparency & Decentralization** — strengthening trust in DeFi through assessment frameworks feels critical for both users and builders.

In our [proposal](https://gov.gitcoin.co/t/gg24-sensemaking-report-at-pre-post-grant-coordination-from-allocation-to-alignment-accountability/21711), we didn’t propose a domain but instead are seeking to validate whether **CollabBerry’s peer-based allocation and accountability tooling** could serve across multiple domains as a complementary mechanism.

What resonates here is the shared emphasis on **transparency as legitimacy**. Your proposal looks at transparency in protocols and decentralization in governance, while CollabBerry is focused on transparency inside funded projects — specifically, how contributors are recognized and how resources are distributed post-grant. Through continuous peer-to-peer assessments, our mechanism produces a reputation signal that informs more equitable allocations, creating a traceable record of accountability.

This feels like a micro-level complement to your macro-level assessment: if DeFi needs external transparency to prove decentralization, projects themselves need internal transparency to prove fairness.

We’d love your perspective: do you see contributor-level accountability as relevant for extending DeFi transparency principles into the way public goods teams operate after funding?

-------------------------

MarcVlad | 2025-09-16 08:15:20 UTC | #5

Thank you for the detailed feedbacks! We've consolidated responses to both below:

* **Specific committed experts, commitments, bios, availability, and COI disclosures (including at least 2–3 independent reviewers with disclosed roles):**

Core experts include:

**TokenBrice**

Role: A key figure in the DeFi community and an integral part of The DeFi Collective.
Experience: TokenBrice is well-recognized for his deep involvement in the DeFi space since its inception. He has been active in numerous governance forums, contributing to discussions and decisions that shape the future of DeFi. His professional journey includes working with Liquity, Paraswap, Monolith, Aave, Maverick Protocol, and others.
Contributions: Known for organizing DeFi-focused meetups in France, hosting live shows, presenting at various ETH conferences, and writing insightful articles on his blog about DeFi trends and developments.
Social Profiles:[ https://twitter.com/TokenBrice](https://twitter.com/TokenBrice) - https://tokenbrice.xyz/- [TokenBrice (TokenBrice) · GitHub](https://github.com/TokenBrice)
Expertise: TokenBrice brings a wealth of knowledge in liquidity management, governance processes, and overall DeFi market trends.

**Nils**

Role: Founder of the lending protocol Vesu and developer at The DeFi Collective.
Experience: Nils has a background in financial engineering and is recognized for his expertise in designing and developing decentralized protocols. His deep technical knowledge of blockchain technology makes him a valuable asset to the team.
Contributions: Focuses on the technical framework for DeFi Scan, self-policing for the DeFi industry, working towards enhancing security, building public trust, and accelerating the adoption of DeFi protocols. Speaker at ETH conference and Devcon.
Social Profiles: [x.com](https://twitter.com/nilsbundi) - [https://www.linkedin.com/in/nils-bundi-6246b998](https://www.linkedin.com/in/nils-bundi-6246b998/) - [nbundi (Nils Bundi) · GitHub](https://github.com/nbundi)

**Ben Levit**

Role: Co-Founder and CEO of Bluechip.
Experience: Ben's main contribution is to have launched Bluechip, which published the SMIDGE framework (Stability, Management, Implementation, Decentralization, Governance, Externals) for assessing the reliability of stablecoins, and to have used this framework to create the first rating agency dedicated to stablecoins in all their forms. Bluechip is also regularly sharing content dedicated to the stablecoin industry.
Contributions: He leads Bluechip in providing independent ratings for stablecoins and participates in as well as hosts Bluechip25, The Crypto Safety Conference.
Social Profiles: https://x.com/levitben - https://www.linkedin.com/in/benjamin-levit-247a2226b/

**Zeugh Anticpature**

Role: Founder of Anticapture and Head of Research at Blockful.
Experience: Zeugh specializes in building resilient organizations and governance systems in the blockchain space, with a focus on capture-resistant designs.
Contributions: He develops frameworks for DAO governance assessments, emphasizing anti-capture mechanisms, and contributes to research on secure, decentralized systems. He is always hacking or presenting at ETH conferences.
Social Profiles: https://x.com/theZeugh

**Rex Hygate**

Role: DeFiSafety Founder and President
Experience: An experienced product expert and consultant with a background in avionics, Rex has managed crypto portfolios and provided insights into DeFi security for years.
Contributions: He created DeFiSafety to offer transparent Process Quality Reviews (PQRs) for DeFi protocols, helping investors assess risks. He speaks on DeFi safety and has evolved the platform to include revenue models like subscriptions for advanced analytics.
Social Profiles: https://x.com/rhygate •[ https://www.linkedin.com/in/rexhygate](https://www.linkedin.com/in/rexhygate)

**Nicolas Consigny** 

Role: Lead of [Kohaku] wallet initative (https://notes.ethereum.org/@rudolf/kohaku-wallet) -DeFi expert at the Ethereum Foundation.
Experience: Nicolas has extensive experience in Ethereum protocol development and coordination, including work on EIPs and hardware integrations.
Contributions: He coordinates developer efforts, contributes to EIP discussions (e.g., EIP-7702), the EF DeFi treasury strategy, and speaks at events like EthCC on topics such as dApp connectivity and Ethereum's future.
Social Profiles: https://x.com/ncsgy •[ https://github.com/nconsigny](https://github.com/nconsigny)

Unfortunately, **L2Beat** decentralization researcher cannot join this domain due to time constraints for the moment. They are interested in discussing collaborations in the close future and want to participate in how decentralization and transparency researcher gather the most up-to-date and presentable data.

* **Reviewer pipeline, training, and QA process (including second reviewer checks and appeals):**

**DeFiScan** is an open-source project where anyone can create and submit protocol reviews via the website by adding .md files in the content/protocols folder on GitHub, following a specific template structure. Community initiatives encourage involvement through the Bounty Program, offering bounties up to $2,000 per review based on complexity (e.g., long codebase, numerous permissions, or external dependencies). Reviews are examined and published by the research team in collaboration with the protocol's core developers to ensure accuracy.

**Bluechip**: Reviews stablecoins follow the [SMIDGE framework](https://cms.bluechip.org/assets/ef4d829e-3874-484a-91dd-3e6d98dbe464), with ratings assigned by the team based on six key factors (Stability, Management, Implementation, Decentralization, Governance, Externals). The process involves independent evaluation, though specific training and QA details are specific to the reviewed stablecoin

**Anticapture**: Focuses on governance assessments through action phases (Propose, Decide, Execute, Evaluate) and capture-resistance spectra. Reviews integrate security and centralization risks, but detailed pipeline, training, and QA processes are not officially published yet.

**DeFiSafety**: Employs Process Quality Reviews ([PQRs](https://defisafety.com/documentation-09)) that scrutinize six key elements of deployed smart contracts (Documentation, Testing, Security, Access Controls, Oracles, and Economics), rating them against best practices. Developers prepare by following guidelines for high scores; reviews are transparent and conducted by the team, with no explicit mention of formal training or second checks, though assessments emphasize verifiable processes. Appeals or updates can be requested via contact.

* **COI policy when a protocol or its investors sponsor a review:**

Reviews involve collaboration with protocols for auditing and publishing, but none intend to recommend investment nor to receive payment from them.

Editorial independence is maintained. Reviews from DeFiscan, Bluechip, Anticapture are not liable for third-party content, and links are for convenience without any financial endorsement.

We might praise and support publicly highly decentralized protocols or teams that have proven their dedication to decentralization and transparency.

* **Shared data formats, and any formal coordination/partnerships to avoid fragmentation (including shared data schema + reviewer pool):**

This domain will serve as a foundation for decentralization researchers and the open community to refine data monitoring, and aggregate frameworks for protocol assessments (e.g., integrate Anticapture's governance-focused reviews) with their related dashboards..

We aim to also publish and discuss draft frameworks here, gradually aggregating details from each contributor's approach where possible, under MIT licenses to promote shared schemas and a collaborative reviewer pool.

*  **Evidence behind the TVL reviewed claim and examples of protocol changes prompted by reviews, with links to diffs and commits:**

Updated claim: from 69% to 89%TVL coverage as of August 2025 with the recent Curve, Compound, and Binance stETH reviews (https://x.com/defiscan_info/articles), on track for 90% by November 2025.(defiscan.info)

Following our reviews, Uniswap V3 verified contracts on Arbitrum and Base.

Links to diffs/commits:
https://x.com/defiscan_info/status/1892909384038035840
https://arbiscan.io/address/0x42B24A95702b9986e82d421cC3568932790A48Ec#code
https://arbiscan.io/address/0x91ae842A5Ffd8d12023116943e72A606179294f3#code
https://arbiscan.io/address/0xadF885960B47eA2CD9B55E6DAc6B42b7Cb2806dB#code

*  **September to October milestone plan with 5 to 10 named protocol reviews, acceptance criteria, and budget per deliverable; plus October deliverables locked (published reviews, rubric, public dashboard):** 

It's challenging for us to commit to a specific publication deadline for a protocol review, as each review includes a "right to answer" from the reviewed protocol team, which often results in unpredictable delays of a few days to a few weeks. Regarding acceptance criteria, it's pretty straightforward; no review is published unless:
1. The full protocol permission scope has been analyzed.
2. The full initial draft of the review has been established.
3. The draft has been reviewed by at least one peer (internal).
4. The draft has been reviewed by at least one team member/expert on the protocol.
5. The review is compliant with our actual framework.

* DeFiscan publishes at least 2-4 reviews, depending on their complexity.

Currently, there are 16 protocols in the review pipeline of DeFiScan : [EtherFi](https://github.com/deficollective/defiscan/pull/225) , [Liquidity V2](https://github.com/deficollective/defiscan/pull/203), [Venus](https://github.com/deficollective/defiscan/pull/201) , [Euler V2](https://github.com/deficollective/defiscan/pull/194), [Eigenlayer](https://github.com/deficollective/defiscan/pull/188), [PancakeSwap](https://github.com/deficollective/defiscan/pull/181), [Cian protocol](https://github.com/deficollective/defiscan/pull/180), [Glo Dollar](https://github.com/deficollective/defiscan/pull/127), [cat-in-a-box](https://github.com/deficollective/defiscan/pull/91), [Rocket Pool](https://github.com/deficollective/defiscan/pull/45) are currently being reviewed and some will be published by the end of October. Full list of protocol reviews can be checked in the pull requests on the [DeFiScan GitHub](https://github.com/deficollective/defiscan/pulls).


Review costs can vary greatly depending on the protocol code size and complexity; for instance, UNIv2 is much easier to assess than Aave. However, we estimate an average cost per review of approximately $ 2,000. Please keep in mind that this average hides deep fluctuations depending on the reviewed protocol (the effective price of the Aave V3 review was above $10k, as it took months of work from our protocol reviewers) Now, October is a special month for DeFiScan, as it will mark our one-year anniversary, and we intend to celebrate with releases!

Our core and main deliverable is a revamp of the framework to provide more granularity on the global rankings (which currently have only four possible tiers: N/A, Stage 0, Stage 1, and Stage 2). October is presently our target for release; however, we will not rush the publication if the new framework is not in a satisfactory state by then.

* Anticapture: Is currently reviewing the state of [Arbitrum](https://anticapture.com/arb) Governance which should be available by the end of October. Official frameworks from Anticapture will also be published here when ready.

* DeFiSafety is reviewing a couple of protocols per month.

* Bluechip is hosting[ the Bluechip25 Conference](https://conference.bluechip.org/) in Vienna with a wide range of public and private institutions ,and is overloaded with stablecoin reviews. We can expect at least 2 new stablecoins reviewed by October.

We also aim to present a detailed product roadmap regarding data pipelines for decentralization and transparency research and want to start gathering feedbacks on this work here!

*  **Outside funders confirmed with at least one LOI before launch (including one anchor co-funder like a security firm, EF, or major DeFi protocol):**

Confirmed funders/sponsors include Ethereum Foundation ([grant](https://www.defiscan.info/blog/ef-grants) announced March 2025, serving as anchor), [Giveth](https://giveth.io/cause/defi-transparency-decentralization) (active QF), [Octant](https://octant.app/project/8/0x4396F167ef86ECBAC27682Eb33AFCa13693dFe40) (active), Devcon (prior campaigns), Liquity (grant received), and others such as Aerodrome, Dyad, Glo Dollar, Maverick, Polygon Labs, Pooltogether, Possum Labs, Synthetics Implemented Right (SIR Protocol), and Velodrome.

* **Funding details and mechanisms**

This proposal for the DeFi Transparency & Decentralization Assessment GG24 Domain in October 2025 requests $100,000 from Gitcoin to fund core activities, including review bounties ($60,000 for 30-60 protocol assessments at $1,000-2,000 each or by hiring a peer-reviewer), API and data pipeline development ($35,000 for unified schemas and aggregators), and $5000 for education initiatives at conferences and various online medium.
We do not request operating funds for the domain experts. With the confirmed sponsored above, this Gitcoin contribution will cement the domain's launch to become a canonical standard for DeFi decentralization and Transparency.

Regarding the **funding mechanism**, we are completely dedicated to operate in the most transparent and accountable way. We propose an hybrid approach: 70% via specific milestones (e.g., bounties tied to published reviews, API launches, live data aggregator...), and 30% retroactively for proven impacts like TVL coverage, framework published. 

* **Minimum viable rubric defined (e.g., checklist of contract verification, key management, governance openness, oracle dependencies):**

**DeFiScan** current checklist:

1. Chain (underlying blockchain centralization risks),
2. Upgradability (contract immutability and upgrade controls),
3. Autonomy (dependencies like oracles with fallbacks),
4. Exit Window (user ability to exit during changes, min 7-30 days timelock),
5. Accessibility (backup UIs and frontends).

Each scored High/Medium/Low risk, determining overall decentralization stage from 0 (full training wheels, high risks) to 2 (no training wheels, low risks).

As mentioned DeFiScan is actively working on a more granular framework and wants to use this domain as one of the places where the community will be able to contribute and demonstrate our neutrality.

**Bluechip** is an independent stablecoin rating agency that evaluates stablecoins using the [SMIDGE framework](https://cms.bluechip.org/assets/ef4d829e-3874-484a-91dd-3e6d98dbe464), focusing on safety and risks, including decentralization and governance aspects. This is tailored to stablecoins (a subset of DeFi protocols), assessing how they maintain pegs, manage risks, and distribute control. Decentralization evaluates concentration of power (e.g., avoiding single-party control), while Governance checks protections against abuse, voting integrity, and holder safeguards. Implementation (smart contracts/oracles) is planned but not fully assessed yet. Parameters contribute to letter-grade ratings (A+ to F), emphasizing long-term stability over short-term volatility.

**Anticapture** has not officially published a framework to assess governance risks, and they integrate security risks along with centralization risks. They focus on flash loan protection, spam resistance, time-based safeguards, threshold and access control, vote mechanics and incentives, emergency mechanism and security standards (audits, MEV, DNS protection…).

**DeFiSafety** provides Process Quality Reviews for DeFi protocols, focusing on safety through development best practices rather than pure decentralization. Their methodology rates protocols (0-100%) on transparency, security, and process quality, indirectly assessing decentralization via access controls and governance transparency. Governance/decentralization isn't a standalone category but is embedded in Access Controls (e.g., admin powers, immutability) and Documentation (e.g., governance disclosure). High scores indicate mature, transparent processes that reduce central risks like unchecked upgrades.

* **Plan for legal/reputational pressure (protocols may push back if flagged as centralized; editorial independence matters):**

We emphasize editorial independence in all reviews: They provide verifiable information without endorsement or recommendation; we are not liable for third-party content; and we focus on objective, fact-based assessments to mitigate pressure. We acknowledge potential pushbacks and will strive to incorporate constructive criticisms, while advancing more precise and unified standards to uphold the cypherpunk ethos and scientific method in cyberspace.

We hope to have answered your questions and are excited to iterate further if necessary

-------------------------

subhanmanj2-png | 2025-09-16 05:54:29 UTC | #6

This proposal tackles the real problem of the “decentralization illusion” in DeFi.It aims to protect users from hidden risks such as admin keys and unverified contracts.By supporting open-source tools and expert reviews, it creates strong public good value.The proposal also sets measurable goals, like reviewing 90% of DeFi TVL by November 2025.It has already proven effective, with $100K+ raised and real improvements like Uniswap verifying contracts.However, it risks duplicating the work of existing efforts such as L2Beat, DeFiSafety, and Bluechip.The budget details are still vague, making it unclear how funds will be used.There are concerns about independence if reviewed protocols also provide funding.The language and domain name feel too complex for broad community understanding.To succeed, it needs simpler branding, clear budget plans, and stronger neutrality safeguards.

-------------------------
