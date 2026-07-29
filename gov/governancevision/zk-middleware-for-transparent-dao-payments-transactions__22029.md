---
id: 22029
title: "ZK Middleware for Transparent DAO Payments / Transactions"
slug: zk-middleware-for-transparent-dao-payments-transactions
category: governancevision
url: https://gov.gitcoin.co/t/zk-middleware-for-transparent-dao-payments-transactions/22029
created_at: 2025-07-19T10:00:26.954Z
last_posted_at: 2025-07-20T07:10:42.952Z
posts_count: 3
views: 1011
like_count: 2
---

# ZK Middleware for Transparent DAO Payments / Transactions

<https://gov.gitcoin.co/t/zk-middleware-for-transparent-dao-payments-transactions/22029>
tobiasocula | 2025-07-19 10:00:27 UTC | #1

Hi all,

I'm building a ZK-powered infrastructure layer that lets DAOs verify grants and payments trustlessly on-chain.

It uses browser-based proof generation and zkSync smart contracts for fully scalable verification of internal transactions (like “the sum of every contribution equals total amount spent,” etc.).

I've just shipped a live demo and I thought Gitcoin may be interested in testing / giving feedback on this project.

I’d love to hear your thoughts or explore ways this could align with your treasury / governance flows.
Here is the demo if you wish to check it out: https://zk-verification.vercel.app/
And this is the GitHub repo storing the frontend logic: https://github.com/tobiasocula/ZK-verification-frontend

I'd love to discuss this further if anyone is interested!
Kind regards and thanks for reading,

Tobias

-------------------------

Sov | 2025-07-19 12:56:42 UTC | #2

Thanks @tobiasocula 

Given the volume of grants (amount of grants + number of grantees) how would you envision something like this be scaled for many transactions and tracking over time?

Also, can you provide some details on what the value add for us (or similar DAOs) in tracking grants in this way?

-------------------------

tobiasocula | 2025-07-20 07:10:42 UTC | #3

Hi Sov,

Thanks for your reply. Using this system, one could verify outgoing payments in an organization (meaning the total amount that got issued is valid for example, without revealing the individual contributions to preserve privacy), because it got verified on-chain, meaning it is completely trustless. All the issuer has to do is interact with the proofing mechanism.
I don't know the situation well enough at Gitcoin, but I can image that in many organizations there is still a part in the grant issuing that is not completely trustless, meaning one must still "trust" the admin for correctly setting up the payment.
For the scaling part, because the system is built on the zkSync L2 chain, which is built to be scalable (or at least a lot more scalable than just the Ethereum L1 chain), so I don't think this will be a problem. The proofing doesn't actually make the payments, it just guarantees that all went well to provide full transparency. One idea could be to build the ZK-proof verification inside the grant issuing itself, such that the proofing happens automatically.
The proofs will then be stored on the blockchain and can just be fetched by making a read-only call.
I hope this clears things up!

-------------------------
