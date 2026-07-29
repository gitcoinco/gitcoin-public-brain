---
id: 10916
title: "Weekly Grants 2.0 Update - 2022/6/14"
slug: weekly-grants-2-0-update-2022-6-14
category: gitcoin-grants
url: https://gov.gitcoin.co/t/weekly-grants-2-0-update-2022-6-14/10916
created_at: 2022-06-14T08:23:26.364Z
last_posted_at: 2022-07-25T00:39:12.700Z
posts_count: 2
views: 2560
like_count: 0
---

# Weekly Grants 2.0 Update - 2022/6/14

<https://gov.gitcoin.co/t/weekly-grants-2-0-update-2022-6-14/10916>
erich | 2022-06-14 08:23:26 UTC | #1

Grants 2.0 is an open-source technology for plural and scalable public goods provision. We are building a modular toolkit for Quadratic Funding and adjacent social incentive designs to increase and govern ecosystem capital.

# Relevant Documents

* [Gitcoin Grants 2.0 Vision ](https://gov.gitcoin.co/t/gitcoin-grants-2-0/9981)
* [Quadratic Funding](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3243656) paper
* [Decentralized Society](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763) paper
* Demos
  * [Passport:](https://drive.google.com/file/d/1oGc74qZd2sUjSk7d5GTchXfwM365eMi9/view?usp=sharing) This week's demo is a bit different. In the spirit of transparency - we decided it would be more valuable to take a minute and talk about the current ceramic node issues we're seeing. There's a lot more the teams are learning - and we will certainly know more by the time I update this post later (if there's not already progress between now and when we recorded)
  * [Grants Hub](https://drive.google.com/file/d/1LyAuPQgzwkx_MRsV3_5DIdzjYkZ00z9Q/view?usp=sharing)
  * This week Round Manager walks through the functionality of [creating a basic program and associated round](https://share.vidyard.com/watch/ceKWmWCmMERDewqWn2sq1Q?) via our Steel Thread UI. You can connect your wallet (on Goerli) and try it for yourself here: [https://rmgitcoin.on.fleek.co/](https://rmgitcoin.on.fleek.co/)

# 2022/6/14 Update

by @brent (Passport), @michelle_ma (Grants Hub), and @nategosselin (Round Manager) 

## Highlights
- Last week came with both the highs and lows. To kick things off, the Passport had a great first day - breaking 1000 Passports submitted to Grants in the first 24 hours and with minimal issues. Day 2 came, and our ceramic infrastructure started to feel the weight of all the traffic. Part of the pains of launching an "Alpha" Product like this is learning as you go, and this week had no shortage of learning. This week will be spent still stabilizing our ceramic infrastructure while preparing for a hackathon
- Last week, Grants Hub was 100% dev-complete with the Grant Hub Phase 1 (MVP). We will spend the next 2-3 weeks getting Grant Hub production-ready (deadline 7/1) and kick off Grant Hub Phase 2 (Anchor) this upcoming Monday, 6/13.
- The Round Manager now has milestones and a demo! The team spent some time this week breaking down the planned goals for Round Manager, turning them into actionable chunks, and aligning on our [overall MVP scope/timeline](https://www.notion.so/MVP-9227f130e5d74e078cd43cd704340c5a). Our goal is to be code complete with our MVP by 7/5/22. With this week’s progress, we have completed about 85% of our [Steel Thread](https://www.notion.so/Steel-Thread-fd85d8ce97c4420f84828fdb3e0c1f91) and are about 20% of the way towards hitting our MVP milestone. The team's ongoing debate was whether we needed a "program" shell for MVP and whether that program should be saved on-chain (vs. housed in a centralized database). While there were some UX benefits to housing program metadata (such as operator wallets) in a centralized store, we felt that the overall benefits of pursuing a decentralized program store were much greater and have decided to pursue that route.

## Product Work

### Passport
- More BrightID UX research/strategy
- Added a bug column and created story’s for improvements
- Launch communications (also we launched 🚀)
- Studied user behavior and feedback
- Explored solutions for user experience
- Lots of monitoring (support and data)
- **Heavy backlog work to prioritize both SDK work and Ceramic issues**
- **Increased pairing time for Brent & Leon (for learning)**
- **Dig into the support channel to expose UX failures**
- **Explore more solutions for UX**
- **Additional hackathon planning and execution**
- **A lot more monitoring (support and data)**

### Grants Hub
- Hosted our first DAO-wide Grants 2.0 Playground event
- Working on Phase 2 Planning (user flow + story mapping)
- Led our first team retro after hitting MVP milestone
- **Kickoff Phase 2 of Grant Hub** — have a PRD with user flow and stories ready to review by kickoff

### Round Manager
-  Shipped Steel Thread program/round demo!
- Aligned on [MVP milestones and timeline](https://miro.com/app/board/uXjVOvQ7EBY=/?share_link_id=932859309712)
- Created [MVP brief](/9227f130e5d74e078cd43cd704340c5a)
- **Pair with Grant Hub team on interfaces for Application flow**
- **Design UI for [Application flow](https://www.notion.so/MVP-9227f130e5d74e078cd43cd704340c5a)**
- **Add designed UI to Steel Thread functionality**
- **Add Application functionality to app**

## Design Work

### Passport
- UI updates to Trust Bonus Page
    - headers & body content updated
    - layout updated
    - error messages updates
- Improved communication around if you already have a Trust Bonus Score
- UI Design reviews with engineering
- **UI adjustments on Passport to include logo and footer updates**
- **Add UI around passport submission/processing status**
- **Mobile designs**
- **Any additional UX/UI support in bug fixes**

### Grants Hub
- Explored wallet onboarding designs
- Continued user research synthesis
- **Continuing working on Phase 2 designs** (adding tracking active grants)


### Round Manager
- Created wireframes for [Steel Thread UI updates](https://www.figma.com/file/aZ3oDEvJOTWnbxn1js1SIq/Round-Manager---Wireframes?node-id=223%3A1480)
- Mapped [Application Flow](https://miro.com/app/board/uXjVOtqxuts=/?share_link_id=707295832457)

## Engineering Work

### Passport
- Addressed BrightId Stamp Issues/Bugs
- Updated stamp expiration from 1mo to 3mo's
- Included a "waiting for wallet signature" alert
- Several Infra optimizations
- UX/UI improvements on Passport
  - better wallet signature messaging
  - Added toasts for successful Stamp
  - Landing page UI updated
- UX/UI improvements on Reader
  - content changes - headers & body
  - layout changes -simplified
- Deployed new ceramic infrastructure on staging to test
- Fixed passport bugs 🐞
- **Ceramic Infrastructure work**
   - stamp data - stop/prevent users from making a second passport
   - add info for users when ceramic is down
   - upgrade the latest ceramicnetwork/stream-tile
   - deploy new infrastructure from staging to production
   - more debugging and more fixes
- **SDK documentation for [Hackathon](https://gitcoin.co/hackathon/passport/)**
   - writing stamps into passports
   - verifying stamps in a passport
   - scoring a collection of stamps
   - code/examples for scoring
   - README's for each package: writer, reader, verifier, scorer, and types
 - **Remove NextJS in favor of a standard CRA structure**
- **Remove @dpopp/ from repository package name**
- **Coordinate with Ceramic Team**
- **Additional Datadog logging improvements**

### Grants Hub
- Implemented mobile web view for Grant Hub
- Implemented localstorage cache to load projects quicker on Grant Hub
- Researched subgraph options for project registry
- **Clean up any bugs from Phase 1** (MVP) 
- **Start working on Phase 2 development** (applying to a round)

### Round Manager
- Deploy Program Factory , Program Implementation contracts along with deploy scripts https://github.com/gitcoinco/grants-round/pull/29
- Create playground for experimental features and update ProgramFactory to use Proxy pattern https://github.com/gitcoinco/grants-round/pull/33
- restructure frontend to use react-toolkit to write cleaner code https://github.com/gitcoinco/grants-round/pull/19
- wire in UI → IPFS → onchain for
    - Grant https://github.com/gitcoinco/grants-round/pull/28 https://github.com/gitcoinco/grants-round/pull/42
    - Program https://github.com/gitcoinco/grants-round/pull/41
- **Explore Subgraph to see how we can leverage graph protocol**
- **Rewrite up voting interface to ensure**
- **Integrate tailwind-ui and improve UI screen**
- **Build skeleton app of explorer**
- **Focus of improving test coverage on contracts**

-------------------------

owocki | 2022-07-25 00:39:12 UTC | #2

are yall still publishing weekly grants 2 updates?  or has it evolved in another direction?

-------------------------
