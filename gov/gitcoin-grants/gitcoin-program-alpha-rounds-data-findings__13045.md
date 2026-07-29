---
id: 13045
title: "Gitcoin Program Alpha Rounds Data Findings"
slug: gitcoin-program-alpha-rounds-data-findings
category: gitcoin-grants
url: https://gov.gitcoin.co/t/gitcoin-program-alpha-rounds-data-findings/13045
created_at: 2023-02-23T02:09:14.800Z
last_posted_at: 2023-05-08T13:01:52.490Z
posts_count: 5
views: 3254
like_count: 31
---

# Gitcoin Program Alpha Rounds Data Findings

<https://gov.gitcoin.co/t/gitcoin-program-alpha-rounds-data-findings/13045>
umarkhaneth | 2023-02-23 03:43:23 UTC | #1

# Gitcoin Alpha Rounds Analysis

The latest alpha program rounds are the first Gitcoin program rounds on the new protocol. They are the closest thing we had to a full GR in S16. All of the grants in these three rounds participated in GR15. The rounds are Open Source Software, Ethereum Infrastructure, and Climate Solutions. 

**Special thanks to @koday for his detailed thoughts on this post. Be sure to check out his [post-op write up](https://gov.gitcoin.co/t/gitcoin-program-alpha-round-post-op-writeup/13043) on the alpha rounds.** 

# Round Results (preliminary):

This data is still being thoroughly checked and will change by small amounts. In addition, this data has not been checked for sybil donations. Since sybil donations mainly are a problem for matching calculations the analysis will focus on crowd behavior. 

More detailed round result information can be found on the dune dashboards for the round:

* [All Rounds Summary](https://dune.com/umarkhaneth/gitcoin-alpha-all-rounds)
* [Open Source Software](https://dune.com/umarkhaneth/gitcoin-alpha-open-source-software)
* [Ethereum Infrastructure](https://dune.com/umarkhaneth/gitcoin-alpha-eth-infra)
* [Climate Solutions](https://dune.com/umarkhaneth/gitcoin-alpha-climate-solutions)


![Screen Shot 2023-02-06 at 8.08.29 PM|663x500](upload://lZ4TeyJ2SU7TGYpBGdjJDUAJMCL.png)


Eth Infra and Climate Solutions raised similar amounts (with Eth Infra slightly ahead) while OSS blasted the roof off. 

### [Open Source Software](https://dune.com/queries/1972207)


![Screen Shot 2023-02-06 at 6.57.37 PM|690x298](upload://9HuJl8qrkmHpPZn7CUXnSnrwgcB.png)
![Screen Shot 2023-02-06 at 6.57.56 PM|690x270](upload://vYbkgZAP0lXT0Bt3bn95Dz23TOw.png)



The OSS round had the biggest winners of the quarter with multiple grants netting over $40k in donations. Notice there is a long tail of grants raising much less than the top few. The top 5 grants (all well-known projects) ended up raising over 50% of all crowdfunding. This is not a bad thing. Grants should not raise equal amounts but instead amounts proportional to how much of the community values them. In this case, it seems likely that popular projects such as DeFi Llama (which aggregates data across DeFi protocols in extremely user-friendly dashboards) and Lenster (Web3 social media built on top of Lens Protocol) are used by lots of people and rose to the top. 

It’s worth noticing that Optinames and MintBot have the same donation values above. This is because they use the same wallet address, which is also what the dune query uses to group donations by grant. It is not however what matching calculations will be based on so these will still be treated as two separate grants.

## [Ethereum Infrastructure](https://dune.com/queries/1972581)

![Screen Shot 2023-02-06 at 8.24.09 PM|690x296](upload://ioeVt5Rej88iV1FFUvl7zMli270.png)
![Screen Shot 2023-02-06 at 8.24.25 PM|690x298](upload://26jgP0Bd2W1IAzDLxqmVqDZUbhv.png)



The shape of the grant distribution is similar in the Eth Infra round as it was in the OSS round but more balanced. **Each project in the Eth Infra round raised at least $1k which is a considerable win.** 

The top few projects in the round include Chainlist, L2Beat, Optimism DAppNode Package, and some familiar favorites like EthStaker (helping expand and decentralizing the staking community), Ethers.JS (open-source library for building on Ethereum), and rotki (open source privacy portfolio). 
Chainlist was unfamiliar to me. It’s run by the DeFiLlama team and allows users to connect their wallet to any number of chains. It seems like a useful application to allow users to easily add more networks to their wallet and make bridging assets easier. 

L2Beat is another website whose prominent feature is a data dashboard. L2Beat focuses on aggregating data on Ethereum scaling and providing users an easy view into the state of various layer 2 protocols, including Total Value Locked, rollup technology, validation method, and risk. 

Optimism DappNode Package’s high performance is initially surprising. The project’s github hasn’t been updated since December, has 10 stars, and 2 forks. 

In contrast, ethers.js is two rungs down the ladder with 6.3k stars, 1.4k forks, and 274k dependent repositories. 

We had an issue early on in the round where projects always appeared in the same order for everyone on grant explorer. This was quickly fixed by the product team. It’s possible Optimism DappNode Package was one of the ones near the top during this brief period of time and rode the wave. 

Pulling the data for donations to this grant by hour, this doesn’t appear to be the case. The grant got a lot of donations late in the round when the issue had been fixed. 

![Screen Shot 2023-02-06 at 8.50.00 PM|690x180](upload://scXqWxI5J7EarPJOFtd7rzEjwre.png)


The reason for its popularity is unclear. However, it may be that the community is simply excited about the potential of this project to bring together two popular ecosystems: Optimism and DappNode. There are a few factors that could be stacking to contribute to Optimism DappNode Package grants popularity in this round, including:

- Optimism and DappNode are both well-known and well-loved names in the ecosystem so this grant may be gathering support from both their communities.
- The round took place right around the time Optimism announced their ‘Bedrock’ upgrade which also caused the OP price to increase

### [Climate Solutions](https://dune.com/queries/1972582)

![Screen Shot 2023-02-06 at 8.52.34 PM|690x291](upload://4wBuga1JM83ION5qn2ViFWuYwxR.png)
![Screen Shot 2023-02-06 at 8.52.47 PM|690x283](upload://38bBboVKsfaFP2z7FKZFaT4ZhF3.png)


The climate solutions round has a similar long tail to the other rounds with a couple of top projects raising much more from the crowd than its counterparts. In this case, ReFi Spring was boosted by a couple of big $5k donations. This project provides grant funding to folks around the world looking to host ReFi events in their area. 

Just below ReFi Spring in donations, ReFiDAO x Commons Stack has the most unique donors. This is a collaboration of two popular projects that are assisting ReFi founders and onboarding more members into the ReFi movement.

Solarpunk Nomads performed better than expected (by the grant owners) in this round and was boosted by appearing near the top of the screen in the early part of the round. The number of donations prior to January 19th are noticeably higher than after for this grant. 

![Screen Shot 2023-02-06 at 8.59.08 PM|690x175](upload://re91XWV6wbn9hFQLdYyuc1NxUYr.png)


Overall, this collection of rounds has similar trends to cGrants: a few top, popular grants often raise most of the crowdfunding with a long tail of grants who raise smaller amounts. This is combatted by creating more matching pools so that top projects can’t dominate projects in emerging sectors. For example, if the OSS projects had been in the same round as climate grants, they would have dominated and been able to claim large chunks of the matching fund. However, by having separate matching pools, climate grants will be able to raise significant funding. This can also be seen in GR15’s DeSci round where the entire round crowdfunded less than $60k but the $500k matching pool meant projects were given a significant funding boost and several of them have been able to significantly ramp up their development. Situations like this are arguably where QF shines the most: large matching pools that can invigorate an emerging ecosystem and informed community members who select the most deserving projects. 

# Comparing the Alpha Rounds to Each Other: OSS has more supporters, but Climate supporters have a stronger preference

The biggest takeaway here is the stellar performance of the Open Source Software round. While its matching pool was the same size as the other rounds, it had more grantees and many more donations. Further, each grantee brought in more donations than any other round. 

![Screen Shot 2023-02-06 at 5.06.32 PM|690x419](upload://rbmCu5dpNXYG4DKKGAvtqLegAqd.png)


On the other hand, if we look at donations by donor, then the average donor contribution is smaller in the OSS round and strongest in the climate round.  

![Screen Shot 2023-02-06 at 5.06.48 PM|690x420](upload://pieGiw6b6FuERBCXUDkycWkSU00.png)


One way to interpret the above two graphs is to say:

- OSS appeals to a much broader section of our community than Eth Infra which appeals to a broader section of our community than Climate Solutions
- Of the people who support each of these categories, the climate supporters have the strongest preference demonstrated by their higher donation amounts.
    - OSS has **a lot** of fans, but Climate’s fans are more passionate

It’s worth taking a moment to caveat the above analysis by re-iterating that this is not looking at passport data or removing Sybils. Early indications point to the OSS round being hit hardest by Sybils but even if Sybils make up ~20% of all donations, OSS would still be far and away in the lead of overall donations. 

# Comparing to GR15

By design, the season 16 alpha rounds are much smaller than GR15. Comparing the overall numbers here isn’t really a fair apples-to-apples comparison. I’ll focus on more specific numbers, but I still want to share a quick sense of the high-level size difference.

- GR15 had 3x more matching funds
- GR15 had 2.5x the number of donations
- GR15 had 1.5x the number of unique donors
- GR15 had 10x the number of grantees

It’s worth noting that curating the round to top grantees made up for some of the reduction in size and it was still fairly popular. Prior analysis has shown that top grantees drive most of the donors and donations. 

## Round Timing

With an entirely new user experience, it’s worth focusing on how this affected community members. We can compare the percentage of total donations that came in each day over the course of the rounds. 

![Screen Shot 2023-02-06 at 5.21.02 PM|690x422](upload://qvzZjjx02sh4QzUphDq8Crb10NU.png)


Note: GR15 was one day longer than the Alpha Rounds.

Overall, the donation pattern looks similar with slightly more donations coming in early during GR15. The reasons for this are unclear but are being explored. Some potential reasons might be due to more marketing in advance of GR15, the rhythmic consistency of quarterly rounds, a new and unfamiliar interface, or bugs with Gitcoin Passport. There is a significant uptick in the favor of the Alpha Rounds on the final day of the round. This may have been partly driven by [this tweet about Gitcoin Passport](https://twitter.com/gitcoin/status/1620475869826514944?cxt=HHwWgIDQwfmNi_0sAAAA). 

# Donating to Multiple Rounds

On cGrants, it was easy to select projects in multiple rounds and checkout once. However, on the new protocol, rounds are separated and a user would have to select projects and checkout multiple times in order to donate to multiple rounds. Do community members accept the higher UX friction and check out on multiple rounds?

![Screen Shot 2023-02-06 at 9.16.41 PM|690x423](upload://iGKISTohpc5EQCzLZM4HHJBEFD0.png)


This data indicates that many of them do. Most notably, the percent of community members who donated to both Climate and Eth Infra projects actually increased significantly from GR15. 

On the other hand, the percent of community members donating to both Climate and OSS or Eth Infra and OSS decreased significantly. This may be because the relatively larger number of community members to the OSS round includes many people who are not individually as strongly passionate about supporting other sections of the Ethereum ecosystem. We can think of them as ‘single-issue voters.’

It’s also notable that the overlap between Climate and OSS decreased more than the overlap between Eth Infra and OSS. The large number of community members who came to the cGrants platform to support OSS may have happened to see a climate grant or two and add it to their cart while browsing. Now, this type of serendipitous interaction is impossible unless community members go out of their way to browse other rounds. 

Caveat: the OSS comparison from GR15 is drawn from the GR15 main pool. To prevent inflating overlap numbers, grants which were in Eth Infra or Climate were removed from the gr15 main pool while doing this analysis. This allows for a comparison of what the overlap would have been in GR15 if grants were only in one of the three rounds. 

# Community Retention: 15k returning donors!

With the cut over from cGrants to the protocol, one significant question facing the DAO is: how much of the community will come with us? 

![Screen Shot 2023-02-06 at 9.43.15 PM|690x408](upload://xxq0QwIFkazHnKp217jpA8SF3xi.png)


A similar number of community members returned for our alpha round as returned for GR15, with only a slight dip. **We seem to be hovering around 15k returning donors which is tremendous!** 

We can also look at the overall distribution of returning vs new donors in each round (note that for this analysis sybil detection is of increased importance and sybils have not yet been filtered from this data). 

![Screen Shot 2023-02-06 at 10.04.35 PM|690x409](upload://q4KxEBCYrDeoz74lvLfHndyFZc8.png)


![Screen Shot 2023-02-06 at 10.04.57 PM|690x416](upload://eYRns7kWgcpF3fjfADEaScHKpTy.png)


The majority of community members donating to the Eth Infra and OSS rounds have previously donated on cGrants. These numbers will likely go up after sybil detection is completed.

The UNICEF round was smaller with ~11k unique donors but also had ~55% of the donors returning from cGrants. Among the 45% of new donors, about 20% of them returned for the Alpha trifecta. They are not included as ‘returning’ in the graphs above which focus on cGrants but are worth mentioning here. The community is on track toward continued growth. 

Note: The underlying query is currently being refined to allow for an edge case where someone donates from a Gnosis Safe -- those donations (less than 1% of all donations) aren't included here.

**Some lingering questions:**

- Communities vary by the issue they support. How can we inspire similar passionate energy as climate citizens in other rounds? On the other hand, how can we expand the number of people who care about the climate?
- Retaining existing community members is arguably easier and more important to our continued success than attracting new ones. How can we increase the number of community members who stick around from round to round from 20% to 80%?
- All three rounds here had equivalently sized matching pools. Climate and Eth Infra each have an approximately 1:6 crowdfunding to matching ratio while OSS has a 3:2 crowdfunding to matching ratio. What is a good ratio for us to aim for with QF rounds?
- What else should we be trying to answer from the data? Please share your ideas for future analysis

-------------------------

Ministry888 | 2023-02-28 16:49:02 UTC | #2

Thank you for the article, although the metrics and publicly available and compiled a very high quality

-------------------------

ZER8 | 2023-03-12 20:25:12 UTC | #3

Wow, congrats to everyone who made this into a reality. The alpha round has some very impressive stats even when compared to GR15. This is a huge signal that shows how much people love, trust and want to participate in the Gitcoin rounds :robot: :evergreen_tree:

-------------------------

jonas | 2023-05-04 13:18:17 UTC | #4

@umarkhaneth More of a question. But are you doing a similar post for the Beta rounds? 

Love this so much, adds so much context for everyone.

-------------------------

jp295 | 2023-05-08 13:01:52 UTC | #11

very good questions :clap: :clap: :clap:, would love to see more community engage to get these problems solved

-------------------------
