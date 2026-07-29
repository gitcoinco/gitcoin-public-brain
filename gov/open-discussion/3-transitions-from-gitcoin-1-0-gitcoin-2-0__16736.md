---
id: 16736
title: "3 Transitions from Gitcoin 1.0 => Gitcoin 2.0"
slug: 3-transitions-from-gitcoin-1-0-gitcoin-2-0
category: open-discussion
url: https://gov.gitcoin.co/t/3-transitions-from-gitcoin-1-0-gitcoin-2-0/16736
created_at: 2023-10-10T21:11:46.356Z
last_posted_at: 2023-10-10T21:11:46.427Z
posts_count: 1
views: 4858
like_count: 9
---

# 3 Transitions from Gitcoin 1.0 => Gitcoin 2.0

<https://gov.gitcoin.co/t/3-transitions-from-gitcoin-1-0-gitcoin-2-0/16736>
owocki | 2023-10-11 05:12:00 UTC | #1

# TLDR
1. Gitcoin's target market is evolving.
2. In response, Gitcoin is evolving too.  Gitcoin's 3 evolutions are :
![3transitions|690x388](upload://7k6XVh6nEuQa2AelODkmIdCgDud.jpeg)

# Market Evolution

Crypto moves FAST.  We are in a rapidly changing ecosystem. 

My high level read on the changing market (at least the parts that affect Gitcoin) is:

1. The markets we are in *(public goods funding, capital allocation, sybil resistance)* are newly crowded/competitive. 
1. QF doesn't solve for every public goods or capital allocation problem, it is only 1 tool in the toolbox.
1. The markets that Gitcoin is in (*public goods funding, capital allocation, sybil resistance)* require credible neutrality + democratic decision making. As [those things can only be provided by DAOs](https://vitalik.ca/general/2022/09/20/daos.html), Gitcoin is evolving from a company to a DAO.
1. The Ethereum ecosystem is evolving towards a [modular architecture](https://ethereum-magicians.org/t/a-rollup-centric-ethereum-roadmap/4698).  Within the broader Ethereum ecosystem there are now many different categories of sub-ecosystems *(layer 1s, layer 2s, NFT ecosystems, infrastructure DAOs, DeFi ecosystems)*  + many of these EVM based communities have billion $$ treasuries.

In this post, I would like to articulate 3 transitions that Gitcoin is undergoing which are meant to address the changing landscape.

# Gitcoin Evolution

I think these transitions are:

| | Gitcoin 1.0  |   Gitcoin 2.0 |
|---|---|---|
| **1. Architecture** | centralized product  | decentralized/modular protocols  |
| **2. Mechanisms** |  just QF |  many mechanisms (QF/QV/direct grants/many mechanisms) |
| **3. Customer** | for Ethereum  |  for any EVM based community |


## 1. Centralized Product => Decentralized / Modular Protocols

The old platform was a centralized monolith that was unforkable + unmaintainable bc it was so large.

The new platform is a suite of decentralized protocols that follow the [unix philosophy](https://en.wikipedia.org/wiki/Unix_philosophy) of doing one thing thing + doing it well.  And each protocol has a well designed interface that allows inputs from unforeseen programs.

|  Module | One Thing It Does Well  |
|---|---|
| Passport  |  Sybil Resistence |
| Grants Explorer  | Browsing Grants  |
| Grants Builder  |  Building Grants |
| Round Manager  | Managing QF Rounds  |
| Allo Protocol QF Strategy | Quadratic Funding   |
| Allo Protocol QV Strategy | Quadratic Voting   |
| Allo Protocol *x* Strategy | *Capital Allocation Mechanism x* |

If designed well, this ecosystem of tools are "supermodular" - meaning that they produce more value than the sum of their parts.  Each new modular added to the ecosystem adds value to rest of the ecosystem.

![Screenshot 2023-10-10 at 2.03.03 PM|690x434, 75%](upload://e2CGhdUSVanqCvyGWVBbxVmkajd.png)

Modularity means that any of these modules 

1. have concerns that are separated by well-defined boundaries, which makes development of each module easier.
2. can be used as a money lego in other programs.
3. can be forked + extended for new purposes.
4. can be forked + replaced with something better
5. development can be parallel pathed across many modules

Per [this Vitalik post](https://vitalik.ca/general/2022/09/20/daos.html), decentralization means that Gitcoin has
1. credibile neutrality
2. censorship resistance
3. better decision making in a democratic environment (what Vitalik calls concave environments)

## 2. QF => many mechanisms

Quadratic Funding is great.  But it's not the only mechanism for distributing capital.  Even if it was, there are many flavors of QF (plain vanilla, MACI, pairwise, cluster mapping, and many configurations of each of these).

In the past 24 months we've seen the rise of
1. retroactive public goods funding (primarily on Optimism)
2. self curating registries (primarily on Protocol Guild)

With the introduction of Allo v2,  we are embarking on a [Systematic Exploration of the Coordination Mechanism Design Space](https://gov.gitcoin.co/t/systematic-exploration-of-the-coordination-mechanism-design-space/12616).  This means that we'll be exploring

1. different flavors of QF
2. Quadratic Voting
3. Direct Grants
3. Badholeholder based / Retroactive public goods funding
4. Self Curating Registries
5. Conviction Voting
6. Assurance Contracts
7. and [more](https://supermodular.xyz/coordination-mechanisms/)!!

At maturity, Gitcoin's product suite could be a toolbox of capital allocation mechanisms that can handle many different types of capital allocation.   These mechanisms will each do 1 thing + do them well.  

When one purchases a toolbox because they need a screwdriver, it is also nice to have a set of pliers + a hammer right next to it.  When one starts doing capital allocation via Gitcoin's toolset, it'll be easy for them to start with one capital allocation mechanism + then pivot to another.  

## 3. for Ethereum => for any EVM based community


### A. Passport

Last cycle, Gitcoin's sybil resistance toolsuite provided sybil resistance to Gitcoin Grants (which serviced the Ethereum ecosystem).
This cycle, Passport will provide sybil resistance to any EVM based community.

Sybil Resistence enables new mechanisms like Quadratic Voting, Quadratic Funding, UBI, Democratic DAOs, and other use cases that leverage a money lego that provides a source of truth about unique-humanness.

I envision an ecosystem of sybil resistent dapps enabled by Gitcoin Passport.  The larger this ecosystem gets as measured in total sybil resistance, the larger the total amount of sybil resistence available to this ecosystem of dApps.

### B. Grants Stack / Allo

The problem that we were solving with Gitcoin Grants 1.0 was helping the Ethereum ecosystem grow it's ecosystem value. 

Gitcoin Grants augmented the Ethereum ecosystems ESP (Ecosystem Support Program) with Quadratic Funding.  Quadratic Funding on Gitcoin served as a more democratic counterweight to the ESP program.

![Screen Recording 2023-10-10 at 2.33.57 PM|446x390, 50%](upload://bFCjt9EepvdyFPOMSTDJ4MCV9Ks.gif)

In the next cycle, Gitcoin Grants Stack (powered by Allo Protocol) will allow any EVM based community to grow it's ecosystem value.

In the next cycle, Gitcoin Grants Stack (powered by Allo Protocol) can augment their existing grants program (or replace the software upon which it runs).

There are [multiple EVM based communities with multi-million $$$ treasuries](https://deepdao.io/organizations), I think a great outcome of this cycle would be if a majority of those organizations were deploying capital using Gitcoin's suite of tools.


----

Feedback welcome.

-------------------------
