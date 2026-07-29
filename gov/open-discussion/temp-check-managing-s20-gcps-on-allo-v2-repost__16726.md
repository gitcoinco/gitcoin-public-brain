---
id: 16726
title: "Temp Check: Managing S20 GCPs on Allo v2 [Repost]"
slug: temp-check-managing-s20-gcps-on-allo-v2-repost
category: open-discussion
url: https://gov.gitcoin.co/t/temp-check-managing-s20-gcps-on-allo-v2-repost/16726
created_at: 2023-10-09T21:44:17.191Z
last_posted_at: 2023-10-12T05:08:52.390Z
posts_count: 7
views: 4425
like_count: 14
---

# Temp Check: Managing S20 GCPs on Allo v2 [Repost]

<https://gov.gitcoin.co/t/temp-check-managing-s20-gcps-on-allo-v2-repost/16726>
nategosselin | 2023-10-09 21:44:17 UTC | #1

**NOTE: the original post was deleted somehow, so this is a repost**

### Summary
The Allo workstream is proposing to manage the administration of Season 20’s Gitcoin Community Proposals (GCPs) on Allo v2. This post outlines the key components of the idea and looks for feedback from the community.

We believe that implementing this proposal would enable us to:
- Lower the barriers to entry for our community members to get involved with Gitcoin
- Proactively seed GCP ideas with the community
- Test-drive “microgrants” as an Allo use-case
- Enable us to dog food the protocol and build momentum for v2

### Format in brief
A GCP budget of $75k would be deposited in an Allo v2 “microgrants” pool, to be distributed over the course of S20. The Allo team would build a front-end app that would enable users to submit GCPs, empower authorized users to approve (more on that below), and allow anyone to view submitted GCPs and their status. 

Anyone would be able to apply for a GCP, as long as they align with focal areas that will be published by the workstream leads.

### Mechanism and approvals
One of the core goals of GCP is to lower the barriers to useful contributions for our community. In order to achieve this, we want to create a relatively simple “microgrant”-style approval path for GCPs that doesn’t require a full community vote. While the exact mechanism is being fleshed out in partnership with the workstream leads, our initial plan is to give approval power to the stewards so that a relatively small number of stewards will be able to approve most GCPs. We welcome mechanism suggestions if you have them.

### Budget: $75k
The budget for this proposal is only the $75k required to fund the GCP pool. The app will be built by the Allo team as part of their S20 resourcing and will not require additional funds. 

### Timeline
The Allo team will be using the Shape-up methodology (as outlined with [Alloscan](https://gov.gitcoin.co/t/introducing-alloscan/16566)) to build the mechanism and app. We are setting an “appetite” of 4 weeks, meaning that we will fit the feature scope of the project so that we can have a finished product in a maximum of 4 weeks. In practice this may mean that we trim scope over the course of the project, but still enable the product to execute the core functionality of operating microgrants. 

To put this to a calendar, the team is currently working against the timeline below. Please note that some of these periods are variable (i.e. remediation could take longer) and that dates could shift as a result:

- Now - 10/20: audit remediation
- 10/23 - 10/27: v2 mainnet deploy week
- 10/30 - 11/3: Profile builder v1 (simple app for creating a v2 profile)
- 11/6 - 12/1: GCP microgrants app build
- 12/4 - 12/8: GCP microgrants app goes live

While this timeline means that we will not have the app live for the first month of S20, we feel that this still gives us the bulk of the season for GCP distribution and is a valuable way for us to dog food v2 this season. 

### Conclusion
Using Allo v2 for the administration of the Season 20 GCP budget is a significant step towards enhancing transparency, community engagement, and effective allocation of resources within Gitcoin DAO. We believe that this proposal aligns with the DAO's mission and values and will contribute to the continued success of the Gitcoin ecosystem. Furthermore, we think this is a valuable experiment for Allo v2 that we think we could ultimately offer to other DAOs. 

We welcome community feedback on this idea!

-------------------------

DistributedDoge | 2023-10-09 23:03:04 UTC | #2

Very much in support of anything that streamlines smaller proposals entering the DAO.

Amount may seem high in contrast to other experiments run by Gitcoin, but if stewards/workstream-leads oversee the funds I see it as equivalent of increasing DAO-wide contractor budget by a negligible amount.

I also think DAOs have a real need for a scalable software that helps to organize and distribute micro-grants/mini-bounties, so this product could be interesting addtion to Allo toolbox.

-------------------------

FractalVisions | 2023-10-10 13:55:12 UTC | #3

This is fascinating 🧐 to us and see the flywheel for GTC governance will open up in 2024 with Allo as a centrifuge of this grant funding mechanism. Helping to separate the liquids from the solids in a way that extrapolates grant funding opportunities for many other communities. 

Shining light 💡 on public goods projects in many areas of the world that have yet to be touched. Each of the micro grants can ultimately uncover what one might see as a GEM (Grants Ecosystem Module) of the Gitcoin ecosystem.

Here is what we imagine the ecosystem will look 👀 like afterwards.

Every GEM 💎 added to the protocol will increase the brightness 🔆 of the GTC mothership. The sustainability of QF & RPGF for projects can become a key component of the crypto industry as each micro grant improves upon old broken legacy systems that no longer serve us. Reflecting back towards a multifaceted public goods sector in the future that leaves no stone 🪨 unturned. Helping to slowly patch back together a monetary system that no longer resembles a closed wall garden by breaking down the digital divide and opening the flood gates of prosperity for those who need it the most due to their valiant efforts to create a better world.

![image|500x500](upload://6GuhZEoI0iTHCVZDR3E72M0mG3z.jpeg)

-------------------------

meglister | 2023-10-10 21:57:35 UTC | #4

Super excited about this!! I have a few "yes ands"/builds...

- Assuming that if the $75k is not spent, it will be returned to the treasury or we'll have a vote to roll it into the next cycle?
- IIRC, we've only had 2 GCPs (Web3 grants report + conf sponsorship) actually go to a vote since May. It seems like we'll get more value out of this experiment with a higher volume of grants/proposals -- wonder how we might be able to instigate that?

-------------------------

owocki | 2023-10-11 04:34:30 UTC | #5

[quote="meglister, post:4, topic:16726"]
It seems like we’ll get more value out of this experiment with a higher volume of grants/proposals – wonder how we might be able to instigate that?
[/quote]

id be interested to see the workstreams issue "missions" or "intents" for things they want to see done by Gitcoin Citizens next quarter.  

this helps the work-streams build the muscle of "build in public" and also focuses the community energy on what the workstreams want done.  it also instigates a higher volume of grants/propoals.

some examples:
- PGN workstream could issue a intents to see stuff built on PGN
- BD or Grants Stack workstream could issue a referral bounty for anyone referring a new DAO with over > $x in assets to run a pilot round
- Once the plugin architecture is built, Grants Stack could issue intents for what types of features they want to see built into Grants Stack.
- Allo could issue intents for what they want to see built on protocol.
- MMM could issue intents for people to do x y or z type of marketing during

these are only suggestions for the types of intents/missions that could be issued by workstreams.

-------------------------

owocki | 2023-10-11 04:37:17 UTC | #6

[quote="FractalVisions, post:3, topic:16726"]
Every GEM :gem: added to the protocol will increase the brightness :high_brightness: of the GTC mothership. The sustainability of QF & RPGF for projects can become a key component of the crypto industry as each micro grant improves upon old broken legacy systems that no longer serve us. Reflecting back towards a multifaceted public goods sector in the future that leaves no stone :rock: unturned. Helping to slowly patch back together a monetary system that no longer resembles a closed wall garden by breaking down the digital divide and opening the flood gates of prosperity for those who need it the most due to their valiant efforts to create a better world.
[/quote]

off topic, but i wrote a bit about the modules in the gitcoin ecosystem a bit [here](https://gov.gitcoin.co/t/3-transitions-from-gitcoin-1-0-gitcoin-2-0/16736#h-1-centralized-product-decentralized-modular-protocols-4) - itd be fun to continue your meme here and do a beautiful visualization/inventory of the GEMs (similar to [https://supermodular.xyz/coordination-mechanisms/](https://supermodular.xyz/coordination-mechanisms/) but for the gitcoin ecosystem ).  perhaps that could be an intent or a bounty i issue to the community and it will attract a graphic designer/frontend dev to do it!

-------------------------

FractalVisions | 2023-10-12 05:08:52 UTC | #7

I love this so much I can’t stop thinking about it.
Thanks so much for sharing. Inspiring to say the least.

I will put this link 🔗 in our resources channel for the devs to check out.

-------------------------
