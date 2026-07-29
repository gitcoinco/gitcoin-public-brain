---
id: 12574
title: "GTC Financial Model"
slug: gtc-financial-model
category: open-discussion
url: https://gov.gitcoin.co/t/gtc-financial-model/12574
created_at: 2023-01-16T04:13:41.010Z
last_posted_at: 2023-01-20T19:29:59.520Z
posts_count: 4
views: 4120
like_count: 9
---

# GTC Financial Model

<https://gov.gitcoin.co/t/gtc-financial-model/12574>
picciobellina335 | 2023-01-16 04:13:41 UTC | #1

*(DISCLAIMER: This is not financial advise.  Do your own research.  Talk to an accountant.  This post and the document linked from it are provided for informational purposes only.)*

There isn't a financial model for Gitcoin publicly available on the forum, so I have been working with @a33titude on one in order to understand the potential value of Gitcoin's economies.  

In this document, we took the most plausible revenue models for GTC Utility and built a spreadsheet around how growth of those revenue models could happen.

We had to make some educated guesses about what growth could look like in order to build the model.  Here is a key (rows in blue were just total guesses):

![model_key|666x208, 50%](upload://jGvHO4zikjJGzOEokkkERqbXoXT.png)

There are about 8 tabs in the spreadsheet.  The most interesting ones are the revenue ones, which model what the various business models of Gitcoin could look like as it matures.

![tabs|690x446, 75%](upload://jdTEwsLDtaxdYva5J66M19nkMmO.png)

Get the model [here](https://docs.google.com/spreadsheets/d/1l35c-yCG-_kxOFZIz-S85mboelqrO_YBV1jrQ-NRVG8/edit).   We would love to see other people fork the model and present their own view of Gitcoin back to us.

Some things we learned by playing with this model.

# 1. Mutual Grants & Protocol Fees could all be lucrative over the long term.  But they will take years to grow.

Here is a view on what these economies could look like if their growth compounds.

![growthovertime|690x213](upload://3PvkF4qMVl7DKuvTgIfx8Az0BWZ.png)


# 2. GTC is vulnerable to running out of stables in treasury.

Here is what the treasury value in stables looks like if stablecoin costs stay low relative to revenue (left) vs if they do not.
![base|690x419, 50%](upload://lVzg9pJKgUbu5dHYlpDwyscnE1g.png) ![toomuchspend|690x441, 50%](upload://tMxSgfkLbiiMU2ypxTg4bwr1JSA.png)

Because revenue will take years to develop, Gitcoin needs to find a way to pay it's bills that isn't stablecoin outflows until it's business models take off.

Of course Gitcoin currently pays most of it's bills in GTC.  It's not clear how long that will last, but it seems to be working for now.  This model makes no attempt to model GTC outflows, (1) because thats really hard to model given how volatile GTC is and (2) a sustainable Gitcoin would be cash flow positive and not overly dependent on GTC. 

# 3. A rising tide lifts all boats.

One nice attribute that Gitcoin has is that it's based around the Ethereum economy, which is growing quite rapidly.  This rising tide lifts all boats, though we can't say how much.  The first cut of this model is in USD, but we are considering doing an Ether denominated one.

-------------------------

kevin.olsen | 2023-01-17 10:52:41 UTC | #2

Thanks for posting and getting this first draft of a model documented and shared out.

On the Mutual Grants, can you say more about how you set up some of the assumptions for future value there?

-------------------------

a33titude | 2023-01-18 02:18:25 UTC | #3

[quote="kevin.olsen, post:2, topic:12574"]
On the Mutual Grants, can you say more about how you set up some of the assumptions for future value there?
[/quote]

Per the model, the hypothesis behind the Mutual Grants tab is 
> Currently called “Mutual Grants”. This is the idea that Gitcoin is a source of alpha for the space + would do a token swap with up & coming projects on the platform. The strategy would be to do investments in alumni, put their tokens in treasury, and to catch the next Uniswap that comes into the platform.

The main insight that powers this hypothesis is that Gitcoin is a source of signal for what projects are up and coming in the space.   The ETH ecosystem has MEV.  The GTC ecosystem has DEV (data extractable value). 

![77uc81|690x388, 50%](upload://3qhCuH9qD3c37sehJ4wCtB727xf.jpeg)


To explore the power of this opportunity, let me illustrate a counterfactual history of Gitcoin wherein Gitcoin had taken 1% of Uniswaps token supply back when it was a Gitcoin Grant.  

In this counterfactual, UNI is as valuable as it is today - the fully diluted network value of UNI is $6,385,373,549 as of today.  In this scenario Gitcoin's stake of Uniswap is worth $63,853,735.49.  

In this scenario, Gitcoin has no worries about it's cash position or size of it's burn because it's got a highly liquid very valuable asset that it got on its "Balance Sheet" early before anyone else saw the value of UNI.

Lets dive deeper into this counterfactual scenario.  In this counterfactual scenario, in their infinite wisdom and foresight, Gitcoin's team also took 1% positions in Yearn, 1Inch Exchange, Rotki, WalletConnect, and others.    That counterfactual Gitcoin has $100 million in liquid assets to invest into Grants Stack.

![winning|690x477, 50%](upload://yiwT7QymRGDCV0kvQ2CTVcCJoA0.jpeg)


# UX

The UX of implementing a feature like this feels pretty simple for me. 

1. Rounds run as per normal. 
2. After the round, the Round Manager sends an email to a subset of grants on the platform (curated by the round manager).
3. The email looks EXACTLY like this TO THE PIXEL:

![download-2|382x500, 75%](upload://kQAt4BhGWVnVzGuNsoF4Gj72GjR.jpeg)

4. The User submits information about their business plan and takes a short 30 minute call with the round manager.
5. The offer amount can be negotiated in a token swapping app.  If both sides accept the offer, a token swap is facilitated.
5. Repeat until deal is closed (or abandoned).
6. Over time Gitcoin gets access to the Data Extractable Value (DEV) in it's ecosystem.
7. If it gets really sophisticated, 
   - Gitcoin can charge large VCs for the DEV coming out of Gitcoin.
   - Gitcoin can share this data with its ecosystem building partners (like Fantom or Uniswap).

# Model

OK now to answer your question about the model @kevin.olsen .

As the trope goes "all models are wrong, some are useful".  The model is 99.99% likelihood wrong about the upside of mutual grants.  How wrong? IDK.  What does the next Uniswap look like?  IDK.  But I do know that whoever those founders are, it is will likely get $$$ from Gitcoin (bc Gitcoin Grants & QF = a source of data signal about whats hot in the ecosystem).

The model assumes that Gitcoin will offer standard deal teams
1. 1k GTC / deal (column H)
2. in exchange for 1% of future tokens (column I)

But it could easily support variable deal terms (eg the standard offer is just "double your match payout for 1% tokens", and Gitcoin puts a blended deal into its financial model in column I/H).

## Portfolio Number Go Up 📈

Over time Gitcoin will hold
1. Column F Num Grants Invested In Yearly
2. Column G Cumulative Grants Invested
3. Column K Total GTC Investment Yearly
4. Column L Cumulative GTC Investment

## So how do you value that portfolio?

If we assume that 
1. Average Project Value at Investment Time (column L)
2. then we have Total Ecosystem Value of Alumni  (column N)
3. and Total Portfolio Value (column O)

Of course the giant elephant in this room is "How much is this token worth?"

![77ubwb|666x375, 75%](upload://votQLwzZtntRzH7uEQWcjqISlg5.jpeg)

There is NO way to know which token will be the next UNI, YFI, etc... So the solution is to take many bets.  If we assume
1. 45% Average Project Value Growth YoY (column M)
2. place many bets

then we will see Total Portfolio Value (column O) grow by about 45% per year.  

Of course most projects will grow 0%, some projects will grow 30%, but maybe 10% will grow 400% and bring the average up for everyone.  

# Execution

I think the most important thing if Gitcoin does this it 
1. preserves its capital
2. makes many small bets earlier than anyone else can
3. over time tries to get better and finding signals that a project is about to ramp it's network

The key thing that would excite me as a GTC part time fanboy/part time critic is to build a market intelligence engine that can invest in projects BEFORE anyone else knows about them.  (Market Intelligence Engine = a combo of tech, product, marketing, data, operations, etc)

![vc model|690x481](upload://ueO8o80ZtBZoAWyEd1jHO2cmORD.jpeg)

Let me know if any questions.

-------------------------

epowell101 | 2023-01-20 19:32:30 UTC | #4

Just catching up on this.  Really excited to see the model & the meme slinging in one post. 

Seriously inspirational and thoughtful work IMO.  

Quick note - there is also a mechanism that Gitcoin has looked at called aqueduct which could also give Gitcoin exposure to the upside of projects.  If you have time, it would be interesting to hear what you thought about that as an alternative approach to the token swap.  
[Tally example](https://blog.tally.cash/tally-wallet-plans-first-gitcoin-aqueduct-to-automate-public-goods-funding-ecosystem-building/)

Secondly - as you know Gitcoin is in the process of launching protocols and a Grants Stack so that all communities could fund their shared needs more easily - without permission from Gitcoin.  The addition of this approach is perhaps "just a detail" in your model however I wanted to mention these ongoing discussions about how / whether to capture value such as revenues from that shift in model.  IMO this *might* shift the curve left somewhat - potentially - as round operators like Unicef succeed and increasingly learn to run their own rounds.  What do you think?

-------------------------
