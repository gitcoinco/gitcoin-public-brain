---
id: 9915
title: "[Proposal] Gitcoin GR13 Matching Pool Allocations"
slug: proposal-gitcoin-gr13-matching-pool-allocations
category: governance-proposals
url: https://gov.gitcoin.co/t/proposal-gitcoin-gr13-matching-pool-allocations/9915
created_at: 2022-02-17T22:18:42.147Z
last_posted_at: 2022-03-01T04:04:52.878Z
posts_count: 20
views: 5717
like_count: 48
---

# [Proposal] Gitcoin GR13 Matching Pool Allocations

<https://gov.gitcoin.co/t/proposal-gitcoin-gr13-matching-pool-allocations/9915>
annika | 2022-02-17 22:18:42 UTC | #1

# **Summary**

This proposal looks to discuss and finalize how funding allocations for the Gitcoin Grants Round 13 Matching Pool are distributed.

After previous successful Grants Rounds, this proposal aims to continue community-owned decision making regarding the structure of the main matching pool.

# **GR12 Matching Pool Results**

### **Background**

Prior to Grants Round 12, the pool was governed by categories that assigned specific percentages of the pool to grants in specific disciplines or geographies.

In Grants Round 12, the community voted to run an experiment proposed by the Public Goods Funding workstream to test Vitalik’s theory that Quadratic Funding should be as effective at allocating funds as allocation via categories. By doing away with specific grant categories and having all grants listed together, we took a step towards simplifying and decentralizing matching. See [GR12 Matching Pool Allocations](https://gov.gitcoin.co/t/proposal-gitcoin-gr12-matching-pool-allocations/9007/7) brief for more context.

### **Results**

On the whole, the Public Goods Funding workstream believes the experiment was a success – directionally, at the very least. We believe the experiment was helpful in getting funding to more grants without complaints from top earners, and allowed us to test our assumptions about removing categories.

Barring a small [implementation error](https://gitcoin.co/blog/grants-round-12-matching-caps/) in the cap logic that was fixed mid-round, the matching cap operated as intended and resulted in a small number of high-funded grantees being capped off at the 2.5% threshold.

All of this said, it is a subjective exercise to define what success of the matching cap looks like – success will depend on one’s philosophical stance on the QF mechanism and how much, if at all, caps should be involved to achieve more democratic outcomes for the long-tail of grantees.

With that out of the way, some information for you to interpret as you please:

**The numbers:***

* In GR12, 10 of 758 grants (1.3% of grants) funded organically hit the matching cap of $25K

* The total matching funds for these 10 grants represented 25% of the entire pool (10 grants x $25,000 = $250,000 on a $1M pool), and it would have been about 64% of the pool ($664,000) if we’d had no cap

* So, as a result of the cap, $414K (= $664K - $250K) was redistributed to the remaining 748 grantees, with each grantee receiving about 1.7x their otherwise expected match as a result of this cap

See also [this great analysis](https://docs.google.com/document/d/1DntTPVP9zGJtSYGerKG8OqJ_w1_-MDTHzF7WCT4yghw/edit) by FDD contributor @kylin on matching cap results.

**Note: These numbers are based on the preliminary round results as of Dec 16. They should be interpreted as directional, as they do not include removals after-the-fact by FDD.*

**And some qualitative data points:**

* The Public Goods Funding workstream did not receive complaints about the cap amount from grantees or funders

* In the [GR12 finale event](https://www.youtube.com/watch?v=W-doVjkkZbg&t=623s), Vitalik suggested the matching cap was a successful experiment, noting that “in some ways, it might even be accelerating Gitcoin finding its product-market fit”

Unfortunately, we do not have the ability to do a concrete ‘what-if’ analysis directly comparing the GR12 results under a matching cap structure versus categories, because the underlying metadata isn’t there. Grants were no longer assigned a category as of GR12 – so without manually going in and assigning a category to each of the 1,000+ grants that came in after GR11, which we have not prioritized for obvious reasons, this analysis is not possible.

So, with all of the information above – and [the full GR12 results](https://docs.google.com/spreadsheets/d/1eJ51CPSsFdNCGvezhhL5B-DiZ04jV4I4blGWFCiNCz4/edit) at your fingertips – we would love to hear from community members as to whether you agree that the cap was a success, and if & how we should continue with it in GR13.

A statement from the PGF workstream:

*We don't know for sure yet if the main pool approach works best long-term, but we do know that there were major benefits for a longer tail of grantees and that it exceeded our expectations despite bugs, and we think it's worth trying again before we drastically change course.*

# **GR13 Proposal**

The Public Goods Funding workstream proposes that the structure of the round remains the same for GR13 at a high-level.

In summary, the structure of the round will have:

* A Main Pool
* Cause Rounds
* Ecosystem Rounds

Details on each:

### **Main Pool**

The GR13 main pool will be a single matching pool fund/distribution of $1,200,000 in matching for the round. No individual grant’s matching contribution amount shall exceed X% of the overall matching pool fund (i.e., $XK) – as voted on by the community (see options below).

### **Cause Rounds**

In addition to the main pool, Gitcoin DAO will continue to leverage the multisig as a pass-through for cause rounds (aka thematic rounds), funded by external sponsors for clear sets of global public goods. As part of our work with[ Other Internet](https://otherinter.net/research/positive-sum-worlds/), we received a wide range of submissions about[ new](https://gitcoin.co/blog/seeking-a-new-kind-of-public-good-closing-the-loop/)[ types](https://gitcoin.co/blog/seeking-a-new-kind-of-public-good-honorable-mentions/) of public goods we should consider funding beyond just web3. In GR12, we experimented with rounds on climate, blockchain advocacy, and human longevity with net new funds. These cause rounds are a foray into Gitcoin moving beyond Digital Public Goods, and into Public Goods more broadly.

By all accounts, these cause round experiments were successful first tests. We raised $1.7M in matching funds across the three causes (more than the main round matching pool!), and have continued to see meaningful interest here – both from our usual Web3 partners as well as from some Web2 donors – moving into GR13.

### **Ecosystem Rounds**

Finally, the DAO will operate ecosystem rounds for groups like Uniswap and Polygon, as we have continued to do in the past. These are pass-through funds that are not drawn from the existing multisig balance.

# **Vote**

The Public Goods Funding workstream has outlined three options on which we would like the community’s input before moving to a Snapshot vote:

### **Option 1: Main Pool @ 2.5%**

Stick to exactly what we did in GR12.

No individual grant’s matching contribution amount shall exceed 2.5% of the overall matching pool fund (i.e., $30K of the $1.2M pool).

### **Option 2: Main Pool @ Different Percentage**

Stick to the GR12 structure, but with a new percentage.

No individual grant’s matching contribution amount shall exceed X% of the overall matching pool fund (i.e., $XK of the $1.2M pool).

We would like to see community members perform their own analysis & propose percentages we might try in the comments on this post.

### **Option 3: Alternative Community-led Proposal**

Gitcoin Stewards and the wider community decide on a new matching breakdown and propose such. This could include going back to categories, or something entirely new. We encourage any Steward or community member to submit their own matching pool breakdown if there are ideas!

Please submit your proposal this week so that we have sufficient time to incorporate it into the vote!

# **Next Steps**

Once we have feedback on both this and any other proposals, the Public Goods Funding workstream will gather all formal proposals and submit a Snapshot vote to decide which to move forward with.

Please do not submit a snapshot vote for your proposal specifically! This just adds confusion and makes it harder for the community’s voice to be heard effectively.

-------------------------

seanmac | 2022-02-18 17:23:16 UTC | #2

[quote="annika, post:1, topic:9915"]
as a result of the cap, $414K (= $664K - $250K) was redistributed to the remaining 748 grantees, with each grantee receiving about 1.7x their otherwise expected match as a result of this cap
[/quote]

This is a very helpful stat. I like that more builders are benefiting with the cap in place, while the big projects are still doing very well. 

There are a few goals that are sometimes in tension here: 
1) to support builders working for the open internet & the open economy... (more grants getting ~$5k/quarter)
2) to allow the community to decide what projects are most deserving of matching funds (supports a less restrictive cap)
3) to increase scale/impact of grants, which requires building awareness, comprehension & support for QF/grants as a credible mechanism for allocating funds (simpler is better)

To me, the 2.5% cap and this structure strikes approximately the right balance between these goals.

-------------------------

socal434 | 2022-02-18 20:15:18 UTC | #3

I second this sentiment. Having the 2.5% helps to spread the wealth without totally limiting the bigger projects that have the ability to generate more hype through social media than the smaller or newer projects.

-------------------------

ceresstation | 2022-02-21 15:01:59 UTC | #4

Would love to get the broader steward community's view on this of course, but personally I want to echo the sentiment that Option 1 or Option 2 makes sense for GR13. 

In particular:

1) I agree with @seanmac that it helps give a larger pool of builders the chance to raise sustainable funding; and that
2) it helps us in turn scale the number of grantees that will be comfortable sticking around in following rounds without needing to scramble and look for funds elsewhere

The case for Option 1 specifically for me comes down to the fact that we aren't just funding public goods but running experiments in how these goods should be funded. To make sure we're getting all the data we need, we should at least try the same options a couple of times over to make sure there are no anomalies (unless it's immediately clear that the choices made were failures, which doesn't seem to be true for GR12). 

One thing I'd eventually like to dive into deeper is how ecosystem rounds could effectively serve as a kind of replacement for independent categories, instead creating an overlapping mesh of different opportunities for grantees (e.g. we could imagine a project, like Dark Forest, that fits into a zktech round, an NFT round, and a gaming round). As @owocki has mentioned, QF can stack:


![b606ff5a76790c5460a740cf9febb7a0826f5bd7_2_1380x862|690x431](upload://rdQqK29JHYMtFauMOw9KfKg2Mwq.png)

However, this progression is already happening naturally, and is fully compatible with Option 1.

**TL;DR:** As always should be making sure we get the experiments we run right, and so pushing forward with Option 1 to measure twice / cut once would be my choice.

-------------------------

bobjiang | 2022-02-22 07:42:14 UTC | #5

First congratulations for the huge success in matching cap in GR12, you and the team did great! @annika 

I would support Option 1 (continuously) or Option 2 (if we could have another N% suggested, like 2%?)

I am not sure what's the impact if we choose 2%, could anyone simulate with GR12 data?
if we could have some detailed data, comparing 2% with 2.5% (existing), I would make a choice.

Anyway, I am open to have other proposal for matching pool distribution.

-------------------------

connor | 2022-02-23 00:21:26 UTC | #6

Thank you for this extremely thorough write-up @annika! It very clearly lays out the results of the last round, and the justification for this GR13 proposal.

Personally, I am in favor of option 1 - the 2.5% cap did a great job of distributing funds more widely to aspiring projects, and it would be great to gather more data using this same benchmark. If the community did opt to go for option 2 and try a different percentage, my feeling is that percentage should be smaller than 2.5%, not higher. But for consistency and simplicity, I'd love to see us go for option 1. 

I also appreciate how you laid out the differences between the main, cause, and ecosystem rounds. Looking forward to experimenting further with these alternate matching pools in the near future.

-------------------------

Fishbiscuit | 2022-02-23 06:18:13 UTC | #7

[quote="annika, post:1, topic:9915"]
GR12 Matching Pool Allocations
[/quote]

For this proposal I think that Option 1 is reasonable as I agree that this format would help more builders in the space.

However, there are potentially many new ways to experiment with grant funding mechanisms and it might be interesting to see how Uniswap or Polygon (or other ecosystem round funders) might want to try different grant funding mechanisms in the future to help nurture key projects in their own ecosystems. As a grant funder, they might have different funding priorities such as [Polygon's focus areas](https://gitcoin.co/blog/polygon-creating-ecosystem-match-pool-for-gr12/) when kickstarting their ecosystem round and designing a grant allocation mechanism that coordinates funding to these focus areas could become a new feature of ecosystem rounds too.

-------------------------

tjayrush | 2022-02-23 13:32:03 UTC | #8

This is great. Thanks so much for putting it together.

I too support the cap. The choice of percentage is hard to make, of course. Sticking with the existing percentage (2.5%) seems totally reasonable.

One thing we might anticipate, though, is that, as the total amount of matching funds goes up, we may wish to impose a hard-number limit as well.

So perhaps, the cap becomes something like, "2.5% with an absolute max of XX US dollars."

In this way, as the amount of matching funds increases, more small projects would get more funding and the projects that are hitting the max are still doing very well (depending on XX).

If a project is getting a couple of hundred thousand dollars per quarter (at some point in the future), I would argue that they should use some of those funds to hire a business consultant to figure out how to monetize.

I much prefer a broad distribution than a concentrated one in the long run and 2.5% is totally arbitrary after all.

-------------------------

kyle | 2022-02-23 23:29:44 UTC | #9

[quote="annika, post:1, topic:9915"]
The GR13 main pool will be a single matching pool fund/distribution of $1,200,000 in matching for the round.
[/quote]

I appreciate the post and thoughtful nature of the options. I would advocate we hold the round at $1MM given the market turbulence and the increased funding in the cause rounds. This is mostly an intuition thing from many rounds before, but I figured I would flag that for thoughts.

[quote="annika, post:1, topic:9915"]
Option 2: Main Pool @ Different Percentage
[/quote]
I was originally going to propose a smaller cap (1.5%) based on the work from Kylin, but Scott's thoughts below have left me conflicted. I like the idea of not changing too much too quickly. So I will hold on that being a formal reccomendation.

[quote="ceresstation, post:4, topic:9915"]
To make sure we’re getting all the data we need, we should at least try the same options a couple of times over to make sure there are no anomalies (unless it’s immediately clear that the choices made were failures, which doesn’t seem to be true for GR12).
[/quote]

One last thought - Gitcoin had been a beacon for funding when others were not offering funds. This enabled sustenance for many projects that have now grown immensely. I am continuing to think about we encourage new projects in the space to find their footing using a Gitcoin Grant, and to reward well established projects less and less.

Something to consider on the product side, is to evaluate if longevity of a project is worth factoring in. ie, projects formed in the last 6 months have a cap of 2.5% projects over 6 months in tenure have a 2% cap and projects over a year old get 1.5%.

This might help us bootstrap more projects and more innovation (though I recognize more ecosystems will fill this gap too).

-------------------------

ceresstation | 2022-02-24 06:03:18 UTC | #10

A few quick thoughts on the round amounts, although I think the other points are interesting to consider:

1) Generally, we've increased matching pool amounts for the main pool (or equivalent categories) round over round, I'm actually not sure if keeping the main pool constant has been done before but I might actually be wrong on this. 

2) Part of the reason this has been done is that each time we agree to raise the matching pool we actually move closer to our goals (across several workstreams) of scaling our impact, we shouldn't simply raise the pool to make things easier for ourselves here but we should also always err on the side of helping more grantees reach sustainability,

3) I do think it's important to figure out how to remain net zero on new funds each round, but in this upcoming round we'll be receiving approximately $1.5m in total funds from matching partners in addition to the $4m in AKITA, so I think $1.2m would be a small increase relative to new funds, if net inflows were lower (despite the macro market) I'd be more inclined to hold back.

-------------------------

annika | 2022-02-24 04:18:18 UTC | #11

Appreciate these thoughts!

**On round size:**

We did toy between proposing $1M and $1.2M before bringing forth the latter. I echo @ceresstation's points - and will add that with how main pool contributions are coming in so far, we're going to end up with a large majority of that $1.2M being net new funds earmarked specifically for GR13, which makes me feel good about the $1.2M route.

At a more macro level on round size, IMO we should find ways to be more scientific / less subjective about this for future rounds. Principally, I agree with @ceresstation that we should strive to be net zero on new funds each round. Given that we often get new contributions after this proposal is finalized, I wonder if we might shift to having the matching pool size ratified alongside payouts post-round, rather than pre-round with the allocations.

**On project longevity as an input to cap amount:**

I love this thought - given that a lot of the ethos of grants is around getting new projects off the ground, I agree that testing creative structures like this might better bootstrap early-stage innovation. Let's explore this as we plan GR14! I'll loop product in on the concept.

-------------------------

DisruptionJoe | 2022-02-24 05:38:32 UTC | #12

I agree with @ceresstation thought on continually raising the amount, especially with the commitments mentioned. 

[quote="kyle, post:9, topic:9915"]
Something to consider on the product side, is to evaluate if longevity of a project is worth factoring in. ie, projects formed in the last 6 months have a cap of 2.5% projects over 6 months in tenure have a 2% cap and projects over a year old get 1.5%.
[/quote]

This is incredibly interesting mechanism design. I really like the intention of this idea. Let's ask @kylin for any insights into how we might better understand what this might look like. 

My reservation is that we haven't done any discovery research into whether the community really wants to focus more on springboarding new grants vs continuous funding. A good way to get feedback would be the tool that Audrey Tang uses to solicit public opinion, Polis. @erich could help us set up a poll to run for a bit. Even if we don't get the answer this round, it would be great to have the insights for the next rounds decision.

-------------------------

kylin | 2022-02-24 09:37:03 UTC | #13

Thanks for putting it all together! @annika 

I would support figuring out a new percentage. 2.5% might be good, but I didn't see sufficient reasons to justify this choice. 

The aim of introducing the cap is to prevent a few grants from dominating the matching pool and letting the rest get more funds. It seems to me that the vision of the re-distribution is not clearly stated. It would be good if we can set specific goals that we want to achieve by introducing the cap, like:

1. ~$5000 is generally enough for a grant in the short term. We want to see at least the top 5% grant could hit this amount.
2. we aim to let half of the grants get at least $500 to help their development.

With some explicit criteria like these, it will be easier to determine what percentage is optimal. I am very happy to work on this if more specific goals can be available.
 
An alternative way perhaps is to let the owners of grants set up caps for themselves before a round starts - a sensible short-term amount that they will need between the current and next round. Once a grant hits its pre-specified cap,  the excess funds will be re-distributed. The advantage of doing this is each grant can have a separate cap rather than a fixed one. It seems more reasonable that projects of different scales/stages/difficulties would have different levels of caps?

@DisruptionJoe

-------------------------

DisruptionJoe | 2022-02-24 15:33:28 UTC | #14

I like your assessment of how we should approach this issue. Perhaps it is late in the game for GR13, but we could look at this as well as Kyle's idea prior to GR14. 

Maybe we could proactively assess GR13 to be able to give insights while the ops team gets input from the community using Polis to figure out what is most important.

-------------------------

erich | 2022-02-24 19:01:33 UTC | #15

Good call, Joe — here is a Pol.is conversation around the matching cap issue: https://pol.is/2n6ccsua2a. Everyone can feel free to share perspectives and vote on each other's views in that link.

Perhaps, we should also consider sharing this on social media and our Discord @seedphrase, @Fred, and @seanmac.

After two weeks or so, we can open a thread on the forum to highlight and discuss the Pol.is report with the discussion results. It will likely help us identify the related views with the most plural common ground in the community.

Let me know if you have questions.

-------------------------

David_Dyor | 2022-02-24 19:06:40 UTC | #16

I support option 1.  Love the idea of introducing a time/grant age factor.
Might as well get at least 2 rounds with same parameters so we can compare as per Scott.

I support the continued increase of the matching pool for optics.  Could do 1.1 if 1.2 seems high.
Thanks for all the discussion on this.  

And to comment on Fishbiscuit's post: I think offering more autonomy to the Ecosystem Round funders via choice on funding mechanism is very intriguing.  This ties in to some of the discussion about potentially having Ecosystem's provide their own eligibility criteria AND reviewers.  Historically most Ecosystem Funders have decided to simply use GC platform criteria & reviewers - but this is not easily scaled up or out.

-------------------------

lefterisjp | 2022-02-26 09:17:39 UTC | #17

Thank you for putting this together @annika 

I think that judging by how GR12 went the cap did not have any bad side effects and it may have indeed helped so I see no reason to experiment too much with almost no time left for GR13.
So I will be supporting option (1). Indeed the cap could change but I don't really have a good alternative suggestion. So for this round I would say we keep it as is. (Option 1).

Something I said in the previous round and I would like to revisit and saw also others suggested is to make the system a bit more modular.

In essence allow grant owners to specify how much they and their team needs for a given quarter and once that is reached that is the cap for the round. There should probably be another cap on top which should be the max they can get but I think this would optimize the rounds (assuming most grant owners are honest).

-------------------------

krrisis | 2022-02-28 23:25:47 UTC | #18

Thanks for the superclear outline & overview Annika! 

As a Steward I totally support option 1, although I'm open to support valid options that come through the community. Really a big fan of the cap, because it gets more funds to smaller projects. To be honest I hadn't seen this explained clearly before, so appreciate this. 

I also support @tjayrush's addition to add a max amount to this cap, but maybe this is only necessary at a later stage - could be good to have two identical rounds in setup to compare data, as Scott suggests.  

Very supportive of this suggestion by Kyle, as Joe echoed as well : 

[quote="kyle, post:9, topic:9915"]
Something to consider on the product side, is to evaluate if longevity of a project is worth factoring in. ie, projects formed in the last 6 months have a cap of 2.5% projects over 6 months in tenure have a 2% cap and projects over a year old get 1.5%.
[/quote]

Supportive of this suggestion as well, could liberate even more funds for smaller projects:

[quote="lefterisjp, post:17, topic:9915"]
In essence allow grant owners to specify how much they and their team needs for a given quarter and once that is reached that is the cap for the round.
[/quote]

With regard to the categories I think it's important to keep on having these clearly on the site for easy navigation (even still a lot to improve here), having all funds into one category (excl side and ecosystem rounds) makes total sense. The distinction between funding categories & thematic categories should be further clarified (although not an immediate solution there, I think it's a lot for non gitcoin people - and even gitcoin people - to wrap their heads around), good thoughts by @ceresstation on this above. 

(Just a reminder, a snapshot vote for this will suffice, as no gitcoinDAO funds will be moved)

-------------------------

bestape | 2022-03-01 00:11:33 UTC | #19

I suggest if the "longevity" cap is included, the timer should start at a certain point in a project's maturity. For instance, my Cheerbot project has been early-stage simmering for a bit, waiting for Web3 to get more involved in the Maker and IRL space. This finally seems to be happening if ETHDenver2022 is any indication! 

The more likely a project will make a big difference, because it's a major innovation or paradigm shift, the more likely it'll take time for that project to find the right moment of opportunity as the market catches up. 

I hope we don't accidentally penalize forward thinking projects that pick patience out of prudence with a one-size-fits-all longevity cap.

-------------------------

kyle | 2022-03-01 04:04:52 UTC | #20

[quote="lefterisjp, post:17, topic:9915"]
In essence allow grant owners to specify how much they and their team needs for a given quarter and once that is reached that is the cap for the round
[/quote]

I love this idea. Further, there may be a threshold that needs to be reached before any funding is given (ideally from individuals as well). 

For example, I post a project of something I am planning to do, but only commit to this idea if I can get $500 in funding. If I dont raise this amount, I will not move forward and the funds I did receive should be returned.

-------------------------
