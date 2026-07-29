---
id: 15050
title: "[Proposal] - Gating who can make a Snapshot governance proposals"
slug: proposal-gating-who-can-make-a-snapshot-governance-proposals
category: governance-proposals
url: https://gov.gitcoin.co/t/proposal-gating-who-can-make-a-snapshot-governance-proposals/15050
created_at: 2023-05-15T18:49:51.240Z
last_posted_at: 2023-06-27T10:55:20.842Z
posts_count: 15
views: 5739
like_count: 35
---

# [Proposal] - Gating who can make a Snapshot governance proposals

<https://gov.gitcoin.co/t/proposal-gating-who-can-make-a-snapshot-governance-proposals/15050>
shawn16400 | 2023-06-19 14:26:44 UTC | #1

### THE PROBLEM:
Over the past month, web3 (Gitcoin included) has experienced a series of “fake” or scam Snapshot proposals that have been posted to various DAO snapshot sites. Last week, SnapshotLabs responded with this guidance: [Snap the scams out!](https://snapshot.mirror.xyz/-uSylOUP82hGAyWUlVn4lCg9ESzKX9QCvsUgvv-ng84)

### TENSION:
The social contract governing the proposal/vote process at Gitcoin was defined in [Gitcoin DAO Governance Process v3. ](https://gov.gitcoin.co/t/gitcoin-dao-governance-process-v3/10358)Generally speaking, anyone can make a proposal on the forum and it has to 1) be available for comment for five days and 2) receive comments from five stewards.  With those two conditions met, and given the formatting of the proposal was correct, the proposal could move to snapshot for vote.

Here is the relevant section from the Governance process v3 listed above: 

> ### Proposal Discussion
> Before a proposal can go to a vote, it must be posted in the appropriate category on the forum for review and comment by the community.
> 
> Proposals brought to the forum must be in the format required by the and address the considerations set out in Table 2: Required Information, above.
> 
> Once it has been posted in the forum, a proposal must:
> 
> * Be available for review and comment for at least 5 days, and
> * Receive input from at least 5 stewards not connected to or working with the proposal/with workstream (any stewards part of the proposal should also be disclosed).
> 
> A proposal that does not meet the requirements for formatting, required information, length of review, or input from stewards will be removed from Snapshot voting if an attempt is made to hold a vote.

*From https://gov.gitcoin.co/t/gitcoin-dao-governance-process-v3/10358*

Previously, the Gitcoin Snapshot voting site was pretty wide open. Nearly anyone could make a proposal on snapshot with, or without following the social convention outlined above.

On four occasions, scam proposals were posted to the Gitcoin snapshot accounts suggesting or proposing Gitcoin airdrops. 

To quickly lock down the proposal capability, the snapshot account was locked using Gitcoin Passport, limiting posters to those who had donated to past grants rounds.  This approach had issues given that database updates were no all ways 100%, thus the account was updated to allow posting only from those with a balance of at least 100GTC, or those who had greater than 1000 Twitter followers.

### PROPOSAL:
The initial movement to lock down the snapshot account was necessary, but it is important to ensure that any major change in governance should be ratified by voters. This is especially important when putting controls and limitations around who can and who cannot make bonafide proposals for Gitcoin.

This being the case, this proposal attempts to do three things:
1. Explores options for gating proposals
2. Articulated pros and cons for each case
3. Set the draft governance proposal for change

### OPTION ASSESSMENT:

To rectify the issue, we identified three options below to gate our Snapshot account. Please provide feedback on those options - or suggest additional options I may have missed.

**Option 1: establish a manual review process & whitelist proposers**

This option would lock down snapshot to “a few” people who would be responsible for 1) reviewing the completeness of the proposal, 2) determining if the process was followed and 3) posting the vote if it passes the check
![image|690x147](upload://9iPAfyMb4BJYOe2GULuAJDh0sVa.png)
.


**Option 2: Continue to use Passport as a control, using at least GTC = 100 **or** twitter followers = 1000**
This option would gate proposals via Gitcoin Passport connected to Snapshot using the existing stamps, which are at least 100GTC tokens held OR 1000 Twitter followers.
![image|690x96](upload://D4yXyOnFYI7uhy9P1RdM3129q0.png)
.

**Option 3: Continue to use Passport as a control, but explore other stamps**
This option would gate proposals via Gitcoin Passport connected to Snapshot but explore using other stamps to gate the community. See the appendix below for a complete list of Passport stamps.
![image|690x115](upload://5As3U1Tv21XXkFB3gr8iis5o5W5.png)

Leading stamp options: 
* GTC staking 100GTC (gold) (drives GTC utility - we use it to make proposals)
  * Stamp seems to unstake after each grant round - not ideal for ongoing votes.
* Github: illustrates open source contributions (but not validated)
* Snapshot - voted on 2 or more DAO proposals: illustrates participation with Web3 Governance

**Recommendation: Option 2**.  
Current best thinking is that a pluralistic passport score is the best option as it will us to add/remove/change stamps as the value changes in response to Sybil actions while providing the most robust defense.  However as the scoring is not available on Snapshot yet, but there is effort under way, it makes the most sense to ratify our current settings Option #2) and adjust when the new scoring methodology is in place. 

In closing, this is not "wow" work that anyone is going to be excited about.  But part of operational excellence is paying attention to governance detail that can come back and bite us in the butt later on.  Going back and cleaning up work that was done on the fly is necessary, however often not very exciting.

-------------------------

shawn16400 | 2023-05-18 14:07:45 UTC | #2

We had a great talk last night with Jeremy, Sophia and @0xZakk discussing this concept.  

In short:
1. Passport gating is the right path to protect snapshot 
2. A minimum passport score should be the gate, not specific stamps.  Specific stamps depreciate over time whereas a score allows for greater voter autonomy and consistency of protection. 
4. GTC staking could be a great option as it continues to be developed 
5. We should to connect this to the Passport plan the MMM team is developing
6. The next exciting challenge will be to implement QV on DAO votes using Snapshot + a Passport score.  More work analytical to be done first.  (hint - @ale.k ) 

Thanks for the engagement!

-------------------------

jengajojo | 2023-05-19 08:52:07 UTC | #3

Thanks @shawn16400 This is a good start and I would be in favor of using passport and adding other offchain or onchain features. * Staking 100GTC (gold) is a great add-on too! 

- Using 'minimum status' according to discourse rules https://blog.discourse.org/2018/06/understanding-discourse-trust-levels/ could be a useful filter
- Governance history:  
  if the wallet has voted on atleast 'x' proposal in the past (in gitcoinDAO or other whitelisted DAOs)
  if the wallet has created proposals on snapshot in other whitelisted DAOs
  if the wallet holds atleast 'x' hypercerts

-------------------------

shawn16400 | 2023-05-21 14:04:40 UTC | #4

Thanks @jengajojo for the engagement on this one.  I really appreciate your feedback. 

[quote="jengajojo, post:3, topic:15050"]
Thanks @shawn16400 This is a good start and I would be in favor of using passport and adding other offchain or onchain features. * Staking 100GTC (gold) is a great add-on too!
[/quote]

I really like this option given it feeds into GTC utility - or using the governance token for something other than just voting.  However at the moment the GTC staking stamp is limited to staking during Gitcoin rounds and it not yet an always-on feature.  Once it is, I think this can be a powerful governance feature.  Here I think about granting sliding governance influence linked to the duration and quantity of staked GTC.  But that is for another proposal once the capability is in place. 

[quote="jengajojo, post:3, topic:15050"]
Governance history:
if the wallet has voted on atleast ‘x’ proposal in the past (in gitcoinDAO or other whitelisted DAOs)
if the wallet has created proposals on snapshot in other whitelisted DAOs
if the wallet holds atleast ‘x’ hypercerts
[/quote]

This is one reason why I am bullish  web3 governance.  We are developing the capability to craft infinitely customizable governance mechanism that can (for the first time ever) attempt to balance differing stakeholder incentives (contributors vs. investors vs. users vs. ecosystem vs partners).  The challenge for governance architects is to 1) limit bureaucracy 2) credibly evaluate outcomes 3) watch for unintended consequences.  

What I like about your suggestions is it provides early thinking for cross-dao integration which is where I hope Gitcoin goes.  This kind of thinking will lead us to antifragile networks and stronger linkages between nodes - especially as attacks get more sophisticated.

What I appreciate about Gitcoin Passport team is their thinking about the sum total of reputational value, or score.  It's less about an individual hypercert or passport stamp.  Each of those certs or stamps have a dynamic anti sybil value - as scammers learn how to circumvent a stamp, that stamp degrades in value, and as such so does the governance strategy designed around individual stamps or hypercerts.

For this reason, I intend to change the paper above from "exploring options" to a proposal using the Gitcoin Passport "score" as opposed to individual stamps.   I hope to have this strategy tested shortly so we can update this proposal and get on with it.

-------------------------

juanna | 2023-05-22 16:41:24 UTC | #5

1,000 Twitter followers sounds a little steep for some of our valued contributors who aren't as active on social media (also easily bought), but staking 100GTC + Passport sounds like it could be the way. It doesn't sound like the staking utility is available yet, so until then, agreed with Passport gating w/ a higher score than our typical donor min.

As someone newer to Gitcoin governance, I'm hesitant to put too many history-based limitations at risk of accidentally barring out myself haha. However, also foresee myself voting more on proposals, versus creating actual them in the actual near future, so even with history-based--it probably wouldn't be an issue. Looking forward to seeing how our experimentations in governance pan out! 

Appreciate everyone putting their brilliant minds together to jam on making governance better for all :heart_hands:

-------------------------

kyle | 2023-05-24 01:34:30 UTC | #6

Thanks Shawn - I appreciate you calling this out and also working to get a viable alternative in place for the current implementation. the Passport Scoring seems like a great option. I don't quite understand this step as it doesn't seem related to gating *creation* of Snapshot proposals.

[quote="shawn16400, post:2, topic:15050"]
The next exciting challenge will be to implement QV on DAO votes using Snapshot + a Passport score. More work analytical to be done first.
[/quote]

Are you thinking we want to have a passport score for voting in addition to the score for posting proposals? Perhaps this is just on the sub domain snapshot voting?

-------------------------

shawn16400 | 2023-05-24 11:46:55 UTC | #7

Hey @kyle!

[quote="kyle, post:6, topic:15050"]
Are you thinking we want to have a passport score for voting in addition to the score for posting proposals? Perhaps this is just on the sub domain snapshot voting?
[/quote]

 You are correct, to keep our proposals clean, this proposal is limited to the *creation* of proposals on snapshot, gated by passport.  Extending the gating of actual voters using passport would be a separate proposal, and a bit more work to be done. :)

-------------------------

ZER8 | 2023-05-24 21:09:22 UTC | #8

This is an important issue, but imo staking 100 GTC & holding 100 GTC is not enough. I would also increase the Snapshot stamp option to - voted on 5(ideally 10) or more Dao proposals. Nowadays people spam vote on snapshot for airdrops a lot. Hope this at least tangentially helps..

So I would opt for a hybrid between option 2 & option 3. Curious to see what others think :saluting_face:

-------------------------

Jeremy | 2023-05-24 22:57:15 UTC | #9

[quote="shawn16400, post:4, topic:15050"]
What I appreciate about Gitcoin Passport team is their thinking about the sum total of reputational value, or score. It’s less about an individual hypercert or passport stamp. Each of those certs or stamps have a dynamic anti sybil value - as scammers learn how to circumvent a stamp, that stamp degrades in value, and as such so does the governance strategy designed around individual stamps or hypercerts.

For this reason, I intend to change the paper above from “exploring options” to a proposal using the Gitcoin Passport “score” as opposed to individual stamps. I hope to have this strategy tested shortly so we can update this proposal and get on with it.
[/quote]

Thanks @shawn16400. We're still finalizing the Snapshot integration which will enable this, but I agree, moving to a pluralistic passport score is the best option as it will us to add/remove/change stamps as the value changes in response to Sybil actions while providing the most robust defense.

-------------------------

Supreme | 2023-05-30 07:03:14 UTC | #10

This seems to exclude many. It also seems to centralize the governance even more by limiting who can submit proposal.  If the proposal was out of left  field, couldn't voters just vote NO?

Also consider auditing hypercerts more thoroughly -  
https://github.com/AnonWLAJFA/hypercerts_audit

-------------------------

shawn16400 | 2023-05-30 13:49:44 UTC | #11

[quote="Supreme, post:10, topic:15050"]
This seems to exclude many. It also seems to centralize the governance even more by limiting who can submit proposal. If the proposal was out of left field, couldn’t voters just vote NO?
[/quote]

You are partially correct, and perhaps a bit of nuance for clarification on decentralization.  

Adding a gating mechanism like this by design limits who can make proposals; our intent is to filter out spam.  I should have saved a screen shot the prior examples before we deleted them but in essence the intent of those snapshot proposals was not to get a proposal passed, but to create false-legitimacy for twitter/airdrop farming campaigns.  Those twitter campaigns pointed to our snapshot account and said "look Gitcoin is going to do xyz!! Sign up now to be the first to get the airdrop!!" followed by some evil link.

Yes, we could leave them up on our snapshot, but if Snapshot is anything like Discord or our Forum, it would quicky be overrun by spambots & trash.   The tension is to set the bar high enough to make the cost of spam higher than the return on the investment, while keeping the costs low enough that any legitimate user can participate.  See this article here by @kyle https://www.gitcoin.co/blog/cost-of-forgery. 

Related to decentralization, this design does not rely on a person or team to decide what can or cannot be posted, but hands the responsiblity for setting the threshold over to the community.  Going one step further, by using the Passport scoring methodology instead of Passport stamps we are opening up the proposal process to anyone who meets the minimum score, not just holders of GTC.   Which I am on the fence about, but its good we dogfood our new scoring technology. 

Thank you for the questions and engagement and I appreciate challenges to our assumptions and logic!

-------------------------

shawn16400 | 2023-06-13 14:25:08 UTC | #12

Quick update on this proposal - the Snapshot team is working with our Passport team to see if / when we will be able to use the Passport score as a gating mechanism.  I am hopeful we can get a target date, but if not, we will move forward with a vote using the current gating mechanism applied on snapshot today.

-------------------------

shawn16400 | 2023-06-19 14:13:07 UTC | #13

Quick update, we do not yet have a target date for implementing the Gitcoin Passport score with 
Snapshot.  Given this is the preferred method for Snapshot gating, so we will move forward with a a proposal to ratifying our current methodology which is outlined as **Option #2** above.  Specifically, the gating is  > 1000 twitter followers or GTC at least 100.  When the scoring capability comes on line, or we find that the current controls are not enough to curb our-of-process proposals, we will adjust via a new proposal. 

![image|363x41](upload://y0UyW2Jum5QiIYgxxHX1gn1RWTn.png)
![image|360x43](upload://cyBaoI0pPCaMDGue7FUatb16JHZ.png)

For clarity, we are adjusting the body of the proposal above to change the recommendation from option #3, to option #2, 

**FROM:** 
**Recommendation: Option 3 with any of the following stamps:**
Implement the following stamps

* Staking 100GTC (gold)
* At least 100GTC held in the wallet


**To:** 
**Recommendation: Option 2**.  
Current best thinking is that a pluralistic passport score is the best option as it will us to add/remove/change stamps as the value changes in response to Sybil actions while providing the most robust defense.  However as the scoring is not available on Snapshot yet, but there is effort under way, it makes the most sense to ratify our current settings Option #2) and adjust when the new scoring methodology is in place.

-------------------------

shawn16400 | 2023-06-19 14:27:52 UTC | #14

This proposal has been moved to snapshot for vote.  The vote will close on 06.26. 

https://snapshot.org/#/gitcoindao.eth/proposal/0xa18926b9dc9592bdf02acc3cef5a41021cebe51f73a2a3d6b007d7c38685b296

-------------------------

shawn16400 | 2023-06-27 10:55:20 UTC | #15

fyi - this snapshot vote has passed with ~99% approval rate.
Metrics:
1891 unique votes
~2.8M GTC tokens cast.

Thank you to all the voters for participating in our governance.

-------------------------
