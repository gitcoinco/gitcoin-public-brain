---
id: 9595
title: "Lifetime Gitcoin Grants Data Analysis and Hypothesis Testing"
slug: lifetime-gitcoin-grants-data-analysis-and-hypothesis-testing
category: open-discussion
url: https://gov.gitcoin.co/t/lifetime-gitcoin-grants-data-analysis-and-hypothesis-testing/9595
created_at: 2022-01-01T06:22:58.352Z
last_posted_at: 2023-10-17T04:22:31.157Z
posts_count: 10
views: 6411
like_count: 38
---

# Lifetime Gitcoin Grants Data Analysis and Hypothesis Testing

<https://gov.gitcoin.co/t/lifetime-gitcoin-grants-data-analysis-and-hypothesis-testing/9595>
Pfed-prog | 2022-05-28 15:39:01 UTC | #1

Lifetime Gitcoin Grants Data Analysis and Hypothesis Testing

This report is a submission for the Gitcoin Bounty: https://gitcoin.co/issue/gitcoinco/skunkworks/252/100027341.


# Summary
A drastic increase in the Gitcoin Matching Pools in Round 12 has not been close to any of the rounds historically. 
The Gitcoin Platform successfully catches opportunistic behaviour in changing grant to a larger matching pool. 
With the new matching pool strcuture in GR12 users have decided to not mention their region. North American grants have dominated the Gitcoin platform and Africa has been neglected.

*On the technical side:*
We have cleaned the dataset optimizing for the Gitcoin dataset and Gitcoin in particular. We have also provided an open-source code in Python that can be used for production.
 
# Introduction
To understand how we can use the data to maximize its utility for the community at large and for decision makers in Gitcoin community, first we have researched the Gitcoin forum posts and the Quadratic Formula.

The posts for Reference:
* https://gov.gitcoin.co/t/proposal-gitcoin-gr12-matching-pool-allocations/9007
* https://gov.gitcoin.co/t/grants-round-12-governance-brief/9495
* https://gov.gitcoin.co/t/gitcoin-round-11-matching-pool-allocations/8386/14
* https://hackmd.io/@bsci-gitcoin/HJdaK6yoY#

Following these posts we outlined the areas of research that could be explored with the given data:
* The distribution patterns in the Gitcoin Grants data, for example, correlations between crowdsourced funding + matching to regions, grant category.
* The effect of changes in matching pools structure prior to GR12 and some insight into the changes that came up with GR12 one pool.

We also provide an account of the peculiarities of the given data such as missing values.

## Structure of the report
First we provide an overview of the Gitcoin rounds data. Then, we deal with the technical side of working with data: filling in the missing values, correcting for artifacts and feature engineering.

The code is open-sourced and available on kaggle at

* EDA: https://www.kaggle.com/pavfedotov/gtc-bounty-eda
* Interactive Map: https://www.kaggle.com/pavfedotov/gtc-map
* Correlations and Modeling: https://www.kaggle.com/pavfedotov/gtc-distribution

We have also uploaded the dataset on kaggle at https://www.kaggle.com/pavfedotov/grallrounds

# Data Cleaning and exploratory data analysis
## Rounds 1-12 Matching Pools and pot sizes
In the rounds data we have noticed that besides the official Gitcoin Rounds data includes the rounds data of its partners. Therefore, as the title of the bounty states 12 rounds we left only GR data and the partners rounds counted in the dataset as the GR.

GR data has the most common name of a matching pool in the data is 'all' since Gitcoin Core team (rounds 1-5) and later in consultation with the Funders League (rounds 6-9) has made more centralised decisions on the matching relative to the current state of governance.
 
![Count of Rounds|690x398](upload://634l9XzYo0cT7gbgL71ODeK8D6H.png)

The second most common occurring round is Infra, Dapp and Community which took place from 7 to 11 round. Nft is the third most common value of the pot.

 
![newplot|690x325](upload://tFzeFGTTxjSjvbyeP9TjbEPt6ml.png)

One of the notable developments in the round 12 was diffusion of the previous structure of matching pools and a trajectory towards one large single pool. Hence, on the graph above we do not see the common categories in round 12. 
In the granular data we noticed that instead of the traditional matching pools that OG Gitcoin users likely got used to, the names have switched to "Uniswap", "Polygon", "ZkTech" among other names. To qualify for such pools the grants need to be in one of the 6 categories such as "dGov" or "dApp"  and co-operate with the partner.
The new grant structure also introduced the new pools such as "Longevity" and "Climate Change" that have stricter qualifying requirements.
In total in round 12 this led to the historically largest amount of unique grant pools - 9. In part due to the amount of partners and available matching funds.
![newplot (1)|690x325](upload://wkcG8Q0QpnSXTJ15IGBGoCEKiqK.png)
 

## Rounds 1-12 Granular data missing values
To begin with, we visualize the missing values to find interesting patterns:

 
![MSNO|690x276](upload://kIFw6nmINmXvT2M8KwThZiNR0or.png)

 
![MSNObar|690x287](upload://zjsYnFyR0NOJAHHe4MMXQ2w3ev4.png)


We can see that the column with the most missing values is crowdfund. On the more detailed analysis we find that rows with missing crowdfund values all contain zero unique contributors, which is very interesting. Some ideas on the underlying pattern: the owner of the grant contributing to the grant, error in data logging or a returning contributor.
 
![1|631x218](upload://miX0ozgDBI4iJuaTPnWF0FtIDz2.jpeg)

We also find that the rows that have nan for total have nan for crowdfund and therefore contain little useful information. In proportion its 15% of the total rows that we drop from the dataframe.
 
![2|313x111](upload://5RluMBaZWWm2POA1RnBG1GdCrBP.jpeg)


## Exploring Gitcoin Detection of opportunistic behaviour

Next, it was particularly interesting to explore the patterns among the unique grants across time.
After we cleaned the data we found that the number of unique grants is 1886.
Personally, I was really interested in exploring the adaptation behaviour in changing the grant region and category and how often that has occurred per grant_id.
To my surprise less than 0.1% of the grants have been involved in such behaviour that we know from the data. Besides, most of actions that changed region involved actually mentioning the region for the first time.
 
![3|293x285](upload://nyIFrWnX67jJukzxSlXFAJ1dQrh.jpeg)


In turn, the grant_id is also connected to the same category across time and Gitcoin has successfully disabled such opportunistic behaviour.

Nevertheless, We decided to test the hypothesis that Gitcoin historically enables changing the grant details if the owner creates similar grant with new details. We assumed that the same grant title might be connected to the same grants. The number of such grants is 44.
On more detailed analysis we evaluated the changed details and it appeared to not be connected to the gaming the system since none of the detailed in the dataset were changed.
Therefore, we are confident that Gitcoin has historically caught opportunistic behaviour in adapting the same grant for more favourable matching pool.

## Regions across time and Continent EDA
From the data, the most common region is none meaning that users in most of the cases decided not to mention the region out of the available options.
 
![4|566x273](upload://50gmeOfAOcNttgihGOKMWh23f6g.jpeg)

It is also interesting that none has coincided with the type of the round and whether there was a pool for a region. Notable that such grants received relatively low amount of matching funds, likely attributed to the Gitcoin penalizing this behaviour.
 
![newplot (2)|690x325](upload://nlClWfwxCXziunuPkw7jyoa1uvO.png)

We also find that the mean total raised funding per grant per round favours Oceania and North America and neglects Africa and Asia to some extent.
![5|213x117](upload://uc2ie5UUEskZKzkE0Ypw9WMF2I.jpeg)

![base (1)|690x345](upload://8bbYNwHQASPXHbYipLFIxzkgaeT.png)

In fact, by capita NA is a strong favourite in terms of the raised funding.

We have also build an interactive map available at https://www.kaggle.com/pavfedotov/gtc-map

Moreover we explore the interaction between matching and the total for category and region variables for Round 11.

In Round 11 the over-subsidized  region was Africa while  under-subsidized was Middle East.
![8|209x182](upload://rtmIKJEIVz7zrKLPVHqix7yt4BH.jpeg)

While for a category dGov was the most subsidized while dApp and Comms were not favoured by QF.
![9|216x126](upload://wJ9eI3wQlzxIcsdgWWXx7Bz0SDX.jpeg)

-------------------------

Pfed-prog | 2022-01-01 10:56:34 UTC | #2

# Correlations Analysis

We have further conducted correlations analysis and found relatively strong relationships between these variables:
![6|443x300](upload://loBk72yUEtpIWai0QPZJOqyzW0U.jpeg)

Interesting Findings:
There is negative low correlation between grant round and match_amount, meaning that as time passes the matching amount decreases
![7|385x104](upload://ldW2oajxH6LUreMnO24F8mkQlIX.jpeg)
Also a similar relationship between grant_id and match_amount. Since new grants have higher number, the new grants are likely to get lower funding.

For the observation with region none there is a negative somewhat mild correlation -0.35 with the number of unique contributors. For this region it is also notable that it has negative correlation of -.27 with total funding raised. However, very similar region undefined has a positive correlation of .17 to total.

The structured heatmap for the variables is as follows:
![MSNObar (1)|461x500](upload://exscI08fpEY0xyuoGQ4pNc1tyc1.png)

# Modeling

We modeled grouped by round and weighted by count of unique grants. We found that on weighted average a mean contribution of 1$ per grant would result into $660 total funding per average grant.
![10|546x88](upload://xrzyx10EXh4G3u8ruCNfEbHv6gh.jpeg)
![11|404x269](upload://zyepPXOK2GgFBomoXw5H1aga88s.jpeg)

In turn, when we add another parameter - average number of unique contributors per round, we get coefficients and results that demonstrate the value of a large amount of unique contributors and the crowdsourced funds:

![image|547x116](upload://9x890KXfUsqjD0ez2jFcrmD0d0V.png)

For instance, if only 1 person donates 1$ to each grant, the grant owners would get around 185$ per grant. But if 1000 people donate a sum that would be equal to .001$ to each available grant, an average total raised per grant would be around 3130$. 
In round 12 there were 882 such grants, hence each of the 1000 would  only need to spend 80 cents.

Next we group by region as well as round and weight by the number of unique grants. 
Since we found that mean_crowdfund is highly significant we will include dummies for each region except one to avoid bias. In addition we include the number of grant round to estimate the effect of the trend.

We find that the most penalized region is Africa followed by Middle East.
![image|589x406](upload://eAzCAcOBQ34y4D75QiVslf0lpd1.png)

### Synthetic Controls

The effect of the separating Africa in GR11 as its own matching pool.
![image|586x335](upload://xBiXXjRTbQmz8ItdBbVmoZ0QBJB.png)

The initial effect of the policy seems to have an immediate positive impact on the Africa in GR 11, but a large negative effect in round 12.

-------------------------

DisruptionJoe | 2022-01-03 21:09:39 UTC | #3

Really great work here! I'm loving lawrence idea to package up all the best insights and continue to deliver the analysis each round

-------------------------

Sirlupinwatson | 2022-01-03 23:53:18 UTC | #4

Yes, nice work @Pfed-prog! 

To a large extent on the correlation analysis + the modeling part. 
It could be great to have a cloud clustering of different mapping as well but this is just an addon.

-------------------------

Pfed-prog | 2022-01-04 09:35:20 UTC | #5

@Sirlupinwatson Do you mean adapt to Gitcoin pipeline? I am pretty sure that i've accomplished exactly what was possible with the given data. I think there is a misunderstanding on how hard is actually to clean this data. Personally, I would prefer to not work with similar Gitcoin dataset in the future. But I definitely made life easier for further applications.

-------------------------

Pfed-prog | 2022-01-04 09:52:41 UTC | #6

@DisruptionJoe I would prefer not to be inlcluded in the meta-report. If my prize depends on the inclusion in the meta-report, please, do not send it to me.

-------------------------

Sirlupinwatson | 2022-01-04 14:52:32 UTC | #7

No, all I am saying is that you made a great analysis. And I like the second part (Correlation + modeling)

-------------------------

cemgundogan | 2022-01-04 16:56:57 UTC | #8

Thank you very much for this unique analysis!

-------------------------

Pfed-prog | 2022-01-04 19:44:36 UTC | #9

Really great to get such a positive response from a policy analysis expert. Means a lot, cheers.

-------------------------

mixmore | 2023-10-17 04:22:31 UTC | #10

Thank you for sharing this great effort.

-------------------------
