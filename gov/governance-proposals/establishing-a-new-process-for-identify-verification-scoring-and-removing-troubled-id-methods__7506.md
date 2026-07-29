---
id: 7506
title: "Establishing a New Process for Identify Verification Scoring (and removing troubled ID methods)"
slug: establishing-a-new-process-for-identify-verification-scoring-and-removing-troubled-id-methods
category: governance-proposals
url: https://gov.gitcoin.co/t/establishing-a-new-process-for-identify-verification-scoring-and-removing-troubled-id-methods/7506
created_at: 2021-06-29T17:03:02.910Z
last_posted_at: 2022-08-17T08:53:10.469Z
posts_count: 18
views: 7561
like_count: 47
---

# Establishing a New Process for Identify Verification Scoring (and removing troubled ID methods)

<https://gov.gitcoin.co/t/establishing-a-new-process-for-identify-verification-scoring-and-removing-troubled-id-methods/7506>
Adamscochran | 2021-06-29 17:08:10 UTC | #1

Yesterday I noticed that some users on Twitter were raising complaints about the lack of attention that identity verification has had in Gitcoin governance. So I spent the evening trying to evaluate how we can improve on that. 

This is an initial proposal to get discuss how we can better address our process of onboarding and evaluating sybil resistance measures.

**Executive Summary of Proposed Changes:**

1. Creates an approach for how the community should propose, vet, score and authorize new ID methods.

2. Creates a standard scoring process for identifying the merits and risks of each identity verification method.

3. Creates a subgroup of elected stewards to manage and maintain that process and scoring methodology.

4. Creates a standard bounty test to demonstrate the validity of each protocol.

5. Cleans up current ID methods and removes non-beneficial methods including:
* Lowering all current +% scores
* Permanently removing Google and SMS verification
* Temporarily removing Idena subject to it passing an additional confidence test and working with the community to improve its score.


**Current Problem:**
For Gitcoin's governance, there is nothing more important than maintaining confidence in Sybil resistance in the Quadratic Funding grants.

This is a process that currently governance delegates have not been a part of and I think our current identity confirmation processes are too lax, overly reward protocols, and lack a standard objective approach.


**The Goal of Identity Linking:**

The goal of verifying an individuals identity in Quadratic Funding is obvious, but the goal of connecting multiple accounts to create an identity score may not be.

In connecting additional 'verification' methods we should be either:

1. Trusting the robustness of the verification method itself to provide a high confidence unique verification.

or

2. Gaining user behavior indicators that Gitcoin can use to gain ML confidence in identifying non-human actors.

**Stewards of the Community:**

At the same time, we should be responsible and respectful stewards of the open source and decentralized communities and not support methods that are:

1. Standardizing reckless or risky security behaviors.
2. Creating inequality of access or opportunity (by assuming cultural or economic behaviors are what make human interaction)
3. Creating exclusionary boundaries (by requiring verification from already known actors)
4. Productizing or unfairly/unknowingly tracking users.
5. Turning users into the product.
6. Preying on economically disadvantaged users for sake of growing their product through incentive schemes.

**A New Process:**

To this end, I'd propose a new set of processes for identity solutions to be added.

This process would be maintained by a sub-group of delegates to be voted in, and called 'The Sybil Stewards'

*A) For Decentralized Unique Identity Processes:*

1. A user, or developer can propose adding a new verification protocol on the governance forum. This would include a:
 * Description of the service
*  A step by step break down of the verification process
* How/if any costs or tokenomics are involved
* Why the user believes this is an adequate identity service.

2. The user would submit a scoring template [see scoring section below] with the scores they believe the service should have.

3. The community would debate and test the identity protocol within the thread. Within 14 days, based on the community feedback, the Sybil Stewards would present their proposed score card for the protocol.

4.  Once a protocol has been scored, it may then be sponsored. A sponsoring user (either the developer, a third-party user, or the Gitcoin DAO if it is interested) would sponsor the proposal by placing a $1000 bounty of $GTC into escrow. From there, the community will have 30 - 90 days (depending on if the protocol takes time to verify) to attempt to become verified on multiple accounts. The first user to show the Sybil Stewards they have successfully created multiple verified accounts on the protocol would win the bounty. If no user can do it by the time it is expired, then the bounty is returned to the sponsor.

5. The outcome of the bounty is then added to the scorecard. So long as the protocol meets the minimum score (0) it would then be voted on via a Governance Snapshot to be added to the next grant round.

6. The specific % of funding boost added would be determined by its score bracket.

*B) For Centralized Unique Identity services and Behavioral Services*

In the case of centralized services and user behavior based services (i.e. Twitter), Gitcoin (the company/developer of Gitcoin) can add these services by:

1. Putting forward a proposal with score on the governance form, along with a scoring template filled in and:
 * A Description of the service
* How/if any costs or tokenomics are involved
* Why the user believes this is an adequate identity service, or why they believe the behavioral data is beneficial to detecting bots, and non-invasive.

2. Allowing at least 14 days for users to investigate and raise concerns.

3. Creating a governance vote for the approval of the addition.

These services should still have their percentages determined by their scores on the scoring template.

*C) Removal*

At any time, any steward may put forward a proposal to adjust, prorate or entirely remove an identity method.

This should be done first with a governance thread to discuss the proposal and then a formal governance vote.

**Scoring Template**

In order to create a *more* objective model of determining the security, correctness and usefulness of different identity protocols, I've attempted to create a rough scoring template.

The expectation is that the community would vote on and improve this scoring template over time. 

Right now the sections are:

* **Requires Public or Semi-Public Posting of Identity Info (-5 to +5)**: If it puts user information under public scrutiny it becomes exclusionary for large populations. Ideal solutions should not require public information (+5), ones that do require public information should keep it gated or secure (0), and not display it in a public web or app especially to external actors (-5)

* **Is Unique (+10 to -5)**: Does the integration tie us to a 'unique person'. The method should not just aim to prove a unique account, or that there is a single human, but that said human is attached to a profile, each person has only one profile, and no two people have profiles on the same identity. 1-10 scored on the success of this. Negative numbers when there is uniqueness of *an* individual but not an identity. -5 when it is entirely non-unique.

* **High Confidence Unique (0 to +10)**: Based on the approach and methodology, how confident can we be that the person is unique, does not own more than one profile, no two profiles are the same person, the profile is active, current, not spoofed, not deceased and is currently owned by the user it claims to be owned by. Currently this is nearly impossible with all options we currently have and is likely only manageable by two-factor, KYC/AML verified, centralized services. However, some services like BrightID which have liveness, and identities built over time begin to get some increased confidence due to the constant effort of human interaction required to build out. The intention of this score is to account for the fact that centralized services trade-off other benefits for high confidence.

* **Requires PII (0 to -5)**: Does this require the user to share, especially with a third-party, personally identifiable information. That can range from their real name (-1) to sensitive document uploads to a 3rd party (-5)

* **Requires Invasiveness Software/Hardware/Public (0 to -5)**: We should not encourage verification methods that are invasive to the users privacy or security. This includes exposing their public information, but also the download or use of specific hardware or software that may be used in tracking. It can range from using a specific web app (0), to a browser extension (-3), to having to download desktop software (-5)

* **Can be spoofed (0 to -5)**: While a criteria that will not apply to most services, some protocols may be spoofed or altered such as IP addresses, MAC addresses and in some indirect manners phone numbers. (We would also include the risk of things like SIM swapping attacks under spoofing) in all such cases, a -5 should be awarded for any identifier that can be spoofed.

* **Easy to Use (+5 to -5)**: The ease of the use of the service (both to sign up, activate, verify if applicable, and connect it to Gitcoin). We should check our own bias here frequently and assume we are referring to the ease of use for a mainstream user who may find something like installing and using MetaMask to have complexity. A ubiquitous service like Google or Facebook with a OAuth login button is a good example of a 5.

* **Makes User the Product (+5 to -5)**: While it is fine for their to be for-profit services, we should take care in not creating incentives to drive users to places where they are the product. While this may be unavoidable at times, it should be a weighted tradeoff. Services that simply show ads to users based on profiles are likely a -1 to -3, whereas services that sell user data are a -5. Currently, no existing cases of positive numbers exist, but a wholly decentralized identity chain may in the future actually allow a user to deproduct themselves on other services which may merit positive scores.

* **Ephemeral/Changing Source (+2 to -2)**: If the source of the verification can be ephemeral or changing (i.e. a temporary phone number/email, or an account that can change hands) it should be -2. If it cannot be swapped out easily it should be a +2. This is a small balancing score to adjust for small risks where accounts *could* be out of service but have not been sold for the purpose of sybil attacks.

* **Has liveness (+5 to 0)**: Liveness scores cover two possible scenarios. The first is if during the verification process the person was live (in person) or live (over constant video). This being superior to something recorded. However, in lieu of being live at point of verification, a service could instead choose to be constantly validating through constant micro-verifications telling us that this person is the proposed identity currently. An example of this comparison is that BrightID requires constant behavioral interactions to grow an evolving score, where as Idena requires a verification every 20 days that has a binary output. This is one of the most complex criteria and may merit additional refinement in the future.

* **Is Non-Subjective (+8 to 0)**: This criteria asks if the verification of the user requires the subjective interpretation of other people, or if it is a binary criteria outcome not subjective to human interpretation. (For clarity, verifying someone's identity documents its an objective test even though a human is performing it). A non-subjective service results in greater fair access and would earn a positive score.

* **Is Decentralized (+5 to 0)**: This criteria asks if the service is decentralized. This does not simply mean that there is a blockchain involved. To get a perfect +5 score a protocol should be decentralized (as in on a blockchain) and decentralized in the fashion that it does not depend on a single app, centralized service, company, software or website for its access. Currently, only ENS meets the +5 score on this list.

* **Cost the User (0 to -10)**: If there is a price to the user (through tokens, fiat or even through tasks that are not directly related to the process of them verifying themselves) the score should be lowered. Any cost of verifying identity creates a bias towards users not only who are economically well off, but, even just have simple access to the payment rails supported by that protocol.

* **Grants Behavioral Insights (+10 to 0):** While we don't want to encourage tracking or privacy violations, there are times when accessing reasonable, public, non-PII information via systems like a social graph, social network firehose, or TheGraph node would allow us to determine a users behavioral profile. An example is connecting a Google account only proves a user created a Google account, so this holds no value. But, connecting a Twitter account allows us to see a users tweet activity, and social connections. This public information does not violate user privacy or create more held PII risk, but, can be an additional signal of humanity. Just like this category we should never deduct value from a user due to a lack of social insights, nor have it be a necessary nor sufficient condition for validating an identity. It should always merely be icing on the cake.

* **Involves 3rd Party Tracking (-8 to 0):** We should aim to discourage and discount methods that involve tracking by third-parties. Either centralized social networks, or situations where users are required to interact via specific apps or softwares that could be monetized or productized.

* **Poor Security Practices (-5 to 0):** We should discourage the use of applications that have poor security practices. A Gitcoin stewards we have a responsibility to promote responsible web3 behaviors, especially to newer users. An example of something that would merit a penalty is Idena's web login system. An account is generated for the user, and they are asked to enter their private key and password in a web browser to log in. The private key is not only entered into a web browser, but is fully viewable in plain text.

* **Works Globally(+10 to -5):** We should aim to give additional weight to services that work globally. Ideally not relying on specific IDs or type of IDs, and not relying on access to specific technology, lifestyles or activities (i.e. having a unique IP address/MAC address/Phone Number is seen as common in many parts of the world, but in economically disadvantaged regions, sharing of a smart phone between multiple people is a common practice)

* **Has Equity of Access (+10 to -10)**: We should also focus on services that create equitable opportunity for a user to enter into the space and be fairly verified. Services that require specific economics, time commitments, time of day commitments, costs or travel can make it challenging for different demographics to get involved. At the same time, systems that require users to already know other users and get verified in concentric circles are exclusionary to isolated new entrants to the market (which is actually something we want to encourage in web3).

* **Use of Profit Incentives (-5)**: Profit incentives create the inverse problem, wherein the prey on the economically disadvantaged to seed their product and create a risk of economic attack. While decentralized systems may need some sort of token, reputation or incentive model to encourage the participation of good actors, this should never come in the form of promoting or advertising the ability to earn money from the protocol. Systems promising income for being verified, or for participating in verification, or successfully verifying or challenging other users create incentives that work against the trust of the system.

* **Could Buy Accounts (-8 to 0)**: A measure of both, is it possible, is it easy and is it likely that accounts could be bought and sold. In a case where it may be possible to sell accounts, but there may be economic or technological disincentives that make it challenging to do (such as slashing, or the account only being transferable by a non-changeable private key)

* **Can Have Collusion (-5 to 0)**: A measure of how easy and likely it is that users within the protocol (or one user with many accounts) could collude to verify additional non-real users, or to make the protocol less secure over time.

* **Can Be Botted (-8 to 0)**: A measure of the possibility of using bots to create or verify new accounts. Things like CAPTCHAs, web sessions, randomness or synchronicity, should not be considered disqualifications in the ability for a user to create and use bots.

* **Needs Reverification (-5 to 0)**: Does the identity need to be reverified again in the future? This may seem only the opposite of a liveness test, but protocols can maintain liveness without needing explicit reverification by doing continual improvement/interactions rather than binary outcomes over time. Reverification creates an undue burden on the user, requires an additional checking burden on Gitcoin, and means that trust of it being the same user likely decays between two verifications until the next is completed.

* **Easy to Maintain (0 to +5)**: This is a measure of the ability to maintain the identity, either by keeping an account active or renewed, or by completing reverification. i.e. a manually ENS renewal with a price is less easy to maintain than having been verified once on another service.

* **Subjective Challenging (-5 to +5)**: Does the system allow others to challenge the identity of another user. If not then 0. If it does, it should be a -5 if that is subjective and a +5 if it is a wholly objective method.

* **Challenge Passed (+25, 0, -10)**: If the protocol claims to verify unique identities and has done a challenge it is +15 points if no user was able to get multiple accounts verified, and up to -10 points if they were. Protocols that do not claim unique identity verification or who have not yet done such a challenge should be assigned a 0.

**Scoring Levels**:

< 0 - Should be removed or denied currently.
0 - 10 - May be approved by governance, but should have no higher a score than +5%
10 - 20 - May be approved by governance, but should have no higher a score than +10%
20 - 30 - May be approved by governance, but should have no higher a score than +15%
30 - 50 - May be approved by governance, but should have no higher a score than +25%
50 - 80 - May be approved by governance, but should have no higher a score than +40%
80+ - May be approved by governance, but should have no higher a score than +60%

**Wider Bands**:

In turn, a users score should start at 50% power and may progress to a maximum of +250%

This model with lower rewards per method, a lower starting vote power and a higher voting cap, allows Gitcoin to introduce more verification methods over time and more heavily weight governance towards users who complete multiple methods.

The lower curve on the scoring level means that even if a user cannot complete preferred methods, they can likely complete many less preferred methods and still take part within Gitcoin grants.

**Current Scores**:

I've created a public Google sheet with rough scores of each of the current verification methods scored using the model proposed above: https://docs.google.com/spreadsheets/d/16g5iZewRmWuI_pPV1CEY7t6YLZrJxsHp6OAfaDZagz4/edit?usp=sharing

The scores for the current methods are as follows: 

![](upload://e52QBITjlslikDh01zbP3VyUIdB.png)

Under this proposal we would be:

* Setting BrightID to +25% verification
* Setting POAP to +10% verification
* Setting ENS to +8% verification
* Setting Twitter to +8% verification
* Setting Proof of Humanity to +5% verification
* Setting Facebook to +5% verification
* Removing Google from verification
* Removing SMS from verification
* Removing Idena from verification. [Temporary]

**Understanding the Idena Score**

In this model, Idena scored incredibly low.

That's not because I believe Idena is a bad concept, or cannot *become* a useful identity service. But, right now their set up lacks the robustness to have fair, equitable and high confidence uniqueness and doesn't encourage the right user behaviors.

Idena requires users to perform validation ceremonies every 20 days. It is done at one set time, and lasts only for 2 minutes. It is at this same hour of the day each 20 days.

Users create 'flips' which are two option questions with a series of pictures. Users must then successfully complete a challenge where in they successfully answer a series of 'flips' correctly at the validation ceremony.

With 6 binary outcome options (0 v 1), a user is required to get >75% of them right to succeed. This means a user has a roughly 9.38% chance of getting it correct when clicking at random.

It also requires users to invite other users and to contribute to flips (creating content for them) in order to reach a verified status, and to maintain that in successive challenges.

To join a validation session users must either download and run a desktop software, or pay to connect to a remote node in a web browser session.

That web browser session involves entering, in plain text, into the web browser, a private key.

Connecting to a remote node costs only $0.08 per session.

This model of accessibility creates a low threshold for an economic attack. At $80 spent, you could attempt 1000 verification bots clicking at random across 1000 sessions. In turn, you'd likely end up with 93 accounts.

Those 93 accounts could contribute known flips to the pool, colluding to make the network verification less susceptible to them specifically in the future.

**Working with Idena**:

While I think Idena should be removed from verification currently, I will reiterate, its not because its a bad concept. It's current state simply presents a lot of risk.

I'd suggest that Gitcoin allocate a sponsorship of $1000 of $GTC for people to test Idena in an attempt to get duplicate accounts over the next 90 days.

If no one is able to claim that, then that would give the Idena the +25 score it needs to reach 0 and remain eligible at a highly reduced percent. They can from there continue to improve and iterate.

(Idena team: I'm sure myself and others would be happy to work with you to help you find some improvements that can be made to improve that score and make it more beneficial for both parties)

**Delegation**:

If you are interested in supporting this work but don't have time to be involved in the process, you can feel free to delegate voting power to me by pasting '0xf07A2439296e07Bc4320AF924E655a01fb69D89C' under the delegation section of your Gitcoin dashboard: gitcoin.co/quadraticlands/dashboard

-------------------------

owocki | 2021-06-29 17:45:32 UTC | #2

Hi from Gitcoin Core team.

Adam thanks for putting together this proposal.  I think it adds some rigor/decentralization to what has until the DAO launch been a very informal/centralized process.

A few quick comments on "whats going on now with TrustBonus", while I'm running between meetings.

0. The Socratic Oath is "first do no harm".  I think that any consideration of the anti sybil data collected here should start with "how do we respect a users privacy".  Stated more forcefully: "Lets make sure we dont DOX our users".  I would be interested in seeing more proposals from the DAO about how to responsibly steward this data (especially and at least until we've decentralized and there is no more centralized data store).
1. Before GitcoinDAO launched, I was heavily involved i doing research on Sybil Resistence and building out the existing Trustbonus tab on the profile (login and go to your profile and click trustbonus).  Check it out to see what exists already.  Youll note that in GR10, we moved from TrustBonus being optional (all users got 100% of match, and bonus was just a bonus) to being more actively promoted as the happy path (users start with 50% match, and by verifying anti sybil they could work up to 150% match).  This was a response to the [volume of sybil attacks in GR9](https://gitcoin.co/blog/gitcoin-grants-round-9-governance-brief/). 
2. Here is the paper that inspired the TrustBonus approach: https://arxiv.org/abs/2008.05300  .  Shout out [Divya Siddarth](https://arxiv.org/search/cs?searchtype=author&query=Siddarth%2C+D), [Sergey Ivliev](https://arxiv.org/search/cs?searchtype=author&query=Ivliev%2C+S), [Santiago Siri](https://arxiv.org/search/cs?searchtype=author&query=Siri%2C+S), [Paula Berman](https://arxiv.org/search/cs?searchtype=author&query=Berman%2C+P) for lighting our path here!
3.  We have been building a tool that would export a privacy aware Personhood Score , backed by this data to the rest of the web, enabling other dapps to easily draft off of Gitcoin's sybil resistence.  Here is a WIP version of that tool: https://proofofpersonhood.com/  .  I am looking for guidance from governance about how/if/when to roll out this tool -- perhaps from the process that Adam proposes above?.  Left to my own devices + before the DAO launched, I'd probably aim to release it for GR11 as an opt in tool (and if governance likes the tool they can decide to turn it on for more people).
4. We are building a tool called "Quadratic Diplomacy", which allows users to stake their GTC on one another -- creating a [web of trust](https://en.wikipedia.org/wiki/Web_of_trust).   I am looking for guidance from governance about how/if/when to roll out this tool.  Left to my own devices + before the DAO launched, I'd probably aim to release it for GR11 with a very very small TrustBonus associated with it (and if Governance likes the tool we can give it a real impact on TrustBonus.). 

I feel like the rollout of the above projects (Quad Diplomacy, and PoPP Passport) should probably have some oversight of Governance, and so I am looking forward to working with the DAO stewards on this in advance of GR11 (September) to do so.  Perhaps we can setup a call where I can give a demo as a starting off point?

-------------------------

owocki | 2021-06-29 19:23:02 UTC | #3

One other note about TrustBonus:  

Right now it's framed as a % multiplier on all donations, which after learning more about the problem I think might not be the best long term solution....   

Why? After studying [Vitaliks On Collusion article ](https://vitalik.ca/general/2019/04/03/collusion.html), we've considered changing the core architecture of this to be a PersonhoodScore which equates to the price of forgery of each identity in the system.

So in this framing, instead of an identity service N giving a TrustBonus % TB, each identity service would give a PS where 1 unit of Personhood Score is equal to $1 Price of Forgery for a new identity mechanism.

What does this accomplish?  Well in [Vitaliks On Collusion article ](https://vitalik.ca/general/2019/04/03/collusion.html), we learned that cheaters come in all shapes and forms, from common petty criminal up to Justin Sun to nation-state actors behaving badly.  By recognizing this core fact, we are at least able to frame this problem in crypto-economic terms -- and make a system cheaper to defend than it is to attack..  

In practice this means if a user is not sybil verified or not, their identity has a PersonhoodScore/Price of Forgery of $X -- where up to $X in benefit you can assume the identity is valid, and after $X you cannot be sure.  

The basic idea here behind PersonhoodScore is that each identity mechanism adds $X to the price of forgery of an identity, and the PersonhoodScore can add/multiply as a user integrates with more identity mechanisms.

EG if Rabbithole.gg were to integrate Gitcoin's sybil resistence one day, and a user with a Personhood Score of 10 comes to them, they can assume that they can safely give a reward worth $10 or under to that user.  

In Gitcoin Grants this is what it would look like in a [straw man Gitcoin Grants contribution dampening model](https://docs.google.com/spreadsheets/d/1e2j2qzQcZlz4Col5qqF3yxKr-NQ5SxVrFuGX7k-xyek/edit#gid=0) which maps a users match amount to their personhood score, ending in a percentage of matching amount that can be safely applied:

![Screen Shot 2021-06-29 at 1.21.32 PM|690x275](upload://hiJwwWEq4HcHfcjGYOorq8bITum.png)

In this model, 
- a user with a **1000** personhood score who contributes contributions that would generate **$100** in matching would get **100%** of their contribution matched.
- a user with a **100** personhood score who contributes contributions that would generate **$100** in matching would get **100%** of their contribution matched.
- a user with a **10** personhood score who contributes contributions that would generate **$100** in matching would get **13%** of their contribution matched.
- and so on..

While were on the topic of how to govern TrustBonus, I figured this reframe might be useful feedback for the proposer.  Open to community feedback as always tho!

-------------------------

Luvlynj | 2021-06-29 20:19:53 UTC | #4

This here is deep, trying to understand it better.....I hope it doesn't alter the already verified trust bonus.

-------------------------

Luvlynj | 2021-06-29 20:31:37 UTC | #5

I think also that another way to add trust bonus verification should come from a person's activities in here, if the activity reads low its definitely would mean fake accounts, maybe put up level of activeness, Low activity, High activity, very high activity. 

I think this should help in some way.

-------------------------

Spugpow | 2021-06-29 21:22:21 UTC | #6

I love this idea, personally:

[quote="Adamscochran, post:1, topic:7506"]
Once a protocol has been scored, it may then be sponsored. A sponsoring user (either the developer, a third-party user, or the Gitcoin DAO if it is interested) would sponsor the proposal by placing a $1000 bounty of $GTC into escrow. From there, the community will have 30 - 90 days (depending on if the protocol takes time to verify) to attempt to become verified on multiple accounts. The first user to show the Sybil Stewards they have successfully created multiple verified accounts on the protocol would win the bounty. If no user can do it by the time it is expired, then the bounty is returned to the sponsor.
[/quote]

As for the rest, I think it's too complex/illegible. I find several of the criteria in the rubric hard to understand or differentiate from other criteria on the rubric, and the scoring system is opaque. This is exemplified by the pair "Is Unique (+10 to -5)" and  "High Confidence Unique (0 to +10)"

If a common rubric is necessary, this would be my suggestion for the process of determining it: 

1. Create a thread where people can suggest evaluation criteria
2. Hold a quadratic vote over all the unique suggestions
3. Select the top 5 scoring criteria and give them equal weight in determining the "score" of a proposed ID solution. 

As for whether a special category of steward is needed just to evaluate IDs, I'm skeptical, but defer to others with more technical knowledge.

-------------------------

Sirlupinwatson | 2021-06-29 21:26:06 UTC | #7

Well basically this post is about remodeling the hole 'User Score' and I'm more than happy with this proposal, there is some part that leave me perplex but overall it's great. 

I think it deserve a deep understanding and even this could be a new topic pinned on top with more than one sub category.

I'll bookmark it!

-------------------------

Adamscochran | 2021-06-29 21:46:41 UTC | #8

>As for the rest, I think it’s too complex/illegible. I find several of the criteria in the rubric hard to understand or differentiate from other criteria on the rubric, and the scoring system is opaque. This is exemplified by the pair “Is Unique (+10 to -5)” and “High Confidence Unique (0 to +10)”

That's specifically outlined in the notes.

One option is the verification model tying the identity to uniqueness or not. The other is a matter of a confidence degree across all the sub criteria of uniqueness.

> If a common rubric is necessary, this would be my suggestion for the process of determining it:
>
>1. Create a thread where people can suggest evaluation criteria
>2. Hold a quadratic vote over all the unique suggestions
>3. Select the top 5 scoring criteria and give them equal weight in determining the “score” of a proposed ID solution.

But, criteria do have different value, so giving an equal weighted score to 5 criteria picked by a community does account for the difference in quality/value of any of those criteria. 

>As for whether a special category of steward is needed just to evaluate IDs, I’m skeptical, but defer to others with more technical knowledge.

By suggesting it is too complicated of a model, then that would actually increase the need for specialized stewards who have spent time deeply understanding that model and can help the community in its evaluations.

Does this model, after one day of work, likely need some refining and clarity? Sure.

But, just because its complicated, doesn't mean you just throw it out and go with something overly simplified.

-------------------------

Sirlupinwatson | 2021-06-29 21:59:31 UTC | #9

Your opinion and proposal deserve some attention, clearly. Thank you very much for your time and effort you did put into this by the way.

-------------------------

Spugpow | 2021-06-29 23:02:58 UTC | #10

For any decision procedure, I think there's a difficult tradeoff between technical optimality and ease-of-use. More optimality in a process allows for input that meets technical criteria, but imposes a tax on 1. speed of the process 2. how many people the process can draw information from 3. the transparency/legitimacy of the process. That said, I wouldn't be surprised at all if my suggestion errs too much in the other direction. 

As a counterproposal, I'd personally sort the criteria in your proposal into the following buckets:

EASE-OF-USE:
**Easy to Maintain**
**Easy to Use**

PRIVACY:
**Requires Public or Semi-Public Posting of Identity Info**
**Requires Personally identifiable info**
**Requires Invasiveness Software/Hardware/Public**
**Involves 3rd Party Tracking**

EQUITY:
**Makes User the Product**
**Cost the User**
**Works Globally**
**Has Equity of Access**
**Use of Profit Incentives**
**Is Non-Subjective**
**Subjective Challenging**

TECHNICAL: 
**Challenge Passed**
**Could Buy Accounts**
**Is Unique**
**High Confidence Unique**
**Can be spoofed**
**Ephemeral/Changing Source**
**Has liveness**
**Could Buy Accounts**
**Can Have Collusion**
**Can Be Botted**
**Needs Reverification**

MISC.:
**Is Decentralized**
**Grants Behavioral Insights**
**Poor Security Practices**

In my uneducated opinion, most of the technical criteria can be evaluated using your competition suggestion, maybe iterated:

[quote="Adamscochran, post:1, topic:7506"]
Once a protocol has been scored, it may then be sponsored. A sponsoring user (either the developer, a third-party user, or the Gitcoin DAO if it is interested) would sponsor the proposal by placing a $1000 bounty of $GTC into escrow. From there, the community will have 30 - 90 days (depending on if the protocol takes time to verify) to attempt to become verified on multiple accounts. The first user to show the Sybil Stewards they have successfully created multiple verified accounts on the protocol would win the bounty. If no user can do it by the time it is expired, then the bounty is returned to the sponsor.
[/quote]

That would leave the following list of criteria in the rubric:

**Is Decentralized**
**Grants Behavioral Insights**
**Poor Security Practices**
**Equity**
**Privacy**
**Ease-of-use**
**Challenge Passed**

To determine their weights, I'd suggest a poll of some kind, ideally using QV, either of everyone or just stewards. 

Feel free to amend or reject this suggestion!

-------------------------

Adamscochran | 2021-06-29 23:14:01 UTC | #11

>For any decision procedure, I think there’s a difficult tradeoff between technical optimality and ease-of-use.

Why?

We aren't talking about a decision process for end users.

We're talking about securing potentially millions of dollars in funding from collusion attacks.

It doesn't matter if it is easy. It doesn't matter if it takes time.

There is no urgency in adding additional verification methods if they could overly tip the scale in favor of collusion.

If it takes 1-2 grant rounds to add a new verification method, that is likely fine. It should simply be as robust as possible while still respecting user private.

>In my uneducated opinion, most of the technical criteria can be evaluated using your competition suggestion, maybe iterated.

The checks aren't binary that can simply fold under one another, they are a bit of a balanced construct to allow for cases wherein both centralized and decentralized services which provide user behavioral predictors *or* attempt to validate a unique identity could pass a threshold test and be scored on a confidence grade, so long as the trade off behaviors don't get too great to outweigh it.

>To determine their weights, I’d suggest a poll of some kind, ideally using QV, either of everyone or just stewards.

Once again, you can't determine the weights in a scoring model by popularity. Using QV to do that would over fit towards popular, easy to game or easy to understand criteria.

Just because everyone agrees a criteria is something that *must* be included, does not mean it is the criteria most valuable in determining the validity of a method.

If you took the reduced risk you created and assigned them scores and then tried to score the current validation methods you'd see its harder than that to create a balanced model which rewards the correct behaviors here.

-------------------------

Spugpow | 2021-06-29 23:49:21 UTC | #13

[quote="Adamscochran, post:11, topic:7506"]
Why?

We aren’t talking about a decision process for end users.

We’re talking about securing potentially millions of dollars in funding from collusion attacks.

It doesn’t matter if it is easy. It doesn’t matter if it takes time.
[/quote]

Sure, and that’s why I think your idea of stress-testing the collusion resistance of IDs is good.

[quote="Adamscochran, post:11, topic:7506"]
Once again, you can’t determine the weights in a scoring model by popularity. Using QV to do that would over fit towards popular, easy to game or easy to understand criteria.

Just because everyone agrees a criteria is something that *must* be included, does not mean it is the criteria most valuable in determining the validity of a method.
[/quote]

This may be true for the technical criteria, but most of the criteria are basically questions of people’s values: how much do you value equity, how much do you value security, how much do you value privacy, etc.

-------------------------

Adamscochran | 2021-06-30 02:31:14 UTC | #14

[quote="Spugpow, post:13, topic:7506"]
This may be true for the technical criteria, but most of the criteria are basically questions of people’s values: how much do you value equity, how much do you value security, how much do you value privacy, etc
[/quote]

The question isn't how much someone values these.

It is the measure of those elements available in the integration.

You can not value it, and it can still be there.

-------------------------

bitsikka | 2021-06-30 17:26:34 UTC | #15

[quote="Luvlynj, post:5, topic:7506, full:true"]
I think also that another way to add trust bonus verification should come from a person’s activities in here, if the activity reads low its definitely would mean fake accounts, maybe put up level of activeness, Low activity, High activity, very high activity.

I think this should help in some way.
[/quote]
100%
FWIW, at BrightID we have been having discussions about pulse-check/heartbeat/importing-trust.

* [Implement a periodic "pulse check" in order to maintain Verified status](https://github.com/BrightID/BrightID/issues/824)
* [Importing Trust](https://forum.brightid.org/t/importing-trust/55)

I hypothesize that non-financial activities or indirectly financial activities that people would do without being required/forced/directly-incentivized to do - e.g. push github PRs, Chat/like/re-share in various social platforms could be recorded anonymized in person's DIDs which Sybil scoring systems like BrightID could poll periodically as heart-beat and adjust scores.

Of-course, the social platform itself would have to be evaluated similarly by sybil scoring system just as the other way round outlined above.

All in all, I think there will need to be a symbiotic collaboration/communication (standard/protocol(s)) between consuming/providing systems for a robust,  uncompromising on values like privacy, yet flexible solution to the problem.

-------------------------

AwakeNing_Tong | 2021-07-01 04:25:25 UTC | #16

Your opinion and proposal deserve some attention.But I still think that the existing mechanism will be effective.

-------------------------

porobov_p | 2021-07-02 13:51:37 UTC | #17

Greetings humans!

Founder of Upala here. We invented the price of forgery concept and now building the system that utilizes it. Super glad to have the discussion started!

Wanna give a quick intro to the concept to those unfamiliar with it. 

The main idea is that the user score is valued in dollars and the user can grab these dollars at any time, after that the user's ID is deleted forever. The procedure is called "explosion" in Upala terms. 

Here's how a case may look like if we want to estimate the price of forgery for an SMS-based verification method.

- We put the $1000 in a pool (as an example - just continuing Adam's thought)
- We set the score of $1 to every person who passes SMS-verification.
- People got verified and we notice no explosions. Everyone decides it is better to keep a working identity than to get $1.
- We raise the score up to $5 to stress-test the verification method.
- Now we see that many accounts started to pass SMS verification just to "explode" and take the money from the pool. It means that the efforts required to forge SMS verification cost less than $5. And malicious actors can profit this way.
- Decreasing and increasing the score we iteratively come to a score with an acceptable rate of explosions. (it's ok to have a "natural" level of explosions - people make mistakes, misunderstand or get emotional). Above this level is where malicious actors have enough incentives to forge the verification method for profit.
- We now can rely on this discovered score as a very accurate quality measurement of the selected verification method. We repeat the same procedure for other verification methods (or even combinations of methods).

For a deeper dive check out this [article on EthResearch on price of forgery](https://ethresear.ch/t/price-of-forgery-digital-identity-measuring-human-uniqueness-score-in-dollars/8328).

With price of forgery approach, we don't have to think(!) and rely on any assumptions about any verification method. The market will drive the scoring of each method to its price of forgery. We also get an assurance for future exploits. If a method got hacked we would see it immediately through an increased explosion rate. That would mean the method should be fixed, or its score should be decreased. 

Love the methodology proposed by @Adamscochran - exhaustive and thought out! I think it can be used "as is" for the preliminary assessment of new verification methods. It can help decide on initial parameters for the price of forgery discovery process:

- acceptable explosions rate
- an amount of budget to put in the pool
- initial score or score conversion rate (for non-binary verification systems)
- etc.

 Some food for thought in this GitHub [issue on Gitcoin and Upala integration](https://github.com/gitcoinco/web/issues/7888). 

@owocki would be happy to help with utilizing the price of forgery concept. Probably we could simplify the Upala protocol specifically for Gitcoin. Curious about where you at. Always happy to discuss.

-------------------------

castall | 2021-07-04 14:52:16 UTC | #18

I support this qualitative approach to assigning trust bonus sizes to different credentials. Thank you for working on this @Adamscochran 

@owocki and team had reasons for choosing the bonuses they did, but this new approach makes the metrics that go into it more transparent, which in turn shows uniqueness protocols what they need to do to improve.

What's our next step to get this proposal enacted?

-------------------------

AndrewIdena | 2022-08-17 12:01:20 UTC | #20

Hey @Adamscochran 

I'm Andrew, the co-founder of Idena. I have recently discovered this discussion and would like to would like to refute the misinformation and wrong conclusions about Idena

> In this model, Idena scored incredibly low.

The low score is due to a lack of understanding of how the Idena protocol works.

> That’s not because I believe Idena is a bad concept, or cannot become a useful identity service. But, right now their set up lacks the robustness to have fair, equitable and high confidence uniqueness and doesn’t encourage the right user behaviors.

It sounds biased and based on false assumptions.

> Idena requires users to perform validation ceremonies every 20 days. It is done at one set time, and lasts only for 2 minutes. It is at this same hour of the day each 20 days.

Idena’s Sybil resistance protocol is participatory based. This kind of protocols are the most privacy preserving and secure. On the one hand, revalidation requirements, simultaneous participation of all users and AI-resistant flip-tests are a guarantee of the uniqueness and liveness of validated users in Idena. On the other hand, this may be one of the reasons for user complaints. As the Sybil-resistance is a hard problem and one has to choose safety over convenience to solve it.

> Users create ‘flips’ which are two option questions with a series of pictures. Users must then successfully complete a challenge where in they successfully answer a series of ‘flips’ correctly at the validation ceremony.

> With 6 binary outcome options (0 v 1), a user is required to get >75% of them right to succeed. This means a user has a roughly 9.38% chance of getting it correct when clicking at random.

The confidence of uniqueness is reflected by the account status and its age. To get Human status in Idena, the user needs to pass 4 validations in a row and get a total score >92%. It takes about 4 months.

The probability of getting the Human status using the random guessing is 0.00015%

We recommend to apply the k factor for the TrustScore of the Idena user depending on the status of the linked Idena account:

* k=0.60 – Newbie with age=1
* k=0.75 – Newbie with age>=2
* k=0.90 – Verified with age>=3
* k=1.00 – Human with age>=4
* k=0 – all accounts delegated their voting power to another account

k=0 should be applied for the delegated accounts to prevent collusion. In the Idena network the delegation is used to create trusted pools of validated accounts. You can find stats about pools here: 

`https://scan.idena.io/#pools`

> It also requires users to invite other users and to contribute to flips (creating content for them) in order to reach a verified status, and to maintain that in successive challenges.

Idena is a decentralized protocol which enables users to mutually validate each other by creating flip tests. In terms of cost, this is an additional hurdle for the Sybil attack.

> To join a validation session users must either download and run a desktop software, or pay to connect to a remote node in a web browser session.

Idena is a decentralized p2p blockchain network. The network has no centralized servers and is secured by ~800 independent validating nodes run by validated Idena participants. Desktop app with the built-in Idena node is the only way to provide users with permissionless access to the network. We urge all users to run their nodes as it improves both the network security and decentralization.

To enable remote access to the Idena network the Idena web app can be used. It’s really easy to use and it’s adopted for mobile.

The web app requires a connection to any Idena shared node. We don’t use infura-like infrastructure with centralized node providers. Instead there are many Idena users who provide their shared nodes for a small renting fee. It’s absolutely free for newcomers.

But if the user wants to keep using the browser instead of installing the desktop node the renting fees can be charged. However it does not make any burdens for users since the validation rewards cover the fees without need to buy coins on the market.

> That web browser session involves entering, in plain text, into the web browser, a private key.

It's misleading information. The Idena web app does not use the plain text for the private key. Encryption is used for the keys. It always has been. User enters an encrypted key which can not be used without the password. 

> Connecting to a remote node costs only $0.08 per session.

The cost of connecting to a shared node is set by other users who provide their nodes. This cost cannot be used to estimate the cost of an attack. Idena participation is free.

> This model of accessibility creates a low threshold for an economic attack. At $80 spent, you could attempt 1000 verification bots clicking at random across 1000 sessions. In turn, you’d likely end up with 93 accounts.

> Those 93 accounts could contribute known flips to the pool, colluding to make the network verification less susceptible to them specifically in the future.

93 accounts can only create 0.9% flips assuming the current network size of 10k+ making collusion ineffective.


Even though we found some criteria to be conflicting and/or biased, we calculated the Idena score according to the proposed structure:

`https://docs.google.com/spreadsheets/d/1Q5KdvU95kvUQsOVYuCzcincdgmxgbytKqby_7WAPY0Y/edit#gid=0`

There are our comments on the Idena scoring:

`https://docs.google.com/spreadsheets/d/1Q5KdvU95kvUQsOVYuCzcincdgmxgbytKqby_7WAPY0Y/edit#gid=226698713`

-------------------------
