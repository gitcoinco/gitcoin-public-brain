---
id: 11460
title: "Scaling Gitcoin Grant Reviews"
slug: scaling-gitcoin-grant-reviews
category: open-discussion
url: https://gov.gitcoin.co/t/scaling-gitcoin-grant-reviews/11460
created_at: 2022-09-08T10:47:54.630Z
last_posted_at: 2022-10-02T20:53:54.644Z
posts_count: 5
views: 3767
like_count: 27
---

# Scaling Gitcoin Grant Reviews

<https://gov.gitcoin.co/t/scaling-gitcoin-grant-reviews/11460>
j-cook | 2022-09-08 10:47:54 UTC | #1

Right now grants are reviewed by a small set of highly trusted individuals within Gitcoin who have built knowledge and mutual trust through experience and discussion. This optimizes for accuracy but at the cost of centralization, high cost, low resilience to reviewers getting hit by buses and a low limit on the number of individuals meeting some trust threshold is a blocker on this model scaling to large numbers of grants. The challenge is to build a protocol that allows grant reviewing at scale to be very fast, very cheap and very accurate. Achieving any two of these is easy (to be cheap and fast, automate completely; to be accurate and fast, pay high fees to trusted reviewers; to be cheap and accurate allow well paid trusted reviewers to work slowly) but optimizing across all three requires more sophisticated protocol engineering.

In the broadest terms, there are two levers available for reducing the cost, increasing the speed and maintaining the accuracy of grant reviews. These are a) decentralization and b) automation. Decentralization grows the pool of reviewers to pace with the growing pool of grants, moving responsibility from a small pool of trusted reviewers to a larger community - i.e. it makes more humans available to do reviewing work. Automation takes mechanistic tasks out of the hands of humans and does them quickly with a computer instead. Both of these approaches offer important improvements but come with limitations that must be managed. For example, decentralizing naively by simply opening up the reviewer pool risks reducing the overall trustability of the pool because adversarial reviewers will participate to skew the grant reviews in their favour or low-competence reviewers will degrade the review quality. Similarly, automation can deliver efficiency gains to the reviewers but too much automation down-regulates nuanced, subjective grant decisions that can only really be made by skilled human reviewers.

A perfect grant reviewing protocol finds the optimal balance between these factors and enables grants to be reviewed with the optimal balance of speed, accuracy and cost. The system also needs to be configurable and manageable for individual grant owners with minimal reliance upon any central provider. There has been substantial R&D within Gitcoin into how such a system could be built. This post will provide an overview of that R&D and the current roadmap.
 
 
## What does a good system look like?

A good system for reviewing Gitcoin grants must:


* Benefit from economies of scale - the cost must not scale proportionally to the number of grants

* Maintain review quality even when the number of grants increases

* Enable all reviews in a round to be reviewed rapidly - the time taken to compelte a round must not scale proportionally to the number of grants

* Have a UX that encourages project leads to take ownership of their own review system configuration and management. 

* Avoid creating game-able incentives and Sybil vulnerabilities.

If there is one concept that has outsized influence on our ability to build such a system, it is **composability**. For Gitcoin grant reviews this means creating a set of tools that are available to be switched on/off and tuned specifically to the needs of individual grants. A composable set of grant review and Sybil defense tools would enable grant/round owners to configure the reviewing environment to their specific needs and the priorities of their users, while encouraging them to take ownership of their own review system. Allowing grant/round owners with domain expertise to make their own decisions about the context of their own grant round decentralizes the rule-making and distributes it across the actual user-community rather than having itcentralized under Gitcoin control. It also likely promotes effective scaling to large numbers of grants because reviewing is handled by sub-communities, effectively parrallelizing the work. In the composable paradigm, larger numbers of grants could be handled by more subcommunities, equivalent to a computer that dynamically adds more processing cores as the the size of some parallelizable task increases. 


## How can we build this sytem?

Outsourcing work to computers reduces the cost of reviews. This has to be balanced against the naunced, subjective decision-making that can only be made by humans, so the challenge is to incorporate the right amount of automation that doesn't compromise review quality. The question then becomes: which tasks can safely be automated?

### Objective reviews

One task that can be automated is a simple check that grants meet the basic eligibility requirements. This can be achieved using a simple, standardized questionnaire given to grant owners at the time of submissions where the answers can be evaluated against a set of conditions, for example:

```
The grant is VC funded: yes/no
The grant has a token: yes/no
Is the owner account at least 100 days old?: yes/no
...
```

Some of these answers can be verified easily using Gitcoin data. The problem is how to determine whether the grant owner has lied about less easily-verifiable questions. One option is to manually review the answers, but this reinstates the human work that the automated eligibility checks were supposed to remove. Another option is to have a whistleblower reward so that grant owners within a round are incentivized to call out peers who have dishonestly characterized their projects, with the equivalent of "slashing" dishonesty being removal from the round or capping their matching pool rewards. It must be irrational for a grant owner to lie about their project's properties. An initial sift of grants that eliminates those that do not meet basic eligibility would cut the number of grants that make it to the review stage by at least 50% (based on data from previous rounds) translating into large cost savings. This eligibility check can be thought of as an initial "objective review" - it asks whether a grant meets a set of defined criteria and ejects those that do not from the round before human reviewers have been involved. Additional protection can come from incentivized whistleblowing. After the objective review the grant will undergo a subjective human review. This requires human reviewers to be assigned to the grant.

### Subjective reviews

#### Reviewer selection

It is also possible to automate the selection of reviewers that are assigned to a particular grant. Review software like Ethelo can pick reviewers from a central pool and assign them to grants that match their preferences, expertise etc, relieving this responsibility from round owners. This seems straightforward, but there must also be a trust layer built into this process to prevent the reviewer pool being populated by low-competence or adversarial reviewers. This can also be automated to a large extent using Gitcoin Passport. Gitcoin Passport is a collection of "stamps" that act as proof of personhood and evidence of expertise or experience in a certain domain. An automated scan of Gitcoin Passport stamps can be used to create a reviewer profile that can then be used to eject suspicious reviewers from the pool or reduce their trust score. Conversely, metrics derived from Gitcoin Passport stamps can be used to verify reviewers as non-Sybil and give them scores that demonstrate their suitability to review certain grants. Gitcoin Passport can be integrated into Ethelo in this way to automate some important and laborious parts of the reviewer selection process, reducing the cost per grant. Not only will the accuracy not diminish, it may well even improve because of the substantial amount of hidden data science underpinning Gitcoin Passport's stamps and trust weighting functions.

This automation can also provide composability and configurability to grant owners by allowing them to tune the Gitcoin Passport stamps that are of itnerest to them and the criteria they think could be used to identify good grant reviewers. The UX for this could be very simple - a one-click option to activate Gitcoin Passport and then some simple input fields to define some terms of interest. Behind the scenes, these tags can then link to specific stamps. For example:

```
GRANT OWNER: Reviewer configuration:

- Sybil threshold: 0-85 (how sure do you want to be that your reviewers are honest humans?)
- Web3 score: 0-85 (how much web3 experience should your reviewers have?)
- Domain expertise: [ text  ]  (what keywords should we look for across the reviewer pool)
- How many reviewers should see each grant?: 2-4 (cost increases per additional reviewer. Default==3)
- etc...
```

There could therefore be a continuum of automation from entirely manual reviewer selection to heavily automated. Each round owner could configure their round with some lower limit on the amount of automation (e.g. "grants in this round must turn Ethelo ON"). Within the bounds set by the round owner, the grant owners could then tune their reviewer settings to their own specific grant. This approach removes a lot of the friction, and cost, associated with reviewer assignment and trust assessment.


#### Reviewing

The previous section showed how the reviewer assignment could be improved using Gitcoin Passport and Ethelo. There are also enhancements that can be made to the reviewing itself. Currently, the actual reviews are a particular bottleneck because they are conducted by a small number of known, trusted individuals with experience reviewing across multiple rounds. However, to scale to more grants, and to demonstrate credible neutrality, we need more reviewers. This raises two important questions:

1) how can we incentivize users to become reviewers?
2) how can we ensure the reviewers in the pool are trustworthy and competent?

Reviewer incentives can be monetary or non-monetary. In GR14 FDD created a model that explored how reviewers could be optimally organized and remunerated for their work. One outcome from this was a scheme that randomly assigned three eligible reviewers with different trust levels to each grant, always ensuring that the total trust level exceeds some threshold. The reviewers can then be paid in $GTC or another community token with the value awarded scaling with their trust level, incentivizing reviewers to participate to get the experience and Gitcoin Passport stamps that raise their trust scores to unlock greater rewards.

Non-monetary incentives have also been shown to be powerful in many communities, especially achievement-gated POAPs and NFTs which could themselves factor into the Gitcoin Passport trust scores or be used directly as Passport stamps. An empiricial experiment is currently underway that will test the performance of reviewers incentivized in different ways in an Ethelo mini-round and also explore what data is most valuable to collect from reviewers and how that data can best be managed and mined.

Gitcoin Passport provides the initial trust score that can be used to give confidence that the reviewers in the pool are non-Sybil and also to partition the reviewer pool into trust levels and knowledge domains. This information can be used to assign reviewers to particular grants according to the preferences of individual grant owners. At the same time, participation increases the trust score of reviewers, especially when they are rewarded with POAPs and NFTs that can be factored into their Gitcoin Passport. This flywheel effect could rapidly grow a community of trusted reviewers for individual communities, for Gitcoin and across Web3 as a whole because the reviewer's credentials would travel with the individual as a composable, transferable set of attributes. Since getting started as a reviewer is permissionless, anyone can jump onto this flywheel and become a trusted individual - the only criteria is active, honest participation. The transferable social reputation and activity-unlocks offered by the POAPs and NFTs might turn out to be more valuable to users than the monetary rewards, which could lead to further cost efficiencies. The positive feedbacks and community-building that can emerge from non-monetary rewards are also desirable because they circumvent to some extent the risk of inadvertently embedding a plutocracy where the barrier to Sybil attacks and dishonest review practises is just some threshold of wealth. It also encourages individuals to take the necessary actions to increase their skill and trustability over time while also attracting new entrants to the reviewer pool, creating a flywheel of positive behaviours that can diffuse across the web3 space. 

The idea of credential transferability is very interesting and draws upon some of the core ethos of web 3 - one could imagine interesting symbioses where platforms that benefit from Gitcoin funding encourage their users to participate in reviews by giving priveleges to their own users if they have a certain trust level or particular set of Gitcoin Passport stamps, and reciprocally provably honest usage of the platform is recognized by Gitcoin Passport in the form of stamps or trust score.


### Appeals, approvals and QC

The proposed grants system is ultimately a consensus protocol - it uses a set of embedded rules to create a situation where the community can agree that grants have been honestly reviewed by human reviewers to an acceptable degree of confidence. However, the protocol requires a social coordination layer underpinning it that can act as a fallback when a) the protocol misjudges a review and b) when an attack successfully breaches the protocol's in built defenses. The simplest model for this is to have some trusted arbiter that polices the grant review process and settles any disputes. However, this is a centralized model, which raises risks of that arbiter being hit by a bus, being evil, or being bribed. Much better is a decentralized mechanism where a community can collectively settle disputes and whistleblow on dishonest behaviour. Some ideas include an iterative mechanism where grants that are disputed are reviewed by another random selection of reviewers, perhaps with a higher overall trust score than in the previous round, this time with access to the dispute details submitted by the grant owner. The cost of this could be covered by the grant owner if the dispute fails and by Gitcoin if the dispute succeeds, creating an economic disincentive for dishonest grants and incentive for honest grants to appeal an unfair result. Other ideas include settling appeals on an open forum with a Gitcoin Passport trust-score weighted vote determining the outcome after a discussion period. These mechanisms need not apply only to appeals, but to any appeal including dishonest grants or reviewers that are identified by other members of the community (whistleblowers).


### Retrospective insights and round-on-round learning

Incorporating more software, such as Ethelo, in the grant reviewing process also enables more data capture that enables round-on-round learning and refinement of the system. A challenge for Gitcoin right now is making its data openly available and accessible but also sufficiently anonymized. In a previous post, we outlined plans for decentralizing Gitcoin data and empowering the community to access it and use it in creative ways. This is likely to be increasingly important as Gitcoin grants scales to more users, as we cannot assume insights from smaller rounds under the original centralized grants system hold true for larger grant rounds managed under Grants 2.0. It makes good sense that as the number of grants, grant owners, reviewers and the size of the data captured all grow, so should the data science community tasked with mining knowledge and refining the system.

A few examples of how this data analysis could feedback into the grants system are a) identification of metrics and indicators that could act as early warning systems for "bad" grants or reviewers; b) indicators that can aid in Sybil detection and refining Gitcoin Passport trust scores.

### Some composability risks

One could imagine a system where the owner of each grant submitted has freedom to easily configure and manage how their project is reviewed. However, offering complete freedom to customize opens the door to nefarious actions by grant owners. For example, a grant owner could remove any quality control and encourage Sybil-type donations to their grant. On the other hand, there could also be cartel risk, where round owners tune their eligibility requirements to be extremely high or very specific to favour certain individuals, creating exclusivity that can then be gamed.

The ideal situation would be to have some incentive structure that encourages grant owners to tune their review configuration to be more stringent rather than less. One could imagine some incentivized inter-community moderation services that cross-calibrate review quality. Pragmatically, at least at the start, protection from composability-gaming would more likely come in the form of some simple binary eligibility criteria that enable a round owner to programatically filter out ineligible grants. This would free up human reviewers for assessing valid grants that need subjective, nuanced human consideration.

## Summary

Gitcoin is growing and it needs a grant reviewing system that can scale. At the moment, grant reviews are too centralized and rely too heavily on the work of a few trusted individuals. To scale we must increase the number of individuals participating in grant reviews while also outsourcing as much of the work of each individual to computers as possible. At the same time, we need the system to be adaptable to the needs of individual groups of users so that the grant reviewing can be community-tailored at the most granular level possible. The vision is that a grant owner can submit their grant to a round that has been specifically configured to meet their specific needs, and they have agency in determining precisely what that configuration looks like. Their grants are then reviewed by a set of reviewers from the community pool with the requisite knowledge and experience. Grant owners can then be satisfied that their round was as safe, fair, aligned with their community's values and completed quickly. Delivering this vision requires a composable stack of accessible reviewing tools and systems of incentives that encourage those tools to be adopted and used honestly. This article has outlined what some of those tools might be and how they might be deployed in Grants 2.0, and also what attack vectors might need to be managed when composability is introduced into the reviewing process.

Moving forwards from here requires weighing up the options for composable reviewing tools, making decisions about what to implement in the coming rounds and how to monitor their performance. There are experiments currently underway with test populations of reviewers that should inform these discussions. 

*@DisruptionJoe and @carl provided very useful feedback on this post*

-------------------------

ccerv1 | 2022-09-08 15:27:08 UTC | #2

Thank you for this post. I agree with you that we have a long distance to travel from the current centralized & highly subjective process to a [protocolized version](https://gov.gitcoin.co/t/the-impactdao-protocoldao-sandwich/8944) of grants review. It's essential to have a credibly neutral grants curation process that achieves a level playing field for all eligible grantees.

IMHO, "credible curation" is a necessary primitive -- arguably on par with Sybil resistance -- but much less understood. We need this to be [trustware](https://orca.mirror.xyz/T70CmuhX95ubkw_JHOxSEy8d_EFeYXgtJnF13mPtaZE).

For GR15, I worked closely with the Public Goods team on the DeSci round -- setting eligibility criteria, doing grantee outreach, and reviewing grant submissions. Here are a few thoughts from my experience,  which build on your suggestions for progressive decentralization:

- **Automation**: A number of eligibility checks can be automated. For instance, determining the amount of funding received in the past, screening for contributors' conflicts of interest, pulling heuristics on the age of the project / number of contributors, screening for duplicate submissions, etc. There could be an interesting use case for [Gitcoin Passport](https://gitcoin.co/blog/intro-to-passport) to score contributors' trustworthiness too.

- **Batching**: Grant reviews can be batched more intelligently for the humans in the loop. For example, grants that have very similar keywords or have shared core contributors can be batched. A reviewer can use batching to make important gating decisions, eg, "are these 5 grants duplicates". There are a lot of UX improvements to make work easier for human reviewers while at the same time training models to aide human decisions. 

- **Biases**: Every reviewer will have their own sources of bias that overtime can be controlled for by comparing their reviews with others in a pool. As a reviewer, I shared my heuristics with other reviewers and my doing so likely had some influence on other reviewers' decisions. It could be helpful to do blind assessments in order to calibrate reviewers and also ensure the right perspectives are represented. Over time, we can develop heuristics for trusted reviewers and provide either rewards or give increased weight to their decisions, like you describe.

- **Feedback loops and notifications**: There needs to be a stronger feedback loop among FDD, round eligibility reviewers, and grantees making updates / clarifications. As a reviewer, I would only look at each grant once and it's possible that grantees made improvements or changes to their profiles that might have changed my decision if I'd been notified. I don't know how/if my or my peers' observations were funneled back to FDD or to grantees.

- **Consensus mechanism**: It wasn't clear to me as a reviewer what the ideal consensus mechanism is for determining eligibility. Should it require an unanimous "hell yes" from all reviewers to be accepted? Should it require a single "hell no" from one reviewer to be ineligible? Should it require a consensus score above a certain threshold? Presumably you'd want to support a variety of consensus mechanism that communities can choose from and the rules of the game are made explicit to grantees at the start of the round.

The Grants 2.0 endgame likely needs to involve two sets of reviewers:
-  True independents who have no skin in the game apart from wanting to develop a good ratings reputation over time, ie, "professional reviewers"
- Deep domain experts who have skin in the game in the sense that they want the round to succeed by having a high quality grant mix, ie, "peer reviewers"

There can be some compelling interplay and game dynamics between these two groups of reviewers. A bit like the role of triage teams and specialist teams in a hospital.

Anyway, thanks again for shining light on such a critical piece of the puzzle!

-------------------------

buildingweb4 | 2022-09-30 04:07:48 UTC | #3

Thank you for the overview of the challenge @j-cook! 

We had a similar challenge in our protocol (how to make domain-specific review processes accurate, decentralized (even trustless) and exceedingly difficult to game). Part of the solution we came up with involves random assignment of reviewers (to prevent collusion between the project and reviewers); reviewers have a domain-specific expertise score (so if multiple reviewers are assigned to a project, their reviews are weighted by their expertise level). 

There are also multiple groups of reviewers - so Group A could be assigned to directly review projects, while Group B is assigned to vote (thru QV) on the quality of each review from Group A. Group B is then divided into two subgroups that vote on the quality of individual voters in the other subgroup (this process is meant to align incentives for every reviewer - reviewers in Group A are incentivized to make accurate reviews, since they get expertise points (and optionally financial compensation) based on the quality of their review, while reviewers in Group B have an incentive to award more points to higher quality reviews (and not some ulterior considerations) since they too are reviewed. Reviewers may also need to temporarily deposit funds for the review process, in proportion to their expected payout (this can serve as an anti-sybil mechanism)

Finally, there is a challenge period where anyone from the community can (trustlessly) object to results - as a security measure against collusion/attacks from within the groups (and that's a process onto itself)

These are just some suggestions for ways to address the scaling/decentralization issue - the right mix of mechanisms/tools really depends on what a community needs (trustless? compensation? etc), so it may be useful to think of these as composable tools in a toolkit..

-------------------------

kyle | 2022-10-02 19:52:30 UTC | #4

Have you open sourced or documents the tools and process you are using to facilitate this?

I have watched a number of folks talk through better ways of doing this, but we have really struggled to go from 0 to 1 on making changes. I dont want to seem ungrateful for the details on the “how might we…” question. I would love to see us build a work back plan now on how we get there :slight_smile:

-------------------------

buildingweb4 | 2022-10-02 21:01:25 UTC | #5

Our current protocol design & mechanisms are based on about a year of red-teaming and improving a previous protocol design. We started coding/testing elements of the previous design, then realized we can make the protocol a lot more robust, so that's where we are.

The discussions/red-teaming were held in our Discord server, while the whitepaper for the protocol is up on github - [here](https://github.com/buildingweb4/Abundance-Protocol/blob/main/public/Abundance-Protocol-Whitepaper.pdf).

This is all still very experimental, and we'd like to get as much input as possible from the wider community on our protocol design. I did however want to share the insights here since it seems our challenge was similar to the FDD challenge for grant reviews, and I believe our solutions can contribute to FDD's success.

With that said, I'm quite new here (though I read through a lot of the discussions on FDD/reviews already) so I'm not entirely sure what stage the project of scaling grant reviews is in, or if the "final" product is well defined yet. If it is, we can look at different approaches to getting there and choosing the options that scale best. If not, I guess that's where the focus should be?

I'd love to help out either way - my background is in economics, architecture/graphic design, and I've been learning fullstack web development & web3 over past 2 years.

-------------------------
