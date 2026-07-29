---
id: 22560
title: "[TEMP CHECK] Fair Fees for GG24"
slug: temp-check-fair-fees-for-gg24
category: open-discussion
url: https://gov.gitcoin.co/t/temp-check-fair-fees-for-gg24/22560
created_at: 2025-08-03T10:53:13.466Z
last_posted_at: 2025-09-10T17:42:23.360Z
posts_count: 20
views: 2891
like_count: 39
---

# [TEMP CHECK] Fair Fees for GG24

<https://gov.gitcoin.co/t/temp-check-fair-fees-for-gg24/22560>
owocki | 2025-08-03 10:58:26 UTC | #1

As we prepare for Gitcoin Grants 24, this post floats adopting a Fair Fees model for attracting and compensating round operators by covering their costs (including software, servicing the rounds). This fee would be sent directly to the round operators running rounds running in GG24.

The [fair fees model](https://ethresear.ch/t/fair-fees-a-dynamic-formula-for-balancing-dapp-value-creation-capture/22225), originally published on[ ethresear.ch](https://ethresear.ch/t/fair-fees-a-dynamic-formula-for-balancing-dapp-value-creation-capture/22225), introduces a transparent, scale-sensitive fee formula that rewards early-stage builders and avoids over-taxing large rounds.

---

### Motivation

As Gitcoin no longer has a software team nor runs most rounds itself, I believe it is essential that we can attract world class round operators and software teams. These fair fees would be a part of attracting, aligning, and retaining those teams in the Gitcoin ecosystem.

---

### The Proposal

Adopt the following formula to compute fees on a domains matching pool size (N):

fee ≔ max(√(1000 × N), N × 0.01)

* For small domains, this generates proportionally higher fees to help fund software development and operations.

* For larger domains, fees cap at 1% of the pool.

* This produces a smooth, predictable curve where protocol fees decline with scale.

This would be a default policy for GG24 domains or rounds receiving Gitcoin ecosystem support (e.g. on coordination, matching, and/or legitimacy).

If you want to better understand how fair fees works, [checkout this spreadsheet](https://docs.google.com/spreadsheets/d/189KZ2zpFyf18XOV9jWL7mgDiLy9aylS_vVzvCFK_Rlc/edit?gid=699870709#gid=699870709) or [the original ethresearch post](https://ethresear.ch/t/fair-fees-a-dynamic-formula-for-balancing-dapp-value-creation-capture/22225).

---

### Why It Matters

* Sustainable: Generates meaningful revenue for round operators, especially for smaller or experimental rounds.
* Fair: Reduces fees on larger rounds, ensuring capital flows primarily to builders and grantees.
* Simple & transparent: Anyone can compute the fee for a given pool size in advance.
* Attracts talented software developers and round operators to Gitcoin

---

### 📊 Example Fees Under Fair Fees

|Pool Size|Fee (Fair Fees)|% of Pool|
| --- | --- | --- |
|$100k|~$10,000|10%|
|$500k|~$22,360|~4.5%|
|$1M|~$31,622|~3.1%|
|$5M|~$70,711|~1.4%|
|$10M|$100,000|1%|
|$50M|$500,000|1%|

---

### Optional (for later discussion)

1. We may explore an “accrued fee” implementation, where fees are calculated incrementally as round operators run multiple rounds (eg round operator x24 for domain y24 in GG24 runs a domain y25 in GG25). This is not part of the current vote but could be piloted in future rounds.
2. We could explore offering the revenue to the operators if they agree to treat the fees as an investment and give Gitcoin upside in their software startup, either in the form of tokens or equity.
3. We could explore augmenting the fair fees formula to make it more or less aggressive.

---

### Temp Check Options

How should we proceed for Gitcoin Grants 24?

* ✅ Yes, adopt Fair Fees
* ✅ Yes, adopt Fair Fees but with changes (eg only if upside is given, or augmenting the formula)
* ❌ No, do not adopt Fair Fees
* 🤷 Abstain

Please vote by 9/1/2025, and feel free to share feedback or suggested tweaks to the formula in the comments.

-------------------------

thedevanshmehta | 2025-08-03 19:53:36 UTC | #2

Love this idea and fully in favor!

It would be nice to have a comparative study between overhead spent before GG23(basically gitcoin tech costs) vs from after GG24 (after domains introduction).

They aren't exactly comparable since now we are taking overhead from the matching fees but would still give us some idea of the cost savings from this approach

[quote="owocki, post:1, topic:22560"]
### Example Fees Under Fair Fees

|Pool Size|Fee (Fair Fees)|% of Pool|
| --- | --- | --- |
|$100k|~$10,000|10%|
|$500k|~$22,360|~4.5%|
|$1M|~$31,622|~3.1%|
|$5M|~$70,711|~1.4%|
|$10M|$100,000|1%|
|$50M|$500,000|1%|
[/quote]

This is a really great segment and think we can set a standard for mechanism builders to adhere towards. I expect some of the core gitcoin rounds like with @MathildaDV leading OSS wll be on the higher end where fair fees would apply, but most might be in the lower range so we'd see 8-10% as overhead - which is actually close to what we see in the traditional world

[quote="owocki, post:1, topic:22560"]
We may explore an “accrued fee” implementation, where fees are calculated incrementally as round operators run multiple rounds (eg round operator x24 for domain y24 in GG24 runs a domain y25 in GG25)
[/quote]

To take some of this discussion forward - i wonder how much this applies to mechanisms that have been tried out already in other areas.

for eg, the butter team has tested their mechanism for optimism and uniswap for over 2 million. so would fair fees apply to those earlier mechanisms too or would it restart and be specific to their domain?

ideally if each domain owner has their own smart contract thats being reused, we could actually apply the fair fees formula to even rounds held outside of gitcoin.

-------------------------

hello2jie | 2025-08-04 02:44:58 UTC | #3


This fee model is generally reasonable, but the 10% fee rate for small pools may place significant pressure on many early-stage or experimental projects.
It is recommended to introduce a tiered subsidy mechanism to prevent fee-related barriers from impacting ecosystem diversity and innovation vitality.

## Optimized Fair Fees Model

Introduce a **tiered subsidy** to reduce fees for small matching pools, easing the burden on early-stage or experimental projects:

### Definitions:

* N: matching pool size
* T: subsidy threshold (e.g., $50,000)
* α: small pool subsidy factor (e.g., 0.5)

### Fee Calculation:

Calculate the base fee as before:

![image|690x82](upload://k6gOjkMOZJrZSArlnWbj3VYe8bL.png)


Apply the subsidy for small pools:

![image|616x156](upload://rQ8OYoo6a3s9VEG7JYBKxStA3kX.png)

---

### Explanation

* For matching pools **smaller or equal to TT**, the fee is discounted by factor α\alpha to help fund early-stage and experimental rounds without heavy fee pressure.
* For pools **larger than TT**, the standard fee applies, preserving fairness and scale economy.
* This approach balances sustainability with inclusivity, encouraging more diverse and innovative projects.

-------------------------

LuukDAO | 2025-08-04 19:36:16 UTC | #4

Glad we're discussing budgeting and rewards proactively. Hitting the operator and program economics right is key for sustainable growth.

The current proposed "fair fee models" seem to optimize for low-touch rounds. The proposed fees are too low to attract, retain, and grow top-tier operators. 

From my experience and research, traditional non-profits, innovation, and development programs have significant operations and fundraising costs. Operations is often 10-15% of the budget, with 5-10% dedicated to fundraising/marketing. 

Due to recent tech innovations and better frameworks, we should be able to cut these costs down significantly; however, aiming for 1% may be unreasonable. 

Ultimately, our objective is to allocate funds most effectively. To accomplish better and more impactful rounds over time, we should provide enough resources for round operators to:
1) design and execute the best rounds, 
2) find and fundraise from the best partners, 
3) conduct R&D efforts to improve round effectiveness, 
4) support round participants pre and post round, and 
5) have some profit/leeway to bridge into the next round.

**My suggestion**
Instead of a fixed fee, align on fee ranges. DDA would have to provide clear plans and argumentation if they want to request above-average fees. 

|Pool Size | Fee Range | % of Pool|
|--- | --- | ---|
|$100k | $10,000 - $15,000 | 10% - 15%|
|$500k | $25,000 - $50,000 | 5% - 10%|
|$1M | $40,000 - $80,000 | 4% - 8%|
|$5M | $150,000 - $350,000 | 3% - 7%|
|$10M | $250,000 - $600,000 | 2,5% - 6%|
|$50M | $1,000,000 - $2,500,000 | 2% - 5%|

In addition to being 2-3x more cost-effective than current best practice programs, we should also aim to outperform in measurability, transparency, and speed. By doing so, we will be able to provide a strong offering to larger, non Web3-native funders.

-------------------------

Oba-One | 2025-08-04 18:48:33 UTC | #5

Love the potential of this approach and agree with @LuukDAO on the fee range.

[quote="LuukDAO, post:4, topic:22560"]
**My suggestion**
Instead of a fixed fee, align on fee ranges that have to provide clear plans and argumentation if they want to request above-average fees.

|Pool Size|Fee Range|% of Pool|
| --- | --- | --- |
|$100k|~$10,000 - $15,000|10% - 15%|
|$500k|~$25,000 - $50,000|5% - 10%|
|$1M|~$40,000 - $80,000|4% - 8%|
|$5M|~$150,000 - $350,000|3% - 7%|
|$10M|$250,000 - $600,000|2,5% - 6%|
|$50M|$1,000,000 - $2,500,000|2% - 5%|
[/quote]

I also align with the **tiered subsidy** suggested by @hello2jie 

[quote="hello2jie, post:3, topic:22560"]
### Definitions:

* N: matching pool size
* T: subsidy threshold (e.g., $50,000)
* α: small pool subsidy factor (e.g., 0.5)

### Fee Calculation:

Calculate the base fee as before:

![image](upload://k6gOjkMOZJrZSArlnWbj3VYe8bL)

Apply the subsidy for small pools:

![image|616x156](upload://rQ8OYoo6a3s9VEG7JYBKxStA3kX)

---
[/quote]

I think another area to address is **frequency**, what's the target amount of rounds over a period of time that makes this sustainable for builders and operators. Also how does the implementation of fair fees look with DDAs?

For example, if a DDA plans to do multiple localism rounds would fair fees need to be applied following the Gitcoin requirements or this will just be on the funds Gitcoin provides DDAs?

-------------------------

Tane | 2025-08-08 05:17:22 UTC | #6

We agree with the core direction of this proposal, but we share @LuukDAO’s concern that the current model underprices operator compensation for larger rounds. 

Especially in the early Gitcoin 3.0 phase, it feels risky to start with incentives that are this thin. 

A better approach could be to begin with a relatively higher fee structure to ensure we can attract and retain top-tier operators who will invest in building strong, sustainable rounds. 
Over time, as the ecosystem matures and we can enable more permissionless participation, competitive dynamics could naturally drive fees lower. 
Starting high and tapering down seems more aligned with long-term sustainability than locking in low incentives from the outset.

-------------------------

owocki | 2025-08-08 15:53:34 UTC | #7

[quote="Tane, post:6, topic:22560"]
We agree with the core direction of this proposal, but we share @LuukDAO’s concern that the current model underprices operator compensation for larger rounds.
[/quote]

do you or @LuukDAO (or anyone else on the thread) want to fork [the model](https://docs.google.com/spreadsheets/d/189KZ2zpFyf18XOV9jWL7mgDiLy9aylS_vVzvCFK_Rlc/edit?gid=699870709#gid=699870709) and propose an alternative scheme?  the model is configurable so it should be possible to tweak these variables and come up with an alternative that matches your values

![Screenshot 2025-08-08 at 9.53.24 AM|422x404](upload://jd2xEaYfsx58UpL4Xwrh1qJInpj.png)

-------------------------

LuukDAO | 2025-08-10 22:51:10 UTC | #8

I forked the [modal and made a version here](https://docs.google.com/spreadsheets/d/1CN6GJDSJIsnt_3c2S3wY4ItQ8QeE-yexRlv1A4w4_fc/edit?usp=sharing), which I feel is decent. 

I used a min fee of 3% and a max fee of 20% with 2.5 decay, which comes close to the ranges I suggested for programs up until 1M, which is most relevant at the current stage. 

For programs above 1M USD in funding, I think the decay could be lower; however, at the same time, program duration would likely increase significantly/ A different model that includes a time dimension could be created for this. 

To operationalize a first version of the Fair Fees Model, I suggest the following: 
- Use a Fair Fee Model, which could be [the version I created](https://docs.google.com/spreadsheets/d/1CN6GJDSJIsnt_3c2S3wY4ItQ8QeE-yexRlv1A4w4_fc/edit?usp=sharing) if we want to increase the attractiveness to operate a DDA and innovate, as a benchmark for fees.

- Have DDA operators specify the exact fee to be charged, with a breakdown of A. personnel costs, B. overhead costs (e.g., legal, marketing), and C. software development and usage costs (e.g., smart contracts and AI). 
- The combined costs of the DDA, including any fees to Gitcoin or other third parties,  should be within a reasonable range of the Fair Fee Model benchmark. 

To start, I suggest a maximum threshold of 25% above the suggested fee according to the Fair Fee Model in cases where personnel, overhead, and software costs are justifiably contributing to increasing the outcome of the DDA and its ability to fundraise pre- and post-program.

-------------------------

kyle | 2025-08-12 17:12:26 UTC | #9

[quote="owocki, post:1, topic:22560"]
this post floats adopting a Fair Fees model for attracting and compensating round operators by covering their costs (including software, servicing the rounds). This fee would be sent directly to the round operators running rounds running in GG24.
[/quote]

Just a basic question - is this fee coming from the matching pool? 100k round gets paid $10k in a fee... and so then the round itself costs the matching pool $110k ?

The next question is, (and this is likely in the GG24 post?) how are pool sizes determined and eligibility evaluated?

-------------------------

owocki | 2025-08-12 18:02:53 UTC | #10

[quote="kyle, post:9, topic:22560"]
Just a basic question - is this fee coming from the matching pool? 
[/quote]

the round funding sources of the round can include the matching pool but needn't be only the matching pool.  ideally in gitcoin 3.0 era we become better at getting matching on matching on matching (thx @syntropicregen for this meme!)
![untitled_84|500x500](upload://26AVNk2hvfzRsHSCSvlpSTxhQUK.gif)

[quote="kyle, post:9, topic:22560"]
100k round gets paid $10k in a fee… and so then the round itself costs the matching pool $110k ?
[/quote]

there are two ways we could go.
1. total is $100k from the funding sources (inc matching pool) and 10% taken from that.
2. total is $110k from the funding sources (inc matching pool) and 10% is taken from that.

i dont have a strong opinion here.  curious what @MathildaDV or @deltajuliet or @kyle thinks

[quote="kyle, post:9, topic:22560"]
The next question is, (and this is likely in the GG24 post?) how are pool sizes determined and eligibility evaluated?
[/quote]

i believe the plan is to do a GTC vote and allocate proportionally to how that unfolds.  

we can evolve more complexity/powerful ways to do it from there (there are a lot of more interesting ideas floating around - condorcet voting, web of trusts, etc, but i think were starting simple and evolving ways to allocate funds from a domain to a subdomain from there)   

@MathildaDV lmk if i got this right.

-------------------------

M0nkeyFl0wer | 2025-08-13 14:26:39 UTC | #11

So glad to see this being discussed. Great idea, I very much support this.

-------------------------

MathildaDV | 2025-08-13 16:57:00 UTC | #12

[quote="owocki, post:10, topic:22560"]
there are two ways we could go.

1. total is $100k from the funding sources (inc matching pool) and 10% taken from that.
2. total is $110k from the funding sources (inc matching pool) and 10% is taken from that.
[/quote]

IMO it would be option 1. 

[quote="kyle, post:9, topic:22560"]
The next question is, (and this is likely in the GG24 post?) how are pool sizes determined and eligibility evaluated?
[/quote]
Correct, it's outlined in this [GG24 Strategy](https://gov.gitcoin.co/t/gg24-structure-strategy-and-timeline/22878) post: 

[quote="MathildaDV, post:1, topic:22878"]
Funding Caps - Each community-operated domain will have a maximum funding allocation, with each funding allocation being more flexible and in line with the quality of the report presented and clear funding needs. It is up to the Gitcoin team to set funding amounts for each domain that will get ratified through governance.
[/quote]

And to be clear, every step needs to be ratified by governance through a GTC vote. Eligibility for domains is already laid out and only eligible domains will go to a vote. Echoing what @owocki has said, the idea is to start simple in GG24, and expand the complexity and scope moving forward.

-------------------------

griff | 2025-09-10 17:06:20 UTC | #13

[quote="owocki, post:10, topic:22560"]
there are two ways we could go.

1. total is $100k from the funding sources (inc matching pool) and 10% taken from that.
2. total is $110k from the funding sources (inc matching pool) and 10% is taken from that.
[/quote]

I would vote #2... give wierd numbers to the operators, round numbers to the public.

[quote="LuukDAO, post:4, topic:22560"]
**My suggestion**
Instead of a fixed fee, align on fee ranges that have to provide clear plans and argumentation if they want to request above-average fees.

|Pool Size|Fee Range|% of Pool|
| --- | --- | --- |
|$100k|~$10,000 - $15,000|10% - 15%|
|$500k|~$25,000 - $50,000|5% - 10%|
|$1M|~$40,000 - $80,000|4% - 8%|
|$5M|~$150,000 - $350,000|3% - 7%|
|$10M|$250,000 - $600,000|2,5% - 6%|
|$50M|$1,000,000 - $2,500,000|2% - 5%|
[/quote]

Love the tIer range, I would suggest that for experiments under $100k there be a lot of freedom, and I would make the pool size a range... I added 2 more tiers:

|Pool Size|% of Pool|
| --- | --- | 
|<$100k|Case by Case|
|$100k-$250k|10% - 15%|
|$250k-$500k|7.5% - 12.5%|
|$500k-$1M|5% - 10%|
|$1M-$5M|4% - 8%|
|$5M-10M|3% - 7%|
|$10M-50M|2% - 6%|
|>$50M|1% - 5%|

Percentage fees work for pure financial distribution, but projects like [Pairwise](https://gov.gitcoin.co/t/the-epic-awards-ethereum-people-s-choice-awards-powered-by-pairwise/23033) which are trying to distribute other forms of capital (e.g. Reputation via an Award Ceremony) are capital efficient, but can't operate in a capital efficient way if they have to increase pool size to make the cost of operation work.

-------------------------

deltajuliet | 2025-08-20 01:00:51 UTC | #14

Happy to see the discourse happening on funding our community and partners in the most equitable way. 

One thing I'm missing from all these proposals/forked structures is what this looks like for the longevity and financial viability of the organization. Are we supporting fair fees at the detriment of our own matching pool? Does this affect the number of rounds that Gitcoin can run in a year? How many rounds? What is the return to Gitcoin in the future for supporting this? 

.. (*the answer is absolutely yes*) but I'm commenting specifically to encourage the community to open up the lens of what fair fees mean for projects to what that means for everyone, including Gitcoin and the ETH community.

-------------------------

owocki | 2025-08-20 05:42:46 UTC | #15

[quote="deltajuliet, post:14, topic:22560"]
… (*the answer is absolutely yes*) but I’m commenting specifically to encourage the community to open up the lens of what fair fees mean for projects to what that means for everyone, including Gitcoin and the ETH community.
[/quote]

does the foundation disclose the treasury balances and amounts and financial monitoring of the DAO ? if you are suggesting people do an analysis of how much this taxes the treasury, linking this information would enable them to do that.

[quote="deltajuliet, post:14, topic:22560"]
Are we supporting fair fees at the detriment of our own matching pool?
[/quote]

i dont see an ethical or responsible or sustainable alternative to compensating our domain operators and software provider network. do you?

i think gitcoin 3.0 with fair fees is much much more capital efficient than gitcoin 2.0 was.

the dao was paying $250k/mo for software and round ops for GG2.0/Grants Lab.  Im not super worried about paying $150k`*`/every 6 months for software/round ops for Gitcoin 3.0, esp if its driving innovation in the market and (if GItcoin 3.3 is ratified) upside for Gitcoin.

`* assumes $1.5m/6 months deployed with 10% of fair fees.`

-------------------------

deltajuliet | 2025-08-22 00:17:50 UTC | #16

> does the foundation disclose the treasury balances and amounts and financial monitoring of the DAO

The DAO reports quarterly, and @Avantgarde does monthly - yup! 

[Gitcoin Matching Pool](https://intel.arkm.com/explorer/address/0xde21F729137C5Af1b01d73aF1dC21eFfa2B8a0d6) : 5,250,343.04
[Avantgarde Managed Funds - Diversification](https://dune.com/avantgardefinance/gitcoin-mp-report-aum) : $14,270,000.00

[Gitcoin Treasury - Timelock](https://intel.arkm.com/explorer/address/0x57a8865cfB1eCEf7253c27da6B4BC3dAEE5Be518) : $2,301,068.28
[Avantegarde Managed Funds - Diversification](https://app.enzyme.finance/vault/0x0f41351921ede8e61071f48fed253d96760720dd) : $5,521,077.82

-------------------------

owocki | 2025-08-30 15:19:39 UTC | #17

i would love to bring this to a vote soon @MathildaDV ! wdyt?  i think we can take the top 1-3 fair fee models and vote on them (or vote not to do fair fees at all).

i also just posted https://gov.gitcoin.co/t/temp-check-gg24-investment-committee/23445 - between fair fees and inidividual investments in high upside teams in gg24 i think there will be some interesting funding experiments happening.

-------------------------

MathildaDV | 2025-09-01 12:45:10 UTC | #18

Yes I will prepare this and let's take this to a vote this week! Agree on the top 1 - 3, as that seems fair to vote on the various models.

-------------------------

vporton | 2025-09-06 03:32:33 UTC | #19

[quote="owocki, post:1, topic:22560"]
Adopt the following formula to compute fees on a domains matching pool size (N):
[/quote]

What is N? What is the unit of measurement of N?

-------------------------

owocki | 2025-09-10 17:42:23 UTC | #20

[quote="vporton, post:19, topic:22560"]
What is N? What is the unit of measurement of N?
[/quote]

its the domain matching pool size, measured in $$$

-------------------------
