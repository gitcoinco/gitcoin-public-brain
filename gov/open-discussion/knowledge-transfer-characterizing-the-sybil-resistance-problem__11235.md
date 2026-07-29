---
id: 11235
title: "Knowledge Transfer: Characterizing the Sybil Resistance Problem"
slug: knowledge-transfer-characterizing-the-sybil-resistance-problem
category: open-discussion
url: https://gov.gitcoin.co/t/knowledge-transfer-characterizing-the-sybil-resistance-problem/11235
created_at: 2022-08-06T05:44:24.194Z
last_posted_at: 2022-10-28T23:13:36.325Z
posts_count: 16
views: 11847
like_count: 55
---

# Knowledge Transfer: Characterizing the Sybil Resistance Problem

<https://gov.gitcoin.co/t/knowledge-transfer-characterizing-the-sybil-resistance-problem/11235>
owocki | 2022-08-26 17:48:18 UTC | #1

# Preamble

This is a knowledge transfer post. With my [recent disaffiliation from leadership in GitcoinDAO](https://gov.gitcoin.co/t/passing-the-torch/10971), I would like to pass along knowledge I have ascertained from 2.5 years of watching Gitcoin Grants grow. This post is a data point for the DAO, whose governance structures continue to retain full control & have final say of how to design Gitcoin Passport.
# TLDR

As Daniel Schmachtenberger [likes to say](https://podcasts.apple.com/us/podcast/a-problem-well-stated-is-half-solved/id1460030305?i=1000526825665), “A Problem Well-Stated is Half-Solved”.

In this post I will try to articulate what I have seen and convey my limited but earnest view on the design space of sybil resistance as it pertains to Gitcoin & the web3 ecosystem.

In this post, I make these assertions:
1. Sybil resistance is an important problem to address.
1. Sybil resistance is an adversarial game.
1. Sybil resistance is an iterative game.
1. Sybil resistance is an evolutionary game.
1. Sybil resistance is an infinite evolutionary iterative game between a diversity of adversaries.
1. What are the criteria for addressing sybil resistance?

This post is a 13 minute read.

# Table of Contents

- TLDR
- Wait, what are sybil attacks?
- The high upside of addressing this problem space.
- Meet your adversaries
- Criteria for desirable approaches to this problem.
  - Criteria 0: The complexity of large social systems
  - Criteria 1: The need for privacy-centricity &amp; sovereignty
  - Criteria 2: The need to avoid plutocracy
  - Criteria 3: Collusion
  - Criteria 4: The need to build in systemic defensibility
  - Criteria 5: The need to build network effects
  - Criteria 6: Enabling Innovation &amp; Preventing Capture with Modularity &amp; Forkability
  - Criteria 7: Enabling Innovation &amp; Preventing Capture with Decentralization
  - Criteria 8: The evolutionary nature of this game
- What will round 69 look like?
- In closing


# Wait, what are sybil attacks?

Many systems that aim to democratically decide outcomes, like Gitcoin Grants, assume each participant is a unique human.

This makes them vulnerable to sybil attacks, where a bad actor creates a large number of pseudonymous identities to subvert the service’s reputation system and gain a disproportionate amount of influence.

Sybil attacks undermine the legitimacy of blockchain-based democratic pluralistic processes. Learn more about sybil attacks [here](https://www.youtube.com/watch?v=v1Dm7FI2AdU).

# The high upside of addressing this problem space.

GitcoinDAO’s impact on the world depends on the success of Gitcoin Grants, which depends on [Quadratic Funding](http://wtfisqf.com), which depends on sybil/fraud resistance.

Without sybil resistance, Gitcoin Grants is a castle in the sky. Sybil resistance is the bedrock of Gitcoin Grant’s legitimacy & the lack of a solid foundational understanding of the problem is a constraint on it’s growth.

But the stakes are larger than GitcoinDAO.

Sybil attacks are why we can’t have nice things. Right now, the DAO ecosystem is built around one-token-one-vote or one-cpu-one-vote schemes. If sybil resistance was addressed, the ecosystem could move to systems built more on one-human-one-vote.

Addressing sybil resistance is very desirable if we want web3 systems that provide utility to everyday citizens of the world, not just the moneyed elite.

Addressing sybil resistance unlocks use cases like:

* quadratic funding
* quadratic voting
* Gini coefficient measurements
* UBI
* one-person-one-vote DAOs
* data collectives
* sybil resistant airdrops
* + other use cases we haven't discovered yet!

# Meet your adversaries

### Script Kiddies

![|624x269](upload://4sjVpV7tfrt9FgrTX07oSSKSgQv.png)

### Petty Criminals

![|239x320](upload://2DDbzw96ZtKE7cKgNV82VDwxIOG.jpeg)

### Rational Economic Actors

![|273x364](upload://rpvlqR3Of0aokvTHHs3IMWwokpy.jpeg)![|378x311](upload://8jnP5Xf8JsArYAR7Dj5SQn0Mz4h.png)

### [Solana DEFI Developers](https://www.coindesk.com/layer2/2022/08/04/master-of-anons-how-a-crypto-developer-faked-a-defi-ecosystem/)

![FZWO5fgWAAQUCxG|497x500, 75%](upload://4fjuXm0lAbFu8Afxl0neWHF4Ep8.png) 
![FZaO_83XEAEwsIf|500x500, 50%](upload://fKz9954IBfEYTU20DSc5FLlCBRG.jpeg) ![FZaxw6yakAAfgV0|585x500, 50%](upload://4aWUScIrWJRJWnTzcGvWkdpcmTB.jpeg)


### Organized Crime

![|417x218](upload://v8NokU1v2cBWYJe5lbW1R2NgLuD.jpeg)

### Nation States

![|485x340](upload://uLvqcFoR5NX5VIwbA8vTSpTtzh7.jpeg)

# Criteria for desirable approaches to this problem.

## Criteria 0: The complexity of large social systems

There are different sophistication levels for each of these adversaries. A script kiddie may lack the skills, organization, and conviction to pull off a sophisticated attack, whereas organized crime & nation states may have nearly infinite budgets, skills, organization, and conviction to attack a system. More sophisticated adversaries will grow & evolve over time, which requires either (1) constant vigilance or (2) systemic anti-fragility on behalf of DAOs that function as digital identity providers.

Adversaries have different motivations. Some adversaries may be in it for the money. Some are in it for the lolz. Some are in it to help you, some are in it to pwn you. Some are just bored and seeking a thrill.

Different adversaries may attempt attacks that are diverse from one another. Some adversaries may pursue schemes that are invulnerable to biometric identity + government identity countermeasures, but are vulnerable to timing-attack countermeasures. Other adversaries may try things that are invulnerable to web of trust and presence based countermeasures, but vulnerable to biometric countermeasures.

Because of the varying types of adversaries, the most comprehensively anti-fragile approach to sybil/fraud resistance will aggregate different types of countermeasures.

![Kirby_passport|400x270](upload://mq41VThVMs9i99fHVlWrDdJCUCH.gif)
(*A good guy aggreagting countermeasuroooooors)*

Because we’ve read [Impact Networks](https://gov.gitcoin.co/t/lessons-about-impact-networks/10305), we know that networks are good at sensing & responding to complex environments. Because of the complexity of the problem, a network is a better institution to address the problem than a company could be.

![rO4KKdujwVAxPJ9SezpusoX-OPCXdMNJZ1e_zwf8K-kxrUJ4V6e1T5J8-71fQLrBv1c3xn2kWfzDZgbZ4BjtjKUbaMejMJWsiE2rUXE_ejccSzcbeh9ui9ftDBIRFiI4CXyhiZho|690x434, 50%](upload://u6yjiPYknGsRAUzWGF9TLTAWdom.png)
*([Lessons from Impact Networks](https://gov.gitcoin.co/t/lessons-about-impact-networks/10305))*

## Criteria 1: The need for privacy-centricity & sovereignty

On challenge with building a system that can address sybil attacks is to manage identity information. Identity information is essential to identifying sybil attackers.

But there are countervailing forces to the need for identity.

In a world where [control of data is a liability](https://vitalik.ca/general/2019/05/09/control_as_liability.html), any designer of said system must avoid becoming a data honeypot - lest it become a headline one day, or worse, silently drift into becoming a deep-state style intelligence agency.

Another requirement of web3 based DID systems is to make them sovereign to their users (eg users can own/manage/delete their data) and privacy preserving. Eg when a dapp discovers whether a user is a unique user or not, they should not find out more information about the user than that without express consent.

## Criteria 2: The need to avoid plutocracy

Sybil resistance is a spectrum, from protecting against script kiddies to protecting against nation states.

One metric that has been kicked around to manage this is the idea of a TrustBonus. Basically you just amplify or dampen quadratic matching according to some percentage. Eg a user with

1. 100% trustbonus + $100 in matching will be able to allocate $100 in matching
2. 50% trustbonus + $100 in matching will be able to allocate $50 in matching
3. 150% trustbonus + $100 in matching will be able to allocate $150 in matching
4. And so on…..

[I was there in rounds](https://twitter.com/owocki/status/1271864852101791744) 4-6 when Gitcoin first started introducing SMS verification and later bright. I know how duct taped together that conception of sybil resistance was 2 years ago. I’m glad it has evolved but I think TrustBonuses are outliving their usefulness.

One reason i have such an aversion to continuing to talk about this as a TrustBonus is that its a legacy concept from the cGrants days that only applies to QF products (other sybil resistant dapps wont have trust bonuses since they don't have quadratic matches).

### OK, but what next?

One way of moving to a more manageable metric is moving to the idea of a Personhood Score = cost of forgery = the cost in USD it would take to forge a users identity. For a system wide KPI, that would make TCF = Total Cost of Forgery in the system, the ultimate KPI that the DAO shoots for to bootstrap a sybil resistant economy.

As the personhood score for a passport grows, it becomes more resistant to certain types of adversaries. Here is a rough estimate of personhood scores by adversary sophistication level:

![|624x64](upload://50TQUeA3o1gbWllqmaSxTH6Ujbd.png)

Cost of forgery is built by connecting multiple stamps. A very rudimentary example:

* If a user connects twitter (+ gitcoin governance decides twitter has a $.10 cost of forgery)
* and a user connects POH (+ gitcoin governance decides POH has a $100 cost of forgery)
* and a user connects brightID (+ gitcoin governance decides brightid has a $10 cost of forgery)
* then the total cost of forgery for that users identity is $110.10

Cost of forgery is how value is transmitted around the ecosystem of Passport users. If I am designing a dapp, and I know the cost of forgery for this user is $110.10, I can rationally reward the user with up to $110.10 worth of sybil resistant rewards.

So in the case of gitcoin, it can give $110.10 worth of matching. Rabbithole (if it integrates with Passport) can give $110.10 worth of rewards. POAP (if it integrates with Passport) can give $110.10 worth of POAP gas fees, and so on

The key insight behind personhood scores is that in an adversarial world there are different levels of sophistication of adversaries Gitcoin wants to protect against (script kiddies => organized crime => nation states). Instead of treating sybil resistance as a binary (yes/no), we instead treat sybil resistance as a spectrum, making the problem more manageable.

Conceptually, you can back into PersonhoodScores with the current architecture of TrustBonus, eg your trust bonus * your matching amount = current dollars at risk.

IMO cGrants is architected backwards. It makes more sense to start with the personhood score + guide the user to either increasing it or muting their contributions by computing their trustbonus.

![|624x261](upload://KTdgzQgZoF79CQBFxwloAhBJdz.jpeg)

I wrote more about this [here](https://gov.gitcoin.co/t/establishing-a-new-process-for-identify-verification-scoring-and-removing-troubled-id-methods/7506/3).

### The Problem with Plutocracy

This brings me to the one major problem with PersonhoodScores. It puts the sybil resistance in economic terms. If designers of the sybil resistant game are not careful, this could give the system very dystopian attributes.

If the TCF (Total Cost of Forgery) of the system is put into parity with the amount of capital in the system, then only rich people can have identities, that is dystopian

If there is not a way for everyday citizens to reliably create a high enough personhood score without having money, that is dystopian.

For this reason, it could be important to prioritize verification mechanisms that don’t filter out citizens without wealth. It could be important to track the number of moneyed identities active in the system vs non-monied identities. Such examples of these systems: BrightID, Proof of Humanity, biometric identification systems. (You can learn more about this problem [here](https://www.youtube.com/watch?v=PlDOjDu-mpU))

![Screen Shot 2022-08-06 at 7.43.46 AM|690x360](upload://7bFkvg2plLz95IVkIwRHPt1vWil.jpeg)

## Criteria 3: Collusion

Say that you’ve architected the perfect sybil resistant identity system.

Or a good enough system. A good enough IMO is a system where the TCF (Total cost of forgery) is greater than the amount of rewards that is available to citizens of the system to exploit it. 

So a good enough sybil resistant identity system is one where 
1. there is $3,000,000 TCF and there is a $2,999,999 matching pool. 
2. Or, in a world where passport is implemented by multiple dApps, there is $3,000,000 TCF and there is a $2,999,999 aggregate economic opportunity across all of those dapps.
3. Or, perhaps the DAOI decides it is willing to accept a 10% fraud risk, so when it has a $3,000,000 TCF, it supports a $3,299,999 aggregate economic opportunity across all of the dapps in Passport-ecosystem.

In this scenario, you still have to deal with collusion attacks. Stuff like “Hey if you contribute to my grant I’ll give you a bribe.” or “I’ll buy your identity from you”.

Really a good enough system is one where The TCB (Total cost of bribery) + TCF (Total cost of forgery) is greater than the amount of rewards that is available to citizens of the system to exploit it.

The bribery/collusion attack surface area is still under research, and deserves its own post.

## Criteria 4: The need to build in systemic defensibility

One of the things I find most inspiring about how Proof of Stake and Proof of Work are designed is how well they function by acknowledging that adversaries exist + fundamentally tilt the design of the system towards defensibility and anti-fragility. Both PoW/Pow, they both boil down to the simple principle of making a system much cheaper to defend than to attack.

1. In PoW, it is way more profitable (and way less risky) to use my mining hardware to mine the next block than it is to try and 51% attack the network.
2. In PoS, it is way more profitable (and way less risky) to use my mining hardware to mine the next block than it is to try and 51% attack the network.

This leads me to the following criteria: In Gitcoin Passport, it should be way more profitable (and way less risky) to participate in the network legitimately than to attack the network.

## Criteria 5: The need to build network effects

If you build the most perfect sybil resistant ecosystem, and no one is there to use it, does it make a sound?

This is called the cold start problem in n-sided networks. 

The flywheel of passport could grow like this: The more users use Gitcoin Passport, the more the TCF of Passport increases, the more dApps/stamps will integrate with it, the more utility it will provide, which causes more users to use it (and the cycle repeats).

How does one cold start this network?  With [Gitcoin Grants scale](https://gitcoin.co/results).

With the right configuration - as this flywheel spins, because networks fundamentally grow exponentially, TCF should start to grow exponentially. Here is an example of one such model of how this could grow (this is an illustration + not a promise of any sort):

![|376x241](upload://frMlfMv48iGucWHOQ9Tn4hYpi4z.png)

Learn more about the network effects of the Gitcoin ecosystem [here](https://gov.gitcoin.co/t/the-network-effects-of-gitcoindaos-protocols/10973).

## Criteria 6: Enabling Innovation & Preventing Capture with Modularity & Forkability

One thing I think is really important about Gitcoin Passport is how forkable it is.

Don't agree with Gitcoin’s (stamps|scoring algorithm|focus on sybil resistance). Fork it! Create your own. Over time, one could build a marketplace of stamping tools, scoring algorithms around Gitcoin Passport. Such a rich ecosystem is the foundation of the network effects of Decentralized Society.

![|624x353](upload://dfEDjyFmO9UsC02p9ucuNxZePT8.jpeg)

![|624x353](upload://bJnEO86ufqQQ5tGfChA3c6QQRky.jpeg)

![|624x376](upload://tLNmlfDBSQuFFDvN5opqG9jfwvW.jpeg)

Forkability requires [great documentation](https://docs.passport.gitcoin.co/) and a great devrel campaign. I’ll be curious to see what evolves here. Let me know if the DAO wants an intro to anyone I know who does DevRel!

A great devrel campaign enables decentralized innovation on top of the Passport Protocol. It invites contributions from everywhere and turns Passport into a schelling point for addressing sybil resistance & creating plural cooperation across social distance that grows stronger over time.

A great devrel campaign would be an attractor that would act as a memetic schelling point for people who want to solve this problem + enable them to contribute their resources (coding skills, capital, anti fraud data analysis, etc) to solving the problem. 
![1_sX8csWo6oQm_gq47--nKKA|690x387, 75%](upload://cHIWhN5XvJCEKMTxYZbGvUHevgx.jpeg)
If done right, this memetic schelling point could even increase in "gravity" over time as more resources are added to it, compounding in strength over time.

## Criteria 7: Enabling Innovation & Preventing Capture with Decentralization

As Gitcoin Progressively decentralizes over time, I think itll move from centralization to a decentralized and modular set of protocol based codebases.

It will move from [socialware to trustware](https://orca.mirror.xyz/T70CmuhX95ubkw_JHOxSEy8d_EFeYXgtJnF13mPtaZE).

* “Socialware - Mechanisms that create assurances through human relationships, incurring a high social coordination cost”
* “Trustware - Mechanisms that create assurances through technology, incurring a low social coordination cost”
* “By using blockchains as our underlying assurance mechanism, we can codify organizational governance through code and not purely documented principles that rely on humans to coordinate around. In doing so, we foster greater trust between parties by minimizing trust in people and maximizing trust in technology.”

![Screen Shot 2022-08-08 at 8.08.10 AM|690x186](upload://icNG7qF3fKizCOfqXcmxe8xPK9C.jpeg)

I think that Gitcoin’s final form could be that of a [Hyperstructure](https://twitter.com/owocki/status/1543651089462939648). Hyperstructures *are crypto protocols that can run for free and forever, without maintenance, interruption or intermediaries*.. The trustware in the center **is** the hyperstructure (blue). The rest of the things the push the network effects forwards are just humans doing whats rational / in their incentive set (purple). In a well designed system this hyperstructure will grow according to network effects (on the right)

On tradeoff I think is interesting to manage here is the time preference of the systems ability to manage attacks.

How can the base of the protocol harden (bc its trustware), but also evolve to continuously ongoing threats (socialware well governed)? Where are yearly, quarterly, weekly, daily, or instant feedback incorporated? Where is more governance oversight needed over socialware, and where can the system move to trustware? And on what time preference?  As the attackers evolve, how can the fraud defense evolve (0) effectively (1) without tipping off the attackers (2) but still in a legitimate (eg transparent to governance) way?

![|156x164](upload://lVnvLwGH9KMraI92Ebu0txiCtfz.png)

Which brings me to…

## Criteria 8: The evolutionary nature of this game

Gall's Law states that all complex systems that work evolved from simpler systems that worked.

With Gitcoin Grants, the simple rules are the rules of [Quadratic Funding](https://wtfisqf.com/). Basically.

1. Funds are continuously raised into a matching pool.
2. For 2 weeks every quarter, there will be a matching campaign where contributions from the crowd to grants in matching rounds n1-x that fill eligibility criteria ec[n] will be matched with funds from matching pool m[n] according to the [pairwse quadratic funding formula](https://ethresear.ch/t/pairwise-coordination-subsidies-a-new-quadratic-funding-design/5553) with sybil resistant identity mechanisms i1-x.
3. Every quarter,
   1. Gitcoin’s governance structure creates consensus about how to evolve each of these rules & mechanism, & the evolves.
   2. The ecosystems taste in projects evolves
   3. Adversaries that want to capture the matching funds evolve.

These simple rules have evolved Gitcoin Grants from:

### Round 1 in Q1 2019 - 200(ish) Contributions - $38k raised

![Screen Shot 2022-08-06 at 12.23.55 AM|690x434, 50%](upload://5ajyvpwzrQ0e8S4vOVlI2pRe0j9.png)

(economic contribution graph - round 1 - each contribution is an edge + each grant/user is a node)

### Round 14 in June 2022 - 100k+ contributions + $5mm raised

![Screen Shot 2022-08-06 at 12.23.14 AM|690x356, 50%](upload://ufMRrIijHPBKdVIaHERubbsxPE1.png)

(economic contribution graph - round 14 - each contribution is an edge + each grant/user is a node)

### The emergent, iterative, evolutionary, zero sum game between the red team & blue team

The primary stated goal of Gitcoin Grants has been fund public goods. But if you look at it from a certain angle, because Gitcoin Grants requires sybil resistance, every Gitcoin Grants round is actually a giant red team / blue team exercise for battle testing Digitally Native Sybil Resistance technologies.

I believe that accepting the iterative, evolutionary, and zero sum nature of this aspect of the grants rounds is key to designing a manageable way of addressing the problem.

Gitcoin’s sybil resistance will evolve as the attackers evolve. It is important to embrace this as an evolutionary game and recognize that the ecosystem is fluid, adversaries will come and go (and possibly get more advanced).

# What will round 69 look like?

IMO the north star is to build a system that:

1. Is anti-fragile to many types of attackoooors.
2. Is privacy preserving & respecting of the users sovereignty
3. Avoids plutocracy/dystopic outcomes
4. Avoids collusion
5. Is systemically anti-fragile because its cheaper to defend than it is to attack.
6. Has network effects
7. Enables Innovation
8. Prevents Capture
9. Embraces the evolutionary nature of this problem

# In closing

In this post, I made these assertions:
1. Sybil resistance is an important problem to address.
1. Sybil resistance is an adversarial game.
1. Sybil resistance is an iterative game.
1. Sybil resistance is an evolutionary game.
1. Sybil resistance is an infinite evolutionary iterative game between a diversity of adversaries.
1. What are the criteria for addressing sybil resistance?


Thanks for reading to the end.

If you want to follow my continued research efforts on these subjects checkout season 2 of the Greenpill podcast which is [all about the subject of digital identity & sybil resistance](https://gov.gitcoin.co/t/greenpill-podcast-season-2-digital-identity-sybil-resistance/11201).

I hope this knowledge transfer post was a valuable data point for you, DAO citizens.

Thank you to @DisruptionJoe @kevin.olsen, Takuya Kitagawa, Razvan, Carl Cervone, @GTChase, @brent @erich + countless others for proofreading earlier drafts of this post. I welcome feedback/comments below.

-------------------------

owocki | 2022-08-06 06:11:10 UTC | #2

[quote="owocki, post:1, topic:11235"]
How can the base of the protocol harden, but also evolve to continuously ongoing threats? Where are yearly, quarterly, weekly, daily, or instant feedback incorporated? Where is more governance oversight needed over socialware, and where can the system move to trustware? And on what time preference? As the attackers evolve, how can the fraud defense evolve (0) effectively (1) without tipping off the attackers (2) but still in a legitimate (eg transparent to governance) way?
[/quote]

Some further thoughts on this:

The DAO could consider a multi layered modular approach to these problems, comprising of multiple reinforcing feedback loops on multiple different time preferences.

![|299x298](upload://iZ9kD3lIN96E3uYE501JpmiUOZb.png)

The loops on shorter time periods rely more on trustware and immediate actions. And the loops on the longer time period rely on DAO governance & take more time.

Some mechanisms that could be in these feedback loops are:

0. New & Better Stamps (Continuous)
1. Upala (Instant)
2. Sybil Data marketplace (Instant)
3. DAO Blue Team Action Squad (Daily)
4. DAO Policy Issuance (Quarterly)
5. A sybil DAO of DAOs that shares information across BrightID/POH (Quarterly)

A sketch of these mechanisms:

### 0. New&Better Stamps

Feedback speed: Continuous

There is a mountain of data on and off-chain that could help increase the personhood score of users in the system.

* My gut says that there is a lot of opportunity with integrating POAPs if the DAO can determine which POAPs are most important
* Carl + Lawrence have done a great job taking a look at multiple data sources in passport and using that to produce sybil-ness, presenting that at Gathering Hour on July 28th 2022.

There should be a continuous feedback loop between the data analysis team + the stamps roadmap, with the ability to add new stamps rolling out often. It should be easy for the user to know what stamps are the highest priority for them to integrate (perhaps the user could sort the stamp UI by total added personhood score).

Right now the GPC is building in new stamp integrations themselves. There is an opportunity to just publish the stamp roadmap + accept PRs from third parties that would allow us to push this development work out to the community.

### 1. Upala

Feedback speed: instant

Upala is a protocol that provides human uniqueness score in dollars. The score of an account represents how much it would cost to forge the account.

Sound familiar? :)

Upala has a quite elegant mechanism where it allows anyone to “liquidate” an account for a reward equal to their personhood score.

Why is this powerful? It allows us to create a rational crypto economic incentive for attackers to claim a honeypot reward. If no one is claiming the reward, we could reasonably assume that no such attacker has been able to manufacture an identity equal to their personhood score

Project website: https://medium.com/six-degrees-of-separation

### 2. Sybil Data Analysis marketplace

Feedback speed: instant

[This is a topic that has been discussed on the forum.](https://gov.gitcoin.co/t/what-can-we-learn-from-brightids-aura-sybil-defense-software/11159) What if GitcoinDAO made the data for it’s sybil attackers available publicly (within reason, in a privacy preserving manner), such that anyone could evaluate where they think attackers come from, and then get rewarded for reporting those attackors to the DAO?

Such a system would provide instant feedback to the Passport ecosystem about how attackers are abusing the system.

This is a model that has been pioneered in other domains by [Numerai](https://numer.ai/).

### 3. DAO Blue Team Action Squad

Feedback speed: Daily

Perhaps the GitcoinDAO FDD or Data science group could continuously monitor the data in Passport during Grants rounds, and propose daily squelches to some sort of governance mechanism. (Perhaps the DAO has a rotating steward slot that is the Sybil Resistance Steward who sits in this role for a quarter at a time, and they are responsible for approving these recommendations). Governance could then verify that those recommendations are legitimate.

If the DAO is successful in decentralizing, the DAO Blue Team Action Squad will not be needed any longer. Over time the DAO Blue Team Action Squad will become part of the sybil data marketplace.

### 4. DAO Policy Issuance

Feedback speed: Quarterly

Perhaps the GitcoinDAO FDD or Data science group be in charge of issuing an algorithmic score for how personhood scores are computed.

A policy could be as simple as follows

> PS = CF = Weight(twitter) + weight(POH) + weight(POAP1) + weight(POAP2) and so on.

Perhaps there could be more complicated logic where certain stamps compound one exponentially. Or perhaps a squelch list could be built in to a scoring policy that dApps could subscribe to (as opposed to computing in memory in the dApp), so that the DAO Blue Team Action Squad’s actions have teeth.

By doing this on a quarterly basis, the DAO can enter into a loop where it

1. Observes the attackers
2. Learns their patterns
3. Recommends policy to governance
4. Governance approves
5. Updates the official GitcoinDAO algorithm

Over time, this system would create algorithmic policies that cover many different permutations of sybil attackers.

### 5. A sybil DAO of DAOs that shares information across BrightID/POH (Quarterly)

Feedback speed: Quarterly

As Gitcoin Passport aggregates more and more data from DeSoc, it will naturally become a information marketplace for the latest trends in sybil resistence.

If Gitcoin wants to be a good neighbor to the systems it integrate switch, it could find a way to report sybil attackors back to BrightID, POH, and any other ecosystem that is integrated with it. Such a data interchange would make the whole ecosystem stronger.

-------------------------

owocki | 2022-08-06 14:02:37 UTC | #3

Some Sybil Resistence Memes, just for fun + to perpetuate this vision :) ..

![6p3q9h|360x232](upload://21DJM9WjGqHEGtT4TVV7JnPalQC.gif)

![6p3u7i|260x241](upload://yRI0nKHP1TXfbJiAF2cUZPWVcWy.gif)

![6p3oyc|675x499, 50%](upload://xeG8zJY5kpSBOpHr231fl5iRMCZ.jpeg) 

![Kirby_passport|400x270](upload://mq41VThVMs9i99fHVlWrDdJCUCH.gif)

![6p3uj5|690x387](upload://1v2GAEUtIJRvc16OyKRCwWMsLNg.jpeg)

![FZWO5fgWAAQUCxG|497x500](upload://4fjuXm0lAbFu8Afxl0neWHF4Ep8.png)

[![Screen Shot 2022-08-06 at 7.49.41 AM|690x390, 75%](upload://cp02Fa5KWpvhPzOARpOP2E6JfAo.jpeg)](https://bits.owocki.com/Wnu7jJeB)

![a6c8e06407f2a0eb830ce6e1ebdcc00a00e561ed|690x388, 75%](upload://vX6MGZ85BSOqikZo92dcvqcacSH.jpeg)


[![Screen Shot 2022-08-06 at 7.45.38 AM|690x387, 50%](upload://athauIfCkz1qrbfLWDuURZ094ii.jpeg)](https://twitter.com/owocki/status/1555896232924442624)

[![Screen Shot 2022-08-06 at 7.46.19 AM|690x486, 50%](upload://jcB6BIIeh9YPggPZIMhlfWrzB9i.jpeg)](https://twitter.com/owocki/status/1555895270373675009)

Not a meme, but here is me announcing season 2 of greenpill pod on DIDs/Sybil Resistence.

[![Screen Shot 2022-08-06 at 7.47.16 AM|690x399](upload://jGqiGSzzNT3Shoe16osPWp6jDjW.jpeg)](https://www.youtube.com/watch?v=GgIzmXJ0Y7U&t=1s)

And here is me announcing Gitcoin Passport on stage at ETHcc.

[![Screen Shot 2022-08-06 at 7.48.17 AM|690x394](upload://jUzyLNTvnhBexJsRHKdazvz1jgF.jpeg)](https://www.youtube.com/watch?v=n6cahMvivjU)

Slides from this talk available [here](https://docs.google.com/presentation/u/1/d/1NY17vw1fOFgp9WR40c0hsDkTnafSGkEPT2Pmemr4Rdo/edit#slide=id.p).

-------------------------

ZER8 | 2022-08-07 18:54:46 UTC | #5


Just wanted to jump in and thank you for taking the time to write this huge and hugely important post Kevin. :robot:
The resources posted here will help everyone interested in the sybil learn more about what a sybil is and at the same time it will give the sybil defenders amazing context, insights and vision


PS. All the memes are good, but the Cat meme with Shaquille is :sweat_smile: :rofl: :joy:  :fire:

-------------------------

DisruptionJoe | 2022-08-08 09:45:43 UTC | #6

[quote="owocki, post:1, topic:11235"]
![](upload://jt5U4oK9KryGO6rExe8JQY9EkCm)

I think that Gitcoin’s final form could be that of a [Hyperstructure ](https://twitter.com/owocki/status/1543651089462939648). Hyperstructures are crypto protocols that can run for free and forever, without maintenance, interruption or intermediaries…

On tradeoff I think is interesting to manage here is the time preference of the systems ability to manage attacks.

How can the base of the protocol harden, but also evolve to continuously ongoing threats? Where are yearly, quarterly, weekly, daily, or instant feedback incorporated? Where is more governance oversight needed over socialware, and where can the system move to trustware? And on what time preference? As the attackers evolve, how can the fraud defense evolve (0) effectively (1) without tipping off the attackers (2) but still in a legitimate (eg transparent to governance) way?
[/quote]

I like to think of this using @pet3rpan model of [microservice DAOs.](https://twitter.com/pet3rpan_/status/1505977368099233793) 

Take something like contributing data to the hyperstructure or staking on models for sybil detection. Either one of these are low value without the other pieces of the structure which aggregates the component value into something worthwhile. This is similar to how your post on facebook isn't that valuable, but millions of peoples posts organized in a particular way are valueable, and you are a part of it. 

How might the smaller systems be rewarded for their contribution to the whole? 

I think this is where the microservice idea comes into play. A continually evolving sybil detection algorithm would require multiple inputs. Each of these inputs can be incentivized by an issuance curve rewarding the useful contributions in very narrow scope. The value created by the system as a whole can then be adjusted to balance the system inputs using a Shapley Value. 

Let me put that in a more concrete example. 

If you contribute data to the sybil defense DAO, you get SDDdata rewards. 

If you contribute code to the sybil defense DAO, you get SDDcode rewards. 

If you contribute models to the sybil defense DAO, you get SDDmodel rewards. 

If you give your opinion on flagged sybils as an evaluator, you get SDDeval rewards. 

Each of these has an issuance curve of its own. In the first few months or years, people might be earning millions of SDDrewards for their contributions, but few $$$ (only what GitcoinDAO and others are willing to pay to subsidize the risk they are taking)

These are the "microservice DAOs" that provide the inputs to the bigger "Sybil Detection DAO"

Now Sybil Detection DAO is only one of the inputs to the FDD system, and FDD is only one workstream in GitcoinDAO. 

If we want to build a hyperstructure, we must first build all the microservice components and then allow the hyperstructure's sustainable value flow emerge. 

Consider this a strong opinion held loosely, but throwing this out there to stimulate the conversation. 

Another cool side effect of this is it builds modular Hyperstructure Legos. Imagine the microservice DAO that finds models that are excellent at detecting sybil accounts is forked to be used to fight a pandemic or to organize debt unions in a way that proves the collective can win. 

Building microservice DAOs is something we can become very good at. It can be in our playbook. Figuring out how to build "can't do wrong" cheaper to defend than attack services that are great at one thing is a huge value to the world. I also don't see how we think we can build the hyperstructure that will provide sustainable fair capital allocation if we can't build a microservice DAO that sustainably incentivizes one action to be done well. 

I love the impact of Gitcoin always being exponential. Let's build some microservices, with massive upside potential as the digital public infrastructure of the future.

-------------------------

epowell101 | 2022-08-08 13:24:46 UTC | #7

Very much the sort of work - but better thought through - I was wondering about in my forum response to the FDD budget request.  

One caveat is the motion of making space for external contributors - accepting external PRs - takes a bit of intentionality of course.  Who does devrel etc and how much patience do we have to find and grow external contributors… requires devrel focus.

Now if we only knew a place w bounties and hackathons to jump start contributor activity! 😜. Ie we are well suited to be great at devrel++

Feels like the code level collaboration is important for the higher level data / service / protocol ecosystem alignment? 

A) do you agree that the OSS collaboration is important and non trivial to nurture and B) do we have devrel folks that can help lead within or across work streams?  (Understanding they’d need to be aligned as a part of a budget request etc…)

Excellent thoughtful post as always and thanks for @DisruptionJoe for tweeting about it

-------------------------

owocki | 2022-08-08 14:07:09 UTC | #8

[quote="DisruptionJoe, post:6, topic:11235"]
I love the impact of Gitcoin always being exponential. Let’s build some microservices, with massive upside potential as the digital public infrastructure of the future.
[/quote]

Hyperstructures are crypto protocols that can run for free and forever, without maintenance, interruption or **intermediaries**..

One attribute here that i think may have flown under the radar in this discussion is this attribute of **without maintenance, interruption or intermediaries**. 

In this light, I'd encourage the dAO to think about how to seperate [socialware vs trustware](https://orca.mirror.xyz/T70CmuhX95ubkw_JHOxSEy8d_EFeYXgtJnF13mPtaZE).  In the past gitcoin has been bad about relying on socialware (intermediaries) too much.  

@DisruptionJoe I think micro-DAOs and microservices are good ideas.  They are similar to the pods idea I posted about [here](https://gov.gitcoin.co/t/8-ideas-for-dao-work-maximum-coordination/10483).  Would you agree they shouldn't all be socialware ?

Here is an updated view  of the hyperstructure graphic I made that visually deliniaties where the trustware is in blue and the socialware in purple.

![Screen Shot 2022-08-08 at 8.00.36 AM|690x348](upload://nUpZhkCC5aBKTvA7gNSFeaHMW9a.jpeg)

The trustware in the center **is** the hyperstructure.  The rest of the things the push the network effects forwards are just humans doing whats rational / in their incentive set.

In a well designed system this hyperstructure will grow according to network effects. 

![Screen Shot 2022-08-08 at 8.03.05 AM|690x412](upload://3HrIyqWV9LMRooOjcq12sYa7Exm.png)

I would do a separate post on the hyperstructure if people are interested.

Of course the final direction here is up to the DAO.  I am here only to transfer knowledge.

-------------------------

DisruptionJoe | 2022-08-08 15:23:13 UTC | #9

[quote="owocki, post:8, topic:11235"]
They are similar to the pods idea I posted about [here](https://gov.gitcoin.co/t/8-ideas-for-dao-work-maximum-coordination/10483). Would you agree they shouldn’t all be socialware ?
[/quote]

Yes, I agree. I think this may be the misunderstanding. I believe we CAN make those microservice pieces into trustware as well! (Or at least many of them.)

-------------------------

owocki | 2022-08-08 22:48:15 UTC | #10

No misunderstanding, was just clarifying that the two approaches are not mutually exclusive

I think the integrated order of preference for me is

1. Social ware
2. Social ware with separation of concerns and competitive marketplace via micro DAOs or pods
3. Trustware

From worst to best.

-------------------------

owocki | 2022-09-02 15:58:51 UTC | #11

Shared this visual of the adversarial infinite game with @kevinolsen today and am sharing it here too since he asked me to share.

![FbqVhOWUUAEKbpL|530x500](upload://7OcgeYZxCDEQPBl0hat5uVlmxBv.jpeg)

-------------------------

owocki | 2022-09-13 18:17:46 UTC | #12

just tweeted this talk for ppl who wanted a nice visual overview of the problem space: 

https://twitter.com/owocki/status/1569727500791709696

here is the deck i used for this talk: https://docs.google.com/presentation/d/1xyQU7dRntgDqUNFGCKVUQXdB0KRe_hgMTKX_7YToP8E/edit#slide=id.p

@kevin.olsen how did the dappcon talk go?  got a video of your preso?

-------------------------

DisruptionJoe | 2022-10-25 13:23:17 UTC | #13

Here is the presentation by @owocki and @kevin.olsen at DevCon Bogota 2022

https://youtu.be/TRoO5fD7TI4

As much as I enjoy the talk which frames the problem, I want to encourage people to check out the developer focused presentation on Passport which begins about 26 minutes into the video.

-------------------------

castall | 2022-10-28 02:13:09 UTC | #14

[quote="owocki, post:1, topic:11235"]
acknowledging that adversaries exist + fundamentally tilt the design of the system towards defensibility and anti-fragility
[/quote]

Yes, you can either design something to stop the adversary or design something to work in spite of the adversary.


BrightID (with [Aura](https://brightid.gitbook.io/aura/) as its best verification method to date) attempts to stop sybil attacks.  (Aura can also stop certain kinds of bribery and collusion.)  But I also designed [attention streams](https://docs.google.com/document/d/1TKA-K8YadRdgz-Qek01TUcCkRaI9CKCXGtJ31AbVWIU/) (a separate thing) to function despite sybils, collusion, and plutocrats. There's a team that built a back end (smart contracts) and is working on a frontend for attention streams for SongADAO "Song Dust", but we need more builders to prototype uses for attention streams.  It will be a lot easier to grok it with prototypes.

-------------------------

castall | 2022-10-28 02:35:20 UTC | #15

[quote="owocki, post:2, topic:11235"]
A sybil DAO of DAOs that shares information across BrightID/POH
[/quote]

I'd like [Aura](https://brightid.gitbook.io/aura) to add tools to input/incorporate DAO/ecosystem findings.  Its goal is to be the swiss army knife for sybil hunters.

-------------------------

DisruptionJoe | 2022-10-28 10:51:34 UTC | #16

The current implementation of aura uses graph analysis. Would it be possible to use other types of analysis in the future?

-------------------------

castall | 2022-10-28 23:13:36 UTC | #17

Yes.  This is a great question.  [I posted my response in the Aura thread](https://gov.gitcoin.co/t/what-can-we-learn-from-brightids-aura-sybil-defense-software/11159/16).

-------------------------
