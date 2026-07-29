---
id: 8115
title: "Request for Proposal: Decentralize Gitcoin Kudos"
slug: request-for-proposal-decentralize-gitcoin-kudos
category: open-discussion
url: https://gov.gitcoin.co/t/request-for-proposal-decentralize-gitcoin-kudos/8115
created_at: 2021-08-02T19:22:42.856Z
last_posted_at: 2022-03-16T03:35:35.098Z
posts_count: 7
views: 5584
like_count: 27
---

# Request for Proposal: Decentralize Gitcoin Kudos

<https://gov.gitcoin.co/t/request-for-proposal-decentralize-gitcoin-kudos/8115>
owocki | 2022-05-28 15:38:06 UTC | #1

Hello DAOfrens, 

This is request for someone to come up with a new decentralized experience for managing Gitcoin.co/Kudos

As we progressively decentralize Gitcoin, the Gitcoin Holdings company is interested in decentralizing the Kudos experience from our [centralized codebase](https://github.com/gitcoinco/web/) to a decentralized frontend.

NOTE: Kudos is already a ERC-721-style NFT with a [smart contract](https://github.com/gitcoinco/Kudos721Contract), so the bones are already in place.

An ideal candidate would be have the following principles:
1. Simplicity - products that do ONE THING and do it WELL.
2. Antifragility - Well-documented Decentralized products that our community can run without the centralized company.
3. Modularity - products that easily unix-style interoperate with each other.

Gitcoin Holdings will provide a database backup of any centralized information (Kudos Images, metadata) needed to make a great Kudosexperience to a winning proposal.

Would any of you be interested in developing a decentralized Kudos? If so please submit a proposal by September 15th 2021.  

Use cases to include in the proposal:
1. view kudos on marketplace
2. send a kudos (xdai or mainnet)

Use cases that are NOT important for the first build out but could be built out later.
1. bulk airdrop of kudos
2. view who else holds a Kudos
3. indirect send of kudos
4. new kudos creation form

Please include

1. Who are you
2. What is your proposal to build this
3. What is your timeline to build this
4. What do you need (funding, etc)

Please submit your proposal as a comment on the gov forum thread.

-------------------------

polats | 2021-08-14 19:59:24 UTC | #2

### Who Are You

Heyo [@owocki](https://gov.gitcoin.co/u/owocki) and fellow Gitcoiners! I’m Paul Gadi, co-founder and CTO at [OPGames](https://opgames.org/). We’re bridging game developers to Web 3.0 by building the open-source tools to make it as simple as possible for them to start integrating with the blockchain.

We’re calling these tools [Game Legos](https://youtu.be/9EF_hrmVMqM?t=224): in the same way that Money Legos was able to bring about the DeFi renaissance, we feel these Game Legos will be instrumental in bringing about the coming NFT Game revolution.

Game Legos are also perfectly in sync with the goals of this RFP. We’re building them open-source and as simple, robust, and composable as we can.

### What Is Your Proposal to Build This

Same as our [PFP proposal](https://gov.gitcoin.co/t/request-for-proposal-decentralized-gitcoin-avatar-builder/8117), we believe this should be built as a Game Lego on top of [@austingriffith](https://gov.gitcoin.co/u/austingriffith)’s scaffold-eth. We believe Scaffold-eth is not only the framework with the most solid foundation but is also the fastest way for developers to get started in Web 3.0. It also has a strong community of builders behind it that we could tap to continue improving the project.

To increase antifragility and modularity we’re considering building the Kudos on top of [Rarible’s new open-source and cross-chain protocol](https://rarible.medium.com/introducing-the-rarible-protocol-an-open-source-cross-chain-tool-for-nft-innovation-318f7c7fb4f0).

### What Is Your Timeline To Build This

The first version will focus only on the marketplace integration and minting + sending kudos.

First step would be to create the new smart contracts on the Rarible protocol. Next would be to test and migrate some of the current kudos to a testnet, perhaps redeploy the assets into decentralized storage, and then make sure they appear on all the supported marketplaces. Finally we can then create a sample UI on scaffold-eth for minting kudos and sending them to other wallets.

An estimate would be about 1 month, barring any smart contract compatibility issues.

#### Enhancing the Kudos Experience

We also have some ideas on how to improve adoption of Kudos which also address the future use cases.

1. Minting scripts should be created for not just xDAI but also other layer 2s to give minters the lowest cost options possible.
2. An open-source widget should be created to allow builders to easily integrate Kudos into their games or apps, something similar to [Opensea’s Embed Collection Feature](https://docs.opensea.io/docs/11-embedding-your-storefront-in-your-own-site).
3. We should also take a look at non Web-3 projects that have broad usage of kudos-like functionality, such as Reddit and Steam Awards, and create code to allow builders to quickly do this. 

Perhaps something to allow us to give out Kudos here on Discourse? Example steam award below:

![|624x612.33206341365](upload://6fmQtuXCULVMdgfHiNcJe7tFwxR.png)

### What Do You Need

1. Being able to consult with Kudos development team, so we can more easily address any issues with migrating over the code and also write solid documentation
2. OPGames can assign a team of developers on it for 5 ETH to build the initial version
3. We’d be interested in collaborating and exploring how to make the project sustainable even after the RFP

Thanks for reading, we’re open to suggestions and comments!

-------------------------

owocki | 2021-08-30 19:46:17 UTC | #3

hey all, pls get your proposals in by September 15th 2021 !  I will aim to hire someone by end of month.

one migration plan i've seen mentioned is that we may want to migrate Gitcoin Kudos to POAP.  i'd be interested in seeing proposals that explore this path.

-------------------------

keikumata | 2022-03-07 16:33:52 UTC | #4

# 👋 **Who are you**

Hi there! We are the Kudos team at [mintkudos.xyz](http://mintkudos.xyz/). Kudos captures individual and team off-chain contributions as on-chain, peer-verified, Soulbound (non-transferable) tokens… all with a celebratory twist! We are unlocking the Contributor Economy, a world where people can fluidly work for communities that they’re mission-aligned with and get paid in ownership by creating the building blocks to contributor identity. For more information, check out our Twitter intro thread:

https://twitter.com/mintkudosXYZ/status/1491604796368773120

### Team

[Kei](https://twitter.com/keikumata)

- technical lead
- previously led engineering at early stage startup and before that worked as a software engineer on the blockchain division of a large tech company

[Catherine](https://twitter.com/unhappiimochii)

- product lead
- previously product manager at a tech company that’s deeply rooted in the future of work

[Kathy](https://twitter.com/kathytzhou)

- design lead
- member of VectorDAO and curates beautiful vibes at Kudos

We also have other part-time full-stack and frontend contributors on the team as well 🕺

# ✏️ **What is your proposal to build this**

We’d like to start with the goal of doing product discovery to ultimately build out a custom user experience that’s appropriate given common user journeys within the Gitcoin ecosystem. The solution we’re proposing would reuse our Soulbound smart contract and various UI experiences to prompt a Kudos creation (both manual and automatic) upon things like bounty completion, quest completion, hackathon participation, and even grant contributions. We would also like to rebuild the Gitcoin profile view as well.

The key here is that any Kudos you receive in Gitcoin should be presentable as part of your decentralized reputation in any context outside of Gitcoin. The non-transferability of the Kudos is a big plus when building proper decentralized reputation that shouldn't be traded or bought. By leveraging the smart contracts and our platform, this should be a win-win situation for everyone. 🙂

Our team currently has a working alpha version of these designs:
https://www.figma.com/proto/lxKJgHUFCRvvaNvvEYBB3N/kudos?node-id=477%3A9337&starting-point-node-id=477%3A9337

- Completed functionalities include: creating a Kudos, specifying recipients, inputting information around the Kudos, claim link generation, profile view, and art generation (we have generic & branded backgrounds)
- Upcoming functionalities: peer-based verification/endorsements where teammates and community can vouch for a contribution, public APIs, more programmatic art generation (open to ideas!)

We strongly believe that our team and the Gitcoin community have a shared ethos of celebrating and capturing contributions in a decentralized world. We would love to share our learnings from our journey in building Kudos, and work together with the wonderful community to build out the best experience for the benefit of the entire ecosystem.

# 🕰️ **Timeline**

We estimate about little over a quarter (~14-18 weeks) to perform product discovery, iterate on designs, and deliver the MVP.

- **2 weeks for team formation** (we want to work on this in collaboration with GitcoinDAO contributors)
- **3** **weeks of product discovery**
    - 1 week for interview script creation & recruiting user interview participants
    - 1 week for conducting interviews and interview synthesis
    - 1 for prioritization & roadmap creation + MVP definition
- **3 weeks to test and iterate on designs**
    - 1 week for brainstorming, creating low-fidelity designs, and user testing recruitment
    - 1 week to user test, synthesize learnings
    - 1 week to iterate on designs and prepare for engineering handoff
- **6-10 weeks to deliver on an MVP** *(rough estimate, highly dependent on output from product discovery)*

# 💎 **What do we need**

- Funding to execute on product discovery & product design, then development. We have a small core team of contributors but would love to enlist community help! Examples of how we’d enlist community help at this stage:
    - Co-create product discovery goals and questions
    - Recruit users from the community to perform user interviews with
    - Conduct user interviews
    - Co-synthesize interview learnings + insights
    - Decide on an MVP and roadmap
    - Co-create designs via community feedback
- Funding to develop the MVP. Again, we would love to enlist community help here as well to develop the MVP.
- Marketing, PR, and communications support from Gitcoin to share our collaboration & partnership goals
- Mentorship on running processes in a decentralized fashion

-------------------------

kyle | 2022-03-08 21:40:02 UTC | #5

Thanks so much @keikumata for the proposal. I love the vision you (collectively) have for Kudos, and that you all are interested in advancing the project Gitcoin has had to put in maintenance mode. 

I am interested in other's opinions on the proposal, and I am highly supportive of us moving this forward and offering some space to form a workstream (like we did with dCompass).

As for next steps, perhaps we can have you meet with a few other folks to share the ideas you have and learn more about we develop software, gather feedback and iterate.

-------------------------

Huxwell | 2022-03-09 18:01:50 UTC | #6

Thank you for this proposal which reflects a desire to collaborate with Gitcoin contributors!

The dCompass contributors would love to meet with your team and eventually work together.
I'm sure that the product discovery, user interviews and design could also help us to find a product market fit.

I didn't find a Github link on your website.
Can you confirm that the MVP will be open source ?

I also saw that you are founder of the mintKudos project, is there already a legal entity established for it ? If so, do you already have investors or do you plan to get funded by VCs or other type of funding?

We can schedule a meeting if you prefer to discuss those topics privately.

-------------------------

keikumata | 2022-03-16 03:35:35 UTC | #7

Thank you @Huxwell ! Apologies for the late response here! We would love to meet with the dCompass contributors as well - what would be the best course of action here? Shall we connect on Discord?

> I didn’t find a Github link on your website. Can you confirm that the MVP will be open source ?

Yes! Everything we build with Gitcoin will be fully open sourced and will take a community-centric approach to development.

> I also saw that you are founder of the mintKudos project, is there already a legal entity established for it ? If so, do you already have investors or do you plan to get funded by VCs or other type of funding?

Yep, there is a legal entity behind the Mint Kudos project in the US. We are looking into multiple sources of funding, and happy to share more about it over a call.

-------------------------
