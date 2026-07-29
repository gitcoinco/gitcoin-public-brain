---
id: 15398
title: "[GCP-013] Seed Universal Impact Pools"
slug: gcp-013-seed-universal-impact-pools
category: governance-proposals
url: https://gov.gitcoin.co/t/gcp-013-seed-universal-impact-pools/15398
created_at: 2023-06-15T16:47:30.610Z
last_posted_at: 2023-07-10T12:48:47.758Z
posts_count: 21
views: 4427
like_count: 103
---

# [GCP-013] Seed Universal Impact Pools

<https://gov.gitcoin.co/t/gcp-013-seed-universal-impact-pools/15398>
0xZakk | 2023-06-27 14:44:33 UTC | #1

**Author(s): [Robbie (Endaoment)](https://twitter.com/RobbieHeeger), [Zakk (Gitcoin)](https://twitter.com/0xZakk)**

**Summary**

This proposal seeks Gitcoin community approval for a grant to fund Endaoment’s Universal Impact Pools: a novel mechanism for matching donations to nonprofit organizations and a collaboration between Endaoment.org and Gitcoin’s Allo Protocol.

The proposal is requesting $60,000 in Eth from Gitcoin’s matching pool to seed the Universal Impact Pool.

**Abstract**

Endaoment is in the process of building an integration with Gitcoin’s Allo Protocol that will allow donations on the existing platform to count as votes in a Quadratic Funding (QF) round. The matching pool for these rounds will be sourced from DAOs, donor-advised funds, and charitable giving organizations. The funds will be distributed to non-profit organizations, further amplifying people’s giving on Endaoment.

This new feature, set to be released on June 29, 2023, will be a new way for communities to match funding to nonprofit organizations and bring the power of QF to a new audience. This proposal further strengthens the relationship between Endaoment and Gitcoin and is strategically aligned with Gitcoin’s goals for Allo Protocol.

**Background**

Endaoment and Gitcoin are leading the effort to innovate on new forms of community-powered, onchain impact. While focused on different types of donation-based funding, both have had an enormous impact on the ecosystem. Together, their technologies present a compelling advancement in philanthropic distribution models and an opportunity to significantly reduce governance decision making for DAOs or individuals who wish to contribute to a wide range of impact-focused causes.

Both protocols have demonstrated the capacity to raise money for public goods organizations—over $100m USD combined and growing. However, there is still a lot of friction for protocols, DAO Treasuries, and Institutional funds to participate in community-matched funding. Previously, both Endaoment and Gitcoin have tried to raise funds for causes through individual governance proposals, individual partnership, and matching efforts. Despite the available capital, success has been much greater with individual donors than with treasury distributions.

This collaboration is our joint attempt to resolve that coordination problem by using the collective activity across the Endaoment protocol as the voting strategy for distributions from a matching fund. Through one-time (or perpetual) donations to this fund, donors and DAOs alike can focus on their own missions while distributing their money in an optimized manner to a wide range of non-profits. The ability to make a single decision while maximizing global impact facilitates a much simpler process for DAO impact initiatives.

In order to create this type of fund, the Allo team at Gitcoin reached out to Endaoment ahead of the launch of their flexible on-chain community fund-matching protocol and tooling infrastructure. The combination of the two protocols’ main primitives (quadratic funding calculations via the Grants Stack and onchain philanthropic activity from the Endaoment Subgraph) presents an example of how open-source interoperable tooling for DAOs maximizes its efficacy when used in concert.

**Motivation**

Gitcoin’s support for Impact Pools is motivated by several key factors:

*1. Strategically aligns with Allo Protocol’s launch*

Endaoment’s integration proves one of the powerful ways in which existing protocols and communities can use Gitcoin’s Allo Protocol: wrapped voting. Existing protocols often attempt to incentivize behaviors like minting, staking, providing liquidity, and so on. So far, this has been done through yield or other reward mechanisms. Allo Protocol unlocks the ability for protocols to turn these same behaviors into voting in a QF round (or any other allocation strategy) by wrapping the protocol method (i.e. `mint()` or `stake()`) in a voting strategy’s `vote()` method.

*2. Creates a plurality of implementations for Quadratic Funding*

Endaoment is a strategically aligned partner to Gitcoin and is equally dedicated to creating a positive impact with web3 technologies. By integrating with Gitcoin’s Allo Protocol, Endaoment is bringing the power of QF to a new segment of web3. This integration means that internationally known nonprofit organizations such as Doctors Without Borders, the Jane Goodall Foundation, WhyHunger, Rainforest Conservancy, the Nature Conservancy, the Electronic Frontier Foundation, and many more will be exposed to QF.

*3. Creates a new impact maximization tool for DAOs (including Grants DAOs)*

This combined effort gives DAOs an entirely new tool for their grant-making and giving. Web3 organizations like ArtBlocks, Uniswap Grants, Circle, Coinbase Impact, Nouns, Ukraine DAO, Unicorn DAO, Constitution DAO, and many more already give to nonprofit organizations using Endaoment. Universal Impact Pools will give DAOs a new tool that simplifies their giving while maximizing their impact.

**Specification**

Endaoment recently kicked off development on an exciting new feature that deeply integrates Quadratic Funding. Impact Pools will be a way to further advance the donations people make on Endaoment by making them part of a QF round. Once launched, Endaoment expects to expand the feature further by running quarterly QF rounds and by eventually launching category-specific matching pools.

> “Impact pools are a new kind of matching fund geared towards a new kind of nonprofit fundraising that uses community protocol activity to allocate equitably to causes”

The first version of this integration uses parts of Gitcoin’s Grants Stack to calculate the quadratic distribution of the matching pool based on donations in Endaoment’s existing protocol. It works in much the same way that Grants Stack does: events emitted by a smart contract in Endaoment’s protocol are indexed offchain; at the end of the round, Endaoment will calculate the distribution of the matching pool based on these events. The distribution will then be shared to the nonprofit organizations on Endaoment. All of this functionality is based off of and meant to closely model how Gitcoin currently runs grant rounds on the Grants Stack.

![](upload://DM5NgRjx5vEB6fBm5YVli4n3pG.jpeg)
We will integrate more deeply with Allo Protocol as we grow adoption for this feature on Endaoment and the Allo team finalizes version 2 of the protocol. At that time, we will write custom voting and payout strategies that bring as much of the calculation and allocation onchain as possible. This will automate QF rounds, which we expect to expand to each category in Endaoment.

At a high-level, this means we will write a custom voting strategy that can be used with Allo Protocol and wrap the existing donation method in Endaoment’s smart contracts. Behind the user interface, when someone donates to a nonprofit on Endaoment, they’ll be interacting with this voting strategy, which in turn interacts with Endaoment’s smart contracts to complete the donation.

**Milestones & Timeline:**

* 05/22 - Development kicks off
* 06/23 - QA begins for Q2 Distribution Round
* 06/29 - Public launch
* 07/01 - Q2 Distribution Round ends using votes from 04/01/23 - 06/30/23
* 07/01 - Start Q3 Distribution Round
* 07/06 - Keynote presentation about Impact Pools at EthBarcelona
* 07/08 - Payout deadline for Q2 Distribution Round

**Budget**

* $60,000 in Eth of matching pool funds for the first year of grantmaking from the Endaoment Universal Impact Pool

100% of these funds will go to seeding the matching pool on Endaoment. All development and operational costs are to be burdened by Endaoment. Endaoment and MMM will co-market the launch as a successful integration with Allo Protocol (already budgeted). Allo’s Developer Relations team will continue to provide technical support for the integration (already budgeted).

**Benefits**

The benefits of this Community Proposal are:

* Endaoment has partnered with Allo Protocol to build out the first example of an important use case of the protocol: wrapped voting. This will be an open source example for how other protocols can do the same.
* Plurality of QF venues: this brings QF to a new audience and community in an organization that is strategically aligned with Gitcoin.

**Drawbacks**

The largest potential drawback for this proposal is that it could set the precedent that matching pool funds will be available for those who integrate with Allo Protocol. While we believe this is a strong, strategically aligned proposal, we recognize that matching pool funds should not always be available for everyone who integrates with Allo Protocol.

**Vote**

Yes: Vote yes to grant $60,000 in Eth to seed the Impact Pool matching pool for QF rounds run on Allo Protocol through Endaoment

No: Do not fund this grand and do not move forward

Abstain: I am missing context or this proposal needs more refinement.

-------------------------

rheeger | 2023-06-15 16:57:41 UTC | #2

GTC family, 

Just want to say how much of a joy its been to work with the whole team at Gitcoin/Allo! It's a real dream to be collaborating so closely with this amazing community of humans. We've been looking up to Gitcoin for a long long time, and we're really excited with how the Impact Pools program highlights both of our protocol's strengths.  

We're deep into integration with the Grants Stack and Allo protocols at this point, and are committed at Endaomnet to growing Impact Pools into a novel category of nonprofit-focused perpetual funding mechanisms. By using the events already emitted from regular usage of the Endaoment protocol as the voting strategy for this universal matching pool, we're providing a new way for onchain capital to be fairly and effortlessly distributed across the collective philanthropic wisdom of Endaoment donors. 

The Endaoment team is here in the forums and ready to answer any questions about architecture, implementation or ongoing plans for Impact Pools. We hope that this proposal will help set the stage for other DAOs, projects and protocols across the industry to make similar commitments to impact with treasury funds, now that the allocation is coordinated through collective decision making & more ethical quadratic funding splits. 

Excited to see this proposal progress! 

Robbie

-------------------------

dae | 2023-06-15 17:07:16 UTC | #3

Thrilled to see the teams at Endaoment and Gitcoin/Allo coming together! Can't wait to see this move forward.

-------------------------

rpedroni | 2023-06-15 17:14:11 UTC | #4

Awesome to see two giants in the giving space working together on such a novel way of doing QF & PGF, props to both communities and teams and all the hard work involved!

-------------------------

azeem | 2023-06-15 18:08:12 UTC | #5

Very excited for this proposal to move forward. Super excited to see Gitcoin and Endaoment coming together for this.

-------------------------

zbronstein | 2023-06-15 18:40:58 UTC | #8

Amazing stuff. Thrilled to be a part of this.

-------------------------

amiller61 | 2023-06-15 18:41:20 UTC | #9

Such an exciting opportunity to help generate real world impact! Kudos to both teams!

-------------------------

pedroyan | 2023-06-15 19:32:56 UTC | #10

Excited to see this new form of giving becoming a reality! :rocket:

-------------------------

jengajojo | 2023-06-16 06:57:49 UTC | #11

Glad to see this initaitive and excited to see the results. Thank you @0xZakk @rheeger 

'Yes: Vote yes to grant $60,000 in Eth to seed the Impact Pool matching pool for QF rounds run on Allo Protocol through Endaoment'

Are the orgs that we are donating to already part of the crypto community or is this a potential way to onboard them?

-------------------------

sight | 2023-06-17 00:54:42 UTC | #13

Great question @jengajojo — I’m Noah the lead designer at Endaoment who helped to shape this initiative, I’ll try to give the whole process picture since I think it shows further contexts/motivations as to how nonprofits fit in here.

All compliant US nonprofits and a growing number of global nonprofits can accept crypto as it stands, through Endaoment smart contracts. Any recipient org can onboard, at which point they can redeem donated or granted crypto as dollars in a connected wallet or bank account. Our goal is minimizing the effort for the nonprofits to benefit in increasing ways from crypto. The goal with the UIP is creating a widespread, optimized impact tool — providing additional funding to any nonprofit which receives donations or grants during a Round. This in turn creates further incentives to onboard to the crypto universe. Further, the broader good we show crypto infrastructure has the potential be, and the more seamless the integration, the more organizations of impact will seek to integrate further into web3, such as participating in GC rounds and more.

-------------------------

Randy | 2023-06-18 04:04:20 UTC | #14

Excited about this collab and the potential to introduce QF to additional nonprofit orgs. I just made my first direct donation on endoament and was curious to dive deeper into the diagram that was shared. 
It seems a bit complex being that you can donate directly and/or to a community fund. Curious to understand how the different donations will influence the matching pool allocation. 

Are all listed non profits able to participate in the quarterly round? 
If not, how will the org select participants? 
I would love to see Gitcoin nonprofit grantees participate in the round. :slightly_smiling_face:

Also, I did not see the option of using a L2 to process donations. Is this currently an option?
If not, are there any considerations of exploring this option for the 1st round? 
I personally have PTSD from gas prices during the Beta round. :melting_face: The gas fees discouraged many from donating. In particular, I feel donors/projects from LatAm and Africa took the biggest hit. I raise this concern since the intention is to make a UNIVERSAL impact and the very base of QF is the number of donors vs the quantity. 

Finally, other than the milestones/timelines shared- how will we measure success? Identifying what success looks like early on will help avoid setting the precedent that matching pool funds will be available for those who integrate with Allo Protocol since any project requesting funds will need to agree on clear/defined deliverables. 

Thanks in advance for your prompt response!

-------------------------

rheeger | 2023-06-19 18:55:10 UTC | #15

Hey Randy, 

Love the way you're thinking about this. 

Let me get some rapid fire answers your way: 

- We are only including Orgs in the matching equation for the UIP. Donations to Funds are not eligible for matching grants, as we want these matching dollars to go into the hands of nonprofits. 

- All orgs that receive donations (whether through a grant from a Private/Community fund, or through a direct donation) will receive matching funds, as long as the organization meets Endaoment's Due Diligence and Funding Policies (see docs *dot* endaoment *dot* org/governance/mission-values). 

- If nonprofit grantees from the Gitcoin community receive donations on Endaoment, they'll be included! 

- Right now, Endaoment only runs on ETH Mainnet. We hear your concerns about GAS, and are working as fast as we can to deploy Endaoment in a multichain/chain agnostic environment. We expect this to change before the end of the summer, and we plan to offer the UIP across any chain that we're operational on. This would mean donations on Mainnet/other L2s would all be counted together into the calculation. As far as this launch goes, however, it was not feasible in the timeframe to take Endaoment multi-chain and launch the UIP in the same swoop. Its a huge priority for us and we're looking forward to improving the gas experience on Endaoment in the immediate future. 

- Measuring success: we see this as an ongoing/permanent matching pool for the Endaoment ecosystem going forward. The distribution schedule at launch is set to 25% of the value of the fund at the end of each quarter. Our goal is to see individuals, projects, protocols, DAOs and companies funding the UIP over time as a catch-all donation mechanism that takes the guesswork out of deciding where & what to fund. We see success as the UIP growing more than it shrinks on a Quarterly basis, at minimum on a yearly basis. We also have built the UIP in such a way that we can introduce more specific Impact Pools around specific issue areas, allowing people to make more targeted general purpose impact (think: Arts & Humanities Impact Pool, Environmental Protection Impact Pool, Food Security Impact Pool, etc...). These issue specific Impact Pools and the interest and fundraising they generate will be a critical evaluation point in the success of the program and integration. Ideally, one year from now, we're sitting on a larger corpus than we start with in the UIP, and several issue specific Impact Pools up and running.

-------------------------

kyle | 2023-06-20 02:21:39 UTC | #16

I appreciate you both posting this, and for the details here. I love the idea of seeding more QF pools on a great platform like endaoment.

the matching pool funds feels appropriate for this given these are going to 501c3 orgs. I also love that we will be splitting this out into a quarterly round, as this gives us time to learn from and experiment with each of the rounds.

Big yes from me and so glad to be collaborating! Plurality in teams leveraging QF will enable us all to learn more, and faster.

-------------------------

Viriya | 2023-06-20 19:00:00 UTC | #17

I'm supportive of this project and am really thrilled to see Gitcoin living it's value of creating real world impact with this partnership with Endaoment! What a fantastic project to kick off the launch activities of Allo. It's really setting the tone for what our tech can enable for the world. 

I also appreciate that dev costs are being covered by Endaoment and pre-approved budget from Allo so this is not a request for additional funds from the DAO treasury. 

One interesting thing in this post to highlight is the risk/drawbacks section. 

[quote="0xZakk, post:1, topic:15398"]
The largest potential drawback for this proposal is that it could set the precedent that matching pool funds will be available for those who integrate with Allo Protocol. While we believe this is a strong, strategically aligned proposal, we recognize that matching pool funds should not always be available for everyone who integrates with Allo Protocol.
[/quote]

I think this sets a really interesting precedent and would like to encourage some thinking from PGF to decide how we might navigate these conversations going forward? Does this move signal that other projects/communities can request funds from Gitcoin's matching pool outside of a grants round? What do we say yes to? What do we say no to? Should there be a seasonal cap of how much other projects and communities can request from our matching pool? 

Further conversation to be had here for sure but I definitely don't think that these questions should block us from moving forward with this proposal :)

-------------------------

J9leger | 2023-06-26 21:17:51 UTC | #18

This makes me super excited about where Allo can be a value add to the broader ecosystem and truly just want to see it live with lots of experimentation and collaboration happening with meaningful projects and builders. 

I'm in FULL support of this experimentation and approach because of two big things:
1) Plurality and integration with partners in the ecosystem. Gitcoin has a lot of connections in the web3 native public goods space but less in the traditional non-profit world. Endaoment will be a great partner that exposes Allo's mechanisms to a new audience 
2) Creative mechanism design and integration for Allo while doing so. This helps decentralize who and how our protocols are being used which is awesome to see. 

Great job @0xZakk and @rheeger for pulling this together and as a total aside, I'm thrilled the Gitcoin Community Gathering could spark a partnership like this.

-------------------------

ccerv1 | 2023-06-27 03:53:56 UTC | #19

I absolutely love this proposal. I believe this type of funding pool is a critical bridge between legacy and web3 grant-makers. I also think this has very high upside potential. I want to see PGF scale to $100M+/year ... and this partnership should be a significant driver of new growth.

On a personal note, I would love to support any efforts to educate organizations like the ones mentioned in this post (MSF, EFF, Jane Goodall, etc) on the radical potential of QF and decentralized funding mechanisms. Similarly, sign me up for any future work to systematically measure the ROI of QF relative to other impact funding mechanisms. I am very passionate about building the legitimacy of QF as an alternative to traditional grantmaking processes!

Congrats to @0xZakk @rheeger and Endaoment for bringing this idea to life. It has my FULL support -- and I wish it a speedy journey from the forum to implementation.

-------------------------

shawn16400 | 2023-06-27 11:29:47 UTC | #20

[quote="0xZakk, post:1, topic:15398"]
We will integrate more deeply with Allo Protocol as we grow adoption for this feature on Endaoment and the Allo team finalizes version 2 of the protocol
[/quote]

This proposal is 
1) focused on the three priorities of Gitcoin and 
2) is cleverly leveraging matching funds to grow Allo 
3) leveraging the network to grow public goods funding across the ecosystem. 

To me this is a good use of resources and I will be voting for this effort.

-------------------------

davidacasey | 2023-06-28 18:11:51 UTC | #21

Really like this proposal! I can say as a representative of Funding the Commons, that we support the proposal and would be more than willing to engage our community in supporting its implementation.

-------------------------

thedevanshmehta | 2023-07-02 09:37:07 UTC | #22

What I do like about this proposal is its potential to introduce QF to non-web3 nonprofits. The system they are used to is matching fund programs ("X funder is matching you for every $1 you donate upto Y amount"), so this proposal with endaoment can change the existing norms around how such matching programs operate.

That being said, i have voted against this proposal for 2 reasons;

1. **Wash trading concerns**: There is almost nothing mentioned in this proposal on how you plan to stop a nonprofit from taking out a loan/using their reserves, donating to their own project & getting back their principal plus profit from the QF distribution.

Will you also be integrating with Passport? Will you only count whitelisted addresses or those that have donated in the past for matching funds? I'd like some more information on how you will tackle this issue.

2. **Obfuscating utility of Allo Protocol**:   You touched upon this briefly in the drawbacks section. I don't like Gitcoin directly sponsoring matching pools in the name of promoting Allo protocol as we won't know whether Endaoment & other projects are integrating with Allo because it's a genuinely useful tool or to simply obtain matching funds. My preferred approach would be connecting & recommending Endaoment /Allo protocol users to matching pool funders rather than giving it straight from our own kitty.

These are just my initial thoughts, I am open to changing my mind !

EDIT: After a healthy [twitter discourse](https://twitter.com/carl_cervone/status/1675292193135665156?s=20) with @ccerv1 , I will change my mind given sufficient guarantees on 1. sybil resistance & 2. co-funding in the impact pool. External funders to the pool will let us show the utility of allo beyond our seed investment, assuaging my second concern.

I would have ideally preferred your proposal to have targets letting us measure the gap between your promises and outcomes actually delivered.  In case you aren't able to do projections for a target, I would like you to report the following at the end of the grant period;

(example) we stopped $30,000 going towards cheating projects (of which there will be at least one); we raised $100,000 over and above Gitcoins seed fund.

-------------------------

ccerv1 | 2023-07-03 11:35:30 UTC | #23

I enjoyed the exchange as well ser :wink:

-------------------------

shawn16400 | 2023-07-11 15:54:59 UTC | #24

This snapshot vote has passed with ~100% approval rate.
Metrics:
2221 unique votes
~10M GTC tokens cast.

https://snapshot.org/#/gitcoindao.eth/proposal/0xac93297544ef49584d4c9360ef79955add4576428c81609c4b56b3f908cc425f

-------------------------
