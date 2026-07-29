---
id: 20023
title: "My Disastrous Experience in GG22"
slug: my-disastrous-experience-in-gg22
category: open-discussion
url: https://gov.gitcoin.co/t/my-disastrous-experience-in-gg22/20023
created_at: 2025-02-19T14:48:11.650Z
last_posted_at: 2025-03-04T22:57:12.159Z
posts_count: 7
views: 1861
like_count: 19
---

# My Disastrous Experience in GG22

<https://gov.gitcoin.co/t/my-disastrous-experience-in-gg22/20023>
xunorus | 2025-02-19 14:48:11 UTC | #1

### **ABOUT ME AND GITCOIN**

I feel completely aligned with Gitcoin’s fundamental values and the experiments they are running around QF and new financing mechanisms.

I’ve been a crypto enthusiast since 2012. I’ve used and promoted crypto as an empowering tool everywhere since then.

GG22 was a disaster for me.
GG20 was amazing—I wasn’t expecting anything, yet I earned 500 bucks.

I’ve been researching and involved in this project for more than three years now.
I'm also a full-time musician—a guitar concertist and composer.

In addition, I’m developing a big project to fulfill my needs as an indie musician (**Musiclog**).

---

### **MY PROJECT**

I created **Ius Naturalis**, a wallet designed for self-sovereign individuals under natural law. Beyond being a regular EVM wallet, it serves as a platform to test and explore **monnaie libre** projects and attestation mechanisms for these individuals, as well as for document management.

My users are communities focused on the application of natural law, people building natural people's tribunals, and those studying alternative mechanisms for living in society.

I believe the niche is somewhere between **2K and 200K** people.

I’ve been researching and involved in this for more than three years now.

---

### GG22

I created a group of around 30-40 people in France who are trying out the wallet and may potentially contribute financially to the project.

The majority are crypto newbies.
I made tutorials and helped my users make small test donations.
Most of them donated just a dollar or less as a test.
Others contributed between 10 and 80 bucks.

---

### THE PROBLEMS

The Sybil detection mechanism, I believe, hurt my project.

I ended up with **0 QF**.
The page says I collected around **$56**, but in reality, it was closer to **$90**(!?).

I ran out of energy even to share this terrible experience.
For now, I continue my research in my free time, with no funding.

I’m developing a **direct crowdfunding mechanism** that integrates with my wallet and enables **stealth donations**.


### LINKS

GIT22 https://explorer.gitcoin.co/#/projects/0xdebe51a2b4727f5eb6fab0c707a4f6507e542a8bdcd031eb10c7035799ed0ba0

GITCOIN CHECKER https://checker.gitcoin.co/public/project/show/iusnaturalis

KARMA https://gap.karmahq.xyz/project/iusnaturalis

DEMO https://iusnaturalis.web.app/

SOURCE CODE https://github.com/energiasonora/iusdappv2

MI PREVIOUS GG20 PROJECT (chatwallet) https://explorer.gitcoin.co/#/round/42161/23/16

-------------------------

MathildaDV | 2025-02-19 18:49:25 UTC | #2

Hi @xunorus thank you for your feedback and post. Something we can do a better job of is more education on how COCM (Cluster Matching QF) works! You can find out more about how it works and affects matching amounts [here](https://www.gitcoin.co/blog/leveling-the-field-how-connection-oriented-cluster-matching-strengthens-quadratic-funding).

But the TL;DR is that if your donations only come from one pool of donors that are also donating with new wallets without reputation then that's the reason you received $0 in matching. I see you got a total of 27 donors, with 23 of them not qualifying for matching. 

I'm sorry you had a bad experience, and as mentioned we can do better at educating around how our updating QF mechanism works. With COCM, we have the strongest sybil resistance we've ever had which is a very important piece to keeping the rounds fair and collusion-free. 

I would recommend in the next round to encourage your donors to not only donate to your project, but also support others within the round, as the projects that have the widest base of support from various communities of donors get a larger portion of the matching.

[quote="xunorus, post:1, topic:20023"]
The page says I collected around **$56**, but in reality, it was closer to **$90**(!?).
[/quote]

This could very well be because a lot of donors donated directly to you through our direct donations instead of through GG22. Direct Donations are permanently live (even outside of a GG round) and on quite a few occasions donors donated via the Direct Donation instead of the GG22 round. This unfortunately resulted in those donations not being eligible for matching. This is being fixed and will not be possible in future rounds. 

I hope this clears it up for you? LMK if you have any further questions or concerns!

-------------------------

owocki | 2025-02-20 17:48:17 UTC | #3

thanks for taking the time to write up this feedback @xunorus - feedback is a gift!

> With COCM, we have the strongest sybil resistance we’ve ever had which is a very important piece to keeping the rounds fair and collusion-free.

agree this is true!

but is very unfortunate (and bad for growth) that CCOM reduces the value prop for new users to the site.

[quote="MathildaDV, post:2, topic:20023"]
I would recommend in the next round to encourage your donors to not only donate to your project, but also support others within the round, as the projects that have the widest base of support from various communities of donors get a larger portion of the matching.
[/quote]

we can ask users to do this... but i do think the fix is that the product UI should push people down this path. @Joel_m is that a smart way to solve for these tradeoffs?

cc @meglister since this is a product suggestion.

-------------------------

meglister | 2025-02-21 17:02:04 UTC | #4

thanks for the feedback @xunorus and the suggestion @owocki -- will see what we can do for the next round!

-------------------------

tomislavmamic | 2025-02-26 14:19:58 UTC | #5

In multiple rounds, whenever I approached someone directly to donate to my project, I would instruct them to donate to a few other projects too. I emphasised this. But, when I checked their donations, most of them only donated to my project. They either didn't understand or didn't care enough.

There should be a warning when someone only wants to donate to one project. Maybe even we should make it a hard requirement to select at least 3 projects and maybe even to allocate between them the similar amounts.

-------------------------

tomislavmamic | 2025-02-27 15:21:09 UTC | #6

Might be worth looking into if COCM could be improved by turning it from a [one-shot game into a repeated game](https://science.howstuffworks.com/game-theory4.htm). Unless I am mistaken, COCM script is run on each round individually. The script is unaware of previous contributions of the donor, or the previous donations and matching received by the project.

A project with a prominent mindshare in a large group of returning donors (those who donate in each round) will always take the cake when compared to a project that gets less donations but from different groups of active donors every time. If we make COCM aware of previous donations, this could potentially be fixed.

A donor who participated in multiple rounds, could have all his contributions to date added to the formula. If she has been repeatedly supporting a same set of projects, she should be punished for it by the new formula and other donors who donate to different projects each round will get rewarded.

What we currently have is the Passport score, but that's solving another issue.

Gitcoin has all the data needed for this and we can even replay the last round results to see what effect would this mechanism have.

Have you considered this @Joel_m ?

-------------------------

UI369 | 2025-03-04 22:57:12 UTC | #7

Do you know if the checkout tells them what their matching will be? Might be a good time for an "upsell" in the UI to help them improve the match rate.

Also if you do carry on and those people donate again in future rounds, I wonder if it would go better, once they are no longer "new wallets"?

-------------------------
