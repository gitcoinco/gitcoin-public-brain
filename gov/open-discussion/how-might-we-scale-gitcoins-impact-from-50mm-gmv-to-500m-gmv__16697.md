---
id: 16697
title: "How might we scale Gitcoin's Impact from $50mm GMV to $500m GMV? 📈"
slug: how-might-we-scale-gitcoins-impact-from-50mm-gmv-to-500m-gmv
category: open-discussion
url: https://gov.gitcoin.co/t/how-might-we-scale-gitcoins-impact-from-50mm-gmv-to-500m-gmv/16697
created_at: 2023-10-07T05:04:43.270Z
last_posted_at: 2024-08-15T21:49:02.399Z
posts_count: 8
views: 6779
like_count: 29
---

# How might we scale Gitcoin's Impact from $50mm GMV to $500m GMV? 📈

<https://gov.gitcoin.co/t/how-might-we-scale-gitcoins-impact-from-50mm-gmv-to-500m-gmv/16697>
owocki | 2023-10-10 18:21:19 UTC | #1

![c173d4e1-a87a-4235-b3aa-0cc6ac6e18a7|500x500](upload://mCN3d3Xtua9oqjkmeuLKXmfzhy6.jpeg)

Per impact.gitcoin.co, the Gross Marketplace Value of Gitcoin sits at $50m*

I would like to offer some thoughts on how the DAO might scale that $50m GMV 10x up to $500m GMV.

Before I get into that, I'd like to tell you about a handful of hard fought lessons for me.  I've gathered these over the last few years and have conveniently summarized for you in less than one page!

1. Because we've listened to [this recent interview with Vitalik](https://www.youtube.com/watch?v=OH3dPShZwagO) we know that the public goods funding problem can be broken down into (1) funding sources + (2) fund distribution mechanisms.  These two sides of the equation need to grow in lockstep together.   

2. Because we've read @meglister 's many fantastic updates, including [Grants Stack Roadmap Updates 2023](https://gov.gitcoin.co/t/grants-stack-roadmap-updates-oct-2023/16642) and we've also read [Systematic Exploration of the Coordination Design Space](https://gov.gitcoin.co/t/systematic-exploration-of-the-coordination-mechanism-design-space/12616) in Jan 23 we know that Gitcoin has a strongly articulated vision on the "fund distribution mechanisms" side of the equation.  Quadratic Funding got us started, and we continue to innovate there, but it's not the end-all-be-all mechanism for all of public goods.  We're building a swiss army knife of fund distribution mechanisms - Quadratic Funding, Direct Grants, + TBD but more details :soon: :tm: .
    - Each of these 3 products can be thought of as fund distribution mechanisms.
         - Allo is a suite of fund distribution mechanisms targeted at developers.
         - Grants Stack is a suite of fund distribution mechanisms targeted at Grants ecosystems.
         - Passport is a fund distribution mechanism for the very hard but very valuable problem of sybil resistance.

3. Because we we've read [Where does the Gitcoin Grants Matching Pool Money Come From?](https://gov.gitcoin.co/t/where-does-the-gitcoin-grants-matching-pool-money-come-from/9036) from Nov 21 we know that we've raised money from sponsorships, NFT sales, and sometimes donations.  

4. Because we've read my post [Scaling Funding for Blockchain-era Public Goods](https://gov.gitcoin.co/t/scaling-funding-for-blockchain-era-public-goods/9797) from Jan 22 and [Public Goods funding - The Race to the Bottom](https://gov.gitcoin.co/t/public-goods-funding-the-race-to-the-bottom/15739) from Kyle in the summer of 23 , we know that we should prioritize legitimate, recurring, deep wells of public goods funding.  So far we've not yet found & tapped something that meets those criteria.  Sometimes the wells of funding we have tapped have been deep/legimate, they've not often been recurring.  

5. Because we've been following the ecosystem this summer, we know that Optimism and Protocol Guild are both on a tear lately.  The Protocol Guild (a self curated registry of ETH core protocol developers) has regularly been pulling in $1m+ sponsorships (total > $10m in the last 18 months ) and even get a TradFi ETF to donate 10% of their fees to them.  Optimism (a Layer 2 that uses Retroactive Public Goods Funding to fund it's public goods) is using revenue from sequencer fees to fund Retroactive Public Goods to the tune of $20m/quarter.    Another interesting entrant is Octant, which is using Golem Foundations massive treasury to stake + return the funds to public goods to the tune of $10m/yr+.

6. Because we [practice practical pluralism](https://medium.com/@owocki/practical-pluralism-322ab0a984c5) we celebrate these successes.. We love to see public goods get funded!  We are proud to be side by side in the ecosystem with these deeply legitimate projects + helping to serve many of the same people they serve, but with different mechanisms.  At the same time, these data points prove to us that *finding recurring/legitimate/deep wells of funding can be done, even in a bear market* and so they give us hope that we will too find a solution!  Also, how we add value to these projects by making Allo good enough that it'll help them?

7. Because we've read Vitaliks post [on where decentralization matters](https://vitalik.ca/general/2022/09/20/daos.html), we know that decentralization matters for (1) democratic decision making (2) censorship resistance (3) credible neutrality.  Because public goods funding requires (1) democratic decision making + (2) credible neutrality, we can take solace that the 24 month odyssey to rewrite the web2 products into decentralized protocols was worth it.  And that any project that wants to compete with us will have to make more effective investments in smart contract engineering, protocol design, and dapp design as well. 

Ok with those hard fought lessons out of the way...  how do we scale 10x from here?

We can (and will) keep [doing things that don't scale](https://paulgraham.com/ds.html).  Or only scale sublinearly (worse than linearly).  Things like building regen culture, chasing sponsorships, doing NFT drops.  I'd go so far as to say that we should be more organized about doing outbound campaigns to partner with other DAOs (in most cases we'd prpose to do a social/tech/token swap + we help fund their public goods as we do it ).

But the bulk of this post is about the promising things that do scale super-linearly (better than linear).  Hopefully by having a conversation about where the highest ROI is, we can start making some smart bets.

What follows is what I'm excited about.   

**Aqueducts** - I'm excited about building modular [aqueducts](https://gov.gitcoin.co/t/gitcoin-aqueduct/9684) for recurring always on funding.   Experiments I think are cool here
- Aqueducts being a formal part of Allo v2
- [The crowdfunding tool](https://community.supermodular.xyz/t/new-open-source-crowdfunding-tool/412) @carlb built while we were at supermodular:
- Taking each of our newly modularized [programs](https://gov.gitcoin.co/t/modularizing-the-program/16670) and creating separate matching pools for each round we run a la climate.gitcoin.eth, eth_infra.gitcoin.eth, eth_oss.gitcoin.eth, eth_community.gitcoin.eth, etc….
- Integrations with Superfluid and/or Radicle Drips or other similar streaming tools.
- Building mechanisms that consume hypercerts, EAS, or other standardized on-chain impact signals + intelligently distribute rewards to them.  Idk any experiments that are doing this yet, except maybe tea.xyz or OSObserver, and I'm mostly just excited about this bc [Vitalik is](https://www.youtube.com/watch?v=OH3dPShZwagO).

**Doing Grants/Airdrops for every EVM based Ecosystem** - I'm excited about the momentum that we've seen in self-serve QF and direct grants since Grants Stack launched.  There are many DAOs out there w billions$$$ in capital that doesnt have the proper distribution mechanisms out there, and we could provide that.  The meta of Airdrops is totally broken right now, and Grants Stack/Passport offer some interesting new tools to evolve that meta forward.  The market for this right now is likely in the tens or hundreds of millions$$$ yearly.

**Doing Grants for fiat ecosystems** - I think that eventually, having fiat capital on-ramps could be huge for Gitcoin.  A [recent architectural analysis even showed how this could be done](https://www.notion.so/Proposal-Fiat-donations-direct-on-ramping-to-PGN-c58eccd9d5814f6e84e28e4bcf4bb2d1), but I think we'll have to focus on EVM ecosystems first.  When the GTM for EVM ecosystems is maturing, it might be prudent to pursue more fiat ecosystems.  The TAM for this is likely in the tens of billions of $$$s/yearly, maybe even more.

**Totally new form factors for capital allocation** - I am excited to see what Allo v2 will bring, and how a fruitful developer ecosystem can be built around it .  Some experiments I'm excite for
- [Quadratic Funding Social Networks](https://gov.gitcoin.co/t/a-quadratic-funding-powered-social-network/9462)
- [Impact Stream](https://www.youtube.com/watch?v=JardevlkgQg)
- Other Allo Integrations like Buildbox, Endaoment, Sablier, or Octant.
- Allo Hackathons

I can't even estimate how big this market becuase the opportunity is so big.  But it is also very complicated GTM wise, because we are bootstrapping a developer ecosystem around our suite of protoocols - and for Allo to be successful, it must make those people successful.  Each of them have slightly different GTM considerations.

**Always on funding sources** - We should always be looking for economically exothermic areas of the ecosystem (meaning they give off funding as a byproduct of normal operations) and then plugging them into our products.  Some examples of economically exothermic parts of Ethereum:

- MEV / Sequencer Fees, especially from PublicGoods.network or other L1s/L2s.
- Contract Secured Revenue/EIP-6968 - I'm cooking up something here with Zak Cole.
- Yield from gtcETH, GLOW, etc.
- DAO Treasuries for any DAO that has a sustainable revenue model (like Uniswap, compound, or any DEFI project)

I think these are each 10$$m+ opportunities.  But we lack any well-funded special teams that have a mandate dedicate to pursuing them and most of them emerge as underfunded side projects.

**Passport -**  Passport has the opportunity to do for sybil resistance what twilio did for SMS.    I wrote a bit about how big of an opportunity I think passport is [here](https://gov.gitcoin.co/t/passport-is-our-aws/10995) last summer.  More on their roadmap [here](https://www.notion.so/gitcoin/Passport-SSOT-e5d4df27d3c54192a947efe315f3f550).  I think there's likely a billion $$$$ market here. The TAM for human identity tools is literally everyone on earth who has an internet connection.

**Internal stuff** - OK, this one is different than the above ones.  It's purely an internal-centric one.  

**> 1. Speaking each others language internally**
I think the one important thing we can do is build up inter-workstream and inter-skillset and inter-network shared understanding + empathy.  We are building an [impact network](https://gov.gitcoin.co/t/lessons-about-impact-networks/10305) shouldnt we be following those best practices? 

How do we create more [common knowledge](https://www.youtube.com/watch?v=v7YbnY1JUhg) about our paths to the most important thing.  Each pocket of important common knowledge can serve as a shelling point for getting important shit done + delivering more Ws than Ls.  This would stretch all of us, because it means that engineers need to speak sales, that BD needs to speak computer science, that we all rally around the product managers for what they need, but it would be high upside if we could.

**> 2. Create a formal organization-wide value heuristic**

I think another intra-workstream thing we could do that would reinforce this is to [we need to make value-delivery + the creation external facing W's the social-political currency + actual economic currency of the DAO](https://twitter.com/owocki/status/1704204134625464515) .  I'd even go so far as to one day formalize this so that everyone is clear on the rubric they are judged against:

A proposed anchor point for the question of "how much is my team generating value?" could be: 

> w₁ = GTC_utility_produced + revenue_generated_in_usd

In the event that a product is pre-revenue their weight can be determined by 

> w₂ = size_of_subDAO_economy_in_usd

I have a whole 'nother post about this I can drop if ppl are interested.  DM me if you want a preview.

**> 3. Decentralization wen?**

I expect that the next 12-18 months will be focused on product/protocol adoption and we will start thinking about ossifying Gitcoin's governance *only after reaching product market fit*.  

I have a whole 'nother post about Gitcoin's path to ossifyication I can drop if ppl are interested.  DM me if you want a preview.


**A rising tide lifts all boats** - Gitcoin is a bet on EVM ecosystems continuing to grow + proliterate.  We are riding Ethereum's network effects like a tide that is lifting all boats.  If Ethereum grows 10x in the next decade, that could lift Gitcoin's boat as well.

One tangible sign of this happening already is that Gitcoin has started raising funds from Optimism Retro PGF + from Octant.  We are extremely blessed to be in a growing ecosystem with a. pluralism of other innovators within the area of public goods funding :)

.


Thanks for reading to the end.  When I think about the next 10x, the above is what I'm excited about.  What are you excited about? 

----- 
 - **impact.gitcoin.co needs an update: the GMV number is actually  ~$52m ish after beta rounds/gg18 but for the purposes of this post, lets call it 50m)*
- **impact.gitcoin.co also doesnt reflect the total size of the sybil resistent economy on Gitcoin Passport.  if you take the sum of all the cost of forgeries on Passport and/or the rewards that have been given because a user has a passport, i estimate that it's between 3-7.5 million $$$ tho*
- Not financial or tax advice. This content is strictly educational and is not investment advice or a solicitation to buy or sell any assets or to make any financial decisions. This post is not tax advice. Talk to your accountant. Do your own research.

-------------------------

carlosjmelgar | 2023-10-08 19:13:59 UTC | #2

[quote="owocki, post:1, topic:16697"]
TradFi ETF to donate 10% of their fees to them.
[/quote]

Normies present a huge opportunity. I've heard @azeem express interest in pursing entities outside of our bubble, including governments. Outsiders see the potential in crypto, but don't know how to take the leap. Many governments have branches focusing on tench/ innovation and climate; this is a great opportunity imo. We do have to go into those opportunities accepting that they want to "Fund What Matters" to them. They probably don't want to YOLO funds into OSS and Eth Infra without being able to produce tangible and relevant results. I've been discussing a featured round with our local Tourism Board. It's been a slow conversation, but I see lots of potential in bridging normies to Ethereum PGF.

[quote="owocki, post:1, topic:16697"]
outbound campaigns to partner with other DAOs (in most cases we’d prpose to do a social/tech/token swap + we help fund their public goods as we do it ).
[/quote]

Ethereum needs more cross DAO coordination. I love this idea. Gitcoin should also b e exploring the opportunity to participate in other DAOs as a delegate(s). Gov forums are where you [find the real alpha](https://gov.push.org/t/discussion-a-community-run-push-grants-program-v3/1484). This is an opportunity to tap into ecosystem grants programs early. The cross DAO integrations can tap into "always on". 

[quote="owocki, post:1, topic:16697"]
There are many DAOs out there w billions$$$ in capital that doesnt have the proper distribution mechanisms out there, and we could provide that. 
[/quote]
Agreed above. Building relationships through governance participation has potential to balance the constant sales hustle we have now. Not sure what workstream this would fall under at the moment. Maybe a combination of GSD, PGF and MMM? 

[quote="owocki, post:1, topic:16697"]
**> 1. Speaking each others language internally**
I think the one important thing we can do is build up inter-workstream and inter-skillset and inter-network shared understanding + empathy. We are building an [impact network](https://gov.gitcoin.co/t/lessons-about-impact-networks/10305) shouldnt we be following those best practices?
[/quote]
We can be doing a better job at this. The contrast in response to PGF for DEI/ Shell vrs. MMM for discord + twitter hacks and the recent GTC highlight a disbalance in empathy within the DAO in my eyes. Not saying MMM deserves harsh treatment, just wishing PGF received similar empathy in public forums. Most was external, but some was also from our own. 


[quote="owocki, post:1, topic:10305"]
Most people love the idea of collaboration as long as it promises to do exactly what you want to do. But that’s not how collaboration works, Collaboration is not forced or coerced. Collaboration is hard because to collaborate you need to give up control.

Networks are networks of relationships. Relationships between network participants is the core basis of trust that allows for antifragility of the network.
[/quote]

This gave me lots to think about how I handle collaboration attempts that don't go my way, Thanks for linking that article.

-------------------------

owocki | 2023-10-08 19:45:50 UTC | #3

thanks for the thoughtful response carlos!  i've got a few areas i want to respond/engage eventually.. but this one is one that immediately brings up something for me

[quote="carlosjmelgar, post:2, topic:16697"]
The contrast in response to PGF for DEI/ Shell vrs. MMM for discord + twitter hacks and the recent GTC highlight a disbalance in empathy within the DAO in my eyes. Not saying MMM deserves harsh treatment, just wishing PGF received similar empathy in public forums. 
[/quote]

i might be overindexing on this.. but i would challenge everyone to look at such divisions like the differences between MMM/PGF (but also other divisions like misaligned priorities between the grants stack/allo team) one layer up the governance stack.  eg try to look at it from a network level instead of a narrative level.  one way to induce this frame is "imagine youre kevin/kyle/a gtc steward/anyone else with a network wide vantage point and people are always coming to you to complain about each other and you're just trying to figure out protopia aka figure out how to piss away less budget/brand/opporutnity-cost on any type of coordination failure, especially feifdom-like, conflict every quarter"

from the perspective of PGF for shell, everyone throwing them under the bus.  from the perspective of MMM, they feel stuck also but in different ways.

from where i stand its just a lot of finger pointing across the groups/feifdoms.   while it's gotten a lot better since a year ago, gitcoin still (in some palces) looks like microsoft whereas i think it maybe should look a bit more like facebook's org or like an [impact network](https://gov.gitcoin.co/t/lessons-about-impact-networks/10305).

![2011.06.27_organizational_charts|512x500, 75%](upload://lWq65ptBPya3z7wJxZJCqblfZCl.jpeg)

feifdoms are a really bad way to organize in a competitive ecosystem if you think about it from first principles for a bit.

![F6aMi8UaUAE0kUT|690x375, 75%](upload://w2bky84ObnwFlLlVsQ5ST1i43kZ.jpeg)

some ways to solve this
- modularize the workstreams to be smaller + so there is surface area for feifdoms to evolve
- formalize the conflicts between groups into a political economy where these modules compete in a market against each other
- formalize the way the dao makes budgeting decisions to align budgets with those who create value so that people always have a SSOT on where their job/salary stands ( a la `job_security = prioritization = GTC_utility_produced + revenue_generated_in_usd`. ) without having to go through some tribal leader to get an answer.
- solve for the fact that low engagement/low output individuals can stick around indefinitely without being noticed (as long as theres no active layoff round going on).  conversely, solve for the fact that high engagement/high output individuals do not have job security.
- follow the best practices from [impact networks book](https://gov.gitcoin.co/t/lessons-about-impact-networks/10305) (especially the ones about building trust across social difference)
- recognize that we shouldnt expect to "solve" for this anytime soon, but instead this will be a slow backburner process of "addressing" it for the next 12-18 months while the DAO is focused on the object level issues of its competitiveness in a crowded markets + product market fit + revenue.
- bring in external stewards who have a lot of clout + time to engage + pick apart the issues. i have a unicorn i might bring in / announce soon
- "culture eats strategy for breakfast" so realize that many of these issues are cultural / training.  invest in education to build the right regen cutlure internally.

-------------------------

carlosjmelgar | 2023-10-08 19:53:20 UTC | #4

[quote="owocki, post:3, topic:16697"]
“culture eats strategy for breakfast” so realize that many of these issues are cultural / training. invest in education to build the right regen cutlure internally.
[/quote]

[Impact Networks](https://www.amazon.com/Impact-Networks-Connection-Collaboration-Catalyze/dp/1523091681) audiobook is $6. We should fire up a DAO (core, community, stewards, partners POC) book club with a review at the end of the month. You get a POAP and next month's book if you read it. Education, culture, team vibes.

-------------------------

owocki | 2023-10-08 21:10:07 UTC | #5

IIRC we did a "gitcoin gathering hour" with the author @daviderlichman about 15 months ago.   we could dig up the recording or invite him to come back + talk about it again

-------------------------

ccerv1 | 2023-10-09 15:28:28 UTC | #6

Epic post. This feels like one that will end up in the Gitcoin canon!

A few reactions:
- $500M GMV is a good target but still a drop in the bucket relative to legacy PGF. It's how much the country of Chad [currently](https://www.theglobaleconomy.com/rankings/government_spending_dollars/) allocates to PGF. (Have fun with that meme btw)
- Vitalik often talks about [convex vs concave](https://vitalik.ca/general/2020/11/08/concave.html) outcomes. I think he brought it up in the latest greenpill podcast ep too. The unanswered question is whether complex yet largely concave allocation mechanisms like QF offer superior results than simply allocating a pool of money evenly across a set of projects (or using some other extremely simple heuristic).*
- If we can demonstrate that crypto PGF is (a) more cost efficient for ecosystem funders and projects,  and (b) leads to better allocation outcomes, then I think we get to $500M very fast.

Let me also disclose that I have a horse in this race -- and am betting that decentralized impact measurement is the linchpin! There's a sweet spot we have yet to find between qualitative and quantitative allocation mechanisms.

(*) Edit: for further reading, checkout [this experiment](https://www.aeaweb.org/articles?id=10.1257/aer.20151404) in Nigeria: "Random assignment of US$34 million in grants" or listen to the [Planet Money episode](https://www.npr.org/sections/money/2016/05/20/478883658/episode-702-nigeria-you-win) about it

-------------------------

owocki | 2023-10-09 15:43:10 UTC | #7

[quote="ccerv1, post:6, topic:16697"]
* $500M GMV is a good target but still a drop in the bucket relative to legacy PGF. It’s how much the country of Chad [currently ](https://www.theglobaleconomy.com/rankings/government_spending_dollars/) allocates to PGF. (Have fun with that meme btw)
[/quote]

this is true!  i think that 10x growth is a hard thing to do, but 1000x feels insurmountable.  so thats why i chose a target horizon of 10x.

[quote="ccerv1, post:6, topic:16697"]
* Vitalik often talks about [convex vs concave](https://vitalik.ca/general/2020/11/08/concave.html) outcomes. I think he brought it up in the latest greenpill podcast ep too. The unanswered question is whether complex yet largely concave allocation mechanisms like QF offer superior results than simply allocating a pool of money evenly across a set of projects (or using some other extremely simple heuristic).*
[/quote]

i think that is an important unanswered question (esp while Gitcoin is primarily QF).  but once we go multi mechanism w the launch of allo v2, there are oppportunity to build mechanisms that take concave inputs and create convex outcomes (like assurance contracts + dominance assurance contracts).  this is an important diversification opportunity for gitcoin

[quote="ccerv1, post:6, topic:16697"]
Let me also disclose that I have a horse in this race – and am betting that decentralized impact measurement is the linchpin! There’s a sweet spot we have yet to find between qualitative and quantitative allocation mechanisms.
[/quote]

decentralized impact eval is def part of the equation and i hope there are partnership oppies in the future!

-------------------------

mars | 2024-08-21 23:52:16 UTC | #8

[quote="owocki, post:1, topic:16697"]
I would like to offer some thoughts on how the DAO might scale that $50m GMV 10x up to $500m GMV.
[/quote]

Some pretty basic and pretty obvious suggestions:

# 1️⃣ To have 💰💰💰 ready to be deployed

When you have $500m of money to be deployed, there is a large amount of ways to spend it.

The easiest and the fastest way to achieve $500m in GMV (Gross Marketplace Value) is to have $500m burning your pocket.

# 2️⃣ Showcase / illustrate / demonstrate the value generated

I think that majority of the Web3 stack was at some point funded by Gitcoin.

**Showcase success stories.**

I think [GainForest](https://x.com/gainforestnow) is quite successful.

I think Sablier is quite sucessful:
* [Sablier Labs Raises $4.5M Seed Round](https://blog.sablier.com/sablier-labs-raises-seed-round/)
* Bootstraped on Gitcoin: https://www.gitcoin.co/blog/gitcoin-grants-round-4

**EDIT / UPDATE:** Uniswap to large extent was funded on Gitcoin (and Etheruem Foundation grants):

![image|661x500](upload://nZEjSKEVIgopujZoMUTfr0gNnCl.png)



# 3️⃣ Onboard nation states to Web3 regen ReFi stack

![image|679x500](upload://3G5yfSus9PbKSXblz2eUgNSRfiS.png)

$500m is 10x from where we are right now, but in the grand scheme of things: conservative estimate.

[quote="mars, post:1, topic:18875"]
# Going 100x from here

Shared this [thought on Discord](https://discord.com/channels/562828676480237578/1047159914956591114/1243934533326475385):

> Gitcoin has easy potential to go 100x from here, I can totally imagine a prosperous country like Norway or Saudi Arabia gives us 1% of their sovereing fund budget to fund public goods.
[/quote]

That's achievable, that's not unrealistic.

![image|690x394](upload://epwKofrffyiF7tDMon1LXpOexHj.jpeg)

# 4️⃣ Inspire big vision:

Imagination + inspiration + dreams = does not require capital upfront.

> '*If your dreams* do *not scare you*, *they* are *not big enough*.'

-------------------------
