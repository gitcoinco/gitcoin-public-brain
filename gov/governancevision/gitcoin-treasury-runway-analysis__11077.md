---
id: 11077
title: "Gitcoin Treasury Runway Analysis"
slug: gitcoin-treasury-runway-analysis
category: governancevision
url: https://gov.gitcoin.co/t/gitcoin-treasury-runway-analysis/11077
created_at: 2022-07-07T02:54:43.236Z
last_posted_at: 2022-07-15T15:58:29.197Z
posts_count: 16
views: 5284
like_count: 28
---

# Gitcoin Treasury Runway Analysis

<https://gov.gitcoin.co/t/gitcoin-treasury-runway-analysis/11077>
Stastny | 2022-07-07 12:41:20 UTC | #1

**Authors:** @Stastny & @SamB from [Llama ](https://llama.xyz/)

Hey all - @Stastny from Llama here. Posting below some treasury runway analysis we pulled together for the DAO.

**Bottom Line / TL;DR**

According to our analysis, GitcoinDAO has the following runway under the scenarios outlined below (assuming current expense rate):

* **No Treasury Diversification**
  * **9.3 years** of runway if token price remains flat
  * **4.7 years** of runway if token price falls 50%
  * **0.9 years** of runway if token price falls 90%
* **$3m Treasury Diversification**
  * **9.3 years** of runway if token price remains flat
  * **4.8 years** of runway if token price falls 50%
  * **1.1 years** of runway if token price falls 90%
* **$15m Treasury Diversification**
  * **8.9 years** of runway if token price remains flat
  * **5.0 years** of runway if token price falls 50%
  * **1.8 years** of runway if token price falls 90%

For more details on the runway analysis, you can access the report [here](https://llama.xyz/reports/gitcoin/runway-analysis-july-2022.pdf).

**Purpose of the Analysis**

The latest $3m treasury diversification [proposal](https://gov.gitcoin.co/t/gitcoin-treasury-diversification-update/10932/9) is live on [Snapshot.](https://snapshot.org/#/gitcoindao.eth/proposal/0x0eb45cfd31ddd2701af3d74ce38a9e87292fe42a6b40b26812ff9889b07daeb3)

In light of those discussions, we aim to provide an illustrative treasury runway analysis under various diversification, operating, and market price scenarios. Specifically, the runway analysis serves to inform the community regarding the impact of:

* Go-forward decisions about expenses
* The potential upside and downside impact of GTC pricing scenarios
* The pros and cons of stablecoin diversification

**Treasury Makeup**

Including unvested GTC currently held in the Gitcoin Vesting wallet, Gitcoin’s treasury stands at nearly ~$134m. The vast majority of this value is denominated in GTC, greater than 99.5%, as Gitcoin currently holds ~$650k in stablecoins and other tokens. Any diversification initiative, whether via venture capital raise or OTC, will come at a discount to today’s prices given fundraise precedent and likely sell pressure. For context, GTC is currently trading at $2.63 as of 7/5/22 close, down nearly 90% from the all-time high last November.

We estimate that a $15m stablecoin diversification initiative would lower the overall value of the treasury to $128m. This assumes $12m sold to venture investors at a 30% discount to today’s price and the remaining $3m sold OTC at an average 5% discount.

Kyle from Gitcoin is leading the strategic raise conversations with investors. In current market conditions, that has been difficult to pull through but we’re assuming that it is still possible for the purpose of this analysis.

**Treasury Runway - Assumptions**

There are four key assumptions to consider when estimating Gitcoin’s runway:

**1. Treasury Make Up** - Any diversification initiative will serve to decrease Gitcoin’s runway at today’s prices while raising its downside floor. The analysis assumes three treasury makeup scenarios: Status Quo (no diversification), a $3m OTC stablecoin diversification, and a $15m VC + OTC stablecoin diversification.
**2. Average Monthly Expenses** - Season 14 budget indicated monthly spend of ~$1.2m. The attached analysis sensitizes this spend to include a 50% decrease and 50% increase in average monthly spend.
**3. Expense Denomination Breakdown** - The analysis assumes that stablecoin assets are used first to fill expense needs with GTC backfilling the remainder.
**4. GTC Price** - While predicting future prices and market environment is impractical, analyzing various average future GTC price scenarios is instructive. The attached analysis includes three different average illustrative future prices for GTC: $0.25, $2.63, and $5.00. $0.25 is a GTC bear case, $2.63 was the current GTC price as of the time of this analysis, $5.00 represents a ~100% premium to today’s price.

**Treasury Runway - Findings**

Under existing conditions (no diversification, $1.2m monthly spend, today’s market prices) we estimate that Gitcoin has ~9.5 years of runway with the ability to stretch that out to ~14 years with significant expense cuts. An extreme bear scenario (GTC @ $0.25) would cut this runway down to less than a year.

The aforementioned $3m diversification scenario would do little to change these figures given the current size of assumed Gitcoin monthly spend. $3m in stablecoin would serve to fund DAO operations for roughly a quarter and runway would not be significantly affecte.

The aforementioned $15m diversification scenario would fund current operations for just over a year and decrease overall runway assuming a stable GTC price of $2.63 by roughly 3-6 months. However, if GTC price were to fall to $0.25, the diversification would nearly double runway in, providing nearly 2 years worth of capital to fund operations.

*Note: All figures current as of UTC Close 7/5/2022.*

-------------------------

myceliumcoordinator | 2022-07-07 12:35:10 UTC | #2

What is the affect of the ~$1.2m in monthly spend on token price?  Will ~$1.2m/mo in downward pressure (assuming people who earn GTC sell it) cause the token price to go down?

-------------------------

myceliumcoordinator | 2022-07-07 13:54:33 UTC | #3

[quote="myceliumcoordinator, post:2, topic:11077, full:true"]
What is the affect of the ~$1.2m in monthly spend on token price? Will ~$1.2m/mo in downward pressure (assuming people who earn GTC sell it) cause the token price to go down?
[/quote]

I now see that there is a section for this under "Additional Qualitative Considerations" in the linked report.

In my opinion, this is a core consideration for runway analysis + worry it has just been appendixed.  Analyzing DAO runway without addressing the impact of continuous GTC selling is like analyzing a car without looking at the engine.

Worst case would be if the readers of this report perceive that the DAO has 9.3 years of runway at current trajectory without considering that the token price is very likely to fall because of the continuous selling.  We are not sure which of the scenarios listed here is the *current trajectory*.

[quote="Stastny, post:1, topic:11077"]
* **No Treasury Diversification**
* **9.3 years** of runway if token price remains flat
* **4.7 years** of runway if token price falls 50%
* **0.9 years** of runway if token price falls 90%
[/quote]

If people perceive the wrong currency trajectory, this false sense of security could be really really bad.    **The DAO is probably on a course where the continuous downward pressure on GTC will cause the token price to go down because there is no systematic opposite upward pressure, but there is no way to know without an analysis**.

I applaud the effort here but I think that additional work is needed to get to a useful runway analysis that DAO members can rely upon.

-------------------------

sarahdw | 2022-07-07 13:56:57 UTC | #4

Thanks! This is great. I know the extreme bear case is an *extreme bear case* but what are the signals or triggers to run this analysis again to ensure we're keeping a close eye on funds?

-------------------------

kyle | 2022-07-07 16:44:19 UTC | #5

Thanks for sharing the details! The numbers seem a bit different from the numbers a few others had been tracking. Specifically, the WS budgets requested in S14 were overly large as they had reserves in them. 

The actual spends are closer to 700k/mo. Here is one graph to track this:
![Screen Shot 2022-07-07 at 12.43.35 PM|690x427](upload://1xldc6a3Q4EmUCA0hCEshv08A3A.png)

h/t to @ChrisDean for generating these.

@Stastny - I would love to confirm a few of your numbers :)

-------------------------

ChrisDean | 2022-07-07 17:53:29 UTC | #6

I created that graph from the actual spend of $665k for May across the workstreams. I accounted for the reserves and excluded them from the budget charts.

-------------------------

Stastny | 2022-07-07 20:49:25 UTC | #7

Thanks for the questions and responses! A few answers/clarifying points below:

[quote="myceliumcoordinator, post:2, topic:11077"]

What is the affect of the ~$1.2m in monthly spend on token price? Will ~$1.2m/mo in downward pressure (assuming people who earn GTC sell it) cause the token price to go down?

[/quote]

There will definitely be sell-pressure as a result of GTC-denominated spend but, in our opinion, any attempt to quantify the magnitude of that effect on average future GTC price would probably fall into “false precision” territory given inconsistent trading volumes and especially given the prices shown in our sensitivity tables are assumed to be a weighted-average over the remaining life of the protocol.

The hope is that this analysis portrays, at a high level, what type of runway the DAO could expect under various spend, diversification, and GTC price scenarios.

[quote="sarahdw, post:4, topic:11077, full:true"]

Thanks! This is great. I know the extreme bear case is an *extreme bear case* but what are the signals or triggers to run this analysis again to ensure we’re keeping a close eye on funds?

[/quote]

Thanks! Would definitely recommend checking out the Gitcoin Financial Reports @Elliott at Llama produces to stay up-to-date on spend and the state of the treasury each month. This may include regular updates on runway down the road.

[quote="kyle, post:5, topic:11077"]

Thanks for sharing the details! The numbers seem a bit different from the numbers a few others had been tracking. Specifically, the WS budgets requested in S14 were overly large as they had reserves in them.

The actual spends are closer to 700k/mo. Here is one graph to track this:

[/quote]

Thanks for passing along! We took the view we should conservatively take the current S14 budget, split it monthly, and round up for our base case. That said, historical actuals vs. budget informed why we pegged our upside case as a 50% cut to base expenses (~$800k / month) versus something more moderate. We thought it was fair to view the token value leaving the treasury as “burn” in the context of this analysis but hopefully the upside sensitivity helps inform a different view on expense projection that others may take based on actuals. I also think the difference between the two numbers is instructive (*i.e.,* if folks start spending their approved budget versus the rates we’ve seen lately then the treasury loses ~5 years of runway at today’s prices).

If this were an exercise in valuation or financial projection I would perhaps feel a bit differently but our perspective is that it behooves the DAO to consider runway with as conservative a point of view as possible (while properly sensitizing inputs to provide context).

-------------------------

ZER8 | 2022-07-07 20:58:29 UTC | #8

I'm just a small fish in this Gitcoin DAO pond, but I believe that having 0,9 years left is a big OH, OH. Even if I get fired and get banned from Gitcoin DAO 4 ever(saying this just to remove the bias) I still want to see Gitcoin succeed in it's mission. It's a future worth living 4. :robot:

Not an expert in the field, but I believe this is a big existential risk and because I'm a big advocate of simplicity I suggest that  either the DAO generates revenue or the stable allocations need to grow considerably(by DCAing ofc).

In the worst possible scenario the token falls 90% and this is possible because we don't have a bottom....si if Bitcoin tanks to 10k 15k we will go under 1$. We need to be prepared for this outcome and I don't think that a 3m$ allocations solves that! We should also start about investing small portions of the treasury as a DAO. Risk management is crucial.

-------------------------

bhargavaparoksham | 2022-07-08 05:02:20 UTC | #9

@kyle 700k/mo doesn't include the GPC workstream budget which is being created starting from next season, right? Including that will make it ~1 mil/mo.

-------------------------

kyle | 2022-07-08 12:15:50 UTC | #10

This is a great call out. Yes, once the GPC workstream is up and running the spend will be above $1M/mo.

-------------------------

myceliumcoordinator | 2022-07-08 15:22:05 UTC | #11

[quote="Stastny, post:7, topic:11077"]
The hope is that this analysis portrays, at a high level, what type of runway the DAO could expect under various spend, diversification, and GTC price scenarios.
[/quote]

In my opinion, this analysis doesnt do any good to predict the DAO runway.

The DAO has no idea if $1.2m/mo in spend is going to cause the token to drop 99% or 0%.  How can anyone who is working at the DAO or holding the token have any confidence in the DAOs runway?

Core token dynamics like the ongoing work-stream's spend effect on token price need to be taken into account to have any confidence in this project's runway.  Or to take course-correcting action if the outlook is grim.

[quote="Stastny, post:7, topic:11077"]
There will definitely be sell-pressure as a result of GTC-denominated spend but, in our opinion, any attempt to quantify the magnitude of that effect on average future GTC price would probably fall into “false precision” territory given inconsistent trading volumes and especially given the prices shown in our sensitivity tables are assumed to be a weighted-average over the remaining life of the protocol.
[/quote]

Why not do an analysis using publicly available information and under different confidence intervals?  If inconsistent trading volumes are a problem you can use longer time periods or make an informed guess.

eg. you could come back saying

>  assuming liquidity remains as A and spend remains at B, we can say with C% confidence that D.

-------------------------

DisruptionJoe | 2022-07-12 08:17:58 UTC | #12

[quote="Stastny, post:1, topic:11077"]
**$15m Treasury Diversification**

* **8.9 years** of runway if token price remains flat
* **5.0 years** of runway if token price falls 50%
* **1.8 years** of runway if token price falls 90%
[/quote]

Where can we find information on how quickly we are looking to make this option a reality seeing how it seems to be an objectively better outcome?

-------------------------

epowell101 | 2022-07-14 20:33:34 UTC | #13

This is great analysis.

That said, I would tend to second @myceliumcoordinator .

As has been pointed out by the same excellent folks contributing to this analysis elsewhere, it is basically a fallacy to simply take existing tokens held in the treasury X market price = value.  This would be similar to a company putting on their books the value of authorized but unissued shares. 

To make more stark the source of the concern underlying the questioning of the value of the treasury, consider that at the time of this forum post the Treasury was "valued" at $134 million - this was the starting point for the analysis.

However CoinMarketCap sees the total value of all circulating supply today as ~$32 million.  [https://coinmarketcap.com/currencies/gitcoin/](https://coinmarketcap.com/currencies/gitcoin/)

So there is no way that our treasury can actually be worth 4-5x the entire circulating market cap, right?  What is the right ratio?  

Suggestion - IMO in addition to other excellent work ongoing to increase GTC utility and diversification, we may want to work on a plan to be "default alive" if we are not already.  There is a methodology for putting together such a plan and the process itself can be clarifying and even cathartic.  This approach would call for us to be explicit about why we are diverging from that plan when we are.  I'm concerned we may not have fully internalized a more difficult base case and therefore are continuing to grow spending into a bear market of uncertain duration while relying on a treasury of thus far unknown value.

-------------------------

HelloShreyas | 2022-07-14 22:55:08 UTC | #14

> Where can we find information on how quickly we are looking to make this option a reality seeing how it seems to be an objectively better outcome?

Hey @DisruptionJoe - we should hopefully execute a $3m diversification in the next few weeks. 

Re. the bigger strategic raise - Kyle's leading those conversations and it's unfortunately taken longer than expected because of market conditions. He outlined some reasons [here](https://gov.gitcoin.co/t/treasury-diversification-working-group-updates-thread/10231/9). But he's still continuing conversations with potential partners and can share updates as he makes progress.

-------------------------

giuliocavallari | 2022-07-15 10:37:11 UTC | #15

Hi, I think treasury diverisification is fundamental for the long-term success of the DAO. However, do you have more information on the funding mechanism? Would this involve minting new tokens to be distributed to investors? Given so, might you not have to take into consideration the possibile implication this will have on price (due to the the increase in the supply of GTC)? Also, could you please explain why funding would be at a discount? 
Thanks and nice work,
Giulio

-------------------------

Stastny | 2022-07-15 15:58:29 UTC | #16

The current assumption in the analysis is that the GTC would be sold out of the treasury. Selling in bulk often comes at a discount given liquidity constraints and fees. A strategic fundraise generally comes with a further discount due to the fact that incoming investors are often asked to lock their tokens up and vest them over some period of time.

-------------------------
