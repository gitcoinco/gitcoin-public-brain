---
id: 15516
title: "Gitcoin Digest #11 2023"
slug: gitcoin-digest-11-2023
category: newscommunity
url: https://gov.gitcoin.co/t/gitcoin-digest-11-2023/15516
created_at: 2023-06-22T18:35:05.682Z
last_posted_at: 2023-06-22T18:35:05.808Z
posts_count: 1
views: 1910
like_count: 3
---

# Gitcoin Digest #11 2023

<https://gov.gitcoin.co/t/gitcoin-digest-11-2023/15516>
rohit | 2023-06-22 19:03:07 UTC | #1

Thanks @gaoa97 for another detailed overview!

# 🔥 Hot Topics:

* @Zack shares a proposal seeking approval of $60,000 in Eth from Gitcoin’s matching pool for [a grant to fund Endaoment’s Universal Impact Pools](https://gov.gitcoin.co/t/proposal-seed-universal-impact-pools/15398): a novel mechanism for matching donations to nonprofit organizations and a collaboration between Endaoment.org and Gitcoin’s Allo Protocol.

* Gitcoin has been invited by the Lit Protocol team to participate in the launch of their testnet and mainnet by operating a Lit Node. Read [@Kevin’s post](https://gov.gitcoin.co/t/lit-protocol-network-participation/15416) to learn more about the motivation and considerations for integrating with Lit Protocol, which is an important key management protocol integral to the privacy features of the Gitcoin Grants Stack.

* Building upon the work done in S17, where DeSci was established as the first community-operated featured round within the new Gitcoin Grants Program. @Boris shares a proposal explaining the work required [to enable ongoing support for DeSci within the Gitcoin grants program](https://gov.gitcoin.co/t/proposal-desci-recognized-subdao-framework-development-and-implementation/15460), and to establish DeSci as the first of several potential subDAOs within Gitcoin.

* Kyle proposes[ to move 3M USDC from the treasury, into the CSDO multisig](https://gov.gitcoin.co/t/proposal-withdraw-and-leverage-partial-usdc-balance-in-treasury/15484) for the purpose of supporting workstream’s budgets to enable the exchange of GTC with USDC from the multisig instead of open markets, with the goal of reducing the amount of GTC leaving the DAO.

# 🧭 Weekly Workstream Update

Here are key highlights from the [weekly workstream update](https://docs.google.com/presentation/d/1WJseBI_raaBPhZFxTD-ProPvb9e9Ay-6vzWSERKmgmY/edit#slide=id.g24f27bb2388_1_10) - (video [here](https://www.youtube.com/watch?v=MJ6Wc5aFWTo))

## Allo + Grants Stack:

* Allo v2 GTM is now in effect, shifting the narrative from QF to position Allo as a platform for unlocking the mechanism creation flywheel.

* Gitcoin is excited to finally share more details about Allo, a protocol for onchain capital allocation. [Read the announcement post](https://www.gitcoin.co/blog/allo-gitcoins-newest-protocol) to learn more about what this means for you and your community

* New [Allo website](https://allo.gitcoin.co/) and [Hype Drips are LIVE](https://twitter.com/alloprotocol). Focus on generating 10+ integrations.

* Check out the [Allo Brand Design Elements](https://gitcoin.notion.site/Allo-Brand-Design-Assets-1b6372032fcf434da3961bc3591261e6) with updated slides, animations, illustrations, and banners. Refined graphics, stickers for FTC Paris, and the brand book and forum post are in progress. [V1 of Brand Book](https://www.figma.com/file/IYFgcVtZPebMxTuUWea4W7/Gitcoin-Grants-Stack?type=design&node-id=339-551&mode=design) is complete!

* The overall architecture of Allo V2 is about 85% complete, considering the progress made in core interfaces and contracts. Ongoing development includes specifications for an initial list of strategies and outlining architecture options for the project registry, protocol fees, and the multi-chain approach.

* Endaoment Integration for QF is live, enabling donor-advised funds to hold GTC to receive and make donations. Check out the portfolios displayed [on their app website](https://app.endaoment.org/portfolios).

* Impact Stream planning and “Call to Build” article writing are in progress, aiming to provide an overview of the architecture and how the core components of the protocol work.

* The focus remains on supporting the development of Allo v2, while the documentation work is paused until further progress.

* Grants Stack updated goals include: supporting 5 direct Grants, 8 easy self-serve (no QV), improving tech debt/internal scalability and running 13 QF rounds.

* Donation History page MVP has been shipped, along with multiple features including: enabling rolling applications, aggregating donations by address in the Indexer, new staging environment, and other updates to support Bedrock.

* Ongoing development on Indexer improvements (deploy/scalability), scoping out multi-round checkout contracts, and adding PGN support in Grants Stack.

* Upcoming focus on improving the Round Application UX, and checkout enhancements (Passport integration with matching estimates, on-page checkout).

* Check out the new [Manager Toolkit](https://manager-toolkit.super.site/): your guide and inspiration for running a Quadratic Funding grants program.

* Support Ticket Stats (June 12-18) increased: 1510 new tickets via live chat and 67 new tickets via email, revolving around Passport stamp, scores, Twitter GTC stamps. Current escalated issue: Typo in explorer page (in progress). Share on Twitter button did not include the link (Resolved). Use support@gitcoin.co or [intercom](https://intercom.help/gitcoin/en/) for filing issues.

## Public Goods Funding

* Beta round finalization with revised matching results [posted](https://docs.google.com/spreadsheets/d/1-WDK9R4h0vBGhnJtFgd1z1ISISeuIfSP26MKaDeSY5c/edit#gid=1842751536) last week, however, follow-up questions led to more discoveries of Sybil attacks and self-donors, which will be updated. Doing one more round of manual review while exploring what automation could catch these cases.

* Next Gitcoin Grants Program Round (Season 18) pushed from July to August.. More to come on the process and structure of Core/Featured rounds. Process for selecting the core rounds, and adding featured rounds in progress.

* Due to market conditions, Schelling Point EthCC - Paris has been reduced to a 3-day long event with 5 new partnerships confirmed: Salus Security, GoPlus, Celo, Golem Foundation, and Drips/Radicle.

* Regional Inclusivity Panel under planning to take place as an afternoon session for Gitcoiners, featuring knowledgeable and experienced people from South Korea and Taiwan. New nominations are still open and welcomed in the panel.

* A [simplified CRM](https://www.notion.so/gitcoin/Simple-CRM-2e86cf87f0724077aa6f4deec843722e?pvs=4) entirely built in Notion to bring spatial awareness, track partnerships, business development efforts and integrate institutional knowledge

## Passport

* Holonym stamp is ready to be turned on and get a score. Upcoming updates for introducing new stamps (e.g. Idena, Civic, Humanode) in progress.

* Maintenance pages and database upgrades have been completed to help with scaling. Planning in progress for Unique Humanity Score improvements, UX improvements, Ceramic ComposeDB Upgrade.

* The focus remains on improving UX scalability for users and integrators based on load testing and rearranging documentation content. New partnerships are interested in pushing the passport creation for load testing (1m-5m passports/ day).

* In pursuit of evolving current marketing strategies, a [win-win co-marketing approach](https://gitcoin.notion.site/Gitcoin-Passport-Integrator-Co-Marketing-Approach-June-2023-Briefing-76234d5e76514000bcf4773b1e10cdc9) has emerged as an effective method to foster ongoing collaborations with multiple orgs, including Linea/Galxe, {r}elinked, OKX. 2k new followers and 100s of thousands of impressions in the last week.

* Linea campaign in progress, featuring the new zkEVM L2 created by Consensus. Running weekly Voyage Quests (7 so far). New quest to remove bots & Sybils, Passport is one of 3 options including: Guild Pin, Galxe Passport (KYC + SBT mint). 480k total net new Passports created since the campaign started.

* Other Protocol updates include:Large influx of new Passports have resulted in additional GTC staking with 104k GTC staked in the last week, we are also seeing the number of integrations increase from 7 at the start of the season to a total of 14 integrations, a total of 820k all time unique Passports have now been created.

* Open bounty for [building an open-source Discourse forum plugin](https://docs.google.com/document/d/10q5VGCMW76cDBui1e6ZGLwG4BWi8yItMmAE7hjCJeec/edit) that will require a user to have and verify their unique humanity with a Gitcoin Passport to gain access to the forum as well as to do different things such as post or create new topics.

* Snapshot integration is still being migrated from SDK to API. Upcoming integrations include: {r}elinked, Thrivecoin, Linea, Collab.land, newcoin/newlife, and Metaforo.

* Passport Brand revisit in progress (the cross-functional working group has been activated to ensure alignment between mission, vision, and marketing assets. Leading up to the ‘Protect What Matters’ campaign and other initiatives to be launched).

* Multiple case studies are in progress and already receiving positive feedback on a recent one using the test faucet. Discourse plugin development is in progress.

* [Release Notes #9](https://gitcoin.notion.site/What-s-New-Gitcoin-Passport-4764ed4f8a3f42fdbd2d5d7dd8637872) is now available.

* Tutorials created for stamp creation process and metadata, as well as onchain stamps content (users). Work in progress for Information Architecture Review, major improvements will be reflected in new documentation structures and upcoming tutorials including: IA content overhaul, Merge user content into Support knowledgebase, and airdrop example app.

* Supermodular team has built a [Passport-gated faucet starter](https://gc-passport-faucet.vercel.app/) that can be forked and run on any network. Prebuilt Passport components are under planning.

## MMM

* [Grant Stacks](https://www.gitcoin.co/grants-stack) and [Allo](https://allo.gitcoin.co/) websites launched. Community Initiatives page and PGN sprint for next week. Side quest: [WTFisQF landing page refresh](https://wtf-is-qf.webflow.io/).

* Since #GitcoinBeta ended in May, we have embarked on an exciting journey that enhances our existing offerings and accelerates innovation. Get up to speed and share the new thread on [WHAT WE’VE BEEN UP TO AT GITCOIN](https://twitter.com/gitcoin/status/1670892624008364032).

* Research & Impact Hub has been updated with project tracking, proposal ideas, and GCP & RFPs process. Current research underway: State of Web3 Grants, State of QF, exploring new research opportunities such as reputation systems and coordination mechanisms

* EthCC planning (SP House, FTC & Gitcoiners coming together), [Passport visual touch-ups](https://docs.google.com/document/d/1rfPmfVDceQze8DNAUmCEsbk3YXoUjP8IgEZ5oU6biaU/edit#), Gitcoin Grants and PGN brand work are underway.
* Gitcoin Steward is the word of the week, defined as an individual that is involved with driving the Gitcoin ecosystem forward through their work in DAO governance. Often, but not always, stewards are delegated governance tokens on behalf of GTC token holders and use them to participate in governance. Check out the [shared glossary](https://gitcoin.notion.site/Gitcoin-Glossary-287c54d3538941349b397cdf8ced4ca1) of terminology where the DAO documents common language and reinforces our shared vernacular.

# 🗳️ GitcoinDAO Governance Overview:

Snapshot polls GTC Stewards. Tally performs on-chain actions. Proposals that have on-chain steps, such as budget requests, are approved on Snapshot before moving on to Tally.

## 📊 Active Proposals:

* Gating Snapshot proposals - [Go vote on Snapshot](https://snapshot.org/#/gitcoindao.eth/proposal/0xa18926b9dc9592bdf02acc3cef5a41021cebe51f73a2a3d6b007d7c38685b296) (closes Monday)
* [[Discussion] Ratify the Results of Gitcoin’s Beta Round](https://gov.gitcoin.co/t/discussion-proposal-ratify-the-results-of-gitcoin-s-beta-round-and-formally-request-the-community-multisig-holders-to-payout-matching-allocations/15166)
* [[Proposal] Seed Universal Impact Pools 1](https://gov.gitcoin.co/t/proposal-seed-universal-impact-pools/15398)
* [[GCP-009] - Upgrading Gitcoin’s Governance Contracts](https://gov.gitcoin.co/t/gcp-009-upgrading-gitcoin-s-governance-contracts/14010)
* [[Proposal] DeSci “recognized subDAO” framework](https://gov.gitcoin.co/t/proposal-desci-recognized-subdao-framework-development-and-implementation/15460)
* [[Proposal] -Schelling Point Istanbul](https://gov.gitcoin.co/t/proposal-schelling-point-istanbul/15260)

## 📅 [Upcoming events](https://gitcoin.notion.site/Upcoming-Events-d749e53de96147a88a2f4864ea381afc)

Gitcoin Community Call: Weekly discussions to seek community opinions on the latest DAO decisions happen every Wednesday @ 12 pm ET. Catch up on recordings of recent conversations here:

* June 22: [Decentralized Design](https://twitter.com/i/spaces/1BRKjZYynAWKw)
* June 14: [Citizens Round Kickoff ](https://twitter.com/i/spaces/1YpKkgQwloYKj)
* June 7: [Beta Round Retro](https://twitter.com/gitcoin/status/1666475003150311424?t=L6EJzbw9qAVVKUyQJuUAFA&s=19)

# 👋 New to Gitcoin?

* Explore the future of Gitcoin at [our new website](https://www.gitcoin.co/), and check out [Gitcoin Community Hub](https://community.gitcoin.co/) for key resources and events.

One more thing! ​The 6th edition of [Funding the Commons](https://fundingthecommons.io/) will take place on 15-16 July in Paris, France. Use the coupon code GITCOINER to get 35% off the tickets - limited spots remaining!

Thanks for reading!

PS: Click [here](https://share.hsforms.com/1qr4-szfGQAmHKqItMstzoAd0r2h) to subscribe to the DAO Digest

-------------------------
