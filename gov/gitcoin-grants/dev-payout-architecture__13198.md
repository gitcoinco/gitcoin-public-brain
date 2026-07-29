---
id: 13198
title: "Dev: payout architecture"
slug: dev-payout-architecture
category: gitcoin-grants
url: https://gov.gitcoin.co/t/dev-payout-architecture/13198
created_at: 2023-03-07T14:49:00.959Z
last_posted_at: 2023-03-07T14:49:01.096Z
posts_count: 1
views: 2118
like_count: 5
---

# Dev: payout architecture

<https://gov.gitcoin.co/t/dev-payout-architecture/13198>
thelostone-mc | 2023-03-07 14:52:44 UTC | #1

Hey, 

thelostone-mc (Aditya) here who's a team lead on the Allo Protocol team. 
Based on recent feedback from the governance post, I'd like to experiment by bring the community into the dicussion / sharing our thoughts as we build out milestones. Consider this a quick checkin from the Allo team with the community and keeping you in loop as we brainstorm and build feature. Would love feedback on this so that we can improve on this.


TLDR: We are building the payout layer onto the allo protocol and would love to share how we are going about it in an effort to be more vocal about how are progressing the protocol. All our discussion / code / issues are open source and on Github, so if you'd like to be more involved -> that's the place I'd encourage you to checkout 


# Payout Flow Architecure
This document aims to outline the design for 

- Payout architecture
- Protocol + Round Fee architecure 


## Payout Architecture 

The payout contract like the voting contract can come in variations of flavours such as:

- Bulk Transfer Payout
- Merkle Claim
- Drip Transfer

### What are we building

The Allo team will focus on defining the interface of the PayoutStrategy (called IPayoutStrategy) via an abstract contract. Any flavour of PayoutStrategy being built would have import this abstract interface contract and that would be able to leverage :  

- core function defined in the IPayoutStrategy
-modifiers which may be useful for the actual implementation
- virtual functions which would have to be implemented by the implementation

We will be using the IPayoutStrategy to build the MerklePayoutStrategy as our first flavour of payout
This would be used as the initial payout mechanism for the rounds run on Allo and would serve as an example for other flavours to be built.


### How are these contracts deployed?

The actual PayoutStrategy itself would follow a factory pattern.
This means every payout strategy would comprise of 2 contracts maintained by the Allo Team 

- **PayoutStrategyFactory contract** (creates PayoutStrategyImplementation for every round)
- **PayoutStrategyImplementation contract** (containing the actual payout implementation)

This is similar to the design of the Round, Program, and QFVotingStrategy is built.
This allows us the benefits of :

- Isolate payout contracts per round
- Creating clones of the payout contract (making deployment cheaper for round operator)
- Give us room to upgrade our contracts as the protocol evolves


### Functions offered by the IPayoutStrategy

- **isReadyForPayout** : function which prevents updating the distribution and signals it's ready for payout
- **withdrawFunds**: function which enables an operator to withdraw pot money. 
- **updateDistribution**: TBD by the actual PayoutStrategyImplementation
- **payout**: : TBD by the actual PayoutStrategyImplementation


## Fee Architecture 

This while a separate feature goes hand in hand with payout and hence is being together.
The v1 iteration aims to build the foundation which allows 

- Protocol to set fee percentage (initially set to 0). This would be updatable by the DAO 
- Operator to add round fee percentage which can be updated till the round ends (we will make the update timeline stricter after we launch this feature )
- Both fees are collected at the time of payout
- funds would be kept in the round contract and sent to the payout contract at the time of payout (this is solely done to support native token payouts as well )

Once we've built this layer out, and run a test, we'll evolve this feature and add restrictions in terms of updating fee percentage. 

### Are the current contracts being upgraded?

Yes, the following contracts would need to be updated to build out the flow : 

- **RoundFactory** - to set the protocol treasury address
- **RoundImplementation** - to charge the protocol fee and invoke PayoutStrategy payout function

Any changes will be documented and will be backward compatible:

**The overall flow:** 

![image|690x308](upload://7Nmb3DJsCDA15209M7dHQ0DR38h.jpeg)

**High level overview of the payout interface:**

![image|690x362](upload://uHNvCgHdlKSlNqDSciNIOhA9gTO.jpeg)



The actual flow which we've brainstormed can be found here:
https://miro.com/app/board/uXjVPsZg30I=/?share_link_id=561484071436

-------------------------
