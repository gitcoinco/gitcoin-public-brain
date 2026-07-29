---
id: 18201
title: "Citizens Innovate GCP – Gitcoin Passport CLI"
slug: citizens-innovate-gcp-gitcoin-passport-cli
category: citizen-grants
url: https://gov.gitcoin.co/t/citizens-innovate-gcp-gitcoin-passport-cli/18201
created_at: 2024-02-29T17:06:11.033Z
last_posted_at: 2024-03-12T23:08:16.617Z
posts_count: 12
views: 4516
like_count: 11
---

# Citizens Innovate GCP – Gitcoin Passport CLI

<https://gov.gitcoin.co/t/citizens-innovate-gcp-gitcoin-passport-cli/18201>
alexdwagner | 2024-03-12 19:36:48 UTC | #1

## Building a Command Line Interface for Gitcoin Passport

*This is an updated version of my previous proposal. This revised version is based on feedback I've received from the Gitcoin community, and a very helpful conversation recently with members of the Gitcoin Passport dev team.*

*Also, the project is [now live on Grants Stack here.](https://builder.gitcoin.co/#/chains/10/registry/0x/projects/0x2232dc3a26e6ddeb679dc83868640cebb94a2e49e3015cf60c393d45eb804585)*

-----
# Passport CLI – A command-line tool for Gitcoin Passport (v0.3)

## Description

This proposal seeks funding to build a command-line interface (CLI) tool for Gitcoin Passport. The purpose of this tool is to simplify and streamline interaction with the Gitcoin Passport API for developers, and to enhance the overall developer experience for Gitcoin Passport.

The first version of the Passport CLI tool will essentially provide a wrapper for Gitcoin Passport’s [existing API functions](https://api.scorer.gitcoin.co/docs), to help devs work with Passport’s API without having to write custom applications or scripts.

More specifically, this tool will leverage Gitcoin Passport's API to allow users to fetch passport scores, fetch stamps for a given Ethereum address, claim web3 stamps, and more, all from their terminal!

#### Impacted Stakeholders and Expected Outcomes

Developers who seek to build with Gitcoin Passport will benefit from improved productivity and an enhanced development process by using Passport CLI.

Passport CLI will allow developers to access Gitcoin Passport’s API without having to write a script or custom software to fetch user Stamps, submit an address for scoring, and to fetch the Passport score for one or more addresses. The Passport CLI will also allow developers and users to claim web3 stamps via the command–pretty cool!

Additionally, the Gitcoin community will experience increased accessibility and usability of Gitcoin Passport via Passport CLI. This command-line tool will provide a more accessible experience to users who are vision-impaired, as CLI tools work better with screen readers, compared to graphics-rich web interfaces.

Expected outcomes include a boost in Gitcoin Passport's adoption and a strengthening of its network effects. Passport CLI will be the first tool built in the Gitcoin Passport ecosystem that is built expressly to serve the needs of developers.

Lastly, I have spoken to members of the Gitcoin Passport dev team and they have expressed excitement and support for this project.

#### Motivation

As a developer actively involved in the Gitcoin community, I've identified the need for easier access to Gitcoin Passport's functionalities. This tool will simplify developers' interactions with the platform, enhancing productivity and engagement. I assure there are no conflicts of interest with this proposal, and any future concerns will be transparently addressed.

#### Why the Citizen Grants Program Should Adopt the Proposal

This proposal has been created specifically with [Gitcoin's Essential Intents](https://gov.gitcoin.co/t/update-gitcoin-s-ratified-essential-intents-2023-2024-and-a-recap-of-our-successes/16818) in mind.

At a glance, the benefits of adopting this proposal and funding the development of the Gitcoin Passport CLI tool are:

* **Prioritizing the developer community** by providing tools that empower developers to contribute more effectively.

* **Contributing to financial longevity of the Gitcoin ecosystem** by supporting the development of utilities that enhance Gitcoin Passport's value.

* **Enhancing the network effects of Gitcoin’s current developer ecosystem** by streamlining the developer experience and fostering product adoption. One success metric for the project is to be responsible for onboarding 100 new developers to the Gitcoin Passport developer ecosystem over the next six months.

The Citizen Grants Program should back this initiative because it directly supports Gitcoin's goal of fostering a thriving developer ecosystem. By reducing barriers and improving accessibility, the Passport CLI tool will attract new developers and enhance the productivity of existing ones. This adoption is essential for nurturing innovation within the Gitcoin community, ensuring its growth and relevance in the blockchain sector. The proposal presents a strategic opportunity to strengthen the Gitcoin ecosystem by making it more welcoming and efficient for developers.

Furthermore, the proposal responds to a clear demand within the community for more efficient ways to interact with Gitcoin Passport, demonstrating Gitcoin's responsiveness to user needs and its dedication to innovation.

By building on the existing infrastructure of Gitcoin Passport and utilizing its public APIs, the Passport CLI tool represents a practical and strategic opportunity to enhance the Gitcoin ecosystem.

#### Challenges

* **Deploying the Passport CLI will require ongoing maintenance and updates to keep Passport CLI function and aligned with Gitcoin Passport.** In the event of any breaking changes to Gitcoin Passport’s API, Passport CLI will need to be updated accordingly. As a part of this proposal, we will co-create a maintenance plan with members of the Gitcoin Passport dev team, which will provide a written protocol in regard to keeping the Passport CLI functional and working, in the event of Passport API breaking changes.

* **Authentication and Signature Generation:** A significant technical challenge identified is handling authentication and signature generation for interacting with the Gitcoin Passport's API. One example of this is that we will need to generate signatures with a user's wallet, possibly requiring interaction with browser wallet extensions or external tools for signing.

* **Claiming Stamps:** Another challenge involves claiming stamps, especially concerning OAuth for Web2 stamps and the authentication flow that might require a browser interaction for user consent. This presents a potential hurdle for a purely CLI-based tool.

We will work closely with the Gitcoin Passport dev team via regular video calls (weekly or bi-weekly) to align with the mission of Gitcoin Passport and Gitcoin’s Essential Intents, and to implement robust solutions for these challenges.

## Specifications

This project will be built using Node and TypeScript, with the goal of closely mirroring the tech stack of Gitcoin Passport.

Additionally, we will use the [Commander.js](https://github.com/tj/commander.js/) library to implement the core command line functionality.

We will utilize environment variables for API key management, emphasizing security through the principle of least privilege. This includes running the CLI tool with user-level permissions, implementing secure API key entry to prevent exposure in command history, and ensuring files generated by the tool have restricted access.

Additionally, we plan to encrypt sensitive data at rest using Node.js's crypto library and secure data in transit with HTTPS, offering guidance on securing .env files against unauthorized access.

The Gitcoin Passport CLI Tools will be installable via npm and designed to support a wide range of functionalities through a user-friendly command-line interface.

### Proposed Feature Set

This feature set was derived based on feedback from Gitcoin Passport users and from members of the Gitcoin Passport dev team.

#### Category 1: Standard Features (Utilizing Public APIs)

**Submit a Wallet Address for Scoring**

* **Command Name:** `submit-passport`
* **Usage:** `passport-cli submit-passport --address <address> --scorer_id <scorer_id> [--signature <signature>] [--nonce <nonce>]`
* **Description:** Submits an Ethereum address to the Scorer for passport scoring. Initially returns a status of PROCESSING or DONE. For PROCESSING status, the score computation is underway and the status can be checked by querying the score with the scorer ID and address.
* **Passport API endpoint:** `POST /registry/submit-passport`

**Fetch User Stamps**

* **Command Name:** `get-stamps`
* **Usage:** `passport-cli get-stamps <address>`
* **Description:** Retrieves and displays a user's verified stamps.
* **Passport API endpoint:** `GET /registry/stamps/{address}`

**Fetch Passport Score for an Address**

* **Command Name:** `get-score`
* **Usage:** `passport-cli get-score <scorer_id> <address>`
* **Description:** Retrieves and displays the Passport score for a specific address as per a given scorer ID.
* **Passport API endpoint:** `GET /registry/score/{scorer-id}/{address}`

**Fetch Passport Scores for All Addresses**

* **Command Name:** `get-all-scores`
* **Usage:** passport-cli `get-all-scores <scorer_id> [--limit <limit>] [--offset <offset>] [--gt <timestamp>] [--gte <timestamp>] [--order <order>]`
* **Description:** Retrieves Passport scores for all addresses associated with a specific scorer. Supports pagination, and filtering scores based on timestamps, with the ability to order results.
* **Passport API endpoint:** `GET /registry/score/{scorer-id}/`

**Fetch Score History**

* **Command Name:** `get-score-history`
* **Usage:** `passport-cli get-score-history <address> [--timestamp <timestamp>]`
* **Description:** Obtains a historical view of scores based on timestamp and optional address.
* **Passport API endpoint:** `GET /registry/score/{scorer-id}/history`

**Fetch Stamp Metadata**

* **Command Name:** `get-stamp-metadata`
* **Usage:** `passport-cli get-stamp-metadata`
* **Description:** Gathers metadata for all stamps available in the Passport ecosystem.
* **Passport API endpoint:** `GET /registry/stamp-metadata`

**Retrieve GTC Stake Amounts**

* **Command Name:** `get-gtc-stake`
* **Usage:** `passport-cli get-gtc-stake <address> <round_id>`
* **Description:** Fetches GTC stake amounts related to the GTC Staking stamp.
* **Passport API endpoint:** `GET /registry/gtc-stake/{address}/{round_id}`

#### Category 2: Advanced Features

Claiming New Credentials

* **Command Name:** `claim-credentials`
* **Usage:** `passport-cli claim-credentials`
* **Description:** Streamlines the process of claiming new credentials for Passport users. (Note: This command's implementation will depend on further collaboration and access to internal APIs.)
* **Note:**
  * For the first version of Passport CLI, we will focus on claiming web3 credentials, as claiming web 2 credentials must be done via oAuth and is beyond the scope of this proposal.
  * The ability to claim web 2 credentials will be built into a later version of Passport CLI.

**Saving to Centralized Storage/Ceramic**

* **Command Name:** `save-credentials`
* **Usage:** `gitcoin-passport-cli save-credentials [--storage-type <type>]`
* **Description:** Enables saving credentials to centralized storage solutions or the Ceramic Network. (Note: Similar to claim-credentials, the feasibility of this command is subject to collaboration outcomes and API availability.)

These command names are designed to be intuitive and reflective of their respective functionalities, providing a user-friendly interface for developers to interact with the Gitcoin Passport ecosystem efficiently.

For further description of the Gitcoin Passport API, see Passport’s [API reference](https://docs.passport.gitcoin.co/building-with-passport/passport-api/api-reference) and the [API playground](https://api.scorer.gitcoin.co/v2/docs).

## Timeline and Milestones

1. **Development of Standard Features (6 weeks):** Implement, test, and refine Category 1 features.
2. **Documentation and Initial Launch (2 weeks):** Finalize documentation and officially launch the tool with Category 1 features.
3. **Advanced Features Development and Collaboration (3 weeks):** Develop Category 2 features based on collaboration outcomes with the Passport team.

### Deliverables

* **Passport CLI Tool:** A fully functional CLI tool capable of interacting with Gitcoin Passport APIs. Can be installed via NPM.
* **Comprehensive Documentation:** Detailed setup instructions, usage guides, and examples.
* **Source Code:** Well-documented and maintainable source code, hosted on GitHub.
* **Maintenance Plan:** We will work with the Gitcoin Passport dev team to create a maintenance plan for Passport CLI.

### Budget Estimate

* **Total Estimated Cost:** $9,000
  * **Research and Planning:** $1,500
  * **Development and Testing:** $5,000
  * **Documentation and Launch:** $2,500

This revised budget accommodates a more comprehensive planning phase, detailed development and testing of features, and the production of thorough documentation.

### Importance of Collaboration

Collaboration with the Gitcoin Passport development team is vital, particularly for the advanced features in Category 2.

We have a verbal promise from members of the Gitcoin Passport dev team to provide periodic guidance to this project, in the form of weekly or bi-weekly video calls to review the progress of this project.

This partnership ensures the CLI tool's alignment with Gitcoin Passport's API stability and future roadmap, laying a strong foundation for its continuous enhancement.

### Measures of Success and KPIs

* **Developer Adoption Rates:** Targeting 200 unique users to install the Gitcoin Passport CLI Tool within the first six months.

* **User Satisfaction:** Achieving an 80% satisfaction rate in post-launch surveys.

* **Contribution to Gitcoin Passport's Network Effects:** Qualitative feedback on increased engagement and adoption.

### Non-Financial Requirements

* Insight and collaboration from members of the Gitcoin Passport development team for advanced feature integration. Ideally, members of the Gitcoin Passport product team as well.

* **Community feedback and testing to refine the tool pre and post-launch.**

## Conclusion

The Gitcoin Passport CLI tool project will be the first tool built specifically for developers in the Gitcoin Passport ecosystem!

Building Passport CLI will boost the network effects within the Gitcoin ecosystem, foster dev community engagement, and contribute to Gitcoin's mission of building and funding public goods.

By initially focusing on public API functionalities and planning for advanced features, this proposal aims to deliver a valuable tool that significantly enriches the developer and user experience.

*Thanks for reading! Obviously I will be replying here in the comments, and you can also dm me via Discord or Telegram–I'm @alexdw5.*

-------------------------

alexdwagner | 2024-02-29 17:10:38 UTC | #2

Tagging @rohit @Jeremy and @lebraat for feedback :slight_smile:

-------------------------

DistributedDoge | 2024-03-01 12:53:05 UTC | #3

Looks neat. Good CLI can go a long way to improve developer experience, so I am petty much sold on that one!

So far Gitcoin is *talking* a lot about improving developer experience, but yours is first initiative I see that may actually *do* something in that direction!

>`npx passport score --from-file addresses_to_check.csv`

You may have hard time gathering feedback *here*, as I am not sure many Passport builders frequent governance forums but we will see how it goes!

Anyways, one feature suggestion would be to add `--json` option for command outputs a bit like  [aws-cli](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-output-format.html) is doing => make it easier to glue scripts together.

-------------------------

alexdwagner | 2024-03-01 19:00:37 UTC | #4

Thanks @DistributedDoge, really appreciate the feedback here. 

You make a good point about going to the devs to gather feedback :slight_smile: 



Also great suggestion to add a `--json` option to format outputs. I will add a card for that!

-------------------------

KarlaGod | 2024-03-05 07:01:26 UTC | #5

Yeah, this is good, sounds like you have development processes covered and thought out. I'm excited to see your milestones report when you start, I hope you get it.

-------------------------

nutrina | 2024-03-05 12:37:21 UTC | #6

Hello,

As a Passport developer I would like to share my take on this.

First, I like CLI tools. I use them daily, and I feel they make a developer more productive. So having a passport cli tool sounds of curse great to me, because I can already imagine how easily I can put together certain workflows.

But building a Passport CLI, is not quite easy.

Reading through the proposal, I think the commands that the cli tool would provide fall into 2 categories:

**Category 1 (easy)**

These commands which can be implemented by using our public API (https://api.scorer.gitcoin.co/docs). This includes features like retrieving a users stamps, score, etc ... It is already possible to interact with the API from a terminal using `curl` commands, and these `curl` commands are provided in the docs page.

It would be easy to wrap these for convenience in a CLI tool.

**Category 2 (hard)**

These are commands that need to tap into APIs that are not officially available to integrators.

Commands that fall into this category would be for example: claiming new credential, saving to centralised storage / ceramic . 

And this is difficult to implement, and also risky because there is no commitment from the Passport team to **not break** these. So the questions is, how to best deal with this situations? There will be maintenance required on the CLI tool as well.

And we do occasionally make breaking changes as continue our implementation. Such breaking changes could mean: any change in the API that are used, authentication methods, new providers that are added.

I am happy to provide further technical insights and answer any questions.

I think it is important to understand these aspects, in order to properly estimate the required effort.

-------------------------

alexdwagner | 2024-03-05 15:45:39 UTC | #7

Thanks @KarlaGod! I appreciate the +1 here :slightly_smiling_face:

-------------------------

alexdwagner | 2024-03-05 16:08:11 UTC | #8

These are some really good points. I appreciate you pointing these things out. I was intuitively grasping towards this, thinking "Alright, the `passport score --address 0x1234abcd…` and `help` commands should be easy enough, but the CI/CD functionality could be a bear–i.e. theres an "easy version" of the CLI tool, and a hard version.

Two potential solutions I see are:

* **Ship the easy version on a shorter timeline and smaller budget.** This seems the wisest path. I am new to the Gitcoin Passport dev community, and this seems like a more manageable lift for my skillset. If the dev community and Passport devs find the CLI tool useful, then there's the option to build additional functionality, such as CI/CD functionality, or functions that are more vulnerable to breaking changes. I'll grant that breaking changes happening in Passport could still break this simpler version of the CLI, but it will likely be less catastrophic than if we build a CLI that has a lot of complex functionality.

* **Work with the Gitcoin Passport leads to figure out who will maintain the Passport CLI tool once it's released.** This would be the "ship the 'hard version' option", although it's worth thinking about who will maintain the project, even if we end up just ship the easy version of Gitcoin Passport CLI. I suppose it could be maintained by either the Passport team, open source contributors, or there could be a periodic bounty to update the tool and fix any breaking changes. I ultimately want to serve the Passport team's vision and the dev community, so will be glad to defer to the Passport team here. 

I am hoping to build the Passport CLI with guidance from Passport devs like yourself, so your feedback is invaluable as I try to shape this proposal into something viable and worth funding for the DAO.

I'd love to chat and run my proposed feature set by you and get your feedback.

-------------------------

nutrina | 2024-03-05 18:41:17 UTC | #9

I think this is a good idea, to approach things incrementally (easy first, then the hard one :) ).

Looking forward for your proposed feature set.

-------------------------

alexdwagner | 2024-03-12 19:13:41 UTC | #10

Hey everyone, just a quick update that I revised my proposal above based on feedback from @nutrina and @lucian from the Gitcoin Passport dev team!

For next steps, I will create the project on Grants Stack, to be reviewed by the Grants Council in early April.

Thank you all for your feedback and your support thus far. I'm excited to apply for this grant and to keep building Passport CLI!

-------------------------

lebraat | 2024-03-12 21:50:24 UTC | #11

Thank you so much @alexdwagner for submitting this proposal. 

The comments and responses between you and @nutrina cover my feedback as well! There is some good value in making it even easier to pull Passport data directly from a CLI to start.

---

I am, however, very interested in enabling users to verify credentials outside of our walls. We have seen some recent interest in this option during partner conversations, so even making just web3 Stamps available via partner sites might be a big win. 

Here is an example screenshot of Bankless Academy enabling users to verify Stamps via their site:
![2024-03-07 16.08.04|690x423, 50%](upload://6ycyhNzFIAPfaTao6F65E7fRFh6.jpeg)

This isn't a great integration from our perspective since they are storing the data in their own databases and not in ours. Enabling partners to verify Stamps via their own site, but making sure to communicate that with us properly would be ideal.

-------------------------

alexdwagner | 2024-03-12 23:09:05 UTC | #12

Thanks @lebraat! This is valuable feedback. I am super curious to know how Bankless built that integration(likely using Passport API, how they are storing credentials data is the part I don’t have a good guess on yet), and how they are using it.

The Passport CLI is essentially a command-line wrapper for the Passport API that stores user keys in secure environment variables, so it should be able to do this in theory.

How do you think that would work in this case, especially in regard to pushing Bankless’ Passport db data to Gitcoin’s db? This may be a question for the Passport dev team :) 

Passport CLI will be downstream of whatever Passport API can do, and basically just extends that to the command-line so you don’t have to script it. 

I’ll do some research to see what I can find out about Bankless’ Passport integration.

-------------------------
