---
id: 17347
title: "[Proposal] Gitcoin killer app"
slug: proposal-gitcoin-killer-app
category: open-discussion
url: https://gov.gitcoin.co/t/proposal-gitcoin-killer-app/17347
created_at: 2023-12-28T04:08:47.357Z
last_posted_at: 2023-12-28T20:59:39.315Z
posts_count: 5
views: 4074
like_count: 10
---

# [Proposal] Gitcoin killer app

<https://gov.gitcoin.co/t/proposal-gitcoin-killer-app/17347>
vporton | 2023-12-28 04:16:04 UTC | #1

# Gitcoin Grant Application

- **Project Name:** Salaries Science
- **Team Name:** World Science DAO
- **Payment Address:** 0x36A0356d43EE4168ED24EFA1CAe3198708667ac0

I propose to allocate funds for development of "Gitcoin killer" app.

## Project Overview :page_facing_up:

### Overview

Gitcoin killer: Gitcoin-like project for both science and software. Special features to support basic science and software components to be priority-financed.

I propose a grants system similar to Gitcoin, but with the following features:
- allocating a part of donation to dependencies
- mandatory affiliate program, to ensure that no scientific discovery goes unmarketed (it is especially important, because a scientific project can be published, so preventing publication or re-discoveries, but go unmarketed, this way blocking development of science)
- rewarding first-comer affiliates, in order not only to start small but encompass broad adoption

The project is planned to be implemented on DFINITY Internet Computer, thanks to its super-low gas fees. Dependencies for software (like `crates.io`) and for science (Semantic Scholar) are projected to be managed by third-party servers in a decentralized way.

This project is unrelated to other projects of Radicle, but its purpose is somehow similar to Drip project. However, my project is focused on a different purpose than only rewarding contributions, but intends to save science for mis-publication catastrophe.

Case study: Ordered semicategory actions (OSA) were discovered by me in 2019. Upon reading my work it becomes obvious that most of future science should build upon this discovery. But publication of OSA wasn't successful and I after a sequence of steps came to the situation that I cannot publish my discovery neither in full (500 pages), nor by parts. So, the entire science development is stalled, until OSA will be published. I see no way to publish OSA through traditional publishers, so we need this project to support scientific marketing: I shown that even one scientific discovery without funds for publication may severely block the entire science. Apparently, other similar cases may exists, so we see that science is in deep crisis.

The radical solution of this problem is to replace the entire system of peer review by quadratic funding.

So, this project is intended for:
- provide good "salaries" to scientists and free software authors (especially for software components and basic science, through allocation of a part of donations to dependencies)
- unstuck science by paid scientific marketing instead of traditional peer review

Importance to unstuck science from mis-publications happened in the centralized world is immense. Even one mis-published scientific project (such as OSA) may push down the entire science and therefore world economy. It is also important to establish an effective way to reward unknown to the world software components authors.

## Team :busts_in_silhouette:

### Team members

- Victor Porton

### Contact

- **Contact Name:** Victor Porton
- **Contact Email:** porton.victor@gmail.com
- **Website:** https://science-dao.org/salaries-science/

### Team's experience

I have an extensive experience with DFINITY Internet Computer programming: I created the MVP (and advanced the work further) of Zon, an elaborate social network on the same platform DFINITY Internet Computer: https://docs.zoncirlce.com

I also have extensive exprience with TypeScript, the language that I am going to use.

I also created XML Boiler: https://github.com/vporton/xml-boiler - the most advanced software for XML processing.

I developed math related to OSA (more than 500 pages).

### Team Code Repos

- https://github.com/vporton
- https://github.com/vporton/zondirectory2
- https://github.com/vporton/xml-boiler

### Team LinkedIn Profiles

- https://www.linkedin.com/in/victor-porton/

## Project Description :page_facing_up:

[The detailed description of the algorithm.](https://github.com/vporton/salaries-science/blob/main/financing-science-algorithm.odt?raw=true)

I am applying for this grant, because I want to save science from mis-publication (including but not limited to proper marketing of OSA).

## Deliverables :nut_and_bolt:

- **Total Estimated Duration:** 410 days
- **Full-time equivalent (FTE):** 242
- **Total Costs:** 47000 USD

### Milestone 1

- **Estimated Duration:** 30 days
- **FTE:** 15
- **Costs:** 3000 USD

| Number | Deliverable              | Specification                                                                           |
| ------ | ------------------------ | --------------------------------------------------------------------------------------- |
| 1.     | Onchain data structure   | Data structures and associated APIs for all on-chain storage described in the algorithm |

### Milestone 2

- **Estimated Duration:** 10
- **FTE:** 7
- **Costs:** 3000 USD

| Number | Deliverable              | Specification                                                                       |
| ------ | ------------------------ | ----------------------------------------------------------------------------------- |
| 1.     | Storing GitHub JSON      | API for reading the JSON file (see the article) from GitHub and storing it on-chain |

### Milestone 3

- **Estimated Duration:** 60
- **FTE:** 40
- **Costs:** 6000 USD

| Number | Deliverable                   | Specification                                                                       |
| ------ | ----------------------------- | ----------------------------------------------------------------------------------- |
| 1.     | general dependencies API      | public API for storing on-chain dependencies                                        |

### Milestone 4

- **Estimated Duration:** 20
- **FTE:** 10
- **Costs:** 2000 USD

| Number | Deliverable                   | Specification                                                                       |
| ------ | ----------------------------- | ----------------------------------------------------------------------------------- |
| 1.     | Gitcoin passport              | Querying and storing Gitcoin passport scores for an address                         |

### Milestone 5

- **Estimated Duration:** 20
- **FTE:** 10
- **Costs:** 3000 USD

| Number | Deliverable                   | Specification                                                |
| ------ | ----------------------------- | ------------------------------------------------------------ |
| 1.     | Creating rounds backend       | Backend for creating matching rounds                         |
| 2.     | Creating rounds frontend      | Frontend for creating matching rounds                         |

### Milestone 6

- **Estimated Duration:** 20
- **FTE:** 10
- **Costs:** 3000 USD

| Number | Deliverable                   | Specification                                                                       |
| ------ | ----------------------------- | ----------------------------------------------------------------------------------- |
| 1.     | Pledging matchers             | Accept matchers pledging matching funds                                             |
| 2.     | Pledging servers              | Accept servers pledging gas tokens                                                  |

### Milestone 7

- **Estimated Duration:** 90
- **FTE:** 60
- **Costs:** 6000 USD

| Number | Deliverable                   | Specification                                                                       |
| ------ | ----------------------------- | ----------------------------------------------------------------------------------- |
| 1.     | Accept donations backend      | Accepting funds from a donor, writing basic donation info, also writing affiliate   |
| 2.     | Accept donations frontend     | Accepting funds from a donor, support for affiliates                                |
| 3.     | Write dependencies            | Query dependencies, store them in the DB                                            |

### Milestone 8

- **Estimated Duration:** 20
- **FTE:** 10
- **Costs:** 3000 USD

| Number | Deliverable                   | Specification                                                                       |
| ------ | ----------------------------- | ----------------------------------------------------------------------------------- |
| 1.     | Matching calculation          | Calculate the entire amounts paid to each user                                      |

### Milestone 9

- **Estimated Duration:** 30
- **FTE:** 15
- **Costs:** 3000 USD

| Number | Deliverable                   | Specification                                                                       |
| ------ | ----------------------------- | ----------------------------------------------------------------------------------- |
| 1.     | Consensus                     | Removal of erring servers by votes of other servers                                 |

### Milestone 10

- **Estimated Duration:** 20
- **FTE:** 10
- **Costs:** 3000 USD

| Number | Deliverable                   | Specification                                                                       |
| ------ | ----------------------------- | ----------------------------------------------------------------------------------- |
| 1.     | Voting for user accounts      | Voting for each user account (or no account)                                        |

### Milestone 11

- **Estimated Duration:** 20
- **FTE:** 10
- **Costs:** 3000 USD

| Number | Deliverable                   | Specification                                                                       |
| ------ | ----------------------------- | ----------------------------------------------------------------------------------- |
| 1.     | Voting for passport scores    | Voting for user's Gitcoin passport scores                                           |

### Milestone 12

- **Estimated Duration:** 20
- **FTE:** 15
- **Costs:** 3000 USD

| Number | Deliverable                   | Specification                                                                       |
| ------ | ----------------------------- | ----------------------------------------------------------------------------------- |
| 1.     | Rewarding servers             | Calculate and pay to server accounts                                                |

### Milestone 13

- **Estimated Duration:** 50
- **FTE:** 30
- **Costs:** 6000 USD

| Number | Deliverable                     | Specification                                    |
| ------ | ------------------------------- | ------------------------------------------------ |
| 1.     | Server reference implementation | Calculate and pay to server accounts             |
|        |                                 | - Semantic Scholar dependencies                  |
|        |                                 | - `crates.io`` dependencies                      |

## Future Plans

In the short term (after the release), I am going to press-release my project and gain some supporters.

In the long term, I am going to displace Gitcoin and Drip replacing them by my project.

The project will be sustainable because it will gather money, among other projects for itself.

We will need further grants for improving design, SEO, and other marketing.

## Additional Information :heavy_plus_sign:

Work I have already done:
- written the [algorithm](https://github.com/vporton/salaries-science/blob/main/financing-science-algorithm.odt?raw=true) (in English). I also started to write Motoko code, but it is very preliminary. (I am also going to replace Motoko by TypeScript.)
- created [NacDB](https://github.com/vporton/NacDB), a database useful for this project.

-------------------------

thedevanshmehta | 2023-12-28 13:26:34 UTC | #2

I appreciate how detailed you have made the proposal.

[quote="vporton, post:1, topic:17347"]
In the long term, I am going to displace Gitcoin and Drip replacing them by my project.
[/quote]

Overall your project seems more apt for receiving money via Gitcoin grant rounds rather than the DAO treasury, which is for helping gitcoin succeed rather than helping any particular project.

Maybe submit this project for GG20 and raise funds from there? Have you taken part in earlier gitcoin rounds?

-------------------------

vporton | 2023-12-28 15:35:20 UTC | #3

[quote="thedevanshmehta, post:2, topic:17347"]
Overall your project seems more apt for receiving money via Gitcoin grant rounds rather than the DAO treasury, which is for helping gitcoin succeed rather than helping any particular project.

Maybe submit this project for GG20 and raise funds from there? Have you taken part in earlier gitcoin rounds?
[/quote]

Yes, I want to receive funding from Gitcoin, please help.

I will submit it to GG20, of course. But I don't expect to receive enough money from GG20.

If I remember correctly, in GR18 my project was rejected due to a misunderstanding. If I remember correctly, nn GG19 there was no DeSci track.

-------------------------

vporton | 2023-12-28 15:39:47 UTC | #4

[quote="thedevanshmehta, post:2, topic:17347"]
Overall your project seems more apt for receiving money via Gitcoin grant rounds rather than the DAO treasury, which is for helping gitcoin succeed rather than helping any particular project.
[/quote]

This project may replace Gitcoin in the future. So, I want money from DAO treasury.

-------------------------

owocki | 2023-12-28 20:59:39 UTC | #5

This proposal is not in line with [Gitcoin's 2024 Essential Intents](https://gov.gitcoin.co/t/update-gitcoin-s-ratified-essential-intents-2023-2024-and-a-recap-of-our-successes/16818), and so I will be voting against this proposal if it is brought to a vote.

@vporton I suggest making a Gitcoin Grant @ https://explorer.gitcoin.co/ and trying to get funding that way.  Good luck!

-------------------------
