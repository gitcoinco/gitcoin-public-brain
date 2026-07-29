---
id: 10770
title: "The Grants 2.0 Funding Stack - Choose Your Own Algorithm"
slug: the-grants-2-0-funding-stack-choose-your-own-algorithm
category: gitcoin-grants
url: https://gov.gitcoin.co/t/the-grants-2-0-funding-stack-choose-your-own-algorithm/10770
created_at: 2022-05-31T23:03:21.144Z
last_posted_at: 2022-08-23T08:36:07.090Z
posts_count: 3
views: 4470
like_count: 22
---

# The Grants 2.0 Funding Stack - Choose Your Own Algorithm

<https://gov.gitcoin.co/t/the-grants-2-0-funding-stack-choose-your-own-algorithm/10770>
DisruptionJoe | 2022-06-01 16:41:51 UTC | #1

# Choose Your Own Algorithm

Grants 2.0 will bring a new paradigm where users will dictate the terms used to fund their shared needs. We might call this the era of CYOA - Choose Your Own Algorithm

Because Quadratic Funding’s theoretical implementation assumes uniqueness of voters, the practical implementation requires an iterative process to discover vulnerabilities and adjust the dynamic components of the system to better align the outcomes with the intention of the community.

**Grants 2.0 will allow any community to choose it’s own funding stack.** Two rounds could fund the same cause with different rule sets, or they could make one large pool combined with better democratic and scientific processes for achieving better outcomes.

The complexity of the system means that an evolutionary approach is appropriate. Users will choose their communities based on how well the communities align with their values. Resources will continue to flow to communities which fund their shared needs in a legitimate and credibly neutral way.

![|624x351](upload://szE7GfGggrPyMwwHoXFe9TzxwgJ.jpeg)

# Grants 2.0 System Components

The backend for grants 2.0 will be hosted on distributed storage creating an “immutable” registry for each of the three components of a grants round.

1. Identity Registry
2. Grants Registry
3. Matching Pool Registry

Each of these components will have a Gitcoin user interface to interact with it. Eligibility for the Gitcoin community UI will be dependent on the Gitcoin’s code of conduct, Gitcoin’s Terms of Service, and Gitcoin’s Platform Eligibility Policy which are enforced by the community through the Fraud Detection & Defense workstream.

Gitcoin community rounds will still be run seasonally and other ecosystems and cause communities will likely choose to run theirs at the same time for a while. Most will use the Gitcoin UI to do this for a period of time after the Grants 2.0 launch.

# Optimizing the Functions

A grant round uses a function f(f(x)) to distribute funds. For Gitcoin community rounds we might consider this f(FDD) as the Fraud Detection & Defense (FDD) workstream is responsible for multiple dynamic components.

The primary functions that make up the f(FDD) function are:

* Passport Verification (Sybil Defense)
* Grant Eligibility

*Note: FDD has done some work on Funding Mechanism designs which has not been used, but is likely relevant when Grants 2.0 is released.*

Each of these functions is composed of multiple inputs which eventually deliver a usable result. Many of these processes involve humans in the loop to statistically validate the algorithms are functioning properly at scale along with continually identifying new behaviors and discovering unknown attack vectors.

Adding even more complexity is the human element in the system. A grant reviewer gets better over time by communicating with others. A community may have a “bad apple”, but be a positive community. An accused user may be subject to a misinterpretation. Etcetera.

Here are all the primary and secondary mechanisms we are currently monitoring or planning to use with Grants 2.0 with a * indicating which are currently being used and ^ indicating current work is being done.

## Funding Mechanism

**f(f(x)) = Funding Mechanism***

The funding mechanisms a community may use to calculate the final matching pool earnings of each grant after a round. This is a combination of many other input functions below.

**f(p) = Pairwise Dampening Coefficient***

A collusion deterrent mechanism based on similar patterns between users.

**f(k) = Plural Pairwise Dampening Coefficient**

Dampening adjustment which incorporates social distance to encourage outgroup collaboration. See @erich [model here](https://gov.gitcoin.co/t/how-soulbound-tokens-can-make-gitcoin-grants-more-pluralistic/10077)

**f(t) = Taxation Mechanism***

Ways to utilize participation fees to change the game theory of a funding mechansim.

## Passport Verification (Sybil Defense)

**f(t) - Gitcoin Trust Score (GTS)***

A score that determines if a user’s donations are eligible for matching consideration in Gitcoin community rounds. This score is also available for dapps to access through passport if they do not want to roll their own algorithm. It can be used to weight influence as a coefficient, or a threshold may be set to convert it to a binary. Gitcoin currently uses both as the “Trust Bonus” determines influence and a binary eligibility determination is used for users deemed over x% likely to be sybil by the probabilistic output of our machine learning algorithm.

**f(u) - Community Passport Verification (CPT)^**

Any community can roll their own user verification using Gitcoin Passport. The Gitcoin trust score is the Gitcoin community’s CPT.

**f(c) = Community Trust Rating (CTR)**

Every stamp issuing community has a trust score. To determine a trust score based on stamps, an algorithm developer would likely need to know if stamps are from communities which can be trusted . To begin we will likely use a binary score which only gives weight to communities we know and trust. FDD would likely create a measurement for the Gitcoin community.

**f(i) = Inter-reviewer reliability( (IRR)***

A score showing the reliability between reviewers to be used in assessing the quality of human evaluations of algorithmic outputs. While this score can’t be used as a “target”, it can show if the humans involved in a review process may need more training or may even be attempting to sabotage a round.

## Grant Eligibility

**f(e) = Grant Eligibility Score (GES)**

A grant review process can be done by one person in a community who is the delegated authority, or by any other mechanism that gives each grant a binary output for eligibility. The current FDD process uses transparency and community reviewers along with a community flagging system for disputes and an appeals process for resolving incorrect determinations and evolving the Gitcoin community eligibility policy. Our work on permissionless reviews is at 50% completion and may serve as a Use Case Specific Reputation stamping opportunity for grant reviewers.

**f(u(x)) = Use case specific reputation^**

Any community may come up with a specific use case for stamping a passport. Some examples might include:

* DAO Contributors
* Donors to a cause
* Attendance at an event
* Certification of a skill

While some might consider a binary output (Did they or did they not), other use cases may want to add some type of weighting specific for the use case such as “how trusted is this reviewer”.

## Grant Discovery

**f(d) = Grant Discoverability Sorting (GDS)***

Each community will choose a sortition mechanism for ordering the grants on the UI. Our a/b test in GR9 showed that changing the sortition DOES produce a substantial difference in outcome. (FDD does not work on this at this time.)

**f(r) = Round Discoverability Placement***

The same principle as the GDP above but for rounds & communities.

-------------------------

llllvvuu | 2022-08-23 17:43:46 UTC | #3

This is a bit off topic, but do we have a wiki for all of these techniques/algorithms? Some of these ideas come from different forums, and require some background knowledge to find on Google. As the QF ecosystem becomes more modular, pluralistic, and decentralized, we could end up with hundreds of variants at every part of the stack. It would be helpful for both researchers and end users (community managers) to have a view into the frontier of global research outside of core contributors/researchers.

If not, I'd be happy to propose and/or contribute to a bounty for this.

-------------------------

DisruptionJoe | 2022-08-23 08:36:07 UTC | #4

Not yet. We have only recently begun to split out our process to include more than the SAD which you can read a high level overview here: https://gov.gitcoin.co/t/closing-the-gap-between-fdd-and-gitcoin-passport-sybil-defenses/11218

Now we are searching for the pluralist answer for the problem by building out a meta-model solution. The long-term goal is to crowdsource the models in a similar way to Numerai. 

Please reach out on Discord and I'll send you a Calendly to discuss how you could help!

-------------------------
