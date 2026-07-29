---
id: 18602
title: "Gitcoin could embrace the Unix Philosophy to create exponential innovation 📈"
slug: gitcoin-could-embrace-the-unix-philosophy-to-create-exponential-innovation
category: open-discussion
url: https://gov.gitcoin.co/t/gitcoin-could-embrace-the-unix-philosophy-to-create-exponential-innovation/18602
created_at: 2024-04-15T21:50:27.732Z
last_posted_at: 2024-04-17T17:23:07.638Z
posts_count: 3
views: 3172
like_count: 15
---

# Gitcoin could embrace the Unix Philosophy to create exponential innovation 📈

<https://gov.gitcoin.co/t/gitcoin-could-embrace-the-unix-philosophy-to-create-exponential-innovation/18602>
owocki | 2024-04-16 20:06:37 UTC | #1

# Gitcoin should embrace the Unix Philosophy to enable exponential innovation

## TLDR

1. The unix philosophy is to (1) build small modular tools that do one thing + do them well (2) make them interoperable with each other.
2. The unix philosophy is a powerful way of developing software because the tools are supermodular to one another (supermodular = exponential value creation)
3. We should adopt the unix philosophy at Gitcoin.

## What is Unix Philosophy?

The Unix philosophy embodies a set of cultural norms and philosophical approaches to minimalist, modular software development. It emphasizes building simple, short, clear, modular, and extendable code that accomplishes a single task well. This philosophy is foundational to the development and design of Unix and its various offspring, including Linux. Key tenets of the Unix philosophy include:

1. Make each program do one thing well: Instead of creating complex programs that attempt to do many tasks, Unix encourages developers to build simple programs focused on one task. This makes the programs easier to develop, understand, and maintain.

2. Expect the output of every program to become the input to another, as yet unknown, program: This encourages the design of programs that can work together, using pipelines and filters to pass data from one utility to another.

3. Design and build software, even operating systems, to be tried early, ideally within weeks: This principle emphasizes the importance of quick prototyping and iterative development.

4. Build a prototype as soon as possible: Similar to "try early", this principle pushes for a working model that can be tested and improved upon, rather than trying to make it perfect the first time.

5. Use software leverage to your advantage: Reuse code when possible instead of reinventing the wheel, benefiting from the collective effort of the developer community.

The Unix philosophy has influenced not only the development of Unix and Linux but also the design of software and operating systems across the computing landscape. It emphasizes efficiency, simplicity, and the importance of open standards and interoperability.

## Why is the Unix Philosophy powerful?

The Unix philosophy's power lies in its emphasis on simplicity, modularity, and composability, principles that make software development more efficient and maintainable. By advocating for programs that do one thing well and work together seamlessly, it ensures systems are both robust and adaptable. This approach reduces complexity, making software easier to understand, debug, and enhance over time. Additionally, the focus on a universal interface and the encouragement of rapid prototyping and tool reuse accelerates development and fosters innovation, allowing developers to quickly iterate on ideas and leverage existing solutions.

Moreover, the Unix philosophy's emphasis on portability and open standards has broadened software's utility and longevity, ensuring applications can run across different environments and evolve alongside technological advances. This has not only democratized access to technology but also cultivated an ecosystem where interoperability and collaboration are foundational . As a result, the Unix philosophy has had a profound and lasting impact on software engineering, influencing not just Unix-derived systems but the broader landscape of computing and development practices.

The modular approach supports the dynamic, distributed nature of DAOs like Gitcoin’s. The unix philosophy enables continuous integration, development, and community-driven innovation, making it a fitting philosophy for this new era of software development.

## Monolithic software

Monolithic software contrasts sharply with the Unix philosophy through its approach to design and functionality. Where the Unix philosophy advocates for simplicity, modularity, and the development of small, interoperable programs that each perform one task well, monolithic software typically bundles a wide range of functionalities within a single codebase. This integration means that tasks and features in monolithic applications are deeply entwined, making it challenging to modify, update, or scale individual components without affecting the entire system. As a result, monolithic systems can become complex and cumbersome, hindering rapid development and adaptability.

While monolithic applications may initially be simpler to deploy and manage, the Unix philosophy's approach typically offers greater efficiency, adaptability, and resilience over the software's lifecycle.

## Modular software @ Gitcoin

Having built Gitcoin 1.0 the wrong way (cGrants was a monolith that was expensive and slow to maintain)... I believe that Gitcoin should fully adopt the unix philosophy in its software development.

This is already partially true.

1. Our software is built upon modular blockchains.
2. Allo protocol contains several different strategies: QF, RetroPGF.
3. Grants stack contains several small applications:
   1. Explorer - for browsing grants
   2. Builder - for building grants
   3. Manager - for making QF rounds

But it is also partially false

1. Allo strategies are all in the same repository.
2. Allo strategies do not have corresponding webapps.
3. Grants Stack’s modular apps are bundled into one repository and for many intents and purposes, one monolithic app.
4. We are beginning to develop monolithic tendencies as a team (merging modular tools.

## Modular software @ Gitcoin would enable bottoms up innovation

Right now the core apps at Gitcoin are

1. Explorer - for browsing grants
2. Builder - for building grants
3. Manager - for making QF rounds

These apps work pretty well for what they do.. But let’s explore things they don’t do.

1. Explorer is a plain vanilla way of exploring grants. What other types of grant exploration are possible?
   1. AI powered discovery of grants
   2. More powerful search functionality
   3. More powerful collections / curation functionality
   4. Social discovery of grants (eg see what my twitter/farcaster network is funding)
   5. Using collaborative filtering and/or a tinder style interface to fund grants
   6. A whitelabel manager that a partner who wants
   7. [One click donations on farcastser frames](https://twitter.com/OrnellaWeb3/status/1775258764570186002)
   8. Fiat checkout
2. Manager is a plain vanilla way of creating a QF campaign. What other types of campaigns are possible?
   1. A manager that uses an LLM to study my community and recommend intelligent defaults
   2. An Openzeppelin-wizard way of creating a manager from an allo strategy.
   3. A results calculator/verification tool - so I dont have to
3. Builder
   1. [Pub/Sub](https://gov.gitcoin.co/t/pubsub-on-allo-v2/17742)
   2. [Allowlist Configurability](https://gov.gitcoin.co/t/allowlist-configurability-a-strategic-investment/17741)
4. Other design spaces to explore
   1. [Aqueducts](https://gov.gitcoin.co/t/gitcoin-aqueduct/9684) -
   2. Tools to crowdfund matching pools.
   3. Karma/Impact Certs
   4. KYC/Compliance Tools
   5. GTC Token Center
   6. AlloScan
   7. [Other things mentioned in the rainbow paper](https://www.gitcoin.co/rainbowpaper)
5. Other funding mechanisms
   1. Maci QF
   2. RetroPGF
   3. Conviction Voting
   4. etc..

If these apps were to be build by our centralized team in a monolithic and sequential way, I am certain it would take decades to do it. Because we’d be doing it single threaded. And we’d have to go through a complicated regression/QA process for each new feature to make sure we didnt break anything.

If we built these decentralized, then our community of citizens can explore these design space without permission.

Here is what i think the design space exploration looks like visualized.

![|624x276](upload://aEc1LhyvgDuWHOUuAVMcMcsRilV.png)

## It's already happening

I am super proud of two modular apps that have been built.

1. ReportCards.Gitcoin.co - a tool for getting a visual of how a QF round is going.
2. Checker.Gitcoin.co - a tool for automating (and augmenting with LLMs) the checking of multiple grants in application queue for a round.

The developers behind both of these projects realized there was a design space that was underexplored by the main Grants Stack app… and took the initiative to build apps that explored the design space in high resolution. Awesome!

## Modular software @ Gitcoin would enable a culture of autonomy within Grants Lab

Autonomy in software development shops is crucial because it fosters a culture of innovation and ownership, leading to the creation of more efficient and effective solutions. When developers have the freedom to make decisions about their work, they're more engaged and motivated, which translates into higher productivity and better problem-solving. Autonomy encourages a deeper understanding of the project as a whole, the problems being solved, enabling developers to anticipate issues, adapt to changes more swiftly, and contribute ideas that can lead to breakthroughs in development practices and end products.

## Modular software @ Gitcoin would enable a culture of intrepreneurship within Grants Lab

Intrapreneurship refers to the practice of applying entrepreneurial skills and approaches within an existing organization to develop innovative products, services, or processes. It encourages employees to take initiative, embrace risk-taking, and pursue innovative ideas as if they were external entrepreneurs, but with the resources, support, and structure of their current employer. This approach fosters a culture of innovation and agility, allowing companies to stay competitive and adapt to changing market dynamics by leveraging the creativity and entrepreneurial spirit of their workforce.

## Modular software @ Gitcoin would enable citizens to create massive tailwinds around gitcoin.

A modular setup encourages a wide range of developers to participate and contribute, as it provides a transparent, trustless system for collaboration. Engaging with an open-source community is crucial for a DAO like ours, as it taps into a global talent pool, accelerating development, fostering innovation, and ensuring the software evolves in response to user needs and emerging trends.

## Challenges

1. We need a way for modular apps to have a shared source of truth for their shared dependencies: L2 network lists, allo contracts + deployment addresses, etc..
2. DevEx - Our developer experience needs some work. For example, great docs + a starter kit. [More on this here. ](https://gov.gitcoin.co/t/allo-v2-b2d-strategy/17744)
3. Integrated ux
   1. For Gitcoin to have worldclass software, we may need a unified navigation across these modular apps. This nav would solve for the discoverability of the apps in the Allo/Gitcoin ecosystem (even I can’t keep track of them right now and i’ve been trying to at https://ecosystem.gitcoin.co/)
   2. There are some clunky things if the apps are deployed seperately. EG having to “connect wallet” separately across explorer.gitcoin.co manager.gitcoin.co and builder.gitcoin.co
   3. Its possible that “weaving” apps will need to be build that weave together various modular apps.
   4. There might be some opportunity to combine modular tools into a thin monolithic app that is a thin wrapper around git submodules of smaller modular apps.
4. Architecture - a few of us did an [architecture evaluation](https://gov.gitcoin.co/t/opening-up-grants-stack-allo-to-more-community-contributions/17145) a few months ago. We would need to revisit + make some decisions about what exactly the architecture/ground rules are for this next era.
5. Maintenance
   1. How are modular packages maintained in a world where those maintainers could go away?
6. Problem/idea exchange - we need a clearing house for exchanging ideas for modular builds + feedback on modular builds.

## Conclusion

In conclusion, unix philosophy is good. It's been repeatedly proven over decades. Let’s adopt it.

Feedback welcome.

-------------------------

quaylawn | 2024-04-17 11:01:12 UTC | #2

No feedback from me as I'm not a techie, although I do wonder if you'd be open to pushing your thoughts on this subject out a bit more publicly. The governance forum doesn't contribute to our *Share of Voice* on these topics, so I'm thinking something along these lines: 

https://www.coindesk.com/consensus-magazine/2024/04/16/what-the-history-of-linux-says-about-the-long-road-to-decentralized-storage-adoption/

I noticed that Linux has featured in the media alongside a discussion on the vulnerabilities of open source tech, specifically [social engineering attacks](https://usw2.nyl.as/t1/43/5604jhfwzv4lji64lntncksh0/0/514592e492460407396ad81b99b70f6a814547034de61a79fb980e162838a9a2) or attempts to exploit [licensing loopholes](https://usw2.nyl.as/t1/43/5604jhfwzv4lji64lntncksh0/1/f10d53b63d7186c5c5ad03921d52aead337512257d2871f23c01ceda5ef8161c).

As **Claudia Richoux** mentions in the CoinDesk opinion piece, "open source codebases are hard to kill", but that doesn't mean it doesn't need protection. 

Building on the data from @ccerv1, as well as the narrative around our return to supporting digital public goods and ecosystem growth, I think this could be a great chance for us to capture a greater *Share of Voice* in relation to OSS. More broadly, this would support our overarching mission to position Gitcoin at the centre of all things web3 grants. 

Currently our dominance in this regard, mapped against 5 other prominent decentralised organisations, is ~42% over the last four months. Happy to share the Notion page where this data has been captured if of interest!

-------------------------

owocki | 2024-04-17 17:23:14 UTC | #3

[quote="quaylawn, post:2, topic:18602"]
No feedback from me as I’m not a techie, although I do wonder if you’d be open to pushing your thoughts on this subject out a bit more publicly.
[/quote]

I'm happy to do it.  But I dont think there will be a lot of demand for content about how Grants lab / Gitcoin does software development unless/until Gitcoin is seen as leading the market in some way (eg is innovative/effective/etc) using this approach.

-------------------------
