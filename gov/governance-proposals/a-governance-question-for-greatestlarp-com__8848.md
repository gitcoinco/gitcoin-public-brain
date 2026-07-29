---
id: 8848
title: "A governance question for GreatestLARP.com"
slug: a-governance-question-for-greatestlarp-com
category: governance-proposals
url: https://gov.gitcoin.co/t/a-governance-question-for-greatestlarp-com/8848
created_at: 2021-10-22T10:39:17.947Z
last_posted_at: 2021-12-10T17:12:26.506Z
posts_count: 35
views: 6762
like_count: 51
---

# A governance question for GreatestLARP.com

<https://gov.gitcoin.co/t/a-governance-question-for-greatestlarp-com/8848>
owocki | 2021-10-22 10:39:52 UTC | #1

![FCOeEKKUcAQto0g|690x388](upload://zTgpYHmGQmGpiFROoZqsLa2K5D0.jpeg)

At Liscon, the moonshot collective launched http://greatestlarp.com/ - a coordination game about coordination games.  In this game, the main character is leading us through each of the 5 levels, starting with level 1 - where you can read about The Greatest LARP in Comic book form, level 2-4 which are NFT auctions, and level 5 which is the "you win" level.  The game starts with "Moloch is winning" and ends with "the good guys win".  The whole point of the game is the community has to coordinate to win the game.  

Read more about the game mechanics  [here in this twitter thread](https://twitter.com/owocki/status/1451180297827930114).  Or checkout this video of Kevin announcing this game on stage [here](https://vimeo.com/manage/videos/637530828)

Here's what the levels look like:

![FCOeqrKX0AASOwh|690x161](upload://4nu7Jo4mvo1KbaPpG9StteId1Z0.jpeg)

Level 2 is an NFT auction on a bonding curve.   Here's how to play according to the copy on the site. 

> Moloch is made of coordination failures, and the only way to beat a monster like that ... is more coordination.
> 
> ETHBots are built to coordinate. They are configured by the community they serve to create coordination. They are the vessels through which humanity coordinates to defeat Moloch.
> 
> To play this level, launch a new hero into the world by minting their NFT. Once 200 Digital ETHBots are minted (155 minted so far), and 3 Statue ETHBots are minted(4 minted so far), humanity can begin its fight against Moloch.

OK so TLDR - once 200 ETHBots are minted, then the community can get to the next level.  Awesome, we're 76% there right?

Well.. if you [look at the price function](https://docs.google.com/spreadsheets/u/1/d/1__uH78nJVYmpwR1XYzgNbz8hCQjz3ONU6fQcOCex7nE/edit#gid=0) on the level, youll see that the price grows exponentially over time as more units are sold.

![Screen Shot 2021-10-22 at 4.14.13 AM|690x423, 75%](upload://k8A4F43H8oBXHIWp24Ht9bZ6Ptd.png)

Lets zoom in on where the community is now, at 155 units sold: 
![Screen Shot 2021-10-22 at 4.22.53 AM|690x418, 75%](upload://jIufTXpIjJOTamPEUxCQCy4gvlb.jpeg)

Looks like the current price for one of these ETHBots is 1.34 ETH, and the price will increasing to 6.6 ETH by the time 200 bots are minted.

Will the community want too pay 1-6.6 ETH per NFT for the next 45 NFTs in order to beat the level?  

# womp womp womp

Well, thats a great question.  And thats why the community built in a mechanism we call the "womp womp" mechanism.  The "womp womp" mechanism reduces the price by 10%.  [Checkout the code here](https://github.com/moonshotcollective/anon-vs-moloch-nft/blob/develop/packages/hardhat/contracts/GreatestLARP.sol#L115).  We call it womp womp because we think using the mechanism sounds like a [sad trombone](https://www.youtube.com/watch?v=tKdcjJoXeEY).  

Here's what the price curve looks like with 1 womp womp.

![Screen Shot 2021-10-22 at 4.30.48 AM|690x427, 75%](upload://wlwWPUsePLZM00lsVd3sTF2nf0e.jpeg)

and here's what itd look like if womp womp's were applied every few days, but the community still purchased the NFTs every few days too.
![Screen Shot 2021-10-22 at 4.31.10 AM|690x408, 75%](upload://vXKpfA9qamtAJKPP0eb21y04k87.jpeg)

TLDR: This mechanism is effectively a way to counter-balance the upward pressure of the price curve.  It is a release valve in case the curve is too steep.

# How do we  use it?

Which leaves us with the question:  should we use it?  if so, how should we use it?

We'd like to leave that question up to [governance](https://gov.gitcoin.co/t/gitcoin-dao-governance-process-v1/7860) - at least getting rough consensus on how it should be used.

To ground the discussion in the goals of the GreatestLARP project (and of broader GitcoinDAO, these are the stated goal of the project
1. spread the message as far and wide as possible
2. raise money for public goods.

So far so good on both fronts, the project has raised $180k in funding for public goods and the comic has been read 100s of times.

Some options for how the DAO proceeds on using "womp womp":
1. don't use it at all.  if the community doesnt consume the NFTs on current price curve, don't pass the level.  don't meet moloch.
2. use it whenever there is not a sale for 24 hours.
2. use it whenever there is not a sale for 7 days.
3. some other proposal (pls comment below)

-------------------------

Huxwell | 2021-10-22 10:54:07 UTC | #2

We could use the womp womp during a Twitter space and do a few "discount rounds", one at the start of the twitter space, one or two in the middle and then an open call for everyone to shill it for 4 more hours after which we would stop the womp womp.

-------------------------

MoonshotCoordinator | 2021-10-22 13:52:26 UTC | #3

I support the idea of using it (the womp womp) during a community live event.

Moonshot Collective's community call seems like a perfect opportunity! 

I'm happy to host another hype stage on Discord too, the launch day vibes were awesome and we convinced at least one statue purchaser to step up (thank you!). 

My only concern is that we might demoralize past and future buyers into thinking we'll always be ready to undercut pricing and they'd be incentivized to wait and see instead of jumping in.

I would favour announcing it (like we have here :slight_smile: ) and committing to only using it at certain preannounced events.

-------------------------

owocki | 2021-10-22 14:30:45 UTC | #4

> My only concern is that we might demoralize past and future buyers into thinking we’ll always be ready to undercut pricing and they’d be incentivized to wait and see instead of jumping in.

I do think it’s important to have a clear and predictable policy for this reason.

-------------------------

matthewcarano | 2021-10-22 17:26:20 UTC | #5

To me, using objective criteria to trigger the womp womp is preferable. In particular I like based on lack of sales (no sales in x timeframe = y% mint price reduction). Feels more blockchainy for one thing, but also gives us predictable events we can use to spread the project.

-------------------------

M0nkeyFl0wer | 2021-10-23 01:29:35 UTC | #6

I'm all for using the womp womp to incentivise more sales during twitter spaces or discord calls. I see it as another form of coordination. Sharing the story of enabling this strategy to keep prices down so we all can come together is an interesting narrative in and of itself.

-------------------------

M0nkeyFl0wer | 2021-10-23 01:43:30 UTC | #7

Personally I won't feel discouraged by keeping prices around what I paid. I actually didn't know the price was going to go up at first and then really regretting not getting up 
off the couch with the dogs to go get my bot sooner. Hahah but it's all good I wanted to support public goods and I got a bot I love. 


![Screenshot_20211020-163145__01|494x500](upload://vKMPx6esZSksgcCD62Lf8SAkPkf.jpeg)

Point being I think as long as people keep buying in and we move forward in the mission together that is the most encouraging thing. Promos during discord calls or twitter spaces is totally fair game and will just continue raising awareness for the project. It will be the strength of the community that gives the project value ultimately.

-------------------------

Colton | 2021-10-23 16:07:12 UTC | #8

Womp womp time! 

I agree it could be fun to do the first one during a community call. Then trigger another every 24 hours if a bot is not sold (or perhaps more often). 

Excitement is growing, but it could fade fast. This system will play out again on level 3 leading to a LARP that takes weeks or more. That's a long time in crypto.

-------------------------

David_Dyor | 2021-10-23 22:43:40 UTC | #9

Just like the tip.party brings people to meetings I think the Womp Womp will bring people to sales.  I like option #2.

Things happen fast and if no sales in a day...things don't look good.

-------------------------

owocki | 2021-10-24 15:18:50 UTC | #10

[quote="Colton, post:8, topic:8848"]
I agree it could be fun to do the first one during a community call. Then trigger another every 24 hours if a bot is not sold (or perhaps more often).
[/quote]

seems like people are coalescing around this as the path forward.  

perhaps the womp womp can be the same time every day to create consistency/predictability

EDIT: i may also suggest allowing 2 womp womps per 24 hours, as in [season 3 the curve is much more steep much faster](https://docs.google.com/spreadsheets/u/1/d/1__uH78nJVYmpwR1XYzgNbz8hCQjz3ONU6fQcOCex7nE/edit#gid=0)

-------------------------

okeaguugochukwu | 2021-10-25 13:25:39 UTC | #11

nice idea ...I propose to it, keep it up.

-------------------------

ObayaDevOps | 2021-10-25 15:24:07 UTC | #12

The community call idea is great

-------------------------

Sandy-Seaweed | 2021-10-25 15:52:11 UTC | #13

Hi @owocki I'm in favor of using the womp womp twice every 24 hours. I think the benefits of raising more funding for public goods outweighs the negative externalities of influencing the bonding curve and corresponding prices. As a Bot holder myself, I'm supportive of this approach, thanks!

-------------------------

Ethnation | 2021-10-25 16:05:14 UTC | #14

I think option 2 will help sustain momentum and help us reach a threshold where we can move ahead more reasonably.

-------------------------

blaylockcomics | 2021-10-25 16:08:06 UTC | #15

Comic creator here. I am all for multiple womp womps a day! Three or four.

-------------------------

Lam | 2021-10-25 16:13:36 UTC | #16

Sers, I propose we WOMP WOMP immediately. Then we pay Steve Aoki to do a cameo saying WOMP WOMP. Fomo ensues and the coordination of ETHbots will surely hit power levels over 9000 to defeat Moloch. Option 2 is also nice.

-------------------------

MoneyManDoug | 2021-10-25 16:30:19 UTC | #17

I also really like that idea, the community calls usually bring in a decent amount of exposure.

-------------------------

Lautaro | 2021-10-25 16:36:05 UTC | #18

I support using a wompwomp if there are no sales on the last 24hs, althought i also like the idea of using it on special events, such as twitter spaces or conferences.

-------------------------

blaylockcomics | 2021-10-25 16:41:48 UTC | #19

Womp Womps could not kick in until prices reach a certain level.

-------------------------

owocki | 2021-10-25 17:49:19 UTC | #20

Hey all, its hard to parse the responses in freeform.  Can you please vote on this poll? 

After 36 hours Ill plan to close the poll + we can institute the policy.

[poll type=regular results=always chartType=bar]
* No womp/womps
* 1 womp/womp every 24h with no sales
* 2 womp/womp every 24h with no sales
* 3 womp/womp every 24h with no sales
[/poll]

[poll name=poll2 type=regular results=always chartType=bar]
* Do it at the same time every day.
* Do it on community calls + communicate those ahead of time.
* Both.
[/poll]

-------------------------

amy | 2021-10-26 23:23:18 UTC | #21

[quote="owocki, post:1, topic:8848"]
Well… if you [look at the price function ](https://docs.google.com/spreadsheets/u/1/d/1__uH78nJVYmpwR1XYzgNbz8hCQjz3ONU6fQcOCex7nE/edit#gid=0) on the level, youll see that the price grows exponentially over time as more units are sold.
[/quote]

Maybe this is a dumb question, but why a price increase? In this case, it feels coordination across 200 people purchasing 200 NFTs feels sufficient than coordination with increasing prices which may push out others from coordinating.

-------------------------

AdamJ | 2021-10-27 04:39:45 UTC | #22

Agree - it doesn't really serve the community to have a price curve that stretches into the stratosphere (exaggeration) just as we are wanting to onboard new members. And I would also not be concerned if prices didn't rise after I purchased.

-------------------------

owocki | 2021-10-27 13:11:04 UTC | #23

The goal of the campaign is twofold:
1. spread the word about the fight against moloch
2. raise money for public goods.

To your point; the price support is probably in support of the 2nd goal over the 1st goal.  But the womp womp is designed to balance this out.

-------------------------

owocki | 2021-10-27 13:11:46 UTC | #24

Poll is now closed, here is the results.

![0f15a14a-62d5-4334-942d-5929bfab38ae|627x499](upload://j1FseHMGaCVUyGf61fQgZwThiPf.jpeg)

Ill plan to execute the womp womps around 9am MST every day, and will post in the telegram channel about it when the txns are submitted.

-------------------------

owocki | 2021-11-01 15:41:42 UTC | #25

Posting this [on behalf](https://t.me/c/1505231312/2111) of @Colton 

**Womp Womp V2:**

The womp womp was designed to strike a balance between (1) spreading the Moloch lore and (2) funding public goods.

Eventually, the current womp womp will unlock the next level, but keep in mind, this same system plays out again on the next level. If this level takes 3-4 weeks, the next level takes 3-4 more. And there's still a final level after that!

*Crypto moves fast and this auction must consider the ecosystem's pace to maximize public goods funding.*

There were no womp womps this morning because a single sale happened 21 hours ago. We have clearly not found a level most participants will engage with, and delaying a womp womp is unnecessarily dragging this process out.

**I propose we womp womp every 24 hours, regardless of sales. When people start buying again, the bonding curve + womp womp will stabilize the price.**

Can you please vote on this poll?

After 36 hours I'll plan to close the poll. Kevin has agreed to "folllow the lead of whatever the community decides".

[poll name="Womp Womp V2"]

- Womp womp every 24h, **regardless of sales**

- Don't change anything. The current Womp Womp works

[/poll]

How many womp womps should happen each day?

[poll name="How many per day"]

- 1 womp/womp every 24h

- 2 womp/womp every 24h

- 3 womp/womp every 24h
- 4 womp/womp every 24h
- 5 womp/womp every 24h

[/poll]

-------------------------

owocki | 2021-11-09 15:40:30 UTC | #26

The community has beat level 2 + we will be moving on to level 3!

> Eventually, the current womp womp will unlock the next level, but keep in mind, this same system plays out again on the next level. If this level takes 3-4 weeks, the next level takes 3-4 more. And there’s still a final level after that!

Based on the above discussion + comments (in which the womp womp was being discussed as a method to beat the active levels), I am interpreting the "womp womp" policy to be applicable to the current active level.   If people feel we need another poll to disambguate womp womp across multiple levels, please feel free to post another poll to measure that sentiment.

-------------------------

owocki | 2021-11-09 17:59:50 UTC | #27

Welcome to level 3 everyone!  here is the curve for level 3 at present:

![b88c556d-3eac-48c8-8802-7b56de447dfe|690x425](upload://9pawTjapauQ8ihEIAidC4fhKPwN.jpeg)

# Lets ratify a new womp wopm policy for level 3, this poll will last 36 hours:

How many womp womps should happen *no matter what* each day?

[poll name="How many per day"]

- 0 womp/womp every 24h
- 1 womp/womp every 24h
- 2 womp/womp every 24h
- 3 womp/womp every 24h
- 4 womp/womp every 24h
- 5 womp/womp every 24h

[/poll]


In addition to the base womp womps (above), should we add a bonus womp womp womp when the price is higher than 0.2 ETH?

[poll name="How many extra womp per day"]

- 0 extra womp/womp every 24h if the price is above 0.2 ETH
- 1 extra womp/womp every 24h if the price is above 0.2 ETH
- 2 extra womp/womp every 24h if the price is above 0.2 ETH
- 3 extra womp/womp every 24h if the price is above 0.2 ETH
- 4 extra womp/womp every 24h if the price is above 0.2 ETH
- 5 extra womp/womp every 24h if the price is above 0.2 ETH

[/poll]

In addition to the 0.2 ETH womp womp + the base womp womp, should we add a bonus womp womp womp when the price is higher than 0.4 ETH?

[poll name="How many extra womp per day above 0.4"]

- 0 extra womp/womp every 24h if the price is above 0.4 ETH
- 1 extra womp/womp every 24h if the price is above 0.4 ETH
- 2 extra womp/womp every 24h if the price is above 0.4 ETH
- 3 extra womp/womp every 24h if the price is above 0.4 ETH
- 4 extra womp/womp every 24h if the price is above 0.4 ETH
- 5 extra womp/womp every 24h if the price is above 0.4 ETH

[/poll]

-------------------------

Sandy-Seaweed | 2021-11-10 15:51:59 UTC | #28

Hi Kevin, I agree with the sentiment of using the womp womp with the conditions you have set above, until, we complete the level, at which point--I recommend no womps to be used in order to maximize any potential lagging sales, which would fund public goods. 

I have voted accordingly, and agree with general consensus of more womps to defeat the Moloch's. Thanks for everything you do. I'm learning a lot through this process.

-------------------------

owocki | 2021-11-11 15:52:23 UTC | #29

poll is now closed. here is the results.  

![Screen Shot 2021-11-11 at 8.51.54 AM|690x432](upload://rV7xQOaHMUzdXiQv0Ku2wUOsNBK.png)
![Screen Shot 2021-11-11 at 8.51.51 AM|690x442](upload://8S5dwVEZnbxij24xIFqRvCVE1zB.png)
![Screen Shot 2021-11-11 at 8.51.48 AM|690x369](upload://cXpC0uGMjtCl1hZZ7wRHApycXYN.png)

-------------------------

owocki | 2021-11-17 19:36:55 UTC | #30

edit: moving the poll to a new post now

-------------------------

MoonshotCoordinator | 2021-11-17 19:04:24 UTC | #31

MoonShotBots launching at our community call was a big win - perhaps we could launch the Final Boss at our call on the 6th?

-------------------------

owocki | 2021-11-17 19:36:05 UTC | #32

thank you for the suggestion. added that to the poll

-------------------------

owocki | 2021-11-17 19:37:03 UTC | #33

Hey everyone,

At the current pace of sales of 4-12 sales per day, and with 80 sales to go, Level 4 ([The Final Boss)](https://zora.co/collections/zora/5725) is about a week away. 

Its possible that the final boss will happen at night time, or during a holiday (US Thanksgiving is coming up).

Some ppl have come to me and told me that its important that for sale optics, it is important that we are able to co-market the final level together when the final boss goes live.

This leads me to the following poll.  What should the final boss go-live policy be?

[poll name="final boss policy"]

- goes live as soon as level 3 is beaten.
- goes live the next business day, at 9am MST.
- goes live after 2 business days, at 9am MST.
- goes live after 3 business days, at 9am MST.
- goes live after 4 business days, at 9am MST.
- launch at the next moonshow collective monthly call on the 6th at 1pm MST

[/poll]

For the purposes of the poll above, lets assume that [holidays as defined by this calendar](https://www.redcort.com/usa-business-holidays) are not business days.  And that weekend days are not business days.

-------------------------

owocki | 2021-11-21 14:07:08 UTC | #34

poll is closed; here is the results. see you at this event https://www.addevent.com/event/Jb7972221
![Screen Shot 2021-11-21 at 7.04.44 AM|690x400](upload://3T9BAWT2vdCtpESXFp5Vlugh4U3.png)

-------------------------

Colton | 2021-12-10 18:03:43 UTC | #35

Hi larper frens, 

Since the Greatest LARP launched, we've raised over $500k--all going directly to the Gitcoin Grants Matching Pool. 

You are all awesome. Seriously. 

We'll be doing a full retrospective on what we've learned so we can make the next fundraiser even more fun, but today we have one more decision to make as a community.

We have pooled 38 ETH in the final boss PartyBid, but momentum has slowed. It's time to decide on the biggest womp womp yet.

Please cast your vote, I'll close this poll in 24 hours. 

and remember, if you want the final battle POAP, join us in the GitcoinParty: https://www.partybid.app/party/0xA2db0A5687F7c1F685e2E62a917b40E3133B3D8E

[poll type=multiple results=always min=1 max=1 chartType=bar]
* Drop the Reserve to 40 ETH when this poll closes
* Drop the Reserve to 45 ETH when this poll closes
* Drop the Reserve to 50 ETH when this poll closes
* 100 ETH! I don't care how long it takes
[/poll]

-------------------------
