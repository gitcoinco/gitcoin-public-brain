---
id: 12546
title: "Public goods Legos: roadmap"
slug: public-goods-legos-roadmap
category: open-discussion
url: https://gov.gitcoin.co/t/public-goods-legos-roadmap/12546
created_at: 2023-01-11T17:01:38.889Z
last_posted_at: 2023-12-19T05:41:07.795Z
posts_count: 6
views: 6263
like_count: 22
---

# Public goods Legos: roadmap

<https://gov.gitcoin.co/t/public-goods-legos-roadmap/12546>
j-cook | 2023-01-11 17:06:45 UTC | #1

An [earlier post](https://gov.gitcoin.co/t/anti-sybil-legos/12265) introduced the idea of Sybil defense "Legos" as composable building blocks that users can use to implement their own anti-Sybil systems. We want grant/round owners to be able to build their own grant management systems by picking freely from a set of tools that can be easily and intuitively connected together and even tweaked and modified to best serve the needs of specific subcommunities. We also want a diverse community of developers and data scientists to analyze Gitcoin data and turn their insights into Legos. Any analysis that can be shown to identify Sybil behaviour can be expressed in code and developed into a Lego.

This post aims to add some more detail and dig a little deeper beyond the conceptual overview in the first post and start to show some of the practicalities of building and implementing anti-Sybil Legos and show where hope to go from here. We also introduce the upcoming Open Data Science Hackathon that will onboard new Lego builders to the Gitcoin/Open Data community.


![](upload://1NE3LSt8rzYaT4uPNsX6zKP0PWG.png)


## What Legos are already available?

Several Lego's are already built and being used to manage Sybils in Gitcoin grants. These are:

- **Gitcoin Passport:** When a user connects a passport, a trust score can be calculated for them which is used as evidence of personhood - the greater the score the more likely they are to be a genuine user.
- **Levenstein distance:** Every user has a username - when they sign up to Gitcoin grants the similarity of their name can be compared against all other usernames to generate a likelihood of the username being auto-generated - evidence of a Sybil account. This Lego **will be deprecated** in the grants protocol because usernames will no longer be available - only Ethereum addresses, wallet IDs and grant/round nonce. 
- **Shared IP**: User IP addresses can also be checked to see if they are shared with many other users. Lots of addresses originating from the same IP could be a marker for Sybil attackers.
- **SAD model:** The user also has a Gitcoin account whose history can be analyzed using the SAD model to give another Sybil-likelihood score.
- **DonorDNA**: When a donor connects their wallet their profile of past donations can be analyzed to see whether it is similar to groups of other users, which may be indicatative of Sybil rings.
- **GrantDNA**: Each grant has a set of donors that can be represented as a set of binary data. This can be used to compare grants against flagged grants to see if they have similar donor profiles.
- **Onchain Intersectionality**: How many out of a set of on-chain credentials does a user have?

The outputs from the Legos are either Booleans (Sybil/non-Sybil) or floats (0-1) representing Sybil likelihood.  They are aggregated and used collectively to come to a decision about the trustability of the user. In summary, the Legos are run independently and the results passed to an aggregator. The user sees the result of each independent Lego and also the result of the aggregator - i.e. they get an overall Sybil likelihood score/trust score and also a break down of the individual Sybil "dimensions".


## What other Legos could exist?

During Season 14, Gitcoin Passport was integrated into Bankless Academy. Analysis revealed that Gitcoin Passport was most powerful when combined with additional anti-Sybil Legos. 

- **Farmer Boolean**: (uses on-chain data to determine whether a user has >X ERC-20 tokens and an average transaction value <Y ETH)
- **Onchain History Boolean**: (has a user engaged in certain web3 activities in a specific timeframe? Activites and timeframe can be customized by round owner)
- **Money-Mixer**: (Does a user interact with mixers e.g. Tornado cash)
- **On-Trend / Off-Trend**: (is the donation profile of a user similar to a grant's target community?)
- **Flagged Activity on Etherscan**: (is an address closely associated with addresses flagged as phishing/spam on etherscan?)


There are many possibilities for more Legos - *any analysis that can be shown to be indicative of Sybil behaviour and implementable as an algorithm could be turned into a Lego*. Some might be relatively complex analyses of on-chain data, like detecting when a user has rapidly swapped funds back and forth in order to seem more active. Sequences of rapid transactions between wallets, especially when they are ultimately returned to where they started or at least stay within a small group of addresses, could be a Sybil behaviour. Other on-chain indicators might be whether a wallet was initially funded from a contract, as this might be a way for Sybil attackers to automate their donations from many externally-owned accounts.

Other simple Legos could be checks for users that hold certain POAPs or NFTs. Some POAPs and NFTs are easy to farm, others require significant investment of time and/or capital. For example, some education programs award their graduates NFTs as proof of completion - those are difficult to farm without taking a course, and they are in very limited supply so the total bribable population is small - ownership of these credentials is good evidence a user is not a Sybil attacker. 
Some specific NFTs and POAPs might be especially high-signal for certain communities - e.g. POAPs distributed in community calls or at in-person meetups. There is also high potential for creating Legos based on past behaviours and interactions with other grant rounds - e.g. has a particular address donated to grants that have been flagged as fraudulent in the past - if so, how often? If some threshold of a user's donations, say 50%, have gone to flagged grants, the user gets flagged too.

Not all Legos have to use on-chain data. There may be more Sybil signals that can be extracted using clever analysis of Gitcoin data - DonorDNA and GrantDNA are good examples of existing Legos that only use off-chain data.

## What do these Legos actually look like?

Right now, these Legos exist as code that is run manually by data scientists. The code is run against individual Ethereum addresses and Gitcoin usernames to determine their Sybil-likelihoood. They are currently run as independent, standalone algorithms, although development is tending towards increased automation and interoperability so that users are better able to implement these algorithms for themselves. 

Right now, Sybil Legos are implemented by Gitcoin data scientists, but in a protocol-based system they will be implemented as a service that can be configured for individual users. Ultimately there should be a freemium type model where foundational Sybil defenses are made available for free, and more computationally heavy algorithms can be optionally added for a fee.

## A Lego development roadmap

### Who can use the Legos?

In the centralized era, Lego users are primarily Gitcoin data scientists (or "Fraud analyts"). These Fraud analysts have access to source code for the various Legos and apply it to Gitcoin data as part of a service provided to round owners. As the platform becomes a protocol, the Legos become increasingly decentralized - first by making the Legos usable directly by round owners, and then by making them available to anyone via a simple dashboard-based UI.

### How to decentralize Legos

Up until now, the focus for Lego developers has been on experimenting with different prototypes and identifying those that are worth developing into products. Now, those existing Legos can be further developed to enhance their useability.


#### More accessible code

Legos are currently discrete code packages that implement some algorithm on Gitcoin data. However, scripts for running algorithms are not particularly useful in their "raw" form - they require additional functions that load and validate Gitcoin data and return a useful, correctly formatted result. The algorithm itself needs to be wrapped in helper functions that turn the code into a self-contained unit that takes in Gitcoin data and returns a Boolean (Sybil/not Sybil) or a float (Sybil likelihood).

More useful would be bundling the code, along with other Legos, into a single package that could be easily imported into user's projects. A good example would be a Python package that could be installed using a package manager, such as

`pip install sybil-legos`

and then individual Legos could be invoked simply using something like:

```
import sybil-legos as sybil

result = sybil.donor_dna(data)
```

This would also naturally extend to other Legos, all available inside the `sybil-legos` package. A minimal example of a pipeline for anti-Sybils could be as follows:

```
import sybil-legos as sybil

dna = sybil.donor_dna(data)
grant_dna = sybil.grant_dna(data)
trust_score = sybil.trust_score(data)

result = sybil.aggregator(dna, grant_dna, trust_scores)
```

In this example, each Lego is invoked as a separate function within the `sybil-legos` package and the results are all fed into an `aggregator` function which applies some decision-making function to the results of each individual Lego and returns a list of Sybils. Likely, the `trust_score` function would make an external call to the Gitcoin Passport API where trust score calculations are already handled in a developer-friendly way that abstracts all the communication with Ceramic, data verification, cleaning and validation away from the end user. 

To best serve the developer community and lower the barrier to entry as far as possible, creating containerized versions of Legos that can be executed in a single line of code, great documentation, explainer articles and investing in devrel activity will go a long way. In this state, Legos are easier for a wider community of developers to implement. This removes a lot of friction in implementing Legos for Gitcoin Fraud Consultants and round owners.

#### No-code Legos

Longer term, it will be much more useful to abstract Lego execution out another level and provide no-code options for implementing the same tools. The transition from code to no-code Lego building is potentially a major unlock in terms of the number and diversity of people that can configure their own Sybil defenses. 

The obvious route to no-code Legos would be a public frontend where users can upload their data (e.g. list of usernames and/or Ethereum addresses) and download their results in a web page. A webpage could enable a user to simply opt-in to the Legos they wish to apply just by clicking tickboxes. The app then uploads the user's data to a virtual machine, execute the selected algorithms, aggregate the results and return Sybil scores back to the browser. It is also easy to imagine additional features being made available via a marketplace of optional anti-Sybil add-ons.

Some advancement in this direction has already been made: the screenshot below shows a web-app interface where users can input the account names of their users and see their Sybil likelihoods as determined by each of six metrics immediately in the browser - effectively a dashboard that shows a round owner whether their round is being attacked.

![](upload://6XTxHHSOiOvGetLD9uHbPCh2pVN.png)

There are costs associated with computing Lego scores. This means that eventually, a cost would need to be attached to the Lego execution such that users pay a small fee to add a Lego to their anti-Sybil pipeline and the actual execution is done in a virtual machine whose management is abstracted away from the user. Web3 integration seems to be a good solution for this -  a cost in ETH or a stablecoin could be calculated depending on the Legos the user has selected to implement which can be paid via a wallet integration before executing the Sybil Lego code. A freemium model may work well, with foundational Sybil algorithms being provided for free, and more computationally heavy ones being optionally added for a fee.

Overall, most of the available Legos are currently only really useable by Gitcoin developers, but the roadmap is to gradually reduce the barrier to entry by first producing extensive documentation and beginner-friendly guides, then sequentially more and more accessible UIs that abstract complexity away from the user.


## How can I help build Legos?

The best way to get involved with Lego development is to participate in the Gitcoin and/or Open Data Science communities. Data scientists are required to analyze Gitcoin data and identify signals that can be used to find Sybils. Developers are required to turn those signals into Legos. There is also a great need for people to work on UX and documentation. A great way to start participating is to join a community hackathon.



![](upload://ljolJzkovib4UiaJjGw7gnbU0dU.jpeg)




### Hackathon 

The Open Data Community is a fast-growing open community founded by Gitcoin. Our mission is to protect web3 by fighting Sybil attackers and resisting recentralization at the data layer. In January 2023 the Open Data Community and Gitcoin will host a hackathon specifically for anti-Sybil Lego builders. Hackers will have access to open data technology such as the decentralized node provider, Pocket, and decentralized data from Ocean Protocol. These tools will be used to hackers to build useful Sybil defense algorithms for Gitcoin's grants protocol. To help builders get off the ground there will be a set of algorithms-of-interest that we would like to see developed into Legos. There may also be more points available for builders that go outside of the suggested data/algorithms and create new ideas from novel data sources.

This hackathon builds upon the success of the inaugural hackathon in autumn 2022. That previous hackathon yielded several novel algorithms that are now being developed into algorithms for the upcoming Gitcoin grants protocol - we want to build on this success and add more algorithms to the anti-Sybil toolbox.

The hackathon will open for applications in January 2023. Until then, visit the [hackathon webpage](https://gitcoin.co/hackathon/DataBuilders/onboard), join the fast-growing Open Data Community on [Discord](https://discord.gg/KJ6PGH4cnK) or follow them on [Twitter](@OpenDataforWeb3).

-------------------------

DisruptionJoe | 2023-01-12 13:53:47 UTC | #2

Great overview. This article I put up to sensemake around the users of legos is a good companion piece as well. https://gov.gitcoin.co/t/using-fdd-fraud-defense-tools-in-a-protocol-future/12526/1

-------------------------

kyle | 2023-01-12 14:23:15 UTC | #3

[quote="j-cook, post:1, topic:12546"]
ownership of these credentials is good evidence a user is not a Sybil attacker.
[/quote]

This assumes we know intent, and the user has sufficient education on the behavior we expect. One minor nuance we have not articulated is that a score is only valuable in predicting behavior if we (system operators) and the users share a common understanding of expectations. This is one place I am feeling like we need to bolster our efforts. 

One of the most common feedbacks we received was "I didn't know ABC behavior wasn't allowed" (ie airdrop farming with lots of wallets). 

[quote="j-cook, post:1, topic:12546"]
The algorithm itself needs to be wrapped in helper functions that turn the code into a self-contained unit that takes in Gitcoin data and returns a Boolean (Sybil/not Sybil) or a float (Sybil likelihood).
[/quote]

I wonder if we have considered other scoring mechanisms like a cost of forgery? Instead of trying to predict whether someone is a good actor, could we introduce a cost of forgery (in $USD) that is then tied to other USD denominated outcomes? For example, if my passport has a cost of forgery of $150 (I have a bankless POAP which was only possible by paying $100, and also I have $50 worth of GTC staked on my passport) then I might only be eligible to direct 2x my passport "value" (value is the interpretation of the cost to forge).

Going a step further, Cost of forgery offers other communities more granular (and arguably intuitive) opportunities to gate airdrops, entrance into the community etc. *I only want to airdrop the amount of tokens up to someone's passport value* or *I only want users (during a QF round) to have 2x their passport value*

One final thought on this, if passport value is better defined and explored, it may open new opportunities on "slashing" conditions where some of that value may be recouped if the user is a bad actor. For example, if we use the same analogy of the $150 passport value, the $50 worth of GTC may be liquid and slashing eligible if it is found I am acting in bad faith (see above though that the context needs to be clear and agreed to). If $50 may be slashed, we now have an economy in which Sybil Hunters are literally getting paid to find bad actors. And as a user, I may receive a 5x bonus to the matching pool funds my donations have (increase risk of slashing, but also increase reward of directing more matching pool funds).

[quote="j-cook, post:1, topic:12546"]
Sybil likelihoods as determined by each of six metrics immediately in the browser
[/quote]

Do you have a link to this?

--
Overall, I really appreciate you outlining the thinking. I see "is this person Sybil" the imprecise question to ask. One question I am interested in exploring more with Passport is "How we can make the system more expensive to attack than to defend and offer immense upside to good actors while deterring bad actors"

-------------------------

DisruptionJoe | 2023-01-12 18:40:52 UTC | #4

[quote="kyle, post:3, topic:12546"]
One of the most common feedbacks we received was “I didn’t know ABC behavior wasn’t allowed” (ie airdrop farming with lots of wallets).
[/quote]

This is a great callout! I think there is value in better user education during their journey and maybe FDD should better communicate these types of simple solutions to GPC! 

There is also communication value in the "This house is protected by Allstate" type deterrence.

[quote="kyle, post:3, topic:12546"]
I wonder if we have considered other scoring mechanisms like a cost of forgery? Instead of trying to predict whether someone is a good actor, could we introduce a cost of forgery (in $USD) that is then tied to other USD denominated outcomes? For example, if my passport has a cost of forgery of $150 (I have a bankless POAP which was only possible by paying $100, and also I have $50 worth of GTC staked on my passport) then I might only be eligible to direct 2x my passport “value” (value is the interpretation of the cost to forge).
[/quote]

Yes. We have a cost of forgery model which was developed this season. It performed almost as well as the regression models when compared to the Thor/Loki datasets. 

We discussed a Upala trial and deprioritized it because it doesn't include systemic value. In other words, it measures how much the stamps and a passport are worth to someone with nothing to gain other than what we would be willing to pay them. This could serve as a great validation to our current cost of forgery model, but would not be useful in stopping the "attacker" sybil persona (as opposed to the "farmer"). 

[quote="kyle, post:3, topic:12546"]
Going a step further, Cost of forgery offers other communities more granular (and arguably intuitive) opportunities to gate airdrops, entrance into the community etc.
[/quote]

I believe this model is in code on the Passport repo. We offered it as another option because of this UX advantage even though it was 2-3% less accurate than the regression models.

[quote="kyle, post:3, topic:12546"]
For example, if we use the same analogy of the $150 passport value, the $50 worth of GTC may be liquid and slashing eligible if it is found I am acting in bad faith (see above though that the context needs to be clear and agreed to). If $50 may be slashed, we now have an economy in which Sybil Hunters are literally getting paid to find bad actors.
[/quote]

This is holy grail level. We need to know two things for this.

1. Are we sure of the slashing condition?
2. What is the proper continuous (closed loop) funding mechanism? (like insurance pools)

We are more focused on the slashing conditions at this point. Are we sure that the account is sybil. I'd love to pair with you on thinking through the product management methods you would use to iterate towards the second mechanism. 

I've always thought of this ability to reward and slash as a module where round owners could create their own settings. (We would likely consult them on best practices to begin.)

[quote="kyle, post:3, topic:12546"]
Overall, I really appreciate you outlining the thinking. I see “is this person Sybil” the imprecise question to ask. One question I am interested in exploring more with Passport is “How we can make the system more expensive to attack than to defend and offer immense upside to good actors while deterring bad actors”
[/quote]

I think this is spot on.

-------------------------

owocki | 2023-01-12 18:48:56 UTC | #5

[quote="j-cook, post:1, topic:12546"]
`result = sybil.aggregator(dna, grant_dna, trust_scores)`
[/quote]

Hey @j-cook I just wanted to make sure you saw [this comment](https://gov.gitcoin.co/t/passport-scoring-as-a-service/12419/7) on another sybil lego post about some of the ways these sybil legos compose (or dont compose).

-------------------------

tkgshn | 2023-12-19 05:41:07 UTC | #6

I've just published absolutely NoCode Lego as DeCartography! 
how can I call you? @j-cook
https://gov.gitcoin.co/t/decartography-beta-is-out-how-to-generate-clustered-data-from-grs-participation-data-and-how-to-improve-current-gitcoin-grants/17290

-------------------------
