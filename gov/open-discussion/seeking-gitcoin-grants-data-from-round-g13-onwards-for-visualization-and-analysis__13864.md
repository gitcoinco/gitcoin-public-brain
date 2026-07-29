---
id: 13864
title: "Seeking Gitcoin Grants Data from Round G13 Onwards for Visualization and Analysis"
slug: seeking-gitcoin-grants-data-from-round-g13-onwards-for-visualization-and-analysis
category: open-discussion
url: https://gov.gitcoin.co/t/seeking-gitcoin-grants-data-from-round-g13-onwards-for-visualization-and-analysis/13864
created_at: 2023-04-07T00:17:53.863Z
last_posted_at: 2023-04-12T06:42:03.754Z
posts_count: 7
views: 1857
like_count: 7
---

# Seeking Gitcoin Grants Data from Round G13 Onwards for Visualization and Analysis

<https://gov.gitcoin.co/t/seeking-gitcoin-grants-data-from-round-g13-onwards-for-visualization-and-analysis/13864>
52hz | 2023-04-07 00:17:53 UTC | #1

Hello everyone,

I hope you're all doing well. I am reaching out to the Gitcoin community to inquire if anyone has access to grant data from Round G13 and onwards, similar to the information found in this spreadsheet:

https://docs.google.com/spreadsheets/d/1OsJ_nmN9mN-i_9h3Yj2mDfjvtsP1qvv3B1zcpER62dk/edit#gid=1223173410

It seems that the data has not been updated since Round G12, and I've only come across well-crafted analyses on the forum. I am curious to know where everyone finds their data.

I am interested in conducting some visualization and research analysis, something like these:
![image|690x161](upload://eUtTzH6bP8gz1zH42ZA88LYwUdD.png)
![image|690x166](upload://xwNQHHh7qfD4eGST5PiXLntNuLg.png)
![image|690x153](upload://9MySWVi7a4UJuE4Vnpb7K7qBNDQ.png)
![image|690x466](upload://d5SHB5Z4A9vb0lsT0pg7sfnHBZP.png)
![image|690x432](upload://hp9hj5vGyu75FI0uANchdF45DvK.png)
![image|690x424](upload://rzL2s4g1QmDJeIeurpkmTTKHin7.png)
![image|690x461](upload://7ERw3B0Meji4zOi48TurZF686As.png)
![image|690x166](upload://fgH877JKw8Uf58gdou7OHYnxcnq.png)
![image|422x500](upload://6GMYqhe4y3VBsihlRm8sjsmhAwU.png)

I would be more than happy to share my findings with the community. Your help would be greatly appreciated!

Thank you in advance!

-------------------------

kyle | 2023-04-08 14:36:12 UTC | #2

Hey there - Love the idea of showcasing more of this work. The Grants data is pretty messy from the centralized platform as we used a good faith validation when computing details, and then would back out Tx data when it didn't actually settle on chain. it meant multiple "sources of truth" were created based on initial Tx creation, and then what would actually settle out.

Have you tried using the API to pul the data you may need though?
Check this out and see if you can pull some of the missing details:
Grant API details - https://github.com/gitcoinco/web/blob/master/docs/API.md

-------------------------

ale.k | 2023-04-11 05:45:26 UTC | #3

hey @52hz 

Like @kyle says- we're very work in progress on the data cleaning from historic grants rounds... so while I don't have this merged with active matching rates or regions (in many cases we don't know the geographic region) I do have this holding site for static grants round data. https://fddhub.io/

Would love it, of course, if anyone was inspired to backfill the extra attributes you reference here - and otherwise, stay tuned for more holistic historic matching rates to date.

-------------------------

52hz | 2023-04-11 20:28:30 UTC | #4

Thank you, Kyle. I tried it, and it seems like this Generalized API access is not available to me. It looks like the link on GitHub hasn't been updated: "Gitcoin provides a simple read-only HTTPS API to access data. The API is live at https://gitcoin.co/api/v0.1"

And also, if multiple "sources of truth" were created based on initial Tx creation, and then what would actually settle out. Does this mean amount_in_usdt >= actual amount? Is there any way we can filter it out? Thanks

-------------------------

52hz | 2023-04-11 20:33:46 UTC | #5

Thank you, Alex. This is super helpful and I believe it's sufficient for me to create some visualizations with the data provided.

I'll touch base with you once I've completed the work!

-------------------------

ale.k | 2023-04-12 06:19:53 UTC | #6

awesome- looking forward to it! Thanks for digging and for your work!!

-------------------------

52hz | 2023-04-12 06:42:03 UTC | #7

Just noticed the category is not in those charts, is there any way I can find the name, category, Eligibility Tag, and Discovery Tag for each grant_id? I know that there is a lot of missing data in regions, but it could still be valuable.

I want to know if there is an existing database, or if I need to use a crawler to collect the data myself. Thank you Alex!

-------------------------
