---
id: 9981
title: "Gitcoin Grants 2.0"
slug: gitcoin-grants-2-0
category: gitcoin-grants
url: https://gov.gitcoin.co/t/gitcoin-grants-2-0/9981
created_at: 2022-03-01T17:00:02.826Z
last_posted_at: 2022-06-24T22:05:18.759Z
posts_count: 22
views: 12564
like_count: 109
---

# Gitcoin Grants 2.0

<https://gov.gitcoin.co/t/gitcoin-grants-2-0/9981>
kevin.olsen | 2022-06-01 15:44:02 UTC | #1

# Grants 2.0

Authors
[Lindsey Thrift](mailto:lindsey@gitcoin.co)
[Kevin Olsen](mailto:kevinolsen@gitcoin.co)

## Purpose of this document:

* Bring awareness to the current thinking inside the Gitcoin Product Collective (GPC) to the rest of the Gitcoin ecosystem
* Broadcast our intentions to the workstreams in the DAO to align efforts and identify overlapping efforts or unaccounted for needs
* Build the muscle of communication, anticipating the need to participate in governance in the near future.

## Who this doc is for:

* DAO Workstream participants
* Stewards
* Engineering, Design, and Product within GPC
* frens

## Intro:

By: [Kevin Owocki](mailto:kevin@gitcoin.co)

Grants 2.0 is the accumulation of all that we’ve learned since launching Gitcoin Grants in January 2019 + evolving it for the last 3 years.

Not only are we solving for decentralization with 2.0, we are also solving for the “meta-problem”.

* The “problem” is public goods funding.
* The “meta-problem” is finding the optimal capital allocation tool for public goods funding.

Instead of a centralized monolith (1.0), grants 2.0 will be forkable, modular, and decentralized.

Instead of having a grants protocol w QF in it (what we did with 1.0), we will create a protocol w a deep liquidity of grants on it, & create an ecosystem on top of it where different flavors of public goods funding can compete to optimally allocate capital on top of it (2.0).

![|420x196](upload://3ELRwiVb7hCoYGYccYia277rDUA.jpeg)

Once grants 2.0 is launched, we will have created an environment where the community can test different public goods funding mechanisms on top of a deeply liquid registry of grants. This tool will allow us to speedrun the “[hill climbing problem](https://cdixon.org/2009/09/19/climbing-the-wrong-hill)” of finding optimal democratic mechanisms for funding public goods.

![|268x117](upload://zVnvKXLzrd2hraTKKl5GbYFXfX3.png)

## Product Vision

From open source software to [public goods](https://otherinter.net/research/positive-sum-worlds/) in the physical world, DAOs and other ecosystem builders (collectives of people) are seeking to gather community signal on where to invest as well as get their initiatives funded.

As [an impact and protocol DAO](https://gov.gitcoin.co/t/the-impactdao-protocoldao-sandwich/8944), Gitcoin envisions a world with thousands of public goods funding rounds running at any given time, distributing capital in an optimal manner that is governed by the community being served. We imagine a future where DAOs and ecosystems can spin-up/skin/fork our Gitcoin Grants experience to participate directly in the Gitcoin Grants ecosystem, and allow them the flexibility to rapidly experiment and to best deliver a grant experience that matches the needs of their community. Gitcoin will build the foundation for on-going, open source development of the tooling, standards, and substrates necessary to reach maximum scale of public goods funding distribution through development of the Gitcoin Grants Protocol.

In accomplishing our vision, grant owners, round owners, and grant funders are all sovereign actors that facilitate their funding coordination through the Gitcoin Grants Protocol.

### Strategy Outline

To achieve our vision, we will build a protocol with a SAM (simple, antifragile, modular) design and plugin architecture such that we are not too tightly coupled to any particular elements of the protocol.

By doing so, the protocol is a container that:

* allows Gitcoin to speedrun the evolution of optimal capital distribution by being able to rapidly test and scale novel mechanisms and embed grants everywhere public goods projects are organizing and launching (such as integrations with DAO service platforms or Retro Public Goods Funding).
* enables the simple adoption of powerful tools that prevent fraud and sybil attacks, and encourage manipulation and curation of the data presented (ie, the Grants that are visible in the interface, the grants that are eligible in a round, the matching funds available, any matching fund caps, etc.).
* Creates opportunity for DAOs to use governance mechanisms to curate and govern their grants program, consequently creating utility for their governance tokens

The protocol must be built in a fundamentally open source manner that not only allows but encourages contributions from the community to advance it - developers are a first class citizen in the Gitcoin Grants ecosystem, and the Protocol will be well documented and have a thriving developer community. If we are successful, a plugin marketplace will emerge and the opportunity for anyone to contribute to the evolution of funding public goods will be within reach.

We will build for the [L2 and multichain world](https://ethereum-magicians.org/t/a-rollup-centric-ethereum-roadmap/4698/57) by maintaining most data in decentralized schemas off-chain and allowing smart contracts to be round specific and composable based on where a round manager chooses to deploy and what token they choose for funding and governance.

Finally, we will decouple grants from rounds so that grantees have a credibly neutral means by which they can create, manage, and update their grants agnostic of any grant round in which they may participate.

## Architecture Overview:

We envision the solution as 4 new code bases: decentralized Proof of Personhood Passport ([dPopp](http://proofofpersonhood.com)), Grants Explorer, Grant Publisher, and Round Manager.

These four apps correspond 1:1 with the core processes and domain concepts that exist within the current centralized and monolithic gitcoin code base.

![|624x377](upload://5289Rl7L6wf13QcYlBV28XooiL5.png)

Note: there is an important architectural change that is implied here that differs from the current gitcoin.co experience. Namely, that each round is a distinct end to end experience, as opposed to the current gitcoin.co that is something of a meta-experience or round aggregator - whereby many grants corresponding to different rounds are presented together with a unified ‘checkout’ experience.

Here, we are imagining each round having a grant explorer that is a distinct dApp that would launch to provide a customizable experience, putting grant curation and discovery in the hands of the community governing that round.

![|624x456](upload://i50uDfZVdRSv56ZL1paT42qkte0.png)

## The road to decentralization:

Our goal is that by the end of Q1 2023 we can run Gitcoin Grants Rounds on a new constellation of software products that cover the core capabilities that gitcoin.co currently provides - giving our platform credible neutrality, opening up our protocol to a broader grants ecosystem, and allowing us to [prototype & test different funding mechanisms](https://twitter.com/owocki/status/1496513186442395649) more rapidly.

#### ![|624x331](upload://qSyzsNr2rwMCn49pe4v87ZWNiix.png)

Starting immediately after GR13 the Gitcoin.co web application will effectively go into maintenance mode. This means the GPG team will only be addressing critical issues to the platform.

As we make progress on our delivery of the decentralized applications we will begin deprecating portions of the gitcoin.co experience and migrating to the new dapps that deliver the corresponding functionality.

#### dPopp

We will kick off the development of dPopp before the end of Q1 2022, and hope to have an MVP before the end of 1H 2022, with the stretch goal of deprecating the trust bonus UI and migrating the gitcoin.co trust bonus experience to dPopp. It is our backstop estimate that the trust bonus in gitcoin.co will be replaced in Q3 2022.

#### Round Manager and Grant Publisher

We will proceed to move through the core functions of the main web application, deprecate functionality in the main web application, and migrate to the corresponding dApps as we deliver them. The Round Manager and Grant Publisher will kick off in Q2 2022 and we hope to have a working end to end system sufficient to allow an alternate protocol to share the underlying decentralized grant registry in GR14. We are orienting this work to enable CLRFund to run a parallel round in GR14 that would demonstrate the decentralization of our registry, while also allowing for a comparison of CLRFund MACI with the existing Gitcoin QF fund distribution mechanism.

#### Grant Explorer

Finally, we will begin development of the Grant Explorer in Q2 2022 to build up to an end to end system that will allow gitcoin to open up our grant protocol to other DAOs.

## The End of the Monolith

It is our goal to deprecate most of the core gitcoin experience by GR16. Given the UX differences between the multiple separate rounds from the current centralized gitcoin experience we expect we may need an additional quarter to deliver a unified UX that replicates the multiple round grant exploration our users expect from gitcoin.co. By Q1 2023 it is our hope that this last piece of development will allow us to completely migrate away from the original gitcoin.co web application, and for us to retire the monolith.

## Questions You Might Have Now

* How is this good for the Gitcoin DAO?
  * It enables a project to start up with Gitcoin and for Gitcoin to gain utility from projects that find product community fit (PCF) through governance token swaps etc. This is a critical component of achieving the [impact DAO protocol DAO sandwich mission](https://gov.gitcoin.co/t/the-impactdao-protocoldao-sandwich/8944).
* Will Gitcoin DAO continue to run grants rounds or will they all be self-run by DAOs and ecosystems?
  * Growth of the Gitcoin grants rounds have shifted from vertical scaling (more money into the main round for the Ethereum community) to horizontal scaling (more matching pools funded by other novel ecosystems and collectives with shared cause based missions).We have identified that the total addressable market of this horizontal scaling and very large and feel confident the growth of this scale on the centralized platform is validation to continue investing in this scale through decentralizing the platform into an open source protocol. 
Gitcoin DAO will continue to run their own round while also assisting others in the running of their rounds (what we call side rounds today). We expect the Gitcoin Grants Protocol will enable Gitcoin DAO to continue to experiment with initiatives such as Aqueduct to discover the highest impact ways of running rounds and supporting ecosystem growth.
* Why would we separate rounds from grants?
  * So that rounds can be run on any chain, by any party, in any manner they wish and grants can be included in those rounds as (1) the grant owner desires to be included and (2) the grant project meets the eligibility criteria of the round
* Why not just SaaS-ify the the round management platform to expedite the building and maintenance of it?
  * By making round management independent of a centralized platform, round managers can configure and build upon the round structure to fully tailor to their needs and to make simple mechanism decisions that fit their needs; it’s likely that the value of creating token utility for DAOs to be able to use their governance tokens for curation and for ecosystems L1/L2 builders to use their native tokens for matching payout increases the inherent value of the Gitcoin Grants Standard and Schemas over building it themselves or using something “off the shelf”.
  * Building a fully open-source protocol also means that we are building a public good that no longer depends on Gitcoin to exist and creates the opportunity for the emergence of a plugin marketplace.
* Why doesn’t this vision and strategy center on quadratic funding?

## Where do we go from here?

We have been working this past month to align this roadmap with Kevin, Kyle, the FDD, GrantOps, our delivery partners, and the GPG. It is our hope that this document will serve as a strong foundation for continued evolution. We welcome any and all feedback to this plan!

So what do we need to pull this off? Besides the focus and a bit of inspiration we’ll need to actually build this thing, we’ll need some help keeping people oriented on the end state while gitcoin.co slows down the rate of improvements. Going into maintenance mode might be hard for some of the team; namely, customer service, or sales might feel neglected as we build the future platform. Helping keep the community and team oriented on the goal of a decentralized multi-DAO future will take everyone’s help articulating the benefits, and weighing the tradeoffs between current and future pains and gains.

If you have any questions, if you see things we may have missed, or have any feedback please tell us. We would love to have the broadest community buy-in to this plan that we can achieve, and we look forward to working together with this community to bring the gitcoin core technologies into [the great revival](https://gov.gitcoin.co/t/the-great-bear-the-great-reset-the-great-revival/9855).

-------------------------

Fishbiscuit | 2022-03-02 04:29:16 UTC | #2

Thank you @kevin.olsen and congratulations on your first forum post! (great meeting you irl at ETHDenver and Boulder btw)

Based on the current architecture, I would imagine that the Public Goods Funding Workstream might evolve to support this as a 'round manager' that could run all sorts of different types of funding rounds for different ecosystems and causes with this product suite as the underlying stack. Potentially this might mean even educating other organisations and foundations on how to run rounds of their own. What do you think? @ceresstation 

I really like how grants will be evolving and am excited to see it happen!

-------------------------

nategosselin | 2022-03-02 15:05:45 UTC | #3

Very excited to see this out in the world. Can't wait to start building :fire:

-------------------------

thelostone-mc | 2022-03-02 15:21:04 UTC | #4

Would these individual teams also share quarterly plans to ensure DAO is informed of the progress as these units likely are to operate independently and overlap over common pieces ?

I would advocate for these and hold them at the same level as other streams so as to ensure these team doesn't work alone but instead with input / feedback from DAO at a high level

-------------------------

lthrift | 2022-03-02 17:51:37 UTC | #5

A lot of this architecture and product vision have been informed by the way the Gitcoin Grants program/Public Goods Funding Workstream have evolved over the the last 12-18 months with the significant scaling of siderounds and community appetite for aqueduct. 

So yes, the modularity and composability of the architecture are to support that continued evolution as we seek to build the tech that enables the amazing work Public Goods Funding Workstream is embarking!

> Potentially this might mean even educating other organisations and foundations on how to run rounds of their own.

Yes! We have heard from PGF that they plan to educate others on best practices for running founds. We hope this is another flywheel effect between the tech and operations of scaling public goods funding. It should also provide a short feedback loop between how the tech is (or is not) enable round management since we're working together within the DAO.

-------------------------

kevin.olsen | 2022-03-03 11:06:28 UTC | #6

I think we're still in the phase where we're building up our governance muscles here in the [Gitcoin Product Collective](https://i.imgflip.com/66ckr5.jpg) but you're spot on that the end state vision is one where we are converging on the workstream governance model. 

It's our hope that posts like these will help broadcast our intentions and bring in collaboration from the DAO, and ultimately create a smooth transition when this work finds it's home as one or more funded workstreams inside the DAO.

-------------------------

DisruptionJoe | 2022-03-03 12:14:09 UTC | #7

I especially like this line of thinking. With the new setup, we will be thinking less about "who will donate" and more about "how do we help them grow their ecosystem". 

I see PGF being instrumental in:

* Listening to customer feedback and suggesting tools to improve round running UI/UX to Moonshot Collective
* Continuing operations for a main and/or Ethereum round
* Building playbooks of "round running best practices"
* Discovering best practices by enabling round experiments like what are being discussed in the [https://gov.gitcoin.co/t/proposal-gitcoin-gr13-matching-pool-allocations/9915/20](https://gov.gitcoin.co/t/proposal-gitcoin-gr13-matching-pool-allocations/9915/20)
* Setting up materials with MMM to begin collecting top of the funnel contacts to solicit for future rounds

-------------------------

ceresstation | 2022-03-03 21:06:23 UTC | #8

I'll likely edit this to respond in more detail when time permits, but I just want to say amazing job on this roadmap @kevin.olsen @lthrift. I'm super optimistic about the direction put forward here, and specifically about the level of thought put into our path towards decentralization. Excited for the great revival.

-------------------------

lthrift | 2022-03-03 22:57:08 UTC | #9

> * Listening to customer feedback and suggesting tools to improve round running UI/UX to Moonshot Collective

I don't think this feedback would/should go to Moonshot Collective, but directly to the product team that is building this tooling. Innovation and continuous improvement should be a principal and practice of all teams building software for Gitcoin, not just Moonshot Collective. 

A bit of a tangent for a separate post, but Moonshot Collective has the opportunity to really be the "[blue ocean](https://www.clearpointstrategy.com/blue-ocean-strategy/)" focused team on the continuum of the product development lifecycle within [Gitcoin Product Collective](https://i.imgflip.com/66ckr5.jpg). 

![Screen Shot 2022-03-02 at 7.35.23 PM|690x202](upload://nNai1oh1xSs7twGfUvcD8D8iATi.png)

-------------------------

DisruptionJoe | 2022-03-04 18:31:16 UTC | #10

I am starting to see a marketplace develop that allows a user to plug and play their own rules for a grants round. They would select inclusive vs exclusive logic for grant eligibility, funding mechanism, and a sybil vendor. One example of these might be community curated, using QF Pairwise, and dPoPP standard sybil defense. 

Do you see moonshot innovating on the marketplace for each of these solutions or on new protocols and dapps altogether? (While acknowledging that it is their decision)

Is that how you see the Gitcoin ecosystem expanding as well?

-------------------------

annika | 2022-03-05 02:11:33 UTC | #11

Very excited for this proposal. Super well-crafted and clearly a lot of long-term thinking here. This will be critical to making grants our grants program even better accessible to the community & scalable for years to come. 

Thank you for all this work!

-------------------------

lthrift | 2022-03-08 04:38:08 UTC | #12

:100:

I think Moonshot could certainly be innovating on new protocols and dapps in this space, but I don't think they will be exclusively. My hope is that the future of Gitcoin Grants is not only built in an open source manner, but that strategy enables the open source expansion of the Gitcoin ecosystem. :seedling:

-------------------------

krrisis | 2022-03-15 04:22:28 UTC | #13

Great and visionary overview, finally caught up on this and all comments below. 

I believe this post will be quoted often in the future, so for that reason, a little possible thing to edit is under 'questions you might have, this last bullet point... 

[quote="kevin.olsen, post:1, topic:9981"]
Why doesn’t this vision and strategy center on quadratic funding?
[/quote]

... seems to be missing an answer? 

Another question I personally have: will any of the work previously done by the dgrants team be recycled? Is part of what was done in that workstream over the past 6 months worth integrating into this new initiative?

-------------------------

thelostone-mc | 2022-03-21 06:51:40 UTC | #14

[quote="krrisis, post:13, topic:9981"]
Another question I personally have: will any of the work previously done by the dgrants team be recycled? Is part of what was done in that workstream over the past 6 months worth integrating into this new initiative?
[/quote]



The work done by the dgrants team was to build out a POC which I believe we succeed.
Building out the actual integration using the learning from the dgrants POC.
While it is too early to say if code would be re-used, I do believe our decisions made here would be based off what we built out on dGrants

-------------------------

kevin.olsen | 2022-03-24 10:29:17 UTC | #15

Good eyes spotting that dangling question there, that definitely got lost in the writing/editing process. 

The answer was hinted at here:

[quote="kevin.olsen, post:1, topic:9981"]
opening up our protocol to a broader grants ecosystem, and allowing us to [prototype & test different funding mechanisms ](https://twitter.com/owocki/status/1496513186442395649) more rapidly
[/quote]

So to flesh that out: our goal is to unbundle the gitcoin grants user and management experiences and provide a container that allows for a pluralistic future with many parallel mechanisms being deployed by different communities. Imagine a smaller ecosystem with high levels of trust, perhaps a DAO funding grants for internal teams, or an IRL community offering a small curated list of grants for their member to steer. We could see non-QF mechanisms being the right fit, and we want the grants 2.0 protocol to be the logical first place to stand up that grant program, and let these communities experiment on the meta-problem space of optimal distribution of funds for public goods.

-------------------------

nollied | 2022-04-06 23:33:21 UTC | #16

i love this so much! 

is there more progress on this? is there a way I can be part of this conversation more often? 

it seems like there's a symmetry for the work you guys are doing with modular design to facilitate mechanism design prototyping and what we're doing in "The Matrix" (which I'm renaming to "Mechanism Design" for next season) squad within FDD. 

part of the vision is to build a simulation environment to do agent based behavioral analysis (using reinforcement learning/game theory) in an environment that is *as close to reality as possible*. [Here is a rough document explaining our vision](https://docs.google.com/document/d/1oWP95oiNrSSZbcMlPVAy6KcjIizG-juxzk0lPDFtdJY/edit?pli=1#).

i think it would be amazing if we met in the middle of our orthogonal perspectives and collaborate.

-------------------------

kevin.olsen | 2022-04-11 10:54:23 UTC | #17

[quote="nollied, post:16, topic:9981"]
i love this so much!
[/quote]

Awesome! 

[quote="nollied, post:16, topic:9981"]
is there more progress on this? is there a way I can be part of this conversation more often?
[/quote]

Yes, we've kicked off 2/3 workstreams, and will be kicking off the explorer/round manager here soon. I'd love to get you across the project, especially given the amount of overlap in thinking about mechanism plurality, data sharing, personhood/community anti-fraud signals... the list goes on.

It's great to see the dialogue unfolding across multiple channels, but I'm noticing the challenge of broadcasting, and sustaining a conversation around Grants 2.0. If you have some thoughts on a better way for us to keep people informed and involved (updates, community calls, dedicated channel in discord) I'd appreciate your ideas.

-------------------------

seanmac | 2022-04-12 17:51:17 UTC | #18

Would love to help you get this support, definitely part of how a product marketer could help. Haven't gotten any submissions to this yet, would love any help from anyone in promoting or making introductions to folks who might be interested. 

https://twitter.com/smacmannis/status/1511814732914651138?s=20&t=LnWwE5ZwrwV-1C_qjewb4w

-------------------------

nollied | 2022-04-29 04:53:38 UTC | #20

for sure! honestly having a discord channel dedicated to grants 2.0 where i and other interested parties can communicate with you guys that would be cool.

-------------------------

kevin.olsen | 2022-05-05 12:03:05 UTC | #21

I think you've joined, but for transparency in the conversation here we've just spun this up! Currently limited to DAO contributors, with the potential to open up wider as we build our community engagement muscles: https://discord.com/channels/562828676480237578/970928914740437043

-------------------------

zkWolf | 2022-05-20 20:20:46 UTC | #22

Hi guys. We built a coordination tool for DAOs and creators to collect feedback. 

I created a sequence for this Gitcoin Grants 2.0 post as an example of how DAOs can use the tool.  Please [have a look](https://app.zeevo.co/dashboard/sequences/e13db9a2-5bf2-4e6f-b33f-0f6c3f5b6fc9) and let me know what you think.  

I also put together a quick write-up on how the tool works and how DAOs can use it [here.](https://mirror.xyz/zeevoco.eth/v8hH_cLES4HASpKb9dgJq-_G9kL-u_PioaYykkS5-PA) 

Sorry for the slightly off-topic post. I blame @owocki for getting me jazzed up about DAO coordination tooling :stuck_out_tongue_winking_eye: 

Hopefully, the Grants 2.0 team will find the tool helpful for keeping in sync with the DAO at large!  :pray:

-------------------------

thetagan | 2022-06-24 22:05:18 UTC | #23

My favorite part about this is that it is expanding the science laboratory. Though QF is an older concept, Gitcoin is testing new variables with new equipment. Now, we are able to upgrade after analyzing the test results. 

Creating better systems for funding public goods is the goal. So, what role will data scientists play in the future development of Gitcoin? How will they work with product designers? 

Furthermore, how can Gitcoin have a macro impact on policy design? What data from Grants 2.0 can help inform economic and governance design?

-------------------------
