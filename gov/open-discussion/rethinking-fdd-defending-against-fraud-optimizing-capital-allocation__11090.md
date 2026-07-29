---
id: 11090
title: "Rethinking FDD: defending against fraud --> optimizing capital allocation"
slug: rethinking-fdd-defending-against-fraud-optimizing-capital-allocation
category: open-discussion
url: https://gov.gitcoin.co/t/rethinking-fdd-defending-against-fraud-optimizing-capital-allocation/11090
created_at: 2022-07-11T13:39:57.118Z
last_posted_at: 2022-09-01T14:39:45.471Z
posts_count: 23
views: 5619
like_count: 47
---

# Rethinking FDD: defending against fraud --> optimizing capital allocation

<https://gov.gitcoin.co/t/rethinking-fdd-defending-against-fraud-optimizing-capital-allocation/11090>
j-cook | 2022-07-11 13:41:28 UTC | #1


## Problem Statement

***"The Fraud Detection & Defense workstream (FDD) aims to minimize the impact of fraud on our community."*** 
*[GR14 Governance Brief](https://docs.google.com/document/d/1icQzWlUafRw1rPRqzBNsk-o2sWEPJ6-seaGrLHYWTF8/edit#heading=h.ihjco4z6rry9)*

To the extent that FDD has thought about optimizing capital allocation, it has been built on top of the assumption that a Sybil-free grants round is an optimal one. However, this overlooks important factors, such as bribery or quid pro-quo among founders and voters or leveraging quadratic funding for non-monetary gains (such as attracting users/followers) and any other game-theoretic quirk of the system that causes reality to diverge from the ideal model of quadratic funding. Ultimately this challenges a foundational assumption of FDD - that a Sybil-free grants round (GR) is an optimal one.  

This means fraud detection and defense should really be **one of several foundational pillars** of the FDD stream, all of which support the general aim of optimizing the capital flow through each GR.

As [Grants 2.0](https://gov.gitcoin.co/t/gitcoin-grants-2-0/9981) approaches, and after a bruising round of [budget discussions](https://gov.gitcoin.co/t/proposal-fdd-season-14-budget-request/10658) in GR14, this seems like an opportune moment to reconfigure FDD into a more holistic operation. At the same time, one of the pertinent criticisms of FDD in the past has been that its objectives and processes have been somewhat opaque and difficult to appraise. A reconfiguration must therefore start with a clear and unambiguous definition of a specific remit, a clear set of performance indicators, and demonstrable alignment with the priorities of the wider community. 

This post is intended to stimulate discussion around evolving FDD so that it becomes more of an optimization layer than a defense widget. Rethinking FDD as an optimization layer flips the narrative from defensive and adversarial to constructive and enabling. It also provides a clear opportunity to start addressing non-Sybil inefficiencies in the grant system alongside the existing Sybil defenses.

The **tldr** for this post is that FDD should stop asking "How do we stop fraud"? and start asking **"How can we optimally allocate capital"**?


## What does optimal look like?

### Promoting the good

The optimal capital allocation does the maximum "good" with the minimum of waste. What consitutes a "good" project is highly subjective but perhaps we can define "good" as "closely aligned with the community's preferences". With some a priori assumptions about what the Gitcoin community values, we might define "good" to be something like:

`goodness = usefulness + fairness + inclusiveness + sustainability`

In reality the community's preferences are probably a dynamic cloud of concepts that shift over time but `usefulness`, `fairness`, `inclusiveness` and `sustainability` seem like core properties that can be fairly well relied upon. That said, these categories are based on my own assumptions and interpretation from my experience in FDD and it would be better to gather some baseline empirical data that demonstrates what the community really values - this could be as simple as a poll or interactive word cloud. The community values can be encoded in a set of grant eligibility requirements, as is currently managed by the "GIA" squad.

Fine tuning of the DAO's understanding of community's preferences can be achieved using repeated snapshots of the aforementioned polls/wordclouds or more formal pre- and post round surveys of applicants, reviewers and observers. These surveys should be designed in such a way as to provide metrics against which a GR can be compared post-hoc, for example:

```
I am interested in funding environmental projects:
    strong agree  agree  neither agree nor disagree   disagree  strongly disagree

I am interested in funding Ethereum infrastructure
    strong agree  agree  neither agree nor disagree   disagree  strongly disagree

etc
```

The resulting data could then provide a semi-quantitative heatmap of community interests. Grants could then be marked with complementary tags by reviewers that can then be analyzed to see if the capital was distributed in alignment with the community preferences approximated from survey results. Consequently, FDD's processes could be course-corrected to improve the allocation round-on-round. 

There is potential for round-on-round learning by updating the weightings for each of the criteria by which the "goodness" of a grant is measured according to the evolving community responses. Survey respondents would have to be anti-Sybil checked somehow - perhaps with a Gitcoin Passport. They could also be incentivized by, for example boosting their Trust Bonus for completing the survey or perhaps using monetary or non-monetary rewards (such as POAPs).

These are relatively simple steps that could be taken to ensure the processes implemented within FDD are really well aligned with the values and preferences of the DAO and the wider community.

This takes care of the "good", what about the "bad"? 

## Minimizing the bad

The "bad" is **capital going to waste**. Assuming obviously invalid or fraudulent grants are filtered out effectively by the eligibility scoring, there are two main ways capital can be wasted within a round:

1) Inefficiencies within the grant reviewing process
2) Capital capture by Sybils and airdrop farmers

At face value it is easy to reduce the cost per review - simply pay less to existing reviewers or hire cheap temps to conduct reviews. However, there is also a cost associated with low quality reviews as they either require multiple rounds of reviewing or increase the likelihood that a grants that are not "good" end up being funded, undermining one of the core principles. 

The value added by reviewing experience and prolonged active engagement with FDD has not yet been quantified, but it could be measured simply by paying for temporary reviewers to review grants in parallel to the existing set of FDD reviewers for a fixed period of time and comparing the grant outcomes. One aspect that I have not seen discussed so far is the cost associated with reviewer attrition - each experienced reviewer that becomes disatisfied and leaves presumably either increases the burden on the remainers, adding "dissatisfaction contagion" risk and accelerating attrition, or incurs a cost to train and onboard replacements. Assuming retaining experienced reviewers is a net value-add to the grant review process, the question then pivots to the best way to remunerate those reviewers without overpaying (wasting capital) and also without underpaying (risk of attrition).

Finding the **optimal incentivization mechanism** that maximizes review quality and minimizes review cost is the primary objective of the FDD "Rewards" team. In GR14 they [prototyped simulations](https://gov.gitcoin.co/t/gia-rewards-okr-report/10438) using an agent-based model to extract insights about the optimal set of conditions for grant reviewing. This used synthetic data in GR14 to develop and calibrate the model and will be fed with empirical data in the coming months. The insights from these experiments should provide an initial foot-hold into optimizing the grant review mechanism that can then be iterated on in successive rounds.

Finally, **Sybil attacks** aim to skew FDD's view of the community preferences by amplifying individuals' voting power. Minimizing Sybil attacks is therefore a way to maximize the alignment between the capital allocated and the community's preferences. Sybil attacks exploded in number in GR14 - at the same time FDD has developed real expertise in dealing with Sybil attacks over several rounds. However, there are also areas for expansion, for example tackling "airdrop farming" Sybils who are difficult to distinguish from genuine new users. This was a major issue in GR14 with the general model being that influencers rally new users to vote for a specific project on the expectation of an airdrop in return and encourage them to maximize their airdrop potential by splitting their votes across multiple wallets. This turns the users into unwitting Sybils. It is far less obvious how to classify, and how to treat, airdrop farmers that only use a single wallet - are they distinguishable from genuine new users?


## Outlook and outstanding questions

FDD could have a more holistic approach to GR security if it reconfigures with "capital optimization" as its overarching goal rather than "Sybil defense". This reconfiguration is an excellent opportunity to realign FDD with the DAO and the wider community, to set some new baselines building from empirical data and to enable closer tracking of FDDs progress against clearly defined KPIs.

The answers are not all presented in this post, it is intended to start a discussion around how FDD should configure itself going into the Grants 2.0 era. Some of the more nuanced questiions that could be pertinent to the discussion but have not been mentioned in the outline above are:

* What are the sensible KPIs FDD can define to track its own progress?

* Can an optimization framework eventually extend to allocate social, emotional, intellectual capital as well - do we get these things for free by optimally allocating monetary capital?

* How can the $GTC token fit be used to best effect in a new capital-optimization framework?

* How can we ensure FDDs capital optimization processes are transferable across rounds in Grants 2.0?

-------------------------

kyle | 2022-07-12 14:18:03 UTC | #2

[quote="j-cook, post:1, topic:11090"]
A reconfiguration must therefore start with a clear and unambiguous definition of a specific remit, a clear set of performance indicators, and demonstrable alignment with the priorities of the wider community.
[/quote]

I love the thinking here and agree with the sentiment ^^ the post lacks performance indicators, but does really help anchor us on a remit where those could be defined. I wonder if this is still presented through the lens of what FDD knows today versus where we aspire to be. FDD may have a heavy hand in Gitcoin's main round, but may see less and less involvement in other rounds as we build up tooling and processes for communities to run rounds themselves. To the quote below:

[quote="j-cook, post:1, topic:11090"]
The resulting data could then provide a semi-quantitative heatmap of community interests. Grants could then be marked with complementary tags by reviewers that can then be analyzed to see if the capital was distributed in alignment with the community preferences approximated from survey results.
[/quote]

It's unclear to me that we would want to move capital based on our communities sentiment in any round except the main round. Keep in mind that many communities bring their users to our platform, which leads me to believe those communities may not participate in our survey, but they greatly impact the funding distribution.

Overall, I feel like this is in the right direction, but may not be inclusive of the entirety of the protocol vision.

The concerns on sybil may be much smaller if we can move more towards a model that only affords a matching contribution amount based on the value of a passport (ie, the price of forgery). Airdrop farmers wont need to increase the value of their passport, but those of who care about the matching funds will (this hypothesis needs to be tested still).

All this to say - I love the idea of thinking about how can we ensure the funds are optimally allocated. I suspect there are large portions of this problem space that PGF would find in their remit today as this spans into the number of grants, the amount of capital to allocate, the quality of contributor (ie, sybil, air drop farming, altruistic).

I would love to chat more to continue to refine the thinking here.

-------------------------

ZER8 | 2022-07-12 21:44:44 UTC | #3

[quote="kyle, post:2, topic:11090"]
I love the thinking here and agree with the sentiment ^^ the post lacks performance indicators, but does really help anchor us on a remit where those could be defined. I wonder if this is still presented through the lens of what FDD knows today versus where we aspire to be. FDD may have a heavy hand in Gitcoin’s main round, but may see less and less involvement in other rounds as we build up tooling and processes for communities to run rounds themselves. To the quote below:
[/quote]

Hello, Kyle. Yes, we are aware of that, but the question is: can G2.0 builders cover the whole spectrum of issues that can occur during another round and just avoid them by design? I personally believe that we should at the very least sync with them and provide our feedback and lessons already learned. 

[quote="kyle, post:2, topic:11090"]
The concerns on sybil may be much smaller if we can move more towards a model that only affords a matching contribution amount based on the value of a passport (ie, the price of forgery). Airdrop farmers wont need to increase the value of their passport, but those of who care about the matching funds will (this hypothesis needs to be tested still).
[/quote]

The cost of forgery is only about ROI, the spectrum of grants/users that we are worried about do not care if the cost of forgery is 1000 -10000$, they only care if the return exceeds the cost and I think we should emphasize this more.

 We prevented over 100k in improper matching allocation by removing certain grants and  I really think we could really help the round owners save a lot capital, thus it's honest to assume that that capital can by used by Gitcoin DAO, Gitcoin Matching pool and/or the FDD. Ofc, this is my GIA pitch, but it has the best intentions behind it and I surely hope it will have a big impact on the matching funds in the future non-gitcoin rounds. :robot:

It would be really cool if we could share out methodology/process with the round owners(4 free, 4 a price, I guess this will be decided down the road) because they will surely saved a lot of funds and at the end of the day we all care about real web3 projects and we want capital to reach those who actually build our future. Btw, in the worst possible scenario we can  create a grant for a project like this and donate more than 50% of the funds raised back to the Gitcoin matching pool. :slight_smile: (the post is mostly about the GIA's perspective on the future of our rounds)

-------------------------

DisruptionJoe | 2022-07-12 16:45:51 UTC | #4

[quote="kyle, post:2, topic:11090"]
I love the thinking here and agree with the sentiment ^^ the post lacks performance indicators, but does really help anchor us on a remit where those could be defined. I wonder if this is still presented through the lens of what FDD knows today versus where we aspire to be.
[/quote]

Context on the motivation and intention of this post:
https://gov.gitcoin.co/t/introducing-the-fdd-review/11095

[quote="kyle, post:2, topic:11090"]
FDD may have a heavy hand in Gitcoin’s main round, but may see less and less involvement in other rounds as we build up tooling and processes for communities to run rounds themselves.
[/quote]

[quote="kyle, post:2, topic:11090"]
It’s unclear to me that we would want to move capital based on our communities sentiment in any round except the main round.
[/quote]

I don't foresee FDD building tools for these communities or substantially impacting how they allocate capital. I do see us learning best practices and improving our data analysis to be higher quality, faster to access and lower cost. We may not materially affect these rounds, but I do imagine we will want to gain insights to which allow us to maintain Gitcoin & FDD's personhood, project quality, and pluralism scoring to lead the space for a while. 

By lead I both mean "hold marketshare" but also provide a competitive north star for other builders in the space to optimize with and against. 

[quote="kyle, post:2, topic:11090"]
Airdrop farmers wont need to increase the value of their passport, but those of who care about the matching funds will (this hypothesis needs to be tested still).
[/quote]

I would guess that after the first airdrop goes out to users which disqualifies airdrop farmers, we will see their behavior shift. 

[quote="kyle, post:2, topic:11090"]
All this to say - I love the idea of thinking about how can we ensure the funds are optimally allocated. I suspect there are large portions of this problem space that PGF would find in their remit today as this spans into the number of grants, the amount of capital to allocate, the quality of contributor (ie, sybil, air drop farming, altruistic).
[/quote]

To be honest, I'm not sure how much of this does actually fall in the domain of FDD vs PGF. It definitely feels good to have the conversation started so we can draw clear lines of accountability around new problem spaces which arise with Grants 2 deployment.

-------------------------

lthrift | 2022-07-13 03:35:21 UTC | #5

[quote="j-cook, post:1, topic:11090"]
FDD should stop asking “How do we stop fraud”? and start asking **“How can we optimally allocate capital”**?
[/quote]

I think this is a really important question for us to be asking, especially with regard to Gitcoin's own grant program as we shift into the Grants 2.0 world that grants communities sovereignty over their own grant programs in a way we were not able to achieve with the centralized platform. 

However, my initial reaction to this is that it seems like a significant expansion of the FDD charter and one that creates duplication with PGF work. This strikes me more as a way to measure success of the Gitcoin Grants program overall, comprised of success in many facets including FDD's domains of responsibility. 

[quote="j-cook, post:1, topic:11090"]
These are relatively simple steps that could be taken to ensure the processes implemented within FDD are really well aligned with the values and preferences of the DAO and the wider community.
[/quote]

I really struggle to reconcile this process for checking the way the community chose to allocate funds during a round. Is this goal not the reason we're using quadratic funding? 

---
One of the elements that I think tends to make FDD's work a bit obscure and hard to follow at times is a lack of clearly defined domains of work. Over several months I believe I've been able to deduce that they are really 3 key areas to which measurable KPIs could be set: 
1. *filtering out fraudulent projects*
2. *evaluating project eligibility for each round*
3. *detecting & defending against **contributor** sybil*.

My observation is that GIA is doing tremendous work with regard to reviewing new grants each round. It seems we should really start dividing this charter into two parts, *fraud protection* and *round eligibility*. Both of these operational lifts are going to be faced by every round operator using Grants 2.0 and it would be prudent of us to take what we've learned from running rounds at such large scale to incorporate it into the design of the Grants 2.0 protocol. 

I believe there are two key ways Grants 2.0 can offer unique value to round operators using the protocol with regard to *fraud protection*. The first is by programmatically verifying as much of the data we use to do reviews today as possible (i.e. requiring a project owner to save a verified credential for the Twitter handle they associate with their project to prove they control it). The second is by having projects in the Grant Hub build up reputation in a variety of ways over time (i.e. acceptance/participation in other rounds run on the protocol, impact certificates, curation/staking by other communities including Gitcoin, etc). Both of these are open design spaces for the Grants 2.0 team and I know @michelle_ma has started scheduling the sessions to collaborate on these with FDD. 

[quote="ZER8, post:3, topic:11090"]
It would be really cool if we could share out methodology/process with the round owners(4 free, 4 a price, I guess this will be decided down the road) because they will surely saved a lot of funds and at the end of the day we all care about real web3 projects and we want capital to reach those who actually build our future. Btw, in the worst possible scenario we can create a grant for a project like this and donate more than 50% of the funds raised back to the Gitcoin matching pool. :slight_smile: (the post is mostly about the GIA’s perspective on the future of our rounds)
[/quote]

I believe the first step to doing this is the engagement I mentioned above with the Grants 2.0 product team where your expertise is baked directly into the design of the protocol. Leaving it open to offer a service to operators whom wish to outsource that which can't be done programmatically seems to me like an idea worth keeping on the table. 

FDD is also collaborating with the Passport team on how to evolve the trust bonus score and iteratively improve our proactive efforts to protect against sybil protection. Similar to Kyle's comment about adjusting the way we allocate matching weight based on the amount of confidence we have that an account is a verified human, this is a clear tactical move we can make that has the potential to greatly reduce the scope of the problem. 

I'd really like to see FDD's work aligned to clear, measurable KPIs that are attached to domains of responsibility that are consistent round over round.

[quote="DisruptionJoe, post:4, topic:11090"]
around new problem spaces which arise with Grants 2 deployment.
[/quote]

I don't know what this means - what are the new problem spaces that arise with the Grants 2.0 deployment? My perspective has been that the problem spaces remain the same and Grants 2.0 is enabling all of us (grants ops, FDD, grantees/project owners, etc) to better address those problems.

-------------------------

DisruptionJoe | 2022-07-13 14:25:41 UTC | #6

[quote="lthrift, post:5, topic:11090"]
However, my initial reaction to this is that it seems like a significant expansion of the FDD charter and one that creates duplication with PGF work. This strikes me more as a way to measure success of the Gitcoin Grants program overall, comprised of success in many facets including FDD’s domains of responsibility.
[/quote]

I agree. However, we simply don't have any metric against which we can a/b test the results of FDD experiments. 

Hopefully the conversation here can help drive us to do exactly what you seem to be advocating for: Setting clear domains of accountability and boundary's of project ownership while we explore the overall north star metric together. 

[quote="lthrift, post:5, topic:11090"]
I really struggle to reconcile this process for checking the way the community chose to allocate funds during a round. Is this goal not the reason we’re using quadratic funding?
[/quote]

Yes, QF provides optimal capital allocation in theory, provided there are no sybil agents and no collusion. Implementation shows us that these may not be the only assumptions which need to be addressed to provide optimal capitol allocation.

[quote="lthrift, post:5, topic:11090"]
*fraud protection* and *round eligibility*.
[/quote]

In the past we have called this platform eligibility (of which fraud is a subset) and ecosystem eligibility (because when we approve a grant to the ethereum ecosystem we are approving it for any subsequent time based "rounds").

[quote="lthrift, post:5, topic:11090"]
The first is by programmatically verifying as much of the data we use to do reviews today as possible
[/quote]

Yes. Reducing costly an inaccurate human labor where it is uneccessary.

[quote="lthrift, post:5, topic:11090"]
The second is by having projects in the Grant Hub build up reputation in a variety of ways over time
[/quote]

Agree. A plugin architecture enabling a marketplace for scoring mechanisms. 

I think a third is providing economies of scale benefits to round managers which reduce their cost of review, increase their legitimacy and credible neutrality, and provide higher resolution expression of interest by community members. 

[quote="lthrift, post:5, topic:11090"]
proactive efforts
[/quote]

I appreciate this use of the terminology. Aligning our vocabulary is usually an under-appreciated first step for aligning our work. 

[quote="lthrift, post:5, topic:11090"]
I don’t know what this means - what are the new problem spaces that arise with the Grants 2.0 deployment? My perspective has been that the problem spaces remain the same and Grants 2.0 is enabling all of us (grants ops, FDD, grantees/project owners, etc) to better address those problems.
[/quote]

I think the ones that we are currently planning for are the same, but I'd also bet that new problems will arise.

-------------------------

owocki | 2022-07-13 16:19:50 UTC | #7

i am posting feedback here at @DisruptionJoe 's request.    per https://gov.gitcoin.co/t/passing-the-torch/10971 i will likely only be posting feedback on posts like these when specifically asked

while i do think that grants capital allocation is an important thing for the DAO to be optimizing,  im concerned about the existing FDD having the skills needed to make a strategy like this successful.

specifically the leadership of the FDD lacking (1) data science skills (2) software engineering skills that can be hands on in the product.  combined this with (3) a perceived history of trying to do too many things + not nailing the core mission when it was small (having a wide focus on the legitimacy of the whole dao vs just nailing sybil/collusion defense), an expanded scope makes me nervous.  

im glad to see that the FDD is [self aware of these issues](https://gov.gitcoin.co/t/introducing-the-fdd-review/11095) and is consciously rethinking these fundamental things.

-------------------------

ZER8 | 2022-07-13 18:28:52 UTC | #8

[quote="lthrift, post:5, topic:11090"]
My observation is that GIA is doing tremendous work with regard to reviewing new grants each round. It seems we should really start dividing this charter into two parts, *fraud protection* and *round eligibility*. Both of these operational lifts are going to be faced by every round operator using Grants 2.0 and it would be prudent of us to take what we’ve learned from running rounds at such large scale to incorporate it into the design of the Grants 2.0 protocol.
[/quote]

Hello, Lindsey. I  do believe that we already are tackling both these issues in the FDD, the Sybil defenders initiative is in charge of what we call "user" moderation(sybil), the GIA initiative is in charge of "content" moderation(grant eligibility in this case).  The Sybil defenders are using a algo, ml + mixed strategy approach to sybil defense and they are doing an amazing job with that. Each round our sybil detection is getting better and better, but I'm not the best experienced person to talk about it. We constantly communicate and share our findings with each other during the rounds.

As the present GIA lead I can attest to the fact that we do have a lot on our plates :smiley: (especially during the round).  The core purpose of the GIA is to:
-Approved grants in a timely manner(here's where reviews come in)
-Appeals and disputes are judged in a timely manner
-Investigating grants
-coordinating with the FDD and wider DAO scope(Granthub, Round Manager, Passport?). I just today understood that granthub will have some features to filter users while round manager will filter out some grant eligibility issues. 

I really hope that we could present what the GIA is doing and how complex are some of the situations that we face to a broader audience and we are actually preparing a forum post for some clarity.

One of our biggest worry are "grant emulations". These are grants that cannot be denied(from an eligibility standpoint), but are dangerous because they can extract a lot of matching. Another very complex issue are grants that modify their scope after being approved.

Each round we get more and more experienced the grant investigations we started during GR14 actually proved to be very efficient at saving matching. 
Those being said I love catching fraudsters and making sure funds are SAFU and I'm actually very excited to see what our collective future looks like. :robot:

[quote="lthrift, post:5, topic:11090"]
I believe there are two key ways Grants 2.0 can offer unique value to round operators using the protocol with regard to *fraud protection*. The first is by programmatically verifying as much of the data we use to do reviews today as possible (i.e. requiring a project owner to save a verified credential for the Twitter handle they associate with their project to prove they control it). The second is by having projects in the Grant Hub build up reputation in a variety of ways over time (i.e. acceptance/participation in other rounds run on the protocol, impact certificates, curation/staking by other communities including Gitcoin, etc). Both of these are open design spaces for the Grants 2.0 team and I know @michelle_ma has started scheduling the sessions to collaborate on these with FDD.
[/quote]

We just had the first one today and we all learned a LOT! :) Very eager for what's next.

-------------------------

DisruptionJoe | 2022-07-13 18:37:07 UTC | #9

The point is not that FDD should be the one to handle defining or measuring this metric. 

[quote="j-cook, post:1, topic:11090"]
At the same time, one of the pertinent criticisms of FDD in the past has been that its objectives and processes have been somewhat opaque and difficult to appraise. A reconfiguration must therefore start with a clear and unambiguous definition of a specific remit, a clear set of performance indicators, and demonstrable alignment with the priorities of the wider community.
[/quote]

This post claims that there is not a metric by which an a/b test could be run to prove whether a given FDD expense is valuable to the community. 

This is the conversation we needed to spark. 

### On a completely different note:

I find it difficult to respond to your criticism because it is citing reasons why FDD might not be the right group to solve the problem, while incorrectly identifying which problem the post aims to solve.

[quote="owocki, post:7, topic:11090"]
specifically the leadership of the FDD lacking (1) data science skills (2) software engineering skills that can be hands on in the product.
[/quote]

I'm going to assume that you are referring to me and not the multiple Ph.D level data scientists who have built and iterated on the current system which is now fully run by GitcoinDAO. Maybe there is another DAO out there which has already solved sybil resistance at scale which you can point to as an example of what qualified looks like in this context?

Did I catch you on a bad day? 

[quote="owocki, post:7, topic:11090"]
(3) a perceived history of trying to do too many things + not nailing the core mission when it was small (having a wide focus on the legitimacy of the whole dao vs just nailing sybil/collusion defense), an expanded scope makes me nervous.
[/quote]

When we started the DAO, everyone had to figure out what was going to happen. Yes, we have gone wide at times, but I would also argue that we have been continually improving and executing on our primary objectives including sybil defense and grant eligibility. 

We report on these improvements every round in the [Governance Brief](https://gov.gitcoin.co/t/gr14-governance-brief/11050)

[quote="j-cook, post:1, topic:11090"]
FDD could have a more holistic approach to GR security if it reconfigures with “capital optimization” as its overarching goal rather than “Sybil defense”. This reconfiguration is an excellent opportunity to realign FDD with the DAO and the wider community, to set some new baselines building from empirical data and to enable closer tracking of FDDs progress against clearly defined KPIs.

The answers are not all presented in this post, it is intended to start a discussion around how FDD should configure itself going into the Grants 2.0 era. Some of the more nuanced questiions that could be pertinent to the discussion but have not been mentioned in the outline above are:

* What are the sensible KPIs FDD can define to track its own progress?
* Can an optimization framework eventually extend to allocate social, emotional, intellectual capital as well - do we get these things for free by optimally allocating monetary capital?
* How can the $GTC token fit be used to best effect in a new capital-optimization framework?
* How can we ensure FDDs capital optimization processes are transferable across rounds in Grants 2.0?
[/quote]

This highlights the primary intention of the post. It is not about reconsidering what work FDD is accountable for, but rather to re-evaluate how we frame our accountability in a holistic way. 

What do you think about these outstanding questions?

-------------------------

owocki | 2022-07-14 09:28:14 UTC | #10

[quote="DisruptionJoe, post:9, topic:11090"]
I’m going to assume that you are referring to me and not the multiple Ph.D level data scientists who have built and iterated on the current system which is now fully run by GitcoinDAO. 
[/quote]

**On Software Engineering**: 

1. I built the cGrants trustbonus system in 2020-2021.   I built it on a shoestring budget nights and weekends based off of [this paper](https://www.semanticscholar.org/paper/Who-Watches-the-Watchmen-A-Review-of-Subjective-for-Siddarth-Ivliev/13e852b3662a0409276ad8e1e2286c80fc4a610b).
2. The GPC has built Gitcoin Passport in 2022 on a budget of roughly $60k/mo.  

With a $400k-$1m/quarter budget at times in 2021 FDD was not able to successfully make any changes to the cGrants system or develop Gitcoin Passport - though it was successful in building data science tools on top of cGrants and a grants review system on top of cGrants + SAAS tools like notion.   

Yes, the system is now run by the GitcoinDAO, but that has been enabled a lot by the Gitcoin Foundation and GPC.  The FDD had a hand in the grants review & sybil data science pipeline being run by the DAO.

Because of the above, I fail to see where you have a credible claim that FDD can do product oriented software engineering.

**On Data Science**:   It's great that you've got people with PhDs on the FDD, but we should really care about results first & foremost.  There have been some successes with data science in the FDD, but there have also been some failures within data science at FDD (which have been [compounded by communication issues](https://gov.gitcoin.co/t/introducing-the-fdd-review/11095)).  Some things I'd like to see
1. three cross validation of the models or otherwise providing the validity of the models) ( @kevin.olsen or other engineers might have more details here)
2. end to end crypto economic mechanisms to find & catch sybil attackers
3. if not end to end systems building, then partnering deeply with the GPC to inform how they build their products.
4. extending out of sybil resistence + analysis of collusion attacks in the system.
5. solving the communication issues

[quote="DisruptionJoe, post:9, topic:11090"]
Maybe there is another DAO out there which has already solved sybil resistance at scale which you can point to as an example of what qualified looks like in this context?
[/quote]

Sure, Proof of Humanity has built a fairly 13k sybil resistent DAO with 1-3 person dev team before launch.  Their dev team is now a bit larger.  The cost of forgery in Proof of Humanity is probably about $100.

As has BrightID.  Also on a fairly small budget.  And they have decentralized their network analysis using their new aura tool.  The cost of forgery in BrightID is probably about $10.

Idena is also fairly interesting, though I dont think their method could scale.

Worldcoin has a very sybil resistent registry based on biometrics that is in the hundreds of thousands. 

Neither is perfect, but both POH/BrightID gotten closer to solving sybil resistence at scale than almost anyone else (GitcoinDAO included).  

None of these other DAOs have solved sybil resistance with large and complicated centralized fraud prevention/data science teams bolted onto software someone else develops.   They have solved it with elegant crypto economic mechanisms integrated with bio/digital mechanisms  .

[quote="DisruptionJoe, post:9, topic:11090"]
Did I catch you on a bad day?
[/quote]

I find it inappropriate to deflect constructive criticism in this way - it causes you to lose credibility because it is in direct opposition to [your own post about finding & engaging with honest critics](https://gov.gitcoin.co/t/introducing-the-fdd-review/11095).  

You asked me for feedback on the post on DMs, which I shared privately.  Then I asked you if I should share it publicly, and I did. When the feedback wasnt what you wanted to hear, you accuse me of just being in a bad mood.  

I will not be commenting on this post anymore and will instead leave it to others in the DAO who have graciously volunteered their own skills, time, & emotional energy to help FDD retool & steer in a new direction.

-------------------------

lthrift | 2022-07-14 03:28:06 UTC | #11

[quote="ZER8, post:8, topic:11090"]
One of our biggest worry are “grant emulations”. These are grants that cannot be denied(from an eligibility standpoint), but are dangerous because they can extract a lot of matching.
[/quote]

I don't think I quite follow what a "grant emulation" is. Could you expand upon what it means that they dangerously extract a lot of matching funds but cannot be denied. This sounds like an eligible grant that is getting strong signal and therefore significant matching. What am I missing here?

-------------------------

lthrift | 2022-07-14 03:36:29 UTC | #12

[quote="DisruptionJoe, post:6, topic:11090"]
Implementation shows us that these may not be the only assumptions which need to be addressed to provide optimal capitol allocation.
[/quote]

Could you make explicit what the other assumptions are that need to be tested?

-------------------------

ZER8 | 2022-07-14 21:58:41 UTC | #13

Hello again, I'm very glad I sparked your interest. :robot: We can have a 15 minute call anytime and I can present some of them.  A grant emulation is a grant that is designed to look like a real project(OS in incipient phase, public good, educational channel, decentralized platform or public good)  => Hence no reason for denial. 
They are like ticking time bomb that explodes after the round begins. :slight_smile:

-------------------------

DisruptionJoe | 2022-07-14 13:02:33 UTC | #14

[quote="owocki, post:10, topic:11090"]
With a $400k-$1m/quarter budget at times in 2021
[/quote]

Our highest quarterly budget was $596k. The second highest was $396k. (Not including reserves because they weren't spent, simply rolled-over)

[quote="owocki, post:10, topic:11090"]
Because of the above, I fail to see where you have a credible claim that FDD can do product oriented software engineering.
[/quote]

I don't believe I made that claim. I thought GPC was the engineering workstream and Moonshot was the prototyping workstream. I do feel we are all aligning now on these expectations. 

[quote="owocki, post:10, topic:11090"]
* three cross validation of the models or otherwise providing the validity of the models) ( @kevin.olsen or other engineers might have more details here)
* end to end crypto economic mechanisms to find & catch sybil attackers
* if not end to end systems building, then partnering deeply with the GPC to inform how they build their products.
* extending out of sybil resistence + analysis of collusion attacks in the system.
* solving the communication issues
[/quote]

1. We run [statistical model validation](https://hackmd.io/UOlkSVK0QMSEsKEB3fUFjQ?both) every round. The difficult part is that we do not have a ground truth to refer to about which accounts are sybil. This means we must scale the subjective human interpretations and continually educate and validate their findings. With larger numbers of reviews, our model becomes better (if done right). Last season the stewards requested we do less evaluations rather than continuing to focus on the metrics which would improve the model accuracy such as lowering the cost per human evaluation, building tools to scale our human evaluations, and defining quality metrics derived from inter-reviewer reliability rather than a ground truth. 
2. We aim to work with Moonshot Collective this season to assist in prototyping. Specifically with operational insights, data analysis, algorithmic research, and mechanism design research. 
3. Our partnering with Passport (GPC) is off to a start
4. This is on our roadmap for Season 15. It also doesn't have a ground truth, but we are starting to run analysis to understand what is currently happening. With Passport, much of this can be framed as incentivizing outgroup collaboration or diversity rather than preventing collusion which is difficult to clearly identify. 
5. This is a start. It is unfortunate that it feels hostile, but we sometimes need to kill the part of ourselves that causes the problem to come back stronger. That is a painful process. 

[quote="owocki, post:10, topic:11090"]
Sure, Proof of Humanity has built a fairly 13k sybil resistent DAO with 1-3 person dev team before launch. Their dev team is now a bit larger. The cost of forgery in Proof of Humanity is probably about $100.
[/quote]

If our algorithmic research is successful, we will fully gain the benefits of PoH and BrightID via our stamp integration. 

Idena has VERY low adoption among our users. 

Worldcoin could be a great passport integration. Or it could be a very poor one due to reputation, lack of overlap with our users, or other unknown reasons. We will definitely look into it. Personally, I am more interested in Good Dollar biometric VCs. 

[quote="owocki, post:10, topic:11090"]
Neither is perfect, but both POH/BrightID gotten closer to solving sybil resistence at scale than almost anyone else (GitcoinDAO included).
[/quote]

A proper weighting of our trust bonus is = or > than either individually and we provided that information during season 13 and will be providing it again in season 14. 

This comment does not consider the number of our users who have signed up for these systems. Do we know that we could grow as fast if we used exclusive logic to block out users who haven't done X?

[quote="owocki, post:10, topic:11090"]
None of these other DAOs have solved sybil resistance with large and complicated centralized fraud prevention/data science teams bolted onto software someone else develops. They have solved it with elegant crypto economic mechanisms integrated with bio/digital mechanisms .
[/quote]

None of them have solved it at scale. We work collaboratively with them. How does one know if the sybil prevention system is working if there is no research or analysis to examine how well it is working?

[quote="owocki, post:10, topic:11090"]
I find it inappropriate to deflect constructive criticism in this way - it causes you to lose credibility because it is in direct opposition to [your own post about finding & engaging with honest critics ](https://gov.gitcoin.co/t/introducing-the-fdd-review/11095).
[/quote]

in that post it says: 

"The writing should not:

* Be seen as the chosen direction of FDD
* Be censored or overly orchestrated by FDD
* Focus on existing alignments, rather it should focus on tradeoffs and prioritization
* Directly critique contributors effort or competency"

This response started by arguing that FDD shouldn't be the WS which is responsible for identifying whether or not funding is optimally allocated. This post was not intended to say FDD should. 

The response also directly focused on contributor efforts and competency. 

[quote="owocki, post:10, topic:11090"]
You asked me for feedback on the post on DMs, which I shared privately. Then I asked you if I should share it publicly, and I did. When the feedback wasnt what you wanted to hear, you accuse me of just being in a bad mood.

I will not be commenting on this post anymore and will instead leave it to others in the DAO who have graciously volunteered their own skills, time, & emotional energy to help FDD retool & steer in a new direction.
[/quote]

Thank you for responding.

-------------------------

DisruptionJoe | 2022-07-14 17:53:57 UTC | #15

[quote="lthrift, post:12, topic:11090"]
Could you make explicit what the other assumptions are that need to be tested?
[/quote]

1. That grants are participating to gain financial benefits, not social or other forms of capital
2. The eligibility policy being necessary at all
3. That there are no other assumptions which are baked into the theory, but not called out

-------------------------

kyle | 2022-07-14 18:57:12 UTC | #16

[quote="ZER8, post:3, topic:11090"]
We prevented over 100k in improper matching allocation by removing certain grants and I really think we could really help the round owners save a lot capital,
[/quote]

I think its important to make a distinction here that Sybil attacks are different from Fraudulent Grants. There are likely other mechanisms we can put in place to prevent fraud. Gitcoin Passport is likely a Sybil tool to start.

[quote="ZER8, post:3, topic:11090"]
thus it’s honest to assume that that capital can by used by Gitcoin DAO, Gitcoin Matching pool and/or the FDD
[/quote]

I dont think I agree with this. We would need consent to make this assertion IMO. Long term, we want ecosystem building this expertise and identifying these grants themselves. Our goal is to be a protocol in the future, not a services team. right now, PGF (Grants Ops) and FDD are services teams... success is when we have moved the outcomes that these groups achieve into the protocol itself. This is not to say that PGF and FDD go away, there will likely always be a need... it just shouldn't **require** those services to be successful.

-------------------------

lthrift | 2022-07-14 20:41:26 UTC | #17

The original response you sent that I got via email was more clear than this one :) In that version you articulated that what you are calling a "grant emulation" is when someone creates a grant, gets approved, and then changes the details of their grant after approval in a way that both attracts more funding and renders them ineligible for some reason. 

Grants 2.0 will require project owners to submit an on-chain application to apply for a round. They will not be able to change the details fo their application after submission. This should reduce, if not entirely eliminate, this problem.

-------------------------

ZER8 | 2022-07-14 22:41:11 UTC | #18


[quote="kyle, post:16, topic:11090"]
I think its important to make a distinction here that Sybil attacks are different from Fraudulent Grants. There are likely other mechanisms we can put in place to prevent fraud. Gitcoin Passport is likely a Sybil tool to start.
[/quote]

Yes, I know! You are right and this is because I'm not always clear when communicating. A sybil attack is not the same as a fraudulent grant, but they do share certain characteristics(this is what I was trying to say), in both cases the attacker wants to extract value from the system. This season we will also start looking at grants data the same way our HE team handles sybils. We will process the data and try to map different behaviour patterns. 

PS. I recently learned the difference between Grants hub and Round manager(where the eligibility issues will lie from what I understood).
[quote="kyle, post:16, topic:11090"]
I dont think I agree with this. We would need consent to make this assertion IMO. Long term, we want ecosystem building this expertise and identifying these grants themselves.
[/quote]

I was just kinda ideating here tbh :slight_smile: 

[quote="kyle, post:16, topic:11090"]
goal is to be a protocol in the future, not a services team. right now, PGF (Grants Ops) and FDD are services teams…
[/quote]

Thank you with being patient with me and for trying to make me see the big picture here, I tend to zoom in too much sometimes :smiley:

-------------------------

ZER8 | 2022-07-15 14:51:30 UTC | #19

Sorry, I honestly don't want to occupy 2 much of your time with these issues. Long story short: grant emulations are almost a whole category. I think I understood a lot more about our collective future direction that after the FDD x Passport call today and what FDD's role in Grants 2.0 will be.

For simplicity in the e-mail I only explained one of the types of grant emulations: grants that change their scope during the round, but there are more types. 

We are preparing a forum post and will try to present these issues also. Thank you and have a nice weekend! :blue_heart:

-------------------------

lthrift | 2022-07-14 23:03:41 UTC | #20

I think this is a good example of my original point :) Which is to say that the already known scopes of work and problem areas FDD addresses are not made clear and measurable. 

I seem to read more posts about what FDD might do in the future and what new things could be explored, yet the known problem areas and scopes of work remain "too complex" and "unmeasurable". 

As a workstream lead who has great dependency on the work FDD does, I hope you all can first take inventory of the work you do today such that the domain is very clear and the KPIs measurable.

-------------------------

DisruptionJoe | 2022-07-15 09:17:55 UTC | #21

[quote="kyle, post:16, topic:11090"]
I dont think I agree with this. We would need consent to make this assertion IMO. Long term, we want ecosystem building this expertise and identifying these grants themselves. Our goal is to be a protocol in the future, not a services team. right now, PGF (Grants Ops) and FDD are services teams… success is when we have moved the outcomes that these groups achieve into the protocol itself. This is not to say that PGF and FDD go away, there will likely always be a need… it just shouldn’t **require** those services to be successful.
[/quote]

I FULLY agree with this assessment. 

[quote="lthrift, post:20, topic:11090"]
I think this is a good example of my original point :slight_smile: Which is to say that the already known scopes of work and problem areas FDD addresses are not made clear and measurable.
[/quote]

This is going to be a focus for us even before Season 15. I hope you see impactful improvements in this area even before the next round budgets are approved. 

[quote="lthrift, post:20, topic:11090"]
As a workstream lead who has great dependency on the work FDD does, I hope you all can first take inventory of the work you do today such that the domain is very clear and the KPIs measurable.
[/quote]

We should ideate more on this as a group. There are a lot of KPIs we are tracking and continually post in the Governance Brief. I believe what I am hearing here is that we are looking for now are KPIs related to user personas rather than overall effectiveness. This would be much more symbiotic with a product driven growth strategy. 

For both Identity and Grants, you would like to see behavior types clustered with user stories labeling the dominant behavior modes. This might give clear quantative insights to assist a product team with expertise in UI/UX and engineering, but less familiarity with (or time for) red team/blue team exercises, algorithmic research, and / or mechanism design. The product team may then use these insights to make better data-driven decisions.

Is this more aligned with your needs from FDD?

-------------------------

epowell101 | 2022-08-31 16:30:26 UTC | #22

I was just referred to this thread again by someone.  The intra Gitcoin snipping in this thread is a bit off-putting to at least some outside of Gitcoin. 

For future readers that lack some context about the real substance of the discussion - it might be useful to watch @owocki amazing greenpill interview w/ Professor Ford regarding sybil attacks and resistance over the years.

[https://www.youtube.com/watch?v=PlDOjDu-mpU](https://www.youtube.com/watch?v=PlDOjDu-mpU)

Afaik Professor Ford is correct in that there have been *decades* of efforts to "eliminate" sybil attacks as they predated our reliance at Gitcoin on quadratic voting.

-------------------------

j-cook | 2022-09-01 14:39:45 UTC | #23

Hi @epowell101 - yea that feels like fair criticism - I tried to capture the discussion as it was going on inside FDD. It is good to be reminded not to be too blinkered. Thanks for the nudge.

-------------------------
