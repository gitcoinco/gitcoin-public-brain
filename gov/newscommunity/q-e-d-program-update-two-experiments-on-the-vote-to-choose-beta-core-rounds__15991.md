---
id: 15991
title: "Q.E.D. Program Update Two: Experiments on the vote to choose beta \"core rounds\""
slug: q-e-d-program-update-two-experiments-on-the-vote-to-choose-beta-core-rounds
category: newscommunity
url: https://gov.gitcoin.co/t/q-e-d-program-update-two-experiments-on-the-vote-to-choose-beta-core-rounds/15991
created_at: 2023-07-28T03:57:08.425Z
last_posted_at: 2023-08-16T17:09:18.923Z
posts_count: 7
views: 2927
like_count: 13
---

# Q.E.D. Program Update Two: Experiments on the vote to choose beta "core rounds"

<https://gov.gitcoin.co/t/q-e-d-program-update-two-experiments-on-the-vote-to-choose-beta-core-rounds/15991>
Joel_m | 2023-07-30 22:21:12 UTC | #1

Hi all! Joel from the Q.E.D. program here. In this post, I'll share some experiments we did to understand how past voting/ funding outcomes change when we use plural QF algorithms. 

*Also -- if you haven't checked it out yet, here's a reminder to check out our [polis conversation on QF!](https://pol.is/7hskapnxhm)*

For these experiments, we looked at the [snapshot quadratic vote](https://snapshot.org/#/gitcoingov.eth/proposal/0x3bebac743d1da8e72618dceb2c108d3cd71dddb10b8008456abcc87c2ca40992) held to determine which beta funding rounds would be "core rounds" (which received more support from Gitcoin) and which would be community led (more info [here](https://gov.gitcoin.co/t/shaping-the-new-gitcoin-grants-program-with-community-engagement/12811)). 

This is a cool dataset to look at because, unlike with normal funding rounds, it's easy to make an argument for what the outcome of this vote "should have been" in hindsight. That's because we now know how many donations each beta round got. If you believe that Gitcoin should directly support the rounds that draw the most attention/donations, then measuring the success of the snapshot vote is easy: you can go down the line of core rounds selected by the snapshot vote and ask: *"ok, did this round actually get much attention during beta?* If it did, then the snapshot vote did a good job at correctly predicting a popular round, but if not, the snapshot vote might've been sub-optimal. Likewise, if a round that didn't get a lot of attention in the snapshot vote ended up getting a lot of donations, that might've been another missed sub-optimality: perhaps that round should have been a core round. And most importantly, we can ask how changing the voting algorithm effects the quality of the results. 

(by the way -- my code is in [this notebook](https://colab.research.google.com/drive/19J5W2UQDK8RSMHD-CkA363KCmI6U2ylu?usp=sharing), for anyone interested)

**1. Comparing snapshot vote results with actual donation outcomes**

Like I said above, this snapshot vote is interesting because you can directly compare its results with the actual donation amounts the beta rounds recieved. Below is a graph showing, for each round, its share of the snapshot vote and what percent of donations it got in beta. When calculating the percent of donations, I first normalized by the size of the matching pool, since that felt like an extraneous factor that would also effect donation amounts. 

![image|651x491](upload://qTOy46MUA6tTLk87yRK02176Jvp.png)

As you can see, the snapshot vote was relatively close for some rounds (ETH Infrastructure and Climate) but fairly askew for others (OSS, DeSci, and ZK Tech). In fact, DeSci, which was not selected to be a core round in the snapshot vote, ended up getting more donations than ZK Tech, front-runner in the vote (after normalizing for the size of the matching pools).

In my last update, I talked about using a metric inspired by *Earth Mover Distance* (EMD) to compare these types of outcomes. Here, you can think of the EMD as the amount of "voting mass" that you'd need to move to get from one outcome to the other. For us, a lower EMD is better. The EMD between the snapshot vote and the actual beta round donations is ~0.44.

Now, we'll explore how the outcome would've changed if we had used some other QF variants instead. By the way -- despite the snapshot vote being called a vote, they actually used QF, not QV. So it's very easy to just plug in other QF algorithms instead.

**2. Using pairwise match**

Pairwise match was [first described by Vitalik](https://ethresear.ch/t/pairwise-coordination-subsidies-a-new-quadratic-funding-design/5553). The basic idea is that whenever you do QF, you can break down the matching funds into chunks, where each chunk corresponds to a unique pair of agents and depends *only* on the amounts that those two agents donated. So, if two agents seem to be colluding, you can take that pair's "chunk" of the matching funds and reduce its size. 

Here are the results when we use pairwise match on the voting data:

![image|636x491, 100%](upload://xMPyIALqgwxhdOzbjjkSV5L1O1j.png)
Here, the pairwise results are sandwiched in between the normal vote results and the actual donation results, so you can compare all three. Pairwise moves results in the right direction for five of the 10 rounds, and achieves an EMD of 0.42 -- so a bit better than the normal quadratic vote, which had an EMD of 0.44.  

By the way, you might notice the "(M = 0.01)" in the legend -- M is an internal parameter to pairwise match. You can see a graph comparing pairwise results for different values of M in the notebook I shared.

**3. Cluster Match via voting profiles**

The idea behind cluster match is to first group agents into clusters, and then put agents in the same cluster "under the same square root". In other words, each group of similar donors get treated as just one donor. I was curious about using this algorithm and defining clusters just based on the set of rounds someone voted for -- so, e.g., everyone who voted just for ETH Infra and Climate under the same square root, and so forth. The results are below.

![image|651x491](upload://o1QQViKYapMXL8k2YFNCURPGPvx.png)

Notably, this algorithm takes a large chunk of votes way from ZK Tech and gives the Web3 community round a good boost in the right direction. But ultimately, there are some issues with strategic behavior that would need to be ironed out before we could use cluster match in this way (feel free to ask for details below). In any case, it achieves an EMD of 0.38.

**4. Connection-Oriented Cluster Match via alpha round donations**

This is the algorithm that Glen Weyl, Erich and I [developed last year](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4311507). The basic idea is to put agents into clusters, like in cluster match, but then *also* do pairwise discounting between pairs of clusters. Here, we chose to cluster agents by their alpha round voting behavior (since the large majority of voters in this snapshot poll also donated in alpha). Instead of putting voters in just one cluster each, we let them be in multiple clusters, with a different strength depending on their donation behavior (i.e., someone who donated to 10 OSS projects and 1 climate projects would have a higher "weight" with the OSS cluster). Lastly, I experimented with some other technical tweaks that I'm happy to go into in the comments. The results are below:

![image|651x491](upload://xyzBiHTkvDhZsdI8zqp4FDOrehI.png)

This algorithm is very near and dear to me, but I have to admit that it doesn't look too hot here. Compared to the other implementation of Cluster Match discussed above, it only does better on ETH Infra. But, there are many parameters to tweak here, so I wouldn't totally count it out. This implementation of CO-CM achieves an EMD of ~0.42, similar to pairwise (although a little bit better, once you look past the second decimal place).

There is more I'd like to talk about, but I should wrap this post up for now. Let me know if you have any questions. Big thanks to @umarkhaneth for getting me high-quality data on alpha round donations, and big thanks to @borisdyakov for suggesting I take a look at this dataset!

-------------------------

DistributedDoge | 2023-07-30 04:57:33 UTC | #2

This is very interesting approach and very elegant notebook, I would like to read more, but it seems like paragraph (3) cuts off in the middle of a sentence:

[quote="Joel_m, post:1, topic:15991"]
 (feel free to ask for details below). In any case, it achieves an EMD of
[/quote]

I got two poorly formulated question: 

**1:** How does CO-CM (4) react to groups with differing numbers of donations? The scenario I am thinking of is two pairs of voters:
   - A and B that cast a single vote for the same grant.
   - C and D that make 99 similar votes. Then D makes one extra vote.

I think naive cluster profile (3) as described would penalize A/B while treating C/D as distinct voters? 

The behaviour I would find desirable is to penalize pair C/D more as such overlap is less likely to be result of random chance. 

**2:** Regarding strategy. I might be wrong here, but with current QF in grants sometimes winning move is not to play (project reaches matching cap before I even voted => my vote would carry 0 additional subsidy => bankroll money wait for next round). 

Is there ever a scenario under mechanism (2) and (4) where a winning move (i.e. one that increases net profit for project) could be to dimnish my donation to my true preference just so that collusion resistance penalizes me less? *Hm... a lot of people are donating only for Rotki so I will donate 99$ to true preference and 1$ to climate stuff just so that I am not lumped with those folks.*
.

-------------------------

Joel_m | 2023-07-30 22:44:23 UTC | #3

Thanks for pointing out the chopped word! That should be fixed now.

As to your two questions:

**1.** This is a great point. Naively clustering by donation profile is only really possible if you don't tell people you're going to do it before hand (or if you're not too worried about people strategizing). Otherwise, as you point out, it's easy for a colluding group to create a slate of slightly different donation profiles, which will let them all seem different to the system. But, if we decide that using donation profiles is an important avenue to explore, we can experiment with ways of making it more robust to the type of behavior you describe. 

**2.** I think the answer is probably yes for (2), but someone wouldn't differentiate themself too much by only giving $1 to a different project. But it gets complicated, because the more money someone gives to another project, the more that other project's matching amount will grow, which will then eat into the matching amount for the project that they actually like. For (4), the answer is definitely no because that algorithm uses alpha round donation behavior to do clustering, not snapshot vote behavior. In general, we're really interested in seeing what these clusting algorithms -- (3) and (4) -- do when you have them cluster on stamps instead of voting/donation behavior, and using alpha donation behavior was supposed to be a sort of stand-in for stamps (because you could imagine someone claiming a stamp certifying that they were, say, a big supporter of OSS projects, etc).

-------------------------

ale.k | 2023-08-03 15:48:12 UTC | #4

Loving to see the early side-by-sides - 

Just a thought, but I wonder if there might be some interesting reveals if you segment the data further beyond round?  For example, those voters who voted in more than 1 round; those voters who had an on-chain history exceeding 1 year or high average monthly transactions on mainnet - just some low hanging fruit on signals that might show some greater detail in behaviors of these groups.

Awesome work - looking forward to more learnings!

-------------------------

koday | 2023-08-04 14:51:47 UTC | #5

Thanks for sharing this analysis, it's super interesting to look at and digest!

My one thought - this seems like a great data set to use but I'm curious how each of the 4 methods you outlined would look if we completely excluded ZK Tech votes. On the surface this behavior seemed like airdrop farming or collusion that skewed the votes for that category, especially when you compare it to a) the number of grantees in that round and b) the number of donors/donations. 

There also were issues with this vote & Passport that meant quite a few people could not participate in time - myself included. I'm curious how many people tried to vote and couldn't, considering I tried multiple times over a span of a few days and was unable to. This is to say I think these results should be explored more, but I also think we could produce a much "better" data set to experiment on with these methods.

-------------------------

borisdyakov | 2023-08-09 19:05:19 UTC | #6

Just wanted to echo what @ale.k and @koday said here – super interesting stuff – and worth exploring a lot more if we ever decide to do another community vote to decide on core rounds :) it would be awesome to be able to use that data to test different ideas/models/hypotheses/etc

For the beta round selection, I know the DeSci community was eager to vote, but GR15 donors/DeSci supporters who didn't participate in the Alpha round probably weren't eligible as their passports would have been expired. 

Multi-round checkout in GS/Allo V2 would also provide a lot of interesting data. Due to high gas fees on Ethereum Mainnet during the Beta Round I think a lot of folks avoided supporting multiple rounds... but once this obstacle is gone we will probably have much richer data on cross-round support. Hopefully multi-round also means simultaneous multi-chain checkout too...

-------------------------

umarkhaneth | 2023-08-16 17:12:57 UTC | #7

Hey Joel!

This was a really interesting read. Contrasting the snapshot vote and grants rounds really shows just how different these outcomes were and I wonder why that is. It's possible they just appealed to two different audiences. For example the DeSci community did not participate much in snapshot but this analysis shows they took a larger share of the donations than one would expect based on the size of the matching pool. It's possible they're less involved/engaged in Gitcoin governance but care more about the grantees in the round. 

This really points to me that if we were to use a snapshot vote to pick core rounds again we'd have to do so differently and maybe we should take QF as governance more seriously. If there's strong community support for a featured round based on donations in the round then perhaps it should be a core round. 

I really like how you're contrasting different QF mechanisms to try and find which one delivers better results. It would be really interesting to see how the results vary by mechanism when zooming in on one round and asking if those results align with what we expect. 

For example, in the recent Citizens Round, the [results](https://gov.gitcoin.co/t/gitcoin-citizens-round-1-results/16302) were surprising. This was primarily a round for the Gitcoin community and in the initial proposal I called out examples of who I hoped this round would fund: 
![Screen Shot 2023-08-16 at 12.58.28 PM|690x105](upload://yvCBkQvTxUJel8IdMx4Vp3kz6nL.png)

Yet, my favorite grants and the favorites of many high-context Gitcoin contributors did not earn much of the matching pool. In the end, the top four projects in the round were all organizations rather than Citizens. We also found significant evidence that the round was attacked by a small army of airdrop farming robots. 

I'm wondering how different these results would be if we used a different mechanism. Instead of linear QF, how would pairwise matching, cluster matching, or connection-oriented cluster matching perform? Would the results be more in line with what we're expecting and resistant to possible sybil/bot attacks?

-------------------------
