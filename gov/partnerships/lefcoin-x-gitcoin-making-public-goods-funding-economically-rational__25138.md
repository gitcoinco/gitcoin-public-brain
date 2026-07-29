---
id: 25138
title: "LefCoin x Gitcoin: Making Public Goods Funding Economically Rational"
slug: lefcoin-x-gitcoin-making-public-goods-funding-economically-rational
category: partnerships
url: https://gov.gitcoin.co/t/lefcoin-x-gitcoin-making-public-goods-funding-economically-rational/25138
created_at: 2026-02-23T07:54:13.983Z
last_posted_at: 2026-03-01T13:20:52.736Z
posts_count: 4
views: 106
like_count: 2
---

# LefCoin x Gitcoin: Making Public Goods Funding Economically Rational

<https://gov.gitcoin.co/t/lefcoin-x-gitcoin-making-public-goods-funding-economically-rational/25138>
Lefcoin | 2026-02-23 07:54:14 UTC | #1

Hey Gitcoin community,

 

I'm Jon, founder of LefCoin (LEF) — a sentiment-indexed token on Base L2 where doing good literally pays. Ivan from the Gitcoin team suggested I bring this here to get community feedback, so here goes.

 

 

## What LefCoin Does

 

LefCoin has a built-in mechanism called the LOVE Index — a composite score (0–1000) computed from 6 subindices tracking real-world sentiment data: global peace, charitable giving, social sentiment, environmental care, community wellness, and on-chain good spending.

 

The LOVE Index directly affects the token's economics:

 

\- Every LEF transfer has a 1% fee routed to a rewards pool

\- That fee is amplified by the LOVE Index — higher index = bigger rewards for all holders

\- When the world is doing well (or when people spend LEF on good causes), everyone benefits

 

The key innovation is the GoodSpend Registry — an on-chain curated list of verified charitable destinations (charities, public goods projects, sustainability orgs). When someone sends LEF to a registered destination:

 

1\. The Good Spend subindex increases on-chain

2\. This raises the overall LOVE Index

3\. Which amplifies rewards for every LEF holder

 

Public goods funding becomes a positive-sum game at the protocol level.

 

 

## Why Gitcoin?

 

Gitcoin and LefCoin are solving the same problem from different angles:

 

\- Gitcoin uses quadratic funding to amplify community voice — small donations get matched, ensuring broad support matters more than whale dominance

\- LefCoin uses a sentiment index to make charitable giving structurally valuable — every donation to a verified destination improves returns for the entire network

 

Together, these mechanisms can create an ecosystem where funding public goods isn't just altruistic — it's economically rational.

 

 

## What We've Already Done

 

\- Gitcoin is registered as a verified GoodSpend destination in our on-chain governance registry

\- 100,000 LEF has been donated to Gitcoin's wallet on Base (BaseScan TX: https://basescan.org/tx/0x45c821e04d72b2af619f8c714602ff2f0f92e43653b7bae28f0bcf78e74035cb)

\- 11 charities total are registered, each received 100,000 LEF — including UNICEF, Internet Archive, Tor Project, Rainforest Foundation, Freedom of the Press, and Giveth

\- The oracle pipeline (18 data sources across 5 categories) is open-source on GitHub: https://github.com/j99lef/lefcoin-oracle

\- All contracts are verified on BaseScan and Sourcify

 

 

## Potential Collaboration Areas

 

I'd love community feedback on any or all of these:

 

1\. Gitcoin Grants Round — Apply for a future grants round. LefCoin's public goods mechanism could be a compelling case for quadratic funding support, and it would demonstrate real community demand.

 

2\. GoodSpend x Gitcoin Grants — Imagine if Gitcoin Grants recipients could register as GoodSpend destinations. Every LEF sent their way would simultaneously fund the project AND boost rewards for all LEF holders. Quadratic funding meets sentiment-indexed rewards.

 

3\. Gitcoin Passport Integration — We're building community governance (LoveGovernance contract) where token holders propose and vote on new GoodSpend destinations. Integrating Gitcoin Passport for sybil resistance would make this governance more robust and credible.

 

4\. Co-marketing the "public goods are economically rational" narrative — This is a story both communities benefit from telling. Gitcoin pioneered the idea that funding public goods can be sustainable. LefCoin makes it protocol-native.

 

 

## Technical Details

 

Token: LEF (ERC-20) on Base L2

Contract: 0x977c8452eEd662F9E6515Be1c5D328946520a005 (https://basescan.org/token/0x977c8452eEd662F9E6515Be1c5D328946520a005)

DEX: Aerodrome Finance (https://aerodrome.finance/swap?to=0x977c8452eEd662F9E6515Be1c5D328946520a005)

Supply: 1B fixed (no additional minting beyond reward amplification)

Oracle: 18 data sources, 6-hour update cycle, open-source

Governance: On-chain proposals, 3-day voting, 4% quorum

GoodSpend Categories: 9 (Charity, Sustainability, Education, Healthcare, Community, Disaster Relief, Animal Welfare, Arts & Culture, Other)

Website: https://lefcoin.com

 

 

## The Ask

 

I'm not here to shill a token — I'm here because LefCoin is architecturally aligned with what Gitcoin is building. The question I want the community's take on:

 

How can we best connect these two mechanisms to make public goods funding more sustainable?

 

Happy to answer any questions about the contracts, the oracle system, or the economics. Everything is on-chain and verifiable.

 

Cheers,

Jon

-------------------------

owocki | 2026-02-23 21:24:17 UTC | #2

[quote="Lefcoin, post:1, topic:25138"]
How can we best connect these two mechanisms to make public goods funding more sustainable?

[/quote]

maybe worth zeroing in on something small (but high upside) for gg25?

-------------------------

Lefcoin | 2026-02-24 12:54:56 UTC | #3

Great shout — completely agree that starting small and high-signal is the move.

For GG25, what if LefCoin contributed a matching pool boost tied to the LOVE Index? The idea: a portion of LEF rewards get directed into a GG25 round, with the amplification rate set by the live index score. Higher global positivity = bigger match.

It's small to start, verifiable on-chain, and gives both communities something concrete to point at.

Happy to scope this out properly if there's interest. What round or category would make the most sense to pilot in?

-------------------------

vporton | 2026-03-01 13:20:52 UTC | #4

Please, also think about integrating it with my project AI Internet-Meritocracy (I can't include links in posts, somebody search it in Google and follow-up with a link, please.) (I don't know in which way, I am asking your advice @Lefcoin).

It is an app that accepts crypto donations and spreads it between free software authors, scientists/researchers and marketers of science. It not only gives salary to every researcher, but also solves (multi-trillion loss in lag of science) scientific publication crisis (when good works receive not enough publicity).

My project currently is KYC authorized to send money only to people (not to organizations or AI agents), but together we could invent something, I hope. Please, think hard.

-------------------------
