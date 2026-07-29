---
id: 17263
title: "[Proposal] Adding oSnap for Gitcoin treasury distributions"
slug: proposal-adding-osnap-for-gitcoin-treasury-distributions
category: open-discussion
url: https://gov.gitcoin.co/t/proposal-adding-osnap-for-gitcoin-treasury-distributions/17263
created_at: 2023-12-12T17:12:49.084Z
last_posted_at: 2024-01-19T18:30:54.640Z
posts_count: 14
views: 7373
like_count: 53
---

# [Proposal] Adding oSnap for Gitcoin treasury distributions

<https://gov.gitcoin.co/t/proposal-adding-osnap-for-gitcoin-treasury-distributions/17263>
alexuma | 2023-12-12 17:12:49 UTC | #1

### Summary

We propose adding oSnap, a governance tool developed by UMA, to the Gitcoin Snapshot space and Safe to allow for automatic onchain execution of token transfers and grant funding after successful Snapshot votes.

### Abstract

The current Gitcoin governance flow uses offchain Snapshot voting to approve or deny proposals. However, proposals that are approved must then be repeated onchain with Tally to achieve onchain execution. This repeated vote is an administrative task that wastes the time and gas fees of DAO participants. There have been instances where the revote on Tally did not achieve Quorum and the revote had to be posted again, wasting even more time and gas.

The adoption of oSnap eliminates the need for the redundant Tally revote by automatically executing successful Snapshot votes onchain, thus consolidating the governance process to one gasless vote on Snapshot that results in onchain execution.

oSnap secures over $250M for treasuries including CoW Protocol, Across, Connext and Shapeshift. A dashboard of all oSnap users can be viewed [here](https://dune.com/risk_labs/osnap-total-value-secured). oSnap was built by UMA, an experienced leader in optimistic verification. UMA’s optimistic oracle currently secures $450M of TVS across bridges, prediction markets and governance tools.

### Motivation

Adding oSnap aims to streamline the execution of governance decisions, bringing a new layer of efficiency and reliability to Gitcoin requiring minimal effort and no disruption to existing DAO governance systems. On top of these benefits, oSnap is highly aligned with Gitcoin as it is a public good that increases decentralization.

### Specification

oSnap is a module that is added to a Safe with rules on how to evaluate a Snapshot proposal. oSnap Safe app lets you add oSnap to your Snapshot space and Safe in a few minutes with no developer time required. A video demonstration of the oSnap Safe App can be viewed [here](https://docs.uma.xyz/developers/osnap/osnap-quick-start).

Once enabled, Snapshot proposals related to the distribution of funds from Gitcoin's treasury can include token transfers with the proposal. There will be no changes related to proposals not related to treasury distributions, such as social votes relating to governance, removing a director, etc.

The updated Snapshot flow for proposals that include treasury distributions would be:

* An oSnap enabled snapshot proposal is created. This process is the same as a normal Snapshot proposal with the addition of transaction data that will be verified and executed if the proposal passes. The Snapshot transaction builder is specifically designed to make it easy to create and verify transaction data for token transfers.
* GTC holders vote on the proposal like any other Gitcoin Snapshot proposal
* If GTC holders approve the proposal by vote, any address can post a bond (2 WETH) for a challenge period (1 to 3 days) and propose to execute the transactions onchain. UMA has implemented a bot that validates proposals (vote passed, meets min voting period/quorum) and posts the bond for DAOs along with covering gas costs for execution (there are no fees to use oSnap).

* If no dispute arises about the proposal’s accuracy during the challenge period, the transactions can then be executed.
* In case of a dispute, the proposal is not executed. UMA token holders vote to resolve the dispute, with the correct party rewarded from the opposing party’s bond. This bonding and dispute mechanism punishes incorrect proposers and disputers and incentivizes honest disputes. Any proposal that was incorrectly disputed can be re-proposed to the oracle for execution without requiring revoting. It is important to note, the dispute resolution decided by UMA token holder votes are not deciding if the transactions can be executed or not, only the bond allocation between the proposer and disputer.

UMA created and maintains oSnap as a public good with no implementation or usage fees because we believe decentralized governance tools are critical to the entire Web3 ecosystem. Since UMA is already running robust monitoring across all of our optimistic oracle integrations and can recycle the bonds posted, the additional costs associated with these services are negligible and it is sustainable to continue providing this service for DAOs. If any changes were to be made in the future, we are committed to having existing DAOs not face any changes (aka be “grandfathered in”).

### Benefits

The benefits of Gitcoin adopting oSnap are:

* Adding oSnap removes the unnecessary, administrative step of an onchain Tally vote when releasing funds from Gitcoin's treasury saving Gitcoin DAO voters time and gas fees.

* Transaction payloads included in proposals that are approved by voters are trustlessly and permissionlessly executed which increases transparency and decentralization.
* Automatic transaction execution by UMA bots is faster than waiting for multi-sig signers along with the bot paying the gas costs for execution.

* The UMA team is continuously making frontend improvements as per user feedback and improving open source monitoring infrastructure for oSnap.

UMA has also focused significant resources on monitoring efforts:

* The same bot that proposes and executes transactions also automatically disputes inaccurate proposals if the following criteria are not met:
  * The proposed onchain transactions match the transactions that were approved in the Snapshot proposal
  * The Snapshot proposal passed with the minimum parameters specified (majority in favor, meets minimum voting period and quorum)
  * The proposal follows the strategy specified in the Snapshot space.

* Proposals are included in the UMA Oracle UI (https://oracle.uma.xyz/) which is the same interface used by disputers verifying and disputing for other third-party integrations (Polymarket, Sherlock, Cozy, and other oSnap integrations).

* UMA sponsors a verification program, that pays UMA community members to verify all optimistic oracle assertions So when any transactions are proposed through oSnap, a Discord ticket is automatically created and an experienced verifier from the UMA community completes a multi-step verification process that focuses on areas such as the transaction payload matching the intent of the proposal, verifies transactions do not include interactions with malicious contracts, etc.

### Drawbacks

While oSnap has been audited by Open Zeppelin, as with any system, there may be unforeseen vulnerabilities.

### Vote

For - Formalizes the community is “for” adding oSnap to Gitcoin.
Against - Formalizes the community is “against” adding oSnap to Gitcoin.

-------------------------

CoachJonathan | 2023-12-15 08:32:05 UTC | #2

I want to express my support for this proposal.

I think the main benefit for me is eliminating the need of posting from Snapshot -> Tally. This is mostly an administrative procedure at this point, taking things we agreed to offchain, onchain. Adding in this functionality removes this step entirely, saves times and resources and attention.

Main potential drawback I see is the increased potential of governance attacks b/c of the reduced time for releasing funds. I see this risk being minimal and am confident we can put in the appropriate safeguards to manage this risk.

Would love to hear from some others to make sure I'm not missing anything in terms of benefits/drawbacks.

-------------------------

CryptoReuMD | 2023-12-15 19:32:21 UTC | #3

Yes please. We need more automatization and stronger decisions. 
Nice :smiley:

-------------------------

annika | 2023-12-15 22:48:16 UTC | #4

I'll express my directional support — I think the UMA team is exceptional: highly competent & professional, and certainly values-aligned with Gitcoin. I also think oSnap looks like a great product that makes sense for this use case.

I would want to see an analysis of benefits & drawbacks from those who are closer to the current Snapshot --> Tally flow and its challenges than I am, and also on any potential technical / governance attack risks here since those are blindspots from my perspective. 

If the main stakeholders overseeing those areas think it is a good idea, I would certainly vote with my support.

-------------------------

Saurabh | 2023-12-20 18:04:00 UTC | #5

I would like to support the proposal. Integrating oSnap by UMA into Gitcoin offers significant benefits for Gitcoin governance.

With oSnap's track record of securing over $250M and UMA's expertise in optimistic verification, the implementation is reliable and secure. Adopting oSnap streamlines governance, aligns with Gitcoin's commitment to decentralization, and brings transparency, efficiency, and reliability to decisions.

-------------------------

CryptoReuMD | 2023-12-20 18:36:50 UTC | #6

[quote="annika, post:4, topic:17263"]
I’ll express my directional support — I think the UMA team is exceptional: highly competent & professional, and certainly values-aligned with Gitcoin. I also think oSnap looks like a great product that makes sense for this use case.
[/quote]

Yup, Trust in Optimstic solutions =). Really nice work and oracles need to be part of any decentralized solution.

-------------------------

Willy | 2023-12-20 20:42:06 UTC | #7

My opinion on this mirrors @annika's. I'm a fan of oSnap and think it could be a great solution offering the best of both worlds: free, gasless voting plus permissionless execution that doesn't depend on a multisig. That said, I defer to more active stakeholders on whether it's the best solution for Gitcoin at this time. 

to quote Annika, "If the main stakeholders overseeing those areas think it is a good idea, I would certainly vote with my support." :handshake: 

Definitely appreciate Uma for building and maintaining this awesome public good and for making this proposal :purple_heart:

-------------------------

robioreefeco | 2023-12-21 01:19:24 UTC | #8

Hola Alex

I believe that reducing the redundant voting steps within Gitcoin's governance flow offers significant advantages. Integrating oSnap to eliminate the need for a second on-chain vote via Tally has the potential to save time, effort, and gas fees for participants. Simplifying the process could notably enhance decision-making efficiency within the Gitcoin DAO, representing a positive step forward.

**First:** The concept of automating the execution of successful Snapshot votes on-chain through oSnap is intriguing. It aligns seamlessly with the objective of fostering transparency and decentralization by executing approved transactions without multi-sig signers. Additionally, I commend UMA for its dedication to continuously improving the frontend, monitoring infrastructure, and verification procedures for oSnap. These efforts significantly contribute to a more reliable integration. However, I am mindful of the necessity for robust security measures. While the system has undergone audits, continuous assessment and improvement are imperative to effectively counter unforeseen vulnerabilities.

**Second:** Community engagement stands as a pivotal factor. A transparent decision-making process, inclusive of feedback, open discussions, and incorporation of community suggestions, will bolster the acceptance and effectiveness of the integration. Moreover, establishing clear contingency plans for disputes or vulnerabilities is crucial. Having well-defined protocols for dispute resolution and prompt mechanisms to address unforeseen issues will be vital for a resilient governance system. I referenced this in relation to the [Incident Regarding Mistransferred Treasury Funds](https://gov.gitcoin.co/t/incident-regarding-mistransferred-treasury-funds/16683) that occurred a few months ago.

**Third:** Considering the potential risks, a gradual implementation approach might be prudent. A phased or pilot phase would allow for identifying and rectifying potential issues before full-scale integration, mitigating risks associated with rapid deployment.

**Conclusion:** While I endorse the overarching aim of enhancing Gitcoin's governance through oSnap integration, I stress the importance of stringent security measures, community involvement, dispute resolution protocols, and a cautious implementation strategy. Therefore, I partially support the integration of oSnap into Gitcoin, contingent upon addressing the outlined considerations comprehensively.

Vote: **Against** ...

**Note**: We should propose the development of an AI tool for managing treasury distributions, with the potential to integrate it with [Gitcoin WalletGuard 🛡️](https://gov.gitcoin.co/t/gitcoin-walletguard/16772) for human verification in specific situations.

Would love to see your suggestions around this proposal:
@ccerv1 @meglister @Viriya @M0nkeyFl0wer @azeem @owocki @shawn16400 

🌊🐠✨

-------------------------

alexuma | 2023-12-21 23:22:16 UTC | #9

Hey [**robioreefeco**](https://gov.gitcoin.co/u/robioreefeco), thanks for the comment! Below are responses to provide more context but let me know if you have any additional questions or concerns.

**First:** The oSnap verification process is a combination of automated and manual validation. The open-source bot UMA and other third-party verifiers run use strict parameters to verify Snapshot proposals. UMA is continuously assessing and improving its verification system along with incorporating feedback from DAOs to improve the oSnap user experience. The manual verification team has biweekly meetings to discuss any questions or issues that arise.

UMA’s manual verification system reviews all oSnap transactions and serves a similar purpose to the Gitcoin WalletGuard. The Gitcoin WalletGuard could also add another layer of security to Gitcoin oSnap proposals. UMA has public bot scripts that can report oSnap transaction proposals to a terminal, Slack, or Discord. These notifications could be used to alert the Gitcoin WalletGuard to review any Gitcoin oSnap proposed transactions that are being verified by the oracle. 

 **Second:** oSnap takes a conservative approach to handling disputes. If any transaction is disputed during oracle verification, that proposal is deleted and can not be executed. The dispute is still resolved by UMA token holders, but this only decides how the proposer and disputer bonds are redistributed. oSnap disputes are straightforward to resolve and since the vote is not deciding if the transactions can be executed, there is little financial incentive for attempts to corrupt the oracle based on the allocation of a 2 WETH bond.

**Third:** We are happy to support Gitcoin in any way to ensure the DAO is comfortable with the implementation. oSnap is currently being used by large DAOs to secure their treasuries with the default implementation.

While a gradual implementation can potentially add complexity and administrative time, there are options for gradual implementations:

* A [guard module](https://medium.com/uma-project/building-on-safe-a-security-veto-for-osnap-daos-036392271032) enables the DAO to veto transactions or potentially add limits to transfer amounts that can be proposed through oSnap.
* Escalation managers would allow Gitcoin to whitelist addresses that can propose transactions (their Safe, UMA bot) and allow anyone to dispute.
* Setting the oracle dispute window higher to start (ie, 3-5 days) gives extra time for your DAO to do their own check on any proposed transactions on top of UMA’s verification system and decentralized disputers. Once comfortable, the liveness period can be decreased to a more typical length (1-3 days).

Let us know if you have any other questions or concerns and we look forward to more comments from the Gitcoin community!

-------------------------

Viriya | 2023-12-22 16:11:20 UTC | #10

Thanks for tagging me and bringing this to my attention @robioreefeco 

I'm going to abstain from commenting as my technical understanding in these matters is extremely limited. I will defer to people (probably @kyle) who understand the security implications of a decision like this. 

That said, it sounds like an awesome value prop (bringing more ease and speed to DAO governance? yes please!) and I would love to see it implemented if more qualified individuals are aligned :slight_smile:

-------------------------

Pradolo | 2023-12-24 18:56:21 UTC | #11

Hello, 

I believe this proposal may not transparently be notifying readers and potential voters on what this solution entails? I am happy to be wrong so please feel free to respond:

If Gitcoin is actually using OZ Governor for DAO execution currently via Tally then this proposal actually requests Gitcoin to reduce its autonomy and decentralisation, adding in multiple layers of trust. It in essence would no longer be a DAO. 

By using UMA with Snapshot and SAFE you add 3 layers of trust, from originally (0?) 
1. You must trust Snapshot a centralised offchain signalling platform on a server (best intended for signalling as it is not e2e verifiable). 
2. You must trust UMA token holders for all future Gitcoin disputes.
3. You must trust a group of multisig signers on a SAFE 

I know there are ways to remove the SAFE, however, this would then place the entirety of the organisations trust on a centralised product, Snapshot. Even though its an amazing product and team! 

I'm shocked to see no other "drawbacks" included in the information outlining these tradeoffs? Apologies if I get something wrong, please feel free to address these as discussion questions. 

This seems like a complete step backwords in being a true DAO. 

UMA seems like a wonderful tool for moving fast in a low stakes environment where you can use multiple layers of trust, not vote onchain with any e2e verifiability, etc. Not in a high-stakes environment where being a true DAO is essential to being resilient and unstoppable.

-------------------------

alexuma | 2024-01-09 23:13:15 UTC | #12

Hi Pradolo, thanks for the comments. I’ll start by responding to your numbered points:

1 - Yes, oSnap is dependent on Snapshot to signal the approval of a DAO vote. However, the existing governance process also relies on Snapshot to signal approval as well. As per the “Moving to Vote” section of the [Gitcoin DAO Governance Process v3](https://gov.gitcoin.co/t/gitcoin-dao-governance-process-v3/10358), after a vote is approved on Snapshot, “No one person should ever vote NO on Tally as all proposals that make it on Tally are classed as passed”. So whether the execution of a Snapshot approved vote is executed through oSnap (as proposed), or through an onchain Tally vote (current system), both systems rely on Snapshot correctly signaling the DAO’s approval.

In the edge case where Snapshot is misreporting vote results, the current system would rely on DAO members to realize this and vote ‘No’ on Tally against the usual governance flow. With oSnap, proposed transactions based on misreported vote results would require only one disputer to block transaction execution. As described in the Specifications section above, UMA token holders would then vote to redistribute the proposer’s and disputer’s bond.

2 - oSnap does rely on there being one honest disputer to dispute invalid proposals. Disputing is public and permissionless. Disputes do not require holding any UMA, but do require posting a bond in WETH or USDC. UMA runs bots that dispute invalid proposals and also sponsors a verification program as described in the above proposal. Gitcoin DAO members are welcome to add another layer of protection by monitoring their proposals and disputing invalid proposals (if they are fast enough!). This can be done using the Oracle UI or running a UMA developed monitoring bot.

UMA token holders only vote if there is a dispute on a transaction batch proposed to the oracle for execution. As soon as a proposed transaction batch is disputed, that proposal can no longer be executed no matter how UMA token holders vote to resolve it. The token holder vote only resolves the bonds posted by the proposer and disputer. Dishonest parties lose their bond and honest parties get a portion of the other’s bond. If a valid proposal is disputed, a new transaction proposal can be created using the same Snapshot proposal results. So the dishonest disputer would be continually losing bonds to block a valid proposal. If there is a dishonest proposer who continually submits dishonest proposals, it would be extremely costly as they would be continually losing their bond.

3 - As you mentioned, the multi-sig can be removed from an oSnap enabled Safe. Considering Gitcoin doesn’t have a Safe or multi-sig signers, we propose adding a new Safe with an oSnap module and then incorporating the existing Gitcoin Governor as a module on the Safe. This enables the existing governance system to serve as a fallback and would prevent Gitcoin from needing to add multi-sig signers or introduce centralization into the Gitcoin governance process.

The proposed implementation accomplishes the main goal of removing redundancy in the voting process (voting on both Snapshot and Tally) with no commitment required to be made until a Tally proposal is created for migrating funds to the Safe. This enables a test oSnap proposal and other testing to be completed before migrating funds.

For Tally to serve as an emergency option, it would require an 'exec call' within the safe contract. While we expect Gitcoin to not need this fallback, it's important to be transparent about the tradeoff. The other additional complexity, as mentioned above, is assets Gitcoin controls with Snapshot and oSnap would need to be migrated to the Safe.

**Proposed Integration Steps:**

**Setup:**

* UMA: Deploy a Safe
* UMA: Add oSnap module to Safe
* UMA: Add existing Gitcoin Governor as a module on Safe
* UMA: Remove all signers from Safe
* Gitcoin: Add the “oSnap by UMA” plugin to Gitcoin’s Snapshot space
Note: all UMA steps above could alternatively be completed by Gitcoin with support from UMA.

**Testing:**
* Gitcoin (optional): Complete test Snapshot proposal with oSnap

**Execution:**

* UMA: Create a Tally proposal for migrating agreed upon amount to Safe

Please let us know if there are additional questions on oSnap or the proposed implementation.

-------------------------

kyle | 2024-01-19 14:23:01 UTC | #13

Thanks for the details here. I have been playing catch up a bit on the conversation and the value proposition.

I heard a rumor that oSnap may soon integrate with Tally, and we could skip the Safe requirement... is that right?

Given the complexity of the integration (having to add oSnap, having to create a new gnosis safe with governor access, etc.) I would likely vote no on this proposal. 

Gitcoin is often very conservative in our approach of new technology related to the treasury and governance (flexible voting being a notable exception, but we have not configured any flexible voting strategies yet).

This seems very powerful for many DAOs that dont rely on governor bravo, and I am excited to hear you all may be working to remove the requirement to have a Safe integrated as well.

-------------------------

CoachJonathan | 2024-01-19 18:30:54 UTC | #14

Hi everyone, the vote is now live on Snapshot here: https://snapshot.org/#/gitcoindao.eth/proposal/0xbba6d5e08ea0adb069fa2b1fcea02333e90b7c8cf387e31c0b77e61f4f29f5b8 and will be live for 7 days.

-------------------------
