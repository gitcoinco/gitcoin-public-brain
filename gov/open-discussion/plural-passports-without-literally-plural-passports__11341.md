---
id: 11341
title: "Plural Passports without literally plural passports?"
slug: plural-passports-without-literally-plural-passports
category: open-discussion
url: https://gov.gitcoin.co/t/plural-passports-without-literally-plural-passports/11341
created_at: 2022-08-23T00:06:58.293Z
last_posted_at: 2022-11-13T18:14:43.653Z
posts_count: 9
views: 4443
like_count: 25
---

# Plural Passports without literally plural passports?

<https://gov.gitcoin.co/t/plural-passports-without-literally-plural-passports/11341>
llllvvuu | 2022-08-23 00:13:35 UTC | #1

One of the great things about Gitcoin's Passport vision is that passports can draw legitimacy from multiple credentials ([pluralism](https://www.radicalxchange.org/media/blog/why-i-am-a-pluralist/)), rather than de-duping via a single-point-of-failure such as the USA's [Social Security Number (SSN)](https://www.ssa.gov/ssnumber/).

That said, "dual citizenship" presents a challenge if the end-user considers every "citizenship" as independently legitimate. (arguably, dual citizenship IRL is already overpowered even without this, but to a much smaller degree)

The fundamental choice is: if I have stamps from all of {PoH, Worldcoin, Idena, Bright ID, KYC, Web2}, what is the incentive for me to put all of these on the same passport, versus creating multiple passports?

The toy model I'll assume here is:
* There are a number of "personhood score" algorithms `personhood(credential1, credential2, ..., credentialN)` each developer can use.
* Each end-user application delivers a payoff of `payoff(personhood)` for a given personhood score.
* Composing these functions implies a payoff function `payoff(credential1, credential2, ..., credentialN)` for the application.
* If every application has their own passport registry, one may choose a different distribution of stamps across passports per app. If every applications checks the Gitcoin registry to dedup stamps, then users must use a consistent set of passports across all apps. In the latter case, each passport has a `total_payoff(credential1, credential2, ..., credentialN)`.
* WLOG, we'll just work with one `payoff` function.

## When to split and when to merge?
If there is some partition of my set of credentials such that `sum(payoff(credentials_i)) > payoff(credentials)`, then it is in my self-interest to maintain multiple passports along this partition.

If `payoff` is convex, then this will never hold, due to [multivariate Jensen's inequality](https://math.stackexchange.com/questions/2190473/generalizing-jensens-inequality-to-several-variables) (in fact, the opposite would hold - if there is someone with an orthogonal set of credentials, I should merge with them). However, personhood is explicitly meant to support concave payoffs - the problem of splitting credentials mirrors the problem of splitting tokens across wallets, in that 2x the personhood shouldn't give 2x the payoff.

In most cases (for example, cutoff-based systems where you get the max payoff for having a sufficient number of credentials), we'll be incentivized to split.

## Cross-credential linkability?
A natural way to approach this (other than accepting only one type of credential), would be to have e.g. a Worldcoin ID linkable to a Bright ID. That way, split passports can be detected and penalized.

Not only do we need to be able to detect this link, but we should be able to detect it *post-anonymization*. i.e. in the following diagram, the application must be able to deduce B without knowing C or D:

![image|414x297](upload://4ZqXrQg1Bd8vHW0w7XAum0a5QOR.png)

There are possibly some clever cryptographic ways this could be done, but at some point *someone* must know A. In practice this means that information linking a face, iris, social graph, Web2 handles, etc together would be out there somewhere.

One could argue that forming this profile is both inevitable (and presents no real harm) and a necessary precondition for Sybil resistance (otherwise, how do we prevent someone from using their iris for one account and their face for another?), and it is sufficient privacy to just not link this profile to any actual activity.

Another viewpoint could be that it is unviable for communities to accept outside credentials (especially anonymized credentials) without having their own additional screens.

I'm curious to hear thoughts on these viewpoints.

-------------------------

ccerv1 | 2022-08-23 04:02:58 UTC | #2

This is a wonderful, well-articulated post. It triggered some late night thoughts. 

I think I’m ok with people having multiple passports or identities — provided they don’t engage in Sybil behavior.

Borrowing your dual citizenship analogy: dual citizens IRL can choose which passport to use, however they can’t use their passports to be registered in two countries at once or to count as two people in one country. Once they’ve entered a country with a given passport, they can only leave by showing the same passport.

The primary issue Gitcoin cares about is stopping n sock puppets from getting match funds for funding the same project n times. 

We need to learn to better detect Sybil behavior. We need to increase the price / diminish the benefit of Sybil behavior. We need to create positive network effects for reputation building behavior. Cross linking credentials could definitely be one of those ways!

-------------------------

owocki | 2022-08-23 17:08:27 UTC | #3

[quote="llllvvuu, post:1, topic:11341"]
The fundamental choice is: if I have stamps from all of {PoH, Worldcoin, Idena, Bright ID, KYC, Web2}, what is the incentive for me to put all of these on the same passport, versus creating multiple passports?
[/quote]

One of the reasons I liked the idea of using a PersonhoodScore in [this post](https://gov.gitcoin.co/t/characterizing-the-sybil-resistance-problem/11235) was that it allows the system to scale against different sophistication levels of attackers, including handling dual passports elegantly.

assuming cost of forgery = personhood score, if the cost of forgery of identity 1 is $10, and the cost of forgery for identity 2 is $100, then the combined identity for these two is $110.   

if you can get $10 in matching from identity 1 and $100 in matching from identity 2, or if you combined the passports + get $110 in matching, then there is no incentive to sybil attack the system.

[quote="llllvvuu, post:1, topic:11341"]
If there is some partition of my set of credentials such that `sum(payoff(credentials_i)) > payoff(credentials)`, then it is in my self-interest to maintain multiple passports along this partition.
[/quote]

I think this is what you already said in different words tho :)

-------------------------

llllvvuu | 2022-08-23 17:42:55 UTC | #4

[quote="owocki, post:3, topic:11341"]
if you can get $10 in matching from identity 1 and $100 in matching from identity 2, or if you combined the passports + get $110 in matching, then there is no incentive to sybil attack the system.
[/quote]

This might not be realistic though. For example for a voting app, would you get 2x the voting power for having 2 credentials? Even in QF I'd argue that the match amount shouldn't equal the personhood score. For example, let's say we updated the "legacy" [trust score](https://gitcoin.co/blog/trust-bonus) to be linear in personhood score. That would require removing the 150% cap, allowing me to get 250% or more in trust bonus if I used all of the verification methods. This number would only go up the more verification methods get added.

So in this system, indeed there would be no incentive to "Sybil", but that's because we would just be handing excess power to the user directly.

[quote="owocki, post:3, topic:11341"]
I think this is what you already said in different words tho :slight_smile:
[/quote]
The math here is actually important. Any system with a cap or tapering will be concave. For example the spreadsheets in the [post you linked](https://gov.gitcoin.co/t/characterizing-the-sybil-resistance-problem/11235) (where you link to [this](https://gov.gitcoin.co/t/establishing-a-new-process-for-identify-verification-scoring-and-removing-troubled-id-methods/7506/3?u=llllvvuu)) are concave (e.g. if the aggregate match was $100k and I was capable of getting $1m cost-of-forgery then I would want to split into 10 passports). And indeed they should be concave: in a world where there are hundreds of verification mechanisms, someone shouldn't get double the match because they had the tenacity to sign up with 20 verification methods instead of 10 (otherwise you get farming captchas all over again).

Another point to note is that forgeries themselves are not independent events. So it's unclear if the assumption `cost_of_forgery(methods) == sum(cost_of_forgery(methods[i]))` is ideal.

-------------------------

owocki | 2022-08-23 17:47:58 UTC | #5

[quote="llllvvuu, post:4, topic:11341"]
For example for a voting app, would you get 2x the voting power for having 2 credentials?
[/quote]

thats up to whomever is writing the scoring algorithm + the weight they assign to each stamp.

[quote="llllvvuu, post:4, topic:11341"]
Even in QF I’d argue that the match amount shouldn’t equal the personhood score. For example, let’s say we updated the “legacy” [trust score](https://gitcoin.co/blog/trust-bonus) to be linear in personhood score. That would require removing the 150% cap, allowing me to get 250% or more in trust bonus if I used all of the verification methods. This number would only go up the more verification methods get added.
[/quote]

i dont think trustbonus scales in a personhoodscore world.

IMO cGrants is architected backwards. It makes more sense to start with the personhood score + guide the user to either increasing it or muting their contributions by computing their trustbonus.

![7P7PubyhFs-9yHGdGjiWpVSYZr6vV5N40_o5gJfB88YOS0oXMHdKBAKxPiFkOlSf37ZiVwMxl77smW-EWEkNdKlszYzQLTIAMyuWWh_gt0pRMetn5vvEe95xgz1V0lfkee9Q56LL7yE6XGlsYlm7rXA|690x288](upload://KTdgzQgZoF79CQBFxwloAhBJdz.jpeg)

[quote="llllvvuu, post:4, topic:11341"]
The math here is actually important.
[/quote]

I agree. Especially about your point about convex/concave designs.  Perhaps whomever at the FDD (or similar) is designing the scoring algorithms for a grants 2.0 world can chime in from here about how those are being designed :)

-------------------------

llllvvuu | 2022-08-23 17:56:30 UTC | #6

[quote="owocki, post:5, topic:11341"]
![7P7PubyhFs-9yHGdGjiWpVSYZr6vV5N40_o5gJfB88YOS0oXMHdKBAKxPiFkOlSf37ZiVwMxl77smW-EWEkNdKlszYzQLTIAMyuWWh_gt0pRMetn5vvEe95xgz1V0lfkee9Q56LL7yE6XGlsYlm7rXA](upload://KTdgzQgZoF79CQBFxwloAhBJdz)
[/quote]

This is the spreadsheet I was referring to - at any given aggregate match amount it tapers at 100%, once I hit 100% I should start over with a new account, basically getting 100% per `aggregate_match_amount` in `cost_of_forgery` I'm able to accrue.

[quote="owocki, post:5, topic:11341"]
Perhaps whomever at the FDD (or similar) is designing the scoring algorithms for a grants 2.0 world
[/quote]
Agreed, very important workstream!

Oddly the FDD design space reminds me a lot of [Palantir](https://www.palantir.com/) (similar skillset and probably some tech that can be taken - though their ideology couldn't be any more different than ours)

-------------------------

owocki | 2022-08-23 20:04:22 UTC | #7

[quote="llllvvuu, post:6, topic:11341"]
This is the spreadsheet I was referring to - at any given aggregate match amount it tapers at 100%, once I hit 100% I should start over with a new account, basically getting 100% per `aggregate_match_amount` in `cost_of_forgery` I’m able to accrue.
[/quote]

i agree. [here](https://docs.google.com/spreadsheets/d/1e2j2qzQcZlz4Col5qqF3yxKr-NQ5SxVrFuGX7k-xyek/edit#gid=0) is a better model 
![Screen Shot 2022-08-23 at 2.03.52 PM|690x275](upload://zOgbcyGR2qnHOrreXKlSYgEIdeX.png)

-------------------------

ccerv1 | 2022-08-24 20:56:40 UTC | #8

Your post ~~nerd-sniped~~ inspired me to do some analysis on dual citizenship in real life. 

[quote="llllvvuu, post:1, topic:11341"]
That said, “dual citizenship” presents a challenge if the end-user considers every “citizenship” as independently legitimate. (arguably, dual citizenship IRL is already overpowered even without this, but to a much smaller degree)
[/quote]

My question: If you could have any two passports, which combination would afford you the greatest freedom to travel around the world with minimal overlap & reliance on a single passport?

The answer: Ghana & United Arab Emirates. Those passports enable visa-free travel to 131 countries, with only 14 cases of overlap.

Runner-up combos include: Andorra & Gambia, Cote d'Ivoire & Japan, Guinea & Malaysia. 

(If you have a US passport, dual citizenship in Ghana or Mali would offer the most visa-tree travel optionality.)

h/t: https://github.com/ilyankou/passport-index-dataset

-------------------------

chaselb | 2022-11-13 18:14:43 UTC | #9

With this considered, I could imagine organizations/platforms who might use Passport for sybil resistance might not use it as we imagine. Instead of computing some "trust score" as a function of all of the credentials within a passport, they choose 1 really robust/secure credential for their ecosystem. In this case, they don't technically NEED Passport, but Passport creates a common interface for these credentials, so a platform/org does not need to research how to integrate with a specific credential's SDK. Also, if they want to switch to a different credential, they can do that with ease without needing to deal with the different integration process of a separate credential. Also, from an end-user perspective, I can keep all of my credentials in one Passport. So if PlatformA requires BrightID and PlatformB requires KYC, then I have all of that in one place.

-------------------------
