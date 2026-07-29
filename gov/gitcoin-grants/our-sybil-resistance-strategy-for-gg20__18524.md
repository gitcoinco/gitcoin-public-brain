---
id: 18524
title: "Our Sybil Resistance Strategy for GG20"
slug: our-sybil-resistance-strategy-for-gg20
category: gitcoin-grants
url: https://gov.gitcoin.co/t/our-sybil-resistance-strategy-for-gg20/18524
created_at: 2024-04-04T10:50:39.074Z
last_posted_at: 2025-03-30T10:23:11.874Z
posts_count: 20
views: 10895
like_count: 58
---

# Our Sybil Resistance Strategy for GG20

<https://gov.gitcoin.co/t/our-sybil-resistance-strategy-for-gg20/18524>
umarkhaneth | 2024-04-04 10:56:54 UTC | #1

By @Joel_m @umarkhaneth 

With big thanks to @Sov and @meglister 


# TL;DR

In this post, we’ll share our Sybil resistance strategy for GG20. Our plan is based on three lines of thought:

1. If you can only look at donation data, complete Sybil Resistance is impossible in any QF mechanism, no matter how fancy.
2. That being said, COCM has a large (though not complete) sybil-reducing effect.
3. The passport team has recently introduced a new verification procedure called Passport model based detection, which reduces user burden and appears to be quite effective when combined with COCM.

Therefore, the strategy is clear: use COCM and Passport’s model based detection for GG20, which will yield a smoother user experience and more sybil resistance.

# Wait, what’s COCM?

You can think of COCM (Connection-Oriented Cluster Match) as a tweak to the Pairwise Match algorithm suggested by Vitalik. Like Pairwise Match, COCM is based on standard QF and attenuates a project's funding if many of its donors have similar donation patterns. However, COCM calculates similarity differently. See [this blog post](https://www.gitcoin.co/blog/wtf-is-cluster-matching-qf) for a full explanation.

# Sybil resistance is at odds with what we like about QF

QF is commonly understood as a fairly democratic mechanism, in the sense that many small donors can out-class one large donor. It turns out that sybil resistance is at odds with this property.

The community uses the term “sybil” in many ways, so let’s clarify what we mean. Imagine a person about to donate to Gitcoin Grants – say, $10 to project X, and $4 to project Y. Before checking out, they pause and ask, “what if I actually split my donations among two separate wallets? I could donate, say, $5 to X and $2 to Y from both wallets, instead of making one big donation.” If that person wouldn’t be better off splitting up their donation (regardless of the original donation amounts or the way they split it up), then I’ll say the QF mechanism is sybil resistant, since people are incentivized just to make their whole donation from one account.

The problem is that any mechanism with this sybil resistance property degenerates into a direct donation mechanism where no matching funds are added. This is because you can apply the logic of the definition in reverse. Imagine that Alice and Bob are two donors to a QF round. Even if Alice and Bob are real people, a mechanism has no way of knowing that their donations aren’t really two sybil donations from a real user named Charlie, whose cart originally held all of Alice’s donations plus all of Bob’s.

In fact, we could replace Alice and Bob’s donations with the donations from our hypothetical Charlie – and because of our Sybil resistance property, we still get the exact same funding results as before. But now our list of donors is one shorter. So what if we do the same thing again? We can pick two random users, combine their donations, and have a guarantee that our mechanism does the same thing before and after we squish them together.

Now we’re in trouble, because we can keep “squishing” users together until our algorithm is just running on one donor who gave the sum of everybody’s individual donations. But we already know what QF mechanisms do when there’s only one donor – they don’t add any matching funds! So our sybil resistant “QF” mechanism is really just a plain old direct donation mechanism.

# In experiments, COCM is much less vulnerable to Sybil attacks

Given that sybil attacks are inevitable in any variation of QF (including COCM), the next step is to see how bad they get. To figure this out, we simulated a bunch of sybil attacks in the donation data for the Zuzalu tech round, which had just over 4,000 donors.

For each project, we had the top 10 donors to that project make some number of sybils (5, 25, 75, or 100) each. We created these sybils by splitting up the real donations among the appropriate number of new wallets – so, no new money was added to the system. Then re-ran QF (or COCM) and saw how much the funding to that project changed. For each amount of sybils per user, we measured the average funding gain across all projects, and the maximum funding gain that any project got. Results are below:

![|475x355](upload://x5C85qHCOEzyy0aPIiNVxw3u8vL.png)

This chart makes it pretty clear that COCM is much more resilient to sybil attacks than standard QF. Let’s zoom in on COCM:

![|470.1995926680244x352.6496945010183](upload://cJNkUGbETZ6tncWa0sl7n2jjhpv.png)

Even in the worst case, generating 1,000 new sybils only nets an extra 0.2 percentage points of funding for a project.

Generating sybils makes so much less of a difference under COCM because it attenuates funding when donors look similar. It may be difficult to generate a large number of sybil accounts that look different enough to get past the attenuation imposed by COCM.

But this leads to a caveat: there are many, many strategies for generating sybil accounts. I tried many of them, but we didn’t try all of them, and we certainly don’t consider ourselves better sybil attack strategists than every other person in the web3 ecosystem. Some attack strategies may be more effective than what we tried.

Nevertheless, these experiments suggest that Gitcoin’s sybil resistance strategy can be adjusted to have a lighter burden on the user. Next, we’ll describe a new approach to Passport that does just that.

# Passport’s Model-Based Detection Provides Lower User Friction and Greater Effectiveness

The Gitcoin Passport team has recently introduced a Model-Based Detection System. This system analyzes the on-chain history of addresses and compares it to the historical data of known human and sybil addresses. Based on this comparison, the model assigns each address a score ranging from 0 to 100, where a score closer to 0 indicates a higher likelihood of the address being a sybil, and a score closer to 100 suggests a higher probability of the address belonging to a genuine human user.

This is a very different approach from the Stamp-Based System, in which users are prompted to connect with different identity providers to prove their personhood. In past rounds, we’ve heard many complaints that people find this manual system too difficult to achieve a high enough score for maximum matching.

One of the advantages of the Model-Based system is that it requires minimum user interaction and could greatly reduce user frustration. The new user experience would be mostly hands-free. Users' wallets will be automatically scanned in the background and assigned a score based on their history.

Additionally, we’re keen to understand if this newer system can provide a level of sybil defense that is at least as effective as Passport Stamps in GG19. We’ll investigate how it would have impacted the results if it had been used instead.

One of the difficulties with the sybil resistance problem is that there is no answer sheet: we don’t have a list of confirmed humans and sybils and have to move forward with our best guesses.

To determine if our solutions are protecting the matching pool from bad actors, we gut-check how our solutions affect which projects get funded. After investigating the projects in the round, a member of our team assigns each project a ‘Legitimacy Score,’ which is just a hand-wavey approximation. 5 means more legitimate, and 1 means less. When comparing COCM to normal QF, we’ve seen it take matching funds away from projects that have less legitimacy and shift them toward projects that have more.

If we were to use Model-Based Detection instead of Stamp-Based, we’d want to see the matching going to the scammy projects be even less while there is an uptick in the matching going to legitimate projects. This is exactly what we see:

![|624x323](upload://n67rnr4Mv2gtJ5BIeuJF2xCw2E.png)

1 and 2 scoring projects all see a slightly greater reduction in matching funding when switching from Stamps to the Model. This is a positive sign because it means the Model is removing voters from matching who are giving to these scammy projects. At the same time, we see a big increase in matching going to more legitimate projects indicating that the Model predicts most of their voters are human and should stay in the dataset. This is also a great sign!

COCM alone redistributes 180,233.84 DAI of the matching fund compared to using normal quadratic funding and Gitcoin Passport. When combined with the Model, the redistribution increases to 227,453.29 DAI, representing a 20% increase in redistributed funds.

Evaluating the impact of the Model without COCM, we find that it still redistributes 82,356.04 DAI. The redistribution shows a moderate to strong positive correlation (0.66) between the effects of COCM and Model on the results. This indicates that both strategies move results in the same direction and provide benefits when used separately. However, the strongest outcome is achieved by using them together.

In GG19, Gitcoin Passport alone, without COCM, would have redistributed 9,643.46 DAI compared to not using Passport at all. The results show a weak negative correlation (-0.13) with COCM results.

It is noteworthy that using the Model would lead to significantly improved funding outcomes, representing a substantial change in the effectiveness of sybil detection. Moreover, this can be achieved without requiring the voter to interact beyond sharing their wallet address, greatly reducing user friction.

The Passport team has done an outstanding job with this model and we're very happy to be working with them. 

However, we should make a caveat: the Model-Based system may look more effective today because no attacker has yet had a chance to game this system. On the other hand, people have had many rounds to try and game stamps. We’ll have to reevaluate our strategy as the attackers evolve continuously.

# Path Forward

Given these lines of analysis, we are planning for Gitcoin to use COCM and Passport Model-Based Detection as its sybil resistance tools for GG20. We believe this strategy will result in better funding outcomes for grantees and simultaneously reduce donor frustration.

We also used COCM in GG19 and have since offered it in an extremely limited-beta to select partners. We’re happy to share that we’ll soon be rolling COCM out as an option for all our partners.

As we’ve mentioned above, no sybil resistance strategy will be foolproof. However, to the best of our knowledge, this is clearly the best path forward with our current available tools.

-------------------------

QCH | 2024-04-06 16:37:02 UTC | #2



---

Thanks for sharing this detailed overview of Gitcoin's sybil resistance strategy for GG20. It's great to see the thoughtful approach you're taking to enhance user experience and address the challenges posed by sybil attacks. The combination of COCM and Passport's Model-Based Detection seems promising, and I'm looking forward to seeing how it contributes to better funding outcomes for grantees. Keep up the good work!

-------------------------

skilesare | 2024-04-15 15:27:19 UTC | #3

While this tech looks cool and it will be very interesting to see how it all plays out, I am left a bit frustrated. I'm trying to bring in a new community that likely has done very little on ethereum in the past. It sounds like they won't be eligible for any kind of grant matching?

I guess I'll just encourage them to get started so things will be in place for GG21, but It seems like I said something similar about building up their passport last season. (https://x.com/ICDevs_org/status/1729525201791017374)

Although I guess if we do find a hands-off approach it will be very welcomed by those donating that don't want to make it feel like a job.

-------------------------

meglister | 2024-04-15 17:55:02 UTC | #4

hey @skilesare ! You've definitely highlighted a gap in our current implementation. Our goal is first to optimize the experience for web3-native folks, which we're addressing with Passport's model-based detection + cluster matching (as well as moving off PGN, as you called out in your post.) Once we've nailed that, we'll address the non-native audience needs, which likely means supporting fiat/credit card checkout.

-------------------------

ReneHdz | 2024-04-16 03:38:35 UTC | #5

That's a great form to give more powerful to the GG20. Awesome strategy guys! :smile: LFG! :potted_plant: :green_circle: :green_heart: Let's grow.

-------------------------

annastone-86 | 2024-04-22 14:01:36 UTC | #6

Hi Everyone,

I’m Anna Stone, and I am one of the founding members of the GoodDollar project, a 100% non-profit universal basic income protocol that operates on Celo, and has over 750,000 members. We have raised funds in various Gitcoin rounds over the years, but most recently for a climate finance dapp built on top of the GoodDollar payment infrastructure, which raised in Gitcoin rounds 18, 19.

I’d like to hear from the team how they believe this proposed change will affect participation in Gitcoin 20. My particular concern is the effect it will have in excluding from QF matching many thousands of users who have participated in the most recent climate and community education rounds that have been run on Optimism and Arbitrum, respectively, and will not show activity on Ethereum. From my perspective this proposed change doesn’t properly balance the need to make Gitcoin an accessible and a useful fundraising product for hundreds of public goods minded organizations that need to raise funds vs. the need to reduce fraud and abuse. Is there a known problem of abuse in past rounds that this proposal is designed to protect against? If so, I’d love to learn more. 

Community education and climate projects are often small and under-funded in nature - their community members are often only able to give small amounts of money ($1-10). I believe this is driving reason behind moving the community and climate rounds to L2s, due to the cost barrier of donating small amounts of funds on Mainnet. It was simply too expensive to motivate mass participation, and excluded thousands of individuals who wanted to give small donations in Gitcoin rounds. However, the shift to L2s created thousands of new Gitcoin users drawn to the promise of QF to “give a little, but make a big impact” - particularly as big partners were brought in giving $100k+ in matching funds. I am sure the Gitcoin team and community knows the stats better than me - but this promise has driven thousands of new Gitcoin passport and Grantstack users over the last few rounds. In Gitcoin 20 Climate Solutions, which has over $300k in available matching funds - this is a big deal for small projects - and they have been able to mobilize and convert their communities into donors accordingly. The people who often donate in these round are often not “native Ethereum users” (though they often can connect dozens of Passport stamps!). On the contrary, I would predict there are a relatively low number of wallets that are “native” Ethereum that donate into the community climate & community rounds.

I personally know many individuals who have onboarded to Web3 via Gitcoin and the promise of QF in past rounds - but they onboarded directly to Arbitrum & Optimism where the rounds were taking place - and created passports via Stamps. How does this proposed change effect these past donors? Will their past donation history qualify them as passing sybil, and qualifying for QF? 

My comments apply to the Community Rounds which have been designed to support public goods accessibility - and less the OSS / dapp / Infrastructure  rounds, which I think are more appropriate “market contexts” for implementing COCM and Passport’s model based detection strategy to experiment with. 

While I admire and commend the innovation here, I’d encourage the Gitcoin community to think practically about what this proposed change will have on community projects like ours (and hundreds of others) that rely on small donors without Ethereum activity - and have worked hard to onboard hundreds of new users into Gitcoin, educate them about QF, convert people to small donors, and watch the magic of public goods funding at work. Given the significant amount of matching funding available in the community rounds in GG20 - I predict this will reduce participation, and ultimately raise questions of fairness in a relatively small number of wallets will dictate the ultimate distribution of matching funds based on the new Sybil strategy. 

Gitcoin Rounds continue to be foundational to supporting our work (and many others), so thank you for all you’ve done to support public goods, and taking the time to consider a community project’s perspective.

-------------------------

meglister | 2024-04-23 22:11:34 UTC | #7

Hi @annastone-86 and thanks for your comments! I appreciate your perspective on new/non-native users! As noted above, this is definitely our next priority to solve for. 

Each of the community round operators were given the option to continue with Passport stamps or use the Passport model-based detection system. Many that opted to use the model based system noted that onramping funds and bridging to an L2 presented enough friction to their non-native users that it was a bigger factor than Passport in preventing donations. We hope to tackle this concurrently with identity verification through a direct fiat onramp or credit card based checkout.

-------------------------

ASTRO-HSU | 2024-04-24 09:25:01 UTC | #8

I'm pleased to see the efforts made by Gitcoin Passport to effectively combat Sybil attacks, but I'd like to provide feedback from the perspective of a participant in Taiwan. The decision to adjust the score of the Coinbase stamp to 16.04, making it as crucial as Ethereum usage records for 'Humanity Score' seems quite unreasonable.

While this may not be a problem for many, it's important to note that Coinbase is a centralized exchange. Many might not be aware that in September 2023, Coinbase announced the expulsion of users in Taiwan from its platform, affecting both new registrations and existing accounts. Is it fair for Gitcoin Passport to use a Coinbase account as a determinant of a wallet being controlled by a real person?

As someone from Taiwan, I envy those who can use Coinbase normally, accessing numerous rewards through Coinbase Wallet and being recognized as real individuals on Gitcoin Passport. However, the issue lies in the fact that Coinbase is not a foundational infrastructure of Web3. If Coinbase is acceptable, why not Kraken, Binance, or other centralized exchanges?

Gitcoin Passport has set a threshold of 20 points to qualify as a real person, but merely having a Coinbase account can earn someone 16.04 points. This creates a significant disadvantage for those without access to a Coinbase account. Essentially, it's as if we are preliminarily labeled as potential bots, forcing us to work harder to collect additional stamps or spend money to prove we are 'real'. This is unfair and needs adjustment.

As a Gitcoin Citizen, I fully support Gitcoin's role in global public funding and hope that my voice encourages Gitcoin to consider participants outside the United States more broadly in future decisions. We are real people, but centralized services can choose not to serve us, which contradicts the foundational principle of equality in Web3.
![Discord Chat IMG 1967|230x500](upload://nnTRH2htSDcva2FQv6ny4lMlKMj.webp)![IMG_1968|245x500](upload://l6bDfLU2sBldarsvvPj0R2JJ4.jpeg)![IMG_1969|274x500](upload://v7vJoWqYRscae8xVEX0At1RhPdJ.jpeg)

-------------------------

deltajuliet | 2024-04-25 19:03:30 UTC | #9

Well put @ASTRO-HSU, appreciate your sharing. I get the frustration, and I'm sure you've seen the notes on [Twitter](https://twitter.com/gitcoinpassport) this week. I think it's useful to surface here so that @meglister and team can take into consideration for GG rounds and of course in the Passport product itself. 

Added some notes below, mostly musings.  

[quote="ASTRO-HSU, post:8, topic:18524"]
Is it fair for Gitcoin Passport to use a Coinbase account as a determinant of a wallet being controlled by a real person?
[/quote]

I would personally call this equitable - humanity is a sum of our parts, Passport humanity - a sum of our stamps. While you are unable to get the CB stamp, others may have a difficult time getting others. It's not necessarily Pokemon for identity and reputation, the team looks at the unique aspects that make up the humans and sybils. You don't have to collect them all, but appreciate your note on the weighting. You'll see below that it's still possible to get a score without it tho. What are your thoughts on that? 

[quote="ASTRO-HSU, post:8, topic:18524"]
However, the issue lies in the fact that Coinbase is not a foundational infrastructure of Web3. If Coinbase is acceptable, why not Kraken, Binance, or other centralized exchanges?
[/quote]

Totally agreed here, and I balk at most things centralized. The team is working to get Binance and OKX to also share KYC verification in a non-doxxing way. @kyle and @Jeremy are working on this. 

[quote="ASTRO-HSU, post:8, topic:18524"]
This creates a significant disadvantage for those without access to a Coinbase account
[/quote]
Mmm I disagree here. I don't have a CB stamp, and a score of 41 after the refresh. Happy to share the stamps I've collected as well. I'm a Gitcoin contributor, but this is a personal wallet so no bags here. 
![Screenshot 2024-04-25 at 8.46.40 PM|690x448](upload://2IusrZ2NrCVdWLXVp3IuWLT8slF.jpeg)



[quote="ASTRO-HSU, post:8, topic:18524"]
Gitcoin to consider participants outside the United States more broadly in future decisions.
[/quote]
YES! I love this. We would love to hear input on who to consider in terms of driving partnerships so that we can make the stamps more equitable worldwide, and not just N.American centric. 

Either way, I hope that helps bring a bit of clarity. I think that what the Gitcoin team is doing for GG20 in terms of data analytics is wildly useful (@umarkhaneth crushes data like Pez) and this strategy is only going to bring funds into the hands of ppl that need it most/are real humans! If you want to talk further on Passport specific stuffs though, my (virtual) [door is always open](https://calendar.app.google/bJ4uzpuQi7ZupmJE8).

-------------------------

meglister | 2024-04-25 20:04:33 UTC | #10

Thanks @deltajuliet and @ASTRO-HSU for the thoughtful notes! I do want to clarify that we are not using stamp-based Passport for any of the current Gitcoin Grants rounds, so the issue you describe will not impact your ability to allocate matching funds. We are instead using Passport's model-based detection service, which relies on over 60+ signals of on-chain activity to determine proof of humanity.

-------------------------

ASTRO-HSU | 2024-04-26 01:44:33 UTC | #11

Thanks @deltajuliet and @meglister  responses. It pretty helpful. I want to clarify something for better for myself and communication with participants. For small donors participating in Gitcoin Grants 20, can we say that they don't need to check their score on https://passport.gitcoin.co/ at all, and just directly donate to the projects of their choice on Gitcoin Grants?

I'm asking this because the current Gitcoin Passport interface is a bit confusing. When you first log in, you receive a Default Humanity Score, which I assume is provided by the model-based detection. However, if you connect any stamp, that score gets overridden and the model-based detection score disappears.

So, I want to confirm: For Gitcoin Grants 20, is it correct that only the initial model-based score is recognized, and any subsequent stamp-based scores have no impact?

Additionally, if a stamp is connected and we want to revert to seeing the model-based detection score, how would we go about that?

-------------------------

meglister | 2024-04-26 15:21:02 UTC | #12

> For small donors participating in Gitcoin Grants 20, can we say that they don’t need to check their score on https://passport.gitcoin.co/ at all, and just directly donate to the projects of their choice on Gitcoin Grants?

That's correct! There is no interaction required with Passport for GG20 rounds. I don't personally work with the Passport product and know that they just introduced some updates, so I will tag @Jeremy to answer your questions in full.

-------------------------

noahchonlee | 2024-04-30 06:32:09 UTC | #13

Hi @umarkhaneth I looked through the link but it doesn't appear to explain COCM and only explains pairwise and cluster matching. What is the "connection-oriented" part?

-------------------------

noahchonlee | 2024-04-30 06:39:26 UTC | #14

Hi @meglister at viaPrize we are also trying to make the onboarding easier for web2 people
We broadly had 2 solutions:

1. Users can log in with self-sovereign wallets OR sign in with dev-controlled wallets (we have custody of the wallets instead of the user)

Basically it means people can choose the ease of use of web2 or the sovereignty of web3
If they choose the wallet we control, they can log in with just an email OTP for account abstraction and make a username and they don't need to worry about keys or wallet addresses or anything

2. All users have self-sovereign wallets, and for people contributing with credit card we take that fiat and mint a stablecoin (such as Glo dollar) and then we add that stablecoin to the smart contract on behalf of the user but track their contribution history through mutable NFT metadata that is associated with their account

For automating swap, we have a uniswap integration to automatically do that for everything that's on one chain, but for bridging we haven't built that yet
Mostly we are focusing on web2 users who will use credit card, anyways

-------------------------

Joel_m | 2024-04-30 21:36:26 UTC | #15

The algorithm described in the blog post as "Cluster-Match QF" is the same as COCM! COCM stands for "Conenction Oriented Cluster Match". We could probably do a bit better with getting all the names in line around here.

-------------------------

Jeremy | 2024-05-01 21:17:29 UTC | #16

Heya @ASTRO-HSU sorry for any confusion. When you log into https://passport.gitcoin.co/ you will the see the Default Humanity Score in the top left. This is the cumulative score from all of the stamps that you have collected in Passport. 
This is NOT the model-based detection score, that is a separate score provided outside of the Passport UI.

-------------------------

thedevanshmehta | 2024-05-02 08:34:55 UTC | #17

[quote="Joel_m, post:15, topic:18524"]
We could probably do a bit better with getting all the names in line around here.
[/quote]

I did love @DisruptionJoe framing of cluster QF as "correlation discounting"

-------------------------

ASTRO-HSU | 2024-05-04 02:22:23 UTC | #18

Thanks! Would like to know if there is any way for users to find out whether their donation will be matched ?

-------------------------

skilesare | 2024-07-17 15:21:09 UTC | #19

I'm bumping this with hopes I can help alleviate some of the issues for my community that caused us to get a dismal GG20 matching score and fix that for GG21. Most of our community is non-native ETH users and I'd like to do what I can to prep them so that they don't look like a bunch of Sybils.

1. Does going to passport and adding stamps help at all? If not I don't want to ask them to do it.
2. We have a mechanism to bridge ETH to our community and I'm wondering if encouraging them to do that would help?  It would mostly be people sending ETH to the bridge contract: https://github.com/dfinity/ic/blob/master/rs/ethereum/cketh/docs/cketh.adoc#deposit-eth-to-cketh

Are there any other Proof of Humanity things that can be done?

What does it look like if people were donating directly from a common smart contract?  For example, if we built a dapp for people to withdraw their ckETH directly to a donation address, would that get registered as a donation, or do they need to call an allo contract directly? If they all deposited from the same contract I'm guessing that would look pretty Sybily?

Thanks for helping me understand how the new mechanism works!

-------------------------

Sirlupinwatson | 2025-03-30 10:23:11 UTC | #20

[quote="umarkhaneth, post:1, topic:18524"]
known human and sybil addresses
[/quote]

Hi there, what is the current sourcing for this data sequence?

[quote="umarkhaneth, post:1, topic:18524"]
If we were to use Model-Based Detection instead of Stamp-Based
[/quote]
Passport scores never really compiled properly within each rounds, so results or metrics must have been dramatically high with error state or false positive
"either a specific stamp is not added to the overall score, or a requirement execution run into an issue as the user side"

And current vision might endure a higher numbers of fraudulent transaction, since I can easily for example create (some agents with post dated or pre-dated commits and contributions to add at my portfolio)

Prior step 1, the quadratic strategy would be void already in some way. 

Let's create a round especially for sybil attack, a free-for-all?

-------------------------
