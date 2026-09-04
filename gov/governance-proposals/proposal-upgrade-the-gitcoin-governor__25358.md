---
id: 25358
title: "[Proposal]: Upgrade the Gitcoin Governor"
slug: proposal-upgrade-the-gitcoin-governor
category: governance-proposals
url: https://gov.gitcoin.co/t/proposal-upgrade-the-gitcoin-governor/25358
created_at: 2026-08-08T14:39:38.343Z
last_posted_at: 2026-09-03T19:22:33.402Z
posts_count: 4
views: 104
like_count: 7
---

# [Proposal]: Upgrade the Gitcoin Governor

<https://gov.gitcoin.co/t/proposal-upgrade-the-gitcoin-governor/25358>
MathildaDV | 2026-08-08 14:39:38 UTC | #1

# **\[Proposal\]: Upgrade the Gitcoin Governor**

In March, [Tally announced](https://x.com/tallyxyz/status/2033914203837280737) their shutdown. [ScopeLift announced](https://x.com/ScopeLift/article/2039102450410434820) that they would be taking over the platform and its operations. As Gitcoin has used Tally for onchain governance, we explored a number of different options, and after internal due diligence decided to remain on the same platform and work with the ScopeLift team towards upgrades, most importantly security, especially after we had to move our treasury funds out of the timelock due to an open attack vector.

## **Summary**

Upgrade the Gitcoin DAO's on-chain Governor from GTC Governor Bravo to a modernized Governor built on OpenZeppelin v5. The upgrade preserves all current voting parameters and adds three capabilities: a Proposal Guardian that can cancel malicious proposals, late-quorum protection against last-minute vote manipulation, and a DAO-adjustable quorum.

## **Motivation**

The current Governor has served the DAO well but predates several improvements in onchain governance tooling. This upgrade closes known safety gaps without changing the voter experience: delegates will propose, vote, and delegate exactly as they do today.

## **What Changes**

Three new capabilities, additive only:

1. **Proposal Guardian.** A designated multisig can cancel proposals (only cancel, never modify or force execution). This is a safety valve against malicious, malformed, or compromised submissions. The DAO can remove or replace the guardian by governance vote. Those holding the seats of signers of the address will manage their own membership, and any change to a signer will be done through a governance vote. By definition, any proposal that does not go through our standard governance proposal process and follows the set format will be deemed malicious. Any proposal that follows the protocol but is highlighted as malicious will be reviewed by the guardian.

2. **Late-quorum protection.** If a proposal reaches quorum near the end of its voting window, the window automatically extends to guarantee a minimum reaction time for delegates. Closes a well-known category of last-block vote flips.

3. **DAO-adjustable quorum.** Quorum becomes a parameter the DAO can change by ordinary governance proposal rather than requiring another contract migration.

All other behavior is preserved. The new Governor is built from these OpenZeppelin extensions: GovernorCountingFractional (preserves ScopeLift's flexible voting), GovernorSettableFixedQuorum, GovernorPreventLateQuorum, GovernorSettings, GovernorProposalGuardian, and GovernorVotesComp (GTC token compatibility).

![Screenshot 2026-08-07 at 13.22.37|690x342](upload://zd3lYfVQya356rgx2MRGE7ffF2y.png)

Quorum, proposal threshold, voting delay, and voting period all remain DAO-adjustable after the upgrade.

## **Execution**

The upgrade is a two-action proposal submitted to the current Governor Bravo:

1. The Timelock designates the new Governor as pending admin.

2. The new Governor accepts the admin role.

On execution, the old Governor can no longer control the DAO timelock, while the new Governor can. ScopeLift will update Cactus (formerly Tally) to reflect the new Governor immediately. All future governance actions will go through the new Governor.

**Important for delegates:** Do not submit new proposals to the old Governor between this proposal going onchain and its execution. Any proposal submitted to the old Governor after this one lands will not be executable and will need to be resubmitted to the new Governor.

## **Validation**

ScopeLift's simulation suite runs the full upgrade lifecycle against forked mainnet state, covering deployment, proposal submission, delegate voting, execution, and post-upgrade Governor operations (including quorum adjustments, Proposal Guardian powers, and parameter updates). ScopeLift will re-run the full suite against the live on-chain proposal data before voting opens. ScopeLift is an experienced team of smart contract engineers with a particular expertise in Governance contracts and onchain operations. They’ve successfully built and upgraded Governance contracts for many large DAOs, including Compound, ZKsync, Radworks, PoolTogether, and Gitcoin itself (during our last upgrade cycle). 

## **Follow-up**

A separate proposal to adopt the **Franchiser** for treasury delegation will follow after this upgrade executes.

## **Vote**

**FOR** to upgrade the Gitcoin Governor
**ABSTAIN** from voting on upgrading the Gitcoin Governor
**AGAINST** upgrading the Gitcoin Governor

-------------------------

owocki | 2026-08-09 18:01:12 UTC | #2

i am supportive of this proposal, pending verification that the upgrade will go smoothly technically.  will dive into the scopelift validation tech.

-------------------------

bendi | 2026-08-17 19:46:51 UTC | #3

Ben from ScopeLift here. We've completed the deployment and simulation testing of the governance upgrade process. You can find the contracts in the repository [here](https://github.com/ScopeLift/gitcoin-gov-upgrades) and the deployment logs and simulations in [this pull request](https://github.com/ScopeLift/gitcoin-gov-upgrades/pull/8).

As you'll see if you dive in we have a suite of tests that exercise the full upgrade cycle, from proposal of the upgrade, votes, success/failure, execution, and subsequent governance proposals afterwards in the new system. These tests fork from mainnet and use real onchain state to ensure they represent what will happen in production.

The test suite is modular. It runs using the actual deploy script, and now that the contract has actually been deployed, it *also* runs using the real deployed bytecode of the upgraded governor. When the upgrade proposal is put onchain, we'll execute another version of the test suite that uses the actual bytes of the onchain upgrade proposal.

ScopeLift has executed governance deployments and upgrades for many DAOs, including Compound, ZKsync, PoolTogether, Radworks, and Gitcoin itself. We are confident this upgrade will function successfully and leave the DAO with a secure, functional governance system. 

Because ScopeLift now operates [Cactus](https://tally.xyz) (formerly Tally), we will also make sure the new Governor is reflected immediately by the client upon successful execution of the upgrade.

Thank you for trusting ScopeLift with this important work. We've been longtime collaborators with Gitcoin across its seasons. We look forward to continuing to work together in the future.

-------------------------

auryn | 2026-09-03 19:22:33 UTC | #4

Late replying here. But yes I'm generally supportive of this and have a great deal of respect for the scopelift team. Gitcoin will be in good hands on Cactus.

-------------------------
