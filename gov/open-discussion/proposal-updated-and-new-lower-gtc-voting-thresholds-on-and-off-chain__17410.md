---
id: 17410
title: "[Proposal] Updated (and new!): Lower GTC Voting Thresholds on and off chain"
slug: proposal-updated-and-new-lower-gtc-voting-thresholds-on-and-off-chain
category: open-discussion
url: https://gov.gitcoin.co/t/proposal-updated-and-new-lower-gtc-voting-thresholds-on-and-off-chain/17410
created_at: 2024-01-13T15:46:23.106Z
last_posted_at: 2024-02-01T09:36:13.489Z
posts_count: 11
views: 3951
like_count: 27
---

# [Proposal] Updated (and new!): Lower GTC Voting Thresholds on and off chain

<https://gov.gitcoin.co/t/proposal-updated-and-new-lower-gtc-voting-thresholds-on-and-off-chain/17410>
kyle | 2024-01-13 15:46:23 UTC | #1

## Context and Update

In our continued efforts to evolve and democratize the governance process within the Gitcoin DAO, we previously proposed ([which passed](https://snapshot.org/#/gitcoindao.eth/proposal/0xa68b33484f5fe3e53f2f51335483057200d3fa08cdafc93c0904b29514cb9980)!) adjustments to the GTC voting thresholds. After valuable discussions and technical consultations, it's clear that some proposed changes need refinement. Specifically, adjusting the 2.5M GTC quorum requirement presents technical challenges and may necessitate deploying a new contract, which we want to avoid. However, we can modify the 1M GTC requirement for creating new proposals.

## Original Proposal Recap

Our initial proposal aimed to empower a broader range of GTC token holders in the governance process by reducing the dominance of large holders. The key points were:

* Lowering the quorum threshold from 2.5M GTC to 1M GTC for both on-chain and off-chain voting.

* Reducing the initial proposal threshold from 1M GTC to 150K GTC.

* Keeping the current time and duration for voting procedures intact.

## Revised Proposal Details
Based on technical advisability, the revised proposal is as follows:

* Maintain Quorum Threshold: While the original plan was to reduce the quorum threshold to 1M GTC, we don’t want to deploy a new governor to make this change.

* Reduce Proposal Threshold: Lower the requirement to initiate a proposal from 1M GTC to 150K GTC, making it easier for a wider range of stakeholders to actively participate in governance.

* Maintain Current Voting Processes: The existing timeframes and procedures for both on-chain and off-chain voting will remain unchanged to ensure continuity and stability in our governance operations.

## Next Steps:

Barring any strong community feedback, we’ll move this (new) proposal through the same governance steps as any proposal follows, with the above mentioned adjustments in implementation (maintain quorum threshold, reduced proposal threshold and maintained voting processes).

## Vote

* Yes - Approve the adjustments to the voting thresholds as proposed.
* No - Do not implement the proposed changes to the voting thresholds.
* Abstain - Neither approve nor disapprove the proposed changes.

-------------------------

CoachJonathan | 2024-01-15 16:25:40 UTC | #2

Thanks for this revised proposal, Kyle. I am in favor of moving forward with this.

Sounds like the work effort needed to implement the new quorum threshold is high and it may be worthwhile keeping this threshold for now until it becomes a much more intense and obvious pain point.

-------------------------

owocki | 2024-01-15 19:40:59 UTC | #3

I will be voting yes on this proposal.

-------------------------

krrisis | 2024-01-18 15:14:18 UTC | #4

Thx for the clear update, will be voting yes

-------------------------

kempsterrrr | 2024-01-22 15:26:39 UTC | #5

Nice initiative, develope dao will be voting yes on this proposal assuming we can get our voting issue cleared up by the time this is elevated.

We're considering a similar change, is there anything you can share regarding how you decided on 150k as the right number of the threshold?

-------------------------

kyle | 2024-01-22 16:03:06 UTC | #6

Great question, the 150k was based on looking at the current GTC delegation amount and trying to be more inclusive of the top 25.

-------------------------

Viriya | 2024-01-23 15:25:49 UTC | #7

Aligned! I'll be voting yes on this.

-------------------------

owocki | 2024-01-23 16:47:26 UTC | #8

[quote="kyle, post:1, topic:17410"]
* Reducing the initial proposal threshold from 1M GTC to 150K GTC.
[/quote]

I do wonder if well start to see spam or malicious proposals with this new lower, threshold. Thinking adversarially for a moment, the path for an attacker to attack the DAO would be
1. Acquire 150k GTC
2. Self-delegate
3. Submit a proposal, hope no one notices. *note: the proposal could be crafted to look like a genuine proposal (like a budget request)
4. Find enough votes to reach quorum.
5. Pass it.

Vigilance from the top delegates + from the [Wallet Guard](https://gov.gitcoin.co/t/gitcoin-walletguard/16772) will be needed.

-------

That said, I am leaning towards voting FOR this proposal.  I think the positives outweigh the negatives..

-------------------------

CoachJonathan | 2024-01-23 17:16:38 UTC | #9

This proposal is now live on Snapshot: https://snapshot.org/#/gitcoindao.eth/proposal/0x7747f4f73400a296f1ef2010ebfdc72f02327ed4c95cd7dd1220f610d6ee0bbf

-------------------------

sarahasher | 2024-01-28 15:45:01 UTC | #10

nice proposal. looking forward for a positive effect once implemented

-------------------------

favvyuc | 2024-02-01 09:36:13 UTC | #11

i will be voting yes to this proposal, its great

-------------------------
