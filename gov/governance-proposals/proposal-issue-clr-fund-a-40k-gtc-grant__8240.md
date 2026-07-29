---
id: 8240
title: "Proposal: Issue CLR.Fund a 40k GTC Grant"
slug: proposal-issue-clr-fund-a-40k-gtc-grant
category: governance-proposals
url: https://gov.gitcoin.co/t/proposal-issue-clr-fund-a-40k-gtc-grant/8240
created_at: 2021-08-15T18:39:06.636Z
last_posted_at: 2021-09-29T16:35:25.689Z
posts_count: 31
views: 8925
like_count: 97
---

# Proposal: Issue CLR.Fund a 40k GTC Grant

<https://gov.gitcoin.co/t/proposal-issue-clr-fund-a-40k-gtc-grant/8240>
lefterisjp | 2021-08-15 19:03:07 UTC | #1

# Summary

![image968|690x200](upload://ff4iGjXIBygmR6LBz7VFBbWzZ8r.png)


This proposal, if passed, would issue a grant of 40k GTC (0.008% of the GTC treasury) to CLR.Fund, a project with a similar mission as Gitcoin (fund public goods) but with a complementary product.

Disclaimer: This proposal was co-authored/reviewed by @austingriffith , @auryn, @owocki and myself.

# Abstract

CLR.Fund is another prominent Quadratic Funding project in the Ethereum ecosystem with a mission/ethos that is similar to Gitcoin. This proposal issues them a grant, which solves for the near term the funding of CLR.Fund.

Secondarily, this proposal if passed would

1. Extend [previous friendly contact between Kevin Owocki and Auryn MacMillian](https://twitter.com/nanexcool/status/1383481998417678342) to formally affirm that Gitcoin & CLRFund are friendly projects built around similar missions.
2. Change the narrative created by other competitive projects working on the same domain. That is the misguided belief that we must have sharp elbows - boxing each other out from each other’s users and demonstrate loud social media clap-backs.
3. It is possible that the goodwill between the two projects could be extended into a formal integration or partnership one day - especially with the [Decentralize Gitcoin workstream](https://gov.gitcoin.co/t/workstream-suggestion-decentralize-gitcoin/180) gaining speed.
4. By pushing new tech and solutions on top of QF (such as MACI), CLR.Fund can act as a testbed/testnet for future gitcoin features and visa-versa.

# Motivation

Gitcoin’s mission is to build & fund the open web. Gitcoin has done that in a few ways, Ethical Ads, Hackathons, Grants, and KERNEL.

Gitcoin Grants is a [prominent pillar](https://gitcoin.co/results) of the Gitcoin ecosystem, and momentum from Gitcoin Grants has been extended to many similar QF projects - recently [Downtown Stimulus](http://twitter.com/dtstimulus) and [FundOSS](http://twitter.com/_fundoss) were driven by the Gitcoin team. Outside of the Gitcoin team, CLRfund, RXC Voice, and Build Guild have been shipped by other teams in the ecosystem.

Similarly to CLR.Fund, Gitcoin Grants is reliant on [Quadratic Funding](https://wtfisqf.com/). A mechanism for “the mathemtically optimal democratic funding of public goods.” Although QF is very powerful, there are a number of problems with QF - scaling it involves solving thorny governance problems - Sybil resistance and collusion resistance are prominent examples. The exploration of this design space is a public good to all QF projects - insofar as the learnings advance all QF projects towards their missions.

For this reason - It is our assertion that CLR.Fund’s implementation of Quadratic Funding is complementary to Gitcoin. Most notably, in the following ways.

* It is pushing forward MACI.
* It is pushing forward sybil resistance & collusion resistance.
* It is funding public goods in the Ethereum ecosystem.
* It is iterative and increasingly effectively proven itself, having run [7 rounds so far](https://blog.clr.fund/).
* Gitcoin Grants has [funded CLR.Fund](https://gitcoin.co/grants/524/clrfund) $33k in the past.
* The CLR.Fund has taken UI/design inspiration from Gitcoin Grants, and extended them to their decentralized QF protocol.
* Given that Gitcoin’s existing Grants product is centralized, and work to decentralize is ongoing, a partnership with CLRFund could be a fruitful way to accelerate the decentralization of Gitcoin Grants - and also to make Quadratic Funding in the Ethereum ecosystem more anti-fragile (similar to how there are many client implementations of ETH2).

# Specification

This proposal if passed would transfer 40k GTC to `0xadca3cF41e2e2517F1862b3CA18E8beF561EEded` - the address specified in the [CLR Fund Governance Doc](https://github.com/clrfund/governance) as the contributor funds address.

This grant is a no strings attached gesture to the CLR.Fund team. It is possible the two projects may formally work together in the future, but not a requirement for the dispersal of funds.

# Benefits

See “Motivation” section above.

# Drawbacks

40k GTC would be removed from the treasury.

-------------------------

ntnsndr | 2021-08-16 04:30:18 UTC | #2

Is there a justification for the particular amount specified here? Why not 30K? 50K?

And is it worth considering this an example of how to model a more reciprocal relationship among DAOs, toward the DAO network [described recently](https://gov.gitcoin.co/t/the-gitcoin-gitcoindao-egregore-is-emerging/) by @owocki? Token swaps, governance, etc.?

-------------------------

nya-elimuai | 2021-08-16 07:27:10 UTC | #3

[quote="lefterisjp, post:1, topic:8240"]
40k GTC (0.008% of the GTC treasury)
[/quote]

Phrased differently: 40k GTC is 0.28% of the *current circulating supply* (14,211,563 GTC). Also, I'm a bit confused, because it was stated in Discord that it is "not probable" that more GTC tokens will be minted: https://discord.com/channels/562828676480237578/846742089392062545/875099923572478003

CC @androolloyd

-------------------------

DisruptionJoe | 2021-08-16 13:35:09 UTC | #4

These wouldn't be newly minted tokens. The split of the tokens minted at inception was half to past contributors and half to a community governed treasury to build the future. Read more about it here: https://gitcoin.co/blog/introducing-gtc-gitcoins-governance-token/

-------------------------

wschwab | 2021-08-17 07:23:11 UTC | #5

I don't see a proposal on the Snapshot - is there a date in mind for opening the proposal, and also what kind of voting period would there be?

I think having good commms on a proposal like this is important too - this isn't a criticism of anything specific, but I've noticed that people tend to miss important proposals and then feel like they got ninja-passed or the like. (There is a core dev who has contributed to EIPs that everyone has heard of who missed the London Hard Fork until after it happened, and made a comment about it being rushed without anyone knowing about it. I suppose he missed the bat crowd on Twitter, or, more likely, doesn't hang out on Twitter at all.) How can we make sure there is maximum transparency on this?

-------------------------

lefterisjp | 2021-08-17 08:55:25 UTC | #6

Hey @wschwab in general the snapshot vote happens at least after 1 week of deliberation on a proposal in the forums.

The approach we try to take on governance is laid out in [this post](https://gov.gitcoin.co/t/gitcoin-dao-governance-process-v1/7860/21).

The way to get more eyes on something is to keep tweeting about it and mentioning it in discord I guess, so that more and more people participate.

----

Regarding the proposal there was also a small convo in Twitter between @androolloyd, @auryn and myself where there was a request of CLR fund to also contribute to the Decentralize gitcoin workstream. The discussion can be seen [here](https://twitter.com/androolloyd/status/1426987033306800133).

-------------------------

Pop | 2021-08-17 10:45:57 UTC | #7

I'd definitely love to see some concrete plans @auryn & clr fund would have with the funds? It's then easier to maybe setup some milestones or identify concrete benefits deriving from this disbursement of funds

-------------------------

lefterisjp | 2021-08-17 11:29:34 UTC | #8

Agreed. I think that the things that were discussed in Twitter as per my post above can and should be formulated more formally in a post in this topic.

-------------------------

55kai | 2021-08-17 11:32:20 UTC | #9

[quote="lefterisjp, post:1, topic:8240"]
CLR
[/quote]

I don't think this will bring any help to the community. No matter what cooperation you say in the future, there is no promise. The funds of the treasury cannot be misused in this way. Unless CLR makes a commitment in specific cooperation and giving back to the community

-------------------------

auryn | 2021-08-17 20:30:38 UTC | #10

Hi Simona! :wave: 

Yeah, this is a really valid question.

I'll start by acknowledging my obvious bias in this vote. Given that bias, I'll abstain from casting a vote. Anyone that wants to vote on this and has delegated to me should delegate to someone else for this proposal.

My understanding of this proposal is that it is less about specific future deliverables and more an acknowledgement of past work pushing the Quadratic Funding and Ethereum Public goods space forward. So I'd be inclined to view it in the same spirit of the [Retroactive Public Goods funding post](https://medium.com/ethereum-optimism/retroactive-public-goods-funding-33c9b7d00f0c) that Optimism recently published. In other words, this would be the Gitcoin DAO explicitly saying *"we value the contributions you have made to the QF space and want to align our future efforts towards funding Ethereum's public goods"*.

That said, I do think there are specific deliverables that we are already planned and would be beneficial to the Gitcoin DAO, that could be much more easily achieved given this extra funding.
Specifically, we are:
1. Building a production ready decentralized QF protocol, with baked in Sybil and collusion resistance, that can scale to billions of users.
2. Making it easy for anyone to deploy their own instance of the clrfund to fund whatever public goods they want, including both the contracts and the app.
3. Building in a modular and extensible way so that instances of clrfund can choose the governance, Sybil resistance, and recipient registry solutions that best suit their community and use-case.

This funding would allow some of our contributors to focus on this full-time, along with bringing new talent in (likely from the Gitcoin community via bounties).

One important thing for the Gitcoin DAO to consider is if/how this fits with the [decentralize grants](https://gov.gitcoin.co/t/decentralize-gitcoin-workstream-budget-request/8121) workstream.

-------------------------

kingsdami | 2021-08-17 21:38:40 UTC | #11

What's the plan for the 40k gtc... how's it to be used

-------------------------

PersonChile | 2021-08-20 03:54:50 UTC | #12

Clr.Fund , desde sus inicios a estado ayudando a proyectos con muy poco volumen 500 usd 100 usd sucede que en algunos paises es mas importante comer que tener financiamiento.

Sin duda apoyaria esta alternativa demostrando que realiza un trabajo etico para la comunidad , si la comunidad se guia por lo que ve y no le gusta la financiacion bajen los fondos a 35K pero sin duda son grupos que no hay que dejarlos solos por un click de distancia.

-------------------------

php | 2021-08-21 02:42:18 UTC | #13

Good question, I also wonder if something like stream or vesting/time lock would make such grants more flexible?

-------------------------

cojocaru | 2021-08-22 05:47:45 UTC | #15

2 questions arise in my mind:
1. how the funds would be spent?
2. how this investment would benefit the Gitcoin community?

-------------------------

lefterisjp | 2021-08-23 17:32:26 UTC | #16

(2) is answered in the OP and by Auryn in his reply.

For (1) I think it's a good question. Auryn went into a bit more detail in his response but perhaps a more official breakdown of costs and a timeline could help alleviate some of the people's concerns here as the amount is indeed rather big.

-------------------------

auryn | 2021-08-23 19:31:27 UTC | #17

In more concrete terms, at the current GTC value, this would give us the capacity to hire ~2 full-time developers and a full-time product manager for the next year, which would radically increase the rate that we can ship the features mentioned above. The other place that some small portion of the funding may be used is to cover infrastructure costs for running the coordinator, since computing the ZKPs can be pretty demanding.

There is some variability to how far this funding will get us, since we would obviously not intend to cash it out immediately.  Ideal case, we could find folks who want to be paid in GTC so there is no need to convert it at all. Otherwise, we would need to convert some portion of periodically (say monthly or quarterly) to cover dev costs.

-------------------------

lefterisjp | 2021-08-23 20:52:20 UTC | #18

Are people satisfied with the answers provided by Auryn and the CLR.fund team? Is there any more things that need to be discussed before we move onto a snapshot vote?

-------------------------

Pop | 2021-08-24 18:38:25 UTC | #19

thank you for detailing this + the even more specific answer re hiring. It would be fantastic if we could identify people wanting to work on GTC payout bounties to further CLR.Fund mission. 

I'd also really love to maybe see a collective report on QF co-authored by Gitcoin and CLR Fund that essentially details the huge progress made in the space since QF became a "thing". This could also really further people's understanding of the concept AND the uptake in setting up/funding grants for future rounds in both projects...

-------------------------

auryn | 2021-08-24 18:52:40 UTC | #20

[quote="Pop, post:19, topic:8240"]
I’d also really love to maybe see a collective report on QF co-authored by Gitcoin and CLR Fund that essentially details the huge progress made in the space since QF became a “thing”
[/quote]
Yeah, I think this would be a really valuable piece of content. Although, at least from clr.fund's side, we'd probably want to wait until after we've run at least one production scale round before authoring a report like this.

-------------------------

griff | 2021-08-26 01:56:32 UTC | #21

Retroactive funding for the win. I would absolutely support this proposal. 

CLR.fund has made huge contributions to the QF space and supporting basically the only "competitor" is exactly the right vibe.

We are all allies in the public goods space. 

I will vote for this without any reservations.

That said, I think it would be in the best interest of GTC to see some vesting requirements in basically all of these large grants... I don't think they have to be even on chain... just a friendly understanding that the holdings would only be liquidated at a certain rate... And definitely would not be "diversified" upon receipt. 

Honestly, with this team I don't even think it would need to be said, they are crypto savvy, understand token economics, and have a culture of making win-win deals... I assume they will hodl the GTC unless they need it. That said.. it would prob be cool to be explicit about that in all big grants that don't have any milestones.

-------------------------

auryn | 2021-08-26 02:05:29 UTC | #22

[quote="griff, post:21, topic:8240"]
That said… it would prob be cool to be explicit about that in all big grants that don’t have any milestones.
[/quote]

Yeah, I have no qualms with this at all. Perhaps some vesting schedule with a clawback option for the Gitcoin DAO would be a good way to put people's mind at ease. Above I mentioned that, at the current value, this could cover one year of costs for two devs and a PM, plus some misc. expenses. So perhaps vesting it continuously over the course of a year, or in four discrete tranches, would make sense.

As much as I'm confident that we could be trusted to do it on a handshake, we have a variety of great tools available to us to eliminate the need for trust, so we may as well make use of them.

-------------------------

makoto | 2021-08-26 14:14:49 UTC | #24

[quote="auryn, post:10, topic:8240"]
My understanding of this proposal is that it is less about specific future deliverables and more an acknowledgement of past work pushing the Quadratic Funding and Ethereum Public goods space forward. So I’d be inclined to view it in the same spirit of the [Retroactive Public Goods funding post](https://medium.com/ethereum-optimism/retroactive-public-goods-funding-33c9b7d00f0c) that Optimism recently published.
[/quote]

Hi. I am overall supportive of the effort clr.fund is doing but I do wonder why we need a separate proposal to acknowledge the past effort. The normal Gitcoin round should fulfil that purpose.

If we pass a proposal without set goals, targets, and deliverables, it may be very difficult to assess the effectiveness of the value delivered. I do suggest changing the format to the "Budget proposal" type.

-------------------------

kyle | 2021-08-31 14:23:18 UTC | #25

I love this idea, specifically the thought that collaboration and the sharing of ideas can flow between teams. CLR.fund is further ahead in MACI and thinking through nested matching pools while Gitcoin is further ahead in scale.

Could we set the expectation that each team connect every two weeks to share current work and brainstorm on learnings and roadmaps a bit? The DOT and KSM analogy sounds wonderful given how tightly those groups collaborate.

@auryn - Would you be open to a sync every two weeks (or whoever is doing the building) to ensure both teams can learn from experiences of the others? When Gitcoin launches the dGrants protocol, the learning will be invaluable from the CLR.fund side to make sure we are offering complimentary experiences.

-------------------------

auryn | 2021-08-31 17:47:24 UTC | #26

[quote="kyle, post:25, topic:8240"]
Would you be open to a sync every two weeks
[/quote]

I'm more than happy to sync up regularly to share learning. Bi-weekly might be a little frequent, given the pace we're moving at currently. But that could change quickly if/when this grant is approved.

-------------------------

kyle | 2021-08-31 21:10:11 UTC | #27

Sounds good - I would love to learn more about the [nesting matching pools](https://forum.clr.fund/t/future-proposal-nested-matching-pools/29) ideas for example :slight_smile:

-------------------------

samajammin | 2021-09-01 15:53:59 UTC | #28

Hey folks - just giving my 2 gwei that I'll be supporting this proposal.

Over the past ~6 months I've been leading a team part-time that is building on the work of the clr.fund with the end goal of running a funding round for Eth2 public goods. You can find our work on GitHub at ethereum/clrfund, which we plan to merge back into the clr.fund monorepo to benefit all future clr.fund instances. We've been working closely with @auryn & the clr.fund team throughout. I've been impressed with the quality of their team members & their passion for their mission. I'm confident they'll make great use of these funds to continue to push this space forward.

-------------------------

anneconnelly | 2021-09-02 22:59:43 UTC | #30

I want to voice some concerns about the proposal. I like CLR and would like to see them funded. However $40K is a lot of money to be giving away without any type of concrete budget for past/future expenses and deliverables. I would like to set a standard for the content of proposals so as stewards, we can be better informed in making decisions about who and what to fund. I don't think this proposal meets that standard and so I wil be voting no. If the proposers can put together a more detailed breakdown of why the request is for $40K in particular, I would be happy to support.

-------------------------

auryn | 2021-09-03 12:26:00 UTC | #31

Hey everyone, this is a little off topic, but relevant to three thread.

Clrfund.fund is currently running a trusted setup ceremony for the latest MACI circuits. These could be reused by any project wanting to use those same circuits.

If you have a few spare CPU cycles, please consider contributing some entropy.

https://ceremony.clr.fund

(there is a manual option in the hamburger menu in the top left if you don't want to give the GitHub app permissions to write to your gists)

-------------------------

auryn | 2021-09-03 12:28:18 UTC | #32

What level of detail are you looking for?

I added some extra details in the comments [here](https://gov.gitcoin.co/t/proposal-issue-clr-fund-a-40k-gtc-grant/8240/17?u=auryn) and [here] (https://gov.gitcoin.co/t/proposal-issue-clr-fund-a-40k-gtc-grant/8240/10?u=auryn).

-------------------------

anneconnelly | 2021-09-03 15:04:02 UTC | #33

Hi Auryn. Firstly, I want to reiterate that my expectations here are for ALL proposals to gitcoin, not just yours. It's about setting standards for the future. 

The information you have provided in a few different comments is helpful, however, I don't think anyone should have to go digging through the comments to get the details of what money is going to be spent on. I would like to see this information up front in the original proposal. 

I would also expect it to be presented in a way that makes a clear link from the funding to the inputs to the outcomes. So your goal is to produce XYZ product, that will take XY hours of time from XYZ type of staff @ $XY rate + $$ other costs, therefor out financial needs are $$$. As opposed to, $40K sounds good, here's roughly what we can do with it.

-------------------------

auryn | 2021-09-29 16:35:25 UTC | #34

Heads up everyone, the Tally proposal to ratify the Snapshot proposal that passed a few weeks back will be live very soon.

If you need to move tokens or update your delegations before the vote, now is your chance.

https://www.withtally.com/governance/gitcoin/proposal/6

-------------------------
