---
id: 16808
title: "[Proposal] Process/Procedure for Handling Funds"
slug: proposal-process-procedure-for-handling-funds
category: governancevision
url: https://gov.gitcoin.co/t/proposal-process-procedure-for-handling-funds/16808
created_at: 2023-10-19T15:06:11.965Z
last_posted_at: 2023-10-21T05:16:39.487Z
posts_count: 2
views: 4020
like_count: 5
---

# [Proposal] Process/Procedure for Handling Funds

<https://gov.gitcoin.co/t/proposal-process-procedure-for-handling-funds/16808>
CoachJonathan | 2023-10-19 15:06:12 UTC | #1

## Background
The other week there was an [incident where we had funds misdirected](https://gov.gitcoin.co/t/incident-regarding-mistransferred-treasury-funds/16683) an incorrect address, rendering the funds stuck. This led to some back and forth about the process of how to move forward. What I'm seeing, are some clear gaps in our documentation around governance.

So far our single source of truth (SSOT) for all things governance has lived in this post about [governance v3](https://gov.gitcoin.co/t/gitcoin-dao-governance-process-v3/10358) and the recently created [Governance Manual](https://manual.gitcoin.co) that will be maintained moving forward. Reading these over, I'm seeing that we have stumbled into undefined territory about how to move forward.

## Proposed Change to Governance

I'd like to propose that moving forward, our governance states explicitly something along the lines of:

> Any new release of funds from Gitcoin's Treasury or Matching Pool requires the approval of GTC token holders

I'm hoping that this clause will actually capture what (I think) @connor and @carlosjmelgar are pointing to in the initial post and by voting "no" and to "abstain" - that if funds are going to be newly sent from the Treasury, that there is some due process required.

This captures scenarios we already vote on, including:
- Approving the funding of workstreams
- Approving the funding of GCPs
- Approving payouts to grantees after each Gitcoin Grants round

One thing that would also be helpful is if Stewards could comment and help draft the exact wording as it should appear in the [Governance Manual](https://manual.gitcoin.co/), specifically on the [Proposals page](https://manual.gitcoin.co/governance-processes/proposals).

After enough comments, we will move this proposal to a Snapshot vote. If passed, I will update the [Governance Manual](https://manual.gitcoin.co/) with the wording we agree on in this thread.

-------------------------

owocki | 2023-10-21 05:17:30 UTC | #2

# First Reaction

[quote="CoachJonathan, post:1, topic:16808"]
> Any new release of funds from Gitcoin’s Treasury or Matching Pool requires the approval of GTC token holders
[/quote]

I'd propose the following change

> > Any new release of funds from Gitcoin’s Treasury or Matching Pool requires the approval of GTC token holders' **delegates**

because that's actually more accurate way of describing how gitcoin governance actually works.

one thing to note here is that the [main gitcoin treasury](https://etherscan.io/name-lookup-search?id=timelock.gitcoindao.eth) already enforces this condition in code.  (per the design of the timelock contract, no funds can be moved without governance approval).

the [the matching pool multisig](https://etherscan.io/name-lookup-search?id=multisig.gitcoindao.eth) does not have the same trustware-based assurances.  if we are serious about this proposal as written, perhaps one thing to do might be to refactor the matching pool multisig to reflect the new social norm.  though now that i'm suggesting it, i dont think this is what carlos/connor were pointing at.  and that has nothing to do with original MMM fund issue.

# Second Reaction

[quote="CoachJonathan, post:1, topic:16808"]
I’m hoping that this clause will actually capture what (I think) @connor and @carlosjmelgar are pointing to in the initial post and by voting “no” and to “abstain” - that if funds are going to be newly sent from the Treasury, that there is some due process required.
[/quote]

as far as i understand it, the treasury already enforces the condition that GTC token holder delegates need to approve it. why make a change in the governance manual to represent this?  it feels like thats a meta level change, when the object level thing connor/carlos are looking for is some debate on a proposal to re-fund MMM?  or maybe thats just symbolic since we know it's going to pass or maybe its a place for [connors cocerns](https://gov.gitcoin.co/t/incident-regarding-mistransferred-treasury-funds/16683/25) to be aired out?  idk maybe im misreading tho.

i kind of understand where connor is coming from, but on the other hand what are we going about it?  i dont see a way to undo it.

i am fairly agnostic to this proposal.  i dont think it hurts, and i dont think it helps.  i hope the [WalletGuard](https://gov.gitcoin.co/t/gitcoin-walletguard/16772) solves for mistransfered funds and we can all go back to focusing on our Essential Intents.

-------------------------
