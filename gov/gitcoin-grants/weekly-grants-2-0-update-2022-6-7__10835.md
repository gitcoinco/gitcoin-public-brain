---
id: 10835
title: "Weekly Grants 2.0 Update – 2022/6/7"
slug: weekly-grants-2-0-update-2022-6-7
category: gitcoin-grants
url: https://gov.gitcoin.co/t/weekly-grants-2-0-update-2022-6-7/10835
created_at: 2022-06-07T18:20:59.335Z
last_posted_at: 2022-06-14T01:42:50.412Z
posts_count: 3
views: 2641
like_count: 2
---

# Weekly Grants 2.0 Update – 2022/6/7

<https://gov.gitcoin.co/t/weekly-grants-2-0-update-2022-6-7/10835>
erich | 2022-06-07 18:20:59 UTC | #1

Grants 2.0 is an open-source technology for plural and scalable public goods provision. We are building a modular toolkit for Quadratic Funding and adjacent social incentive designs to increase and govern ecosystem capital.

# Relevant Documents

* [Gitcoin Grants 2.0 Vision ](https://gov.gitcoin.co/t/gitcoin-grants-2-0/9981)
* [Quadratic Funding](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3243656) paper
* [Decentralized Society](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763) paper
* Design prototypes
  * [Grants Hub](https://www.figma.com/file/obBzCCL8KwoTlVBb5g3ccN/Grant-Hub---Wireframes?node-id=249%3A1000)
  * [Round Manager / Explorer](https://bafybeiew6b2vzsan6szmghz336uc4fm37bn4fmrtdq6fh5ny66tb6we644.on.fleek.co/)
* Staging applications
  * [Grants Hub](https://gitcoinco.github.io/grants-hCreate high-level plan and timeline for finishing the Genesis projectsub/)
  * [Round Manager / Explorer contracts](https://github.com/gitcoinco/grants-round/pull/26)
* Video demonstrations
  * [Passport](https://drive.google.com/file/d/1amMgrC2P_agkrwuTkr2wH8zRwfipEAME/view?usp=sharing)
  * [Grants Hub](https://drive.google.com/file/d/1imFs6YGMjWhEggZcxiNnX9dja5T4o8T5/view?usp=sharing)
* Live applications
  * [Passport](https://passport.gitcoin.co/)

# 2022/6/7 Update

## Highlights
* This week is launch week for Passport - which means this week was spent shipping a ton of UI/UX changes. In terms of MVP, completing the last stamp (BrightID) marked the completion of MVP. Additionally, we have code up for a Reader on gitcoin.co/trust to give users a Trust Bonus Score. Does it feel done - like we’ve crossed some sort of line? No, not at all. The feedback we’ve been gathering has provided us plenty of UI/UX improvements. It’s helped us validate our assumptions on some problems, and invalidate what we thought were problems elsewhere. It’s helped us discover more about the value we’re providing to our users, and how we can provide more.
* Grants Hub is targeting to be dev-complete with Grant Hub MVP by Friday, June 3rd. With this week’s progress, we are about 90% of the way to hitting our MVP milestone. Our goal is to have Grants Hub production-ready by July 1st, 2022. 
* This week the Round Manager / Explorer team finished fleshing out the contract structure and tested deploying it to Goerli using some helper scripts we’ve written. We also created a basic UI shell for the [Round Manager Steel Thread](https://miro.com/app/board/uXjVOyDFRMM=/?share_link_id=589961971819) — this currently allows you to connect a wallet, but next week we will begin wiring the contracts up and adding more functionality to the UI. 


## Product Work

### Passport

* Shared & gathered user-feedback
   * Reader (staging) & Passport in Weekly Sync
   * Passport in DAO Vibes
   * Directly with members of the DAO
* Coordinated PMM work w/ Sean
* Wrote several UI/UX stories based on user-feedback
* **Test more UI/UX changes**
* **Launch Passport for GR14**
* **Create story’s for improvements and bugs**
* **Support the support team**
* **More BrightID UX research/strategy**

### Grants Hub
- Started planning for Phase 2 (Anchor) — set up Phase 1 retro next week & Phase 2 kickoff on Mon 6/13, first draft of Phase 2 user stories
- Set up weekly “Grants 2.0 Playground” session to drive DAO-wide visibility of Grants 2.0 progress
- **Lead first “Grants 2.0 Playground session” for the DAO → build a running Grants 2.0 FAQ with feedback and questions**
- **Finalize Phase 2 (Anchor) PRD and user stories**

### Round Manager / Explorer
- Mapped the user journey for Grant Explorer ([Miro here](https://miro.com/app/board/uXjVO2CrhpI=/?moveToWidget=3458764526650540270&cot=14)) and created first draft Steel Thread mockups
- **Finish Steel Thread mocks + stories for Grant Explorer**
- **Create high-level plan and timeline for finishing the Genesis projects**

## Design Work

### Passport

* Trust Bonus page:
    * Made UX/UI changes based on user-feedback
    * Designed a 3 step process for creating, scoring, and saving the passport w/ Gitcoin
    * Made copy changes to better articulate expectations
* Passport:
    * Added loading states for stamp cards during passport creation
    * Designed POAP pop-up (not found, found, & expanded) states during stamp verification
* **Testing to validate assumptions**
* **Mobile designs**
* **Coordinating with MMM and product to finalize end-to-end copy**
* **UI Design reviews with engineering**

### Grants Hub
- Led user research synthesis session and drafted feature changes for Phase 2 (Anchor) from these learnings
- Updated CTA on cGrants 
- Completed Phase 1 (MVP) designs for mobile view
- **Finalize Phase 1 (MVP) mobile web designs**
- **Continue improving Phase 2 (Anchor) designs**

## Engineering Work

### Passport

* Completed implementation of BrightId Stamp
* Updated Alchemy RPC for prod readiness
* UX/UI improvements for Reader on /trust - added the 3-steps content (Connect, Score, Save)
* UX/UI improvements on the Passport
    * added loading spinners
    * better modal text - for BrightID process
    * better toast text for notifications - also BrightID process
    * added a 404 page
* Node whitelisted by Ceramic team and mainnet connection completed
* Replaced merkle root w/ a hashing function in the VCs we issue for stamps (PII protection)
* Worked on Datadog implementation for analytics
* Investigated Passport Bugs
* **More UX/UI improvements on the Passport**
    * better wallet signature messaging
    * add toasts for Stamp completion notifs
* **More UX/UI improvements on the Reader (/trust)**
    * remove unnecessary content
    * warnings when trying to leave the page w/o saving
    * better experience for users w/ existing Trust Bonus Score
* **Finish Datadog**
* **More bug search** 

### Grants Hub
- All of the hi-fidelity mocks/pages have been built out in the dApp with the exception of the modal and toast component
- **Developer docs for Phase 1 (MVP)**
- **Finish up MVP UI work (modal, toast component)**
- **Integrate Phase 1 (MVP) development on mobile web**

### Round Manager / Explorer
- Upgradeable contracts deployed on Goerli for the round (details in Demo #1 above) —> those contracts have been verified on etherscan and include the ability to:
    - deploy a grant round factory
    - deploy the grant round contract
    - create a round via factory (which clones the round contract)
    - deploy a dummy voting mechanism
    - manage RBAC on round contract  (ability to add/remove operators on grant round)
    - update on-chain storage variables in round
- Build out basic UI which can be viewed through the link in Demo #2. (This is from  https://github.com/gitcoinco/grants-round/pull/19 which has not been merged as we are discussing on if **rtk** is what we want to use)
- Enabled auto-deploying on PR against main on fleek (staging env). This means you can test PR on IPFS before they get merged
- **Implementing Program Factory & Program Implementation on chain**
- **Adding deploy scripts for the same and have em deployed**
- **Improve contract coverage**
- **Explore Graph**
- **Finalize on frontend library to use with hub team**
- **Wire in contract deploy to Steel Thread UI**

-------------------------

Luvlynj | 2022-06-13 20:48:56 UTC | #2

Why even after stamping my passport and it been verified..  my wallet still says "There are no ceramic account associated with this wallet" 

Please what is the reason?

And after donation, I didn't receive a mail to confirm that the donation was successful.

-------------------------

owocki | 2022-06-14 01:42:50 UTC | #3

[quote="erich, post:1, topic:10835"]
It’s helped us validate our assumptions on some problems,
[/quote]

any plans to make the proof of humanity module connect a different wallet?  i use a diff wallet for my POH wallet vs my grants contributions.

[quote="erich, post:1, topic:10835"]
Grants Hub is targeting to be dev-complete with Grant Hub MVP by Friday, June 3rd.
[/quote]

this post was published june 7th?

when do we expect to have a GR15 product roadmap?  eg when will we know what GR15 will look like from a product perspective?

[quote="erich, post:1, topic:10835"]
* **Launch Passport for GR14**
[/quote]
any stats on how this is going?

[quote="erich, post:1, topic:10835"]
Video demonstrations

* [Passport ](https://drive.google.com/file/d/1amMgrC2P_agkrwuTkr2wH8zRwfipEAME/view?usp=sharing)
* [Grants Hub ](https://drive.google.com/file/d/1imFs6YGMjWhEggZcxiNnX9dja5T4o8T5/view?usp=sharing)
[/quote]

great to see these demo videos. imo this is a much better way to traverse this info than a long list of text updates.

would love to see others in the DAO watching these demos + giving feedback, given how grants 2.0 is an essential intent for the dao

-------------------------
