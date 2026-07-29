---
id: 9559
title: "Grant round analysis"
slug: grant-round-analysis
category: open-discussion
url: https://gov.gitcoin.co/t/grant-round-analysis/9559
created_at: 2021-12-30T08:15:54.804Z
last_posted_at: 2021-12-30T08:15:54.884Z
posts_count: 1
views: 2561
like_count: 1
---

# Grant round analysis

<https://gov.gitcoin.co/t/grant-round-analysis/9559>
bizzyvinci | 2022-05-28 15:39:00 UTC | #1

This is in response to this [bounty](https://gitcoin.co/issue/gitcoinco/skunkworks/252/100027341) to analyze gitcoin grants.

My analysis is a jupyter notebook in this [github repo](https://github.com/bizzyvinci/Gitcoin-grant-round-analysis) or [google colab](https://colab.research.google.com/github/bizzyvinci/Gitcoin-grant-round-analysis/blob/main/analysis.ipynb) and it consists of 2 stages.

The first stage looks for the trends from `GR1` to `GR12`. It is obvious that things are getting bigger and bigger such as number of grants, match amount, contributions and total funds. I also included the average total funds raised and how categories and regions have evolved. Then there's wordcloud to visualize vocabulary of grant titles.

![gr_category|689x233](upload://hWZ5lFeb943daCbreivFVTiA1z5.png)


The second stage is to compare quadratic funding (QF) with a single pool for GR12 with category funding (CLF) in GR11 and GR10. The first discovery is that there are a lot of grants that raised $0 in total. This was a point raised [here](https://gov.gitcoin.co/t/proposal-gitcoin-gr12-matching-pool-allocations/9007/2?u=bizzyvinci) about large skew or variance in the amount raised by grants as we see the match amount, contribution, and total raised by  a single project reach their peak in GR12.  

![qf_vs_clf|690x244](upload://47K0jvFnoujH7zPPpP5K8dh04o0.png)
![qf_vs_clf2|690x249](upload://3vdh5OPeT3Aa6X6z02VwTwBc7Mf.png)

The analysis resolves the debate about whether there would be skew or not in this [post's](https://gov.gitcoin.co/t/proposal-gitcoin-gr12-matching-pool-allocations/9007) comments.  It is important to note that funds were distributed between various categories and regions, it is some individual projects that were hurt. There's a talk about variance for public good funding [here](https://vitalik.ca/general/2021/11/16/retro1.html) and it seems that's the essence of quadratic funding. But I think there's probably a need for discussion on how a large number of projects had 0 contributors and therefore 0 funding and if a large skew is what we want.

Please note that the GR12 with 0 total are empty in the original [dataset](https://docs.google.com/spreadsheets/d/1OsJ_nmN9mN-i_9h3Yj2mDfjvtsP1qvv3B1zcpER62dk/edit#gid=1223173410) (as I filled `Nans` with 0). But they have 0 `num_unique_contributors` and $0 `match_amount` (and somehow have 1 or 2 `num_contributions`). So clarity from @owocki would be needed.

-------------------------
