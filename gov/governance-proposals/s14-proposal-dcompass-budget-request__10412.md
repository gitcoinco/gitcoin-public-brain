---
id: 10412
title: "[S14 Proposal] dCompass budget request"
slug: s14-proposal-dcompass-budget-request
category: governance-proposals
url: https://gov.gitcoin.co/t/s14-proposal-dcompass-budget-request/10412
created_at: 2022-04-24T17:20:32.006Z
last_posted_at: 2022-05-09T18:15:56.197Z
posts_count: 20
views: 5165
like_count: 39
---

# [S14 Proposal] dCompass budget request

<https://gov.gitcoin.co/t/s14-proposal-dcompass-budget-request/10412>
Huxwell | 2022-05-03 11:33:30 UTC | #1

**TLDR**

The dCompass workstream is requesting a total of 110 200$ (19k GTC - $5.8/GTC) for Season 14, which is 2 times less than our previous budget request and it will be the last season that dCompass receives recurrent funding from Gitcoin DAO's treasury.

The focus for this season will be on:
- Season 13 catch up:
  * Beta release & deployment on Polygon
  * Onboarding new projects, DAOs and protocols
- Season 14 goals:
  * Gitcoin quests migration over dCompass
  * Build incentives for quest creators

**Milestone Report**

**Contributors** : 
- 3 full-time devs
- 6 part-time (Alp moving from FT to PT, adding 2 new PT contributors)
  - 1 new dev
  - 1 new token engineer
  - 1 scrum master/PM
  - 1 designer
  - 1 business dev
  - 1 content creator/quest migrator

**Funds spent**: 16 291 GTC (April spendings included but not yet executed)
**Funds carrying over the next quarter**: 26 691 GTC
**Have the actions of the workstream brought back value into the DAO/treasury** ?
Not yet but we do expect to generate value and revenue by the end of Season 14.

**Season 13 retrospective**
[v] = success [x] = failure

**Main goals:**
- [v] Rewarding users going through pathways & quests
- [v] [Alpha release](http://alpha.dcompass.xyz/) on the Rinkeby testnet and Schelling Point live demo
- [x] Beta release & deployment on mainnet and Polygon
- [x] Onboarding new projects, DAOs and protocols

**Product goals:**
* [v] Project Sponsor Pass (stake required to submit a project for review)
* ~~If any, display all the smart contracts of a project~~
* [v] ERC20 allocation and distribution for pathway and quest creation
* [v] Claim ERC20, ERC701 and ERC1155 rewards
* [v] Public profile page & browse profiles by pathway & quests progress(eg: query all users that completed the Gitcoin Grants 101 pathway)
* [v] Performance, additional datastore to act as a caching layer such as ThreadDB or PostgreSQL
* [v] [Website](https://dcompass.framer.website/) (about, features, values, go to dapp)
* [v] Allow users to ~~choose between~~ use markdown ~~or use the Gitbook integration~~ for pathway & quest guides
* [x] Smart contract audits, mandatory before going to production and we’d appreciate any advice from the community on our [contracts ](https://github.com/Discovery-Labs/dCompass/tree/main/packages/hardhat/contracts).
* [x] Beta launch on mainnet and Polygon + research and potential deployment on other scaling solutions
* [WIP] Responsiveness

**Proposal Body**

***Season 14 Roadmap***

* [As a pathway or quest creator, I want the option to create a pathway or quest for free](https://trello.com/c/Bsa0GnoW)
* [As a quest creator I want an incentive to create quests (tip creator and/or give % on the reward allocation fee)](https://trello.com/c/B4pV7aZI)
* Edit [project](https://trello.com/c/MhrBt9gW), [pathway](https://alpha.dcompass.xyz/profile) & [quest](https://trello.com/c/KbSsztsm)
* [As an adventurer I will get rate limited on my answer submition for a quiz](https://trello.com/c/WdpmDMIy)
* [Skill tree (progress per project & pathway)](https://trello.com/c/Jo8PP67t)
* User testing and user feedback improvements
* New quest type "open challenge" (design contest, bug bounty, etc)
* Security audits by [code4rena](https://code4rena.com/)
* Beta release on Polygon
* Tokenomics draft for the v1 of our token
* Documentation and engineering wiki
* Gitcoin quests migration over dCompass

***Budget distribution***
![Capture d’écran 2022-04-26 à 20.21.02|690x343](upload://2sdNJ2m0mAAY5ZdswhOaGD09Fl3.png)

## **Vote**

**FOR** - If you vote “yes”, the **dCompass Workstream** will get funded for a last season, and the proposed budget above will be allocated to the multisig of the dCompass Workstream `0x756239E5B7D2aa6F3DA0594B296952121Fb71606` and we would work towards a mutual grant agreement post Season 14.

**AGAINST** - If you vote “no”, the dCompass Workstream won’t be funded by the Gitcoin DAO anymore and the requested budget won’t be allocated.

-------------------------

kyle | 2022-05-02 05:16:55 UTC | #2

[quote="Huxwell, post:1, topic:10412"]
If you vote “no”, the dCompass Workstream won’t be funded or supported by the Gitcoin DAO ... no mutual grant agreement would be created.
[/quote]

Hey Huxwell, I want to call out that this really rubbed me the wrong way - "no mutual grant agreement would be created." Gitcoin has bootstrapped your entire development effort, extended its brand, conference and community for you test your ideas thus far (AFAIK). Putting the point in here that no funding for S14 would have you walk away from that support with no upside to Gitcoin is wild to me.

I wonder if I am miss-understanding what you mean here?

Asking for 19k GTC is relatively small, but dCompass has continually missed outcomes is has stated it would achieve and fails to attract traction (outside of those in Gitcoin trying to support your efforts with paths like Grants and FDD). I believe you are learning an immense amount about why it is so hard to start a project as a technical founder and still make progress on growing/testing your hypothesis, but largely defecting from the Gitcoin DAO does not seem to have paid off.

-------------------------

Pop | 2022-05-02 10:05:59 UTC | #3

Echoing the intensity of the YES/NO vote dynamic in terms of relationship and work that has already been done together. As the past couple of seasons' milestone reports show, the workstream can improve on delivery so a collaborative vs a split approach may be more constructive? 

And apologies if I missed this but wasn't there a plan to work with @kyle on a potential business plan? Or a finer delineation of structure, setup and mission?

-------------------------

Huxwell | 2022-05-02 15:21:36 UTC | #4

[quote="kyle, post:2, topic:10412"]
Hey Huxwell, I want to call out that this really rubbed me the wrong way - “no mutual grant agreement would be created.”
[/quote]

Sorry it was a clumsy statement coming from [this post](https://gov.gitcoin.co/t/constructing-a-mutual-grants-committee/10347), in the context of a failure, why would Gitcoin even bother for a mutual grant ?
[quote="Huxwell, post:8, topic:10347"]
**Pessimistic scenario:**
If dCompass was to fail again for accomplishing the Season 13 goals (going to production and hitting KPIs) then no mutual grant agreement would be created.
[/quote]

But even if we stop getting funded by Gitcoin, we'll continue to work on the product anyway and I'm confident that we'll get better and better. So having a mutual grant agreement regardless the outcome of this proposal makes a lot of sense.

-------------------------

kyle | 2022-05-02 15:36:49 UTC | #5

[quote="Huxwell, post:4, topic:10412"]
in the context of a failure, why would Gitcoin even bother for a mutual grant ?
[/quote]

This is a great question and something I want to really make sure I spell out. A decision to not fund dCompass (IMO) is not because it is a failure. It would be because Gitcoin needs to focus on the most important thing and cover off spend in areas that are adjacent to its core protocol ambitions.

The work you are doing, the product you are building and community you are growing is not something I would ever call a failure. It may be something that now longer fits where Gitcoin can spend resources though. Hopefully you don't assume that a decision to not fund in S14 means failure. It could mean instead that its time for Gitcoin to refocus where it invests, and for you to continue to grow and launch to see if you can get traction.

[quote="Huxwell, post:4, topic:10412"]
But even if we stop getting funded by Gitcoin, we’ll continue to work on the product anyway and I’m confident that we’ll get better and better. So having a mutual grant agreement regardless the outcome of this proposal makes a lot of sense.
[/quote]

This is great to hear. Thanks for calling that out.

-------------------------

Fishbiscuit | 2022-05-02 20:15:52 UTC | #6

I'd like a clarification on the need to fund dCompass for this quarter as there's currently more funds carried over this quarter than the requested budget itself.

Can dCompass sustain itself this quarter without requesting for more budget? It does seem possible based on the budget breakdown hence for now there isn't much need to get funding either.

Thank you!

-------------------------

Huxwell | 2022-05-02 21:00:54 UTC | #7

[quote="Fishbiscuit, post:6, topic:10412"]
I’d like a clarification on the need to fund dCompass for this quarter as there’s currently more funds carried over this quarter than the requested budget itself.
[/quote]

Yes we could eventually use the funds carrying over this season but then it means that we wouldn't have any reserve at all when Season 14 ends.
So if the mutual grant agreement isn't set up by then it means we will be without funds during our product launch.. and I think that no one in our workstream would be comfortable with that.

-------------------------

Fishbiscuit | 2022-05-02 21:16:15 UTC | #8

Yes, hence the format that most workstreams have followed thus far is:

Requested Budget + 60-days reserve - current reserves 

This will probably suffice for this workstream. 

Which would be
19k + 11.4k - 26.9k = 3.5k GTC


*as another note, I don't think 3000 GTC is enough for smart contract audits

-------------------------

lefterisjp | 2022-05-03 09:07:51 UTC | #9

**Roadmap**

I would like some clarification on the goals.

What are some of the bullet points? Any link for more information/explanation?

What is `Free quest creation`, what is reward alocation etc. ?

**Budget**

As I am writing to the other workstreams I would like to generally tighen the belt for everyone as we are in a bear and we need to ensure the continuing existence of Gitcoin DAO and the completion of its main goals.

But looking at your budget it seems pretty logical. With $6 per GTC and 9 people for 3 months it seems to amount to $3,555 per person per month. Which is a normal salary for us in Europe.

But compared to the other budgets I have seen it's much smaller. Do I misunderstand something? Is it not 9 people who will be paid their salaries through this?

-------------------------

Huxwell | 2022-05-03 12:15:21 UTC | #10

[quote="lefterisjp, post:9, topic:10412"]
What are some of the bullet points? Any link for more information/explanation?

What is `Free quest creation` , what is reward alocation etc. ?
[/quote]

Sorry about the lack of context, I've updated the Season 14 goals with a link to the respective Trello cards with more informations.

I hope that it can help for now but we'll work on official documentation during S14.

[quote="lefterisjp, post:9, topic:10412"]
**Budget**

As I am writing to the other workstreams I would like to generally tighen the belt for everyone as we are in a bear and we need to ensure the continuing existence of Gitcoin DAO and the completion of its main goals.

But looking at your budget it seems pretty logical. With $6 per GTC and 9 people for 3 months it seems to amount to $3,555 per person per month. Which is a normal salary for us in Europe.

But compared to the other budgets I have seen it’s much smaller. Do I misunderstand something? Is it not 9 people who will be paid their salaries through this?
[/quote]

Yes the calculation is pretty much right as an average for the PT & FT contributors. I'd even say that we're underpaying ourselves if we were to compare with the dev salaries of other workstreams/in the space. But we were fine with that as it reduces our burn rate and helps the project over the long run.

Gitcoin DAO is doing a good job at incubating us! 
However, we have bigger needs than what's on our budget request and I don't think that it would be healthy to stay as a workstream that keeps requesting more GTC over time while the focus of the DAO seems to be around funding other initiatives.

-------------------------

DisruptionJoe | 2022-05-04 11:40:54 UTC | #11

I think dCompass should be moved to a mutual grant. Gitcoin should see upside in the product, but not run it. 

That also means not being a workstream which participates in CSDO. 

Overall, I'm very supportive of dCompass. I'd like to see them get the funding they need via the mutual grant structure rather than the workstream structure.

-------------------------

Sirlupinwatson | 2022-05-05 12:11:51 UTC | #12

Last conversation that we had was to meet up with @kyle and start to plan/design a business plan/roadmap that could be sustainable in the future, have you guys work on that part? 

I would personally love to see this project come to life, I do not wish to put any blockers on that but we should look back in time on what is working and what is not at this point and decide if a mutual grant or still being funded by the organization is the right fit. 

The gitcoin Flywheel: Learning while earning/meeting and creating more leaders... In that retrospective I am still supporting this project

-------------------------

annika | 2022-05-09 04:43:45 UTC | #13

Jumping in to provide my two cents as I go through all the proposals.

At a macro level, I very much also echo the questions raised about whether dCompass should continue to exist as a workstream in the context of the DAO. While the Trello links are helpful to dive into some of the specific objectives, I believe this budget request lacks context as to the 'why' of dCompass & the broader vision it is setting out to accomplish, and how that fits into the rest of the work the DAO does.

Given our focus on Grants 2.0 & becoming a Protocol DAO and my lack of clarity as to how dCompass fits into that, I plan to vote 'no' on this budget request. That said, I am eager to explore @DisruptionJoe's suggestion of evaluating dCompass in a Mutual Grants context.

Finally, if this budget request is indeed pushed forward as a workstream funding request as proposed - to @fishbiscuit's point, in keeping consistent with the approach of all the other workstreams, I believe the requested amount should be 3.5K GTC, not 19K GTC.

-------------------------

bobjiang | 2022-05-09 06:59:26 UTC | #14

for dCompass,
I have some questions:

1. what is the goal (could benefit Gitcoin)? - maybe I missed some context.
2. what is the business model (revenue) after season 14 (or without funding from Gitcoin)?
3. what is the growth plan? (how to get more projects in and get more quests)

Thanks

-------------------------

Pop | 2022-05-09 09:35:45 UTC | #15

@Huxwell it would be great to have these addressed before the council call happening this afternoon CET

-------------------------

griff | 2022-05-09 15:09:07 UTC | #16

This is a great proposal, and a great project... but I have to vote no on this proposal as is... sadly given the current market conditions I don't think the DAO can take on revitalizing quests :-/

-------------------------

Huxwell | 2022-05-09 17:31:21 UTC | #17

[quote="bobjiang, post:14, topic:10412"]
what is the goal (could benefit Gitcoin)? - maybe I missed some context.
[/quote]
dCompass’ primary mission is to onboard, guide and educate users about trustworthy Web3 protocols and DAOs.

[quote="bobjiang, post:14, topic:10412"]
* what is the business model (revenue) after season 14 (or without funding from Gitcoin)?
[/quote]
For the recurring revenue, there is a fee for the creation of quests with ERC20 tokens as rewards.

We're also working on a sponsor pass that might act as a partnership deal.

[quote="bobjiang, post:14, topic:10412"]
what is the growth plan? (how to get more projects in and get more quests)
[/quote]

The growth plan is to reach out to projects with some quests already built for their community and get feedback as well as users.

-------------------------

owocki | 2022-05-09 17:45:06 UTC | #18

[quote="Huxwell, post:1, topic:10412"]
If you vote “no”, the dCompass Workstream won’t be funded or supported by the Gitcoin DAO … no mutual grant agreement would be created.
[/quote]

Did I read this right?  dCompass will be renegging on the previously offered governance rights if this proposal is not funded? (see below)

[quote="Huxwell, post:7, topic:10356"]
Yes Gitcoin DAO should have a say in the governance of the dCompass DAO. Gitcoin is the biggest funder so far and it makes sense if it’s one of the main governing entity of the dCompass DAO.

I’m open to negotiate regarding the amount but we can offer 2 seats in our council, which is currently a 3/5 multisig that we can update to be 5/8 so by owning 2 seats, Gitcoin DAO would have 25% of the governance rights.

If Gitcoin DAO continues to fund us (through GTC or any other token), we’re open to make a mutual grant agreement to make a swap between GTC and the DCOMP token for a maximum of 5% of our total supply.
[/quote]

[quote="Huxwell, post:4, topic:10412"]
Sorry it was a clumsy statement coming from [this post](https://gov.gitcoin.co/t/constructing-a-mutual-grants-committee/10347), in the context of a failure, why would Gitcoin even bother for a mutual grant ?
[/quote]

Are you saying that dCompass has no funding options other than GitcoinDAO?   

I believe that we shouldn't be investing in teams that won't invest in themselves.  If dCompass isn't going to continue without funding from GitcoinDAO, that's a pretty negative signal to me.

-------------------------

Huxwell | 2022-05-09 18:14:35 UTC | #19

No that's not what I'm saying! I mean that in the worst case scenario, if we were not able to deliver the MVP in production after season 14, I thought that it would be considered as a failure for Gitcoin DAO and that the community wouldn't even consider our mutual grant proposal.

[quote="owocki, post:18, topic:10412"]
[quote="Huxwell, post:4, topic:10412"]
Sorry it was a clumsy statement coming from [this post](https://gov.gitcoin.co/t/constructing-a-mutual-grants-committee/10347), in the context of a failure, why would Gitcoin even bother for a mutual grant ?
[/quote]

Are you saying that dCompass has no funding options other than GitcoinDAO?

I believe that we shouldn’t be investing in teams that won’t invest in themselves. If dCompass isn’t going to continue without funding from GitcoinDAO, that’s a pretty negative signal to me.
[/quote]

I've never said that and it seems clear on the conclusion of the same post that you quote above
[quote="Huxwell, post:4, topic:10412"]
**But even if we stop getting funded by Gitcoin**, **we’ll continue to work on the product anyway** and I’m confident that we’ll get better and better. So having a mutual grant agreement regardless the outcome of this proposal makes a lot of sense.
[/quote]

-------------------------

owocki | 2022-05-09 18:15:56 UTC | #20

[quote="Huxwell, post:19, topic:10412"]
I’ve never said that and it seems clear on the conclusion of the same post that you quote above
[/quote]

OK - Sounds Good.  Maybe I misread. Thanks for clarifying.

-------------------------
