---
id: 11611
title: "Sybil Defence Ideas for Gitcoin and Grant Owners"
slug: sybil-defence-ideas-for-gitcoin-and-grant-owners
category: open-discussion
url: https://gov.gitcoin.co/t/sybil-defence-ideas-for-gitcoin-and-grant-owners/11611
created_at: 2022-10-05T21:32:16.355Z
last_posted_at: 2022-11-05T10:26:03.654Z
posts_count: 5
views: 3426
like_count: 22
---

# Sybil Defence Ideas for Gitcoin and Grant Owners

<https://gov.gitcoin.co/t/sybil-defence-ideas-for-gitcoin-and-grant-owners/11611>
Momonosukke | 2022-10-06 06:47:47 UTC | #1

Hey everyone,

This post contains a series of arguments and suggestions aimed at improving Gitcoin’s sybil resistance. It is informed by our own experience and investigation of some of the networks of sybil accounts that have targeted the Gitcoin platform as a whole, and individual grants more specifically.

We have a strong appreciation for how important this problem is because we were recently put in a position where our own motivations were questioned. Our grant was attacked by fraudulent donations and it put us in a position where we had to prove our own innocence. The burden of proof should never be on a victim of an uncontrollable external event they were harmed by.

The first contribution we would like to make is open sourcing a tool for on-chain sybil analysis. Many of the addresses behind the sybil accounts donating to our grant on Gitcoin were conducting most of their activities on Zksync, which is a relatively new L2 with technical properties that can be helpful to malicious actors conducting automated sybil attacks.

This tool helped us aggregate data from different blockchains and analyse them. We hope that it can help others, especially grant owners, that may want to take a proactive role in Gitcoin sybil resistance, by starting with their own grant: https://github.com/fileverse/sybil-analysis

We are confident that if we were able to find so many connections between networks of sybil accounts with the limited data and resources we had, these connections will be even clearer using a larger dataset and by crowdsourcing the analysis.

Recommendations:

By analysing our own sybil attackers we were able to discover some important patterns of attack that can be prevented by changing certain verification and account management features on the gitcoin platform. We focus on five areas of intervention:

* Targeting of Grant
* Discovery of Grant
* Automation
* Evolving Sybil Behaviour

[Targeting a Grant] Capping the number of donations that can be made to a particular grant based on the trust score. Eg: Anyone donating more than 10 times to a particular grant should have a trust score of 100+ on the gitcoin passport.

[Targeting a Grant] Allowing grants to flag sybil behaviour on their grant - similar to flag grant function.

[Targeting a Grant] Give grant owners the ability to reject QF matching tied to a specific donors’. Because donations come directly to grant addresses, what grant owners can at least do is identify malicious actors and put them in a category of “not to be counted for QF matching”. This is useful on many levels. First, it allows GitcoinDAO to see that a grant being targeted is actively fighting off the attackers. Second, it creates a quick response mechanism that leads to faster identification of attackers and a safer, fairer round. Third, it allows for corroboration to occur. For example, you will be able to see that of the top 10 grants’ owners, 7 of them have reported at least 60% of the same accounts. Grant owners are the best front line you have, given the appropriate tools, to create a sybil resistant Gitcoin platform.

[Discovery of Grant] For the “trending” category only using the donations made from the users that have a trust score greater than 100.

[Automation] Add some value to the trust score automatically by checking the activity / age of the github account.

[Automation] Add recaptcha score to each transaction made from the gitcoin platform.

[Evolving Sybil Behaviour] Real time sybil flagging engine (see below).

Real Time Sybil Flagging System

This system relies on the assumption that parts of sybil networks are automated systems and exist to manipulate the Gitcoin platform in ways which might not be obvious to someone looking from the outside.

This is an attempt to design an adaptive system that can take advantage of external analysis and FDD teams investigators. Participation from the FDD Team and community members is a very important factor for its success.

![|194x127](upload://mggfq6hGNMf0pVxuAAvudwfjKPh.png)

In the above graph A and B Node transfer some money to C which then donates that money to some grant.

In our case and of some other grants this pattern was followed:

![|459x187](upload://oF0IhDL5OJ3fHHWVRao5qM8zA3L.png)

We analysed donations made to our and others’ grants and found that the addresses associated with potential sybil accounts were all donating to us by following the same script / pattern of transactions which we describe below:

* Retrieve money from the same bridge.
* Do the similar type of transactions prior to the donation (do some token swaps and/or mint some NFT).
* Donate on low nonce, below nonce 15.
* Donate to one grant only.
* Return the rest of the money back into the bridge.
* Stop all activity once nonce 15 is reached or before.
* Rarely have any activity on the ethereum blockchain.

Finding from this that formed the base of assumption for the proposed system:

* There is always a source of funds in the sybil
* Sybil addresses usually interact with similar services (bridges, mixers, DEX, CEX)
* Sybil usually do txns among their accounts to keep the total cost of doing the sybil attack low

A more proactive system:

* Penalise all the other nodes interacting with the known sybil nodes in realtime
* Penalise all the other nodes using services used by known sybil nodes for cycling of funds. This assumes that there are unique mixers or other smart contracts being used by sybil nodes that would be very unlikely to be used by regular users.
* Take the input from community and FDD team of known sybil accounts in real time

Output of this system is the likelihood with which any given input account is a sybil node. Using sybil node score in real time matching calculation.

How it works:

1. Start with a known sybill set that might expand or contract
2. Keep a list two sets - one hop, two hop from the sybil set nodes
3. Any donation is received by a grant. Get all the nodes that are one hop away from the node. Both in and out txns.
4. Check if there are matches in this from the sybil set(1), sybil set hop 1(0.5) and sybil set hop 2(0.25). Depending on the match, add all the values. To get the sybil score

* In this case drop off per hop is ½, and can be tweaked depending on the performance of the system in real time.

5. Keep the min and max values of sybil score to map this value on that spectrum and get a percentage. Can use different ways to get the percentage.

If any account doing the donation has a high sybil score above sybil threshold -> reduce their impact on the grant donation matching metric calculation.

Areas of Improvement:

* Include hops on different networks for generating one hop and two hop of known sybil set for step 2.
* Include hops on different networks for step 3.
* Tweak the sybil threshold depending on grant’s reputation
* Tweak the sybil threshold depending on rounds progression
  * 0.1 on day 1
  * 0.2 on day 2
  * 0.4 on day 3
  * … so on
* FDD keeps adding nodes to sybil set during the round from their independent analysis
* Independent analysis of sybils flagged by the grant and their addition to sybil set

The above system is not a ‘one stop solution’, but a way to increase the attack cost involved with the sybil attacks as we can catch basic patterns from this. In most cases systems get attacked frequently by bots because it’s easy to do so and has low or no penalty.

The parameters should be tweaked to reflect the situation at hand and sophistication of the sybil attackers.

Hope this post is useful to anyone out there trying to solve sybil resistance.

-------------------------

connor | 2022-10-05 23:24:15 UTC | #2

I really appreciate you writing all this up, sharing your Sybil analysis on Github, and more! This is very well written.

And at the end of the day, it is indeed very hard to tell and prove whether a grant owner is involved in their Sybil donations. 

From what I've seen there are two main categories of attackers:

1. Users Sybil attacking their own grant to significantly increase their matching (often fake/made-up projects)

2. Users farming possible future airdrops by Sybil attacking specific grants they are not associated with but have reason to believe might do an airdrop in the future

The problem has seemingly gotten worse with more big projects like Optimism airdropping to Gitcoin donors, ZKsync rumors, etc.

There are also now tons of posts and threads like this one that speculate on grants to donate to (Fileverse is often included) and many of the grants in these lists end up getting the most donations:

https://twitter.com/OlimpioCrypto/status/1568728742494875648 

Hopefully once the Grants Protocol launches, and Passport is built out, there will be a much higher barrier to entry for creating multiple/fake profiles

-------------------------

ccerv1 | 2022-10-06 11:49:19 UTC | #3

Thank you for this post -- and for the helpful ideas on improving Sybil defense!

[quote="Momonosukke, post:1, topic:11611"]
This tool helped us aggregate data from different blockchains and analyse them. We hope that it can help others, especially grant owners, that may want to take a proactive role in Gitcoin sybil resistance, by starting with their own grant: [GitHub - fileverse/sybil-analysis](https://github.com/fileverse/sybil-analysis)
[/quote]

You should consider packaging this into a submission for the [Gitcoin hackathon](https://gitcoin.co/issue/29389) that's happening right now.

I'd love to see this tool be adopted as a new sybil scoring lego, both for FDD and the wider Ethereum community!

-------------------------

vijaykrishnavanshi | 2022-10-19 15:52:27 UTC | #4

Hey @connor,
 
Indeed, sybil resistance is a very hard problem to solve in decentralised systems and we see Gitcoin trying its best to tackle it by crowdsourcing solutions and appreciate it. 

I prefer thinking of sybil attacks and resilience in terms of actors trying to exploit a system using the parameters it's based on. Focusing on the motives of the attackers and solving the problem based on motives can get quite complicated as the sybil networks evolve.

System parameters on the other hand are known at all times. And although stopping the sybil attacks is the ideal outcome, a good second goal to have is tweaking the system parameters so that it doesn't lose its purpose or value because of ongoing sybil attacks.

For the time being that is why we suggested some checks and balances that can be implemented in the short term to not have such scenarios in the future grant rounds. And also an adaptive system for long term defence.

-------------------------

ZER8 | 2022-11-15 17:06:45 UTC | #5

Just my 2 cents, but ideally Gitcoin should try to gain advantage of these airdrop farmers(because they are really unstoppable) and "convert then into regens without them knowing it"(I think you actually used this sentence).  Some complex reverse engineering techniques may help achieve this goal.

-------------------------
