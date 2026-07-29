---
id: 20208
title: "Gitcoin Grants 23: Setup & Evaluation Process"
slug: gitcoin-grants-23-setup-evaluation-process
category: gitcoin-grants
url: https://gov.gitcoin.co/t/gitcoin-grants-23-setup-evaluation-process/20208
created_at: 2025-03-25T23:25:41.142Z
last_posted_at: 2025-04-03T08:05:27.117Z
posts_count: 5
views: 2240
like_count: 19
---

# Gitcoin Grants 23: Setup & Evaluation Process

<https://gov.gitcoin.co/t/gitcoin-grants-23-setup-evaluation-process/20208>
MathildaDV | 2025-03-25 23:25:41 UTC | #1

# Gitcoin Grants 23: Setup & Evaluation Process

Gitcoin Grants 23 (GG23) will run from April 2 - 23, and we’re excited to share the process we’ll use to determine and ratify final matching amounts across the program. As we continue to improve our funding rounds with a focus on transparency, integrity, and community impact, this post outlines how we set up GG23, how results are evaluated, and the methodology used to finalize the distribution of matching funds.

## TL;DR

* GG23 includes both Program Rounds (curated by Gitcoin) and Community Rounds (run by ecosystem partners).
* Matching amounts were distributed using a Sybil-resistance-enhanced Quadratic Funding model, supported by COCM (Connection-Oriented Cluster Matching) analysis.
* A COCM calculator is used after the round is complete to finalize results, which is then posted to the forum for community input over the course of 1 week.

---

## How We Set Up the Rounds

GG23 featured a total of 10 rounds, including:

* 4 Program Rounds: OSS Program, led and curated by Gitcoin.
* 6 Community Rounds: Designed and run by ecosystem partners, and partly funded by Gitcoin. *Additional rounds will run that weren’t directly funded by Gitcoin.*

### Matching Pools

* Total GG23 Matching Pool: $1.348M
* OSS Program Matching: $1.2M
* Community Rounds Matching: $130k
* Experimentation for [GTC Utility](https://gov.gitcoin.co/t/gtc-utility-experiment-for-gg23/20044): $18k

---

## How We’ll Evaluate Results

At the close of the round, Gitcoin applied a rigorous evaluation process to ensure fair and credible distribution of matching funds:

Quadratic Funding

In GG20, we introduced a two-pronged sybil analysis strategy, outlined in detail [in this post.](https://gov.gitcoin.co/t/our-sybil-resistance-strategy-for-gg20/18524) It has shown to be incredibly effective as a strong strategy in our Quadratic Funding rounds. We will continue to drive forward with this strategy for GG23, finalizing each of the above rounds using the calculator that uses the approach of combining Passport’s Model Based Detection and COCM.

TL;DR:
Passport’s MBD:
This system analyzes the on-chain history of addresses and compares it to the historical data of known human and sybil addresses. Based on this comparison, the model assigns each address a score ranging from 0 to 100, where a score closer to 0 indicates a higher likelihood of the address being a sybil, and a score closer to 100 suggests a higher probability of the address belonging to a genuine human user.

COCM:
COCM takes Quadratic Funding (QF) to the next level by tackling its biggest challenge—manipulation through fake accounts and coordinated groups. By analyzing how connected donors are, COCM ensures that projects with genuine, diverse community support get the most matching funds. This method not only promotes fairness but also reflects the true values of the community, giving round operators more accurate insights into what their network really supports. [Read this blog post](https://www.gitcoin.co/blog/leveling-the-field-how-connection-oriented-cluster-matching-strengthens-quadratic-funding) for more in-depth information.

Calculations using the COCM calculator occur directly after the round has been completed, where we use these insights to make an informed decision on how best to distribute funds. If there are any projects that need to be excluded due to them breaking any of our core [eligibility criteria rules](https://gov.gitcoin.co/t/gg23-oss-program-eligibility-criteria/20072), we will do this manually. After this is completed, the results are posted to the forum in roughly a week after donations end. The results will open for comments for a week before payouts are conducted.

### Retro Funding

$600k towards a curated round of 30 top OSS projects.

More details on the OSS Program eligibility can be found [here](https://gov.gitcoin.co/t/gg23-oss-program-eligibility-criteria/20072).

The Retro Funding round for GG23 was designed to support high-impact, mature projects based on their historical contributions to Gitcoin Grants and OSS.

For this round, a curated selection of 30 projects was identified using a force-ranked Elo rating system. This ranking was based on matching amounts received across at least 3 OSS rounds between GG18 and GG22. The goal was to recognize projects with sustained impact and strong community support over time. More in-depth details of this will be posted this week by the Open Source Observer team.

This is a metrics-based round, where we will provide metrics for the voters to make their decisions.

We are implementing a tiered badgeholder system for voting on Retro Funding allocations. Each tier will be weighted appropriately, with “experts”[ weighted the highest](https://gov.gitcoin.co/t/gg23-supporting-builders-at-every-stage-of-growth/20024) in voting.

Once voting is concluded, we will work closely with Open Source Observer to finalize the results, equally posting these to the forum for community input before conducting payouts.

### GTC Utility Experiment

We will include a retrospective of how the experiment went and what the outcomes were.

---

## ✅ How We Make Final Decisions

The final matching amounts reflect the outcomes of:

1. Unadjusted QF results
2. COCM-adjusted matching calculations
3. Manual review and edge-case decisions

We followed Gitcoin's values of transparency, fairness, and credible neutrality throughout the process. Where significant matching reductions were made, those decisions were documented and communicated with round operators and projects.

These final matching amounts are now being proposed for ratification by the community. Once ratified, funds will be distributed via the Gitcoin Grants protocol to all eligible grantees.

---

## Next Steps

* Community [pre-ratification of the GG23](https://gov.gitcoin.co/t/gg23-pre-ratification-proposal/20136) matching amounts is now open.
* If you have questions or feedback on the process, please share them in the comments below.

-------------------------

wasabi | 2025-03-26 01:53:29 UTC | #2

Thank you so much for this detailed post outlining the process for GG23; super bullish :rocket:

The introduction of a Retro Funding Round for Mature Builders reinforces the fairness and improves the COCM distribution of the QF Rounds :clap:

-------------------------

Hydrapad | 2025-03-27 04:55:26 UTC | #3

This is Amazing !! :clap: 
Must say too many things to follow !! How can we make things scalable and simple :pray:

-------------------------

MathildaDV | 2025-03-27 22:02:13 UTC | #4

[quote="Hydrapad, post:3, topic:20208"]
Must say too many things to follow !! How can we make things scalable and simple :pray:
[/quote]
Ha! This is what running a round in the background looks like! Where we may simplify we do and we will, but overall these rounds are complex and it has many, many pieces! That being said it's always my goal to work closely with the community to ensure we provide more clarity and spaces for input where there are gaps.

-------------------------

MarcVlad | 2025-04-03 08:05:27 UTC | #5

Thanks for the infos and supporting builders!

-------------------------
