---
id: 9566
title: "GR12 topic analysis"
slug: gr12-topic-analysis
category: open-discussion
url: https://gov.gitcoin.co/t/gr12-topic-analysis/9566
created_at: 2021-12-30T19:02:40.190Z
last_posted_at: 2021-12-30T19:02:40.268Z
posts_count: 1
views: 2222
like_count: 3
---

# GR12 topic analysis

<https://gov.gitcoin.co/t/gr12-topic-analysis/9566>
freespirit | 2022-05-28 15:40:54 UTC | #1

Hey everyone! I tried to find and share something meaningful in the Grants Rounds dataset shared in the "Analyze Lifetime Gitcoin Grants Data Rounds -12" bounty (https://gitcoin.co/issue/gitcoinco/skunkworks/252/100027341).
As I couldn't actively participate in the hackathon itself I was interested in what kind of grants were most funded, e.g. what's popular now. A simple way to achieve this was to extract keywords for the most successful grants. I faced two problems:
 * how to determine the top successful grants? I used the crowdloaned amount in USD
 * retrieve the texts of the grants - as they could not be fetched through an API I simply copied the texts of grants from the gitcoin.co page of each grant (for the top3 only!)

So, I got the texts of the top3 GR12 grants and used OpenAI's GPT3 API to find the top keywords/phrases. Then I did the same for GR11 out of curiosity, to find what has changed as a trend for the past two rounds.

My work can be found at https://github.com/freespirit/gr12_simple_topics

I would also share the results here for brevity and comfort of the readers:

---- 
**GR12**

> ZigZag Exchange - ZigZag, DEX, StarkNet, zkSync, Starkware.

> Dark Forest - blockchain games, decentralized games, zkSNARKs, Ethereum.

> Coin Center is educating policy makers about public blockchains - Bitcoin, cryptocurrency, blockchain, policy research.

**GR11**

> Dark Forest - zkSNARKs, blockchain gaming, Ethereum, xDAI.

> ETHPlanet - member of togETHer - ethereum, blockchain, smart contract, dapp, solidity.

> Nym - Nym, privacy, anonymity, unlinkability, decentralized mixnet, blockchain.

----

I made some simple conclusions about the last two grants:
* blockchain games (GameFi, etc.) remain a hot topic. Particularly - Dark Forest is among top 3 in two consecutive rounds
* rollups, L2, etc. became more popular
* privacy and anonymity gave way to policy and research

Bonus:
* the top 3 GR12 grants have attracted 2.5x more crowdfunded amounts - from ~160k to ~425k
* the number of unique contributors (total for top 3) has almost doubled - from ~14k to ~27k

----
Next: once texts are available through an API I would be happy to do similar analysis for a wider range of grants:
 * historical trends - how have "most popular" topics changed throughout the history of the grants
* analysis of all grants in a given round - what other topics were there
* I would like to think more how can we predict future topics of interest, e.g. what topics would receive most grants at GR13, are there trends that are about to "break out", etc.

I would like to hear your thoughts and ideas for future work and improvement on this work. Thank you for reading!

-------------------------
