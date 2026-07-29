---
id: 12764
title: "Tax Mechanisms for GitCoin Grants"
slug: tax-mechanisms-for-gitcoin-grants
category: gitcoin-grants
url: https://gov.gitcoin.co/t/tax-mechanisms-for-gitcoin-grants/12764
created_at: 2023-02-05T02:04:50.758Z
last_posted_at: 2023-03-07T10:55:20.177Z
posts_count: 5
views: 3273
like_count: 18
---

# Tax Mechanisms for GitCoin Grants

<https://gov.gitcoin.co/t/tax-mechanisms-for-gitcoin-grants/12764>
octopus | 2023-02-05 02:04:51 UTC | #1

I would like to propose some mechanisms for giving GitCoin Grants more Sybil resistance without enforcing strong identity. 

My personal feeling is that there may be a relatively simple solution, which is to charge a "processing" tax of N USD for the very first donation that an account makes. This means that it costs at least (N+1) USD to make only one donation of 1 USD. The average cost per donation goes down as an account makes more donations (over multiple rounds, or to multiple projects within a single round). Making 1000 1USD-Sybil accounts now costs (N+1)*1000 USD. This discourages making multiple accounts for Airdrop Farming, as well. Honest users will be able to absorb this, whereas dishonest strategic users will be disinclined. 

In addition, I feel it would be fair to charge projects a small  graduated fee based on the proportion of the matching pool they have earned. Just like poker players tip the dealer after winning, it's legitimate for projects which have strong showings to redirect some of that towards the GitCoin Grants protocol that did the hard work of making the process possible. 

Pragmatically, compare the cost and potential public disagreement with these mechanisms to the resources needed for FDD work and the Passport service. While those projects have a role to play, simply being a bit more careful about the flow of funding may be a simple way to help Grants rounds be more self-sustaining and self-protecting.

-------------------------

connor | 2023-02-14 08:08:49 UTC | #2

I'm a fan of this idea and it's very similar to one concept I wrote about in an old GTC utility brainstorm. I still think it's a very reasonable approach to disincentivize airdrop farmers/sybils/low effort fake grants. My approach was coming from the angle of adding new use cases for GTC (considering both a simple fee mechanism and a staking approach) but touches on the same exact mechanism you describe. One of the main points I'd like to highlight as a TLDR:

>Charging a flat fee that is not returned to the user does make the platform “pay to play” and may disproportionately impact lower-income grantees and donors. However, this is the easiest way to make fraud and Sybil attacks more costly to bad actors. There likely exists a low enough fee threshold where the expected value of cheating is not profitable for most attackers, while still minimizing the number of honest users who are truly priced out.

I'll drop excerpts from the doc below (with some of the introduction for context, but some sections skipped:

> GTC Utility and Protocol Sustainability in Grants 2.0 and Onward
Preface: Sustainability
... 
>1. Protocol fees -> ...
> 2. Managed services -> ...
> 3. Token Utility -> Create new use cases for GTC that solve meaningful problems, increase demand for the token, and grow our community in engaging ways
-Leverage mechanism design to gamify Grants and QF for all stakeholders
-Disincentivize bad actors applying for and funding grants with increased risk and penalties
-Provide means for the community to earn tokens via the protocol by simply engaging and taking part in productive incentivized actions
-Token utility becomes a coordination and cooperation tool
...
Consequently, this document will mainly focus on exploring ideas for # 3 - GTC utility - in isolation, for protocol-mandated token utility, and positive-sum mechanisms.

>Background on GTC and Token Utility
Current GTC uses:
...
Primary Platform Stakeholders:
...
Framework, approach, assumptions
Consider the problems Gitcoin Grants currently faces, and how integrating new mechanisms using Gitcoin’s native governance token can help solve or alleviate those issues. (As opposed to trying to fit GTC into as many areas as possible to increase token demand - a solution looking for a problem).
Building true utility into a token should lead to a scenario where even if the protocol is completely finished and the team is dissolved, the token continues to be used and valuable. 
....
With this in mind - how can the Gitcoin DAO position GTC to play a key role in the Grants 2.0 protocol long term, irrespective of any core team’s involvement or future upgrades? Is this even possible in a social/impact DAO?

> **Use case 1: Barrier to entry** (perhaps the lowest lift GTC use case in the near term)
**Problem**: Fraud, spam, impersonation, and Sybil attacks are rampant because there is little to no cost and plenty to gain by cheating quadratic funding or grant programs.
**Solution**: Charge a base fee in GTC for certain platform actions.
For example:
A grantee must pay or stake GTC to open a new grant
>* For any initial grant hub application
>* Possibly for applying to specific rounds

>A donor or passport user must pay or stake GTC to verify and register their identity
>* Passport staking features in progress to increase trust bonus - but as long as this is optional, it will not sufficiently disincentivize Sybil attacks or airdrop farmers
>* Some or all rounds could require a GTC stake before a donor can participate
>* Trust bonuses could increase logarithmically over time the longer GTC are staked or delegated or used to actively govern (ie. max bonus 200% as time approaches infinity)

>Where would the GTC go?
Easiest solution:
>* GTC is burned (supply decreases)
>* GTC is sent to the general matching pool (held long-term and/or used for matching)
>* GTC is sent to DAO treasury

>More complex solution with staking (+ risk):
>GTC is staked on identity/grant
>* Stake could be locked until grant or identity chooses to remove themselves
>* If there is no threat of losing this stake, there is no disincentive for cheaters
>* Stake could be returned if approved, and confiscated if not (but centralized?)
>* Decentralized and community-led disputes - users who find and flag bad actors could be rewarded with the staked GTC, however, this would require a robust arbitration and dispute mechanism (hard problem to solve)

>Staking GTC on profiles or grants is generally the more interesting option and has more long-term potential to experiment with new mechanisms. However, in its current form (conviction voting to sort grants in UI, passport stake for trust bonus) **there is no risk of losing funds, and no penalties for bad actors, thus it does not address the problem of fraudulent grants/donors.**

>**Charging a flat fee that is not returned to the user does make the platform “pay to play” and may disproportionately impact lower-income grantees and donors. However, this is the easiest way to make fraud and Sybil attacks more costly to bad actors. There likely exists a low enough fee threshold where the expected value of cheating is not profitable for most attackers, while still minimizing the number of honest users who are truly priced out.**

A final bit expanding on the topic:

> Barrier to entry (continued - funders)
Matching funders could be made to stake GTC to run their own round (less of an issue for cGrants, but worth considering for Grants 2.0 when self-serve rounds see widespread adoption)
>* Could make sense depending on how 2.0 contracts work - is there a trust assumption with payouts? Could a round operator rug grantees? Is there a risk they don’t pay out the matches or they can game the results, or will matching funds be held in escrow the entire round (arbitration needed)?
>* Grants program/round owners also need to gain reputation, build trust, and establish identity. Similar to grantees, round owners are also orgs that may need to be trusted and can stake/pay GTC to establish legitimacy
>* “Social contract” utility: Round owners using managed services could be required to “lock” GTC for ~1(?) year and participate in governance

>Misc. considerations:
>* Can users staking still delegate to others or vote on governance themselves?
>* If Eth or stables or any other token works in lieu of GTC is it just another “Chuck E Cheese” forced transactional token (lacking real utility)? I’d argue no, because:
>--- Network effects - protocol value grows with more users and more use cases
>---Fostering GTC usage aligns incentives and encourages ecosystem participation
>* What does the Gitcoin protocol/platform offer that disincentivizes others from forking out the fee or token?

If you made it this far - thanks for reading! I go on to explore some other token use cases (maybe I'll share in the future) but this is what's relevant to this thread. The TLDR is - I (and others) have thought about this idea. Long term I think grant/identity staking is a more creative and positive-sum solution, but given how complex that can get, I really agree that in the near term, a simple tax/fee mechanism will help mitigate a lot of problems around Sybils/spam/fraud. I hope we can keep this conversation going!

-------------------------

DisruptionJoe | 2023-02-14 13:44:12 UTC | #3

[quote="connor, post:2, topic:12764"]
Long term I think grant/identity staking is a more creative and positive-sum solution, but given how complex that can get, I really agree that in the near term, a simple tax/fee mechanism will help mitigate a lot of problems around Sybils/spam/fraud. I hope we can keep this conversation going!
[/quote]

I really love this work. Its great that you shared it here. As you know from working with me for quite a while now, I used to be much more opinionated in terms of what will and won't work. I'd prescribe certain mechanisms as a solution to problems. 

What I've been realizing with the grants protocol is that our job is to enable experimentation of these mechanisms. The protocol provides some level of control in experimentation which is conducted by non-collaborating entities. The protocol itself turns these non-collaborators into collaborators by providing economies of scale benefits from any experiement as shared R&D for all future programs. 

This comment is definitely a "yes, and..." to your and Octopus suggestions. 

I'd love to push the conversation from "Is this a good mechanism?" to "Is this mechanism only a few clicks away for any program manager?"

We are the program manager for the Gitcoin Core rounds so we can lead the field in experimentation as we dogfood our protocol. My comment here is a suggestion as to how the Program & Protocol teams can work together to accelerate the R&D cycle of the entire Gitcoin ecosystem!

-------------------------

connor | 2023-02-15 00:23:11 UTC | #4

Yep fully agree - I think we need to build (and enable others to build) all types of extensions and features to experiment with. When we consider various mechanisms like this, I don't think a "yes" vote means the feature should be adopted across the board for all rounds, but rather it would be a useful option for round owners to have, that can be toggled on and off as desired.

-------------------------

jengajojo | 2023-03-07 10:55:20 UTC | #5

Love the idea of hitting two birds (token value accrual and Sybil resistance ) with one stone with a “processing” tax. However, the resulting barrier to entry is a valid point. 

Instead of a fixed tax of N USD per new donor, how about using a % of the initial donation as a tax. One can apply regressive % over subsequent donations meaning the more times one donates, the lesser 'tax' will be paid.

On the side of charging projects, I suggest an 'opt-in' switch instead of a default minimum to begin with. This way projects can themselves decide how much value to give back to GitcoinDAO either as a % of their received donation or matching bonus.

-------------------------
