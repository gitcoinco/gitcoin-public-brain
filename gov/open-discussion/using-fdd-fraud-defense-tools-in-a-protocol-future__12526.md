---
id: 12526
title: "Using FDD Fraud Defense Tools in a Protocol Future"
slug: using-fdd-fraud-defense-tools-in-a-protocol-future
category: open-discussion
url: https://gov.gitcoin.co/t/using-fdd-fraud-defense-tools-in-a-protocol-future/12526
created_at: 2023-01-09T14:03:45.900Z
last_posted_at: 2023-01-09T14:03:46.028Z
posts_count: 1
views: 3246
like_count: 6
---

# Using FDD Fraud Defense Tools in a Protocol Future

<https://gov.gitcoin.co/t/using-fdd-fraud-defense-tools-in-a-protocol-future/12526>
DisruptionJoe | 2023-01-12 09:37:59 UTC | #1

# User Personas for Fraud Defense Tools

The primary user persona for fraud defense tools is the "Fraud Consultant". This is a person who understands the past sybil attacks and steps taken to mitigate them. They are not only able to consult program & round operators, but also other uses of Passport, Project, and Program protocols. 

The second user persona for fraud defense tools is the "Round Operator". Most likely this will be someone on the Gitcoin PGF workstream team for early rounds. Their primary interest is maintaining a happy community where funders and donors both feel that capital is optimally distributed in their program (or at least as close as possible). 

The "round operator" is the persona of someone focused on a single instance of a grant round voting event. The term "program operator" is referring to the operator of multiple rounds for the same program. Imagine Uniswap hosts 4 rounds per year. The program operator and round operator are likely, but not necessarily the same person. "Event operator" further abstracts this role to include events which are not Gitcoin Grants related such as a vote on snapshot (which has integrated Passport). 

# The Basics for Understanding Fraud Defense Tooling

This discussion will focus on the Fraud Consultant (FC) user persona. There are four likely tools in the FC toolbag. 

1. Passport Scoring App  (Being built by GPC with FDD) 
2. Wallet Scoring App  (Built by FDD - Repurposing from account handle to wallet) 
3. Grant Scoring App  (FDD building - mvp this season likely, but may be S17)
4. Program Governance App   (Future project - Not discussed here)

![GR15 Identity Analysis (Internal)  (13)|690x388](upload://2q82bcl3WeRcMvdcpZip9mzDjUl.jpeg)

Each of these application will use open source modules, "legos", to consistently retrieve, aggregate, and compute useful signals for fraud defense techniques to be applied to grants rounds. 

While Passport Scoring as a Service will work for many use cases, it will not be enough for communities with high value decisions and/or those who wish to maximally empower voters. One score for all communities will always be subject to type 1 & type 2 errors. Because no single analysis will tell us if users are sybil or not, we will need to customize scoring for each program for the best protection possible. 

![GR15 Identity Analysis (Internal)  (11)|690x388] (upload://wcujowe2Skt8pe6Osis6SKIRy2W.jpeg)

# What are these Legos?

[Fraud Defense Legos](https://gov.gitcoin.co/t/anti-sybil-legos/12265) are the individual modules which combine to provide targeted analysis regarding known fraudulent behavioral indicators. 

Each Lego is an analysis which is validated to be correlated to an account being sybil. Analysts decide what the threshold is for this signal to be enough to count. The Levenstein distance is good one to share as it is not longer in use with the switch to the protocol. Notice how we set a threshold to determine a boolean output. 

![GR15 Fraud Analysis (Internal)  (16)|690x388](upload://uGHWNKF0RdlAxlsZKZpFc1TtyMl.jpeg)

Some of the legos are for analysis. Some extract data directly from RPCs or a subgraph. Others clean or wrangle data. In all, these legos are crowdsourced and strengthened by the Open Data Community. The secret sauce lies in how we use them to build customize fraud mitigation for each program and event. 

The primary reason for needing these Legos as middleware for the fraud defense applications is that fraud defense is an iterative game. Once a behavior is detected and mitigated, the fraudsters find a new loophole. The legos allow for continuous integration / continuous delivery of the right analysis at the right time. 

# The Applications

Here we will show how two of 2 of 4 applications will be used and the legos needed to operate them. 

## Passport Scoring Application

## Passport Legos

- Passport User Interface(s)
- Passport Data Extraction Tool
- Passport Scoring as a Service Module
- Passport Scoring Legos (Composable open source analysis formatted to be executable & readable by the Passport Scoring Application) 

The PSA allows a user to view all the stamps a user has acquired (or set of users) allowing them to recommend a best course of action for preventing fraud within the requirements of the round. 

### Passport Application Examples
Here are a few examples of how considerations on how this will work in practice. This will only focus on the Gitcoin Grants use case. 

**Example 1** - A Program/Round Operator would like to "gate" access to voting in a QF/QV vote. An FC might recommend that they use some combination or score of stamps to gate their particular round. 

Passport Scores are instance specific and are applied by the event operator. A passport score may be applied to a user when participating in a vote/round. They may apply a score when the user joins a community. How a score is used is always on the event operator side of the system. The ability to update or change a score is therefore irrelevant because the event operator can always choose to modify how they interpret an existing score provided by Gitcoin or anyone else. 

- A set of specific stamps a user MUST have
- A number of total stamps a user MUST have
- Use the Boolean Output of one of Gitcoin's Passport Scoring as a Service models
- Use a combination of PSaaS + another requirement
- Design custom set of stamp weights (or download another user/community list) 
- An event operator can always create an "escape hatch" where a user who is denied can do some other action to "prove" they should be allowed

**Example 2** - A Program/Round operator would like to gate access to only users who have a passport without any stamp/scoring requirements. They instead wish to "weight" the users voice in the vote. The reason they would use Passport stamps for weighting rather than onchain wallet signals is because Passport provides a shared ETL layer for their community to verify, validate, and reproduce algorithmic policy decisions. 

Simple algorithms
- decrease weight by 50% if less than 2 stamps
- increase weight by 100% if more than 2 stamps

Complicated algorithms
- Quadratically increase voice for each stamp a user has
- Create custom teir levels of stamps with associated voice benefits
- if user has x & y stamps, then use the PSaaS to weight their voice
- PSaaS Cost of Forgery Model

Complex algorithms
- PSaaS regression models
- Create a custom ML model
- Host your own community semi-supervised reinforcement learning model

**Example 3** - A Program/Round operator wouls like to hold the right to "squelch" (apply a 0 coefficient) to a user during or after the round based on behavior during the round. 

- Uses the complete Fraud Defense Stack during the round to assign a subset of users to "Thor & Loki datasets" (for sure sybil & not sybil) which can be used to run a standardized Machine Learning model against using Passport Stamps as the only features in the model. At first this seems counter-productive, but the purpose of doing this is to allow the community to verify and reproduce the results, validate the ML model, and have humans evaluate the Thor & Loki datasets.

### Open Questions about Passport Scoring Application and how Gitcoin uses it

- Should Gitcoin have a set of stamps which are required, but not legibile? The purpose of Verified Credentials (VC), the technology that stamps use, is that they are different than Soul Bound Tokens (SBT) is consent. A passport user must accept any stamps that the third party is willing to attest to. These stamps are all open source and a technical user could verify that the stamp is what it claims to be. Gitcoin could offer a set of stamps which include both positive and negative information. The user might not consent to us looking at onchain activity to see if they have a history of sybil behavior, but a single grant program (maybe Gitcoin's) could require these stamps where a user is consenting for us to run all of our sybil detection analysis?
- Should Gitcoin (or a private entity spun out) keep a centralized DB (or decentralized) with a history of analysis results for Passports? (or a history of how many communities have claimed them as sybil)
- Should Gitcoin include a consent claim stamp for all publicly available onchain data?
- Should Gitcoin build a known identifier module to allow communities to privately share their "blacklist"? (Think a stamp that verifies you aren't on any) 


## Wallet Scoring App

### Wallet Legos

- Onchain Data Extraction Legos (Standardized datasets indexed automated - Custom datasets TBD)
	- Grant Round Donations/Votes
	- A Wallet's historical transactions
	- x number of hops from a wallet
	- Initial funding wallet
	- Automated Onchain Extraction Tool
	- Decentralized Validation Tool (drops a copy of every data extraction info IPFS/Arweave)
	- New custom data schemas
- Wallet Scoring Legos (Composable open source analysis code which can be executed & read by the wallet scoring application) 
	- Historical Behavior Analysis
		- Intial Funding Wallet
		- Total transactions by wallet
	- Event-Based Behavioral Analysis (usually used for a complete round
		- Wallet behavior in a previous round
		- Number of donations this round
	- Dynamic Realtime Analysis
		- Analysis pulled during an event
		- Any analysis used for the Fraud Defense Dashboard (Freemium Tool) 
		- Compound analysis using multiple analysis legos
			- Percentage of a wallet's donations went to flagged grants
			- Percentage of flagged programs of total programs participated in

### Wallet Application Examples

Here are a few examples of how a Fraud Consultant might use the wallet scoring application.

**Example 1** - FDD/Gitcoin stamps a user with the results of Wallet Scoring Application outputs. (Referenced above in PSA questions section) 

**Example 2** - An event operator uses passport to gate, but still feels like their round may have been sybil attacked

**Example 3** - An event operator wants their round to be open/inclusive without Passport gating and hires Gitcoin/FDD to dynamically monitor the round and use reactive sybil mitigaion techniques if needed. 

**Example 4** - A standardized post round analysis provided to all programs > $x GMV

-------------------------
