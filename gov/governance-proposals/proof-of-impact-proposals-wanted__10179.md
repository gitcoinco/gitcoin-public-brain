---
id: 10179
title: "Proof Of Impact 🌱 [Proposals Wanted]"
slug: proof-of-impact-proposals-wanted
category: governance-proposals
url: https://gov.gitcoin.co/t/proof-of-impact-proposals-wanted/10179
created_at: 2022-03-23T02:37:06.026Z
last_posted_at: 2022-07-13T16:36:15.423Z
posts_count: 11
views: 5920
like_count: 40
---

# Proof Of Impact 🌱 [Proposals Wanted]

<https://gov.gitcoin.co/t/proof-of-impact-proposals-wanted/10179>
owocki | 2022-03-23 14:37:12 UTC | #1

ImpactDAOs any DAO that has a positive impact on the world

Following the success of https://gov.gitcoin.co/t/impactdao-cartographers-wanted/9866 , we now have a telegram group with 130 people [[link]](https://t.me/+ORZ8joj8_AhjM2I5) who are working together to discover the space of ImpactDAOS.

I've also started working with @Aleborda21, who has done a wonderful job putting together a [resource library on the subject with information on 100s of DAOs](https://gitcoin.notion.site/ImpactDAO-Cartographers-Map-Room-18c0126b82af40ccb46405427ffb834d).  We plan to release a small book in PDF/softcover at DevConnect on 4/21.  It would catalogue over 100 ImpactDAOs, and here is what it would look like:

![Cover|690x422](upload://8WviWf2q2bL4v1RED7cY3Q1eZFz.jpeg)

# Extending this momentum

I would like to challenge the community to extend this momentum.  I would like to see a ImpactDAO RatingsDAO emerge.

The RatingsDAO would maintain an important money lego: **a Proof of Impact**.  Such a DAO would maintain an on-chain registry of which ImpactDAOs have what Impact.  Such a money lego could be used to facilitate trustless smart contract functionality only available to ImpactDAOs, and would also allow ImpactDAOs to display an independently verified "Proof Of Impact".

This RatingsDAO could solicit & ingest attestations about a DAO's social impact, independently verify their impact, and then issue a report card on them.    [(here is a write up I did a few weeks ago about what such an attestation framework could look like)](https://gov.gitcoin.co/t/quadratic-funding-x-effective-altruism/10016/7)

The Report cards would perhaps be available via smart contract and then also via a beautiful web interface.

Here are two mocks of what an ImpactDAO rating card could look like (all numbers made up, for demonstration purposes only):

![Screen Shot 2022-03-22 at 8.18.29 PM|690x298, 75%](upload://rutXoACa03GCUVqy1htGVFPChWJ.png)
![Screen Shot 2022-03-22 at 8.18.24 PM|690x267, 75%](upload://4R2D7w6jOwPseOFX6cSjmyeNiAU.png)


I think that the above ratings primitive could be deeply valuable to the space if
1. it has a deep liqudity of ratings.
2. it is backed by a highly [legitimate](https://vitalik.ca/general/2021/03/23/legitimacy.html) governance. The governance should also be uncapture-able and [hella forkable](https://twitter.com/YalorMewn/status/1419723207674777601).  ImpactDAOs should be able to/invited to participate in the conversation about their impact.
3. it'd be nice if it plugged into other money legos, like say [Gitcoin Grants 2.0](https://gov.gitcoin.co/t/quadratic-funding-x-effective-altruism/10016/7).  Allowing Gitcoin Grants to display Impact Ratings in it's UI


Such a ratings primitive could be used to create interesting new smart contract modifiers available only to DAOs with high impact scores.  Imagine if the following primitives were available in smart contracts:

`modifier onlyImpactDAORatingAbove(uint 256 above_score)`
`modifier onlyImpactDAOSocialRatingAbove(uint 256 above_score)`
`modifier onlyImpactDAOMaterialRatingAbove(uint 256 above_score)`

Is anyone working on something like this or interested in starting to? If so, I would like to talk to you. Please (1) [join this telegram](https://t.me/+ORZ8joj8_AhjM2I5) (2) post a proposal below in 500 words or less that articulates how you would attack this problem and what would have to be true for it to happen (hint: please ask for funding, I want to fund good proposals!).

I have budget to fund as many promising proposals as I receive, and will decide how to spend that budget on a case by case basis.

-------------------------

owocki | 2022-03-23 02:46:12 UTC | #2

Free name idea for a Ratings DAO:  Effective DAOtrusim :P

-------------------------

Jahed | 2022-03-23 12:47:44 UTC | #3

Awesome initiative, and reminds me of some of the stuff we talked about on the pod. Would be interesting to get the PopcornDAO folks involved with this (Anna-marie Swan, Mike Kisselgof, Anthony Martin), as well as Evan Miyazono from Protocol Labs

-------------------------

joanna | 2022-03-23 13:15:18 UTC | #4

this is awesome, you are amazing @owocki 
eager to build the new world together <3

-------------------------

thelostone-mc | 2022-03-23 14:11:49 UTC | #5

[quote="owocki, post:1, topic:10179"]
Such a ratings primitive could be used to create interesting new smart contract modifiers available only to DAOs with high impact scores. Imagine if the following primitives were available in smart contracts:

`modifier onlyImpactDAORatingAbove(uint 256 above_score)`
`modifier onlyImpactDAOSocialRatingAbove(uint 256 above_score)`
`modifier onlyImpactDAOMaterialRatingAbove(uint 256 above_score)`
[/quote]

@nategosselin Yo so this is something interesting. Might be worth keeping it at the back of our head during the grant round manager. Think about it.
If above product existed -> how neat would it be to use allow the grant round to rely on this to fetch grants from the registry.

While this goes takes a tangent to the vision of Grants2.0 where we expect the grant to apply for the grant round. Having something like this down the line -> would be a nice feature

Imagine collections but an actually legit / vetted collection

-------------------------

nya-elimuai | 2022-03-24 01:26:24 UTC | #6

This might also relate to what the _ixo Foundation_ is doing: https://www.ixo.world

-------------------------

bestape | 2022-03-24 02:14:07 UTC | #7

We'll need this to determine priority at our International Legal Clinic: https://gitcoin.co/grants/4811/lexdao-providing-legal-aid-to-impactdaos-funded-by . 

Thank you for initiating the resource.

Also other graders, like ixo Foundation?

-------------------------

zhiganov | 2022-04-29 01:21:20 UTC | #8

Hi guys!

**Protein** is looking to build a web3 version of BCorp/MSCI to make it easier for ImpactDAOs to access funding, investment and other novel mechanisms to boost their impact. There is a need for impact investors and philanthropists to be able to synthesize due diligence, using the tools of web3 to escape the siloed and proprietary approach of legacy ESG initiatives.

A token curated registry (TCR) of ImpactDAOs with their validated impact / traction scores would create a key ingredient in a composable ecosystem to improve the collective impact of the web3 world.

Such registry is basically a curated list of impact DAOs, which enables discovery of impactDAOs for potential contributors, investors, funders. Each ImpactDAO receives an on-chain score from a validator, allowing for investment vehicles and other token mechanics / governance to be built on top. For example a tracker fund could invest in the 10 highest impact across all projects, or the 10 highest impact in solving the food crisis, or buy a crypto ETF based on the tokens of top DAOs across specific areas of impact (for retail investors). Alternatively, an active donor fund could use this list to adjust its recurring / streaming donation. Conversely, a certain score could be used for gating access to the list, e.g. on the Regen Stack for web3 orgs that want to address their impacts but are outside of their expertise: highly rated forestry might be recommended for offsetting, highly rated design for reuse featured for laptops equipment, etc.

The impact rating can be kept honest due to 1) crypto economic incentives for evaluation / challenging scores and adding / removing DAOs from the registry, 2) robust governance system that would ensure legitimacy of the process.

**This grant would allow us to reach the goals of Stage 1:**

* Develop the scoring mechanism v1 - impact values that validators would be attesting to. These could range from internal policies and processes through to verifiable impacts.
* Design the incentive structure v1 required to ensure all eligible ImpactDAOs are scored and that their scores are an accurate reflection (this would include arbitration mechanisms).
* Validate the demand from potential investors (consumers of the curated list)

**What we need**

* 35,000 USDC
* Support from RatingsDAO / access to talent from ICC/Gitcoin network (e.g. for game theory and token engineering)

**Once Stage 1 is completed, we’ll look for additional support to:**

* Prototype the investable TCR
* Build frontend for ease of navigation
* Train validators / evaluation agents to use our scoring mechanism
* Kickstart the ecosystem for decentralized validation of ImpactDAOs, incl. supplying it with the necessary liquidity

**Who we are**

Protein Community is a community DAO, building out the Good Growth standard and cultural / regenerative accelerator. We've just released our pilot cohort, supporting and funding projects that ‘bring under-represented communities into the new economy’. We are currently evaluating our approach before our next “recelerator” which focuses on supporting projects and their regen stack.

You can learn more about us on Twitter @protein

-------------------------

deeparocks | 2022-05-05 21:56:09 UTC | #9

Proof of Impact is easy to verify for digital goods but it gets messy for on ground projects. No matter how many videos and stories the project creator supplies it needs to be attested and verified by an independent person. You got to make that field trip and talk to the beneficiaries to assess the real impact. Oracles could potentially be a solution to prove impact in a decentralized way

-------------------------

OrBlob | 2022-05-13 08:08:24 UTC | #10

Hi folks,

My name is Or (@realblob), I work in impact management and measurement. I lead a community of SDG stakeholders and professionals and I work with startups to help them align their KPIs with impact KPIs, indicators, and frameworks. Our proposal is to align impact metrics and values with monetary values and streamline their incorporation into transactions through an "Impact Oracle". 

**Why?**
Over the years we’ve noticed that much of impact accounting is a mess of acronyms that create a race to the bottom. Companies do the minimum in order to be up to par with regulation/certificates. This is because we fundamentally do not have metrics that value impact in monetary terms (outside of marketing).

Essentially, ESG, SDGs, IMP, GRI, SASB, and other acronyms and methodologies are “patches” to an economic system that does not value environmental and social impact. Our economic system “speaks in money” and we respond with qualitative impact analysis. We “patch” our economy with certifications, verifications, and different tags or stickers that symbolize that the goods or services are aligned with our values, but this does not change the context of the system. 

**What?**
Impact Oracle (IO) is a price oracle for impact that draws on market values and stakeholder consensus. Instead of creating a rigid top-down accounting for impact, we decentralize the process and allow the price of impact to reflect its actual value in monetary terms.

IO maintains a registry of the value of impact, as a flexible, ad-hoc, community-sourced metric. Constantly evolving, living, and changing with the needs and values of the ecosystem. Just as prices of commodities and assets change with market demands, so must impact. Using this pricing, IO compensates for positive impact and offsets negative impact.

By creating a price for every type of impact we create a new metric for businesses to measure against. By making this metric monetary, we create a new potential revenue stream and incentivize a race to the top: More impact = more profit. 

This creates transparency, impact, alignment, and transformation of the economic incentives in our economy like never before. IO creates a system in which verification of impact is an all-in-one process. Any organization, DAO or otherwise, can streamline their impact accounting, getting compensation for positive impact and offsetting their negative. 

**How?**
By connecting to legacy systems such as the company’s logistics, supply, ERM software, etc. we can correlate their actual activities with their real impact. We don’t need to track each DAO or company individually as we can connect with MRV systems, tokenization frameworks, and existing data. 

More on the “How” in our lite paper which I'd be happy to share.

What we’re looking for:
We are currently building the tokenomics and governance system and building partnerships with relevant stakeholders to supply capital and professional resources. This should be a cross-chain endeavor and we would like for it to be built for Ethereum as well as other blockchains. 

Any of the following would be of massive help:
-	35K USDC for an MVP of the Oracle
-	Professional and tech support from the ICC community
-	Community-building support for the IO DAO through Gitcoin and others

(This proposal is similar to a proposal in the the "Impact Certificate" thread - if one is accepted, we will rescind the other)

-------------------------

owocki | 2022-07-13 16:36:15 UTC | #11

hey all, thanks again for the discussion + for the proposals. 

we posted about the next step for this initiative here => https://gov.gitcoin.co/t/impact-certificates-proposals-wanted/10499/29

-------------------------
