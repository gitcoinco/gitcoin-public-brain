---
id: 19765
title: "Deep Funding - a visual guide in 3 easy steps"
slug: deep-funding-a-visual-guide-in-3-easy-steps
category: open-discussion
url: https://gov.gitcoin.co/t/deep-funding-a-visual-guide-in-3-easy-steps/19765
created_at: 2024-12-17T05:08:21.755Z
last_posted_at: 2025-02-24T04:57:33.324Z
posts_count: 4
views: 2914
like_count: 8
---

# Deep Funding - a visual guide in 3 easy steps

<https://gov.gitcoin.co/t/deep-funding-a-visual-guide-in-3-easy-steps/19765>
owocki | 2024-12-18 19:26:01 UTC | #1

# deep funding : a visual guide in 3 easy steps

deep funding is a new way of funding open source software introduced by Vitalik Buterin last week.  myself and @sejalrekhan and a few others are working on a pilot with him.

the 1st deep funding pilot is $170k in ETH to figure out which OSS dependancies of Ethereum to fund.  

the basic question being asked here is "what dependancies do we fund? which are the most important to Ethereum?"

STEP 1 the first thing we do is map the dependancies.

![Screenshot 2024-12-18 at 12.25.39 PM|470x500](upload://dxhgiUJMjtly0IJhYnfJ1o8wLI6.jpeg)

to do so, a data layer is created mapping the various dependencies (vertices) of a project and the connections between them (edges).

now we must evaluate which dependency to fund at what level.

but how do we do that?  there is a scale problem here. current public goods funding mechanisms require funders to evaluate each project, making the process increasingly burdensome as the number of applicants increases. funding mechanisms end up depending either on a large group of people, creating incentives for projects to publicly campaign to get themselves known, or a small group of people, creating incentives to privately curry favor and limiting the mechanism’s effectiveness at scaling beyond a small number of projects.

in Deep Funding, most of the work gets done by a public market of allocators, that suggest proposed weights of edges in a graph, which answer the question “what percent of the credit for A belongs to B?”. potentially, there could be millions of weights to allocate, and so we encourage using AI to do this.

this market of allocators assign weights to the edges to indicate their relative importance.

![Ge-ZisJWIAA_nMV|527x500](upload://gf8e3zZgc3VwGtFyxZ22oFJYy8Z.jpeg)

now that we've got a handful of agents that have ranked the dependancies and formed opinions about which part of the dependancy graph to reward, its time to figure out which agent is correct.

to do that, a jury of experts “spot-check”s the graph, expressing expert preferences on a randomly selected set of edges. 

the goal of all of this is to determine: which agents most closely align with your preferences?

![Ge-Z1LtWUAAuL2t|509x500](upload://yKrLe7g2MFtWKcSDDIeSznqNIqB.jpeg)

at the end the prizes will be distributed. 

the mechanism then distributes funding to repos based on the weights provided by agent allocators that are most compatible with the spot checking results. 

here is how prizes in the pilot will be distributed:
* $170k - repos based on the weighting of their edges by the winning model
* $40k - models that conform the best with spot check results by jury members manually giving weights
* $40k - prizes to open source submissions of models, based on how interesting they are to jury members

what is the timeline for this experiment?

* NOW - Data on 40,000 Ethereum dependencies for building your model has been rleased
* Jan 20th - Sample spot check data by jury members to train your model
* Jan 20th - Deadline for “early bird” prizes for open source model submissions. At least half of the open source model submission prize pool will be reserved for early bird submissions.
* Feb 20th - Submit your model 
* Feb 27th - Results (the same day as schelling point :) )

if you want to get involved and submit a model, checkout deep funding dot org

thanks to vitalik, allo, gitcoin, voicedeck, oso, evalscience, drips, and pairwise for the hard work building this with us!

zooming out - it is an exciting time, we are prototyping a new way of funding what matters!  i hope to see this pilot be successful and see the  mechanism spread far and wide in 2025!

it could grow in 2 ways i think
1. fund more open source.
2. fund other things that depend on dependancy graphs

lots of other things have dependancy trees that could be funded this way 
1. open source software, dependancy trees of software
2. scientific research, eg dependancy trees of citation graphs
3. assembly theory - dependancy trees of simpler assemblies/legos its built upon
4. music - eg dependancy trees of sampling of other songs/beats.
5. legal systems, eg dependancy trees of precedent  
6. movies, dependancy trees of ideas (for example star wars was a fork of dune)
7. journalism, eg dependancy trees of reporting
8. what else?

TLDR - deep funding funds dependancy trees deeply.  it is a new frontier in public goods funding!  pilot is happening.  

DM if you are DTF (down to fund) a deep funding pilot in your own ecosystem.

-------------------------

Oba-One | 2024-12-19 23:33:03 UTC | #2

Checkout the Greenpill Podcast discussing [Deep Funding](https://deepfunding.org)!
https://youtu.be/ygaEBHYllPU?si=jeqYK1pK-HZ4rhF_

-------------------------

CanopyCulture | 2024-12-20 04:59:38 UTC | #3

When we think about Ethereum's dependencies, we often focus on software libraries, code bases, and direct technical dependencies. However, one crucial yet underfunded dependency category is mid-sized server farm operations across the globe.

These aren't massive centralized data centers, but rather professional node operations that:
- Provide robust computational power for the network
- Maintain geographic distribution and decentralization
- Operate at a scale above home nodes but below major cloud providers
- Require significant technical expertise and capital investment

This infrastructure layer is currently underfunded in the Ethereum ecosystem, despite being critical for:
- Network resilience and performance
- Reducing reliance on major cloud providers
- Supporting growing network demands
- Maintaining true decentralization

We can look to Filecoin as an example of how to better support this type of infrastructure - they've successfully created incentives for mid-sized storage providers around the world.

The $170k pilot to identify critical dependencies could be an opportunity to recognize and start addressing this infrastructure gap. While software dependencies are obviously important, the ecosystem also needs to consider how to better fund and incentivize these crucial infrastructure providers that sit between individual stakers and centralized server farms.

-------------------------

APAC | 2025-02-24 04:57:33 UTC | #4

This pilot is awesome. I happened to read an article which was unrelated , yet, seems to speak directly to this issue in the manner by which it would approach Deep Funding per se.

I'm hoping this pilot leads to a community of great minds who can eventually help create the foundation for a really vibrant framework where qualitatively good OSS contributions can get the funding it/they deserve 🙇.

-------------------------
