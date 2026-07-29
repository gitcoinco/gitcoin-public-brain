---
id: 19904
title: "[SGTM 003]: Approving Multisig Structure for Avantgarde to Manage the Matching Pool Assets"
slug: sgtm-003-approving-multisig-structure-for-avantgarde-to-manage-the-matching-pool-assets
category: open-discussion
url: https://gov.gitcoin.co/t/sgtm-003-approving-multisig-structure-for-avantgarde-to-manage-the-matching-pool-assets/19904
created_at: 2025-01-29T12:16:31.734Z
last_posted_at: 2025-02-10T07:32:13.961Z
posts_count: 8
views: 2293
like_count: 19
---

# [SGTM 003]: Approving Multisig Structure for Avantgarde to Manage the Matching Pool Assets

<https://gov.gitcoin.co/t/sgtm-003-approving-multisig-structure-for-avantgarde-to-manage-the-matching-pool-assets/19904>
Avantgarde | 2025-02-03 10:45:16 UTC | #1

## [SGTM 003]: Approving Multisig Structure for Avantgarde to Manage the Matching Pool Assets

The Gitcoin community recently approved a proposal for Avantgarde Finance to support the [Matching Pool](https://etherscan.io/tokenholdings?a=0xde21f729137c5af1b01d73af1dc21effa2b8a0d6) (MP) with strategic asset management ([Avantgarde x Gitcoin: Strategic Asset Management for the Matching Pool](https://gov.gitcoin.co/t/sgtm-002-avantgarde-x-gitcoin-strategic-asset-management-for-the-matching-pool/19698)). The following proposal aims to establish a secure and efficient multisig structure that grants Avantgarde the necessary permissions to manage the Matching Pool assets according to the outlined strategy.

Based on updated simulations using historical data and the $4.3m earmarked for 2025 GG spending, our analysis suggests that a 60% growth asset / 40% stablecoin allocation has the lowest long-term failure rate (i.e., % of simulations where the pool was fully depleted from spending) with 1.8 years of funding in stables up front (excluding any future yield generated).

![|602x415](upload://qiNZSmNfqAOW9DcwweJFkpqsB2N.png)

Since this is ultimately a matter of subjective risk tolerance and preference, the proposed strategy remains open for discussion. We look forward to hearing any final input that the community may have, and are also happy to rerun simulations under different risk assumptions if the community’s preferences have changed. In any case, we will continue to update this analysis as market conditions evolve.

# **Proposed Multisig Structure for Strategy Implementation**

To implement this strategy securely and efficiently, we propose a multisig structure with role modifiers that allows Avantgarde to perform certain treasury management actions autonomously within a pre-defined set of restrictions.

More specifically, the Zodiac Roles Modifier v2 along with the Zodiac Pilot Chrome extension will be used to interact through Zodiac roles, which allows for efficient execution of time-sensitive operations.

* **Repo:** https://github.com/gnosisguild/zodiac-modifier-roles
* **Audit:** https://github.com/gnosisguild/zodiac-modifier-roles/tree/main/packages/evm/docs

## Proposed Setup

* **Avatar safe:** This safe will be controlled by Gitcoin using the same signers as the Matching Pool multisig, and will hold all the assets to be managed by Avantgarde.
* **Manager safe:** This safe will be connected to the Avatar safe and will be used by Avantgarde to execute trades via four signers (listed further below).
* **Roles and Permissions:** The Avatar safe will define the Manager safe's permissions through an onchain Roles Modifier contract.
  * **Whitelisted Protocols & Assets:** The initial list of protocol functions and assets will need approval from the signers on the Avatar safe.
  * **Future Approvals:** This whitelisted universe will likely evolve over time with market conditions, and additional approvals may be needed in the future. We will try to minimise this where possible so there is less operational burden on Gitcoin’s end.

![image|690x461](upload://n4iwum9cC8yPEf62C8r4OEW2Wbi.png)

### Setup Addresses

* **Avatar safe:** TBD
  * Signer 1: 0x3C2dAe5E0cF3F27943686E9468A06a8377809813
  * Signer 2: 0xd58bB7Ae72B5b2FDc980C908baB75013a3628820
  * Signer 3: 0x0EdEeA07FB4E700a2A502FDB43414Bde3c75F8ee
  * Signer 4: 0x5F834C8f70baaEAfAd00662Cd214245c9A1A9ef5
  * Signer 5: 0x5a5D9aB7b1bD978F80909503EBb828879daCa9C3
  * Signer 6: 0x393BC37ea5493233D2bDC68FD59Dd97Ee01B18Cf
  * Signer 7: 0xc2E2B715d9e302947Ec7e312fd2384b5a1296099
* **Management safe:** TBD
  * Signer 1: 0xF75a212A5d5c3e208B9694bc854dEa7A942908eC
  * Signer 2: 0xb64baD5e60320a946b76c05Ea07Aff1552B4d27a
  * Signer 3: 0xaC412b86bF26B10D31F531eF1cb80Ef2276f86f2
  * Signer 4: 0xCB2DCf0134686C028E7C1F174be0B53c58c62DBf

### Zodiac Permissions

This [link](https://docs.google.com/spreadsheets/d/1ZU7PZ3HYxEoV2mUBGq5o31yIIOPaSXjRzAd5dnVbZ5M/edit?gid=0#gid=0) provides a list of the protocols and tokens that we propose to be whitelisted to run the outlined strategy at time of writing. As mentioned, this universe of protocols and assets will likely evolve with market conditions—one example being Pendle related positions, which mature at regular intervals and would need a new approval each time a new market with new maturity is launched.

To enhance the operational efficiency we also propose to include two dedicated Enzyme vaults to the approved asset universe (one for growth assets and one for stablecoins), which will utilize the Enzyme protocol to allocate to tokens such as Pendle where relevant addresses change regularly, whereby the Avatar safe would only need to approve said vaults on Enzyme once instead of each individual market into perpetuity. Enzyme is among the most battle-tested protocols in DeFi, with multiple [audits](https://docs.enzyme.finance/general-info/security/audits) since going to mainnet in 2019. If deemed necessary, we are also happy to put a hard cap on Enzyme exposure as a % of the total. When this proposal has passed, we’ll set up the permissioned Enzyme vaults dedicated to this purpose.

Following this proposal, the transactions required to enable the relevant interactions with the listed DeFi protocols will be sent to the Avatar safe signers to execute.

# Next Steps

**1. Community to vote on the proposal to begin the execution phase for management of the Matching Pool, including the set up of the structure and moving the relevant assets.**

**2. Once passed:**
**2.1.** The Avatar and Manager safe addresses will be generated.
**2.2.** Add Avantgarde signers to the Manager safe.
**2.3.** Gitcoin's signers on the Avatar safe then approve the list of permissions for Avantgarde to manage the strategy.

**3. Following the operational set up, MP signers will then send the relevant assets to be managed (listed below) from the [MP](https://etherscan.io/tokenholdings?a=0xde21f729137c5af1b01d73af1dc21effa2b8a0d6) to the new Avatar safe.**
**3.1.** 1590 ETH and 3100 WETH from the MP address to be included in the Avatar safe.
**3.2.** The ETH to be excluded from the above (e.g. which is to remain in the current MP address) are the ~$2.66m in ETH earmarked for GG23 and GG24 as outlined in the proposed Gitcoin Grants 2025 Strategy.
**3.3.** As a side note, since this amount remaining in the MP address is earmarked for a near term cash flow, we would also suggest they are converted to USDC within the MP to reduce the asset liability mismatch in the interim.

**4. Avantgarde to begin executing the MP strategy and putting the assets to work as per [SGTM 002](https://gov.gitcoin.co/t/sgtm-002-avantgarde-x-gitcoin-strategic-asset-management-for-the-matching-pool/19698).**
**4.1.** Once allocated, Avantgarde can begin the periodic reporting cycles for the program.
**4.2.** Avatar safe signers will liaise with Avantgarde on an ongoing basis regarding the upcoming matching pool cash flow needs to be funded from the managed assets.
**4.3.** Avantgarde will raise liquidity in a timely manner to facilitate return of required funds to the MP address as required.


# Voting Options

1. Yes, move 1590 ETH and 3100 WETH from the MP address to the Avatar safe for management.
2. No, do not move funds from the MP address.
3. Abstain.

-------------------------

deltajuliet | 2025-01-31 23:12:57 UTC | #2

I've been part of crafting this proposal (but have no gains that will be realized outside of back to Gitcoin) and I’m confident in Avantgarde’s proposed multisig structure for managing our Matching Pool assets. The 60%/40% split is solidly backed by our simulations, and I’m excited to see how this strategy plays out. It was difficult to decide how/what to diversify, and I'm looking forward to the community’s weigh-in.

I appreciate the clear approach of separating the Avatar and Manager safes and leveraging Zodiac’s role modifiers to keep things secure and efficient. That said, I’d love for our experts and community to take a closer look and validate the methods we’re using with Avantgarde to ensure everything is airtight. cc @ccerv1 @meglister @kyle @owocki 

Overall, I’m in favor of diversifying our assets as outlined and believe this structure will strengthen our Grants ecosystem. I'll vote yes to this.

-------------------------

Avantgarde | 2025-02-03 10:52:40 UTC | #3

Hi everyone,

Following further consideration, we have made a minor update to the proposal to instead use Zodiac Roles Modifier v2 rather than v1 for managing the MP assets via the Avatar safe; mainly due to the improvements in tooling and role management of v2 — including a more intuitive user interface, enhanced call data scoping for granular permission control, and support for advanced logical conditions for complex permission structures. This will help to streamline operations and provide greater scalability for future needs.

Audit reports for v2 are available here: https://github.com/gnosisguild/zodiac-modifier-roles/tree/main/packages/evm/docs

Additional documentation: https://docs.roles.gnosisguild.org

Any questions just ask!

-------------------------

Sov | 2025-02-03 13:17:34 UTC | #4

I appreciate @deltajuliet analysis and share the excitement about this proposal. 

While I'm not positioned to evaluate the technical implementation deeply, the overall structure - mainly the 60/40 split and the security approach with separated safes - appears well thought out.

I look forward to hearing more technical validation from our community experts, but I support this approach.

-------------------------

MathildaDV | 2025-02-05 16:58:07 UTC | #5

Generally very excited to see the momentum created here. Thank you to the @Avantgarde team and @deltajuliet for spearheading this effort. Diversification of the MP has been something that we've wanted to see for a long time, and I believe it's in the best interest of our builders and our program to be responsible around how we manage the funds and to provide longevity and sustainability.

I'm in favour of this proposal, but I echo what others have said here: I would love for others who have less directly involved with this engagement to weigh in on this strategy.

-------------------------

cmurdock | 2025-02-06 13:02:33 UTC | #6

I would vote to approve this diversification and multisig structure. I also look forward to any comments by @meglister and @kyle

-------------------------

meglister | 2025-02-07 14:45:21 UTC | #7

I vote to approve the multisig structure. Appreciate Avantegarde's thoroughness in the proposal and am looking forward to seeing how this performs.

-------------------------

Avantgarde | 2025-02-10 07:32:13 UTC | #8

Thank you @deltajuliet @MathildaDV @Sov @cmurdock @meglister for signalling your support, allowing the proposal to now move to a vote. 

Keen to get going with this and start improving capital efficiency and revenue generated from the MP assets!

-------------------------
