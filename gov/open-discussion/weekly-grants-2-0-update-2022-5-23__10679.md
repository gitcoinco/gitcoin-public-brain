---
id: 10679
title: "Weekly Grants 2.0 Update — 2022/5/23"
slug: weekly-grants-2-0-update-2022-5-23
category: open-discussion
url: https://gov.gitcoin.co/t/weekly-grants-2-0-update-2022-5-23/10679
created_at: 2022-05-23T08:28:07.261Z
last_posted_at: 2022-05-23T21:24:40.677Z
posts_count: 2
views: 3038
like_count: 5
---

# Weekly Grants 2.0 Update — 2022/5/23

<https://gov.gitcoin.co/t/weekly-grants-2-0-update-2022-5-23/10679>
erich | 2022-05-23 15:15:46 UTC | #1

**Grants 2.0** is an open-source technology for plural and scalable public goods provision. It's a modular toolkit for social ecosystems to utilize Quadratic Funding and adjacent incentive designs. 

# Relevant Documents

* [Gitcoin Grants 2.0 Vision ](https://gov.gitcoin.co/t/gitcoin-grants-2-0/9981)
* [Quadratic Funding](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3243656) paper
* [Decentralized Society](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763) paper
* Design prototypes
  * [dPopp Project](https://www.figma.com/proto/RIsPkjpIaeEc73SjLiHK2G/dPopp?page-id=1652%3A46017&node-id=1654%3A46865&viewport=-1674%2C-220%2C0.15&scaling=min-zoom&starting-point-node-id=1654%3A46865&show-proto-sidebar=1)
  * [Grants Hub](https://www.figma.com/file/obBzCCL8KwoTlVBb5g3ccN/Grant-Hub---Wireframes?node-id=249%3A1000)
* Staging applications
  * [dPopp Project](https://orange-sky-5671.on.fleek.co/)
  * [Grants Hub](https://gitcoinco.github.io/grants-hub/)
* Demonstrations
  * [dPopp Project](https://drive.google.com/file/d/1iCMXxa8k5UPS7xV37-N0oGqexrF5tF4G/view?usp=sharing)
  * [Grants Hub](https://drive.google.com/file/d/1WBKMANj0tvb-yyF_kPxXd6gJHyfYuvvD/view?usp=sharing](https://drive.google.com/file/d/1WBKMANj0tvb-yyF_kPxXd6gJHyfYuvvD/view?usp=sharing))
  * [Round Manager / Explorer](https://miro.com/app/board/uXjVO2CrhpI=/?moveToWidget=3458764525471008392&cot=14)

# 2022/5/23 Update

By the product managers: @brent (dPopp Project), @michelle_ma (Grants Hub), and @nategosselin (Round Manager / Explorer)

## Highlights

* The dPopp project is on course to complete the minimum viable product for Grants Round 14 - i.e., ready for adoption towards GR14's Trust Bonus. This week we are about ~87% complete with our MVP Goal, with about ~83% of our timeline complete. We also have made significant progress on the reader implementation into Trust Bonus.
* Grants Hub targets to be dev and testing-complete with Grants Hub minimum viable product by Friday, June 3rd. With this week’s progress, they are about ~30% of the way to hitting that milestone. Their goal is to have Grants Hub production-ready **by July 1st, 2022**, in time for the GR14 claims period, where we will prompt grants owners to migrate their grants from cGrants to Grants Hub.
* The Round Manager / Grant Explorer team hopes to run ~3 alpha rounds on their minimum viable product before November. That should enable us to run at least one of the end-to-end GR16 ecosystem rounds on the new protocol. The goal for GR17 is to run all rounds on the protocol. The team aims to scope out the minimum viable product by next week.

## Product Work

### dPopp Project

* Paired w/ engineering to remove the logjam in backlog, knocking out a lot of Acceptance Criteria
* Planned dPopp Project branding w/ GR14 (launching alpha - for Gitcoin use only)
* Worked on the path to prod details and any launch plans
  * Created checklist for prod and determined URL location/domain to use for GR14
  * Started planning support strategy for GR14
* Researched BrightID & Idena integrations
* **Finish support strategy for GR14 and communicate plans**
  * Coordinate with Gitcoin support team on support details
  * Establish on-call plans for engineering & product support
* **Lots of product walkthroughs to test UX and clean up small interactions**
* **Research usage numbers of previous rounds for better traffic expectations for GR14**

### Grants Hub

* Completed v2 product requirements document with updated phases and timelines available.
* **Start research for Round Operators** (i.e., if grant owner details are needed, et cetera.)
* **Finalize Round Manager <> Grant Hub flow interaction** (applying to a round, tracking grant status, et cerera.)

### Round Manager / Explorer

* The Round Manager team has partnered with GPC leadership and the Grant Hub team over the past two weeks to officially kick off the Round Manager work and scope the MVP. Given OOO and time zone differences, we've been able to have five synchronous sessions of 2-4 hours each. In that time, we've reviewed/aligned on the Genesis Brief, documented initial risks, and mapped about 90% of the Round Manager journey, including:
  * Creating a program and adding team members
  * Configuring a round and deploying it
  * Applying to a round (though this will live in Grant Hub)
  * Reviewing and approving grants
  * Starting, operating, and closing a grants round
  * Note: we decided the round payout process requires more product discovery (see goals below)
* Find out more:
  * [Genesis brief](https://www.notion.so/Grants-Explorer-and-Round-Manager-Genesis-c74df8c04e0e45898f1885ad6a8bb5c8)
  * [Kickoff Miro board](https://miro.com/app/board/uXjVO2CrhpI=/?moveToWidget=3458764525471008392&cot=14)
  * [Kickoff meeting notes](https://www.notion.so/Grants-Explorer-and-Round-Manager-Genesis-c74df8c04e0e45898f1885ad6a8bb5c8)
* **Map user journey for Grant Explorer**
* **Align on the timeline for Round Manager / Grant Explorer Minimum Viable Product**
* **Steel thread stories for Round Manager**
* **Discovery of KYC/payout requirements**

## Design Work

### dPopp Project

* Worked on micro-interactions for a hi-fidelity end-to-end prototype
* **Further work on micro-interactions and small cleanup details**
* **Finalize minimum viable product of verifiable credential flow designs in the prototype and Figma doc clean up ready for dev**

### Grants Hub

* Produced high-fidelity mocks for Grant Hub.
* **Start designs for GR14 Claims flow** (prompt users to migrate their grants from cGrants to Grant Hub)
* **Start designs for “applying to a round” and “tracking grant status” via Grant Hub.**

### Round Manager / Explorer

**Draft user flows/wireframes for Round Manager**

## Engineering Work

### dPopp Project

* Began verifiable credentials: POAP and Facebook
* Completed several variable credentials: ENS, PoH, Twitter, Facebook
* Started work on new tracks: Grants & Interface
  * Created dPopp-reader repo enabling content pull of a passport based on the wallet address
  * Styled verifiable credential interfaces, including updating tests to account for the style changes
* Deployed ceramic node on staging
* **Finish verifiable credentials for GR14: POAP and BrightID**
* **Finish planning task list for prod readiness details**
* **Continue work on Ceramic Mainnet Network, including coordination with Ceramic team to allow listing**
* **Complete Grants work - reader implemented into Trust Bonus**
* **Monitor and stress test nodes**

### Grants Hub

* Built out “edit project” functionality
* Made progress on UI — improved layout of Grants Hub
* **Continue working on UI to match hi-fidelity designs.**
* **Continue research on Grant Hub storage options** (IPFS, Ceramic, et cetera.)

### Round Manager / Explorer

* The engineering team has worked on setting up the technical environments for our team development, mainly mirroring the Grant Hub setup.
* Relevant links:
  * [Github team](https://discord.com/channels/562828676480237578/974183960240336916/974184399748862032)
  * [Github Project](https://github.com/orgs/gitcoinco/projects/8)
  * [Github Repo](https://github.com/gitcoinco/grants-round)
* **Steel thread development for Round Manager**
* **Continue environment setup**

## Marketing and Communications

* The dPopp Project continued work on its branding: “The dPopp Project is an identity verification application. It provides a secure, flexible & plural container for an individual's verifiable credentials. Digital applications (such as Gitcoin Grants) adopt the dPopp Project to verify unique personhood and memberships and increase plurality.”
* At a meetup organized by Ethereum Foundation in Berlin **on May 25th**, @kevin.olsen and I will give a presentation about the evolution of Gitcoin Grants and how Grants 2.0 can scale up plural capital provision: https://www.meetup.com/de-DE/Berlin-Ethereum-Meetup/events/285987321/

-------------------------

owocki | 2022-05-23 21:24:40 UTC | #2

i already left my comments on last weeks progress in discord.  can copy it here if we want to use the gov forum as the source of truth in future :P

-------------------------
