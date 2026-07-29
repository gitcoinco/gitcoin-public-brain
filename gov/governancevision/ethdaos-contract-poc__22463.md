---
id: 22463
title: "EthDAOs Contract PoC"
slug: ethdaos-contract-poc
category: governancevision
url: https://gov.gitcoin.co/t/ethdaos-contract-poc/22463
created_at: 2025-07-31T19:28:11.986Z
last_posted_at: 2025-11-03T07:19:32.442Z
posts_count: 4
views: 928
like_count: 3
---

# EthDAOs Contract PoC

<https://gov.gitcoin.co/t/ethdaos-contract-poc/22463>
skilesare | 2025-07-31 19:28:12 UTC | #1

I hope this is the right place to put this, if not, feel free to move it.

After wishing and hoping for many years, I finally put code to paper and reached a working PoC of a self-sovereign DAO scalability solution!  

TLDR: Vote gaslessly on controlling cross-evm and Internet Computer assets with your ECR20 tokens(NFTs coming soon). 

Feature Set:
- Deploy a smartcontract that gives you Snapshot like voting on motions, evm transactions, or IC transactions.
- The transactions are auto-executed via threshold-ecdsa, so no one has the private keys. If you make the contract itself the owner then only the DAO can execute transactions against other EVMs and the IC.
- Vote with a simple SIWE transaction...no other accounts needed.
- Votes send a balance proof to the contract for veracity at block X.
- It will all be open-sourced once I can get my security review done.

Here is a quick demo:

https://youtu.be/Jbq0xfrzsPQ

Lots of features to go(Support evm NFTs, Proposal Builder, Quorum, Staking, Following) and lots of polish to do, but as a potential highly aligned user of something like this, I thought I'd take the temperature on how interesting(or not) something like this might be.

This was built on a grant, and if I can prove some broad ecosystem interest, it would help with the next one!  Thanks for your time.

-------------------------

wasabi | 2025-07-31 21:17:16 UTC | #2

As a DAO maxi, i would say, this is very interesting and somehow makes me remember the Zodiac methodology to control Mainnet assets from Gnosis.

-------------------------

skilesare | 2025-08-06 17:13:04 UTC | #3

Thanks for the reference. I'm not too familiar with Zodiac, but after taking a look, this is how I'd say the systems compare:

Zodiac Concepts:

**Avatars** - Each contract that is deployed through EthDAOs gets a theoretically infinite number of EVM addresses that it can use for different purposes.  These addresses are constituted through threshold ecdsa, so the private keys, in a sense, don't exist. 13 or 34 independent node subnets coordinate on signatures,  so you have pretty robust security there without someone running around with backup keys.

**Modules** - If you would like some custom functionality, you can deploy a custom contract with that functionality to your EVM of choice and call transactions there, or program your own Internet Computer canister (rust or motoko) that can itself then have its own set of sub avatars(ecdsa account). So you have a couple of different sets of programmability.  The core functionality is modularized so you can build other tools around it to do additional things either by IC execution proposals, or **automatically via looking for events on othe EVMs** via consensus-based RPC out calls and/or through some other kind of trigger(ie. anytime we recieve funds at X make a proposal to distribute it to Y, Z, Q.)

**Modifiers** - I'm not too sure how this is different than the modules listed above, but I get the sense that it is meant to manipulate any transaction that comes through the system? I'd be interested to know more. It seems like they may be equivalent to the 'settings' for a standardized module?

**Guards** - Our ETHDaos module does let you configure the DAO to only accept evm execution and/or IC execution proposals for preconfigured contracts.  It is certainly an interesting concept to also limit and/or filter the values in those proposals. I'll have to think through how one might set that up, but since IC contracts are upgradeable you can just update the creation hooks for a specific contract/function call and have it throw out things that don't fit.

Most of these things can happen gaslessly and most of the automation(like polling for events through an RPC) can be prepaid by the dao via cycles(which are relatively cheap).  The consensus mechanisms generally provide a much better security threshold than some key or third-party service running in some project's amazon instance.

If you know of anyone on that team who might be willing to speak to me, I'd love to discover some lessons learned and figure out if there is something we can do better/more reliably/more secure.

-------------------------

webx3456 | 2025-11-03 07:19:32 UTC | #4

You got my support because eth Dao contracts must be readable and marked during application and the follow up to be made after the application

-------------------------
