---
id: 18296
title: "GG20 Proposal: OpenCivics Consortium Round"
slug: gg20-proposal-opencivics-consortium-round
category: governancevision
url: https://gov.gitcoin.co/t/gg20-proposal-opencivics-consortium-round/18296
created_at: 2024-03-12T03:56:39.332Z
last_posted_at: 2024-03-26T14:10:54.260Z
posts_count: 14
views: 3751
like_count: 22
---

# GG20 Proposal: OpenCivics Consortium Round

<https://gov.gitcoin.co/t/gg20-proposal-opencivics-consortium-round/18296>
Clinamenic | 2024-03-14 00:36:03 UTC | #1

**Name (or Topic/Theme) of Proposed Round**

OpenCivics Consortium Round

**How many times has this round been run during a Gitcoin Grants round?**

This will be our second round, GG19 having been our first. [See the report card of our previous round here](https://reportcards.gitcoin.co/424/0xe60a569ec8aac2045d9fda306dc2a16cc1e52a90).

**How big is your team that will run this round? Who is your team?**

We will have four round operators: Patricia Parkinson, Benjamin Life, Renee Davis, and Spencer Saar Cavanaugh (Clinamenic). Clinamenic LLC will handle the deployment of the contract and the calling of the functions, in lieu of an established OpenCivics entity to assume liability.

Patricia Parkinson - https://twitter.com/polyparkinson
Benjamin Life - https://twitter.com/omniharmonic
Renee Davis - https://twitter.com/reneedaos
Spencer Saar Cavanaugh - https://twitter.com/clinamenic

OpenCivics: [Twitter](https://twitter.com/OpenCivics) | [Website](https://opencivics.co/) 
OpenCivics Mainnet Multisig: 0x04f45dB8b906838787405d8B47336153b95F95F1

**How does this round align with Gitcoin’s mission?**

This round will utilize quadratic funding as a means of channeling the wisdom of the crowd in determining grant funding for impact projects in the broad field of civic impact and technology. This grant round will be the second in a series of grant rounds, over the course of which a dialogue will be maintained between grantor (OpenCivics) and grantee (the consortium members). 

Additionally, we plan on implementing certain attestation (EAS) and certification (Hypercerts) mechanisms to better track and recognize impact onchain, in the interest of transparency and accountability.

**What do you anticipate the size of the matching pool will be (either fundraised from partners, raised independently through your connections, or a combination of both)?**

The matching pool will be at least 5 ETH (approx. $20k at the time of writing), in addition to any funds from matching donors or sponsors we manage to secure.

**Who will be advisors for this round, if anyone?**

While the round will be managed by the four individuals mentioned above, there will not be any formal advisors for this round. 

**Please describe the eligibility criteria you envision for this proposed round.**

We plan on reusing, and perhaps slightly revising, the eligibility criteria of our previous round:

- Requirement 1: Projects are creating impact through public goods, civic service, civic works, civic innovations or civic utilities.
- Requirement 2: Projects exhibit clear relevance to the broad framing of civic innovation.
- Requirement 3: At least one project steward is a member of OpenCivics consortium (Application link: https://go.opencivics.co/application )
- Requirement 4: Project team size and skills correlates to use of funds and desired impact.
- Requirement 5: Project demonstrates a clear track record of previous work.

**How large is your community approximately?**

Several dozen members, not all of whom are associated with projects applying for or included in this grants program.

**What type of projects would you like to fund?**

We aim to fund projects driving civic innovation, and projects making civic impact. Civic innovations can be infrastructure, technology, social processes, educational curricula, or initiatives available to all members of a society. 

For more information about how we define civic innovation, [please see this document](https://opencivics.notion.site/What-is-Civic-Innovation-0a75860d643f4ffda5484449d553520d).

**Approximately how many grantees do you believe will be eligible to apply to this round?**

We aim to include 5 grantees in this round. Given the size of the matching pool, we would rather a smaller number of grantees receive substantial grants, than a larger number of grantees receive insubstantial grants. We are also generally targeting earlier stage impact projects, for whom these relatively low levels of funding can make more of a difference.

**Impact Assessment: If and how do you intend to assess grantee impact over successive rounds? This could include, but is not limited to Hypercerts, GAP, Deresy, etc.**

We intend to ask grantees, in their application for this round, to articulate their goals regarding the impact or results of the funding they receive in this round, and we intend to periodically check in on this progress, and ultimately conduct an evaluation before the following round starts. 

We also plan on issuing tailor-made Hypercerts for grantees that meet their impact goals, and we hope these certifications will demonstrate a track record of impact for the grantee, better enabling them to apply for future funding. 

We also intend to implement a Request for Attestation (RFA) mechanism, whereby the general public is invited to make attestations to the impact and activities of the grantees, which we hope will function as a grassroots form of impact evaluation to complement the centralized evaluation OpenCivics will conduct via Hypercerts.

**Is there anything else that community members should consider when voting for which rounds to focus on in the upcoming GG20 grants round?**

Even if this OpenCivics Consortium Round is not accepted into the Gitcoin Community Round and is not given matching funds, we will still be actively working alongside other grant round managers and impact evaluators in this space. We also hope that any effective practices we develop over the course of this and future rounds may prove useful to other grant round managers.

-------------------------

Clinamenic | 2024-03-12 04:17:59 UTC | #2

Curious if folks here have any ideas about the best way to go about setting/evaulating impact milestones onchain (or in some other public/transparent P2P manner).

I'm told that the submission info (at least, the info we set as public) is available onchain with Grants Indexer ([someone replied](https://warpcast.com/rohitmalekar.eth/0x87efe296) to my question on farcaster), and that it can all be accessed via some querying approach, but thats presently a bit beyond my understanding. 

Either that, or we just ask grantees to fill out an EAS schema where they state their impact milestone(s), and then OpenCivics then checks in at a later time and confirms if said impact is made by a certain date (perhaps just some point before our next round, which is TBD). Then, if the impact goal is met, OpenCivics can issue a hypercert tailored to that impact, and list the contributors to that project. 

Thats the basic idea, and we plan on keeping it relatively simple within those bounds, but I'm not sure if there is a way to cut out that first bit, namely the step where the grantee fills out an EAS schema regarding their intended impact. Ideally, that can take the form of the actual grants stack submission, and then OpenCivics can deploy an attestation confirming said impact, followed by the hypercert. 

Just thinking out loud, curious if this makes any sense to anyone haha

-------------------------

Clinamenic | 2024-03-12 04:22:18 UTC | #3

So my question is this: if we include a question in the grantee application form for this round (after deploying a new program + round contract, on the chain we choose), how do we access the onchain record of that application info? 

Is there a way we can have an EAS schema point to this onchain info? So OpenCivics can create an "impact evaluation" schema, make attestations with that schema, and point them at their corresponding grantee application info?

If so, we can also have our Request for Attestation system work similarly, where we create an "Impact Attestation" schema which anyone can fill out and point to the grantee application info of their choice.

-------------------------

mortech | 2024-03-12 11:23:02 UTC | #4

You can check out Grantee Accountability Protocol here great tooling for reporting and visibility https://gap.karmahq.xyz/

-------------------------

FractalVisions | 2024-03-12 12:52:16 UTC | #5

We second this. Our ecosystem has already setup Karma in participation for our rounds grantees to report their grant accountability via the GAP. It’s an amazing tool utilizing the EAS to record data.

-------------------------

MathildaDV | 2024-03-13 19:34:29 UTC | #6

Hi @Clinamenic do you mind adding the following to your proposal? (This is something that the council brought up purely to make it easier for them to identity team members & orgs across proposals as they're not familiar with everyone). 

- Link out to the social handles of all operators
- link out to the org's social handle
- funding address 

I'll be asking this of all applicants and I'll be amending the template too! Sorry if it's caused any inconvenience!

-------------------------

Clinamenic | 2024-03-14 00:36:57 UTC | #7

Of course - just added this info to the initial post! Makes total sense to give this info about the team.

-------------------------

Clinamenic | 2024-03-14 00:40:06 UTC | #8

Depending on which chain we deploy on (likely Arbitrum, but maybe Optimism), OpenCivics would need to deploy another multisig. 

Last time, because we ran the round on PGN and PGN didn't have multisigs, we ran the round with our four EOAs as round managers. This time, we may spin up a special purpose multisig for running this round, and if we do we'll make that known. 

How does all that sound? Anything else we should keep in mind, in terms of compliance with Gitcoin's policy for community rounds?

-------------------------

MathildaDV | 2024-03-17 19:36:32 UTC | #9

All that sounds fine to me. As long as you're able to show the Gitcoin team proof of funds ahead of the round!

-------------------------

Clinamenic | 2024-03-17 19:53:00 UTC | #10

Totally, right now the funds are sitting in this account on mainnet, which was made just to facilitate deposits into grant contracts:

https://etherscan.io/address/0xB72b259e54518a044908c71F3647a61185F04e4e

-------------------------

MathildaDV | 2024-03-18 02:08:00 UTC | #11

Thank you once again for your proposal! Please note that the council will review and vote the week of March 18 - 22. Voting won't take place in a public setting (to avoid any collusion). 

Results will be posted on the gov forum March 25th. Please be available the whole of next week to answer any questions on this post that the council may have!

-------------------------

Clinamenic | 2024-03-26 04:37:26 UTC | #12

For anyone interested, I just finished drafting this article about the methodlogy we intend to use for this grant round, incorporating Grants Stack, EAS, Grantee Accountability Protocol, and Hypercerts. 

Feedback welcome!

https://solosalon.clinamenic.com/preview/WyH0oeMtV61YXB3VnLkS

-------------------------

wasabi | 2024-03-26 12:53:23 UTC | #13

As a fan of milestones tracking and reporting; I'm stoked to see this framework in action, the wealth of data produced by this framework will be very valuable.

-------------------------

Clinamenic | 2024-03-26 14:10:54 UTC | #14

Haha I'm so excited by this idea of an onchain social/semantic graph, especially as its pertains to philanthropy.

-------------------------
