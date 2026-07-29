---
id: 20044
title: "GTC Utility Experiment for GG23"
slug: gtc-utility-experiment-for-gg23
category: gitcoin-grants
url: https://gov.gitcoin.co/t/gtc-utility-experiment-for-gg23/20044
created_at: 2025-02-21T21:33:49.162Z
last_posted_at: 2025-06-08T23:39:04.234Z
posts_count: 7
views: 2969
like_count: 27
---

# GTC Utility Experiment for GG23

<https://gov.gitcoin.co/t/gtc-utility-experiment-for-gg23/20044>
gnomadic | 2025-02-22 16:01:39 UTC | #1

We see a strong opportunity to create meaningful token utility in GG23. While we haven’t launched many experiments in this area before, this presents an exciting chance to explore and learn. By testing new approaches, we can develop a stronger perspective and expertise on what will be most effective.Our first experiment will be fast/lean and lean into market trends that are currently successful.

We would like to run this experiment through GG23’s QF OSS Program, which will have a total of $600k matching pool. We will be requesting 3% of the round value (600k USDC) at 18k USDC to fund the staking rewards for this experiment. This request for funds will be included in the matching pool ratification ahead of the round.

**Experiment #1 GG23: Stake for your favorite projects**

The basic concept is that anyone can stake GTC on projects in a GG round to showcase their support and draw greater volumes of crowdfunding, excitement, and matching funds.

How it works:

1. Round starts
2. Gitcoin funds the stake rewards pool (with 18k USDC)
3. Projects apply and get approved
4. Projects show up on explorer
5. Users stake GTC on grants to signal support. Minimum stake is 1 GTC. No maximum stake.
6. For every project, we keep track who has staked how much (aka we know the % )
7. Once the round ends, QF distribution runs and we know which projects get what % of the pot

For example:



* If project A gets 5% of the pot , then reward pot for staking on project is 5% of 18k (900 USDC).  
* This 900 USDC is split between the stakers based on how much % they had staked
* If wallet1 accounts for 50% of the staked tokens for project A, they get 50% of 900 (450 USDC)
* If wallet2 accounts for 1% of the staked tokens for project A, they get 1% of 900 (9 USDC)

-------------------------

paul2 | 2025-03-03 21:06:05 UTC | #2

Love this idea :slightly_smiling_face:

btw this can be done as-is using [Gardens](https://app.gardens.fund/), and would integrate nicely into our [GG23 Community Round Application](https://gg23.grantships.com/view-draft/0x781ce54b73730667e7390caa0e52d4d585b574f274f780c4e0bb96a18a996c30-0). 

Especially with this pool in our application:

> 1. **Best OSS on Ethereum** - curated list of best projects on Ethereum.

The way this pool works is:
* Stake the minimum $GTC and sign the [Gitcoin Code of Conduct](https://support.gitcoin.co/gitcoin-knowledge-base/about-gitcoin/code-of-conduct) onchain to be able to create and vote on proposals.
* People can stake additional $GTC to get more voting weight in the Pool. This can be 1 token = 1 vote, or quadratic voting (multiple options for sybil resistance for this).
* Community members can dispute abusive or irrelevant proposals, which a Safe of Gitcoin contributors rules to approve or block (more optimistic + decentralized than an approval-based moderating system).

As an experiment, I imagine this type of governance pool might work better *without* the explicit promise of funding. Not to say that airdropping $ to winners wouldn't be a good idea, but maybe seasonally looking at results and sending out project rewards only if the Gitcoin community feels good about the results. That might work better from a collective intelligence POV, without making it any less fun to hold $GTC to participate.

Plus, with conviction voting in Gardens you can require voter support on proposals over longer periods of time, which should help with that issue even more :seedling:

-------------------------

meglister | 2025-03-10 21:25:17 UTC | #3

Thanks @paul2 ! We'd love to use Gardens more in the future. I think it's important that this version be integrated into Grants Stack UX to encourage participation. 

Definitely interested to see the impact of rewards... I'm personally very pro-rewards but happy to be proven wrong :slight_smile:

-------------------------

ivanmolto | 2025-03-11 21:10:51 UTC | #4

That sounds exciting @gnomadic :raised_hands:
Will you be using the Human Passport score or another solution to address Sybil attacks? 
Also, to stake, do you first need to make a donation to the project? IMHO requiring a minimum donation to stake is the only way to generate greater volumes of crowdfunding, excitement, and matching funds.

-------------------------

owocki | 2025-04-16 18:50:40 UTC | #5

follow the gtc staking experiment stats here :slight_smile: 

https://dashboard.boost.explorer.gitcoin.co/

current stats
![Screenshot 2025-04-16 at 12.50.26 PM|669x500](upload://8jPVxrhOXERctFvMgAN0GzOeuH3.jpeg)

-------------------------

Hydrapad | 2025-04-17 10:31:06 UTC | #6

This is amazing !! good work :clap:

-------------------------

ivanmolto | 2025-06-08 23:39:04 UTC | #7

I want to congratulate the Boost experiment for innovating on GTC utility during GG23. It was a unique mix of *regen* and *degen* energy — a bold experiment with strong potential.

That said, the user experience could benefit from improvements, especially regarding unclear communication around time penalties and the unstaking process.

#### What I loved:

* GTC staking rewards as an incentive to signal valuable projects.

* The design served as a **“stake to place”** mechanic, helping grantees surface by self-staking. It reminded me of paid placements in iTunes, Google Play, or carrier-curated app stores — but with an onchain, regen twist.

* The simple app concept for claiming staked GTC and batch reward transfers was great — it helped reduce confusion and save on gas fees.

* While it was a volatility season the price of the GTC going up + rewards made the Boost experiment a perfect trade.

In essence, in my opinion this experiment worked like a **degen-flavored prediction market with regen intentions.**

#### Areas for improvement (if this experiment is applied in future rounds):

* **Documentation clarity:**

The example scenario (e.g., a grantee receiving 50% of the matching pool) was misleading. Grantees' matching is capped to 10%. I would recommend to include the working formula and a realistic example directly in the docs and UI.

* **Transparent penalties:**

The *Time-Weighted Staking Bonus* was not explained upfront. While the formula was in a GitHub repo, it wasn’t referenced anywhere, and the disclaimer was only shown after rewards were distributed.

* **Unstaking timing:**

Ideally, stakers should be able to unstake shortly after the round ends. The smart contract had the rules to start stakes at the round donations start date. And claim stakes after the donations end date. But while the mosts stakers were aware of this nearly all of them waited to claim until the green light from Gitcoin team except three (and two were rewarded).
It's a functional flaw if unstaking depends on a communication date, even though users can interact directly with the smart contract without waiting for a green light from Gitcoin.

-------------------------
