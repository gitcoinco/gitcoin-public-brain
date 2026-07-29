---
id: 10340
title: "IRP Research for Gitcoin"
slug: irp-research-for-gitcoin
category: governancevision
url: https://gov.gitcoin.co/t/irp-research-for-gitcoin/10340
created_at: 2022-04-11T15:05:17.206Z
last_posted_at: 2022-04-11T15:05:17.294Z
posts_count: 1
views: 2433
like_count: 0
---

# IRP Research for Gitcoin

<https://gov.gitcoin.co/t/irp-research-for-gitcoin/10340>
Layn | 2022-04-11 15:05:17 UTC | #1

Hello guys,

After @David_Dyor  comment in the [DAO Design Best Practices](https://gov.gitcoin.co/t/dao-design-best-practices/10219) thread, I decided to investigate a little bit more about Incident Response Plan (IRP), to see if it may be interesting for Gitcoin.

My conclusion is that it makes more sense for protocols where smart contracts keep some assets. The best example that I found is from MakerDAO, they call it [Emergency Shutdown](https://docs.makerdao.com/smart-contract-modules/shutdown), which actually is the only one that I found with a clear and well documented IRP.

If I understood properly, Gitcoin doesn't have any protocol that works automatically and has the risk to be exploited. Only one scenario comes to my mind where we could need an IRP for a non-propotol DAO, and also it depends on the kind of DAO's governance (mostly those where 1 token = 1 vote). Which is a person or group of people who get a majority or enough votes to propose and approve an initiative that goes against the DAO mission. Could I, with enough tokens, vote something that hurts the DAO but benefits me?

I checked how the governance works in Gitcoin, and it's not yet clear to me if anyone could make a proposal or proposal should comes always from workstreams. Could a workstream, or individual with enough votes propose to fund a non-open-source project? It doesn't benefit me (at least directly or to your knowledge).

I found an entry in the thread [Gitcoin DAO Governance Process v2 - updated](https://gov.gitcoin.co/t/gitcoin-dao-governance-process-v2-updated/7860)  addressing this concern:

![image|690x180](upload://ic8bXY77bOWbZsDvFAIgcP6rat2.png)


But is very vague and subject to interpretation, or not addressing all possible scenarios (I may not look for benefiting myself, but just to hurt the DAO...) I would expand that point, protecting the DAO for anything that doesn't align with our mission (whitelisting instead of blacklisting). So anything that is not clear on behalf of the public goods, is not allowed, not even to propose. 

Do we have anybody with a laws background/experience who could redefine this point, making more clear what can be proposed/voted?

-------------------------
