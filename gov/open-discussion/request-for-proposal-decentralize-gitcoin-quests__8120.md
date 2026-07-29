---
id: 8120
title: "Request for Proposal: Decentralize Gitcoin Quests"
slug: request-for-proposal-decentralize-gitcoin-quests
category: open-discussion
url: https://gov.gitcoin.co/t/request-for-proposal-decentralize-gitcoin-quests/8120
created_at: 2021-08-02T20:53:06.086Z
last_posted_at: 2021-08-30T19:45:39.261Z
posts_count: 7
views: 4791
like_count: 13
---

# Request for Proposal: Decentralize Gitcoin Quests

<https://gov.gitcoin.co/t/request-for-proposal-decentralize-gitcoin-quests/8120>
owocki | 2022-05-28 15:38:06 UTC | #1

Hello DAOfrens, 

This is request for someone to come up with a new decentralized experience for managing Gitcoin.co/Quests

As we progressively decentralize Gitcoin, the Gitcoin Holdings company is interested in decentralizing the Quests experience from our [centralized codebase](https://github.com/gitcoinco/web/) to a decentralized frontend.

An ideal candidate would be have the following principles:
1. Simplicity - products that do ONE THING and do it WELL.
2. Antifragility - Well-documented Decentralized products that our community can run without the centralized company.
3. Modularity - products that easily unix-style interoperate with each other.

Gitcoin Holdings will provide a database backup of any centralized information (Quests Content) needed to make a great Quest experience to a winning proposal.

Would any of you be interested in developing a GitcoinDAO homepage? If so please submit a proposal by September 15th 2021.  

Proposal should include:
1. Browsing Quests
2. Playing a Quest
3. Winning + receiving a reward (NFT or ERC20

Not needed to be included:
1. leaderboard
2. new quest creation form

Please include

1. Who are you
2. What is your proposal to build this
3. What is your timeline to build this
4. What do you need (funding, etc)

Please submit your proposal as a comment on the gov forum thread.

-------------------------

reza | 2021-08-07 13:55:07 UTC | #2

[quote="owocki, post:1, topic:8120"]
decentralized frontend
[/quote]

Hey there,

I'm reza(@rezahsnz on Gitcoin), not that deep on eth development but have some idea about quests and thought we could get it refined and hopefully an end product could be imagined from there.

So the basic idea is to move the whole `quests` saga into the `NFT` space. Each quest would be an ERC-721(or 1155) contract  where the questions(the actual question + the choices) together with the (encrypted) answers are stored in decentralized storage platforms like IPFS. Questions could also enjoy some freedom in what they are: text, sound, video, svg, ... or a combination of them. Quests would then be deployed on chain and ready to be taken by people. Anyone could then take a quest and try her chance and if successful, she is awarded a token representing her accomplishment and as a bonus the contract could also award them some fungible stuff too.
This way our quests would enjoy some degrees of openness + transparency and we could also expect unofficial UIs around them. 

You asked for decentralized UI but this is a clear backend hack but the though is raw and I look forward to hear your feedbacks. If I were to implement a mvp out of this I think 1-2 months is enough with 2 eths as compensation.

Cheers,

-------------------------

DragonDev1906 | 2021-08-08 08:15:19 UTC | #3

I have put some thought (perhaps too much) about what I think the ideal quest system would look like (see below). While I don’t know if something like this was intended as an answer, the content is relevant when thinking about the design/architecture of the new quest system, which is why I wanted to write it here anyways. Also, I hope this is the correct place to put it (Not sure if this is what was meant by the "gov forum thread").

# Definitions used

* Governance entity: The entity, person, group of persons, smart contract, voting system or DAO that is responsible for managing quests
* Governance system: The system used by the Governance entity

# Quest data storage

I would suggest creating a smart contract that keeps track of the quest creator and references a JSON file containing the quest data via URL (for example using IPFS). This smart contract should have the following functions:

* a public function for quest creation (new quests might start as a proposal before they are displayed to everyone)
* a function to accept a quest proposal (only callable by the governance entity)
* a function to edit the URL/IPFS hash should there be an error (should probably be callable by the governance entity and the quest creator, in the latter case it might make sense that the change must be accepted first)
* a function to remove a quest (only callable by the governance entity)
* a function to mark a quest as played by an address. This could be stored as a mapping(address => mapping(questID => Boolean)). (Only callable by the quest submission verification system)
* (optional) all ERC-721 methods (so that the owner can transfer ownership if he wants or even trade it).

The quest solution probably should not be stored in the quest data, as that would easily allow someone to cheat (a problem most decentralized solutions probably have).

Additionally, there should be at least one entity running an IPFS node storing quest data (even if centralized), otherwise it might happen that quest data is lost at some point.

Reasons:

* Storing the quest (and ownership) in a smart contract provides Integrity, everyone can see any changes made and the history of all quests is stored (at least while the file is on IPFS)
* Storing the quest data/settings/config via IPFS means less data needs to be stored on chain.
* Everyone can access the quest data and it is stored decentralized. That way nobody can modify it unless they use the governance system.
* This is probably the simplest system to store quest ownership and data on the blockchain while allowing a governance entity to manage/filter the quests.
* Having all quest data available allows different systems / User Interfaces to use the quest system (as proposed below)

# Quest evaluation

This is probably the hardest part to decentralize without providing too many opportunities to cheat. I currently see two possible options:

* Keep quest evaluation in the centralized codebase and share quest solutions between a subset of community members (part of and/or selected by the governance entity). If the centralized company is unable to verify correct results the data is at least not lost but still available. There should also be a (well documented) public repository allowing easy deployment of an alternative. To allow the switch it might be necessary to store the URL of the quest verifier in the smart contract.
* Use a system that can store secrets on the blockchain (or in a node that provides it to the smart contract). The user could submit his (encrypted) result to a smart contract that emits an Event for which a Node listens, who then checks if the answer is correct. Currently the only system doing something similar that I know of would be ChainLink, but I don’t know much effort this would be to implement.

I do not know which solution would be better or easier to implement. The second one would probably be more resilient, as it is already decentralized. Nevertheless, only a limited amount of people should have access to the quest solutions. I would recommend to choose the first option but implement it in such a way that it is possible to switch if needed.

# (optional) Centralized Cache

Given the number of quests it might be worth storing a list of them (Name, Creator, …) on a server or IPFS file, to reduce the number of requests the browser must send to display the Quest list. This should probably include the author profile pictures as they are currently quite slow to load.

# Browsing Quests

I would suggest keeping a list of quests, but make the following modifications:

* Make the list sort-able (Client-side). Sometimes I only have 15min, so I’m not yet interested in quests with 30min reading time.
* Remove the Description, Quest Owner and Stage columns and instead make a quest entry expand on click to show this information below the table entry. The “Info” button never worked for me (it’s probably better to display the entire text if you clicked on a quest entry) and when searching for a quest I’m usually not immediately interested in the Quest Owner.
* Instead of the Stage column display if a quest has been beaten and how many attempts where made (I currently can’t see the attempt number until I play the quest. The number of attempts could also be only displayed after expanding a quest entry.
* Make the search completely client-side to make it faster (as far as I can tell the information is already loaded in the browser on page load)
* Don’t have anything below the Quest table, instead put it in another tab (even if the tab switch is completely on the client side). I don’t think it is user friendly if you must scroll past a long list of quests to get to other parts of the application.
* (optional) Remove tabs and improve quest filtering. Perhaps some people don’t care about how difficult a quest is because they want to get them all. Instead, I would suggest adding a show-only-beaten, show-only-attempted, show-only-new checkbox filter and do the same for difficulty. Ideally there would also be a min/max limit for the estimated play time. (In addition to the existing search option). If there are multiple quest types (as the current codebase seems to suggest) there should also be a filter option (or even a column) displaying what type of quest it is.
* Force all quest entries in the table to be of the same (pre-defined) height (if it’s possible at least). This would prevent items from moving around while the page is loading (which was previously the case, I think)

Regarding Implementation, I would suggest building this part in Vue or React, then build it to static files and deliver it from the gitcoin server and/or from IPFS.

# Playing a quest

I do not have a proposal for changing how a quest is played, except for this:

* First, everything related to the quest system should be well documented. This includes how to get quest data from the smart contract and IPFS, how to use the verification system to check if an answer is correct or not and where to get all the media files used by the current/official quest system (and referenced by the quest data).
* Quest creators should be able to add custom files (for example a custom background) by including the (IPFS) URL/Hash in the json file. This would allow more flexibility in the quest creation and the media files wouldn’t have to be provided by gitcoin.
* (optional) It should be possible to create a second version of the quest system using the same quest data with the information provided by the documentation. This could, for example be using three.js to display Information or the quest environment in 3D but might be limiting which quests can be used.
* (optional) To achieve Modularity the player should be able to select which quest User Interface they want to use (for example someone with a slow PC might not want to display things in 3D). This could be done by having a selection in the quest list and a (cached) list of supported quests for each User Interface.

Similar to “Browsing Quests”, this should probably be build into a static site and hosted on the gitcoin website and/or IPFS.

# Winning & receiving a reward

I do not have a good idea on how to improve this part, but here are my thoughts:

* Personally, I like that you can get Kudos for playing a quest, but I find it a bit weird that multiple quests give the same Kudos, and it is rarely related to the Quest itself (for example “Robot Found His Love” has nothing to do with the quest “Journey to IPFS”, as far as I can tell). There are so many Kudos, that perhaps each quest should give a different one (though there are probably a thousand reasons otherwise).
* If someone can come up with a good ERC-20 reward, perhaps it can be combined with rewarding Kudos: You get the ERC-20 reward for all quests (maybe the amount is based on the difficulty and/or time estimate) and some quests additionally give a Kudos. Ideally one that fits the quest.

Regarding implementation of the reward(s):

It is probably best to have a second smart contract with setQuestFinished-rights on the first smart contract that is called by the submission verifier (or the user with a valid signature of a verifier), gives the reward(s) and set’s the quest to completed in a single transaction.

# Open Questions (that I can think of)

* How to keep the quest solution secret (see above for the Ideas I had)
* How to implement the time limit for questions and the attempt count. The player could receive the questions via HTTP from a server instead of them being publicly visible on the blockchain, but this would be a more centralized solution.

# Please include

I’m currently studying IT-Security and have some experience in Solidity, Django, Vue3 and React.

Mainly, I wanted to give my thoughts on the topic, but I’m open to help building it, too (together with other people). Because I don’t yet know how much time I have next semester, how many people would work on it or the exact scope, I obviously cannot give a timeline.

-------------------------

polats | 2021-08-14 20:09:09 UTC | #4

### Who Are You

Heyo @owocki and fellow Gitcoiners! I’m Paul Gadi, co-founder and CTO at [OPGames](https://opgames.org/). We’re bridging game developers to Web 3.0 by building the open-source tools to make it as simple as possible for them to start integrating with the blockchain.

We’re calling these tools [Game Legos](https://youtu.be/9EF_hrmVMqM?t=224): in the same way that Money Legos was able to bring about the DeFi renaissance, we feel these Game Legos will be instrumental in bringing about the coming NFT Game revolution.

Game Legos are also perfectly in sync with the goals of this RFP. We’re building them open-source and as simple, robust, and composable as we can.

### What Is Your Proposal to Build This

Same as our [PFP proposal](https://gov.gitcoin.co/t/request-for-proposal-decentralized-gitcoin-avatar-builder/8117), we believe this should be built as a Game Lego on top of @austingriffith 's  scaffold-eth. We believe Scaffold-eth is not only the framework with the most solid foundation but is also the fastest way for developers to get started in Web 3.0. It also has a strong community of builders behind it that we could tap to continue improving the project.

Creating a generic Quests component is very complicated, @DragonDev1906  has done a great job of breaking down an implementation. We’re approaching it from the Game Lego perspective, where we’re aiming for game developers to start using it for creating quests for their games and reward their players with on-chain assets. An example game with quests is shown below:

![|416x831](upload://unIY8fHzePGbdZkjHYdROs3hubj.png)

The first version will focus only on the creation and completion of quests. We will create a form on top of scaffold-eth where game developers can create quests and save them on a smart contract. We will then have an example HTML5 game that players can play where they can login, see available quests and attempt the quest. Finally we will have a server backend that communicates with a smart contract that validates quest completion (at least until we can properly do this in a decentralized way).

The backend is unfortunately centralized for now, similar to how quests are evaluated on current games. We can use an open-source multiplayer game server for this such as [Nakama](https://heroiclabs.com/) or [Colyseus](https://www.colyseus.io/arena), which should have some battle-tested security checks against cheating. The multiplayer game server will then have a private key which can allow it to validate quests on the smart contract and send out the reward.

### What Is Your Timeline To Build This

We estimate this will take 2 months. There are a lot of moving parts though and there are still a lot of unknowns!

### What Do You Need

1. Being able to consult with Quests development team, so we can more easily address any issues with migrating over the code and also write solid documentation
2. OPGames can assign a team of developers on it for 10 ETH to build the initial version
3. We’d be interested in collaborating and exploring how to make the project sustainable even after the RFP

Thanks for reading, we’re open to suggestions and comments!

-------------------------

reza | 2021-08-17 08:01:31 UTC | #5

I suggest going with a sophisticated on-chain backend and waiting for frontends to pop up from interested people, sort of open frontends. No one could guarantee that any selected frontend would be the best because any judgement is future-blind and limited to what has been received so far.

-------------------------

Huxwell | 2021-08-18 13:36:20 UTC | #6

Hi @owocki and everyone !

**Introduction**
I am a full stack developer(4 years of professional exp and my hobbies are mainly focused around learning security, devops/infrastructure and sharing knowledge). I'm also a user of Gitcoin quests. While I was really enjoying farming some Kudos and learning I noticed some problems that I'm sure you're already aware of (dead links, limited to 1 ressource by quest, bypass of the timeout, flat view, etc.).

My side projects were mostly focused on education so I though that expending on Gitcoin quests and combining it with open source & decentralized content could be a nice hack. That's why my awesome team mates and I have been working on a project called Discovery for 2 hackathons in a row (3 weeks each with a lot of research and brainstorm in between).

**What ?**
Discovery - a gamified learning platform where members of the official protocols team collaborate with content creators and researchers, developers or security experts to create high-quality courses that are built around open source trustable and verifiable content.

Learners will be able to browse courses by topic or project name and at the end of a lesson they'll go through a quest (could be a simple quizz, a code challenge or an action such as "participate to this hackathon" or ie for a lesson about Ceramic & IDX, a quest could be "create your DID and link it to your Github account")

[Here's the demo video](https://www.youtube.com/watch?v=L3qW1ocfTkk) and some images from the previous hackathon:
![discovery-pathways|690x357](upload://4dn6TPRp30HeKr3njKffhevWeQ8.jpeg)
![unknown|690x390](upload://mvdYeTlAutDIhhOWEnVZsNe2i3I.png)

**How ?**
We are using Gitbook to create content (like many other protocols), so we've created a Github Action that can be plugged in any repo (Gitbook or code) and the files of the repo will be uploaded to FileCoin and IPFS through web3.storage. 

We then generate an NFT that contains metadata such as the IPFS urls/CIDs of the files of the repo, the name of the authors, the Github commit id, etc. We then upload that NFT to NFT.storage and we also create a Ceramic Document that contains the IFPS url/CID returned by NFT.storage. 

This will be used as a Token URI in our NFT Smart Contract, so the NFT will be dynamic and it will change every-time the content of the course is updated. The NFT representing the course will have variants (common, uncommon, epic, legendary) and we'll use Chainlink's VRF to randomly drop a common or legendary NFT to people completing the quest.

We went for Ceramic and IDX as our main data & authentication layer (it handles relationships between records and structures our data model: learners, contributors, projects, courses, quests)

For the quests, we are using Chainlink to make a GET request from our NFT SmartContract to our Ceramic Instance through an API Consumer contract in order to validate that the requester has the permission  to mint an NFT(quest completed & hasn't already minted his NFT). The answers of the questions are hashed and there is a server side rate limiter that keeps track of the attempts.

**When ?**
We'll probably need 4-6 months to get a decent alpha version, 3-4 months to make changes and improvements based on the feedback and then we can do an open beta release (so 7-10 months total)

**Needs ?**
On monday, I've submitted my resignation ! I'm done working for web2 private companies and I'm going to start working full time on open source web3 projects. Discovery would be a great starting point so we'll need funding to pay:
- UI/UX designers
- People deeply involved in web3 education, ideally with technical knowledge
- Front-end developers (ideally experienced with ThreeJS, that could create a view to explore the Web3 space in 3D but not required)
- Token engineers (interested in mechanism design and behavioral  incentives)
- More developers, security experts, dev ops (experienced in back-end & Solidity, decentralized storage solutions, etc)
- Members from Gitcoin to give feedback and to help us co-create the future of decentralized gamified education in Web3.

Kind regards

-------------------------

owocki | 2021-08-30 19:45:39 UTC | #7

hey all, pls get your proposals in by September 15th 2021 !  I will aim to hire someone by end of month.

-------------------------
