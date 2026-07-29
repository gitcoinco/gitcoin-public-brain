---
id: 17243
title: "[Proposal] Testing a GCP Format with SeaGrants"
slug: proposal-testing-a-gcp-format-with-seagrants
category: open-discussion
url: https://gov.gitcoin.co/t/proposal-testing-a-gcp-format-with-seagrants/17243
created_at: 2023-12-08T18:45:27.867Z
last_posted_at: 2023-12-18T15:37:18.272Z
posts_count: 5
views: 3655
like_count: 15
---

# [Proposal] Testing a GCP Format with SeaGrants

<https://gov.gitcoin.co/t/proposal-testing-a-gcp-format-with-seagrants/17243>
nategosselin | 2023-12-08 18:45:28 UTC | #1

# Summary

We propose dogfooding the new SeaGrants app to administer a January GCP budget on Allo v2. The total budget would be $25k, with individual applications eligible to receive a maximum of $5k. Applications would be funded as long as at least 3 Gitcoin stewards approve it.

# Abstract

This proposal aims to utilize the newly developed front-end, SeaGrants, to facilitate the distribution of $25,000 in Gitcoin Community Proposal (GCP) funding. SeaGrants was inspired by the original desires behind the Gitcoin Community Proposal process, which aimed to make it easier for community members to make tangible contributions to the Gitcoin ecosystem. By implementing this proposal, we intend to streamline and democratize the allocation of these funds, empowering community members to play a more active role in supporting and growing the Gitcoin ecosystem. In addition to streamlining the grant distribution process, this initiative will also serve as a valuable opportunity to test out a new GCP format, setting the stage for an upcoming evolution of our community engagement channels that [CoachJ](mailto:jonathan@gitcoin.co) is currently developing. Furthermore, it’s a valuable opportunity to showcase the capabilities of Allo v2.

# Motivation

The motivation behind this proposal is rooted in addressing three core objectives:

1. Empowerment of Community Members: We aim to support the vision of the GCP process by simplifying the application and distribution of grants. This will empower community members to take an active role in shaping the future of Gitcoin.
2. Accelerated Growth: By making it easier for community members to access GCP funding, we expect to see an increase in the number of tangible contributions to the Gitcoin ecosystem. This will lead to accelerated growth, innovation, and community engagement.
3. Showcasing Allo v2: This proposal provides an excellent opportunity to highlight the capabilities of Allo v2, as it demonstrates both the ease of creating new mechanism variations and what’s possible for developers using our SDK.

# Specification

The implementation plan for this proposal includes the following:

* Funding Pool: A total of $25,000 will be deposited into an Allo v2 pool, which will be prominently visible on the SeaGrants app, ensuring transparency and accessibility to all community members.
  * Maximum Grant Amount: Grant applications can request a maximum of $5,000 each, ensuring a fair allocation of resources.
* Voter Eligibility: Stewards who have at least 100,000 tokens delegated to them will be eligible to vote on grant applications. Eligible stewards will have one vote per application.
* Distribution Period: The $25,000 will be available for distribution in the month of January 2024, with the following windows:
  * Application Period: Applications will be accepted from January 8th to January 12th, providing a five-day window for community members to submit their proposals.
  * Review and Comment Period: From January 15th to January 19th, grant applications will be in a review and comment period, allowing community members to provide feedback and assess the proposals.
  * Voting Period: Voting by eligible stewards will take place from January 22nd to January 26th.
* Evaluation Criteria:
  * Applications should be focused on advancing one of our three Essential Intents:
    * 1) Network Effects — Maximizing the network effects of our ecosystem to grow product adoption
    * 2) Community First — Cultivating a community that thrives on providing positive change and meaningful engagement
    * 3) Financial Longevity — Ensuring the economic health and vitality of Gitcoin
  * Applications will be evaluated based upon their ability to drive meaningful impact against any one of those EIs.
* Approval Criteria: Applications that receive at least three "yes" votes during the voting period will be approved and receive their requested amounts.
* Funding Order: Funded applications will be processed as soon as they receive their third yes vote. If there aren't enough funds remaining in the pool to fulfill an approved application, that specific application will not receive funds.
* Unused Funds: Any leftover funds from the pool will be returned to the DAO, ensuring efficient use of resources and community funds.

# Benefits

The core benefits of implementing this proposal include:

* Democratized Grant Distribution: Making it easier for community members to access GCP funding.
* Increased Community Engagement: Encouraging more community members to contribute to the Gitcoin ecosystem.
* Dogfooding Allo v2

# Drawbacks

While the proposal offers significant benefits, there are potential drawbacks to consider:

* Increased Administrative Load: Managing a streamlined grant distribution process may require additional administrative resources.
* Quality Control: Ensuring the quality and impact of funded projects will be critical to the success of this initiative.

# Vote

Voting "Yes" on this proposal signifies support for distributing $25,000 in GCP funding through SeaGrants in January 2024, furthering the goal of empowering community members and accelerating Gitcoin's growth. Voting "No" indicates opposition to this proposal.

-------------------------

CoachJonathan | 2023-12-12 16:50:42 UTC | #2

I will be voting yes to this proposal and looking forward to seeing how this test fares on the waters of Web3 grants (see what I did there?).

-------------------------

Viriya | 2023-12-12 18:30:57 UTC | #3

Fun to see this go live! 

Who is owning and vetting the initial proposals before they go to vote? Or is this a completely decentralized process? 

I feel a bit weary about the voting threshold given the things outlined in the drawbacks section. I know we're working on communicating our roadmaps and getting the community more involved with RFPs but we're definitely not there yet. I'm also aware that most haven't seen the governance strategy that @CoachJonathan is working on so there's little understand how this interplays with that but I do know just from personal conversations with him that it could interface well with it. 

I'm down to try the experiment though. Little cost to test a gov tool that could potentially be used elsewhere :) 

Would love to know (just for my own curiosity) what problem this product solves for other potential customers. That isn't entirely clear to me and if I know I might be able to help position this for adoption at other orgs!

-------------------------

alexalombardo | 2023-12-12 19:43:55 UTC | #4

Excited to see us try/showcase new things on Allo while also solve an internal challenge which is the funding of community proposals 

This also allows us to allocate a defined amount for GCPs and overall create more structure and hopefully a replicable process 

And from a marketing POV is a nice moment for Allo to talk about something beyond Grants Stack but still align with the larger Gitcoin vision/proposition

I also like the idea of doing this at the Gitcoin org level but also as a way for workstreams to earmark funds that then can go to funding contributor led projects within the workstream, allowing for a bit of flexibility/creativity that still feels democratic and definitely see this being relevant for a lot of orgs if it can be a low lift, super simple process/tech

That said I'm curious - where do these proposals get submitted and echoing @Viriya how are they evaluated?

-------------------------

CoachJonathan | 2023-12-18 15:37:18 UTC | #5

Hi everyone, after speaking with @nategosselin about this we agreed that this post doesn't necessarily require a formal proposal since these funds have already been allocated to [Allo's budget in their S20/S21 budget request](https://gov.gitcoin.co/t/proposal-allo-s20-21-budget-request/16766).

Since no net new funds will be released, this post is more of an FYI than a proposal and folks can expect to apply and take advantage of the funding in the new year once this initiative kicks off.

-------------------------
