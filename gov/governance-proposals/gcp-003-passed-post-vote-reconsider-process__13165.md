---
id: 13165
title: "[GCP-003] - PASSED - Post-vote “reconsider” process"
slug: gcp-003-passed-post-vote-reconsider-process
category: governance-proposals
url: https://gov.gitcoin.co/t/gcp-003-passed-post-vote-reconsider-process/13165
created_at: 2023-03-04T19:22:04.485Z
last_posted_at: 2023-03-20T00:36:20.674Z
posts_count: 29
views: 6367
like_count: 70
---

# [GCP-003] - PASSED - Post-vote “reconsider” process

<https://gov.gitcoin.co/t/gcp-003-passed-post-vote-reconsider-process/13165>
shawn16400 | 2023-03-20 00:35:33 UTC | #1

Title: [GCP-003] - Post-vote “reconsider” process

**Author(s):** Shawn16400, Gitcoin Steward Council, 

**Summary:**

This proposal creates a mechanism for appealing a decision that has been ratified via the Gitcoin Governance process. This process is intended to be used sparingly and is not designed to be an alternative litigation process for dissatisfied users of the governance process.

**Abstract:**

This mechanism is designed as a stop-gap measure in cases where there is a material change in information around a vote that could have changed the outcome of a vote had that information been known prior to the vote being cast. A suitable example of a case to reconsider a vote would be if there is new information that, if known prior to the vote, might have changed the outcome of the vote.

To note, this process is designed for situations where any new material information is brought to light, or there is a significant environmental change. In the case of new information being brought to light, it does not pass judgment on if the new information was asymmetrically unavailable (information was withheld, obfuscated, or omitted) or if new information was previously unknown and has recently been discovered.

**Motivation:**

The web3 space changes rapidly and good governance processes protect against the implementation of bad choices, but it also needs to be flexible enough to rapidly adjust as new information as it is made available. Without a controlled process in place, the DAO is at risk for being forced to implement outdated decisions, move in an uncoordinated fashion, or make inappropriate or unauthorized declarations in order to repeal decisions in a way that might cause the entire governance process to be called into question.

**Specifications:**

This outlines the order of operations that the DAO might expect to encounter. This process is designed to be light enough to flex with changing circumstances, yet give enough direction to guide a just process in relation to decision makers and decision flow.

*A typical case:*

1. The case at issue is related to a vote which has recently closed

2. New or previously unknown information is made public in relation to the vote, or there has been a significant change in the environment (ex: drastic change in BTC/GTC price)

3. A call to "reconsider the vote" is raised by a current CSDO member **to** the Steward Council

* The call to “reconsider the vote” must be brought by a CSDO member who 1) cast a vote in the election in question AND 2) whose vote was aligned with the outcome of the election.
> * Example 1: if the vote failed, a member of CSDO who specifically voted **against** the proposal must raise the question to the Steward Council
> * Example 2: If the vote passed, a member of CSDO who specifically voted **for** the proposal must raise the question to the Steward Council

4. Ideally, the situation is discussed in the next CSDO meeting, but this is not required.

5. The subject is added to the next Steward Council meeting for discussion and decision.

6. The Steward Council support team will invite the appropriate parties to the meeting.

7. After discussing the issue, there can be one of two outcomes from the Steward Council:

* A. If the Steward Council votes in the affirmative to "reconsider the vote", then the Steward Council makes the decision known and the original vote is null and void. The proposal can be brought back for a revote by the original proposer following the standard governance process. The proposal may be the same or amended as per the preferences of the proposer. If the proposal is not brought by the original proposer within 7 days, the original vote is considered null and void.

* B. If the Steward Council does not motion to "reconsider the vote", or if a motion to "reconsider the vote" fails a majority vote, the original vote stands and must be executed as originally passed.

**Benefits:**

* This proposal allows for the coordinated reconsideration of proposal

* This process establishes a higher bar for reconsideration as to avoid the relitigation by the disaffected voters of the proposal.

* This process protects the DAO from activist voters who attempt to use the governance process as a method to circumvent the educated will of the voters.

* This process is not novel. It is a reapplication of Robert's Rules of Order NR which has been robustly tested in parliamentary procedure.

**Drawbacks:**

Core to the governance process is belief the process is just and efficient. Continuous reconsidering of proposals opens the process for misuse, abuse and can erode confidence in the governance process. These cases should be carefully considered before raising a motion to reconsider:

* This process should only be used when new information is made public, or there is a significant environmental change.

* The process should not be used to relitigate righteous votes

**Vote:**

YES: Implement the reconsideration process as outlined

NO: Do not implement the reconsideration process as outlined

-------------------------

alif313 | 2023-03-05 04:39:56 UTC | #2

Its very good, i think this make a big proposal project

-------------------------

shawn16400 | 2023-03-06 15:18:57 UTC | #3

Picking comments up here from the FDD thread:
https://gov.gitcoin.co/t/s17-proposal-integrated-fdd-budget-request/12738/44?u=shawn16400 

[quote="DisruptionJoe, post:44, topic:12738"]
This is really great work. One suggestion: CSDO doesn’t have any legitimacy in this context. The steward council would serve as a better appellate court because their legitimacy comes from the token holders.
[/quote]

I agree there are two options here for this review, CSDO and the Steward Council and both have advantages and disadvantages.  Lets hit the highlights:

CSDO has greater history, it has better internal context, and is likely to continue for the foreseeable future.  However, it is not an elected body, it is comprised of Gitcoin insiders, and the CSDO charters states that its decision space includes "DAO-wide governing agreements (except what’s passed to Snapshot vote)".  ([link](https://gov.gitcoin.co/t/csdo-charter-v1/12490))

The Steward Council includes independent external-to-Gitcoin members, it is an elected + appointed body, it include executive thinkers from outside Gitcoin, and it includes some of the highest context members internal to Gitcoin.  However, the Steward Council is a new experiment, the effectiveness of the body has not yet to be proven, and it was setup up as an advisory body without decision rights.  ([link](https://gov.gitcoin.co/t/proposal-v2-of-the-steward-council/11639))

As a governance thinker, I am ok with either body acting as a stop-gap measure knowing it is the voters who will decide the ultimate outcome.  Over time, if the Steward Council experiment proves resilient, moving this kind of case to the that body would seem like a normal maturation. 

[quote="DisruptionJoe, post:44, topic:12738"]
Our governance says that a snapshot vote is final. If you look at Uniswap, 100% of their snapshot votes are enacted on Tally. Do we want to be the ones to change this precedent for the ecosystem based on a few posts on the forum rather than a legitimate process? How do we remain leaders in legitimacy after that?
[/quote]

We would not be the first DAO to enact a stopgap measure between on and off chain voting.  Maker for example has a "cooling off period" post-vote in which time a stop to a vote could be triggered by a whale or collection of whales. Their process requires the  burning of MKR and to my knowledge has never been used, but it exists. 

This being said, legitimacy is derived from 1) having a defined process 2) following that process dispassionately and 3) changing / ratifying a process when the need presents itself.  This proposal attempts to do just that.

-------------------------

kyle | 2023-03-06 18:29:32 UTC | #4

Thanks, Shawn for proposing this.

It does feel like the highest context body (CSDO) are likely the most informed when it comes to budgetary matters for workstreams. However, if a general GCP was put to vote and then contested, I am less sure CSDO is the right body to contest.

Here are a few examples:
1 - Workstream Z works in conjunction with other workstreams to propose a budget. Information materially changes, or new information is surfaced (a key person leaves the workstream, the use of funds in previous season was inaccurately reported, etc.), CSDO will likely be the body that best understands the impact and can request workstream Z reconsider.
2 - A GCP to fund a partnership with another team/DAO passes. Information materially changes or new info is presented. In this case, CSDO is directly impacted by the proposal as it outside the workstreams. Although a CSDO member may have been involved in the original proposal, it should not be a proposal that directly impacts their work. As a result, the Steward Council may have as much context as CSDO and could serve as an appellate board.

I wonder if we want to spell out this type of nuance in the "reconsider" steps of our governance?

-------------------------

jengajojo | 2023-03-07 09:21:45 UTC | #5

If the need to reconsider a vote has emerged, then the follow assumption 

[quote="shawn16400, post:1, topic:13165"]
governance process is belief the process is just and efficient
[/quote]

has be violated as you point out. In this case, an internal body does not have sufficient legitimacy to make decisions which is why an appeal is called out in the first place. In such case I would suggest the case either goes to a specialist dispute resolution body like Ombuds or an external group such as [Kleros](https://kleros.io/)

-------------------------

shawn16400 | 2023-03-07 09:54:27 UTC | #6

[quote="jengajojo, post:5, topic:13165"]
In this case, an internal body does not have sufficient legitimacy to make decisions which is why an appeal is called out in the first place.
[/quote]

Thanks @jengajojo for the comment and reminders.  A solid process is case independent and it is good practice to segregate an incident from governance design, but to confirm that the invented process will work for that case, as well as others.  I do agree that an internal body left to itself to make a final decision would be a centralization step too far.  Recall that in this proposed solution, we are looking for the Gitcoin Stewards (voters) to make a final choice.

[quote="jengajojo, post:5, topic:13165"]
specialist dispute resolution body like Ombuds or an external group such as [Kleros](https://kleros.io/)
[/quote]

I did look at Klerios as a solution and even purchased 5000 PNK to participate in the courts, but I did not see sufficient evidence that their process would be appropriate for our volume.  Should the volume of "reconsiderations" at Gitcoin increase to a meaningful level, we may have to look at other solutions, but given Governance has a habit of unchecked expansion, I strive to keep processes as light as possible.

However, if there is sufficient support for an alternate path from Stewards, I open to investigating further.

-------------------------

shawn16400 | 2023-03-07 10:33:36 UTC | #7

Hey Kyle, I suspect that over time the right place for these kind of issues would be the Steward Council given it does have a measure of impartiality and it includes both internal and external resources.  However given the Steward Council is in its first elected season and the efficacy of the council has not been proven (vs. the cost), it may be premature to assign this to the Steward Council.  If the council is not renewed in three months due to a poor ROI, we would have a gap.  

To your point, we could design a process that could steer decisions to one body vs. another depending on the type, but I might suggest we take that step if the volume "reconsiderations" proves problematic. 

Regardless, this is what I would describe as a "happy problem".  Gitcoin has two possible options for this kind of process where many orgs would scramble to come up with one legitimate body.  And in either case, if the decision is made to reconsider a vote, the token holders own the ultimate decision.

But, as there are opinions on this on both sides, there are pros & cons for both sides, let's do the democratic thing and get a sense from those following this discussion.  

[poll type=regular results=on_vote chartType=bar]
# Which body should decide if Gitcoin holds a "reconsider" vote
* The CSDO team should be the body to "reconsider"
* The Steward Council should be the body to "reconsider"
* Neither should be the body to "reconsider"
[/poll]

-------------------------

annika | 2023-03-07 19:33:01 UTC | #8

I agree with the nuance @kyle puts forth in that we may want to have separate "reconsider" bodies depending on the type of vote (i.e., some stuff might be better for CSDO, other stuff for SC).

Not to open up a whole new can of worms, but my understanding is that the GCP process itself is pretty new and kind of still in development — so maybe this 'reconsider' process should be developed and implemented in the context of that broader process, and also separately in terms of the non-GCP proposals process.

-------------------------

shawn16400 | 2023-03-08 14:35:55 UTC | #9

Thank you @annika - I appreciate your input on this.  Building on input from @kyle what if we broke the reconsideration down like this:

CSDO: Votes that impact what the DAO does:  
(ex: budgets, x-stream efforts, governance changes)

Steward Council: Votes impacting the ecosystem 
(ex: partnerships, Grants program changes, bubble cases)

Backtesting this logic, in the last 9 months I see about 8 cases that might have gone to the SC based on this segregation (if there were a reconsideration case brought)

* [GCP-001] - Funding IndexCoop gtcETH offering
* GR16 Round Structure 
* Ratify the Results of Grants Round 15 and Payout Matching Allocation
* GR15 Round Structure
* GR14 Round Structure & Grants Eligibility Update
* Withdraw $10MM of GTC to diversify our treasury and increase governance partners
* Ratify the Results of Grants Round 13 and Payout Matching Allocations
* Partnership & Mutual Grant with Wonder

@kyle @annika  does this segregation sense and get to your needs?

-------------------------

kyle | 2023-03-08 15:51:19 UTC | #10

It does make sense. Perhaps there is a default as well? In the short term, when there is confusion CSDO is the correct body, and then longer term as we continue to decentralize, we can transition that to Token holders (or Stewards if that remains a concept)?

-------------------------

ebransom | 2023-03-08 18:49:08 UTC | #11

I do think having this process would be helpful. 

I am part of the Steward Council, and I do think an external / internal group like this would be well suited to decide whether a vote should be reconsidered, as it would be less susceptible to internal politics / have a more removed point of view on whether the issue is material. 

I'm not sure that group would be well suited to propose that the vote be reconsidered in the first place. 

I like the specification that someone who voted for a proposal that passed or against a proposal that failed be the one to bring up the consideration of another vote. 

Perhaps CSDO proposes and SC determines whether to reopen?

-------------------------

Yalor | 2023-03-08 18:49:32 UTC | #12

I think the "Rage-quit" mechanics are the example of this in Moloch. 

Members who disagree with the decision to approve a certain proposal can Rage-quit and leave with their funds before the proposal passes. 

How would this look if the DAO was able to "Rage-quit" funding a work-stream 🤔 I don't know but kind of fascinating as an example of liquid governance. 

For example, I would love to be able to revoke my tokens for a certain initiative if I felt the leader of that initiative was no longer capable or qualified to execute on it. 

I think the Stewards should probably be the ones to review the case and make the final decision, sort of like DAO jury duty ⚖️ let the people who are not closest to the situation hear the facts and then make a decision. 

Overall I think having some kind of a claw back mechanism for proposals that don't have the full support of the DAO should be enacted, so that we can stay fluid with our decision making process and ensure everyone held is to the highest standards. 

Happy to be involved or brainstorm about the specifics on this process as it develops.

-------------------------

shawn16400 | 2023-03-08 21:36:07 UTC | #13

Today we presented this proposal to the Steward Council and through deliberations arrived at a suggested hybrid solution.   A CSDO member would be the one to raise the case to the Steward Council for consideration, ideally but not necessarily, after bringing it for discussion at CSDO.  This path allows CSDO to loosely gatekeep referrals (any CSDO member can raise a referral), but then sends the issue on to the Steward Council for a decision.   Thank you to @ebransom @eugyal @drnicka @ccerv1 @epowell101 @griff @kyle @kevin.olsen and @ceresstation for the input and great discussion.

-------------------------

shawn16400 | 2023-03-09 15:57:34 UTC | #14

[quote="Yalor, post:12, topic:13165"]
How would this look if the DAO was able to “Rage-quit” funding a work-stream :thinking: I don’t know but kind of fascinating as an example of liquid governance.
[/quote]

Hey @Yalor I really like the rage quit concept, especially from a co-founder and early start up perspective.  This kind of a mechanism incentivizes major token-holder collaboration (in order not to diminish the treasury) but allows for a planned exit when common ground cannot be found.

For Gitcoin Stewards, it might have less applicability given many of our stewards hold more delegated tokens vs owned tokens.   And rage quitting for Gitcoin stewards or contributors means they might have rage, they might quit, but the cost to the DAO is social/reputational vs. having a treasury impact.  :) 

For anyone interested in the rage quit concept, here is a quick [article](https://coinmarketcap.com/alexandria/glossary/rage-quit).  

[quote="Yalor, post:12, topic:13165"]
For example, I would love to be able to revoke my tokens for a certain initiative if I felt the leader of that initiative was no longer capable or qualified to execute on it.
[/quote]

You nailed it.  One of the gaps in our budgeting process is that we have only binary votes and signaling is only up/down.  If you compare FDD and DAOops S16 vs. S17 vote performance, there is little correlating voting data suggesting a workstream is in jeopardy - indicators are all social. 

@krrisis Umar and I are working on an updated budgeting process should allow for better signaling. 

[quote="Yalor, post:12, topic:13165"]
I think the Stewards should probably be the ones to review the case and make the final decision, sort of like DAO jury duty :balance_scale: let the people who are not closest to the situation hear the facts and then make a decision.
[/quote]
Consensus is building around this direction and is consistent with what the Steward Council told us yesterday.  Thanks for the affirmation and engagement @Yalor, it really helps.

-------------------------

shawn16400 | 2023-03-09 16:43:36 UTC | #15

I have updated this proposal based on input from the steward council meeting on 03.08.  You can view the live stream of that meeting [here](https://www.youtube.com/live/fv_6AJgyvDU?feature=share)

The major adjustment with the proposal is that CSDO initiates the motion to reconsider, and the subject is then taken up by the Steward Council for decision.  This adjustment allows an internal body with maximum context (CSDO) to raise and issue, but then refers the decision an elected/appointed body for decision (Steward Council).

Thanks @ebransom for this concept - it is an elegant solution that leverages the strengths of both bodies. 

If we receive a few more comments on this post from Stewards, we will move this from "ideas and open discussion" to the "proposal" phase. 

if you want to see the original proposal - you can find it here: 
https://docs.google.com/document/d/1IRo4AB7K1HYi_gDGBzeqWxKf5nrWvnJdlqZNB5QQxyY/edit?usp=sharing

-------------------------

DisruptionJoe | 2023-03-09 20:33:00 UTC | #16

I think my voice here would count this as a fifth steward voice allowing this to move forward. Additionally, I'll state here that I'm ok with applying this process to FDD's season 17 vote. 

Thanks for your hard work Shawn!

-------------------------

epowell101 | 2023-03-10 16:42:32 UTC | #17

I'm also supportive, as per discussion. And I would second the appreciation from DisruptionJoe - thank you Shawn!!

-------------------------

shawn16400 | 2023-03-10 17:54:38 UTC | #18

Thank you to the following stewards who commented on this proposal here on the forum @epowell101 @DisruptionJoe @kyle @Yalor @ebransom and @annika  and thanks to the community members @alif313 @jengajojo for the input.  Given we have 5+ steward comments, we have moved this to the proposal category with the intention of going to snapshot for vote in the week of March 13, 2023.

-------------------------

DisruptionJoe | 2023-03-10 19:03:43 UTC | #19

To clarify, my understanding is this. 

1) Put up a snapshot vote to ratify the revote process

2) Conduct the revote process on FDD S17 Budget Request

3) If revote is requested using this new process, then I would repost the vote for FDD S17 Budget Request. If it wasn't requested using the process, then delegates with enough tokens delegated on Tally would be required to post the FDD S17 Budget Request as is. 


For the record, I'm expecting the revote to be requested. My purpose has been to get this process solidified and I consider this result a success. 

***Quick Reminder - Solving this whole issue is literally an objective I put forward for FDD S17 dissolution success:***
![Image 2023-03-10 at 11.58.48 AM|690x221](upload://2BzQxXVCotNUmVJY1huPW4Lzj1b.jpeg)

I will likely craft a separate GCP to directly ask for a similar amount of funds to dogfood the Allo protocol for a sybil defense round which would be featured during the beta rounds.

-------------------------

shawn16400 | 2023-03-13 12:26:17 UTC | #20

Hi stewards and GTC holders - this GCP has gone to snapshot for vote and can be found here:

https://snapshot.org/#/gitcoindao.eth/proposal/0xe2c92f304f9ba0eb1617f1b8ef2874e0e56a2ce07f610173385b52fd04fea166


Please head over to snapshot and cast your vote!

-------------------------

shawn16400 | 2023-03-13 12:21:35 UTC | #21

[quote="DisruptionJoe, post:19, topic:13165"]
Put up a snapshot vote to ratify the revote process
[/quote]

Hi @DisruptionJoe 
I don't want to get too far ahead of ourselves, given this proposal has to pass first, but if it does pass, and the FDD budget fails to be taken up for reconsideration (either voted down, or not considered by the steward council) then you are correct, the FDD budget would have to be posted and ratified via Tally.  

[quote="shawn16400, post:1, topic:13165"]
B. If the Steward Council does not motion to “reconsider the vote”, or if a motion to “reconsider the vote” fails a majority vote, the original vote stands and must be executed as originally passed.
[/quote]

-------------------------

kyle | 2023-03-13 16:58:17 UTC | #22

[quote="shawn16400, post:1, topic:13165"]
If the Steward Council votes in the affirmative to “reconsider the vote”
[/quote]

Hey Shawn - Can you be more specific on what this structure looks like? How does the Steward council vote... is it a majority vote? is it that a member of that council presents the option to revote and a second member affirms the need for a revote, etc.

Would love to vote on this proposal but dont feel I have enough details to support yet.

-------------------------

shawn16400 | 2023-03-13 20:57:20 UTC | #23

Hi Kyle, 
Thanks for the question.  According to the text in the proposal, the steward council votes **for** a "reconsideration" or **against** a reconsideration using a simple majority vote.  The reconsider motion is brought to the steward council via a CSDO member which meets the criteria.   

The reference was obscure in the proposal, so thanks for asking the question and raising this up. 

From the proposal:
[quote="shawn16400, post:1, topic:13165"]
B. If the Steward Council does not motion to “reconsider the vote”, or if a motion to “reconsider the vote” fails a majority vote, the original vote stands and must be executed as originally passed.
[/quote]

Also, as I mentioned briefly in our quick discussion, we did not define a quorum for a decision takens by the Stewards Council.  Said another way, what minimum number of Steward Council members should be in attendance before a vote can be called?  Typically, a quorum is anywhere from a 51% (most common) to 66% (less common) of a voting body, as defined by that body.  To avoid this turning into an issue in the future, I will add that topic for our next steward council election.

-------------------------

lefterisjp | 2023-03-14 16:54:16 UTC | #24

Hmm this process though sounds nice, I can see it complicating the governance process and introducing a lot of strife.

In the motivation section you mention:

> Without a controlled process in place, the DAO is at risk for being forced to implement outdated decisions, move in an uncoordinated fashion, or make inappropriate or unauthorized declarations in order to repeal decisions in a way that might cause the entire governance process to be called into question.


But can you perhaps give a more contrete example than in the specifications? Why should any member of the CSDO have the power to ask for a vote recondisderation?

I can see this being open to abuse and for creating impermanence in the way governance works.

-------------------------

DisruptionJoe | 2023-03-14 18:03:41 UTC | #25

Here is the concrete example in which I'm pushing for a resolution that is fair/legitimate. 

https://gov.gitcoin.co/t/s17-proposal-integrated-fdd-budget-request/12738/46?u=disruptionjoe

-------------------------

CoachJonathan | 2023-03-14 18:59:11 UTC | #26

Finally getting a chance to read through this. Kudos on the thoughtfulness behind this and I'm fully supportive.

One clarification I'd like:
[quote="shawn16400, post:1, topic:13165"]
If the proposal is not brought by the original proposer within 7 days, the original vote is considered null and void.
[/quote]
I'm not 100% sure I understand this one sentence. 
The original proposer can propose again - great.
And if they don't propose, then what happens?
If the vote is being "reconsidered, isn't the vote considered null and void regardless?

Once I get this answer, I will be sure to vote :)

-------------------------

lefterisjp | 2023-03-14 20:31:14 UTC | #27

Okay I see. In such a case a process for a revote makes sense. I am going to vote in favour

-------------------------

shawn16400 | 2023-03-14 23:41:13 UTC | #28

[quote="CoachJonathan, post:26, topic:13165"]
If the vote is being "reconsidered, isn’t the vote considered null and void regardless?
[/quote]

Hey @CoachJonathan thanks for the question - and yes, you are correct.  After a motion to reconsider has passed, the original vote is essentially dead and the 7 day deadline is a bit redundant.  The intent of the 7 day timeline was to prompt the original proposer to move with haste to get the issue to resolution, or to accept the issue dead.  When we get to a point of writing a constitution (summation of governance processes) we could simplify the proposal and clean that up a bit. :)

-------------------------

kyle | 2023-03-20 00:36:20 UTC | #29

It looks like this proposal passed! Congrats to the team working on this, and thanks for submitting the Governance Process change.

-------------------------
