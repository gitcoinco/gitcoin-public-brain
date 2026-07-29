---
id: 12204
title: "[feedback] Upgrading the Gitcoin Governor Contracts - Flexible Voting?"
slug: feedback-upgrading-the-gitcoin-governor-contracts-flexible-voting
category: governancevision
url: https://gov.gitcoin.co/t/feedback-upgrading-the-gitcoin-governor-contracts-flexible-voting/12204
created_at: 2022-12-01T15:47:21.136Z
last_posted_at: 2023-04-03T22:46:19.994Z
posts_count: 23
views: 4441
like_count: 35
---

# [feedback] Upgrading the Gitcoin Governor Contracts - Flexible Voting?

<https://gov.gitcoin.co/t/feedback-upgrading-the-gitcoin-governor-contracts-flexible-voting/12204>
kyle | 2022-12-01 15:47:21 UTC | #1

Hey Everyone - I have some excited news to share, and I would love to solicit feedback before we get too far along on a few of our Governor upgrade details.

After a couple of [false starts](https://gov.gitcoin.co/t/upgrading-the-gitcoin-governance-contracts/10721), we are about 2/3rds of the way done in scoping the [new Governor Contracts](https://github.com/gitcoinco/2022-Governor-upgrade) for the Gitcoin DAO and Treasury. These contracts are being developed by our friends and partners at [ScopeLift](https://www.scopelift.co/). These folks have worked with Gitcoin for years and have helped us build a number of other products. They have also been championing [flexible voting](https://gov.gitcoin.co/t/introducing-flexible-voting-an-extension-to-the-governor-enabling-new-voting-mechanisms/11115) for DAOS and worked with Uniswap to introduce this concept.

Okay, so the exciting news! We are about 2/3rds of the way done and we have a few questions we would love community feedback on. If you can answer the poll, it would be greatly appreciated, but we are essentially looking for feedback on if Flexible Voting should be implemented as part of this governor upgrade, or if we would like to "play it safe" and avoid allowing the voting mechanism. From @bendi - "Flexible Voting allows for the construction of new mechanisms which make governance participation easier, cheaper, and more accessible for GTC holders."

You should really checkout the post linked above what flexible voting is, but to save a few clicks, here is a great graphic outlining the benefits of it. Essentially flexible voting enables Snapshot strategies. Those who have GTC staked in an LP can still use that GTC to vote for on-chain proposals.
![flex-voting-diagram|690x388](upload://t7GK8vdM1ieF2z0DR5VgjJPZbCt.png)

We are about to start testing the new contracts and will have more info to share on those soon, but we hope to have a vote live in January to upgrade the governor contracts from the Governor Alpha we have today, to an Open Zepplin Variant of Governor Bravo. I can share more of the contract details in a subsequent post soon (ie, if threshold amounts changes are proposed, quorum numbers, etc.)

For now, give me your thoughts on flexible voting!
[poll type=regular results=always chartType=bar]
* Yes - Flexible Voting is important to our Governance
* No - Flexible Voting doesn't seem necessary and we should skip it.
[/poll]

-------------------------

shawn16400 | 2022-12-01 16:56:57 UTC | #2

Just catching up on this concept and it looks appealing.  @bendi if you need help in scenario development or testing, let me know - I would be happy to help!

-------------------------

krrisis | 2022-12-08 22:52:43 UTC | #3

An open tab that I missed here - I voted no here because we mainly use Tally for transferring funds, not so much for voting itself, so not sure it is needed.

-------------------------

kyle | 2022-12-09 15:23:38 UTC | #4

I appreciate the reply and the consideration.

I was of the same mindset as you Kris, but then I wondered if having that option would still be important for those who dont want to hold GTC in a wallet. ie, large token holders could move tokens to Aave and then still help us ratify snapshot results.

I like that it gives folks more options on how to hold their GTC.

-------------------------

DisruptionJoe | 2022-12-09 17:18:21 UTC | #5

Not sure if I understand it correctly, but I believe the delegation happens on Tally for both Tally and snapshot. Therefore, the upgrade to flexible voting would make it easier for us use tokens for governance while also using them for other productive use cases. 

I would also like to propose that we should add some type of either
1) Expiration of delegations
2) Ability for someone to drop their delegations if they no longer want to participate

-------------------------

kyle | 2022-12-09 17:35:33 UTC | #6

I love these ideas. I can check to see if those are available options.

@bendi to perhaps chime in... and @mds1

-------------------------

bendi | 2022-12-12 16:39:22 UTC | #7

Hey @kyle, thanks for getting this conversation started, and thanks for your patience in my reply! Has been a busy few weeks for us :sweat_smile:

You did a great job summing up what Flexible Voting is all about. We think being able to participate in both DeFi (with your GTC) and governance at the same time is a compelling use case and we recently [received](https://twitter.com/AaveGrants/status/1570431140389097473) a grant from Aave Grants DAO to add Flexible Voting support to ATokens. We expect the work will be done early next year.

One note I want to add: while depositing tokens in DeFi protocols is *one* of the use cases we imagine, there are a lot more, and some of them are just as exciting—if not more so. A couple I'm really excited about are Layer 2 voting (bridge your GTC to a rollup, vote from the rollup with low gas fees) and shielded voting (deposit your GTC to a pool and vote privately with ZKPs).

[quote="shawn16400, post:2, topic:12204, full:true"]
Just catching up on this concept and it looks appealing. @bendi if you need help in scenario development or testing, let me know - I would be happy to help!
[/quote]

Sure let's chat. Will follow up!

[quote="krrisis, post:3, topic:12204, full:true"]
An open tab that I missed here - I voted no here because we mainly use Tally for transferring funds, not so much for voting itself, so not sure it is needed.
[/quote]

Hey @krrisis, thanks for your thoughts! I'm not quite sure what you mean here regarding Tally and transferring funds. Happy to expand if you have any specific questions. That said, we've been in touch with the folks at Tally (they rock!) and they've [signaled](https://docs.tally.xyz/user-guides/tally-contract-compatibility/flexible-voting-extension) their support for the FV mechanism, and even a willingness to support it in their tooling should a DAO request it!

[quote="DisruptionJoe, post:5, topic:12204"]
Therefore, the upgrade to flexible voting would make it easier for us use tokens for governance while also using them for other productive use cases.
[/quote]

Yep! That's exactly right @DisruptionJoe 

[quote="DisruptionJoe, post:5, topic:12204"]
Expiration of delegations
[/quote]

This is an interesting idea! Since delegations happen inside the GTC contract, not the Governor contract, the only way to add this by default would be to migrate the community to a new version of GTC. That said, with Flexible Voting, you could design a delegate contract that sub-delegated to regular voters, and included configurable expiration by default. In other words, with Flexible Voting you could build an *opt-in* version of this.

[quote="DisruptionJoe, post:5, topic:12204"]
Ability for someone to drop their delegations if they no longer want to participate
[/quote]

As it stands now anyone can revoke a delegation by re-assigning it at anytime, including to themselves or to no one. So I think this basically exists already. Unless I'm misunderstanding what you mean?

Anyway if anyone else has other questions about either the Governor upgrade or Flexible Voting, please hit me up! I'll be keeping an eye out for replies :slight_smile:

-------------------------

DisruptionJoe | 2022-12-12 19:28:24 UTC | #8

[quote="bendi, post:7, topic:12204"]
As it stands now anyone can revoke a delegation by re-assigning it at anytime, including to themselves or to no one. So I think this basically exists already. Unless I’m misunderstanding what you mean?
[/quote]

As a steward who is receiving delegations, I no longer wish to participate in this ecosystem and would like to release all delegations that are currently assigned to me.

-------------------------

bendi | 2022-12-14 15:42:53 UTC | #9

[quote="DisruptionJoe, post:8, topic:12204"]
As a steward who is receiving delegations, I no longer wish to participate in this ecosystem and would like to release all delegations that are currently assigned to me.
[/quote]

Ohh interesting I see what you mean now—the *steward* removing other delegations. I'm curious about the motivation for this feature. Like a ragequit kind of thing?

Thinking about the implementation, similar to the idea of expiring delegates, I believe to implement this globally you'd have to migrate the community to a new version of GTC. But I believe, off the top of my head without thinking about it *too* deeply, it could also be built as an *opt-in* feature with Flexible Voting. Great example of how this new primitive will allow the building of all kinds of new stuff by 3rd party devs, including things we haven't conceived of yet!

Edit: Grammar

-------------------------

DisruptionJoe | 2022-12-14 18:36:51 UTC | #10

This request came from a specific incident. One steward of ours who was also a steward from ENS was offered a full time position with Gitcoin. They posted on ENS about the offer and that they no longer could put the time and attention to being a good steward, but not many read it. 

A while later they were confronted at a conference from an ENS fan/user who was upset that stewards with large delegations, this person specifically, were not paying attention. 

This steward had no ability to say "My priorities have changed and I can no longer serve in this role"

-------------------------

bendi | 2022-12-15 14:59:32 UTC | #11

[quote="DisruptionJoe, post:10, topic:12204"]
This steward had no ability to say “My priorities have changed and I can no longer serve in this role”
[/quote]

Yeah this makes sense. Like I said, a great example of how FV can be used to build lots of stuff. In the future I can imagine that the large majority of base delegations will be to contracts that come with their own sets of rules and features like this. It allows innovation in the way delegation works without having to ever upgrade the token contract!

-------------------------

chaselb | 2022-12-19 17:51:21 UTC | #12

I like this concept as it stands. I think it adds a lot of, well, flexibility. I think a more balanced decision could be made on whether or not we should upgrade though if we got a full understanding of the risks of updating. How battle-tested is the flexible voting contract? What new attack vectors do we open ourselves up to? How much more context does this require of the average voter (i.e., does this add a lot of complexity that would require some of our non-technical voters to read up on?).

Also, another separate question that I'm curious about, does this allow me to give GTC to someone while keeping the voting power without their knowledge? As in, could I give my GTC to person A, but beforehand delegate the votes to contract B without person A's knowledge?

-------------------------

bendi | 2022-12-20 14:43:16 UTC | #13

Hey @chaselb, these are all *great* questions! Let me try to take them one or two at a time!

[quote="chaselb, post:12, topic:12204"]
How battle-tested is the flexible voting contract? What new attack vectors do we open ourselves up to?
[/quote]


Flexible Voting is an extension of the battle tested OpenZeppelin Governor. The OZ Governor is audited and used by many DAOs. Our extension is minimal and can be be seen [here](https://github.com/ScopeLift/flexible-voting/blob/master/src/GovernorCountingFractional.sol). A good chunk of the code in that contract is itself borrowed from other OZ extensions. Overall the "new code" is extremely minimal, which is by design! All that said, we are also pursuing an audit for the extension, with funding being the biggest blocker.

[quote="chaselb, post:12, topic:12204"]
How much more context does this require of the average voter
[/quote]

The short answer is none. If a holder or voter is happy with the way things currently work, then no change would be required in their behavior. The FV system is fully backwards compatible with the existing Governor and so voting and delegating can continue as-is. Where a user might need to think a bit is if they choose to opt-in to something built with FV that enables a new experience.

For example, we're currently finishing up AToken support for FV with a grant from Aave. This would theoretically allow depositing your GTC into Aave, but still voting with your share of the unborrowed Pool. Obviously, a new UX will have to be built for this, and obviously we'll want to keep that UX as clean and simple as possible. But all of that is purely on an opt-in basis.

[quote="chaselb, post:12, topic:12204"]
does this allow me to give GTC to someone while keeping the voting power without their knowledge? As in, could I give my GTC to person A, but beforehand delegate the votes to contract B without person A’s knowledge?
[/quote]

Nope! Delegation is done in the GTC Token contract, which would change, so the rules around delegation don't change either. When you transfer your GTC, your delegation (whether to an EOA or to a contract) is reset.


Edit: clarity

-------------------------

chaselb | 2022-12-20 15:17:39 UTC | #14

[quote="bendi, post:13, topic:12204"]
Our extension is minimal and can be be seen [here](https://github.com/ScopeLift/flexible-voting/blob/master/src/GovernorCountingFractional.sol). A good chunk of the code in that contract is itself borrowed from other OZ extensions. Overall the “new code” is extremely minimal, which is by design! All that said, we are also pursuing an audit for the extension, with funding being the biggest blocker.
[/quote]

Okay so just to be clear, the proposed extension is currently unaudited, and not currently implemented by any other major DAOs?

[quote="bendi, post:13, topic:12204"]
For example, we’re currently finishing up AToken support for FV with a grant from Aave. This would theoretically allow depositing your GTC into Aave, but still voting with your share of the unborrowed Pool.
[/quote]

Also, this leads me to a belief that in order for users to get benefits from the type of examples listed above for FV, the actual lending protocols would have to add some sort of functionality on their end. Is this correct?

-------------------------

bendi | 2022-12-21 16:23:27 UTC | #15

[quote="chaselb, post:14, topic:12204"]
Okay so just to be clear, the proposed extension is currently unaudited, and not currently implemented by any other major DAOs?
[/quote]

Yep, the new code is not yet audited (working on it) and not yet used by a major DAO.

[quote="chaselb, post:14, topic:12204"]
Also, this leads me to a belief that in order for users to get benefits from the type of examples listed above for FV, the actual lending protocols would have to add some sort of functionality on their end. Is this correct?
[/quote]

Correct. In the case of Aave, they'd have to deploy an FV compatible AToken for GTC, or any other Governance token. They've given us a grant to write said AToken contract, which should be [done soon](https://github.com/ScopeLift/flexible-voting/pull/21).

In general, we're very aware that the project has a bootstrapping problem, i.e. a chicken-and-the-egg style issue. We're aggressively attacking this from every angle, as we [discussed](https://www.scopelift.co/blog/introducing-flexible-voting) in the blog post, to try to get the activation energy needed.

We believe the adoption of FV will be a big unlock for the ecosystem, and in the spirit of Public Goods we're trying to make it happen with grant funding and community support! We've had a number of parties express [support](https://docs.tally.xyz/user-guides/tally-contract-compatibility/flexible-voting-extension) for the extension, and should have some more announcements to share in this regard soon.

Gitcoin has often been a leader in adopting new tech in the ecosystem. ScopeLift helped build the zkSync integration into Gitcoin Grants back when zkSync was the *only* rollup live in production, and had less than $100K in funds on the network. I think it's fair to say that decision by Gitcoin was an inflection point for Ethereum's L2 ecosystem. We hope the Gitcoin community will see this as an opportunity to once again be leaders the ecosystem.

-------------------------

bendi | 2023-02-02 22:40:54 UTC | #16

For anyone interested, we just shared a blog post about our integration of Flexible Voting with Aave, which is now completed:

https://twitter.com/ScopeLift/status/1621275019929059329

-------------------------

kyle | 2023-02-06 20:12:10 UTC | #17

Thanks, Ben.

As an FYI on progress for others. We have been making progress on adopting this and will likely move to change out the contracts after Eth Denver. we are delaying our roll out a bit as we want to make sure Tally.xyz can support the new contract details too.

You can see the repo here: https://github.com/gitcoinco/Alpha-Governor-Upgrade

-------------------------

bendi | 2023-02-07 14:57:58 UTC | #18

Yes! Thanks Kyle. A couple other notes that folks might be interested in:

* The Flexible Voting extension is being audited by OpenZeppelin at the end of the month. We'll of course make the full report public when the process is over.
* I'll be speaking on Flexible Voting and what the upgrade would mean for the DAO at Schelling Point :)

-------------------------

bendi | 2023-03-07 21:33:15 UTC | #19

Thanks to the community members who came to my Schelling Point talk. I'll post the video once it's available as well.

After the talk, I had a great brainstorm with a few folks about even more cool stuff that can be built with Flexible Voting. People keep coming up with cool new things that could be built, including:

* A chained delegation scheme where voting weight follows a chain of delegation until someone in the chain votes
* An incentivized voting scheme where anyone who fails to vote loses a small amount of their stake, which is given to those who did vote
* An opt-in doxxed voting pool (for sybil resistance) where votes are amplified quadratically with a pool of token weight delegated by the DAO or another whale

There was a lot of interest for Flexible Voting at ETHDenver from other DAOs as well. Our audit with OpenZeppelin starts this week, and I'll share updates on that as it progresses. There's a lot of momentum building for more modular governance! We're excited to get the proposal up for the Gitcoin community later this month!

-------------------------

shawn16400 | 2023-03-08 10:03:06 UTC | #20

Hey Ben, 
After your presentation, I spoke with several other governance architects about the capability and there was broader interest beyond Gitcoin.  Specifically @mmurthy at https://www.karmahq.xyz/, the folks at the [DAO Governance Collective](https://twitter.com/DAOgovernance) and [mel.eth](https://twitter.com/emjicy) who has some interesting delegation ideas where this could be put to work.  Ping me in discord and let's continue the conversation  shawn16400#5507

-------------------------

bendi | 2023-03-08 16:11:03 UTC | #21

Amazing! Thanks so much. Friend request sent on Discord.

-------------------------

kyle | 2023-04-01 12:00:51 UTC | #22

Hey all - one more update!

We are getting close to our deploy and testing phase. This means, contracts have been audited, settings have been set (currently no planned changes to the governor options), and we are getting ready to start our testing. We will deploy the new contracts and expose those so that we encourage additional testing :pray: 

Stay tuned for more details next week!

-------------------------

bendi | 2023-04-03 22:46:19 UTC | #23

Hey everyone, as @kyle said, we've completed the audit of Flexible Voting Governor with OpenZeppelin, and [the results](https://blog.openzeppelin.com/scopelift-flexible-voting-audit/) are now available for public review. Only a few low severity issues were identified and all have been fixed.

Later this week, we'll be deploying the prospective new Governor for Gitcoin and sharing the upgrade proposal with the community to begin the formal governance proposal.

You can read about the audit and everything else going on with Flexible Voting (there's a bunch!) in this Twitter thread we just shared:

https://twitter.com/ScopeLift/status/1643018667972788224

-------------------------
