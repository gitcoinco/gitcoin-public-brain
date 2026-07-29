---
id: 19495
title: "Wonderland x Gitcoin - Update"
slug: wonderland-x-gitcoin-update
category: product
url: https://gov.gitcoin.co/t/wonderland-x-gitcoin-update/19495
created_at: 2024-10-08T14:58:25.703Z
last_posted_at: 2024-10-12T05:56:36.263Z
posts_count: 2
views: 2842
like_count: 10
---

# Wonderland x Gitcoin - Update

<https://gov.gitcoin.co/t/wonderland-x-gitcoin-update/19495>
Wonderland | 2024-10-08 14:58:25 UTC | #1

# Wonderland x Gitcoin - Update Oct 8th, 2024
This report aims to keep the Gitcoin community and the DAO updated on Wonderland's work and progress as a strategic partner in the development of the Gitcoin protocol.

![image|690x178](upload://ffvWYpRPXHY4rVXQlXsBEsA84Xm.jpeg)

## **What are we working on?**

The Wonderland team, in collaboration with the Gitcoin team, is focused on two key projects for the Gitcoin ecosystem:

-   **Allo v2.1**: Aiming to improve the core protocol and strategies to increase modularity and composability.
-   **Indexer v2**: Focused on rebuilding the Gitcoin indexer from the ground up, with a better separation of concerns to ensure scalability and forkability.

## **Allo v2.1**

We have improved the Allo protocol in version 2.1 to optimize the developer experience. Previously, creating a strategy required 400 lines of code; now, thanks to reusable components, only 30 lines are needed. This makes it easier for users to create pools (funding campaigns) and interact with them through the improved Allo core. We’ve developed additional tools, such as libraries and extensions, that make strategies more modular, enabling developers to build custom strategies more easily. We have also refactored and optimized existing strategies to take full leveraging of these new tools.

### **Key Improvements**

-   **Strategy tools: Tools** that facilitate the creation and modularization of customized strategies.
    -   [**Base Strategy:**](https://github.com/allo-protocol/allo-v2.1/blob/dev/contracts/strategies/BaseStrategy.sol) Base contract that includes all the “main” actions of a strategy (fund pool, register recipients, allocate funds, distribute funds).
    -   [**Extensions:**](https://github.com/allo-protocol/allo-v2.1/tree/dev/contracts/strategies/extensions) These extensions provide additional functionality to the base strategy, enabling developers to implement more advanced.
        -   **Recipient Extension:** Provides detailed recipient data with a review system.
        -   **Milestone Extension:** Manages milestone-based strategies.
        -   **Gating Extension:** Adds additional logic for customized strategies.
    -   **Libraries**: Strategies for managing voting and calculating the results of a Quadratic Voting or Funding on chain.
        -   Added [QF](https://github.com/allo-protocol/allo-v2.1/blob/dev/contracts/strategies/libraries/QFHelper.sol) and [QV](https://github.com/allo-protocol/allo-v2.1/blob/dev/contracts/strategies/libraries/QVHelper.sol) libraries.
-   **Core and Strategies Improvements:**
    -   [Removed](https://github.com/allo-protocol/allo-v2/issues/574) the requirement for Allo team approval for every strategy
    -   Improved user experience by enabling [batch calls](https://github.com/allo-protocol/allo-v2/issues/592) for registering and allocating to [multiple pools](https://github.com/allo-protocol/allo-v2/issues/585) and managing pool roles.
    -   [Improved usage](https://github.com/allo-protocol/allo-v2/issues/593) of `msg.sender` to allow support for meta transactions.
-   **Strategy Refactoring**:
    -   [Refactored](https://github.com/allo-protocol/allo-v2.1/tree/dev/contracts/strategies/examples) DirectAllocation, D**onationVoting, easy** RPGF**,** QVImpactStream, QVSimple and RFP strategies.

**Note:** We drastically improved the unit tests for both the core and strategies, as well as added integration tests.

### **Current Status**
Allo v2.1 is currently under internal review. Wonderland's security team is performing a comprehensive audit of the contracts and strategies to ensure the highest level of security and reliability. Following that, the testing team will apply advanced fuzzing and symbolic execution tests. Once this process is complete, the protocol will be ready for production.

### **Timeline**
Allo v2.1 will be ready in 1-2 weeks at the time of this writing (pending external audit).

## Indexer V2
We are redesigning the Gitcoin Grants Stack indexer, which was originally built to index/query cross-chain grant data across the Allo ecosystem. It currently faces design limitations such as dependency on external vendors, scalability problems, and it was also not built for a multi-mechanism future. Indexer v2 addresses these issues through a modular architecture that improves flexibility and scalability while maintaining compatibility with existing data.

We are in the early stages of this project, finalizing the technical design. We will soon share the specifications of the new design with the community.

### **Timeline**
We estimate having the Indexer V2 ready in Q1 2025. We'll also have an MVP ready by the end of this year.

## **Next Steps**
We are excited to continue working alongside the Gitcoin team. In the coming months, we will provide further updates. Any feedback from the community is welcome!

-------------------------

free2ride19 | 2024-10-12 05:56:36 UTC | #3



"Exciting updates! Looking forward to Allo v2.1's release in the next 1-2 weeks. The redesign of the Gitcoin Grants Stack indexer (Indexer V2) sounds promising, addressing scalability and flexibility issues.

Key takeaways:

- Allo v2.1: 1-2 weeks
- Indexer V2: Q1 2025 (MVP by end of 2024)
- Modular architecture for improved flexibility and scalability

Appreciate the transparency and community involvement. Keep us posted on progress!

Questions:

- Will Indexer V2 support additional chain integrations?
- How will the new design impact existing grant data?

Eager to provide feedback and collaborate."

@free2ride19

-------------------------
