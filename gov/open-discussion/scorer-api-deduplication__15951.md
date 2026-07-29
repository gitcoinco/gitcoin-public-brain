---
id: 15951
title: "Scorer API Deduplication"
slug: scorer-api-deduplication
category: open-discussion
url: https://gov.gitcoin.co/t/scorer-api-deduplication/15951
created_at: 2023-07-25T20:33:46.224Z
last_posted_at: 2023-07-25T20:56:24.972Z
posts_count: 2
views: 1472
like_count: 3
---

# Scorer API Deduplication

<https://gov.gitcoin.co/t/scorer-api-deduplication/15951>
Mika | 2023-07-25 20:33:46 UTC | #1

What I don't get about the Scorer API is how these two can go together:

1. "The scores assigned to Passports will not change once they are issued. This means that there is no need to recalculate Passport scores or synchronize them again in case of duplicate stamp submissions"

2. removed and expired stamps can be reissued on another passport and count towards its score

It seems like for one-time claims (airdrop, faucet etc) it should not count the same stamp on a second passport within the same scoring instance, even if it has been removed from the first one.. or am I missing something?

-------------------------

Jeremy | 2023-07-25 20:56:24 UTC | #2

Heya, that's a fantastic question. In a lot of the integrations the the scores are taken in a 'snapshot' type format (e.g. at the end of the Gitcoin grants round, or before a raffle is submitted, etc). However, this could be a potential attack vector and we're looking into how to resolve now to prevent that from being abused!

-------------------------
