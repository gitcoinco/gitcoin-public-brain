---
id: 10938
title: "Airdrop Farming"
slug: airdrop-farming
category: open-discussion
url: https://gov.gitcoin.co/t/airdrop-farming/10938
created_at: 2022-06-15T10:41:24.726Z
last_posted_at: 2022-09-27T21:34:46.464Z
posts_count: 3
views: 3923
like_count: 25
---

# Airdrop Farming

<https://gov.gitcoin.co/t/airdrop-farming/10938>
DisruptionJoe | 2022-06-16 08:51:14 UTC | #1

# Airdrop Farming

## Purpose

Inform stakeholders of the current mitigation efforts and current plans for future mitigation. Align our understanding and definitions internally and externally. Discuss the potential solutions.

## Overview

Quadratic Funding grants rounds run on Gitcoin are an experiment in a new form of democratic decision making. The legitimacy of Gitcoin’s Grants protocol still depends on ensuring a few key factors:

* Sybil attacks are detected and mitigated
* Collusion is thwarted and not allowed
* Matching pool funds continue to be bountiful
* The community shows up to fund and offer their opinion (via donations) on how matching pool funds should be allocated

These factors rely on a decision-making policy that has transparent and rigorously followed guidelines and an effective anti-fraud program.

Lately, we have seen a substantial behavior increase which we believe threatens the integrity of the Gitcoin Grants system. We call it “airdrop farming”; users whose donations are driven primarily by the promise of an airdrop. This post highlights the findings of our internal discussions about how to define, recognize, and respond to this behavior.

### Definitions

**Airdrop Farming** - The act of donating with the intention of getting an airdrop, not for the intention of signaling support for that public good in a QF round

**Sybil Attack** - Anytime a single actor donates to a single grant using multiple user accounts within a single QF round

**Sybil Account** - One of multiple accounts controlled by a single actor

**Sybil Behavior** - Known common actions of sybil accounts

**Sybil Donation** - A donation by a sybil account

**Actor** - An individual human who may control one or multiple accounts

**User Account or Account** - A unique user account which logs into Gitcoin for participation in a QF round

**Squelching** - Squelching is a function which disables the accounts eligibility to affect matching pool allocations

**Squelched Account** - Donations from a squelched account do not affect matching pool allocations

**Sybil Account Detection** - A combination of manual and algorithmic processes used to detect & squelch sybil accounts

### Current State

***It is always unacceptable for a user to make donations from different/multiple user accounts to a single grant within a QF round***

Airdrop farming with multiple accounts is almost always a [sybil attack](https://en.m.wikipedia.org/wiki/Sybil_attack) on [quadratic funding](https://qf.gitcoin.co/) grants rounds.

* It distorts how the matching pool is distributed, whether intentionally or unintentionally
* It encourages sybil attacks
* It creates misaligned incentives for projects to not share or talk about their future plans

This behavior is a sybil attack in that calculations in the modified quadratic funding algorithm are affected in the same way as any other sybil attack, though the motivation may be different.

Although the damage may be unintentional on the part of the donor, the effect is the same. If grants receive donations from more unique user accounts than unique actors, it directs matching pool funds away from grants which do not engage in this behavior.

***Accounts which participate in a sybil attack, sybil donations, or known sybil behaviors may be squelched***

Sybil accounts will lose their ability to affect matching pool allocations. The community has consented to QF rounds without fraud. By participating in a sybil attack, the account is signaling an intent to participate in a way that has not been consented to by the Gitcoin community.

User accounts may be squelched manually or algorithmically. This allows airdrop farmers to continue farming/donating (their intended action) without diverting matching funds from the intended outcomes of the community.

Any account which is squelched algorithmically is reassessed every time the Sybil Account Detection process is run.

***Airdrop farming by a single actor using a single account is not a sybil behavior***

A single actor is not considered a sybil attack, however, there is reason to state that a single actor using a single account to donate could be considered part of a sybil attack in the future. For example, if a grant was to pay an influencer who then offers to reimburse followers who donate, this would be considered a sybil attack in addition to QUID PRO QUO.

***Ignorance should not be allowed to be used as an excuse.***

All sybil donations should be removed from eligibility to affect the matching pool; this means that the original user's intent would be preserved, but no other grant would be harmed by the signal distortion. We need to bolster our training efforts to ensure donors are aware of this issue. This policy also would help our user education process by incentivizing grants to actively discourage this behavior, since grants with only legitimate one-account-per-user donations will be advantaged in the matching pool allocations.

### Conclusion

There may be edge case circumstances where a user may have legitimate reasons for creating an additional account and giving donations from both accounts. An example would be a young programmer who wants to give money to a cause which is illegal in the country where her parents still live, but also wants to make publicly identifiable donations to other causes. However, **we should never allow any person to make donations from multiple accounts to a single grant. If we do not enforce "one person, one donation", we will quickly see the legitimacy of the system overrun with behaviors that exploit it, whether knowingly or unknowingly.**

## Next Steps

FDD will perform a data analysis to understand how much airdrop farming has impacted matching allocations in the past and how to best mitigate the negative effects and promote positive externalities.

* Develop a data model which can reliability identify airdrop farming separate from sybil behavior
* Understand an airdrop tax amount, how much the average grant has lost due to illegitimate grants
* An understanding of methods for regulation such as:
  * taxing the recipients the “airdrop tax” to return
  * Gradual sanctions applied to trust bonus
  * Sybil stories which may be added to passport
  * Methods for incentivizing desirable behavior; signaling for public goods funding

Shout out to @kyle @annika @octopus @nollied @Sirlupinwatson @tjayrush @danlessa @kylin and @connor

-------------------------

tjayrush | 2022-06-17 11:16:35 UTC | #2

Kudos to Joe and anyone else involved in putting this together. It's very well done, clear, and moves the conversation forward.

I agree with much of this -- especially the idea of `squelching` and also the idea that some people are doing things that are totally natural and justified but that doesn't mean those donations should be matched.

The other thing that comes forward is the need to educate people about the rules, but this feels like a user flow issue on the website. Are users notified on the website when they've been squelched? Is there any chance of identifying potential `squelchees` prior to them making the donations?

-------------------------

ccerv1 | 2022-09-27 21:34:46 UTC | #3

Great post!

I think we can be more precise in differentiating between a user operating *multiple usernames* + multiple wallet addresses and a user with a *single username* + multiple wallet addresses. 

Of course, both are Sybil attacks if they are cycling accounts to fund the same grant(s). 

However, the more benign attack is a user with a *single username* + multiple wallet addresses. This is much more likely to be airdrop farming and, like you say, allows airdrop farmers to continue farming/donating (their intended action) without diverting matching funds from the intended outcomes of the community. 

(Whether this type of quid pro quo behavior violates the community's grant eligibility requirements is a separate matter.)

-------------------------
