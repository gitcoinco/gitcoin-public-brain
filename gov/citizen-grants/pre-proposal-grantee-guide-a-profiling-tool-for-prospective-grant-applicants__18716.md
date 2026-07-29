---
id: 18716
title: "[Pre-Proposal] Grantee Guide - A Profiling Tool for Prospective Grant Applicants"
slug: pre-proposal-grantee-guide-a-profiling-tool-for-prospective-grant-applicants
category: citizen-grants
url: https://gov.gitcoin.co/t/pre-proposal-grantee-guide-a-profiling-tool-for-prospective-grant-applicants/18716
created_at: 2024-05-02T14:50:09.403Z
last_posted_at: 2024-05-06T16:33:26.063Z
posts_count: 7
views: 3185
like_count: 10
---

# [Pre-Proposal] Grantee Guide - A Profiling Tool for Prospective Grant Applicants

<https://gov.gitcoin.co/t/pre-proposal-grantee-guide-a-profiling-tool-for-prospective-grant-applicants/18716>
rohit | 2024-05-02 14:51:46 UTC | #1

Thanks to @harryeastham for seeding the concept and to @umarkhaneth for reviewing.

tl;dr The following ideation post proposes a prototype for a data app to inspire confidence in potential grantees on Gitcoin Grants (GG) and Independent Rounds by demonstrating other successful funding journeys on Grants Stack. This post kick-starts an 8-week timeline to accelerate from idea to app using Citizens Innovate by supporting and funding builders with the most robust proposals.

Timeline:

* **May 2 - May 16th:** The post will be open for feedback on the gov forum until May 16th, along with a [sign-up form](https://forms.gle/cVZ6voLCmFxY8q3q7) for Citizens interested in opting for a direct grant to build the prototype
* **The week of May 20th:** A debrief call and 1:1 sessions the following week with Citizens interested in submitting their proposal for funds to build the prototype
* **The week of May 27th:** The Grant Council may approve one or more GCPs to implement the functionality
* **June 3rd to June 28th:** 4-week timeline to implement the prototype with interim demos as well as support and mentorship from Gitcoin team members with context on the problem

### Hypothesis

> Prospective Gitcoin grantees are more likely to apply for a grant on Grants Stack when they see the journey of similar grantees in their niche who have successfully raised funds on Gitcoin Grants and Independent Rounds.

### Validation

We propose a self-service data app prototype designed to test this hypothesis for potential applicants. This prototype will allow users to input a summary of their project and retrieve information about similar grantees who have previously participated in Gitcoin grants. The prototype will provide answers to questions like:

* Which projects similar to ours have participated on Gitcoin in the past?
* How much funding have these projects raised over time?
* How much funding can we expect to receive for our project?
* Which funding rounds are we eligible to apply for?
* What attributes are key to increasing the chances of being accepted in these rounds?
* What else?

### Technical Considerations

These are for reference only. Interested builders are encouraged to research and opt into most appropriate approaches to address the problem.

***Where can I find data about past grantees?***

Databases such as [RegenData](https://regendata.xyz/) and [Gitcoin Grants Data Portal](https://grantsdataportal.xyz/) provide valuable information that can be leveraged to support prospective grantees. These databases can retrieve:

* A list of past grantees whose work is similar to the user's project.
* The trend of their participation in Gitcoin, including the number of contributors and the amount raised over time.

***How do I find grantees similar to the applicant?***

To facilitate this, clustering algorithms can be employed to match a given project description with similar grantees. For an example of how feature extraction, dimensionality reduction, and similarity measurement are implemented, refer to the [GrantsScope App for GreenPill x Octant round](https://gp-octant.streamlit.app/). Click [here](https://github.com/rohitmalekar/gp-octant) for the GitHub Repo. Advanced approaches involving Retrieval-Augmented Generation (RAG) or fine-tuning LLMs might also be relevant here.

***How do I estimate how much funding a prospective grantee can expect?***

The [historical curves in the power law distribution](https://x.com/RohitMalekar/status/1773102167890559420) of the matching pool could provide a suggestive range of funds that could be raised in a QF round. This estimation requires assumptions for percentile rank and the size of the matching pool.

### Limitations and Risks

* **User Assumptions and Expectations:** The tool relies on user inputs regarding their assumptions about percentile rank and matching pool size to estimate potential funding. Incorrect assumptions or a lack of understanding about these parameters could lead to unrealistic expectations about the funding amount. Educating users on how to make informed assumptions is crucial.

* **Algorithm Bias and Fairness:** The algorithms used may inadvertently favor certain types of projects or grantees based on the data they have been trained on. This could lead to a lack of diversity in the recommended or seen as successful projects, potentially reinforcing existing biases in funding allocation.

* **Complexity of Clustering Algorithms:** Clustering algorithms are central to matching project descriptions with similar past grantees. However, these algorithms' complexity could lead to implementation and maintenance challenges. There's also the risk of overfitting, where the model is too closely fitted to the historical data, potentially making it less effective in predicting or matching new, unseen projects.

### Next Steps

* Share your feedback here on the hypothesis and validation approach before May 16th
* Sign up [here](https://forms.gle/cVZ6voLCmFxY8q3q7) if you want to opt in for a deeper dive to submit a proposal to build this prototype or to shadow along the discussions and demos.

-------------------------

Sov | 2024-05-04 13:07:56 UTC | #2

I’m in support of this.  

The grantee journey is an important part of our work and surfacing more information and insights as this initiative seeks to do is a great idea.

-------------------------

mars | 2024-05-04 22:01:34 UTC | #3

### FYI

### Related

> demonstrating other successful funding journeys on Grants Stack

Successful journeys.

Passing the review.

Inclusing automated AI review. 

2 humans did ✅ but AI did ❌ and basex.com was ultimately rejected. Wish I've received this feedback sooner in order to improbve the application.

![image|230x500](upload://2GO3HZflkjYGVirfbXdxLPReV2b.jpeg)

Link to the AI reviewer that was in use for Climate Coordination Network (community round): https://checker.gitcoin.co/public/projects

That sounds like a decent tool that can offer immediate feedback in order to clarify various nuance. 

### Please highlight differences between existing and proposed tool 🙏

### Feature request: instant feedback

*(me not wasting time and energy to clarify various issues)*

### Additional question about eligibility

> [sign-up form](https://forms.gle/cVZ6voLCmFxY8q3q7) for Citizens interested in opting for a direct grant to build the prototype

Do you need to be a Citizen (capital "c") in order to buidl? What is the minimum citizenship requirement? I was rejected from recent Gitcoin Citizen round (another rejection) so not sure if eligible to apply?

-------------------------

rohit | 2024-05-06 14:14:47 UTC | #4

[quote="mars, post:3, topic:18716"]
Wish I’ve received this feedback sooner in order to improbve the application.
[/quote]

Hey @mars This looks like a climate round application. If you haven't already, please share your inputs with [Climate Coordination Network](https://twitter.com/climate_program).

[quote="mars, post:3, topic:18716"]
I was rejected from recent Gitcoin Citizen round (another rejection) so not sure if eligible to apply?
[/quote]
The short answer is yes. You may apply for a direct grant under Citizen Grants (Forward or Innovate) regardless of a decision on another grant application.

The long answer is that writing a proposal for a direct grant is a time-consuming endeavor. To streamline the process and facilitate more focused discussions on the problem space, assess potential technical pathways, and assist citizens in determining whether they wish to commit to writing a proposal, I recommend utilizing the sign-up form. Whether individuals are interested in shadowing the process to gain insight and context or are ready to submit a proposal themselves, we encourage them to sign up and participate.

-------------------------

KMLLC | 2024-05-06 14:27:54 UTC | #5

I am not a builder or have developer skills, that being said would love to share our story both from business and personal POVs of how Gitcoin has benefited us since we have been involved, circa GG18. I feel strongly that providing peer support for incoming grantees to have a model and resources they can learn from so they can have the best possible experience in applying for grants offered. Level setting expectations I feel strongly has high value so grantees are prepared for the seasonal grind, while asynchronously thinking about activity in between seasonal efforts.

-------------------------

Decentralizedceo | 2024-05-06 14:44:27 UTC | #6

I am in full support of this! 
It will be a great tool that will enhance the grantee experience for sure. 
I can also see this being used for the ["gofundop"](https://gofundop.vercel.app/) project. A way for projects to obtain a fraction of their potential resources to kick start their initiatives.

-------------------------

mars | 2024-05-06 16:33:26 UTC | #7

[quote="rohit, post:4, topic:18716"]
writing a proposal for a direct grant is a time-consuming endeavor
[/quote]

[quote="rohit, post:4, topic:18716"]
assist citizens in determining whether they wish to commit to writing a proposal
[/quote]

Now I see!

It's not for GG20 (or other runds proposal).

It's for **direct grant**.

Now I see the difference, I should pay more attention to the title of the topic.

I would solve this problem using "no code" approach. Intentionally brief  "expression of interest". 1 pager, simple, basic info:

> We know that writing a grant proposal is massive task that's why offer "expression of interest" that is 1 page long and allows us to offer direct feedback whether the fully pledged proposal is likely to be accepted.

-------------------------
