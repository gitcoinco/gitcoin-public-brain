---
id: 25227
title: "Tally Is Shutting Down — Option to Maintain the Existing Interface (No Contract Changes)"
slug: tally-is-shutting-down-option-to-maintain-the-existing-interface-no-contract-changes
category: governancevision
url: https://gov.gitcoin.co/t/tally-is-shutting-down-option-to-maintain-the-existing-interface-no-contract-changes/25227
created_at: 2026-04-13T18:04:45.139Z
last_posted_at: 2026-04-16T08:23:23.141Z
posts_count: 2
views: 43
like_count: 2
---

# Tally Is Shutting Down — Option to Maintain the Existing Interface (No Contract Changes)

<https://gov.gitcoin.co/t/tally-is-shutting-down-option-to-maintain-the-existing-interface-no-contract-changes/25227>
DavidLen | 2026-04-13 18:04:45 UTC | #1

Hi delegates and community members,

I'm David Len. My team and I built and maintained the governance Discourse layer used by Aave and 10+ DAOs. Given Tally’s shutdown, we’re exploring a path to keep a familiar governance interface available for DAOs that rely on it.

**Proposal** We are prepared to host and maintain Tally Zero — Tally’s open-source governance client — preserving the existing frontend experience without requiring contract changes or migrations. No relearning of the platform.

**What this means**

* Continued access to a familiar governance UI

* No changes to existing governance contracts

* Minimal disruption to current delegate workflows

**Sustainability & security**

* We have operated governance infrastructure across 10+ DAOs on a lean model

* We are pursuing grant funding to cover audit costs and will publish a transparent cost structure before any DAO commits to anything

**Why we’re working on this**

Existing DAO governance flows depend on accessible interfaces

**Signal request (non-binding)** If your DAO would consider using a maintained version of Tally Zero, a simple reply or indication of interest helps us quantify demand. This costs you nothing and keeps the governance running without disruption.

Happy to share more details or walk through the architecture.

— David Len

-------------------------

bear-wang | 2026-04-16 08:23:23 UTC | #2

To be honest, I think that the previous way that Tally ran was not very good. 

As a fundamental component of the Web3 governance system, its underlying architecture is OpenZeppelin's open-source Governor contract, so there should be a totally open-source solution for the community to use and maintain the UI/UX interface of the governance process. We (Degov) were once Tally's users, and we have many new ideas and want to contribute to their platform, but we have no way to do that because of the closed-source nature of their UI/UX. So, we made the decision to build our own governance platform, called Degov, which now supports more than 30 DAOs and is still growing and open-source since day one. It is also designed to be hosted by anyone, so that the community can easily deploy and maintain their own governance platform without relying on a third-party service. 

I think that's the final picture of a healthy Web3 governance ecosystem: whether you are a big or small project, you can easily deploy and maintain a reliable and user-friendly governance platform for your community instead of paying for a third-party service or relying on a closed-source solution.  As for Gitcoin governance, we already support it; you can check it out here: [https://gitcoin.degov.ai/](https://gitcoin.degov.ai). I wrote another post in this forum [https://gov.gitcoin.co/t/consider-migrating-gitcoin-dao-governance-to-degov/25202](https://gov.gitcoin.co/t/consider-migrating-gitcoin-dao-governance-to-degov/25202), but have received no feedback yet.

-------------------------
