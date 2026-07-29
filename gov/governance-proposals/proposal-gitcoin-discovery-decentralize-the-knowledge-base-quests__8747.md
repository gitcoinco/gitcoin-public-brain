---
id: 8747
title: "[PROPOSAL] - Gitcoin Discovery: Decentralize the Knowledge Base & Quests"
slug: proposal-gitcoin-discovery-decentralize-the-knowledge-base-quests
category: governance-proposals
url: https://gov.gitcoin.co/t/proposal-gitcoin-discovery-decentralize-the-knowledge-base-quests/8747
created_at: 2021-10-06T22:20:12.876Z
last_posted_at: 2021-10-20T07:53:15.986Z
posts_count: 15
views: 6152
like_count: 75
---

# [PROPOSAL] - Gitcoin Discovery: Decentralize the Knowledge Base & Quests

<https://gov.gitcoin.co/t/proposal-gitcoin-discovery-decentralize-the-knowledge-base-quests/8747>
Huxwell | 2021-10-06 22:32:07 UTC | #1

## Abstract

This proposal aims to introduce a new Workstream (WS) called **Gitcoin Discovery** within the **Gitcoin DAO.** The Workstream will be responsible for decentralizing and improving the **Gitcoin** **Quests**, which will become **dQuests**,  through the **Gitcoin Knowledge Base**, which will become **dKnowledge.** 

Built on a decentralized infrastructure, **dQuests** is a **gamified** **platform** where users will be able to progress through various types of quests—like quizzes, code challenges, and on-chain transactions—gaining the ability to verify their diverse skillsets ([see initial prototype - HackFS Hackathon Finale live demo](https://www.youtube.com/watch?v=UGJA6eahQBg)).

- **dKnowledge** will contain educational information and FAQs about the **Gitcoin ecosystem, Web3 projects, and technologies.** The content within the Knowledge Base will be used to populate **quest preparation materials.**
- By successfully completing a quest, users will be able to:
    - earn **XPs** and increase their **ranking**
    - mint **Quest** & **Badge NFTs** with a **random rarity**
    - and grow their **Dynamic Skill Tree NFT** by **validating** their **learnings** and **actions** through **on-chain micro-credentials**.
![Frame 1|690x401](upload://p1pNR5U1FFrzWSuMfiWIKhOqyj0.jpeg)

        

## **Motivation**

Getting started in Web3 is difficult because the information needed to overcome the steep learning curve is:

- Scattered
- Unreliable
- Censorable

**Gitcoin Discovery** will be a community-driven, learning platform for onboarding and engaging users & developers into Web3.

In order to provide high-quality courses built around open source, trustable and verifiable content, members of the Web3 projects will collaborate with community experts in various fields such as:

- content creation
- development & infrastructure
- research and security

As the **Gitcoin DAO** expands, we believe there are 3 main problems that need to be solved:  

- **Aggregating ever-growing but scattered information**
- **Retaining users and community members/contributors**
- **DAO project management, contributor management, and intuitive onboarding**

Once the changes are implemented: 

- Contributors will be motivated to perform certain tasks on the Gitcoin Knowledge Base, such as:
    - suggest edits
    - suggest translations,
    - update information, etc.
- The implementation of Quest, Badge, and Skill Tree NFTs will add an incentive layer for platform users and DAO contributors to engage with the ecosystem.
- Platform users can be onboarded to the GitcoinDAO and to Web3 projects easily with verified skills and interests.
- Platform users can trade their quests & badge NFTs.

## Overview

**Gitcoin Discovery Workstream** (**GDW**) believes that the first step to solving these problems is to **decentralize** the **Gitcoin Quests** by motivating contributors to actively participate in the expansion of the **GitcoinDAO**.

**Gitcoin Discovery** **Workstream** will consist of 2 sub-streams:

- **dKnowledge** will contain information related to the Gitcoin ecosystem (grants, bounties, GTC, hackathons, policies, FAQs, etc.)
- **dQuests** will display the content from **dKnowledge** in a more engaging way and it will reward users for validating their learnings and actions.

We believe in **effective collaboration** required from our end to be able to implement the improvements we are proposing.

That's why our budgetary framework is thoughtfully drafted for efficient **cross-Workstream collaboration**, as shown below: 

![Brainstorming Sessions (3)|690x291](upload://wIJEhVhgAsDdUgA88ORzItRgMpa.jpeg)


## **Specification**

### Roadmaps

**To see the roadmaps in general refer to the pages below:** 

[dQuests Roadmap](https://www.notion.so/dQuests-Roadmap-5a43290a54814d3cbca92296d866976a)

**[dKnowledge Roadmap](https://www.notion.so/bea828cf10364e378c3d8c917fdfc312)**

### Measuring Success

Our **workstream** will **solve** most of the **current Gitcoin Quests' issues**:

- Quests are not grouped by project or topic
- Content is mainly for techies
- Repetitive Q&As
- Time-inefficient to load quests and go through a quiz
- Bypass of security measures (e.g. quest timeout and quest completion verification)

**dKnowledge** 

- Decentralization of Gitcoin Knowledge Base infrastructure
- User-friendly library format to Knowledge Base
- Collecting, forming, and organizing scattered information related to Gitcoin ecosystem
- Increase community participation into the decentralized Knowledge Base (dKnowledge)
    - community pool prizes for translations, edits, completion of missing information, etc.
- Translation of the content within dKnowledge to 5 languages (Chinese, Japanese, French, English, and Spanish)

**dQuests** 

- Decentralization of Gitcoin Quests infrastructure
- Quest preparation material template
- Dashboard for project owners/contributors
- Introduction to dBadges to verify the skills of a contributor/user via Dynamic NFTs

**Gitcoin Discovery Features**

- Dynamic NFT Skill Tree
- dBadges
- DAO member onboarding structure
- dQuest, project dashboard
- Squad incentivization policies on content creation for quests and knowledge base
- Mentorship sessions

**Our long-term roadmap is the following**:

We will need **6 months(Q4 2021 - Q2 2022)** to get a decent **alpha** version on the **3 milestones** described below,
then **3** **more months(Q2 2022)** to make changes and improvements based on the feedback,
and then we'll be ready for an **open beta release**.

**Our short-term roadmap (*which is what the current funding's for*) is the following:** 

**Milestone 1 -** 1 month

**Intuitively pleasant user interface** - We will create a user interface that will allow for users to join the Gitcoin Discovery Web dApp. The user will be able to create new "projects" which will entail creating and uploading data to GitBook. We will create and test a Github Action that can be plugged in any repo (GitBook or code), which will automatically upload the files of the repo to FileCoin and IPFS through web3.storage. In addition to the files of the repo, we will have the creator of the project upload images which will be ranked according to rarity. These images will be uploaded to web3.storage and using Web3.js, we will store in mapping with the image CIDs linked to the rarity and project name on-chain and emit an event of the storage.

**Milestone 2 -** 2 months

We will begin to implement and extend the multiple smart contracts needed for our project flow. A Project Factory smart contract will control the access, approvers, and minting of NFTs. This contract will inherit from ERC-721, and will keep track of pending eligible addresses for future minting. We will use Identity-Link Services built on top of IDX and Ceramic (Ceramic and IDX are built on top of IPFS) to link the GitHub account to an ethereum address(es) and DID through the user profile page. Separately a Topic Factory smart contract for contributors to established projects will be created. Within this contract, the Chainlink VRF will be used to add randomness to the minting of the NFT. We will also build a Chainlink external adapter which will pass the metadata and the chosen image from the mapping to NFT.storage and return the URI from NFT.storage to the smart contract.

**At the end of Q4, upon the completion of the above-mentioned milestones, we will kick off Q1 2022 with Milestone 3 as described below:** 

**Milestone 3 -** 2 months  

We will build a subgraph that will track the metadata of the project and topic NFTs. This will serve as a project registry and will also store the details of the projects. Our front-end will use the NFT.storage URIs to display the details about the projects and topics. We will build a smart contract for the quests that users will complete within the topics. The UI will be built for presenting these quests. The smart contract will call a Chainlink External Adapter which will check the Ceramic streamID for proof that the user completed the quest and will also pass metadata to NFT.storage and return URI to the contract. This will also utilize the Chainlink VRF contract for randomness according to pre-set thresholds within the smart contract. We will build a subgraph that will track the metadata of the project and topic NFTs. This will serve as a project registry and will also store the details of the projects. Our front-end will use the NFT.storage URIs to display the details about the projects and topics. We will build a smart contract for the quests that users will complete within the topics. The UI will be built for presenting these quests. The smart contract will call a Chainlink External Adapter which will check the ceramic streamID for proof that the user completed the quest and will also pass metadata to NFT.storage and return URI to the contract. This will also utilize the Chainlink VRF contract for randomness according to pre-set thresholds within the smart contract.

**Maintenance and Upgrade Plan:** Our team will update any library that we use on a continual basis. We will provide maintenance for the overall availability and security of the dApp. This will include bug fixes, monitoring, upgrades to major versions of tools such as Chainlink v2, new web3.storage releases, et al. We will also be looking for ways to enhance our existing features.

## **Benefits**

The core benefit of this proposal, if approved, is that GDWS will improve the ways and means of collaboration between GitcoinDAO contributors, GitcoinDAO Workstreams, and Gitcoin platform users. It would open the DAO to test, improve and implement ever-growing community incentivization protocols. 

Further along the line, Gitcoin Discovery, with planned features to be presented as we progress, will help onboard thousands, if not millions of users and developers into Web3 space. 

We emphasize the vision provided in the research of *[Modular Politics: Toward a Governance Layer for Online Communities](https://dl.acm.org/doi/pdf/10.1145/3449090)*; 

> (1) Modularity: Platform operators and community members should have the ability to construct systems by creating, importing, and arranging composable parts together as a coherent whole.
(2) Expressiveness: The governance layer should be able to implement as wide a range of processes as possible.
(3) Portability: Governance tools developed for one platform should be portable to another platform for reuse and adaptation.
(4) Interoperability: Governance systems operating on different platforms and protocols should have the ability to interact with each other, sharing data and influencing each other’s processes.
> 

## **Drawbacks**

If we had to build the whole infrastructure to achieve decentralization it could have been a challenge but as we're going to use composable technologies and great libraries like NFT.storage, Web3.storage, Ceramic, Chainlink VRF, The Graph, and other tools for the right job, it will make it easier to build this dApp.

## About our Team

[Gitcoin Discovery **Team Members** ](https://www.notion.so/Gitcoin-Discovery-Team-Members-814f7fa2402941dc9b9d48f9cc03c8b2)

## ADDITIONAL INFORMATION:

**What do you need from Gitcoin and when?**

A lot of collaboration! 
We would like to have a dedicated budget for Gitcoin Discovery Workstream to expand our collaborative efforts to decentralize Gitcoin with other existing Workstreams.

We are asking funding for a total of **63k GTC** for **Q4 2021**. ([see detailed budget distribution diagram here](/uploads/db4391/optimized/2X/e/e554289dc080b52d2f6ef615566261f8663b1c88_2_1035x436.jpeg)).

Starting from Q4, we would like to collaborate with **Public Goods Workstream** to; 

- Decentralize the informational resources (library, knowledge base, research papers, etc.),

Starting from Q4, we would like to collaborate with **MMM Workstream** and have 2 full-time developers working on; 

- Trading of NFTs earned on dQuests within DAOmart.

Starting from Q4, we would like to collaborate with the **FDD Workstream**:

- DevSecOps squad will help us with infrastructure, security-related tasks such as;
    - CI/CD
    - Observability & Availability
    - GitOps
    - Security audits
- Policy squad will work on:
    - Content approval to make sure it complies with our policy
    - Recommend updates for articles dealing with subjectivity
- Content & user support squads will work on:
    - Decides what content needs to be added and is responsible for drafting
    - Collaboration between content, user support & policy
    - Discord Knowledge Bot

Starting from Q4, we would like to collaborate with **Moonshot Collective** **Workstream** projects and have: 

- 2 full-time developers (Scaffold ETH Contributors) working on building a Scaffold ETH Pathway and quests,
- 2 full-time developers (OpenSignal Contributors) working on:
    - Project curation
    - Course curation
    - Course farming (staking)
    - Quest curation
- 2 full-time developers (Subgraph dev team) working on:
    - Subgraph Development
    - Subgraph Curation
    - Subgraph Consumption
- 1 full-time designer and 1 full-time developer working on:
    - Figma design system
    - React component library
    

Starting from Q4, we would like to collaborate with **Ambassadors and Advisors** to reach out to people deeply involved in web3 education, ideally with technical knowledge;

- Token engineers (interested in mechanism design and behavioral incentives)
- Members from Gitcoin and Gitcoin DAO to give feedback and to help us co-create the future of decentralized gamified education in Web3.

This is an open call for collaboration with:
- GitcoinDAO: its workstreams and contributors
- @TEC
- @BanklessDAO

## **Vote**

**FOR** - If you vote "yes", Gitcoin Discovery Workstream will be created, and the proposed budget above will be allocated to the multisig of the Gitcoin Discovery Workstream. 

**AGAINST** - If you vote "no", Gitcoin Discovery Workstream won't be created, and the requested budget won't be allocated.

-------------------------

qedk | 2021-10-07 06:02:25 UTC | #2

this sounds great, let's do this! :muscle:

-------------------------

krrisis | 2021-10-07 10:26:15 UTC | #3

Wow, what a great and especially detailed proposal. Fantastic that you guys put so much work in this. First thought I have, in order to keep things efficient at this point in our development is: do it, but don't create a new workstream, become a part of the '[Decentralize Gitcoin' WS](https://gov.gitcoin.co/t/workstream-decentralize-gitcoin/180), spearheaded by @phutchins. 

I think the depth, ambition and impact of this proposal should not be underestimated but maybe it could be more effective to spin it off into becoming its own workstream in one of the next phases and live under an existing one for now? The main advantage is that it simplifies the budget side of things, it can be incorporated in an existing budget, which means less budgets to pass through every month. 

Just my two gwei ofc. Curious to read more feedback here!

-------------------------

bobjiang | 2021-10-07 12:38:46 UTC | #4

Hi @Huxwell 

This is a fantastic idea, love it.
In special it could help the users to learn web3 with current knowledge base, and integrating NFT, knowledge base, quests together.

I also quote @krrisis advice here because I strongly agree with Kris.
It is hard to maintain a workstream (with lots of ops like communication, budgeting, etc), but you could start from small, inside decentralized gitcoin workstream now. 
Once it is required, you can create new workstream as described in your post.

[quote="krrisis, post:3, topic:8747"]
don’t create a new workstream, become a part of the '[Decentralize Gitcoin’ WS](https://gov.gitcoin.co/t/workstream-decentralize-gitcoin/180), spearheaded by @phutchins.
[/quote]

-------------------------

owocki | 2021-10-07 13:45:01 UTC | #5

63k GTC is a lot of trust upfront with no delivery of the alpha until 6-9 months from now.  is there any way to put that into escrow?  how doe sthat work if the MVP doesnt get delivered adequately?

-------------------------

Huxwell | 2021-10-07 16:40:34 UTC | #6

Yes and of course it is clear to me that I will sign an Open Source Software Agreement where the funds will be released upon completion of what is defined for each milestone, starting simple with a Milestone of one month.

It's my bad because I mixed short-term and long-term..
The idea was to use 35k GTC for cross-stream collaboration.
A big chunk would be dedicated to the FDD for DevSecOps related tasks and to the Moonshot Collective for the prototyping of specific features and/or to boost the integration with an existing protocol such as Open Signal.

However, this kind of collaboration might make more sense after the alpha release. So we will ask for a smaller budget, that will be put into escrow.

-------------------------

Fishbiscuit | 2021-10-07 16:41:40 UTC | #7

Hello! I love the vision of a decentralised learning community platform. Its a problem I think about everyday and I hope you won't mind the long post!

However, as @owocki and @krrisis has mentioned, starting an entire workstream + becoming one of the highest budget workstreams is quite an ask.

May I suggest being first incubated in the decentralise Gitcoin workstream as a project? 

Here's some thoughts from working in education in blockchain:
1. As you've rightly pointed out, knowledge is extremely scattered. There has been several efforts to try to make sense of it but `knowledge_curation_speed < knowledge_production_speed` and its hard to catch up on what's even out there yet. That alone is a large project and can be quite opinionated in the sense that what you choose to include and what you don't shapes the minds of the folks that learn it. 

2. What you're proposing seems really very very very similar to Rabbithole. I've been doing Rabbithole quests and one drawback was that it was a good way for already crypto native folks to get further ahead but most people that were new to crypto couldn't figure out how to get started (signing, tx, gas, needing ETH to start). Building up that ramp is a massive UX challenge too!

3. I've been in some conversations about inter-DAO onboarding and a big challenge has to do with levelling people from 0 context to "I can figure out what's happening in Discord"-level context

Some suggestions:
1. It seems that putting the objectives of onboarding, learning, and engaging in a single platform might lead to a fractionalisation of intent so I'd **suggest picking one objective as a priority first**!

2. I'd suggest **building this on a chain that doesn't require as much gas**. Also, there are quite a few assumed prerequisites to be able to interact with the platform (based on what I'm seeing so far) the first quest should be simple and get folks to claim their first POAP or something that doesn't cost anything.

3. Building an MVP in a shorter timeframe (<6 months) by **putting together tools that currently exist and seeing how people interact with them**. Such as using Mirror for paying for articles, Setting up knowledge bounties to get people to work on content, integrating with the effort on dQuests and so on

Some offers:
1. I've been talking to folks at where I work and expounding the idea that education should be a public good, contributing to this knowledge base would be something we'd be happy to help!

2. I'll drop this over to Bankless' Academy and see how the response goes

-------------------------

Huxwell | 2021-10-07 17:35:36 UTC | #8

Thanks a lot for this feedback @Fishbiscuit and @krrisis !

I understand that starting as our own workstream seems pre-mature and too ambitious but it was just a way of saying that this project would require collaboration across workstreams and DAOs rather than just being in a silo for tech savies.
And I'm completely fine with the approach of starting small within the Decentralize Gitcoin workstream if that's what the consensus is.

> 1. As you’ve rightly pointed out, knowledge is extremely scattered. There has been several efforts to try to make sense of it but `knowledge_curation_speed < knowledge_production_speed` and its hard to catch up on what’s even out there yet. That alone is a large project and can be quite opinionated in the sense that what you choose to include and what you don’t shapes the minds of the folks that learn it.

Yes and our strongest opinion is that the content will be open source and we will leverage the use of existing open source tools like Gitbook for content co-creation.

> 2. What you’re proposing seems really very very very similar to Rabbithole. I’ve been doing Rabbithole quests and one drawback was that it was a good way for already crypto native folks to get further ahead but most people that were new to crypto couldn’t figure out how to get started (signing, tx, gas, needing ETH to start). Building up that ramp is a massive UX challenge too!

It is indeed similar to existing projects at the surface, the one you mentionned is great but not open source and at the service of VCs. And they are also very opinionated on how people should learn. And in their case, you're completely right, it's mainly used by crypto-natives.

So that's why on our [demo](https://www.youtube.com/watch?v=UGJA6eahQBg), I explain the difference between our two main pathways,
 **Branch'ed:**
Theoretical content for users willing to learn how to use the best Web3 projects and tools.

**Decrypt'ed:**
Technical content for developers and technology enthusiasts willing to expand their skills.

> 3. I’ve been in some conversations about inter-DAO onboarding and a big challenge has to do with levelling people from 0 context to “I can figure out what’s happening in Discord”-level context.

I completely agree, that's why project creators will be able to create their own pathway, to ease the onboarding process by giving an overview of their project in an engaging way.

> 1. It seems that putting the objectives of onboarding, learning, and engaging in a single platform might lead to a fractionalisation of intent so I’d **suggest picking one objective as a priority first** !

The purpose of this is to have a centralised content delivery platform which is built on a decentralized and cost efficient infrastructure, you can think of this as a digital school where anyone is free to join and leave, where you learn therotical content, you experiment, you "pass exams" and get recognition for it.

I'd be more than happy to collaborate with you and the Bankless Academy!

Please reach out to me on Discord: Huxwell #2172 or by email: huxwell.fsociety@gmail.com (anon/public email, don't be scared by it :smiley:)

-------------------------

phutchins | 2021-10-07 21:46:46 UTC | #9

First of all, I love the thought and detail that has been put into this plan and budget. Others have captured many of the thoughts that I have as well so I'll keep my feedback as short as possible.

**Budget and scope**
The budget ask and team seems a bit large to get started. I am all for talking about how we could bring you into the Decentralized Gitcoin workstream as an incubator to get things going and prove out the idea. I also agree that we could trim the initial scope to get laser focus and set the effort up for quick and clear results.

**Team**
There are a number of roles that probably aren't necessary to get started and at least a few of them might not be a full time role for one project. A few of the roles however could potentially be shared resources between dGrants and Discovery. Project management and the Product roles are good examples of that. I'm interested to chat about potentially bringing on full time contributors to these roles that we would share within the workstream.

**Proposal Content**
While I love the detail, I think it would be helpful to split this into two documents. One which is a high level summary covering intent, direction, high level timeline, and team roles. This document could link to the next which would contain all of the greater detail that you've provided here. That presentation would help get more people interested more quickly by trimming down the time commitment for reviewing.

Let's chat!

-------------------------

Huxwell | 2021-10-08 00:01:39 UTC | #10

Thanks for your feedback @phutchins!
We would be more than happy to join the Decentralized Gitcoin Workstream and share product resources.

[quote="phutchins, post:9, topic:8747"]
**Budget and scope**
The budget ask and team seems a bit large to get started. I am all for talking about how we could bring you into the Decentralized Gitcoin workstream as an incubator to get things going and prove out the idea. I also agree that we could trim the initial scope to get laser focus and set the effort up for quick and clear results.
[/quote]

We've put more thought into how Gitcoin Discovery will operate and we've also reworked the budget request (33k GTC for Q4 instead of 63k GTC).
We probably won't ask for a specific budget for collaboration with other workstreams, but instead will focus on delivering the first features:
![8364c7f8fc08c3c64c0adb1a5229d7be|690x203](upload://3XKqd1lbtbdOxUM8XNc1WyUDPXc.png)

I agree that this proposal is very cumbersome and some parts are a bit confusing. We will certainly write a new document that will be more coherent and straight to the point.

Let's chat more on Discord!

-------------------------

socal434 | 2021-10-10 08:46:24 UTC | #11

This seems like a great idea and I think the smaller start within the existing workstream will be a good way to prove out the project while minimizing some of the risk.

-------------------------

lee0007 | 2021-10-11 22:26:33 UTC | #12

I see there are a number of considerations here in the process of being determined yet given engineering strengths, knowledge base and existing quests I believe GitcoinDAO is in a very strong position  to develop a gamified onboarding solution to rival rabbithole.gg - which strikes me as an excellent "public goods" investment.  

From my position

- investigating the future for a GitcoinDAO Ambassador program 
- as a member of the InterDao Alliance
- involved with changes to onboarding at IndexCoop for Asia Pacific
- as KB4 cohort

I can confirm, there is common and agreed awareness of the need for **education lead pathways** to onboard and retain talented community contributors (and people at large) into the web 3 ecosystems.

We have a small requested Q4 budget (6k) for the Ambassador program I would be keen to collaborate on this project as it would underpin the future of all onboarding initiatives, community development and growth.

-------------------------

dereksilva | 2021-10-12 15:40:42 UTC | #13

One significant issue that Secret Network has run into recently is people asking for funds denominated in $SCRT, and then the price fluctuating significantly (e.g. from $2 to $5 per SCRT in a matter of days). I think it would be wise to lay down a USD figure and ask for that amount to be distributed in GTC at various milestones. This helps protect everyone from volatility, regardless of the direction, shields contributors from being undervalued, and protects the DAO from overvaluing contributions at time of remittance.

-------------------------

Huxwell | 2021-10-20 02:41:08 UTC | #15

Hey everyone,

Thanks a lot for your feedback and interest in Discovery!

We'd like to move forward by creating a vote on Snapshot in the following days that will contain an updated and simplified version for the proposal and budget request that you can find below.

**NOTE:** We've decided to rename **Discovery** to **dCompass**.
https://gov.gitcoin.co/t/proposal-integrate-dcompass-within-dgitcoin-to-build-dquests-dknowledge/8836

-------------------------

AwakeNing_Tong | 2021-10-20 07:53:15 UTC | #16

yea,,this sounds great, let’s do this! :muscle:

-------------------------
