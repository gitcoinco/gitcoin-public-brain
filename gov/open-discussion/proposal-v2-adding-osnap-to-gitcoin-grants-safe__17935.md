---
id: 17935
title: "[Proposal V2] Adding oSnap to Gitcoin Grants Safe"
slug: proposal-v2-adding-osnap-to-gitcoin-grants-safe
category: open-discussion
url: https://gov.gitcoin.co/t/proposal-v2-adding-osnap-to-gitcoin-grants-safe/17935
created_at: 2024-02-20T14:15:15.260Z
last_posted_at: 2024-03-18T11:37:35.023Z
posts_count: 12
views: 5018
like_count: 26
---

# [Proposal V2] Adding oSnap to Gitcoin Grants Safe

<https://gov.gitcoin.co/t/proposal-v2-adding-osnap-to-gitcoin-grants-safe/17935>
alexuma | 2024-02-20 14:29:05 UTC | #1

### Summary

We propose adding oSnap, a governance tool developed by UMA, to the Gitcoin Grants Matching Pool Safe to allow for automatic Safe Tx execution of grant distributions after successful Snapshot votes.

This is an amended proposal that incorporates feedback from the Gitcoin team and community. The original proposal can be found [here](https://snapshot.org/#/gitcoindao.eth/proposal/0xbba6d5e08ea0adb069fa2b1fcea02333e90b7c8cf387e31c0b77e61f4f29f5b8).

### Abstract

The current grant process relies on multi-sig signers of the Gitcoin Grants Matching Pool Safe to govern and manage funds because grant funds are in a Safe that is separate from the Gitcoin treasury. Adding oSnap enables GTC voting to govern how the funds are allocated from the Safe and removes the reliance on the multi-sig signers.

oSnap secures over $250M for treasuries including CoW Protocol, Across, Connext and Shapeshift. A dashboard of all oSnap users can be viewed [here](https://dune.com/risk_labs/osnap-total-value-secured). oSnap was built by UMA, an experienced leader in optimistic verification. UMA’s optimistic oracle currently secures $450M of TVS across bridges, prediction markets and governance tools.

### Motivation

Adding oSnap decentralizes the execution of grant decisions and empowers GTC holders by enabling tokenholders to govern how the Gitcoin Grants Matching Pool Safe funds are allocated. Due to Gitcoin grant funds being in a Safe and Gitcoin having an active Snapshot space, adding oSnap requires minimal effort and no disruption to existing DAO governance systems. On top of these benefits, oSnap is highly aligned with Gitcoin as it is a public good that increases decentralization.

### Specification

oSnap is a module that is added to a Safe with rules on how to evaluate a Snapshot proposal. oSnap Safe app lets you add oSnap to your Snapshot space and Safe in a few minutes with no developer time required. A video demonstration of the oSnap Safe App can be viewed [here](https://docs.uma.xyz/developers/osnap/osnap-quick-start).

Once enabled, Snapshot proposals related to the distribution of funds from Gitcoin’s Gitcoin Grants Matching Pool Safe can include transaction data with the proposal (details below). After a successful Snapshot vote, the transaction is proposed in Safe (put onchain) and verified by UMA’s optimistic oracle before being executed by the Safe. There will be no changes to the Gitcoin DAO treasury or proposals for treasury distributions or social votes relating to governance, removing a director, etc.

The updated Snapshot flow for proposals that include grant distributions would be:

* An oSnap enabled Snapshot proposal is created. This process is the same as a normal Snapshot proposal with the addition of transaction data that will be verified and executed if the proposal passes. The Snapshot transaction builder is specifically designed to make it easy to create and verify transaction data for token transfers.
* GTC holders vote on the proposal like any other Gitcoin Snapshot proposal
* If GTC holders approve the proposal by vote, any address can post a bond (2 WETH) for a challenge period (1 to 3 days) and propose to execute the transactions onchain. UMA has implemented a bot that validates proposals (vote passed, meets min voting period/quorum) and posts the bond for DAOs along with covering gas costs for execution (there are no fees to use oSnap).
* If no dispute arises about the proposal’s accuracy during the challenge period, the transactions can then be executed.
* In case of a dispute, the proposal is not executed. UMA token holders vote to resolve the dispute, with the correct party rewarded from the opposing party’s bond. This bonding and dispute mechanism punishes incorrect proposers and disputers and incentivizes honest disputes. Any proposal that was incorrectly disputed can be re-proposed to the oracle for execution without requiring revoting. It is important to note, the dispute resolution decided by UMA token holder votes are not deciding if the transactions can be executed or not, only the bond allocation between the proposer and disputer.

UMA created and maintains oSnap as a public good with no implementation or usage fees because we believe decentralized governance tools are critical to the entire Web3 ecosystem. Since UMA is already running robust monitoring across all of our optimistic oracle integrations and can recycle the bonds posted, the additional costs associated with these services are negligible and it is sustainable to continue providing this service for DAOs. If any changes were to be made in the future, we are committed to having existing DAOs not face any changes (aka be “grandfathered in”).

### Benefits

The benefits of Gitcoin adopting oSnap are:

* oSnap enables GTC voting to govern how Gitcoin Grants Matching Pool funds are allocated and remove the reliance on the Safe multi-sig signers (signers can still act as a fail safe, if needed).
* Transaction payloads included in proposals that are approved by voters are trustlessly and permissionlessly executed which increases transparency and decentralization.
* Automatic transaction execution by UMA bots is faster than waiting for multi-sig signers along with the bot paying the gas costs for execution. The gas cost of the transaction execution is paid for by these bots instead of the multi-sig signers.
* The UMA team is continuously making frontend improvements as per user feedback and improving open source monitoring infrastructure for oSnap.

UMA has also focused significant resources on monitoring efforts:

* The same bot that proposes and executes transactions also automatically disputes inaccurate proposals if the following criteria are not met:
  * The proposed onchain transactions match the transactions that were approved in the Snapshot proposal
  * The Snapshot proposal passed with the minimum parameters specified (majority in favor, meets minimum voting period and quorum)
  * The proposal follows the strategy specified in the Snapshot space.
* Proposals are included in the UMA Oracle UI (https://oracle.uma.xyz/) which is the same interface used by disputers verifying and disputing for other third-party integrations (Polymarket, Sherlock, Cozy, and other oSnap integrations).
* UMA sponsors a verification program, that pays UMA community members to verify all optimistic oracle assertions So when any transactions are proposed through oSnap, a Discord ticket is automatically created and an experienced verifier from the UMA community completes a multi-step verification process that focuses on areas such as the transaction payload matching the intent of the proposal, verifies transactions do not include interactions with malicious contracts, etc.

### Drawbacks

While we recognize UMA is new to Gitcoin, oSnap has been deployed without problems to other ecosystems. We are hoping to forge a stronger relationship with Gitcoin to overcome the unknown nature of the technology and team supporting it.

It is worth noting that automation tools like this are only as secure as the voting structure and votes themselves. Configuration of Snapshot now becomes an attack vector for those with the authority to make proposals where previously off chain proposals were still gated by the safe signers. We plan to work with Gitcoin to ensure the snapshot strategies are sound and configured properly for their implementation along with Gitcoin being comfortable with the steps to include transfers in Snapshot proposals.

Onchain bot proposed transactions may expose the treasury to funds being drained if there is an error in the mechanism or transaction payload approved on Snapshot. The waiting period, challenge period, and the bot proposing transactions directly from Snapshot help alleviate that risk, but it’s difficult to guarantee no such actions can ever occur.

While oSnap has been audited by Open Zeppelin, as with any system, there may be unforeseen vulnerabilities.

### Vote

For - Formalizes the community is “for” adding oSnap to the Gitcoin Grants Safe.
Against - Formalizes the community is “against” adding oSnap to the Gitcoin Grants Safe.

-------------------------

Sov | 2024-02-22 14:46:39 UTC | #2

Thanks for this post and the thought you put into lining out all aspects of the potential integration.

The major question I have is what the level of effort to deploy this integration is, and will the effort be something that the team at UMA will be taking on, or is the expectation that will be something Gitcoin takes on?

Knowing the different aspects related to planning and execution of this would help the community to make an informed decision.

Thanks again,

-------------------------

alexuma | 2024-02-22 22:23:13 UTC | #3

Hey @Sov! Thanks for the comment.

We created an oSnap Safe App that takes care of the deployment process and no contract changes are needed. We are happy to walk through the deployment process and answer any questions with the team before adding oSnap.

Here is a video walking through the deployment process in less than 2 minutes:
https://www.youtube.com/watch?v=tj_m6XMoPO4&embeds_referring_euri=https%3A%2F%2Fcdn.iframe.ly%2F&source_ve_path=OTY3MTQ&feature=emb_imp_woyt

-------------------------

CoachJonathan | 2024-03-05 12:53:00 UTC | #4

Hey everyone, just catching up on this now.

I am still supportive of this as I was last time. It sounds like this proposal has addressed some of the previous concerns that had the vote be a "no".

-------------------------

kyle | 2024-03-12 15:07:33 UTC | #5

I thought I had replied to this - it looks like I have just been answering questions in lots of Discord places and not on the forums here.

I am supportive of this proposal and I love the idea of moving more of our voting (especially for the grants matching pool!) to permissionless interactions. GTC was launched to govern the grants program and it now extends to governing the technology that was launched post-token. Adding this integration enables snapshot votes to move funds without the need for the SAFE signers to be involved. It's a huge win to bring that automation to the safe.

This also means, more power is accruing to GTC token holders in deciding how to allocate Gitcoin's Matching pool funds.

-------------------------

Sov | 2024-03-12 18:09:18 UTC | #6

Thanks for these replies!  I wanted to drop a quick question here and see if this integration would change or conflict with any of the existing tools we use, namely Tally and/or Snapshot?

-------------------------

alexuma | 2024-03-13 19:01:27 UTC | #7

Hey @Sov, great question.

Adding oSnap would not conflict with any of Gitcoin's existing tools:

* Snapshot: Adding Snapshot transactions to a proposal is optional and can be determined by selecting a checkbox when creating a Snapshot proposal. If left unselected, the proposal will act exactly how it does today.
* Safe: Your Safe will still have the option to execute transactions with the multi-sig signers and function the same as it did before integrating oSnap. You can think of oSnap as another option for onchain execution and it will not limit any of the existing functionality.
* Tally: From my understanding, Gitcoin uses Tally for onchain execution of Treasury distributions using a Governor contract. Adding oSnap to the Grants Safe will have no impact on the Governor contract or any of the onchain actions completed on Tally.

Let me know if you have any other questions or if any of the above responses need further clarification.

-------------------------

Viriya | 2024-03-13 19:48:32 UTC | #8

I'm in support of this proposal and I really appreciate @alexuma reworking and adjusting based on our questions and concerns. Thank you!

-------------------------

Sov | 2024-03-13 22:04:16 UTC | #9

Thanks for this!  Given these details, I am in support of this agreement as well!

-------------------------

meglister | 2024-03-14 12:30:17 UTC | #10

Thanks @CoachJonathan @kyle @alexuma for helping me understand the details of the proposal -- I am supportive of this

-------------------------

Saurabh | 2024-03-14 17:44:52 UTC | #11

I would like to support the proposal. Integrating oSnap by UMA into Gitcoin offers significant benefits for Gitcoin governance.

-------------------------

CoachJonathan | 2024-03-18 11:37:35 UTC | #12

This proposal has met the minimum threshold of Steward comments and has been posted to Snapshot: https://snapshot.org/#/gitcoindao.eth/proposal/0xa38c8a3507a848c2e4007b133cbe86ba30553a7a06d2bb266471b93756d1af17

-------------------------
