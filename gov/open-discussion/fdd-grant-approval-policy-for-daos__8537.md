---
id: 8537
title: "FDD Grant Approval Policy for DAOs"
slug: fdd-grant-approval-policy-for-daos
category: open-discussion
url: https://gov.gitcoin.co/t/fdd-grant-approval-policy-for-daos/8537
created_at: 2021-09-10T16:14:16.240Z
last_posted_at: 2021-10-05T23:19:22.601Z
posts_count: 9
views: 4137
like_count: 17
---

# FDD Grant Approval Policy for DAOs

<https://gov.gitcoin.co/t/fdd-grant-approval-policy-for-daos/8537>
DisruptionJoe | 2022-05-28 15:34:43 UTC | #1

The number of DAOs applying for grants has been increasing exponentially. The issue we are facing is much in the same way "token" as a term cannot define all tokens, "DAO does not define all DAOs"

As a collective focused on building opensource coordination tools which help solve public goods fundings problems, GitcoinDAO will need to select a policy for DAO inclusion in grants. 

As of now, we have taken the lenient approach only denying for sybil and unqualified accounts. 

I hope to have a productive discussion around what criteria should be considered and what the thresholds should be for inclusion. 

Here is an inexhaustive list of criteria considerations: 
* Is it already established?
* Is there smart contract governance? (Moloch, Compound, Multisig?)
* Should every substream and individual be allowed their own grants?
* Is the DAO open to participants or permissioned?
* Is the DAO designed to be forkable? Composable? 
* Was the DAO a "fair launch"
* Can members of the DAO rage quit

I might add in as well that a few principles to consider here are: 
* Positive Sum
* Ability to Exit
* Modularity
* Equal Access
* Transparency

-------------------------

David_Dyor | 2021-09-10 17:54:01 UTC | #2

Other important considerations:

How many members in this dao?
How old is this dao?
Does this dao have any external funding at all?

I can say with confidence, the gate is much too wide and without sentry.

I mean Gitcoin Grants are much too permissive.  They accept almost anyone.

For an example take a look at this NFT related project. [NFT Grant 3575](https://gitcoin.co/grants/3575/funding-for-creating-nfts) It provides almost zero info yet there is no reason to deny this grant which is backed by policy.  FDD Policy is aware of this shortcoming.

-------------------------

Huxwell | 2021-09-11 00:10:16 UTC | #3

@DisruptionJoe I like the method used by Protocol Labs(IPFS, FileCoin, etc) [proposal template here](https://github.com/filecoin-project/devgrants/blob/master/.github/ISSUE_TEMPLATE/opengrant.md) 
We can do something similar with 3 reviewers or more per pull request (a PR = a grant request).

The curation feature/dApp could use that as a grant request registry.

Adding on your questions:

Please describe in more detail why this proposal is valuable for the Gitcoin ecosystem or Public Goods. Answer the following questions:
- What are the benefits to getting this right?
- What are the risks if you don't get it right?
- What are the risks that will make executing on this project difficult?

Please describe in details what your final deliverable for this project will be. Include a specification of the project and what functionality the software will deliver when it is finished.

Please break up your development work into a clear set of milestones. This section needs to be very detailed (will vary on the project, but aim for around 2 pages for this section).
For each milestone, please describe:

- The software functionality that we can expect after the completion of each milestone. This should be detailed enough that it can be used to ensure that the software meets the specification you outlined in the Deliverables.
- How many people will be working on each milestone and their roles
- The amount of funding required for each milestone
- How much time this milestone will take to achieve (using real dates)
- Specify your team's long-term plans to maintain this software and upgrade it over time.
- Team members, Relevant Experience, Team code repositories

-------------------------

socal434 | 2021-09-11 07:49:11 UTC | #4

I think this is a very comprehensive form and would for sure help weed out anyone who is just trying to get some free money for a project they never really intend to deliver on. I mean look at the example provided by @David_Dyor , it is literally just one line asking for money to create NFTs so that he (or she) can sell the created NFTs on OpenSea.

-------------------------

php | 2021-09-11 13:26:09 UTC | #5

Good example (grant 3575), maybe just add a limit in web form:  text introduction no less than 200 (meaningful) words...

-------------------------

erich | 2021-11-16 20:12:49 UTC | #6

Here is a Pol.is conversation on this issue that we can leverage to find rough consensus with the community.

**Gitcoin Grant Approval Policy for DAOs**
Recently, there's been a rapid increase of DAOs (Decentralized Autonomous Organizations) with all kinds of missions and socio-technological mechanisms in the Ethereum ecosystem. Under which criteria should DAOs be allowed to receive funding in Gitcoin Grants rounds? Please feel free to discuss here: **https://pol.is/34rdajkfxk**.

-------------------------

David_Dyor | 2021-10-03 17:36:02 UTC | #7

My thoughts on this are evolving. What if we made no distinction between different types of applicants, individuals or a group of individuals, but we simply held them all to the same standard.

It seems like daos are becoming the new business model in web3.  We should probably allow them.

The real challenge is determining what proof is acceptable for an applicant, then requesting our applicants provide such a proof with their original application, so stewards and volunteers don't have to spend weeks chasing it down when they could be doing more productive things for the Dao.

-------------------------

erich | 2021-11-16 20:12:20 UTC | #8

Interesting @blazingthirdeye! Would you mind feeding this into https://pol.is/34rdajkfxk so we can see how much agreement the community shares relatedly?

-------------------------

David_Dyor | 2021-10-05 23:19:22 UTC | #9

You bet.  Done!  

Everyone go complete that survey linked by @erich please.  We want to know what everyone thinks.

-------------------------
