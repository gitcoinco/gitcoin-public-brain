---
id: 18098
title: "Citizens Innovate GCP - Gitcoin Grants Data Portal"
slug: citizens-innovate-gcp-gitcoin-grants-data-portal
category: citizen-grants
url: https://gov.gitcoin.co/t/citizens-innovate-gcp-gitcoin-grants-data-portal/18098
created_at: 2024-02-25T17:27:11.960Z
last_posted_at: 2024-07-25T12:53:02.661Z
posts_count: 16
views: 4558
like_count: 46
---

# Citizens Innovate GCP - Gitcoin Grants Data Portal

<https://gov.gitcoin.co/t/citizens-innovate-gcp-gitcoin-grants-data-portal/18098>
davidgasquez | 2024-03-06 13:04:38 UTC | #1

# Gitcoin Grants Data Portal

This is a Request For Feedback for the Gitcoin Grants Data Portal [Gitcoin Citizens Innovate](https://gitcoin.notion.site/Citizens-Innovate-cf556fdb861143e78765410b368565c2) grant proposal.

## :memo:  Proposal Description

The proposal ask for $20k in funding over four months to enhance access to curated datasets on the [Gitcoin Grants Data Portal](https://davidgasquez.github.io/gitcoin-grants-data-portal/), aiming to foster community engagement, network effects, and cost efficiency in decision-making and analysis across the ecosystem.

The Data Portal has had a significantly impact already through collaborations, better directories, analysis (e.g: clustering, visualizations), Sybil hunting, and supporting adjaccent communities (e.g: Arbitrum), enhancing data access and utility across multiple initiatives (see [Impact](###Impact)).

For context, the [Gitcoin Data Portal](https://davidgasquez.github.io/gitcoin-grants-data-portal/) is an [open source](https://github.com/davidgasquez/gitcoin-grants-data-portal), serverless, and local-first open Data Platform for Gitcoin Grants Data. It has evolved into the schelling point for open and permissionless datasets around Gitcoin Grants and related areas. 

![upload_4cc99155b3988601fc4273f66beb8204|690x306](upload://5fpoCl307EmU6ZEY6F6jieF1Bpl.png)

### :bulb: Motivation 

> **Frictionless access to Community Curated Gitcoin Grants Datasets :arrow_right: More analysis work gets done :arrow_right: Better decisions**

Accessing and analyzing clean and curateed Gitcoin Grants data has been historically time-consuming and complex task. Gitcoin Data Portal removes those obstacles by providing a central hub where community curated Gitcoin Grants datasets are accessible to everybody!

By lowering the barrier of entry and having more people look into the data, we expect to see more people re-using the curated datasets to make better decisions and produce interesting reports and tools!

### 📑 Specifications

Proposal is split into two stages. First we improve data portal by making it more accessible. Then, focus on increasing its utility and profile by opening it to relevant data from other communities.

**Stage 1:** Provide Gitcoin with single place to get all interesting Gitcoin datasets in easy-to-consume format. We are already doing this, but we want to make the project better, easier to use and seen by more people!

**Stage 2:** Extend **Gitcoin Data Portal** to become **Grants Data Portal** holding up-to-date information about multiple Web3 Grant communities (Arbitrum, Optimism, Giveth etc.) in a single place!

### :wrench: Technical Details

For a short overview on how the Gitcoin Grants Data Portal works, see the [about-page](https://davidgasquez.github.io/gitcoin-grants-data-portal/about.html#key-features). You can think of it as a lightweight data pipeline built using [Dagster](https://dagster.io/), [dbt](https://www.getdbt.com/), and [DuckDB](https://duckdb.org/), with additional module that allows us to publish website to Github pages and render Jupyer notebooks. 

![image|690x208](upload://bdjAyDn9EQPujhjQsLP8gDPxZiG.jpeg)

The pipeline fetches raw data from various sources, transforms it using `dagster` and `dbt` up and materializes the tables it into `.parquet` files which are then pushed to IPFS. 

Example datasets for gitcoins include all Allo v1+v2 (`donations`, `projects`, `rounds`) as well as some more technical data taken from other sources (e.g. list of Allo Contract deployments or gas consumed by mainnet project registry)

The scope of the technical work is to design and build:

- Robust pipelines to ingest, clean and join new datasets
- Notebooks and models to analyze and curate existing datasets
- Multiple improvements on the DX side; CI, CD, Contributing Guides, ...
- Tests to ensure data quality across datasets

## :world_map: Roadmap

### Stage 1

> $8k, 2 months

- Better documentation
    - improve overall documentation
    - add contributor guides
- Better datasets
    - evolve dbt models
    - unify schemas
    - add tests
    - add new Gitcoin datasets to portal (e.g. Snapshot, Discourse stats)
    - introduce basic support for `project profiles` data coming from other communities (e.g. Giveth, Drips, Octant)
- Better UX
    - add Jupyter and Obervable notebooks as examples showing how to use portal data 
    - promote portal on X by publishing analysis, notebooks
    - serve data in multiple formats to make it more accessible (e.g. checkout a spreadsheet via simple streamlit site)

### Stage 2 

> $12k, 2 months

Extend scope of portal to serve multiple communities and become THE place to go to find open datasets about projects/donations in crypto-grants ecosystem. `Gitcoin Data Portal` => `Grants Data Portal`

- Add more non-gitcoin datasets to the portal (e.g. Octant, Giveth, Drips)
- Create shared tables by reconciling multiple schemas e.g. `all_project_profiles` (Giveth + Gitcoin + RetroPGF)
- In addition to `project profiles` track `donations data` coming from other communities (tricky - everyone has different way of doing that)
- Experiment with various forms of serving data (e.g. S3 bucket)

**Stretch goals** we *may* implement, but it depends on collab with external actors:

- Transfer data to/from OS-Observer, RegenData.xyz
- Publish impact blog post(s) on OS-Observer 
- Export (some) data to Dune/Flipside. [we can do this easily, just for some small datasets]
- if there is interest from LLM groups, serve tokenized text/embeddings in a format that can be easily consumed by NLP/LLM models (but we need to know *which* models)

## 💼 Budget & Milestones

We ask for payments to be delivered in four monthly installments at end of each month. Expenses would cover development effort by @DistributedDoge and @davidgasquez. We will set aside some funds ($1000~) for maintenance and infrastructure costs (around $20/month currently for the IPFS pinning service). 

| Month | Payout   | Milestone              |
|-------|----------|------------------------|
| 1     | $4000    | Better pipeline        |
| 2     | $4000    | Better UX              |
| --    | --       | REVIEW                 |
| 3     | $6000    | More data              |
| 4     | $6000    | **Grants Data Portal** |

Between milestones 2 and 3, we can review the state of the portal and evaluate the best way to continue with further funding.

### Essential Intents & Benefits

In this combined section, we map each community intent to percieved benefits of funding this proposal. Some of those can be used as KPIs. 

#### Community Engagement
1. Make Gitcoin data easier to access and use.
3. Attract new analysts interested in working with Gitcoin Data.
4. Save time for existing analysts and developers in Gitcoin Community .

#### Network Effects
1. Support other Citizen and Core initiatives. 
2. Support Gitcoin adjacent communities.
3. Help Gitcoin identify high-potential grantees from other ecosystems.
4. Help Gitcoin understand current market trends.
5. Let community collaborate on curated models ala [Dune Spellbok](https://github.com/duneanalytics/spellbook), but for Grants data.

#### Cost Efficiency 

- Assume average analyst is paid 50$/h
- Assume portal turns 5 hour of data preparation and cleaning into 1 hour
- Saves 200$ per single use of portal

> 10 users ==> $2k savings
> 100 users ==> $20k saving
> 1000 users ==> $200k savings

On top of that:
- Community is incentivized to work on shared datasets instead of re-building the same data pipelines over and over for each project.
- Thanks to the project modularity other Python codebases can borrow our data-fetching pipelines
- The final curated datasets are available for free to anyone!

### 🤔 Drawbacks

#### Portal may publish incorrect data
Mitigating this by writing `dbt models` to ensure data quality + improving CI-pipelines. For Gitcoin we have `RegenData.xyz` to spot check our datasets for inconsistency. Exposing datasets to as many users as we can will also make them more resilient.

#### Portal may become more costly to run due to changes
One of the portal tenets is to be "lean" and "cheap". At the moment we need no long-running server so the only cost for public version is $20/month Filebase subscription to publish data on IPFS. Running local stack on local machine (within Github codespace) will always stay completely free.

#### Portal may be hard to use
The only thing you need to use the portal is knowing which datasets will cover your needs and be able to read/use them. We are actively  (1) talking to anyone interested in using Gitcoin data and (2) publishing datasets in open and standard formats to make sure things move in the right direction!

Developing (e.g: pipeline for a very large dataset) might become more complex in the future. At that point we'll evaluate the best approach to keep things lean.

#### Portal won't be maintained once funding runs out
At the end of the day, the portal is "*just*" a batch processing pipeline that generates some static files. That means that you press button, get the data and then forget it exists untill next time you need data. No long lived servers to maintain! If at a certain point the portal is not maintained and someone needs it, it'll only need to clone and run it from their computer to get up to date datasets.

That said, some maintenance will be needed to deal with changing models and the natural evolution of APIs but we are already doing that with no funding for last 4 months so it is not that time consuming.

### :boom: Impact

List of collaborations using Gitcoin Data Portal or data coming from it:
- Providing data for OS-Observer impact-tracking [research](https://docs.opensource.observer/blog/gitcoin-grants-impact)
- Growing OS-Observer grantee [directory](https://github.com/opensource-observer/oss-directory) (~30% of Github projects imported using)
- [Providing data for Grantee-clustering POC](https://gov.gitcoin.co/t/concepts-pocs-and-early-results-for-personalized-grantee-recommendations/17469)
- Providing data for Gitcoin-end-of-year [visualization](https://twitter.com/RohitMalekar/status/1742196496152642030?s=20)
- Sybil hunting in Citizens#2 round
- Arbitrum-led Open Data Community [hackathon](https://github.com/OpenDataforWeb3/DataGrantsforARB)

Data Portal positions itself in a strategic place as smoothing access to quality and curated datasets can support many different iniatives in very cost-efficient manner.

## :speech_balloon: Conclusions

**We are asking for $20k funding over the period of four months to improve the Gitcoin Grants Data Portal**.  Funding will be used in the development and iteration of existing data-platform. **First stage of the proposal requires $8k over two months**.

This proposal now enters community feedback period until end of the month, so we encourage everyone to share feedback here, or on the [project Github](https://github.com/davidgasquez/gitcoin-grants-data-portal)! Thanks for reading. :raised_hands:

-------------------------

Pfed-prog | 2024-02-25 18:25:39 UTC | #2

[quote="davidgasquez, post:1, topic:18098"]
#### Portal won’t be maintained once funding runs out

At the end of the day, the portal is “*just*” a batch processing pipeline that generates some static files. That means that you press button, get the data and then forget it exists untill next time you need data. No long lived servers to maintain! If at a certain point the portal is not maintained and someone needs it, it’ll only need to clone and run it from their computer to get up to date datasets.

That said, some maintenance will be needed to deal with changing models and the natural evolution of APIs but we are already doing that with no funding for last 4 months so it is not that time consuming.
[/quote]

There should be funding available, I hope.

Definitely, take a look at OpenData Community available funding

https://github.com/OpenDataforWeb3/DataGrantsforARB

-------------------------

epowell101 | 2024-02-25 20:32:35 UTC | #3

Just a quick note to say that I think it would be a great idea for the Gitcoin Grants Portal to be supported in this way.  

This is exactly the sort of work that by its nature should be independent from Gitcoin for the sake of credibility.  

Most importantly, I've seen both @DistributedDoge and @davidgasquez collaborate with me and others in the OpenData Community.  They ship, they comment, they listen, they dig in, they volunteer their time to help others in the OpenData Community.  

Lastly, it is worth emphasizing that the architecture of the Grants Data Portal is itself distributed and open, using systems such as IPFS and leading open-source projects such as DBT.   I'm willing to look the other way on the reliance on GitHub here and there since much of the open-source world is similarly dependent.  

Anyway - I'm strongly supportive of this project as a data nerd, one of the founders of the OpenData Community, and as a collaborator with @davidgasquez and @DistributedDoge

-------------------------

ccerv1 | 2024-02-25 23:21:20 UTC | #4

Full disclosure: I am a data nerd and therefore I probably do not represent the typical Gitcoin community member.

But ... as a frequent user and collaborator of the Gitcoin Grants Data Portal, I'd love to see these types of improvements. I'll also add that I've only had good experiences working with @davidgasquez and @DistributedDoge.

Finally, I realize that it's hard to review these types of proposals without considering other ways of spending $20K or the overall financial targets for the DAO. Assuming Gitcoin has appetite for a small-scale data GCP, then I enthusiastically support this proposal.

-------------------------

owocki | 2024-02-25 23:57:07 UTC | #5

I support this proposal.  I will be voting yes on this proposal.

-------------------------

skyfoxx | 2024-02-27 16:27:24 UTC | #6

It's a really good proposal, but I'm curious, why not update it to use a dashboard from Dune or Bitquery?

That would remove the complexity of maintaining the stack/ documentation, and make it about maintaining just queries over time.

I would assume easier to build the UX and users to access the data?

-------------------------

Jeremy | 2024-02-26 15:17:57 UTC | #7

I support this as well, the more we can have open data in the ecosystem for others to review, use, and make recommendations, the better it will be for us to improve the systems. I think @umarkhaneth was doing some work on this and could provide some data flows and/or data pipelines.

We can also provide data that is publicly available either directly from Passport (indexer or APIs) and also from our Ceramic node.

I'm a huge fan of the work @DistributedDoge has already done for the DAO!

-------------------------

umarkhaneth | 2024-02-26 22:53:21 UTC | #8

I love this proposal. Having data backed up to IPFS and openly accessible for community analysis is a design pattern I think will proliferate in Web3. I'm glad to see @davidgasquez and @DistributedDoge buidling.

I'd like to add more of Gitcoin's historic data to the portal. The Allo indexer picks up data from the Beta/GG17 forward. I have a dataset of all donations and matching information from GR1 through Alpha/GG16 we should add. DMing to see what the best way to do this is

-------------------------

DistributedDoge | 2024-02-27 09:38:08 UTC | #9

Thanks to everyone for the kind feedback so far!

Noted down actionable items from the suggestions:

- move some logic from Github-actions to Dagster
- look into passport data (so far we serve `passport_scores` from indexer_v1)
- add docs explaining how to share data with Gitcoin Portal

To give more context to DAO members thinking about spending, current funding pool for Citizen Innovate proposals is about 450k GTC. 

Regarding suggestion that `there should be funding available` - there really is! The better job we do indexing Web3 Grants the more future funding opportunities open ahead of the portal (e.g. Octant, Optimism Retro). But for now let's gather enough resources to build the thing without distractions!

-------------------------

rohit | 2024-02-27 13:07:42 UTC | #10

I am going to wear two "hats" to respond :grin:

As a user of the portal, it's been an absolute blessing to access the data in familiar realms of SQL over having to learn GraphQL or building pipelines to get data from Indexer. I look forward to iterating on the next version of GrantsScope to include recommendations for the upcoming Citizens Round using this portal (and setting split funding/drips to reflect this dependency).

As the program manager for Citizens Innovate, I recommend tracking the adoption of the effort (unless already in place) using metrics that make the most sense (view counts, trends in spikes, etc.). While not a show-stopper for this roadmap, it will help establish a baseline against which you can capture trends over time.

-------------------------

Viriya | 2024-03-04 15:26:40 UTC | #11

I'm sorry to be slow to respond here. Somehow I missed this proposal. Thanks for the poke @rohit :slight_smile: 
I really appreciate the notes and bodes of confidence outlined by others who have been deep in Gitcoin's data. I plan to vote yes on this proposal. I think it will set amazing foundation for some of the things we're trying to accomplish as an ecosystem and it will unlock opportunities for better and easier impact reporting in the future.
I'm particularly interested in Stage 2 :slight_smile: 

I appreciate the call out about the maintenance issue (which we all know is a challenge). Once stage 2 is complete, there may be an opportunity for RPGF within the Gitcoin Citizen Grants fund and perhaps other programs that can cover the maintenance costs.

-------------------------

KarlaGod | 2024-03-05 07:08:13 UTC | #12

Data is an important part of *"on-chain feedback & analysis"*, it'd be great to have *a kind of* one-stop-shop where everyone can go and get historical data on Projects and Gitcoin grants rounds and even predict outcomes for the next round, and have accurate data to work with for growth.

-------------------------

meglister | 2024-03-06 18:37:57 UTC | #13

Hey @davidgasquez and @DistributedDoge , thanks so much for this thoughtful proposal! I'm broadly in support of it. I've also chatted with a few of our data folks internally at Grants Lab and am copying some feedback and ideas here for your consideration.

- First of all, the tech stack and usage of IPFS is really cool! Kudos on this setup.
- There's a few things we think would make this data set much more useful, based on our experience with other users of the Grants Stack Indexer. These include passport scores and more historical data (which we are happy to help with!) 
- From my perspective, these kinds of additional data, custom models, and non-Gitcoin data sources are key to making the project useful. There are definitely easier ways to just access the raw data, so we should focus on enriching this data set and making it maximally useful for rich analysis.
- Pushing fresh labels to Dune that are generated through this project would also be awesome.

One thing to consider for the future: we have a project that we maintain internally (RegenData) that provides nearly identical functionality (though is gitcoin grants only + hosted on cloud server instead of ipfs). I think there's value in rewarding your historical efforts and the improvements noted through this proposal, though I'd want to reevaluate if we should continue supporting both in the future. Would love to discuss if/how we might bring these efforts closer together to maximize data usage and collaboration.

-------------------------

davidgasquez | 2024-03-07 18:49:11 UTC | #14

Thanks for the kind words! 

> There’s a few things we think would make this data set much more useful, based on our experience with other users of the Grants Stack Indexer. These include passport scores and more historical data (which we are happy to help with!)

Let's chat! If you're up for it, feel free to [just open issues](https://github.com/davidgasquez/gitcoin-grants-data-portal/issues/new) there and we can take it from there.

> There are definitely easier ways to just access the raw data, so we should focus on enriching this data set and making it maximally useful for rich analysis.

That's our hope with the next iterations. Making better datasets and mke them easier to consume for different types of analysis.  :100: 

> (RegenData + Grants Portal) Would love to discuss if/how we might bring these efforts closer together to maximize data usage and collaboration.

Agree! Would love to chat about that. Personally, I have started to think of the Grants Data Portal as potentially downstream from the RegenData database and models. Those are probably more advanced and battle-tested, so we could totally reuse the public ones and avoid duplication.

-------------------------

meglister | 2024-03-07 19:42:08 UTC | #15

Awesome, thanks for your reply @davidgasquez ! Maybe we can start a group chat with some of the core data folks in Grants Labs/citizen's community. Mind sending me a message on discord or tg and we can take it from there?

-------------------------

rohit | 2024-07-25 12:53:02 UTC | #16

@davidgasquez @DistributedDoge congrats on the new website for Gitcoin Grants Data Portal - https://grantsdataportal.xyz/

Summarizing the features I was able to test successfully here - accessing data based on the latest Allo model, updates to the latest models for Passport Score, features for improved developer experience (abstracting IPNS gateway with static URL, the case for addresses always trips me :D great to see it consistent now), and datasets beyond Gitcoin donations (Giveth, Karma, Discourse). I have verified these milestones on Karma GAP as well.

As we discussed, some scope from the original proposal (contributor guides, reference Jupyter notebooks, optionality in data formats) is pending development.

As the next step, I will proceed with a prorated Citizen Grants payment of $16K in parity with completed milestones. Looking forward to the adoption of the portal for data analysis, reporting and insights - All the best!

-------------------------
