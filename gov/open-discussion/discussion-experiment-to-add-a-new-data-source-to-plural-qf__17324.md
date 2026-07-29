---
id: 17324
title: "[Discussion] Experiment to add a new data source to Plural QF"
slug: discussion-experiment-to-add-a-new-data-source-to-plural-qf
category: open-discussion
url: https://gov.gitcoin.co/t/discussion-experiment-to-add-a-new-data-source-to-plural-qf/17324
created_at: 2023-12-22T03:27:13.850Z
last_posted_at: 2023-12-22T03:27:13.918Z
posts_count: 1
views: 3222
like_count: 2
---

# [Discussion] Experiment to add a new data source to Plural QF

<https://gov.gitcoin.co/t/discussion-experiment-to-add-a-new-data-source-to-plural-qf/17324>
tkgshn | 2023-12-22 03:27:13 UTC | #1

side story from https://gov.gitcoin.co/t/decartography-beta-is-out-how-to-generate-clustered-data-from-grs-participation-data-and-how-to-improve-current-gitcoin-grants/17290
---
The hypothesis is that if we simulate Plural QF using cluster data with DeCartography, we can implement a more reliable Pluralism. To implement this with Gitcoin, I think a demonstration would be in order. There are several candidates for how to proceed with that. For example, we could do backtesting in GR, where there are fewer participants, and then try it out in GR19? (backtesting: testing a method/algorithm on historical data before testing it on production data to see if it works)

So I was going to do backtesting, but the IPFS linked at https://fddhub.io/downloads/grant_rounds is broken. Where is the data for this?

---

After backtesting, I’ll be able to provide data like this https://gov.gitcoin.co/t/how-much-does-plural-qf-reduce-collusion-compared-to-normal-qf/15709 this image compares RetroPGF vs Gitcoin. but, imagine comparing current Plural QF vs Plural QF by DeCartography social graph

after backtesting, we can continue to provide clustered data if gitcoin can be paid

https://gov.gitcoin.co/t/gr14-governance-brief/11050
Now it looks like FDD has been dissolved, but Sybil Account Detection (SAD) was originally there.
 
>The primary Sybil Account Detection (SAD) model used in production is operated by the Data Operations squad. Sybil Operational Processes (ASOP). Humans evaluate random samples of accounts to statistically validate the model and to identify new behavioral insights which can be built into new "features" or inputs to the machine learning model by the Community Intelligence squad.
  Briefly, the process is to "humanely determine suspicious accounts and to reflect the findings in the machine learning model.

FDD has spent an average of `$12,000`/round on this work, which is referred to as "Human Evaluations." DeCartography can be easily understood by replacing this work as crowdsourcing.

The expenses required to convert GR participant data into a social graph using DeCartography are as follows: 
To begin with, the expenses are calculated using the following structure
 - Size of data to be analyzed
 - How many times per session you want the crowd worker to solve the task
 - How much to pay per session
 
A simple code to calculate the necessary expenses can be found at: 
 https://gist.github.com/tkgshn/aece3bdd6ba193ebb2be932d621f131c

---
# Next Action
- anyone teach me about where is GR3 data (to preparing backtesting)
- after backtesting, I'll share the result. then, let's keep discuss paid PoC

-------------------------
