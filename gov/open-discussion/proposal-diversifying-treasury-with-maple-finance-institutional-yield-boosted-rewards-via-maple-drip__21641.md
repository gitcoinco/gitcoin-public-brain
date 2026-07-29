---
id: 21641
title: "[Proposal] Diversifying Treasury with Maple Finance – Institutional Yield + Boosted Rewards via Maple Drips"
slug: proposal-diversifying-treasury-with-maple-finance-institutional-yield-boosted-rewards-via-maple-drips
category: open-discussion
url: https://gov.gitcoin.co/t/proposal-diversifying-treasury-with-maple-finance-institutional-yield-boosted-rewards-via-maple-drips/21641
created_at: 2025-07-07T17:53:58.926Z
last_posted_at: 2025-07-18T19:45:01.172Z
posts_count: 14
views: 3571
like_count: 31
---

# [Proposal] Diversifying Treasury with Maple Finance – Institutional Yield + Boosted Rewards via Maple Drips

<https://gov.gitcoin.co/t/proposal-diversifying-treasury-with-maple-finance-institutional-yield-boosted-rewards-via-maple-drips/21641>
andret | 2025-07-07 17:53:59 UTC | #1

## 1. Summary

This proposal recommends allocating **$100,000 from Gitcoin DAO’s treasury** to Maple Finance’s institutional lending pools to earn predictable yield while diversifying away from a heavy GTC exposure.

I'm proposing a **phased approach**:
1. Start with a **3-month commitment** via Maple’s **Drips** rewards program to test the strategy while boosting returns.
2. If the DAO is satisfied after that period, we can discuss extending to 6 months (for even higher rewards) and/or increasing the allocation.


## 2. Abstract

Gitcoin’s treasury today is heavily concentrated in GTC, which makes us vulnerable to market swings and limits our options to sustainably fund grants.

By converting $100,000 into stablecoins and deploying it in Maple Finance’s vetted institutional lending pools (USDC or USDT), we can earn ~6.3–6.6% **base APY** from overcollateralized loans to KYC’d borrowers like trading firms and market makers.

Committing this capital via Maple’s **Drips rewards program** for an initial 3-month period adds an average ~3.5% APY in additional rewards. That gives us a total target yield of ~9.8–10.1% while keeping risk manageable.

This “test-and-learn” phase lets us evaluate the strategy with minimal commitment before considering scaling it up.


## 3. Motivation

### Treasury Diversification

Right now, most of our treasury sits in GTC (price risk) or idle stables earning little to nothing. That’s not a sustainable setup for a DAO that needs to keep funding grants and operations for years.

We need better diversification. Maple offers exposure to **real credit markets in crypto**, not DeFi yield farming games.

### Why Maple Finance

Maple is trying to be DeFi’s **credit layer** for institutions. They’re not doing retail degen loans; they’re providing undercollateralized (but carefully underwritten) credit to trading firms and market makers with real KYC/AML processes.

They use **Pool Delegates** to approve borrowers and manage risk. These pools survived the 2022 meltdown and have gotten stricter in Maple V2. For us, it’s a way to earn stable, predictable yield by supporting real institutional lending activity on-chain.

Maple’s smart contracts are battle-tested, with multiple audits (Spearbit, Halborn) and an active Immunefi bounty program.


### Why Syrup / Drips Rewards

Maple launched the **Drips** program to reward liquidity providers willing to commit capital for longer terms.

Here’s the simple model:

* No commitment = 1x Drips
* 3-month commitment = 1.5x Drips
* 6-month commitment = 3x Drips

By committing for 3 months initially, we get **50% more Drips rewards** than passive LPs. Drips rewards are distributed pro-rata and designed to encourage “sticky” liquidity that’s reliable for Maple’s borrowers.

This isn’t just about chasing APY. It’s about:
* Earning more yield **by being a committed LP**
* Helping DeFi credit markets become more stable and mature
* Aligning our treasury strategy with Maple’s long-term approach to institutional lending

**APY Example for USDC Pool:**

* Base APY: 6.3%
* Avg Drips rewards: ~3.5%
* Total expected APY: ~9.8%

By starting with 3 months, we keep risk and liquidity lockup manageable. Later, if the DAO is comfortable, we can increase allocation and go to 6 months for 3x Drips rewards.


### Why This Matters for Gitcoin

This approach puts our treasury funds to work in a more productive way, earning yield while supporting credit markets that can help grow the broader crypto ecosystem.

It’s a step toward making our treasury work for us while helping the space mature.


## 4. Specification

**Amount Proposed:**

* $100,000 worth of GTC or stablecoins

**Deployment Steps:**

1. Treasury multisig converts GTC to USDC or USDT as needed.
2. Deposit stablecoins into chosen Maple Finance Pool.
3. Commit this position through Maple’s Drips program for 3 months (1.5x Drips rewards).
4. Treasury committee monitors and reports quarterly on:
  * Base APY earned
  * Drips rewards accrued
  * Overall treasury diversification impact

**Post-Test Plan:**

* After 3 months, the community reviews results.
* DAO can vote to:
  * Extend to 6 months (3x Drips rewards).
  * Increase allocation.
  * Withdraw or reallocate if unsatisfactory.

**Example Pools:**

* USDC Institutional Pool (~6.3% base APY)
* USDT Institutional Pool (~6.6% base APY)

|Pool | Base APY | AVG Drips Rewards APY | Total Expected APY|
|--- | --- | --- | ---|
|USDC | 6.3% | ~3.5% | ~9.8%|
|USDT | 6.6% | ~3.5% | ~10.1%|


## 5. Benefits

1. Diversifies away from GTC price volatility
2. Predictable yield: ~6.3–6.6% base APY + ~3.5% Drips rewards ≈ ~9.8–10.1% total
3. Phased 3-month test reduces lockup risk
4. Supports the growth of DeFi’s institutional credit layer
5. Aligns with a responsible, sustainable approach to treasury management
6. Rewards us for being a reliable LP, not just chasing short-term yield


## 6. Drawbacks / Risks

* **Smart contract risk** – mitigated by audits and bounty program
* **Counterparty credit risk** – borrower defaults possible, but Pool Delegate underwriting and overcollateralization mitigate this
* **Liquidity risk** – minimum 3-month lock for the test period
* **Rewards variability** – Drips program terms can change, and rewards depend on pool participation
* **Stablecoin risk** – limited but present (USDC/USDT exposure)

### Security Mitigations

* Maple V2 improvements: better transparency, stricter underwriting
* Multiple formal audits (Spearbit, Halborn)
* Live Immunefi bug bounty
* Pool Delegates can be replaced for poor risk management


## 7. Voting Options

1. **Yes –** Approve allocating $100,000 in stablecoins from the treasury to Maple Finance lending pools, with an initial 3-month commitment via Maple’s Drips rewards program. After the 3-month period, the DAO will review performance and decide whether to extend to 6 months, increase the allocation, or withdraw.
2. **No –** Do not allocate funds to Maple Finance or participate in the Drips rewards program.
3. **Abstain –** I choose not to vote either way.

-------------------------

jrocki.eth | 2025-07-09 14:52:34 UTC | #2

I like the idea of diversification and making treasury assets productive. For instance Optimism recently enabled staking of their sequencer ETH. 

https://gov.optimism.io/t/allow-the-optimism-foundation-to-stake-a-portion-of-sequencer-eth-through-season-8/9710

Before doing anything like this though I think it is important that we understand the additional operational overhead that would come with something like this.

-------------------------

andret | 2025-07-09 15:36:30 UTC | #3

Hey @jrocki.eth , thanks for the feedback.

I totally agree, it's important to be realistic about the overhead before moving ahead. That’s actually part of why I framed this as a phased, 3-month test first. The idea is to start small, figure out the practical steps (like multisig execution, monitoring yield, reporting), and see if it’s something the DAO feels comfortable scaling or automating longer-term.

For this first 3-month commitment, I actually think the operational load is pretty light if we keep it simple:

1) Multisig swap from GTC to USDC/USDT
2) Deposit into Maple pool and commit with the 3-month Drips option (all in one UI)
3) Light monitoring (just checking rewards and APY monthly)
4) Two forum updates with yield and rewards details (one at the end of each of the first two months)
5) Final Investment Report at the end of the 3-month commitment
6) Proposal at the end of the 3-month commitment to decide whether to withdraw, roll forward, or increase the allocation.

That’s basically two transactions up front, basic tracking, and a final governance check-in.

The idea is to deliberately keep it small and easy for this test phase so the DAO can see if it’s worth scaling up or automating later.

If there are other operational concerns I’m missing, would love to hear them so we can plan for them early.

-------------------------

wasabi | 2025-07-09 15:45:11 UTC | #4

gm @andret thanks for writing up this proposal. 

[quote="andret, post:1, topic:21641"]
This proposal recommends allocating **$100,000 from Gitcoin DAO’s treasury** to Maple Finance’s institutional lending pools to earn predictable yield while diversifying away from a heavy GTC exposure.
[/quote]
can you provide URLs to the institutional lending pools?

[quote="andret, post:1, topic:21641"]
Gitcoin’s treasury today is heavily concentrated in GTC, which makes us vulnerable to market swings and limits our options to sustainably fund grants.
[/quote]
Are you aware of the treasury diversification efforts with [Avantgarde](https://gov.gitcoin.co/t/passed-sgtm-002-avantgarde-x-gitcoin-strategic-asset-management-for-the-matching-pool/19698), can you outline how your approach is better? 

[quote="andret, post:1, topic:21641"]
By converting $100,000 into stablecoins and deploying it in Maple Finance’s vetted institutional lending pools (USDC or USDT), we can earn ~6.3–6.6% **base APY** from overcollateralized loans to KYC’d borrowers like trading firms and market makers.

Committing this capital via Maple’s **Drips rewards program** for an initial 3-month period adds an average ~3.5% APY in additional rewards. That gives us a total target yield of ~9.8–10.1% while keeping risk manageable.
[/quote]
How liquid are those lending pools? Is there any "cooldown" period before the unwinding is completed?

[quote="andret, post:1, topic:21641"]
They use **Pool Delegates** to approve borrowers and manage risk. These pools survived the 2022 meltdown and have gotten stricter in Maple V2. For us, it’s a way to earn stable, predictable yield by supporting real institutional lending activity on-chain.

Maple’s smart contracts are battle-tested, with multiple audits (Spearbit, Halborn) and an active Immunefi bounty program.
[/quote]
can you provide Docs to the Pools Architecture or URLs to the Audits?

-------------------------

andret | 2025-07-09 17:50:42 UTC | #5

Hey @wasabi, happy to clarify and share some concrete references!

[quote="wasabi, post:4, topic:21641"]
can you provide URLs to the institutional lending pools?
[/quote]

SyrupUSDC:
https://app.maple.finance/earn?_gl=1*1hdsamc*_ga*MTk4ODY3NzI1NS4xNzUxODg3NTUx*_ga_7GW90C7X77*czE3NTIwNzY3ODUkbzUkZzEkdDE3NTIwNzcwOTgkajU2JGwwJGgw

For clarity:

SyrupUSDC is considered a pool and it uses a segregated SPV structure, whereas Maple Pools (such as Maple's Blue Chip pool) use segregated bankruptcy-remote entities for each individual pool.

SyrupUSDC yield is derived from a blend of Maple High Yield Secured and Blue Chip Secured lending pools (https://app.maple.finance/#/v2/lend/pools - you need to create a Maple account to view them), meaning it aggregates yields from multiple Maple pools rather than operating as a single isolated pool.

All the pools mentioned above use the same smart contract infrastructure and borrower network, but SyrupUSDC provides retail users simplified access to diversified institutional lending yields.

[quote="wasabi, post:4, topic:21641"]
Are you aware of the treasury diversification efforts with [Avantgarde](https://gov.gitcoin.co/t/passed-sgtm-002-avantgarde-x-gitcoin-strategic-asset-management-for-the-matching-pool/19698), can you outline how your approach is better?
[/quote]

Yes, I'm aware of the Avantgarde proposal. I’m not saying that my approach is better, but this investment could be done in parallel with the Avantgarde one to improve diversification and risk mitigation. I see a few benefits in investing via Maple/Syrup, specifically in lending to institutional borrowers.

**High Yields:** Syrup targets 15% net APY and has consistently outperformed leading DeFi lending protocols through active management and high utilization. This outperformance comes from actively sourced deals and strategic loan duration management.

**Enhanced Risk Management**: Loans are overcollateralized with rigorous borrower underwriting, including KYC/AML checks and balance sheet assessments. Collateral is held with institutional-grade custody solutions like Anchorage and BitGo, with 24/7 monitoring and automated margin calls.

**Professional Active Management**: The Maple Direct team actively manages loan health through conservative liquidation levels (always above 100% collateralization) and proprietary alert systems with multiple price feeds.

**Yield Enhancement**: Beyond base lending rates, Maple stakes collateral through liquid and native staking, passing additional yield to lenders.

**Institutional Borrower Quality**: All borrowers are vetted institutions with operational sophistication to meet margin calls quickly in volatile markets, providing more predictable risk profiles than typical DeFi protocols.

[quote="wasabi, post:4, topic:21641"]
How liquid are those lending pools? Is there any “cooldown” period before the unwinding is completed?
[/quote]

The following are screenshots of the Maple High Yield Secured and Blue Chip Secured lending pools:

![image|531x500](upload://cfIm9RAD2wjOe6XWtL4hBU0DN4x.png)

![image|518x500](upload://dHwFoJChNSxSySWxefBLjdGyb2z.png)

**Idle Pool Liquidity:** Amount of tokens currently sitting in the pool available to process withdrawals or fund loans.
**Short-Term Liquidity:** Amount of tokens currently sitting in yield-generating strategies available to be converted into immediate liquidity.

SyrupUSDC has moderate liquidity with a withdrawal queue system. Maple specifies that most withdrawals are processed in under 24 hours, but could take up to 30 days depending on available liquidity.

Regarding the withdrawal process:

* Withdrawals are processed first-in, first-out as liquidity becomes available
* Funds continue earning interest while in the withdrawal queue
* Assets are sent directly to the lender's wallet once processed

However, there's also an instant liquidity alternative:

* For immediate access, syrupUSDC tokens can be swapped via Uniswap or Balancer instead of using the withdrawal queue. This provides instant liquidity but the "swapper" will be responsible for any fees, slippage, and risks associated with the swap.

There's no specific "cooldown" period - only committed deposits need to mature before becoming eligible for withdrawal.

[quote="wasabi, post:4, topic:21641"]
can you provide Docs to the Pools Architecture or URLs to the Audits?
[/quote]

On their website, after registering, you can access all the details (pool strategy, documentation, and monthly updates) about their pools.

These are the links:
1. High Yield Secured Lending - https://docsend.com/view/s/rpnugkiyipkv3m6m
2. Blue Chip Secured Lending - https://docsend.com/view/s/pnfq487xxky4f3w3

Maple Documentation: https://docs.maple.finance/

Audit Information: https://syrup.gitbook.io/syrup/technical-resources/security

Each Syrup supported lending asset has its own smart contract, and the addresses of these smart contracts are documented in their technical resources under Addresses:
https://syrup.gitbook.io/syrup/technical-resources/addresses

-------------------------

ivanmolto | 2025-07-13 11:39:05 UTC | #6

Thank you, @andret, for your comments and clarifications — much appreciated. That said, now that Avantgarde’s strategic asset management is in place, I sincerely wouldn’t support setting up an additional treasury management solution with Maple Finance. The logistical overhead, resource demands, and associated risks don’t justify a 3-month allocation that only yields $1,350–$3,750. At this point, I’m more bullish than ever on ETH as a core treasury asset.

-------------------------

andret | 2025-07-14 13:15:43 UTC | #7

Hey @ivanmolto thanks for your feedback. Just want to clarify that the Avantgarde proposal is about the Matching Pool. My proposal is about Treasury management (see also this proposal about treasury funds: https://snapshot.box/#/s:gitcoindao.eth/proposal/0xd83c3f76d615f387e5f828f1ba683194061ee1573da7739bff64f78f29ccc5cb).

Also, as I stated in the text of the proposal, the 3-month commitment of “just” $100k is just a test. The return, should the DAO opt for a higher investment and a longer commitment (= higher Drips multiplier) at the end of the testing phase, would definitely be higher.

-------------------------

MathildaDV | 2025-07-14 18:36:24 UTC | #8

Thanks for the proposal. Just to clarify, Avantgarde is also managing the treasury as [this proposal](https://gov.gitcoin.co/t/sgtm-004-generating-yield-on-dao-treasury-assets-to-support-runway/20217) that passed earlier this year. 

Also, thank you for providing further links and resources for us to look at, as I did feel that the original proposal was lacking that information. I'm not opposed to looking at other proposals outside of what Avantgarde is managing right now, but I would likely vote against running two side by side, echoing what @ivanmolto has mentioned above about overhead.

-------------------------

Avantgarde | 2025-07-15 07:39:14 UTC | #9

To provide some additional context:

As outlined in the proposal referred to by @MathildaDV, the 5m USDC that was previously held in the DAO treasury has recently been deposited to earn yield (see transactions from the safe [here](https://app.safe.global/transactions/history?safe=eth:0xBe66C0391453F4b5C5eFd47DdcCB2f6bA6aA513F)) and will have its first monthly update soon.

While we are also running some yield strategies on a portion of the treasury's GTC, we are of the understanding that no further GTC sales should be made for additional stablecoins. Should this change, we are of course happy to assess other opportunities and work with any service provider should the DAO wish to do so.

-------------------------

andret | 2025-07-16 13:24:42 UTC | #10

Hey @Avantgarde, is [this link](https://app.enzyme.finance/vault/0x0f41351921ede8e61071f48fed253d96760720dd/financials) the correct place to check the stats for your DeFi Yield Vault where you deployed the $5M USDC?

-------------------------

andret | 2025-07-16 13:36:58 UTC | #11

I absolutely understand your position, and thanks for the feedback!

To add some context, you can check out Maple’s most recent pool performance stats here: [Drips Season 10 performance](https://maple.finance/insights/drips-season-10) (it shows both base yield and Drips bonuses).

Another point worth keeping in mind: during market expansion phases, when the cost of capital rises, ‎Maple’s lending revenue tends to benefit. That’s a general trend across L&B protocols, but given Maple’s institutional focus, their performance often runs above avg (something reflected in the data from the link above).

-------------------------

Avantgarde | 2025-07-18 09:12:58 UTC | #12

Hi @andret that is indeed the link to the vault on the Enzyme UI, where you can see portfolio composition, policies, fees etc. The Enzyme UI only shows the share price and unfortunately not the current APY (we've requested this feature), which right now is at 9.64% on the DeFi Yield Vault. 

The treasury is a low risk profile, and for the time being the funds need to stay liquid and ready to be used for near-term cash flows if required, hence the approach (which may be different from the credit risk profile offered by Maple).

-------------------------

andret | 2025-07-18 13:46:43 UTC | #13

Hey @Avantgarde, thanks for clarifying that.

[quote="Avantgarde, post:12, topic:21641"]
The treasury is a low risk profile, and for the time being the funds need to stay liquid and ready to be used for near-term cash flows if required, hence the approach (which may be different from the credit risk profile offered by Maple).
[/quote]

If 3‑ or 6‑month term commitments on Maple aren't suitable for our liquidity needs, we could also look at the **High Yield Secured Lending Pool**, which currently shows a **10%** 30-Day APY.

Here’s why it might be worth considering:

* **Different yield structure:** the pool lends to accredited institutions that are over‑collateralized with liquid digital assets, plus redeploys part of that collateral (staking or lending) for extra yield.
* **Diversified risk:** loans go to well-underwritten institutional borrowers, reducing counterparty risk compared to retail DeFi exposure. Plus, collateral is held in qualified custody.

Compared to “classic” DeFi vaults (like yours on Enzyme), this option combines institutional loan yield *and* collateral redeployment returns, giving us a different risk-exposure profile.

I’m not saying this is better than the current approach (Avantgarde's), but maybe we could consider:
1. Starting with a small test allocation, say $100k, into the High Yield Secured Lending Pool.
2. If it performs well and the DAO agrees, Avantgarde could deploy part of the $5M into Maple. This might be simpler than splitting responsibility or setting up a separate process.

Here’s the screenshot for reference:

![High Yield Secured Lending Maple 4|507x499, 100%](upload://2t2sRJZ0sJnVjs9Zdg3MEnLKKRk.png)

Regarding liquidity for near-term cash needs, I understand your point. Currently, the "Estimated Time to Receive Withdrawal" for the High Yield Secured Lending Pool is 30d,  which isn’t insignificant. However, starting small (e.g., $100k, possibly scaling to $1M over time) shouldn’t hamper our ability to meet near-term cash needs. The majority of the treasury would remain fully liquid.

Happy to hear what you guys think, and whether you'd consider diversifying the $5M investment using Maple.

P.S. A useful article about [Maple's yield generation, underwriting and risk management](https://maple.finance/insights/yield-generation-underwriting-and-risk-management)

-------------------------

Erd_9k | 2025-07-18 19:45:01 UTC | #14

Key strengths I appreciate:

Phased commitment: Starting with a 3-month term allows the DAO to evaluate performance before making longer-term decisions. This shows prudence.

Drips incentives: Leveraging Drips to boost yield without taking on excessive additional risk is a smart move, especially given the stable borrower base Maple targets.

Risk transparency: I like that the proposal doesn't downplay the risks. Smart contract, credit, and stablecoin risks are real, but it's clear that mitigations (audits, underwriting, bounty programs) are in place.

Alignment with Gitcoin values: This strategy supports broader crypto infrastructure (i.e., real-world credit rails for institutions), which aligns with Gitcoin's mission to grow public goods in web3.

Some things I’d like to see during the test period:

* Monthly updates or dashboards showing yield performance, any borrower issues, and market conditions that may impact risk.
* A clear exit plan if things don’t go as expected — especially in the event of a credit event or sudden yield drop.
* Exploration of ETH-based options in the future for diversification beyond just stables, if/when feasible.

Overall, I support this initiative. It reflects responsible treasury management and contributes to maturing the DeFi credit space. Let’s test, learn, and optimize.

✅ Voting Yes

-------------------------
