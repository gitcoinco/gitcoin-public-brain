---
id: 19277
title: "RFP - Allo Yeeter Build"
slug: rfp-allo-yeeter-build
category: citizen-grants
url: https://gov.gitcoin.co/t/rfp-allo-yeeter-build/19277
created_at: 2024-08-22T17:40:59.547Z
last_posted_at: 2024-10-26T02:20:46.508Z
posts_count: 11
views: 5284
like_count: 46
---

# RFP - Allo Yeeter Build

<https://gov.gitcoin.co/t/rfp-allo-yeeter-build/19277>
deltajuliet | 2024-08-22 17:40:59 UTC | #1

Continuing from Mathilda’s [Updated Citizen Grants strategy](https://gov.gitcoin.co/t/citizen-grants-program-updated-strategy/19203) & Owocki’s [6.9M Citizen’s Fund Temp Check](https://gov.gitcoin.co/t/temp-check-6-9m-gtc-citizens-fund/19204) - Gitcoin presents the latest RFP for the community to weigh in on. We expect to have more as we march towards Devcon, and a backlog of ideas and projects we like to include our community in helping us build. For further context on previous initiatives like this, check out the [Citizen’s Grant Program Announcement](https://gov.gitcoin.co/t/proposal-gitcoin-s-citizen-grants-program/17470) - the initial version of our Citizen’s Grant program. 


## TL:DR

Allo Yeeter is a smart contract toolkit aimed at simplifying capital allocation within the Gitcoin ecosystem. This RFP seeks proposals to develop and integrate Allo Yeeter into our tool suite, focusing on transformative ideas that align with Gitcoin's vision for a regenerative web3 environment. You can learn more (and best) from @owocki's Loom and Figma below. 


## Description

Allo Yeeter is envisioned as a smart contract toolkit designed to facilitate very simple capital allocation. The goal is to leverage Gitcoin’s expertise in public goods funding to create a robust, simple, and user-friendly tool that will drive innovation in capital allocation mechanisms. We are looking for proposals that will help us turn this idea into a reality, integrating it with existing tools and ensuring it aligns with Gitcoin's broader strategic goals.


## Motivation & Target Fundees



* Allo GMV - Drive grants, innovate on capital allocation mechanisms, and expand educational outreach. 
* Builders/Innovators 


## Stakeholders



* RFP Manager - @deltajuliet : Responsible for overseeing the entire process, evaluating proposals, and managing the project.
* Internal Stakeholders @owocki: Gitcoin’s core team members, who will provide input and feedback throughout the project.
* Community Stakeholders: Gitcoin community members, who will be engaged during testing and feedback phases.


## Resources



* [Loom Walkthrough](https://www.loom.com/share/52fef4d7674548fbb9cd4426e076c017)
* [Figma Designs ](https://www.figma.com/design/ndyaRwScJSs9lIo02VQwEv/Allo-Yeeter?node-id=0-1&t=0TCOUnM8JGY61gdN-0)


## Scope of Work



* Creation of the Allo Yeeter smart contract toolkit, including all necessary components for capital allocation.
* Testing - with iterations based on feedback from the community and internal stakeholders.
* Demo - Live demo with the Gitcoin community 
* Documentation for both developers and users, ensuring the toolkit is accessible and easy to understand
* Light Design to polish shared Figma - Gitcoin branding will be shared. If you are a team that does not believe you have the design resources to apply, we still encourage you! We can work with you, the community and our internal resources to ship. 
* Published Retrospective 


## What tools/access will this RFP need



* Allo Fork 
    * 2.1 
    * Allokit
    * Indexer
* Figma or other design consideration
* Hosting


## Selection Criteria

Proposals will be evaluated based on the following criteria, there is an older RFP template [here](https://docs.google.com/document/d/1LxpAmQXNDOPKVouUYnUar1ZOb-4gvtXUmROiArZAL8s/edit?usp=sharing) for reference:



* Competency of building the tool end to end. Especially React skills + smart contract dev xp will be prioritized.
* Demonstrated ability to develop and deploy smart contracts and blockchain-based tools.
* Proposals should have realistic timelines with clear milestones and deliverables.
* Proposals should include a plan for engaging the Gitcoin community throughout the development process.
* Proposals should link to Github, or other similar (published) work and testimonials 


## Timeline

This is a proposed submission timeline and is subject to change based on number of proposals submitted. Should a suitable proposal not be submitted within the 5 day period, the stakeholders (@@) will notify the community with reasoning and an updated timeframe. 



* Proposal Submission Period: Open for 5 days following the RFP announcement which is suitable time for prospects to review the above Loom and Figma file for context/ask questions here in the forum. 
* Evaluation Period: Winning bid selected within 3 days of submission period closure.
* Project Commencement: Work begins immediately upon selection.
* Milestones: Midway update, ¾ project progress presentation, final delivery, and retro publication.


## What we (Gitcoin) think this is worth 

For this initial RFP - we’d like to ask the community to weigh in on strategies to use for budgeting in the future. Including (but not limited to) hourly rates, cap sizes for proposals and locking GTC. For this specific project - we suspect ~2 weeks worth of time to implement but will consider all proposals based on the team, structure and quality. 


## Evaluation & Announcement

At the close of the submission period, the RFP manager and workstream will select the winning bid according to the criteria. Any adjustments to the criteria will be published.


## Commencement of Work

The winning proposer will commence work immediately, following the milestones and timelines specified in the RFP. Compensation will be disbursed upon the achievement of each milestone.


## Evaluation and Lessons Learned (Retro)

Upon conclusion, the project will be evaluated with an after-action report. Feedback from the RFP manager and community will be documented to refine future processes.





## Hazards and Lessons Learned



1. Allokit is still in its infancy
2. Indexer v2 not ready yet, 2.1 contracts are in testnet.
3. No Devrel/Documentation as of right now

-------------------------

deltajuliet | 2024-08-26 17:30:29 UTC | #2

Updating with some notes on @owocki's X engagement! 

I'm chatting with @noahchonlee tomorrow on his idea to prize it up! 

> Would this work better as a prize? 
> Rfp = looks for bids for lowest price
> (Builders bid lower)
> Prize = builders are hooked seeing an amount, and it can be crowdfunded
> (Funders bid up until builder bites)

and @sophia suggested connecting Hypercerts. 

> would be so cool to connect this to a hypercert. so as you mint it automatically yeets to all the addresses of owners
> 
> [@bitbeckers](https://twitter.com/bitbeckers)
> [@holkexyz](https://twitter.com/holkexyz)

Will give further context and info as it comes up. :black_heart:

-------------------------

noahchonlee | 2024-08-28 00:58:48 UTC | #3

Great call! 

Inspired me to write up a full RFP vs prizes comparison...

**RFPs vs Prizes**

|**Request for Proposals**|**Crowdfunded Prizes**|
| --- | --- |
|1. Builders bid down|1. Funders bid up|
|2. Funder chooses who works on it|2. Builders decide amongst themselves who works on it|
|3. Guess who will do the best|3. Choose who did the best|
|4. One entity is chosen to build it|4. Multiple entities can compete or merge into one team|
|5. Pay per hour or in milestones|5. Paid for how much demand is fulfilled|
|6. Funds have been sent whether a failure or a success|6. Funds awarded after evidence of success, or refunded if not|
|7. Traditional and established|7. Fun and engaging|

Let’s unpack that.

**1. Who Bids + 2. Who Chooses the Pursuer + 3. How to Choose the Winner**

A request for proposals (RFP) works like so:
-A company, community, or government releases a description of what they need built

-Builders respond with a “bid” describing how much they would need to be paid, a time estimate, and why they should be trusted to do a good job. **(1. Builders bid down)**
-The company chooses one of the builders to take the contract **(2. Funder chooses who works on it)** who they believe will do the best job at a reasonable price. **(3. Guess who did it best)**

A crowdfunded prize works like so:

1. A company, community, or government releases a description of what they need built and a deadline for when it should be done

2. They and others may add funds to a prize for building it, and depending on whether capable builders respond with interest, they may add more to incentivize builders **(1. Funders bid up)**

3. Builders who expressed interest may communicate with one another to decide who will pursue the prize (<b>2. Builders decide amongst themselves who works on it)</b>
4. Funders choose the winner(s) (**3. Choose who did the best)**

**4. One Pursuer or Multiple**

Unlike in an RFP where one group or person is chosen to take the contract, prizes are open for multiple teams to pursue and submit evidence of their work.

At viaPrize we have found that when multiple teams want to pursue a prize, about 1/3 of the time they decide that it would be fun to compete.
This could lead to a redundant duplication of effort and result in a disappointed builder who doesn’t win, but so far this has gone well because some builders just want the experience and they were informed if there were others also working on it. We also make it possible to split the prize amongst multiple winners.
However, most of the time builders don’t compete. Maybe a 1/3 of the time the builders decide to work together and around 1/3 of the time they decide amongst themselves who would be the single best person to work on it.

In other words, a prize leaves it more open for interested builders to both decide to compete or collaborate by merging into a new team. Additional builders can also participate in the efforts and be added to the team throughout the process because who is working on something is not decided upfront by the group posting the idea.

**5. Pay Style**

RFP also tends to pay builders per hour or in milestones.

A crowdfunded prize however is a pool of proven demand showing how much money people committed to an idea that they want to be turned into reality.
Whoever makes that happen collects the award and thus is paid for the amount of demand they fulfill rather than per hour, which is closer to an entrepreneurial model of work.

**6. When Funds Are Sent**
Builders also take on more entrepreneurial risk because if they do not succeed, they will not receive the award because the funders have the guarantee that they will either receive what they asked for or they get their money back.

**7. Motivation**

We’ve found that the format is fun and celebrates builders while also providing guarantees to funders, and this often motivates incredible results. One of our earliest prizes consisted of 2 people each adding $50 to build a productivity app which someone from Ukraine built, donated the money, and it has now received over 10,000 downloads. (See Intenty in the Google Play store.)

In the future we could add voting or quadratic funding to disburse matching funds into a prize, but it’s fascinating to note that a prize is already quadratic psychologically even if the amount of money added to it isn’t. We’ve found that a potential prize pursuer is far more motivated if they see that multiple people are supporting an idea. In other words, their motivation is quadratic.

RFPs are more established and traditional than prizes, and both RFPS and prizes have their own strengths and weaknesses…

What do you think?
Would you prefer to add money to an RFP or a prize?
Would you rather work on an RFP or a prize?

At viaPrize we are not just founding a company. We are pioneering an entire new economic mechanism. However, anyone can do this. Just like how Gitcoin pioneered quadratic funding, we welcome anyone to join this endeavor and we will share what we discover along the way.

-------------------------

deltajuliet | 2024-08-29 18:41:02 UTC | #4

You're fantastic @noahchonlee, really appreciate your enthusiasm and [the work you've done to innovate donations.](https://gov.gitcoin.co/t/we-donated-to-gitcoin-projects-with-credit-card-review-of-paypal-fiat-payments-in-gg21/19287) 

I'm 100% down to turn this into a prize, it means we can open up venues for running rfps on Grants Stack & Allo, extending to Farcaster and having partners join in. 

In fact, this RFP already has a "Part 2" we're considering. @Sov would love you to weigh in here on some of the work we could continue on with, and potentially create a prize fund for this and future work?

@owocki @MathildaDV - wdyt? 

I'd also be curious what this is worth - and fund it to be compelling to future builders. Including but not limited to a referral program.

-------------------------

Sov | 2024-08-29 21:39:33 UTC | #5

Thanks for this @noahchonlee awesome to see you here and the ongoing dedication to building that you and the team at ViaPrize has!

I would be open to explore this.  I would like to make sure whatever we do that funds allocated traverse the Allo Protocol so that any value flows hit the north star we have for Allo GMV.

Down to collaborate!  LFGTM!

-------------------------

noahchonlee | 2024-08-29 22:13:04 UTC | #6

Thank you for the encouraging responses!

If I understand correctly, Allo is a collection of open source funding allocation protocols. What if crowdfunded prizes became one of the tools in Allo?

-------------------------

tomislavmamic | 2024-09-04 14:48:24 UTC | #7

How does Allo Yeeter differentiate from disperse.app?

-------------------------

Oba-One | 2024-09-09 04:03:55 UTC | #8

# RFP Title: Greenpill Dev Guild Allo Yeeter Proposal

## Overview

Allo Yeeter a quick, simple and user-friendly mechanism built on Allo Protocol for programmatically allocating capital directly to designated wallet addresses via a smart contract.

## Scope of Work

### User interface

A simple user-friendly way to interact with the Allo Yeeter

* Built with NextJS, React, Tailwind, Typescript
* Simple web app deployed on Vercel

### Yeeter Smart contract

A mechanism for inputting addresses and weights for distribution and executing the distribution of tokens.

#### distributeFunds(wallets: address[ ], weights: number[ ], *erc20* contract: address, amount: uint256)

Disburse funds to addresses according to their weight and the amount specified.

### Greenpill Dev Guild Yeeter Workshop

After completing the Allo Yeeter beta version, the Greenpill Dev Guild will invite the Greenpill community and interested developers to a workshop to learn about the building process, test the product and brainstorm use cases.

## **Selection Criteria**

The Greenpill Dev Guild will take responsibility for developing Allo Yeeter, utilizing previous work done by guild members in a similar project. Guild members have experience working with React and developing Solidity smart contracts and will approach the tasks together, meeting the milestones on time.

## Timeline

* Initial design and wireframe: 2 weeks
* Yeeter smart contract, UI and Allo Protocol integration: 2 Weeks
* Community workshop, user testing and submission/ request for comment: 2 Weeks

## Budget

10,000 GTC

* App design, UI/UX
* Frontend and smart contract engineering/Allo protocol integration
* Greenpill Dev Guild Yeeter workshop

@cauetomaz
@Evan Hudson
@Kit Blake 
@MattyCompost
@Oba-One

-------------------------

deltajuliet | 2024-09-21 10:49:02 UTC | #9

Thanks for all the thoughtful responses, convos and ideation on this. We've awarded this RFP to @Oba-One and the GP Dev Guild for $10,000 GTC from the Citizen's Grant Fund. 

We've reviewed the RFP in a kickoff call, and they will update here with refined milestones, considerations and notes shortly. 

In the meantime, @rohit reached out and has some ideas of crossover with the Atlantis team and their Impact Miner project that he'll share here for consideration for further versions of this.

-------------------------

Oba-One | 2024-10-04 02:57:11 UTC | #10

**Project Update**

We're currently two weeks into building Allo Yeeter and are on track to have work completed in the specified timeline. We had a meeting with @masterhw last Friday to discuss the custom strategy we will build with Allo. The conversation was productive and afterwards our engineering team dove into the protocol and the Allo team provided a draft Yeeter strategy to build from.

During our weekly call which is every [Wednesday at 2:30pm PST](https://meet.google.com/jkk-iybx-jft) we set our tasks for the next 2 weeks which are in parallel to complete designs, app scaffolding, and the Yeeter strategy.

After the completion of this sprint we will submit our 1st milestones.

To stay up date with progress use these links.

**Project Board**: https://github.com/orgs/greenpill-dev-guild/projects/16
**Repo**: https://github.com/greenpill-dev-guild/allo-yeeter

-------------------------

Oba-One | 2024-10-26 02:20:46 UTC | #11

**Project Update**

We have successfully created the prototype of Allo Yeeter! The last few weeks have been focused on completing designs, UI and the custom strategy. We're now at a good point to polish and optimize Allo yeeter so the UI is crisp and users can yeet with minimal actions. Feel free to watch the Loom video by Julian demoing the app or try it out yourself.

**Demo** : https://www.loom.com/share/69392a5deead441a80dd9f082a0d255f?sid=e15d6980-c36b-4579-abb3-ba5ab035d289
**Prototype** : https://allo-yeeter.vercel.app/steps/recipients
**Project Board** : https://github.com/orgs/greenpill-dev-guild/projects/16

-------------------------
