---
id: 25228
title: "[SECURITY UPDATE] Treasury Protection & Governance Transition: What We Did and Why"
slug: security-update-treasury-protection-governance-transition-what-we-did-and-why
category: governancevision
url: https://gov.gitcoin.co/t/security-update-treasury-protection-governance-transition-what-we-did-and-why/25228
created_at: 2026-04-13T20:57:51.499Z
last_posted_at: 2026-04-26T20:32:14.879Z
posts_count: 4
views: 100
like_count: 9
---

# [SECURITY UPDATE] Treasury Protection & Governance Transition: What We Did and Why

<https://gov.gitcoin.co/t/security-update-treasury-protection-governance-transition-what-we-did-and-why/25228>
MathildaDV | 2026-04-13 20:57:51 UTC | #1

## [SECURITY UPDATE] Treasury Protection & Governance Transition: What We Did and Why

### TL;DR

Tally, the platform powering Gitcoin's on-chain governance execution, is shutting down. In parallel, a security review identified a structural vulnerability in our current governance architecture that could expose treasury assets to attack. In response, the Gitcoin Foundation and DAO coordinated a pre-emptive protective measure: liquid treasury assets have been moved to a new Safe multisig. Governance signaling continues as normal. This post explains what happened, why, and what comes next.

### Background: Two Converging Pressures

In mid-March 2026, [Tally announced](https://www.coindesk.com/markets/2026/03/17/gensler-and-biden-were-just-better-for-crypto-says-tally-ceo-as-dao-governance-platform-shuts-down) it would wind down operations after six years, having powered on-chain governance for over 500 DAOs including Uniswap and Arbitrum. This created an immediate operational necessity for Gitcoin: our governance execution layer needed to migrate regardless of any other considerations.

Concurrently, a security review surfaced a known class of governance vulnerability that our current architecture does not protect against. The combination of these two factors created a time-sensitive window that warranted action outside the standard governance cadence.

### The Vulnerability

Gitcoin's current governance model operates on token-weighted voting with timelock execution. This design, common across DAOs, has a structural asymmetry:

* An attacker needs only one successful proposal to execute an irreversible treasury action
* Defense requires continuous monitoring and timely coordinated response
* There is currently no execution-layer veto or circuit breaker

If quorum can be reached at a cost lower than the value of assets controlled, governance becomes economically attackable. Publicly announcing this vulnerability through a standard governance proposal, with its associated timelock, would have created a window for exploitation before mitigation could be completed. We would, in effect, be advertising the attack vector to potential bad actors at the precise moment we were most exposed.

### What We Did

**Phase 1: Immediate Action (In Progress)**

* Liquid treasury assets have been transferred from the on-chain Governor contract to a new Safe multisig (4-of-5 signers)
* The multisig is modeled on Gitcoin's existing matching pool custody structure, with trusted, distributed signers
* On-chain governance proposals remain active and continue to function as signaling and instruction to the multisig
* No changes have been made to DAO governance structure or voting mechanisms

### Why This Was Done Without a Vote

The Foundation's governing documents address this scenario directly. Article 2, Section 4 restricts the Foundation from allocating or distributing DAO treasury assets without a DAO Resolution — but this action is a protective custody transfer, not an allocation or distribution. No funds are being spent or disbursed. Article 5, Section 7's use of the word "disbursements" specifically implies spending, not custodial movement for protection.

Separately, Article 2, Section 4(b) permits the Foundation to act without a DAO Resolution to comply with legal or other core requirements. Tally's shutdown constitutes exactly that kind of independent operational necessity.

This action has been flagged as appropriate under the Foundation Constitution and reflects the fiduciary responsibility embedded in steward and Foundation roles.

### Tradeoffs We're Accepting

This is not a framing-free decision, and the community deserves transparency about what we're trading:

* We are temporarily introducing a trusted execution layer
* Pure automatic on-chain execution is reduced in the short term
* The multisig represents a centralization point that would not be acceptable as a permanent state

We believe this tradeoff is correct: protecting treasury assets takes precedence over automation under current threat conditions. This is a temporary bridge, not a destination.

### What Comes Next

**Phase 2: Governance Hardening**

We will move toward a structurally improved governance system. The work ahead includes:

* Timelock improvements and extended reaction windows
* Execution guardrails and circuit breakers at the protocol level
* Scoped treasury permissions and rate limits
* Spending controls that constrain proposal impact
* Optionally delegate the GTC in the treasury to the multisig

**Path Forward**

* Near term: Multisig provides execution protection while governance tooling migrates away from Tally
* Medium term: Hybrid governance with constitutional updates and execution guardrails
* Long term: Return to fully on-chain execution once the vulnerability class is structurally mitigated

As governance hardens, the multisig will transition to an emergency backstop function, or be removed entirely.

### Governance Continuity

To be explicit: governance is still active. Stewards and token holders continue to signal intent through proposals. The multisig executes in accordance with those signals. The community's voice in directing resources and priorities is unchanged.

Further updates will follow as Phase 2 work progresses. A formal governance hardening plan will be shared for community input before implementation.

Questions and feedback welcome in this thread.

-------------------------

owocki | 2026-04-14 18:16:07 UTC | #2

i voted for this in tally because i want to see the treasury safeguarded.  i am not crazy about the tradeoffs we had to take, but they are acceptable to me if the alternative is risking having the treasury drained.

if anyone has feedback on the medium/long term solution, pls contact me.  will be spending some cycles on this in q2-q4.

-------------------------

bear-wang | 2026-04-16 08:34:29 UTC | #3

I fully agree with the decision mentioned above. When it comes to the issue of fund security, we must not be careless, and adopting a decisive approach is entirely correct.

-------------------------

narcov_eth | 2026-04-26 20:32:14 UTC | #4

I agree with this decision @MathildaDV. Automation should never come at the cost of asset safety.

[quote="MathildaDV, post:1, topic:25228"]
protecting treasury assets takes precedence over automation under current threat conditions.

[/quote]

A temporary multisig is reasonable if it gives Gitcoin time to harden governance safely.

-------------------------
