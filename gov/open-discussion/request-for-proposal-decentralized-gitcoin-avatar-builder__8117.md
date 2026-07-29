---
id: 8117
title: "Request for Proposal: Decentralized Gitcoin Avatar Builder"
slug: request-for-proposal-decentralized-gitcoin-avatar-builder
category: open-discussion
url: https://gov.gitcoin.co/t/request-for-proposal-decentralized-gitcoin-avatar-builder/8117
created_at: 2021-08-02T19:37:43.715Z
last_posted_at: 2021-08-14T18:08:18.797Z
posts_count: 2
views: 3014
like_count: 5
---

# Request for Proposal: Decentralized Gitcoin Avatar Builder

<https://gov.gitcoin.co/t/request-for-proposal-decentralized-gitcoin-avatar-builder/8117>
owocki | 2022-05-28 15:38:06 UTC | #1

Hello DAOfrens, 

This is request for someone to come up with a new decentralized experience for creating [Gitcoin-style avatars](https://gitcoin.co/onboard/profile?steps=avatar).

As we progressively decentralize Gitcoin, the Gitcoin Holdings company is interested in decentralizing the avatar builder.  

We build the avatar builder so that users could celebrate their uniqueness and have a cool way of showing off their individuality on the site.  As  

We also feel that there was a missed oipportunity here to leverage our [art assets](https://github.com/gitcoinco/web/tree/master/app/assets/v2/images/avatar3d) to ride the PFP boom, and perhaps fund public goods with the ETH received.

An ideal candidate would be have the following principles:
1. Simplicity - products that do ONE THING and do it WELL.
2. Antifragility - Well-documented Decentralized products that our community can run without the centralized company.
3. Modularity - products that easily unix-style interoperate with each other.

An ideal proposal would 

1. (at a minimum) 1:1 replicate the centralized experience at `https://gitcoin.co/onboard/profile?steps=avatar` but store the code/avatars in a decentralize way.
2. (at a maximum) create a new novel way to make these avatar's into PFPs and fund public goods with them.

Please include

1. Who are you
2. What is your proposal to build this
3. What is your timeline to build this
4. What do you need (funding, etc)

Please submit your proposal as a comment on the gov forum thread.

-------------------------

polats | 2021-08-14 18:08:18 UTC | #3

### Who Are You

Heyo @owocki and fellow Gitcoiners! I’m Paul Gadi, co-founder and CTO at [OPGames](https://opgames.org). We’re bridging game developers to Web 3.0 by building the open-source tools to make it as simple as possible for them to start integrating with the blockchain.

We’re calling these tools [Game Legos](https://youtu.be/9EF_hrmVMqM?t=224): in the same way that Money Legos was able to bring about the DeFi renaissance, we feel these Game Legos will be instrumental in bringing about the coming NFT Game revolution.

Game Legos are also perfectly in sync with the goals of this RFP. We’re building them open-source and as simple, robust, and composable as we can.

### What Is Your Proposal to Build This

OPGames has already started building an open-source PFP creator over at https://github.com/alto-io/game-legos/tree/avatar

![image|690x423, 100%](upload://c849YT0cPf927cuVKwRZnKtlW19.jpeg)

We’ve been building it on top of @austingriffith’s scaffold-eth. We believe Scaffold-eth is not only the framework with the most solid foundation but is also the fastest way for developers to get started in Web 3.0. It also has a strong community of builders behind it that we could tap to continue improving the project.

We’ve used some of the scaffold-eth code already to achieve some of the requirements in the RFP. It already stores the avatars in a decentralized manner via IPFS, and uses the example smart contracts to mint them as NFTs.

### What Is Your Timeline To Build This

A lot of the initial effort will be migrating over the frontend to scaffold-eth. After that we’ll integrate the PFP generation with the NFT minting contracts. Finally, properly documenting the project would also take some time.

An estimate would be **1 to 1.5 months**, depending on the code complexity.

### What Do You Need

1. Being able to consult with the original developer of the frontend would be great, so we can more easily address any issues with migrating over the code and also write solid documentation
2. OPGames can assign a team of developers on it for 5 ETH to build the initial version
3. We’d be interested in collaborating and exploring how to make the project sustainable even after the RFP. Perhaps we can build a DAO where all projects using it would donate a portion of their PFP sale to the DAO?

Thanks for reading, we're open to suggestions and comments!

-------------------------
