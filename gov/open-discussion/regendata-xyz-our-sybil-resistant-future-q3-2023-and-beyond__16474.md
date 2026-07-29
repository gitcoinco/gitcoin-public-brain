---
id: 16474
title: "RegenData.xyz + Our Sybil-Resistant Future Q3 2023 and beyond"
slug: regendata-xyz-our-sybil-resistant-future-q3-2023-and-beyond
category: open-discussion
url: https://gov.gitcoin.co/t/regendata-xyz-our-sybil-resistant-future-q3-2023-and-beyond/16474
created_at: 2023-09-06T22:51:53.147Z
last_posted_at: 2023-09-13T21:28:59.930Z
posts_count: 6
views: 5715
like_count: 33
---

# RegenData.xyz + Our Sybil-Resistant Future Q3 2023 and beyond

<https://gov.gitcoin.co/t/regendata-xyz-our-sybil-resistant-future-q3-2023-and-beyond/16474>
owocki | 2023-09-06 22:57:30 UTC | #1

[![|506x500](upload://aybKMyLaX4TG2PuPkXiIK9Qi267.jpeg)](https://twitter.com/thedevanshmehta/status/1692603574252101985?s=46&t=X0oQ26a3ezptVAZLp1QFaw)

This document is meant to describe the sybil resistance investments being made for S18/S19/S20, and to begin to describe what a minimum viable anti-sybil future looks like.

This document was prepared by:

1. @umarkhaneth 
2. @ghostffcode 
3. Owocki
4. @Jeremy 

# Problem Statement

The Gitcoin anti sybil ecosystem has many different moving parts.

1. The transition from cGrants => Grants Stack/Allo/Passport
2. The transition from FDD => ODC.
3. The cluster mapping project by Joel Miller.
4. The YOLO data analysis that Umar does to support Connor in anti sybil work.

As it stands right now, there is no group that is formally responsible & enabled via budget to deliver solid anti sybil results for the program (especially GG18). Passport is focused on their product. PGF works on fundraising & round ops. Our aim is to build the glue between these groups and enable anti-sybil to be better every round than it was the last round.

Anti sybil at Gitcoin is an ongoing evolutionary game between the anti-fraud folks (blue team) and the sybil/collusion attackers (the red team). We aim to empower a diverse & decentralized ecosystem of blue teams to stay ahead of the red team’s evolving tactics.

Right now, the anti sybil pipeline is pretty barebones. Umar has a series of scripts & data sources that he uses to put together an analysis that he delivers to Connor/PGF.

# Solution

Our hope is to enable Umar to contribute his data sources, scripts, and methodology into a resource known as RegenData.xyz (formerly [Grants-ETL](https://gov.gitcoin.co/t/grants-etl-a-new-tool-to-make-pulling-data-for-anti-sybil-anti-collusion-analysis-easier/16060))... which any data scientist has easy access to. By enabling this community of data scientists to have access to all the data they need without writing a bunch of custom ETL scripts + also have access to Umar’s tools very easily, we will empower these data scientists to do what they are good at (finding sybils) and not what they’re not (cleaning data, writing data gathering scripts). This ecosystem of data scientists will be able to do their own sybil/collusion analysis and contribute back to RegenData.xyz, ultimately creating a plurality of approaches & a community of practice around anti sybil/collusion at Gitcoin.

![|624x229](upload://kGNdN29c4HSgCV5Olxk8mevT4qG.png)

Instead of relying on personal relationships between Umar + Connor, this community of practice will have a diverse tapestry of relationships.

Further, we will be developing this community with community/ecosystem funding to draw in and retain top data scientists.

All in all, this initiative is designed to help the blue team systematically stay ahead of the red team by accelerating the Blue team OODA Loop end-to-end:

![|624x419](upload://l0EDTCU82SjVTUJ36K6BgPcp2oW.png)

# Goals

What are our goals for the future?

## Near term priority

* good sybil resistance for GG18
* get Umar reports on grants-etl

## Med term priority

* Good sybil resistance for GG19
* Add in the ability to update these passport scoring algorithms with blocklist + data that we find.
* give all of this to ODC & other groups (publish via OCEAN, etc)
* Co-develop community driven lists (Humans/Good actors, Sybil / Bad actor, Attacker(s), Suspicious, etc)
* Fund Red Team Work Through a QF Round (come take the matching pool if you tell us how you do it)

## Long term priority

* Invite outside community contributions + support them with funding.
* Integrate Joel Millers cluster mapping algorithm.
* Nurture a community of blue-team contributors.
* Introduce more governance to the process.

## Ongoing priority

* Make sure Grants-ETL has the latest data + reports in it.
* Iterate + Revise the ecosystem as we learn.

## Call to Action

If you are interested in getting access to this toolset / community, please join the [RegenData.xyz community on telegram](https://t.me/+rMPm30SrC583NjZh).

-------------------------

umarkhaneth | 2023-09-10 01:26:28 UTC | #2

There are three big challenges we've been discussing in reaching this future I want to explicitly call out here

1. Attracting sufficient talent - We need more data scientists. We're boosted by the ODC. Evan has done a great job stewarding this community as a data science hub. They've been thought-partners and their members spent time to try to assist Connor's sybil squelching in the Beta round. They also were willing to extend their help for the Citizens round and now GG18. Their team continues to put effort into this area and develop greater expertise in Anti Sybil. They'll be invaluable partners in continued work. We should also seek to draw in the many sybil hunters in other communities like Hop, Connext, and Optimism to learn their methods, collaborate, and build a schelling point around anti-sybil work. 

2. Assessing the accuracy of our methods - There is no answer sheet. We have to know how our methods perform in order to pick the best from among them to use, focus on, and develop but we don't know who the sybils are and aren't. What'll likely be most helpful here is backtesting on the lists we do have, visualizing on-chain activity, and some manual evaluations. 

3. Not giving the game away - As we invite people to be a part of our sybil resistant future we also invite the sybils in to come learn how we're detecting them. There is a tipping point in adversarial games where being completely transparent is more of an advantage than a disadvantage. When open-sourcing increases the talent made available to help our blue team to such an extent that it outweighs the disadvantage we give up to the red team. Until we reach that point, we're discussing what it looks like to use permissioned tiers among new members of the blue team to unlock greater access to developed detection methods.

-------------------------

jengajojo | 2023-09-11 07:01:42 UTC | #3

Thanks for summarising current state of anti-sybil strategy. 

- Is it possible for non GG rounds or anyone using the grants stack in their own communities to get access to sybil defence for their own rounds? Maybe sybil defence as a service?

[quote="umarkhaneth, post:2, topic:16474"]
Not giving the game away
[/quote]
This is a good point. Is there an open document today which the red team can read up on to get a overview of which sybil strategies have been identified?

-------------------------

umarkhaneth | 2023-09-13 14:59:52 UTC | #4



[quote="jengajojo, post:3, topic:16474"]
Is it possible for non GG rounds or anyone using the grants stack in their own communities to get access to sybil defence for their own rounds? Maybe sybil defence as a service?
[/quote]

Yes absolutely 

[quote="jengajojo, post:3, topic:16474"]
This is a good point. Is there an open document today which the red team can read up on to get a overview of which sybil strategies have been identified?
[/quote]

No that would help the sybils too much. 

Good questions!

-------------------------

mars | 2023-09-13 15:46:57 UTC | #5

[quote="umarkhaneth, post:4, topic:16474"]
[quote="jengajojo, post:3, topic:16474"]
Maybe sybil defence as a service?
[/quote]

Yes absolutely
[/quote]

# 💯 💯 💯

The sybil-resistance is practical for Gitcoin matching rounds as well as broader Web3 ecosystem.

### Related: Hop Protocol 25% bounty

*(this could provide ongoing revenue stream for "good guys" team)*

https://decrypt.co/143231/hop-protocols-sybil-hunter-payout-unveils-powerful-new-airdrop-tool

> If all checked out, those hunters were to be rewarded 25% of all HOP tokens with a one-year lockup.

Some more links in the theme:

* https://github.com/ArbitrumFoundation/sybil-detection
* https://mirror.xyz/x-explore.eth/AFroG11e24I6S1oDvTitNdQSDh8lN5bz9VZAink8lZ4
* https://www.coindesk.com/consensus-magazine/2023/04/10/crypto-airdrop-sybil-attacks/

-------------------------

FractalVisions | 2023-09-13 21:28:59 UTC | #6

I just wanted to share my two cents here for the day!!!

We worked really hard early on last year to help beta test with Guild and give them as much feedback as possible to improve the UI and UX of their product. Shortly after we watched many other protocols and integrations expand to utilizing this platform for safeguarding their communities. 

Including Gitcoin passport.

https://guild.xyz/

I figured this was worth sharing to help give others guidance on how they can also make participants of their community more honest when it comes to building their ecosystem during or in between the donation rounds for quadratic funding on Gitcoin.

Also, I must add that it’s really cool you can purchase the Gitcoin governance token directly on this platform..!!

https://x.com/fractal_visions/status/1701457846184161640?s=46&t=_8dkepIOA6H5XhasVM4F9g

There are many other tools out there that are also very useful through this platform you might find will help increase the Sybil prevention efforts of your ecosystem.

Shield 🛡️ is also one of our ecosystem partners  that has a integration with Guild to detect users wallet behavior activities onchain.. They have helped significantly to provide safety amongst all allowing us to sleep a little bit better at night.

https://www.getshield.xyz/

I hope to add value to the Gitcoin ecosystem by sharing our trials and tribulations over the years along with additional resources or tools 🧰 we have recently learned about.

Personally we have watched many grant systems become highly sought out by these methods of gaming the system. So we must be extra diligent when implementing these prevention mechanisms in order not to give away the secret sauce.

If you like what we do and want to help support us on our mission we would love to have you in our guild as well..!

We want to set a safety standard & positive example for others to use as a template for their own ecosystem. Feel free to check out our template for your own ideas. Give us some feedback and if you have any questions, please let us know!

https://guild.xyz/fractalvisions

-------------------------
