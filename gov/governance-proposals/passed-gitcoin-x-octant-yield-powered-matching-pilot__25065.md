---
id: 25065
title: "[PASSED] Gitcoin × Octant Yield-Powered Matching Pilot"
slug: passed-gitcoin-x-octant-yield-powered-matching-pilot
category: governance-proposals
url: https://gov.gitcoin.co/t/passed-gitcoin-x-octant-yield-powered-matching-pilot/25065
created_at: 2026-01-19T15:44:17.007Z
last_posted_at: 2026-02-24T01:06:51.235Z
posts_count: 9
views: 312
like_count: 21
---

# [PASSED] Gitcoin × Octant Yield-Powered Matching Pilot

<https://gov.gitcoin.co/t/passed-gitcoin-x-octant-yield-powered-matching-pilot/25065>
MathildaDV | 2026-03-11 16:57:45 UTC | #1

# **Gitcoin × Octant Yield-Powered Matching Pilot**

## **Summary**

This proposal seeks approval for a longer term experiment with the goal of deploying an approved amount into a Gitcoin vault deployed on Octant v2 (matched by Octant), with the generated yield being used towards matching for Gitcoin Grants. Octant would not only provide vault infrastructure, but is also a co-design partner for the round where yield is being spent, while Gitcoin governance retains final authority over allocation decisions.

Gitcoin would deploy a pre-approved portion of Matching Pool (gitcoin.eth) assets into Octant’s non-custodial, audited vault infrastructure, routing yield (and only yield) into Gitcoin Grants matching pool. Octant has committed to matching Gitcoin’s deployed capital up to $2M, alongside co-branding and signaling support.

The goal is to evaluate an experimental low-risk yield strategy that can underwrite meaningful matching at Gitcoin scale while preserving principal. *Gitcoin sets the strategy at our own discretion.* 

## **Motivation**

Gitcoin Grants has historically relied on surplus treasury funds and episodic sponsorships. This model does not compound and becomes fragile as treasury constraints tighten.

Yield-powered matching offers a different primitive:

* Principal is preserved

* Funding scales with time, not one-off decisions

* Incentives align around long-term stewardship of capital

Octant provides an existing coordination layer that routes yield from established DeFi protocols toward public goods, without introducing leverage, custody risk, or bespoke financial engineering. This pilot tests whether that model is compatible with Gitcoin’s risk tolerance and governance standards.

## **How do the vaults work?**

Octant vaults are non-custodial yield-routing vaults built on the ERC-4626 standard and Yearn v3 architecture. Octant does not generate yield itself. Vaults deploy assets into DeFi protocols that the depositor selects based on its own risk profile (such as large lending markets or ETH staking systems), and separate principal from yield at the smart contract level.

Principal always remains owned by the depositor and can be withdrawn at any time. Only realized yield produced by the underlying DeFi protocols is routed to a designated allocation address, in this case the Gitcoin Grants matching pool.

Unlike traditional yield vaults, Octant vaults do not compound returns back to depositors. All yield is automatically redirected for funding purposes, turning standard DeFi yield into a capital-preserving funding mechanism.

The underlying vault and strategy architecture follows battle-tested Yearn v3 patterns, with Octant acting as a coordination and routing layer rather than a yield generator.

For readers who want a deeper technical explanation of the vault architecture, strategies, and allocation mechanisms, a [full explainer is available here](https://octantapp.notion.site/octant-4626-vaults).

## **Asset Class**

The asset being deployed would be either [USDC](https://app.morpho.org/ethereum/vault/0xBEEF01735c132Ada46AA9aA4c54623cAA92A64CB/steakhouse-usdc) or USDS. The USDS yield comes from Sky’s native Savings Rate (SSR), which is user-accessible [here](https://sky.money/features#savings). The SkyCompounder strategy programmatically deposits USDS into the same Sky savings contracts.

As an example, with a yield of 4.5%:

* $1M from each ($2M total) = $32k per quarter in accumulated yield

* $2M from each ($4m total) = $64k per quarter in accumulated yield

## **Proposed Structure**

1. $1M deployed from gitcoin.eth, matched by Octant, totalling $2M.

*Octant will match by deploying their funds to their own vault, sending the yield to the same address.*

*After 4-6 months, we will consider adding another tranche of up to $1M (matched by Octant), after the initial experiment has been tested.*

### **Round Focus & Brand**

* Scope will be co-defined but the final round structure remains with Gitcoin governance.

* The round the yield is deployed to will include Gitcoin × Octant co-branding.

## **Risks & Mitigations**

**Smart contract risk**

* Octant vault framework has undergone [external review (Spearbit audit).](https://github.com/golemfoundation/octant-v2-core/tree/develop/audits)

* The yield-generating DeFi protocol will be selected also with a view on previously conducted audits and implemented security mechanisms.

**Strategy risks and Yield volatility**

* Should the strategy incur a loss, Octant’s vault architecture is designed to protect principal: unharvested yield is used to absorb losses first, ensuring principal remains protected as long as possible. 

* No yield guarantees.

* Matching size is explicitly variable and conservative.

*Note: Gitcoin retains full custody and control of its principal at all times. Funds deployed into the vault are not time-locked, can be withdrawn at any point, and strategies can be changed if desired. This proposal is scoped to a single pilot round; any continuation, scaling, or reuse of accumulated yield beyond the pilot would require separate discussion and approval.*

## **Success Criteria (Pilot-Specific)**

This pilot is successful if:

1. Principal is preserved (no loss).

2. Yield is successfully harvested and used for GG26 and onwards matching.

3. Operational processes (deployment, harvesting, withdrawal) function as expected.

4. Governance can clearly assess whether:

   * yield-powered matching is worth repeating

   * the risk/return profile is acceptable

   * the mechanism meaningfully improves funding sustainability

Clear failure signals include:

* Loss of principal

* Excessive operational overhead

* Yield insufficient to justify complexity

## **Decision** 

Yes - Deploy $1M into the Octant vault from gitcoin.eth

No - Do not move forward

Abstain - Choose not to vote on this proposal

*This proposal is an experiment in making public goods funding more structural rather than episodic, without compromising Gitcoin’s treasury discipline.*

-------------------------

kyle | 2026-01-19 16:13:13 UTC | #2

I am generally supportive, especially if we are pulling funds back from Avantgarde. 

Do we have any estimates on yield generated? I suspect even if it’s lower than market rate, the matching from octant acts as a multiplier on any funds we put in, making it worth while.

-------------------------

LuukDAO | 2026-01-19 18:19:59 UTC | #3

Thanks for working out this proposal in more detail @MathildaDV 

I’m in favour of starting with a 1M commitment to make it worth our time.

Starting with SSR also makes sense to me, as the risk is as low as it gets onchain while still securing the current 4% APY (8% if including Octant’s match).

Assuming we move forward this soon, we should be able to earn about 3-5 months of yield ahead of GG25 payouts.

The initial examples you shared are a bit too optimistic. Below are my simulations based on the current SSR:
1M each (at 4%) = $80k per year = $20k per quarter
2m each (at 4%) = $160k per year = $40k per quarter

Even at those reduced rates, the rewards would cover a large share of Gitcoin ops and GG programs. If we could get comparable rates on our entire treasury, we would likely be net neutral.

Overall, big fan of this collaboration with Octant and the overall direction!

-------------------------

vpabundance | 2026-01-22 17:55:14 UTC | #4

Hey @LuukDAO thanks for the response.  We were intially thinking of trying to make this happen quickly so that GG25 payouts would be a possibility, but decided it’s best to take our time with this, get community feedback, and move forward if/when everyone is feeling good about the proposal.

To that effect, this is why we pushed when we would think of harvesting yield for funding.

[quote="MathildaDV, post:1, topic:25065"]
* Yield is successfully harvested and used for GG26 and onwards matching.

[/quote]

So from my POV, if we move forward with this, we should be able to understand if this idea as a whole is working as intended, with a decent amount of yield for GG26, with the numbers dependent upon when we deploy and how much is deployed.  Your numbers look good though.

-------------------------

LuukDAO | 2026-01-22 20:43:53 UTC | #5

Using the first harvests in GG26 makes sense. Overall, really excited about this direction and further Gitcoin <> Octant collaboration. Will vote in favor of starting with $1m and monitoring closely to potentially scale further :slight_smile:

-------------------------

owocki | 2026-01-27 14:03:16 UTC | #6

i am supportive of this proposal

-------------------------

MontyMerlin | 2026-02-09 16:29:59 UTC | #7

I am supportive of this proposal. Shifting grants towards being funded from yield while also having separate allocations from Gitcoin's remaining treasury toward strategic investments feels like it could be a good strategy for regenerating GTC. 🌱

-------------------------

rohit | 2026-02-19 14:20:12 UTC | #8

Supportive of this proposal. Would love to see Gitcoin transitioning from a sponsor-dependent grants platform to a capital-backed public goods institution. That transition matters more than the specific yield itself.

-------------------------

ccerv1 | 2026-02-24 01:06:51 UTC | #9

Sorry I’m late, I was AFK, but I am supportive of this proposal as well.

-------------------------
