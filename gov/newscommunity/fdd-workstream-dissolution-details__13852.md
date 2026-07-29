---
id: 13852
title: "FDD Workstream Dissolution Details"
slug: fdd-workstream-dissolution-details
category: newscommunity
url: https://gov.gitcoin.co/t/fdd-workstream-dissolution-details/13852
created_at: 2023-04-06T12:41:46.970Z
last_posted_at: 2023-07-07T04:14:49.407Z
posts_count: 9
views: 4201
like_count: 84
---

# FDD Workstream Dissolution Details

<https://gov.gitcoin.co/t/fdd-workstream-dissolution-details/13852>
DisruptionJoe | 2023-04-07 16:38:02 UTC | #1

The Fraud Detection & Defense workstream has come a long way since its ideation in [May 2021](https://docs.google.com/document/u/0/d/13I8-xgn39bNKVWsgQtrxzdQCMEXgx6ZDLzKZTShH-rI/edit) and inception in [August of 2021](https://gov.gitcoin.co/t/proposal-fdd-wg-anti-fraud-sybil-collusion-q3-budget-request/8210). As one of the first workstreams, it helped to create a pathway for other workstreams to follow.

In my view, the work of FDD over the past couple of years has been a highlight of Gitcoin and what DAOs can do in general.

> ***We stopped over $3 million in fraud with unknown amounts deterred.***

We started and spun out Support, DAOops, and Grant Eligibility functions as we found solutions for managing the sybil problem.

Gitcoin is providing a way for people to collectively make decisions that aren’t pure plutocracy (1 token = 1 vote) in a legitimate and credibly neutral way. When someone says “I want to run my rounds like Gitcoin does” they are indeed saying “Gitcoin has the only mechanism which has delivered decentralized funding decisions at scale in a way that the community trusts”.

We learned that the reason sybil is an unsolved problem is because all known solutions involve trade-offs. The work of FDD is now complete because tools & processes for communities to choose either side of these tradeoffs now exist. Not only do they exist, but we have also built & launched the processes and communities needed to continue the research & development cycle without us.

> ***The launch of the Allo protocol, GrantStack, and the maturity of Passport are signals that the time for FDD is done. A centralized entity should no longer be in control of detecting or sanctioning fraudulent behavior.***

This function now lies with the communities running rounds and the service providers who support them. We hope the ability to use the tools and processes we have developed will continue Gitcoin’s reputation as a trusted way for communities to fund what matters.

As the workstream winds down, we’d like to help the DAO smoothly transition through the dissolution of the FDD workstream and the transition to have fraud defense a vital part of end-to-end accountable product workstreams.

To accomplish this, we are going to cover the following:

* What we accomplished
  * Sybil Management Solution
  * Project Highlights
* What we are doing this season
  * Quick FAQ
  * S17 roadmap
  * People transitions
  * Accounting closure
* What we learned which may still be of use
  * Data Infrastructure
  * Sybil detection
  * Grant eligibility
  * Decentralization

# What We Accomplished

Gitcoin has stopped $3 million in fraud since season 9, most of that coming from FDD.

* Over 30,000 human evaluations of algorithmic policy determinations
* Performed over 15,000 grant reviews for fraud & initial round eligibility
* Mitigated over 250 disputes
* Judged over 100 appeals

Gitcoin is the shining light in web 3 that shows people something other than pure plutocracy is possible. It is the only mechanism that has scaled a system other than 1 token = 1 vote for distributing funding. People believe in Gitcoin because they have seen $50 million in funding with a relatively small amount of harm due to fraud. Trust is the product Gitcoin provides.

## Created a Solution for Managing the Sybil Attack Problem

The Sybil Scoring Legos System for continued sybil defense is the needed tool to compliment Gitcoin Passport’s ability to gate rounds. We learned that the participants of each round have unique properties. Some of these work well with a gating/weighting system. Some do not.

The solution for managing sybil attacks requires the ability to detect malicious behavior during the round. Most importantly, any decision made using data during the round must be reproducible. This includes using transparent and auditable code, data version history from the time the data was collected, and a provenance guarantee.

Sybil Scoring Legos System has the following properties:

* Transparent and auditable data pipeline for algorithmic policy decisions
* Allow for a non-technical user to identify the violated behavior
* Reintroduces explainability underneath ML algorithms used to scale
* Composability in ML algorithms allow fast updates when new attacks are found
* Anyone can build productized algorithms and interfaces using OS code
* Crowdsourced research & development to continually assess validity
* “Kerckhoff Compliant” system design made possible by being fully open

## Highlight Projects & Accomplishments

* First DAO to run a Machine Learning Operations (MLOps) pipeline
* First DAO to execute a (politically) decentralized conflict resolution process with our appeals escalation process for grant rounds
* Started and spun out Support, DAOops, Onboarding, and Grant Eligibility
* Launched the OpenData Community - a community fighting sybils & protecting web3 from capture at the data layer: https://opendatacommunity.org/
* A first opted-in and consented graceful wind down of a DAO workstream
* Ran on budget with industry leading transparency for 7 seasons
* Created an ethical transparency mechanism in the FDD Review
* Provided support for other teams including first trust bonus algorithms for Passport, Financial Audits for DAOops, and Grant Reviews for PGF
* Started the workstream with a multisig counsel of experts to protect Gitcoin funds
* First workstream to voluntarily decrease budget on steward request
* First workstream to provide funding options to stewards in a vote
* Returned 100% of reserves to treasury EVERY season
* Only workstream which didn’t increase budget request amount when CSDO made agreements to keep budgets flat

# What We Are Doing This Season

## Quick FAQ

### When will FDD dissolve?

FDD will officially dissolve on April 28th. We’ll host a community call the 26th of April to do a public retro and celebration of this workstream’s work. All core contributors who have new priorities within other workstreams have already been embedded into the necessary meetings during the last several weeks, and these contributors who have been hired-on by new workstreams will have their official hand-off to new leadership beginning April 7th. It is understood that these contributors will continue their efforts to wind-down FDD while also gaining context and making an impact in collaboration with their new workstreams.

### How will FDD be funded through S17 since the budget request was not granted?

Due to some savvy treasury management tactics and independent funding sources, FDD still has ample funds to continue the work that was originally proposed in the S17 budget request. The additional funds requested in association with this budget were declined during a new vote appeals process pioneered by the Steward’s Council last Monday; however, thanks to the total amount of reserves and surplus funds, FDD is still able to complete the season uninterrupted..

Since the overwhelming consensus was that FDD’s budget *strategy* was in-line with the DAO’s desires, but the funding mechanism was in question, FDD leadership believes the best course of action is to utilize remaining funds in the service of those strategic outcomes already agreed to and voted upon by the DAO.

### So what happens during S17? We’ve only got one more month!

We have already made good headway on many of these initiatives outlined in the S17 budget. FDD expects all deliverables to have been completed by April 28th.

All core and part-time contributors who are working directly towards those deliverables will be paid through until that point. In any cases where contributors and the DAO decided to part ways, severance has been paid or will be paid at such a time as that contributor’s work ceases to directly contribute to those key deliverables.

### What about sybils…?

As Gitcoin is absorbing risk as a mindset within all of its remaining workstreams, sybil-detection and anti-collusion work will continue to live within Passport’s roadmap, Allo’s systems’ design, and PGF’s core trust and reputation work.

# Season 17 Roadmap

## Continued Trust in Gitcoin’s Ability to Prevent Fraud

Data informed recommendations to mitigate fraud are made continuously available.

### Fantom & Gitcoin Alpha Round Recommendations

* Fantom required a lot of back and forth work
* Alpha rounds completed - Overview [here](https://docs.google.com/presentation/d/1U4q3TMiNZiOpHFIu5r_jIvA7X6g0eXcgdtVpLJM5OLw/edit?usp=sharing)

### A Scalable Mitigation Sybil Solution Exists

* Sybil Scoring Legos System [docs](https://github.com/Fraud-Detection-and-Defense/lego-docs)

### Sybil Defense Innovation & Insights Continue after FDD

* Open Data Community 2nd hackathon funded 39% by Gitcoin
* ODC will conduct the 3rd hackathon which runs mostly after FDD season is over
* ODC will maintain the research and development cycle for legos

### Passport has Analysis & Data Science Support

* Provided job description suggestions
* Provided analysis & data science support for reweighting the algorithm

### Recommendations to Correct Web2 Vulnerabilities are Followed Through

* Followed through with product team to find solutions

## Empowering the DAO with Open Data, Infrastructure, & Processes

Data processes & pipelines are reliably available & maintained.

### An On-chain Data Extraction Solutions that Meets the Needs of Real-Time Anomaly Detection

* Nodes have been delivered
* Stack includes Erigon archive node w/ Trueblocks

### Open and Decentralized Data Repository for the Community

* All data can be found at https://fddhub.io/

### Gitcoin Analytic DB & Query Interface

* Being worked on by Zen, Baoki, & Alex
* Goal is to pull in the node data allowing for realtime anomaly detection

## FDD Workstream Dissolution Success

FDD contributors and work is smoothly transitioned and/or shut down.

### Successful Transition of Contributors

* Documented below
* Two contributors still unsure of placement

### Clearly Documented Closing of Accounts & Obligations

* Final plans agreed upon in FDD and shared to CSDO
* Creating FDD MolochDAO for any future airdrops or other value unlocks

### A Proposal for a Ratified Process to Spin-Out “Investible Workstreams”

* Joe handling this objective
* Multiple model potential - Working on JokeRace to propose best model
* Current front running models
  * Onchain SAFE/SAFT for subDAOs by Joshua Tan
  * Proposal Inverter spun out from Developer DAO & TEC
  * Pure Mutual Grant vote

## People Transitions

FDD talent will be moving to new opportunities, some with other workstreams and some outside of Gitcoin. Here we aim to inform you of next steps for each current member of FDD.

These members will be transitioning to other workstreams and their transitions have been confirmed by the person listed:

* Alex - Sr. Fraud Analyst > PGF Program (Maxwell)
* Baoki - Data Analyst > Allo Protocol (Nate)
* Zen - Data Engineer > Allo Protocol (Alex/Kevin)
* Sorana - Operations/Analyst > Allo Protocol (Kevin)
* J-Cook - Technical Writer > DevOps (Zakk)

These members will not be moving forward with a Gitcoin workstream.

### Disruption Joe - Workstream Lead (Last day 4/28)

Not pursuing a future role with a Gitcoin workstream. Launching Plurality Labs, a service organization intended to help communities utilize the tools built by FDD and manage governance and grants programs. Will likely participate in the Round Operators program. Last projects include successful management of transitions, accounting wind down, and bringing a proposal for investible workstreams to the DAO.

### Tigress - Workstream Lead (Last day 3/24)

Not pursuing a future role with a Gitcoin workstream. Received a recommendation letter for her next opportunity. Last project finished as she handled operations through EthDenver and had her final day after prepping for the winddown.

### OmniAnalytics - Data Scientist (Last day 4/28)

Not pursuing a future role with a Gitcoin workstream. Open to future project-based scopes of work in contract with Gitcoin. Has [OmniacsDAO](https://omniacsdao.xyz/) focused on making data science a public good. Last project involved assisting in data scraping for the Alpha rounds, passport reweighting, and a behavioral analysis of onchain data.

### Evan Powell - Operator

Not pursuing a future role with a Gitcoin workstream. Choosing to continue the work of the Open Data Community to achieve sustainability. The Open Data Community will run its third hackathon even though the FDD season technically ends on 4/28, though the hackathon will run from 4/25 to 5/30. Potential to create a GCP for Gitcoin to be an official founding member as they launch governance.

### Non-core Trusted Members

* Yogeesh - Part time software engineer (ML)
* Eric - Part time software engineer
* Adebola - Former core on Project-based scope this season

## Accounting Closure

FDD has 2 main wallets and at times have used EOAs for trading. Trading EOAs do not hold funds for any extended period of time outside of the duration of the trade other than a few hundred for gas.

### FDD Primary Multisig 4/7 - Currently holds $0

The primary FDD multisig had its full amount sent to the operations wallet at the beginning of Season 17. To ensure our ability to meet commitments, the entire balance was then traded to stablecoins.

### FDD Operations Multisig ⅔

The operations wallet has the rest of the FDD treasury. The last salary payments will go out on 4/10. Payments for the last 3 weeks of the season will have been fulfilled via double payments the previous 3 weeks.

### Leftover Funds After Final Payroll

* Funding of approved travel & personal development expenses
* Hosting a Featured Round during the Gitcoin Beta round with
* Summoning a MolochDAO for FDD members to own any future value

We would love for you to join us for the summoning ceremony which is tentatively scheduled for 4/26 during our farewell FDD celebration event during the Gitcoin community call.

# What We Learned Which May Be of Use

## Data Infrastructure

* In an org which aspires to transparency, the need for data quality assurance and pipeline management best practices goes beyond the DAO.
* Our community members and stakeholders have a vested interest in learning from our grants rounds; we are pioneering QF in many ways, and before Gitcoin can share take-aways and establish greater thought leadership in this emerging discipline, we must be clear on our own methodologies and exercise greater tracking and versioning control on our datasets.
* On-chain data and self-sovereign databases are a non-negotiable in a world where governments and government-sized cloud storage providers disrupt the data availability we all depend on.
* We can learn from some high-profile errors of web3 projects of late: we need to be the experts in our own ecosystem. To do this, we have to set up enterprise-level anomaly detection and adopt a risk mindset throughout the org.
* Grants Partners trust us with funds with the understanding that we can safely and fairly distribute those funds: a prerequisite to guaranteeing their safety and keeping their trust is to monitor for new and emerging exploits.
* It’s a high quality problem, but to scale and lean into the hypergrowth that Gitcoin is headed towards, we cannot continue the level of manual analysis which we have conducted in the past. Whether it’s PGF reviewing grant applications or FDD reviewing sybil rings: we need to prepare automated tactics utilizing statistical analysis to free up our contributors to do their best work at scale.

## Sybil Detection

* FDD has done ample research and employed many partners in solving the sybil problem for our ecosystem. While sybil research and on-chain identity is an ongoing topic throughout the web3 space, the bottom line is: Gitcoin knows how best to protect its own grants rounds.
* Statistical analysis allows us to detect and silence votes where there is evidence of script-execution of grants support or recycled funds in play; with the new availability of on-chain signals, we can positively ID supporters who use the same funding mechanism or execute identical heuristics across wallets and be sure that their votes are counted only once per unique identity.
* The wider community remains fascinated by the problems of sybil detection, and with the cleaning of Gitcoin and FDD datasets, we can provide a wealth of information and access to these budding sybil slayers. We are excited for the models and solutions to come that build on Gitcoin’s expertise to further articulate the nature of these exploits.
* Sybil Scoring Legos will likely need to be connected to Passport. This may be through another community or company attesting to wallets that participate in a round or Gitcoin itself. Gitcoin might hold a list of ineligible wallets for its own program, but this is not universal.
* Passport is a great solution for gating/weighting user participation in votes. However, Gitcoin must enable transparent and auditable analysis based decision making which scales based on users behavior in a round. This is because of the adversarial nature of sybl defense.
* It is also necessary to provide a choice to program managers. While adjusting the results of a vote after votes are cast (retroactive sybil discounting) seems more unethical than gating access using Passport, the compounded effect of gating is arguably more unethical. Any inherent biases in the stamps available and peoples ability to pass the gating will compound over multiple rounds and holds the potential to speedrun building inequality. Offering a choice allows program managers to own this decision and users can “vote with their feet”.

## Grant Eligibility

* Grant Eligibility and the larger question of verifying grantee reputation on an ongoing basis is one area within which there are huge automation opportunities
* The NLP based work already pioneered by FDD can be found [here](https://github.com/Fraud-Detection-and-Defense/CASM).
* For beta rounds, increased automation will be trialed and proactive as well as retroactive QA checks will be in place so that we can develop a way forward. Stay tuned!
* It is likely that a review protocol which incentivizes accurate reviews could cthange reviewer optimal strategy. If a user has a grant in 1/n rounds but is reviewing grants (Not for eligibility to a specific round, but validating individual attestations about a grant) then their likelihood of reviewing something relevant to themself is lower.
* We should push for separation of reviewing grants for possessing qualities and then matching those qualities to the rounds they are eligible for as this system scales better and creates better data for studies across ecosystems.
* A review protocol might find that holders of certain stamps might perform better at reviewing correctly. We looked into this with our Ethelo review experiment in Season14. The data can be found here.

## Decentralization

* In any situation where decisions must be made by the community, the decision can be made in the following ways: Delegated authority to an individual/committee OR a weighted input model.
* Weighted input models can represent the community. Our [reward modeling research](https://gov.gitcoin.co/t/gia-rewards-okr-report/10438) in season 13 shows that it is possible to find “minimum viable decentralization”. This is the number of reviewers needed to ensure the outcome is in alignment with the desire of the community provided an assumption of less than ⅓ bad actors. [Simulation Github](https://github.com/Fraud-Detection-and-Defense/rewards-system-model).
* All algorithmic and human decisions require an appeals process to maintain legitimacy. This is because there is always a potential for criteria being written in a way that multiple ways of reading it can both be considered reasonable. There are also situations where the external environment changes in a way that requires the community to reconsider previous decisions.
* Retroactive sybil discounting and any other algorithmic policy enforcement must be transparent and reproducible. As long as there is a functioning appeals process, the decisions can be made off-chain with an optimistic assumption which can be challenged.

# In Conclusion

We started with a belief that a high-resolution democracy should better incorporate the will of the governed. We no longer need to delegate authority to single points of failure, incompetency, or corruption. Instead, we can provide systems of minimum viable decentralization that truly capture the will of the participants.

This ended up being at odds with the structure of the DAO after the bear market brought us concerns around sustainability. The wartime DAO decided to lean in on efficiency. To minimize risk and to focus on delivering the most important thing - Allo protocol. Only upon delivering the Allo protocol have we found the truth behind what value Gitcoin is truly providing - a trusted way to use funding mechanisms which are susceptible to fraud.

A bear market pushed the DAO to move to sustainability mode and had us drop multiple important projects at FDD such as decentralizing the user and grant review processes. This is a problem because the promise is corruption free public goods funding, but when only one actor is delegated authority it provides a single point of failure. We had hoped to have this ready when the protocol was launched.

Choosing to not fund this work is understandable when you think of the protocol as the rails for public goods funding, but not when you think of it as ***corruption proof public goods funding.*** Hopefully, the launch of the protocol and new DevRel efforts will have the community innovating solutions to this and other similar challenges. Going forward, we’d advocate for the DAO to consider all the ways a grant program can be captured or corrupted.

The timing for FDD to wind down is perfect. The community is empowered by the protocol launch and they have the solution available for managing the sybil problem. Members of FDD moving into end-to-end accountable workstreams is already bringing data-first thinking to the product which we expect to provide incredible benefits.

***We hope that FDD is seen as a shining example of a graceful wind down of a workstream setting an example for all of web 3.*** 

We thank all the token holders, stewards, and DAO contributors who supported us.

Special thanks to Christine & Tigress for setting up & driving our operations respectively.
@ChrisDean @tigress 

A big shout out to our original multisig keyholders who took a chance early on.
@mzargham @akrtws @lefterisjp @tjayrush @bobjiang @octopus 

To all our contributors, core trusted and part time, THANK YOU. I can only tag 10 total so I'll stop here!

-------------------------

Kritikal_Eye | 2023-04-06 19:30:30 UTC | #2

HI Joe,

Thanks for this post.  It seems like it is your good way of framing your opinion of the FDD workstream legacy, and maybe positioning it for possible future Retroactive Rewards.

I am curious if you have anything you'd do differently if you could do it all over again?  Do you have any constructive criticism for yourself?

Id certainly feel more comfortable voting for retroactive rewards for FDD in the future knowing those answers.

(Posting this with a throwaway account because I am not comfortable doing it otherwise + anonymous accounts are not against the Forum Code of Conduct.  I hope that is okay!)

-------------------------

DisruptionJoe | 2023-04-07 16:26:45 UTC | #3

We have no intention of taking any future retroactive rewards. It's a good question though. I believe the current retroactive rewards round is setup to disqualify anyone who was paid by the DAO for their work. 

We do mention that we are keeping the FDD alive as a MolochDAO. This is because we have $22,500 coming from Aave upon completion of a project. Additionally, there is the possibility of future airdrops which we would hate to go to waste :grin:

[quote="Kritikal_Eye, post:2, topic:13852"]
I am curious if you have anything you’d do differently if you could do it all over again? Do you have any constructive criticism for yourself?
[/quote]

Yeah. A ton! Everything is a learning experience and there are few in my life I would do exactly the same. By no means were we perfect, but we did work hard and try to produce results. I think our results and transparency stand on their own. I don't feel regret as I allow myself grace to understand the difficulty of the position and to accept our successes. This is not to say I didn't learn immensely from the experience or that we didn't fail on some attempts. Do I want to go back in a time machine to do it differently - no. Will I take the lessons I've learned into my future endeavors - yes. 

We aren't leveraging this for future retroactive public goods funding - frpgf :joy: Therefore, I'm not sure what you would like to hear, but here it goes:

A few things I could have done better:
- **Organize FDD work in Github from day 1 rather than Notion** - We could have been more open and had community contributions from the start. We were scared that the attackers would see what we were doing and win. Now I know that with the open data on the protocol, our fraud defense can be "kerckhoff compliant". 
- **Hire better from day 1** - Our original model was to see how decentralized we could be while still hitting objectives. What the DAO saw as wasted spending, I saw as lessons in how to decentralize. The bear came along and this was no longer worth it and we had to run the workstream like a company department to survive. This had positive and negative effects. We were able to hire world class talent, but we also lost some world class passion. Its hard to let go of passionate people willing to work hard, but efficiency requires specialist and expertise. We could have skipped the first part if we knew the DAO wasn't interested in workstreams being autonomous. 
- **Better communication of the need for a review protocol** - I feel quite bad that we can't offer program managers better systems for review and appeal. Decentralized systems are only as strong as their weakest point and until these items are solved, we can't provide a corruption resistant guarantee. 
- **Focus more on personal development** - Sybil resistance is a gnarly problem and working on it was very captivating. I spent less time than I should have developing myself and my relationship with leaders around the DAO. Many people reported that they felt FDD worked in a silo. I felt that we rarely got responses from others. I didn't know how to respond to comments like "I don't have time to read this detailed report you put together. I feel like you're ddos the voters" next to "this doesn't tell me enough" and "I don't have the skills to understand this so I'm going to vote the way xxx person did". At a casual glance I can complain about the stewards, but in reality I have to accept that I did not work hard enough fostering relationships to support everything we wanted to get done. 

I'm sure I made a million other mistakes along the way. I hope my learnings help you understand my perspective and prepare for your future.

-------------------------

lee0007 | 2023-04-07 02:54:13 UTC | #4

Phenomenal undertaking, FDD delivered under your leadership @DisruptionJoe and imo the results see you recognised as world-class leaders in Sybil defence at Scale. Onwards & upwards :heart_on_fire:

-------------------------

ccerv1 | 2023-04-07 02:56:57 UTC | #5

I just wanted to share a brief note of appreciation to @DisruptionJoe plus all the current and former members of FDD for their contributions, their impact, and their graceful transition. I had the privilege of working with this group for one season: FDD was an exceptional collection of regens dedicated to preserving the integrity of quadratic funding and innovating with on-chain data. I'm excited to see what you all do next. Just remember to watch out for Cici!
:face_holding_back_tears: :green_heart: :raised_hands:

-------------------------

jengajojo | 2023-04-07 09:46:56 UTC | #6

Thank you @DisruptionJoe @tigress @omnianalytics @epowell101 and others for your fantastic contributions :fire:

-------------------------

epowell101 | 2023-04-08 13:49:36 UTC | #7

Just a quick note to say thank you to DisruptionJoe who took a chance on me - and has taught me an enormous amount about everything from Anti-Sybil approaches -> to DAO governance techniques -> to who is who in the wonderful Zoo that is regen web3.

This isn’t the end but just the beginning of the DAO we all love - Gitcoin - becoming more data savvy and of the broader ecosystem as well being able to protect themselves through the use of data & regen rangers.  Thank you DisruptionJoe 🫡❤️

-------------------------

ZER8 | 2023-04-11 21:18:28 UTC | #8

As a former member, team lead in FDD, but even more importantly as a person that was genuinely passionate about defending web3, public goods and also Gitcoin grants+ grantees this feels like the end of an era. I remember that last year in a call we were asked to describe what's happening in the DAO using one word and I chose "transformation"...it seems like the transformations will continue and at some point I'm sure equilibrium in Gitcoin will be reached :dart:

Everyone that worked in FDD and with Disruption Joe knows the level of leadership skills he posses, the iron nerves he has and the amount of work he put in to the FDD success(which translated into funds safu for the DAO and the grantees). :white_check_mark:

Speaking solely from the results POV I actually believe they could not have been better...stopping over $3 million dollars in fraud, developing algorithms, reviewing a HUGE volume of grants all while constantly coordinating with every WS, grant creator and all the parties involved in the grant program was a huge responsability and I'm certain that @DisruptionJoe was the perfect man for this job. As a bonus the FDD also created the ODC lead by @epowell101 which already has amazing results :shield:

**Honestly I don't think that this outcome is only FDDs fault,** as the DAO dynamics and also products constantly shifted and at times we even saw some competition over coordination. We can also involve some 101 evolutionary biology and see at this particular situation as an evolution, the dominant WS that posses leadership with more tokens delegated survived and absorbed talent from the other WS that did not. FDD strived to be have credible neutral results and also to be credible neutral and that could be seen as a mistake.

**I would like to thank all the contributors** that put in passion/work and strived to protect the Gitcoin rounds while ensuring credible neutral processes for the grants program. **Special thanks to DisruptionJoe for all your work and for the mentorship that you provided to everyone in the FDD and also the DAO as a whole**.  Best wishes to everyone and I hope to see you all in the web3 ecosystem :smiley_cat:

-------------------------

tkgshn | 2023-07-07 04:14:49 UTC | #9

@DisruptionJoe 
>We stopped over $3 million in fraud with unknown amounts deterred

how to estimate? if you have any resources to quantify, I'd like to see them. maybe it can show the Price-performance ratio for DeCartography.

https://gov.gitcoin.co/t/how-much-does-plural-qf-reduce-collusion-compared-to-normal-qf/15709/

-------------------------
