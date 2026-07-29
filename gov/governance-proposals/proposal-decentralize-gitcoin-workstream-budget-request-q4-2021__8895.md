---
id: 8895
title: "[Proposal] Decentralize Gitcoin Workstream Budget Request - Q4 2021"
slug: proposal-decentralize-gitcoin-workstream-budget-request-q4-2021
category: governance-proposals
url: https://gov.gitcoin.co/t/proposal-decentralize-gitcoin-workstream-budget-request-q4-2021/8895
created_at: 2021-10-27T19:10:19.399Z
last_posted_at: 2021-11-08T16:19:33.608Z
posts_count: 7
views: 3257
like_count: 19
---

# [Proposal] Decentralize Gitcoin Workstream Budget Request - Q4 2021

<https://gov.gitcoin.co/t/proposal-decentralize-gitcoin-workstream-budget-request-q4-2021/8895>
phutchins | 2021-10-27 19:10:19 UTC | #1

# dGTC Workstream Q4 Budget Proposal

Workstream Mandate: Progressively Decentralize Gitcoins core services and products.

## Budget Request

Request to send 127k GTC (138k mins remaining 10k GTC & 40k DAI from Q3) to the dGTC multisig to fund their Q4 2021 budget.

Gnosis Safe address: 0x931896A8A9313F622a2AFCA76d1471B97955e551

## Q3 Achievements & Budget Deployment

In Q3 of 2021 the dGTC workstream utilized the budget granted to take the Decentralized Grants platform from a rough draft concept to working POC. We have kicked off a Grant Round for the Moonshot Collective team which contained 11 grants. Since the start of the round we have had 3 new grant submissions which have gone through the approval process and you can see on the platform at https://grants.gtcdao.net/

Out of the 41,300 GTC received for Q3, we have 10k GTC and 40k DAI remaining which we are moving forward to our Q4 budget.

Reference previous budget here: https://gov.gitcoin.co/t/decentralize-gitcoin-workstream-budget-request/8121

## Q4 Goals High Level

During Q4 the Decentralize Gitcoin workstream will (and has already started to) continue to collect feedback and improve the user interface and user experience, build additional features based on what is most important to run the round in GR12 and for claiming payouts, start working on implementing active sybil resistance and basic curation, and kick off the DID/Sybil Score Aggregation project and DevOps/Data initiative.

## Q4 Team Growth High Level

In Q4 we will scale the team in order to meet the goals that we have outlined above (and in more detail in the detail breakdown).

For the dGrants project team, we are adding two more full time developers focused on backend and blockchain to lessen our reliance upon outsourced development, a temporary marketing resource to assist with promoting the dGrants side round in GR12, and a temporary designer to level up the dGrants experience.

We will bring on a Project Manager as a shared resource across all dGTC projects who will also be responsible for community relations.

For the DID and DevOps/Data projects, we will bring on 2 new team members each to kick off those teams and work with our lead team to draft a plan and roadmap.

## New Projects

We are adding two new projects to the dGTC workstream.

The **Sybil Score Aggregation project** aims to solve the problem of making it easy to consume and make decisions based on sybil score data from multiple sources. It is fairly clear that no single provider is reliable enough on its own and aggregating the outputs from these providers in a way that makes the score reliable, portable, and easily consumable. This will meet the needs of dGrants by ensuring that legitimate contributions are given appropriate weight at the end of the grant round, thus ensuring fair distribution of the funds. To simplify the end goal here would be to have a robust identity aggregator which would be able to connect to different identity providers (entirely configurable) allowing users to link their identity and share it with dApps. This platform/protocol should be decentralized/distributed and open however never expose a users private data.

The **DevOps / Data projects** started within the FDD workstream lead by Philip Hutchins (the lead of this workstream) and is now moving under the dGTC workstream. The DevOps project aims to standardize CI/CD and security practice throughout the DAO and act as a service provider to the Gitcoin DAO workstreams. The Data project aims to coordinate the standardization of data needs across the DAO and to build a data lake enabling reporting, analytics, and feed our machine learning platform. Once the DevOps and Data teams have some momentum, we plan on building out the machine learning portion of the data team to move the sybil resistance effort to within the DAO.

# Detail Breakdown

## Q4 Goals & Budget Deployment Detail

Improve the dGrants UX

* Loading speed
* Error handling
* Consistent results
* Tech Debt payoff
* Improve image upload
* Improve documentation

Continue to build out dGrants features

* My grants (unapproved/approved)
* My donations
* Grant Matching Funds Claiming experience
* Grant categorization

Run side round in GR12

* Finalize Grant Registry Contract changes
* Finalize L1/L2 support and approach

Convenience Layer - Design framework / foundation for plugins

* Active sybil resistance
* Curation (filtering good grants) - Adding simple UI/UX

Kick off DID/Sybil Score Aggregation Project

* Hire engineers to begin working on an architecture proposal

DevOps & Data

* Hire engineer to build CI/CD & Security proposal
* Hire engineer to collect all workstreams data beads and build data dictionary

### Stretch Goals

Enable another entity to run a grant round using own instance dGrants

Work toward another entity utilizing canonical grant registry

# Budget Breakdown

## Team - 136k GTC

Current positions - 72k GTC

* Workstream Lead
* Lead Dev Full Stack (20h)
* Senior Dev Full Stack (20h)
* Senior Dev Full Stack (40h)
* Lead Dev Full Stack (40h)
* Dev Full Stack (40h)
* Design (20h)
* Scopelift (100-200h)

New Positions (dGrants) - 22k GTC (19k GTC Recurring / 5k GTC One Time)

* Senior Developer - Solidity Expert (full time)
* Senior Developer - Backend (full time)
* Marketing
* Designer

New Shared Team Positions - 6k GTC

* Project Manager - Projects & Community

New Full Time Positions (DID) - 18k GTC

* Senior Developer Backend - Web3 / Identity / Crypto
* Senior Developer Full Stack - Web3 Design

Incubator DevOps & Data - 17k GTC

* Senior DevOps / Security Engineer (40h) (Contributor in Trial)
* Senior Data Engineer (40h) (Contributor Pending)

Incubator Discovery (Discovery budget not included in this request)

* Covered in [Gitcoin Discovery Proposal](https://gov.gitcoin.co/t/proposal-integrate-dcompass-within-dgitcoin-to-build-dquests-dknowledge/8836)

### Operational - 2k GTC

Infrastructure - 1387 GTC

Tools - 217 GTC

Security - 737 GTC

-------------------------

DisruptionJoe | 2021-10-29 00:54:26 UTC | #2

I'd like to see the dGitcoin stream expand to integrate curation tools, build better identity integration for our sybil defense, and operationally maintain a community data lake.

There is a lot to be done here, but getting dGrants deployed on Mainnet & Polygon was a great season one start for this workstream. 

Voting yes to this proposal.

-------------------------

Huxwell | 2021-10-29 14:48:48 UTC | #3

I'm super excited to the idea of joining the Decentralize Gitcoin workstream! We have a lot to learn from your experience building dGrants. And also a lot of knowledge & resources to share.

I'm biaised, but I will vote yes for this proposal!

***DECENTRALIZATION FTW*** :rocket:

-------------------------

seedphrase | 2021-11-01 12:55:45 UTC | #4

I think yall have done great work so far
I support the expansion of your team


Curious about how MMM workstream could contribute as far as marketing/design goes

-------------------------

phutchins | 2021-11-01 19:12:43 UTC | #5

Thanks a bunch! I'd love to jam on how this could work as well. It would be great to have the MMM team take on some or all of our marketing needs allowing us to stay focused on decentralization and the technology!

-------------------------

lefterisjp | 2021-11-03 12:00:07 UTC | #6

I am inclined to vote yes as decentralizing gitcoin grants is one of the long-term goals we should be having.

As mentioned in other budget proposals it would be cool to see dollar amounts as this is money to be spent while developing in the next 3 months and it's kind of hard to judge with GTC amounts, an asset with inherently volatile value.

-------------------------

David_Dyor | 2021-11-08 16:19:33 UTC | #7

Voting yes to this proposal.  I hope dGitcoin will support the cross-Dao-ops initiative to ensure our Dao is working together towards common goals.

-------------------------
