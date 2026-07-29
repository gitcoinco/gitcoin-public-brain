---
id: 17744
title: "Allo v2 - B2D Strategy"
slug: allo-v2-b2d-strategy
category: open-discussion
url: https://gov.gitcoin.co/t/allo-v2-b2d-strategy/17744
created_at: 2024-02-12T19:17:38.783Z
last_posted_at: 2024-03-13T14:37:32.608Z
posts_count: 5
views: 3745
like_count: 16
---

# Allo v2 - B2D Strategy

<https://gov.gitcoin.co/t/allo-v2-b2d-strategy/17744>
owocki | 2024-05-09 22:26:29 UTC | #1

Thanks to @meglister and @0xzakk for proofreading this and providing early feedback

# Allo v2 - B2D Strategy

# TLDR


what OpenZeppelin is to tokens, I want Allo to be for capital allocation

eg when a dev wants an ERC20/ERC721 at a hackathon, they dont write their own. they just pull OZs because they are well documented + high lindy + easy to fork and get running with.

in 2026, when a dev wants to do QF/QV/RetroPGF/Conviction Voting, whatever they dont write their own. they just pull allo's because they are well documented + high lindy + easy to fork and get running with.


# Why

OpenZeppelin maintains a repository of common token contracts for the EVM. This resource is really useful because a developer can pull an audited, well documented, high-lindey, easy to use [ERC20 token contract](https://docs.openzeppelin.com/contracts/4.x/erc20) or [ERC721 token contract](https://docs.openzeppelin.com/contracts/4.x/erc721) off the shelf + deploy it in their app.

OpenZeppelin has created a flywheel of better contracts, which attracts more developers, and that creates better contracts, and so on… (repeat) This flywheel spins + that creates value for the ecosystem. It also creates more qualified customer leads into their for-profit business lines (see their offerings at https://www.openzeppelin.com/ ).

![|624x249](upload://pgGv39xMAE3km4h4COwWng1aK7f.png)

I propose that we create a similar flywheel for Allo v2.

Instead of purely pursuing B2B contracts with high value customers, we should make it easy for any developer to pull an audited, well documented, high-lindey, easy to use capital allocation contract out of Allo v2.

This will create a similar flywheel for Gitcoin as exists in Open Zeppelin. We will create a flywheel of better contracts, which attracts more developers, and that creates better contracts, and so on… (repeat) This flywheel spins + that creates value for the ecosystem. It also creates more tools & services in the Allo ecosystem. This increases Allo’s network effects + eventual impact. It also is a moat against a potential competitor. Once Allo is seen as THE resource for capital allocation, it will make it very hard for any competitor to usurp Allo.

![|624x269](upload://1Vz2w0fGxbvYdz7O7Lk6rPDJ41Q.png)

# What

Instead of purely pursuing B2B contracts with high value customers like the amazing integrations with great partners…, we should make it easy for ANY developer to pull an audited, well documented, high-lindey, easy to use capital allocation contract out of Allo v2.

We should go B2C (or B2D).

This means that the median developer at a hackathon should know about Allo + have resources to support them building a hack with it.

This means that the median engineer at a DAO should be able to pull Allo off the shelf + into their DAO’s capital allocation stack.

# How do?

How do we do that?

Some times we could consider doing.

1. Come up with a B2C GTM Strategy
   1. What is the formal Market Analysis, Value Prop, Positioning of this tool?
2. Gut take: Pareto optimal approach is to focus on Great product, docs, hello-world apps, allocation strategies, and the SDK. These feel like the most immediately high leverage things.
3. Other things we could focus on:
   1. World class docs.
    2. World class developer support.
    3. Easily forkable hello-world apps for common use cases.
       1. QF, RPGF, CV
       2. Bounties, Direct Grants (committee), RFP (committee)
    4. Outbound DevRel
    5. Lots of hackathon sponsorships.
    6. Great product
         1. The permutations of allocation strategies, aqueducts, registries, allowlist options available through allo should allow you to easily configure the most powerful capital allocation tools.
 7. KPIs
     1. Number developers building on allo
     2. Number of apps built on allo.
 8. See also
    1. [Nader Dabits list of what we need ](https://twitter.com/dabit3/status/1748179559663509681)
       1. - good product, reliable network
        2. - great documentation
        3. - clis that are up to date and enable more developer velocity
        4. - easy to access, reliable rpc support
        5. - easy to access developer support channels with fast response times
        6. - reliable testnet / faucet
        7. - quality reference architectures & codebases
        8. - sensible and well organized bounty and / or grants program
        9. - team members available at a small handful of in person events around the work to meet irl
    2. [And here](https://twitter.com/dabit3/status/1745289389566038288)
        1. Table stakes for a successful DevRel program
        2. - Great product & sdks
        3. - Pristine documentation with copy /paste, executable code examples
        4. - Simple developer quickstart guide
        5. - 60 second or less, 0 to 1 CLI app generator
        6. - Accessible & responsive developer support channel(s)

# Open Questions

1. Do we want to pursue this?
2. If so, who should lead it? Someone in Grants Lab? Or is this an ecosystem collective pod?
3. How much budget is appropriate for a pareto optimal appraoch?

-------------------------

Sov | 2024-02-13 01:33:16 UTC | #2

I would be in favor of this.  Finding ways to drive creativity and growth on top of Allo at the edges would be a major unlock.

My sense is that this would require a collaborative partnership with Grants Lab to providing DevRel and product development resources paired with EC providing community engagement and incentive structures via programs like Citizens Grants.

In terms of budget maybe we should look at developing some accessible RFP/RFGs that could be released to the community (with semi defined scope/funding amounts - example below from AGD) or create an inspiration for builders criteria that define some of the ideas we have and let others take those and apply for funding through an open applications process.

https://aavegrants.org/request-for-grants-rfgs

-------------------------

owocki | 2024-03-04 19:08:42 UTC | #4

i LOVE this take

![Screenshot 2024-03-04 at 12.08.35 PM|584x338](upload://Ai1UnMLOPTCzpoeIBHMRmhvWCdf.png)

https://twitter.com/dabit3/status/1763652678222299428

-------------------------

owocki | 2024-03-07 15:07:39 UTC | #5

another good one 

https://twitter.com/binji_x/status/1765565122204860641?s=12&t=X0oQ26a3ezptVAZLp1QFaw

![Screenshot 2024-03-07 at 8.07.33 AM|593x488](upload://oE8CCtvcdcJqmb6N6aJ5hnv5Wy9.png)


this one is part of the culture, cant be prescribed from leadership.

-------------------------

owocki | 2024-03-13 14:37:32 UTC | #6

another one for when we get our stuff together on allo v2/2.1 devrel

[![Screenshot 2024-03-13 at 8.37.09 AM|690x458](upload://tCkRKUl2SXjtap8MAhP0t0DUktV.png)](https://twitter.com/dabit3/status/1767744891155534274?s=46&t=X0oQ26a3ezptVAZLp1QFaw)

-------------------------
