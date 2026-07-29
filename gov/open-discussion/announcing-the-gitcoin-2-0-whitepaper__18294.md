---
id: 18294
title: "Announcing the Gitcoin 2.0 Whitepaper"
slug: announcing-the-gitcoin-2-0-whitepaper
category: open-discussion
url: https://gov.gitcoin.co/t/announcing-the-gitcoin-2-0-whitepaper/18294
created_at: 2024-03-12T01:23:50.483Z
last_posted_at: 2024-03-13T20:01:22.008Z
posts_count: 2
views: 4080
like_count: 15
---

# Announcing the Gitcoin 2.0 Whitepaper

<https://gov.gitcoin.co/t/announcing-the-gitcoin-2-0-whitepaper/18294>
meglister | 2024-03-12 01:24:55 UTC | #1

Last week at EthDenver, I had the honor of introducing Gitcoin's 2.0 whitepaper with my coauthor @owocki ! We've been working hard on Gitcoin 2.0 behind the scenes for a while, and it's exciting to have this vision live in the world. 

Here's a link to the whitepaper: https://www.gitcoin.co/whitepaper/read
Don't want to read? Here's a quick infographic! https://www.gitcoin.co/whitepaper#

I encourage you to read the paper... it's a quick 10 pages, I swear :) I'm also capturing some highlights below.

# History of Gitcoin / 2.0 Transformation
Gitcoin has been around since 2017 -- basically forever, in crypto years! During that time, we've gone through a few pivotal transformations that have led up to Gitcoin 2.0. We've recently completed the 2.0 transformation. This transformation was driven by many changes in the market, including the expansion of the Ethereum ecosystem with L2 launches, the growth of open-source development, and increasing adoption of grant programs. Gitcoin’s transformation breaks down as the following:

* Transformation from a centralized, Gitcoin-operated platform to a suite of **modularized products and protocols** that anyone can use and build on top of.
* Transformation from only Quadratic Funding to **many types of capital allocation** mechanism
* (Quadratic Funding, Direct Grants, Retroactive Public Goods Funding, and more).
* Transformation from Ethereum-only to being deployed across **many EVM-based networks** ‍
* (Optimism, Arbitrum, Base, Polygon, zkSync, Scroll, Avalanche, and more).

![gitcoinevolution|690x311](upload://6Iwb4OGmgKoQ7y68SCJA5wtna7f.png)

# What is Gitcoin 2.0?
Gitcoin 2.0 builds on our success in Quadratic Funding and grants programs more generally. We believe that this traction and success points to a larger opportunity in a new area, which we're calling *Capital Allocation*. Capital allocation is a simple concept: it’s the act of deciding how to distribute funding or resources. If you’ve ever paid bills, taxes, or repaid friends for a meal, you’ve allocated capital. Capital allocation is a task for most individuals but a full time job for many: governments and grant-making organizations spend vast amounts of time and money figuring out the process, logistics, and decision-making involved in allocating capital. At scale, capital allocation inevitably becomes mired in gatekeeping, rivalrous decision making, and lack of transparency and accountability. 

![image|690x488](upload://70nl1mzMscw5X1VYe6kXItToHfu.png)

Blockchain and crypto, with their programmable smart contracts, present incredible advantages towards allocating capital in an efficient, effective, and transparent manner. Gitcoin has seized this advantage by moving the entirety of our grants program onchain: from governance, creation, management, and disbursement. Moving the grants program onchain and it being open source also allows us to build a network of developers, grants programs, and capital allocators in web3 – which all ultimately benefit the Gitcoin ecosystem.

# Grants = Growth
While the market for web3 capital allocation tools is currently limited to organizations with token treasuries, we expect this market will grow by many orders of magnitude. However, 11 years after the invention of Ethereum, web3 is still in the early stages of growth. Grants have emerged as a core driver of growth in web3 – both through builder onboarding as well as retention. Builders are onboarded through grants when tokens are distributed as incentives or compensation. These grants are often given in the early stages of a project and provide crucial funding to the project, as well as visibility and validation. Many early stage builders opt to apply for grants instead of raising traditional seed funding. Grants can be disbursed much more quickly than VC capital and come with added benefits, including publicity and connections to other grantees within the ecosystem. Unlike VC funding, they don’t require builders to give up equity. Grants instead create positive-sum outcomes by distributing funding in the native currency of their ecosystem, where value may accrue if the project is successful.

![image|690x311](upload://xg3yIdWvKzwBHPwJsBMIDApa1VN.png)

Grants = Growth isn’t just theory – it’s been empirically tested and proven over the previous four years of the Gitcoin Grants program. The chart above maps [strong correlations between grant funding received and value-additive activity for a given project](https://docs.opensource.observer/blog/gitcoin-grants-impact). For every $1M that has been paid out through Gitcoin Grants since 2019, there are seven full-time developers who are still active in the project. Factoring in the crowdfund multiplier, that ratio grows to 13 retained full-time developers for every $1M put into the matching pool. These numbers are particularly impressive when you contrast them with the [$76B in venture funding](https://pitchbook.com/news/reports/q4-2023-crypto-report) that has produced roughly .1 developers per funding dollar.

# Our Solutions
The design space of capital allocation is vast. Though our first and primary focus is solving the grants use case, we’ve designed a modular solutions stack that is intended to be extensible or repeatable across many different use cases.


The stack consists of three primary layers.

1. Protocol Layer
2. Application Layer
3. Program Layer

![image|690x488](upload://7P8lZTujFHO5LUhcgE7RVq6BAVP.png)

**First, and most extensible, the protocol layer.** Allo Protocol, short for Capital Allocation Protocol, is designed to be an infinitely flexible and extensible but also trusted and precise method of capital allocation.


**Secondly, the application layer.** Gitcoin’s Grants Stack is a no-code platform for running grant programs. The app currently provides the ability for grants managers to create, manage, and run Quadratic Funding, Direct Grants, and Retro PGF grants, with plans to extend into any grants mechanism with strong popular demand. Grants Stack is an open-source dApp, which allows communities to customize their experiences by creating companion applications or even forking the application to create their own version.



**Finally, the program layer,** which is the most long standing and Gitcoin-specific part of the stack. The Gitcoin Grants program is a powerful tool to onboard and educate communities on the power of grants programs. It has run 19 funding rounds to date and distributed over $59M in funding to the Ethereum ecosystem.

# Conclusion
The evolution from Gitcoin 1.0 to Gitcoin 2.0 marks a significant milestone in the field of capital allocation, especially in the realm of public goods funding within the Ethereum ecosystem and beyond. By transitioning to a more decentralized, modular approach and expanding its funding mechanisms beyond Quadratic Funding, Gitcoin has positioned itself at the forefront of a movement towards more democratic, efficient, and transparent capital allocation practices. The expansion into various blockchain networks signifies a broadening of Gitcoin's impact, offering a scalable and flexible platform for funding public goods across the web3 space. We couldn't be more excited about what's to come.

## Acknowledgements
We would like to acknowledge those who have supported Grants on Gitcoin, including our Grantees, Donors, and Matching Pool partners.

Thank you also to our many collaborators on this paper. @MathildaDV edited this paper and @harryeastham created designs and the microsite. @ccerv1 and @umarkhaneth provided the data analysis referenced in Grants = Growth.

‍

-------------------------

Viriya | 2024-03-13 20:01:46 UTC | #2

You can now watch a [video presentation of this whitepaper here](https://www.youtube.com/watch?v=rBFSavB82hw):

<iframe width="873" height="491" src="https://www.youtube.com/embed/rBFSavB82hw" title="Grants as a Growth Vehicle" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

-------------------------
