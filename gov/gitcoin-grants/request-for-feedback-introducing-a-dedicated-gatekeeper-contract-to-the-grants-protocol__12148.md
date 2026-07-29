---
id: 12148
title: "[request for feedback] Introducing a dedicated gatekeeper contract to the Grants Protocol"
slug: request-for-feedback-introducing-a-dedicated-gatekeeper-contract-to-the-grants-protocol
category: gitcoin-grants
url: https://gov.gitcoin.co/t/request-for-feedback-introducing-a-dedicated-gatekeeper-contract-to-the-grants-protocol/12148
created_at: 2022-11-28T21:38:55.546Z
last_posted_at: 2023-01-07T11:47:31.162Z
posts_count: 8
views: 2705
like_count: 22
---

# [request for feedback] Introducing a dedicated gatekeeper contract to the Grants Protocol

<https://gov.gitcoin.co/t/request-for-feedback-introducing-a-dedicated-gatekeeper-contract-to-the-grants-protocol/12148>
nategosselin | 2022-11-28 21:38:55 UTC | #1

Note: The design discussed below is a product of the Grants Protocol team: @thelostone-mc @hansmrtn @chibie @bhargavaparoksham Josef @melissa + @nategosselin 

The Grants Protocol team is close to wrapping up the [Quadratic Funding development work](https://www.notion.so/gitcoin/v1-Quadratic-Funding-Rounds-3f6b819df66247199ed05d3ee785558f) and have begun designing for the [Quadratic Voting outcome](https://www.notion.so/gitcoin/v1-Quadratic-Voting-Rounds-9e42b799e0bd4c25a4a2c9a364f7413d). A key concept that this work will introduce is how the protocol will allow communities to configure voter/donor eligibility. 

After several design sessions, we've coalesced around a solution where we introduce the concept of a "gatekeeper" contract into the protocol — this is a new contract that would live alongside the [current constellation that each round requires](https://github.com/gitcoinco/grants-round/tree/main/packages/contracts) (round core contract, voting contract, and payout contract). The benefit of setting this logic as a separate contract is modularity and flexibility — it gives the protocol a lot of room to develop new methods of voter eligibility without having to change other core contracts. The tradeoff is that it requires the deployment of another contract for each round.

We'd love to hear thoughts from the community on this: What do you think about having a standalone "gatekeeper" contract to handle voter eligibility?
[poll type=regular results=always chartType=bar]
* Yes — love this idea
* Not sold — we'd like for you to consider another approach
[/poll]

Thanks for sharing your thoughts!

-------------------------

kyle | 2022-11-28 21:47:37 UTC | #2

I love the solicitation on the design. Hopefully more folks chime in.

I have not deployed a round yet (looking forward to deploying one soon!) - do we know how much this might impact the cost of the round if we deploy, now four contracts, to mainnet?

Overall, I love the idea of compartmentalizing functionality and I think its great to pull out this piece to a *gatekeeper* contract. I am also not a smart contract dev, so I would love to get some feedback from a few other folks too :)

-------------------------

safder | 2022-11-28 22:27:16 UTC | #3

Echo the appreciation for soliciting community feedback on the design! 

I'll preface this by saying I'm also not a smart contract dev, so take this feedback with a grain of salt: 
* One other tradeoff I can think of is that this adds an additional potential point of failure/complexity that could break when Round Managers try to run their own rounds without developer help. 
* Could this not be achieved with some combination of interfacing/interaction between the existing contracts, and allowing enough flexibility in the parameters for each of those pieces instead of introducing a new contract? Modularity is great but so is making sure each piece communicates well with the whole.

-------------------------

alexdwagner | 2022-11-29 23:45:22 UTC | #4

Also not a smart contract dev, but wanted to echo @safder's comments about added complexity. I'm guessing Round Managers will be mostly non-technical and trying to put myself in their shoes(which is easy bc I'm not a dev! lol).

I'm also curious how this will work with Passport? Is this something that might be rolled into Passport at some point?

The way I understand it is that Passport handles identity verification, and the Gatekeeper contract handles eligibility. How would they work together?

-------------------------

nategosselin | 2022-12-01 13:59:27 UTC | #5

Thanks for the feedback everyone! Glad to hear that you like this kind of feedback format. Here are some thoughts to specific questions.

From @kyle:
> do we know how much this might impact the cost of the round if we deploy, now four contracts, to mainnet?

Good question! We have not done a formal analysis of deployment cost yet, but it's on our radar. Our goal is to make sure that this is an affordable process for communities. 

From @safder:
> One other tradeoff I can think of is that this adds an additional potential point of failure/complexity that could break when Round Managers try to run their own rounds without developer help.

We're designing with non-technical communities in mind and are building our contract structure alongside a UI that handles all of this. Non-technical communities won't have to worry about figuring out the underlying contracts.

From @alexdwagner:
> I’m also curious how this will work with Passport? Is this something that might be rolled into Passport at some point?

We actually designed this with Passport in mind! By pushing the logic to the Gatekeeper contract, you have the flexibility to say things like "use Passport for gatekeeping" or "only allow holders of XYZ NFT to vote".

-------------------------

DisruptionJoe | 2022-12-02 14:24:42 UTC | #6

Really happy to see this being shared in this way. Thanks Nate! I'm supportive of modularity as a driving principle. I'm not yet aware of any tradeoffs where I wouldn't preference modularity at this point.

[quote="nategosselin, post:5, topic:12148"]
Good question! We have not done a formal analysis of deployment cost yet, but it’s on our radar. Our goal is to make sure that this is an affordable process for communities.
[/quote]

Would this contract be a mandatory part of deploying any round or optional?

-------------------------

thelostone-mc | 2023-01-07 07:24:41 UTC | #7

[quote="DisruptionJoe, post:6, topic:12148"]
Would this contract be a mandatory part of deploying any round or optional?
[/quote]

This would be optional as we would have voting strategies which might not require an gatekeeper (like qf) 

[quote="alexdwagner, post:4, topic:12148"]
I’m also curious how this will work with Passport? Is this something that might be rolled into Passport at some point?
[/quote]
Oh yeah so thinking out loud on this 

 **Scenario :**
We are building a gatekeeper layer into the protocol which serves as an eligible voter list. We'd end up supporting different gatekeeper strategies one of them being passport gatekeeper 

**Flow:** 
Round creator creates a round -> selects the passport gatekeeper strategy -> where they would provide min score/some other attribute Anytime a voter wants to vote -> the frontend would talk to the gatekeeper contract -> which would talk to passport contract to fetch the score and return if user can vote / not (edited)

The beauty of the design is that -> we can build out different flavours of it.
To the round operator -> it's just a matter of choosing if they want to use a gatekeeper and if so which one and provide data for it

-------------------------

ZER8 | 2023-01-07 11:54:43 UTC | #8

Hello and HNY everyone :sparkles:

Thanks for sharing this with the Gitcoin community, this is a novel approach and as a steward and ex contributor I honestly trust the GP team decision to create a "gatekeeper" contract.

I think the feedback depends on the POV of the person reading. If you are a Gitcoin contributor you may have a different opinion from a round manager. Because there are more types of round managers( some representing big orgs, some will be people like me who want to experiment and support PGs and people that build for the common good)  an interesting idea would be to ask potential round owners for feedback also (if you believe it would be valuable) and try to learn from their collective opinions, but I guess that is kinda out of the scope of this post.

But, as Kyle said above, the costs will be the main interest of people that want to create small rounds. Some rounds may only distributed thousands of dollars, a cost of deployment of over 100$(mainet) can be an issue for those who are just starting out.

Update: It's cool 2 see that the contract is optional. :robot:

-------------------------
