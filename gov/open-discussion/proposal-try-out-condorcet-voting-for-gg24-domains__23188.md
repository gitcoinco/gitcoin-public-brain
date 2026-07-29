---
id: 23188
title: "Proposal: Try out Condorcet Voting for GG24 Domains"
slug: proposal-try-out-condorcet-voting-for-gg24-domains
category: open-discussion
url: https://gov.gitcoin.co/t/proposal-try-out-condorcet-voting-for-gg24-domains/23188
created_at: 2025-08-20T22:57:07.205Z
last_posted_at: 2025-09-09T11:28:23.604Z
posts_count: 6
views: 966
like_count: 15
---

# Proposal: Try out Condorcet Voting for GG24 Domains

<https://gov.gitcoin.co/t/proposal-try-out-condorcet-voting-for-gg24-domains/23188>
Joel_m | 2025-08-20 22:57:07 UTC | #1

*(Thanks to @thedevanshmehta @clesaege @sejalrekhan for helping me think about this!)*

**TL;DR** – in this post, I propose Condorcet voting as an option for deciding how to allocate money to GG24 domains. We can run Condorcet voting and the typical [weighted vote ](https://docs.snapshot.box/proposals/voting-types#weighted-voting) in parallel and on the same data, and then decide which outcome we prefer.

As public goods funding matures, Gitcoin is exploring diverse funding mechanisms and round themes. But as the number of mechanisms and domains grows, a new challenge arises:

**How do we decide how much funding should be allocated to each mechanism/ round?**

The current status quo is a naked GTC vote: everyone inputs their preferred way of distributing the money, and we just take the average (or "mean"), weighted by how much GTC each person has.

This type of "mean" weighted voting has two drawbacks. First, it encourages strategic behavior, since there’s an incentive to overstate or understate your preferences in order to make the average go up or down. Second, it results in **peanut-butter spread distributions** where many proposals get just a small amount of money. In the context of GG24 domain funding, this is an especially bad issue, since we’re voting on the funding to entire rounds: it’s really not desirable for an entire round to just get a tiny sliver of the funding pot. If we instead use mean voting to simply decide on the top X domains to fund, we’re still left with the question of how to allocate between those top X domains, and in particular, we’re left without a clear way to make sure the allocation we choose corresponds to everyone’s preferences.

Instead, we propose **Condorcet Voting** as an alternate way of calculating a funding distribution. Condorcet Voting avoids peanut-butter spreads and it’s “strategy proof”, meaning there’s no incentive to misreport your preferences. It can also be configured to give users with more GTC more voice in the process, maintaining GTC utility.

## **How does Condorcet voting work?**

Similar to the [weighted vote ](https://docs.snapshot.box/proposals/voting-types#weighted-voting)strategy on snapshot, users simply input their desired funding distribution (i.e. 10% to domain X, 50% to domain Y, etc) and have their importance weighted by their token holdings (e.g. GTC). The results from condorcet are calculated quickly in Python and compared with the results from a simple weighted vote. Since the input to the mechanism looks just like it does in the weighted vote scenario, we can run the vote on Snapshot and compare the two results afterwards, similar to how we compared results from regular QF with cluster QF.

The output from the weighted votes is what’s called a “**Condorcet winner**”: a funding spread that the community would prefer over any other funding spread, in a head-to-head vote.

In other words, imagine that the community could vote on either adopting the Condorcet winner or some other option. No matter what other option you choose, Condorcet will always beat it out, by definition! This is why Condorcet voting avoids peanut butter spreads: if some domain gets a very small amount of funding it needs to be because the majority of voters actually want that funding to be there, compared to another distribution with that funding removed.

## **Benefits of Trying Condorcet Voting for GG24**

* User’s voices can be weighted by the amount of GTC they have, achieving GTC utility. So nothing changes for the user interface for voting.
* Condorcet voting is Strategy-Proof: there’s no way to game the system. This isn’t true with the mean weighted voting tool employed on Snapshot.
* Condorcet voting avoids peanut-butter spread style distributions, which is very important when we’re funding entire domains. So we could use Condorcet to not just select top domains but also decide on funding between them, which isn’t possible with Snapshot mean weighted votes where we have to disregard domains below a certain threshold.
* Condorcet voting is easy to use: users just input their preferred funding spread.
* One can run Condorcet voting and a more typical “mean vote” in tandem and compare the results, since they both take the same input. In other words, adding on a Condorcet voting calculation costs nothing in terms of UI overhead.
* Because of the way Condorcet winners work, Condorcet voting always returns a non-polarizing output that everyone in the community can agree on.

Appendix:

1. Results of FIL RPGF program if we took condorcet winners instead of mean - [https://docs.google.com/spreadsheets/d/1JdXsEK96he6QliRVeJkggdvylnjQJfm4jKNbMz7Qt38/edit](https://docs.google.com/spreadsheets/d/1JdXsEK96he6QliRVeJkggdvylnjQJfm4jKNbMz7Qt38/edit?gid=1517965966#gid=1517965966)
2. Wikipedia page on Condorcet voting: https://en.wikipedia.org/wiki/Condorcet_method

If anyone has questions, please reach out in the comments. I'm very excited about the possibility of trying this out for GG24!

-------------------------

owocki | 2025-08-20 23:52:52 UTC | #2

thanks for the proposal joel..  

i asked chatgpt5 what condorcet voting is and this is what it said

> Condorcet voting — TL;DR
> * Voters rank candidates.
> * Compare every pair head-to-head; if one candidate beats all others, that’s the Condorcet winner.
> * Sometimes no such winner exists because of cycles (A > B, B > C, C > A).
> * When cycles happen, Condorcet methods (e.g., Schulze, Ranked Pairs) choose a winner from the strongest pairwise set.
> * Pros: honors majority preferences in matchups. Cons: can be complex and somewhat strategy-sensitive.

heres what claude ous 4.1 says:

> Condorcet voting is a voting method where the winner is the candidate who would beat every other candidate in a head-to-head matchup.
> 
> **Key points:**
> 
> * Compare each candidate against every other candidate one-on-one
> * The "Condorcet winner" beats all others in pairwise comparisons
> * Problem: Sometimes no Condorcet winner exists (creating a cycle like rock-paper-scissors)
> * When there's no clear winner, different Condorcet methods use different tiebreakers
> 
> Think of it as finding the candidate who would win a tournament of all possible two-way races.

is this roughly correct?  it seems to differ from your example in "How does Condorcet voting work?" so maybe they are variants of each other. 

------

any chance you all have a google sheet where i can play with various gtc scenarios of [gtc steward voting pattern](https://www.tally.xyz/gov/gitcoin) and see the results in condorcet vs trad voting weights.

does a Condorcet snapshot strategy exist?  thats what we use for voting usually

-------------------------

thedevanshmehta | 2025-09-09 11:25:31 UTC | #3

I'll let Joel respond separately but here are some of my thoughts on this proposal;

[quote="owocki, post:2, topic:23188"]
it seems to differ from your example in “How does Condorcet voting work?” so maybe they are variants of each other.
[/quote]

The main way they are different is in the wikipedia example, we'd only compare candidates with each other. Whereas here, we compare allocations like 20% to A and 30% to B vs 20.5% to A and 29.5% to B vs 21% to A and 29% to B ad infinitum

So in addition to the benefits pointed out about removing peanut butter spreads and strategic voting, GTC stewards should also get some more input on level of funding that each domain should receive which is a tricky question to figure out.

[quote="owocki, post:2, topic:23188"]
does a Condorcet snapshot strategy exist? thats what we use for voting usually
[/quote]

So the cool part is we can use the same Snapshot weighted vote interface but then feed those outputs into Joels python script, and then run a simple vote asking stewards whether they prefer option A (mean results from the weighted vote) or option B (condorcet results from the weighted vote)

When i spoke to the snapshot team about this, they said adding condorcet as a voting strategy isn't something they've received as a request but they would be happy to do if Gitcoin paid for premium ($6k per year). I think we should see run this and poll high context people like you, carl, mathilda etc on which of the 2 matches their prefernces better (weighted vote computed with condorcet or mean).

I personally see this as a zero cost experiment, similar to how we could compare regular QF and cluster QF results from the same voter input and see which one matches our intuition better.

-------------------------

Joel_m | 2025-08-21 16:51:55 UTC | #4

[quote="owocki, post:2, topic:23188"]
is this roughly correct? it seems to differ from your example in “How does Condorcet voting work?” so maybe they are variants of each other.
[/quote]

Yes! These explanations definitely are correct, but they're very general explanations. Because we're working in a narrower context, a lot of things become simplified / easier for us. 

For example: the explanations talk about needing every voter to rank every pair of candidates. But for us, each "candidate" is a funding spread, so we can do the rankings automatically. If a user just reports their *favorite* funding spread, we can automatically figure out their rankings based on how close or far any other funding spread is from their favorite.

Another example: in the most general setting referenced above, a Condorcet winner doesn't always exist. For us, it actually does, because of the way you can smoothly grade between all the different "candidates". The above example mentions that Condorcet winners don't always exist because you can have a cycle of three (or more) candidates that each beat the next guy (like rock paper scissors): A beats B, B beats C, C beats A. If that were to happen in our case (where A, B, and C are all funding spreads), it turns out that you could take the *average* of those three spreads and the resultant option *is* a Condorcet winner. This wouldn't be possible in general (like if A, B, and C were all different people that wouldn't make any sense) but in our case it is. 

Lastly, problems of strategizing are also ameliorated for the same reason. (I can explain this more if there are Qs but I don't want to talk anyone's ear off)

In short -- because of our specific context, a lot of things become simplified / easier with Condorcet voting, but those explanations are still correct in general. 

I will see if I can work towards some type of spreadsheet showing analysis of the steward voting under Condorcet.

-------------------------

clesaege | 2025-08-22 16:16:17 UTC | #5

First I'd like to add that what Joel propose is not simply Condorcet (for that we would need to ask participants to rank all possible distributions which is impractical), but that the proposed method is:
- Ask participants to supply their preferred distribution.
- Assume that participants prefer distributions closer to their owns.
- Simulate a Condorcet vote on all proposed distributions.

Here is a vibe example:

### Domains 
A, B and C.

### Options (candidate distributions)

* **X** = (A=60, B=30, C=10) — from Voter 1
* **Y** = (A=20, B=50, C=30) — from Voter 2
* **Z** = (A=10, B=40, C=50) — from Voter 3

### Distances (L1) and rankings

**Voter 1** (prefers X)

* d(X,X)=**0**
* d(X,Y)=|60−20|+|30−50|+|10−30|=40+20+20=**80**
* d(X,Z)=|60−10|+|30−40|+|10−50|=50+10+40=**100**
→ **Ranking:** X > Y > Z

**Voter 2** (prefers Y)

* d(Y,X)=|20−60|+|50−30|+|30−10|=40+20+20=**80**
* d(Y,Y)=**0**
* d(Y,Z)=|20−10|+|50−40|+|30−50|=10+10+20=**40**
→ **Ranking:** Y > Z > X

**Voter 3** (prefers Z)

* d(Z,X)=|10−60|+|40−30|+|50−10|=50+10+40=**100**
* d(Z,Y)=|10−20|+|40−50|+|50−30|=10+10+20=**40**
* d(Z,Z)=**0**
→ **Ranking:** Z > Y > X

### Pairwise Condorcet comparisons

* **X vs Y:** V1→X, V2→Y, V3→Y → **Y wins 2–1**
* **X vs Z:** V1→X, V2→Z, V3→Z → **Z wins 2–1**
* **Y vs Z:** V1→Y, V2→Y, V3→Z → **Y wins 2–1**

### Result

**Condorcet winner = Y (A=20%, B=50%, C=30%).**

Note that the method extends quite naturally when voters do not provide an allocation to all domains (which is different from preferring a 0 allocation).  For example you could put:
* **W** = (A=50) as your preferred distribution
*  Which would then have for distances:
   * d(W,X)=|50-60|=10 
   * d(W,Y)=|50-20|=30
   * d(W,Z)=|50-10|=40
→ **Ranking:** X > Y > Z

[quote="Joel_m, post:1, topic:23188"]
We can run Condorcet voting and the typical [weighted vote ](https://docs.snapshot.box/proposals/voting-types#weighted-voting) in parallel and on the same data, and then decide which outcome we prefer.

[/quote]
We can do that, but keep in mind that we may not see the full picture here. The main goal of Condorcet is to reduce opportunities for strategic voting, so if voters do not know the method which will be used, it's unclear how this benefit different methods (you may end up having people not voting strategically because they fear condorcet will be used, making averaging look better than what it actually is).

[quote="Joel_m, post:1, topic:23188"]
This type of “mean” weighted voting has two drawbacks. First, it encourages strategic behavior, since there’s an incentive to overstate or understate your preferences in order to make the average go up or down.
[/quote]

[quote="Joel_m, post:1, topic:23188"]
“strategy proof”
[/quote]

Indeed, with mean voting, if you expect other people to value A less than you do, you can just vote (A=100,B=0,C=0) even if your true preference would have been (A=50,B=50,C=0). The proposed voting system doesn't have those kind of issues (in most case, per arrow theoreme there may still be some edgecases of strategic voting, but they are orders of magnitude less problematic than mean voting).

[quote="Joel_m, post:1, topic:23188"]
Second, [mean voting] results in **peanut-butter spread distributions** where many proposals get just a small amount of money.
[/quote]
The proposed method on the other hand would lead to a lot of domains allocated exactly 0. So we can get both the selected domains and the allocation in one shot.

## Median - like method
If we had only 2 domains to allocate, we would only need to specify one domain (if A=x, we have B=100-x). And if we were to apply this method, we should end up with the median.
Here with more than 2 domains, we can see this method as a generalization of the concept of median in higher dimensional spaces. With those two nice properties of:
- If the majority of voters want to allocate 0 to a domain, it should get 0.
- Overstating/Understating one's preference strategically will be unlikely to affect the result.

-------------------------

bonustrack | 2025-09-09 11:28:23 UTC | #6

Hey, here is Fabien from Snapshot, I just want to rectify something, the price is not $20k a year but $6k a year, it's part of Snapshot Pro, you can learn more about it here: `https://snapshot.box/#/s:gitcoindao.eth/pro`. Please let us know if you have any question or if there is anything we can help you with, you can ping me here or on Telegram: `https://t.me/bonustrack`

-------------------------
