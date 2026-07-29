---
id: 9292
title: "[Proposal] Implementation of a Decentralized Bounty Platform - Progressive Decentralization Workstream"
slug: proposal-implementation-of-a-decentralized-bounty-platform-progressive-decentralization-workstream
category: governance-proposals
url: https://gov.gitcoin.co/t/proposal-implementation-of-a-decentralized-bounty-platform-progressive-decentralization-workstream/9292
created_at: 2021-12-02T06:30:53.227Z
last_posted_at: 2021-12-05T18:44:52.585Z
posts_count: 11
views: 6752
like_count: 34
---

# [Proposal] Implementation of a Decentralized Bounty Platform - Progressive Decentralization Workstream

<https://gov.gitcoin.co/t/proposal-implementation-of-a-decentralized-bounty-platform-progressive-decentralization-workstream/9292>
ethanl | 2021-12-02 06:32:32 UTC | #1

# Decentralized Bounty Platform Proposal to Gitcoin

Bounty boards are centralized repositories of discrete tasks with an associated price tag for each job. De-bounty Platform (DB) is an interface to monitor the off-chain development progress of freelancers, and react to pre-set milestones with on-chain logic set by bounty providers. Bounties will be automatically delivered via a smart-escrow.

## Abstract & Motivation 
Bounty boards have the potential to become the de facto form of labor organization in the cryptosphere by creating open labor markets. This is as DAOs are proliferating at an unprecedented rate and are able to derive high value from bounty boards: Opposed to hiring, DAOs typically utilize bounties to incentivize the community to complete various tasks in the form of tech development, design, PR content, metaverse building, etc. DAOs require platforms to manage these bounty interactions to help build trust between two, previously unfamiliar, people/entities.

This proposal outlines a plan for Gitcoin to implement a decentralized bounty platform parallel to their existing bounty platform. This "de-bounty" platform (DB) will utilize Gitcoin bounty platform's frontend and EthSign Smart Agreement's backend to automatically fulfill the agreement outlined in bounties in a trustless manner. 

The intention of this proposal is to provide freelancers and bounty issuers with a decentralized means of issuing job bounties and automating compensation once the job is complete —opposed to Gitcoin's existing centralized workflow. The reduction of potential bias from centralized entities —repo owners & maintainers— via pre-set job terms and smart escrow enables freelancers and bounty issuers to enjoy more frictionless, trustless interactions. 

This proposal is in-line with the directives outlined in the following [Progressive Decentralization](https://gov.gitcoin.co/t/workstream-suggestion-decentralize-gitcoin/180/2) governance workstream.

DB Features Include:
- Decentralized escrow service of bounty rewards
- Automated payment execution triggered by API
- Project milestones management dashboard
- On-chain records that provide a solid foundation for an identity verification & credit system
- Diverse bounty categories (technical development, operational tasks, DAO-related etc.)

## De-Bounty Platform (DB) Specifications
See [Gitcoin Proposal: De-Bounty Platform Specifications](https://www.notion.so/0465799913564578aa627e13e9e7221e) for details on DB's workflow and features.

## Road Map For this Development

Phase 1 - 1.5 months, 4000 GTC

Functionality 

- Front End
    - DID Integration (Torus, Metamask, etc)
    - Project Management Dashboard
    - IPFS + Arweave website
    - Adapt Gitcoin front-end and UX to accommodate interaction with smart-escrow
- Back End
    - Integrate Ethsign Smart Agreement
    - Credit score for users based on on-chain record

Phase 2 - 1.5 months, 2000 GTC

- User testing using Gitcoin DAO's and EthSign's communities
- Creation of Moderator DAO to be a jury-based dispute resolution system

Additional Features:

- Multi-user claiming from the same bounty
- Integration of **Discord Bot Plugin,** a plug-and-play bot that facilitates issuer-freelancer communication, and allows for bounty creation, editing, listing, claiming, removal within Discord communities. Users are linked to their respective bounty URL to manage the bounty.

### Drawbacks

The largest drawback of DB is the issue of resolving disputes as bounty issuers must close the job repo determining whether the pre-set job term was met; this is especially true for complicated or non-binary jobs. 

DB includes a Moderator DAO to act as a jury-based dispute resolution system. Additionally, DB will assign credit scores, based on past job interactions pulled from on-chain records, to both bounty issuers and freelancers to discourage bad actors.

### **Implementation**

**Budget & Timeline:** 6000 GTC from Gitcoin DAO. Use of funds: 2 contracted frontend developers and 1 smart contract developer over 3 months to integrate Gitcoin's frontend with EthSign Smart Agreement's existing backend, and to test the platform. 

**Requests from Gitcoin:** Access to code and design assets pertaining to Gitcoin bounty platform's frontend to create a Gitcoin-EthSign co-branded frontend. Assistance in creating and distributing PR materials relating to overviewing DB. Access to Gitcoin's DAO community for user testing.

### Voting

**Yes** - I agree to the above proposal to implement a decentralized bounty platform parallel to Gitcoin's existing bounty platform interface that monitor's the off-chain development progress of freelancers and reacts to a pre-set milestones with on-chain logic set by bounty providers. This proposal will be executed by EthSign's development team, and funded according to the "Budget and Timeline" above.

**No** - I disagree to the above proposal and do not support the implementation of a decentralized bounty platform.

-------------------------

Xin | 2021-12-02 17:33:23 UTC | #2

Hi there, this is Xin, founder of EthSign. We are building operating system for DAOs, bounty board is one of the most important part in DAO toolkits. Onchain escrow contract eliminate security concerns, which will be a big help in scaling Gitcoin bounty board, make it to be a common good that adopted by other projects and DAOs.

-------------------------

Pfed-prog | 2021-12-02 18:14:08 UTC | #3

Personally, I have encountered bounties which are impossible to accomplish. The goal of the issuer is to say that the final product is not completed, hence, you will not receive a payment at all. 

I think establishing milestones would help to some extent, especially for organizations with low-med reputation.
But, yes from a position of a developer that has received bounties from Ceramic, Badger, Parsiq and Reflexer, I am for this proposal.

-------------------------

php | 2021-12-11 03:52:53 UTC | #4

Hi,

The idea is great and the design is feasible. Will you also be able to provide some document link of EthSign backend, or some details about the contracted developers?  So the roadmap details can be easier to understand.

-------------------------

connor | 2021-12-03 02:19:38 UTC | #5

Hey all! Connor from Gitcoin Core here. Quick disclaimer and for context: I've been part of a few discussions between Gitcoin and EthSign, the first back before GitcoinDAO was launched. Initially we spoke about using their Web3 enabled agreement signing product, and that evolved into discussions around how their tooling could be used to build a decentralized bounties platform. While we have not partnered together yet on anything officially, I've watched the EthSign team and platform grow significantly over the past year.

Gitcoin's first product launched in 2017 was bounties, and it remains a core part of the platform (+ backbone of hackathons and virtual events). The DAO is primarily focused on Gitcoin Grants, and I believe most of us agree the top priority is launching a permissionless decentralized quadratic funding platform, and turning cGrants into dGrants. I think the same should be done for cBounties to dBounties, but currently our teams and workstreams don't have the bandwidth to focus on it yet.

With the explosion of DAOs, there is a great opportunity for the first (or best) open and decentralized bounty protocol to get widely adopted. Something that can integrate with Discord, gov forms, snapshot/tally, etc. With trustless escrow, verifiable milestones, arbitration, little to no fees. The current Gitcoin bounty platform is a bit outdated and sluggish, but the brand name and community are powerful.

I believe this will take some time and warrants more discussion and fine-tuning, but if the DAO thinks it's worth funding, I'd love to see what the EthSign team can build in collaboration with Gitcoin.

-------------------------

bobjiang | 2021-12-03 02:50:51 UTC | #6

you're right. 

The goal for this proposal is to split huge bounty to small ones, and submission with payment step by step.

-------------------------

kyle | 2022-04-25 15:03:21 UTC | #7

[quote="ethanl, post:1, topic:9292"]
This “de-bounty” platform (DB) will utilize Gitcoin bounty platform’s frontend and EthSign Smart Agreement’s backend to automatically fulfill the agreement outlined in bounties in a trustless manner.
[/quote]

thanks for the proposal. i appreciate the thought in the system design. Gitcoin used to use the bounties.network protocol in a similar approach, but ultimately abandoned the flow as the gas fees and legitimacy of simply have funds in escrow were highly discouraging. funders could remove funds the same way they can today. i wonder if you have considered how to combat this? ie, which L2 you would propose?

[quote="ethanl, post:1, topic:9292"]
opposed to Gitcoin’s existing centralized workflow
[/quote]

you also mention that this approach would offer a decentralized alternative, do you have any other organizations that are interested in using this beyond Gitcoin? Any thoughts yet of audits and review of the smart contracts escrow setup?

-------------------------

jxu | 2021-12-05 08:24:34 UTC | #8

Hey, I'm Jack, the co-founder and tech lead of EthSign.

>  funders could remove funds the same way they can today. i wonder if you have considered how to combat this?

If we are referring to the funders being able to withdraw funds, we have a system in place where withdraws by the funder before the job deadline requires explicit authorization from the freelancer in the form of an ECDSA signature, which can be transmitted off-chain.

> gas fees

We can be present on any L2 network with Chainlink presence. We are also able to function on L2s without Chainlink but that would take away the automated execution (will require manual triggers) and off-chain data acquisition capabilities.

On a second thought, we can also pivot to Gelato if necessary but that will require some rewrites.

> do you have any other organizations that are interested in using this beyond Gitcoin?

We are working on integrating both our smart agreement product (what's said here) and our PDF signing product with a few finance platforms and DAOs.

> Any thoughts yet of audits and review of the smart contracts escrow setup?

Yes, an audit is most definitely required, especially when we deal with money. However, we would like to request an audit after we can get a preliminary code-lock as any change in code requires a new audit.

-------------------------

jxu | 2021-12-05 08:27:15 UTC | #9

This is correct, we are able to accommodate staged (for the lack of a better term) data sources and payouts.

-------------------------

jxu | 2021-12-05 08:29:06 UTC | #10

We have some basic documentation here (sorry, can't send links): 
`https://docs.ethsign.xyz/about-ethsign-smart-agreement/introduction`

It's by no means complete but should provide a decent overview.

-------------------------

Xin | 2021-12-05 18:44:52 UTC | #11

Technical walkthrough for EthSign Smart Agreement: https://docsend.com/view/ipjahgt8e2wskjjx

-------------------------
