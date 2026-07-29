---
id: 20975
title: "[GG23] Hypercerts For Nature Stewards – Full Round Report"
slug: gg23-hypercerts-for-nature-stewards-full-round-report
category: gitcoin-grants
url: https://gov.gitcoin.co/t/gg23-hypercerts-for-nature-stewards-full-round-report/20975
created_at: 2025-06-16T05:07:11.542Z
last_posted_at: 2025-07-03T18:58:25.262Z
posts_count: 2
views: 1574
like_count: 14
---

# [GG23] Hypercerts For Nature Stewards – Full Round Report

<https://gov.gitcoin.co/t/gg23-hypercerts-for-nature-stewards-full-round-report/20975>
fatinhamzah96 | 2025-06-16 05:14:30 UTC | #1


The GG23 Hypercerts for Nature Stewards Round supported 29 environmental projects across the globe through a hybrid funding model that rewarded both public support and verified impact. This report outlines how we ran the round, what worked, key results, and lessons for the future.

## Round Period
Application Period: March 17 – April 16, 2025 (rolling application)
Donation Period: April 2 – April 16, 2025

## Acknowledgements
We extend our deepest thanks to all participants, project teams, donors, community supporters, and contributors who made this round a success. 
Special thanks to round funders  (each contributed 5,000 USDGLO, total 20,000 USDGLO):
- GainForest
- Hypercerts Foundation
- Ma Earth
- Celo Public Goods – ‘Matching on Matching Program’

Thank you to Gitcoin for enabling us to participate and connect with the broader Web3 community.

## Organizers & Advisors
**Round Operators:** Nurfatin Hamzah (GainForest), Holke Brammer (Hypercerts Foundation) | @holkeXYZ

**Advisor:** Sophia Rokhlin (Ma Earth)

**Coordination Team:** Sharfy Adamantine, David Dao, Niña Cerilla, Satyam Mishra, Gabriel Nunes, Diego Rivera Buendía (all GainForest)

## Summary of Results
**Applications:** 36 projects applied
**Donations:** 922 individual donations
**Unique Donors:** 350 people contributed
**Total Donated:** $4,117.27 (including $504.35 in total fiat donations, of which $362.10 came from 32 verified PayPal accounts via normie.tech)
**Match Pool:** 20,000 USDGLO (≈$19,975)
**Platform(s) Used:** Ecocertain.xyz, Gitcoin Builder, Gitcoin Grants Stack, Paypal donation via normie.tech for non-Web3 donors


## Background of This Round
This round focused on driving adoption of Ecocert, a new Environmental Hypercert hosted on [Ecocertain.xyz](http://ecocertain.xyz). Ecocerts serve as trusted, data-backed certificates that document real environmental impact. By using them, nature stewards can showcase their work transparently and connect with Web3 donors through a dedicated impact marketplace.

We received 36 applications and selected 29 projects to take part in the round. Of these, 9 were completely new to Web3. Our team supported all selected projects in creating and publishing their Ecocerts. For the newcomers, we guided them from scratch—setting up wallets, creating Gitcoin Builder profiles, issuing Ecocerts, and learning how to promote their work. To make this process smooth, we used the **GainForest Buddy System**, pairing each steward with a mentor for 1:1 support and regular check-ins. We also created demo videos and shared basic marketing materials to support them in communicating their impact.

To make the process more accessible, we used **Google Forms for applications** instead of requiring applicants to start with a Gitcoin Builder profile, which typically needs a Web3 wallet from the beginning. This approach was inspired by the onboarding strategy used by Ma Earth in a previous round. It helped lower the barrier for nature stewards unfamiliar with Web3 and allowed us to onboard them gradually before introducing more technical steps like wallet creation and Gitcoin Builder Profile setup.

In addition, we introduced **Paypal donations** to make it easier for non-Web3 donors to support these projects. This expanded visibility and unlocked a broader base of support. The cost for Paypal donation adoption was covered by Celo Public Goods (many thanks!!).

## Impact Quadratic Funding (ImpactQF) & Matching Funds Distribution
We recently introduced Impact Quadratic Funding (ImpactQF) to distribute matching funds in this round. ImpactQF builds on traditional quadratic funding by addressing a key gap: standard QF often favors projects with strong marketing over those with real, measurable impact. Regen Coordination Global GG23 also used ImpactQF in their round, reflecting a shared push for impact-based funding.

The mathematical foundation of ImpactQF modifies traditional quadratic funding by incorporating impact verification:
![enter image description here](upload://lKAX7vjrrR3zsELRPZ8yPGP4Ucr.webp)

In this formula, each contribution (ci) is multiplied by an impact verification score I(x) derived from impact quality evaluations. This ensures that funds flow to projects delivering genuine environmental outcomes rather than just those with effective marketing campaigns.

Key features of ImpactQF include:


 **1. Broad Community Support through COCM (Connection-Oriented Cluster Matching) – provided by Gitcoin**

We used COCM data from Gitcoin to score contributor addresses. This system identifies legitimate users and protects matching funds from sybils and airdrop farmers.
 - 100% of contributor addresses were scored using the Passport system
 - 58 Users (16.6%) received full matching (passport score over 50)
 - 6 Users (1.7%) received partial matching (passport score between 25 and 50)

*🔹 Full matching means contributions are matched at 100% of the calculated amount.
🔸 Partial matching means contributions are matched between 50-100%, depending on passport scores.*

**2. Impact Quality Consideration using [DeepGov](https://www.deepgov.org/) - evaluated externally**

Impact scores from DeepGov are integrated directly into our matching formula through the I(x) component. DeepGov is an AI-powered governance platform that evaluates and scores the quality of project impact, with these scores mathematically weighting each contribution before calculating matches.

To simulate diverse evaluation perspectives, we used three scoring personas in DeepGov:

 - **Panda** (41.9%) – Prioritizes community alignment and storytelling clarity
 - **Luna** (38.7%) – Focuses on data transparency and verifiability
 - **Ultra-Grant** (19.4%) – Values scale and systemic potential

Each project received a final weighted score based on these personas. This determined the allocation of the DeepGov-based portion of the match pool.

During the process of customizing DeepGov for this round, we received a concern from a previous round operator regarding a project with a history of fund misuse. In response, we made a manual adjustment to that project’s score within DeepGov to reflect this risk, ensuring responsible fund allocation.

Projects evaluation and the individual feedback from each persona on DeepGov can be viewed here:
 👉 Visit [this page](https://allo.deepgov.org/) and select project & round to see the detailed review.
 
## How ImpactQF Was Calculated for this round
Each project received an Impact Score from DeepGov, expressed as a percentage, which was used to weight its COCM-adjusted match from Gitcoin. The formula for the raw ImpactQF value is:
	
	ImpactQF = (COCM Match) × (Impact Score %) ÷ 100
To stay within the fixed $20,000 matching pool, we applied a scaling factor. Each project’s raw ImpactQF value was divided by the total of all raw ImpactQF scores, then multiplied by $20,000:
	
	Scaled Match = (Raw ImpactQF ÷ Total Raw ImpactQF) × $20,000
This process ensures that funding is distributed proportionally based on both independent community support and verified environmental impact, while respecting the total matching fund cap.

## Proof of Impact: The Role of Stamps in Ecocert
To further strengthen impact verification, projects were required to submit “stamps” as part of the Impact Passport system. These stamps act as digital proofs of impact and include verifiable evidence such as geotagged tree planting data, photos and videos of events, formal reports, and other relevant documentation.

![Example of Proof of Impact](upload://7SCYStpgEq1zQj1JFevVwN2OzFa.webp)

In this round, these stamps were integrated into the Ecocert platform’s “Proof of Impact” section, creating a transparent and accessible repository of each project’s impact claims. This evidence plays a critical role in validating the DeepGov impact scores and ensuring that the matching funds are truly supporting projects delivering measurable environmental benefits.

**Read more about the Impact Passport and ImpactQF framework [here](https://gov.gitcoin.co/t/citizen-grants-gcp-impact-passports-and-impact-quadratic-funding-impactqf/19712).**

## Insights from the Hybrid Matching Model
With ImpactQF, we aimed to balance community support with project quality and accountability.

After analyzing the final results, we observed key trends:

 **1. Impact Scores Actually Changed How Money Was Distributed**
When we factored in how well projects performed, about $2,700 (13.5% of all funding) moved from one project to another. This shows that measuring impact creates real financial consequences, not just feel-good metrics.

**2. Popular Projects Aren't Always the Best Performers**
There was almost no connection between which projects the community initially funded most and which ones actually delivered the best results. Community excitement doesn't guarantee project success.

**3. We Found Unexpected Winners** 
The hybrid approach revealed 4 "hidden gems" - small projects that delivered amazing results despite getting little initial funding.

### Payout of Matching Funds
The distribution of matching funds will be executed by purchasing portions of each project’s Ecocert on ecocertain.xyz, proportional to the matching amount they have earned. This approach not only delivers funding but also encourages projects to enrich their Ecocerts with ongoing proof of impact—creating a trackable, evolving record of their work. Payouts will be completed within 3-4 days after the round report is published.

### Results Summary Table
![enter image description here](upload://alTz7uOodY4BQFXld6MLNwp8xcb.webp)

## What Went Well
### During the round
- Successfully onboarded nature stewards new to Web3, helping them engage in impact funding.
- Established a dedicated marketplace for impact certificates through Ecocert on Ecocertain.xyz.
- Attracted Web3-native projects engaged in land restoration and conservation into the GainForest network, supporting ongoing monthly community calls.
- The GainForest Buddy system helped onboard everyone to Ecocertain.xyz, which is a new platform, and provided extra support for those new to web3 by guiding them step-by-step.
- Added new ‘Proof of Impact’ feature to Ecocert, allowing projects to attach multiple links to increase certificate quality and credibility.
- Supported grantees with basic marketing materials to help them promote their work effectively.

### Post round
- Invited all participating projects to join the GainForest network to stay connected and access ongoing support. 
- Hosted two post-round community calls to foster learning and peer exchange:
	- A sharing session featuring five project teams from this round, who reflected on their experience and lessons learned
	- A peer-sharing session by Frank Hu from Green Sofa Taiwan on Impact Storytelling, helping grantees strengthen how they communicate their work.

**Watch the recordings [here](https://gainforest.gitbook.io/docs/community/monthly-community-calls)!**

## Challenges & How We Handled Them
**1. Onboarding & Coordination**
Onboarding time was limited to under two weeks, requiring intensive hand-holding—especially for 9 communities new to Web3, starting from wallet creation. Coordination was manageable with 29 projects, but scaling will need more streamlined onboarding to avoid overburden.
Due to the intensive onboarding required, both grantees and the team had limited capacity to promote their campaigns during the round. In future rounds, we plan to strike a better balance between onboarding support and promotional momentum.

**2. Technical Challenges with ImpactQF**
This round involved experimenting with ImpactQF for the first time, which brought several technical and coordination challenges. We used DeepGov, a new tool that enables configurable AI politicians for capital allocation and governance. While promising, it took time to adapt and code DeepGov specifically for the structure of this round.

We had planned to integrate DeepGov outputs with Quadratic Funding (QF) scores from Gitcoin. However, due to timing and ongoing platform changes, the data for our round was not indexed, and the CSV export came out empty. By the time we followed up, the Gitcoin Grants Manager platform had sunset, which meant we no longer had access to the built-in scoring tools.

We’re deeply thankful to the Gitcoin team, especially Mathilda and Bliss, who generously supported us despite these changes. They provided access to temporary open-source data, which allowed us to continue. 

## Lessons Learned
**1. Start Early & Streamline Onboarding**
Onboarding nature stewards to Web3 tools needs to start earlier and be more continuous, especially since intensive hand-holding is required for newcomers. While coordination was manageable with 29 projects, scaling to more communities will require streamlined onboarding processes to avoid overburdening the team and grantees.

**2. Expand Demo & Support Materials**
Providing demo videos proved highly valuable for easing the learning curve and should be expanded alongside other user-friendly resources.

**3. Balance Onboarding and Promotion Efforts**
There is a trade-off between onboarding support and promotion time—intensive onboarding limited the time grantees and the team could spend on promotion during the round. Future rounds should plan carefully to balance these demands.

**3. Prepare for Technical Adaptations**
Experimenting with new tools like DeepGov brought valuable insights but also required additional time to adapt and integrate. We aim to build flexibility into timelines to accommodate this in the future.

## Looking Ahead
- Projects can continue reporting proof of impact and create new Ecocerts as they generate more outcomes funded by this round.
- Plan to integrate demo videos directly into Ecocertain.xyz to ease onboarding.

## Paypal Donation through [normie.tech](https://normie.tech/)
To increase accessibility and visibility for projects, we enabled donors who do not use Web3 wallets to support projects via Paypal through normie.tech. This option allows a broader audience to contribute, expanding the donor base beyond crypto users. The adoption costs for this Paypal donation method were covered by Celo Public Goods.

In total, **$504.35 USD was raised via PayPal donations, of which $362.10 USD came from 32 verified PayPal accounts**. Each verified account is counted as a unique donor, which is important because the number of verified donors influences the amount of matching funds each project receives.

## Conclusion
This round marks a step forward in redefining how environmental efforts are recognized and supported. By onboarding nature stewards into Web3, we introduced an alternative path to traditional funding—one that is more accessible, transparent, and impact-driven. We intentionally designed this process to lower the barriers for first-time Web3 users, while strengthening connections between established environmental groups already active in the Web3 space.

Through Ecocert and the Ecocertain.xyz marketplace, we began addressing a key gap in Web3 funding: the tendency to reward marketing over measurable impact. This experiment with impact-based Quadratic Funding offered a way to center the real work being done on the ground.

This collective effort wouldn’t have been possible without support from environmentally aligned communities such as Hypercerts Foundation, Ma Earth, and Celo Public Goods. Nature is a shared commons and this round proves that funding its protection can be reimagined.

-------------------------

Sov | 2025-07-03 18:58:25 UTC | #2

Thanks for this detailed retrospective. 

The experiment shows promise, particularly in that impact scores shifted the funding distribution.  The finding that community enthusiasm doesn't correlate with delivery matches what I've observed across other ecosystems.  This hybrid QF model could be valuable for other impact rounds.

Thanks for the partnership and solid execution through the technical challenges.

HTH!

-------------------------
