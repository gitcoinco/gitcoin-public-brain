---
id: 10208
title: "Product Idea - Introducing uxtesting.party for feedback and discussion"
slug: product-idea-introducing-uxtesting-party-for-feedback-and-discussion
category: open-discussion
url: https://gov.gitcoin.co/t/product-idea-introducing-uxtesting-party-for-feedback-and-discussion/10208
created_at: 2022-03-24T00:34:30.784Z
last_posted_at: 2022-03-30T15:13:07.557Z
posts_count: 3
views: 2477
like_count: 3
---

# Product Idea - Introducing uxtesting.party for feedback and discussion

<https://gov.gitcoin.co/t/product-idea-introducing-uxtesting-party-for-feedback-and-discussion/10208>
paulwalnuts | 2022-03-24 00:34:30 UTC | #1

Hey Everyone,

I'm a new contributor on the product side coming from web2. I put together this pitch to solve a problem on the UX Testing side. Timing might not be perfect since the Moonshot Collective is actively trying to re-organize the product portfolio. 

I'm hoping to get some feedback on this idea and learn potential pitfalls in my thinking and [wireframes](https://app.mural.co/t/dao7464/m/dao7464/1647570345926/b974194d83556887aab6569752172b31534eb912?sender=uc7c3bf0e362db080aaaf5767). 

## Problem
Crypto users are a subset of the total population. An even smaller subset are DAO contributors. An even smaller subset of that are DAO operators.

It takes a lot of work to find these DAO operators and test our prototypes the way they were built (read: rapidly).

Because it's difficult to find DAO operators, the DAO ecosystem does not test as much of their product as it could*

*_this statement has not been validated_

[![Screen Shot 2022-03-23 at 5.01.24 PM|505x500](upload://rQhvsne5XH05EUwhwbMRVWn1eg6.png)](https://app.mural.co/t/dao7464/m/dao7464/1647570345926/b974194d83556887aab6569752172b31534eb912?sender=uc7c3bf0e362db080aaaf5767)


## Product Solution/Vision
Create a permissionless and possibly decentralized rapid testing platform for DAOs to more easily test their prototypes and designs.

## Target User(s)
* Primary User - DAO Operators
* Secondary User - DAO Contributors

## MVP Goals
* Increase the number of usability tests conducted by Moonshot Collective by x%
* Build a database of at least 200 DAO contributors and 20 DAO operators for future user interviews

## Product Roadmap

### Summary
* Step 1
  * Build a decentralized 'first click ux test' platform and collect emails of DAO operators
* Step 2
  * Add more types of usability tests and allow other DAO contributors to create their own tests
* Step 3a
  * DAOs can fork uxtesting.party to create their own database of DAO ecosystem contributors

OR

* Step 3b 
  * Continue building a decentralized user testing platform where a tester could see and aggregate of all UX tests they are qualified for based on their area of focus

[![Screen Shot 2022-03-23 at 5.02.13 PM|690x448](upload://tOG3NyLLddiItvmOFmpsOdfVLaR.png)](https://app.mural.co/t/dao7464/m/dao7464/1647570345926/b974194d83556887aab6569752172b31534eb912?sender=uc7c3bf0e362db080aaaf5767)

## Wireframes
The wireframes are for two paths:

1. Creating a test
2. Taking a test

[![Screen Shot 2022-03-23 at 5.02.04 PM|690x413](upload://deBtr47VNAgcW9xzZYV7PhSoQaZ.png)](https://app.mural.co/t/dao7464/m/dao7464/1647570345926/b974194d83556887aab6569752172b31534eb912?sender=uc7c3bf0e362db080aaaf5767)



## How does this product grow its userbase?
* Word of mouth/Discord
* Expanding the platform to allow other DAOs to create their own tests

## How could this product generator revenue?
* Charge-per-test-created
* Take percentage of each payout to a tester
* We could charge a yearly subscription fee to use the platform
* Scaled percentage - the more people taking the ux test, the less the creator pays per test. This wouldn't generate as much revenue, but it would increase awareness as test creators would want more users completing tests.

## Unanswered questions and risks
* Are DAO contributors comfortable giving us an email address?
* Does this need to be decentralized when there is already usabilityhub.com? 
* Does this live on-chain?
* Do these tests have an expiration date? 
  * What happens to the funds if they do have an expiration date?
* How would a user receive support? 
  * Who would they contact?
* Are we adding incentives where they aren't needed?
* Is a 'first click' test useful to the Gitcoin DAO?
* How does this product fit into the Moonshot Collective product strategy?
* How do we make sure a single entity doesn't drain the entire test fund?
* How does a test creator fund a UXtesting Party?
* What types of tokens should we allow?

## Next Steps
* Get feedback from Gitcoin members
* Build the MVP
* Launch MVP
* Iterate on feedback and work on productizing uxtesting.party

-------------------------

umarkhaneth | 2022-03-29 00:44:55 UTC | #2

Hey Paul,

I really like this idea -- there are lots of DAO operators who may have a hard time finding the best tools to use. There are also lots of DAO tooling being made. I could see operators use this product as a flip book of DAO tools to help them find the ones they like the most.  I'm not sure if they would keep coming back to the platform after they find what they need unless they're the continuous growth type (which I hope they are!)

On the UX testing side, this would of course need to have good testing/tracking of the user like [Mixpanel](https://mixpanel.com) and while data privacy is always a concern -- I think it could be mitigated by being upfront that as a UX-testing platform this is a measurement tool.

Let's jam on this sometime

Umar

-------------------------

paulwalnuts | 2022-03-30 15:13:07 UTC | #3

Hey Umar!

Thanks for the feedback. I think the first step here is to build a database of DAO operators we could tap to continue doing user testing with. I was hoping paid incentives would help operators keep coming back to finish UX tests, but maybe that isn't really a great incentive. Either way, you brought up an excellent point which needs to be validated.

When you say we would need good testing/tracking from Mixpanel, are you talking about general analytics or to utilize Mixpanel to help track individual tests? I agree with the former, but I'm not sure if we need to decide a solution on how we track individual UX tests. 

As for data privacy, I think it's definitely a concern since we are asking users to connect their wallet. Again, I think this needs to be validated as an actual user concern and how we might get eyes on how the tool is being used.

-------------------------
