---
id: 19569
title: "Updating PGN's contract to make funds easier to claim"
slug: updating-pgns-contract-to-make-funds-easier-to-claim
category: pgn
url: https://gov.gitcoin.co/t/updating-pgns-contract-to-make-funds-easier-to-claim/19569
created_at: 2024-10-30T20:29:19.546Z
last_posted_at: 2024-11-16T13:44:03.822Z
posts_count: 2
views: 2970
like_count: 10
---

# Updating PGN's contract to make funds easier to claim

<https://gov.gitcoin.co/t/updating-pgns-contract-to-make-funds-easier-to-claim/19569>
deltajuliet | 2024-10-30 20:29:19 UTC | #1

## TL;DR

PGN is proceeding with its planned shutdown, and we've now developed new contracts to help users claim their remaining funds. Currently, there is approximately $525,000 in ETH and $90,000 in tokens remaining on the network. We're implementing a simple claiming process that will be fully detailed in the PGN Docs, and there's no immediate deadline for claims.


## Remaining Assets

There are approximately $90,000 worth of tokens still on PGN, with $89,415 of this amount being claimable by EOA users. The majority of these funds are in DAI (around $80,000), with additional smaller amounts distributed across GTC, USDC, and USDT. Currently, there are 444 accounts holding tokens on PGN, with nine accounts holding more than $1,000 each in DAI.

The network currently holds 195 ETH, valued at approximately $525,000 at the time of writing. Of this amount, about 149 ETH will be claimable after the shutdown process is complete. 

The remaining ~46 ETH fall into two categories: 
- ~31 ETH already in the process of being withdrawn 
- ~15 ETH in various contracts. 

While some users have already begun withdrawing their ETH, not all withdrawals have been completed. These pending withdrawals can still be processed even after PGN is shut down. 

Additionally, around 15 ETH is distributed across 225 contracts on PGN. All funds from non-Gitcoin contracts, totaling 4.257333 ETH, will be transferred to the [Matching Pool](https://etherscan.io/address/0xde21f729137c5af1b01d73af1dc21effa2b8a0d6) for future Gitcoin Grants rounds.



* ETH: ~195 ETH ($525,000)
    * ~149 ETH claimable
    * ~31 ETH unclaimable, already in the process of being withdrawn
    * ~15 ETH unclaimable, in contracts


- Tokens: ~$90,000 total
   - Mostly DAI (~$80,000)
    * Smaller amounts in GTC, USDC, and USDT
    * 444 accounts total, 9 holding >$1,000 in DAI


## Claiming Process

We're implementing a new contract called BalanceClaimer. This contract will handle the verification and distribution of both tokens and ETH to eligible users. We're also updating the PGN bridges to work seamlessly with the BalanceClaimer contract, allowing for straightforward claim transactions.

Every EOA user will be able to find their address in a merkle tree file that contains all the information needed to execute their claim. We'll provide detailed, step-by-step instructions for this process in the PGN Docs.



* A new BalanceClaimer contract will verify and manage all claims
* Users can check their claimable amounts via a merkle tree file
* Step-by-step instructions will be available in the PGN Docs
* No immediate deadline for claims


## Additional Points



* Balances under $0.01 won’t be included in the claims process, so users with tiny amounts will not be able to retrieve these. 
* Currently, there’s no set deadline for claiming funds, but this might be adjusted if needed in the future.
* Lastly, any NFT assets created on PGN will not be moved to another network.

Detailed instructions for the claiming process will be available soon in our documentation at docs.publicgoods.network. We encourage all users to keep an eye on the documentation for updates and to begin preparing for the claiming process. While PGN's journey as a public goods experiment is coming to an end, we remain committed to ensuring that every user can successfully recover their assets. :black_heart:

-------------------------

NEKO | 2024-11-16 13:44:03 UTC | #2

Thank you for article useful for all our community

-------------------------
