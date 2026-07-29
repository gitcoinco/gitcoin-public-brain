---
id: 11927
title: "Decentralized social graph as an oracle powered by the wisdom of the crowd for the era of Plurality"
slug: decentralized-social-graph-as-an-oracle-powered-by-the-wisdom-of-the-crowd-for-the-era-of-plurality
category: open-discussion
url: https://gov.gitcoin.co/t/decentralized-social-graph-as-an-oracle-powered-by-the-wisdom-of-the-crowd-for-the-era-of-plurality/11927
created_at: 2022-11-13T01:11:34.629Z
last_posted_at: 2022-12-21T05:19:17.915Z
posts_count: 5
views: 5180
like_count: 10
---

# Decentralized social graph as an oracle powered by the wisdom of the crowd for the era of Plurality

<https://gov.gitcoin.co/t/decentralized-social-graph-as-an-oracle-powered-by-the-wisdom-of-the-crowd-for-the-era-of-plurality/11927>
tkgshn | 2022-11-13 01:13:03 UTC | #1

Aura is a countermeasure against Sybil attacks, but the only other weakness of Quadratic Funding, resistance to collusion, is currently [Pairwise coordination subsidies](https://ethresear.ch/t/pairwise-coordination-subsidies-a-new-quadratic-funding-design/5553) by Vitalik.

Others, such as [How to Attack and Defend Quadratic Funding](https://medium.com/block-science/how-to-attack-and-defend-quadratic-funding-a10f0152f069) There is also a pattern of using data science, led by BlockScience, as shown in , but I propose a new layer.

We have published a draft of a white paper on a protocol called **DeCartography** that outputs data from the Plurality social graph as an oracle.

A longer version can be read here
https://docs.google.com/document/d/1i4rPj1qlvV9RhfP9jwaI_ESEMZ-7tvBLbftDdOmEWWk/edit#


Here is a summary

This prevents collusion, or perhaps it would be better to call it "Plurality Quadratic Funding.
 **Precisely, it reduces voting power from similar clusters.**

This ideology is based on "Plurality" which coordinates across the following differences

* [How Soulbound Tokens Can Make Gitcoin Grants More Pluralistic](https://gov.gitcoin.co/t/how-soulbound-tokens-can-make-gitcoin-grants-more-pluralistic/10077)
* [50 actually independent thinkers are worth more than 1000 NPCs who all consume the same media and vote the same way](https://twitter.com/VitalikButerin/status/1580313964067508224?s=20&t=hx_luOMMPz6k808SXzmGog)
* [Regenerative Society](https://docs.google.com/presentation/d/1NY17vw1fOFgp9WR40c0hsDkTnafSGkEPT2Pmemr4Rdo/edit#slide=id.g134bebec90a_1_106)
* https://www.radicalxchange.org/media/blog/why-i-am-a-pluralist/

I don't know if the concept of "distance" is used in the current Gitcoin Grants for Pairwise coordination subsidies, but by establishing a contrasting position with "services that automatically create social graphs from transactions," the Gitcoin FDD team is able to create a social graph that is more personalized, more relevant to the needs of the community, and more effective. I think we can provide data to Gitcoin's FDD team.


[details="service that automatically creates social graphs from transactions"]
* Gitcoin(BlockScience)
* Bubblemaps
* Breadcrumbs
* LensProtocol(?)
[/details]

Simply put, we ask people to answer "Is this wallet address similar?" by comparing two transactions ⭕️ or ❌.

To draw this into a two-dimensional map like a social graph, when n people vote on each simple question, each opinion is tied to an n-dimensional value. By clustering them, the Assumpution can be dropped into a single social graph.

**Generate the coordinates of the consensus on the Assumption**.
  Assumption" here refers to the decision "Is this wallet similar (similar community)?
In this case, there are only two options, Yes or No, but I think this alone will prevent some degree of collusion.

![image|690x447](upload://ayLZe4v3HO9OFI3w1wVqOvMwtOj.jpeg)
*The image is an earlier prototype, with the tags as choices. This is how the two addresses are lined up, with the question, "Are these two similar?" would be a good question to ask*.

If more than 51% of the respondents give the same answer, we will simply use that answer as the decision. Actual adjustments would need to be made. For Civil Attack, we of course recommend using Gitcoin Passport.

This is because, as you may know if you are familiar with consensus systems as well as PoS, I believe it will settle at **Schelling Point**.

In this case, I expect that the Assumpution will settle on "roughly like this" and when they are separated, we can create coordinates with some accuracy
* [Nash Equilibria and Schelling Points](https://www.lesswrong.com/posts/yJfBzcDL9fBHJfZ6P/nash-equilibria-and-schelling-points)
* https://blog.ethereum.org/2014/03/28/schellingcoin-a-minimal-trust-universal-data-feed

As for aggregation, I wonder if **Pol.is** could adopt a method to help find consensus.
* https://compdemocracy.org/algorithms/
* https://blog.pol.is/pol-is-in-taiwan-da7570d372b5
* ![image|525x500](upload://1yFuc89VkCV99bB14huKjRNqI2I.png)
* **If n people interpret an opinion, n dimensional values are tied to the opinion (clustering with dimensionality reduction)**
* ![image|498x500](upload://upMQH8sjms3OqXxFWyo7b5oxXDa.png)
* >The machine learning that's done, in pol.is, is done in real-time, and we do clustering, just like you would have in a recommender engine, Except that pol.is visualizes the groups


**The data that DeCartography can provide as Oracle should look something like this**!

* ![image|690x266](upload://4kHhc5V8qlkX6nnUvn5Xxn9y6oU.jpeg)

As for what attributes people are donating with Gitcoin Grants, [Towards a Pluralism Passport Built from DeSoc Legos](https://docs.google.com/presentation/u/1/d/1eINBNP9Ikbs1Melr_g4KDjeNSjAsc-NPyBz4XPo9L8k/edit#slide=id.g13c284ad96c_0_1), but we may be able to map this.

Then we could incorporate the concept of Social Distance.

This may be a promise of Quadratic Land, but I think many people may not understand this Plurality Quadratic Funding at first, so it would be good to have an educational site like this.
![image|552x396](upload://xvBaNSElfP7tACO3RFwAOtM2yTZ.png)

**Concepts like this Relation Oracle, and Weight Oracle could become the new Plurality identity.**

Thanks to [DisruptionJoe](https://twitter.com/DisruptionJoe), [_sgtn](https://twitter.com/_sgtn) for their reviews.

-------------------------

DisruptionJoe | 2022-11-18 13:23:32 UTC | #2

I love this paper and your description. This really gets to the heart of the often overlooked part of the Decentralized Society paper by @GlenWeyl Puja & @vbuterin . Without worrying about SBTs & VCs, this paper directly deals with the k coefficient used to dampen collusion. Better stated, it encourages outgroup collaboration. 

[quote="tkgshn, post:1, topic:11927"]
I don’t know if the concept of “distance” is used in the current Gitcoin Grants for Pairwise coordination subsidies, but by establishing a contrasting position with “services that automatically create social graphs from transactions,” the Gitcoin FDD team is able to create a social graph that is more personalized, more relevant to the needs of the community, and more effective. I think we can provide data to Gitcoin’s FDD team.
[/quote]

This is really great work. It is only the second serious attempt at deriving a k value which I have seen next to @erich work on the subject. 

I really hope this project can receive great funding as a grant and perhaps from the DAO (via FDD) directly. The more I look at it, the more I realize that as open source software it will definitely be a public good. I don't know what immediate business model might fund it, so it is likely up to us. 

I would love to know if the software can be used only with inputs from publicly available data such as onchain donations made in Gitcoin rounds and/or passport stamps?

-------------------------

tkgshn | 2022-11-19 01:44:13 UTC | #3

Thank you so much @DisruptionJoe . I'd like to make a new era.

I've been researching [Ethelo](https://gov.gitcoin.co/t/hello-supermodular-xyz-fka-web3studio/11211/2?u=tkgshn) and the FDD team's move recently. I think this so-called way of working is like a PoC with Gitcoin, and I think that DeCartography could proceed in basically the same case.

* https://gia-testing.ethelo.net/page/welcome-to-the-gia
* https://docs.google.com/document/d/1bFfmDK0ZQ9ij4B9mYWPyAGbHjAhlyTFtrkuCS_vrokI/edit


At first, we are thinking of providing our oracle in a way that only FDD can use it because it can be like the GraphQL API (even centralized).
What kind of data structures can be added to the k-value (which we call the "QF function")? For example, [the "Humanity" of a Gitcoin Passport should have a QF whose voting power increases or decreases depending on the linked accounts](https://go.gitcoin.co/blog/a-community-based-roadmap-for-sybil-detection-across-web-3).
We hypothesize that given a user A and the project they are donating to, the oracle interface could easily adjust voting power by returning "how far away from the existing donors this user is in the cluster (deviation)".

What might we do
First, use the API to get the list of voters from the previous Gitcoin Grants
Add them to the PoC target address group and plot them to the most intermediate point once they have been rated by (say) 10 or more different people)
This allows one account to be answered "is this address similar or not" from at least 10 different interpretations with a Yes, No, or None and plotted on a 2-dimensional graph

-------------------------

tkgshn | 2022-11-19 01:47:21 UTC | #4

and here is a "WTF IS DeCartography Quadratic Funding"'s prototype.
https://gyazo.com/8b113ac16d48430e3d299ad7fdbf0015

-------------------------

tkgshn | 2022-12-21 05:19:17 UTC | #5

**update**: MVP for worker's is here
https://gyazo.com/7b759607d84ae3380dd6a50cb3fdb6c3

-------------------------
