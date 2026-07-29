---
id: 19902
title: "[GCP - XXX] Predictive Funding Competition for GG23"
slug: gcp-xxx-predictive-funding-competition-for-gg23
category: citizen-grants
url: https://gov.gitcoin.co/t/gcp-xxx-predictive-funding-competition-for-gg23/19902
created_at: 2025-01-29T09:21:18.658Z
last_posted_at: 2025-02-10T12:23:54.314Z
posts_count: 12
views: 2393
like_count: 34
---

# [GCP - XXX] Predictive Funding Competition for GG23

<https://gov.gitcoin.co/t/gcp-xxx-predictive-funding-competition-for-gg23/19902>
thedevanshmehta | 2025-01-29 09:35:26 UTC | #1

**Summary**

This GCP proposes to support a machine learning competition to predict funding received by projects in GG23. The objective is an understanding of the metrics and models that are most likely to give a similar allocation outcome as the human judgment mechanism of quadratic funding.

For this, we are requesting a total of 20,000 GTC (~$11k as of 29th January), half of which is given as prizes to winning contestants while the other half covers pay for judges and operating expenses.

**Abstract**

Deep Funding has a market of AI models competing to make predictions aligning as closely as possible with human judgment. Plugging in Deep Funding for GG23 will be an experiment in replicating human judgment in QF with AI, create an information surfacing tool for voters, and more generally involve the machine learning community with gitcoin rounds.

There are 3 primary components :

1. A list of all competing projects in GG23

2. A competition where contestants provide weights to each project indicating the relative funding they will receive

3. After funding amounts are announced, finalizing a leaderboard showing which ML models best predicted funding to projects in the round

**Motivation**

With its move to becoming multi-mechanism, especially retrofunding and futarchy, the Gitcoin ecosystem needs a capability boost in its understanding of metrics and assessment of predictions. This competition seeks to do just that by asking top performing model submitters to make public the metrics considered in their predictions on relative funding between projects in GG23.

Previously, Deep Funding demonstrated the impact of these contests by asking models to predict funding received by projects in Gitcoin, Optimism, Open Collective and Octant rounds from 2019 to 2024. You can see the submissions in the contest here; to give one example, the current [top rated model](https://research.allo.capital/t/submission-of-entries-to-the-deep-funding-mini-contest/22) by @davidgasquez used the following weights to predict how much funding a project would receive

![image|224x500](upload://kbnNP8LmS1eZbly76sI0h2EIQ0C.jpeg)


By expanding Deep Funding to GG23, we can gauge the impact of AI models in predicting not just past funding but also upcoming round results. **If the gap between model predictions & eventual funding allocation is narrow, we can eventually utilize these models to determine how much funding a project should receive in a round without them having to even take part in it**

This collaboration will result in;

* Submissions on Gitcoin’s forum by machine learning experts on what parameters fed into their models could best predict results of a GG23 round before it is concluded

* An indicator to voters on which projects are predicted to be perform well in a GG23 round

* Provide concrete data on the gap between the winning models' predictions of funding received by projects in the round and the actual amount it ends up receiving in GG23.

**Specifications**

1. Creation of the GG23 predictive funding contest on [cryptopond.xyz](https://cryptopond.xyz)

* *Receive the Project List*: Upload a list of all participating projects to cryptopond.

* *Submit Your Predictions*: For each project, forecast the fraction of the total funding it will receive. All predicted weights must sum to 1.

* *Compare to Reality*: When the round completes and actual payouts are finalized, we’ll calculate the actual weight for each project. For example, if Project A receives $10,000 out of a $100,000 round, its weight is 0.10.

* *Scoring*: We’ll use RMSE (root mean squared error) to evaluate how close each submission is to the real, final allocation. The model with the lowest RMSE wins.

2. Submission write-up by model submitters on Gitcoin forum

To be considered for prizes, model submitters will need to submit a write-up similar to the earlier contest ([example](https://research.allo.capital/t/submission-of-entries-to-the-deep-funding-mini-contest/22)). Participants are encouraged to be visual in their communication, show weights given to their models, share their juypter notebooks or code used in the submissions and explain the performance parameters of their model.

3. A jury will look at the comments and model performance and select the prize winners

We will use willing jury members from the mini-contest to also judge models in GG23. The committee for the mini-contest is composed of @vbuterin (Vitalik Buterin) , @Kronosapiens (Daniel Kronovet), @Joel_m (Joel Miller), @ccerv1 (Carl Cervone) and @octopus , with Devansh Mehta as facilitating member.

Those members willing to re-serve for the GG23 competition will comprise the jury.

**Milestones**

1. Get competition uploaded on cryptopond

2. Finalize the leaderboard of submissions based on how closely their model matches with actual GG23 round allocation

3. Choose winners from among those making a writeup on Gitcoin’s forum

**Budget**

We are requesting a total of 20,000 GTC for this experiment.

10,000 GTC will be awarded as prizes to winning model submissions.

5000 GTC is kept aside for operational expenses such as getting the contest uploaded to cryptopond, marketing of the initiative to get high quality model submissions and completion of other reporting requirements under this grant

5000 GTC is kept aside for compensation of committee members that are willing to serve (maximum of 1000 GTC per member). Unutilized funds from this bucket will be returned to Gitcoin.

**KPIs**

1. Schelling point for machine learning models and AI agents: Number of model submissions and high quality comments on the forum from contestants (Quantitative)

2. Performance benchmarking : Measure gap between top model predictions on funding allocations and the actual allocation to projects (Quantitative)

3. Information surfacing tool: Useful to GG23 participants in seeing which projects are predicted to perform well (Qualitative)

special thanks to Nidhi Harihar, @sejalrekhan , @MathildaDV & @owocki for their comments on the draft

-------------------------

davidgasquez | 2025-01-30 08:54:31 UTC | #2

Excellent write up @thedevanshmehta! I'm excited about this proposal. Wanted to share some scattered thoughts as a mini-contest participant.

- An **alternative target** might be to predict the `total_funding_usd` instead of the `relative_funding_in_round`. This would make the problem and error easier to understand. 
  - The training becomes: **`project, round, usd` and is distributed one week before the round starts**. The test set to predict would be only  `project, round` where round is `gg23` on the entire dataset.
  - The **evaluation is done at the end of the round**, comparing the test set contestant predictions with the real funding received (I'd say before the quadratic funding is applied to keep things simple).
  - Since you'd be asking for total funding received, **you can compute the ratio later on** and compare the ratios with the live ratios in the round.
  - This approaches will miss projects that apply during the round or the week earlier. That's ok as they can be excluded from the ratio calculations too later on. **This approach focuses on keeping the problem as close to the goal** (predict the potential funding a project would get if they applied) as possible.
- Given there is no possible data leaking, and you want accuracy, prices should reward more the position in the leaderboard than during the mini contest (getting to error 0 or, more hard to detect, getting the test set locally and overfit the model parameters are possible)
- Would be great to come up with a way to reward multiple models (similar to Numer.ai) so there is some specialization encouraged, and the price is spread a bit more between useful models.
- Depending on your goals (e.g: GC running models in future rounds), it might be useful to reward also open source submissions in some way. They might be open source at the end of the competition, but will help future competitions as they will be able to use the same approach.

-------------------------

Sov | 2025-01-29 15:55:54 UTC | #3

Excited to see this creative approach to understanding allocation patterns! The competition format could provide insights into what drives successful outcomes.

A few questions I have:

1. Have you considered including historical GG round data as a training set for the models? This could help establish baseline performance metrics before tackling GG23 predictions.
2. Regarding the judging criteria - are there plans to weight the quality of explanation/documentation in the forum write-ups? Some of the most valuable insights might come from participants even if they don't achieve the lowest score.

Count me as supportive of this initiative. It's exactly the kind of creative experimentation we need to better understand and improve our funding mechanisms.

-------------------------

owocki | 2025-01-30 05:35:22 UTC | #4

I am supportive of this proposal.

-------------------------

thedevanshmehta | 2025-01-31 12:39:59 UTC | #5

Thanks for all the responses! some thoughts below

[quote="davidgasquez, post:2, topic:19902"]
An **alternative target** might be to predict the `total_funding_usd` instead of the `relative_funding_in_round`. This would make the problem and error easier to understand.
[/quote]

This is true, while adding an extra variable that models need to predict: amount of community contributions in the round.

By making it relative funding, we eliminate the error fluctuations that occur because community contributions were greater or lower than expected.

so with that in mind, do you think **project, round, weight** is better or **project, round, USD**?

[quote="davidgasquez, post:2, topic:19902"]
The **evaluation is done at the end of the round**, comparing the test set contestant predictions with the real funding received (I’d say before the quadratic funding is applied to keep things simple).
[/quote]

Curious to know why you think quadratic funding should be eliminated when its usually 2-3x more than community contributions. 

wouldn't it be more fun if models also have to account for wide support in community base? Otherwise we skew the contest with a project receiving a single large donation. Also, if we want to expand crowdsourced predictions to whether a wallet would be counted as a sybil or not, including QF in final leaderboard rankings is an important intermediate step we can take.

[quote="Sov, post:3, topic:19902"]
Have you considered including historical GG round data as a training set for the models? This could help establish baseline performance metrics before tackling GG23 predictions.
[/quote]

[quote="davidgasquez, post:2, topic:19902"]
This approaches will miss projects that apply during the round or the week earlier. That’s ok as they can be excluded from the ratio calculations too later on. **This approach focuses on keeping the problem as close to the goal** (predict the potential funding a project would get if they applied) as possible.
[/quote]

So there's certainly an advantage to giving past gitcoin data as training and closing new model submissions once the round begins.

This would be a question for @MathildaDV : in GG23, can we keep an early bird deadline (say 10 days before the round begins), where if they apply and get accepted they are entered into the predictive funding contest? We would then run the contest for only one week before GG23 starts, which will hopefully drum up some interest in the main round.

David Gasquez had an excellent point that if we include 1 week of data in GG23, we can't really know how well models predict funding to projects since we literally have some of the funding data in the round. so new submissions in the contest needs to close BEFORE the round begins.

[quote="davidgasquez, post:2, topic:19902"]
* Given there is no possible data leaking, and you want accuracy, prices should reward more the position in the leaderboard than during the mini contest (getting to error 0 or, more hard to detect, getting the test set locally and overfit the model parameters are possible)
* Would be great to come up with a way to reward multiple models (similar to Numer.ai) so there is some specialization encouraged, and the price is spread a bit more between useful models.
[/quote]

I like this idea, we keep one prize amount just for having the least error possible. Purely meritocratic with no juror bias involved.

[quote="davidgasquez, post:2, topic:19902"]
Depending on your goals (e.g: GC running models in future rounds), it might be useful to reward also open source submissions in some way. They might be open source at the end of the competition, but will help future competitions as they will be able to use the same approach.
[/quote]

[quote="Sov, post:3, topic:19902"]
Regarding the judging criteria - are there plans to weight the quality of explanation/documentation in the forum write-ups? Some of the most valuable insights might come from participants even if they don’t achieve the lowest score.
[/quote]

Would be curious to know your thoughts on the split in prize amounts, between purely meritocratic and based on leaderboard ranking vs forum writeups. 50-50 would be my initial guess just shooting from the hip

One other thought i had: since its not a very large amount earmarked as prizes for contestants (~10k GTC), could we create a multi-sig like deepfunding.gitcoin.eth and try crowdfunding amounts into it for adding to the prize pool, as @owocki has sometimes done in the past for other new initiatives? 

Excited to see the support so far and hope we can get this tested out in GG23!

-------------------------

davidgasquez | 2025-02-04 08:44:26 UTC | #6

Great points @thedevanshmehta! 

[quote="thedevanshmehta, post:5, topic:19902"]
so with that in mind, do you think **project, round, weight** is better or **project, round, USD**?
[/quote]

Weights sounds great! We can always go from total USD to round weight when building a model! :) 

[quote="thedevanshmehta, post:5, topic:19902"]
Curious to know why you think quadratic funding should be eliminated when its usually 2-3x more than community contributions.
[/quote]

You are totally right! We should be including quadratic funding as it's also a function of number of contributors.

[quote="thedevanshmehta, post:5, topic:19902"]
50-50 would be my initial guess just shooting from the hip
[/quote]

Sounds good! I think, even if small, splitting prices to get a diverse set of approaches is worth in this early prototypes. The focus should be on exploration!

-------------------------

thedevanshmehta | 2025-02-05 13:03:01 UTC | #7

Hi @MathildaDV  what next is needed to move ahead with this challenge for GG23?

Would be keen to have enough time for preparation!

-------------------------

MathildaDV | 2025-02-05 13:30:07 UTC | #8

Thank you for this proposal. I think this is a great and would be a great addition to GG23! I'm all about experimenting and building hype for the round. 

@thedevanshmehta next steps here is that our internal grants council will vote on whether to approve this GCP and then I'll update you here on the forum.

-------------------------

mars | 2025-02-06 11:33:55 UTC | #9

[quote="thedevanshmehta, post:1, topic:19902"]
create an information surfacing tool for voters
[/quote]

I'm against this. Will act as "priming": https://en.wikipedia.org/wiki/Priming_(psychology)

That directly leads to privacy / confidentiality / publicity of the model / weights / results. I think a simple solution will be to "commit-reveal"... Publish a hash before the round, publish the results after the round?

[quote="thedevanshmehta, post:1, topic:19902"]
You can see the submissions in the contest here.
[/quote]
Please update the link.

----

About the info on the projects there is also: https://checker.gitcoin.co/ and Karma GAP and https://devouch.xyz/ etc...

I think that GG funding rounds and the aspect of voting / marketing / shilling has some value in itself.

-------------------------

MathildaDV | 2025-02-07 13:34:21 UTC | #10

I'm happy to announce that this GCP has passed! The team has voted for this to move forward. I'll be in direct touch with @thedevanshmehta and co for next steps. 

And to answer this question: 

[quote="thedevanshmehta, post:5, topic:19902"]
This would be a question for @MathildaDV : in GG23, can we keep an early bird deadline (say 10 days before the round begins), where if they apply and get accepted they are entered into the predictive funding contest? We would then run the contest for only one week before GG23 starts, which will hopefully drum up some interest in the main round.
[/quote]

IMO this would be pretty difficult as applications are generally only open for 2-2.5 weeks ahead of the round and it'll be another piece to communicate out. But let's discuss this more in detail to see where we may be able to find a middle ground.

-------------------------

thedevanshmehta | 2025-02-08 09:38:20 UTC | #11

This is great news!

Looking forward to seeing how well modeloors can forecast the funding each project will get in GG23.

[quote="MathildaDV, post:10, topic:19902"]
applications are generally only open for 2-2.5 weeks ahead of the round
[/quote]

Even having one round of projects accepted 5 days before the forecasting begins would be sufficient! 

So one early bird deadline to apply which is a week before GG23, and another regular deadline which wouldn't count towards weights of projects. Happy to explore alternatives as well that might be better and still not bias model submitters towards simply extending the community funding for projects in the first few days of the round.

-------------------------

ccerv1 | 2025-02-10 12:23:54 UTC | #12

Happy to see this move ahead! It's been great working with this group over the past two months on Deep Funding.

-------------------------
