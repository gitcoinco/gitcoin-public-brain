---
id: 10760
title: "Weekly Grants 2.0 Update – 2022/5/30"
slug: weekly-grants-2-0-update-2022-5-30
category: gitcoin-grants
url: https://gov.gitcoin.co/t/weekly-grants-2-0-update-2022-5-30/10760
created_at: 2022-05-30T17:54:18.405Z
last_posted_at: 2022-12-06T06:43:41.348Z
posts_count: 3
views: 2795
like_count: 3
---

# Weekly Grants 2.0 Update – 2022/5/30

<https://gov.gitcoin.co/t/weekly-grants-2-0-update-2022-5-30/10760>
erich | 2022-06-01 17:37:01 UTC | #1

Grants 2.0 is an open-source technology for plural and scalable public goods provision. We are building a modular toolkit for Quadratic Funding and adjacent social incentive designs to increase and govern ecosystem capital.
# Relevant Documents

* [Gitcoin Grants 2.0 Vision ](https://gov.gitcoin.co/t/gitcoin-grants-2-0/9981)
* [Quadratic Funding](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3243656) paper
* [Decentralized Society](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763) paper
* Design prototypes
  * [Passport Project](https://www.figma.com/proto/RIsPkjpIaeEc73SjLiHK2G/dPopp?page-id=1652%3A46017&node-id=1654%3A46865&viewport=-1674%2C-220%2C0.15&scaling=min-zoom&starting-point-node-id=1654%3A46865&show-proto-sidebar=1)
  * [Grants Hub](https://www.figma.com/file/obBzCCL8KwoTlVBb5g3ccN/Grant-Hub---Wireframes?node-id=249%3A1000)
  * [Round Manager / Explorer](https://miro.com/app/board/uXjVOyDFRMM=/?share_link_id=778953574277)
* Staging applications
  * [Passport Project](https://orange-sky-5671.on.fleek.co/)
  * [Grants Hub](https://gitcoinco.github.io/grants-hub/)
* Video demonstrations
  * [Passport Project](https://drive.google.com/file/d/14J5kZhF6G7_-OJZyEp6aKlLHymH2Aqqi/view?usp=sharing)
  * [Grants Hub](https://drive.google.com/file/d/1FALvA6LIyVFmwL_0W0HraFfDwGrQEUQH/view)
# 2022/5/30 Update

## Highlights

* The Passport is ~93% of our MVP Goal, with a week left on our timeline (same for the other goal of using Passport for Trust Bonus in GR14); this means we have one last stamp to finish and a few minor UI changes. While we're on course to complete, ideally, we would have spent about 1-2 weeks sooner to give us plenty of time to test everything. Next week, we will evaluate our product, processes, support, et cetera, to make sure it's ready to run on GR14. I'll be asking people to jump in, create Passports, connect them to their profile on Gitcoin, and give feedback. On Wed (June 1st), we'll decide whether we're confident about running Passport for GR14. So far, things look good, but there are very tight timeframes here.
* The Grants Hub will be dev-complete with Grant Hub by Friday, 6/3. We are about 60% to hitting our MVP milestone with this week's progress. Our goal is to have Grant Hub production-ready **by July 1st, 2022**, in time for the GR14 claims period, where we will prompt grant owners to migrate their grants from cGrants to Grant Hub.
* The Round Manager / Explorer team spent a significant chunk of our team time prepping cGrants for GR14, but we have outlined our Steel Thread for Round Manager and begun shipping core pieces of our development foundation!

## Product Work

### Passport

* Passport changed to Gitcoin Passport
* Strategy/Planning beyond GR14
* Coordination w/ Grants support team for GR14
* Wrote Passport Bug Bounty
* Prod Readiness Planning
* **More coordination w/ the Grants support team for GR14**
* **Internal Testing from Gitcoin/GitcoinDAO**
* **Shipping additional support documentation**
* **Product documentation cleanup**
* **Anything and everything needed to prep us for GR14**

### Grants Hub

* Started User Research Hub for Grants 2.0 overall
* Meeting with Grants Ops team members this week and next to get acquainted and start Round Operator / Gitcoin internal research
* **Set up a testing cadence for Grants 2.0** — internal (potential weekly live demo and Q&A session) and external (user interviews)
* **Convert PRD into a deck for a more visual timeline and roadmap for Grant Hub**

### Round Manager / Explorer

* Created Steel Thread[ mockups](https://miro.com/app/board/uXjVOyDFRMM=/?share_link_id=778953574277) and[ opportunity brief](https://www.notion.so/Steel-Thread-fd85d8ce97c4420f84828fdb3e0c1f91)
* (additional cycles spent on cGrants / GR14)
* **Organize and kickoff wave of user discovery**

## Design Work

### Passport Project

* UX/UI updates
* Supported engineering team w/ UX/UI direction and feedback
* **Minor UX/UI updates**

### Grants Hub

* Completed designs for GR14 CTA (for prompting folks to migrate to Grant Hub during GR14 Claims period)
* Started explorations for the “apply for a grant” flow in Grant Hub for Phase 2 (Anchor) and Phase 3 (Alpha)
* **Refine explorations of the "apply for a grant" flow in Grant Hub for Phase 2 (Anchor) and continue the flow for Phase 3 (Alpha)**

### Round Manager / Explorer

* The first draft of Round Manager[ wireframes](https://www.figma.com/file/aZ3oDEvJOTWnbxn1js1SIq/Round-Manager---Wireframes?node-id=2%3A90)
* **Next rev of Round Manager Wireframes**

## Engineering Work

### Passport

* Completed POAP Identity Stamp
* Landing Page and Stamp dashboard UI updated
* We set the Web2 integrations to "live" (Google, Facebook)
* passport.gitcoin.co is ready to go Live
* Reader for Trust Bonus Score integration is functionally complete (gitcoin.co/trust)
* **Finish BrightID stamp**
* **Minor UX/UI improvements for Reader on /trust**
* **Get node allowlisted by the Ceramic team**
* **Complete Ceramic Mainnet connection**
* **Continue planning Sybil prevention/detection supported by protecting PII through stamps/VC**

### Grants Hub

* Researched and reworked the project hub contract to allow multiple owners in a gas efficient way
* Researched indexing solutions for cross contract/L2 deployments
* Researched file storage protocols that could enable gasless updates of metadata
* Began work on the design system/component library
* **Dev-complete with Grant Hub — matches hi-fidelity designs**
* **Start work on GR14 CTA**

### Round Manager / Explorer

* Integrated styling tool, Tailwind
* Created base contract setup and architecture
* Added solidity coverage support
* Wrote PRs for IPFS/action reducer and deployed script for GrantRoundImplementation
* (additional cycles spent on cGrants / GR14)
* The completed pull request for our [base contract setup](https://github.com/gitcoinco/grants-round/pull/2)
* The completed pull request for [integrating our styling tool, Tailwind](https://github.com/gitcoinco/grants-round/pull/13/files)
* **Finish environment setup**
* **Work on Steel Thread**

## Marketing and Communications

We rebranded the dPopp Project to the **Gitcoin Passport**, as you might have noticed.

-------------------------

owocki | 2022-05-30 18:24:34 UTC | #2

Thanks leon!  I left some comments in the discord demo channels.

For others in the DAO - I'd be curious if these weekly G2.0 updates are useful.   What would have to be true for these updates to be a focal point upon which the DAO rallies around G2.0?

-------------------------

s9aintQAI | 2022-12-06 06:43:41 UTC | #3

Hello, where can I see the latest on the Grants 2.0 launch?

-------------------------
