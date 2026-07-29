---
id: 7832
title: "[Proposal] Ratify the Results of Grants Round 10 and Formally Request the Community Multi-Sig Holders to Payout Matching Allocations"
slug: proposal-ratify-the-results-of-grants-round-10-and-formally-request-the-community-multi-sig-holders-to-payout-matching-allocations
category: governance-proposals
url: https://gov.gitcoin.co/t/proposal-ratify-the-results-of-grants-round-10-and-formally-request-the-community-multi-sig-holders-to-payout-matching-allocations/7832
created_at: 2021-07-09T21:19:20.216Z
last_posted_at: 2021-09-07T17:20:20.360Z
posts_count: 17
views: 4861
like_count: 42
---

# [Proposal] Ratify the Results of Grants Round 10 and Formally Request the Community Multi-Sig Holders to Payout Matching Allocations

<https://gov.gitcoin.co/t/proposal-ratify-the-results-of-grants-round-10-and-formally-request-the-community-multi-sig-holders-to-payout-matching-allocations/7832>
DisruptionJoe | 2021-07-15 18:54:30 UTC | #1

GTC Proposal - ([VOTE OPEN NOW on SNAPSHOT](https://snapshot.org/#/gitcoindao.eth/proposal/QmdLNbbE4CHPwyhfsqjj1qzst2NFjXS6Ax3moqWwgVWjQa)) Ratify the Results of Grants Round 10 and Formally Request the Community Multi-Sig Holders to Payout Matching Allocations

We ask our Community Stewards to ratify the GR10 payout amounts as being correct, fair, and abiding to community norms, including the judgements and sanctions made by the Anti-Fraud Workstream.

[Review the Grants Round 10 Governance Brief](https://gitcoin.co/blog/gitcoin-grants-round-10-governance-brief/)

To payout the matching allocations from Grants Round 10, we need the stewards to ratify the matching allocations. This comes with the extra responsibility of ratifying the decisions made by Gitcoin Holdings and the Anti-Fraud & Collusion workstream of GitcoinDAO.

To make the payouts in a timely manner, we would like to suggest voting on Wednesday, July 14th*.

Here are the need to know items:

* The round totals on the site are not adjusted for[ anti-sybil measures](https://medium.com/block-science/evaluating-the-anti-fraud-results-for-gitcoin-round-10-cec9277ce5b2).

In response to a few requests to make the data easier to read. We’ve updated this new version with the Blockscience fraud detection and Gitcoin results side by side (data is the same):

[Grants Round 10 Final Payout Amounts](https://docs.google.com/spreadsheets/d/1xD6XW4tJ7e9Fkvti-WflkS-MxOggKzEmkVrzHpLB_q0/edit?usp=sharing)*
*Feel free to comment directly on the sheet.

* The total fraud tax for GR10 was $14,350, down over 50% from GR9
  * The fraud tax is the difference in allocations before and after the sybil account contributions are deactivated from matching eligibility.
* Grant Approval, Grant Disputes, and User Sanctions are now determined by the Anti-Fraud & Collusion workstream with oversight from the community.
* Ratifying the decisions of the Anti-Fraud workstream does not create new policy.
* There will be opportunity to discuss their decisions in depth and ratify new policy prior to GR11.

The defensive measures taken to protect against fraud and collusion had incredible results. This may have been partly because of the community involvement and oversight.

While there is still more work to be done in progressively decentralizing the grants platform, ratifying this round’s closure will set a precedent for trusting, but verifying the workstream's decisions. (Similar mechanism design to an optimistic roll-up).

Please vote FOR or AGAINST

FOR You ratify the results as reported by Gitcoin Holdings & the Anti-Fraud & Collusion workstream and request the keyholders of the community multi-sig* to payout funds according to the [Grants Round 10 Final Payout Amounts](https://docs.google.com/spreadsheets/d/1xD6XW4tJ7e9Fkvti-WflkS-MxOggKzEmkVrzHpLB_q0/edit?usp=sharing) the non-custodial GR10 deployment contract.

AGAINST You do not ratify the results and request keyholders of the community multi-sig wallet to delay payment until further notice.

*This allows for 5 days of deliberation from today, 7/9/21 until 7/14/21. Round totals for before and after defensive measures will be added here on Monday 7/12/21.

** The Ethereum ecosystem is governed by the community multi-sig which we intend to transfer to the GitcoinDAO treasury once select criteria has been met.

For questions, comments or concerns on any of the above, please comment below or join the [Gitcoin Discord](https://discord.gg/cD6RKWjZ6g)!

-------------------------

Sirlupinwatson | 2021-07-09 22:24:50 UTC | #2

[quote="DisruptionJoe, post:1, topic:7832"]
Review the Gitcoin Grants Round 10 Governance Brief here
[/quote]

Hi @DisruptionJoe I hope you are doing well. 

To see the Round 10 Governance Brief, we need an authorization from Google looks like.

-------------------------

DisruptionJoe | 2021-07-12 13:59:17 UTC | #3

Wrong link! The governance brief is here: [https://gitcoin.co/blog/gitcoin-grants-round-10-governance-brief/](https://gitcoin.co/blog/gitcoin-grants-round-10-governance-brief/)

It has been updated in the post

-------------------------

lefterisjp | 2021-07-12 21:05:40 UTC | #4

How can we see how much is the fraud tax for each grant? So a comparison before/after the algorithm runs for each grant?

-------------------------

DisruptionJoe | 2021-07-12 21:11:57 UTC | #5

It is in the Blockscience reference materials. 

[This is the full study overview](https://hackmd.io/XdCMH5DtRHyPNLCGDFZ-oQ)

[This is the before after comparison](https://www.dropbox.com/s/ezl2ku5nvr2yuhi/r10_grants.csv?dl=0)

-------------------------

tjayrush | 2021-07-14 01:54:12 UTC | #6

The 'before and after' comparison is a CSV file with the follow header:

```
grant, modified, total_amount, match, funding, funding_diff, relative_funding_diff, include_filter, max_payout
```

Is there any further information about what these fields mean and how they were derived? I don't see that on the study overview. Also, any information on the rows of data? It's hard to tell, but it seems each grant has three rows of data. Is there an explanation of that?

I wouldn't normally ask, but my row (TrueBlocks) has an entry that looks differently to others (it has `true` in the `include_filter` field), so I'm wondering why.

-------------------------

DisruptionJoe | 2021-07-14 18:06:42 UTC | #7

I've gotten a few requests to make the data easier to understand. I've cleaned up this version with the Blockscience fraud detection and Gitcoin results side by side and a separate sheet showing before and after with the payout amounts. 

[Grants Round 10 Final Payout Amounts](https://docs.google.com/spreadsheets/d/1xD6XW4tJ7e9Fkvti-WflkS-MxOggKzEmkVrzHpLB_q0/edit?usp=sharing)

Feel free to comment directly on the sheet.

-------------------------

DisruptionJoe | 2021-07-14 18:14:02 UTC | #8

Reply from Danilo below. Looks like it wasn't used. I can't speculate on what it was, but looks like a thresh-hold of some sort.  Do you have his contact info? 

I also updated the original post with a sheet that has both of the results in an easy to read side by side. 

A - grant identifier (can be duplicated)
B - scenario (modified=False is the original data & modified=True is what happens when contribs from sybil users are removed. If blank, then this is related to the comparison between scenarios)
C - Sum of raw contributions (USDT)
D - Quadratic Match
E - Quadratic Funding (USDT)
F - Difference between fundings on the two scenarios (USDT) - associated with Fraud Tax per Grant
G - Share of F in relation to E (original scenario)
H - not used
I - max between E for the two scenarios

-------------------------

tjayrush | 2021-07-15 00:45:22 UTC | #9

This is great. Exactly what I was looking for. Thanks.

-------------------------

wschwab | 2021-07-15 08:22:05 UTC | #10

why did DeFi Latam vote against? I'm not sure what their tag is here

-------------------------

DisruptionJoe | 2021-07-15 14:57:35 UTC | #12

There was a dispute on the Commons Simulator (Grant 277) being included in the LatAm sub-round for $50,000.

The decision made was that the grant could stay in the category because it had existed since round 4 and had always been in LatAm, this is just the first time there was a pool dedicated to that region. The owner didn’t switch the region when the pool was announced.

We also advised that while we think this was the proper way to handle this round, we advise the stewards to consider how we can define the policy to better achieve the intended outcomes in the future. (The policy updates will happen before the next round.)

The Definitions subgroup that works on policy thought that it would be inappropriate to disallow them from GR10 by changing policy mid-round.

-------------------------

lefterisjp | 2021-07-17 07:59:47 UTC | #13

I will vote for the ratification as I don't see anything wrong. But what I don't like is that I feel kind of powerless to understand exactly how/why the differences in the payouts are as they are.

I was in the calls and heard the Blockscience guy explain but I might be stupid as I still don't totally grok it.

The differences in most grants are minuscule except for the edge ones. Then the question would be what can these grants do to improve the situation in the future? Or is it (as is my understanding) completely out of their hands?

-------------------------

Sirlupinwatson | 2021-07-17 13:34:16 UTC | #14

It's mainly a transparency question or aspect. From what I've seen in the spreadsheet, many amount has been overpaid or in some case underpaid (very few) from what I understand.

At the same, I really think it's great to see that this process has been reviewed and audited and some difference has been found.

-------------------------

DisruptionJoe | 2021-07-19 14:19:05 UTC | #15

I do understand that the calculations kind of feel like a "black box" at this point. 

Our goal with the anti-fraud workstream will be to make sure the data and calcs can be run and verified by the community in the near future. We will post the list of users to disable from matching benefits and let the greater wisdom of the community find error or issue. 

It will take more time before that is fully enabled.

A problem now is that we are working to build the decentralized grants tech (dGrants) so it is not likely that we will have cycles to document the data structures of the "legacy" version. We also must consider that as long as Gitcoin Holdings has centralized servers hosting any data, they also maintain liability for that data. 

I think this round the vote to approve is saying something like "We recognize the Gitcoin team has had sole control over this in the past (and still does). We approve the methodology and intentions used and appreciate the direction the team is moving to decentralize this aspect of the system. The oversight and mechansism aren't perfect now, but to get payments out and not have perfect be the enemy of good, we approve."

This will probably still be true for GR11. We will improve, but not have it perfect. I expect that each oversight and decision making mechanism will be improved both in documentation and execution. 

The goal would be to have strong mechanism design in place when the time comes to fully decentralize the technological architecture hosting grants along with the political power and decision making in a way that is verifiable through open-source software.

-------------------------

DisruptionJoe | 2021-07-19 14:19:44 UTC | #16

Thanks for taking the time to thoughtfully interact through this process. It's nice to see.

-------------------------

tjayrush | 2021-07-24 02:31:20 UTC | #17

Just a quick note here on the decision to use 'graduated sanctions' in this case. I think that was a good idea. One of Elinor Ostrom's tenets is that sanctions should be graduated -- small at first and increasingly larger as time goes on and the undesirable behavior doesn't correct itself. In this case, I'm sure it was an oversight/mistake, so no sanction was warranted. If the group doesn't correct it for Round 11, then the dispute may resolve in a different way.

-------------------------

David_Dyor | 2021-09-07 17:22:57 UTC | #18

[quote="DisruptionJoe, post:12, topic:7832"]
The Definitions subgroup that works on policy thought that it would be inappropriate to disallow them from GR10 by changing policy mid-round.
[/quote]

This is logical.  The 'Commons Stack' (CS) has a few longstanding grant applications with Gitcoin.  And they are an altruistic organization doing good work!  Full disclosure, I am a trusted seed (approved member) of the CS.

while Ostrom suggests graduated sanctions our current appeal policy is rather binary.  Either a grant gets approved or it does not.  There is an entire Gitcoin User Policy under development which imo should house the graduated sanctions to be issued for contraventions of user policy.  I see don't see a real spot for gradation of the appeals process unless we consider having graduated levels of appeal available to grant applicants (which is my suggestion).

There are huge growing pains right now as the decentralization process matures.  This was expected and tolerable.  Joe has a great perspective:  We must not let the striving for perfection destroy the good system we currently have.  It is continually improving.  

Accordingly, I support ratification.  
disclosure:  I am part of the Gitcoin Dao Fraud Detection & Defense (FDD) workstream.

-------------------------
