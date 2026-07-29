---
id: 11314
title: "Benefits of using Price of forgery in Gitcoin"
slug: benefits-of-using-price-of-forgery-in-gitcoin
category: governancevision
url: https://gov.gitcoin.co/t/benefits-of-using-price-of-forgery-in-gitcoin/11314
created_at: 2022-08-18T07:24:41.431Z
last_posted_at: 2023-08-13T00:03:19.032Z
posts_count: 5
views: 4463
like_count: 11
---

# Benefits of using Price of forgery in Gitcoin

<https://gov.gitcoin.co/t/benefits-of-using-price-of-forgery-in-gitcoin/11314>
porobov_p | 2022-08-18 07:24:41 UTC | #1

Wrote a follow up for the [Green pill episode on Price of forgery](https://twitter.com/owocki/status/1559599940887662594?s=21). Thought it fits as a post here. Please check it out. Happy to discuss.

# TL;DR

What benefits GC can get with known forgery price for every human verification (HV) method in use. I see three general things:

1. Accurate trust bonus
2. A solid data point to rely on when crafting a KPI or perfecting fraud detection
3. A way to monetise anti-Sybil and fraud detection efforts

Please see some thought-provoking advantages below. I’m sure I’m missing something. 

# WHY? Quantitative quality control.

### 🪙 Fairer trust bonus 🪙

Upala protocol ensures that Price of forgery (PoF) is defined by the market. Which makes Upala accurate, responsive and reliable (even bots cannot beat the market 😉). Every human verification method can be fairly and accurately measured with PoF.
 
The protocol can also detect if an HV method gets exploited in a new (cheaper) way. That allows to track reliability of HV methods over time.

### 🧚 Safer matching funds 🧚

PoF organically brings HV methods into money dimension. Which makes it easy to reason about capital allocation. Be it crafting KPIs or perfecting fraud detection techniques there is new solid data to rely on. The following may be of use:  PoF of a HV method, PoF across a group of users, total PoF of all users.

### 🍀 Monetising anti-sybil and fraud detection efforts 🍀

Gitcoin is a massive web2 to web3 gateway and a big trusted player already. Giving away passports here seems like a perfect resonator for the upcoming digital identity wave. 

In order for the pill to remain green it is essential that those passports are scored in decentralized, simple and transparent manner. PoF can provide that.

Further adoption of the passport will allow to monetise anti-sybil and fraud detection efforts through fees.

# HOW? Simple and fast integration.

Upala was made for GC. It can provide automated, transparent and ongoing PoF measuring.

### Easy to start 🍾

We can start today. Upala is perfectly compatible with Gitcoin passport architecture.

### Cost-effective 🌱

The price of forgery measuring can go in a gentle way. The ongoing cost of the method could be as low as the rate of users get hacked (meaning hacked the hard way - loosing their eth addresses).

### Invisible for users, tempting for bots 🍯

Ordinary non-malicious users are not required to take any actions to get their scores. They don’t even need to know. It is bots who actively participate in PoF measuring.

### Ready today 🎬

Upala is deployed on Gnosis (previously xDai) chain. Tools for mangers are below.

### Highly ****automatable 🦾****

It’s all numbers. Bots vs bots. Human factor is avoided 🤖

# WHAT. Links.

### Integration

- Upala protocol on Gnosis chain - [https://blockscout.com/xdai/mainnet/address/0xD404Fb7635dB26D783dd8D2DF87Be1c504436268/transactions#address-tabs](https://blockscout.com/xdai/mainnet/address/0xD404Fb7635dB26D783dd8D2DF87Be1c504436268/transactions#address-tabs)
- Tools for managers - [https://github.com/upala-digital-identity/group-manager-cli](https://github.com/upala-digital-identity/group-manager-cli)
- Moving to price of forgery + turning gitcoin into identity provider. [Here](https://gov.gitcoin.co/t/workstream-anti-fraud-workstream-assemble/158)
- [Measuring Price of forgery methodology](https://github.com/gitcoinco/web/issues/7888) (a bit outdated, but the general idea holds, working on a better methodology now, will post a link here)
- [Manager tools demo](https://youtu.be/wj__Alue-0g) (9 min video)

### Price of Forgery and Upala

- Video - [https://www.youtube.com/watch?v=u_jAXgcvjyg&t=1s](https://www.youtube.com/watch?v=u_jAXgcvjyg&t=1s)
- Upala Dashboard - [https://www.notion.so/Upala-HQ-a46d88209ecb4a4cabf1560acc8673a2](https://www.notion.so/UPALA-DASHBOARD-a46d88209ecb4a4cabf1560acc8673a2)
- For a deeper dive check out this [article on EthResearch on price of forgery](https://ethresear.ch/t/price-of-forgery-digital-identity-measuring-human-uniqueness-score-in-dollars/8328).

### Join the resistance

- Telegram - [https://t.me/cherish_the_difference_Upala](https://t.me/cherish_the_difference_Upala)
- Discord - [https://discord.gg/fa3q8rq](https://discord.gg/fa3q8rq)
- Twitter - [https://twitter.com/TheUpala](https://twitter.com/TheUpala)

-------------------------

porobov_p | 2022-09-13 08:02:16 UTC | #2

# Gentle PoF discovery methodology

Duplicating from [Upala docs.](https://www.notion.so/upalahq/Gentle-PoF-measurement-methodology-af87bc33315a44d08a4cb03f49c45177) 

**Please support our [Price of forgery measurement campaign for Gitcoin on Gitcoin grants](https://gitcoin.co/grants/7602/price-of-forgery-measurement-campaign)**

# A reminder on price of forgery

Price of forgery (PoF) may be viewed as a way to quality control human verification (HV) methods. Upala protocol allows bots to sell (”liquidate” or “explode” in Upala terms) their IDs for a specific amount money. Depending on the amount bot farmers are either incentivized to forge a HV method or not. The amount which is just below their incentive is considered the Price of Forgery for the particular human verification method. See this video to [learn how price of forgery works](https://www.youtube.com/watch?v=-XLTxLdjbeQ&feature=youtu.be). And check out this article - [Measuring human uniqueness score in dollars](https://ethresear.ch/t/price-of-forgery-digital-identity-measuring-human-uniqueness-score-in-dollars/8328) on Ethresearch.

# The gentle methodology🧚

PoF could be measured in multiple ways. Below is the methodology that is optimised for **cost-efficiency** (there’s cost vs time polarity).

# Score auction

### Score auction overview

**Score** - the amount of money that we offer to a user that passed a HV method.

**PoF** - the score value which we consider the current Price of Forgery for the HV method. The thing which we are measuring. Unknown at the beginning. And should be remeasured periodically.

**Bid** - the score value being tested

The measurement goes in auction steps. The bid is set to some low value and is raised slowly over time. As soon as the number of bot liquidations exceeds a predefined threshold, the corresponding bid is considered the PoF. The bid is then reset to a much lower value and the gradual increase is started again. If threshold is hit again that bid defines new (lower) PoF. The bids are always below PoF.

![Price of forgery auction|306x500](upload://33nE70QFRlkK9nkUlmsXc9AkUDc.jpeg)


### Score auction parameters

**Bid duration.** A period of time during which a bid is being tested (let’s use one day as an example).

**Starting bid.** The score we start with. It makes sense to keep it low. 

**Bid Step.** A number of percents that the bid goes up if the previous bid didn’t attract enough bots. The lower this value is the more accurate PoF we can get, and the more time it will take. 

**Liquidations** **threshold (or just threshold).** Every period will have some liquidations going on (people got hacked, liquidating out of curiosity or by mistake - not real bots). We define the **threshold** of such liquidations as a number of bots which is “enough” to be considered a bot army.

**Step down.** A number of percents that the bid goes down after the threshold was hit.

**Pool size.** The amount of money that is exposed to bots. Defines how many bots can be liquidated simultaneously (n = Pool_size / bid ).

You can experiment with different parameters in this [Price of Forgery campaign estimation doc](https://docs.google.com/spreadsheets/d/1pu2dBCbRTgj7IvA7cMuGKq2TKzReVx_aHxPZt4gc0Gs/edit?usp=sharing).

### PoF accuracy and up-to-dateness

When measuring PoF you can stop as soon as the number of liquidations hits threshold for the very first time. If the parameters were set right you may get an accurate enough PoF for your use case. At least you should be able to see the difference between HV methods being tested.

![Have a rest, look at “Fluffy pink clouds and robots, HD, highly detailed, fantasy style, fairytale”|500x500](upload://1rHCHjUuH1qzHI6WQQSadO4llua.jpeg)
Have a rest, look at “Fluffy pink clouds and robots, HD, highly detailed, fantasy style, fairytale”

But you’ve got to remember that there are always more skilful bot farmers around the corner. Some of them may have missed your PoF campaign due to insufficient publicity. Some of them may have developed more effective exploits for HV methods that you use. Both of those means that **PoF will go down over time**. You can keep your PoF up-to-date either by **repeating PoF discovery periodically** or by keeping your pools always filled.

# PoF and Pool size relation

We call PoF PoF because PoF shows cost of forgery PLUS revenue of the bot owner (🚂-PoF-PoF-PoF). More specifically it can be broken down as follows:

```jsx
PoF = CoF + (Fixed+Revenue)/n
```

, where:

**PoF** - price of forgery (or bid in the current period - see auction parameters),

**CoF** - cost of forgery per bot (manual labour, Upala fee, Ethereum fees, etc.),

**Fixed** - fixed costs for a bot army, risks, efforts of getting butt off of the couch, etc.,

**Revenue** - total revenue of the bot farmer,

**n** - bot army size that CAN be liquidated.

If a bot owner liquidates their army, their revenue looks like this. 

```jsx
Revenue = n × (PoF - CoF) - Fixed
```

**So bot owner revenue depends on army size they can liquidate.** And it is group manager who controls the army size through the number of possible liquidations. Which is:

```jsx
n = Pool / PoF
```

, where

**Pool** - pool size. The amount of money allocated in pool. From bot farmer perspective it is the amount of funds that can be drained simultaneously. Here and further threshold is neglected ( Actual_pool_size = bot_army * PoF + threshold )

**Army size is an important parameter to measure PoF correctly.** Think of the difference between pool sizes of $10 and $10,000 when PoF is set to $1. No one’s gonna bother creating 10 bots for a 10 buck reward. Bot owners should have an incentive to create armies. At the same time setting pool size to $1,000,000 does not make much sense either.

# Pool size auction

PoF and Pool size always go in pair. To find the pair we will now improve the methodology described above by introducing variable pool size.

## Pool size auction overview

Just like with the bids above, we gonna gradually increase **pool size** within single bid duration. 

For example we can increase pool size from $1,000 to $5,000 during the day (if our bid duration is one day). Then for a specific bid we gonna have a chart like this.

![Pool size auction|373x500](upload://fDlqXZ7m0su6sBOkmYt0mKPzgyx.jpeg)


Now the liquidation threshold may or may not be hit at a specific pool size for a given bid. And if it is hit we’ll have both PoF and its corresponding Pool size. And, accordingly, if liquidation threshold is not met (if there’s not enough bots for us to be considered an army) we proceed to the next bid and start with the lower pool size limit again. 

And same as with bid step above, we can reduce **pool size step** to increase accuracy. Greater number of steps would mean a more precise PoF and Pool size pair.

## Pool size auction parameters

**Lower pool size limit**. The pool size that we are starting with for every new bid.

**Upper pool size limit.** The maximum pool size that we define for this particular HV method. 

**Number of steps.** The number of increases of pool size within single bid duration. 

**Pool size step.** The increase in pool size. Can be derived from bid duration and number of steps.

```jsx
Pool_size_step = (Upper_pool_size_limit - Lower_pool_size_limit) / Number_of_steps
```

These parameters should be dealt with care. Accuracy and PoF measurement costs depend significantly on them.

Both upper and lower limits should be set according to Gitcoin needs. **Recommendation will soon be described bellow. Please follow the topic if you are interested.**


**Please support our [Price of forgery measurement campaign for Gitcoin on Gitcoin grants.](https://gitcoin.co/grants/7602/price-of-forgery-measurement-campaign)**

-------------------------

porobov_p | 2022-09-21 11:49:38 UTC | #3

# Figuring out auction parameters

This is the continuation of the post above - the next step. Also a duplicate from the newest section in Upala docs.

This document is intended to help you build intuition on how to set parameters of the Score and Pool size auctions specific to your project and human verification methods that you use. The auctions are described here - [Gentle PoF discovery methodology](https://www.notion.so/Gentle-PoF-discovery-methodology-af87bc33315a44d08a4cb03f49c45177).

The most complex parameter is the Upper pool size limit. It is described in details. Others are touched just slightly.

# Score auction parameters

## **Bid duration, bid step, starting bid, step down**

When setting up these parameters one should consider time vs money polarity. You can get PoF a lot faster if you have significant budget. If you wanna cut costs on the PoF measurement campaign go slow (start with low bids, increase bid duration, make small steps up and big steps down).

## **Liquidations threshold**

See lower pool size limit.

# Pool size auction parameters

## **Number of steps and Pool size step**

Decide on one of these and calculate the other. 

```jsx
Pool_size_step = (Upper_pool_size_limit - Lower_pool_size_limit) / Number_of_steps
```

Number of steps can increase accuracy of the discovered “Score - Pool size” pair. The only thing that prevents it from being too granular is gas costs (transaction fees). Try to keep steps small.

## Lower pool size limit

Pool size which we need to set at the start of the pool size auction.

If we could predict the **liquidations threshold** (the liquidations that happen due to non-Sybil reasons) that value could be used to define the starting pool size. But we don’t know what this threshold is and all we can do here is guessing.

One thing to consider here is duration. If we start too low, the climb will take longer. It makes sense to start with a considerable sum. $500 - $1000 should do in general.

![Cute pink fluffy robot fairy, hd, highly detailed, fairytale, portrait|500x500](upload://c3mYGrsIQ2fPfHZZqBi4aoQuHPi.jpeg)
Cute pink fluffy robot fairy, hd, highly detailed, fairytale, portrait

## Upper pool size limit

The upper limit should be defined with care. It is platform specific.

Imagine we have $10,000,000 in our pool. Even with low PoF that would probably create enough incentive to develop a new exploit for the Human Verification method that we are trying to asses. While this may be of a particular use, we are interested in measurements only. Thus the upper limit should be meaningful to our platform. And it should be economical to say the least. 

Below are the things to consider when setting up this parameter.

### Revenue and Extractable value

We can try to make malicious actors hunt for the Upala pool and not for the value encapsulated in our platform (e.g. matching funds in case of Gitcoin). A good starting point is to think of malicious actors revenue. If they are trying to extract value from our platform the revenue looks like this:

```jsx
Fraudster_Revenue = Extracted_Value - Extracting_Costs - Bots_Costs
```

, where

**Fraudster** - a malicious user that tries to extract value from our platform,

**Extracted_Value** - the value that the fraudster can extract (e.g. Gitcoin matching funds),

**Extracting_Costs** - efforts needed to extract the value (Outwitting Fraud Detection team, **risks** on failing to do so, etc. For Gitcoin these are all the efforts needed to create an eligible grant, spread donations across multiple grants to mimic genuine behaviour, etc.),

**Bots_Costs** - efforts required to create a bot army.

If a malicious user now has an option to “sell” their bot army the revenue for doing so is:

```jsx
Bot_Farmer_Revenue = Pool_Size - Bots_Costs
```

, where

**Bot_Farmer** - a malicious user that breaks HV methods just to liquidate their bot army for the reward from Upala pool,

**Pool_Size** - same as above, pool size at risk (or if looking from bot farmer side the amount of funds that can be drained from the pool simultaneously),

**Bots_Costs** - efforts to create bot army (both Fixed and Cost of Forgery per bot).

Let’s imagine a situation when it makes more sense (or equally reasonable) to sell bot army then to hunt for the platform value. It will happen when the revenues are equal. 

```jsx
Fraudster_Revenue = Bot_Farmer_Revenue
```

Let’s be humble and assume that Extracting_Costs for our platform are 0 (it is also safer to assume so). And if we now substitute revenues from both sides with their values from the formulas above we got:

```jsx
Pool_Size = Extracted_Value
```

So if we offer a pool size that would be comparable or greater than maximum possible extracted value, there would be no sense for the malicious actor to hunt for that value anymore and turn to bot liquidations instead.

This is useful. We can use this Pool_Size value as our Upper Pool Size Limit right away. If we were right with the Extractable value our **existing malicious actors** should liquidate their bots. But as we are in the open market there are other actors in the wild. Which gives us a chance to cut costs.

### **Fraudster and Bot farmer**

Pool size limit that we derived from the extractable value should not be regarded as an inevitable expense. There’s a chance bots take it all. However it is likely that we will see enough of liquidations far below the upper limit. And there are reasons for that.

Notice that when we discussed malicious user revenue we introduced two different entities: the Bot farmer and the Fraudster. These are opposing forces.

Consider the Fraudster. We neglected their efforts to extract value from our platform. But even if there are little efforts required, the risk of being detected is high, it increases over time and - which is more important - the risk is unknown.

Earning on bots liquidations on the contrary is transparent and straightforward. Which gives a considerable advantage to the Bot framers. It is no coincidence that one of the main Upala’s principles is protecting bots rights.

Bot farmers are narrowly specialised on bots (or better say on specific HV methods). They don’t care for the extractable value. With their presumably better forgery methods they can outperform the Fraudster. Meaning that they can win the auction. They gonna “sell” their bots faster, taking lower bid and/or lower pool size. Which cuts our costs.

<aside>
🎭 A tragedy of commons for bots. Not only they compete but the “winning” bot unveils the PoF, which is then used to block bots 🤖😢

</aside>

### **Promotion**

In order for the campaign to be accurate and economic we need to signal both existing bots and future bots about Upala pool. Current malicious actors must be informed that there’s now an option for them not to attack the platform itself(hunting for the Extractable value). Wider bots community must be informed that they now can generate some bots “for sale”.  Thus our PoF discovery campaign budget should include promotion:

- Show the campaign in the your interface and docs
- Promote it with existing tools (e-mail subscriptions, social media, etc)
- Advertise the campaign with paid ads

Have a look at the [Signalling bots](https://www.notion.so/Signalling-bots-125ec386fc10450faca198e9a6d71bfd) campaign for Gitcoin for inspiration. 

It also makes sense to try talking with bot farmers directly. If they tell you the army size and bid that they would definitely bite, let them prove that!

![Pink furry robots in front of a TV in a victorian style room, hd, highly detailed, fairytale|500x500](upload://5z30NgUoRakBhhNfaF0LhDgmEO2.jpeg)
Pink furry robots in front of a TV in a victorian style room, hd, highly detailed, fairytale

### Time vs Money

Another thing that can make your PoF discovery campaign more accurate and economic is time. Same as with Score auction you can increase bid duration and number of pool size steps. On networks with low transaction fees you can get a very smooth increase of pool size. Thus saving on the otherwise abrupt increases of pool size (or from bot farmer perspective bot army size).

Time is also important because bots need time to build tools. It makes sense to start advertising before the campaign begins. So that all players are in the game when the game begins. 

If you are not currently under attack or you can afford being attacked (if learning PoF is not urgent), you can probably cut some costs by increasing the total campaign time.

# Other things to consider

### **It’s ok to loose the whole pool**

Loosing the pool is the point when you get information about bots. Regard pool funds as an investment or a as a service fee. Think of how much you can save after you have the correct assessment of the HV methods that you use.

### **Respect bot farmers and play fair**

Remember there are ordinary and honest people behind those bots. They are just exploiting vulnerabilities. They chose this job because they like it. They do work for the benefit of humankind. They teach us how to deal with machines. So when time comes, we would be prepared. 

### **Use dedicated pool for every HV method**

You should be able to distinguish different bot armies and different players. If you want to measure PoF of a combination of methods, create a dedicated pool for that as well.

### Split extractable value between multiple pools

If you have multiple HV methods and all of them need to be passed to extract value from your platform, then split the amount that you got in [Revenue and Extractable value section](https://www.notion.so/Figuring-out-auction-parameters-6db2845773df49d6a9e01308e84e1359) between multiple pools.

# Links
[This document on Upala Notion](https://upalahq.notion.site/Figuring-out-auction-parameters-6db2845773df49d6a9e01308e84e1359) (got table of contents)
[Gentle PoF discovery methodology](https://www.notion.so/Gentle-PoF-discovery-methodology-af87bc33315a44d08a4cb03f49c45177) 
[Signalling bots](https://www.notion.so/Signalling-bots-125ec386fc10450faca198e9a6d71bfd)
[Play around with parameters - Price of Forgery campaign estimation doc](https://docs.google.com/spreadsheets/d/1pu2dBCbRTgj7IvA7cMuGKq2TKzReVx_aHxPZt4gc0Gs/edit?usp=sharing)
[A follow up for the Green pilled episode with Upala](https://www.notion.so/A-follow-up-for-the-Green-pilled-episode-with-Upala-da296e0a331a4f1fafe5cc55df3be8da) - benefits of using PoF for Gitcoin

Next up... a budget proposal. Keep in touch, humans!

-------------------------

DisruptionJoe | 2022-09-21 12:38:19 UTC | #4

Thank you for the progress updates here. I know @kishoraditya who is guiding our research efforts is paying attention. It is also extremely helpful that you were able to set up the Grant to fund a first discovery pool.

-------------------------

Digijoe7 | 2023-08-13 00:03:19 UTC | #5

This was a great read! Very informative and beneficial! :grinning: :rocket:

-------------------------
