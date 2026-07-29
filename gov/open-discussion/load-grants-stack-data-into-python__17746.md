---
id: 17746
title: "Load Grants Stack data into Python!"
slug: load-grants-stack-data-into-python
category: open-discussion
url: https://gov.gitcoin.co/t/load-grants-stack-data-into-python/17746
created_at: 2024-02-12T21:21:41.216Z
last_posted_at: 2024-02-13T04:08:54.635Z
posts_count: 3
views: 2762
like_count: 10
---

# Load Grants Stack data into Python!

<https://gov.gitcoin.co/t/load-grants-stack-data-into-python/17746>
DistributedDoge | 2024-02-12 21:23:39 UTC | #1

### How to load Grants-stack data into Python?

Are you working with `Python` and feel the pressing need to obtain fresh Gitcoin Grants Data as nice `dataframe` without going through boring data-processing steps? If so, **check this out**: 

```python3
import pandas as pd

grants_stack_rounds = pd.read_parquet('http://grant-data.xyz/rounds.parquet')
grants_stack_rounds.info()

#This uses public IPFS gateway, so ~1/10 times it can be slow/fail.
```
This gets you dataframe with all Grants Stack rounds that you would normally obtain from [Grants Stack Indexer (v1)](https://github.com/gitcoinco/grants-stack-indexer) packaged in a single pandas dataframe ready for analysis, processed like so:
- columns -> renamed to `snake_case`, 
- nested `metadata` -> extracted to columns
- addresses -> normalized to `lowercase`.

More interesting files (data refreshes weekly, on monday!):
- [http://grant-data.xyz/projects.parquet](http://grant-data.xyz/projects.parquet) - all projects in Allo v1 registry
- [http://grant-data.xyz/round_votes.parquet](http://grant-data.xyz/round_votes.parquet) - all donations to every Allo v1 round

**Buyer beware** this is WIP so use **HTTP** for now => if clicking link doesn't work in your browser, try pasting the entire link in your searchbar including `http://` part.

I also don't reccomend using this for anything mission-critical, but it is prety neat for interactive terminal session if you want to load data quickly to check something.  

### How this works?

Now that you have the data, check out:

- See [Gitcoin Grants Data Portal](https://davidgasquez.github.io/gitcoin-grants-data-portal/) for ETL pipeline that makes it all possible.
- See http://grant-data.xyz for IPFS bucket where files are being served.
- See [github](https://github.com/davidgasquez/gitcoin-grants-data-portal) to contribute, report bugs or request more data!

TL;DR @davidgasquez, with some help from myself is running a Dagster pipeline that uses Github Actions to grab data from `grants-stack-indexer`, clean it and send it to IPFS bucket.

Domain redirect can take some extra time, it can be faster to refer to the bucket using its IPNS name instead. Here is an example of linking `/projects`, that is equivalent to link above:

[https://cloudflare-ipfs.com/ipns/k51qzi5uqu5dhn3p5xdkp8n6azd4l1mma5zujinkeewhvuh5oq4qvt7etk9tvc/projects.parquet](https://cloudflare-ipfs.com/ipns/k51qzi5uqu5dhn3p5xdkp8n6azd4l1mma5zujinkeewhvuh5oq4qvt7etk9tvc/projects.parquet)

Because IPFS bucket is open to anyone, you can also use it to ask SQL questions about Grants-Stack data using DuckDB webshell, like so:

[DuckDB_query](https://shell.duckdb.org/#queries=v0,select-name%2C-votes%2C-amount_usd-FROM--'https%3A%2F%2Fcloudflare%20ipfs.com%2Fipns%2Fk51qzi5uqu5dhn3p5xdkp8n6azd4l1mma5zujinkeewhvuh5oq4qvt7etk9tvc%2Frounds.parquet'-WHERE-votes-%3E-50-LIMIT-10~)

### What now?

I am writing this post because I believe that fetching Gitcoin Data for analysis of any kind is something that should be easy, and effortless!

At this moment data from `Gitcoin Grants Data Portal` has been in use by @ccerv1, @rohit, @umarkhaneth and some `Open Data Community` folks, but I would like to open the project to wider audience to collect more  feedback and encourage folks to test it out!

So for anyone reading this I would like to ask for some feedback and open discussion!

- Do you find the solution presented here useful?
- Is there some other format in which you would like data to be served (I am thinking excell spreadsheets for non-nerds)?
- Is there some data about Gitcoin rounds that you would like to see, that is hard to obtain?

I would also be interested to hear about other community-run Gitcoin "data-sphere" projects that people are working on? I am currently aware of `oss-observer` and `RegenData`, but those are both high profile made by Gitcoin insiders. At risk of sounding pragmatic, **Citizens Retro Funding #3** right around the corner, makes this excellent time to surface any community contributions in this area!

-------------------------

ccerv1 | 2024-02-12 22:34:13 UTC | #2

This is great!! I loved getting parquet files directly. Thanks for sharing and raising awareness for this awesome resource.

-------------------------

rohit | 2024-02-13 04:08:54 UTC | #3

This wonderful abstraction brings the onchain data into familiar territory for anyone comfortable with SQL. Thanks, @davidgasquez and @DistributedDoge!

If anyone is looking for sample queries/projects using Gitcoin Grants Data Portal, here are a few you can fork to start building upon:

- https://github.com/rohitmalekar/2023wrapped - Query for all voters who contributed to Rounds in 2023
- https://github.com/rohitmalekar/PGF-s-Deep-Fields - Query for all projects that received at least $10 or more in 2023

-------------------------
