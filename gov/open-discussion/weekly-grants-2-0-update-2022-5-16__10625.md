---
id: 10625
title: "Weekly Grants 2.0 Update — 2022/5/16"
slug: weekly-grants-2-0-update-2022-5-16
category: open-discussion
url: https://gov.gitcoin.co/t/weekly-grants-2-0-update-2022-5-16/10625
created_at: 2022-05-16T18:54:39.123Z
last_posted_at: 2022-05-18T10:32:07.772Z
posts_count: 7
views: 3493
like_count: 16
---

# Weekly Grants 2.0 Update — 2022/5/16

<https://gov.gitcoin.co/t/weekly-grants-2-0-update-2022-5-16/10625>
erich | 2022-05-20 09:20:52 UTC | #1

*This thread consolidates weekly updates for various initiatives affecting the Gitcoin Grants 2.0 protocol.*

*The primary use of this thread is for updates from the Grants 2.0 team at Gitcoin. Still, it may also include updates from projects that utilize the Grants 2.0 toolkit or build related/similar social technologies.*

---

Grants 2.0 is an open-source technology for pluralistic and scalable public goods provision. We are building a modular toolkit for Quadratic Funding and adjacent social incentive designs that enables decentralized, self-organizing ecosystems to increase and govern their capital.

# Relevant Documents

* [Gitcoin Grants 2.0 Vision](https://gov.gitcoin.co/t/gitcoin-grants-2-0/9981?u=leone)
* [Quadratic Funding](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3243656) paper
* [Decentralized Society](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763) paper
* Design prototypes
  * [dPopp Project](https://www.figma.com/proto/RIsPkjpIaeEc73SjLiHK2G/dPopp?page-id=1652%3A46017&node-id=1654%3A46865&viewport=-1674%2C-220%2C0.15&scaling=min-zoom&starting-point-node-id=1654%3A46865&show-proto-sidebar=1)
  * [Grants Hub](https://www.figma.com/file/obBzCCL8KwoTlVBb5g3ccN/Grant-Hub---Wireframes?node-id=249%3A1000)
* Staging applications
  * [dPopp Project](https://orange-sky-5671.on.fleek.co/)
  * [Grants Hub](https://gitcoinco.github.io/grants-hub/)
* Video demonstrations
  * [dPopp Project](https://drive.google.com/file/d/1tsgcrGoO6gQQBTsfSWm3P-hnLacvP8Aa/view?usp=sharing)
  * [Grants Hub](https://drive.google.com/file/d/1WUDBWIEBvwiQq0xWr368IPdlZCWsTkRo/view)


# 2022/05/16 Update

## Highlights

* The dPopp Project, the identity verification application for contributors, is in full swing building the MVP for Grants Round 14. Momentum is growing substantially.
* Grants Hub, the grantee project registry, aims to be production-ready **by July 1st** when we'll prompt projects in Gitcoin Grants to migrate over.
* The team kicked off work on the Round Manager. This Quadratic Funding module will connect contributors, grantees, and matching funders.

## Product Work

### dPopp Project

* Planned for dPopp to cGrants integration.
* Separated work into tracks to scale efforts: verifiable credentials, grants, reader, and interface.
* Added all stories needed for MVP in the backlog.
* Added weekly updates and dPopp to cGrants product requirements document.
* **Further research on BrightID and Idena.**
* **Finish details on dPopp to cGrants integration.**
* **Increase coordination on branding.**
* **Prioritize MVP & GR14 deadlines.**

### Grants Hub

* Improved Grant Hub documentation flow.
* Notion page now hosts hub v1 PRD and weekly team updates.
* Github Project now includes new requirements from Round Manager kickoff and updated timelines.
* **Get v2 of Grant Hub PRD ready with updated MVP use cases and short-term + long-term roadmap.**
* **Tag team with Eduardo and Nate on user research and testing for Round Manager and the "Apply to a Round" flow:** Start sourcing partners and questions to ask partners.

## Design Work

### dPopp Project

* Reviewed mockups for MVP UI changes.
* Created mockups for dPopp to cGrants.
* **Finish adding micro-interactions:** The goal is to create a high-fidelity end-to-end prototype for testing.

### Grants Hub

* Updated user flows & wireframes with changes from Round Manager kickoff
* Kicked off user interviews this week.
* **Start testing mid to high-fidelity prototypes with users for Grant Hub & Round Manager.**

## Engineering Work

### dPopp Project

* Completed migration of credential storage to ceramic from local storage
* Worked on build issues w/ dPopp app & reader app, (due to monorepo & shared dependencies).
* Made progress on ENS, PoH, and Twitter stamps.
* Built v1 of the Reader, completing a single slice of end-to-end.
* **Split the monorepo to reduce build issues** (also makes codebase easier to fork)
* **Start work on new tracks:** Grants and Interface.
* **Reduce tech debt:** Add Ceramic integration tests into the CI pipeline and improve application unit tests.

### Grants Hub

* Steel thread proof of concept is demo ready — included login, create and view a grant, and publish a grant (edit a grant is WIP).
* **Add edit-a-grant functionality.**
* **Lint the code base and remove any existing error.**
* **Get the front end code coverage up & the UI looking good.**
* **Start technical documentation.**

## Marketing and Communications

Organized a dPopp Project branding/naming workshop with @seanmac and @seedphrase and various product stakeholders.

-------------------------

lefterisjp | 2022-05-16 19:22:46 UTC | #2

Hey thanks a lot for the update!

[quote="erich, post:1, topic:10625"]
Grants Hub, the grantee project registry, aims to be production-ready **by July 1st** when we’ll prompt projects in Gitcoin Grants to migrate over.
[/quote]

Question for this. So for S15 all grants will be on 2.0, or do you intend to have some experiment with 1.0 and some in 2.0?

-------------------------

owocki | 2022-05-16 20:27:52 UTC | #3

Hey Leon, are there any plans to release the demo videos that is in #gpc-demos on discord, here, on the weekly thread?

Any plans to have the round manager updates on this thread too?

-------------------------

ZER8 | 2022-05-16 23:55:41 UTC | #4

I believe only one round will run on G 2.0 in GR15....Let me find the diagram

-------------------------

erich | 2022-05-17 10:59:48 UTC | #5

Thanks, Owocki -- I just added the video demonstrations.

[quote="erich, post:1, topic:10625"]
Video demonstrations

* [dPopp Project](https://drive.google.com/file/d/1tsgcrGoO6gQQBTsfSWm3P-hnLacvP8Aa/view?usp=sharing)
* [Grants Hub](https://drive.google.com/file/d/1WUDBWIEBvwiQq0xWr368IPdlZCWsTkRo/view)
[/quote]

To your question about the Round Manager: @nategosselin, are you driving the Round Manager? If so, would you mind providing a related weekly update via Discord on Fridays, too, so we can consolidate it here alongside the other Grants 2.0 updates?

-------------------------

lthrift | 2022-05-17 19:35:08 UTC | #6

The plan at this point is for all projects to register in the Grant Hub for GR15 and we will reflect those projects in the current gitcoin.co grant explorer. More details to come as we get the core components built and map out the exact adoption plan.

-------------------------

vogue20033 | 2022-05-18 10:32:07 UTC | #7

Nice update here. Thanks Leon.

-------------------------
