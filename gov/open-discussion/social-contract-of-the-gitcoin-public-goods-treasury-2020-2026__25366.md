---
id: 25366
title: "Social contract of the gitcoin public goods treasury [2020 - 2026]"
slug: social-contract-of-the-gitcoin-public-goods-treasury-2020-2026
category: open-discussion
url: https://gov.gitcoin.co/t/social-contract-of-the-gitcoin-public-goods-treasury-2020-2026/25366
created_at: 2026-08-31T06:30:15.712Z
last_posted_at: 2026-08-31T06:31:38.271Z
posts_count: 2
views: 10
like_count: 0
---

# Social contract of the gitcoin public goods treasury [2020 - 2026]

<https://gov.gitcoin.co/t/social-contract-of-the-gitcoin-public-goods-treasury-2020-2026/25366>
owocki | 2026-08-31 13:35:30 UTC | #1

the objective of this post is to make the history of the contours of the social contract of the gitcoin public goods treasury legible to Transition Stewards.

the original social contract was

> multisig is setup w the social contract "this $$$ is for public goods" ....
>
> [@owocki, sept 1 2020](https://x.com/owocki/status/1300794815055970304)

that's the whole thing. the grants multisig (`0xde21F729137C5Af1b01d73aF1dC21eFfa2B8a0d6`) was deployed in august 2020 and announced on sept 2, one day after that tweet, with the first funds deposited inside a week. the original keyholders were hudson jameson, david hoffman, eric conner (econoar), anthony sassal, and owocki, running 3-of-5.

not one of those humans is load-bearing today. by nov 2021 had rolled off, and the question put to the forum was whether to rotate the keys to top stewards (trent, austin, linda, lefteris) or move everything into the dao timelock. it became a ship of theseus after that, every plank swapped, governed by gitcoin dao rather than by five guys who knew each other. the sentence outlived all of its original signers, which is the actual test of whether a social contract is real.

the social contract held for six years without amendment.

what changed was never the contract. it was the implementation: who puts money in, what counts as a public good, who ratifies the allocation, and whether the pool is a flow-through account or a balance sheet. each era met the same promise a different way.

## 2019: the ethereum foundation writes the check

round 1 was a $25k matching pool that inspired 200 donors to add another $13k, $38k total to open source. rounds 1 through 6 came from the EF plus small donors.

ethereum's richest institution subsidizing ethereum's commons, with gitcoin running the math. at $25k nobody had to think hard about legitimacy, and the contract was met by the simple fact that the money went out the door to open source.

## 2020-2021: the funder's league

rounds 7 through 10 pulled in yearn, synthetix, chainlink, three arrows, defiance, and dozens of others. round 11 added nft drops (moonshotbots, greatestlarp) alongside vitalik's akita donation.

the sept 2020 tweet is the moment this became necessary. once the money stopped coming from one foundation, "this $$$ is for public goods" needed an enforcement mechanism, and the answer was an m-of-n multisig staffed by prominent community members rather than a centralized team.

in may 2021, gitcoin dao launched, with GTC given specific governance control over the public goods funding campaigns.  the multisig now had a deliberative body to consult.

by nov 2021 the multisig held roughly $15m, which we described then as 15 rounds forward-funded. that same post listed six real funder motivations, and only one of them was charity. "prove that ethereum can fund public goods" was on the list, so part of the pool was always a demonstration budget.

the structural fact that falls out of this era, argued by lefterisjp in the gr12 allocation thread: *"it's not the GTC holders who gave the funds to the matching pool. it's the funder's league."* governance could ratify process.

## 2021-2022: governed, then modular

gr12 removed categories and imposed a 2.5% matching cap ($25k on a $1m pool). 10 of 758 grants hit it, and $414k got redistributed to the remaining 748, worth about 1.7x their otherwise expected match (directional numbers, per the gr13 proposal's own caveat, taken before FDD removals). a redistributive norm bolted onto the qf math, ratified by vote.

at the same time cause rounds and ecosystem rounds arrived as pass-through: the sponsor funds their own pool, gitcoin operates it, the multisig balance never moves. gr15 had over $2.6m committed pre-round across the main round, 4 cause rounds ($900k+) and 13 ecosystem rounds ($1.3m+). the ratified actuals came in higher and narrower: $3.1m in combined matching pools across 12 ecosystem rounds.

so two implementations of one contract were now running under a single name. the trust (donor-given, unrestricted, held indefinitely) and the pass-through (sponsor-directed, restricted, gitcoin as operator).

## 2022-2024: the firewall gets written down

the informal promise got stated explicitly, repeatedly, in governance:

* "the Gitcoin Grants matching pool are funds that were entrusted to us by the community (separate from our treasury)" (2024 grants strategy outline)
* "We have never used matching pool funding for anything else than ... matching pool funding. it is why sponsors have shared these funds with us in the past" (krrisis, gcp-011 thread)
* "these funds were raised for our quarterly matching pools" (gg19 thread)

and gitcoin never took a cut, on connor's reasoning that matching pool funders "are not really purchasing a service they are making a generous (charitable) donation." (cgrants did carry an optional 5% donor-side fee, and that routed back into the matching pool rather than to gitcoin.)

separate safe, separate governance path, zero rake, through every budget crisis of the dao years. that's the part that makes the sept 2020 tweet more than a nice sentiment.

## 2023-2025: from checking account to endowment

gg19 in nov 2023 is the hinge. roughly 8,917 ETH / \~$16m in the multisig, $600k across three program rounds ($200k each), and m0nkeyfl0wer's proposal flipped the ask to *pre*-ratification, explicitly dropping the post-round snapshot vote so payouts could move faster. devansh mehta objected that pre-approving would lead to less vigorous community discussion of the results.

2024 then cut the OSS round to twice-yearly with a $1m target pool (up from $250k), replaced the web3 community round with up to $125k/quarter of "matching on matching," and handed eligibility to elected badgeholders.

sgtm-002 put avantgarde over the assets in dec 2024: just under $24m, over 97% in ETH, WETH and long-tail holdings including the akita, moved toward a 70/30 ETH/stables target.

this is the quietest implementation change of the six years. the pool stopped being money in transit and became a managed balance sheet with a dune dashboard. the contract still held, because yield and principal were still earmarked for grants, but "held in trust" started to mean something closer to an endowment than an escrow.

## 2025: co-funding becomes the default

gg24 inverted the ask. domains raise their own money first, gitcoin matches. allocations at launch (oct 2025, amended down from an original $1,255,000) were $1,175,000 of gitcoin match against $632,500 in third-party commits, 54% co-funded, with a matching council able to reduce or withdraw gitcoin's commitment if a domain missed 80% of its fundraising goal. those are launch allocations, not audited post-round actuals.

the 2026 strategy sets the target at 60-70% external, with gg25 aiming near 70%.

this is the pool being used as leverage rather than as the whole purse. same contract, better ratio: every gitcoin dollar now drags roughly a dollar of somebody else's into public goods.

one honest erosion, flagged by wasabi in that same thread (picking up a concern ccerv1 raised first): between $125,500 and $170,680 of the gg24 matching request was earmarked for round operations rather than grantees. "100% goes to the community" is no longer literally true, the round operations were market standard, and seen as a concession to practicality of deploying capital in market.

## 2026: yield instead of principal

the octant pilot deploys $1m from gitcoin.eth, matched by octant to $2m, into non-custodial erc-4626 vaults. only realized yield routes to matching, and principal is never spent. at 4.5% that's roughly $32k per quarter.

as of jul 23 2026 the pool holds $10,189,330, against $6,897,677 in the dao's operational treasury. the h2 2026 budget request restates the split plainly: the treasury funds opex, the matching pool funds rounds, "the matching funds will be used towards public goods, as is the mandate for the pool."

yield-powered matching is the sixth implementation of the same 2020 sentence. it just tries to make the promise perpetual rather than terminal.

## what held, what moved

held for six years: the money is not gitcoin's to spend on itself, custody sits outside the operating entity, allocation runs through a public legitimacy process.

moved constantly:

|  | who funds it | what "public good" meant | pool's form |
|----|----|----|----|
| 2019 | ethereum foundation | ethereum open source | grant budget |
| 2020-21 | protocols, whales, nft drops | ethereum + adjacent ecosystems | forward-funded multisig |
| 2022 | sponsors, pass-through | causes (climate, longevity, advocacy) | trust + pass-through |
| 2023-24 | gitcoin's own balance sheet | OSS and eth infra, narrowed | drawdown |
| 2025 | coalitions, 54% external | domains chosen by sensemaking | leverage |
| 2026 | yield on principal | TBD | endowment |

---

-------------------------

owocki | 2026-08-31 06:31:38 UTC | #2

[quote="owocki, post:1, topic:25366"]
the objective of this post is to make the history of the contours of the social contract of the gitcoin matching pool legible to Transition Stewards.

[/quote]

@MathildaDV and @deltajuliet , just yeeted this with claude to make this info legible to Transition Stewards.  i pulled a lot of the details out of my AI second brain, but this was a best effort attempt - keep me honest here if i missed anything, yall were around for a lot of this too.

-------------------------
