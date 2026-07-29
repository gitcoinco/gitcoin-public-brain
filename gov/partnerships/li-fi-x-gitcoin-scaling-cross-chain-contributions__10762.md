---
id: 10762
title: "LI.FI x Gitcoin: Scaling Cross-Chain Contributions"
slug: li-fi-x-gitcoin-scaling-cross-chain-contributions
category: partnerships
url: https://gov.gitcoin.co/t/li-fi-x-gitcoin-scaling-cross-chain-contributions/10762
created_at: 2022-05-30T21:03:10.314Z
last_posted_at: 2023-07-22T08:23:30.503Z
posts_count: 3
views: 2655
like_count: 5
---

# LI.FI x Gitcoin: Scaling Cross-Chain Contributions

<https://gov.gitcoin.co/t/li-fi-x-gitcoin-scaling-cross-chain-contributions/10762>
kram | 2022-05-30 21:12:35 UTC | #1

**Discussion:** 

LI.FI is super interested in working with Gitcoin to expand the platform's cross-chain contribution capability. This post is designed to begin a conversation about what a Gitcoin x LI.FI collaboration could look like. Here are our current thoughts. 

**End Goal:**

Create a GCP from LI.FI that, once passed, will allow Gitcoin users to contribute tokens from any chain without having to leave the Gitcoin website.

*Gitcoin’s Current Cross-Chain UI/UX*

Gitcoin is the OG crypto fundraising platform. However, as it currently stands, Gitcoin only allows users to donate tokens from Ethereum, Zksync, and Polygon. Furthermore, when “checking out” on the Gitcoin site, a user who wants to donate DAI on Polygon or Zksync is met with a pop-up that looks like this:

![|218x223](upload://wmrSyehIky0Gs4I216C9VrEwNCc.png)

Gitcoin then sends users to a new window to either 1) deposit funds on Polygon or 2) connect to a new wallet on Zksync. This type of user experience is challenging to navigate and off-putting – especially considering the median contribution is less than $2.

![|182x201](upload://qewcdUE9cflb866NqItQCtL92if.png)

For Gitcoin to remain the premier crypto fundraiser, the user experience for donating needs to be SIMPLE and SMOOTH. In all practicality, Gitcoin needs to allow contributions from any chain, with any token, with the least amount of clicks necessary - which can be enabled with LI.FI.

**What A LI.FI x Gitcoin Collaboration Could Look Like**

With LI.FI, Gitcoin could accept any token from any chain on its front end via the “checkout” button. Then, on the back end, LI.FI would facilitate a transfer to Polygon and a swap from any token to DAI – all in one click of the Polygon “checkout” button. As Gitcoin scales the chains it accepts donations from, this functionality could be expanded past Polygon.



**Three ways to integrate LI.FI**

* For the best UX: [The LI.FI SDK](https://docs.li.fi/products/integrate-li.fis-js-sdk/install-li.fi-sdk)
  * Gitcoin can integrate LI.FI into its UI using our JS/TS SDK. This is the most efficient and optimal solution for Gitcoin. Through the LI.FI SDK, Gitcoin can fetch routes, fetch user balances, and execute transactions for cross-chain contributions.
While this does require a bit more developer input, LI.FI would be more than excited to dedicate a dev for the integration.

* A compromise: An additional page: [Any Chain, Any Token Contribution Deposits](https://transferto.xyz/ukraine)
  * Our team can help make Gitcoin a completely new contribution page. We recently pushed out an example of how this could look to help facilitate cross-chain donations to [KlimaDAO](https://transferto.xyz/showcase/etherspot-klima?toChain=pol&toToken=0x2791bca1f2de4661ed88a30c99a7a9449aa84174).
* Alternatively: [The LI.FI Widget](https://docs.li.fi/official-documentation/simple-integrations/li.fi-widget) – easiest solution, but not as native of an experience
  * Gitcoin can use our LI.FI widget to facilitate cross-chain cross-chain contributions in a matter of hours. This widget could be activated via a newly created “bridge” button on Gitcoin’s website, which would allow users to bridge tokens to Polygon or Ethereum from any of LI.FI’s supported chains.

**Conclusion**

LI.FI would be very excited to help Gitcoin integrate a cross-chain checkout solution (with the least developer burden possible).

We believe that offering one-click cross-chain contributions is a killer feature for Gitcoin and would love to help make this possible.

**About LI.FI**

LI.FI is the most advanced bridge aggregation protocol on the market. Audited twice (Code4rena - March ‘22, Quantstamp - April ‘22) and with a team of around 25 people, LI.FI aggregates 9 bridges across 15 EVM compatible chains and all available DEX aggregators & DEXs on those chains into a single solution.

Special features: whitelisting, blacklisting, and a "prefer" function allowing integration partners to customize the suite of bridges that they utilize to their liking (e.g. if the project only trusts trust-minimized bridges like Connext & Hop).

[List of supported chains, bridges, DEXs](https://docs.li.fi/products/supported-chains-bridges-and-exchanges)

Our widget and SDK are the ultimate cross-chain money legos for dApps to build on top of or plug into themselves.

* We’ve integrated multiple fallback bridges+DEXs so that you don’t have to
* We maintain bridges+DEXs so that you don’t have to
* We choose the best bridges based on our research so that you don’t have to (positioning ourselves neutral)

For further examples of how LI.FI works, please refer to:

* [Alchemix](https://alchemix.fi/swap) - SDK Integration 
* [Alps Finance](https://app.alps.finance/#/trade) – SDK integration
* [Transferto.xyz](https://transferto.xyz/) – LI.FI B2C interface
* [Cross-Chain Klima Staking](https://transferto.xyz/showcase/etherspot-klima?toChain=pol&toToken=0x2791bca1f2de4661ed88a30c99a7a9449aa84174) – Custom built cross-chain staking product for Klima

Our documentation can be found here:

* SDK: [https://docs.li.fi/official-documentation/](https://docs.li.finance/official-documentation/)
* API: https://apidocs.li.fi

Website: https://li.fi/

Contact: @philippzentner on Telegram, akshay@li.finance via email

-------------------------

Luvlynj | 2022-06-13 21:00:27 UTC | #2

I think this is a very thoughtful idea, because the idea of checking out only on Eth based makes the whole idea of decentralisation flopped.

Using a cross chain would not only help the donator but also the developers

-------------------------

JowyAlt | 2023-07-22 08:23:30 UTC | #3

Thanks for information, i hope this news is good for everyone

-------------------------
