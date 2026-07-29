---
id: 9752
title: "dGrants GR12 Round Payout Data Verification"
slug: dgrants-gr12-round-payout-data-verification
category: open-discussion
url: https://gov.gitcoin.co/t/dgrants-gr12-round-payout-data-verification/9752
created_at: 2022-01-21T21:05:52.493Z
last_posted_at: 2022-01-28T22:01:13.548Z
posts_count: 2
views: 2357
like_count: 5
---

# dGrants GR12 Round Payout Data Verification

<https://gov.gitcoin.co/t/dgrants-gr12-round-payout-data-verification/9752>
phutchins | 2022-05-28 15:38:07 UTC | #1

Hey dGrants friends! We've been busy building the prototype of dGrants and running the Gitcoin Building Gitcoin round in GR12 and now that it has wrapped up, its time to execute the match payouts!

This was the first round that was a part of the main Gitcoin quarterly rounds. Our goal is to progressively decentralize the protocol design, software, and process around dGrants. The payout process is currently quite centralized as we believe it is most important to focus on decentralizing the core Grant Registry and the protocol behind it. 

We will continue to work towards decentralizing the payout process and as a first step we are publishing the data that we used to execute payouts. 

You can find that data here: https://github.com/dcgtc/dgrants/blob/GR12Payouts/contracts/deploy-history/out-2.json

In order to verify you can use the branch that is linked above and a starting block of 22016624 and an end block of 22610354.

The process is currently poorly documented but you can find the documentation that we do have in the comments in the header of the file here: https://github.com/dcgtc/dgrants/blob/GR12Payouts/contracts/tasks/payout-data/poc.data.ts

-------------------------

bestape | 2022-01-28 22:02:03 UTC | #2

How were the numbers presented on grants.gtcdao.net calculated? Looking into a discrepancy that I personally don't mind but will hopefully help the community if we can figure out the reason. Thanks!

-------------------------
