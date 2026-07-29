---
id: 12727
title: "[S17 Proposal] INTEGRATED Gitcoin Passport Budget Request"
slug: s17-proposal-integrated-gitcoin-passport-budget-request
category: governance-proposals
url: https://gov.gitcoin.co/t/s17-proposal-integrated-gitcoin-passport-budget-request/12727
created_at: 2023-01-31T00:25:11.208Z
last_posted_at: 2023-02-22T08:33:47.093Z
posts_count: 29
views: 5477
like_count: 53
---

# [S17 Proposal] INTEGRATED Gitcoin Passport Budget Request

<https://gov.gitcoin.co/t/s17-proposal-integrated-gitcoin-passport-budget-request/12727>
kyle | 2023-02-14 16:17:39 UTC | #1

# Gitcoin Passport S17 Workstream Budget Proposal

*edited Feb 14*

*Given February is halfway done, we reduced some of the DevRel budget and trued up to what we expect to actually spend in Feb. This reduced our total budget by just a bit.*

------
During Season 17, the GPC workstream (Gitcoin Product Collective) has decided to split into two workstreams: Gitcoin Allo which is focused on the continued development of our Grants protocol and stack, and Gitcoin Passport which is focused on our Passport protocol and stack. Splitting GPC into two workstreams will allow for a more "complete" team structure in the future. @kyle and @kevin.olsen will be workstream leads for this workstream.

Now that the protocols are both live, we feel we should construct each of the workstream teams to focus accordingly. In time, these two teams will run independent of each other. For S17, there will continue to be tight collaboration.

Gitcoin Passport is a billion dollar opportunity to create a truly sybil resistant web experience. We are increasingly of the opinion no one sybil solution will be enough, but we certainly have an opportunity to curb the vast majority of sybil attacks with Gitcoin Passport.


## Essential Intents

We are focused on a couple of the Essential Intents. Specifically the following two:
1) Protocol Adoption + Growth
2) Financial Sustainability

A case can probably be made that we are also focused on growing the Grants program as we will support Sybil prevention, but that is a secondary goal on our long arc roadmap.


## TL;DR

This season the Passport workstream is going to focus on the following outcomes:
1) Continue to grow the number of Passport holders, and the number of communities integrating with passport
2) Introduce and test at least one new scoring mechanism for other communities to consume
3) Create a first class developer experience for those integrating with passport (either in app or scoring), and drive the number of integrations up to 25

**Based on what we learned in Season 16**, we will continue to refine infrastructure, strengthen partnerships and take a more thoughtful approach to roadmap planning and feature development. We were just crushed by instability in upstream service providers and so we are making some infrastructure changes to prevent this from happening in the future. We are also going to ensure that we give users the ability to record their passport details on-chain, which will further help reduce the load on key components of our infrastructure.

We have had changes in our team composition in S16; we lost two team members (and had another go out on parental leave). As a result we will focus on building context and team cohesion while rallying around our two sided protocol (one side for passport holders and one side for those who seek to access passports).


> 💡For more context regarding our vision & the current state of the workstream, please refer to the [📄Notion page for Passport](https://www.notion.so/gitcoin/Passport-843e5bfda1ba44f7b9d2cd3cd7059911).

## Amount

Gitcoin Passport (GP) is requesting **281,538GTC = $492,691** for S17. We will be leaving all reserves with the Gitcoin Allo workstream, and as a result we are requesting the full amount of reserves be funded (full 60 days @ ~190k GTC). This means however that the Allo workstream should be requesting less GTC as they will have a relatively large reserve. 

A full breakdown of the budget can be found at the end of this post.

|Gitcoin Season|Season 15|Season 16|Season 17|
|---|---|---|---|
|Season Budget|$N/A|$N/A|$492,691|

*The amount of GTC requested and the value of the reserves will be adjusted based on the current market value at the time this proposal is moved to Tally using the lower of the current price or the 20 day moving average, whichever is lower.*


## Milestone Report for the past Season

**Legend**
🟢 Success / completed / shipped
🟡 Incomplete but will hit goal and/or priority changed for initial description
🔴 Incomplete, will not hit goal (see description for reasons why)
⚫️ Canceled (see description for reasons why)


|Initiative/Project|Always-on|Key Results|Value Delivered|
|---|---|---|---|
|Gitcoin Grants protocol is able to use Passport to programmatically identify donors as unique humans|NO|🟢 Passport used in Alpha Rounds|Analysis is needed to confirm the expected result (low fraud tax)|
|Passport has a productized set of scoring methods that meet the use cases of the majority of interested of communities|NO|🟢 Multiple scoring mechanisms developed with FDD|Scoring for alpha rounds, and scorer API|
|Passport and its components are verifiable on-chain so any dApp can integrate passport, verify, and trust the source of passports data/components|NO|🟡 the scoring API is live, passports on not on-chain (outside ceramic)|This has enabled programatic integration of our scoring service|
|Passport holders are able to easily navigate their passports to understand how it could be used across different communities (Research and Design output)|NO|🟡 We have had turn over on the Product Marketing and Product Management roles for Passport, this has slowed down our ability to make progress here|This will make advocates of Passport holders||


## Objectives and Key Results
S17 is going to bring a renewed focus on our product practice to ensure we are intentional in the items we are scoping and building. What this means is, we are going to try and get ahead of the feature development we would like to complete, scope those features on Github, and ensure they are appropriately described such that we can bounty some of that scope if we want to. Essentially, this is the first season where we want to build muscle around inviting outside contributors to help us build functionality that we see as valuable.

You can expect us to deliver on the following next season:
1) Improving the passport holder's user experience by bolstering the education in app and streamlining workflows for stamp verification. 
*(Milestone: Passport Holder User Experience)*
2) On chain passport data / scores. We have found developers want to access this data on chain, and not just through Ceramic.
*(Milestone: On-chain scoring)*
4) Continued infrastructure scaling to ensure we can handle the load of Gitcoin Grants Rounds :sweat_smile: 
*(Milestone: Scoring API Minimum Viable Product)*

We are eager to strengthen our partnership with DevRel and Product Marketing to relaunch Gitcoin Passport in February of this year (updated docs, updated marketing, more education, new website, etc.)

> [You can see some of the progress on the marketing front here](https://go.gitcoin.co/passport)
> (Huge thanks to MMM for leading this work!)

Though we are not defining this as a cmomitted objective, we will also be spending time expanding our GTC Staking use case, and improve that experience. We are seeing adoption of this utility and passport holders are using this as a means to increase their humanity score (for the Gitcoin Alpha Rounds). In time, we want to build out slashing capabilities to create a Sybil hunting microeconomy, thereby rewarding those helping us find and remove sybil actors.

### List of S17 Goals

|Initiative/Project|Always-on|Metrics|Expected Impact|
|---|---|---|---|
|**Protocol Adoption Growth**<br>Improve Passport Holder's User Experience|No|* Increase the number of average stamps a passport holders holds by 10% <br>* Reduce the time it takes to verify stamps by 25% |- Improved usability (especially on mobile)<br>- Improved sentiment of Passport <br>|
|**Protocol Adoption Growth**<br>Improve integratooooors experience|No|* Increase the number of devs integrating with Passport <br>* Improved sentiment of our documentation and developer experience |- Reduction in time required to integrate<br>- More creative and expansive use cases surfaced <br>|
|**Protocol Adoption Growth**<br>Develop a second scoring mechanism for integrators to select from|No|* Multiple scoring methods are used in App |- Diversified use cases for Passport|


## Budget Breakdown
We have broken the budget down by staffing, contracting, devrel, and opex as we feel like this gives fairly granular details into where the funding will be going. This does not currently show the cost for each initiative, but we hope to do this next season with the milestone based bounty work we may be doing.

We kept some budget for hackathons / contractor's work on scoring mechanisms, and also called out Dev Rel uniquely as we expect this to be an expense that **grows** for the DAO in the future. 

Finally, this budget grows slightly over the past season as we added another developer to bring the team to four FT devs (with a fifth on paternal leave right now). Once our developer who is on paternal leave returns, our extra engineer will move back to the Allo workstream. We are thankful for the coverage during the paternal leave.

Our New Multisig for funding the workstream is: [0x19E50fA5623895D5a2976693eaFF5C2F879510ed](https://app.safe.global/eth:0x19E50fA5623895D5a2976693eaFF5C2F879510ed/home) | the signers for this are: Kyle (kbw), Kevin Olsen, Michael, Janine, Annika)

### View: USD per Category

|Gitcoin Passport in USD||Feb|Mar|Apr|Total|
|---|---|---|---|---|---|
|Staffing||||||
||Passport Core Contributors|96,751|96,751|96,751|290,254|
||Passport Leadership / Ops|26,146|26,146|26,146|78,438|
||Severance|0|0|0|0|
|Total Staffing||122,897|122,897|122,897|368,691|
|Contracting||||||
||DevOps|3,000|3,000|3,000|9,000|
|Total Contracting||3,000|3,000|3,000|9,000|
|DevRel||||||
||Devl Rel|15,000|20,000|20,000|55,000|
||Hackathons & Bounties|5,000|5,000|5,000|15,000|
|Total DevRel||20,000|25,000|25,000|70,000|
|OpEx||||||
||Saas Fees (AWS, Datadog, fleek, etc.)|15,000|15,000|15,000|45,000|
|Total OpEx||15,000|15,000|15,000|45,000|
|||||||
|Total GPC Budgeted Spend||160,897|165,897|165,897|$492,691|
|60 Day Reserves|||||$328,428|
|S16 Treasury Balance|||||0|
|Total S17 Request|||||$821,119|


Thanks for the consideration.

-------------------------

shawn16400 | 2023-01-31 11:40:48 UTC | #2

Thanks @kyle 
Recall stewards, this is part one of two budgets coming budgets from GPC.  The next will be for the Grants Stack. 
Stewards who volunteered to review both: @griff @azeem @farque65 @bobjiang and @annika

-------------------------

azeem | 2023-01-31 16:12:37 UTC | #3

Looking forward to going through everything!

-------------------------

eugyal | 2023-01-31 18:32:22 UTC | #4

I'm excited about the future of Passport. Would love to see it being used across other platforms and DAOs in the future.

-------------------------

farque65 | 2023-02-01 18:24:03 UTC | #5

This draft looks very interesting. I also look forward to going through everything. It is great to see the initiative to Improve Passport Holder’s User Experience. That will definitely be a key step to accomplishing the essential intents. There are a fair bit of issues with the ceramic storage of passport. Have these been addressed? Is there a plan to offer other passport storage solutions?

-------------------------

J9leger | 2023-02-02 04:41:28 UTC | #6

I'm excited to see Passport break out into it's own workstream. I think it's an important protocol and it's critical to get this right this season. Passport was a headache for the Alpha rounds and I'm both disappointed in how it worked while at the same time really glad we had these alpha rounds to test it and know what needs to be done before launch. 

I'm excited to see a really strong team work on this for the season and supportive of the investment to make Passport successful.

-------------------------

kyle | 2023-02-02 21:16:11 UTC | #7

[quote="farque65, post:5, topic:12727"]
There are a fair bit of issues with the ceramic storage of passport
[/quote]

Yes! You can see details on this [Github Milestone](https://github.com/gitcoinco/passport/milestone/15). the tl;dr is that we are setting up a DB layer as our source of truth, and we will write to ceramic on the backend (to decentralize the data store), but we wont rely on ceramic for our front end experience.

[quote="farque65, post:5, topic:12727"]
Is there a plan to offer other passport storage solutions?
[/quote]
Yes! As part of this seasons budget are anticipating posting scores on chain as well. this will enable access via smart contracts directly :slight_smile:

-------------------------

michaelgreen06 | 2023-02-06 18:08:53 UTC | #8

I'm excited for the the passport team to take advantage of this massive opportunity of web3 ID! 

🤞 we can solve the problems we learned about in the Alpha rounds and have a super successful launch at ETHDenver and during the Beta rounds!

-------------------------

azeem | 2023-02-07 15:33:15 UTC | #9

Honestly, I can't wait for Passport to be it's own workstream. It's not only important to our own protocol, but for the web3 ecosystem as a whole. Everywhere I look people are looking to solve what we seem to have a first mover advantage on, and I'm excited to see this building block achieve success from our lego stack. On top of that, it'll be key to get right for what we're doing ourselves with the launch over the next few months.

I'm in support of this proposal.

-------------------------

bobjiang | 2023-02-08 01:28:23 UTC | #10

Thanks @kyle for your detailed budget request for S17!

I believe that the most important thing for Gitcoin Passport is the stability now.
It encountered the connectivity issues to Ceramic many times since live. (especially each grant round when the running load is high)

For the budget, is there a typo below?

**Total DevRel** line for Feb/Mar/Apr.

-------------------------

lefterisjp | 2023-02-08 11:02:40 UTC | #11

Hey. For this gitcoin budget season I will be following a different approach. I am not happy with how many things have been going in gitcoin and the way budget reviews work so I will either be abstaining or voting No in most budget reviews.

Despite the budget cuts I still think the DAO is burning too much money and it needs to become more lean.

I am more inclined to see development like this and allo get funded rather than other stuff.

-------------------------

kevin.olsen | 2023-02-08 11:57:53 UTC | #12

Good catch, the monthly subtotals aren't summing correctly but the season total is correct

-------------------------

griff | 2023-02-08 21:15:43 UTC | #13

![Screen Shot 2023-02-09 at 5.07.37 AM|690x46](upload://zpT1PodYdYfpvn12oTaImrnAir7.png)
I think these 5k's should be 20k's but that still doesnt fix the subtotals... oh well not important... the 512k number is accurate and the $854k number is accurate.

Is passport tasked with supporting the post round sybil analysis? 

I am not excited about such a huge spend on passport this quarter, would prefer a slower ramp up of the reserves.

That said I'm, in general, supportive of this proposal, but I want to ask every workstream... what would happen if this proposal didn't pass? 

Not fear mongering, just a practical reality. This post clearly explains what "yes" looks like... What would "No" look like?

-------------------------

kevin.olsen | 2023-02-09 17:01:07 UTC | #14

Hey Griff, thanks for the questions.

[quote="griff, post:13, topic:12727"]
Is passport tasked with supporting the post round sybil analysis?
[/quote]
Currently no, this work has lived in FDD, and the post round analysis is still up in the air where it will live in the new structures. I can see the benefit to having this happen here, or closer to the round operations work. Either way the post round analysis should be feeding back to product to ensure we enable the scaling of this work via software product development.

[quote="griff, post:13, topic:12727"]
I am not excited about such a huge spend on passport this quarter, would prefer a slower ramp up of the reserves.
[/quote]

This is the standard 60 reserve request, because this is a new workstream Passport has no reserves and is requesting the full amount (Allo has maintained the reserves from the former GPC and you'll see that reflected in the Allo budget request)

[quote="griff, post:13, topic:12727"]
That said I’m, in general, supportive of this proposal, but I want to ask every workstream… what would happen if this proposal didn’t pass?
[/quote]

Totally get it, and I posed the same thought experiment to FDD on their budget. For Passport, given there are no reserves, it would stop this workstream before it started — basically a no vote on splitting GPC and a no vote on thin workstreams. 

We haven't received any pushback from stewards on this split, so it's not a scenario we're seriously planning for. 

In the hypothetical where both budgets fail, we have less than 2 months' runway (having brought on the devrel expenses from PGF), and it would be a best effort to meet obligations as we close up shop. I imagine most contributors would be quite distracted lining up their next jobs, and we would expect very low output and high attrition. That would also leave Passport without operations or maintenance. The DAO would need to decide what to do with the Passport product, either shutting it down, finding and staffing a new team, or finding a 3rd party team that would want to take over the development and operations of Passport.

In the hypothetical scenario where the Allo budget passed, we could try to pull the workstreams back together. The Allo budget + Reserves could just cover both workstreams operations for the season. But would completely deplete GPC workstream reserves, leaving the re-unified workstream in a precarious position.

-------------------------

kyle | 2023-02-09 22:17:56 UTC | #15

[quote="griff, post:13, topic:12727"]
This post clearly explains what “yes” looks like… What would “No” look like?
[/quote]

I appreciate the question.

There are two options (likely more) that I could see:
1. We go back and see if we can make cuts in DevRel spend (this is planned hires) and reduce some of our contracted work (perhaps in dev ops). 
2. We look to cut headcount. We don't have much opportunity on the team to do this, but we can evaluate those actions if needed. As an FYI, the headcount is fixed and is slightly large, but we have a team member on parental leave, so we have and "extra" dev salary right now.

And finally, if we decided not to fund passport at all (even after some proposed cuts), we would mostly spin down development and likely need to lay off the team. Allo could maintain the hosting, but it would stay static for a while.

-------------------------

griff | 2023-02-10 08:52:19 UTC | #16

[quote="kevin.olsen, post:14, topic:12727"]
Either way the post round analysis should be feeding back to product to ensure we enable the scaling of this work via software product development.
[/quote]

I think as much work as possible should live in the product teams... especially since passport is the front end of sybil protection, and this post round analysis is the backend of the work, it seems tying these systems together under one team so the needs of each can feed back into each other. It seems that would be ideal.

On a side note, opening up donations to people without a valid passport at the end was a great call and I hope is a standard move. Let people donate and update their passport at the end of the round. Way better UX IMO. 

[quote="kevin.olsen, post:14, topic:12727"]
In the hypothetical where both budgets fail...
[/quote]

Thank you for giving me the full spectrum of the decision at hand. I know its a hard thing to discuss... but it really helps.

I guess part of why I am asking this question is to illustrate the issues with our current system of voting and how ill suited it is for the task at hand. 

Not sure of what the solution will look like next season, especially if DAOops doesn't pass... but I would love to help make a more functional system next quarter.

-------------------------

kevin.olsen | 2023-02-10 12:40:55 UTC | #17

[quote="griff, post:16, topic:12727"]
I think as much work as possible should live in the product teams… especially since passport is the front end of sybil protection, and this post round analysis is the backend of the work, it seems tying these systems together under one team so the needs of each can feed back into each other. It seems that would be ideal.
[/quote]

I like this suggestion a lot and see Passport similarly. I have seen a lot of conversations where Passport is mischaracterized as only the front-end prevention. In truth, it relies on the continuous observations and improvements offered by the back-end analysis, and bringing those together into a single workstream feels like a natural fit to me as well.

[quote="griff, post:16, topic:12727"]
On a side note, opening up donations to people without a valid passport at the end was a great call and I hope is a standard move. Let people donate and update their passport at the end of the round. Way better UX IMO.
[/quote]

Thanks. I agree with that as well!

[quote="griff, post:16, topic:12727"]
I would love to help make a more functional system next quarter.
[/quote]

I would love everyone's input on improving the experience of working across the Grants Stack, Allo,  and Passport ecosystem. I will take a minute to give a shoutout to the team that, after battling the instability with our ceramic node all round, were able to turn around a working re-architecture of Passport in less than a week to enable end-to-end stamp collection and scoring for the grace period.  Shout out to Gerald, Lucian, Tim, Chibie, Erich, and Kyle. Going forward, with this architecture, we expect to have much more predictable performance under load.

-------------------------

DisruptionJoe | 2023-02-12 19:00:50 UTC | #18

[quote="griff, post:16, topic:12727"]
I think as much work as possible should live in the product teams… especially since passport is the front end of sybil protection, and this post round analysis is the backend of the work, it seems tying these systems together under one team so the needs of each can feed back into each other. It seems that would be ideal.
[/quote]

I fully agree that as much of this as is possible should live in the product team, but there are two different functions happening here in the post round analysis. I believe one belongs with the product teams (Not only passport) and one belongs with the program. 

The product goal is to make iterative improvements so the product alone can offer a delightful and trustworthy experience. 

The program goal is to ensure that the program managers, including our own, are able to assess the issues that come up in a round and use analysis to ensure they get results that will continue their communities trust in the legitimacy and credible neutrality of the round. 

Here are a few things that might surprise people. I think the passports system of reputation attestation, gating, and a shared ETL layer for transparent algorithmic policy decisions which is needed for Projects and for Programs as well as identity. 

We've discussed this need for Projects in FDD as far back as Season 13. Recently, I've been hearing "Project Reputation that works like Passport" from the product team. I an HIGHLY certain we will need the same thing for Programs within a year. Two years max. 

However, when you ask the product team to solve a problem specific to each individual round, it crosses a known problem in working styles. Zargham is great at comparing the pace of work to its technical difficulty. The product teams don't work at the pace the program managers need to keep the trust of their community. That is what FDD has been doing this whole time. 

I suggest that a Fraud Analyst who is focused on the program managers gaining trust from their communities using our product should take a holistic view of the issues. They will look at GRANT FRAUD in addition to identity fraud. They will look at signals that combine the two. They will make recommendations to Product Managers to mitigate the current inadequacies of the products AND work with the product teams to retrospectively understand the issues which needed data analysis to mitigate. 

[quote="kevin.olsen, post:17, topic:12727"]
I like this suggestion a lot and see Passport similarly. I have seen a lot of conversations where Passport is mischaracterized as only the front-end prevention. In truth, it relies on the continuous observations and improvements offered by the back-end analysis, and bringing those together into a single workstream feels like a natural fit to me as well.
[/quote]

For the reasons above, I disagree with this. But I think I figured out why we aren't communicating this well. It is matrix of issues which confuses the situation. 

Yes, Passport relies on backend analysis to close the loop. Let's look at a happy path where Passport does in fact close the loop...

Should the Allo protocol be opinionated that preventative sybil defense is the only acceptable option? 

Should retroactive sybil discounting be applied using only the Passport stamps as signals? 

***Retroactive sybil discounting (squelching) requires other on-chain signals which may or may not be consented to, but are public data. This is because the other non-consented pieces of information are where we find the data delta between legitimate behaviors and illegitimate ones.*** 

Depending on how you answer these, we could place both Jobs To Be Done into Passport product:

Preventative Gating of Sybils & Retroactive Sybil Discounting (Squelching) 

However, these are two distinct JTBD that should both be OPTIONS from an unopinionated primative or protocol. And each has its own loop to close.

But neither addresses the work that moves at the speed of real-time mitigation. Without this, the Program Managers lose the TRUST of their communities. These communities then lose trust in GITCOIN. Communities want to be paid out ASAP after rounds. We usually take 3-4 weeks. Product teams shouldn't be trying to work at the pace of prioritized product development AND putting the fires out for specific rounds with real time analysis.  

Check out the specific section in [this article](https://medium.com/block-science/operationalizing-the-gitcoindao-anti-sybil-process-7f2595544f44) called "Clustering Workstream Modes & Frequencies in Decentralized Communities: The Socio-Technical Frequency Map" for more on the pacing issue. 

This is why I'm advocating for Passport to hire a Data Analyst/Scientist who works closely with a Data Analyst on the Allo team and a Fraud Analyst on the PGF Growth/Program team.


I'm willing to learn that I am wrong on this point. Strong opinion, held loosely. But I will take the bet that program reputation is a thing at this time next year!

-------------------------

annika | 2023-02-11 03:18:29 UTC | #19

I'm comparing this budget to the Allo budget and am struck by a couple figures:

**Top-line: Passport's $500K vs Allo's $800K**
I'm surprised Passport's budget is 5/8ths as big as Allo's given that Allo has a much bigger product scope; would expect Passport to come in as a smaller share of the total previously-GPC budget. How does this stack up vs. prior seasons in terms of breakdown, and do you guys imagine this breakdown stays roughly constant in future seasons?

**Devrel: Passport's $90K vs. Allo's $60K**
Similarly, I am surprised that Passport is requesting a bigger absolute devrel budget this quarter than Allo is -- since IMO, Devrel efforts should be overindexed on Allo rather than Passport. Why is Passport's Devrel request bigger?

Thanks!

-------------------------

kyle | 2023-02-14 03:26:04 UTC | #20

Thanks, Annika - great questions :)

[quote="annika, post:19, topic:12727"]
How does this stack up vs. prior seasons in terms of breakdown, and do you guys imagine this breakdown stays roughly constant in future seasons?
[/quote]

We have one FT contributor on parental leave, and are "borrowing" one eng from Allo. This will reset in April, and we will go back down in size. I expect the Passport team to stay lean and likely will have the budget decrease further once some of the dev rel projects are complete (more on that below).

[quote="annika, post:19, topic:12727"]
Why is Passport’s Devrel request bigger?
[/quote]

Passport is in full DevRel build out mode, with a planned "relaunch" at the end of Feb. This means, we have a few folks working on "getting started" guides, videos and sample applications. Allo is not yet ready for this type of support and development. They will be launching a public beta at EthDenver, and the full rounds will be run in April. I would expect our DevRel budget to drop at that time, and Allo to increase quite a bit to accommodate a similar build out.

It is highly likely we will not use all of the DevRel budget we are requesting, but we wanted to leave a bit of room for opportunistic collaborations.

I hope this helps! let me know if you have more questions or see areas you want us to adjust.

-------------------------

kyle | 2023-02-14 18:35:28 UTC | #21

As a heads up to folks - I moved this budget to Snapshot for vote!

Hoping for your support.

https://snapshot.org/#/gitcoindao.eth

-------------------------

linda | 2023-02-17 00:13:49 UTC | #22

I voted yes on this proposal. While the budget is higher than I would expect, I'm supportive of the DAO putting in the resources for a period of time to see what is possible with building out and improving Gitcoin Passport as I think there is a lot of potential and my past interactions with it indicated to me there was significant work to be done to improve the product / user experience.

-------------------------

GClayMiller | 2023-02-17 01:28:22 UTC | #23

Thanks for this breakdown Kyle, all very helpful. Makes sense to me that the Product Collective has broken up into Passport & Allo—I imagine this will increase efficiency and save costs over time.

How many engineers make up the Passport Core Contributors vs Leadership/Ops?

Are the 60 day reserves just 2 months of additional runway in case unexpected costs arise? Are they returned to the treasury if unspent or rollover to the next season?

Thank you!

-------------------------

kevin.olsen | 2023-02-17 14:11:25 UTC | #24


[quote="GClayMiller, post:23, topic:12727"]
How many engineers make up the Passport Core Contributors vs Leadership/Ops?
[/quote]
Currently the core Passport team is 5 engineers (one is out on parental leave), 1 PM, and 1 Designer. Leadership/Ops is a team of 3. 

[quote="GClayMiller, post:23, topic:12727"]
Are the 60 day reserves just 2 months of additional runway in case unexpected costs arise? Are they returned to the treasury if unspent or rollover to the next season?
[/quote]

Correct, unspent reserves roll over to the next season, and the following season we will only request the funds from treasury needed (i.e. expected operations + 60 day reserves - current reserves)

Thanks for your interest, hope that helps you evaluate your support for the budget!

-------------------------

lefterisjp | 2023-02-19 22:53:20 UTC | #25

Why is there not an abstain vote in the snapshot?

-------------------------

lefterisjp | 2023-02-20 14:15:13 UTC | #26

Anyway I intended to vote abstain to protest the high value, but since time is running out and I am probably not gonna have access to this key till it runs out I am voting a reluctant yes since I know that development is important (though imo too expensive)

-------------------------

kevin.olsen | 2023-02-20 16:32:06 UTC | #27

The Abstain option wasn't set up accidentally. It was an oversight when Kyle put it up on Snapshot.

I appreciate your position regarding cost and respect whatever decision you make regarding this proposal.

-------------------------

kyle | 2023-02-22 02:29:42 UTC | #28

Hey all - I wanted to offer some updates given this budget passed. 

I posted this to Tally and wanted to share an update on the amount given the price of GTC.

**Amount:**
Gitcoin Passport (GP) workstream is requesting 404,750GTC* for S17. We will be leaving all reserves with the Gitcoin Allo workstream, and as a result we are requesting the full amount of reserves be funded.

*The GTC total will be adjusted based on the current market value at the time this proposal is moved to Tally. In this post, we used a $1.98 conversion rate. The vote will request the $USD amount in GTC at the lower of the current price or the 20 day moving average.

Here is a link to the Tally post: https://www.tally.xyz/gov/gitcoin/proposal/46

Voting will go live in 48 hours.

-------------------------

shawn16400 | 2023-02-22 08:33:47 UTC | #29

This snapshot vote has passed with ~100% approval rate.
Metrics:
1289 unique votes
~8.2M GTC tokens cast.

To note, the number of GTC tokens cast was below average, likely because there was no "abstain" option included in this vote. 

Thanks to @griff, @azeem @farque65 @bobjiang and @annika for all the time they dedicated as volunteer steward reviewers of this budget.

https://snapshot.org/#/gitcoindao.eth/proposal/0xd87e0ae2a52d68860616dd21d4e0ddc552d672712d2e11a52e08a27213106108

-------------------------
