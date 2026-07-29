---
id: 19770
title: "Adaptive Deep Funding"
slug: adaptive-deep-funding
category: open-discussion
url: https://gov.gitcoin.co/t/adaptive-deep-funding/19770
created_at: 2024-12-18T00:38:18.463Z
last_posted_at: 2024-12-19T18:37:58.382Z
posts_count: 2
views: 1883
like_count: 3
---

# Adaptive Deep Funding

<https://gov.gitcoin.co/t/adaptive-deep-funding/19770>
DistributedDoge | 2024-12-18 00:38:18 UTC | #1

**TL;DR:** What if we could build a mechanism where Gitcoin donors directly steer "deep funding" towards repositories/projects they care about?

## Deep Funding

[Deep Funding - a visual guide in 3 easy steps](https://gov.gitcoin.co/t/deep-funding-a-visual-guide-in-3-easy-steps/19765)

The existing design for deep funding assumes that it’s possible to create a quality model (or ensemble of models) that sufficiently answers the question: *"What is valuable?"* 

- Even if multiple models are in place this feels like approach of central planner. 
- This approach doesn’t appeal to me as a donor. I want to direct my money to projects I care about, not rely on a third party’s determination. I am much more liberal when it comes to money that comes from Gitcoin round sponsors.
- Deep funding also emphasizes **good models** as a key part of the mechanism. I’d rather have **donors** drive the mechanism, adjusting rules toward the desired outcome: **funding dependencies.**

I am going to take part in "model contest" and maybe it would produce good models that I like to use, but really interesting question for me is - can we build better **deep funding** using wisdom of crowds, instead of AI/ML? 

### Main Idea is to propose "Adaptive" flavour of deep funding:

1. **Initialize deep funding** by starting with weights in a **neutral position**.
2. Allow these weights to be adjusted through Gitcoin donations.
3. Stream sponsor money to projects according to the current weights.

You can imagine this process as donors paying to teach a neural network to steer sponsor funds toward the outcomes they value. 

If some donor prefers to use "AI agent" to decide where his funds should go - they could do that in this system.

This is still popularity contest, but thanks to "trickle-down" effect it does better job funding dependencies than current approach where each project in a round is independent.

---

#### Example Initial Position:

* *"Every dependency gets a fixed share of the matching pool per hour."*


**Simple Round:**
A round with four projects:

* "Gitcoin,"
* "Gitcoin-Citizens,"
* "Chainlink,"
* "Chainlink-Marines."

Each starts earning $3/hour. Donating to the "Gitcoin" project would also benefit "Gitcoin-Citizens" (as part of its dependency tree) - but not as much as if we donated to "Gitcoin-Citizens" directly.

![image|487x500](upload://sq0zwGA6uZxgJhV3ndRG7BqaLNQ.png)

Total rate of funding coming from sponsors is some fixed number (e.g. 12$/h).

### Key Differences from Gitcoin Today:

1. **Dependencies:**
Projects must declare dependencies (e.g., "Bankless" → "Bankless-London") or infer them (e.g., software dependency trees).
2. **Trickle-Down:**
Matching needs to account for the "trickle-down" effect when calculating final distributions.
3. **Trickle-Up:**
If dependencies get donations "upstream" project should benefit as well.
4. **Streaming Matching:**
The matching pool could either stream in real-time or calculate at the end of a round.

---

### Considerations:

1. Exact algorithms for weight updates/trickle-up/down are required.
2. "Initial distribution" could be more complex - something metrics based. It doesn't need to be perfect, because donors should quickly correct it.
3. Projects may excessively split into smaller units to capture more initial funding (happens already).

I am still trying to iron out how such "deep funding through crowdfunding" mechanism could work so would be happy for any feedback or alternative ideas!

-------------------------

KMLLC | 2024-12-19 18:37:58 UTC | #2

Love this model, perfect example of multiple mechanism funding, leveraging various capital allocation mechanisms.

-------------------------
