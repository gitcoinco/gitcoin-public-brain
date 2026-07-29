---
id: 17145
title: "Opening up Grants Stack/Allo to more community contributions"
slug: opening-up-grants-stack-allo-to-more-community-contributions
category: open-discussion
url: https://gov.gitcoin.co/t/opening-up-grants-stack-allo-to-more-community-contributions/17145
created_at: 2023-11-20T19:23:04.532Z
last_posted_at: 2023-11-20T19:23:04.619Z
posts_count: 1
views: 3496
like_count: 7
---

# Opening up Grants Stack/Allo to more community contributions

<https://gov.gitcoin.co/t/opening-up-grants-stack-allo-to-more-community-contributions/17145>
owocki | 2023-11-20 19:28:11 UTC | #1


Thank you to: Andrea Franz, Kevin Owocki, Meg Lister, Carl Barrdahl, Zakk Fleischmann

# TLDR

1. We convened to discuss how to do software development in a post-Allo v2/Grants Stack integration world. Should we enable anyone to contribute to the Allo/Grants Stack roadmap?
2. We decided that the Grants Stack Team will continue their current development style for the next 12 months.
3. In parallel, Owocki/Raid Guild and Allo Workstream will build on top of Option E - Allo webapps.

# What we did

The Grants Stack (GS) product has come a long way over the last year – but it is still early in its journey. There are tons of features we want to build and new opportunities in the grants space to explore.

We’re really interested in leveraging the unique power of the Web3 ecosystem and open-source development in order to accelerate our product capabilities exponentially and flexibly, rather than the traditional linear growth model of new, full-time dev/product/design headcount.

With the integration of Allo v2 features into Grants Stack, we have an opportunity to build new funding mechanisms and tooling more quickly and flexibly at the protocol layer. We’re also interested in exploring ways to make our front-end architecture more flexible and modular for external developers to contribute without substantial onboarding and deployment time and costs.

Allo and Grants Stack are complementary in that both create capital allocation tools for communities to Fund What Matters (™) in their own communities. While GS is focused on going deep on enterprise grade no-code tools, Allo creates the opportunity space to explore broader possibilities of experimental/developer focused opportunities.

![|625x496](upload://ubmbxcvYeBqNVV2B9vW6fp6D2XH.png)

With this in mind, we came together to explore the different ways we might work together and align how we do development.

In doing this evaluation, we used the following criteria:

1. Ease of onboarding external devs
2. Accelerates GS growth, including revenue growth
3. Ability for Grants Stack team to “feature flag” or control visibility of externally contributed features
4. Level of effort (able to integrate Allo v2 + MVP this in a reasonable time frame, eg not more than 4-6 weeks)

We also evaluated the risks. Introducing an architecture for community involvement could create new pressures on the GS core team (like code review, merge conflicts, architecture, community engagement/devrel). Grants Stacks customers typically desire enterprise grade product quality, and we would need a way to ensure quality through the process.

#
The options we evaluated

|Option|What|
| --- | --- |
|A - Do Nothing|Status Quo, do nothing.|
|B - Plugin Architecture|Undertake a re-architecture towards a plugin architecture that allows anyone to augment grants stack code. Plugins could be loaded dynamically in rounds. We would then build a plugin marketplace where people could discover/rate/download plugins.|
|C - Fork Architecture|We would allow developers to simply fork the grants stack codebase and build/design on their own fork. TBD if/how these would be merged back into grants stack upstream.|
|D - Modular Webapps|We focus on having developers build modules around Grants Stack that are compatible with Grants Stack, and build around (as opposed to replace) core functionality.|
|E - Allo Webapps|Similar to option D, but we heavily focus on pushing developers to build webapps on top of Allo v2.|

# Decision

We see a strategic opportunity to enable an ecosystem of developers to build new functionality around Grants Stack & Allo. This would enable not only faster development but a more diverse set of developments.

But the Grants Stack team is highly focused on customer adoption right now, and a giant re-architecture or change in working norms is not in the cards right now - therefore Option B and C are not viable.

The group has decided that Option E is the best path forward for the next 12 months.

# Appendix A - Full Evaluation of different options.

## Option A - Do Nothing

Status Quo, do nothing.

Pros: Nothing changes

Cons: Nothing changes

## Option B - Plugin Architecture

To allow developers to easily contribute to Grants Stack, we would extract all the QF (and Direct Grants) functionalities to a self contained module to prepare the core part to load any kind of voting and distribution strategy.

We could encourage plugins that mostly just write new strategies.. but we may also make available the ability to override any function/object/template (subject to some security considerations)

A new extension will be published on IPFS and registered in an Extensions Registry contract, saving the hash of the package signed by the owner, to be able to verify it in the front-end.

Eventually, Community members will be able to sign messages to curate the registry, something similar to the Web of Trust or on-chain attestations to establish the authenticity of the extensions. we could build a UI that allows people to browse/install packages into their grants stack instance.

Doing this will simplify the way people can contribute to Grants Stack, with simple PRs with self contained extensions, without the need to touch all the codebase, preparing Grants Stack in the future to load any extensions from a decentralized Extensions Registry curated by the community.

[More details in this document.](https://docs.google.com/document/d/1obbH5WgBbeW4X1Gkel1CnORplEmfUsYqp1duYsNDwiA/edit)

Pros: Enables an ecosystem to build on top of GG.

Cons: Refactor would take some time. Complexity comes from managing security concerns, curation of registry, plugin overlap/conflicts.

## Option C - Fork Architecture

To allow developers to easily contribute to Grants Stack, we would allow them to simply fork the grants stack codebase and build/design on their own fork.

We would call these branches “Grants Stack Frontier”. For example, the branch that Supermodular built for [Collections](https://github.com/gitcoinco/grants-stack/pull/1786) could be called “Grants Stack Frontier - Collections/Supermodular” and the [Hypercerts/GS integration](https://gov.gitcoin.co/t/better-impact-funding-the-greenpill-hypercerts-gitcoin-combo-move/16477) could be called “Grants Stack Frontier - Hypercerts/Raid Guild”..

We could spin up infrastructure for them to run pilot rounds on top of their new codebases.

Only the best PRs would get merged back into Grants Stack main branch. We would provide strict guidelines around feature flagging, ux, documentation, variable scoping, code standards, and merge conflict reduction of what we’d accept upstream.

There would likely be a bunch of dangling forks that are never merged back in.

Pros: Enables an ecosystem to build on top of GG.

Cons: Messy merge conflicts + eventual codebase bloat.

## Option D - Modular Ecosystem Built Around Grants Stack

In this option, we abandon our goal of allowing developers to easily contribute to Grants Stack. Instead, we ask that they build modules around it that are compatible with Grants Stack, and build upon (as opposed to replace) core functionality.

This option is arguably already in place. Just look at all of the fun stuff that Supermodular built that fits within this category!

|Built on|When|Name|Desc|Link|
| --- | --- | --- | --- | --- |
|Allo v1|Q2 2023|Funding.Social|See who you're following on lens + who they contribute to on Gitcoin|[Go](https://funding.social/)[(opens in a new tab)](https://funding.social/)|
|Passport|Q2 2023|Passport Gated Airdrop Tool|A forkable tool to allow anyone to airdrop a token gated by Gitcoin Passport|[Go](https://twitter.com/owocki/status/1671581682925965312)[(opens in a new tab)](https://twitter.com/owocki/status/1671581682925965312)|
|Allo v1/Passport|Q2 2023|Grants-ETL|a tool to make pulling data for anti sybil/collusion easier.|[Go](https://gov.gitcoin.co/t/grants-etl-a-new-tool-to-make-pulling-data-for-anti-sybil-anti-collusion-analysis-easier/16060)[(opens in a new tab)](https://gov.gitcoin.co/t/grants-etl-a-new-tool-to-make-pulling-data-for-anti-sybil-anti-collusion-analysis-easier/16060)|
|Allo v1|Q1 2023|Quadratic Yeeter|a tool to create a Grants Stack round in 1 click|[Go](https://community.supermodular.xyz/t/new-build-bulk-uploader-for-gitcoin-grants-registry/442)[(opens in a new tab)](https://community.supermodular.xyz/t/new-build-bulk-uploader-for-gitcoin-grants-registry/442)|
|Allo v1|Q1 2023|Gitcoin Grants crowdfunder|a tool to make a crowdfunding aqueduct into Gitcoin Grants|[Go](https://crowdfund-matchingpool.vercel.app/pool/0x74ad514636f1386f374e1107435f35d393d0b279)[(opens in a new tab)](https://crowdfund-matchingpool.vercel.app/pool/0x74ad514636f1386f374e1107435f35d393d0b279)|
|Allo v1|Q1 2023|Gitcoin Grants data vis|an easy way to visualize Gitcoin QF rounds crowdfund data structure.|[Go](https://twitter.com/owocki/status/1658103631500161024)[(opens in a new tab)](https://twitter.com/owocki/status/1658103631500161024)|
|Allo v1|Q1 2023|Partnership Protocol|An easy way to see the top grants round projects + get in touch with them for partnership/BD folks.|[Go](https://community.supermodular.xyz/t/partnerships-tool-on-grants-stack/261)[(opens in a new tab)](https://community.supermodular.xyz/t/partnerships-tool-on-grants-stack/261)|
|Allo v1|Q1 2023|Economic Graph Generator|A tool to visualize Economic Graphs on top of Allo Protocol|[Go](https://community.supermodular.xyz/t/help-wanted-build-economic-graph-tool-on-top-of-allo-protocol/430/5)[(opens in a new tab)](https://community.supermodular.xyz/t/help-wanted-build-economic-graph-tool-on-top-of-allo-protocol/430/5)|

Pros: No new re-architecture effort needed

Cons: People can’t replace/replicate core GS functionality, only build around it.

## Option E - Allo Webapps

In this option, we abandon our goal of allowing developers to easily contribute to Grants Stack. Instead we ask them to build webapps on top of Allo v2.

These webapps could be tightly coupled with the new Allo v2 strategies + data structures, and would be optimized for easy forking + building of new webapps. Kind of like [Scaffold ETH 2](https://github.com/scaffold-eth/scaffold-eth-2) but for Allo.

We could then maintain a registry of the best Allo v2 webapps that customers could use.

Pros: Enables an ecosystem to build on top of GG. No effort needed for Grants Stack team

Cons: Allo/Grants Stack likely to not be in sync from a code/business model/culture perspective.

-------------------------
