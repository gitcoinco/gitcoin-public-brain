---
id: 17290
title: "DeCartography Beta is out! How to generate clustered data from GR's participation data, and how to improve current Gitcoin Grants"
slug: decartography-beta-is-out-how-to-generate-clustered-data-from-grs-participation-data-and-how-to-improve-current-gitcoin-grants
category: open-discussion
url: https://gov.gitcoin.co/t/decartography-beta-is-out-how-to-generate-clustered-data-from-grs-participation-data-and-how-to-improve-current-gitcoin-grants/17290
created_at: 2023-12-18T07:25:51.923Z
last_posted_at: 2023-12-20T23:47:35.190Z
posts_count: 2
views: 4151
like_count: 9
---

# DeCartography Beta is out! How to generate clustered data from GR's participation data, and how to improve current Gitcoin Grants

<https://gov.gitcoin.co/t/decartography-beta-is-out-how-to-generate-clustered-data-from-grs-participation-data-and-how-to-improve-current-gitcoin-grants/17290>
tkgshn | 2023-12-20 03:01:27 UTC | #1

# TLDR
I finally finished a project I had been working on for some time called **DeCartography**.

A brief description of this project is "a tool to analyze and cluster data from participants in Gitcoin Grant Rounds and other events through crowdsourcing"

This clustered data could be used as an **infrastructure for Plural QF** and may be useful in [reducing collusion](https://gov.gitcoin.co/t/how-much-does-plural-qf-reduce-collusion-compared-to-normal-qf/15709). As a result, it is hypothesized that paying DeCartography to generate clustered data would make GR more efficient in funding.

However, Plural QF needs to cluster participants as donors. Therefore, **if we decide to analyze clusters based on "XX" (hard coding), a hack will be created to circumvent this.** (well known as [Perverse incentive](https://en.wikipedia.org/wiki/Perverse_incentive), [Campbell's law](https://en.wikipedia.org/wiki/Campbell%27s_law), and [Goodhart's law](https://en.wikipedia.org/wiki/Goodhart%27s_law))

https://x.com/DeCartography/status/1604248863661084681?s=20

Therefore, it is **necessary to cluster participants without defining criteria**.

> Theoretically, you can't do that. It's a contradiction!

You might think, But we believe it is possible with an **analytical oracle that balances the based on [Schelling Point](https://blog.ethereum.org/2014/03/28/schellingcoin-a-minimal-trust-universal-data-feed)**. That is DeCartography.

So, DeCartography can be understood as a **Relational computational oracle**. For better understanding, two aspects will be explained.
![image|690x196](upload://k9G1yPx33MYEl9RwyvFTuIaFWZ7.jpeg)
1. computational oracle. It analyzes some data and returns clustered data. 
2. crowdsourcing platform. The analysis process is distributed through crowdsourcing. Crowd workers can solve tasks according to their "intuition" and receive compensation from DeCartography.


Currently, [data from GR15](https://fddhub.io/) is being used for analysis, and crowdsourced workers are being paid in ETH (an unpriced token) distributed by **goerli testnet.**

In the future, we would like to use this tool to cluster GR participants and use it as an infrastructure for Plural QF. As a result, if we can prevent collusion and increase the financial efficiency of GR, we can make the project profitable as a computational oracle.

I would like to get feedback from everyone in the Gitcoin community.

---

# How to trial DeCartography

https://medium.com/decartography/decartography-beta-experiment-0-building-a-credible-neutrality-social-graph-powered-by-web3-3ed1a77887ca

**TRY NOW ➡️ http://app.decartography.com/**

[![Image from Gyazo](upload://ylUhcTsF04O9s05nnKCKkw31PRm.gif)](https://gyazo.com/22e64cc57defa57f4c7475bfd015706d)


- ***If your GitcoinPassport (GP) score is less than 10 or you have not created one, you will get an error when logging in***. In that case, please go to http://passport.gitcoin.co/#/dashboard to create and score your GP 
![image|680x478, 50%](upload://dBvmc57CiWWRtX8r0EJyxmcTX8y.png)

- Recommend using MetaMask to test from your desktop browser - After the task, Goerli testnet will send you the ETH reward. Transaction propagation may take a little time
![image|627x500, 50%](upload://fQpFgSAzGB6CRp9yhQbsdP0t0hX.jpeg) 
![image|680x394, 50%](upload://yneSjXXOMpDFHn0rLUEYwk4TuaK.jpeg)

https://twitter.com/0xCommune/status/1734831236810715339

---

# Detail as the project

## Problem

The core of the [QF attack vector is  **Sybil attacks** and **collusion**](https://medium.com/block-science/how-to-attack-and-defend-quadratic-funding-a10f0152f069).

For the former, [Gitcoin Passport, a DID aggregator, can mitigate damage by making it harder to create multiple accounts and adjusting voting power based on the Humanity Score](https://gov.gitcoin.co/t/decentralizing-sybil-defense-using-gitcoin-data/11382). The latter, on the other hand, makes it difficult to determine what is collusion. Therefore, a mechanism to adjust voting power based on the relationship between donors is proposed. In this area, Vitalik proposed [Pairwise coordination subsidies](https://ethresear.ch/t/pairwise-coordination-subsidies-a-new-quadratic-funding-design/5553/20?u=owocki), which was later published by @Joel_m as [Plural QF](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4311507) and [implemented](https://gov.gitcoin.co/t/proposal-ratify-the-results-of-gg18-and-formally-request-the-community-multisig-holders-to-payout-matching-allocations/16553) in Gitcoin by @umarkhaneth.

https://gov.gitcoin.co/t/q-e-d-program-update-1-request-for-community-input/15533/2

https://gov.gitcoin.co/t/q-e-d-program-update-two-experiments-on-the-vote-to-choose-beta-core-rounds/15991

https://gov.gitcoin.co/t/q-e-d-program-update-three-plural-qf-in-gg18-educational-posts-podcasts/17000

https://gov.gitcoin.co/t/proposal-ratify-the-results-of-gg18-and-formally-request-the-community-multisig-holders-to-payout-matching-allocations/16553

However, the clustering of participants that will be the infrastructure of the Plural QF is based on "clustering based on direct donation profiles (`donation_profile_clustermatch`)" and "predefined cluster data (`cluster_df`)".  
ref: https://github.com/Jmiller4/qf-variants/blob/main/qf-variants.py

as I mentioned above as **if we decide to analyze clusters based on "XX" (hard coding), a hack will be created to circumvent this.**  To make significant progress on this, a tool that "analyzes without defining indicators" would make it more collusion-resistant.

**Actually, indicator/matrix is hacked by some of the community.**
https://twitter.com/YourAirdropETH/status/1593422583088619522?ref_src=twsrc%5Etfw
https://dune-sight-69e.notion.site/3c304b7bbc2942bcb1dcd33bf6eb3e51

**"Project Side Witch Checking and Witch Prevention Ideas Sharing" describes how to avoid Gitcoin's civil judgment.** This is the problem we're facing

## Value Proposition 

Assumed Plural QF decreases collusion. it makes GR more effective. DeCartography provides infra data for Plural QF. so, **DeCartography makes GR more effective.** 

We provide clustered data in an anti-fragile analysis method that is resistant to such "indicator hacks". Its strength lies in its ability to cluster data using a decentralized, crowdsourced model, enhancing the reliability and integrity of data analysis in Gitcoin grant rounds and other events.


## Underlying Magic

The platform uniquely combines crowdsourcing with a peer prediction method, enabling analysis without predefined indicators. This method centers around Schelling Points, ensuring a more organic and unbiased clustering of data.

![image|690x206](upload://gYwckMFaWWRcSOfOebadU5NHq5X.png)
https://docs.decartography.com/ClusteringAlgorithm/


## Funding Model

This is the one of the oracle's business model. They receive compensation from the organization requesting the data analysis. The funds are used to compensate the crowd workers.
An example of money spent on similar roles is FDD's SAD.

- Revenue: Collect "data analysis/provide fees" from Dapps.
    - e.g., Gitcoin's #FDD. but, [they're dissolution](https://gov.gitcoin.co/t/fdd-workstream-dissolution-details/13852). so, I don't know who managing this. or, collaborating with [Plurality Labs](https://www.tally.xyz/gov/arbitrum/proposal/48957903989337452494807960514286334301924688097662612089398341037722439754861?chart=0)? cc @disruptionjoe
- Expenses: Distribute reward to crowd workers.

The difference is the profit.

It is estimated that 26% of users are Sybils (based on [GR14's data](https://gov.gitcoin.co/t/gr14-governance-brief/11050)). and spend 1/eval for Human Evaluations. 


> ## Human Evaluations
> 
> Although human evaluations are critical for removing bias and improving the sybil account detection algorithm’s learning rate, the stewards elected FDD to reduce this effort.
> 
> * GR14 = $1.00/eval | $3000 for 3,000 evaluations by 10 contributors
>   * Restructuring of the team
>   * Lowering the amount of evaluation while increasing the quality
>   * Reducing the cost per review by almost 30%
> * GR13 = $1.42/eval | $17,050 for 12,000 evaluations by 37 contributors
>   * Second time “sybil hunters” improve quality
>   * Established systems for recruiting and executing
>   * Focused on improving quality while lowering cost/eval
>   * Brought out the meme culture in FDD
> * GR12 = $4.39/eval | $26,350 for 6,000 evaluations by 25 contributors
>   * Opened up participation to all GitcoinDAO contributors
>   * First inter-reviewer reliability analysis to improve inputs
>   * Focused on improving quality of data entering the system
>   * Higher cost to get the inputs right and attract new people to participate
> * GR11 = $1.25/eval | $1,750 for 1,400 evaluations by 8 contributors
>   * First DAO led evaluations - Probably higher cost due to expert time from core team and SMEs for help
>   * Fairly low quality, little training done

DeCartography has the potential to replace this one. 

## Go-to-Market Plan

### Initial Steps

* **Current Status**: We have already launched the platform for analyzing GR15 data. However, currently, the rewards are distributed in testnet tokens.
* **Immediate Plan**: Following discussions in this post, we aim to transition to using ETH for rewards. We have allocated approximately $3,000 for the Proof of Concept (PoC). so, after discussing it with the Gitcoin team, we can start it.

### Market Penetration Strategy

1. **Proof of Concept with GR15 Data**: Using the data from Gitcoin Grant Round 15, we will demonstrate the effectiveness of DeCartography in reducing collusion. This will serve as a strong case study to showcase the platform's capabilities.
2. **Launching "DeCartography Rounds"**: Similar to the concept of rounds in Gitcoin Grant and RetroPGF, we will introduce "DeCartography Rounds." These rounds will focus on analyzing specific datasets, concluding once the analysis is complete.
3. **Integration with Plural QF**: The analyzed data from these rounds will be utilized to enhance the Plural QF mechanism, demonstrating the practical application of our tool.

### Outreach and Engagement

* **Target Audience**: Our primary audience includes teams hosting other QFs, Gitcoin community members, and potential collaborators in the field of decentralized funding.
* **Educational Content**: We will publish articles and case studies (inspired by sources like [Vitalik's Blog](https://vitalik.eth.limo/categories/gitcoin.html) and [Optimism’s article](https://optimism.mirror.xyz/Upn_LtV2-3SviXgX_PE_LyA7YI00jQyoM1yf55ltvvI) to educate our audience about DeCartography and its impact on reducing collusion.
* **Community Engagement**: Engaging with the community through forums, social media, and Gitcoin governance discussions to gather feedback and build a user base.

### Monetization Strategy

if find a word from [Public goods Legos: roadmap](https://gov.gitcoin.co/t/public-goods-legos-roadmap/12546), we'll aim to 
> users can upload their data (e.g. list of usernames and/or Ethereum addresses) and download their results in a web page

> The app then uploads the user’s data to a virtual machine, execute the selected algorithms, aggregate the results and return Sybil scores back to the browser. It is also easy to imagine additional features being made available via a marketplace of optional anti-Sybil add-ons.

>There are costs associated with computing Lego scores. This means that eventually, a cost would need to be attached to the Lego execution such that users pay a small fee to add a Lego to their anti-Sybil pipeline and the actual execution is done in a virtual machine whose management is abstracted away from the user

>a cost in ETH or a stablecoin could be calculated depending on the Legos the user has selected to implement which can be paid via a wallet integration before executing the Sybil Lego code. A freemium model may work well, with foundational Sybil algorithms being provided for free, and more computationally heavy ones being optionally added for a fee.

* **B2B and B2C Integration**: Developing a marketplace where data analysis seekers (toB) can post projects, and individuals wishing to work as crowd workers (toC) can apply. This will be similar to platforms like [AWS’s MTurk](https://www.mturk.com/).

* **Cost Structure**: Implementing a pricing structure based on the complexity of the analysis and the computational resources required, payable in ETH or stablecoins.

### Long-Term Vision

* **Expanding Services**: Post successful implementation in Gitcoin rounds, we plan to extend our services to other platforms and QF hosts, emphasizing the tool's ability to decrease collusion and enhance funding efficiency.
* **Building Reputation**: The initial phase will be more about building a track record and less about profit, paving the way for broader adoption and market penetration.
* **Faucet as Hyperstructure**: DeCartography trying to achieve ETH Faucet (on-ramp) for the next billion people as a Hyperstructure
   * Crypto faucets are a way to earn small amounts of free cryptocurrency by completing simple tasks. for example, you can claim testnet ETH at https://goerlifaucet.com/ or https://goerli-faucet.pk910.de/. 
   * However, many faucets for the public ETH testnets, including the Goerli testnet, have been [drained by farmers and bots](https://www.gitcoin.co/blog/gitcoin-passport-powfaucet). This has led to a lack of working faucets and a poor developer experience. **So, some Anti-bot services are required before claiming ETH in the faucet.  e.g., [PoWFaucet](https://www.gitcoin.co/blog/gitcoin-passport-powfaucet), [Superchain Faucet](https://blog.oplabs.co/superchain-faucet/)**
   * DeCartography can aim better on-ramp for the next billion people. probably reward from decartography is not many amounts, but crowdsourcing means a sustainable way. so, if you don't have enough gas fee, you can earn in DeCartography. which can also integrate with Wallet Apps in the future.

## Competitive Analysis

some other examples you imagine are **maybe not similar staff.**
they can generate a social graph based on paritipate's transaction. however, they must set an indicator/matrix to analyze. (include [Gitcoin](https://gov.gitcoin.co/t/quadratic-funding-x-effective-altruism/10016), [Token Engineering](https://twitter.com/tokengineering/status/1370096357906735113?ref_src=twsrc%5Etfw), [bubblemaps](https://bubblemaps.io/), [Breadcrumbs](https://www.breadcrumbs.app/) and [Nansen](https://www.nansen.ai/))

one of the similar things is [Nemurai](https://gov.gitcoin.co/t/knowledge-transfer-characterizing-the-sybil-resistance-problem/11235/2), [Aura](https://gov.gitcoin.co/t/what-can-we-learn-from-brightids-aura-sybil-defense-software/11159) and [SchellingCoin](https://blog.ethereum.org/2014/03/28/schellingcoin-a-minimal-trust-universal-data-feed).

however, DeCartography is such a unique. I had never seen this type of Oracle. 

## Financial Projections and Key Metrics


 **Key Metrics**: Focusing on the number of datasets analyzed, customer satisfaction ratings, and the rate of collusion reduction in funding rounds.

I think it would be a good idea to first provide a social graph that will serve as the infrastructure for Plural QF as a demonstration with Gitcoin. This is a concrete benefit that is easy to understand.

However, we would like to expand beyond that. Make it loosely coupled like the current Gitcoin Passport, which is also used for other Dapps as a Sybil measure.

(after several demonstrations with Gitcoin) The first and foremost idea would be integration with Grant Stack." As mentioned in the "Monetization Strategy", the goal is to make it available to everyone as a Hyperstructure. The fee will be charged on a pay-as-you-go basis based on the amount of data to be analyzed.



## Current Status, Accomplishments to Date, Timeline, and Use of Funds


this project was developed from a year ago. at first, the blueprint was [published in ETH NewYork '22](https://ethglobal.com/showcase/decartography-u9prm) as a hackathon, then [started being discussed in Gitcoin forum](https://gov.gitcoin.co/t/decentralized-social-graph-as-an-oracle-powered-by-the-wisdom-of-the-crowd-for-the-era-of-plurality/11927)

- **Current Status**: Successfully launched for GR15 data analysis.
- **Future Roadmap**: In the next six months, we aim to integrate with additional funding rounds and refine our clustering algorithms.
- **Use of Funds**: The funds will be allocated towards technological development, expanding our team, and marketing efforts to increase platform awareness.

-------------------------

fcarva | 2023-12-20 23:47:35 UTC | #2

huge! happy to see this out! congrats!

-------------------------
