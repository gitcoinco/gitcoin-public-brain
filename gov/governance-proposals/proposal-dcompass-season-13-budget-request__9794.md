---
id: 9794
title: "[Proposal] dCompass - Season 13 budget request"
slug: proposal-dcompass-season-13-budget-request
category: governance-proposals
url: https://gov.gitcoin.co/t/proposal-dcompass-season-13-budget-request/9794
created_at: 2022-01-31T20:46:56.236Z
last_posted_at: 2022-04-14T21:12:52.081Z
posts_count: 16
views: 5062
like_count: 60
---

# [Proposal] dCompass - Season 13 budget request

<https://gov.gitcoin.co/t/proposal-dcompass-season-13-budget-request/9794>
Huxwell | 2022-02-07 10:14:33 UTC | #1

## **TLDR**:
The dCompass workstream is requesting a total of 38k GTC for Season 13.
The focus for this season will be on:
- Rewarding users going through pathways & quests
- Beta release & deployment on mainnet and Polygon
- Onboarding new projects, DAOs and protocols

## **Milestone Report**:
Q4 2021 Retrospective and January 2022 update
https://gov.gitcoin.co/t/proposal-integrate-dcompass-within-dgitcoin-to-build-dquests-dknowledge/8836/19?u=huxwell

## **Proposal body**:

****Season 13 roadmap****
- **dCompass** - PROJECT
   - Project Sponsor Pass (stake required to submit a project for review)
   - If any, display all the smart contracts of a project
   - ERC20 allocation and distribution for pathway and quest creation
   - Claim ERC20, ERC701 and ERC1155 rewards
   - Public profile page & browse profiles by pathway & quests progress(eg: query all users that completed the Gitcoin Grants 101 pathway)
   - Performance, additional datastore to act as a caching layer such as ThreadDB or PostgreSQL
   - Smart contract audits, mandatory before going to production and we'd appreciate any advice from the community on our [contracts](https://github.com/Discovery-Labs/dCompass/tree/main/packages/hardhat/contracts).
   - Beta launch on mainnet and Polygon + research and potential deployment on other scaling solutions
   - Responsiveness
   - [Website - WIP](https://dcompass.webflow.io/) (about, features, values, go to dapp)
   - Allow users to choose between uploading a markdown file or use the Gitbook integration for pathway & quest guides

- **Gitcoin Knowledge Base** - PROJECT
*While working on the v1 of the Gitcoin Knowledge Base with FAQs and translations, we realized a pain point that could serve the Gitcoin DAO Community greatly by addressing one of the main problems; **contributor onboarding**.* 
By working with Workstream and Squad leads for the last month on the Gitcoin Knowledge Base, we started to prepare *Handbooks*, which are one-stop information hubs for Workstreams that include **introductions to workstream squads** and **step-by-step instructions** on **how to contribute** to each workstream squad.
We'll focus on creating 3 handbooks as an example for other workstreams and Gitcoin products:
  - Handbook for the Moonshot Collective Workstream
  - Handbook for the FDD Workstream
  - Handbook for the Gitcoin Grants (what is gtc grants, cGrants vs dGrants, contribute to a grant)
  - Translations of the *Handbooks*

- **dKnowledge** - SQUAD
  - Integrate **Moonshot Collective developer pathway** to dCompass dApp
  - Integrate **FDD contributor pathway** to dCompass dApp
  - Integrate **Gitcoin grants pathway** to dCompass dApp
  - Content curation and guide creation for pathways & quests
  - Preparation of Blog Articles to standardize the use of Handbooks across DAOops

**Success metrics and KPIs**
I would consider our workstream successful if we have a decent MVP deployed in a production environment at the end of Season 13.

Some KPIs
- Get at least 6 projects to purchase a sponsor pass
- Create pathways and quests with at least a total of $100K rewards distributed
- Get at least 1000 users that engage with a project, pathway or quest

**Season 13 budget request**
We're requesting a total of **38k GTC** that will be used to compensate contributors and to handle various expenses such as the smart contract audits and the infrastructure costs (Ceramic Node and a few other instances running on AWS).

![Capture d’écran 2022-01-31 214207|690x343](upload://1n8jWiHitlJT9l4nZfAuFRd7lAf.png)

## **Vote**

**FOR** - If you vote "yes", the **dCompass Workstream** will continue to exist within the **Decentralize Gitcoin Workstream** , and the proposed budget above will be allocated to the multisig of the dCompass Workstream `0x756239E5B7D2aa6F3DA0594B296952121Fb71606`.

**AGAINST** - If you vote "no", the dCompass Workstream won't be funded or supported by the Gitcoin DAO anymore, and the requested budget won't be allocated.

-------------------------

Sirlupinwatson | 2022-02-01 13:44:17 UTC | #2

Listening to BBB Big Buck Bunny this morning :slight_smile: 

When this will be live on snapshot? 

[quote="Huxwell, post:1, topic:9794"]
Project Sponsor Pass
[/quote]
Interesting, do you have more info about the Sponsor Project Pass?
Looking great!

-------------------------

Huxwell | 2022-02-01 15:44:27 UTC | #3

I would say in about a week if everything goes well.

The last step for submitting a project is to choose the sponsor pass plan. Then those projects will be reviewed by the dCompass community and if approved they get the Sponsor Pass NFT and we take their staked tokens.

![image|690x370](upload://nqNPhkuaAqD2evrU3G85VYHH8hD.png)

It will certainly change so we're open to feedback regarding the pricing and features.

-------------------------

Huxwell | 2022-02-07 10:02:57 UTC | #4

Thanks to @matthewcarano [here's a demo video of the dCompass dApp]( https://www.youtube.com/watch?v=KUPT0L8voLo)!

The feedback is always more than welcome!

-------------------------

kyle | 2022-02-08 19:25:38 UTC | #5

Thanks Huxwell for the comments on the other thread., I figured I would move the conversation over here. 

It sounds like you are interested in updating the branding to denote this is a Gitcoin Project, which I appreciate. Given Gitcoin is funding this work, showing ties and branding that gives this 

You also have mentioned there is the intention to eventually launch this protocol as a unique community/DAO. We are forming some precedent in how we launch new DAOs from Gitcoin, with the goal of making sure Gitcoin, as the funding partner, is able to participate in the upside in any growth that dCompass. Have you given consideration to what it might mean to offer upside to Gitcoin (the community and DAO)?

-------------------------

Huxwell | 2022-02-09 10:26:13 UTC | #6

[quote="kyle, post:5, topic:9794"]
You also have mentioned there is the intention to eventually launch this protocol as a unique community/DAO.
[/quote]

Yes the idea of creating our own DAO is something we had since the beginning and that was briefly discussed with @owocki during the first meeting about decentralizing quests. It's a mid-term goal (6 months or 1 year) but it is important to start having those conversations to avoid creating chaotic situations when the time comes.

[quote="kyle, post:5, topic:9794"]
We are forming some precedent in how we launch new DAOs from Gitcoin, with the goal of making sure Gitcoin, as the funding partner, is able to participate in the upside in any growth that dCompass. Have you given consideration to what it might mean to offer upside to Gitcoin (the community and DAO)?
[/quote]

Here's what we have in mind so far:
- On pathway & quest creation, there will be a 15% fee on the rewards allocated where 5% will go to the Gitcoin treasury.
- A token swap, so Gitcoin will always have a big say about the project.

-------------------------

maerg | 2022-02-09 13:28:12 UTC | #7

Hi Kyle, 

As @Huxwell mentioned we intend to make sure that our mission, values & goals are aligned with Gitcoin DAO and the Gitcoin community. 

Currently, we are a group of builders, and we are structuring the coordination between our working groups. We are putting a lot of effort to make sure we have the core structure today to progressively decentralize in the future.

As Cali mentioned, we talked with @owocki about revenue(fee) sharing, and a potential Token Swap before the launch. 
In addition to those, we have been talking with @beist to align our business model and pricing to benefit GitcoinDAO as much as possible - we are trying to build a structure where we can funnel more sponsors to the Gitcoin Hackathons via dCompass dApp. 
Other than the monetary value that we can add, we are building funnels to ease onboarding for the GitcoinDAO through pathways & quests; working with @DisruptionJoe, the FDD workstream, and the MC to create the initial onboarding structures. 

Having that said, we are a part of the GitcoinDAO family and we would love to discuss these in detail to make sure the DAOs support to dCompass is justified and we have the necessary structure set for GitcoinDAO to play a great role in the future of dCompass.

-------------------------

DisruptionJoe | 2022-02-09 16:41:49 UTC | #8

I'm very in support of this proposal. With a small budget they executed and are about to drop a critical piece of web 3 infrastructure. They are an example of decentralization in action. 

Please fund this stream and do not delay!

-------------------------

kyle | 2022-02-09 17:29:33 UTC | #9

Thanks so much for the info. This is helpful to know these conversations are in flight. 

Assuming they continue in good faith and when the workstream is interested in spinning out we have involvement from the DAO at large (not just Owocki), I am supportive of funding the workstream.

-------------------------

maerg | 2022-02-11 12:52:50 UTC | #10

Thank you @kyle 
Sorry for not adding these details to our forum post. We learn as we go! 
And, we will make sure to prepare documentation to detail these initiatives and share it with you all.

-------------------------

krrisis | 2022-02-15 06:32:48 UTC | #11

Adding a comment here to make sure dCompass can move this proposal asap to Snapshot. I will probably abstain from voting on this proposal because I've seen dCompass struggle to be fully integrated within GitcoinDAO, or even within the DGitcoin Workstream. I don't think this is per se a bad thing, knowing that the goal is to become a separate DAO within the year. 

However I do think investing in better and more communication within the DAO would be a good thing. The forking away without warning from the Gitcoin Discord was in that context a sign that better communication is needed. Even if in the future you become a separate DAO, good communication within that DAO will be key, so just passing this on as a note. I hope we'll be able to collaborate in S13 on how we can get there together, and I hope I'll personally find more time to jump on calls to discuss these pain points and figure out how to facilitate better. 

Most important point why I will abstain is a lack of time to really dive deep into what DCompass has accomplished & wants to accomplish. 
What I do know is that both @Huxwell & @maerg are two massively competent, hard-working & talented contributors who believe deeply in the mission of Gitcoin & decentralization, so hopefully other stewards will have time to dive deeper (missing at least one comment at time of writing).

-------------------------

bobjiang | 2022-02-17 06:49:31 UTC | #12

dCompass comes from GitcoinDAO, dQuest.

This is a great experiment to gamelize the knowledge and quest on Gitcoin.
I will support the continuous experiment.

-------------------------

Fishbiscuit | 2022-02-17 14:08:50 UTC | #13

@Huxwell great job putting together this budget request! I'm personally very invested in the education space and I think we can afford to give you the space to experiment and try to build new ways to engage developers in a scalable manner.

**Suggestions**
- there might be some open source education material that would like to work with us on this, I noticed free code camp coming up with a [Web3 education course](https://www.freecodecamp.org/news/carbon-neutral-web3-curriculum-plans/)
- I'd like to see dCompass featured at ETHGlobal as a learning pathway for Scaffold-ETH (since this is an existing pathway)
- if you'd like some curriculum development work I can offer some time to help build this out
- perhaps collaborating with places like Bankless Academy (i think there were some initial conversations), Secureum, buildspace might help. I'd imagine these organisations could have a free version/trial version on dCompass and dCompass could help provide referrals to these more advanced courses

**Curious about**
- I'd like to see where the project is managed, I couldn't find it on Notion
- how would you keep the Gitcoin Knowledge Base present considering that GitcoinDAO is constantly evolving
- how the proposed DAO will interact with overall regenerative economics ecosystem (@Aleborda21)

Otherwise it's tentatively a yes from me

-------------------------

lefterisjp | 2022-02-21 11:58:32 UTC | #14

I like what this workstream has put out so far with the budget they have and especially compared to other streams the request for funding is not extraordinary so I will support it.

-------------------------

Huxwell | 2022-04-04 15:22:14 UTC | #15

**Season 13 milestone report**

**Contributors** : 4 full-time & 2 part-time
**Funds spent to date from S13 fund allocation**: 9221 GTC (21.4% of the dCompass treasury)
**Notable achievements for the quarter so far**:
- Big improvements on the product organization, kudos to Eli our scrum master
- [As a quest creator I want to configure how the rewards of the quest are distributed to the adventurers](https://trello.com/c/KACFAZ3o/1-5-as-a-quest-creator-i-want-to-configure-how-the-rewards-of-the-quest-are-distributed-to-the-adventurers)
![Capture d’écran 2022-04-04 163102|690x360](upload://3B8Kyf7Lwo3ThHe31NrAOcyiL5V.png)

- [As an adventurer I want to complete a quiz so that I can claim the various rewards](https://trello.com/c/uUgRKeC3/4-5-as-an-adventurer-i-want-to-complete-a-quiz-so-that-i-can-claim-the-various-rewards)
![image|690x361](upload://sEyCC8VPggPMOeYOH0UymzIMqLC.png)
![image|690x356](upload://6iflowmjEgoQrUi1KMlTHSa1ETP.png)

[Claim quest rewards transaction example on a testnet](https://rinkeby.etherscan.io/tx/0xa03ecd1cd91d360739350d6e60d829d335dc261315d33a0a425e32270bc70f5c) & [NFT Reward on opensea](https://testnets.opensea.io/assets/0xad66eccb5dc5a9d00a820fcf898fa72061539d52/1)
- [As a visitor I want to see a list of users that completed a quest](https://trello.com/c/oD0aZqr1/9-8-as-a-visitor-i-want-to-see-a-list-of-users-that-completed-a-quest)
![image|690x316](upload://psVn7Ztuy8RWwKFkxEhH7z3VkGu.png)
- Staging app to allow anyone to test and play with the first quests on testnets will be deployed during this week.

**Achieved S13 roadmap goals so far:**
- Project Sponsor Pass (stake required to submit a project for review)
- ERC20 allocation and distribution for pathway and quest creation
- Claim ERC20, ERC721 and ERC1155 rewards
- Performance, additional datastore to act as a caching layer such as ThreadDB ~~or PostgreSQL~~

**Blockers in moving towards goals (if any):**
No blockers but we're planning to attend multiple events to demo dCompass during devconnect and announce an official release of the MVP.
**Have any of actions of the workstream brought back value into the DAO/treasury (and if so, what?)**
Not yet but we do expect to generate value and revenue by the end of Season 13, post devconnect/official release.

-------------------------

Huxwell | 2022-04-14 21:14:38 UTC | #16

Here's the staging app with a bit of delay!
https://dcompass-staging.herokuapp.com/

Anyone that has some Rinkeby ETH should be able to go through the Gitcoin Grants pathway and complete the quest to claim the rewards.

Let us now if you're having issues or any feedback to provide.

-------------------------
