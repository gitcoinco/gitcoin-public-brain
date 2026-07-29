---
id: 9797
title: "Scaling Funding for Blockchain-era Public Goods"
slug: scaling-funding-for-blockchain-era-public-goods
category: governancevision
url: https://gov.gitcoin.co/t/scaling-funding-for-blockchain-era-public-goods/9797
created_at: 2022-01-31T23:24:13.023Z
last_posted_at: 2022-02-10T12:29:53.638Z
posts_count: 5
views: 7100
like_count: 27
---

# Scaling Funding for Blockchain-era Public Goods

<https://gov.gitcoin.co/t/scaling-funding-for-blockchain-era-public-goods/9797>
owocki | 2022-01-31 23:24:13 UTC | #1

Every so often I’m tagged in a thread where someone has an idea about how to fund public goods with MEV, block rewards, or some other similar scheme.

Having been an active participant in some of these discussions about such ideas between 2017 - present day, and having been involved with the growth of Gitcoin Grants during those times, I have some context I would like to share on the subject.

High level - There are two barriers to high throughput public goods funding:

1. Funding Distribution Mechanisms
2. Funding Sources

Funding distribution mechanisms & funding sources are two sides of the same coin. They need to grow together, and not grow too far out of balance with one another.

# First barrier: Distribution Mechanisms

Before we even talk about funding sources for blockchain-era public goods, we need to talk about distribution mechanisms.

If we are to build a [pluralistic civilizational scale infrastructure for funding public goods](https://gov.gitcoin.co/t/a-vision-for-a-pluralistic-civilizational-scale-infrastructure-for-funding-public-goods/9503), we will need to have ways of distributing those funds with [high legitimacy](https://vitalik.ca/general/2021/03/23/legitimacy.html).

Funding sources can only have a positive impact on public goods if they can be distributed legitimately.

Legitimacy means different things to different populations. To myself, it means a mechanism is credibly neutral, and can consistently direct funding towards those who are delivering the most value for public goods, without being captured by other interests. Much of what constitutes legitimacy in this category of mechanism is worth its own post ([Vitaliks post on the subject is a great start](https://vitalik.ca/general/2021/03/23/legitimacy.html)), but there is one thing to know before we continue here:

**An implemented mechanism can only maintain legitimacy up to a certain scale.**

For example, Gitcoin Grants can currently deploy $6m/qtr to public goods with high legitimacy (low fraud tax), but at $600m/qtr, it cannot. Over time, as Gitcoin’s 2022 goals include “more scale”, that may change.

There are other great mechanisms out there. Another Quadratic Funding mechanism with high legitimacy, CLR.Fund funded on the order of $50k last quarter. Another project focused on crowd giving, [Giveth](https://giv.giveth.io/), is doing similar experiments. Optimism, in their [Retroactive Public Goods Funding experiment round](https://vitalik.ca/general/2021/11/16/retro1.html) gave away $1million last quarter.

For the purposes of this post - Let's assume that at some point, the mechanism design space will advance to a point where 100x the funds can be deployed to blockchain based mechanisms for funding public goods.

What are the most plausible places where that funding to come from? What funding sources have been tried in the past & what can we learn from those attempts?

# Second Barrier: Scaling funding for public goods.

Let’s lay out the history of what’s been tried and failed, so as to create common understanding about the state of the most promising funding sources of public goods.

In this post, I plan to focus on the most promising sources of funding for public goods. The criteria for promising are as follows:

1. **recurring** sources of funding for blockchain-era digital public goods.
2. **deepest** wells of funding for blockchain-era digital public goods.
3. **legitimacy** insofar as it is accepted by a majority of ecosystem participants

There are other important categories of public goods funding that I do not focus on, because they do not meet the above definition. For example:

1. I do not focus on fiat digital public goods. To learn about those, checkout Nadia Egbal’s excellent [Lemonade Stand](https://github.com/nayafia/lemonade-stand).
2. I do not focus on the way the Gitcoin matching pool is presently funded because it is focused on smaller contributions that do not recur. For more on that, checkout [Where does the Gitcoin Grants Matching Pool Money Come From?](https://gov.gitcoin.co/t/where-does-the-gitcoin-grants-matching-pool-money-come-from/9036)
3. I do not focus on amazing (but one-off) sources of funding by generous individuals or protocols who have struck it big and have an admirable (but one off) inclination to give back.

# Potential Funding Sources

With the above out of the way, let us explore the most seemingly promising (recurring + deepest liquidity + legitimacy) funding sources for blockchain era public goods.

## EIP 1559 or other burn-mechanisms

[EIP 1559](https://eips.ethereum.org/EIPS/eip-1559) introduced a new mechanism: a network fee that is burned every block.

How could this fund public goods? [The idea](https://twitter.com/sobizR/status/1487622057122668546) goes something like this:

> Instead of letting ETH issuance go negative, that money would be better spent funding research, core development, dapps, public goods, etc

On its surface, this seems like a promising novel source of funding for public goods. It satisfies both of our initial criteria for what a promising mechanism looks like: It’s both (1) recurring and (2) deep well of possible funding. Billions of $$$ in [burned ETH](https://watchtheburn.com/) could be redirected to public goods funding.

But upon further inspection, there are many problems with using this mechanism for public goods funding:

1. There is no on-chain governance for Ethereum, and no plans to create it. Therefore there is no legitimate way to decide which mechanisms the funding goes to.
2. Public goods funding mechanisms will be at the app layer, whereas the ETH burn is at the protocol layer. If the protocol layer were to bless specific apps as recipients of this funding, it would break the credible neutrality of the protocol layer.
3. The funding could be captured. The All Core Devs meetings would get 1000x more political (and susceptible to attacks) get when billions of $$ need to be allocated somewhere each month.

For these reasons, the contributors behind EIP 1559 decided not to include a public goods funding mechanism in EIP 1559. While EIP 1559 satisfies the criteria for recurring + deep well of funding, it does not satisfy the criteria for legitimacy of the participants.

### Scorecard
- [ ] Legitimate
- [X] Recurring
- [X] Well-Funded

## EIP 1890 & other Block Rewards Funding Initiatives

[EIP 1890](https://eips.ethereum.org/EIPS/eip-1890) was a proposal (which has since been withdrawn) to add a block reward to the Ethereum network which could be used to sustainably fund ecosystem public goods.

From the EIP:

> We recognize that, while technically trivial, the real challenge in inflation-based funding is social: how to fairly capture, govern, and distribute block rewards. It will take time to work out the answer to these questions.

This EIP ended up failing for the same reasons that proposals to add public goods funding via EIP 1559 failed. It breaks the credible neutrality of the protocol layer, requires on-chain governance, and could be possibly captured. 

While EIP 1890 satisfies the criteria for recurring + deep well of funding, it does not satisfy the criteria for legitimacy from the perspective of the participants in the Ethereum ecosystem (other ecosystems [such as BCH](https://news.bitcoin.com/bitcoin-cash-miners-plan-6m-development-fund-by-leveraging-block-rewards/) have decided that it is legitimate for their ecosystems).

### Scorecard
- [ ] Legitimate
- [X] Recurring
- [X] Well-Funded

## L2 Sequencer Fees

The founders of the Optimism L2 network [have pledged](https://twitter.com/optimismpbc/status/1445444759628091392) to donate 100% of their network's early sequencer fees to the public good of the Ethereum network.

Note that these are "private" profits, rather than "public" issuance, so this pledge was made at the discretion of the founders of Optimism, baked into their network design.  This sidesteps some of the legitimacy challenges with EIP 1559 / EIP 1890 issuance.

Since Optimism does $100k/day in sequencer fees, this is a promising way of funding public goods. It satisfies both our criteria of being a deep well of funding and being a recurring source of funding.

Since Optimism is a L2, it does not have the same security assumptions (nor need to stay credibly neutral in governance) as the Ethereum network. L2s are islands of experimentation in which funding for public goods can be baked in at the protocol layer.

### Scorecard
- [X] Legitimate
- [X] Recurring
- [X] Well-Funded

## Opt-in Pledge 1% Schemes

Over the last few months a handful of projects have been developed to allow projects to pledge a portion of their revenue to public goods funding. Some examples of these projects:

* [Protocol Guild](https://stateful.mirror.xyz/mEDvFXGCKdDhR-N320KRtsq60Y2OPk8rHcHBCFVryXY) - a way of pledging a portion of a DeFi/NFT projects network fees to fund public goods - specifically ETH protocol R&D and client development.
* [Gitcoin Aqueduct](https://gov.gitcoin.co/t/gitcoin-aqueduct/9684) - a way of pledging a portion of your net protocol fees to public goods, either to fund your own ecosystem or broader Ethereum public goods.
* [Green Pill](https://greenpill.party/) - a way of pledging a portion of your net worth to public goods.
* Public Goods Coalition - governance-minimized mechanism for funding a broad set of public goods across the ecosystem.

These initiatives are still inchoate, and it remains to be seen whether they will scale to create social consensus insofar as they create deep wells of recurring funding.

### Scorecard
- [X] Legitimate
- [X] Recurring
- [?] Well-Funded

## MEV auctions

MEV is the amount of value a miner can extract, above and beyond block rewards, by sequencing transactions. Karl Flouresch [explains](https://ethresear.ch/t/mev-auction-auctioning-transaction-ordering-rights-as-a-solution-to-miner-extractable-value/6788):

> being a block producer tasked with producing a particular block gives you a lot of power within the span of that block, letting you arbitrarily reorder transactions, insert your own transactions before or after other transactions, and delay transactions outright until the next block, and it turns out that there are a lot of ways that one can earn money from this. For example, one can front-run decentralized exchanges (both Uniswap-style and the order book variety), be the first to claim whistleblower rewards, have a favorable position in ICOs, as well as many other forms of mild manipulation of applications. Recent research shows that the revenue that can be extracted from this (called “miner-extractable value 283” or MEV) is potentially significantly higher than transaction fee revenue.

An MEV auction would be a way of capturing a portion of MEV by auctioning off rights to order transactions in a block to the highest bidder. 

While this may seem like an insignificant right, it actually has deep potential.  In the wall st financial world, there are firms that spend tens of millions of $$$ to create data centers that are close enough to Wall st to frontrun transactions.

Once implemented, the revenue from the MEV Auction could be used to fund public goods. This is basically what L2 sequencers do already.

### Scorecard
- [X] Legitimate
- [X] Recurring
- [X] Well-Funded

## Nation-State Taxes Redirection

Once web3 has generated enough highly-legitimate mechanisms for funding public goods, it is possible that fiat government tax revenue could be redirected to these mechanisms. Especially if the mechanisms prototyped in web3 are able to distribute funds in a way that is more credible, scalable, and low-overhead than their legacy counterparts.

One early example of this was [Downtown Stimulus](https://twitter.com/dtstimulus/status/1305838829245329408) - a Quadratic Funding experiment for retail businesses affected by COVID19 - which successfully distributed $45k worth of funding in Q2 2020.

There is a large opportunity here to "export" these mechanisms beyond blockchains. This is how Ethereum can "give back to the world" and how we can have more positive sum interactions with non-crypto institutions.

### Scorecard
- [X] Legitimate
- [X] Recurring
- [X] Well-Funded

# Conclusion

Funding Sources & Mechanisms for legitimate distribution of public goods funding are two sides of the same coin. 

There is interesting activity happening in both places, but it is not a solved problem - especially at scale. There is a diverse set of participants in the Ethereum ecosystem who are working on these problems.

(Thanks to [Tim Beiko](https://twitter.com/TimBeiko) for providing feedback on this post)

-------------------------

M0nkeyFl0wer | 2022-01-31 23:34:33 UTC | #2

Finding a solution to this problem is perhaps the ultimate unlock for humanity to thrive and survive. Love the score card. Great filter to apply to future projects focused on the same problem.

-------------------------

erich | 2022-02-15 20:41:28 UTC | #3

Another very much underexplored public goods funding mechanism that I'd like to see more experiments with is a concept called **Partial Common Ownership**. It's also known under the acronyms **COST** (Common Ownership Self-Assessed Tax) and **SALSA** (Self-Assessed Licenses Sold at Auction).

Consider a system where property owners themselves specify the value of their property and pay a tax rate towards public goods of, say, 2% of that value per year. But here is the twist: whatever value they specify for their property, they have to be willing to sell it to anyone at that price.

The theory promises that this gives us more productive and just markets than capitalism and communism. Follow this excerpt from @GlenWeyl and Eric Posner's 2018 book "Radical Markets" to read more about the mechanism's political-economic philosophy and mechanics: https://assets.press.princeton.edu/chapters/s11222.pdf.

![image0|690x436](upload://ybMFfRCn9rsPJjcVPYedM2MQq18.jpeg)
*[Henry George](https://en.wikipedia.org/wiki/Henry_George) kickstarted the movement for property value taxes back in the 19th century..*

Here are some neat implications of self-assessed property taxes in democratic, self-organizing ecosystems I want to highlight:

* If the value of a private property goes up, the income of public treasuries goes up. Rightly so, because the value of "private" goods often goes up due to community effort. For example, Moonshot Bots sell well because the community likes them. The Empire State Building is valuable because Manhattan's unique, vital, and diverse community makes it a sought-after and famous real estate. Billboards like in the above figure are pricey because communities look at them! Just as the eyeballs of the people in the Gitcoin community might look at this website right here and now or gitcoin.co/grants, and many more websites. (More on the subject of websites in a bit).
* Assuming informed/rational behavior among the agents, the allocative efficiency of any property is nearly maximized while maintaining investment efficiency.
* Less room for price discrimination in property markets. See an illustrative example of the problem here, as it looks like [single women are losing out due to price discrimination in property markets](https://www.economist.com/graphic-detail/2020/02/25/single-women-are-losing-out-in-the-property-market?utm_campaign=the-economist-today&utm_medium=newsletter&utm_source=salesforce-marketing-cloud&utm_term=2020-02-25&utm_content=article-link-4) under capitalism.
* Unjust deprivation of property (as in genocides and slavery) does not come with permanent property rights for the new proprietors.

#### What are some exciting experimentation opportunities around this idea?
* Content-control rights on websites.
  * Imagine "featured grants" on Gitcoin webpages. Community members would exchange the rights to publicly display their favorite grants on these pages. The resulting value taxes could go to the Gitcoin grants treasury. Besides the continuous revenue stream for the Gitcoin Grants treasury, this would also solve the inevitable social problems around grants sortition on gitcoin.co/grants, @annika, @connor, and @ceresstation.
  * Imagine a similar arrangement for featured token pairs on Uniswap. Again, the related tax could go to the Uniswap grants treasury. (It looks like a social tool like this would be a natural match for DAOs.)
  * Imagine self-assessed control rights of ads/content would become the default on the web.
* ENS names. Web domains.
* Art/music NFTs. (Although personally, I'd prefer more open-source art/music production funded quadratically.) For instance, Moonshot Bots generated a one-time payment for the grants treasury. In comparison, with self-assessed licenses, every Moonshot Bot NFT might have continuously generated Gitcoin Grants treasury revenue until today and beyond.
* Almost any intellectual property (e.g., voting rights, software)
* Block proposer rights after the Ethereum merge. The mechanism could help deconcentrate power on the consensus layer of proof of stake blockchains more generally.
* To name a few of the countless physical property examples: screen control rights at conferences, billboards, land, machines, e-scooters, trains, apartments, offices.

The sky's the limit. And I'd love to help drive a Moonshot around this mechanism. For example, call it ads.party considering the website content control rights the lowest hanging fruit. There'd be generally two different approaches to kick this off, either double down on a particular case, say Gitcoin Grants ads. Or on the other hand, on building a software development kit for website administrators like Gitcoin, Uniswap, and The Economist to govern ad/content control rights on their pages.

Check out some existing repositories and prototypes around the partial common ownership mechanism here:

* GeoWeb imagines the mechanism in augmented realities: https://github.com/Geo-Web-Project
* Nonomos is a prototype of it for media control rights on websites: https://github.com/anoanoano/NonomosHL
* Wildcards applies it to art NFTs to fund wildlife conservation: https://github.com/wildcards-world
* "This Artwork Is Always On Sale": https://github.com/simondlr/thisartworkisalwaysonsale
* [Calendar.org](https://calendar.org/) is a live experiment to assign global names to days on the Gregorian calendar: https://etherscan.io/address/0xb283c835410DC2c8429fBb38a410Ce021E263C78#code

The blockchain era opens a vast design space for programmable markets. However, let's not trick ourselves into the exact design mistakes like permanent ownership that inevitably lead to disproportionate power concentrations and conflicts. Instead, builders, in the name of public goods and democracy: Let's dare to prototype more radical markets that benefit ecosystems holistically.

-------------------------

kyle | 2022-02-10 00:15:13 UTC | #4

I have loved learning about Harberger Taxes lately as well. One additional use case is NFT or Loan values, which is something Gitcoin Friends @captnseagraves is working on.

-------------------------

DisruptionJoe | 2022-02-10 12:29:53 UTC | #5

[quote="erich, post:3, topic:9797"]
Imagine self-assessed control rights of ads/content would become the default on the web.
[/quote]

Phenomenal idea here.

I love the clear examples you and Kevin use in this conversation. It turns a conversation riddled with economic, academic, and ethereum jargon into an enjoyable read. Well done.

-------------------------
