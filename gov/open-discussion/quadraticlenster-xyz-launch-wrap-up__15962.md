---
id: 15962
title: "QuadraticLenster.xyz Launch Wrap-Up"
slug: quadraticlenster-xyz-launch-wrap-up
category: open-discussion
url: https://gov.gitcoin.co/t/quadraticlenster-xyz-launch-wrap-up/15962
created_at: 2023-07-26T16:11:06.590Z
last_posted_at: 2023-07-28T11:31:05.530Z
posts_count: 3
views: 3852
like_count: 7
---

# QuadraticLenster.xyz Launch Wrap-Up

<https://gov.gitcoin.co/t/quadraticlenster-xyz-launch-wrap-up/15962>
owocki | 2023-07-26 22:08:17 UTC | #1

*Thanks to Raid Guild, Lenster, Gitcoin, Stani, Nader, and everyone who helped with this launch!*

# The Vision

At EthCC, Supermodular announced the launch of a new integration with Lens Protocol that will bring Quadratic Funding (QF) to web3 social apps.

The pilot launch was QuadraticLenster.xyz, a web3 social media app with funding mechanisms embedded in the newsfeed. The first QF round ran from July 17 to 25, 2023, and allowed all Lenster users to reward creators or organizations they value during the week of EthCC. By leveraging [Gitcoin’s Allo Protocol](https://allo.gitcoin.co/), users could tip any post that mentions #ethcc and tap into the $10,000 USD matching pool.

Our vision for this launch was: “QF transforms posting on social media into a lucrative income opportunity for creators, enabling popular posts to magnify earnings. It also creates a virtuous cycle where social media rewards the most active creators of public goods and other prosocial behaviors. We are replacing ‘likes’ with tips, which can be further amplified by Allo matching pools; this new feature can stimulate positive behavior through economic incentives and create a more regenerative and less divisive social media experience.”

With QF, the number of contributors matters more than the amount funded. Relatively small tips can have large impact, propelling a $1 USD tip to have $100 USD worth of impact (or more, if a post has many contributors). In each instance, a matching pool is raised and tips from the crowd are matched according to the number of tips via the QF algorithm. This unique funding mechanism, [conceived by Vitalik Buterin, Glen Weyl, and Zoë Hitzig](https://scholar.harvard.edu/hitzig/home), has been used to [fund $50m worth of public goods on Gitcoin](https://impact.gitcoin.co/) through 18 matching campaigns.

Stani Kulechov, Founder and CEO of [Aave Companies](https://aave.com/) said: “People need public town squares that enable positive-sum behavior so that individuals as a community can align their contributions towards a collective movement. As a social networking initiative, QF for public goods has the incredible potential to support positive actions that benefit us all.”

This integration brought public goods funding, popularized by Gitcoin, and embedded it into the Lens ecosystem.

During the pilot round, users could go to https://quadraticlenster.xyz/, find a post with the #ethcc hashtag, and click the ‘send tip’ button. If you are a creator, you can create a post with the #ethcc hashtag and begin to receive tips and access the matching pool.

# The Launch

Watch the talk @ [https://www.youtube.com/watch?v=-zT9l63LkEU or click below![|624x357](upload://7TZMzZKQoePQOHN70xelOmIK1h8.jpeg)](https://www.youtube.com/watch?v=-zT9l63LkEU)

I also did a podcast episode with Glen Weyl (QF Paper Author) on this experiment.  Watch it here: https://www.youtube.com/watch?v=bikJSo7qnDU

[![Screenshot 2023-07-26 at 4.08.01 PM|690x401](upload://cOqhHI6papQt8TjbP5VG0DzykSi.jpeg)](https://www.youtube.com/watch?v=bikJSo7qnDU)


# The Goal

My goal for the pilot round is to validate these ideas:

1. This could be an easier way to onboard people into quadratic funding.  Our goal was 100 contributions.
2. Microtransactions have long been a dream for people who want to fund a better internet, and move us away from the attention economy. But people don’t care about the micro-transactions, they are too micro. What if quadratic funding can solve this by making a 30c microtransaction worth $10?
3. People spend 15 minutes per quarter funding grants on Gitcoin, is there potential inputting the mechanism behind Gitcoin into social networks they spend hours per day on?
4. We can use social media to algorithmically upregulate public good (instead of just things that hijack attention).
5. Gitcoin 1.0 had a [QF social network component to it](https://gov.gitcoin.co/t/a-quadratic-funding-powered-social-network/9462), now that web3 social is here, we could revive this in a Gitcoin 2.0 world.

# The Experiment

Raid Guild + Supermodular built a Lenster.xyz fork that leveraged [Allo Protocol](https://allo.gitcoin.co/) to implement quadratic funding on tips, and launched a $10k QF round (which i will fund) for anyone whos talking about #ethcc on quadraticlenster.com (our lenster fork), and we get at least 100 contributions + positive buzz about the tool. Here’s what it looked like:

## Creating a post

![|624x563](upload://2PKJSirjlX0yvHh7NKTjKbt97ZK.png)

## Sending a tip

![|624x421](upload://t1tEbbx4OxrH96GGQUPvobvUIhA.jpeg)

## How the match multiples work:

![|425x219](upload://yWikoR98YmjUHCp50w3WaZ9fnx0.gif)

## Viewing a post that has tips & matching

![|624x336](upload://46s37VVKBSXvJTLvyhjczBfUX3e.png)

# The Results

I am happy to say that the round was a moderate success!

Here are some stats:

* Round Start: 7/20 - 7/25
* Contributions: 581
* Unique Contributors: 181
* Total contributions: $4.9k (6.9 WMATIC)
* Round Size: $10k (12k WMATIC)
* Top Posts: You can view the top posts in the round at https://www.quadraticlenster.xyz/rounds-overview

## The good:

1. [Payouts are out!](https://www.quadraticlenster.xyz/posts/0x01cf85-0x10)
2. We contributed $10k and the community contributed $5k! Woo hoo for amplifying our own contribution.
3. We reached and (very much surpassed) our 100 contribution goal.
4. We successfully validated that it was easier to onboard onto Quadratic Funding Rounds by simply posting in a social media environment, we validated that people would send microtransactions when there are quadratic matches.

## Things to work on:

* The contracts were exploited and we had to redeploy them (more details [here](https://www.quadraticlenster.xyz/posts/0x01cf85-0x0b))
* We have seen some evidence the round was sybil attacked. An investigation is ongoing.
* Matching funding is required to keep this experiment going.
  * One idea for future sustainability is to have rounds themselves be funded through tipping; once they reach a threshold the round goes live. Like a climate round that then in turn can potentially fund posts made by reforestation, re-wilding initiatives etc.
* Our comms could have been better. People missed the announcement, drowned out with other ethcc news. For some reason, we never sent the press release out during launch. (This might be on me for not cat herding better)

##  Final thoughts

* I’m thrilled with the participation we saw. I imagine we can see 100x-1000x these results if we can get this QF tipping module distributed to the rest of the lens network,I’d even venture to say that it would be a killer feature for Lens as more creators begin earning an income from QF.
* Over the next 18 months, I expect that we will see this re-built on top of Lens v2 and Allo protocol v2. (so that it works inside Lensster.xyz + Orb + all other Lens enabled social apps).
* In the first version, we sponsored the #ethcc hashtag. In the next version, we will allow anyone to sponsor any hashtag.
* I would like to double down on this QF form factor, the ideal end state will be to have many sponsored QF rounds happening at the same time on social media, upregulating pro-social/public goods behavior. Perhaps one way to start would be to have normal Gitcoin rounds have side-car QF rounds on Lens to allow a broader swatch of humanity.
* It was interesting to observe the content that emerged from the round. From people writing up [great explainers](https://www.quadraticlenster.xyz/posts/0x01a14e-0x011f) to using the platform for [development funding](https://www.quadraticlenster.xyz/posts/0x01cdd5-0x01).

-------------------------

carlosjmelgar | 2023-07-27 11:20:23 UTC | #2

Congrats, this was well executed! I'm excited about SoMe users using QF without knowing wtfisqf. These innovations allow for meaningful adoption of tool stacks by making it more vibey and less nerdy. 

[quote="owocki, post:1, topic:15962"]
It also creates a virtuous cycle where social media rewards the most active creators of public goods and other prosocial behaviors.
[/quote]

This is such a powerful concept, looking forward to seeing this become a reality. 

[quote="owocki, post:1, topic:15962"]
“People need public town squares that enable positive-sum behavior so that individuals as a community can align their contributions towards a collective movement. As a social networking initiative, QF for public goods has the incredible potential to support positive actions that benefit us all.”
[/quote]

Wen GHO? Stani is big on the idea of programming values into money. Would love to see GHO integrated in the future. 

[quote="owocki, post:1, topic:15962"]
Matching funding is required to keep this experiment going.

* One idea for future sustainability is to have rounds themselves be funded through tipping; once they reach a threshold the round goes live. Like a climate round that then in turn can potentially fund posts made by reforestation, re-wilding initiatives etc.
[/quote]
Would you consider ad revenue for this? i.e. funding partners get a sponsor banner on the site + GP episode + tweets + hypercerts reflecting whatever impact was created during the round. 

Crowdfunding campaigns for the matching funding can align with things like World Ocean Day, Earth Hour, Earth Day. The QL account can make daily posts announcing the raise for the upcoming rounds, allowing used to contribute leading into the round. 

Feedback: 
I spent the first few days posting from mobile. Txns appeared to send but didn't actually post. I didn't realize this until I opened my laptop a few days later.

-------------------------

Viriya | 2023-07-28 11:31:05 UTC | #3

[quote="owocki, post:1, topic:15962"]
Matching funding is required to keep this experiment going
[/quote]

I wonder if we can experiment with this in GG round marketing. Ad spend (which we don't normally do btw but could front a small matching fund for the experiement) could go to the matching pool instead of boosted posts. We could track engagement with the campaign through a hashtag and distribute the pool retroactively. 

I think it could be really interesting as A LOT of community members produce incredible content during the round to support grantees and their communities...all for free! Would be awesome to show them our appreciation as a community. 

I would feel more comfortable doing this when Lens figures out it's bot problem. Candidly, my experience there has mostly been interacting with bots so it's kinda lame but I LOVE the concept of Lens and QL. Do they have plans to integrate Passport or some other form of POH? Also, I don't have a Lens profile bc I'm not cool enough...I'd love to continue to partner and experiement with Lens across the board, especially once it's more widely available.

-------------------------
