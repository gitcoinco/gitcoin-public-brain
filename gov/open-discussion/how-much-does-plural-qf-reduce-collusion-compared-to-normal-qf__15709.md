---
id: 15709
title: "How Much Does Plural QF Reduce Collusion Compared to Normal QF?"
slug: how-much-does-plural-qf-reduce-collusion-compared-to-normal-qf
category: open-discussion
url: https://gov.gitcoin.co/t/how-much-does-plural-qf-reduce-collusion-compared-to-normal-qf/15709
created_at: 2023-07-06T10:23:57.521Z
last_posted_at: 2023-07-12T18:51:25.247Z
posts_count: 6
views: 2880
like_count: 17
---

# How Much Does Plural QF Reduce Collusion Compared to Normal QF?

<https://gov.gitcoin.co/t/how-much-does-plural-qf-reduce-collusion-compared-to-normal-qf/15709>
tkgshn | 2023-07-06 10:23:57 UTC | #1

In our efforts to mitigate collusion and make QF more effective, we've been exploring the concept of Plural QF. To illustrate this, let's consider a comparison between Plural QF and Normal QF.

## The Setup
Let's consider 
- **2 projects** with 
- **7 contributors** each
- and a **$100 matching pool**

## The Results
Under Normal QF, our projects received:
- Project #1: $140
- Project #2: $129

Under Plural QF, our projects received:
- Project #1: $154
- Project #2: $115

Let's break it down.

---

### Normal QF
![image|690x106](upload://1s3fQT1pBYQCCigQP12M45SguSd.png)

Contributors donated to Project #1 as follows: 5, 10, 0, 20, 0, 10, 50. This resulted in:
- Funded amount: $95.00
- Matched amount: $45.31
- Total: $140.31

![image|690x101](upload://aWoQJBKF9BsZX0j6RDfpHr4uB1L.png)

Similarly, Project #2 received donations as follows: 5, 15, 5, 5, 20, 10, 15. This resulted in:
- Funded amount: $75.00
- Matched amount: $54.69
- Total: $129.69

---

### Plural QF
We simulated a social graph for the same number of contributors. Using the COCM model and running a Python script, we obtained the following results:

assume Social Graph 
![image|690x408](upload://wTsmhTRFxD9TpF4f8ll2tNElnyE.png)

`$ python3 multipleproject.py cocm "[[0], [1, 2], [2, 3, 4, 5], [5, 6]]" "[[50, 5], [5, 15], [10, 5], [0, 5], [20, 20], [0, 10], [10, 15]]"`
→`[289.7424515457382, 199.92969686897504]`
calcurated with https://github.com/tkgshn/plural-qf/blob/main/multipleproject.py


Project #1:
- Funded amount: $95.00
- Matched amount: $59 (calculated using the COCM model)
- Total: $154

Project #2:
- Funded amount: $75.00
- Matched amount: $40 (calculated using the COCM model)
- Total: $115

### More Info

![image|690x472](upload://i2qb1HcFqIkPMmc23ML0lGAN4cE.jpeg)

For a closer look at our simulations and calculations, check out 
- simulation code: https://github.com/tkgshn/plural-qf/blob/main/differentamount_Simulation.py
- more: https://scrapbox.io/tkgshn/how_to_implement_wtfipluralqf_update#647930e009c5f200008d3de4

To understand how Plural QF could influence individual contributors, consider this: **if you're in a good social position like `Agent0`, increasing your contribution amount can have more impact than a similar increase from an agent in a less advantageous social position.**

### Comparison with RetroPGF and GR11 (Infra round)

![image|511x500](upload://fnEL6potl0ZxG7FyAU94aCBidwV.png)

it's compared our findings with the data from Optimism's Retro Funding Round 1. [Vitalik Buterin](https://vitalik.ca/general/2021/11/16/retro1.html) observed that the retro round had less variance, the winners were more well-known projects, and there was more focus on infrastructure as opposed to user-facing projects. Here are our visualizations of these comparisons:

VitalikButerin said below in https://vitalik.ca/general/2021/11/16/retro1.html
>It is my own (admittedly highly subjective) opinion that the retro round winner selection is somewhat higher quality
  The retro round was low variance
  The retro round winners are more well-known projects
  The retro round focused more on infrastructure, the Gitcoin round more on more user-facing projects


https://docs.google.com/spreadsheets/d/10nOQ_umnNpS1Ef_y0Jt9yNdv8UevEo_9PJt7D8phJMw/edit?usp=sharing

---

maybe DeCartography's future is likes this
![image|545x500](upload://DcsyFsUCyvABji9kCJYkCVXoNW.png)
https://www.figma.com/file/zvbu9R8rBKrbovGXLuKSGG/Untitled?type=design&node-id=0-1&mode=design&t=LcMRwtOWxIwOphyZ-0

Let's continue the conversation around improving QF through Plural QF. Your thoughts and insights are always welcome.

-------------------------

Joel_m | 2023-07-07 00:12:16 UTC | #2

Hey @tkgshn, great stuff! As you move forward with the COCM algorithm, I would recommend playing with the amount that contributions are attenuated. 

To be clear about what I'm talking about (and in case anyone else is interested), if you look at the formula for COCM in the ["Beyond Collusion Resistance" whitepaper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4311507)  -- equation (16) at the top of page 15 -- there's this function *K(i,h)*. Here *i* is an agent and *h* is a group. In the paper, *K(i,h)* either returns agent *i* 's contribution (if agent *i* and group *h* have nothing to do with each other), or the root of *i* 's contribution (if there's even a small social connection between *i* and *h*).

So overall *K(i,h)* is a pretty simple function, and that's because when we were writing the paper we really just wanted something that would satisfy our definition of collusion resistance. But I think that in practice, one can make *K* more sensitive to the specifics of *i* 's relationship to *h* -- for example, it could smoothly grade between the two options I mentioned above, instead of just returning one or the other, based on how socially close agent *i* is to group *h*. I think that being more delicate here might produce better outcomes.

-------------------------

koday | 2023-07-06 21:27:09 UTC | #3

This is really cool, thanks for sharing! I'm excited to see more experiments and simulations with pluralistic QF and it'd be awesome if we can eventually integrate some form of it into Grants Stack. I do have a few questions though:

[quote="tkgshn, post:1, topic:15709"]
To understand how Plural QF could influence individual contributors, consider this: **if you’re in a good social position like `Agent0`, increasing your contribution amount can have more impact than a similar increase from an agent in a less advantageous social position.**
[/quote]

In this example, do all agents know their social position or plurality "score" before they donate? I.e. the first donor knows nothing, but the 2nd donor knows where they stand in relation to the 1st, and the 100th donor knows how they relate to the first 99. Is it more advantageous to keep this data open and what are the game-theoretical impacts of doing so? Or should this be hidden and only used to calculate matching amounts after the round has ended?

Also - is there enough on-chain data to make pluralistic QF more impactful than regular QF? Or do we need to add off-chain data to build an adequate base-level social graph? In this example it seems like the more active a wallet has been in different ecosystems, the more likely they are to have their match attenuated compared to a wallet that's active in only 1 ecosystem. To me, this doesn't seem like a meaningful way to scale donation matching. 

CC @Joel_m in case you have any thoughts on the above.

-------------------------

tkgshn | 2023-07-07 01:41:27 UTC | #4

Firstly, let me express my appreciation for your thoughtful feedback and comments.

@Joel_m , thank you so much for your insight! I must confess that the mathematical portion of the "Beyond Collusion" paper was a bit of a challenge for me. I was mainly referring to the code posted on GitHub, so it is incredibly valuable to receive feedback directly from the author. Your suggestion on making the function `K` more sensitive to the specifics of `i`'s relationship to `h` is intriguing, and I agree that the coefficients in Plural QF are worth fine-tuning. Given that DeCartography has a stand-alone function to generate a social graph and is **loosely coupled with the QF formula itself**, I believe that iterative experimentation and simulation is the best approach to adjust the formula. I intend to continue sharing this process publicly for ongoing discussion.

-------------------------

tkgshn | 2023-07-07 02:05:23 UTC | #5

As I mentioned in my response to Joel's comment, DeCartography serves as an oracle providing a social graph, and it is loosely coupled with the QF formula itself. Therefore, in answer to your question, I believe it depends on **when Gitcoin (or QF) decides to perform the calculation**.

In my previous [post](https://gov.gitcoin.co/t/proof-of-concept-utilizing-decartography-for-plural-qf-enabling-social-identity-based-collaboration-amidst-differences/15698), I mentioned that what DeCartography intends to do in its initial experiment is:

- Analyze the data from GR15, where project funding has already been distributed (precisely, only the unique wallet addresses of participants are needed to generate a social graph by DeCartography)
- After that, DeCartography will return the analyzed data to Gitcoin, and we plan to calculate the results of GR15 using regular QF and the results of GR15 as Plural QF simulated by combining the social layer
- We then plan to report these results in the forum and hope to adjust various coefficients accordingly.

---
[quote="koday, post:3, topic:15709"]
In this example, do all agents know their social position or plurality “score” before they donate?
[/quote]

So, in this case, all agents as participants in the GR Round would **not be able to know** their social position or plurality “score” in advance.

---

[quote="koday, post:3, topic:15709"]
Also - is there enough on-chain data to make pluralistic QF more impactful than regular QF?
[/quote]

I had a call about this with @erich yesterday. In his presentation on "[Plural Funding at Funding the Commons](https://youtu.be/RM7UFpSemjA?t=1594)", he mentioned using [EAS](https://attest.sh/), etc., for Plural QF. 
![image|690x381, 50%](upload://c9gb6fipwSTXiaqMzQp2fgxFsI.jpeg)
![image|690x383, 50%](upload://o2LXAwG2C3KuCJbhPhVO4dTrOxl.jpeg)
![image|690x381, 50%](upload://aakrIlK91ODKrGczr4GOU4JtfvP.jpeg)


However, I personally feel that the number of attestations/certification as attendees / POAP distributed in the first place is **STILL** small. 

Therefore, DeCartography intentionally does not "analyze data" but generates a social graph based on intuitive classification ([Schelling Point](https://medium.com/witnet/on-oracles-and-schelling-points-2a1807c29b73)) by crowd workers. Hence, DeCartography holds a unique position among Relational Oracles, and even if EAS grows or decides to acquire off-chain data, I think it is possible to integrate them and locate them in the social identity layer of Plural QF.

---
at last, I really appreciate your feedback to build.
more info (almost still WIP) is here
- https://decartography.github.io/docs/
- https://drive.google.com/file/d/1Q-OTIH_dBJ9a8gxJWsQm9qCHxd9_MolQ/view?usp=sharing

-------------------------

Joel_m | 2023-07-12 18:51:25 UTC | #6

[quote="koday, post:3, topic:15709"]
In this example, do all agents know their social position or plurality “score” before they donate? I.e. the first donor knows nothing, but the 2nd donor knows where they stand in relation to the 1st, and the 100th donor knows how they relate to the first 99. Is it more advantageous to keep this data open and what are the game-theoretical impacts of doing so? Or should this be hidden and only used to calculate matching amounts after the round has ended?

Also - is there enough on-chain data to make pluralistic QF more impactful than regular QF? Or do we need to add off-chain data to build an adequate base-level social graph? In this example it seems like the more active a wallet has been in different ecosystems, the more likely they are to have their match attenuated compared to a wallet that’s active in only 1 ecosystem. To me, this doesn’t seem like a meaningful way to scale donation matching.
[/quote]

Hey @koday sorry for the late response! But yes, these are two important points to consider. Aside from what Taka has said, I want to offer my own thoughts, since we may diverge in some ways.

As for the question of whether there's enough data: I think it is possible to get enough data to do something meaningful, and the idea that @erich and I have had is to use passport stamps as identity markers, rather than using on-chain events. We hope that by looking at a few well-chosen "special" stamps that are relevant to the funding round in question, you can get good results. 

As for openness of data, and whether or not that creates an opportunity for strategizing -- you're right that if everyone can see the data that CO-CM uses, they can strategize, which we probably don't want. In particular, under CO-CM, there can be situations where an agent's funding impact would go down if they claimed a new identity marker. So agents might be shy away from claiming certain markers. But we definitely want to encourage agents to claim all the identity markers they can, especially since these markers are really passport stamps (and from the passport perspective, more stamps are always good since they mean you're less likely to be a Sybil). So, I'm tweaking the algorithm so that it always rewards agents for claiming more stamps/ identity markers. It probably won't have the same mathematical properties as the old algorithm, but I think the tradeoff will be worth it in this context.

-------------------------
