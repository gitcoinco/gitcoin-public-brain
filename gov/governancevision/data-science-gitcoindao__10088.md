---
id: 10088
title: "Data Science @ GitcoinDAO"
slug: data-science-gitcoindao
category: governancevision
url: https://gov.gitcoin.co/t/data-science-gitcoindao/10088
created_at: 2022-03-15T22:05:39.188Z
last_posted_at: 2023-10-22T10:04:08.631Z
posts_count: 29
views: 8574
like_count: 90
---

# Data Science @ GitcoinDAO

<https://gov.gitcoin.co/t/data-science-gitcoindao/10088>
owocki | 2022-06-01 17:30:01 UTC | #1

I think there is so much potential in investing data science at Gitcoin.

This is informed by a few things
- [Prior Experience](https://www.linkedin.com/in/owocki/). A few years ago, I was the Director of Engineering at a clean energy startup that set up a fairly robust data warehouse ETL/snowflake schema system to run advanced analytics on time series data.  I've also been in a few different product oriented positions at various web2 startups that had mission critical ecommerce checkout flows with A/B testing, marketing emails to optimize those funnels.  This one time, when i was CTO of an online dating site (a double sided marketplace, just like Gitcoin), I built a matching engine that matched users on 20 dimensions.
- Per [gitcoin.co/results](https://gitcoin.co/results), Gitcoin has helped 66,712 funders reach an audience of 292,817 earners. Gitcoin has facilitated 1,740,075 complete transactions to 10,247 unique earners.  Understanding the [4 years of data](https://gitcoin.co/results) at Gitcoin, particularly the [Grants Rounds data](https://twitter.com/owocki/status/1441415242009886723), gives me a hunch that there are interesting opportunities in understanding the data.

The objective of this thread is to start a conversation. **What should the data science practice at Gitcoin look like?**

Here are the data science opportunities matters I'm aware of at GitcoinDAO

- **Product Analytics &  Data Science**
  - Responsible for understanding how users use the platfrom.
- **Marketing Analytics & Data Science**
  - Responsible for understanding how to drive more core actions (like Grants checkouts)
- **Complex Systems Insights**
  - Responsible for guiding the QF matching engine with deep analytical insights (perhaps one day even simulating agent-based contributor behaviour)
  - Responsible for  publishing advanced analytics-based insights from our datasets.  [Heres an example of what this could look like.](https://www.gwern.net/docs/psychology/okcupid/themathematicsofbeauty.html)
- **Fraud insights**
  - Responsible for (Joe, correct me if I'm wrong) surfacing fraud on the Gitcoin Grants network (whether sybil or collusion) and partnering with Governance to remediate in a legitimate way.

An assortment of tools are used in these practices at Gitcoin.  Here are the ones I'm aware of:
- Etherscan
- Dune Analytics
- The Graph
- PostgresSQL
- Google Analytics
- Metabase
- Google spreadsheets
- Google presentations
- Acquia
- CADCAD
- Machine Learning Tools (not sure which ones)

 I'd welcome corrections from any workstream leads on the above.  The above is just my best approximation of the tools/roles as they currently stand int he DAO.

I'd be curious if people in the community would be interested in putting forward a proposal to the DAO to formalize a data science practice at GitcoinDAO (which currently resides in multiple different groups at varying levels of coordination)

I'd like to end on this questions: 
1. **What should the data science practice at Gitcoin look like?**
2. If Data Science was an *area of practice* at Gitcoin, what would it look like?  
3. How could it span multiple workstreams or squads(teams) & cross-pollinate between them?

![Screen Shot 2022-03-15 at 3.58.14 PM|690x448, 50%](upload://6Y5bwATL6fQ1cP4RniJ4lGk5n7b.jpeg)

-------------------------

simba-sandy | 2022-03-17 13:27:18 UTC | #2

1. Have a dedicated analytics person working with every team- MMM, DAOops. While central teams have their advantages, core teams will either always be stuck in prioritization queue or forever unaware of how data can help and wont be as impactful as they could have been with data.
2. It might also be fair for contributors to expect to know where their grants are being put to work. An opt-in visibility tool which also helps set expectations. While we have FDD for flagging and preventing fraud, we might need a function to raise the bar on best practices for governance and fund utilization using data.

-------------------------

seanmac | 2022-03-18 17:04:15 UTC | #3

This would be so incredibly helpful. We are dramatically underinvested in this area. We have a wealth of incredible data that we can and should be using to better understand how we can better serve our stakeholders and increase our impact. MMM is just starting to scratch the surface here with work that we're doing in the growth substream but we have a long way to go. Getting support from a DAO-wide data science team is essential to our work and our ability to fulfill our mission.

-------------------------

jonas | 2022-11-08 09:56:33 UTC | #4

For the time being I think that there is a lot of work being done in silos. And just as you say, more cross-pollination between ppl that do data currently could have great benefit to improve our products. 

Data that I use day to day include; 
Traffic data
Grants performance (add to carts, checkouts)
Mobile performance
Monitoring traffic sources
Campaign monitoring (newsletters etc)

A powerful link would be data to be set in comparison with grants data from Metabase to compare and identify new opportunities for growth. 

How do we structure all this? Maybe;

1. A data scientist who can identify interesting data and create datasets based on our grants data, and do all the queries.
2. A google analytics (or similar tool) wizard who monitors user behavior and run A/B tests to continually improve our product. 
3. A product manager. 1 and 2 should work closely with the PM to understand their product better and identify pain points in the funnel and where there is potential to improve. 

One pitfall we could encounter is to create fantastic datasets and insights, but no idea how we can execute on the data. Identifying the right stakeholders and making everyone onboard will be important for the project's success. 

This also needs to align with the Web 3.0 ethos to collect as little data as possible to be able to do our job. I think transparency and inclusion of the GitcoinDAO would be crucial to be able to do this well.

-------------------------

nategosselin | 2022-03-21 21:29:32 UTC | #5

I'd love to see us invest more in this area. My .02 gwei would be to separate the idea into two pieces:

1) How do we build a scalable, modular, anti-fragile data backbone across GitcoinDAO?
2) How do we encourage a culture of using data across the opportunities within the DAO?

In my mind, #1 should be a data-focused product team with the remit to build a scalable data warehouse/system that can make data more easily available to analyst-level data users. In other words, how do we knit all of our data sources together and let SQL users get value out of it (given they have the business context)?

#2 feels like building a group of analysts and scientists (i.e. more advanced data users) that can be embedded on specific workstreams. Maybe it lends itself to a guild model like the Gitcoin Product Collective?

-------------------------

nollied | 2022-03-22 00:23:29 UTC | #6

it's interesting you post about this, i was just thinking about the feasibility of launching an AI workstream, similar to moonshot collective. 

[quote="owocki, post:1, topic:10088"]
perhaps one day even simulating agent-based contributor behaviour
[/quote]

this is what the matrix squad in FDD is working on btw.

[quote="simba-sandy, post:2, topic:10088"]
Have a dedicated analytics person working with every team- MMM, DAOops. While central teams have their advantages, core teams will either always be stuck in prioritization queue or forever unaware of how data can help and wont be as impactful as they could have been with data.
[/quote]

i think this point should be wrestled with a little more. one interesting benefit of having a dedicated AI workstream would be that these services could be provided, with the goal of creating data unions/revenue streams (carefully of course to avoid negative incentivizations).

if we did have an AI workstream, it should play a supportive role, facilitating collaborations and acting as a service to the DAO.

[quote="jonas, post:4, topic:10088"]
A powerful link would be data to be set in comparison with grants data from Metabase to compare and identify new opportunities for growth.
[/quote]

this is another benefit, the ability to cross-correlate data for insights.

[quote="jonas, post:4, topic:10088"]
This also needs to align with the Web 3.0 ethos to collect as little data as possible
[/quote]

and for the data that we do collect, the reports should be openly available.

[quote="nategosselin, post:5, topic:10088"]
In my mind, #1 should be a data-focused product team with the remit to build a scalable data warehouse/system that can make data more easily available to analyst-level data users. In other words, how do we knit all of our data sources together and let SQL users get value out of it (given they have the business context)?
[/quote]

beautifully put.

-------------------------

tigress | 2022-03-23 20:01:54 UTC | #7

[quote="owocki, post:1, topic:10088"]
1. **What should the data science practice at Gitcoin look like?**
2. If Data Science was an *area of practice* at Gitcoin, what would it look like?
3. How could it span multiple workstreams or squads(teams) & cross-pollinate between them?
[/quote]

Having Data Science as an Area of Practise or sometimes also called Community of Practise in larger web2 IT organizations is a common pattern. However, this DS-Area would not do any particular work for projects, OKRs or initiatives. Their goal is to reflect upon and improve their craftmanship by ways of learning from each other and presenting or socialising at events. If they get really productive they might develop and provide trainings for other Areas. For example: enabling developers so they learn from Data Scientists. 

There is this idea of "Team Topologies" out there that could be helping us design and visualize how we work together. And also discuss several options how Data Science could look like and interacts with others. 

![image|474x362, 100%](upload://wdUoKtpgBRIcQGw3t9Vlj1Erzqz.png)

https://www.slideshare.net/matthewskelton/beyond-the-spotify-model-team-topologies-devtestnorth-20190925-matthew-skelton

-------------------------

Fred | 2022-03-28 12:38:02 UTC | #8

@ivanmolto from Builderband helped the MMM Workstream create a [Dune Dashboard](https://dune.xyz/ivanmolto/Gitcoin-DAO) with an overview of the GitcoinDAO governance and finances. These visuals greatly increase the transparency of our DAO - and they look super cool!
Feel free to reach out with feedback.

-------------------------

umarkhaneth | 2022-03-29 02:48:15 UTC | #9

100% support this 

Giving people access to quality data, with a data dictionary, and the ability to use tools like SQL and Python will probably drive them to generate insights on their own. Data-savvy contributors who want answers will look for them -- they just might need the infrastructure/access to do so. 

This is what AWS is really good at -- although a centralized technology -- it makes it easy to have your data somewhere people can find and run more advanced analytics on using tools like SQL, & Jupyter Notebooks. It also allows for granular role-based access control. I don't know what the decentralized alternative is but would love to

-------------------------

DisruptionJoe | 2022-03-30 18:24:17 UTC | #10

Great work here. I'd love to see the number of delegators each steward has delegating to them as well. Something like this: 
![Image 2022-03-08 at 9.43.32 AM|326x500](upload://ly9n860EnH1z0rBGbkG8t4Jp9JV.jpeg)

-------------------------

Fred | 2022-04-15 09:35:47 UTC | #11

Number of delegators has been added to the table. @ivanmolto have also been working hard on an additional deep dive into our Governor Alpha set up.

Some very interesting data can be found here: https://dune.xyz/ivanmolto/GitcoinDAO:-The-case-for-Governor-Alpha

-------------------------

owocki | 2022-04-17 03:24:52 UTC | #12

[quote="Fred, post:8, topic:10088"]
These visuals greatly increase the transparency of our DAO - and they look super cool!
[/quote]

was just messing around with breadcrumbs.app tonight and was able to come up with [this sankey diagram](https://www.breadcrumbs.app/reports/1360) that allows ppl to follow the flow of GTC out of the timelock + to the workstreams + to their contributors. pretty neat!

![screenshot_1650165792123|589x500](upload://aXjBE4f0Np2trYP348YJI2khStQ.jpeg)

ivan, would love to show u breadcrumbs.app sometime.

-------------------------

Fred | 2022-04-17 19:22:18 UTC | #13

This is cool! We have discussed creating a subgraph for the Steward Health Card-project as a potential metric of engagement. The theory being that Stewards receiving GTC less than 4 hops from the multisig is a strong indicator of engagement. Especially if it's occurring month after month.

-------------------------

ivanmolto | 2022-04-20 21:22:54 UTC | #14

Yes, of course. I would love it. I didn't know about this tool. It is a result outstanding visually!

-------------------------

Pop | 2022-05-01 09:55:21 UTC | #15

this is great - I would love to use some of this for the workstream and treasury health dashboard to be added as DAO tools alongside the steward health cards

-------------------------

Fred | 2022-05-13 13:18:15 UTC | #16

@ivanmolto  and I have been looking into the correlation between **GTC outflow from GitcoinDAO** and **GTC spot price**. A common belief is that Workstreams compensating contributors with GTC would somehow negatively impact the price of GTC. We put this theory to the test through a number of queries in this [Dune Dashboard](https://dune.com/ivanmolto/Interaction) to see if it holds any water.

In order to produce a meaningful analysis we couldn’t just track GTC outflow from *Workstreams* and compare that to GTC price. To accurately test this hypothesis we need to take one step further and track GTC outflow from *contributors* in relation to price.

A common conception about contributors receiving compensation in GTC is that they will immediately sell their tokens for other assets, causing a massive sell wall and negative price movement as a result.

After analyzing 269 unique contributors over time we can see that this is far from the truth. The data show that contributors of GitcoinDAO are likely to hold their GTC and the average amount of GTC held by this group is *increasing*. The first figure below shows the number of contributors who hold more than 0, 100 and 1000 GTC respectively. The second figure displays the amount of GTC held (x100) in total by this group as well as their average GTC holdings. These metrics are all increasing.

![|624x437](upload://5bJa54r7gBIMde4m9lSFeVGyal4.png)

We could not find a correlation between GTC outflow from Workstreams and GTC price movement:

![|624x181](upload://gGBRiJIIlDYEKH0KIG5LakuhAaV.png)

As we looked further into what could impact GTC we found a correlation between GTC and other governance tokens. In general, GTC seems to be following the movements of the market sector. The figure below show the price movement of other governance tokens and GTC, relative to their price on May 25th 2021:

![|624x195](upload://w6mCosysDZK7Mja4dL0PmepI3oE.png)

In conclusion; the hypothesis that sending GTC to Workstreams who then pay contributors would negatively impact GTC price can **not** be proven through the data. GTC *is* however correlated to similar tokens in the sector.

We encourage you all to look through the [dashboard](https://dune.com/ivanmolto/Interaction) and we welcome feedback on ways to improve these further. A couple of additional visuals and tweaks will be added to the dashboard in the coming days.

Enormous shoutout to @ivanmolto for the amazing job.

Our two previous dashboards can be found here:
[GitcoinDAO: Governance & Financial overview
](https://dune.com/ivanmolto/Gitcoin-DAO)[GitcoinDAO: Governor Alpha & Timelock](https://dune.com/ivanmolto/GitcoinDAO:-The-case-for-Governor-Alpha)

-------------------------

ivanmolto | 2022-05-12 22:08:31 UTC | #17

The same to you @Fred It has been an amazing job side by side with you. Please all you enjoy the insights!

-------------------------

Lunacat | 2022-05-12 23:42:21 UTC | #18

Great to see some data!  Thanks for taking effort and time to put together.

> After analyzing 269 unique contributors over time we can see that this is far from the truth.

Does this mean data set is limited to these 269 individuals over the entire time frame?  So any contributor that may have joined in Feb 2022 would not be counted?

> In conclusion; the hypothesis that sending GTC to Workstreams who then pay contributors would negatively impact GTC price can **not** be proven through the data.

Assuming the population is constant throughout the period, the conclusion is undeniable.  But concerns right now are more forward looking -- it's easy to hold an appreciating asset, especially given most contributors have likely been sitting pretty from wider market during this time.  Will be interesting to revisit this after each round and see how trend develops in response to wider market turmoil

-------------------------

Fred | 2022-05-13 06:53:20 UTC | #19

I could have clarified the "269" number a bit better. 
269 is the current number of total contributors we are able to identify on-chain.

On May 25th 2021, when GitcoinDAO launched, we had 0 on-chain contributors. Now we've reached 269. A visual for the number of total contributors over time can potentially be added to the dashboard for clarity! 

In my opinion we have seen some pretty big market turmoil in the last months but I absolutely agree, it will be very interesting to see how things evolve. Thanks!

-------------------------

kishoraditya | 2022-05-13 07:10:22 UTC | #20

This is great @Fred and @ivanmolto 
It would also be great to see if or not rounds exhibit any trend in pricing of GTC!

-------------------------

Pop | 2022-05-13 07:57:15 UTC | #21

Totally missed this in March - what an interesting insight into representation

-------------------------

Pop | 2022-05-13 08:05:49 UTC | #22

Great work @Fred and @ivanmolto - It is always important to look towards data, especially in a highly charged dynamic like a market downturn. It's easy to make assumptions yet we must always keep ourselves in check to ensure governance decisions are not made emotionally but rather objectively and from a fully informed place of intention.

When we were discussing this and even though I had an inkling the contributor sell could not affect things as much, I really did not grasp just how much hodling was actually going on. The same with the pattern of other gov tokens which is why I made the suggestion to add that chart in order to give place this analysis against the broader market background.

I am keen to see these analyses progress and become a tool in the gov process. Perhaps, something we look to include in the improved versions of workstream accountability flow or in any voter matrix we may choose to adopt - provided they achieve balance between objectivity and personal takes.

-------------------------

myceliumcoordinator | 2022-05-16 15:34:35 UTC | #23

[quote="Fred, post:16, topic:10088"]
In conclusion; the hypothesis that sending GTC to Workstreams who then pay contributors would negatively impact GTC price can **not** be proven through the data. 
[/quote]

The inverse is also true!   This analysis does not show that selling tokens to market DOES not create downward price.

[quote="Fred, post:16, topic:10088"]
We could not find a correlation between GTC outflow from Workstreams and GTC price movement:

![](upload://gGBRiJIIlDYEKH0KIG5LakuhAaV)
[/quote]

How can you draw that conclusion from that graph?  You just showed a bunch of data that has a bunch of outflows and a large decline in price.  There's no rigor to this analysis method.  There's no control group, nor is there any analysis of the liquidity of the market in this analysis.

[quote="Fred, post:16, topic:10088"]
In general, GTC seems to be following the movements of the market sector.
[/quote]

[quote="Fred, post:16, topic:10088"]
GTC *is* however correlated to similar tokens in the sector.
[/quote]

GTC is down 50% vs ETH over the last 30 days, so I dont think you can say the outflows are in line with the rest of the market decline.

This chart is from [coingecko](https://www.coingecko.com/en/coins/gitcoin/eth):
 
![foto.jpeg|690x130](upload://7qhWBVwfvPmyn70uUM7qg274lRl.png)

I think doing an analysis about this could be important, but more rigor is needed to be able to form conclusions backed by data in my opinion.

-------------------------

umarkhaneth | 2022-05-16 17:57:48 UTC | #24

Hey! I really enjoy the discussion here. I would love to get an hour on the calendar to pull together various people with data backgrounds or interest within the DAO. We could do some introductions and share projects we're working on.

Please fill out this lettuce meet if you're interested: https://lettucemeet.com/l/XDZrr 

All are welcome!

-------------------------

php | 2022-05-16 21:38:08 UTC | #25

Maybe this way:

the practise only deal with data anonymisation, and data infrastructure, and model performance evaluation.

With anonymised data, all the rest can be put as bounty so be publicly worked on by any contributors

-------------------------

David_Dyor | 2022-05-24 22:25:12 UTC | #26

What an interesting and unexpected find.  Thanks for this work!

-------------------------

Fred | 2022-06-06 12:35:54 UTC | #27

Late reply here, but we’ve been hard at work getting data from off-chain CEXs added to the dashboard. This has proven to be harder than we anticipated, however we are now able to track sales from contributor addresses across all of the major CEXs which has been a big milestone.

[quote=myceliumcoordinator, post:23, topic:10088]

The inverse is also true! This analysis does not show that selling tokens to market DOES not create downward price.

[/quote]
[quote=myceliumcoordinator, post:23, topic:10088]

How can you draw that conclusion from that graph? You just showed a bunch of data that has a bunch of outflows and a large decline in price. There’s no rigor to this analysis method. There’s no control group, nor is there any analysis of the liquidity of the market in this analysis.

[/quote]

I think you misunderstood my previous post; we could not *find* a correlation with our current data and methodology. Not being able to prove a hypothesis does not necessarily mean that the opposite is true.

Circling back to sell pressure from contributors;
We’ve recently added a graph over relative GTC price vs daily total contributor sales (DEX+CEX).
(A correlation analysis has not yet been initiatied at this point):

![bild|690x239](upload://fL0kb0otNYF5HzhQJnh5PaJ5LkD.png)


Even though we are now able to track *contributor* sales on CEXs we’ve yet to find a way to get accurate *total* CEX volume into the dashboard. Until we have this data available natively in Dune I’ve grabbed the daily volume (CEX+DEX) from Coinmarketcap and Coingecko and plotted this graph:

![|624x476](upload://mNP1qx3OD1rLElHt14DGU3T5C13.png)

The volume has stayed between 1M - 10M GTC per day for the majority of GTC’s history.
Median GTC volume according to Coinmarketcap = **2.7M GTC/day**.
Median GTC volume according to Coingecko = **2M GTC/day**.

This is the graph of total GTC sales from contributors on DEX & CEX:

![bild|690x189](upload://npBpVc3IR75AEqU5qruptg8baq1.png)

Even on days of relatively large GTC sales from contributors, **10k GTC/day**, contributor sell pressure is still **less than half a percent** of the median daily volume.

(10k GTC/day is roughly equivalent to the 90-95th percentile. A normal distribution graph of contributor sell pressure is in the works. This will allow you to grab any percentile of contributor sell pressure and compare that to the total daily volume.)

[quote=myceliumcoordinator, post:23, topic:10088]

GTC is down 50% vs ETH over the last 30 days, so I dont think you can say the outflows are in line with the rest of the market decline.

[/quote]

I think you’ve misunderstood the governance token part of the dashboard as well. We are comparing GTC to other *governance tokens*, which are *all* down vs ETH.

For convenience we've now grouped together other governance tokens into a basket on the graph. Although we haven’t initiated a proper correlation analysis to define the strength of the association, a correlation is clear:

![bild|690x239](upload://2Oxd0APfAbKowe02BSbiL2srhJX.png)

[quote=myceliumcoordinator, post:23, topic:10088]

I think doing an analysis about this could be important, but more rigor is needed to be able to form conclusions backed by data in my opinion.

[/quote]

As stated earlier, the dashboard will receive continuous updates as we are able to track more data. I’d be happy to continue the conversation and discuss things further if you are interested in helping out!

(Please note that Dune is performing internal upgrades at the moment and some graphs will not load properly until this work has been completed. The dashboard may also be slower to load)

-------------------------

keneeze.eth | 2022-06-06 11:52:17 UTC | #28

Thank you for all the good work you do, I agree that Data Science should be one of the priorities of the Gitcoin DAO, the insights that can be gleamed from a well done data analysis model could be a big help in further optimizing the entire grants system.
There is a popular saying where I come from, it goes this way.
“In God we trust, everyone else should bring data” I believe that at the heart of everything Gitcoin is trying to achieve with public goods, being able to keep track of the true impact of Gitcoin’s operations both within the Gitcoin Ecosystem and to the wider ethereum community could give the leadership a true sense of where the DAO is and precisely where it should be going, the results of a good data culture could serve as the best possible compass for Gitcoin DAO, the answers are all in the numbers.

- keneeze.eth🔥_🌱 (Wildfire DAO, Public Goods Operator)

-------------------------

mixmore | 2023-10-22 10:04:08 UTC | #29

I will try to be as short and simple as possible.

Data science is a very broad field with multiple areas, like data analysis, statistics, mathematics such as differentiation and integration, linear algebra, dealing with databases, SQL, big data, business intelligence, machine learning, deep learning, artificial intelligence, dealing with natural languages, image classification, reinforcement learning, and simulation. There are also other areas under data science.

But initially, let's try to choose some tools that can benefit us in Gitcoin.

There are many other tools, but let us now mention only these tools.

One of the tools of data science is the use of programming languages and their various libraries. The most famous programming languages used in data science are Python and R, but the majority depend on Python.

There are many libraries related to data science, but let us mention some of them. TensorFlow Keras Scikit-learn PyTorch NumPy Pandas Seaborn Matplotlib

And other tools, such as Excel

Statistical programs can be useful. There are free, open-source, and powerful programs like JASP.

Business intelligence programs such as Microsoft Power BI, Tableau, and Google Data Studio are very useful in building a control dashboard that summarizes data, tracks it, and does other things.

Statistics and mathematics are essential in data science. It can be used by statistics programs or by the Python programming language, and some of the libraries associated with it Statistics is a very broad field and is fundamental to data science.

dealing with databases and the SQL language

Data visualization

Machine learning and deep learning help predict, classify, and cluster.

Tools that help in the field of crypto

There are also many tools here, but let us mention some of them.

Blockchain network browsers

Dune Analytics, Flipside Crypto, and Footprint Analytics

The Graph

Tools like Defillama,Token Terminal, Coin Market Cap, Coingecko, Glassnode, Debank, Tradingview, Messari, and other tools

Data science is useful in any department and in anything, as long as there is data related to it.

Like any crypto project, data science will help in these departments.

**Products Department:** 
For any product, we will find that there is data related to it, and by analyzing it, the performance of these products can be greatly improved and also developed.

**Financial Department:**
Analyzing financial data is very useful in developing future financial plans, improving current financial performance, and finding solutions to financial problems.

**Marketing department:**
I think it is essential that the use of data science is very beneficial to the marketing department, and the use of data science is a long explanation that requires a separate topic.
Governance and community management:
Data science is very useful when analyzing data in forums. Snapshot, Discore, and other governance tools will be very useful in improving decentralization and decision-making processes.

**External environment:**
Analyzing competitor data and crypto market data in general may sometimes be more important than data analysis for the project itself.

**Research and development:**
Data science helps with the reports and insights extracted in the research and development department, if there is such a department in any crypto project.

Machine learning and deep learning tools related to classification and clustering can be used to build tools that contribute to increasing security in products, but this is a complex topic that would take a long time to explain.

Simulation can also be used to develop some decisions and some products, and some machine learning, deep learning, and artificial intelligence tools can help in this.

Providing data analysis reports to the community helps increase transparency and decentralization.

Public management benefits from all reports generated by all departments.

**Now, how will things go?**

The first step is to determine the data sources. Where can the required data be obtained?
The most difficult point is how to deal with it, meaning that if the required data is stored in databases, then it is easy to deal with, but if they are, for example, on a website, then we will need to write code to scrape data from this website. There are other cases in which data is stored, and each case has different solutions.
Sometimes it is not possible to extract data.

It is important to know the goals of each department.

What is the goal?

After defining the goal, we can know the questions related to achieving it.

We will use data science to find answers to these questions.

I will give a very simple example. To explain it,
If I had a goal, for example, to write topics on this forum that would receive a lot of interaction,

This is the goal.

Therefore, there are questions related to this goal: What are the topics and trends that can achieve interaction? How can I know that?

Using data science, I will analyze the data on this forum to find which topics have the most interaction and, therefore, know what direction I should write about.

This is how things work. Every department has goals, and these goals produce questions. By analyzing the data, we try to find answers to these questions.

If we can organize the data extraction process, the rest of the steps will be easy.

Data science and how to use it I can write several topics about it and publish them here on the forum if this is allowed.

I am open to discussion.

-------------------------
