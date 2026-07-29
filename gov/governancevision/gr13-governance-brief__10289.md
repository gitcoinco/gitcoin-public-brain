---
id: 10289
title: "GR13 Governance Brief"
slug: gr13-governance-brief
category: governancevision
url: https://gov.gitcoin.co/t/gr13-governance-brief/10289
created_at: 2022-04-01T19:07:27.893Z
last_posted_at: 2022-04-04T17:19:43.546Z
posts_count: 4
views: 3680
like_count: 13
---

# GR13 Governance Brief

<https://gov.gitcoin.co/t/gr13-governance-brief/10289>
DisruptionJoe | 2022-04-02 00:46:53 UTC | #1


# GR13 Governance Brief

Grants Round 13 has been a monumental round for improving the community ownership, legitimacy, and credible neutrality of our systems. This post discusses how the Fraud Detection & Defense workstream (FDD) has worked to stay ahead in the red team versus blue team game. It also documents the decisions and reasons behind our subjective judgements. This workstream is tasked with minimizing the effect of these liabilities on the community.

# Sybil Defenders

## Sybil Detection Improvements

FDD is responsible for detecting & deterring potential sybil accounts. In the past we have done this using a semi-supervised reinforcement machine learning algorithm run by BlockScience. This season we transferred the ownership of the [Anti-Sybil Operationalized Process](https://medium.com/block-science/operationalizing-the-gitcoindao-anti-sybil-process-7f2595544f44) to FDD with contributors running it end-to-end.

During Season 13 we identified multiple new behaviors by the sybil attackers. Part of this was made possible by our Matrix squad. The squad developed a classification of all sybil behaviors and began to challenge assumptions held in the current process. Another effort helped us to understand the nuances behind the behaviors such as “airdrop farming” or “donation recycling”.

GR13 also saw the first run of our “community model”, a second algorithm built from scratch to test and improve the Blockscience built ASOP model. FDD intends to use the newly developed community model and the ASOP model in the future, potentially as an ensemble with the human evaluations.

The human evaluators, commonly referred to as “sybil hunters”, are key to the system. Not only do they help train the system while actively providing inputs, they also provide statistical validation for the model. [Humans-in-the-loop](https://medium.com/vsinghbisen/what-is-human-in-the-loop-machine-learning-why-how-used-in-ai-60c7b44eb2c0) (HITL) machine learning combined with rewards for evaluators allows us to decentralize the inputs to the system. This means the system “thinks” like the community, not the engineers that built it.

GR13 saw an increase in the number of human evaluations by 100% with the cost going down by 300%!

* GR10 - Core team does all evaluations
* GR11 = $1.25/eval | $1,750 for 1,400 evaluations by 8 contributors
  * First DAO led evaluations - Probably higher cost due to expert time from core team and SMEs for help
  * Fairly low quality, little training done
* GR12 = $4.39/eval | $26,350 for 6,000 evaluations by 25 contributors
  * Opened up participation to all GitcoinDAO contributors
  * First inter-reviewer reliability analysis to improve inputs
  * Focused on improving quality of data entering the system
  * Higher cost to get the inputs right and attract new people to participate
* GR13 = $1.42/eval | $17,050 for 12,000 evaluations by 37 contributors
  * Second time “sybil hunters” improve quality
  * Established systems for recruiting and executing
  * Focused on improving quality while lowering cost/eval
  * Brought out the meme culture in FDD

![|379x237](upload://jNd9rZo1UK8KH9zDUJsYGno0RV4.png)

## GR13 Sybil Incidence & Flagging

[Blockscience GR13 Statistical Review](https://hackmd.io/@bsci-gitcoin/SkdBF87Xc)

A total of 11.9% of the Gitcoin users making donation in GR13 were flagged during R13. The Sybil Incidence during this round is significantly lower than R12, with an estimate of being approximately 70% of it was before.

The Flagging Efficiency was 84% (lower boundary: 77% and upper boundary: 93%) which means that the combined process is under flagging sybils compared to what humans would do.

![|624x257](upload://tnyxZsoKZG96oNzVRMCEVFCiAaC.png)

Please note that some metrics are followed by a confidence interval in brackets, in keeping with statistical analysis practices.

GR13

* Estimated Sybil Incidence: 14.1% +/-1.3% (95% CI)
* Estimated # of Sybil Users: 2453 (between 2227 and 2680 w/ 95% CI)
* Number of Flagged Users: 2071
  * % of flags due to humans: 951
  * % of flags due to heuristics: 1067
  * % of flags due to algorithms: 53
* Total contributions flagged: TBD
* Estimated Flagging Per Incidence: 84%

GR12

* Estimated Sybil Incidence: 16.4% (between 14.5% and 18.3%)
* Number of Flagged Users: 8100 (27.9% of total)
  * % of flags due to humans: 19.4%
  * % of flags due to heuristics: 34.7%
  * % of flags due to algorithms: 49.2%
* Total contributions flagged: 115k (21.7% of total)
* Estimated Flagging Per Incidence: 170% (between 118% and 249%)

GR11

* Estimated Sybil Incidence: 6.4% (between 3.6% and 9.3%)
* Number of Flagged Users: 853 (5.3% of total)
  * % of flags due to humans: 46.1%
  * % of flags due to heuristics 14.3%
  * % of flags due to algorithms: 39.6%
* % of total contributions flagged: 29.3k (6.6% of total)
* Estimated Flagging Per Incidence: 83% (between 57% and 147%)

Compared to GR12, we saw a significant decrease in sybil movements. If we assume the $1.4 million in individual donations came from ½ the number of total donors which donated over $3 million in GR12, we still have a significant drop in sybil behavior.

According to human evaluation statistics, it has increased by a factor of 2.6x (between 1.6x and 5.0x). This was matched by a more than proportional response through flagged users, which seems to be “over efficient”. The interpretation of this is that the combo of using human evaluations, heuristics, squelches and algorithms is generating more flags than if we did flag the entire dataset of users using humans only.

## GR13 Sybil Detection Details

Gitcoin Grants sybil detection depends on three fundamental inputs: survey answers as provided by the human evaluator squads, Blockscience provided heuristics, and a ML model that uses the previous two pieces in order to fill in “scores” of how likely an user is or is not sybil. With those pieces available, it is possible to compute an “aggregate score” that decides if a user is sybil or not.

This aggregate score depends on a prioritization rule which works as follows:

1. Has a user been evaluated by a human? If yes, and if his score is 1.0 (is_sybil = True & confidence = high), then flag it. If the score is 0 or 0.2, then do not flag.
2. Else, has the user been evaluated by a heuristic? If yes, then simply use whenever score has been attributed
3. For all remaining users, use the flag as evaluated by the ML prediction score.

GR13 is the second time that we’re able to have an indirect proxy about how sybil incidence evolves during the round. We increased the number of human evaluations from 6,000 to 12,000. The estimated sybil incidence on each round is illustrated on the following figure.

![|624x257](upload://b6CsQdJMtZeU51znKSlp8Yuwjyz.png)

Notice the spike in human evaluators catching sybils during the fifth round. This may be a sign that the evaluators were learning from each other about a newly discovered behavior present in this round. The behavior included a video from user [Imeosgo](https://gitcoin.co/imeosgo).

[rss3空投数量可以查询了，我可以领几万块钱。去年领了好几个项目，几十万到手](https://www.youtube.com/watch?v=Md1yJtlw7m8&t=12s)

The user encourages people to create sybil accounts and donate to grants to receive airdrops. (Post on Airdrop Farming in the works!) This hypothesis is dually supported by traffic spikes from China during this timeframe as well.

While these anecdotes are intuitive, FDD will work to invalidate the hypothesis between rounds and use the information to continue improving Gitcoin’s fraud detection & defense effort..

# Grants Intelligence Agency

The GIA evolved from a couple of initiatives and workgroups within the FDD two months before GR13 began. It has four squads: Development, Review Quality, Policy and Rewards. The main goal of the GIA is to handle grant reviews and appeals. While executing on the current round is the primary goal, decentralizing and opening up our processes to the community is also of high importance.

.

Grant eligibility is handled by a collaboration of multiple working groups. They review new grant applications and any grants which are flagged by the community. The grant review process is also continually being decentralized. Feedback from the process feeds into the policy via an English common law method.

When the stewards ratify the round results, they are also approving the sanctions adjudicated by the FDD workstream.

Full transparency to the community* is available at:

* [Grant Approvals](https://www.notion.so/gitcoin/3940c8762a304e8c9630a05418ebd2a1?v=8fd78e98993e4dc29fd40a5b12a9ea75) - When new grant applications are received
* [Grant Disputes](https://www.notion.so/gitcoin/e79f1dd9e5074a1d986ee3f91b12943e?v=74372375b4ba42ebb269be219f2c452d) - When a grant is “flagged” by a user
* [Grant Appeals](https://www.notion.so/gitcoin/5627564cce204a0f8ae5af463873bb3d?v=2510b1a2634b4a0ea24cf2b81241d13a) - When a grant denied eligibility argues an incorrect judgment

*User Actions & Reviews is currently in “open review” allowing for select participation to stewards due to sensitive Personal Identifiable Information (PII) data and potential vulnerability to counter-attacks.

Additional transparency for all flags is provided at [@gitcoindisputes](https://twitter.com/GitcoinDisputes) Twitter.

## ![|317x294](upload://pXu4tDVbR3EG13bepv8KbaThu5u.jpeg)

FDD is dependent on the Gitcoin Holdings team for a few operational needs including some technical infrastructure, administrative access, and tagging of grants for inclusion in the eco & cause rounds. The coordination and communication between FDD | GIA, Gitcoin Holdings, PGF | Grants Operations squad, and DAOops | Support squad needs to continue to evolve and improve for matters related to grant eligibility.

## New Grant Application Review Process

Between GR12 and GR13, FDD shifted to an open grant review period beginning 1 month before the round and ending 1 week into it. The [Grant Review Quality](https://www.notion.so/gitcoin/FDD-Review-Quality-13445a7023bd481789ca1e314c145391) squad in FDD is responsible for ensuring that reviews are handled in a timely manner and that the reviews are of a high quality.

Before the round began the Grant Review Quality squad ensured that the grant application backlog was reviewed and all new grants were approved/denied before February 11th, 2022. During the round, the grant approvers hit their goal of approving grants in under 48 hours or less (except for the weekends).

Due to complications with getting data from Gitcoin Holdings we were unable to use our newly developed tool to help scale the grant review efforts. Luckily, FDD had approved a review quality budget which contained a “plan B” for grant reviews to use the previous system. (Which cost the DAO a significant amount!)

A birds eye view of the progress in grant reviews

* GR10 |
  * 3 Reviewers / NA cost
  * First time using outside reviewers
  * FDD did not have a budget yet! Volunteer help.
* GR11 | 7 Reviewers / $10,000
  * Opened up to the community even more
  * Multiple payments models tested
* GR12 | 8 Reviewers / $14,133 (1 approver - Joe)
  * Experimented with two grant review squads
  * Recruited more community members and started to focus on quality
* GR13 | $5.38 cost per review & 2.3 average reviews per grant
  * 2,300 Reviews / 1000 Grants (Duplication error made this an estimate)
  * 7 Reviewers / $12,380 (2 approvers -Joe, Zer8)
  * The main focus was balancing between high quality reviews and number of reviews
  * Working towards Ethelo integration, senior grant reviewers => Trusted seed reviewers



The experiment run in GR12 using Ethelo for the Grant Disputes not only provided the same outcomes as the former review process, it garnered 53 reviewers in 7 days. Of the reviewers to use the system, 65% reviewed all of the grants presented. All this for the reward of a POAP! By using the Ethelo system in the future, a cost savings is likely.

## Grants Disputes & Appeals

The policy squad exists to create and maintain policies affecting platform use and grant round participation. They set definitions based on reviewer feedback and advise on judgements for flags, disputes, appeals, and sanctions during the round.

During GR13, a discussion on the governance forum included analysis and recommendations for a grant eligibility policy change triggered by the [BrightID appeal](https://gitcoin.notion.site/BrightID-191-87bafad66140414ebf235f85ecb771e6). This discussion found the need for policy to be an iterative process informed by the public goods workstream and the community as well as FDD. Should Gitcoin model its authority like English common law? What alternatives exist?

The outcome of the BrightID appeal was found using a well thought-out process which needed more education and validation from the community to execute. This is the process we had recommended prior to BrightID being the first appeal to make it to the level of needing to change a policy!

![|435x251](upload://527N0ZWDH20dYS5w6xYsHdIKQCk.png)

However, the collaboration between FDD & PGF Grants Ops showed us that the snapshot vote was unnecessary at this level. The process ended up playing out in these steps:

1. BrightID submits their request for appeal
2. The FDD source council hears the case as an appellate judge would to determine if the appeal has merit. In this case, they found it to be a [novel situation](https://gov.gitcoin.co/t/proposal-grants-policy-update-projects-with-tokens/10125).
3. The appeal was then posted to the governance forum for discussion. The FDD recommended a steward vote for legitimacy of the process, but the post did not get 5 stewards commenting in approval of moving it to a vote.
4. FDD then went with its judgment and reactivated the grant. (Technically, the grant was reactivated before the round to participate rather than “being in jail while awaiting trial.)

The first appeal to require a policy shift produced deep discussion & general agreement about how the dao should process appeals and found ways to increase the decentralization of the entire process. The real question was which appeals should reach a Steward vote, and which can be disposed of by (currently) the FDD or a decentralized group?

While the policy change suggestion did not proceed to a Snapshot vote it resulted in progress for Gitcoin. It also involved suggestions of market cap limitation for projects with governance tokens whereas presently, projects with tokens get denied. The policy change itself was deferred to a time after the grant round.

Gitcoin Grants policy is currently held on a “living document” which can be found on the new Knowledge base which was recently installed at support.gitcoin.co. This new open source Gitbook instance, which is maintained by the support squad, replaces the previous closed source Happyfox knowledge base.

# FDD Statement on GR13

The sybil attacks slowed down this round, but they are not stopping. They are evolving new and more complex tactics which require FDD’s best effort to defend. Last round we commented on our dependence on Gitcoin Holdings to supply new sources of data outside of what we are whitelisted to access.

FDD requires an appropriate level of data access to quickly respond to new red team strategies. The blue team is at a significant disadvantage when we must wait months to get approval to access the data needed to defend against new styles and classes of attack.

Simply getting the publicly available data about grants to integrate into our review software took the entire time between GR12 and GR13 due to legal concerns. The issue was finally solved for us on 3/11, two days after the start of GR13. We could have redirected the current integration which sends information to Notion. (Not to mention we lost the testing opportunity and all the learning we would have gotten by using the fully operational software which only needed the integration to avoid manual inputting of the data. This issue cost the DAO around $10-15k.)

We currently have two open data requests which have both been open for over a month. How is the Fraud Detection & Defense workstream supposed to function properly when we cannot access data in a dynamic way which allows us to respond to new behaviors?

We again encourage Gitcoin Holdings to make ALL data that isn’t legally protected available to the FDD workstream. Our data storage layer squad can work with Gitcoin Holdings engineering to set up a warehouse with proper roles and permissioning for DAO contributors and the public. Please help us to innovate further and faster.

[Disruption Joe](https://twitter.com/disruptionjoe), FDD Workstream Lead

-------------------------

owocki | 2022-04-03 23:49:52 UTC | #2

OOoh Sybil report day! woo hoo. :christmas_tree: 


[quote="DisruptionJoe, post:1, topic:10289"]
Estimated Sybil Incidence: 14.1% +/-1.3% (95% CI)
[/quote]

what is the numerator / demoninator here?  is this on a per-user basis? or per-contribution basis?

interesting that the number is not that far down between GR12/GR13 given the new bot protections.  i wonder if most of the sybil attackers or automated or not.

[quote="DisruptionJoe, post:1, topic:10289"]
[rss3空投数量可以查询了，我可以领几万块钱。去年领了好几个项目，几十万到手](https://www.youtube.com/watch?v=Md1yJtlw7m8&t=12s)
[/quote]

its interesting when videos like this get leaked to FDD.  i think that game theoretically, videos like this will always get leaked to FDD.  

here's why: Because quadratic funding requires the largest number of contributors possible to get the highest matching, black hats will try to create sybil accounts at scale by scaling their comms, and in the inevitably large population that consumes those videos, someone is likely to tip off the FDD.


[quote="DisruptionJoe, post:1, topic:10289"]
They are evolving new and more complex tactics which require FDD’s best effort to defend.
[/quote]

what is the policy on disclosure of said tactics?  is there transparency with stewards about them?  i suppose yall dont want to be public about what they are to avoid tipping off attackoooorrrs?

[quote="DisruptionJoe, post:1, topic:10289"]
The coordination and communication between FDD | GIA, Gitcoin Holdings, PGF | Grants Operations squad, and DAOops | Support squad needs to continue to evolve and improve for matters related to grant eligibility.
[/quote]

ACK - donno what all can be done (and how) while Grants 1.0 is in maintenance mode, but happy to take a look.

> The blue team is at a significant disadvantage when we must wait months to get approval to access the data needed to defend against new styles and classes of attack.

ACK - lets work together on this. 

> Simply getting the publicly available data about grants to integrate into our review software took the entire time between GR12 and GR13 due to legal concerns.

I'm not sure this is entirely accurate.  Lets get on the same page here. 

GR12 ended in mid-December 2021.   FDD first made the GPG (Gitcoin Product Group) aware of the technical needs to integrate Ethelo in [late Jan](https://discord.com/channels/562828676480237578/916079015280926790/936348899168370718).   You [first requested a legal engagement for](https://discord.com/channels/562828676480237578/941434914409185300/941435166621040710) Holdings to integrate with Ethelo in mid February 2022.

Let me know if I am mistaken about these days. I searched my Discord & gmail, but may have missed something!

> We currently have two open data requests which have both been open for over a month. How is the Fraud Detection & Defense workstream supposed to function properly when we cannot access data in a dynamic way which allows us to respond to new behaviors?

As you noted, the data requests were opened a month ago - in early late February / March during a code freeze & right before GR13 started and were open during the busy period during the round.

I advise that FDD revisit the expectation that Holdings can provide access at the last minute (right before a round).  I want to remind everyone that 
1. the GPG has put Grants 1.0 into maintenance mode.  There is not much work being done beyond KTL (Keep the Lights On) work, and focus has shifted to Grants 2.0 (which will not have these data access issues because its decentralized!).
2. the legal team (just 1 person) is rather preoccupied with a (somewhat complicated) (1) international Foundation asset transfer + (2) the KERNEL spinout + (3)an ever-changing regulatory environment.

because of this, the resources to sort through multiple data requests (each of which carry massive data privacy liability risks) are not always ready to respond to the FDDs requests in a timely matter.

I also want to name a miscommunication between the groups. When the Holdings company gave access to BlockScience/FDD back in late 2021, I was told that BlockScience was managing the dataset + making it available (in a privacy preserving way) to community contributors. It does not seem like that function has been maintained or migrated to the FDD.  Are there plans to migrate that function to the FDD? It was not made clear to us that the FDD was treating Holdings as the source of truth for data requests and therefore would require multiple more data connection requests to Holdings for different projects over time (at present, it seems like multiple per quarter).  Given the Ethelo request in Q1 2022, and now your two new data requests in Q2 2022, I think an adjustment in expectations is in order.  

I have massive empathy for the FDD's need for data, but I dont know that Holdings can always accomodate them under current circumstances.

Here is what I'd suggest:
1. Holdings can agree to a SLA in which data requests are responded to within a certain time period.
2. We set up expectations of what a "work request" looks like between the two orgs.

In exchange, I hope to see FDD take further ownership of their own outcomes - I think that means three things
1. at least 1 quarter advance notice
 - and/or - 
2. FDD takes the brunt of the product/engineering work (a well-tested PR to gitcoinco/web comes with the request)
3. FDD takes the brunt of the legal work (a legal structure that minimizes risk for Holdings)
- and/or -
4. We enable FDD to stand on it's own two feet, without Holdings. This means either waiting for Grants 2.0 or enabling it for Grants 1.0 by FDD creating a "all for one, one for all" datawarehouse that has scrubbed any PII in it, so it can service its own data requests.

Let me know what you think of this proposal.

---

I'm glad to see the progress the FDD has made on sybil data detection & scaling its resources and I dont want that to be overshadowed by my attempt to clarity some things & draw some boundaries above.  Glad we can have these discussions constructively and respectfully, this is what decentralized governance is I think.

-------------------------

bobjiang | 2022-04-02 05:48:32 UTC | #3

I believe we need a close coordinations in these teams including product team. 
E.g we could have a weekly sync call 1 month before GR14.

[quote="DisruptionJoe, post:1, topic:10289"]
The coordination and communication between FDD | GIA, Gitcoin Holdings, PGF | Grants Operations squad, and DAOops | Support squad needs to continue to evolve and improve for matters related to grant eligibility.
[/quote]

New knowledge base site is live now.
[quote="DisruptionJoe, post:1, topic:10289"]
[support.gitcoin.co](http://support.gitcoin.co).
[/quote]


Last but not least, about the grant status according with Grant policy, I have some suggestions, will create a separate post for it.

-------------------------

DisruptionJoe | 2022-04-04 17:19:43 UTC | #4

[quote="owocki, post:2, topic:10289"]
i wonder if most of the sybil attackers or automated or not.
[/quote]

Intuitively, I would say the answer is no. I believe the largest known class of sybil attack is "airdrop farming". Working on a gov post to release next week about this behavior. In short, we are currently making this behavior trigger an account to be ineligible for matching funds if the ml identifies the account as sybil as opposed to simply a new account. 

A big question remains concerning the connection of a grant owner to media/influencers convincing followers to airdrop farm as a sybil attack. 

[quote="owocki, post:2, topic:10289"]
what is the numerator / demoninator here? is this on a per-user basis? or per-contribution basis?
[/quote]

This is sybil users / unique users to contribute in GR13. 

[quote="owocki, post:2, topic:10289"]
what is the policy on disclosure of said tactics? is there transparency with stewards about them? i suppose yall dont want to be public about what they are to avoid tipping off attackoooorrrs?
[/quote]

Right now we are considering our methods to be "open review". Any steward can contact me for a walkthrough of our system, but I believe this will also require nomination by at least one person from the steward council to prevent a malicious actor from becoming a steward via GTC holdings and gaining access to sensitive info. 

[quote="owocki, post:2, topic:10289"]
ACK - lets work together on this.
[/quote]

It is getting better thanks to Engineering and Legal leadership engaging more on the topic. Some of the questions are just difficult though, so this is less blame and more awareness in intention. 

[quote="owocki, post:2, topic:10289"]
FDD first made the GPG (Gitcoin Product Group) aware of the technical needs to integrate Ethelo in [late Jan ](https://discord.com/channels/562828676480237578/916079015280926790/936348899168370718). You [first requested a legal engagement for](https://discord.com/channels/562828676480237578/941434914409185300/941435166621040710) Holdings to integrate with Ethelo in mid February 2022.

Let me know if I am mistaken about these days. I searched my Discord & gmail, but may have missed something!
[/quote]

I believe in Jan was when you were added to conversations. The discussions absolutely started during GR12 as we manually input the data for our test run on disputes. 

In January, we picked up the thread again as we set our Season 13 outcomes and began to work on them. This is when we began very actively pursuing the outcome. 

[quote="owocki, post:2, topic:10289"]
in early late February / March during a code freeze & right before GR13 started and were open during the busy period during the round.
[/quote]

This is when a more aggressive push for the access happened due to outcome ownership being assigned within FDD for Season 13. Access to more data, specifically having gitcoin holdings make all data available which is not PII be available to FDD has been a request since before FDD officially started in August 2021. 

[quote="owocki, post:2, topic:10289"]
the GPG has put Grants 1.0 into maintenance mode. There is not much work being done beyond KTL (Keep the Lights On) work, and focus has shifted to Grants 2.0 (which will not have these data access issues because its decentralized!).
[/quote]

Nate, Lindsey, and Kevin Olsen have been great about communicating what is happening with this transition and including us in their discovery. 

[quote="owocki, post:2, topic:10289"]
1. the legal team (just 1 person) is rather preoccupied with a (somewhat complicated) (1) international Foundation asset transfer + (2) the KERNEL spinout + (3)an ever-changing regulatory environment.

because of this, the resources to sort through multiple data requests (each of which carry massive data privacy liability risks) are not always ready to respond to the FDDs requests in a timely matter.
[/quote]

This would also fall under the desire to share because of awareness rather than blame. I am pushing for it because our workstream depends on this data access. I'm guessing MMM and Grants Ops will begin pushing for this priortity as well due to their need for realtime data to make good decisions. 

[quote="owocki, post:2, topic:10289"]
I also want to name a miscommunication between the groups. When the Holdings company gave access to BlockScience/FDD back in late 2021, I was told that BlockScience was managing the dataset + making it available (in a privacy preserving way) to community contributors. It does not seem like that function has been maintained or migrated to the FDD. Are there plans to migrate that function to the FDD?
[/quote]

Blockscience did indeed transfer the knowledge, code, and processes for this. What they couldn't transfer is the access tokens assigned to them with an NDA contract wherein they shouldn't share it with FDD contributors, therefore we needed a new one of our own to access the same data. We also ran into issues around the VPN requirements (whitelisting) and the addition of DevOps to Gitcoin Holdings and the DAO taking longer than planned. There were also rate limiting issues. 

Metabase is not a sufficient tool for real-time data analysis of the type we do. Many times our data requests would simply save the DAO money as it takes contributor time to scrape and piece together data which could be shared in a more efficient (and accurate) way. 

[quote="owocki, post:2, topic:10289"]
FDD takes the brunt of the product/engineering work (a well-tested PR to gitcoinco/web comes with the request)
[/quote]

We provided the code for the ethelo data request and it still took a couple more weeks for the legal side. I think this request is very reasonable though. 

[quote="owocki, post:2, topic:10289"]
We enable FDD to stand on it’s own two feet, without Holdings. This means either waiting for Grants 2.0 or enabling it for Grants 1.0 by FDD creating a “all for one, one for all” datawarehouse that has scrubbed any PII in it, so it can service its own data requests.
[/quote]

Our Data Storage Layer squad has shared the [architecture and process plans](https://docs.google.com/presentation/d/1cnmIG7TSM8qfK23ebtI16psTZNtEVSocMtQxCwS6Tso/edit?usp=sharing) for this and built the portion of the system we can. 

I do think this solution is best because of the need for data analysts to "tinker" with the data to find the insights with significant meaning. It is difficult to make a perfect request for exactly the data you need. 

[quote="owocki, post:2, topic:10289"]
I’m glad to see the progress the FDD has made on sybil data detection & scaling its resources and I dont want that to be overshadowed by my attempt to clarity some things & draw some boundaries above. Glad we can have these discussions constructively and respectfully, this is what decentralized governance is I think.
[/quote]

I appreciate the discussion.

-------------------------
