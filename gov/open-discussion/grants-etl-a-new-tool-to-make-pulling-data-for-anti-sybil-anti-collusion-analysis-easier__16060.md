---
id: 16060
title: "Grants-ETL, a new tool to make pulling data for anti-sybil/anti-collusion analysis easier"
slug: grants-etl-a-new-tool-to-make-pulling-data-for-anti-sybil-anti-collusion-analysis-easier
category: open-discussion
url: https://gov.gitcoin.co/t/grants-etl-a-new-tool-to-make-pulling-data-for-anti-sybil-anti-collusion-analysis-easier/16060
created_at: 2023-07-31T13:59:01.203Z
last_posted_at: 2023-07-31T13:59:01.277Z
posts_count: 1
views: 2755
like_count: 11
---

# Grants-ETL, a new tool to make pulling data for anti-sybil/anti-collusion analysis easier

<https://gov.gitcoin.co/t/grants-etl-a-new-tool-to-make-pulling-data-for-anti-sybil-anti-collusion-analysis-easier/16060>
owocki | 2023-07-31 14:04:19 UTC | #1

Supermodular has developed an early version of **grants-etl** - a tool that could enable data scientists to find the sybils faster/better/cheaper.

Our hypothesis is that there a need for an easy to setup relational database with clean data + a well documented schema to enable ppl to do great data work on Grants Stack/Allo/Passport without having to spend a bunch of time building their own **Extract Transform Load (ETL)** pipeline that talks to Ipfs, the graph, multiple rpc endpoints etc....

Here is a visual of what Extract Transform Load (ETL) looks like:

![|624x243](upload://aT8pClII0pb8VxDrsaWdHS3QjQ2.png)

**Our goal for this build:**
1. Create a data warehouse that allows data scientists to query information about a grants round, its contributions, and the 2nd order data about the contributors (txn history, profile, passport stamp analysis, etc).... into a well documented schema.
2. Enable it to be run locally, such that there is no central intermediary that holds & maintains the data.
3. To start, the tool will pull down information about rounds, grants, contributions, and users. But the tool is designed for easy extensibility. Anyone could build an ETL pipeline into this tool for
    1. Passport stamps or scores
    2. Data about each user from any L1/L2
    3. Any other source of data

And then PR it back into the main repo.

**Our goal for this tool long term:** My hope is that over time, as more ETL pipelines are built, and more data scientists build on top of this tool, the tool will compound in value + that will create more momentum for the blue team (sybil defense). If we can convince ppl who run Grants rounds to fund data science work, the tool will become an attractor for a blue team data economy on top of the Gitcoin ecosystem.

Play with the tool at [https://github.com/supermodularxyz/grants-etl](https://github.com/supermodularxyz/grants-etl)
Got feature requests? [Log an issue here](https://github.com/supermodularxyz/grants-etl)

I’d love feedback:

1. If you are a data scientist, is this tool useful for you?
2. If you are doing anti-sybil or anti-collusion, is this tool useful for you?
3. What ETL pipelines should be built into the tool?
4. Feel free to open up a Github Issue if you have feedback: https://github.com/supermodularxyz/grants-etl/issues

Thanks to @ghostffcode from the Supermodular team for being my huckleberry on this build!

-------------------------
