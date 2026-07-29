---
id: 19047
title: "Pre-proposal: Fund Muqa to build on Gitcoin stack"
slug: pre-proposal-fund-muqa-to-build-on-gitcoin-stack
category: citizen-grants
url: https://gov.gitcoin.co/t/pre-proposal-fund-muqa-to-build-on-gitcoin-stack/19047
created_at: 2024-06-27T14:11:50.170Z
last_posted_at: 2024-06-28T20:09:26.705Z
posts_count: 4
views: 3120
like_count: 6
---

# Pre-proposal: Fund Muqa to build on Gitcoin stack

<https://gov.gitcoin.co/t/pre-proposal-fund-muqa-to-build-on-gitcoin-stack/19047>
tomislavmamic | 2024-06-28 20:12:12 UTC | #1

# Pre-proposal: Fund Muqa to build on Gitcoin stack

Hello Gitcoin,

I am kindly asking you to review this pre-proposal, join the discussion and provide your sentiment for this temp check. Thank you to @RohitMalekar and @CoachJ for helping with this proposal.

## Background
Last summer, thanks to the Funding the Commons support and Gitcoin's funding, I started [working on a project](https://explorer-v1.gitcoin.co/#/round/42161/0x5aa255d5cae9b6ce0f2d9aee209cb02349b83731/65) which would get my home town, City of Split, to try out QF for one of their grant programs.

Since then, I have done a lot on advancing the idea. From multiple meetings with various city officials, collecting the data on city's grants programs, analysing it, presenting at [UNDP](https://innovation.eurasia.undp.org/urban-transformation/) conference for cities, researching the needed tech stacks and potential integrations, to narrowing down the how and where we would use QF.

Also, I applied for EF Next Billion with this project in mind. Not only the [project was selected](https://blog.ethereum.org/2024/06/24/next-billion-cohort4) as one of the very few, but it got additional funding for the purpose of building the app.

## What are we building?
Ethereum has a number of protocols and apps that are both mature enough and solve a need a city has. We are building an open-source app customised for cities, which will serve as an interface to the Ethereum ecosystem of apps and protocols. Premier example of these, and the first one we want to offer access to is Gitcoin.

One of the most important things cities do, is allocating money for public goods. Whether they need direct grants, QF, retro funding or something else, they could and should use Allo protocol. We intend on running our grant programs on Allo protocol.

Gitcoin has built Grants Stack for the purpose of providing an easy and powerful interface for using Allo protocol. While using Allo protocol is a non-brainer for us, for Grants Stack we have some obstacles to use it as-is. It comes with its own set of features which are not directly usable by cities in their interaction with non-web3-native citizens, while some features which are needed are missing. We want to use as much of Grants stack as possible, but we have yet to look deeper and decide how to do it.

Here are some of the things we'll probably need to do differently:

- we need to offer users an in-app non-custodial wallet with no need to manage private keys (we plan to use Cometh Connect for this)
- we need to offer simple in-app onramp solution which works well with local banks, cards, currencies and KYC requirements.
- we need to abstract away the cryptocurrency used, so that users who top up euros, see euro balance (which means we need to use euro stablecoin)
- we need to make it in local language with local legal documents
- we need to be able to support different types of grants than what is currently supported by Gitcoin. (Eg. citizens propose projects, but the city gets the money and executes)
- we need to use city-specific tools and available data for sybil resistance, and possibly for KYC
- we need to only show the rounds which a citizen can participate in
- we might need to integrate a forum for discussions on the rounds
- we might need to integrate an option for donors to vote on disbursement of funds after the execution
- we might need to allow for documents submission
- we might need to add additional types of fields in the submission forms


## Where are we now?
To advance [or help implement] this project I was recently selected as part of the Ethereum Foundation's Next Billion Fellowship Program.  With their advisory and financial support we will build a minimum viable app for the purpose of running one specific QF grant round in Split, Croatia. Unfortunately, this funding is limited and besides building the app for pilot, doesn't cover much more.

Also, there are multiple grant programs with multiple grant rounds which we could run through the app as well. We could just run the pilot, or we could build such an MVP, which would be usable by any city or other institution to run local grant programs on Ethereum and Allo. We have already started talks with UNDP about this possibility. They work directly with more than 100 cities and national governments, and thourgh their network, we could reach more users quickly.

## What do we expect from the pilot?
The pilot will run in Split in September 2024. with a goal of at least 30 proposals and 1500 citizens donating (1% of population).

These citizens will be onboarded on Ethereum and Gitcoin.

## What do we expect to achieve with additional funding?
### June 2024 - November 2024
We will create an app and run a successful pilot in the city of Split during the fellowship (). We will do the necessary legal work, local marketing campaign, establish key partnerships, provide support for grant program managers, grantees and citizens, create a report and build a website to showcase the outcome.

### December 2024 - May 2025
We will run multiple rounds of different types during the 6 months following the pilot.
Types of rounds:
1. Municipal grant program
2. Participatory budgeting
3. Journalism funding on the national level
We will onboard the first cohort of cities after the pilot. We will make necessary adjustments to the app.

## What do we ask?
### Supplement the funding for current development milestone
We ask for funding to start working right away on incorporating Allo and Grants stack and preparing to run multiple rounds after the pilot on this infrastructure.

### Extend the development runway to build more than prototype
We ask for funding to extend our development runway from 3 to 9 months, where for each quarter (or more frequent if needed) we would set objective and relevant milestones.

### Costs of operations, marketing, bizdev and legal
We ask for funding to run local campaigns for rounds, for business development activities and for other costs there might be such as legal costs.

# Conclusion
Please provide your opinions and thoughts. Do you think this project should be funded by Gitcoin. If not, why not and can we change something to make it better fitting. If yes, please express your support.

-------------------------

owocki | 2024-06-27 17:36:05 UTC | #2

seems interesting!  we ran a QF pilot in boulder CO back in 2020 [[ref](https://twitter.com/dtstimulus)]... 

and i think that QF/funding is something that can legitimately trojan horse crypto into the mainstream (and also make ppls first interaction with crypto be receiving $$$ to pay their rent, as opposed to buying a speculative asset).

1. how much $$$ are you looking for?
2. how much GMV will this generate?
3. do you have a lo fi prototype of what you are building?

i wonder if this is something that could leverage [allo starter kit](https://github.com/gitcoinco/allo-starter-kit) to reduce the build time! @carlb

-------------------------

carlb | 2024-06-28 07:48:12 UTC | #3

Really cool idea Tomo!

I love the ideas for reduction friction in the UX by using non-custodial wallets, in-app onramps and KYC.

Like @owocki mentions, Allo Starter Kit could be leveraged to help you with interacting with Allo Protocol and Indexer.

Allo Starter Kit is at its core:
- An SDK to communicate with Allo2 and Grants Stack Indexer. Each of the method is wrapped in a ReactQuery hook to simplify frontend development.
- A collection of building blocks and components for discovering rounds, projects, applications, details about them, creating rounds, registering projects etc.
- Flexible and pick & choose what you need
- Extensible (extend create round form component with functionality required by the custom Allo Strategy)

We currently have a Web3Provider using RainbowKit but it should be trivial to create a custom one for Cometh Connect. (There's also a way to pass a custom sendTransaction function to the ApiProvider)

Here's how I see it being leveraged for your build:
- A custom Allo2 Strategy that handles the custom logic of citizens and payouts to city (+ euro stablecoin)
- A Next.js app using AlloStarterKit to query Grants Stack (https://grants-stack-indexer-v2.gitcoin.co/graphiql) and interact with Allo2
- Your own custom logic for Onramp, KYC, city-specific tools, forum, documents,translations, etc
- "Querying rounds which a citizen can participate". This might not be available in the GrantsStack Indexer so you would need to query the round contracts directly (can be done from a server-side endpoint to cache responses)
- Custom components for voting after execution
- AlloStarterKit Strategy Extension for additional fields in the submission forms (Or Custom Components that call Allo2 via AlloKit)

AlloStarterKit is still in alpha so some functionality might not be implemented yet in the links below:

Links:
- Github - https://github.com/gitcoinco/allo-starter-kit
- Storybook - https://allo-starter-kit-storybook.vercel.app
- Demo App - https://allo-starter-kit-demo.vercel.app

Happy to answer any questions!

-------------------------

tomislavmamic | 2024-06-29 09:06:13 UTC | #4

It's very cool what you have done in Boulder! I hope to see more of such initiatives.

[quote="owocki, post:2, topic:19047"]
QF/funding is something that can legitimately trojan horse crypto into the mainstream (and also make ppls first interaction with crypto be receiving $$$ to pay their rent, as opposed to buying a speculative asset).
[/quote]
I couldn't agree more. A day will come when thousands of regular people will participate in funding and managing local public goods without even realising they are using blockchain. I believe this day is closer than we think. Also, I believe this use-case is the perfect candidate for non-speculative first use of Ethereum for masses.

---

[quote="owocki, post:2, topic:19047"]
how much $$$ are you looking for?
[/quote]
I wasn't sure if this proposal is even eligible or would receive positive sentiment so I didn't create any estimates yet. I'll make an estimate in the coming days/week.

I had some estimates before, but these need reviewing and updating. I'll post asap.

---

[quote="owocki, post:2, topic:19047"]
how much GMV will this generate?
[/quote]
For the pilot itself, I am expecting up to $100k. But in the long run, we are entering potentially the biggest opportunity, as noted [in this comment]( https://gov.gitcoin.co/t/how-might-we-scale-gitcoins-impact-from-50mm-gmv-to-500m-gmv/16697/6) by @ccerv1 :

[quote="ccerv1, post:6, topic:16697"]
$500M GMV is a good target but still a drop in the bucket relative to legacy PGF. It’s how much the country of Chad [currently ](https://www.theglobaleconomy.com/rankings/government_spending_dollars/) allocates to PGF.
[/quote]

What is also important to note is the [type of the opportunity]( https://gov.gitcoin.co/t/how-might-we-scale-gitcoins-impact-from-50mm-gmv-to-500m-gmv/16697). These are recurring + legitimate + deep wells of funding.

---

[quote="owocki, post:2, topic:19047"]
do you have a lo fi prototype of what you are building?
[/quote]
Not yet. But we will have in a few weeks. The work done so far was mostly research and BD. We are just starting the work on actual application.

---

We will definitely use Allo Starter Kit, but also other Gitcoin's products as much as possible.

-------------------------
