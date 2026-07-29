---
id: 12419
title: "Passport scoring-as-a-service"
slug: passport-scoring-as-a-service
category: open-discussion
url: https://gov.gitcoin.co/t/passport-scoring-as-a-service/12419
created_at: 2022-12-21T13:45:06.373Z
last_posted_at: 2023-01-23T01:03:07.197Z
posts_count: 10
views: 6758
like_count: 38
---

# Passport scoring-as-a-service

<https://gov.gitcoin.co/t/passport-scoring-as-a-service/12419>
j-cook | 2022-12-21 13:45:06 UTC | #1

***The aim of this post is to explain how passport scoring-as-a-service enables Gitcoin Passport to act as an important Sybil defense Lego in the Gitcoin grants protocol***

Gitcoin is migrating from being a centralized grant-giver to being a decentralized grants protocol. To do this, developers are creating building block, or "[Lego](https://hackmd.io/DIiRYEIjQmagN53RCs9fYg?view)", tools that can be used by individual round owners to implement their own Sybil defense strategy. One of the most well-known Lego's is [Gitcoin Passport](https://passport.gitcoin.co/).

Gitcoin Passport is a tool that allows users to collect stamps that provide evidence that the holder is a real person. These stamps might prove that a user has engaged in certain hard-to-fake web2 or web3 activities in the past such as having a Twitter account with a certain amount of followers, a Google account or a BrightID or Proof-of-personhood persona. Collections of stamps act as evidence of personhood such that a trustable passport is difficult to create quickly or cheaply enough to be used by a Sybil attacker. Specific subcommunities can also define their own set of stamps - perhaps certain POAPs or NFTs that demonstrate that a user was present at some event or contributed to some project. Combinations of stamps can be used to quantify the extent to which a user should be trusted.

## Scoring

Some kind of analysis pipeline is required to translate stamp ownership into trustability. Representing a stamp collection in the form of a trust score enhances the privacy preserving qualities of Gitcoin Passport by only exposing to apps the user's score, not the stamps from which the score was derived (which could in some cases otherwise be used to "fingerprint" an individual). Personal identifying information such as doxxable connections to social media are already omitted from the Gitcoin Passport as the stamp is generated after a one-time exposure of, for example, a Twitter account. Only the stamp is preserved, indicating that the user demonstrated ownership of the account, but no information about which specific account they own.

Apps are therefore required to make decisions about the trustability of a user from analyzing stamps alone. A minimal scoring example might be to simply count the stamps - more stamps = more trust. However, different stamps can offer stromger or weaker evidence of personhood. A simple stamp-count overlooks this and assumes equality among stamps. A Sybil attacker could easily use this oversight to create passports full of "cheap" stamps to game the stamp-count algorithm. Alternatively, perhaps strongly favouring very expensive NFTs or exclusive memberships, or putting high thresholds on metrics such as follower count for social media accounts could effectively deter Sybil attackers. However, this prices out many honest users as well as Sybils and also excludes honest newbies who have not had time to build up much of an online track record.

This tension between eliminating Sybils while being as inclusive as possible to a diverse userbase neccessitates a more sophisticated approach to Sybil scoring.

## Trust Bonus

Gitcoin Passport exposes an API for scoring passports that has its roots in the Gitcoin Fraud Detection and Defense (FDD) trust bonus algorithm. The data fed into the algorithm are the stamps in a user's passport. The scoring algorithm is effectively a weighted sum of the stamps normalized to range between 0 and 1. The grants protocol can then interpret this score as a trust metric and set a threshold value that users must exceed in order to participate in a grant round. Alternatively, the score can be used to amplify or dampen a user's influence in the round rather than imposing a binary in/out condition.

The challenge for developers is to determine the optimal weigths assigned to each specific stamp. This is an area of synergy between Gitcoin Passport and FDD. Since FDD is concerned with identifying diagnostic signals for Sybils by analyzing Gitcoin data, they are well positioned to examine the complex relationships between stamp combinations, honest users and Sybils. One aspect of this is identifying how strong a signal can be extracted from certain stamps, and another is suggesting alternative stamps that have particularly high signal. Given a set of possible stamps, FDD can determine the relative importance of each as predictors of Sybil accounts, and define the weighting that the stamps are assigned in the trust score calculation.

Gitcoin Passport can then incorporate these weightings into their trust score algorithm and provide the scoring as a service - abstracting the data scraping, processing, analysis and interpretation away from the end-user.


## Customization

The above approach is a very convenient way for round manager to determine, algorithmically, how much to trust individual users without exposing their personally identifying data. However, for some use-cases the standard set of stamps might not be sufficient. For example, a specific grant round might focus on participation in certain subcommunities, or feel that a certain bootcamp POAP is very important, or perhaps certain rounds might be better tuned to eliminate more Sybil's at the cost of excluding more false-positives (e.g. a DeFi round) or tuned to be inclusive at the cost of missing more Sybils (e.g. an environmental or social cause that attracts more new users).

In these cases, the default weighting algorithm provided by Gitcoin's FDD analysis might not be optimal. Therefore, the scoring service must be customizable. Customization can happen in the scoring service itself, by overriding the FDD-suggested weights. Development of a second layer of app that modifies the weights in the scorintg service is already a roadmap item for Gitcoin Passport. Users that override the weights would still be able to use the service as normal, but with an intermediate stage of weight-adjustment. Later, multiple scoring algorithms could be developed so that the service can satisfy as many use-cases as possible. Each time a user itnegrates the scoring service, a new instance of the scorer is created, meaning that many scorers with different configurations can exist simultaneously, serving different communities. 


For users that to define their own scoring algorith, Gitcoin Passport offers a Software Development Kit that includes functions for reading and writing to and from streams in Ceramic (where Gitcoin Passport data lives), verifying and scoring Passport stamps. This gives complete freedom to developers to implement any algorithm they wish calculate their trust scores. However, they also have to deal with the data cleaning and validation steps that are taken care of as part of the scoring service. This includes de-duplication, where the service checks for users submitting the same stamps multiple times.


## Scoring as a Service

The usefulness of the scoring process depends upon how intuitive it is to implement for the end users that need to implement it. A straightforward example is a round manager in the new Gitcoin grants protocol that wishes to use the trust score of each user to determine their influence in the round. They have the option to implement something bespoke for themselves by developing using the Gitcoin Passport SDK or to build using the standard scoring model. The latter option is set up as a service in order to be as simple to implement as possible. To use the scoring service, each user is required to sign a message proving ownership of an Ethereum address. For each proven address, the service grabs the passport data associated with the addresses from Ceramic and applies the FDD scoring algorithm, returning a trust score for each address. This is all handled "under-the-hood" so the user never has to interact with Ceramic or handle any stamp verification or validation - this is all handled by the scoring service.

## Outlook/summary

The scoring algorithm is a critical part of what makes Gitcoin Passport so useful - it takes the evidence presented in the form of stamps and presents it as a number that conveys the trustability of the passport holder. This means it can be used as a Lego in a project's Sybil defense strategy. Providing scoring as a service ensures the scoring Lego is easy to use and widely accessible, while also being customizable to different use cases.

-------------------------

epowell101 | 2022-12-21 19:10:10 UTC | #2

The vision - and execution here - is pretty incredible so much so that it helps restore my faith in DAOs.  We are not all talk, vibes, memes, votes, & votes about voting - there is cutting-edge software, community building & data science happening as well -> in order to bring closer a world in which communities can fund their shared needs through quadratic voting & more.

-------------------------

castall | 2022-12-22 21:14:34 UTC | #3

I appreciate your detailed thoughts on scoring-as-a-service. I imagine most apps using passport for sybil resistance will want this.

You mention privacy. I think that's important, so let's discuss what we're already doing and what we still need to do.

[quote="j-cook, post:1, topic:12419"]
generated after a one-time exposure of, for example, a Twitter account.
[/quote]

How do we ensure that this one-time exposure isn't leaked by the stamp issuer?

[quote="j-cook, post:1, topic:12419"]
This includes de-duplication, where the service checks for users submitting the same stamps multiple times.
[/quote]

How does the scorer service deduplicate with

[quote="j-cook, post:1, topic:12419"]
no information about which specific account they own. ?
[/quote]

The scoring service would need access to a range of stamps from an individual. Do we currently have a means for an individual to authorize that access? If yes, how do we ensure that the information isn't reshareable (e.g. the scoring service leaks what it knows)? Or is the set of stamps a user holds public (minus the specific accounts used, which is redacted like you said before)?

BrightID has a solution to prevent cross-linkability between apps that leaves no data (such as account information or ownership proofs) on BrightID nodes. I can go into more detail about BrightID's approach and other solutions we explored once I get a fuller sense of what Gitcoin Passport is already doing for privacy, and what still needs to be done.

-------------------------

koday | 2022-12-22 23:07:16 UTC | #4

[quote="j-cook, post:1, topic:12419"]
For example, a specific grant round might focus on participation in certain subcommunities, or feel that a certain bootcamp POAP is very important, or perhaps certain rounds might be better tuned to eliminate more Sybil’s at the cost of excluding more false-positives (e.g. a DeFi round) or tuned to be inclusive at the cost of missing more Sybils (e.g. an environmental or social cause that attracts more new users).
[/quote]

I found this super interesting! Excited to see how this will be customized to maximize benefits for different rounds as more and more start to run on the protocol.

-------------------------

ZER8 | 2022-12-23 07:17:50 UTC | #5

Kudos for the excellent article @j-cook, I guess that it can be really eye opening for everyone interested in the evolution of sybil defense in Gitcoin rounds and also all around web3.

[quote="j-cook, post:1, topic:12419"]
. For example, a specific grant round might focus on participation in certain subcommunities, or feel that a certain bootcamp POAP is very important, or perhaps certain rounds might be better tuned to eliminate more Sybil’s at the cost of excluding more false-positives (e.g. a DeFi round) or tuned to be inclusive at the cost of missing more Sybils (e.g. an environmental or social cause that attracts more new users).
[/quote]

There was a lot of back and forth between all the parties involved in the grant round to decide what those "tolerences" were for each type of cause round. I have to be honest I didn't think about this situation it in the way you described here when I was in the game, but it's fascinating how much what you described above resembles the way in which he have kinda handled eligibility(taking into acount that in the past we were operating in a DAO dynamic environment).

[quote="j-cook, post:1, topic:12419"]
To use the scoring service, each user is required to sign a message proving ownership of an Ethereum address. For each proven address, the service grabs the passport data associated with the addresses from Ceramic and applies the FDD scoring algorithm, returning a trust score for each address. This is all handled “under-the-hood” so the user never has to interact with Ceramic or handle any stamp verification or validation - this is all handled by the scoring service.
[/quote]

The fact that bad actors are actually very good at emulating "honest" behavior may give the Passport/FDD teams a lot of headaches as the red team will observe closely what the blue team is doing. If I where a malicious entity I would read all the articles posted on the forum and try to prepare my game for future rounds => Users may have squeaky clean ETH addresses that look great to the eyes of the "observers"(may it be an algo or human), but their intentions may prove to be the exact opposite. The way in which the sybil spectrum evolved in the past year is worrisome to say the least and it's currently still a huge unsolved problem(and opportunity also). It's also fascinating to see it all evolve. 

While the challenges are quite diverse and complex to face it does seem that most of the threats to efficient capital allocation in the rounds can be reverse engineered out of them  in more way than one.

-------------------------

DisruptionJoe | 2023-01-03 14:34:42 UTC | #6

The scoring service as built buy the GPC team using analysis & data science from FDD now lives here: https://github.com/gitcoinco/passport-scorer

-------------------------

owocki | 2023-01-12 13:16:09 UTC | #7

[quote="j-cook, post:1, topic:12419"]
For users that to define their own scoring algorith, Gitcoin Passport offers a Software Development Kit that includes functions for reading and writing to and from streams in Ceramic (where Gitcoin Passport data lives), verifying and scoring Passport stamps. This gives complete freedom to developers to implement any algorithm they wish calculate their trust scores
[/quote]

Quick Knowledge Share Post:

I was just revisiting the greenpill episode that I did with [Professor Bryan Ford](https://bford.info/) (who has been working on sybil resistence for 18 years).

At [this timestamp](https://youtu.be/PlDOjDu-mpU?t=2130) I asked him about anti sybil aggregators (Passport).  In his answer, Professor Bryan Ford makes a couple great points about designing aggregating scoring algorithms. 

TLDR:  

0. Professor Bryan Ford is against relying whollly on mechanisms that are fungible with money (eg stake X tokens get $X in cost of forgery) bc they are exclusionary to ppl without $$$.
     - a holy grail might be to find mechanisms that have a high cost of forgery for attackers but are marginally difficult for actual ppl 
1. Professor Bryan Ford advises that hybrid mechanisms can have problematic attributes depending on whether you use an AND/OR gate on them.
      - (**fungible** with money mechanism) **OR** (**non fungible** with money mechanism) = (**fungible** with money mechanism) 
     - (**fungible** with money mechanism) **AND** (**non fungible** with money mechanism) = ( **NON fungible** with money mechanism) 

A few recommendations:
1. In the docs for the scoring algorithm, it might be worth expanding on these best practices.
2. The [whole episode](https://youtu.be/PlDOjDu-mpU) is worth its weight in gold for ppl designing passport IMO.  But [this timestamp](https://youtu.be/PlDOjDu-mpU?t=2130) covers the point above.  If you're working on Passport, it might be worth listening!

-------------------------

ale.k | 2023-01-13 04:36:28 UTC | #9

Very much in agreement on prioritizing (and continuously reminding ourselves) not to be N America-centric here in terms of what’s “cheap” and what’s “costly.” We discuss this a lot with the incentive for farming-- $2USD is worth an hour of work to some. $2USD/per day is incentive enough for all manner of systems testing. Thinking of captcha farming, for example…

Agree that documentation can help to address some of this in terms of “best practices” – but maybe we also want to intentionally seek out and tell the story of example-exploits that iterate the intention and the pay-out that the attacker was seeking. @DisruptionJoe @j-cook on best possible medium for this type of story-telling…

Personally I think, the extractor/attacker dynamic and all of the assumptions that go along with it deserve examination… and caution in how we deploy our inherited anti-fraud language is also probably something to keep top of mind as we build. Will listen in on the episode here with my coffee tomorrow :headphones: - thanks for kicking off this convo & for the rec @owocki

-------------------------

letmehear | 2023-01-13 11:18:34 UTC | #10

how to create first grand in gitcoin , sir ?

-------------------------

llllvvuu | 2023-01-23 01:03:07 UTC | #11

Personally, I think supporting a large universe of stamps is a **good feature for Passport but a bad feature for any particular Passport score.**

A normal person will collect 2-5 stamps to join a community (such as a Round built on Grants Protocol). If they join many communities, they may accumulate more stamps, but I don't think we should privilege that. Because at that point one is advantaging stamp collectors and power users to a degree which I don't feel is inclusive.

One could try to level the field by capping or heavily diminishing returns past 5 stamps. But this wouldn't work, because stamp collectors would just start over on new passports.

I think **each community admin should be decisive about using a Passport score which is decisive about focusing on a small universe of stamps which is feasible for a normal user to complete**, so that they don't get flexed on by someone with 1000 stamps.

-------------------------
