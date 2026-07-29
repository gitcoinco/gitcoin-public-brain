---
id: 18268
title: "Citizens Innovate - Convert x% ETH/wETH into OETH for Passive Yield Generation"
slug: citizens-innovate-convert-x-eth-weth-into-oeth-for-passive-yield-generation
category: citizen-grants
url: https://gov.gitcoin.co/t/citizens-innovate-convert-x-eth-weth-into-oeth-for-passive-yield-generation/18268
created_at: 2024-03-07T22:59:28.586Z
last_posted_at: 2024-07-25T19:44:31.149Z
posts_count: 9
views: 4768
like_count: 6
---

# Citizens Innovate - Convert x% ETH/wETH into OETH for Passive Yield Generation

<https://gov.gitcoin.co/t/citizens-innovate-convert-x-eth-weth-into-oeth-for-passive-yield-generation/18268>
pete | 2024-03-08 13:01:00 UTC | #1

# Title: Convert  x% ETH/wETH into OETH for Passive Yield Generation

# Summary

Convert x% of the idle ETH/wETH from the Gitcoin treasury into Origin Ether for treasury diversification and yield generation.

# Abstract 

At the moment, more than 20% of the Gitcoin DAO treasury is made up of ETH. On its own, ETH does not earn yield, it will only accrue value from positive price movement. Rather than sitting idle, converting a portion of the ETH into OETH will diversify the treasury, help fund grants, donations, and social causes, and will help cover other Gitcoin DAO expenses, extending the runway of Gitcoin passively.

# Specification

*Origin Ether (OETH)*

[Origin Ether](https://www.oeth.com/) was launched in May 2023 and is an ERC20 LST aggregator that generates yield while sitting in your wallet by tapping into blue-chip protocols. OETH is backed 1:1 by stETH, rETH, frxETH, ETH, and WETH at all times; holders can go in and out of OETH as they please. Similar to stETH, OETH yield is paid out daily and automatically (sometimes multiple times per day) through a positive rebase in the form of additional OETH, proportional to the amount of OETH held.

OETH yield comes from a combination of:

1. Deploying collateral across Curve, Convex, Morpho, Balancer, and Aura
2. LST validator rewards
3. A 50bip exit fee is charged to those who choose to exit OETH via the [dapp](https://app.oeth.com/) (completely avoidable if using a DEX), this fee goes back to OETH holders
4. OETH sitting in non-upgradable contracts does not rebase, instead the interest generated from those tokens is provided to those that can rebase

These 4 yield generating functions combined enable OETH to generate higher yields than holding any single LST or farming ETH manually. The current collateral allocation and yield strategies can be seen on-chain at all times via the [OETH analytics page](https://www.oeth.com/analytics). Future OETH collateral and yield strategies are governed by [OGV stakers](https://governance.ousd.com/stake). More information on OETH and its mechanics can be found in the [OETH docs](https://docs.oeth.com/).

There is no set emission schedule for OETH - as with stETH, OETH is minted on demand when users lock their ETH or LSTs into the protocol, and burned on demand when users exit OETH for the collateral ETH or LSTs. OETH is completely non-custodial, there are no lock-ups, terms, or conditions. Any web3 wallet should be able to support OETH and its rebasing function, including hardware wallets and multi-sigs. There’s no need to ever again give up the keys to a 3rd party platform, such as Celsius, Blockfi, or FTX, to earn yield.

## Performance & Growth 

The OETH TVL, now over $170m (44,467 ETH), has been trending upwards and has been well received by users with the yield OETH is generating. OETH yield is currently at 7.24% APY, whereas native staking yield on ethereum has ranged from 3.03% - 4.03% APY over the last few months. 

![Screenshot 2024-03-07 at 3.04.05 PM|690x328](upload://qEsdVylWodPc1fciySdpGU61Dby.jpeg)

Origin has managed to integrate OETH to a range of verticals across Defi, including vaults, restaking, and money markets:

Eigenlayer - [Eigenlayer](https://app.eigenlayer.xyz/token/oETH)
Pendle - [Pendle](https://app.pendle.finance/trade/markets/0x62187066fd9c24559ffb54b0495a304ade26d50b/swap?view=pt&chain=ethereum)
Harvest - [Harvest App](https://app.harvest.finance/ethereum/0x924e022Ef8636FfA5971215e6Aac2652f7e9606e)
Beefy - [Beefy](https://app.beefy.com/vault/convex-oeth)
Yearn - [Yearn Vaults ](https://yearn.fi/vaults/1/0x79F4a9ed7a6196c67a2D6BCE8eC55E9F18802018)
Teahouse - [Teahouse ETH Vault](https://vault.teahouse.finance/ethereum/0xE1B3c128c0d0a9e41aB3fF8f0984e5d5bEf81677/)
Timeswap - [Timeswap](https://app.timeswap.io/#/borrow/ethereum/36b184ba-6601-47d2-afaa-5a9838f15ea4)
Interest Protocol - [Interest Protocol](https://interestprotocol.io/)
Tai - [Money God](https://app.tai.money/#/)
Myso - [Myso](https://app.myso.finance/)
Metastreet - [MetaStreet](https://app.metastreet.xyz/home)
Davos - [Davos Protocol](https://davos.xyz/app/loans/collateral/?network=eth&token=wOETH)
Locus - [Locus Finance](https://app.locus.finance/vault/xETH)

## Estimated Return

OETH rebasing happens at least once per day, but often multiple times per day. Yield earned from OETH is always subject to compounding interest. Please use [this calculator](https://docs.google.com/spreadsheets/d/1PB_xOT1SJvnvnJ4SeDy6aM8cninNJ4gNFvLLaahkwzg/edit?usp=sharing) to estimate the OETH return over four years. The calculations assume the investment is held within a rebase-capable EOA wallet, or that the smart contract wallet has opted-in for yield. On the calculator, cells in green are investments made at the beginning of the month, while cells in orange are months with no OETH investment. Some DAOs prefer to start with an initial test transaction. Parameters you may want to change and explore in the calculator are cells B70 - B73, B76 - E79, and B81 (outlined in bold boxes). To change the OETH APY or investment amount, select File > Make a Copy.

OETH vs the underlying LSTs - Please see the [30](https://ipfs.io/ipfs/bafkreihopcixhvpcyvrhpsl5i3ya4ii6ckqw5vlhf2e4xeut7aywnspv3m), [60](https://ipfs.io/ipfs/bafkreihxw4u6j4gle5j2hb5mhfubfwp6vusphknkdzsvp5e4dvtwcosk7u), and [90](https://ipfs.io/ipfs/bafybeibbav6wbcmpdwvlu3wovwdl5nlkqngw4rv7npm2u5jl57ztjq4rtq)-day reports to the Lil Nouns DAO on OETH performance vs stETH, rETH, and frxETH.

## Monitoring and Reporting

Occasionally, DAOs choose to appoint a delegated treasury team to help keep track of the OETH investment, participate in the collateral allocation votes, and initiate the investments into OETH. While there is no need to actively manage an OETH position due to the automated features of OETH, Gitcoin may want to appoint a similar treasury team.

Monitoring of the current OETH APY, strategies, and backing collateral, is always available in real time on the [OETH Analytics](https://www.oeth.com/analytics) page. A day-to-day OETH APY can be seen on [Proof of Yield](https://www.oeth.com/proof-of-yield), which is updated daily. Proof of Yield breaks down how much each yield strategy is contributing to the yield distribution:

![Screenshot 2024-03-07 at 3.23.00 PM|601x500](upload://n2hl3dcc38hdrniZFLA4XITj1ys.png)



API endpoints containing OETH data are also available via the [API page of the OETH docs](https://docs.oeth.com/data/api). To assist with reporting and decision making, the core team and community can use [this link to join](https://analytics.ousd.com/reports/subscribe) the distribution list that will receive a weekly OETH analytics report. Here is an example analytics report from the week ending August 06, 2023: [OETH Analytics Report](https://analytics.ousd.com/reports/weekly/2023/31).

## Benefits of Using OETH 

There are a few reasons for why Gitcoin would choose to use OETH over of attempting to utilize the same yield strategies: 

The yield will always be higher with OETH than if you were to use any of the same yield strategies, since not all OETH is opted-in for yield, and because of the exit fee. At the time of writing 34,168 OETH is opted-in for yield and 10,294 OETH is not, so Gitcoin would receive this boost in yield from the OETH opted-out. With the exit fee Gitcoin would get paid each time there's an exit - sometimes there’s a large exit that brings the combined yield into the 100s!

The Curve/Convex strategy would be very difficult (if not impossible) to replicate without having a Curve pool with a gauge + millions in TVL - Gitcoin would essentially need its own stablecoin and voting power and would be competing for yield incentives against the other large flywheel token holders, such as Frax, Alchemix, Convex, and Origin. 

The OETH protocol chases not just the highest yields but also the safest. During the weekend of March 10 when USDC and DAI depegged, it took the Origin strategists/Origin engineers about 4 minutes to notice the depeg, and 16 minutes to start the process of moving the funds to a safer strategy. $0 were lost! 

The OETH protocol covers all gas costs for sending yield to holders, and for moving funds between yield strategies, which is happening weekly but eventually will happen daily. With the price of gas on Ethereum, this could get costly for Gitcoin if Gitcoin were to follow the same harvest and reallocation schedule. 

The cost for security - Origin has OpenZeppelin on retainer! Every new OETH contract is audited before going live. OETH security is prioritized over new feature development. The same level of security would cost Gitcoin millions of dollars in audit and development costs. 

Top-notch development team - OETH shares 95% of the same code as OUSD, which has been live on mainnet for more than 2 years - longer than many projects today! The battle-tested code that has seen over $400m combined has been and continues to be developed by a team of 11 full-time engineers. This level of talent required to maintain the smart contracts would be extremely expensive for Gitcoin, if Gitcoin were to try and replicate the OETH strategies. 

With the extra funds Gitcoin will generate from OETH for the treasury, here are several ways to use these funds:

* Subsidizing public goods spend
* Subsidizing grant spend
* Subsidizing Gitcoin infrastructure, admin, and Passport expenses
* Subsidizing Gitcoin marketing, promotions, conference expenses, and swag
* Subsidizing cost for collaboration with other projects
* Rewards to those holding GTC over time
* Funding large team efforts for less
* Extending the Gitcoin DAO runway

## Contracts/Technical Requirements

Very little work is necessary to implement this proposal. The required steps are:

1. Gitcoin will convert the ETH/wETH into OETH via any of the following methods:

* Minting on [OETH.com](https://app.oeth.com/)
* Swapping on [Curve](https://curve.fi/#/ethereum/pools/factory-v2-298/deposit)
* Swapping on [Uniswap](https://app.uniswap.org/#/swap?inputCurrency=0x856c4efb76c1d1ae02e20ceb03a2a6a08b0b8dc3&outputCurrency=ETH)
* Swapping on [Maverick](https://app.mav.xyz/pool?chain=1&tokenA=0x856c4efb76c1d1ae02e20ceb03a2a6a08b0b8dc3&tokenB=0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2&fee=0.0004&width=0.001)


2. Gitcoin will “Opt in” by calling the 'rebaseOptIn()' function

Yield generation for Gitcoin will begin within 24 hours of holding the OETH within the treasury wallet. There are no KYC, KYB, or partnership requirements to earn yield, all that is necessary is to hold the tokens in a rebase-capable wallet.

If using a Gnosis Safe-connected wallet, Gitcoin will convert the ETH/wETH into OETH using the OETH dApp within Gnosis, and then will “Opt in” to yield generation by clicking the Opt in button within Gnosis or by calling the 'rebaseOptIn()' function.

A screenshot of the Opt in button on Gnosis can be seen here:

**![Gnosis|624x409.27458256029684](upload://j0PbN7Z5glSK7zsgo4cifdeptQM.png)**

##  Marketing Support

Origin’s marketing team will gladly provide support for co-marketing, should Gitcoin pass this proposal. Co-marketing can include long form Tweets and threads on [Origin's Twitter](https://twitter.com/OriginProtocol), live Twitter Spaces, features in Origin’s monthly investor email, announcements to [Origin’s Discord](https://discord.com/invite/ogn) audience, and an addition to [Origin’s ecosystem page](https://www.oeth.com/ecosystem). A Telegram group between the Origin and Gitcoin marketing teams can also be set up to discuss additional co-marketing ideas and efforts.

## Potential Risks and Mitigation

There are six possible risks when using OETH, and Origin is making sure to reduce each risk as much as possible:

*New token risk* - Given OETH is a relatively new token, some may be worried that OETH is prone to new attack surfaces. While this may be true for other new tokens, OETH was built reusing 95% of the [OUSD](https://ousd.com/) code, of which 10+ audits have been done since 2020. Not that long ago, [OUSD reached a market cap of $300m](https://defillama.com/protocol/origin-dollar) without breaking, and without diminishing the APY it was capable of generating. Origin continues to work on OUSD, despite the lower market cap.

*Counterparty risk* - OETH is governed by OGV stakeholders around the world. Everything from yield generation to fee collection and distribution is managed by a set of smart contracts on the Ethereum blockchain. These contracts are upgradeable with a timelock and are controlled by hundreds of governance token holders. While the initial contracts and yield-earning strategies were developed by the Origin team, anyone can shape the future of OETH by creating or voting on proposals, submitting new strategies, or contributing code improvements. We intend for all important decisions to be made through community governance and limited powers to be delegated to trusted contributors who are more actively involved in the day-to-day management of the protocol.

*Smart contract risk of the yield strategies* - Origin is only using platforms for yield generation that have a proven track record, have been audited, have billions in TVL, maintain a bug bounty program, and provide over-collateralized loans. Over-collateralization in itself, combined with liquidations, provides a reasonable level of security for lenders.

*Collateral risk* - Origin has chosen 3 of the largest LSTs to ever exist to back OETH, and they have maintained their peg quite well since launch. They have also demonstrated significant growth in circulating supply, so the Origin team is confident that the 3 LSTs will maintain their peg and that OETH will remain stable to ETH. To ensure accurate pricing at all times, OETH is using Chainlink oracles for pricing data for rETH and stETH, and a dual oracle for frxETH that combines two sources: the Curve frxETH/ETH EMA oracle and the Uniswap frxETH/FRAX TWAP oracle. In situations where any OETH collateral falls below peg, [OIP-4 disables minting](https://github.com/OriginProtocol/origin-dollar/issues/1000) of additional OETH tokens using the de-pegged asset.

*Slashing risk* - Since OETH is collateralized by multiple LSTs at the same time, OETH is protected from slashing from any individual collateral LST. If there is a small slash, the OETH yield will simply decrease, as income will likely exceed the size of the slash. During a major slashing event, both the slashed LST and OETH will experience a drop in value relative to ETH, but OETH should not fall as low and for as long as the slashed LST, as the remaining un-slashed OETH collateral LSTs will soften the blow. There will never be a negative OETH rebase.

*Smart contract risk of OETH* - Origin is taking every step possible to be proactive and lessen the chance of losing funds. Security reviews are prioritized over new feature development, with regular audits being done, and multiple engineers are required to review each code change with a detailed checklist. There are timelocks before protocol upgrades are launched, and deep dives into the exploits of other protocols are constantly being done to make sure the same exploits don’t exist on Origin contracts. Security is extremely important to the Origin team. OETH was built reusing 95% of the OUSD code, of which 10+ audits have been done since 2020. All audits can be seen on [Audits - OUSD ](https://docs.oeth.com/security-and-risks/audits), and OpenZeppelin is now on retainer. On-chain insurance protocol InsurAce awarded OETH and OUSD the [highest possible security rating of AAA](https://app.insurace.io/coverage/buycovers), of which only 2 other projects on the InsurAce platform have received. Optional OETH cover is currently available for both OETH and OUSD on InsurAce. Origin Defi also maintains a $1m bug bounty through [Immunefi](https://immunefi.com/explore/), with a resolution time of 5 hours.

External OETH analysis:

[Llama Risk](https://cryptorisks.substack.com/p/asset-risk-assessment-origin-ether) - Asset Risk Assessment: Origin Ether (OETH)
[Auxo](https://mirror.xyz/auxo.eth/1NXxHhJmj44EfHmvA5pEH7mpSLtg-CbYRqmuEkaTRRk) - OETH - Protocol Analysis

OETH in the news:

[Coindesk](https://www.coindesk.com/tech/2023/05/16/origin-protocol-enters-competitive-ether-yield-market-with-oeth-offering/) - Origin Protocol Enters Competitive Ether Yield Market With OETH Offering
[TokenInsight](https://tokeninsight.com/en/news/origin-protocol-launches-yield-aggregating-eth-derivative-called-oeth) - Origin Protocol Launches Yield Aggregating $ETH Derivative Called $OETH
[Blockster](https://blockster.com/maximize-eth-staking-yields-with-oeth-a-yield-bearing-ether-pegged-token-by-origin-protocol) - Maximize ETH Staking Yields with OETH: A Yield-Bearing, Ether-Pegged Token by Origin Protocol

## References/Useful links

* Website/dapp: https://oeth.com/
* OETH Docs/Litepaper: https://docs.oeth.com/
* OETH Contract: [Etherscan](https://etherscan.io/address/0x856c4Efb76C1D1AE02e20CEB03A2A6a08b0b8dC3)
* Audits: https://docs.oeth.com/security-and-risks/audits
* CoinGecko: https://www.coingecko.com/en/coins/origin-ether
* Communities
* Github: https://github.com/originprotocol
* Twitter: https://twitter.com/OriginProtocol
* Twitter: https://twitter.com/OriginDeFi
* Telegram: https://t.me/originprotocol
* Discord: https://discord.com/invite/ogn
* Medium (blog): https://blog.originprotocol.com/

## Disclosure

Peter is a core member of Origin Protocol and is joined by the fully doxxed [Origin team](https://www.originprotocol.com/community) and community, which includes hundreds of thousands of members and open-source contributors. Many members of the Origin team, including both founders, are holding a significant portion of their personal wealth in OETH. Origin Protocol’s corporate treasury is also holding millions of dollars in OETH. We have skin in the game and are willing to put our own money at risk with the code we have written.


## Vote

We propose the vote to be a yes / no vote.
Convert x% ETH/wETH into OETH, or do not convert. 

1 - Yes to convert ETH/wETH into OETH
2 - No do not convert ETH/wETH into OETH

-------------------------

CoachJonathan | 2024-03-08 13:00:27 UTC | #2

Hey @pete, just an FYI that I've moved this into the Citizen Grants section of the governance forum and have also changed the title since we are no longer using a numbering system for GCPs.

-------------------------

pete | 2024-04-08 15:33:16 UTC | #3

Hey @CoachJonathan, do you have any recommendations for ways to get more eyes on the prop, since there haven't been any questions or comments on it?

-------------------------

kyle | 2024-04-09 18:12:50 UTC | #4

Thanks for the post!

I want to confirm my understanding:
1. The goal/intention of the proposal is to move some amount of Eth from the matching pool into oEth.
2. The expected APY is currently 4% (and is based on a combination of other staking tokens from lido, rocket pool, etc)

This seems to be an okay option, and not much different from dsEth or options from IndexCoop. It does seem to be a worse option than to leverage EtherFi or other options that have a much higher yield. 

Do I have the details right though?

-------------------------

pete | 2024-04-09 20:41:10 UTC | #5

Hi @kyle,

The goal and intention of this proposal is to earn yield for Gitcoin by converting a portion of Gitcoin's idle ETH into OETH. The ETH can come from the matching pool or from any of the Gitcoin wallets (Ex: [wallet 1](https://etherscan.io/tokenholdings?a=0x19e50fa5623895d5a2976693eaff5c2f879510ed), [wallet 2](https://etherscan.io/tokenholdings?a=0x57a8865cfb1ecef7253c27da6b4bc3daee5be518), [wallet 3](https://etherscan.io/tokenholdings?a=0xde21f729137c5af1b01d73af1dc21effa2b8a0d6)), or from both - the OETH yield to Gitcoin will be the same.

The APY you are seeing is a trailing number - it has been as high as 7.49% APY over the last month, Origin's Proof of Yield confirms this: https://www.oeth.com/proof-of-yield/2024-03-18 

OETH is similar to Index Coop's dsETH, just with less assets used as collateral (3 vs 6), a higher yield (4.01% trailing vs 3.62%), and a much higher market cap ($156m vs $2.51m).

The above yield is real yield, coming from the mix of heavily audited strategies. There is no leverage, points, or speculated assets involved to reach the stated APYs. Although, if Gitcoin was interested in taking on the additional slashing and smart contract risk of restaking/liquid restaking for point farming, OETH is currently supported on [Eigenlayer](https://app.eigenlayer.xyz/restake/oETH), [InceptionLRT](https://www.inceptionlrt.com/app/restaking/restake/?token=oETH),  and [Eigenpie](https://www.eigenlayer.magpiexyz.io/restake).

-------------------------

CoachJonathan | 2024-04-12 08:21:06 UTC | #6

Hey @pete thanks for the ping.

The current Grants Council of @meglister @owocki (who is OOO for the next 2 weeks) and @Viriya should take a look at this and comment. I imagine that they will rely on the expertise of @kyle to help suss out the opportunity here.

I also wonder how this ladders (or competes?) with the work being done by @deltajuliet in her [treasury diversification](https://gov.gitcoin.co/t/temp-check-sgtm-000-treasury-management-strategy-for-gitcoin-v1/18564) post.

Lastly a couple of points for @rohit (our program manager) that are worth flagging:
- I think it's worth pondering how to further decentralize the Grants Council roles in the coming months
- We also discussed making some amendments to the categories of submissions that might impact a proposal like this and am wondering when we can get more information about this upcoming shift.

-------------------------

pete | 2024-04-12 18:59:35 UTC | #7

[quote="CoachJonathan, post:6, topic:18268"]
I also wonder how this ladders (or competes?) with the work being done by @deltajuliet in her [treasury diversification](https://gov.gitcoin.co/t/temp-check-sgtm-000-treasury-management-strategy-for-gitcoin-v1/18564) post.
[/quote]
As far as treasury diversification goes, OETH would be a great fit, but diversification does not need to be exclusive to OETH - spreading the ETH across multiple aggregators, LSTs, and LRTs would also be a great idea.

@deltajuliet I would also recommend taking a look at [OUSD](https://ousd.com/) for the stablecoin half of the treasury management strategy - the OUSD [yields](https://analytics.ousd.com/apy?rows=120) have been stellar lately!

-------------------------

meglister | 2024-04-12 21:20:42 UTC | #8

Thanks for pinging. I don't think this is an appropriate proposal for the Citizen's Innovate program or the Grants Council. This sits outside our current remit of funding initiatives that advance our product development and adoption and Essential Intents. I think this is best considered through a treasury diversification lens being led by @deltajuliet  (which also covers the matching pool.)

-------------------------

pete | 2024-07-25 19:44:31 UTC | #9

Hi @deltajuliet, there are some updates to share on OETH! As of the morning of 7/15/24, following a [proposal](https://snapshot.org/#/ousdgov.eth/proposal/0x76f64251d37310c5d241ec84a892751c7a34874faff7af848db193141ea24a6f) to convert OETH from an aggregator into a true LST, OETH no longer has exposure to other LSTs or yield strategies, as all OETH collateral LSTs have been divested back to ETH. That ETH will very soon be staked through SSV/P2p native DVT staking, so OETH can now be officially considered an LST. An additional [OpenZeppelin audit](https://github.com/OriginProtocol/security/blob/master/audits/OpenZeppelin%20-%20Origin%20SSV%20Native%20Staking%20-%20June%202024.pdf) for this new version of OETH was completed several weeks ago. Redemptions back to ETH are currently available at a 1:0.999 rate, and the addition of an [OETH ARM](https://www.originprotocol.com/arm-announcement) will soon enable instant exit liquidity at a 1:1 rate. 1. OETH will achieve the tightest peg to ETH of any LST with the combination of the ARM and [AMO](https://www.oeth.com/oeth-amo-improvements), and will also be the highest yielding when considering the additional yield from DVT staking.

-------------------------
