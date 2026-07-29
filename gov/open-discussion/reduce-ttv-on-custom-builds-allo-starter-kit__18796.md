---
id: 18796
title: "Reduce TTV on Custom Builds -- Allo Starter Kit"
slug: reduce-ttv-on-custom-builds-allo-starter-kit
category: open-discussion
url: https://gov.gitcoin.co/t/reduce-ttv-on-custom-builds-allo-starter-kit/18796
created_at: 2024-05-14T17:49:35.421Z
last_posted_at: 2024-05-14T17:49:35.488Z
posts_count: 1
views: 2783
like_count: 1
---

# Reduce TTV on Custom Builds -- Allo Starter Kit

<https://gov.gitcoin.co/t/reduce-ttv-on-custom-builds-allo-starter-kit/18796>
owocki | 2024-05-14 17:54:42 UTC | #1

# TLDR

* Gitcoin Grants Lab offers two types of partnerships: pre-baked products and completely customized builds.
* The Allo Starter Kit aims to address the tradeoff between customization and scalability by enabling quick creation of fully customized Allo builds.
* A Proof of Concept (POC) demonstrates basic components for an Allo app, with plans for an MVP including UI refinement, documentation creation, and internal testing.
* The Allo Starter Kit has the potential to reduce time-to-value (TTV) for new builds, increase market agility, but open questions remain regarding maintenance, customer demand, breadth of Allo builds, and potential cross-selling opportunities.

# Context

Gitcoin Grants Lab currently has two modalities of customer partnership.

1. We sell you a pre-baked product (QF on Grants Stack, RetroPGF on EasyRetroPGF) which is customizable up to a certain point.
2. We sell you a completely customized product for your build (Arbitrum LTIP, Maci on Allo).

There is an important tradeoff space here.

1. The formerly is only partially customizable but comes with economies of scale because the COGS (costs of good sold) scales sublinearly to the number of customers (after the first one).
2. The latter is completely customizable (increasing the chance of a win at the cost of dev/product/account manager bandwidth) at the cost of COGS scaling linearly with customers.
   1. Note: If we succeed in graduating a product from the latter to the former, then COGS would scale sublinearly.
   2. Thereby, we can currently build custom things only (1) for important customers (2) for large expected value (on a GMV basis) customers or (3) if we think that we can resale the product to another customer.

# The Design Space

The design space can be drawn as:

![|457x401](upload://aMNLeKoyp2kVFu2FZJuHW4QkDxK.jpeg)

# Solving for this tradeoff space.

I think that we can solve for this tradeoff space by creating an Allo Starter Kit that allows anyone to create a new completely customized build within hours (not days/weeks).

Such a tool would reduce the TTV (Time to Value) for new Allo based builds, enabling more strategic agility in our GTM.

## Allo Starter Kit POC

@carlb recently did some exploration of this. He created an Allo UI Component SDK dev kit.

For scope he just did some very basic components to demonstrate

- Components for Discover Rounds & Projects, Details for Round and Project

- Wallet components (connect button) with the configuration Gitcoin / Allo supports/prefers

- Data fetching is happening inside these components so the dev only has to send a query prop to define what data to fetch (only show rounds with specific strategies, sorting, pagination, ...)

- Uses tailwind and can easily be themed with colors and fonts

This is a proof of concept of an app that would enable a developer to create an Allo app from an existing strategy in 10 min.

He Recorded a loom showing it in action:

https://www.loom.com/share/5ad67d683eef4011adf5bb7a86837d8b

Watch this ^^ then continue

## Allo Starter Kit MVP

What would an MVP of this app look like?

1. Design team skin the starter kit in such a way that the components look good.
2. Carl continues to build out Starter Kit.
3. DevRel
   1. Create documentation about how to use the starter kit to create a full webapp in < 1 hour.
   2. Create documentation about how to (1) use existing Allo strategies or (2) create a new Allo strategy in < 1 hour.
 4. Ship it
 5. Start using it internally for important builds we have coming up (MACI for QF, Arbitrum LTIP, or other things on [Megs $50m GMV roadmap](https://docs.google.com/document/d/1zhUsjdaeyImnaECIsVf2hFg2VUmysUhPGYP6efGjOIE/edit)) to realize cost savings for existing projects.
 6. If it works internally, start shipping it to Gitcoin Citizens + broader Gitcoin community (along with a list of requested builds).

# The Design Space in a year

Once the [Grants Stack plugin system is built](https://gov.gitcoin.co/t/opening-up-grants-stack-allo-to-more-community-contributions/17145) and the Allo starter kit has shipped, I think the design space looks like this:

![|624x501](upload://zbQbItu4NmArkUBGC6OOHF37tgx.png)

# Conclusion

By investing in an Allo Starter Kit, we can reduce the TTV of new builds, and therefore strategically increase agility of our go to market with customers.

Though it is not a primary consideration in this document, there are secondary benefits to this investment. This Allo starter kit would complement and accelerate bottoms-up leadership initiatives already in motion such as those outlined in briefs on [Unix Philosophy](https://gov.gitcoin.co/t/gitcoin-could-embrace-the-unix-philosophy-to-create-exponential-innovation/18602).

# Open Questions

1. Once we’ve built something successfully for a customer, who maintains it? How does an app progress from a POC to a fully maintained app?
2. How many customers demand completely custom build outs, vs can be satisfied with our existing toolsets?
   1. Right now we have a goal to go DEEP on Allo GMV in 2024… How BROAD will we need to go on Allo builds to create that?
   2. Can we cross-sell a product suite with enormous agility/breadth to enable further landing + expanding at customers? Does this become a USP for us?

-------------------------
