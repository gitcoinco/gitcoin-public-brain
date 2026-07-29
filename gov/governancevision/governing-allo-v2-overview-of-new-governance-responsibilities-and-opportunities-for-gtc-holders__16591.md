---
id: 16591
title: "Governing Allo v2 - Overview of new governance responsibilities and opportunities for GTC holders"
slug: governing-allo-v2-overview-of-new-governance-responsibilities-and-opportunities-for-gtc-holders
category: governancevision
url: https://gov.gitcoin.co/t/governing-allo-v2-overview-of-new-governance-responsibilities-and-opportunities-for-gtc-holders/16591
created_at: 2023-09-27T16:33:01.127Z
last_posted_at: 2024-04-15T18:22:21.767Z
posts_count: 11
views: 4175
like_count: 24
---

# Governing Allo v2 - Overview of new governance responsibilities and opportunities for GTC holders

<https://gov.gitcoin.co/t/governing-allo-v2-overview-of-new-governance-responsibilities-and-opportunities-for-gtc-holders/16591>
0xZakk | 2023-09-27 16:33:01 UTC | #1

The second version of Allo will be going live on main net [soon](https://gov.gitcoin.co/t/the-path-to-allo-v2). When it does, the Gitcoin community will have a new set of responsibilities: governing a protocol. This has been [a long time in the making](https://gov.gitcoin.co/t/introducing-gitcoin-grants-stack-allo-protocol-product-overviews-part-1-of-2/12664) and I'm excited for what this means for our community.

After launch, we will progressively decentralize control of the protocol from the protocol team to the DAO. The goal of this post is twofold:

1. Educate the DAO on what governing Allo v2 means and what this responsibility entails
2. Outline the roadmap for how this transition will happen

## Governing Allo v2

There are a couple of components to the protocol that will be under the DAO's control.

### 1. Fee switches

The first mechanism within Allo that the DAO will control is the two fee switches built into the protocol. The two fee switches are:

1. A base fee (in Eth) applied at the creation of every pool in Allo
2. A percentage fee applied at the funding of every pool (denominated in the pool's token)

Both of these values will be set to 0 when the protocol goes live on mainnet. @nategosselin and I, as co-leads of the protocol team, will provide further guidance here in the forum as we are talking with people integrating with Allo v2. Ultimately, we will need to "discover" what an appropriate fee will be with our partners and community.

### 2. Upgrades

The protocol is implemented using a proxy contract, so that implementations of the contracts can be upgraded and patched over time. When these contracts are owned by Gitcoin's governance process, updating the underlying implementation contracts for the protocol will have to go through an onchain vote.

The process of governing the design and implementation of updates to the protocol is the [Allo Improvement Process](https://docs.allo.gitcoin.co/overview/allo-improvement-proposals). This process was designed by the Allo protocol team and is modeled off of EIPs from Ethereum and PEPs from Python.

### 3. Approved Strategies

The largest area of governance for the DAO is the list of approved strategies.

The protocol maintains a list of strategies that are "approved," meaning they've been vetted and used by the community building on top of Allo. These strategies are maintained in a list in the Allo core contract (`Allo.sol`). This makes it a lot cheaper and easier to deploy common allocation strategy contracts, which is the case for applications like Grants Stack.

Adding and removing strategy contracts from the list of approved strategies is subject to a vote. The Allo protocol team will work with the community to design a pre-proposal process that ensures new strategies have been audited and are generally applicable to people building on the protocol.

## Progress Decentralization

We will roll out governance of the protocol slowly and follow a process of progressive decentralization. When the audit is finished, the protocol team will announce a launch date. For the launch to mainnet, these parameters will be controlled by a multisig.

Overtime, we will decentralize by transferring these rights to Gitcoin token holders. This will happen through a proposal, where Gitcoin's governance will accept ownership of Allo v2.

### Phase 1: Multi-sig and Temp Checks

For the first 9 months after the protocol launches, we will use a process of off chain temperature checks with GTC token holders and the aforementioned multi-sig to implement changes to the parameters described above.

This is desirable for two reasons. First, Gitcoin as a DAO hasn't previously governed a protocol and we want to build the muscle within this community while offering stability for groups building on top of the protocol. Second, we anticipate that most changes to the protocol will be small tweaks that happen in the first 9 months - things like upgrades and new approved strategies. To maintain the pace that we've been working on, the Allo protocol team will keep these decisions to a multi-sig.

At the time of launch, we expect the total amount of funds flowing through the protocol to be quite low, making multisig ownership at the start a safe option. 


**Ask:** We'd like community input on who should be a signer on this multi-sig

### Phase 2: Token-based voting

As more groups start to use the protocol, more pools are created, and more funds flow through the protocol we will hand governance over to the DAO. This will be important as the number of pools increases and the protocol stabilizes. At that point, we want ownership of the protocol to be under the Gitcoin community.

## Parting Thoughts

The next few months will be exciting as we launch and grow adoption of the protocol. This represents a huge milestone for the team and the Gitcoin community. I'm excited for us all to work together to govern Allo.

Let's go fund some public goods.

-------------------------

Decentralizedceo | 2023-09-27 23:08:28 UTC | #2

Thanks for the insight on the progress and future plans of Allo V2. @0xZakk please regarding Phase 2, is there a specific number or pool amount(in mind) for the protocol to reach before handing the governance over to the DAO?

-------------------------

meglister | 2023-09-28 15:22:34 UTC | #3

This is an exciting milestone -- congrats! I'd love to see power users and people building on top of Allo be signers on the multisig to increase shared ownership/responsibility. Maybe ImpactStream, Endaoment, and Grants Stack could be some of the initial reps?

-------------------------

jon-spark-eco | 2023-09-29 03:27:22 UTC | #4

Congrats to the Allo team! This is a huge accomplishment that should be celebrated. I am excited to see how people will build new strategies on top of it. 

+1 to @meglister 's suggestion to include builders on the multi-sig. I think ImpactStream, Endaoment, and Grants Stack along with a few stewards with large GTC delegation. Maybe ask for volunteers from the top delegates and then a GTC vote to ratify the final signers.

-------------------------

jengajojo | 2023-09-29 07:40:21 UTC | #5

Glad to see this update and excited to see how the community tackles the new governance surface area.

I second the suggestion on having builders on the multi-sig. I'd like to suggest including one or more value aligned stewards not employed by Gitcoin DAO or foundation to also be included in the mix to further the decentralisation agenda. I'm happy to sign up :slight_smile:

-------------------------

0xZakk | 2023-09-29 13:11:49 UTC | #6

Thank you @Decentralizedceo @meglister @jon-spark-eco @jengajojo for your responses!

Our goal early on is going to be to iterate quickly with partners building on the protocol. We'll want to be able to work in quick feedback loops and having too many signers on the multi-sig will likely get in the way of that. How would y'all feel about a phased approach to the multi-sig:

Phase 1: 2/3 multi-sig (first ~3-6 months)
Phase 2: 3/5 multi-sig (next ~3-6 months)
Phase 3: 5/7 multi-sig (last ~3 months)

-------------------------

Decentralizedceo | 2023-09-29 14:07:15 UTC | #7

I think that makes sense in terms of efficiency. A pilot approach will allow for better scrutiny when identifying weak areas that could be improved.

-------------------------

jon-spark-eco | 2023-09-29 15:38:29 UTC | #8

I think the phased multi-sig role out you propose is an excellent way to go and as you noted, adds quickness to the process. Probably obvious but I would want the 3 - Phase 1 signers to have strong security training/practices in place. Things like fresh wallets for signing that are only used for this purpose. A vote on who these signers are would still be good for transparency and DAO buy-in. It might make sense to nominate all 7 signers and have a plan of who is in Phase 1 and then who is added for the following phases. This way, those folks can stay up to date throughout the rollout knowing in the long term they will have this responsibility.

-------------------------

Tuchain | 2023-10-02 16:34:26 UTC | #9

Interesting read. Looking forward to these developments :slight_smile:

-------------------------

jon-spark-eco | 2024-04-11 18:05:41 UTC | #10

Now that it has been ~ six months since this post, I wonder what the current thinking/strategy for the long-term governance of Allo is. Now that Allo has rolled back in with Grants Stack as a part of the Grants Lab, is it being governed internally, or is there a move to community governance of the protocol? Was a 2/3 Safe setup? Is the plan laid out previously by @0xZakk still in play? Thanks in advance for any updates from the team.

-------------------------

meglister | 2024-04-15 18:22:21 UTC | #11

Hey @jon-spark-eco thanks for your comments. The long-term thinking hasn't changed wrt progressive decentralization. Since Allo v2 went live on mainnet in October, we've had one major completed build outside of Gitcoin with several more in the pipeline over the next few months. The multi-sig is still all controlled by fulltime contributors as we've been rapidly deploying across chains and speed of signing is pretty critical at this stage. I'd love to get to a point where the protocol relies less on approvals for new usage (likely some Allo v2.1 changes needed) and we have built an active dev community to shift some responsibility to -- looking at later this summer for both of those, hopefully!

-------------------------
