---
id: 20217
title: "[SGTM 004]: Generating Yield on DAO Treasury Assets to Support Runway"
slug: sgtm-004-generating-yield-on-dao-treasury-assets-to-support-runway
category: open-discussion
url: https://gov.gitcoin.co/t/sgtm-004-generating-yield-on-dao-treasury-assets-to-support-runway/20217
created_at: 2025-03-27T19:01:15.323Z
last_posted_at: 2025-12-10T15:16:23.931Z
posts_count: 27
views: 6415
like_count: 70
---

# [SGTM 004]: Generating Yield on DAO Treasury Assets to Support Runway

<https://gov.gitcoin.co/t/sgtm-004-generating-yield-on-dao-treasury-assets-to-support-runway/20217>
Avantgarde | 2025-03-27 19:06:33 UTC | #1

# TL;DR

Avantgarde Finance proposes to further support the ongoing efforts to [get Gitcoin profitable](https://gov.gitcoin.co/t/its-time-for-gitcoin-to-get-profitable/19922) by activating idle assets in the [Gitcoin DAO treasury](https://etherscan.io/address/0x57a8865cfb1ecef7253c27da6b4bc3daee5be518#multichain-portfolio) to earn yield, grow the reserves, and improve overall financial sustainability.

As part of this proposal, Avantgarde in collaboration with MYSO will manage two different strategies on behalf of the Gitcoin DAO and its treasury:

* **USDC Strategy**: Deploying $5m USDC to a DeFi Yield Vault to earn above mainnet yield.

* **GTC Strategy**: Run an on-chain covered call strategy on GTC to earn yield without selling at depressed market prices, starting with two smaller $250k tranches.

**The goal of each strategy is to earn yield, and to earn yield only**. There are **no intentions to sell/swap** any of these tokens, merely to grow the size of the pie.

Details below.

# Introduction

Most so-called “altcoins” have been on a downward trend and struggled to maintain positive price momentum over time, hurting native-heavy treasuries along the way. Despite plenty of organisational achievements, GTC has unfortunately fared no better. The Gitcoin community did well to swap $5m worth of GTC into USDC through proposal [SGTM 001](https://v1.snapshot.box/#/gitcoindao.eth/proposal/0x08ce2761367b65bb652f9b92dabadca34d93a81d6bb4e91de0dcefd0fb763ad5) back in May of last year, and following the passing of [SGTM 002](https://v1.snapshot.box/#/gitcoindao.eth/proposal/0x524d7f51ea46bdc8fc461b999eff7a8da146386e5a49528b31d0a41293f0fe13), Avantgarde and Gitcoin are now building on these efforts together to address the situation further.

SGTM 002 introduced a much-needed diversification and yield-generation strategy for the Matching Pool (MP) that will significantly improve capital efficiency, extend the runway by earning yield on currently idle assets, and diversify into yield-bearing stablecoins to mitigate overall portfolio volatility and impact of trending price declines in the native token. A risk-robust multisig structure has also been agreed on and approved through proposal [SGTM 003](https://v1.snapshot.box/#/gitcoindao.eth/proposal/0xee2ebda98e107e57eb4bb19fd63a19f52bb73c9c38225ba8da65ef40388c2318), providing the necessary flexibility to execute said strategy in a satisfactory manner while providing ample protection for the DAOs assets.

While this has been long overdue, this strategic partnership between Gitcoin and Avantgarde not only signals the community’s readiness to address the issue of financial sustainability wholeheartedly, but also provides the means to do so in line with the community’s risk appetite. Ongoing efforts to [get Gitcoin profitable](https://gov.gitcoin.co/t/its-time-for-gitcoin-to-get-profitable/19922) could be further supported by applying the same best practices to the Gitcoin treasury as we’re now doing to the MP to improve financial sustainability.

As noted elsewhere,

[quote="owocki, post:1, topic:19922"]

Gitcoin exists to **fund what matters**—to allocate resources to the builders, public goods, and regenerative projects that push the space forward. But to fulfill this mission **at scale and over time, Gitcoin itself must be financially sustainable.**

[/quote]

Hence, this proposal outlines a path to strategically activate Gitcoin DAO’s idle treasury assets with the following key goals in mind:

* Offset the opportunity cost of not having idle treasury assets generate meaningful yield.
* Earn yield on the idle USDC
* Earn yield on a portion of the idle GTC without selling at current depressed market prices.

This proposal thus contains two strategies, one for each of the following assets: USDC and GTC. Details on each strategy follows in the same order below.

# Yield Generation

## 1. USDC Strategy (managed by Avantgarde)

A by-product of thoughtful diversification of the treasury is the potential for generating revenues for the DAO. In addition to reducing treasury volatility, allocations in stablecoins (but also ETH) can be put to work in DeFi to generate yield that will support DAO sustainability. We consider deploying the treasury’s idle USDC very much a necessary step for the Gitcoin community to help support the DAO’s sustainability and longevity.

On-chain rates in DeFi vary by collateral, across protocols, and through time (block by block). Rates are currently between 5% and 10% for the most liquid stablecoins markets like AAVE V3 and Compound. As such, they provide a useful baseline to illustrate the potential revenue that can be generated for the DAO.

![|602x416](upload://dZfBHdJdjwF6CvEGvIGejo946wG.png)

The Avantgarde DeFi Yield Vault provides diversified exposure to on-chain stablecoin yield within DeFi via tokens pegged to USD. The strategy takes an active, conservative approach, focused on diversification and larger battle tested protocols to manage capacity and smart contract risk. The strategy is run fully on-chain via an Enzyme vault. For reference, Avantgarde has been running the strategy in a regulated and permissioned vehicle offered to institutional clients since June 2024, yielding ~10% as of mid-March 2025.

![|602x415](upload://6anxzJSJZORdgf1FJC2baHq7XC3.png)

The team has experience managing the strategy through a number of environments, including the low yield environment in second half of 2024, until the volatility of the US election, and the subsequent regime change and run up in on-chain yields. Hence, we are comfortable with this approach and believe it to be in line with the risk capacity of the Gitcoin community. We recognise that change is the only constant within DeFi and are prepared to adapt the strategy as the opportunity set evolves, whilst staying true to the risk-conservative philosophy.

As discussed above, the fully on-chain [DeFi Yield Vault](https://app.enzyme.finance/vault/0x0f41351921ede8e61071f48fed253d96760720dd) will replicate the same conservative stablecoin strategy followed in the regulated vehicle, but in a format tailored for DAOs (fully on-chain and non-custodial). As such, **we propose that the Gitcoin DAO deposits its idle $5m USDC into the Avantgarde DeFi Yield Vault on Enzyme to earn yield**.

### Avantgarde DeFi Yield Vault

An actively managed, non-custodial and permissioned vault for whitelisted DAO treasuries to access on-chain yields within DeFi, focusing on the largest, most battle-tested protocols.

* Currently yielding around 10% (annualized), realistic average expectations 7-15% APY.

* Aims to be diversified across stablecoins, protocols, and underlying yield sources while balancing the level of yield with risk and capacity.

* Competitive fees, 0.5% protocol fee and 7.5% performance fee; calculated and paid out automatically by the vault.

* Reporting is on-chain provable and auditable 24/7 via the Enzyme UI, and Avantgarde will provide additional formal reporting on the performance of assets on a quarterly basis, and can respond to interim questions as the community deems appropriate.

* To protect participating DAOs from scrutiny, regulatory or otherwise, ownership of the vault is held by Avantgarde Treasury and controlled via a 3/5 multisig made up of two signers from Avantgarde Treasury, two signers from Avantgarde Finance, and one from Enzyme.

* Avantgarde Finance acts as the delegated manager with certain smart contract roles & permissions (ensuring that Avantgarde can not misappropriate the funds). However, the vault will remain open to other potential DAOs interested in utilising the vault for its treasury in a similar manner (this would require Avantgarde to whitelist them as a permissioned depositor). Gitcoin would benefit from the economies of scale as gas costs incurred from running the vault would be spread amongst a wider depositor base.

* The DAO can withdraw from the vault by notifying Avantgarde (the Delegates included as signers on the execution multisig (PGov, Tane and SEEDGov) could technically also withdraw if for whatever reason needed). Please note that the DeFi Yield Vault may hold positions that accrue rewards on third party protocols which ideally should be claimed prior to a withdrawal. Hence, while we could withdraw instantly and receive the deposit in the tokens held in the vault, the optimal way would be for the DAO to communicate its desire to withdraw in advance to facilitate liquidity management within the vault and ensure a seamless withdrawal process.

## 2. GTC Strategy (managed by MYSO)

Looking at the GTC price chart over the last 2 years, we can see that there’s been plenty of volatility and sideways chopping in between spikes.

![|602x380](upload://9abhNftLXJ8HQiSUC9RX1zwncyY.jpeg)

(source: [Coingecko](https://www.coingecko.com/en/coins/gitcoin))

While this is not an ideal picture for token holders, it presents profitable opportunities for the DAO to generate revenue off of this volatility on its idle GTC assets using structured covered call options. We explain how this strategy works in detail further below and provide examples to showcase its potential. The yields achievable through said strategy can be significant and provide a meaningful boost to the Gitcoin treasury, which could be used to offset operational expenses and/or mitigate some of the price decline.

### What’s a Covered Call?

A covered call is an option strategy that uses, as in this case, GTC as collateral to sell call options to institutional trading firms. The call option gives the trading firm the right—but not the obligation—to buy the committed GTC tokens at a pre-agreed strike price. Institutional trading firms are willing to pay for these call options to capitalize on volatility, whereby the seller (i.e., the DAO) receives an upfront, USDC-denominated premium immediately upon execution. 

*Note, these trading firms are not taking any directional view on the asset but rather their motivation is to carry out so-called "[gamma scalping](https://zetamarkets.substack.com/p/advanced-gamma-scalping-techniques?open=false#%C2%A7gamma-and-theta-a-balancing-act)", which involves hedging the acquired option to “buy low” and “sell high” dynamically, making profits from price swings.*
#### **Since the intention is not to sell any GTC;** 
* strike prices will be set far out from current GTC price so that the likelihood of reaching it is minimal.

* The aim is to continuously roll over this strategy to earn yield for the DAO.

![|602x329](upload://ih4UTfEIwZmyOl5YDBZcLsMlant.png)

#### Key Benefits of a GTC Covered Call:

* Upfront yield generation – Yield is earned immediately upon match via MYSO v3, with no need to wait until expiry.
* Stablecoin-denominated yield – Yield is paid in stablecoins, allowing for automatic treasury diversification without selling GTC.
* Efficient capital utilization – Large GTC amounts (up to $1 million notional, potentially more) can be deployed, unlike lending or DEX LPing, where only a fraction of capital is utilized.
* No outright selling of GTC – This strategy minimizes market impact and selling pressure compared to direct GTC sales.
* Selective divestment at higher prices – GTC is retained unless the strike price is reached, ensuring that if exercised, it is automatically swapped into stablecoins at favorable prices.
* Lower downside risk vs. holding – Compared to simply holding GTC, a covered call provides downside protection via the premium earned, which is paid upfront regardless of whether the option expires in the money.

### Proposed Covered Call Strategy

We propose a bespoke covered call strategy with:

* **Notional**: $500,000 GTC (2 x $250k tranches)
* **Strike prices**: Between 120-150% of the current spot price
* **Expiry**: 14-60 days
* **Strike selection**: Based on historical conversion probabilities
* **Initial target upfront premium**: ~$5,000 upfront for first 30 days and $250k tranche
* **General target premium**: ~2% of notional every 30 days (i.e., 24% in annualised terms)

**Note, effective yields may vary depending on GTC price and volatility.*

**The strategy aims to minimize conversion probabilities** by estimating future returns based on a random forest regressor and set strikes accordingly. The strategy can be continuously rolled over as long as no conversion occurs.

To ensure optimal parameter selection, we conducted some backtesting on GTC’s price history and ran some regressor models to predict future realized returns, which we then used to inform strike prices. See [here](https://docs.google.com/document/d/1uvQRIKkCmf_1ES1DmuddhLDNAgYgcTtrtQb4TAMQaJQ/edit?usp=sharing) for more details on the backtesting. We will continue to run these analyses on a rolling basis to make sure parameters are adapted to changing market conditions.

### Mechanics of the GTC Yield Strategy

#### 1. Strike and Expiry Selection

* Strikes will be set based on historical GTC return bounds, ensuring that the probability of conversion remains low (see next section and plot below).
* **Call strikes will be positioned where GTC’s price has not exceeded with a 90%, 95%, and 99% probability** over historical timeframes.
* This ensures that, in the rare event of option conversion, the strike price remains well above the current market price.

#### 2. Yield Calculation

Covered call strike and days-to-expiry selections are optimized for annualized returns while maintaining a minimal conversion probability. Below, we have plotted how relative premiums change for different timespans (days-to-expiry) and given a target conversion probabilities—for example, 10%. For instance, when writing a covered call with 30 days to expiry and aiming to maintain a maximum 10% conversion probability, the corresponding relative strike price that meets this criterion would be 128%. This means that price appreciation of up to 28% within the next 30 days is maintained, while any returns above that level are capped.

![|602x399](upload://3maolg2JoS4VLzaVVWkE3MiLlkz.png)

Using these strikes, one can then calculate the indicative relative option premiums for writing calls at those strike levels across varying days-to-expiry combinations (see plot below). For example, a covered call with 30 days to expiry and a 128% strike would yield a ~2.4% relative option premium, meaning that writing a call on $500,000 worth of GTC would generate an upfront premium of $12,000 USDC for the GTC treasury. As expected, relative option premiums tend to be lower for strikes with lower conversion probabilities and higher for those with higher conversion probabilities. Additionally, relative option premiums generally increase as the number of days to expiry extends.

![|602x399](upload://ajCK0pO5NQ9CD9MeD6C66cvTyL4.png)

#### In the Unlikely Event of a Conversion and Additional Risk Management

While this strategy aims to keep the probability of conversion low to avoid selling GTC, it cannot be ruled out entirely if we also want to earn some yield. In the event that we do see a major short-term rally beyond what our ongoing assessments suggest and GTC is converted into stablecoins, we can cycle back into GTC efficiently by writing cash-secured put options using the received stablecoin amounts (this can also be combined with yield bearing stablecoins). This approach is commonly referred to as "option wheel", where one systematically sells covered calls and, if converted, writes puts to repurchase the underlying asset at a lower price. By utilizing put writing, we could:

* **Buy back GTC at a predefined price** – Writing a put option on the received USDC amount allows us to repurchase GTC at a strike price we determine, ensuring controlled re-entry.
* **Continue generating premium** – Similar to covered calls, writing puts generates additional yield, meaning the DAO benefits from stablecoin-denominated income while maintaining flexibility in repurchasing GTC.
* **Optimize capital efficiency** – Instead of holding stablecoins passively, put-writing ensures the capital remains productive, allowing for continuous cycling between GTC and stablecoins based on market conditions.

For execution, the put-writing strategy can be carried analogously to call writing taking into account the DAO’s liquidity and market exposure preferences, with strike prices and expiries structured accordingly. This allows for an efficient re-entering into GTC if needed.

For additional comments on risk management, see [this](https://docs.google.com/document/d/1f5zz72T0EjxQACbLmFjOvCmYLXC0Tht6SDzTlyKxT2o/edit?usp=sharing) doc.

# Implementation and Execution

While the infrastructure setup and implementation of the proposed treasury management strategy will be fully detailed in a follow up on-chain proposal, we outline the implementation from a high level below.

Typically, Avantgarde has used **a combination of Safe multisig roles & permissions** (via the Zodiac Roles Modifier) for implementing bespoke treasury management strategies, as was recently approved in proposal [SGTM 003](https://v1.snapshot.box/#/gitcoindao.eth/proposal/0xee2ebda98e107e57eb4bb19fd63a19f52bb73c9c38225ba8da65ef40388c2318) for the Matching Pool.

**We propose to follow a similar structure for the DAO treasury**, as it provides beneficial flexibility to easily withdraw USDC for upcoming ops cost needs from the Foundation as well as fine-tune execution on the GTC strategy, while still protecting the DAOs assets.

The assets to be managed will be sent into a separate Avatar safe *(owned by the Gitcoin Governor contract and controlled by the DAO)* with certain set permissions so that the manager can only perform specific pre-agreed actions on selected protocols (Enzyme and MYSO). The Manager multisig will be a 2 out of 5 and have Avantgarde, Myso, PGov, Tane and SEEDGov; allowing Avantgarde and Myso to line up and sign on the time-sensitive options transactions with flexibility while still maintaining two layers of security (Avatar safe with permissions + /5 multisig).

## USDC Strategy
As mentioned, the USDC will be deposited in a non-custodial fashion from the Avatar safe into the Avantgarde DeFi Yield Vault on Enzyme.

[Enzyme](https://enzyme.finance/) is an on-chain and decentralized asset management protocol that has been on mainnet since 2019, and is as such one of the most battle-tested protocols across Ethereum. Enzyme is an open source code base, and the smart contract code for both the Enzyme vaults and the platform’s core protocol can be found on[ Github](https://github.com/enzymefinance). The contracts are fully tested and independently audited; the most recent [release](https://github.com/enzymefinance/protocol) (v4) [audited](https://github.com/enzymefinance/protocol/tree/v4/audits) by[ ChainSecurity](https://chainsecurity.com/) and [OpenZeppelin](https://openzeppelin.com/) amongst others, with a[ current bug bounty of $400’000.](https://immunefi.com/bounty/enzymefinance/) The[ Enzyme App](https://app.enzyme.finance/) has also been fully audited.

## GTC Strategy

Execution of the covered calls will be done through the [MYSO v3](https://www.myso.finance/) protocol, which eliminates the need for institutional trading firms to take custody of Gitcoin tokens or rely on off-chain legal agreements. The entire process is decentralized, secure, and transparent, ensuring maximum returns while retaining full asset control.

MYSO is a DeFi protocol specializing in on-chain structured products, enabling HNWIs, treasuries, and asset managers to generate upfront stablecoin income by writing bespoke covered calls and cash-secured puts on a wide range of ERC-20 tokens. The protocol sources institutional liquidity by partnering with leading trading firms, ensuring competitive pricing and efficient matchmaking for large-sized trades. By enabling trustless, on-chain settlement, it eliminates counterparty risk, allowing users to write options more efficiently.

The protocol consists of two core smart contracts: the Router and the Escrow Implementation Contract. These contracts are publicly available in the official MYSO V3 repository and have been thoroughly audited (see [Omniscia Audit Report](https://omniscia.io/reports/myso-finance-call-option-system-v3-6737e49a92361c0018163789/)). Users only need to interact and approve the core Router contract, which manages all token transfers related to option writing, auction creation, bidding, exercising, borrowing, and fund withdrawals.

# Reporting

Avantgarde Finance will provide monthly (written) reporting on the strategies’ performance.

# Compensation Structure

**USDC Strategy**
The DeFi Yield Vault comes with a competitive 0.5% protocol fee and 7.5% performance fee; calculated and paid out automatically by the vault.

**GTC Strategy**
We will charge 15% of fees on any USDC denominated yield we make out of this. The rest will remain with the DAO and can be diverted to the USDC Strategy to complement and grow the USDC reserves.

## *About Avantgarde*
*Avantgarde is a licensed and DeFi-native asset management firm that specializes in non-custodial, on-chain strategies and strategic advisory for a range of DAOs, foundations, and crypto natives. The team has been active in DeFi since 2016 with significant experience in DeFi operations, including as co-founders of the on-chain asset management protocol Enzyme.*

*Leveraging our extensive investment and operational track records from TradFi firms such as Goldman Sachs, Blackrock, and Credo, we help DAOs and foundations to optimise treasury management strategies, improve financial sustainability, and support long-term growth. Some of our past and current clients include Nexus Mutual, Gitcoin, Near, Uniswap and Arbitrum.*

## *About MYSO*
*MYSO is a DeFi protocol specializing in on-chain structured products, enabling HNWIs, treasuries, and asset managers to generate upfront stablecoin income by writing bespoke covered calls and cash-secured puts on a wide range of ERC-20 tokens. The protocol sources institutional liquidity by partnering with leading trading firms, ensuring competitive pricing and efficient matchmaking for large-sized trades. By enabling trustless, on-chain settlement, it eliminates counterparty risk, allowing users to write options more efficiently.*

*MYSO has collaborated with numerous treasuries, including Telos, Evmos, DIA, and Across, as well as several HNWIs. The protocol has undergone security audits by Omniscia, Trail of Bits, Statemind, and ChainSecurity and is backed by leading crypto-native investors, including HashKey, Wintermute, GSR, Nexo, Huobi, and CMT.*

-------------------------

PGov | 2025-03-27 21:11:12 UTC | #2

​We support this proposal to generate yield on Gitcoin DAO's treasury assets because it strategically enhances the organization's financial sustainability. 

By deploying $5 million USDC into a DeFi Yield Vault managed by Avantgarde Finance, Gitcoin can earn yields between 5% and 10%, leveraging trusted and established protocols like AAVE V3 and Compound. Further, implementing an on-chain covered call strategy on $GTC tokens allows the DAO to generate income without selling its native tokens, effectively balancing risk and return.​

Overall, we think these strategies build upon previous successful initiatives, and Avantgarde Finance are prudent risk managers aligned with Gitcoin's mission.

-------------------------

Sov | 2025-03-27 23:41:32 UTC | #3

I support this proposal.  I have had the opportunity to work with the team for a number of months now and they have demonstrated their capabilities and, I believe, are well aligned to help with this.

In addition to their capabilities they have been a great partner to us and spent the extra time to understand our needs and been patient as we worked to progress these initiatives forward.

-------------------------

wasabi | 2025-03-28 00:13:34 UTC | #4

I fully support this proposal, I had the pleasure to meet with the team last week, and they're very aligned with Gitcoin needs and wants for this treasury diversification & yield strategy, I had the opportunity to ask questions and understand the risks for both strategies on a video call, also the team remains available for anyone that have further questions about the approach.

-------------------------

SEEDGov | 2025-03-28 15:50:40 UTC | #5

We're really happy to see this proposal!

We believe the approach proposed by Avantgarde is well-thought-out and balanced. Regarding the stablecoin strategy, we find it more than reasonable. A yield between ~7.5% and ~10% sounds pretty good in current market conditions. Also, the protocols picked to achieve it, the DeFi OGs, seem like the right choice. As for the GTC strategy, we also find it reasonable since the approach to minimises the risk whilst generating stablecoin-denominated returns on idle tokens, making perfect sense. 

Looking ahead, we'd like to suggest that in the medium to long term, it might also be wise to consider addressing liquidity challenges more directly. Whilst the current strategies focus on yield generation without selling GTC at depressed prices, something not to be overlooked, a complementary approach to improve GTC liquidity could further improve the DAO's financial position. 

All in all, **we support this proposal** and look forward to see its impact on the financial sustainability of Gitcoin's DAO treasury.

-------------------------

robioreefeco | 2025-03-28 17:37:21 UTC | #6

I partially agree, the proposal is theoretically sound but impractical under current conditions.

### Considerations:

1. **Smart Contract & Protocol Risks** – While the proposal emphasizes conservative, battle-tested protocols, DeFi strategies inherently carry smart contract and counterparty risks.
2. **Covered Call Risks** – If GTC price surges unexpectedly, the covered call strategy could lead to the loss of tokens at an undervalued strike price.
3. **Liquidity Management** – The USDC yield vault may require proper liquidity management for seamless withdrawals, which should be clearly outlined.

### Suggestions for Clarity:

* Specify the **exact risk mitigation measures** for both strategies.
* Provide a **backtesting analysis** or past performance comparison for covered call strategies.
* Clarify **governance and oversight** mechanisms to ensure treasury assets are handled transparently.

**To boost GTC’s value and utility, we should study (or partner with) [Andre Cronje](https://x.com/AndreCronjeTech)’s yield-focused experiments.**

-------------------------

Recce | 2025-03-29 14:01:17 UTC | #7

I support this proposal. If $GTC needs to do justice to its investors this needs to be done. I'd like more such proposals to flow through as I hold these GTC

-------------------------

Avantgarde | 2025-03-29 16:23:10 UTC | #8

Thank you all for sharing your thoughts so promptly! We're glad so many of you see value in the strategies we're proposing, and very much appreciate the kind words some of you've shared.

Addressing some comments below:

[quote="SEEDGov, post:5, topic:20217"]
Looking ahead, we’d like to suggest that in the medium to long term, it might also be wise to consider addressing liquidity challenges more directly. Whilst the current strategies focus on yield generation without selling GTC at depressed prices, something not to be overlooked, a complementary approach to improve GTC liquidity could further improve the DAO’s financial position.
[/quote]

Thank you @SEEDGov for your support. We'd be happy to discuss GTC liquidity and assist the DAO in any way we can.

[quote="robioreefeco, post:6, topic:20217"]
### Considerations:

1. **Smart Contract & Protocol Risks** – While the proposal emphasizes conservative, battle-tested protocols, DeFi strategies inherently carry smart contract and counterparty risks.
2. **Covered Call Risks** – If GTC price surges unexpectedly, the covered call strategy could lead to the loss of tokens at an undervalued strike price.
3. **Liquidity Management** – The USDC yield vault may require proper liquidity management for seamless withdrawals, which should be clearly outlined.

### Suggestions for Clarity:

* Specify the **exact risk mitigation measures** for both strategies.
* Provide a **backtesting analysis** or past performance comparison for covered call strategies.
* Clarify **governance and oversight** mechanisms to ensure treasury assets are handled transparently.
[/quote]

Thank you @robioreefeco for taking the time to review our proposal and provide your feedback. 
We wanted to address your points below, as we believe many of them are already covered within the proposal.


* **Smart Contract/Protocol Risks:** We understand that smart contract risk is a fundamental aspect of engaging with blockchain technology and DeFi, it is also kind of the whole point and thus difficult to avoid. Both Enzyme and MYSO are battle-tested and well-audited protocols. If we were to avoid established smart contract protocols entirely, there would be very limited avenues. See below for more context:

[quote="Avantgarde, post:1, topic:20217"]
[Enzyme](https://enzyme.finance/) is an on-chain and decentralized asset management protocol that has been on mainnet since 2019, and is as such one of the most battle-tested protocols across Ethereum. Enzyme is an open source code base, and the smart contract code for both the Enzyme vaults and the platform’s core protocol can be found on[ Github](https://github.com/enzymefinance). The contracts are fully tested and independently audited; the most recent [release](https://github.com/enzymefinance/protocol) (v4) [audited](https://github.com/enzymefinance/protocol/tree/v4/audits) by[ ChainSecurity](https://chainsecurity.com/) and [OpenZeppelin](https://openzeppelin.com/) amongst others, with a[ current bug bounty of $400’000.](https://immunefi.com/bounty/enzymefinance/) The[ Enzyme App](https://app.enzyme.finance/) has also been fully audited.
[/quote]

[quote="Avantgarde, post:1, topic:20217"]
contracts are publicly available in the official MYSO V3 repository and have been thoroughly audited (see [Omniscia Audit Report](https://omniscia.io/reports/myso-finance-call-option-system-v3-6737e49a92361c0018163789/)).
[/quote]

* **Covered Call Risks:** The "GTC Strategy" section, particularly under "Strike and Expiry Selection," details how we intend to mitigate the risk of losing tokens at an undervalued strike price. ***Our strategy involves setting strike prices far above the current market price** (120-150% depending on short/longer duration) **and continuously rolling over the strategy. The goal is to earn yield with a minimal probability of conversion.***

* **Liquidity Management/Governance Oversight** The "USDC Strategy" section, under "Avantgarde DeFi Yield Vault", specifically addresses the withdrawal process and we further elaborate on this and the governance/oversight mechanisms under the "Implementation and Execution" section; which includes the use of a separate Avatar safe controlled by the Gitcoin Governor contract and a 2 out of 5 multisig with representatives from Avantgarde, MYSO, PGov, Tane, and SEEDGov, outlining the permissions and controls in place for managing the treasury assets.



* **Provide Backtesting/Risk Management:** As mentioned in the "Proposed Covered Call Strategy" section, we have conducted backtesting on GTC's price history and included a link to the detailed backtesting analysis within that section, as well as a link to what we believe are the most relevant points on covered call risk management. See below:

[quote="Avantgarde, post:1, topic:20217"]
To ensure optimal parameter selection, we conducted some backtesting on GTC’s price history and ran some regressor models to predict future realized returns, which we then used to inform strike prices. See [here](https://docs.google.com/document/d/1uvQRIKkCmf_1ES1DmuddhLDNAgYgcTtrtQb4TAMQaJQ/edit?usp=sharing) for more details on the backtesting. We will continue to run these analyses on a rolling basis to make sure parameters are adapted to changing market conditions.
[/quote]

[quote="Avantgarde, post:1, topic:20217"]
For additional comments on risk management, see [this](https://docs.google.com/document/d/1f5zz72T0EjxQACbLmFjOvCmYLXC0Tht6SDzTlyKxT2o/edit?usp=sharing) doc.
[/quote]

We hope this clarifies the points you raised. We are confident that the strategies offer a balanced and safe way to generating yield on the Gitcoin DAO treasury while prioritising risk management.

Thank you again for your feedback, and we welcome further discussion.

-------------------------

Hydrapad | 2025-03-29 18:22:10 UTC | #9

I agree with the notion that DAO treasury should diversify it's revenue stream.

-------------------------

Tane | 2025-04-01 08:28:28 UTC | #10

Thank you for the proposal, @Avantgrade. 

We appreciate your efforts in advancing the DAO's treasury management strategy, a crucial step for its sustainability. We weren't heavily involved in the discussions for [SGTM 002](https://gov.gitcoin.co/t/passed-sgtm-002-avantgarde-x-gitcoin-strategic-asset-management-for-the-matching-pool/19698) and [SGTM 003](https://gov.gitcoin.co/t/sgtm-003-approving-multisig-structure-for-avantgarde-to-manage-the-matching-pool-assets/19904), but we recognize their importance and agree that further progress is necessary.

We appreciate the goal and the general idea, and let us share some questions for better clarity. 

1.Following the approach in [SGTM 002(for the Matching Pool)](https://gov.gitcoin.co/t/passed-sgtm-002-avantgarde-x-gitcoin-strategic-asset-management-for-the-matching-pool/19698), was increasing the treasury's ETH allocation to capture staking yields considered? If this path wasn't chosen, could you elaborate on the rationale behind that decision?

2.Regarding the USDC strategy, we would love to know how the 7.5% performance fee can be justified, especially when compared with other platforms. We also ask how the 7-15% target APY is realistic, considering [the linked Enzyme vault's ](https://app.enzyme.finance/vault/0xfa9fa21e2f38353b31ec7d67820f6df0b20f2a02) current performance (~5% APY).

3.We are also a bit skeptical about the GTC covered call strategy. With GTC only [~20% of the treasury](https://deepdao.io/organization/aca77a4e-ecb1-4eb3-a722-979977a52eb4/organization_data/treasury) while it's critical to include the native token strategy for other DAOs like Compound and Arbitrum, is the risk of reducing this allocation necessary? We also might need to define the target/goal of the treasury management strategy and should discuss if GTC strategy is indeed needed to meet our goals? 

For instance, deploying $5M USDC out of the $7M currently held in this [wallet](https://zapper.xyz/account/0x57a8865cfb1ecef7253c27da6b4bc3daee5be518) at a 10% APY could potentially generate $500k per year based on simple calculation.
While it's clear that income from treasury management alone is unlikely to cover all DAO expenses, this $500k could cover the majority of the estimated $609k needed for DAO operations, as detailed [here](https://docs.google.com/presentation/d/10zaUOyhRLKLRBOOLLpPti9gVutSI6cT0lHMV2cideAs/edit?slide=id.g31990768e1c_0_796#slide=id.g31990768e1c_0_796).

Additionally, we face potential issues: if our own DAO initiatives significantly increase the GTC price, the strategy could force sales, conflicting with our long-term holding goals. We should also consider the risk that effectively repurchasing GTC later (e.g., through the planned put options) might not always work out smoothly or as expected.

Therefore, we should clearly define target GTC holdings and establish a minimum threshold. If our holdings fall below this minimum, it should prompt us to review and potentially adjust our overall treasury management strategy, including how we utilize options.

-------------------------

Avantgarde | 2025-04-02 10:59:47 UTC | #11

Thank you @Tane for your thorough feedback. We clarify the points you bring up below:

### Regarding increasing the treasury’s ETH allocation for staking yields:

There are different considerations for the allocation of the Matching Pool, which **does not have the same starting composition and also has its own cashflow needs**. We believe that the **treasury was too volatile in the past** based on the adverse reaction of the community to price moves that can be considered normal and within the bounds of statistical expectations given the volatility of the assets involved (see year-over-year changes in USD terms below).

![|377x111](upload://kLz1srMsw7XHLEpiAxh11zjpQNf.png)

While the balance between different assets in the treasury could naturally change with organic price moves back to where stablecoins again represent a smaller portion of the overall portfolio, **we feel the priority right now should still be on managing risk and not increasing it**.

### Regarding the USDC strategy, the 7.5% performance fee and 7-15% target APY:

**A 7.5% performance fee is lower than many similar strategies in this space**, especially considering this is an actively managed strategy (that adapts to changing market conditions to optimise yield while adhering to a conservative risk profile).

Regarding performance, the **target APY is based on historical yields** and ultimately the yield environment across DeFi during the holding period will be a large driver. DeFi yields are inherently dynamic and fluctuate based on market conditions, protocol incentives, and overall demand for borrowing and lending. The 7-15% range reflects our realistic expectations considering historical data and potential market scenarios. **We shared a couple of charts in the proposal illustrating the volatility of these yields over time, please find them [here](https://gov.gitcoin.co/t/sgtm-004-generating-yield-on-dao-treasury-assets-to-support-runway/20217#h-1-usdc-strategy-managed-by-avantgarde-4).**

On the performance of the linked Enzyme vault, whilst this does follow the same strategy from risk perspective as the proposed vault, the existing structure was built with a different architecture (it powers a regulated fund vehicle) and accordingly the realised performance figures include a number of offchain costs - the proposed vault used for this prop is fully onchain and will not include these costs (which have made up ~50% of the regulated fund's total expenses incurred since inception).

### Regarding the GTC strategy:

We believe this strategy allows us to generate valuable yield on an otherwise idle asset in a way that aligns with the DAO's long-term goals and improves the DAO's financial sustainability. To reiterate, **our intention with the GTC strategy is solely to generate yield on our existing holdings on an ongoing basis, with no intention to sell GTC outright**. Yes there will be a small 5-10% probability of hitting strike prices and converting in the short-term, but again we have means of rotating back into GTC and even earn additional yield in the meantime, so we believe the “risk” associated with an unlikely but still possible conversion is being overplayed.

We acknowledge your points about GTC representing ~20% of the treasury but also understand **the DAO's need to improve its financial situation**. The $609k cited for operations doesn't encompass all budget requirements as far as we understand it, and the $5M USDC will likely be drawn upon for Foundation operations and other needs.

Regarding DAO initiatives increasing the GTC price, we obviously share your enthusiasm for DAO initiatives that could achieve this. We work closely with the Foundation and the DAO and would be thrilled to see such success come this way. As outlined in the proposal, **we will continuously monitor market conditions and the impact of Gitcoin's initiatives to adjust the covered call parameters** (strike prices and expiry) accordingly to ensure the strategy remains aligned with the DAO's long-term holding goals.

We do want to address what appears to be **a misconception that sales are forced when in reality strike prices and expiry dates can be set according to the DAO's needs and preferences**. Again, we will work with parameters where the probability of conversion is low, and set strikes at a comfortable distance from the current spot price.

To further illustrate with an example, if a covered call was set with a 30-day expiry and a 130% strike, and the premium was 2%, then if GTC increases by 30% after 30 days, there's no foregone upside. In fact, the DAO is better off, having converted at 130% of the spot price and also earned 2%. If GTC rallied by 35% in 30 days, the foregone upside would be "just" 3% (conversion at 130% plus 2% earned vs. the 135% spot price increase).

So **conversion doesn't necessarily lead to an inferior outcome than simply holding**, and secondly, one can accommodate and integrate price views into the strategy by setting strikes accordingly. Historically, a **short-term rally of the magnitude needed to hit the simulated strikes is improbable** according to the backtesting. Even in the event of such a rally, the DAO would realise a profit at a significantly higher price point, which would likely be viewed positively given the current financial situation.

You are correct that writing put options doesn't guarantee the repurchase of GTC if the strike price is not reached—but again, these **parameters are adjustable and we can set strike prices and expiries with strong probability of execution**. If the DAO for some reason would be in dire need of immediately acquiring additional GTC, we could just outright buy it. But since we believe there would be no need for such a rush, we could buyback at shorter duration intervals (say 7, 14, 30 days) to **allow the DAO to earn additional yield** on the stablecoins while having the option to buy back GTC at a predetermined price.

Regarding your example of deploying $5M USDC at a 10% APY generating $500k per year, while the simple calculation is correct, it's important to **note that current average yields on, for example, Aave are closer to 5%**---though we aim to outperform these baseline rates through strategic allocation and active management.

Lastly, we agree that defining target GTC holdings and establishing a minimum threshold is a valuable consideration for the overall treasury management strategy. We are in ongoing discussions with the Foundation, and the efficient, value-aligned management of the GTC holdings remains a key priority.

Let us know if you need any further clarifications!

-------------------------

Hydrapad | 2025-04-02 20:03:27 UTC | #12

[quote="Avantgarde, post:11, topic:20217"]
Regarding your example of deploying $5M USDC at a 10% APY generating $500k per year, while the simple calculation is correct, it’s important to **note that current average yields on, for example, Aave are closer to 5%**—though we aim to outperform these baseline rates through strategic allocation and active management.
[/quote]

@Avantgarde Thank you for this amazing proposal. It seems 10% APR on Stable coin is little too high in my opinion. Since it's a large sums of assets we are investing, why not create our own protocol for Gitcoin and develop strategies around GTC, It would be great for attracting external investors as well. And We the Gitcoin community can rally behind it with our own fund, jus saying !! :pray:

* Research 
* Development of Staking Protocol ( with good strategies and good APR% )
* Deployment

-------------------------

Tane | 2025-04-03 06:13:09 UTC | #13

Thank you, @Avantgarde for addressing our earlier questions and concerns. The detailed responses provided have effectively clarified most of the points raised, and we greatly appreciate the transparency.

In conclusion, we support this proposal. Given Gitcoin's current financial situation, pursuing additional yield through the outlined treasury management strategy is both prudent and justified. The risks you've explained appear acceptable and manageable within reasonable control measures.

[quote="Avantgarde, post:11, topic:20217"]
Lastly, we agree that defining target GTC holdings and establishing a minimum threshold is a valuable consideration for the overall treasury management strategy. We are in ongoing discussions with the Foundation, and the efficient, value-aligned management of the GTC holdings remains a key priority.
[/quote]

This aspect is essential for the effectiveness of the overall treasury management strategy, and we look forward to further clarity on this point in future discussions or updates.

-------------------------

deltajuliet | 2025-04-08 20:21:08 UTC | #14

Snapshot vote is live: https://snapshot.box/#/s:gitcoindao.eth/proposal/0xcf00de512cb500c78178a32db3a93528d7b5983d51105c5372151867eaeb1dce

-------------------------

Avantgarde | 2025-04-16 11:46:01 UTC | #15

Gm community - We're happy to say that the proposal passed with 99.99% of votes in favour! Thank you to everyone that took the time to vote, we greatly value the support and trust placed in us, and aim to deliver the best results possible for the Gitcoin DAO.

Next steps involve setting up the infrastructure as outline [here](https://gov.gitcoin.co/t/sgtm-004-generating-yield-on-dao-treasury-assets-to-support-runway/20217#implementation-and-execution-15), followed by an onchain Tally vote to move the assets to be managed into the Avatar safe so that we can begin executing on the strategy. We've already started the process and hope to have the proposal ready later next week or shortly thereafter given the upcoming Easter holiday.

We'll be back with an update once the proposal has been queued on Tally.

-------------------------

Recce | 2025-04-21 03:44:13 UTC | #16

Now please work on getting the price up to some respectable levels. Investors in GTC have been hammered very badly that a $28 token is down to $0.33 as of today. GTC needs to be a top 100 token and I think Avantgarde is more than capable of doing it

-------------------------

Avantgarde | 2025-04-21 09:33:27 UTC | #17

Thank you @Recce for your feedback and for expressing your concerns about the GTC price. We understand the frustration of seeing the token's value decline significantly. However, it's important to clarify that the strategies and overall mandate focuses on prudent treasury management – specifically, generating yield on idle assets to grow the reserves and improve the DAO's financial sustainability.

**Actively pushing the token price upwards is not within the scope of treasury management.** Token price is primarily driven by market forces, adoption, and overall sentiment, which are influenced by a wide range of factors beyond the direct control of us as a treasury manager. Our expertise lies in responsible asset deployment and risk management to improve the long-term financial health of the DAO, which we believe ultimately contributes to the ecosystem's strength and potential for future value appreciation.

Would recommend engaging with the various threads and posts on GTC utility highlighted by @owocki in this thread [here](https://gov.gitcoin.co/t/its-time-for-gitcoin-to-get-profitable/19922) for more context on the work being done re GTC utility etc.

-------------------------

Avantgarde | 2025-05-01 09:21:54 UTC | #18

Gm Gitcoin community! 

Following the passing of the [Snapshot temp check](https://snapshot.box/#/s:gitcoindao.eth/proposal/0xcf00de512cb500c78178a32db3a93528d7b5983d51105c5372151867eaeb1dce), the onchain Tally proposal has been queued and voting starts in less than 24hrs and ends early Wednesday next week. 

We're mindful of the various public holidays taking place across the world today, tomorrow and Monday next week, and would greatly appreciate if delegates can find the time to get votes in sooner rather than later. 

https://www.tally.xyz/gov/gitcoin/proposal/42131400951029541481048442097364639224689659286943854755170681178246078774463?govId=eip155:1:0x9D4C63565D5618310271bF3F3c01b2954C1D1639

Thank you all, we look forward to start executing on these strategies!

-------------------------

Avantgarde | 2025-06-05 10:24:40 UTC | #19

Gm and thank you to everyone that supported the proposal and helping it get over the quorum line - exciting to see all the new Stewards voting!

As soon as the proposal has been executed, we will allocate the funds as outlined. More updates to follow soon!

-------------------------

Sucre | 2025-08-04 17:32:19 UTC | #20

✅ In Favor  I fully support this proposal. Activating idle treasury assets to earn yield in a sustainable way is a smart move. It aligns with long-term financial health without compromising the tokens. Excited to see Gitcoin lead by example in responsible DeFi.

-------------------------

Avantgarde | 2025-08-04 19:11:31 UTC | #21

Gm Gitcoin community. 

After having deployed the SGTM 004 assets in late June, July was the first full month for the deployed strategies outlined above. As a reminder, 5M USDC were deposited into Avantgarde's [DeFi Yield Vault](https://app.enzyme.finance/vault/0x0f41351921ede8e61071f48fed253d96760720dd/portfolio) on Enzyme, and another 1.6M GTC were deployed into a covered call strategy on MYSO.

Below we provide the first update and will continue to do so here in this thread on a monthly cadence. 


### July Update
The [1,600,000 GTC](https://etherscan.io/tx/0xafd5937d1c5d902e6e2b51aeaefb2960bf38a2a98b6a0cd3f315a8aac98cf569) deployed into a covered call strategy via MYSO resulted in a **premium of 10,072 USDC**, which were subsequently deposited into the same DeFi Yield Vault as the 5M USDC. The covered call expires on 21st of September, at which point the strategy can be rolled over, depending on the call's outcome.

The DeFi Yield Vault saw an increase of 0.47% (or 5.8% annualised) in July. After a muted period for stablecoin yields which saw the supply rates of USDC on Aave struggle below 4%, the environment has shifted in the last week with a significant uptick in risk appetite following positive regulatory news in the US. 

The vault has taken the opportunity to reposition into higher yielding opportunities, within the context of its focus on large and battle tested protocols with high capacity. Expected returns have increased, with a portion of the portfolio fixed at 10% until September, and an increased allocation to USDC lending on Morpho, which is currently yielding 9%.

-------------------------

Donny_Jerri | 2025-08-15 09:33:04 UTC | #23

I was in favor of this proposal and love to follow these updates.  The utilization of sustainable DeFi strategies being employed is a pleasure to see for a ReFi public goods funding platform and DAO like ours.

-------------------------

Avantgarde | 2025-09-02 11:32:12 UTC | #24

### August Update

The DeFi Yield Vault saw an increase of 0.79% (9.92% annualised) in August. Risk appetite saw wild swings during the month, as ETH reached a new all time high before retracing over 10% into the end of the month. Funding rates whipsawed in tandem with price action, ending the period relatively subdued. Stablecoin yields remained healthy and the strategy maintained its positioning through the volatility, having secured a portion of the portfolio at a fixed 10.5% at the end of July and earned an average of 9.4% on the floating rate component through the period. The vault continues to focus on large and battle-tested protocols with high capacity and will look to adjust positioning into the end of September and redeploy capital as current positions mature.

-------------------------

Avantgarde | 2025-10-11 16:09:17 UTC | #25

### September Update
The DeFi Yield Vault saw an increase of 0.78% in September. Crypto prices moved higher in the first half of the month with ETH peaking at 4760 before moving into a period of choppy price action into month end. Funding rates followed an intuitive pattern, as strong risk appetite gave way to muted leverage demand as prices declined in the last two weeks of September. Stablecoin yields remained healthy through the majority of the period and the strategy continued to benefit from its allocation to fixed yield into the positions expiry in the last week of September. Opportunities were more muted in the last week, with the vault maintaining more exposure to floating rates until better fixed yields present themselves

With the market rallying in the summer, GTC also saw price go higher, from 0.203 in late June up to as high as 0.45 in mid August. This rally saw the covered call on 1,600,000 GTC exercised at a strike price of $0.3334 per GTC, yielding $533,203 USDC for the DAO (see [this link for full details](https://www.myso.finance/option/1:0x0e8f84852997dfb6c64d8a2cf66e3f0104b8e42b)). Since then, prices have come down to $0.2163 as of October 11th. After checking in with the Gitcoin team, the acquired $533k USDC will be deposited into the DeFi Yield Vault alongside the other ~$5M USDC to earn yield. Should the DAO have a strong preference to instead utilise the USDC as collateral to buyback GTC via cash-secured puts, we're happy to consider and elaborate on that further.

![image|690x359](upload://r0iEgy7rqW0MgtFK2uoNW0cuvSC.png)


As of today, the Avatar safe holds roughly $5,533,000 USDC.

-------------------------

Avantgarde | 2025-11-06 14:09:50 UTC | #26

### October Update
October proved to be a historic test for the crypto space, breaking the multi-year "Uptober" trend, including the severe flash crash on 10/10, which triggered a record level of liquidations across the space. The DeFi Yield Vault, where the DAO's stablecoins are currently allocated, saw an increase of 0.19% over the month (2.30% APY), as risk appetite and leverage demand waned, compressing yields in the second half of the month. Against this environment, the strategy took the opportunity to adjust positioning, increasing the allocation to attractive fixed yield positions against a backdrop of declining risk sentiment.

**November 6th Addendum**

* The first week of November has seen significant volatility in prices and also a number of notable events within DeFi.
* The Avantgarde DeFi Yield Vault has no direct exposure to the Balancer v2 exploit, no direct exposure xUSD, no direct exposure to the Moonwell exploit, and no direct exposure to Compound comets
* There is heightened volatility and large shifts in liquidity as markets continue to digest these events. We continue to monitor second order effects closely and our current assessment is that any potential secondary impacts at the strategy level are small and contained.
* Whilst risk is elevated, there have also been significant opportunities in otherwise sound markets that are impacted by this short term liquidity squeeze, leading to spikes in yield and abnormally high returns for those in a position to take the other side. Avantgarde has retained a high level of liquidity, which enables us to take a balanced approach in this environment, through a combination of controlled de-risking and measured allocations to capture opportunities from short term dislocations.

-------------------------

Avantgarde | 2025-11-14 21:03:44 UTC | #27

Dear Gitcoin community, **given recent events and as a follow-up to the November 6th addendum, we are here providing another update:**

As you may be aware, the market was shaken by recent events surrounding Stream Finance and its yield strategy xUSD, which announced a $93 million loss last week and subsequently halted all withdrawals. Among other things, this event had an immediate and severe domino effect on Elixir, which had significant exposure to Stream. The loss of this backing caused Elixir's deUSD stablecoin to de-peg and collapse, evaporating liquidity across the ecosystem and preventing withdrawals on underlying Morpho vaults, impacting a number of players in the space.

Our vaults had zero direct exposure to xUSD, nor did we have exposure to any Morpho markets where xUSD was used as collateral. The primary knock-on effect we have been monitoring is with Elixir’s deUSD, as Elixir (the entity) has lending exposure to Stream. Due to the uncertainty surrounding Elixir's exposure to Stream, the sdeUSD market on Morpho became illiquid, with all supply being borrowed. The Avantgarde USDC Morpho vault had a ~2% position, allocated to lending USDC to the sdeUSD market on Morpho. Due to our internal risk management framework and portfolio constraints at each allocation layer, the lookthrough exposure to the affected Morpho market was limited to ~1% in the DeFi Yield Vault where the DAO is invested.

To prevent the position from growing as it accrues an exponential amount of interest and protect against further impact, we redeemed the liquid ~98% of the vault's assets from this specific Morpho vault to segregate the funds while leaving the distressed 2% exposure to the sdeUSD market contained within the Morpho vault contract. That 98% liquid component has been moved to Aave as a temporary, defensive measure where they are currently earning a safe baseline yield, pending redeployment into the new, upgraded Morpho v2 vaults which we had already been in the process of building a migration plan for.

Segregating the funds ensures that all future on-chain accounting for the main, healthy portion of the vault is accurate and, importantly, enables the DAO to retain their full claim on any potential recovery value from the isolated 2% position. The resolution of the sdeUSD position remains unclear. If the loan is repaid (the 2% exposure), there is potential upside as Stream’s debt grows (currently accruing a yield north of 200% APR), though this recovery remains highly uncertain.

We will continue to monitor the situation and will update the DAO if any recovery becomes possible. Thank you for your continued trust in us, we are proud to be serving the Gitcoin community.

-------------------------

Avantgarde | 2025-12-10 15:17:19 UTC | #28

### November Update
November was characterized by broad market stabilization as the ecosystem absorbed the liquidity events of the previous month. However, stabilization has not equated to recovery in terms of yield generation and the DeFi sector remains in a risk-off posture, which has had a direct impact on stablecoin performance as funding rates remain flat and structurally suppressed across the board. We have subsequently de-risked positions to Aave to maintain conservative positioning in fixed yield given the increase volatility during the month. Nonetheless, the DeFi Yield Vault generated an **annualized yield of 6.05% in November**, and the DAO's deployed USDC holdings now stand at [$5,624,611](https://app.safe.global/home?safe=eth:0xBe66C0391453F4b5C5eFd47DdcCB2f6bA6aA513F).

.

-------------------------
