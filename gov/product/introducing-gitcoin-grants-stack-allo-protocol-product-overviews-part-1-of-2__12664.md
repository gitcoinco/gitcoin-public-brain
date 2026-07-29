---
id: 12664
title: "Introducing: Gitcoin Grants Stack & Allo Protocol - Product Overviews (Part 1 of 2)"
slug: introducing-gitcoin-grants-stack-allo-protocol-product-overviews-part-1-of-2
category: product
url: https://gov.gitcoin.co/t/introducing-gitcoin-grants-stack-allo-protocol-product-overviews-part-1-of-2/12664
created_at: 2023-01-24T14:52:17.111Z
last_posted_at: 2023-09-05T18:13:10.028Z
posts_count: 10
views: 13358
like_count: 57
---

# Introducing: Gitcoin Grants Stack & Allo Protocol - Product Overviews (Part 1 of 2)

<https://gov.gitcoin.co/t/introducing-gitcoin-grants-stack-allo-protocol-product-overviews-part-1-of-2/12664>
Viriya | 2023-06-22 17:35:52 UTC | #1

co-authored by @nategosselin, @Viriya & @alexalombardo 

**We're excited to introduce two new Gitcoin products: Gitcoin Grants Stack & Allo Protocol!** *This is foundational reading for anyone learning about our products and Gitcoin's future as a protocol DAO. We welcome comments and feedback as we build in public alongside our community*.

This is the first of a series of intro posts it will detail:

* What is Allo Protocol & its vision as a digital public good
* What is Gitcoin Grants Stack, how it works, and what makes it a key tool for our ecosystem
* A rudimentary overview of our short-term adoption model

First, here’s a snapshot of our current product architecture to really conceptualize what we’re talking about and how it all fits together.

![|624x217](upload://ltpNIu9IkF1iGJSjfnz1HsRSkho.png)

# The Story of Allo Protocol: Rebuilding cGrants from the ground up

The Gitcoin Grants Program has grown immensely since its launch in 2019 — from one matching pool supporting open source to many concurrent pools serving interests as varied as climate, Eth Infra, and DEI. Over that period, we learned that every unique community is going to want to have a similarly unique implementation of their grants program.

There isn’t a single model that is right for every organization, and being able to tweak things like project eligibility criteria or donor matching settings allows the community to dial in the right program for their needs.

Unfortunately, our legacy grants platform (affectionately called cGrants or “centralized grants”) was not designed to allow that level of customization — plus we would be the first to admit that it could no longer handle the scale at which we were operating.

So a decision was made to begin building new tech to improve and scale, not only our own community-led funding efforts (i.e., Gitcoin Grants), but also to support ANY community-led funding initiative at scale.

**Enter Allo Protocol** (formerly known as grants protocol)

Allo Protocol is a digital public good that will act as foundational funding infrastructure for the open web. **It is the first and only open-source, decentralized, modular protocol that enables groups to pool and allocate funds to support their collective goals.**

It was created to empower communities’ growth and evolution by enabling them to scalably fund their shared needs.

Allo Protocol will feature:

* **Democratic Funding Mechanisms:** There is a [huge design space for funding allocation mechanisms](https://gov.gitcoin.co/t/systematic-exploration-of-the-coordination-mechanism-design-space/12616), and Allo Protocol makes it easy for builders to experiment with and iterate on those foundational tools. The protocol will launch with a customizable Quadratic Funding mechanism, and will work with the community to further flesh out that library so communities can immediately benefit from optimal capital allocation.
* **Builder/Project Registry:** Builders seeking funding can create a project profile that’s stored in a universal project registry. They can use this profile to apply to any grants program built with Allo Protocol. In the future, projects will be able to accrue reputation that will streamline grant reviews for teams on both sides of the process.
* **Modularity:** There are a number of key decisions a community needs to make for capital allocation (who’s eligible, who can vote, how much is available, etc) and Allo Protocol is designed to be modular at each of those points. Builders will have the freedom to rapidly solve focused problems, while communities will be able to plug-and-play emergent tools to level up their grants programs.
* **Integrations:** Web3 is constantly innovating, and Allo Protocol is designed for easy integration with a range of tools. A Sybil defense integration with Gitcoin’s Passport Protocol has already been built, and interfaces exist for easy use with payment protocols and more.
* **Permissionless Customization:** Open-source and decentralized, any dev can permissionlessly compose upon and extend its functionality.

### Allo Protocol’s ambitions

We believe the power of humanity is in strong, local communities. Local physical communities have a rich tradition of investing in their own future — building public spaces, schools, business corridors, and other engines of growth.

One of the reasons this is true is that the tools for this kind of decision-making has existed at the town level for centuries: resource pooling through taxes and fundraisers, then fund allocation via city councils, school boards, and so on.

With the birth of the internet, we discovered that physical proximity is only one way to define “local”. Take a glance at any news feed, subreddit, or gaming community and you will see vibrant communities brought together in the neighborhood of their interests and beliefs.

**Allo Protocol’s vision is to unlock the power of these digitally local communities by giving them the rails to begin investing in their own future.**

With this protocol, we envision these modern publics to finally have the library of tools they need to easily pool resources and invest in their own future.

We’re so excited to see what new engines of growth we will build with Allo Protocol.

### Naming Allo Protocol

Finding a name for Allo Protocol was a hot topic in the DAO. We’re grateful for the lively conversation and all of the suggestions shared. If you’re curious about why we ended up with the name “Allo” out of the list of names we explored, check out the [naming summary post by @alexalombardo](https://gov.gitcoin.co/t/discussion-series-evolving-the-gitcoin-brand-naming-our-protocols-products/12500/40?u=viriya) 

**Allo Protocol (formerly referred to as grants protocol) is the protocol layer that enables Gitcoin Grants Stack.**

# Gitcoin Grants Stack

**Gitcoin Grants Stack is a protocol-enabled solution that enables any community to easily create, manage and grow a grants program.**

Built with the Allo Protocol, Gitcoin Grants Stack is the first-ever decentralized, customizable, smart contract-enabled solution that connects grants program managers, project owners and community members to manage and participate in community-oriented grants programs.

Gitcoin Grants Stack enables a streamlined management process for grant program managers–from program setup to application management to funds allocation–making it easy to manage and grow their program. It encourages community members to discover and support new projects in their digital neighborhood. It empowers project owners to seek funding, apply to grants programs, and build their web3 reputation and beyond.

### Gitcoin Grants Stack’s Core Functionality

Gitcoin Grants Stack has three main components that make it possible to manage, discover, donate to, and participate in grants programs.

![|624x249](upload://mdBJ1opjRqHt41vJfxgEMNSYcA8.png)

* **Manager** (formerly “Round Manager”): E*nables program managers to create and deploy a program plus track and manage grantee applications and simplify approvals processes*
  * Ability to receive and approve applications created in Builder
  * Ability to run Quadratic Funding rounds with Passport Sybil Defense
  * Ability to do bulk payouts
* **Explorer** (formerly “Grants Explorer”): *Encourages donor discovery and support of different programs and projects*
  * Ability to browse and discover different grantees within a given Quadratic Funding grants round
  * Ability to donate to different applicants/projects
* **Builder** (formerly “Grants Hub”): *Empowers project owners to create a single profile where they can build reputation and manage applications, and accept direct donations*
  * Project Management:
    * Create a project on any supported chain
    * Edit an existing project (note: edits to a project would only be reflected in applications submitted after the change)
  * Application Management:
    * Apply to a grants round on any supported chain
    * View application status (Approved/Rejected/In Review, or Active)
  * Project Reputation Creation & Verification:
    * Verify ownership of their project credentials (currently just for Twitter & Github)
    * View project stats - See and manage grant rounds they've applied to and/or participated

Additionally, through an **integration with Gitcoin’s Passport Protocol**, it also helps with identifying & protecting from bad actors (Sybils) on the donor and applicant sides, preventing the draining of program funds

For more details on beta functionality and primary marketing audiences, please see the [Gitcoin Grants Stack Marketing Brief](https://gitcoin.notion.site/Grants-Stack-8ee0b8d6b9d24abf8d5f72ca9927734d) [Notion]

## Why is Gitcoin Grants Stack important for the web3 ecosystem?

Gitcoin has a rich history of empowering builders and setting them up to thrive. We want to decentralize, democratize, and scale that superpower.

We believe that one of the ways to do that is by creating open-source, democracy-first tools to enable it. Gitcoin Grants Stack will provide any community with the tools it needs to foster a thriving ecosystem by tapping into their community’s intelligence and democratically funding their most promising builders.

Now that we've tested our stack with alpha rounds with UNICEF, Fantom, and Gitcoin Grants we can feel confident that we can begin to permissionlessly ramp up usage of this tool in Q2!

## Gitcoin Grants Stack & Allo Protocol - how they fit together (+ a sneak-peek into our adoption strategy)

The way we’ve been thinking about how these two products can grow alongside each other can be likened to a familiar protocol-centric ecosystem–Lens

Gitcoin Grants Stack is to Allo Protocol as Lenster is to Lens Protocol:

the app layer to the protocol layer

where end users engage with the app layer and developers engage with the protocol layer.

If you’ve been on the pulse of Lens Protocol, you’ll know that their initial comms push (and therefore adoption strategy) was mostly developer first.

They leveraged great brand marketing to drive interest for their protocol layer. They built out their decentralized social graph by using emotionally-driven movement messaging while simultaneously driving developers to ideate on use cases and build dApps to integrate with Lens protocol.

Internally, we often look to Lens as a wonderful success story in growing its two-sided user base. That’s why we feel it’s worth mentioning that Gitcoin is taking a slightly different approach which is detailed below.

**Below is a rudimentary snapshot of our proposed user adoption approach vs. Lens’:**

<table>
  <tr>
    <th>  </th>
    <th><b>Gitcoin</b></th>
    <th><b>Lens</b></th>
  </tr>
  <tr>
    <td><b>Product Strategy</b></td>
    <td>Gitcoin already has an application with product-market fit (QF grants) and is building a protocol beneath it to support future growth.

Given this, Gitcoin has a clear need to build an improved grant program UX first and foremost.We have a solid MVP use case (Gitcoin Grants) and stoke for scaling the permissionless availability of QF in particular. We need to balance scaling this application while also building the protocol later.
</td>
    <td>Lens is a protocol that does not yet have an application with product-market fit.

Because of this, Lens is dev-first and is focused on attracting devs to its ecosystem to build dApps and additional functionality. They are in a position where they can focus purely on enabling builders.
</td>
  </tr>
  <tr>
    <td><b>Marketing Strategy</b></td>
    <td>Gitcoin has an established brand. Our users are familiar with our ethos and many have already interacted with our products and grants program. 


Less foundational brand work needs to be done in order to build legitimacy. Rather, we need to double-down on marketing highly-functional products with clear value props to ensure that our brand trust is maintained and that we retain user engagement. 

Of course, we will always leverage our brand's klout and build community around our ethos, however we feel that an additional focus on product marketing will be needed to drive adoption of our tools.
</td>
    <td>From the get-go Lens focused on building a movement around the possibilities of decentralized social media. This, paired with exclusive gated access, gave the project an air of mystique. 

The brand’s hype successfully built legitimacy and attracted early users to their registry and devs to their ecosystem.
</td>
  </tr>
  <tr>
    <td><b>DevRel Strategy</b></td>
    <td>Gitcoin’s products (both the Gitcoin Grants Stack dApps and Allo Protocol) were built by internal devs. 

Our first course of action will be to build clear external-facing documentation to enable outsiders to make sense of our developer ecosystem. 

A devrel enablement & community strategy is also being worked on and we will likely start to see fruits of that labour by late S18/early S19
</td>
    <td>Lens’ taking a dev-first strategy meant that their dev engagement strategy was built from the start with an external (dev) audience in mind. 

They quickly cultivated a community of excited builders with high exposure and emphasis on their “dev garden” initiative. </td>
  </tr>
</table>



**In part 2 of this series, we will share a preliminary roadmap and a more fulsome adoption strategy for Allo Protocol.**

-------------------------

alexalombardo | 2023-01-24 19:20:32 UTC | #2

Thank you for this Laura! 

Thinking through the positioning of our "products" - the protocol layer, app layer and the program layer - has helped us to really distill the value proposition and audience relevance for each, enhancing our ability to effectively communicate and align the DAO In our shared product vision and roadmap, and simultaneously help us build stronger marketing and DevRel strategies.

I've never been more clear on the GItcoin product portfolio - what each product does, why each product exists, who each product is for - than I am today.

This is going to also help us with how we think about the individual product identities from a design standpoint, which will only further strengthen our overall market positioning - helping us to drive our mission forward.

Thanks to the GPC team for being such great thought partners as we've hashed this out over the past months!

-------------------------

Viriya | 2023-02-02 10:39:14 UTC | #3

For reference, here's a diagram with the program layer added :) - still a WIP as we evolve the format of Gitcoin Grants. 

![Screenshot 2023-02-01 at 11.06.27 AM|690x346](upload://hQNIrOmoV25vvjEyoaRioAySRCU.jpeg)

-------------------------

michaelgreen06 | 2023-01-25 19:19:01 UTC | #4

Thanks so much for this post! 

It's so nice to have a source of truth as to what things are called and what they do! 

This post also got me super STOKED about what we're doing over here at Gitcoin. 

LFG!

-------------------------

epowell101 | 2023-01-25 19:31:55 UTC | #5

Thanks.  Talk about product marketing!  This is great.

Two questions that linger to me:

**First** - how do the parts of Gitcoin fit together - if they do - to deliver a total product to users?
- for example, I believe MMM played a crucial role in the success of Unicef's round and similarly I know that with every round FDD gets pinged by operators asking for help in protecting their rounds

*The product stack you articulate here so well is pretty much pointless without the pieces that wrap around it to turn it into a solution that programs and communities can use, as you know.*  MAYBE another layer on your layer cake could be useful to highlight those optional components - i.e. the demand creation, communication, and explanation & more from MMM & the deep levels of defense and explanation from FDD and so on (grant ops w/d seem to fit as well?).  

**Secondly** - I would love to have included a pointer or pointers to the code itself.  While DevRel hasn't been all important yet - getting into the habit of expecting a technical audience to also hit our write-ups now and again and giving them some way to dive deeper might be a good idea?

TL;DR - 
1.  Total product > code stack; could / should we add those additional components to the reference write up somehow?
2.  If we are talking code -> show me the code :moneybag:

-------------------------

Viriya | 2023-02-02 10:38:26 UTC | #6

[quote="epowell101, post:5, topic:12664"]
Talk about product marketing! This is great
[/quote]

It is but a start. You ain't seen nothin' yet ;) 

[quote="epowell101, post:5, topic:12664"]
**First** - how do the parts of Gitcoin fit together - if they do - to deliver a total product to users?
[/quote]

I really appreciate this perspective. 
Clarifying question: Are you asking for an outline of our service functions in relation to these software products? If that's the case, our service offering is something we're still in the discovery of. @connor is currently spearheading this work. 
That said, I could do my best to create something in the future that encapsulates marketing, security and even devrel services.

[quote="epowell101, post:5, topic:12664"]
Total product > code stack; could / should we add those additional components to the reference write up somehow?
[/quote]

Funny you mention this, it WAS part of the original diagram but I was asked to take it out for now because the code repos are being amalgamated and tidied atm. I will include it in the diagram of our next post. 

---

Appreciate your thinking here @epowell101, as always. I'm hoping that the initial simplicity of this diagram will help ppl begin to really get the transformation we're undergoing and allow them to make quick sense of what's going on at a high level. Agree that a more in-depth piece of writing (accompanied with a more complete diagram) would further contextualize our efforts. I will put it on my list lol.

-------------------------

PaigeDAO | 2023-02-01 17:47:08 UTC | #7

I love this phrase you used: 
 "vibrant communities brought together in the neighborhood of their interests and beliefs."

So eloquent!  :green_heart:

-------------------------

joaoroeder1985 | 2023-07-02 15:31:38 UTC | #8

Gm guys, im developer web3, im so excited for build together this ecosystem!

-------------------------

gulliverz | 2023-08-28 11:28:20 UTC | #10

Eagerly waiting for the second overview.

-------------------------

Viriya | 2023-09-05 18:13:10 UTC | #11

Thanks for the poke @guilliverz. Given these products are in experimental flux, we actually created a whole new section of this forum to follow along on our product development journey. You'll find updates from our product managers there and links to roadmaps, etc. :slight_smile: 

Check it out here: https://gov.gitcoin.co/t/about-the-product-category/15407

-------------------------
