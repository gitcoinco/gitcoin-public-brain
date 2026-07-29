---
id: 12265
title: "Anti-Sybil Legos"
slug: anti-sybil-legos
category: open-discussion
url: https://gov.gitcoin.co/t/anti-sybil-legos/12265
created_at: 2022-12-08T14:42:15.159Z
last_posted_at: 2022-12-12T23:23:43.000Z
posts_count: 5
views: 5378
like_count: 18
---

# Anti-Sybil Legos

<https://gov.gitcoin.co/t/anti-sybil-legos/12265>
j-cook | 2022-12-08 14:49:18 UTC | #1

*This post is intended to give a high level outline of the way we are thinking about composable  anti-Sybil Lego's as we move to the protocol-based grants system*

Gitcoin depends on Gitcoin grants which depends on quadratic funding which has to be defended against Sybils. The core of this is solving for one-human one-vote. Right now, Gitcoin does this by identifying Sybil behaviours in users and then "squelching" those users from the system - this is done using a sequence of data science tools and human reviews that are managed by a relatively small pool of trusted operators. However, Gitcoin is decentralizing by converting the core functions into a set of tools that together comprise a protocol that can be applied by individual round and grant owners rather than by a centralized team. The tools can also be forked and recombined in creative ways in other projects, making them useful across the whole of Web3, not just within Gitcoin.

This transition requires the Sybil defense and grant reviewing procedures currently managed by humans to be broken down into discrete units, defined in code, documented and made accessible as composable building blocks. These are known as "Legos". Lego bricks are simple building blocks that can be connected to each other in creative combinations to form all kinds of structures or even machines that are much more complex than their component parts. Similarly, modular, composable software tools can be used to build imaginative systems for defending against Sybils. 

This post examines what a "Lego" is and what we should be aware of when we build them.

## What does a Lego look like?

A "Lego"is a discrete unit that performs one, specific function in the Gitcoin protocol. It should work as a building block, meaning that it should be deployable on its own, taking well defined inputs and returning some known outputs. It should also connect to other Legos, which requires some standardization of types and formats for inputs and outputs so that tools can be chained together in intuitive pipelines. Making these Lego's available empowers the community to build on top of them and saves developers from having to repeatedly reinvent the wheel when building out new products.

To be truly composable,a Lego should be:

- **Tightly scoped**: the tool should fulfill one single function without side-effects so that it can be deployed in a variety of contexts with reliable outcomes.
- **Free and open**: open source codes that is publicly available, auditable, able to run on normal consumer hardware.
- **Permissionless**: not requiring special credentials or licenses to view, download or deploy, and users have the ability to fork the code any time.
- **Accessible**: sufficiently well-documented and with intuitive UX to enable a wide community of users
- **Minimal dependencies**: protect the "supply chain" by minimizing the dependencies. Where dependencies are unavoidable, bundle them or make them very easy to access.
- **Modular**: uses common formats and types so that outputs of one Lego can become inputs to another in pipelines - i.e. the legos are designed to be used as building blocks for larger systems with no specific predetermined structure.
- **Open governance**: Decisions about the development of the Lego's should not be gated by individuals or centralized groups - instead governance should be open so that users can trust that the code will be developed and maintained with integrity and community participation. 

Some examples of Lego's that conform to these norms are smart contracts on Ethereum. Smart contracts, or even individual functions of smart contracts, can be forked and rewritten, or stacked on top of each other in creative ways to build new protocols. This is common practise in DeFi, where primitives such as asset borrowing, lending and staking contracts are combined in many different ways by teams aiming to create protocols optimized for yield, or resilience, or security. Token standards such as ERC-20 (Ethereum token standard) and ERC-721 (Ethereum NFT standard) are composable primitives that can be built on top of - there is a huge diversity of token and NFT projects built on top of these original standards, often in combination with DeFi Legos, creating a diverse landscape of decentralized financial products and a community with freedom and agency to create new versions and implement new ideas.

We want to bring that freedom and agency to public goods funding. Rather than being centralized overseers of public goods funding, we want to share tools that empower the community to do it in clever and creative new ways.

## Gitcoin Legos

To enable this decentralized future, we need Lego's that can be used to protect public goods funding from Sybil attacks. There is a diverse plurality of attackers, so we need a diverse and reactive plurality of defenses and this can only come from bottom-up protocols built by communities, for communities, using composable primitives. If the default settings for Sybil scoring doesn't work for a sub-community? No problem, open, composable tools allow subcommunities to optimize their own configurations and to chop up and recombine the tools in the right way for their specific use-case. Attackers do this to exploit vulnerabilities - the only way to tip the scales in favour of defenders is to enable defenders to do the same. For example, a grant seeking to build specific web3 infrastructure could benefit from filtering proposals based on recurring keywords or phrases. However, this behaviour could feasibly be learned by a text-generating Sybil algorithm that could capitalize on the same recurrence patterns. Alternatively, a Lego based system could enable round owners to comply with different standards in different scenarios, for example KYC/KYB Legos could be incorporated into a grant when required, and ommitted otherwise. 

![](upload://1NE3LSt8rzYaT4uPNsX6zKP0PWG.png)


### Gitcoin Passport

One major Lego that is already available is Gitcoin Passport. Gitcoin Passport is a tool that allows users to prove they have some credentials that make them more trustable. These credentials can come from Web2 or Web3. Example from Web2 include having a Facebook, Twitter, Github or Google accounts that meet some basic criteria (number of followers/posts etc). From Web3, BrightID, ENS and Proof-of-Humanity profiles can be used as stamps. The stamps are generated by the user exposing their Web2/Web3 accounts once, and then a stamp is minted in the user's Passport, with no personal identifying data saved along the way. The passport only includes the stamps - the proof that evidence exists - and no actual identifying data (working like a zero-knowledge proof). 

One of the powerful features of Gitcoin passport is that the precise combinations of stamps in a wallet can be used to generate a "trust score". This can then be used to scale the influence a user has on a vote - more trusted leads to greater influence, less trusted leads to smaller influence. This trust-score could also be used as a threshold - if a user does not have trust score at least `X`, they cannot participate. Alternatively, specific stamps might be required for participation in certain grant rounds. In some ways Gitcoin Passport is a kind of Lego of Lego's in that it is itself a modular component in a Sybil defense system, but it can also be thought of as a wrapper around various stamp combinations that provide evidence for some specific credential. For example, one passport credential might be "Professional Presence" which takes in LinkedIn and Twitter stamps - another might be "Web3 education" that takes in NFTs or soulbound tokens administered by verified courses (e.g. Rabbit Hole, Gitcoin quests, various bootcamps). "Community Involvement" might include a boolean for whether a base-line number of grant donations has been met, as well as other indicators such as a boolean for number of twitter followers. This way of thinking implies some heirarchy of Legos, with stamp combinations that fulfil some common purpose being low-level Legos and Passport itself being a higher level Lego. 

Importantly, communities using Gitcoin Passport as an identity/Sybil defense Lego can define new stamps and screen passports in ways that give them the greatest power to defend their grant round. A great example is using GitPOAP as a stamp as this proves that a user has made some contributions to a specific Github repository, indicating that they are really part of a builder community for some project. This would be a very important stamp for one community, but irrelevant for many others. Rather than being a simple test of whether a user has a "valid" passport, communities are empowered to build nuanced trust and reputation systems from Gitcoin Passport stamps and related tooling.

As part of the tooling, Gitcoin passport exposes an API for builders that includes functions for scoring passports. This means prebuilt, free and open-source tools for analyzing and digesting Passport data can easily be integrated into a Sybil defense/identity system. The API makes it easy for developers to adjust the way a platform scores combinations of stamps. If a user doesn't agree with the default scoring algorithm defined by Gitcoin data scientists - no problem, they can define something that works for them without havign to build new tools from scratch but by tweaking parameters in simple API calls. The API itself is openly available and documented so it could be forked and revised by developers that want to make more substantial changes to the underlying code. Eventually, the landscape should include intuitive "no-code" UIs (e.g. web apps) for end users to define and combine their own Legos but also deeper access via modular APIs and open-access source code for developers. 

Gitcoin Passport is also a great example of composable tools being built for one purpose (Gitcoin Sybil defense) but being used in creative ways across Web3. It is being used to give roles in Ethstaker's Discord server, for gating NFT mints at Bankless Academy and adding Sybil resistance to the [Snapshot](https://go.gitcoin.co/blog/gitcoin-passport-snapshot-making-dao-coordination-more-secure) decentralized voting platform - very valuable use-cases that are completely disconnected from the original intended purpose - the epitome of composability!

![](upload://f6DjhTxJCtIhsHF6VZOxF3dtx2C.png)

### What other Lego's do we need?

Gitcoin Passport is a very powerful anti-Sybil lego with similarities to real passports in that it serves as a form of identification that also uses stamps to demonstrate temporary association and compliance with some entity. Certain country stamps are considered more high-trust than others and that gives some variable reputational boost to the passport holder. 

However, it has also been shown that retroactive squelching of Sybils paired with Gitcoin Passport is required to really robustly defend a grant round. At the moment this is done using a trained machine learning pipeline that is operated by a few expert operators within the Gitcoin Fraud Detection and Defense squad. The challenge is to turn this centralized modelling into a set of composable Sybil defense Lego's. One option might be to develop a standard template for modelling and model auditing so that users can train models on their own features and present the results openly to the community. It would be logical for the [Open Data Community](https://www.loom.com/share/bd5a722fdd91444b81e525f650f2e857) to participate in developing and audting models for subcommunities and ensuring they meet basic standards for performance and statistical significance. This would make it possible to train models for specific subsets of users rather than a single model that applies generally to the whole of Gitcoin. These retroactive Sybil defense models can then become Legos that round owners can use in combination with other tools, including Gitcoin Passport, to defend their grant rounds against Sybil attacks. The power is with the user - they can choose to train independently, or they can use Gitcoin models "out-of-the-box".

There are also less technical tools that could become Sybil-defense legos. For example, rulesets or guidelines for resolving disputes (someone tagged as Sybil might claim to be an honest user and require human intervention). It is also possibel to develop governance legos, so that good practises developed in Gitcoin DAO can easily be forked and applied to sub-communities - again preventing users from reinventing the wheel.


## How will people use them?

The beauty of composable, modular tools is that the original developers cannot predict all the ways the tools might be used, just like the manufacturer of Lego bricks can't anticipate what will be built with them. However, we can explain the intended purpose. The lego's developed at Gitcoin are intended to turn the platform into a decentralized protocol. Individual round owners will be able to simply import useful tools for Sybil resistance, dispute resolution, governance etc that they can tweak and control without relying on a centralized team from Gitcoin but at the same time benefiting from the experience and expertise of Gitcoin data scientists, grant managers etc who develop the tools in the first place.


## Dangers of Lego

Building with Lego's is amazing because there is an infinite combination of blocks that can be used to realize a wide space of possibilities. However, there are risks associated with this composability model too.

First, when we empower users we also empower Sybil attackers. Being completely open source and accessible also means giving Sybil attackers insight into the inner workings of the defenses that aim to keep them out. This might enable them to attack more effectively - the opposite of the desired outcome. However, it is still likely that the net effect of open-sourcing Sybil defense lego's is enhanced security. The reason is that just because an attacker can understand the tools used to build a protocol, it doesn't necessarily follow that they can then attack it. The composability principle suggests that it is the combination of Lego's the attacker would have to overcome, not the individual Lego's themselves. It doesn't help an attacker to know that they require a certain Passport stamp if that same passport stamp has a cost of forgery higher than they are willing to pay, for example. This is especially true when subcommunities are empowered to set their own eligibility requirements as they can require very specific sets of credentials that might not only be hards to forge, but be specific to that subcommunity, limiting the potential rewards for an attacker. Overall, it seems more likely that plurality in the defensive layer will shift the risk:reward ratio in the favour of the defender, not the attacker.

Bribery and blackmail, on the other hand, might be a bigger problem. What happens if, instead of bearing the cost of making Sybils conform to some eligibility requirements, an attacker instead spends their capital on bribing a round owner to adjust the requirements in their favour? With composable, tuneable tools, the round owner might have the agency to tune down certain parameters or be more lenient than they otherwise would in the trust scoring system to benefit an attacker in return for some reward. This is where human intervention is important - some heirarchy of oversight where round managers monitor grants in their round and set some top-level requirements (e.g. minimum trust score must be at least `x`, `y` stamp is an essential requirement etc) would help to combat this.

Similarly, accounts that have combinations of stamps and other credentials that are likely to be classified as non-Sybil (which can be tested by attackers using the open-source tools and some assumptions about the decisions round owners will make regarding their configuration) could be bought and sold on a black market. An example might be a user that is a real, vetted person with substantial proof-of-personhood associatd with their address deciding to sell access to that address for use in a specific round they were not already intending to participate in. Renting out personhood could be a profitable strategy for users, and the market would naturally find a price per rental that is high enough for users to be incentivized to participate and low enough that attackers would profit by using the rented accounts to vote in a particular way.

There is also a risk of creating unintended consequences and vulnerabilities in some combinations of Lego's. It is very powerful to be able to create anything, but it is also difficult to anticipate all the various attack vectors and weaknesses that could inadvertently be introduced when Lego's are arranged in certain configurations. While anything can be built from lego, it is also possible to build wobbly towers. We must try to prevent this with solid documentation and educational resources and community oversight. Incentivizing code maintenance and testing as well as building will be an important defensive strategy against these "wobbly tower" scenarios.

Finally, there is the risk of releasing tools that others could use for nefarious purposes, or in ways that do not match the ethos of the original developers. For example, even if individual Lego's do not collect and store personal identifying information, a fork of the same tools might. It would be difficult for users to tell between implementations that are sufficiently private and those that are not. At this stage, the only real defense against this is a vigilant community that can call these behaviours out, clear and accessible documentation that contains ample warning about potential scams and attacks, and the development of great user friendly tools that *do* meet community standards that will naturally be adopted instead.

## Summary

Composability is a superpower for decentralized protocols. Gitcoin Passport is a great example of a high-utility identity Lego. We also need to build out more anti-Sybil lego's to enable the transition to decentralized protocol, while also being aware that composability introduces some new risks. There is a lot of opportunity for contributions from the extended Gitcoin community (importantly including the Gitcoin passort and Open Data Science communities) in the form of new Legos as well as maintenance, testing and auditing of existing ones. The broader and more diverse the community of Lego builders, the more decentralized and resilient the new Gitcoin grants protocol will be.

*Thanks to several contributors from FDD and Gitcoin passport for contributing to this post!*

-------------------------

DisruptionJoe | 2022-12-08 17:09:37 UTC | #2

[quote="j-cook, post:1, topic:12265"]
It should also connect to other Legos, which requires some standardization of types and formats for inputs and outputs so that tools can be chained together in intuitive pipelines.
[/quote]

This is definitely crucial. I see the legos as some of the first "modules" being built to improve round operator experience. Starting with individual analysis that directly say something about a wallet's history, how a wallet interacted with a discreet round, or if a grant is an outlier in receiving sybil donations is the first step. 

When these types of analysis are combined, we then get analysis like "What ratio of the donations from this user went to grants previously flagged for having outlier levels of sybil donations. 

Finding the best thresholds for decision making will likely be done via data science models. However, the legos themselves being open source allows the community to verify that the flags triggered were triggered fairly. They could even suggest better models which result in reduced errors. 

[quote="j-cook, post:1, topic:12265"]
for example KYC/KYB Legos could be incorporated into a grant when required, and ommitted otherwise.
[/quote]

Love this callout to the KYC use case.

[quote="j-cook, post:1, topic:12265"]
For example, one passport credential might be “Professional Presence” which takes in LinkedIn and Twitter stamps - another might be “Web3 education” that takes in NFTs or soulbound tokens administered by verified courses (e.g. Rabbit Hole, Gitcoin quests, various bootcamps). “Community Involvement” might include a boolean for whether a base-line number of grant donations has been met,
[/quote]

I'd really love to see a DevRel squad really leaning into this "meta-stamping" which provides more context to a set of stamps. 

[quote="j-cook, post:1, topic:12265"]
he reason is that just because an attacker can understand the tools used to build a protocol, it doesn’t necessarily follow that they can then attack it.
[/quote]

FDD had an over-arching internal goal to be "Kerckhoff Compliant" by the end of this year. The majority of sybil behavior on the platform is from naive sybil accounts which are unlikely to invest the time and resources to look into our defenses. For those that do, new behaviors will be caught and GTC utility use cases may bring us a system which is more expensive to attack than it is to defend. 

[quote="j-cook, post:1, topic:12265"]
Bribery and blackmail, on the other hand, might be a bigger problem. What happens if, instead of bearing the cost of making Sybils conform to some eligibility requirements, an attacker instead spends their capital on bribing a round owner to adjust the requirements in their favour? With composable, tuneable tools, the round owner might have the agency to tune down certain parameters or be more lenient than they otherwise would in the trust scoring system to benefit an attacker in return for some reward.
[/quote]

Understanding "optimal capital allocation" will help with this. The community can highlight rounds that are working and ones that aren't. Donors can vote with their feet by choosing to participate in another round when they deem a round operator to be illegitimate. 

This is not only useful for identifying illegitimate round operator behavior, but also for identifying the best "funding stack". Which set of modules & legos generally result in better outcomes?


Overall, it is a great article! Thanks!

-------------------------

Salvador | 2022-12-08 22:50:50 UTC | #3

This post and [this one](https://gov.gitcoin.co/t/allocationism-towards-a-holistic-purpose-vision-strategy/11948) and [this one](https://gov.gitcoin.co/t/what-can-we-learn-from-brightids-aura-sybil-defense-software/11159/4) reminded me of this comment by @lthrift 

[quote="lthrift, post:20, topic:11090"]
I seem to read more posts about what FDD might do in the future and what new things could be explored, yet the known problem areas and scopes of work remain “too complex” and “unmeasurable”.

[/quote]

Does the FDD have plans to build any of these "Anti Sybil Legos"?  Which of the things "FDD might do in the future" has it ended up following through on?

-------------------------

DisruptionJoe | 2022-12-09 14:35:29 UTC | #4

Thanks for your thoughtful response. FDD in its current form has some propriety knowledge because we don't want to explicitly show the attackers how to beat the system. 

That said, we had an internal goal to become "[Kerckhoff](https://en.wikipedia.org/wiki/Kerckhoffs%27s_principle) compliant" by the end of this year. We aren't there yet. We will be there for the beta launch of the protocol. 

Here is an example of the current legos application. 

![Image 2022-12-09 at 2.00.02 PM|690x408](upload://u3xO905VwZ3oXhz4123Xh0Lyw6m.jpeg)

To address the two posts you referenced:

The first is a post on Allocationism. It is a high level idea that I was sharing with the DAO. It wasn't a specific call to action for FDD. (Though the post did have a specific call to action of one session exploring the DAO's movement to community led which happened the following day.) 

[quote="DisruptionJoe, post:1, topic:11948"]
# Conclusion

Join our DAO wide strategy session tomorrow at DAOvibes to continue thinking about how we will transition when the protocol has been launched!
[/quote]

For the second reference, yes, this is something we would like to do, but this specific suggestion is not actioned at this time. We have built out dashboards for the Fantom & Unicef round exposing data. Next we will need to take this to the next step to combine with the open source lego packages. 

We have made adjustments to our team to be able to quickly build out the legos while continually increasing the bar for quality. Our focus is on adjusting to the onchain future where we no longer have the account name as a primary key. Additionally, we need to make sure the passport scoring is sufficient for use cases outside of grants like Bankless NFT drop & Snapshot voting integrations. 

[quote="Salvador, post:3, topic:12265"]
Does the FDD have plans to build any of these “Anti Sybil Legos”? Which of the things “FDD might do in the future” has it ended up following through on?
[/quote]

You can evaluate our budget requests for the past 5 seasons and the milestone reports which accompany them. I'm not aware of many items that we have promised to execute and haven't. I do understand that it can be confusing to see many ideas floating on the forum and not knowing which are actually on our roadmap. 

I'd be happy to connect to discuss further if you would like. disruptionjoe#6464 on discord

-------------------------

Salvador | 2022-12-12 23:24:01 UTC | #5

Thank you for your response @DisruptionJoe 

I see now the legos outlined in the [S16 FDD Budget Request](https://gov.gitcoin.co/t/s16-proposal-integrated-fdd-budget-request/11890) and am looking forward to seeing them BUILT in season 16!

[quote]
* Scoring / Registry as Service

* In-house scoring innovation across use cases

* Enable Passport for Sybil Defense

* Enable RO to set programmatic eligibility requirements

* Passport stamps and different use cases across different communities

* New Donor scoring algo
[/quote]

[quote]
Designed scalable Sybil Scoring Legos
[/quote]

-------------------------
