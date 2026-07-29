---
id: 18620
title: "[Discussion] Addressing immediate gaps in DAO governance"
slug: discussion-addressing-immediate-gaps-in-dao-governance
category: governancevision
url: https://gov.gitcoin.co/t/discussion-addressing-immediate-gaps-in-dao-governance/18620
created_at: 2024-04-17T09:33:48.573Z
last_posted_at: 2024-05-27T18:00:04.692Z
posts_count: 18
views: 7156
like_count: 27
---

# [Discussion] Addressing immediate gaps in DAO governance

<https://gov.gitcoin.co/t/discussion-addressing-immediate-gaps-in-dao-governance/18620>
jengajojo | 2024-04-17 09:33:48 UTC | #1

# Summary

Upgrade governance processes at Gitcoin DAO by fixing governance gaps and creating a DAO constitution.

# Motivation

Today, governance in the DAO works as following:

* Proposers take guidance from the governance manual
* In most cases the manual provides guidance for what the proposer wants to achieve
* In some cases (eg [1](https://snapshot.org/#/gitcoindao.eth/proposal/0xb2094445891a515a6c58d8b44c4c2428e66d2e5f1f1e81a2741036eb97e6d6e8),[2](https://snapshot.org/#/gitcoindao.eth/proposal/0xd43f0a882b581e41bea6c0b162f2eab3b425a8cea5cbfa6da65e11a21ce364be)) there the proposal does not clearly fall into a given category so its combined into governance proposals

This creates confusion and a lack of standardization when it comes to following procedure, documenting changes and following an iterative development process for evolving governance.

# Specification

As part of [DAOplomats engagement with Gitcoin](https://gov.gitcoin.co/t/empowering-gitcoins-governance-gitcoin-x-daoplomats/18615) we have analyzed key aspects of the DAO's governance and here are our suggestions. 

**1. Differentiate between proposals based on how they are enforced.**

Currently there are 4 types of proposals: funding, ratification, governance and reallocation and no difference between regular proposals and community proposals. However there is some overlap between the four categories and some proposals which do not fall in any of the other three categories are posted as governance proposals by default.

In order to provide a clear distinction as well as guidelines for future proposers the following changes are suggested.

Implement two master categories: Onchain and Offchain and two sub categories for each. The proposer can follow this flowchart to identify which type of proposal they are making irrespective of where they lie in the ecosystem orbit

![Screenshot 2024-04-10 at 15.32.02|690x220](upload://oM4JgVDltjYv32CTDlxmmyWt9Qq.png)

### Definations

| Offchain | Offchain | Onchain | Onchain |
|--------|-------|-------|-------|
| **Social** | **Legal** | **Admin** | **Token** |
| Agreements enforceable by peer pressure which do not require changes to any contracts. | Agreements enforced by the legal system and which involve updating the legal setup | Agreements enforced by the blockchain which involves Making changes onchain without changing token balance | Agreements enforced by the blockchain which requires changing token balance|

Examples:

|Social|Legal|Admin|Token|
| --- | --- | --- | --- |
| Establishing/modifying DAO cadence|Electing/removing foundation director|Updating governor contracts|Sending/receiving/depositing/withdrawing/staking/lending/borrowing tokens|
| Modifying essential intents | Establishing/disbanding legal entities such as Grant Lab | Forming/disbanding multi-sigs |  |
| Modifying/electing council members (CSDO/Grants council) | Dissolving the foundation | Adding/removing members to any multi-sig |  |
| Modifying program or product policies |  | Delegating tokens |  |
| Adding/removing partners |  | Adding/removing Hats to a member or a multi-sig | |
| Establishing/modifying constitution |  |  |  |
| Changing Governance policies, tooling or other mechanics |  |  |  |




Based on what a proposal finally aims to achieve, the proposer can decide on a category and subcategory and proceed with the governance flow. The forum categories can be modified to reflect these changes.

**2. Create a DAO constitution**

In order to solidify the core principles of the DAO, a constitution which captures high level goals of the DAO should be created. This document should be rarely modified and should require significant consensus to be established and modified.

**3. Implement a minimum threshold for Steward approval based on proposal type**

In order to receive a higher quality signal from token holders and avoid spam, it is suggested that stewards should have a higher skin in the game for each consecutive change. Here is the minimum suggested threshold based on proposal types

|Type|Social|Legal|Admin|Token|
| --- | --- | --- | --- | --- |
|Minimum Voting Weight|1|10|100|1000|

**4. Improved proposal labelling**

Based on which stage a proposal is in its life cycle, it is primarily the responsibility of the author to label the proposals as follows:

* Initiating proposals as drafts for community feedback, marked as [DRAFT].
* A “temperature check” phase to gauge community sentiment, indicated as [TEMP CHECK].
* Finalising the proposal for voting, labelled as [READY]
* After the final vote has concluded, labelled as [PASSED/FAILED]

**5. Updating manual**

1. Updating the DAO Structure: The governance manual currently does not include recent changes such as Ecosystem collective and other entities in the DAO orbit such as grants lab, passport, RPP etc.. It is suggested that the manual be updated to reflect these changes. This also includes removing older unexisting structure such as Workstreams

2. Recategorise and organise governance roles from various types to three main types: Multi-sig signer, Pod Member and Governooor. Each of these categories can then include subcatgories to signal specific subroles such as matching pool guardian or CSDO member as MS signer. WS lead, Ecosystem contributor, core contributor as a pod member. Steward, delegator and governance coordinator as governooor.

3. Delegate the responsibility for updating the manual to the governance coordinator: Since the manual only reflects changes made by gitcoin governance, updating it should not require a DAO vote.

# Next Steps:

* Collect feedback from the community
* Submit a formal proposal

-------------------------

deltajuliet | 2024-04-17 11:36:06 UTC | #2

Sweet, thanks for this @jengajojo! Would love some clarification around a couple of things...

> we have analyzed key aspects of the DAO’s governance and here are our suggestions.

Does this include community feedback or simply a DAOplomats audit?

> Based on what a proposal finally aims to achieve, the proposer can decide on a category and subcategory and proceed with the governance flow. The forum categories can be modified to reflect these changes.

These definitions & examples are great but look less tailored to Gitcoin as an org. Are these standard examples or are you suggesting that we create some of these policies for the org? 

> Create a DAO constitution

Is this different to our process [outlined here](https://gov.gitcoin.co/t/gitcoin-dao-governance-process-v3/10358) by simply a different name? This is also taking into consideration your notes on the DAO manual below (removing/updating the structure) which currently lives in Gitbook. 

> Recategorise and organise governance roles from various types to three main types
-  Governooor: Hard pass on this naming. 
- Also worth noting there is no formal CSDO anymore. 
- How does this tie into the [defining community work](https://gov.gitcoin.co/t/defining-community-at-gitcoin-part-1-creating-shared-mental-models/18341/3) that @CoachJonathan is doing? 

In general I'm supportive of initiatives that improve our governance, including this one, but what I'm not seeing are the expected outcomes of this work or over-arching goals for these improvements. Would love to see those laid out!

-------------------------

jengajojo | 2024-04-17 12:39:53 UTC | #3

This post is aimed at starting a discussion on the suggested changes and based on community input we will come back with an actual proposal.

[quote="deltajuliet, post:2, topic:18620"]
Are these standard examples or are you suggesting that we create some of these policies for the org?
[/quote]
The suggestion is to create these policies to replace the existing ones.

The goal of the constitution is to capture high level consensus within the org. Currently these are documented as 'North Stars' in the gov manual. Here are some examples [[1](https://gov.optimism.io/t/working-constitution-of-the-optimism-collective/55),[2](https://docs.ens.domains/dao/constitution)] which may help you understand the desired output

These suggestions are intended to make it easier for 
- future proposers to identify which domain of governance they want to access 
- for admins to manage the forum efficiently 
- make stewards more accountable to their role. 

This builds on some of the work which was started here [1](https://gov.gitcoin.co/t/what-should-stewards-vote-on/17167/4) [2](https://gov.gitcoin.co/t/governance-roadmap-s19-20-beyond/16645/15)

-------------------------

CoachJonathan | 2024-04-25 16:19:07 UTC | #4

Thanks @jengajojo for getting the ball rolling on some of these initiatives. Though conversations like these might seem mundane and unnecessary, I truly believe that they are critical aspects of Gitcoin's legitimacy as a DAO and important pieces on Gitcoin's path to decentralization.

Additionally, I believe that more thorough documentation & closed loopholes = more robust governance, which starts a network effect that leads to more legitimate governance.
![Governance Flywheel|500x500](upload://q0KG6tag0iLffLbRTMdW1QLio7S.png)

## My thoughts on some of the proposals

[quote="jengajojo, post:1, topic:18620"]
1. Differentiate between proposals based on how they are enforced.
[/quote]

I am a big fan of this thinking and this is the easiest aspect for me to say "yes" to. In terms of the examples just below, I think there is a bit of finessing we can do to capture real examples of what Gitcoin tokenholders should be voting on. 

When I read examples of voting on modifying the cadence, changing governance tooling, foundation director elections, and multisig actions, I tend to agree. When I read other things like product policies and adding/removing partners, I am less in agreement. 

I appreciate that these are all just examples to get the ball rolling. @jengajojo where is the best place to capture the full extent of these examples - here in the governance forum or in some sort of working doc? I'd love to tease out these examples and create clear guidelines as to what does/doesn't need to be voted on + what category it fits into.



[quote="jengajojo, post:1, topic:18620"]
2. Create a DAO constitution
[/quote]

When I initially thought of a constitution, I think of examples like [Working Constitution of the Optimism Collective](https://gov.optimism.io/t/working-constitution-of-the-optimism-collective/55) and ENS' constitutions. These focus more on token holder rights and is a foundational document that any governance system would have.

When I think of the [Gov v3 post](https://gov.gitcoin.co/t/gitcoin-dao-governance-process-v3/10358), I see this as part constitution, part incomplete and hard to read governance manual. 

I am not overly concerned with the direction we head, though I would like to see us double down on the Governance Manual since this is the most comprehensive and clear document we have relating to governance (and has a decent UI compared to a long, drawn-out document). 




[quote="jengajojo, post:1, topic:18620"]
**3. Implement a minimum threshold for Steward approval based on proposal type**
[/quote]

This seems fine and safe to try.


[quote="jengajojo, post:1, topic:18620"]
**4. Improved proposal labelling**
[/quote]

Very supportive of creating some standards like this. Whether these are the final words, I don't have a strong opinion, though the flow seems right.


[quote="jengajojo, post:1, topic:18620"]
**5. Updating manual**
[/quote]


[quote="jengajojo, post:1, topic:18620"]
Updating the DAO Structure: The governance manual currently does not include recent changes such as Ecosystem collective and other entities in the DAO orbit such as grants lab, passport, RPP etc… It is suggested that the manual be updated to reflect these changes. This also includes removing older unexisting structure such as Workstreams
[/quote]

Sounds good to me.


[quote="jengajojo, post:1, topic:18620"]
Recategorise and organise governance roles from various types to three main types: Multi-sig signer, Pod Member and Governooor. Each of these categories can then include subcatgories to signal specific subroles such as matching pool guardian or CSDO member as MS signer. WS lead, Ecosystem contributor, core contributor as a pod member. Steward, delegator and governance coordinator as governooor.
[/quote]

To @deltajuliet's point, not aligned to governooor language (let's use something more clear here). @jengajojo who did you envision were "Pod Members"? I'm not clear on who these people are.

And to @deltajuliet's point about CSDO - this is another out-of-date aspect of the governance manual since this group no longer exists, and I'm happy to work with you to make sure that this gets accurately updated.
[quote="jengajojo, post:1, topic:18620"]
Delegate the responsibility for updating the manual to the governance coordinator: Since the manual only reflects changes made by gitcoin governance, updating it should not require a DAO vote.
[/quote]

This works for me. To be clear, right now I am responsible for doing these updates, and I would like to see this responsibility moved to or shared with the DAOplomats team.

<hr>

I am mostly aligned to the suggestions above minus 1 or 2 things. Thanks for getting the ball rolling on these items!

-------------------------

jengajojo | 2024-04-26 07:23:12 UTC | #5

Thanks for the feedback and support @CoachJonathan 

[quote="CoachJonathan, post:4, topic:18620"]
where is the best place to capture the full extent of these examples
[/quote]
If there won't be much contention about this then a reply to this forum post will be sufficient, however if you think this will result in a long discussion, we can move this to a working doc.

[quote="CoachJonathan, post:4, topic:18620"]
who did you envision were “Pod Members”?
[/quote]

Refering to these posts on pods, https://gov.gitcoin.co/t/introducing-gitcoin-s-ecosystem-collective/17954 if we were to adopt the 'Pod structure' DAOwide, then we can have separate pods for each group and have 3 master categories for overall roles in the DAO as mentioned earlier and several sub-categories inside the Pod category.

Happy to change the Governoor suggestion to anything else the community feels makes sense.

-------------------------

Viriya | 2024-04-30 14:58:44 UTC | #6

I think reducing friction in governance with these proposed changes make sense and I appreciate the thinking being done by @CoachJonathan and @jengajojo here. Posts like these won't garner much interest and feedback here, even though they are fundamental to how our DAO ultimately operates. 

I'm aligned to the call outs by Jonathan and trust that, as a lead at EC, he is doing the due diligence to help steward this proposal in a way that makes sense for us. 

I think overall, if we can update/repurpose docs/tools that currently exist vs. creating net new things, that would be my preference!

-------------------------

Decentralizedceo | 2024-05-09 08:02:01 UTC | #7

Thank you for this @jengajojo This was very well thought out and would love to see it implemented further down the line. 
I do have a question about this: 
[quote="jengajojo, post:1, topic:18620"]
|Type|Social|Legal|Admin|Token|
| --- | --- | --- | --- | --- |
|Minimum Voting Weight|1|10|100|1000|
[/quote]

Would this not break down the votes into tiers and some may not have a voice in certain matters? Unless that is the actual intention. Please elaborate if possible.

-------------------------

Decentralizedceo | 2024-05-09 08:03:35 UTC | #8

Well said!! With @jengajojo and @CoachJonathan reasoning towards a DAO structure, we are in good hands.

-------------------------

jengajojo | 2024-05-09 11:57:07 UTC | #9

Thank you for the feedback @Decentralizedceo  The intention here is to get approval from stewards who have more skin in the game as the consequences of each tier can significantly alter the state of the DAO. Irrespective of their voting weight all stewards are free to comment and express their opinions on all matters.

-------------------------

Sov | 2024-05-09 12:38:39 UTC | #10

Thanks for this.  

Directionally, I agree with what is outlined, but I have a few questions I would ask for clarity:

* How will the Gitcoin decide what goes in the DAO constitution versus the governance manual?
* Are there any specific examples of how proposals would be differentiated by enforcement type? 
* How will the minimum approval threshold be determined?

-------------------------

jengajojo | 2024-05-09 13:04:30 UTC | #11

Thanks for the feedback and the questions.

- The suggestion here is that: High level things about Gitcoin which are not going to change regularly shall be part of the constitution, however more operational aspects which evolve regularly shall be part of the manual. If the DAO approves going in the direction of forming a constitution, then we shall post a DRAFT first to collect feedback before we proceed to making a final proposal.

-  Here are a few examples of each category:

**Social**
https://gov.gitcoin.co/t/gg20-eligibility-criteria-community-rounds/17846
https://gov.gitcoin.co/t/proposal-amendments-to-the-steward-council/15118
https://gov.gitcoin.co/t/gcp-003-passed-post-vote-reconsider-process/13165
**Legal**
https://gov.gitcoin.co/t/proposal-the-gitcoin-foundation-a-proposal-to-represent-the-gitcoin-dao-irl-by-a-cayman-islands-foundation/9983

**Admin**
https://gov.gitcoin.co/t/proposal-v2-adding-osnap-to-gitcoin-grants-safe/17935
https://gov.gitcoin.co/t/proposal-updated-and-new-lower-gtc-voting-thresholds-on-and-off-chain/17410
https://gov.gitcoin.co/t/gcp-009-upgrading-gitcoin-s-governance-contracts/14010
**Token**
https://gov.gitcoin.co/t/passed-budget-request-for-the-gitcoin-ethcc-activation/18451
https://gov.gitcoin.co/t/ecosystem-collective-s21-22-budget-proposal/18240
https://gov.gitcoin.co/t/gcp-011-support-the-funding-the-commons-hackathon-residency-and-conference-series/14904

- I have posted a suggestion for the minimum approval. If there are no comments against it, then it will be proposed as it is. However, if the community wants to discuss it further we can setup a offchain vote to determine these thresholds.

-------------------------

Sov | 2024-05-09 13:34:46 UTC | #12

Great, thanks for the explanation.  LFG.

-------------------------

CoachJonathan | 2024-05-15 14:19:28 UTC | #13

I think that we are almost there with these suggestions. There are two items I want to address in this comment:

1. Category examples
2. Gitcoin constitution

## Category Examples

Based on the initial draft the @jengajojo created, I want to offer some amendments to the tables:

|Offchain|Offchain|Onchain|Onchain|
| --- | --- | --- | --- |
|**Social**|**Legal**|**Admin**|**Token**|
|Agreements enforceable by a social contract which do not require changes to any contracts|Agreements enforced by the legal system and which involve updating the legal setup|Agreements enforced by the blockchain which involves making changes onchain without changing a token balance|Agreements enforced by the blockchain which requires changing a token balance|

Examples:

|Social|Legal|Admin|Token|
| --- | --- | --- | --- |
|Establishing/modifying DAO cadence|Electing/removing foundation director|Updating governor contracts|Sending/receiving/depositing/withdrawing/staking/lending/borrowing tokens|
|Ratifying DAO-wide goals|Establishing/disbanding legal entities such as Grant Lab|Forming/disbanding multi-sigs||
|Modifying/electing council members ~~(CSDO/Grants council)~~(ex: GG Community Council)|Dissolving the foundation|Adding/removing members to any multi-sig||
|~~Modifying program or product policies~~||Delegating tokens||
|~~Adding/removing partners~~||Adding/removing Hats to a member or a multi-sig||
|Establishing/modifying constitution||||
|Changing Governance policies, tooling or other mechanics|||

Changes:
* Removed:
     * Modifying program or product policies
     * Adding/removing partners
* Changed:
     * From: Modifying Essential Intents, To: Ratifying DAO-wide goals

## Gitcoin Constitution

I'm not 100% sure on what the next step is here.
[quote="Sov, post:10, topic:18620"]
How will the Gitcoin decide what goes in the DAO constitution versus the governance manual?
[/quote]

I'm also still not 100% clear on this, though it seems like the gist is "things that will change 'often' go in the manual and things that 'stay the same' go in the constitution". I'd love to codify this more concretely so that we're clear on what goes where.

I am also not clear if there is still a plan to maintain posts like the [Governance v2](https://gov.gitcoin.co/t/gitcoin-dao-governance-process-v2-updated/7860) and [Governance v3](https://gov.gitcoin.co/t/gitcoin-dao-governance-process-v3/10358) post with a follow-up Governance v4 post. As I indicated in my original comment above, my vote is no since these posts are long, confusing and filled with gaps.

-------------------------

Viriya | 2024-05-15 18:29:42 UTC | #14

Thanks for this @CoachJonathan 

[quote="CoachJonathan, post:13, topic:18620"]
I am also not clear if there is still a plan to maintain posts like the [Governance v2 ](https://gov.gitcoin.co/t/gitcoin-dao-governance-process-v2-updated/7860) and [Governance v3](https://gov.gitcoin.co/t/gitcoin-dao-governance-process-v3/10358) post with a follow-up Governance v4 post. As I indicated in my original comment above, my vote is no since these posts are long, confusing and filled with gaps.
[/quote]

I would say "no" to this as well. There should be a pinned post to easily access the manual though. I would also suggest that when things change (via proposals voted on) the conclusion of each post would state that this is now reflected either in the manual or constitution.


[quote="CoachJonathan, post:13, topic:18620"]
I’m also still not 100% clear on this, though it seems like the gist is “things that will change ‘often’ go in the manual and things that ‘stay the same’ go in the constitution”. I’d love to codify this more concretely so that we’re clear on what goes where.
[/quote]

Please do! I don't think that blocker directly affects this proposal, does it?

-------------------------

jengajojo | 2024-05-16 08:57:24 UTC | #15

Thanks for the feedback @CoachJonathan & @Viriya. 

[quote="CoachJonathan, post:13, topic:18620"]
Changes:

* Removed:
  * Modifying program or product policies
  * Adding/removing partners
* Changed:
  * From: Modifying Essential Intents, To: Ratifying DAO-wide goals
[/quote]
I agree with the above changes.

To clarify the topic further:

**Constitution**:

A constitution typically refers to a fundamental set of principles or established precedents that govern an organization or a state. It often outlines the structure, functions, and powers of the various entities within the organization. Constitutions are usually formal documents, sometimes legally binding, and are often difficult to change. They often embody the core values and principles upon which the entity is founded and serve as the supreme law of that organization. Now in the context of DAOs, smart contracts are ideally the supreme way to govern, however, as an industry, we are not at a place yet where we can codify everything hence the closest we can get to having something enforced is to have it legally binding. Since there is no precedent here, individuals or orgs can use this document (Constitution) to fight for their rights in a court of law and it is ultimately for that court to decide the course of action. 

**Governance Manual**:

A governance handbook/manual, on the other hand, is more practical and operational in nature.It provides detailed guidelines, procedures, and best practices for governing the organization effectively. Unlike a constitution, a governance manual is typically more flexible and subject to periodic updates and revisions. It may cover a wide range of topics including decision-making processes, roles and responsibilities of stakeholders, codes of conduct, financial management protocols, and risk management strategies. The document serves as a manual or reference guide for those involved in the day-to-day operations and decision-making processes of the organization.

In summary, while both documents aim to establish a framework for governance, a constitution focuses on fundamental principles and structures, often with enforcement mechanisms, while a governance handbook/manual provides practical guidance for implementing those principles & managing the organization efficiently.

[quote="Viriya, post:14, topic:18620"]
I would also suggest that when things change (via proposals voted on) the conclusion of each post would state that this is now reflected either in the manual or constitution.
[/quote]
In this context, changing the constitution can involve its own sub-category under legal proposals where in the main goal of the proposal is to exclusively modify the constitution. Whereas, any other proposal can indirectly affect governance procedures and the manual can be updated to reflect that change. As an example:

The purpose of Gitcoin today is 'to empower communities to fund their shared needs.' Now if someone wants to change this mission, they have to put a proposal to exclusively change this mission, the proposal cannot have any other agenda. Vs. changing from a seasonal cadence to a quarterly one does not fundamentally alter the principles or structures but helps in managing the org efficiently, hence this can be included in the manual and does not necessarily need its own proposal.

-------------------------

CoachJonathan | 2024-05-19 08:33:51 UTC | #16

Based on the conversation so far, I think what is missing for me is a more clear example of what is actually going to go into the constitution.

[quote="jengajojo, post:1, topic:18620"]
**2. Create a DAO constitution**

In order to solidify the core principles of the DAO, a constitution which captures high level goals of the DAO should be created. This document should be rarely modified and should require significant consensus to be established and modified.
[/quote]

Maybe for the sake of moving this convo forward, let's make the word more clear that we'll "explore the development of a constitution".

This way as we move forward, we have flexibility to decide on the best path for us in a separate convo.

-------------------------

jengajojo | 2024-05-27 13:08:33 UTC | #17

Thank you for the feedback everyone. Please check out the [proposal](https://gov.gitcoin.co/t/proposal-streamlining-governance-processes/18873) post for next steps

-------------------------

mars | 2024-05-27 18:00:04 UTC | #18

[quote="jengajojo, post:11, topic:18620"]
**Legal**

https://gov.gitcoin.co/t/proposal-the-gitcoin-foundation-a-proposal-to-represent-the-gitcoin-dao-irl-by-a-cayman-islands-foundation/9983/35
[/quote]

### That was July 2022:

[quote="kyle, post:35, topic:9983, full:true"]
Hey all - I want to close the loop that this has now successfully closed! :partying_face: This means, the DAO now formally owns a vast number of gitcoin assets, and we are continuing to unplug from Gitcoin Holdings (whom is now rebranding as the Web3 Events company).

There are no immediate impacts for the DAO, but now that assets, the brand name, and other items are transferred, it means we can start to formalize the relationship between the DAO contributors and the newly created operating company within the foundation.

Thank you all so much for the support and enabling the DAO to move forward. This is a huge step for us, and for other DAOs who are looking to us for guidance on how to navigate the real world legal entity status for DAOs.
[/quote]

I'm genuinely curious what is the current legal status of Gitcoin / DAO / various related entities?

Related resource: https://ecosystem.gitcoin.co/ *(so many members of the ecosystem)*

Asking because if there is some existing legal structure IRL it means law / rules / compliance / regulation / accounting / annual reports / etc... And not everything that is on-chain is compatible with IRL.

-------------------------
