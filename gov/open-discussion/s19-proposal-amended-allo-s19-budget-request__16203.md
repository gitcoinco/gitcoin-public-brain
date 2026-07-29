---
id: 16203
title: "[S19 Proposal Amended] Allo S19 Budget Request"
slug: s19-proposal-amended-allo-s19-budget-request
category: open-discussion
url: https://gov.gitcoin.co/t/s19-proposal-amended-allo-s19-budget-request/16203
created_at: 2023-08-08T20:14:30.588Z
last_posted_at: 2023-08-11T13:53:19.401Z
posts_count: 2
views: 1527
like_count: 5
---

# [S19 Proposal Amended] Allo S19 Budget Request

<https://gov.gitcoin.co/t/s19-proposal-amended-allo-s19-budget-request/16203>
deltajuliet | 2023-08-08 20:14:30 UTC | #1

Posting on behalf of @nategosselin while he's OOO this week :slightly_smiling_face:


### Allo TL;DR

Allo is a **resource allocation protocol** — it empowers groups to efficiently and transparently allocate pooled capital. Version 1 of the protocol launched in H1 2023 and was pressure-tested by the Gitcoin Alpha/Beta rounds on Grants Stack, a third-party audit by Sherlock, and an initial cohort of integrations. [We decided to begin working](https://gov.gitcoin.co/t/allo-grants-stack-mid-season-update/15278) on [Allo v2](https://docs.google.com/document/d/1Me5jdrkQy7dQkBYys4LZ7cTLIJCdjSHOlughBhTiLIU/edit#heading=h.tvxzmiinefwo) in S18 given the feedback from those experiences, which surfaced that v1 was not adequately hitting our goals for the protocol.

Despite the pivot to v2, we have made a lot of progress with Allo Protocol this past season:

* The [core v2 contracts are built](https://github.com/allo-protocol/allo-v2) and [deployed to testnets](https://twitter.com/alloprotocol/status/1686437328506540036?s=20), and we are kicking off a Community Build Period in August before going to audit
* We also built [~13 allocation strategies for the library](https://github.com/allo-protocol/allo-v2/tree/main/contracts/strategies). This effort enabled us to build a mix of production-ready and POC strategies for launch, as well as pressure-test our interfaces.
* [Endaoment](https://endaoment.org/) has [launched](https://www.nonprofitpro.com/article/endaoment-and-gitcoin-unveil-new-200000-universal-impact-pool/) a [Universal Impact Pool](https://app.endaoment.org/universal) on top of Allo
* Grants Stack is on track to hit its QF goals for S18 using v1
* Direct grants was developed on Allo v1 by Grants Stack
* Deployed Allo v1 to PGN for GG18
* Impact Stream [announced its plan](https://satchel.works/@wclittle/ventures-episode-151) to enable public goods funding in Togo with Allo
* Allo v2 was featured in 6+ talks and workshops across EthBarcelona, Funding the Commons, and EthCC, helping build a pipeline of teams interested in building on top of the protocol

We are excited to build on this momentum as we move into S19.

### S19 Strategy

We see resource allocation as a broad market category that we can help define. Given the newness of this category, our team is taking a vertical approach to launching Allo v2 so that we can bring clearly shaped use cases to market and ease adoption for new users. **We are focusing specifically on web3 grants as our first market segment** , as we are closer to the problem space from our history with Gitcoin Grants and have a healthy pipeline of interested programs.

We consider the end user of this segment to be web3 grants programs — e.g. teams that are distributing funds to advance a cause or grow an ecosystem. While we realize that most programs will not interact directly with the protocol, we want to use their major pain points (as uncovered by past Gitcoin reasearch) as guides to ensure that solutions are present in the Allo ecosystem. Specifically, we are focusing on the following user problems:

1. **Unwieldy grants management workflows** — most programs rely on general tools (Notion, Excel) to manage their workflows, which become hard to use as the program scales.
  * *Intended protocol solution* : Power the allocation backend of grants management apps, so that those products can focus on workflows.
  * *S19 focus* : Secure integrations with pre-existing management apps (e.g. Grants Stack, Questbook, etc) and seed complementary grants products (curation tools, etc).
2. **Vetting applicants** — Grants managers tend to spend a large chunk of time vetting applicants, instead of working with accepted grantees to achieve success.
  * *Intended protocol solution* : Maintain a universal profile registry with blockchain-secured verification and trust signals for applicants. This will cut down on time spent vetting by enabling programs to set programmatic acceptance criteria and providing trust signals for any additional manual review.
  * *S19 focus* : Bootstrap the Allo profile registry by enabling past Gitcoin grantees to port over their data and seeding profile management products.
3. **Customizable, secure, and transparent program rules** — Despite common styles, every community has slightly different program configurations (eligibility, voting, etc) and similar demands for transparency and accountability.
  * *Intended protocol solution* : Provide a library of audited, secure, and transparent allocation strategies that can easily be copied and customized for each program.
  * *S19 focus* : Use hackathons to drive additional strategy creation, and push audited library of strategies to mainnet.

#### What’s next?

You can read more about the investments we’re making to achieve our goals and what’s on our roadmap at the links below.

* [Allo Vision + Strategy](https://docs.google.com/document/d/18wwdBJhC6Ukgp-lZ_ecmL7_cim0YhdO6a6brylYlHhQ/edit?usp=sharing) — our long-term plan for Allo
* Allo GTM: Web3 Grants (*coming soon* ) — our plan for launching Allo within the web3 grants vertical
* [Roadmap](https://docs.google.com/spreadsheets/d/1Pwfh-F87TPi_L2ykYhqa4UOIKwzlKrVnUmxEgs4CasI/edit#gid=0) — our next 3-6 months of development projects

### S19 Goal

**3 products built on Allo v2**

* Status: 0 / 3
* We know that grants programs will require user interfaces to use Allo v2. With the protocol foundation laid, we want to focus on getting our initial cohort of Allo v2 products up and running.

While this is the objective we’ll focus on hitting, we will also be track and report on the following key metrics:

* Mainnet pools created on Allo v2
* Dollars distributed by Allo v2 pools
* Profiles created on Allo v2

### S19 Budget Request

As [originally proposed](https://gov.gitcoin.co/t/proposal-gitcoin-allo-workstream-season-18-19-budget-request/14114), Allo + Grants Stack had a combined S19 budget of $1,119,066 (not including reserves). When the teams split ([more here](https://gov.gitcoin.co/t/allo-grants-stack-mid-season-update/15278)), the workstream leads reviewed team costs and came up with a rough budget split — Allo’s portion of the original S19 budget was calculated as ~28%, or $339,950.

**Our new S19 budget request is $438,449 before reserves, an increase of 29%.** A few notes on this request:

* The increase is almost entirely driven by the need to audit v2 before pushing to mainnets. We will conduct an initial audit of the core contracts, as well as auditing allocation strategies that are ready for production. The budget for audits is $110k, based on a variety of quotes we’ve obtained from respected auditors.
* Despite the increase from the audit, the revised S19 budget from Allo + Grants Stack combined is still a reduction from the original S19 budget for the two workstreams.
* We have updated our team structure, replacing a part-time DevRel head and part-time Workstream Engineering lead with a full-time head (Zakk) covering both functions. The impact on our overall budget is effectively flat, but you’ll notice that some budget has shifted from the DevRel line item to Contributor Salaries.

|Line Item|August|September|October|Total|
| --- | --- | --- | --- | --- |
|Total budgeted spend|$109,483|$181,483|$147,483|$438,449|
|33% reserves||||$146,150|
|Past Season Treasury Balance||||$72,942|
|**Total S19 Request**||||**$511,656**|

Budget Evolution:

||S18 (original budget)|S18 (projected actuals)|S19 (original budget)|S19 (revised ask)|
| --- | --- | --- | --- | --- |
|Budget|$319,950|$324,847|$339,950|$438,449|

#### Budget Breakdown

Allo Protocol is staffed by the following team:

Core contributors (5):

* Nate (Workstream lead - Product)
* Zakk (Workstream lead - Engineering)
* Aditya (Engineering lead)
* Jason (Engineer)
* Kurt (Engineer)

Part-time contributors (1):

* Sorana (Ops)

Our cost breakdown is as follows:

||S18 (original budget)|S18 (projected actuals)|S19 (original budget)|S19 (revised ask)|
| --- | --- | --- | --- | --- |
|Contributor Salaries|$211,765|$213,891|$211,765|$268,950|
|Contracting|$18,000|$69,000|$18,000|$24,000|
|DevRel|$69,061|$32,440|$69,061|$20,000|
|OpEx|$21,125|$9,516|$33,625|$125,499|

#### Closing thoughts

Allo will likely remain free for the majority of this season while we focus on adoption. We are actively developing revenue and token utility plans that we’re excited to share in the near future.

-------------------------

CoachJonathan | 2023-08-11 13:53:19 UTC | #2

I will be voting in favor of this proposal.

The delays on fully launching Allo have been unfortunate, though there seems to be a clear path forward and a bright future for this product. I'd like to see that funds make their way to this lean team to finally (and fully) release this protocol into the wild.

-------------------------
