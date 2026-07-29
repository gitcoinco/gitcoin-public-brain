---
id: 15533
title: "Q.E.D. program update 1 + request for community input"
slug: q-e-d-program-update-1-request-for-community-input
category: newscommunity
url: https://gov.gitcoin.co/t/q-e-d-program-update-1-request-for-community-input/15533
created_at: 2023-06-23T22:18:20.863Z
last_posted_at: 2023-06-30T08:16:09.683Z
posts_count: 3
views: 2606
like_count: 9
---

# Q.E.D. program update 1 + request for community input

<https://gov.gitcoin.co/t/q-e-d-program-update-1-request-for-community-input/15533>
Joel_m | 2023-06-23 22:24:05 UTC | #1

Hi everyone, Joel from the [Q.E.D. program](https://gov.gitcoin.co/t/gcp-010-evolving-gitcoin-grants-the-q-e-d-quadratic-experimentation-and-development-program/14174) here. Today marks two weeks into the program, so it’s time to update you all on our progress. I’m going to focus on two big lessons we’ve learned so far, and then give two brief technical updates.

**Lesson 1: translation isn’t just technical**

Our goal with the Q.E.D. program, in a nutshell, is to adapt state-of-the-art QF research for use at Gitcoin. But you can’t just immediately take the mechanisms from research papers, plop them into python, and then call it a day (although [I did do that](https://github.com/Jmiller4/plural-qf), if anyone’s interested): translating between the world of pure math (where QF whitepapers live) and the real world requires a lot of technical adjustments. We were expecting this.

What I wasn’t expecting, however, is that QF isn’t just an algorithm that web3 communities like because it has appealing mathematical properties. It does have nice properties, of course, but in my time reading forum posts and talking to community members, I’ve gotten the impression that folks also like QF for more intuitive reasons. I’ve heard people say they like QF because it’s egalitarian, democratic, empowering… Based on the qualitative research on the topic, it seems to me that QF serves as a mirror for the community’s values: the community co-creates an implementation of QF, sees if the outcome matches their intuitive idea of what should be happening, and then adjusts accordingly for the next grants round.

Because of all of the intangible value propositions, translation can’t just be about the technical details. We have to also make sure that our work syncs up with the Gitcoin community’s idea of what QF should be. To that end, I’m requesting community input so that we can really flesh out our understanding of how the community intuitively thinks about QF and make sure the Q.E.D. program provides the maximum possible value. If you have time, please visit this [polis conversation](https://pol.is/7hskapnxhm) and let us know what you think. Additionally, I’d love to have one-on-one meetings with anybody who’s interesting in taking a deeper dive – to set one up, email me at joeldmiller73@gmail.com.

**Lesson 2: collusion resistance can be private or public**

I’ve learned that Gitcoin has a few cool ways of dealing with sybil networks. Previously, Gitcoin’s fraud defense team implemented sybil defense measures that were kept relatively private, in order to keep bad actors from adjusting their behaviors to avoid censure. On the other hand, Gitcoin Passport provides what I would call a more “public-facing” approach to sybil resistance, where rules are out in the open. Both approaches have advantages, and as we try to understand how to implement anti-collusive QF, this distinction presents the first obvious crossroads. Do we want to keep the rules of our implementation relatively private, or make them public? While we’re open to re-negotiating this issue, right now I strongly feel that our implementation should be public. A public implementation will allow for much easier integration with Passport and other like-minded products in the web3 space, and on a more fundamental level, it better aligns with my belief that social diversity (the backbone of anti-collusive QF) is something to be celebrated and encouraged, rather than something to be hidden away.

**Technical update 1: Metrics for assessing outcomes**

Assessing the differences between outcomes from different QF rounds will be an important part of our analysis. Based on some conversations with members of the data guild, it looks like a metric inspired by [earth-mover distance (EMD)](https://en.wikipedia.org/wiki/Earth_mover%27s_distance) will work well. For our purposes, we can think of EMD as a measure of distance between two different sets of funding amounts: intuitively, the EMD is the total amount of money one would need to move around between various projects to get from one set of funding amounts to the other.

For example, suppose that in a world with only two projects competing for grants funds, I could run algorithm A, which gives both projects $100, or algorithm B, which gives one project $50 and the other $150. Then the EMD between these two outcomes is 50 – since if you start with the outcome specified by algorithm B, then move $50 from one project to the other, you get the outcome specified by algorithm A.

The [most general definition of EMD](https://en.wikipedia.org/wiki/Earth_mover%27s_distance) is a little complicated, but for our special case, it’s easier to define. Let f(*p*,A) be the amount of funding given to project *p* in outcome A. Then our EMD-inspired metric can be defined more simply as

EMD(A,B) = ½ Σ*ₚ* f(*p*, A) - f(*p*, B)

where "Σ*ₚ*" denotes a sum over all projects *p*.

EMD becomes useful when you have some approximate idea of what “should” happen – in this case, some idea of the socially optimal allocation. If you can estimate that, then the EMD between algorithm X’s allocation and the socially optimal allocation is a great metric for evaluating algorithm X. I’ll talk more about how we can estimate socially optimal allocations in the next update.

*Extra info for nerds: if you think of an allocation outcome over n projects as a point in n-dimensional space, then the EMD between outcomes A and B is closely related to the L1 distance (or “manhattan distance”) between the “point” versions of outcomes A and B. But thinking of outcomes as points opens you up to many more distance metrics, for example, L2 (euclidean) distance. So really, there are many closely related metrics to choose from.*

**Technical update 2: Python tool for minimum distance on the Ethereum network**

As I began to dive into the Ethereum data, I found it useful to whip up a simple python tool to query the “distance” between two wallets, where distance is measured in degrees of separation between wallets – i.e., if wallet P transacted directly with wallet Q, the distance between P and Q is one. If wallets Q and R also transacted, but wallets P and R never transacted, then the distance between P and R is 2. I’m sure many have already coded up similar tools, but if anyone is looking for a simple implementation, you can find my code in a google [Colab notebook](https://colab.research.google.com/drive/1A-iibp5lAmhnmhHbOjgBWX3bUfYLKv_7?usp=drive_link) or on [GitHub](https://github.com/Jmiller4/ethdistance/blob/main/ethdistance.py).

That’s all for now. If you have any feedback please let us know in the replies, and if you want to chat one-on-one about QF, please reach out to me via email ([joeldmiller73@gmail.com](mailto:joeldmiller73@gmail.com)). Thanks!

-------------------------

ale.k | 2023-06-26 21:36:10 UTC | #2

[quote="Joel_m, post:1, topic:15533"]
EMD becomes useful when you have some approximate idea of what “should” happen – in this case, some idea of the socially optimal allocation. If you can estimate that, then the EMD between algorithm X’s allocation and the socially optimal allocation is a great metric for evaluating algorithm X.
[/quote]
I think the sensitivity here to the community's sense of "fairness" in any grants round is key. Very excited to hone not only the (amoral) mathematical framework for distributing funds, but also for the research necessary to understand the deeply felt and, as you say, "intuitive" reasons that we all appreciate QF mechanisms.

Looking forward to more learnings and so appreciative of our talks so far @Joel_m - it's been great to have new attention on these age-old problems of fairness and collusive behaviors.

-------------------------

jengajojo | 2023-06-30 08:16:09 UTC | #3

I wanna echo your point on 

[quote="Joel_m, post:1, topic:15533"]
translation isn’t just technical
[/quote]

Some suggestions:
- Create visually appealing interfaces for folks to play with the mechanism in order to understand QF 
- Create an ELI5 version of QF and give it an ELI5 name
- Translating from Math to English is Stage 1. Translation from English to other languages is an equally challenging endeavour. We have been building the latter since 2 years for the broader crypto community and happy to help you with that too! :slight_smile: DMs are open

-------------------------
