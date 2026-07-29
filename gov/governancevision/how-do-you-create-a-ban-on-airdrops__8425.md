---
id: 8425
title: "How Do You Create A Ban on Airdrops?"
slug: how-do-you-create-a-ban-on-airdrops
category: governancevision
url: https://gov.gitcoin.co/t/how-do-you-create-a-ban-on-airdrops/8425
created_at: 2021-08-29T05:58:55.365Z
last_posted_at: 2021-09-10T11:32:41.317Z
posts_count: 12
views: 3547
like_count: 54
---

# How Do You Create A Ban on Airdrops?

<https://gov.gitcoin.co/t/how-do-you-create-a-ban-on-airdrops/8425>
tra38 | 2021-08-29 06:01:05 UTC | #1

Recently, I suggested [banning GTC airdrops from the Gitcoin governance process](https://gov.gitcoin.co/t/proposal-to-adjust-code-of-conduct-wrt-airdrops/8383/6?u=tra38). Airdrops have the potential to incentivize bad behaviors (such as contributing to a grant in the hopes of receiving an airdrop in the future), and it may be better to remove said incentives outright.

However, when I started trying to type up a formal proposal for this ban on airdrops, I realize that such a ban would not be "enforceable"...assuming that all proposals are passed by a simple majority. Today's proposals cannot (and probably should not) bind the future community. So any future proposal to create an airdrop could simply include additional text to repeal all existing bans on airdrops. A ban on airdrops would therefore be toothless, and thus not worth the time of the community to vote on.

What could be done instead is to create a proposal that mandates that any proposal to create an airdrop must receive a supermajority of votes (like, say, 2/3rd majority), rather than a simple majority. If the future community does feel that an airdrop is necessary, the future community must prove it by getting enough votes to reach that supermajority threshold. This should prevent the ban on airdrops being repealed by a simple majority...but it does seem unfair to have a simple-majority proposal require a supermajority of votes to overturn. Would I therefore need to subject my own "ban" proposal to that same criteria (must receive the same supermajority of votes to be enacted)?

Or are there any other way to ban or restrict GTC airdrops that I am not thinking of?

-------------------------

owocki | 2021-08-29 13:48:19 UTC | #2

Sidestepping the convo about *whether its a good idea or not to "ban" airdrops* to talk tech for a bit:

Building MACI (   https://appliedzkp.github.io/maci/ ) into Gitcoin Grants would be one way.  Basically this infrastructure makes it impossible to know WHO is contributing to each grant -- but the QF matching coordinator can still calculate the matching totals with zero knowledge proofs.

@auryn is prototyping such a system with CLR Fund. There is actually an open proposal to give them a grant => https://snapshot.org/#/gitcoindao.eth/proposal/QmZYrZKBaExvZsnNNfKbFixJe2C7PNY96DtoF1tQtdNhLN

-------------------------

auryn | 2021-08-29 14:04:10 UTC | #3

It's worth clarifying what is hidden and what is visible.

All contributions to the matching pool are visible. Although you could use something like Tornado Cash or Umbra to mask this.

All contributions to the round are visible, these are not at easily masked.

Allocations within a round are secret.

What does that mean in practice?

Let's say I contribute $30 to project A and $10 to project B. An outside observer can see that I contributed $40 to the round, but cannot know which projects I contributed the funds to and with what ratio.

So this effectively stops rewards/airdrops based on contributions to survive rounds, but not rewards/airdrops for contributing to the matching pool or the round a whole.

-------------------------

tra38 | 2021-08-29 17:21:18 UTC | #4

> So this effectively stops rewards/airdrops based on contributions to survive rounds, but not rewards/airdrops for contributing to the matching pool or the round a whole.

It is this latter issue (rewards/airdrops for contributing to the matching pool) that I'm trying to regulate. I'm starting to think though that as long as all contributions are made public, attempting to regulate these types of rewards/airdrops would be foolhardy. Even if it was possible to prohibit the Gitcoin governance process from doing these rewards/airdrops, another entity could simply do them "on their behalf".

-------------------------

auryn | 2021-08-29 20:54:58 UTC | #5

What negative outcomes are you hoping to avoid?

When you talk about rewards/airdrops, are you imagining a specific token or entity?

-------------------------

tra38 | 2021-08-29 21:23:26 UTC | #6

The negative incentive had been detailed before by @owocki [here](https://gov.gitcoin.co/t/proposal-to-adjust-code-of-conduct-wrt-airdrops/8383).  Specifically, I want to avert the following scenario: "Person X contributes to get formal compensation (tokens, access to service, etc.) from the project".

This is considered bad behavior (likely because that person's contribution will be expensive and would probably be of lower-quality than contributions based on more altruistic motivations). There's a lot of commentary about trying to discourage this behavior. However, the commentary in question (changing the code of conduct, internet memes, etc.) only regulates the discourse - what is said publicly. It doesn't actually stop the incentivizing behavior itself. If someone is motivated to contribute in return for compensation, they will do so whether they post in a Discord channel or not.

As long as said formal compensation is still theoretically possible, there *will* be an incentive for people to contribute simply to receive compensation in the future, even if it is unclear when or if it will come. It may even lead into certain people who desire compensation instinctively backing any proposal that promises them compensation, regardless of its merits.

Only a limitation on compensation itself could address the underlying issue. If it is made clear that no compensation is possible, then this bad behavior will not exist. At this point though, I don't know how one would be able to make that guarantee.

> When you talk about rewards/airdrops, are you imagining a specific token or entity?

When I first posted this thread, I was thinking about Gitcoin Governance giving out GTC to certain parties as a reward for their previous contributions. This could have been generalized to any organization giving out any sort of reward to people based on what they did in the past.

-------------------------

auryn | 2021-08-30 14:22:01 UTC | #7

Ok, I understand what you're saying.

Personally, I think that "banning" airdrops is pointless, for the reasons you already mentioned; even if the DAO bans it today, nothing stops it changing it's collective mind tomorrow.

The more important thing is norm and expectation setting.

It should be clearly communicated that contributions to the matching pool are altruistic donations to public goods. There should be no expectation of compensation, recognition, or reward. Anyone who expresses disappointment at this should be corrected and redirected to the prior and clear communication of this.

If some choose to withhold their contributions because of this, so be it.

-------------------------

lefterisjp | 2021-08-30 15:22:30 UTC | #8

You can't ban airdrops based on publicly available data. MACI is one thing you can do.

So many projects, including gitcoin, have done it that by now it's considered standard.

But I **hate** the problem it has created with people coming in discords of projects they donated and asking "when the payout is".


Perhaps the way around this is:

> It should be clearly communicated that contributions to the matching pool are altruistic donations to public goods. There should be no expectation of compensation, recognition, or reward. Anyone who expresses disappointment at this should be corrected and redirected to the prior and clear communication of this.

As Auryn suggests.

-------------------------

ceresstation | 2021-09-03 23:20:03 UTC | #9

+1 I think @auryn has the right idea here, setting clear expectations for users and to making sure to direct people to the rules would help a lot.

@Yalor @Pop maybe we can add a note on airdrops to the governance guide / code of conduct too?

-------------------------

bobjiang | 2021-09-04 13:56:45 UTC | #10

Hi Scott,

Agree with you to add code of conduct for Gitcoin community.

-------------------------

Pop | 2021-09-08 08:57:28 UTC | #11

Adding section to guidelines now :ballot_box_with_check:

-------------------------

tjayrush | 2021-09-10 11:39:47 UTC | #13

There's two issues here I would like to add:

1. We should distinguish between airdrops or rewards given by the 'matching donors' and those given by 'grant recipients.' It's perfectly legitimate for matching donors to offer rewards as a way to incentivize regular people to donate more. This is identical to what happens in the real world when, for example, a rich donor doubles every donation given by the general public. This type of 'reward' has no negative effect on the outcome of the QF mechanism. In this case, I consider GitCoin itself to be a matching donor. I think it's fine for GitCoin to incentivize donations by airdropping GTC. The type of rewards we need to address are rewards given by grant recipients to their donors. These type of rewards have a negative effect on the QF, and are, in essence, bribes.

2. The second point I want to make is that if the solution we come up with destroys the most important aspect of QF (its openness), we will have created the wrong solution. If, by fixing the "we should ban airdrops" problem, we destroy the "outside observers can verify the mechanism without permission" we will have killed the baby in its cradle. Any of these "we the people all working together"  mechanisms  (which QF is), must always support "...and we believe it works as designed because we can see how it behaves without asking permission."

-------------------------
