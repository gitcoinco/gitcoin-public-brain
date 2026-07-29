---
id: 18119
title: "Exploring Grants+"
slug: exploring-grants
category: open-discussion
url: https://gov.gitcoin.co/t/exploring-grants/18119
created_at: 2024-02-26T18:02:47.478Z
last_posted_at: 2024-03-09T09:01:53.938Z
posts_count: 5
views: 3491
like_count: 11
---

# Exploring Grants+

<https://gov.gitcoin.co/t/exploring-grants/18119>
owocki | 2024-02-26 18:08:00 UTC | #1

Grants+

# TLDR

1. Gitcoin is focused on Grants right now,
2. but we see a lucrative design space beyond Grants; we call it Grants+.
3. We are exploring this design space ourselves.
4. We are also enabling others to explore the design space in a way that adds value back to Gitcoin.
5. This value proposition will grow over time as more people understand & execute it.

For full context on this post, please read the Gitcoin Rainbow Paper first (link coming soon ™).

# Grants+

We aim to explore the vast potential beyond the familiar territory of Gitcoin centered around grants, venturing into what we refer to as “Grants+”. This ambition involves delving into the non-skeuomorphic frontier of capital allocation.

How do we begin to reason about what we will find in this frontier? How do we evaluate the immense opportunity space and the transformative power it holds?

Reflecting on the internet’s evolution– how innovations like email, instant messaging, social media platforms, and large language models revolutionized information exchange– allows us to envision the possible shifts in our methods of Funding What Matters. The emerging “internet of value” promises to redefine financial transactions and capital distribution, moving beyond traditional grants.

![Screenshot 2024-02-26 at 11.01.16 AM|690x222](upload://45AhkplW1keRy9G0yM5KAIePUDb.png)


Just as we now exchange information in much higher volume and more powerfully than we did before the internet, we believe that Grants+ will offer much higher volume and more powerful ways for ecosystems to do capital allocation or collective action.

# Traversing the Design Space

The basic modules of Allo’s simple core are:

1. **Tokens** being ingested into Allo and [Aqueducts](https://gov.gitcoin.co/t/gitcoin-aqueduct/9684) that get the tokens into Allo.
2. **Registry** - list of projects which could be funded.
3. **Strategy** - how to distribute capital to the projects in the registry.

One way to think about the design space for capital allocation is all permutations of these modules = (sum of all possible aqueducts) x (sum of all possible onchain assets) x (sum of all possible registries) x (sum of all strategies).

A naive way to traverse the design space would be by brute force - e.g. by simply trying all different permutations of modules.

This naive approach would not be efficient. So we do not expect to run campaigns on top of Allo for every permutation of this design space. So how should we traverse the design space?

Viewing design space exploration through the lens of a classic computer science “hill climbing program,” it allows us to reason about the most promising configurations.

Initially, we define our search area as “the sum total of all possible capital allocation configurations,” with our metric for success being “the generation of value for customers.”

By conducting funding rounds on Allo and analyzing the outcomes, we can empirically navigate the design space. This process involves iteratively refining our approach based on what we learn, aiming to reach a higher point within the design space. This OODA loop (Observe, Orient, Decide, Act, repeat) is a formula that we’ve used in the past to mature Gitcoin Grants Stack and the Gitcoin Grants program.

From time to time, we may integrate the latest research from theorists in our network in order to make bigger leaps towards an optimal design.

![|511x315](upload://9W4A9VmnxvE6vA1pqpEU1ukooms.png)

You can [read more](https://gov.gitcoin.co/t/shape-rotators-guide-to-funding-what-matters/17174) about how we’ve explored this design space so far.

# Multiple Local Maximas

The above graphic is misleading, as there will not be one global maxima of “the best possible capital allocation method” possible for all of humanity.

It is likely that there will be multiple local maxima of Allo protocol configurations that work well for specific capital allocation problems.

![|624x579](upload://l0fanVkahXtKh5E00j6ESfHDNOi.png)

By encouraging a plurality of these local maxima to be discovered and available out of the box in Allo, we can build a funding ecosystem in which one mechanism does not become overly dominant. By having a plurality of mechanisms, none of which are dominant, the Allo ecosystem becomes less fragile than it otherwise would.

# Decentralized Exploration of the Design Space

It would not be possible to explore the full breadth of this design space ourselves.

A prime example of this approach in action is EasyRetroPGF.xyz - RetroPGF is a design space pioneered by Optimism, and we have launched EasyRetroPGF.xyz to allow anyone to run an Optimism RetroPGF style campaign in their own ecosystem.

Another example is the streaming Quadratic Funding pilot recently launched by Superfluid. Using this application, which combines the streaming money primitives from Superfluid and an Allo strategy, users are able to run realtime Quadratic Funding rounds.

Because Gitcoin cannot explore the entire design space ourselves, Allo is designed to empower others to navigate this terrain themselves and then collaborate with Allo to share their discoveries with a broader audience.

There are many other builds being built into Allo. We hope to see these as pull requests back into the main Allo repository.

![|624x471](upload://EOcKukZukUtUfYGdl7XLxF0MK8.png)

Our ambition is for Allo to become a pivotal tool for developers integrating capital allocation into their projects. Once the Allo repository becomes a reliable source of audited, well-documented, Allo strategies, we believe there emerges an immense value prop for developers to harness Allo’s capabilities within their own applications.

From the perspective of the Gitcoin network, these developers who are pushing the frontier of capital allocation design space

1. act as decentralized explorers of the capital allocation design space..
2. & have opportunities to align their incentives with Gitcoin’s along the way. This could be through participating in our Citizens Grants program, which utilizes Allo, or by fostering economic interoperability with Gitcoin through other channels.

What OpenZeppelin has done for ERC20/721 contracts, Allo could do for capital allocation. Success in establishing Allo as a hub for these contracts could generate a positive feedback loop: better contracts attract more developers, leading to even better contracts, and so on. This cycle not only enhances the ecosystem's value but also expands the tools and services within the Allo ecosystem, bolstering its network effects and competitive advantage.

For more on this strategy, check out [Allo B2C Strategy](https://gov.gitcoin.co/t/allo-v2-b2c-strategy/17744).

# Gitcoin as attractor

One can think of Gitcoin as an attractor - or gravity well, that attracts new opportunities into it. Every new partner, integration, or other opportunity that enters Gitcoin’s orbit builds momentum to Gitcoin’s social layer, technology layer, or economic layer, and therefore adds to the attractiveness for future opportunities to enter Gitcoin’s orbit.

![|500x327](upload://jSs7SqTLXTrePSAxqN6oBin9yDf.png)

# Reflexively growing

One cool thing about this attractor is how it can grow over time. It can grow reflexively.

Reflexive growth refers to a process where success breeds further success, creating a positive feedback loop that accelerates expansion and influence. This phenomenon is powerful because it can lead to exponential growth and dominance in a market or sector by leveraging initial successes to fuel further advancements and attract more resources.

![|624x299](upload://fE0O6Wditf0MrPDENsdIqw3s5aw.png)

Right now, building on allo is hard. But over time it will get easier (and higher upside) as this cycle generates a network of tools, devs, and other momentum built around it.

One way to think of this is through exponential thinking. Reflexive growth cycles like this can create exponential growth in network utility due to Metcalfe’s law:

![|624x292](upload://4ZlKYAiSCX5MQPIWSnO1ROu0sX0.png)

# Conclusion

In Summary,

1. Gitcoin is focused on Grants right now,
2. but we see a lucrative design space beyond Grants; we call it Grants+.
3. We are exploring this design space ourselves.
4. We are also enabling others to explore the design space in a way that adds value back to Gitcoin.
5. This value proposition will grow over time as more people understand & execute it.

-------------------------

owocki | 2024-03-05 18:38:32 UTC | #2

video version of this post, from my talk at ethdenver =>  https://www.youtube.com/watch?v=P6TFcBEXESk

[![Screenshot 2024-03-05 at 11.38.22 AM|690x409](upload://isyPeY6j1CmnNxGLZT2nC4qmoPh.jpeg)](https://www.youtube.com/watch?v=P6TFcBEXESk)

-------------------------

notthere-2023 | 2024-03-06 10:20:12 UTC | #3

Hi Kevin, I am reading the "The Gitcoin Whitepaper",find something confusing:

![image|690x186](upload://tsfiW6BEdDLTm2YNvLAfeIu1s9c.png)

I interpret this as 76B * 0. 1 = 0.76 B, 76B / 1m * 13 = 988000, which is not able to reach the conclusion. 

Sorry for the disturbance of my comment, I can't find a way to publish posts but am also confused about it.

-------------------------

ccerv1 | 2024-03-07 13:51:24 UTC | #4

Thanks for stress-testing the numbers! I'm the author of the original report, which you can find [here](https://docs.opensource.observer/blog/gitcoin-grants-impact). 

Here's a quote explaining the math:

> According to Electric Capital's 2023 edition of the [Developer Report](https://www.developerreport.com/reports/devs/2023?s=developer-report), the sector has a total of 6,889 full-time open source developers. Meanwhile, more than [$76 billion](https://pitchbook.com/news/reports/q4-2023-crypto-report) has been invested by venture capital firms since 2018 according to Pitchbook. This translates into a return of less than 0.1 full-time developers for every $1M raised in venture capital.

Essentially: 
- $76B invested
- 6889 FT devs retained
- Ratio of $11M spent per FT dev retained
- Equiv. to 0.09 FT dev per $1M

-------------------------

notthere-2023 | 2024-03-09 09:01:53 UTC | #5



Thanks for your reply Carl! I think I misunderstood the meaning of "per funding dollar" here, it makes sense now.

By the way I have tried to translate the whitepaper in to chinese, appreciate your work and insights in those ideas! And want to translate the rainbowpaper next week.

-------------------------
