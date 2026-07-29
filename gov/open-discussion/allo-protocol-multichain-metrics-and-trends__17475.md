---
id: 17475
title: "Allo Protocol multichain metrics and trends"
slug: allo-protocol-multichain-metrics-and-trends
category: open-discussion
url: https://gov.gitcoin.co/t/allo-protocol-multichain-metrics-and-trends/17475
created_at: 2024-01-24T11:17:13.296Z
last_posted_at: 2024-01-24T22:20:40.832Z
posts_count: 8
views: 3297
like_count: 20
---

# Allo Protocol multichain metrics and trends

<https://gov.gitcoin.co/t/allo-protocol-multichain-metrics-and-trends/17475>
ivanmolto | 2024-01-24 11:17:13 UTC | #1

Hello everyone!

I wanted to give you a heads up about a new Dune dashboard focusing on metrics and trends of the Allo Protocol across various chains.

You can explore it here => https://dune.com/ivanmolto/allo-protocol-multichain

The included data is sourced from Arbitrum, Avalanche, Base, Ethereum, Fantom, Optimism, Polygon, and zkSync.

Please note that there is no available data for PGN in Dune.

Since the data is directly extracted from the Allo smart contracts, it may contain information from test rounds and projects. However, I believe the insights into trends are valuable.

Personally, I found the cumulative data from rounds and projects (which appears to be very seasonal) and the normalized visuals showcasing the performance of each chain to be particularly interesting.

Happy to hear your comments, insights, and suggestions on how to enhance this dashboard. Thank you!

-------------------------

umarkhaneth | 2024-01-24 15:48:26 UTC | #2

Nice work again, Ivan! Thank you for building! 

I love what you're working on here and would love to collaborate to push this a little further.

[quote="ivanmolto, post:1, topic:17475"]
Since the data is directly extracted from the Allo smart contracts, it may contain information from test rounds and projects. However, I believe the insights into trends are valuable.
[/quote]

Yeah this is definitely true. From my internal tracking, the total number of non-test rounds should be closer to 73. 

Are you able to add the amount of $$ that has been transferred by each contract and/or the # of votes? If so, filtering on this (e.g to only include rounds with at least $10 transferred and 10 votes) could help filter out test rounds. We may also be able to add an ALLO GMV metric which would take first prize! 

Another good strategy is filtering on the name of the round to exclude rounds which have 'Test' in the name but I'm not sure if this data can be accessed on dune (I think it's mostly in IPFS but hope to be wrong). 

Kudos again on the build my man. Great to see you hacking some more!

-------------------------

ivanmolto | 2024-01-24 16:47:39 UTC | #3

Thank you @umarkhaneth for your valuable feedback.

[quote="umarkhaneth, post:2, topic:17475"]
Are you able to add the amount of $$ that has been transferred by each contract and/or the # of votes? If so, filtering on this (e.g to only include rounds with at least $10 transferred and 10 votes) could help filter out test rounds. We may also be able to add an ALLO GMV metric which would take first prize!
[/quote]
I will explore it. Sure it will help to filter out test rounds.

Sorry for the naive question but what does it mean GMV? :sweat_smile:

Thank you once again as your job is a source of inspiration for all of us.

-------------------------

umarkhaneth | 2024-01-24 17:09:35 UTC | #4

[quote="ivanmolto, post:3, topic:17475"]
Sorry for the naive question but what does it mean GMV? :sweat_smile:
[/quote]
Gross Marketplace Value. In this case it'd be the sum of all dollars sent through Allo. For example, our Gitcoin QF GMV is $58M+ from adding crowdfunding and matching funding dollars. 

[quote="ivanmolto, post:3, topic:17475"]
Thank you once again as your job is a source of inspiration for all of us.
[/quote]
My hope is to opensource data analytics at gitcoin more and more and make it easier for anyone to contribute + be retroactively funded. We'll see how that goes and if it ends up being a smart or naive bet in the end!

-------------------------

ivanmolto | 2024-01-24 17:19:03 UTC | #5

Awesome! Open sourcing data analytics at Gitcoin has been a smart bet, for sure. 
Thank you!

-------------------------

umarkhaneth | 2024-01-24 17:51:10 UTC | #6

Thank you for always being a reliable builder. Looking forward to more :green_heart:

-------------------------

meglister | 2024-01-24 21:42:58 UTC | #7

this is awesome @ivanmolto , thanks for publishing! I'd love to find a reliable way to filter out test rounds because there are SO many of them... any suggestions? (we are happy to modify how we test internally if helpful)

-------------------------

ivanmolto | 2024-01-24 22:20:40 UTC | #8

Thank you @meglister Much appreciated.
[quote="meglister, post:7, topic:17475"]
I’d love to find a reliable way to filter out test rounds because there are SO many of them… any suggestions?
[/quote]
The suggestions from @umarkhaneth are good to filter out. I need to deep dive more on the information we can get from Dune as some logs are not decoded. 

On the other hand, I love the Allo Indexer and all the data that can be extracted.

-------------------------
