---
id: 11481
title: "Knowledge Transfer: Generate Economic Graph Visualizations"
slug: knowledge-transfer-generate-economic-graph-visualizations
category: open-discussion
url: https://gov.gitcoin.co/t/knowledge-transfer-generate-economic-graph-visualizations/11481
created_at: 2022-09-11T01:54:23.945Z
last_posted_at: 2025-10-11T19:28:22.252Z
posts_count: 7
views: 4745
like_count: 13
---

# Knowledge Transfer: Generate Economic Graph Visualizations

<https://gov.gitcoin.co/t/knowledge-transfer-generate-economic-graph-visualizations/11481>
owocki | 2022-09-11 01:59:08 UTC | #1

Over the years I have been publishing graph visualizations of the Gitcoin Grants datasets, like [these](https://twitter.com/owocki/status/1540257178233106433).

![Screen Shot 2022-09-10 at 7.45.08 PM|627x500, 75%](upload://l4NCWXi5skqJCHbvpfuf33UqyJa.jpeg)
This is data from Grants Round 13.  Each node in the network is a user (or grant) and each edge is a transaction between those nodes.

I find these graphs are useful for visualizing each grants round in 3-dimensional space.  Using this data you can see which users/grants are [hyperconnectors](https://www.shortform.com/blog/malcolm-gladwell-connectors/) and which are on islands unto themselves.

@Benwest asked me to [tell him how to generate mesh visualizations of the grant data.](https://twitter.com/BenWest/status/1565818468934492162), so here goes:

# On Grants 1

1. Get staff permissions on Grants 1 from CSDO.
2. Go to `https://gitcoin.co/_administration/mesh` 
3. Enter the fields on the form, and click 'Go'.
4. This doesnt ALWAYS work because sometimes there is so much data the tool times out (either server side, or client side it can crash your browser).  If this happens, try again and use the 'trimmed' parameter to trim the dataset by 99%.

Here is what the form looks like.  The fields:
1. Trimmed, 0% to 99% how much should the data be trimmed into a representative sample? (default: 0%)
2. Label: Do you want to see the names of the nodes? (default: no)
3. Theme: light or dark, self explanatory (default: light)
3. type: return grant data, bounties data, tip data, kudos data, or all data (default: all data)
4. From/to: from => to dates (default: current day)

# /results updates

Every round I've historically tweeted out these onto [this thread](https://twitter.com/owocki/status/1540257178233106433) and updating [https://gitcoin.co/results/](https://gitcoin.co/results/) with the new viz [here](https://github.com/gitcoinco/web/blob/master/app/retail/templates/results.html#L190)

Now [that I'm disaffilated](https://gov.gitcoin.co/t/passing-the-torch/10971) I wont be doing this for [GR15 data](https://gitcoin.co/_administration/mesh?trim_pct=97&show_labels=0&theme=light&type=grant&year=2022&month=9&day=7&to_year=2022&to_month=9&to_day=22&submit=Go).  Someone in the DAO should probably do it IFF it the DAOs intent to keep publishing these.


# On Grants 2

If anyone wishes to build a similar tool for traversing the data in Grants 2, you can just use [simplegraph.js](https://github.com/gitcoinco/web/blob/master/app/dataviz/templates/dataviz/mesh.html#L30) to do it.  Just plug in the transactional data to that visualization tool.

There are probably better graph analysis tools to use, but simplegraph.js is the one i've used.

-------------------------

ccerv1 | 2022-09-11 02:09:06 UTC | #2

This is amazing. I want to give it a whirl!

For other tools for making directed or undirected network graphs, also consider:
- [Flourish](https://flourish.studio/) - easy no code solution
- [Observable](https://observablehq.com/@d3/force-directed-graph) - need to know some javascript and have your data processed, but very easy to customize AND takes advantage of the full d3 physics engine
- [Plotly Cytoscape](https://dash.plotly.com/cytoscape) - need to know python and how to deploy to a web server. This is even more customizable and helpful if you want a standalone webapp with features that a user can customize.

You can also just use NetworkX in python for a static visualization, but that's no fun.

-------------------------

owocki | 2022-09-11 06:07:53 UTC | #3

[quote="ccerv1, post:2, topic:11481"]
For other tools for making directed or undirected network graphs, also consider:
[/quote]

I think there is a sweet spot for data exploration/viz tools like these to hasten the DAOs ability to turn data into learning into insights.   could be major alpha in the [infinite game against the red team](https://twitter.com/owocki/status/1565728303767375873)!

-------------------------

owocki | 2023-08-20 19:40:16 UTC | #4

FYI there are now two graph visualization tools you can use for allo protocol era economic graph vis

1. https://gitcoin-beta-networks.streamlit.app/ by @umarkhaneth (works for alpha rounds)
2. https://grants-graph.vercel.app/ by @ghostffcode (works for alpha rounds/GG18)

neat to see one of the most prominent grants out there using these visualizations to promote the round :) https://twitter.com/lensterxyz/status/1692963337330729288

-------------------------

umarkhaneth | 2023-08-21 13:52:39 UTC | #5

https://gitcoin-networks.streamlit.app/ 

The economic graph visualizer lives at this link now ^ added gg18 in there and filters by donation amount + passport score

-------------------------

ccerv1 | 2024-06-27 21:00:43 UTC | #6

Adding these little toys:
https://ethereumgrantsdata.streamlit.app/
https://github.com/ccerv1/ethereum_grants_data

-------------------------

owocki | 2025-10-11 19:46:52 UTC | #7

gitcoin 3.0 era explorer : https://viz.gitcoin.co/
code: https://github.com/owocki/gitcoin_30_3d

(still WIP)

-------------------------
