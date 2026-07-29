---
id: 17635
title: "The Impact Web of Trust Could Change Everything 💰"
slug: the-impact-web-of-trust-could-change-everything
category: open-discussion
url: https://gov.gitcoin.co/t/the-impact-web-of-trust-could-change-everything/17635
created_at: 2024-02-07T22:00:42.806Z
last_posted_at: 2024-09-19T17:22:34.894Z
posts_count: 5
views: 6052
like_count: 19
---

# The Impact Web of Trust Could Change Everything 💰

<https://gov.gitcoin.co/t/the-impact-web-of-trust-could-change-everything/17635>
owocki | 2024-02-08 18:40:48 UTC | #1

Thanks to @ccerv1 and @Jonassft for reviewing (and in some places, co-authoring) this post.

# TLDR

This brief argues that The Impact Web of Trust Will Change Everything about web3-era capital allocation.

A Web of Trust is a decentralized trust model used for verifying the authenticity of participants in a network through mutual endorsements, rather than relying on a central authority. It enables users to establish trust based on the recommendations or validations from others within the network.

We are witnessing the  creation of an Impact Attestation Web of Trust that will create powerful new ways of allocating capital to Fund What Matters - at new degrees of precision and scale.

This will lead to a totally revolutionary category of impact funding applications that could eventually secure $$billions of value.

# The Impact Web of Trust Will Change Everything

## What's a Web of Trust?

A Web of Trust is a decentralized trust model used primarily in cryptography and online communities, where trust in the authenticity of digital entities (like public keys) is established through a network of mutual assurances. Rather than relying on a central authority to validate identities, users vouch for each other's trustworthiness through digital signatures, creating a networked chain of trust. This method allows individuals to assess the credibility of digital certificates or identities based on the trustworthiness of those who endorse them, new categories of peer 2 peer commerce.

![|624x325](upload://vpnITdYrSzSdQsMH1yDKdjG21BR.png)

## What are the most famous webs of trust?

### 1. Academic Papers

The academic paper citation regime functions similarly to a Web of Trust, albeit in an intellectual and scholarly context. It relies on the collective credibility of authors, journals, and institutions, where the citation of sources acts as endorsements of reliability and relevance in the academic discourse. This network of scholarly references and peer reviews creates a trusted framework for advancing knowledge, where the validity of research is continuously vetted and reinforced by the academic community.

Relevance: (Secures $$$millions of research papers + directs flows of scientific funding)

### 2. Pagerank

PageRank, originally developed by Google's founders, can be viewed as a form of a Web of Trust for the internet, where web pages are ranked based on their link structure and the quality of these links. Each link to a page is considered a vote of trust and authority, with links from highly trusted sites carrying more weight. This algorithm creates a hierarchical system of trustworthiness and relevance, enabling users to discover the most authoritative and reliable pages on the web based on the collective endorsement of the online community.

Relevance: (Secures $$$millions of web SEO Traffic)

![|273x218](upload://eiMMZJZaaP9QXQ9iAhFXwh8shw8.png)

### 3. Knights Templar

The Knights Templar were an OG web of trust, founded in the 12th century during the Crusades. They were entrusted with the protection of pilgrims traveling to the Holy Land. To facilitate this mission, they developed a system akin to modern banking, where pilgrims could deposit their assets in one Templar location and receive a document to redeem their wealth at another, making long journeys safer.

Relevance: (Precursor to modern banking, so people could travel without carrying their assets)

## What is the Impact Web of Trust?

AKA the impact = profit capital allocation web of trust.

The Impact web of trust is a series of attestations where impact is being made. These attestations could be stored on  either Hypercerts or [EAS](https://www.youtube.com/watch?v=6yCbiSDaqUk) attestations, and would be linked in a network to other attestations.

Here is a visual of what it looks like:

![|519x546](upload://pfHOHRjVeCmBNW9L4J4tivyfU2H.png)

## Triple Sided Market

Right now we (royal we: Gitcoin, Optimism, Giveth, ClrFund, Hypercerts, etc) are building the triple sided market of impact attestations, and growing the network value of all impact attestations on EVM based blockchains.

The tree sides of this market are

1. Demand
2. Supply
3. Evaluation

This 3 sided market looks like this:

![|296x122](upload://nVOBmX6gA6Pe31n27zTWZx6ZUa0.png)

This flywheel is already humming!

1. **Impact** **Demand** is being bootstrapped by funders on Gitcoin, Optimism, Giveth, ClrFund, Hypercerts, etc.
2. **Impact** **Supply** is bootstrapped by grant owners on the same platforms.
3. **Impact** **Evaluation** is being bootstrapped in many different forms: QF Voters, Optimism Badgeholders, Hats Roles, or many other onchain signals

Like many systems that are subject to network effects, this network could be subject to [metcalfes law](https://en.wikipedia.org/wiki/Metcalfe%27s_law) + create exponential value.  

![Screenshot 2024-02-07 at 3.32.59 PM|690x348](upload://z0CGRRxNDuPs5kV7B2SgsypmFoo.png)

At scale, this network will completely change the capital allocation game on-chain. With a dense source of high-signal data about impact attestations (and which ones are reliable), we will be able to build much more powerful capital allocation mechanisms.

# How can Gitcoin build for this future?

1. Make sure the WoT is compatible with the Allo registry (even more so, an interface across diff projects that can be the source of truth)
2. Build Impact Evaluation tools compatible with Allo.
3. Bootstrap frontier experiments in Impact Evaluation, Demand, and Supply.
4. Democratize successful experiments in Impact Evaluation, Demand, and Supply.

# Appendix A - Risks

What are the risks to this vision?

1. **Goodharts law** - as soon as a measure becomes a target, it ceases to be a good measure. Does this mean that the system evolves infinitely as we increment t+=1 over time?
2. **Not enough capital in to bootstrap demand side. Or Not enough supply side.**
   - I dont believe either of these things after seeing Gitcoin/Optimism/Giveth/ClrFund/etc work really well. I think its possible the ability to bootstrap will vary by Impact vertical tho. Starting with Open Source Software funding, there is enough money/data to get started.
3. **Not enough relevant attestations for your use case** (the oracle problem will likely be a problem for non digital impact!). Need to find clever ways of bootstrapping. Starting with digital impact like OSS is a good place to start.
4. **Oracle problem**, especially for offchain Impact Attestations likely to be a source of pain.
5. **Spamming**. Need to differentiate between people who give attestations liberally and those who are more reserved in their evaluations.
6. **Anonymity and pseudonymity.** Bad reviews are important but people need to feel safe so they can offer them without fear of being canceled or retaliation.

# Appendix B - Opportunities

What are the opportunities for executing on this vision? (Thanks to Jonas for mostly authoring this)

1. A shift from via distinct voting rounds to constant preference expression/signals is needed:
   - **The old paradigm:** Thus far PG funding has been structured in distinct rounds, where users are asked to express what projects they thought were impactful to them or think should receive more funding. E.g. Quadratic Funding is the prime example. This system can only scale to a certain accuracy. It has large overhead in hundreds of human hours spend casting votes.
   -  **The new paradigm:** Web3 Citizens generate a constant stream of signals of what was impactful to them. Instead of requiring citizens to review a large list of projects and tell the system what they think deserves funding or was impactful, citizens generate signals in their everyday lives: When they find an article helpful, when they use a product, when they like a tweet, etc.
   -  **This is generally, not a new idea:** Twitter doesn’t ask you at the end of the quarter what tweets you thought were useful, instead it allows you to constantly signal what tweets were useful while engaging on the platform.
2. **Bootstrap with existing data.** We should focus on leveraging existing signals, and only generate new ones if absolutely necessary. Examples:
   * Having a library in the dependency tree of your repo
   * Collecting a Mirror NFT
   * Collecting a POAP for visiting an event
   * Using a protocol onchain
   * Etc.
   * Our goal should be to integrate these into everyday activities, not to make them a separate activity.
3. **Reputation:** We need to understand the profile of citizens who generated a signal. Are they trustworthy? Are they human? Do they have other properties which are important to the funder (e.g. a core user of Optimism, a builder on Optimism)?
4. **Impact Evaluation**: Now that we have collected a number of valuable signals on impact, we need to design the algorithm which makes sense of these. (e.g. PageRank and others)
   * There is an opportunity to create a plurality of ranking algorithms, eg KevinRank might be emphasize certain values, whereas JonasRank might emphasize different ones and so on.
   * Here Citizens’ should be asked to express their values for how capital should be allocated in the ecosystem: Do we only reward OS projects? Should we allocate more funding to education than ethereum development? Etc
   * One of the challenges here is that each diff niche is diff. The attestation schemas for OS will be diff from education will be diff from ppl building wallets vs those consuming block space.
   * Perhaps a next step could be defining the diff niches + which attestations we care about. and lets start with doing it in 2-3 places + only expand once its working there.

# Appendix C - Types of evaluators

(Thanks to Carl for mostly authoring this)

One thing about attestations is that they are revocable. This means you can revoke an attestation made about a project if you think it’s no longer having the impact it’s supposed to or new evidence comes to light. It also means a network of impact evaluators could attest that each member meets a certain standard (eg, is free from conflicts of interest) but their membership in the network could be revoked if they fail to uphold that standard.

Over time you will want to see a plurality of trusted evaluators. This is already starting to happen with Optimism RetroPGF and through attestation-based tools like Karma GAP.

Here are some of the types of evaluators we think are necessary:

* **Citizen evaluators.** Anyone should be able to evaluate projects and public goods that impact them or that they care about. In RetroPGF, Zuzalu was a project that had an important impact on a relatively small number of people but still received a large token award. When questions were raised about why Zuzalu received such a large reward, the people who benefited from it stood up Zuzalu and explained why they thought it was impactful. Ideally, those types of attestations should have been visible before the project was scrutinized, not in response to scrutiny.
* **Professional evaluators.** Similar to traditional ratings agencies, there should be organizations that are credibly neutral and bring a technical approach to evaluating groups of projects. Open Source Observer is working in this area. Jesse.xyz also created an open framework for identifying and scoring projects building on Base. Unlike traditional ratings agencies, these evaluations should be open source and hella forkable.
* **Experts**. People with deep experience and subject matter expertise should offer expert reviews of projects’ impact. In RetroPGF, Lefteris and TJ Rush are examples of people who offered perspectives on specific groups of projects that held a lot of weight because of their domain experience.
* **Self evaluation.** Self-reporting is also a critical part of the evaluation. In RetroPGF, every project had the opportunity to submit a list of relevant impact metrics in their application. These were hard to discover / compare, but it’s a form of attestation. Karma GAP is also getting people to self-report milestone completion.
* **Funder evaluation**. Not relevant in the RPGF3 case, but there are plenty of examples of funders evaluating their projects.
* etc

Once we have the evaluation layer, we can also build the algorithmic and curation layers. Instead of having the Yelp algorithm for ranking restaurants we can have a plurality of approaches. Imagine being able to see a ranking that takes into consideration Kevin’s knowledge of a city, Meg’s taste in Japanese food, and Carl’s sense of what makes a place good for a friday night with friends.

-------------------------

flowscience | 2024-02-09 19:45:04 UTC | #3

I'd love for someone to simulate game theory strategies like those used for the Prisoner's Dilemma (e..g tit-for-tat etc) to model how attestations, impact evaluation, and capital allocation could work at scale. Those who generate impact are often the same ones evaluating it and creating demand for it. The interactions become much more complex than a binary cooperate/defect, but I'm optimistic similar strategies that are "nice" will prevail.

-------------------------

mars | 2024-02-10 01:54:16 UTC | #4

* Web of Trust = massive problem.
* Reputation on the internet = massive problem.
* Identity on the blockchain = massive problem.
* Impact evaluation = massive problem.
* Climate change = massive problem.

[quote="owocki, post:1, topic:17635"]
Once we have the evaluation layer...
[/quote]

Something I've been working on for a while: BaseX.com literally an evaluation layer.

The core purpose of the BaseX is evaluation of impact / externalities / cobenefits. Tagline from the homepage: **"universal evaluation engine"**

What is the implemented solution? 
1. Create a report *(permissionless, anyone can do it)*
2. Create an evaluation of a report *(permissionless, anyone can do it)*

Both reports and evaluations are fact-checked by Kleros jurors and will be rejected when fraudulent. Current still on the testnet, not real money, not real incentives, but the Kleros integration works and you can test-drive the platform: https://staging.basex.com

Reputation (Web of Trust) of evaluators: **TODO**. I haven't started working on it because I know it is a massive problem, on top of that we do not have enough data.

*(segway into getting moar data)*

### Partnerships / BizDev / onboarding

I've just posted this video to Climate Coordination Network, an independent Gitcoin round:

https://youtu.be/hI5wiKDnYn8?si=lFvaucaht7Yvm1-D

Printing your own money, why not, it's my gift (carrot) towards the projects who will use BaseX. Stick would be even better - round operators requiring returning projects to submit impact report using BaseX? *(or any other evaluation platform that is scalable and ready to go)*

### Going deep / questions / next steps 

This reply is high level. Happy to tell you more and go deeper. In this forum thread. Via DM. On a call. On Twitter spaces. On a podcast.

Or just DYOR, click around, [test-drive the platform](https://staging.basex.com/) or check the [website](https://basex.com/), [whitepaper](https://wiki.basex.com/signed/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fbf508c3d-6404-4754-9ab1-1b6e97b081a1%2Ff28e75e6-d54e-49e6-bd3c-da0d1e423c6f%2Fwhitepaper.pdf?table=block&id=03c2d54c-f909-4438-872f-ed36b28ee06c&spaceId=bf508c3d-6404-4754-9ab1-1b6e97b081a1&name=whitepaper.pdf&cache=v2), [pitchdeck](https://file.notion.so/f/f/bf508c3d-6404-4754-9ab1-1b6e97b081a1/1bf03f85-ca81-4a48-833a-6d714620653c/BaseX_-_pitchdeck.pdf?id=629c4463-477c-458b-ab94-38a28529761a&table=block&spaceId=bf508c3d-6404-4754-9ab1-1b6e97b081a1&expirationTimestamp=1707616800000&signature=BwpOGB6GoYUb9rgZ795ECZ2WUDoKjRtsQMvV-opACAk&downloadName=BaseX+-+pitchdeck.pdf), [wiki](https://wiki.basex.com/)...

![image|690x382](upload://aKBdpAQ6vTK5LBOwMYzBSTZrcDi.jpeg)

Only slightly embarassed,  I hope your experience will be smooth.

-------------------------

owocki | 2024-09-13 13:19:07 UTC | #5

Enjoyooors of this post might also like this new piece from ENS [Transitive Trust for P2P Reputation Systesm](https://mirror.xyz/0xeee68aECeB4A9e9f328a46c39F50d83fA0239cDF/GLCRxzd7Y68_lWNnLxk4FG20sOWDwcQE_stQt6V7y1Y)

-------------------------

mars | 2024-09-19 17:22:34 UTC | #6

Enjoyooors of this post might also like this project from ETH Denver, that was literally inspired by this forum thread, 7 minutes demo:

https://www.youtube.com/watch?v=Nc1whvHuR9I

Hackathon submission: https://devfolio.co/projects/trust-impact-4bf0

-------------------------
