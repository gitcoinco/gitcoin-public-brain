---
id: 18705
title: "[Nerd post] Updates to Cluster Mapping / Matching!"
slug: nerd-post-updates-to-cluster-mapping-matching
category: gitcoin-grants
url: https://gov.gitcoin.co/t/nerd-post-updates-to-cluster-mapping-matching/18705
created_at: 2024-04-30T21:31:17.262Z
last_posted_at: 2024-05-04T13:14:19.091Z
posts_count: 4
views: 4041
like_count: 27
---

# [Nerd post] Updates to Cluster Mapping / Matching!

<https://gov.gitcoin.co/t/nerd-post-updates-to-cluster-mapping-matching/18705>
Joel_m | 2024-04-30 21:40:38 UTC | #1

Hi all,

I want to briefly share an update to the algorithm we use to calculate QF results. This is a minor tweak, but I like sharing this type of thing with the community because transparency/ community consent for the algorithms we run is is good. I also always love feedback, positive or negative.

Before I go further, [you can find the code here.](https://github.com/Jmiller4/qf-variants) The function COCM (with the default inputs) is what I'll be explaining in this post. 

COCM (Connection Oriented Cluster Match) works in three steps. 
1. First, it takes in data about "clusters", which are just different (possibly overlapping) groups of users. You could generate cluster data from POAPs, twitter follower lists, or even the donation records (where if someone donates to project X, they're put in project X's cluster). Users can also have "weights" in a cluster, denoting how strongly they belong to it. For example, you could use github repositories as clusters, where if I make *n* pull requests to that repository, I have a weight of *n* in that repository's cluster. In general, round operators can choose what cluster data to use (or they can not use COCM at all, of course).
2. COCM calculates "similarity scores" between each user and each cluster. 
3. Finally, COCM runs QF, but then attenuates each project's funding if many of its donors are similar according to the scores calculated in step 2.  

Step 2 is what we'll focus on here. First, here's how we used to calculate similarity scores. Lets call the user U and call the cluster X. If a U is in X, their similarity score to X is 1. Otherwise, we look at all the other clusters that U is in, and look at all the people in all of those clusters. Then we ask, how many of *those* people are in X? We use that fraction as the similarity score.

The issue with this method is that we don't use any of that juicy weight information I mentioned above. Let's say user U is in cluster Y, and everybody else in Y is also in X, with a really high weight. If we gave all those people a really low weight instead, it wouldn't change the similarity score between U and X. But shouldn't it? 

So our new way of calculating similarity scores essentially does exactly that. You can think of it as an adaptation of the old method but with a weighted average, instead of an unweighted average. 

You can also think of the new method as an analysis of a [Markov process](https://en.wikipedia.org/wiki/Markov_chain), like what Google uses in their PageRank algorithm. We can think of a graph of all users and all clusters, where directed edges from users to clusters (and vice versa) are weighted according to that user's weight in that cluster, and normalized so that all outgoing edges sum to 1 (thus forming a probability distribution). Then, we can start at user U's node and randomly jump to a cluster that U is in according to the probabilities on their outgoing edges. Then we can randomly jump from that cluster to a user, with probabilities proportional to each user's weight in that cluster. Then we can jump to another cluster from whatever user we wind up at. 

Now, here's a question: what's the probability that after all of that jumping, we wound up at cluster X? If user U is closely connected to X via many intermediate clusters and donors with high weights, the probability will be high. If U isn't closely connected to X, the probability will be low. So this probability is precisely what we use for the similarity score between U and X. 

This new method of calculating similarity scores really improved the sybil resistance of the algorithm. All of the charts in @umarkhaneth 's [recent post](https://gov.gitcoin.co/t/our-sybil-resistance-strategy-for-gg20/18524/1) were calculated with this new version of COCM.
.
That's all for now. Please let me know if you have any questions or feedback!

-------------------------

owocki | 2024-05-02 23:31:31 UTC | #2

I'm really exceptionally proud to see that new & powerful flavors of collusion-resistence are being pioneered at Gitcoin.  Keep up the great work @Joel_m !

-------------------------

M0nkeyFl0wer | 2024-05-03 14:29:53 UTC | #3

Not only is this work dope the name of this post is exemplary 🤓

-------------------------

Sov | 2024-05-04 13:14:19 UTC | #4

We love to see it.  Awesome work @Joel_m

-------------------------
