---
id: 25152
title: "Ethereum Has ENS for People. What About Everything Else?"
slug: ethereum-has-ens-for-people-what-about-everything-else
category: open-discussion
url: https://gov.gitcoin.co/t/ethereum-has-ens-for-people-what-about-everything-else/25152
created_at: 2026-03-04T20:03:51.930Z
last_posted_at: 2026-03-31T11:37:11.806Z
posts_count: 9
views: 159
like_count: 13
---

# Ethereum Has ENS for People. What About Everything Else?

<https://gov.gitcoin.co/t/ethereum-has-ens-for-people-what-about-everything-else/25152>
carlb | 2026-03-04 20:03:52 UTC | #1

# **Ethereum Has ENS for People. What About Everything Else?**

## The Problem

Ethereum has ENS for addressing people. But what about everything else?

A GitHub repository. An npm package. A DNS domain. A YouTube channel. These are the entities that build, maintain, and power the internet — and none of them have an Ethereum address.

This creates a problem that every funding protocol has solved independently:

* **Drips** built a custom oracle to map GitHub repos to addresses.
* **Gitcoin** maintains its own project registry.
* **Every new protocol** that needs to send money to “the maintainers of react” has to build another bespoke system from scratch.

We’ve been building the same plumbing over and over. It’s time for a shared primitive.

## The Solution: Two Companion ERCs

We’ve submitted two ERCs ([PR #1580](https://github.com/ethereum/ERCs/pull/1580)) that solve this at the protocol level:

### ERC-8182: Off-Chain Entity Registry

A single, shared registry that maps off-chain identifiers to Ethereum addresses.

```
ownerOf(keccak256("github", "ethereum/go-ethereum")) → 0xabc...
```

That’s it. One call. Any protocol, any agent, any dapp can resolve any off-chain entity to an Ethereum address — permissionlessly, on-chain, with no API keys or trusted backends.

Ownership is proven through pluggable verifier contracts. Today, that means oracle-signed proofs. Tomorrow, it means zero-knowledge verification (zkTLS, DNSSEC). The registry doesn’t change — only the verifiers upgrade.

### ERC-8183: Claimable Escrow

The registry solves *who owns what*. The escrow solves *how to pay them before they show up*.

Every identifier in the registry has a **deterministic deposit address** — computable by anyone, before the entity has ever touched Ethereum. Fund `github:org/repo` today. The maintainers claim it whenever they’re ready.

This means a grants protocol can allocate funding to every dependency in a project’s supply chain in a single transaction, without any of those maintainers having registered first. The money waits for them.

## Why Now: The Agent Moment

This infrastructure was always needed. But the rise of AI agents makes it urgent.

An agent instructed to “fund the maintainers of react” needs to:

1. Resolve the identifier to an Ethereum address
2. Compute a deposit address if nobody has registered yet
3. Transfer tokens — in one transaction, with no human coordination

Without a shared registry, every agent framework would need its own identity resolution backend. That’s the fragmentation problem all over again, but at machine scale.

With these ERCs, any agent, any framework, one `ownerOf` call. Entity resolution becomes a solved problem.

## Design Philosophy

**Minimal surface area.** The registry is a pure mapping — it holds no funds, charges no fees, has no privileged operators beyond verifier governance.

**Pluggable verification.** The `IVerifier` interface is a single function: `verify(id, claimant, proof) → bool`. It supports oracles today and ZK proofs tomorrow, with zero changes to the registry.

**No transfer function.** Changing the registered address requires revoking and re-claiming with a new proof. Ownership is always tied to verified control of the off-chain entity — not to whoever holds a private key.

**Architecturally independent.** The registry and escrow are separate ERCs. Protocols that only need identity resolution depend on the registry alone. The escrow is optional — and replaceable.

## The Path to Canonical

ENS became canonical because it was a single deployment that every wallet, dapp, and block explorer integrated. We’re building for the same outcome:

1. **Standard first** — the ERCs establish the interface
2. **Single deployment** — one registry per chain, a shared Schelling point
3. **Early integrations** — protocols that already need entity resolution (Gitcoin, Drips, and others) adopt the shared primitive instead of maintaining their own
4. **Agent adoption** — agent frameworks integrate `ownerOf` as the default resolution layer

The code is written. The [reference implementation](https://github.com/carlbarrdahl/ethereum-canonical-registry) includes the registry, oracle verifiers for GitHub and DNS, the escrow module, a TypeScript SDK, and backend signing services.

## Get Involved

* **ERC PR:** [ethereum/ERCs#1580](https://github.com/ethereum/ERCs/pull/1580)
* **Reference implementation:** [ethereum-canonical-registry](https://github.com/carlbarrdahl/ethereum-canonical-registry)
* **Discussion:** [Ethereum Magicians](https://ethereum-magicians.org/t/erc-8182-off-chain-entity-registry-erc-8183-claimable-escrow/27899)

We’re looking for feedback on the verifier interface, the identifier scheme, and which protocols should integrate first. If your project addresses off-chain entities — or if you’re building agents that need to resolve them — we’d love to hear from you.

---

*Carl Barrdahl builds funding infrastructure in the Ethereum ecosystem. Previously: EasyRetroPGF (Gitcoin), Allo Protocol, DeepGov.*

-------------------------

ivanmolto | 2026-03-04 22:35:05 UTC | #2

[quote="carlb, post:1, topic:25152"]
This means a grants protocol can allocate funding to every dependency in a project’s supply chain in a single transaction, without any of those maintainers having registered first. The money waits for them.

[/quote]

**Hey Carl,**

I love the idea and the technical approach, but I'm concerned about the legal and tax implications.

The fact that a grants protocol can allocate funding to every dependency in a project's supply chain in a single transaction—without any of those maintainers having registered first—means we're essentially assigning wallets to people or entities who haven't opted in. They may not even want crypto donations.

In Europe, MiCA requires that under certain terms you identify the recipient of your transactions. This could mean that as a donor, you're creating a taxable event for recipients without their consent. How do you deal with this?

-------------------------

carlb | 2026-03-05 09:05:02 UTC | #3

Hi Ivan,

Great question! The important distinction here is: funds aren’t sent *to* anyone, they are locked in an escrow *for* an entity identifier. No wallet is assigned, no transfer occurs. The entity must actively claim (proving control of the identifier) before any movement of funds. Until then, it’s a conditional commitment, not a transfer.

Compare to airdrops hitting wallets without consent, here nothing moves until the recipient opts in.

Does that address your concern, or do you see gaps I’m missing?

-------------------------

ivanmolto | 2026-03-10 13:23:23 UTC | #4

Sorry, Carl, for not replying sooner, and thank you for the clarification — much appreciated. That's very cool.

From a capital-efficiency perspective, how long are the funds kept in escrow while waiting for a potential opt-in from the recipient/entity identifier? If the potential recipient does not opt in, are the funds returned to the donor (after a cooldown) period?

Also, while waiting to be withdrawn by the grantees, do these funds remain idle, or do they generate any yield? Thanks

-------------------------

carlb | 2026-03-18 18:47:40 UTC | #5

@ivanmolto these are great questions! Currently there is no mechanism to handle these cases. Any suggestions are very much welcome!

-------------------------

1a35e1 | 2026-03-18 19:08:07 UTC | #6

Hey @carlb We build a spec such that we can tag other entities on ENS pretty easily. We are just about to start talking about it but since this thread was so on the nose I felt it was pertinent to share.

We are also working with @Sov to expand how this expands to `Grant`,  `GrantProgram` , `GrantRecipient` so we can encode this type of information easily.

 *Please see `https://ens-metadata-docs.vercel.app/`*  also happy to chat more about how your use cases could be represented on ENS.

-------------------------

carlb | 2026-03-18 19:33:36 UTC | #7

hey @1a35e1, thanks for sharing! Interesting work on the metadata spec.

I think we’re solving different ends of the same problem - ERC-8185 resolves off-chain identifiers (GitHub repos, npm packages, domains, bluesky, etc) to Ethereum addresses. Your metadata layer enriches those addresses with structured context.

Would love to hear more about how the Grant/GrantProgram/GrantRecipient schemas work. Happy to chat!

-------------------------

1a35e1 | 2026-03-19 11:35:54 UTC | #8

I can’t seem to DM. I’m `x1a35e1` on TG.

-------------------------

eliottreich | 2026-03-31 11:37:11 UTC | #9

This hits exactly right for the agent infrastructure problem. As agents become economic actors in their own right, they need the same resolution primitives that humans have. The composability angle is key — any agent or protocol should be able to call ownerOf() and resolve identities autonomously without custom integrations.

-------------------------
