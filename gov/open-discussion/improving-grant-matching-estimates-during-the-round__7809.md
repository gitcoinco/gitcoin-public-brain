---
id: 7809
title: "Improving grant matching estimates during the round"
slug: improving-grant-matching-estimates-during-the-round
category: open-discussion
url: https://gov.gitcoin.co/t/improving-grant-matching-estimates-during-the-round/7809
created_at: 2021-07-07T21:47:01.566Z
last_posted_at: 2021-07-11T19:08:42.846Z
posts_count: 3
views: 3453
like_count: 14
---

# Improving grant matching estimates during the round

<https://gov.gitcoin.co/t/improving-grant-matching-estimates-during-the-round/7809>
UBIpromoter | 2022-05-28 15:38:59 UTC | #1

I would like for the Gitcoin Stewards to tackle the problem of improving grant matching estimates during the round.
This has been one of my biggest frustrations over the past year and I have seen many projects impacted.

I see two main problems:

* Grant Recipients are given inflated estimates of expected matching during the round.
* Grant Makers are given inflated estimates of how much matching their donations will earn for recipients.

**Grant Recipients**
Early in the round, the estimated matching calculations are generous and move up quickly as donations come in.

But once saturation happens it is very hard for most projects to maintain their matching numbers even if donations continue to come in at a healthy pace.

I have only paid close attention to a few grants, but in all of those cases, the final QF matching has always ended up lower than the midpoint estimate despite the donation $s being much higher by the end. In most cases the Total (donations + matching) is less by the end of the round than the Total at the halfway point of the round.

I think we can and should do a better job estimating the QF matching.
I expect the smart thinkers and coders here can come up with something simple and elegant that would be much closer to reality.

The first solution that jumps to my mind is to use the past rounds as a guide to likely future flows of donations.
I suspect that if we graphed the flow of donations over the last few rounds that we would see a roughly similar trend (by percentage terms over the course of the round).
For example something like: by day 1 we see ~20% of donations, day 3 ~25%, day 10 ~60%, day 14 100%.
If we know we are very likely to reach saturation around day 10, that expectation should be reflected in our ‘estimates’ at all prior points.

Perhaps we should only base the estimates on the portion of the grant funding that we expect applies to the number of days that have passed.
It would not be perfect, but it would be closer to reality and would get ever more accurate as the round progressed.

**Grant Makers**

I don’t understand why, but it seems we are showing granters overly optimistic estimates for how much QF matching their donations will earn.

The site shows user a nice little guide suggesting how much matching would go to a $1 contribution or a $100 contribution.

But late in the round these $1 estimates often show hefty estimates that make little sense.
At this point most grant’s total estimated matching is going down every hour.

For example, late in the round on the BrightID grant I took a screenshot, it was showing a $17 QF estimate on $1.
This despite the fact that the matching at that point matching was running <2:1 with a $3 average donation.
As generous donations continued to pour in, the estimated matching continued to fall.
![BrightID Grant|266x267](upload://9GZforwNPgTmlLO4LkhSeJhrJPK.jpeg)
Many other grant see this same dynamic every round.

I love Gitcoin’s QF grant rounds.
And I believe we can come up with better estimates to give both donors and recipients.
I look forward to hearing other’s thoughts on this problem set and working on a team to help improve things.

-------------------------

chanmayson | 2021-07-09 05:54:27 UTC | #2

加油！我支持这个捐赠行动！最好要公布捐赠项目阶段性进展，最好是定期公布项目进度、捐赠资金的使用情况、还有项目下一步的实际计划

-------------------------

owocki | 2021-07-11 19:10:20 UTC | #3

Here is some data that can inform this discussion.  

How match estimates changed over time during GR10, by round.

`https://gitcoin.co/grants/stats`

Also click to the 'Stats' tab of any grant you own to see some data about how your grant has performed on a few KPIs.

-------------------------
