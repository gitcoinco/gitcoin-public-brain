---
id: 10721
title: "Upgrading the Gitcoin Governance Contracts"
slug: upgrading-the-gitcoin-governance-contracts
category: governancevision
url: https://gov.gitcoin.co/t/upgrading-the-gitcoin-governance-contracts/10721
created_at: 2022-05-26T13:05:13.172Z
last_posted_at: 2022-06-01T16:04:17.943Z
posts_count: 5
views: 3156
like_count: 7
---

# Upgrading the Gitcoin Governance Contracts

<https://gov.gitcoin.co/t/upgrading-the-gitcoin-governance-contracts/10721>
phutchins | 2022-06-01 17:22:16 UTC | #1

In its humble beginnings, the Gitcoin DAO deployed the Governor Alpha contract to manage the DAOs treasury. As we have grown as a DAO we have learned more about our needs from governance. Since the initial deployment, some significant improvements have been made to the available governance contracts which either solve or reduce the inconvenience of the problems that we have experienced. Additionally, there are changes that we can make prior to upgrading our governance contracts that will have a positive impact on the DAO as a whole with little effort.

Here, I will identify the issues that have been experienced and propose a multi stage plan for getting to a better place.

**Issues Experienced**

1. The unnecessary delay on our timelock extends the amount of time it takes to turn around budget requests
2. 1MM votes as a requirement for creating a proposal restricts proposal creation more than necessary and creates a bottleneck slowing down our progress
3. In addition to the above, only one active proposal can be created by someone with 1MM votes
4. Minimum vote threshold of 2.5MM GTC votes is not adjustable with the current contract
5. Delegation that happens after a proposal is made is not considered for that vote (even though we might want it to be… ie, Someone makes a proposal, a steward’s position is then known, I want to change and revoke my delegation to that steward)
6. When a steward needs to step away for a period of time, it is costly both financially and operationally for token holders to re-delegate

**Solution Steps & Timeline**

Let’s walk through these issues one at a time and identify short and long term solutions where appropriate.

**For #1**, fortunately there is an easy short term solution available. We will simply create a proposal to adjust the delay on our time lock to a very small time period. Longer term solutions would include upgrading the time lock and keeping a short time period which would also give us the added benefit of being able to point multiple governance contracts at a single timelock if we ever desired.

**For #2-4**, we should upgrade from Governor Alpha to Open Zeppelins implementation of Governor Bravo. Not only will this solve problems #2-4 by adding configurability to these parameters, but it will add upgradability to our Governance contract making for a much smoother process in the future when subsequent upgrades are desired as well as other features that may prove useful in the future.

To test this, we will deploy an instance of the Governor Bravo contract and point it to our token. There is a handy wizard provided by OpenZeppelin which makes it nice and easy to select the various governance components that we would like to utilize. We can deploy a duplicate version of our existing time lock and fund it with a minimal amount of tokens. Tally allows for adding test contracts so that we will be able to test the process end to end through the real Tally interface.

OpenZeppelin Wizard - https://docs.openzeppelin.com/contracts/4.x/wizard

Tally - https://withtally.com

**For #5**, even though this seems like a desired change, removal of the delegation changes lock after a proposal is submitted creates a vulnerability.

**For #6**, there does not currently appear to be a solution for this problem. We will put this in the “Future” bucket and connect with Open Zeppelin to brainstorm around how this problem could be solved.

**In short, this post proposes that we execute the following plan.**

*Immediately* - Reduce the delay on our timelock via governance proposal

*30 Days* - Conduct thorough testing using the new Governor Bravo

*90 Days* - Completed update of the Governance Contracts

*Future* - Continue to address friction, bottlenecks, and needs

**Q&A**

*How does this affect me?*

Token Holder - No action is required

Steward - No action is required

Proposal Creation - There may be some down time on Tally while the interface is migrated to the new governance contract but the experience should remain nearly the same

*What will the transition from Alpha to Bravo be like?*

The transition should be mostly seamless with the significant changes being behind the scenes on Tally. There may be a short period of down time on Tally while we transition from the old contract to the new. After this transition, users should see the newly available features from Governor Bravo.

*What new features does governor Bravo provide?*

* Ability for voters to abstain transparently
* Ability to add textual reason to your vote
* Upgradability path for future upgrades
* Ability to cancel unwanted proposals instead of voting no
* A review/analysis period allowing holders to review the proposal

*Should we upgrade the timelock contract?*

Upgrading the timelock contract would pose the most difficulty among all of the upgrades that we have covered here. I see no urgent immediate need to upgrade within the next 90 days and propose that we bring this topic up for review after executing our 90 day Alpha to Bravo upgrade plan.

**Wrapping up...**

Before we move forward, let’s discuss any thoughts or concerns about this approach and the changes that come along with it. Throughout the process we considered the leading governance contract options such as Compound, OpenZeppelin, Moloch, and Aave and feel strongly that this path is the best way to go forward.

-------------------------

bobjiang | 2022-05-26 14:41:48 UTC | #2

Thanks a lot for this upgrading, there are lots of work @phutchins 

Would I have another issue to be fixed in this upgrade or in future?

The issue is:

If a new GTC holden buy $GTC from market, (let's say it's a new wallet address)
after the transaction succeeded, the new user cannot vote anything, unless they delegate to themselves explicitly. 

so could the new user get the voting power automatically after the tx is successful?

[I have got several new users report in support]

-------------------------

Fred | 2022-05-29 08:36:49 UTC | #3

Amazing to see this take shape. I’m very much in favor of upgrading to OZ Bravo.

[quote="phutchins, post:1, topic:10721, full:true"]
*Should we upgrade the timelock contract?*

Upgrading the timelock contract would pose the most difficulty among all of the upgrades that we have covered here. I see no urgent immediate need to upgrade within the next 90 days and propose that we bring this topic up for review after executing our 90 day Alpha to Bravo upgrade plan.
[/quote]

Don't we need to move all funds over from the Gov Alpha timelock to the new Gov Bravo contract in order to use the benefits?

-------------------------

phutchins | 2022-06-01 16:01:50 UTC | #4

This is a great callout and definitely would be nice if there were a built in solution. The current state of things however is that in order to avoid costly transfers, voting is not done based on token balance but by delegating explicitly instead.

https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.6.0/contracts/token/ERC20/extensions/ERC20Votes.sol#L22

We could do more research here but we would likely need to migrate to another token with the current features available.

The best we can currently do is to make it as easy as possible in the voting tools to have insight into delegation status and make it easy to delegate to self.

-------------------------

phutchins | 2022-06-01 16:04:17 UTC | #5

With the ability to adjust the waiting period for the time lock to a very low number (we will confirm what the shortest time period is), there shouldn't be an immediate need to migrate funds from one time lock to another. From my current understanding, the current time lock will work with Gov Bravo. We will of course confirm this in our preliminary testing.

-------------------------
