---
id: 22923
title: "GG24 Sensemaking Report: Privacy-Preserving, Legally-Compliant KYC for Grants and Web3"
slug: gg24-sensemaking-report-privacy-preserving-legally-compliant-kyc-for-grants-and-web3
category: gitcoin-sensemaking-szn
url: https://gov.gitcoin.co/t/gg24-sensemaking-report-privacy-preserving-legally-compliant-kyc-for-grants-and-web3/22923
created_at: 2025-08-13T14:54:31.990Z
last_posted_at: 2025-08-25T12:44:10.981Z
posts_count: 9
views: 2031
like_count: 19
---

# GG24 Sensemaking Report: Privacy-Preserving, Legally-Compliant KYC for Grants and Web3

<https://gov.gitcoin.co/t/gg24-sensemaking-report-privacy-preserving-legally-compliant-kyc-for-grants-and-web3/22923>
M0nkeyFl0wer | 2025-08-19 21:59:19 UTC | #1

Big props to **@owocki** and @MathildaDV for pushing this sensemaking approach forward. One of the biggest pain points I ran into while running Gitcoin Grants was KYC. It is a legal requirement, but it is also an Achilles heel for much of the Web3 space, creating massive honeypots of personal data that are magnets for trouble. I am putting this report forward to explore how Gitcoin could lead the charge in building and testing open-source, privacy-preserving, legally-compliant KYC solutions, and actually dogfood them while allocating funds and making these tools widely available to others in the space. 

## GG24 Sensemaking Report: Privacy-Preserving, Legally-Compliant KYC for Grants and Web3

---

### Problem & Impact

Every time someone says "KYC," I picture a giant jar of honey left out in the open. It’s put there with the best intentions, maybe to cook something delicious or feed the community, but it also attracts every bear, wasp, and opportunist in the area.

When I ran Gitcoin’s grants program, that “honey” was stacks of sensitive identity documents sitting where anyone with the wrong intentions could get to them. You don’t have to be a security expert to know that’s asking for trouble. Identity documents are powerhouse bait. You leak them and you have trouble.

We’ve seen the consequences:

- **Ledger**: customer data breach that exposed names, phone numbers, and addresses to attackers.  
- **Fractal ID**: over 6,300 users exposed, including passports and selfies, because an operator account got compromised ([source](https://cryptoslate.com/web3-kyc-vendor-fractal-id-loses-over-50k-users-passport-info-in-data-breach/?utm_source=chatgpt.com)).  
- **Transak**: hit via third-party KYC vendor access, affecting 92,000 users’ names, dates of birth, ID documents, and selfies ([source](https://thepaypers.com/crypto-web3-and-cbdc/news/transak-data-breach-affects-over-92000-users-following-phishing-attack?utm_source=chatgpt.com)).  
- **Coinbase**: internal breach where bribed staff leaked 70,000 users’ IDs and addresses ([source](https://cointelegraph.com/news/coinbase-data-scandal-scrap-kyc?utm_source=chatgpt.com)).  
- **Quadriga**: personal documents sent to a now-infamous exchange operator, later revealed to be fraudulent.

This is not just a security problem, it’s a systemic trust problem. Every time a grant platform, exchange, or protocol uses traditional KYC, it inherits the honeypot risk. One breach can have devastating effects on vulnerable communities—activists, dissidents, and marginalized groups—who depend on privacy for their safety.

Right now, there’s no broadly adopted, open-source, privacy-preserving KYC solution that meets legal requirements and doesn’t store raw personal data. That’s why this is urgent: regulators like OFAC and FATF are tightening compliance rules, while users’ tolerance for surveillance and data risk is plummeting.

**Meaning Check**: This matters to users because the stakes are personal. When someone’s ID, address, and face are exposed, the risk is not hypothetical—it’s phishing attacks, harassment, stalking, identity theft, and sometimes physical danger. For grants programs like Gitcoin’s, the current model puts both applicants and program staff in a position where sensitive data is accessible, creating liability and anxiety on both sides.

---

### Sensemaking Analysis

**Tools used**:  
- Comparative breach analysis of Web3 and fintech KYC incidents.  
- Stakeholder perspective from running Gitcoin’s grants program and participating in other KYC-heavy ecosystems like Thrive.  
- Evaluation of emerging privacy-preserving identity technologies, including zero-knowledge proofs (ZKPs), verifiable credentials (VCs), and “proof of clean hands” frameworks.

**Sources consulted**:  
- Public reporting on KYC data breaches from CoinTelegraph, CryptoSlate, The Paypers, and others.  
- Gitcoin governance discussions on trust, compliance, and domain stewardship.  
- Technology documentation from projects like Holonym, Human Passport, and zkKYC research groups.

**Data aggregation**:  
I cross-referenced breach incidents with the KYC vendor model used, looked at whether storage was centralized or encrypted, and identified where insider access was possible. I also compared legal requirements (OFAC, FATF, GDPR) against technical capabilities of ZKPs and VCs to confirm that privacy-preserving compliance is viable.

The picture is clear:  
1. Centralized document storage is the most common failure point.  
2. Insider abuse is almost as common as external hacks.  
3. There is no shortage of technical approaches—what’s missing is an open, trusted, well-funded space to develop and scale them.

Gitcoin can use GG24 as a platform to surface, test, and scale multiple approaches to privacy-preserving KYC, then “dogfood” the winning prototypes in live grant rounds.

---

### Gitcoin's Unique Role & Fundraising

**Unique role**:  
Gitcoin can do what few organizations can: fund public goods, run experiments in production, and convene developers, legal experts, and privacy advocates in the same room. This is not about picking one vendor. It’s about running an open competition of ideas and implementations.

Gitcoin’s grants is the perfect live environment to test these solutions at scale, using real users and real compliance needs. The process itself can be part of the experiment
whether through a conventional grant round, a deputized expert panel, quadratic funding for community-vetted tools, or hybrid approaches.

**Why a network, not one org**:  
The privacy-preserving KYC challenge is too broad for a single company to solve. A network approach allows multiple vendors to emerge, iterate, and compete. This avoids lock-in, reduces systemic risk, and encourages interoperability.

**Fundraising reality check**:  
This is a problem the ecosystem will pay to solve. Likely sponsors and partners include privacy tech orgs, compliance-conscious DeFi protocols, exchanges and foundations focused on open-source infrastructure. There is a clear path to $50K+ in matching funds from sources like:  
- Ethereum Foundation’s Privacy & Scaling teams.  
- Protocol Labs (Filecoin/Libp2p ecosystem).  
- ZK technology grants programs.  
- Public goods funds from major L2s (Optimism, Arbitrum).
- Centralized exchanges and other venders like Coinbase

---

### Success Measurement & Reflection

**Outcomes in 6 months**:  
- At least two open-source, ZKP-enabled KYC systems deployed by GG25
- No raw ID data stored in human-readable form.  
- At least one system passes an independent compliance and legal audit.  
- One other grant platform or crypto protocol adopts a funded solution.

**Measuring genuine impact**:  
Beyond counting active integrations, we can measure:  
- Reduction in sensitive data exposure points for Gitcoin staff and grantees
- Audit results confirming privacy and compliance claims.

**Satisfaction test**:  
In 6 months, the Ethereum community should be able to say:  
- “We’ve proven that you can run a legally compliant KYC process without building a data honeypot.”  
- “We have open-source reference implementations anyone can adopt.”  
- “We used Gitcoin to fund and test it ourselves.”

---

### Domain Information

**Proposed domain**: *Privacy-Preserving Compliance Infrastructure*

**Domain experts**:  
- Privacy tech developers (e.g., Holonym, zkKYC researchers)  
- Crypto-savvy compliance lawyers  
- Gitcoin grants ops veterans  
- ZK and AI computer vision engineers

**Mechanisms**:  
- Quadratic funding rounds for community input.  
-  Milestone-based direct grants with expert reviewers 

**Sub rounds**:  
Yes. Could include:  
- Prototype sprint.  
- Audit and compliance challenge.  
- Integration round for adopting platforms.

I am very much open to iterating on the methodology or structure for this idea, the key thing is creating a space for finding working, legally compliant KYC solutions that are open source and privacy preserving.

-------------------------

MathildaDV | 2025-08-13 19:18:48 UTC | #2

So nice to see @M0nkeyFl0wer popping into the forum again, and with such a strong report! Thank you ser. I'm curious, do you have a domain allocator (someone or a group that would operate the domain) in mind?

-------------------------

M0nkeyFl0wer | 2025-08-13 19:32:22 UTC | #3

Hey hey! I was thinking of working with Web3 Privacy and some of their extended community on this.

-------------------------

owocki | 2025-08-13 22:40:56 UTC | #4

> Privacy-Preserving Compliance Infrastructure

I think if we could hit Privacy-Preserving AND Compliant AND the ux doesnt suck (both for the grantees and the round operators), then that prettymuch nails the target of what i'd be looking for here

-------------------------

yosriady | 2025-08-14 02:25:32 UTC | #5

[quote="owocki, post:4, topic:22923"]
> Privacy-Preserving Compliance Infrastructure
[/quote]

I imagine a pre-requisite for this is Privacy-Preserving Analytics

-------------------------

Donny_Jerri | 2025-08-18 18:53:21 UTC | #6

I was literally scrolling and reading each one searching for a privacy ZK domain as it is certainly one of the biggest challenges Ethereum and all of us in general face.  

Loved reading this report.

-------------------------

owocki | 2025-08-19 05:52:43 UTC | #7

## 2025/08/15 – Version 0.1.1

### By Owocki

### Prepared for M0nkeyFl0wer re: "GG24 Sensemaking Report: Privacy‑Preserving, Legally‑Compliant KYC for Grants and Web3"

(vibe-researched-and-written by an LLM using [this prompt](https://github.com/owocki/gg24/blob/main/prompt_individual.txt), iterated on, + edited for accuracy quality and legibility by owocki himself.)

---

## Proposal Comprehension

**TITLE**
GG24 Sensemaking Report: Privacy‑Preserving, Legally‑Compliant KYC for Grants and Web3

**AUTHOR**
M0nkeyFl0wer

**URL**
https://gov.gitcoin.co/t/gg24-sensemaking-report-privacy-preserving-legally-compliant-kyc-for-grants-and-web3/22923

### TLDR

You rightly identify KYC’s Achilles‑heel problem: secure document collection creates centralized honeypots with systemic trust and safety risks. You propose that Gitcoin leverage GG24 as a testbed for multiple open‑source, privacy‑preserving KYC solutions—like ZKPs and verifiable credentials—validate them via real grants rounds, avoid storing raw PII, and build compliant, audited systems that others in Web3 can adopt.

### Proposers

M0nkeyFl0wer – brings firsthand KYC pain point experience running Gitcoin Grants; collaborative with governance leads (Owocki, MathildaDV).

### Domain Experts

You reference engagement with privacy‑tech developers (e.g., Holonym, zkKYC researchers), compliance lawyers, Gitcoin ops veterans, ZK and AI/computer vision engineers—but don’t yet have named participants.

### Problem

KYC typically accumulates sensitive ID data—selfies, passports, DOB—that becomes a honeypot for breaches (Ledger, Fractal ID, Transak, Coinbase, Quadriga), creating legal exposure, trust failures, and risk to grantees, especially vulnerable populations.

### Solution

Run a competitive, open process in GG24 to surface and test privacy‑preserving, legally compliant KYC solutions (e.g., ZKPs, verifiable credentials). “Dogfood” the prototypes in grants rounds, ensure no raw PII storage, audit compliance, and enable downstream adoption.

### Risks

* Building these solutions may be complex and slow and dependant upon archaic zk knowledge.
* is funding the main thing to unblock this category?
* Regulator requirements (OFAC, FATF) may impose unavoidable data retention. Getting compliance lawyers and auditors to sign off could be time‑intensive.
* Lack of named experts or clear implementation partners raises execution risk.

---

## Outside Funding

You mention realistic paths to ≥\$50K in matching funds from Ethereum Foundation (Privacy & Scaling teams), Protocol Labs, ZK grants, Optimism/Arbitrum public‑goods funds, and CEX vendors like Coinbase—but pitches or LOIs aren’t yet confirmed.

---

## Why Gitcoin?

You make a strong case: Gitcoin uniquely combines public‑goods funding capacity, real user environments (grants rounds), and community convening to identify and scale privacy‑preserving KYC where others may only build vendor solutions.

---

## Owocki’s Scorecard

| # | Criterion                                        | Score (0‑2) | Notes                                                                                                                                                |
| - | ------------------------------------------------ | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Problem Focus                                    | 2           | Clearly identifies a real, urgent, under‑served problem with real consequences.                                                                      |
| 2 | Credible, High‑leverage, Evidence‑based Approach | 2           | Approach is high‑leverage; methodology credible; citations to breach examples strengthen it.  |
| 3 | Domain Expertise                                 | 1           | Domain knowledge is referenced; needs named experts or teams engaged.                                                                                |
| 4 | Co‑Funding                                       | 1           | Clear funding paths identified but not yet secured; opportunity to solidify with partners.                                                           |
| 5 | Fit‑for‑Purpose Capital Allocation Method        | 2           | Matches Gitcoin’s strengths: experimental, open, community validated funding style (competition, dogfooding).                                        |
| 6 | Execution Readiness                              | 1           | Vision is compelling but execution plan needs fleshing out (who builds, audit partners, timeline).                                                   |
| 7 | Other (vibe check)                               | 1           | Clear urgency, good framing; would benefit from UX consideration and institutional engagement details.                                               |

**Total Score: 10 / 14**
**Confidence in score: 75%**

---

## Feedback:

### Major

* Secure at least one anchor funder or partner to demonstrate co‑funding traction.

### Minor

* Flesh out the execution plan: identify partners (audit firms, dev teams), timelines, milestones for GG25.
* Clarify UX flows for grantees and admins—good compliance can flounder with poor UX.
* Consider legal edge cases: what jurisdiction requirements are most likely? Any hardened frameworks or precedents?
* Articulate clearly how you’ll measure “privacy reduction” or “honeypot elimination” beyond audit pass/fail.

---

## Steel‑Man Case

### For

This proposal attacks a critical vulnerability in grant platforms and Web3 infrastructure. By partnering with Gitcoin’s ecosystem, open, privacy‑preserving KYC can be built and matured under real usage. This leverages Gitcoin’s unique convening and funding role to push the ecosystem forward responsibly and meaningfully.

### Against

The scope may be ambitious for GG24 timelines; legal and technical complexity could slow progress. Without named experts, committed funders, or pilot implementations, the proposal risks being seen as exploratory rather than deliverable within 6 months.

---

## Rose / Bud / Thorn

**Rose**

* Grips a real, high-stakes risk in Web3 identity.
* Aligns Gitcoin’s strengths with ecosystem signal.
* Framed with urgency, ethical clarity, and open‑source vision.

**Thorn**

* Execution plan needs specificity: who, how, when, with whom?
* Partnerships and funding proposals are still hypothetical.
* Potential UX and jurisdictional complexity under‑addressed.

**Bud**

* If you bring in compliance lawyers, audit partners, and a pilot test (even a prototype), this could become a GG24 flagship.
* A privacy‑preserving KYC module built here could be adopted by many protocols beyond Gitcoin.
* With early funding partner secured, you can build momentum and confidence from the community.

---

## Research Notes

* Need clarity on compliance partner engagement.
* How will Gitcoin handle cross‑jurisdictional regulation differences?
* UX needs fleshing out—what grantee experience looks like.
* Future diligence: mock audit, proof-of-concept, sample user flows.

-------------------------

deltajuliet | 2025-08-19 21:58:55 UTC | #8

Thanks @M0nkeyFl0wer for putting this forward. I’m reviewing all GG24 proposals against [my steward scorecard](https://gov.gitcoin.co/t/gg24-domain-proposal-voting-scorecards/23016/5?u=deltajuliet) for consistency and transparency. You know as well as I do what a pain point this is, and I welcome the opportunity to find solutions for tools that don't make me pull my hair out. 

---

### ✅ Submission Compliance
- Word count: ~1,150 (within required range)  
- All template sections present and complete  
- Domain Info detailed, though experts not yet confirmed  
- Verdict: **Compliant**

---

### 📊 Scorecard Evaluation
**Total Score: 13 / 16**

| # | Criteria | Score | Notes |
|---|----------|-------|-------|
| Problem Clarity & Relevance | 2 | Clear systemic framing of KYC honeypot risk |
| Sensemaking Approach | 2 | Breach analysis, regulatory review, ZK/VC technology survey |
| Gitcoin Fit & Uniqueness | 2 | Gitcoin uniquely suited to fund, test, and convene |
| Fundraising Plan | 1 | Potential funders named, no commitments yet |
| Capital Allocation Design | 2 | Multi-mechanism approach (QF, direct grants, subrounds) |
| Domain Expertise & Delivery | 1 | Categories of experts listed, but not confirmed |
| Clarity & Completeness | 2 | Meets template fully, well written |
| Gitcoin Support Required | 1 | Gitcoin would need to convene experts, secure funders, host pilots |

---

### ⚠️ Execution Gaps
- No confirmed domain experts or partners yet - knowing @M0nkeyFl0wer I don't see this being an issue ahead of the round 
- No anchor funder committed (trivial) 

---

### 📌 Next Step
This is a compliant and strategically strong proposal. To strengthen it further before ratification:  
- Confirm at least one domain expert and one funder  
- Flesh out the execution plan (who builds, who audits, expected milestones)  
- Add detail on UX and jurisdictional edge cases  

With these in place, this could serve as a high-priority GG24 domain.

-------------------------

sepu85 | 2025-08-25 12:44:10 UTC | #9

Thanks for surfacing this proposal on **privacy-preserving KYC** — striking the right balance between compliance and decentralization is a critical challenge for the grants ecosystem.

In our [proposal](https://gov.gitcoin.co/t/gg24-sensemaking-report-at-pre-post-grant-coordination-from-allocation-to-alignment-accountability/21711), we didn’t propose a domain, but rather set out to validate whether **CollabBerry’s peer-based allocation and accountability tools** could serve across domains as a complementary mechanism.

Where this connects for us is at the intersection of **trust and compliance**. KYC ensures legitimacy at the level of *who receives funds*. CollabBerry experiments with legitimacy at the *contributor level* once funds enter a project — ensuring fair, transparent distribution through peer-to-peer assessments and automated payouts.

Together, privacy-preserving KYC and contributor-level accountability could form two layers of assurance: one external (validating recipients) and one internal (validating allocations within teams). Both strengthen trust in how public goods funding is used.

We’d be curious: do you see potential alignment between external compliance mechanisms like KYC and internal accountability tools like CollabBerry to create an end-to-end trust framework for grants?

-------------------------
