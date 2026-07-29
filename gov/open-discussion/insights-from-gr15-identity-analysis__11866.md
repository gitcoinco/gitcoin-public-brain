---
id: 11866
title: "Insights from GR15 Identity analysis"
slug: insights-from-gr15-identity-analysis
category: open-discussion
url: https://gov.gitcoin.co/t/insights-from-gr15-identity-analysis/11866
created_at: 2022-11-07T11:37:24.090Z
last_posted_at: 2022-11-12T00:31:01.639Z
posts_count: 5
views: 3064
like_count: 15
---

# Insights from GR15 Identity analysis

<https://gov.gitcoin.co/t/insights-from-gr15-identity-analysis/11866>
j-cook | 2022-11-07 11:42:34 UTC | #1


There are three facets to Sybil defense - humans, algorithms and passports. Passport aims to proactively assess evidence of personhood, vetting individuals before they participate in a grant round. Algorithms are used to retrospectively identify Sybil behaviours for individuals already participating in the round. Humans are there to resolve disputes and provide subjective input where necessary, as well as setting thresholds and round eligibility requirements.

Each of these approaches ultimately aim to distinguish users into two categories: Sybil and non-Sybil. Real, honest users have high value to the Gitcoin ecosystem and should also have high trust scores because they exhibit clear non-Sybil behaviours in advance of, and during, a grant round. For example, they might have participated in many activities that can be represented in the form of passport stamps and may have reputation or credentials that can carry over from previous rounds. Sybils, on the other hand, have low (or even negative) value to the Gitcoin ecosystem and, assuming the system works well, should have low apparent trust score. However, there are two substantial challenges: 

1) Sybil's sometimes put considerable time, money and effort into increasing their apparent trust score without also adding value to the ecosystem. These create Type 1 errors (false negative) in the Sybil defenses. 

2) Honest users who are new to Gitcoin or new to Web3 more generally may lack the credentialks that give them high trust scores, despite being non-Sybil. These create Type 2 (false positive) errors in the Sybil defenses. 
 
From the Sybil defense perspective, newbies and airdrop farmers/"cheap" Sybils probably look quite similar, while Web3 native contributors and sophisticated attackers probably look similar. This is a complex problem because raising the bar for proof-of-personhood to mitigate attacks also risks eliminating new users, while lowering the bar of personhood to enable new users makes the system easier to attack. The top level challenge is to appropriately balance between inclusivity and security.

## Key takeaways

- Gitcoin Passport alone is not yet a robust Sybil Defense mechanism, but pairing it with Sybil scoring shows great potential.

- Creating Sybil scoring "legos" and allowing grant owners and round managers to apply them to sub-communities could be a big value-add to current Sybil defense.



## Learning from data

We might hypothesize that:

- Developing more sophisticated algorithms will lead to more effective squelching of attackers. However, this runs the risk of creating an arms race since, in an open protocol, the algorithms can be known and gamed by attackers, necessitating constant updates. 

- Introducing more passport stamps or weighting high-signal stamps more strongly in the Sybil defenses will eliminate more adversarial users from a grant round. However, this will also come at the cost of silencing more new users. 

- Introducing more humans-in-the-loop to ake subjective decisions will help reduce both type-1 and type-2 errors, but this is expensive, slow and vulnerable to bribery/corruption. 
 
To test these hypotheses, we can interrogate GR15 data.

### GR15 passport data

20,055 users used Gitcoin passport in GR15. 87% of those users achieved a trust score greater than 100%, meaning their contributions were boosted in the matching pool. Passport users overall preferred to use Web2 stamps (Twitter, Facebook, Github, Discord, Google, LinkedIn) compared to Web3 stamps (ENS, POAP, BrightId etc). The median user collected 6 individual stamps. There was a very steep dropoff in frequency of stamps beyond initial verification for the Web2 platforms, though. For example, almost all passports had a verified Twitter account, but less than half had >10 tweets, less than 1/3 had >100 followers, >1/10 had >1000 followers and ~1/100 had >5000 followers. For Github, 100% of users had an account, but <1/10 of users had 5 or more repositories. Almost all users had a Facebook account, but less than 2/5 had one with a profile picture.

<img align="left" width="350" height="350" src="upload://aEPziCjYUfeDAF1wEl5Kw7yDQsu.png">

<img align="left" width="350" height="350" src="upload://1fX03EpkS8UQBKO0y1j3XdSrU95.png">
 
<br></br>

While it is not surprising to have fewer users meeting more stringent requirements, the drop off is unexpectedly sharp and might signify large numbers of potentially adversarial users gaming the system by only aiming to meeting the basic standards that enable to them to avoid being squelched. It is known, for example, that accounts on these platforms can be bought and sold in bulk on black markets. Accounts meeting basic requirements are likely to be cheaper and more readily available than more fully-featured versions. Alternatively, it might be that users simply don't know that we want them to maximise their stamps, rather than just collecting the minimum viable set. Either way, the data indicate that the web2 stamps might only convey a relatively weak signal for Sybil defense. 

On the other hand, Gitcoin data had a much more gradual drop off rate, indicating the stamp design works as intended, with increasing effort required to obtain increasingly prestigious stamps. This suggests these stamps might be weighted more heavily in future rounds to improve proactive Sybil defense.

Despite the high adoption of Gitcoin Passport and the promising results for the efficacy of Web3 stamps, we observed a low correlation between the trust bonus arising from passport stamps and the users labelled Sybil by FDDs algorithms (see bar chart below). If passport stamps were a viable standalone Sybil defense mechanism then we would expect a steady decrease in the number of squelched accounts as the trust bonus increases, but this is not what we observe. This is also reinforced by the observation that 58% of the users that were squelched in GR15 had Gitcoin  Passports.

<br></br>
![](upload://oN3Yvf6oWSNpOGBVKw5pxpTGmg8.png)
<br></br>

The user's APU scores can boost the signal in some cases. The APU score is an Accumulated Partitioned Uniqueness value calculated from the number of stamps in a passport and the uniqueness of their combination. The relationship between APU score and squelching needs some further investigation because there was a condition in place that meant no-one could *lose* trust bonus during a round which mayhave skewed the data by allowing some users with below-median APU scores to achieve the maximum +150% trust bonus.

Ultimately, though, the unlock comes from combining passport with algorithmic scoring. This approach gives a much stronger set of signals. 

In addition, staking $GTC was a very strong signal for honesty in these analyses, but the result is probably skewed by the fact that folks holding $GTC *before* it becomes used to enhance a user's trust score are probably high-integrity users anyway, whereas in future rounds buying and staking $GTC will be known to be beneficial for increasing a user's influence. Future attackers might buy and stake $GTC specifically to legitimize them so they can launch an attack.

For example, if we assert *a priori* that **new users** are likely to have minimal on-chain activity, a single wallet address, a unique username and a unique ip address, while an **airdrop farmer** is likely to have more on-chain activity such as POAP and NFT ownership, multiple wallet addresses, nonsense usernames and duplicate ip-addresses. Classifying users by these criteria and then looking at their behaviours reveals some strong signals:

- new users fund climate, desci, diversity and education topics

- web3 natives tend to fund crypto advocacy, ethereum infrastructure and open source software.

- Airdrop farmers tend to focus on DeFi


![](upload://nuLPWxy3SXaru7yMxIZRHdoeAB.png)
![](upload://gPCbKYJqA6RW8T63OwlXhYNy42d.png)



This makes sense because lots of users might onboard to Web3 specifically to contribute to causes they already care about, such as climate and DEI, whereas farmers are primarily interested in receiving an aridrop in the form of some token that is most likely to come from DeFi. This implies that calibrating climate, DeSci and DEI more leniently might be appropriate in order to include the large population of new users attracted to those rounds, while DeFi needs to be calibrated strictly to defend against attackers and farmers. This is the kind of calibration that can be done by a round manager and then fine tuning done at the grant level in the new protocol based grants system.


## How to better identify noobs and farmers

In the previous section we made some assumptions about how new users and airdrop farmers are likely to behave. However, those hypotheses were presented in qualitative, subjective terms that don't lend themselves very well to detection algorithms. To algorithmically classify users into identity bins we need some quantitative measures in the parameter space of the Sybil detection algorithms that map to those qualitative behaviours so that they can be used as filtering measures. To determine which parameters might be diagnostic for farmers vs noobs, we plotted the scores from each metric for users known to be noobs and farmers and looked to see which showed distinct separation between the groups (see figure below). The three metrics that appear to be useful in distinguishing these two identities are the intersectionality score, donor DNA distance and shared IP address count. Farmers and noobs both spread across the full range of SAD scores, had similar APU scores and had a lot of crossover in Levenshtein distances. 

![](upload://r4TtQY541IFbA1RZsTruPH8ttkf.png)

From these data we can identify the following set of parameters that encode the identities of new users and farmers:

Measure                 |   Noob           | Farmer        |
|---------------------- |------------------|---------------|
|Intersectionality score| 0                | >= 1          |
|DonorDNADistance       | 0.1 < x < 0.25   | <= 0.1        |
|IPSharedCount          | 0                | >= 3          |

This information could be used by round managers to algorithmically filter users on entry to a grant round in a way that usually welcomes new users and blocks airdrop farmers. The simplest form of filtering would simply be to gate entry to users that matched the Noob criteria, squelching those that match the farmer criteria. In this context, gating means disallowing participation by reducing the influence of a squelched account to zero as a consequence of the scoring legos, as opposed to "hard-gating" which explicitly prevents a user from accessing the platform, e.g. a blacklist.


## Sybil defense legos

GR15 demonstrated that no single metric on its own was able to distinguish Sybils from honest users. The plot below shows large crossover between the squelched and non-squelched users for six individual parameters.

![](upload://dcM1ZUcAvw592aIc2u8rwT8EyrK.png)


However, these metrics become more powerful when they are combined together. They can be thought of as Sybil-scoring legos - not very useful on their own but able to be connected and stacked in creative ways to form more useful super-structures. One example is breaking the total user population into classes and checking whether the aforementioned legos are better able to distinguish between specific subpopulations rather than simply distinguishing users that may have been squelched for a diverse set of reasons. In FDD we have two reference populations known as Thor and Loki representing known non-Sybil and Sybil users respectively. The Thor and Loki users are represented by the green and pink lines on the plot below.

![](upload://koHGrdTzLm2LodVECN0FjLEcL54.jpeg)

The honest (Thor) users have very low LevDistance, Intersectionality and DNADistance scores and high SAD and IPSharedRatio scores, while the Loki users are the opposite. Squelched users and users without Gitcoin passports tend to be more similar to Loki than Thor, although the signal is dampened across all metrics, presumably due to large variation across the populations. Users that have stake GTC ("self stakers") have a profile much more closely resembling Thor. This indicates high potential for stacking Sybil scoring metrics to better identify honest users from Sybils.


## Sybil-scoring-as-a-service

The utility of these Sybil-scoring legos can be levelled up by providing them via a web app. Users can then tweak parameters, analyse their own community of users and configure their own defenses. A prototype Sybil-scoring-as-a-servioce dashboard is shown below:

![](upload://6XTxHHSOiOvGetLD9uHbPCh2pVN.png)


In this dashboard, a grant owner can analyse individual users or groups of users using all the different metrics and simulate the effects of imposing certain eligibility criteria (e.g. how many users are squelched when I set the following thresholds...). Additional pages could be used to view different combinations of legos.

## Summary

Analysis of GR15 showed that Gitcoin Passport on its own was not a strong diagnostic tool for Sybils. Part of this may be because users don't realize that they are supposed to maximize their passport stamps, as opposed to meeting a set of minimal viable requirements. However, creating Sybil-scoring legos and pairing them to Gitcoin Passports holds great promise for better Sybil detection. Building services that allow grant owners and round managers to easily apply those legos to their own subcommunities of users could be a major unlock in a composability-focused grants protocol. Staking $GTC is a very strong signal for honesty in our pilot studies, but this needs to be confirmed with a larger population of users in case the result is skewed in favour of behaviours associated with current $GTC holders. People may well buy $GTC specifically to stake and launch a Sybil attack.

-------------------------

DisruptionJoe | 2022-11-09 17:24:04 UTC | #2

To clarify, I will break this down due to having heard from multiple individuals who have interpreted this in a way that is slightly off from it’s intention.

[quote="j-cook, post:1, topic:11866"]
Analysis of GR15 showed that Gitcoin Passport on its own was not a strong diagnostic tool for Sybils. Part of this may be because users don’t realize that they are supposed to maximize their passport stamps, as opposed to meeting a set of minimal viable requirements. However, creating Sybil-scoring legos and pairing them to Gitcoin Passports holds great promise for better Sybil detection.
[/quote]

Put a large emphasis on “WAS” in the first sentence. This was the first round using the Passport with the new APU algorithm. For a starting point it was not unreasonable to think that uniqueness and effort would be good measures to prevent sybil attack. We learned that sybil attackers see enough value in attacking that they are willing to put the time and effort into unique activities to earn higher trust bonus.

This is GREAT news! We learned!

We were able to use the REACTIVE layer (sybil scoring legos) to squelch those users who got past the PREVENTATIVE layer of sybil defense. This information will give us insights as to which stamps are most vunerable to attack.

We can use this information to introduce weights and biases to either the stamps themselves, or the combinations of stamps which APU scores. We can call this “Cool APU”.

While the Passport did not do a great job of gating the round from Sybils in this first attempt, it did give us excellent data to help us win the infinite game of sybil defense! This information will be used to better PREVENT sybils in the future using passport.

Learnings from future rounds in addition to FDD building new legos which detect sybil behaviors native to design partner use cases will help Passport to become a quality sybil PREVENTION tool for all of web 3.

Holistically, Sybil Resistance is an infinite & evolutionary game. It is a three legged stool requiring consistent updating of scoring and tooling. The legs of the stool include Prevention, Detection, and Reaction. Passport will soon provide both the best tool for preventative sybil defense AND an optional shared data layer for ethical observability & reproducibility of algorithmic policy decisions used in Reactive sybil defense.

-------------------------

kishoraditya | 2022-11-10 14:33:03 UTC | #3

As @DisruptionJoe mentioned,  apt to the point that we are learning how stamps will start gating Sybil from entering the system

**Food for thought**: Even if passport prevented thousands of Sybil efforts, we don't know as they didn't enter the system, and IMO, now estimating that would be a vanity thing for us as well GPC from the adoption front, it would somewhat turn into qualitative understanding in the later stages when the protocol sees the peak of its growth rate.

And since in a way to be inclusive towards all, giving the benefit of the doubt in a way, we are not "enforcing" passport, it is always an option to have a reputation in the system. I am thinking it this way, after 15 rounds we are getting a vague understanding of who are sybils and with stamps, we are moving towards understanding how to identify them faster and better.
![image|690x401](upload://bXO9nvrpJZGU6aoxruTRIvuKnfo.png)

-------------------------

ccerv1 | 2022-11-10 16:04:26 UTC | #4

I agree fully with this take. 
To go deeper, I would say GR15 revealed two areas where more work is required to close the gap: 
- **Product side** : we're not confident that users understood we wanted them to collect as many stamps as possible (many likely thought the objective was to collect the minimum stamps needed to achieve a 150% trust bonus). The UI needs to surface this better. There's also some interesting design space to make stamp collecting feel fun, like Gitcoin did with QF.
- **Analysis side** : determining which combinations of stamps offer the strong proof of personhood for a given a community. We have anecdotal evidence that certain stamps will be strong signals for certain communities (eg, GitPOAPs for OSS), but we don't have robust data to back it up (yet).

-------------------------

php | 2022-11-12 00:31:01 UTC | #5

Thank you for sharing this! I know my friend who is new to gitcoin is not used to do brightID (somewhat intimidating), or they might don't have twitter account (non-English speaking background), new github as  not tech....

I know such new account will have low weight, assuming they donate 'normal' will they be noobs?

Also I wonder if there are analysis on the matching pool?

-------------------------
