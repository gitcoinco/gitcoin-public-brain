---
id: 17469
title: "Concepts, PoCs, and Early Results for Personalized Grantee Recommendations"
slug: concepts-pocs-and-early-results-for-personalized-grantee-recommendations
category: open-discussion
url: https://gov.gitcoin.co/t/concepts-pocs-and-early-results-for-personalized-grantee-recommendations/17469
created_at: 2024-01-23T12:22:58.093Z
last_posted_at: 2024-04-09T17:33:46.905Z
posts_count: 7
views: 3655
like_count: 24
---

# Concepts, PoCs, and Early Results for Personalized Grantee Recommendations

<https://gov.gitcoin.co/t/concepts-pocs-and-early-results-for-personalized-grantee-recommendations/17469>
rohit | 2024-01-23 12:22:58 UTC | #1

tl;dr Over 4 different rounds, [GrantsScope](http://grantsscope.xyz/) (more [context](https://gov.gitcoin.co/t/gg18-grantee-discovery-using-llm-enabled-conversations/16192)) has helped donors discover grantees through LLM-assisted conversations. As the next iteration in the quest to reduce information asymmetry for donors, the post explores two options to drive grantee recommendations in future Gitcoin Grants Rounds.

### Ask
GrantsScope started as a bunch of Python scripts I used to make my decisions about contributions to Gitcoin Grants. As it found relevance and support in the community, I would love to incorporate your feedback on which direction the effort should evolve next. All feedback on the relevance and utility of the following features is welcome!

### Motivation
While the use of LLMs to explore projects through questions and conversations is impactful in a variety of ways to find out about value-aligned grantees (latest examples [here](https://x.com/RohitMalekar/status/1726662662803820789?s=20), [here](https://x.com/RohitMalekar/status/1727055572686782631?s=20), and [here](https://x.com/RohitMalekar/status/1727420457379676430?s=20)), the onus to ask the relevant question is still on the user.

>  **How might we further reduce the donor's cognitive load when helping them discover grantees and the work they care about for rounds with a large (>100) number of participants?**

### OPTION 1: Personalized recommendations by tapping into historical donation data
**Approach:** Find the most supported projects by people who contribute to projects you most support
1. Lookup user's favorite projects based on who they contributed the most over the last year
2. Tag all the voters who also supported the projects the user supported the most
3. Find out what other projects this cluster of community contributed to that the user hasn't donated for
4. Sort these projects based on dollars contributed and the number of votes by the user's cluster of community

**Working Prototype:** Enter your ETH address (you don't need to sign anything) to view your personalized recommendations - https://2023-wrapped-gitcoin.streamlit.app/
**Code:** https://github.com/rohitmalekar/2023wrapped
**Sample:** These are personalized recommendations for me based on how contributors who also support my favorite projects have donated through 2023.

<div align="center">

![Screenshot 2024-01-23 at 4.38.31 PM|561x500, 50%](upload://msnX7qtApHz1SVKTRp0fo2O91AX.jpeg)
</div>

<div align="center">

![Screenshot 2024-01-23 at 4.38.41 PM|552x500, 50%](upload://veFh6gIwUEQ7yayRCCCCIoAVCyC.jpeg)
</div>

**Next Steps:** Deploy a round-specific personalized recommendation list for GG20 donors

**Limitations:**
- Since the recommendations are based on existing signals in data, they amplify existing biases too
- Does not factor impact in sorting recommendations

### OPTION 2: Interactive visualization to discover similar projects based on clustering
**Approach:** One approach to exclude existing biases in contribution data for discovering new grantees is to limit the scope of data discovery to the grantee-submitted project description (and, in the future, impact). By classifying the nature of work and clustering related projects, donors can visually navigate through a crowded round based on their preferences.

As a donor, you can then overlay your investments on such a visual and choose to:
1. Double down on investments in specific domains that you care about by discovering peer projects to teams you are already aware of
2. Spread your funds across different clusters for a more diversified strategy

**Code:** For a sample set of Climate Round grantees https://github.com/rohitmalekar/grantee-clustering

**Samples:** Here are some algorithmically determined organic groupings of projects (a) saving water bodies, (b) protecting forests, (c) utilizing solar power, respectively

<div align="center">

![TSNE 0|690x361, 75%](upload://lpXKke22z9cxraMSdSTV1WbXjQN.png)
</div>
<div align="center">

![TSNE 1|690x361, 75%](upload://iEbO5xh4zoRMc1F2KVyAW2twrgx.png)
</div>
<div align="center">

![TSNE 3|690x361, 75%](upload://qd5YmxWNV13xNpCRkgCdYrMm4P4.png)
</div>

**Next Steps:**
- Abstract the complexity of the clustering algorithm for an intuitive interactive user experience
- Fine-tune the clustering method to suit the data and context

**Limitations:**
- Clustering cannot be 100% automated and requires human-in-the-loop to finalize results
- Does not factor impact yet. However, once impact data can be captured in a structured manner across grantees, performing clustering based on verified impact is worth a shot in the future.

-------------------------

umarkhaneth | 2024-01-25 13:18:20 UTC | #2

This is lit! 

Grantee discovery remains an unsolved problem and I dig your prototype for solving it. 

I tried out some of your builds here and wanted to offer reflections from my experience using them for when you take these to the next level. 



For option 1 I think this really shined in helping me discover lesser-known projects that I may like. In particular, Common Stack, Praise, and Giveth seemed like great recommendations for me. I agree with this limitation you point out. 
[quote="rohit, post:1, topic:17469"]
Since the recommendations are based on existing signals in data, they amplify existing biases too
[/quote]
Some of my top recommendations were for projects I know are extremely popular/common in the data (like Jediswap, L2Beat, DefiLlama). I wonder how you may account for the extremely-popular and skew the results toward the more niche projects.

I would love to try using this during a live round to help me discover projects to donate to. 

For option 2, I'm a fan of HDBSCAN clustering and like your approach to clustering on project descriptions. I could see the results from running this being most useful for grantees to find others working on similar problems to collaborate with. 

But tbh I'm not sure I completely appreciate the visualization. I liked just receiving a list of projects to check out (in option 1) and the graphs aren't doing too much for me.

As a grantee, it could be cool to view a list of similar projects and for each project also maybe provide a 'distance score' based on the result of the description embeddings.

BTW if we were to A/B test the recommendations from option 1 and option 2, my personal guess is option 1 would be more likely to convert. Curious what you think

-------------------------

rohit | 2024-01-25 18:10:25 UTC | #3

[quote="umarkhaneth, post:2, topic:17469"]
I wonder how you may account for the extremely-popular and skew the results toward the more niche projects.
[/quote]

My hunch is that the popular projects are propping up also because the analysis is on the entirety of the 2023 data. A round-specific recommendation list (by Eth Infra, Climate etc.) should make it more interesting.

Also, there are multiple ways to bell the recommendation logic, and it will need some experimentation. For example, the default flow is below, and with other alternative levers in brackets.

1. Lookup my favorite projects (only in this round | over the last 6 months | by # of votes only, not amount)
2. Collate all voters who also supported these projects (pick the top X percentile by donation amount | pick the top X percentile by number of votes | pick only first-time voters)
3. Sort and recommend other projects supported by these voters (filter only first-time grantees | exclude if already leading in top 10)

Now you can get niche project recommendations to an inquiry like:
- *"In Climate Round, which first-time grantees are being most supported by veteran voters with donation history similar to mine?"*
- *"Which projects outside of the top 10 list in web3 community round are getting most support by first-time voters with voting preferences similar to mine*?" 

We will have to pick a couple of options that resonate most without overloading the user with too many choices.

[quote="umarkhaneth, post:2, topic:17469"]
I liked just receiving a list of projects to check out (in option 1) and the graphs aren’t doing too much for me.
[/quote]

This makes a lot of sense (thinking about Amazon and Netflix).

[quote="umarkhaneth, post:2, topic:17469"]
BTW if we were to A/B test the recommendations from option 1 and option 2, my personal guess is option 1 would be more likely to convert. Curious what you think
[/quote]

Yes, I think so, too. Option 2 requires a predisposition, similar to the cognitive effort involved in the conversation with LLM. Might be relevant for a smaller set of advanced users. An ideal workflow would be to populate recommendations, make tweaks, bulk checkout, and be done.

-------------------------

krrisis | 2024-01-29 19:36:57 UTC | #4

This is sooo epic - just tagging @meglister for visibility. 

Hopefully at some point we can get a link to useful 'add-ons' like these on grants stack (for the ones that are not integrated in GS ofc)

In any case agree, grant discoverability is key, and this is great work to be retroactively rewarded.

-------------------------

buildingweb4 | 2024-01-30 06:58:37 UTC | #5

This is really great! Integrating impact data would be definitely a game changer since that's one aspect of QF that's not as robust.
But regarding your Option 1 question on recommendations; I was wondering if its also possible to integrate into the algorithm a check on confirmation bias. In other words, instead of only surfacing projects based on what you already like, what your friends/people with similar interests support, etc. why not actually do the opposite; from time to time surface a project that is outside of your "comfort zone." That may help you (and the algorithm) get a better sense of the landscape of projects out there, and will prevent "echo chambers" from forming within the wider community.

-------------------------

rohit | 2024-01-30 08:28:12 UTC | #6

[quote="buildingweb4, post:5, topic:17469"]
why not actually do the opposite; from time to time surface a project that is outside of your “comfort zone.”
[/quote]

Love the anti-pattern here! Will run a few tests on this. Thanks for the suggestion!

-------------------------

rohit | 2024-04-09 17:33:46 UTC | #7

**Update:** Both methods have been deployed in the app below to offer a seamless experience for one-click personalized grantee recommendations for the Citizens Retro Round #3.

https://gitcoin-cr3.streamlit.app/ 

The tool will help you:
1. Re-discover the grantees you've supported in the past
2. Explore grantees backed by the community who also champion your favorite projects on Gitcoin
3. Introduce you to grantees similar to the list in #1 and #2 using clustering algorithms

-------------------------
