---
id: 16764
title: "[Proposal] Lower GTC Voting thresholds on and off chain"
slug: proposal-lower-gtc-voting-thresholds-on-and-off-chain
category: governance-proposals
url: https://gov.gitcoin.co/t/proposal-lower-gtc-voting-thresholds-on-and-off-chain/16764
created_at: 2023-10-16T16:47:15.187Z
last_posted_at: 2024-02-13T21:14:11.408Z
posts_count: 18
views: 8367
like_count: 51
---

# [Proposal] Lower GTC Voting thresholds on and off chain

<https://gov.gitcoin.co/t/proposal-lower-gtc-voting-thresholds-on-and-off-chain/16764>
kyle | 2023-11-02 13:05:57 UTC | #1

## **Proposal to lower GTC voting thresholds both on and off chain**

We currently see [~10 large GTC token holders](https://www.tally.xyz/gov/gitcoin/delegates) with the majority of on chain voting power, and ultimately decide most on/off chain decisions. I want to change this, and one of the first steps will be to lower the thresholds so that smaller token holder's voices will have a larger presence in the process. 

We have needed to keep a number of folks above 1MM to ensure proposals can be created, but by lowering the thresholds, we can lower the amount of GTC of individuals and enable the community to more broadly decide and participate in impactful ways.

It is hopefully no secret that token delegation from larger GTC token holders is why the top 10 have the token delegation allocations they do. This has largely been to empower those with the most context to help lead and guide governance. What this actually created though is a group that feels they cannot dissent, and a community that has a diminished voice in the process. 

Our [current v3 gov process](https://gov.gitcoin.co/t/gitcoin-dao-governance-process-v3/10358) outlines the following:

> There are two kinds of votes, off-chain and on-chain:
> 
> * Off-chain voting takes place on [Snapshot ](https://snapshot.org/#/gitcoindao.eth) and is required before any vote can be moved to an on-chain vote (if necessary). The vote period is 5 days. [Use this template for reference ](https://snapshot.org/#/gitcoindao.eth/proposal/0x43aa826eeca4380a8acabe787b41aea9b05a88c7958d5197cc77160183a9449e)
> * On-chain voting is required in addition to Snapshot voting for proposals that would move GTC from the DAO treasury or make other key changes to the structure of the DAO. Gitcoin will be using [Tally ](https://www.withtally.com/governance/gitcoin/voters) to upload on-chain proposals. The vote period is 5 days. [Use this template for reference. ](https://www.tally.xyz/governance/eip155:1:0xDbD27635A534A3d3169Ef0498beB56Fb9c937489/proposal/28) 

There is also a call out on post about quorum requirements -- ie, a need for 2.5M GTC to participate in all votes for the vote to be considered valid.

### Risks
Lowering the voting threshold opens us up to more governance attacks if large amount of tokens are acquired. This can be mitigated through delegation to a couple of key long term steward token holders who perhaps don't activate those wallets unless an attack is visible. This is common and you can see this with Uni when key votes haven been decided by largely silent voters to help protect the network.

### Vote
I would like to have us vote to amend our v3 governance process (introduce a v3.1) that amends these in the following ways:
**1. New quorum threshold of 1MM GTC instead of 2.5MM GTC for both on chain and off chain voting**
**2. Lower initial proposal threshold down to 150k GTC from 1MM GTC**
**3. Maintain time and duration process as outlined above****

Would love feedback on this ahead of the S20 budget votes to allow for more impactful community participation.

-------------------------

koday | 2023-10-16 17:57:12 UTC | #2

This is interesting - I think it's a great step towards empowering the community and allowing more people to participate in governance while feeling like they can actually make a difference and I support the proposal.

An idea I had while reading this is using Passport and/or QV in the governance process to put more value on individuals voting instead of the total number of GTC. Another idea is to reference data from the gov forum to increase voting weights (e.g. 10hr read time adds 10k GTC equivalent voting power, 1 post created with X impressions = Y GTC equivalent voting power, etc). 

I'm just thinking out loud here and I'm not sure if any of this has been experimented with before, but I believe there are interesting metrics we could attach a value to in terms of governance voting that might also empower more grassroots efforts across the community.

-------------------------

meglister | 2023-10-30 21:53:58 UTC | #3

I'm sorry to miss the opportunity to do this for S20 budget votes -- I'm in favor of this because it feels like it makes a meaningful step towards more participation without introducing too much risk. I would also love to see action on the long-term stewards as risk mitigators, but doesn't feel like that's a blocker to launching this.

-------------------------

CoachJonathan | 2023-10-31 08:47:05 UTC | #4

Apologies for the late response on this.

I think overall I'm for the idea of lowering thresholds but I had some questions about this proposal.

Context:
- My understanding is that anything we vote on as a DAO first goes to Snapshot (offchain social contract) and then moves to Tally (onchain contract)
- Tally is mostly symbolic - a reflection of results that happened on Snapshot
- There is also an unwritten (for now) rule about having a proposal in the forum up for a certain amount of days + a certain amount of comments

Question:
- Do these thresholds impact Snapshot *and* Tally, or just Tally?
- How does this work with the minimum amount of time/comments in the forum?

I'm trying to conceptualize how all of this would work and want to make sure I'm crystal clear that this, indeed, would solve the problem you outlined.

-------------------------

krrisis | 2023-10-31 16:29:24 UTC | #5

I'd be down for point 2 & 3, but I do have a question about point 1.

[quote="kyle, post:1, topic:16764"]
**1. New quorum threshold of 1MM GTC instead of 2.5MM GTC for both on chain and off chain voting**
[/quote]

If we lower this threshold it seems to me we risk to diminish voter participation even more, no? In the sense that even just one or two token holder could make a proposal pass. I know your proposal would be to change this, but wondering if lowering this threshold is the key factor here (rather than dialogue with the token holders who delegate) and does not increase the risk for governance attacks too much? 

Know the answers to your Qs here Jon so quick response :

[quote="CoachJonathan, post:4, topic:16764"]
* Do these thresholds impact Snapshot *and* Tally, or just Tally?
[/quote]

Both, that's what kyle means with offchain & onchain as explained above. 

[quote="CoachJonathan, post:4, topic:16764"]
* There is also an unwritten (for now) rule about having a proposal in the forum up for a certain amount of days + a certain amount of comments
[/quote]

[quote="CoachJonathan, post:4, topic:16764"]
* How does this work with the minimum amount of time/comments in the forum?
[/quote]

Time of comment in the forum is actually in the ratified gov proposal, here: 

[quote="kyle, post:1, topic:10358"]
Once it has been posted in the forum, a proposal must:

* Be available for review and comment for at least 5 days, and
* Receive input from at least 5 stewards not connected to or working with the proposal/with workstream (any stewards part of the proposal should also be disclosed).
[/quote]

-------------------------

azeem | 2023-10-31 23:46:56 UTC | #6

As one of the largest token delegates who does have over the 1 million threshold I definitely feel this is a good step to take in making things a more fair process overall. Definitely supportive of this.

-------------------------

Viriya | 2023-11-01 13:59:44 UTC | #7

I'm in favour of this direction generally. I'm interested to see and incentivise a reorg the delegate body to create more external accountability. I also think this external accountability will have a tertiary effect of uniting Gitcoin's leadership body to better communicate our decisions and plans to external holders. 

I'm also interested to hear about the technical nuances @CoachJonathan outlined but am certainly in favour of this experiment.

-------------------------

CoachJonathan | 2023-11-24 13:56:02 UTC | #8

Hey everyone, I'm keen to revive this chat since the proposer is offline until the new year.

I think most of my curiosities have been satisfied. One thing I want to explore with folks on the forum is around the risks.
[quote="kyle, post:1, topic:16764"]
This can be mitigated through delegation to a couple of key long term steward token holders who perhaps don’t activate those wallets unless an attack is visible. This is common and you can see this with Uni when key votes haven been decided by largely silent voters to help protect the network.
[/quote]

I'm wondering if before putting this to a vote, someone would be willing to work with me to more concretely describe what measures we actually want to put in place. 

If we were to move with the suggestion Kyle made, I would like to bust out a formal agreement in this proposal. Something like "We will start up the Governance Defence Council. This is how the council is structured..." and actually describe some of the mechanics around it to ensure this actually gets put into place.

I'm happy to lead the charge on adding this to the proposal. What I would love form the Gitcoin Community is either a) a co-captain to steward this with me or b) suggestions from others about DAOs who have successfully implemented this. I'd love to fork documentation where possible so that I'm not fully reinventing the wheel.

-------------------------

CoachJonathan | 2023-11-29 15:24:39 UTC | #9

[quote="kyle, post:1, topic:16764"]
This can be mitigated through delegation to a couple of key long term steward token holders who perhaps don’t activate those wallets unless an attack is visible.
[/quote]

### Addendum to Proposal: Establishment of Guardian Stewards

**1. Purpose and Function of Guardian Stewards**

* **Role**: Guardian Stewards will act as a defensive mechanism against governance attacks in the DAO. They will remain largely passive but will be authorized to activate their voting power in case of a detected attack or threat to the integrity of the DAO's governance.
* **Activation Criteria**:

Clear guidelines will be established to define what constitutes a governance attack, ensuring that the Guardian Stewards' power is exercised judiciously and transparently.

**2. Election Process for Guardian Stewards**

* **Nomination**: Core Contributors at the DAO can nominate candidates for the role of Guardian Steward. Nominees should have a demonstrated history of long-term involvement and a deep understanding of the DAO's mission and governance.
* **Voting**: The election of Guardian Stewards will be conducted via a special DAO vote, separate from regular governance votes, to ensure fairness and transparency.

**3. Source of Tokens for Guardian Stewards**

* **Allocation**: A specified amount of GTC tokens will be allocated to the Guardian Stewards. This allocation could come from a dedicated fund or reserve within the DAO's treasury, specifically earmarked for governance defense.
* **Token Stewardship**: The tokens will remain under the control of the Guardian Stewards but are to be used solely for the purpose of defending the DAO's governance process.

**4. Roles and Responsibilities**

* **Monitoring**: Guardian Stewards will be responsible for monitoring voting activities and identifying potential threats.
* **Decision to Act**: The decision to activate their voting power must be unanimous among all Guardian Stewards to prevent misuse.
* **Transparency and Reporting**: Guardian Stewards will be required to provide transparent reporting on any actions taken, including the rationale behind activating their voting power.

**5. Term and Accountability**

* **Term Length**: Guardian Stewards will serve for a fixed term of one year, after which new elections will be held.
* **Accountability**: They will be accountable to the broader DAO community, with mechanisms in place for the community to recall a Guardian Steward if necessary.

**6. Title and Recognition**

* **Title**: Members of this group will be formally recognized as "Guardian Stewards" of the DAO.
* **Recognition**: Their role and contributions to maintaining the integrity of the DAO's governance process will be acknowledged and valued by the community.

<hr>

This is a strawman proposal and is open to feedback and comments. Some areas I would love to see some discussion around include:

> Guardian Stewards

Open to suggestions on the name of this role (maybe we should have this be a "committee" or "council" with several "members"?

> Clear guidelines will be established to define what constitutes a governance attack,

I would love help defining these.

> Members of the DAO can nominate candidates for the role of Guardian Steward

I'm open to suggestions on who gets to nominate candidates. Right now I have indicated "Core Contributors" but am happy to open this up to all Stewards/GTC holders. I'm also open to closing this off and making this a decision process led by the Executive Director of the Foundation.

> The election of Guardian Stewards will be conducted via a special DAO vote

I'm not sure what the pros/cons of a GTC token nominated candidate would be. Also open to explore 1-person-1-vote system, so long as we are clear about who gets to participate.

> A specified amount of GTC tokens will be allocated to the Guardian Stewards.

My thought is something to the order of 1M tokens, and am open to suggestions here.

> with mechanisms in place for the community to recall a Guardian Steward if necessary.

I am happy to lead on this and put something in later to address this (similar to other roles in the Governance Manual, Guardian Stewards will have roles, responsibilities and decision rights).

-------------------------

MathildaDV | 2023-12-01 21:58:50 UTC | #10

Love the idea of Guardian Stewards. 

I am in favour of allowing Core Contributors to nominate members! I feel like the core contributors (especially those who has been at Gitcoin for an extended period of time) can have a lot of good context within the DAO and the inner workings of Gitcoin. I do also think it would be valuable to allow Stewards to be a part of this process. 

Which brings me to my next point (and forgive me if this isn't the correct thread to drop this in), but I've been pondering the voting power that core contributors get in general. What about contributors who have been at the DAO for over a year and who would like to become more active within governance but they hold little to no voting power? Is there a way to enable those contributors to have more of a say? Especially because of the context they hold. I myself am a steward and I find myself in this position so it's the reason I've been curious :) 

We also have a lot of inactive stewards -- what happens to stewards who aren't participating in governance anymore?

-------------------------

Donny_Jerri | 2023-12-05 09:10:37 UTC | #11

This to me is spot on the point.  Every web3 community I am involved with that has community governance has the same issues with large holders that become non-participatory at a certain point.  This heavily influences the mechanisms in place.  Community delegated stewardship roles should elevate this as all of the little active people know who the real guardians are and can put them in positions to guide efficiently.  

Lowering the threshold to allow for a broader base is also needed for true community governance.  

Bravo.

-------------------------

CoachJonathan | 2023-12-05 11:58:34 UTC | #12

Thanks for the feedback :) I'm going to leave this up for a few more days for comments before integrating feedback & moving this to a vote.

Regarding your point about voting power - right now there are no formal ways to request larger token delegations. The only way to do this afaik is to find out 1) who are the large token holders and 2) ask them to delegate these to you.

One initiative I'd like to see happen in the new year is something that can start to address this gap - how do we have high context, willing participants grow their delegation without compromising the (possibly desired) anonymity of these large token holders.

One possible option that we'll explore in the new year is the introduction of clearer parameters for 1 reputation-based 1-person-1-vote system for certain governance issues. I don't think what you're pointing to is an isolated issue, and likely happens all over the Web3. 

Will add this to the governance roadmap to explore in the new year.

-------------------------

charlesfreeborn | 2023-12-05 17:16:03 UTC | #13

This is a welcome development and I am in support of this proposal

-------------------------

CoachJonathan | 2023-12-07 20:49:31 UTC | #14

Hi all, I will be moving this to a vote shortly. Below is some revised language I would like to propose. Changes include:

- Guardian Stewards will be assigned for their first term, and then elected hereafter
- Edited section on recognition
- Added a budget section (not a funded role)

### Addendum to Proposal: Establishment of Guardian Stewards

**1. Purpose and Function of Guardian Stewards**

* **Role**: Guardian Stewards will act as a defensive mechanism against governance attacks in the DAO. They will remain largely passive but will be authorized to activate their voting power in case of a detected attack or threat to the integrity of the DAO’s governance.
* **Activation Criteria**: Clear guidelines will be established to define what constitutes a governance attack in a separate post/thread, ensuring that the Guardian Stewards’ power is exercised judiciously and transparently.

**2. Election Process for Guardian Stewards**

* **Nomination**: For the first term, Guardian Stewards will be assigned by the Gitcoin Foundation. In the future, Stewards and Core Contributors will be able to nominate candidates for the role of Guardian Steward. Nominees should have a demonstrated history of long-term involvement and a deep understanding of the DAO’s mission and governance.
* **Voting**: Once we have our first elections, Guardian Stewards elections will be conducted via a special DAO Core Contributor vote, separate from regular governance votes, to ensure fairness and transparency and that elected members are being selected by high context individuals. As we get closer to election time, there is possibility of opening up this election beyond Core Contributors.

**3. Source of Tokens for Guardian Stewards**

* **Allocation**: A specified amount of GTC tokens will be allocated to the Guardian Stewards. This allocation could come from a dedicated fund or reserve within the DAO’s treasury, specifically earmarked for governance defense.
* **Token Stewardship**: The tokens will remain under the control of the Guardian Stewards but are to be used solely for the purpose of defending the DAO’s governance process.

**4. Roles and Responsibilities**

* **Monitoring**: Guardian Stewards will be responsible for monitoring voting activities and identifying potential threats.
* **Decision to Act**: The decision to activate their voting power must be unanimous among all Guardian Stewards to prevent misuse.
* **Transparency and Reporting**: Guardian Stewards will be required to provide transparent reporting on any actions taken, including the rationale behind activating their voting power.

**5. Term and Accountability**

* **Term Length**: Guardian Stewards will serve for a fixed term of six months, after which new elections will be held. Guardian Stewards can run for reelection as many times as they would like.
* **Accountability**: They will be accountable to the broader DAO community, with mechanisms in place for the community to recall a Guardian Steward if necessary.

**6. Title and Recognition**

* **Title**: Members of this group will be formally recognized as “Guardian Stewards” of the DAO.
* **Recognition**: This role will be documented and maintained in the Governance Manual and will be entrusted to Stewards in high esteem in the Gitcoin Community.

**7. Budget**

* **Funding**: This role will not be funded due to the little amount of action that will be required.

-------------------------

CoachJonathan | 2023-12-07 21:05:17 UTC | #15

The vote for this proposal is now live on Snapshot: https://snapshot.org/#/gitcoindao.eth/proposal/0xa68b33484f5fe3e53f2f51335483057200d3fa08cdafc93c0904b29514cb9980

-------------------------

CoachJonathan | 2023-12-13 07:53:04 UTC | #16

A reminder that this proposal is still live on Snapshot for another day and is (ironically) below quorum to pass. Stewards, please get active and vote!

-------------------------

CoachJonathan | 2023-12-18 12:14:02 UTC | #17

This snapshot has closed and option 1 “Yes makes these changes” has won.

The full text for the option was: Voting “Yes” to 
1. New quorum threshold of 1MM GTC instead of 2.5MM GTC for both on chain and off chain voting)
2. Lower initial proposal threshold down to 150k GTC from 1MM GTC
3. Maintain current governance time and duration process

Metrics:
1,524unique votes
~3.4M GTC tokens cast.

Thank you to the author for the proposal and to all the stewards and GTC token holders who cast their vote.

<hr>

As a follow-up I will be taking on the execution of this and will outline a timeline for implementation in the new year.

-------------------------

kyle | 2024-02-13 21:14:11 UTC | #18

Hey all - Super excited to share that this has passed and been executed! 

This is one step to make our governance more approachable and move power away from the largest GTC token holders. Soon, we can explore more and more options (like quadratic voting) to continue to grow governance participation.

-------------------------
