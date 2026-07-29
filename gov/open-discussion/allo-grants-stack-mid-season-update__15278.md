---
id: 15278
title: "Allo + Grants Stack Mid-Season Update"
slug: allo-grants-stack-mid-season-update
category: open-discussion
url: https://gov.gitcoin.co/t/allo-grants-stack-mid-season-update/15278
created_at: 2023-06-08T13:30:38.833Z
last_posted_at: 2023-06-08T13:30:38.914Z
posts_count: 1
views: 2010
like_count: 10
---

# Allo + Grants Stack Mid-Season Update

<https://gov.gitcoin.co/t/allo-grants-stack-mid-season-update/15278>
meglister | 2023-06-08 13:30:38 UTC | #1

Authors: @meglister and @nategosselin 

While we’re not quite halfway through S18 yet, it’s been such an eventful month that we wanted to share some mid-season updates from the Allo + Grants Stack workstream!

The highlights:
* Allo + Grants Stack team split
* Grants Stack S18 strategy and roadmap
* Allo v2 and S18 strategy

## Allo + Grants Stack Team Split
Allo and Grants Stack remain funded and organized as a single workstream for S18 & S19. The product, engineering, data, developer relations, and product support resources that are part of the workstream have formally organized into two separate teams within the workstream, each focused on a specific user archetype and associated product:

* **Allo Protocol** for developers requiring resource allocation tools
* **Grants Stack** for program managers requiring a user-friendly tool for operating grants programs

### Why now?
We’re making this split now because we are at a natural inflection point with our initial products launched, and because this user-focused organizational structure unlocks key benefits that will enable us to better pursue our goals. Additionally, with Meg joining as Product Lead for Grants Stack in May, we have the resources available to lead these products independently.

### Why split?
We’re splitting the two teams because we think that this structure will better position us to pursue our goals. Specifically, we think our teams will benefit from:

1. **User-centric Product Focus:** By establishing dedicated teams for Allo Protocol and Grants Stack, we can foster a stronger product focus. Allo Protocol targets developers, necessitating a deep understanding of their technical needs, preferences, and challenges. Grants Stack, on the other hand, caters to end-user program managers who require an intuitive and user-friendly interface. Allocating resources, expertise, and time to each team will allow us to immerse ourselves in the intricacies of each product, resulting in improved quality and better alignment with user requirements.
1. **Specialized Skill Sets:** Splitting the teams will allow team members to develop and specialize in skills relevant to each product's target user base. Allo Protocol will require expertise in blockchain-based protocol infrastructure, integration capabilities, and developer toolkits, while Grants Stack may necessitate skills in UX design, data analytics, and program management. By leveraging specialized skill sets, we can improve efficiency, productivity, and innovation within each team, resulting in higher quality deliverables.
1. **Enabling Different Work Styles:** We have a hypothesis that building protocols will require a different work style than developing end-user-facing interfaces, as there will be heightened risks of deploying new always-on smart contracts. Splitting teams will enable each team to build development processes more tailored to the type of product they’re building.

We’re excited about the benefits of this split and grateful for the flexibility and enthusiasm that the whole workstream + Gitcoin DAO has brought to our new teams!

## Grants Stack Strategy
During the pre-beta round period, including our S18-19 budget cycle, the team was primarily focused on shipping a product that would be functional for the May beta program. Running 15 rounds in May was an awesome milestone – it demonstrated that we had successfully built a decentralized grants application that was capable of running high-volume Quadratic Funding programs.

The beta program also afforded us the opportunity to hear feedback from a wide range of participants and use that data to reassess our S18 strategy and roadmap. Though the beta program was the most successful use of Grants Stack to date, we did note a lot of user pain and friction that prevents wider adoption and promotion. We’ve noted a need to address that for future serviced rounds, as well as to make the product easier to use and understand for self-serve grants managers. 

We’ve also been executing on our commitment to explore funding mechanisms outside of Quadratic Funding. We kicked off a partnership with Bootnode to build a Direct Grants MVP and are actively looking for grants managers interested in participating in a direct grants beta round. We had previously lined up a large Quadratic Voting partnership, which influenced our commitment to QV this season but fell through. Though we found other potential partners, the demand for QV is less immediate than QF (self-serve and serviced) and direct grants. It feels more impactful to focus on those two new efforts in order to increase adoption before tackling another new mechanism.

With that in mind, we’ve modified our original seasonal goals.

Original:
* 13 - Quadratic Funding rounds
* 5 - Direct Grants programs
* 5 - Quadratic Voting events

New:
* 13 - Quadratic Funding rounds (run through PGF)
* 5 - Direct grants programs
* 8 - Self serve Quadratic Funding rounds

This new framing allows us to invest in adoption of the self-serve experience, which we’re confident in as a cornerstone of grants and our forward strategy. We will also continue to experiment with new mechanisms in the form of direct grants and applied or observational research into other mechanisms (eg - QV or conviction voting).

You can view the full Grants Stack S18 Strategy and Roadmap at the links below:
* Strategy: [Grants Stack S18 Strategy](https://docs.google.com/document/d/1nEuAOYdUy9nMMiDvHvMa1vi4gDeTOeEW_G7yTACmnSU/edit#heading=h.fdurw9uhm5r)
* Roadmap: [Grants Stack Roadmap](https://docs.google.com/spreadsheets/d/1ckMnZWXeJzMfrg8C1g305OE1cRFWaULnu2rpKhnbTdE/edit#gid=0)

## Allo Strategy
Over the last few months, Allo Protocol v1 has been pressure-tested on three fronts:


* **Gitcoin Beta Rounds:** We successfully ran the Gitcoin Beta Rounds on Grants Stack, marking a significant step forward for our Quadratic Funding mechanism. 
* **Third-Party Audit:** Sherlock, a third-party auditor, thoroughly reviewed the protocol and provided comprehensive feedback.
* **Protocol Integrations:** The DevRel team has initiated a cohort of protocol integrations, including a subset of teams building new allocation mechanisms. 

While we’re excited that Allo is in a position to even be tested in these ways, we're mindful of the feedback received, which highlighted unintended barriers to developing new mechanisms within our existing architecture. Specifically, we heard that:
* Our combination of on-chain data with off-chain QF calculations made the mechanism feel black-box
* Our current core contract design enforces some quadratic-specific parameters that don’t make sense for the broader world of allocation mechanisms we want to enable
* There are extraneous elements in the protocol (e.g. programs) that can be pruned to simplify Allo and make it easier to build upon

To meet this challenge, the team has decided to kick off work on Allo v2 this season. We’ve decided to begin work on a new version instead of pursuing iterative v1 improvement as we think there is a greater long-term benefit to rethinking our architecture from first principles. This will enable us to take into account everything we’ve learned and the new use cases we’ve heard about since our design sessions for v1. Our hunch is that much of our current code will be reusable, but that there is an alternative configuration that will unlock the power of our protocol. We are expecting to wrap up the first of three phases of the v2 project (architecture) by early July, at which point we will also be able to share more clarity on timing for the following two phases.

You can view the full Allo S18 strategy and more detail on Allo v2 at the links below:
* Strategy: [Allo Protocol S18 Strategy](https://docs.google.com/document/d/1gL8Y3klppln37ihOksd1RJQUYzfqwtTlSQNx9GOlt5o/edit#heading=h.fdurw9uhm5r)
* Allo v2: [Brief: Allo Protocol V2](https://docs.google.com/document/d/1Me5jdrkQy7dQkBYys4LZ7cTLIJCdjSHOlughBhTiLIU/edit#heading=h.tvxzmiinefwo)

## Final thoughts
We’ve hit some exciting milestones for both products – and we know we still have a ton of work ahead. We’re focused on achieving product-market fit and growing adoption to make democratic allocation of capital an accessible and widespread reality. We’re grateful for the support of the Gitcoin community and DAO and welcome feedback on our learnings + goals!

-------------------------
