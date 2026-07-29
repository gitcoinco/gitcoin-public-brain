---
id: 19721
title: "[GCP - XXX] YOLLOW.XYZ: Making Public Goods Funding Fun and Accessible"
slug: gcp-xxx-yollow-xyz-making-public-goods-funding-fun-and-accessible
category: citizen-grants
url: https://gov.gitcoin.co/t/gcp-xxx-yollow-xyz-making-public-goods-funding-fun-and-accessible/19721
created_at: 2024-12-09T10:45:57.165Z
last_posted_at: 2025-01-08T17:38:06.773Z
posts_count: 17
views: 3329
like_count: 42
---

# [GCP - XXX] YOLLOW.XYZ: Making Public Goods Funding Fun and Accessible

<https://gov.gitcoin.co/t/gcp-xxx-yollow-xyz-making-public-goods-funding-fun-and-accessible/19721>
wtfsayo | 2024-12-09 10:48:37 UTC | #1

## Summary

This GCP proposes to fund the development of YOLLOW.XYZ, an innovative mobile-first alternative frontend interface for the Allo protocol that reimagines public goods funding through a simple, engaging swipe-able interface. 

By reducing friction in the donation process and making funding more accessible, YOLLOW aims to increase participation in grant rounds and demonstrate Allo's potential as flexible infrastructure.

For this initiative, we are requesting $55,000 USDC (for Phase-I) distributed over 4 months for design/development, infrastructure, and launch costs.

## Abstract

YOLLOW.XYZ transforms public goods funding from a complex transaction into an engaging discovery and donation experience. The platform introduces two core innovations:

1. **Single-Gesture Funding**: Transform multi-step donations into intuitive gestures (inspired by premier match-making Apps):
    - Swipe right to donate $1
    - Super-like to donate $5
    - Swipe left to pass
2. **Story-Driven Discovery**: Present projects through visually engaging cards that emphasize impact and learn from user interactions to create personalized discovery.

Additionally we're targeting broad spectrum of platforms that can benefit from same codebase:

1. Farcaster Frames-V2 (farcaster/warpcast) [Phase I]
2. Mobile Web [Phase I]
3. Native (ios + android) [Phase II]

We're planning to launch (Mobile Web + Farcaster) alongside next quaterly gitcoin round [Phase I].


## Motivation

Allo Protocol needs alternative frontends that unlock its potential in new ways. YOLLOW brings consumer-grade UX innovations—specifically proven card-based interactions(used in matchmaking)—to public goods funding, making donations frictionless for web3 natives while creating an intuitive experience for users that come on-chain for first time.

### Strategic Value for Gitcoin/Allo

- Demonstrates Allo's potential as open infrastructure for on-chain consumer apps
- Tests proven consumer-grade interfaces on web3 infrastructure
- Drives protocol usage through mobile-first approach
- Creates path to engaging mainstream donors through familiar interaction patterns
- Validates Allo protocol's vision as flexible funding infrastructure

## Specifications

### Work Components

### 1. Product Development Stream

- Full mobile web using React Native Web
- Farcaster Frames-V2 Compatibility
- Discovery Algorithm
- Integration with Allo protocol contracts/subgraphs
- Internal DB/KPI Tracking setup
- Authentication via Privy
- Stable-coin payments
- Deep Linking to specific projects / rounds

### 2. Product Design Stream

- Comprehensive Figma designs & branding assets
- Multiple UI/UX variants for User testing
- Landing page & marketing materials
- Micro-donation interface optimizations
- User testing and feedback loops
- Explore Co-marketing initiatives with Gitcoin

### 3. Launch Stream

- Mobile Web deployment
- Farcaster Frames-v2 integration
- User Testing
- Meeting KPIs through Outreach and other Activities
- Launch on Farcaster Frames-v2, Mobile Web

### Technical Architecture

- React Native Web for cross-platform compatibility & maximum code reuse
- Integration with Allo protocol subgraphs for project data
- Privy for seamless web3 authentication
- PostgreSQL for user preferences and analytics

## Roadmap and Milestones

<details>

| Month | Product Development Stream | Launch Stream | Product Design Stream |
|-------|---------------------------|---------------|----------------------|
| 1 | • Project setup & infrastructure<br>• React Native Web repo initialization<br>• Core architecture implementation<br>• Authentication system (Privy)<br>• Basic API structure<br>• Database schema design<br>• Initial Allo protocol integration | • Technical documentation setup<br>• Infrastructure planning & deployment<br>• Farcaster Frames V2 POC<br>• Development environment setup<br>• Analytics implementation<br>• Monitoring setup | • Design system creation<br>• Brand identity development<br>• User research initiation<br>• Initial wireframes<br>• Design prototypes (3 variants)<br>• Landing page mockups |
| 2 | • Donation flow implementation<br>• Transaction batching system<br>• Project discovery algorithm v1<br>• Caching layer setup<br>• Error handling system<br>• Performance optimization<br>• Testing infrastructure | • Alpha testing program launch<br>• Bug tracking system setup<br>• Landing page deployment<br>• Community channels setup<br>• Initial user documentation<br>• Test environment deployment | • User testing (Alpha)<br>• Interface refinement<br>• Animation prototypes<br>• Marketing assets creation<br>• Design system documentation<br>• Accessibility audit |
| 3 | • Full feature implementation<br>• Mobile web optimizations<br>• Farcaster integration complete<br>• Push notification system<br>• Offline support<br>• Beta version deployment<br>• Performance testing | • Beta program management<br>• Support system setup<br>• Documentation completion<br>• Marketing campaign prep<br>• Community moderator onboarding<br>• Launch strategy finalization | • Beta feedback integration<br>• Final UI polish<br>• Launch assets creation<br>• Marketing collateral<br>• Help center design<br>• Tutorial flows |
| 4 | • Bug fixes & optimizations<br>• Performance tuning<br>• Security hardening<br>• Final QA testing<br>• Production deployment<br>• Monitoring refinement | • Public launch execution<br>• Marketing campaign activation<br>• Community engagement<br>• Analytics monitoring<br>• User support scaling<br>• Launch incentives rollout | • Post-launch refinements<br>• User feedback integration<br>• Design iteration planning<br>• Analytics dashboard design<br>• Success metrics tracking |

</details>

### Stream Dependencies & Checkpoints

**Month 1 Checkpoints:**
- Infrastructure & Architecture Sign-off (Dev + Launch)
- Brand Identity Approval (Design)
- Technical Specification Document (All Streams)

**Month 2 Checkpoints:**
- Alpha Release Readiness Review (All Streams)
- User Testing Results Analysis (Design + Launch)
- Performance Benchmark Report (Dev)

**Month 3 Checkpoints:**
- Beta Launch (All Streams)
- Marketing Strategy Sign-off (Design + Launch)
- Security Audit Completion (Dev)

**Month 4 Checkpoints:**
- Production Launch Readiness (All Streams)
- Community Growth Metrics (Launch)
- Performance & Stability Verification (Dev)


## Budget Breakdown

Total Request: $55,000 USDC

### Allocation (Estimates):

- Product Development Costs: $30,000
    - Development Team: $25,000
        - Frontend: $15,000
        - Backend: $10,000
    - Technical Infrastructure: $5,000
- Product & Graphic Design: $15,000
    - Design & UX: $6,000
    - User Testing: $4,000
    - Branding & Graphics: $5,000
- Launch & Marketing: $10,000
    - Launch Incentives: $5,000
    - Marketing & Outreach: $5,000


Exact Allocations to be shared as we progress!

## Success Measures

### Quantitative KPIs

**1. User Engagement**
   - 500+ unique donors within first 3 months
   - 30% user retention rate
   - Distribution: 60% via Farcaster, 40% via mobile web

**2. Donation Metrics**
   - $5,000+ total donation volume in first 3 months
   - Average donation value: $1-$5 per transaction
   - 30%+ conversion rate from install to donation
   - 95% transaction success rate

**3. Technical Performance**
   - < 2s average load time
   - < 3% transaction failure rate
   - 99% platform uptime

### Qualitative Metrics

- User satisfaction surveys
- Project creator feedback
- Community engagement quality
- Platform stability and reliability
- Innovation in UX/UI design

## Benefits

1. **Increased Accessibility**
    - Lower barrier to entry for new donors
    - Mobile-first approach reaches wider audience
    - Simplified donation process increases conversion
2. **Protocol Innovation**
    - Demonstrates Allo's flexibility
    - Pioneers new UX patterns for web3
    - Creates reusable components for ecosystem
3. **Ecosystem Growth**
    - Attracts new donors to platform
    - Increases overall donation volume
    - Improves project discovery

## Challenges & Considerations

1. **Technical**
    - Complex mobile web development with animations
    - Farcaster Frames-V2 integration
    - Discovery Mechanism / Algorithm
    - Deep linking UX
2. **User Adoption**
    - New interaction pattern may face resistance
    - Potential Need for education and onboarding
3. **Resources**
    - Ongoing maintenance needs
    - Server costs and scaling
    - Marketing and user acquisition


## Frequently Asked Questions

<details>
<summary>
Expand
</summary>

| Section | Question | Answer |
| --- | --- | --- |
| **Technical Implementation** | How will you handle transaction fees for micro-donations in Phase I? | • Direct transaction processing on L2:<br>   - Immediate execution of $1 and $5 donations<br>• Using supported L2 network with Allo Protocol's contracts<br>• Near-instant transactions<br>• Minimal L2 transaction costs |
| | How are you integrating with Allo Protocol? | • Direct integration with existing Allo Protocol contracts<br>• Using Allo subgraphs for project data<br>• Leveraging Allo's standard donation flows<br>• No custom smart contracts needed<br>• Following Allo's standard integration patterns |
| | How does Farcaster integration work? | • Mobile web app with minimal additional code:<br>• Activates Farcaster context when opened in Warpcast<br>• Uses Warpcast's built-in authentication<br>• Same core experience as regular mobile web |
| **Launch Strategy** | Why focus on Farcaster for Phase I? | Strategic benefits:<br>• Engaged web3 community<br>• Auto-authentication in Warpcast<br>• Easy Access to large distribution<br>• Lower user acquisition costs<br>• Faster feedback loops |
| | What's the initial target market? | Phase I specifically targets:<br>• Existing Farcaster users<br>• Web3 native donors<br>• Current Gitcoin grant participants<br>• Mobile-first crypto users |
| **User Experience** | How will the Phase I interface work? | Phase I implements:<br>• Swipe right: $1 donation through Allo Protocol<br>• Super-like: $5 donation through Allo Protocol<br>• Project deep-dive on tap<br>• Basic filters and sorting<br>• Transaction history view |
| **Operations** | How will you handle transaction-related support? | Support structure focused on user experience:<br>• Transaction status monitoring<br>• In-app transaction history<br>• Clear error messaging for failed transactions<br>• User-friendly status updates<br>• Documentation for common transaction issues |
| | What are the Phase I success criteria? | Clear 3-month targets:<br>• 500+ unique donors through Allo Protocol<br>• 95% transaction success rate<br>• $5,000+ total donation volume<br>• <2s average load time<br>• 30% user retention<br>• Platform uptime of 99% |
| | How will you sustain the platform after the initial funding? | Post-Phase I Sustainability Strategy:<br>• Revenue from grant round operators integrating YOLLOW interface<br>• Participation in future Gitcoin rounds and ecosystem grants<br>• Collaborations with aligned communities<br>• Implementation of staking mechanism for sustainable operations |
| **Security & Risk** | How do you ensure funds safety in Phase I? | Leveraging Allo Protocol's security:<br>• All transactions through audited Allo contracts/Standard Procedures<br>• No custom smart contract risk<br>• Transaction logs in DB<br>• Clear transaction status updates on UI |
| | What happens if Phase I metrics aren't met? | While we're ambitious with our targets, we believe in adaptability:<br>• Continuous user testing and feedback loops<br>• Iterative improvements based on community input<br>• Flexible approach to feature prioritization<br>• Regular communication with stakeholders<br>• Focus on sustainable, organic growth |
| **Future Development** | How will Phase I inform future development? | Data-driven approach:<br>• User interaction patterns with Allo Protocol<br>• Transaction pattern analysis<br>• UI/UX effectiveness metrics<br>• Community feedback collection<br>• Market fit assessment |

</details>


## Team Composition
- **Plor-** Plor has fifteen years of experience as a developer, backed by a Master's degree in Computer Science. He holds certifications in agile methodologies and DevOps. Over the last few years, plor has been an active member of RaidGuild, contributing to collaborative tech initiatives. Throughout his career, he has leveraged his expertise to optimise software development processes, emphasising efficiency and innovation.

- **Sayonara-**  Sayonara is a designer turned full-stack developer, hailing from India. He is specialised in user experience software development in Web3. His passion are decentralised finance (DeFi) applications, while he successfully driven development for a wide range of decentralised applications. As an active participant of RaidGuild, he currently focuses on stakeholder-driven development in the ever changing landscape of decentralised digital technologies.

- **Anya Biarozka-** Anya is an experienced Art Director and UX/UI & Brand Designer with over 10 years in the industry. Over the past 4 years, she has specialized in Web3, contributing her expertise to projects such as Gitcoin, Acala Protocol, Tableland, Karpatkey, The Sphere DAO, and Deep Work Studio, among others. Recently, she contributed as an Art Director and Visual Designer to the *Gitcoin Onchain Capital Allocation Handbook*.



## Conclusion

YOLLOW.XYZ aims to be an experiment in making blockchain invisible while making public goods funding more accessible and engaging through a consumer-centric approach. By building on Allo protocol, we can focus on innovation while leveraging proven infrastructure. This project has the potential to significantly increase participation in grant rounds and demonstrate the flexibility of Allo protocol as a foundation for diverse funding experiences.

Our initial phase focuses on mobile web and Farcaster Frames-V2, with a clear roadmap for potential native mobile app development in Phase II, ensuring we can iterate and validate our core concept before expanding to additional platforms.

---

Note: By submitting this proposal, we represent and warrant to Gitcoin that all the information it contains is true and complete to the best of our knowledge.

-------------------------

0xZakk | 2024-12-09 17:23:19 UTC | #2

Hey, I'm really excited to see this proposal come through. This is a really exciting project and a STACKED team!

-------------------------

kischiman | 2024-12-10 01:08:55 UTC | #3

Well presented, I'm very excited about this!

-------------------------

tbsoc | 2024-12-11 10:54:56 UTC | #4

Definitely like the approach here and can see the mobile first approach being much more user-friendly for lots of types of people who want to donate to many projects but don't want to have to manually search through the applicants in each round.

-------------------------

masterhw | 2024-12-11 21:59:16 UTC | #5

Love the idea of alternative grants interfaces. Perhaps it can represent good-spirited competition for who can most effectively match donors & worthy projects. Really valuable work, hope to support the team on advising Allo integation.

-------------------------

meglister | 2024-12-12 02:47:22 UTC | #6

This is a cool proposal -- I love the idea of mobile-first innovation!

I'm a little stuck on the investment ($55k) vs return ($5k in donations). What would have to be true to make the return much larger than the investment -- how could we increase donations or make the investment smaller? I'd be thrilled to support a $20k build that we redirect mobile users to for the next QF GG round, see how it goes (even without cool animations!) and determine the next funding steps from there.

Additionally from a UX perspective... we've thought about a swipeable interface and worried about the fatigue that might present given the number (100s) of projects in a grants round. In "traditional"/Tinder-like swiping interfaces, it doesn't matter if the user gets bored and abandons swiping -- they've completed the actions they came there for. However, if a user gets bored and leaves the grants experience, we miss the opportunity to actually collect their donation! Wonder how we might mitigate this or if you've done any testing to disprove the concern?

-------------------------

wtfsayo | 2024-12-12 19:13:58 UTC | #7

Thank you so much for your thoughtful feedback and enthusiasm for this proposal, **Meg**! I really appreciate the opportunity to clarify and expand on a few aspects.

1. **Investment vs. Return**

The **$5k** figure is just one way to measure quantitative returns, and of course, it may vary depending on adoption and usage. However, the core aim of this project is much broader: to renew interest in public goods funding for everyone, make the experience enjoyable, and reduce friction so donating feels like an opportunity rather than a task.

This project also serves as a first-of-its-kind experiment for **Gitcoin's Allo protocol**, paving the way for decentralized, community-built frontends. If successful, it could inspire more developers to build innovative interfaces for Allo, creating a stronger and more diverse ecosystem.

To test and refine the product, we plan to use key events leading up to the next Grants Round, such as **Oasis-On-Chain** and **ETH Denver**, to gather real-world insights. With **Gitcoin's** support, particularly through marketing and social channels, we're confident in maximizing its reach and impact.

2. **Budget Flexibility and Community Support**

While we'd be thrilled to work on this at any level, the proposed budget reflects the resources needed to deliver a polished build. This would allow us to work full-time, stay laser-focused over the next few months, and ensure the final product is something both the Gitcoin team and the community can be proud of.

That said, we deeply value **Gitcoin's** community-driven development ethos. This tool is designed to be adaptable for a variety of use cases—for example, we could see the **Greenpill** network hosting monthly swipe sessions or even **Gitcoin** internally using it to surface innovative ideas through donation as a signaling mechanism.

3. **Swipe Experience and UX Concerns**

Your concern about swipe fatigue is very valid. To mitigate this, we've envisioned features to strike the right balance between helping users fund and discover projects:
 • **Filtering Options**: Users could filter by community rounds or project types, similar to setting preferences in traditional swipe apps.
 • **Budget-Aware Design**: Many donors may come in with a set budget (e.g., **$10–$15**). After they exhaust it, they can decide to continue swiping purely to discover exciting projects or leave the app at their convenience.
 • **Dual Emphasis**: The goal is to make funding and discovery equally seamless, ensuring donors feel they've contributed meaningfully while also exploring innovative ideas.

We've also tested this idea informally with several members of the **Gitcoin** and adjacent ecosystems, and the feedback has been overwhelmingly positive. We're committed to building this in close collaboration with the community to ensure it meets their needs while delivering a fun and impactful experience.

**Closing Thoughts**

Once again, thank you for the thoughtful critique and ideas. We love the suggestion of a phased approach (e.g., a **$20k** MVP) and would happily explore how we can incorporate this to demonstrate the concept effectively while keeping development community-driven.

We're so grateful for your support and feedback—it's invaluable as we shape this project into something meaningful for **Gitcoin** and the broader public goods ecosystem. Let us know how we can continue refining the proposal to align with **Gitcoin's** vision!

-------------------------

owocki | 2024-12-13 03:00:32 UTC | #8

[quote="masterhw, post:5, topic:19721"]
Love the idea of alternative grants interfaces.
[/quote]

who is the target market for this?  how will we get it in their hands?

to me mobile confers that its for embodied cap allo.  how do the constraints differ here?  i think an event (embodied experience) wiould be the right place to bring this to market.

gitcoin is runing schelling point ( https://schellingpoint.gitcoin.co ) on 2/27 in denver.  what would have to be true to scope this down in time/cost and deliver value for schelling point? (as defined by a committte of SP organizers)  i would personally put $5k into the projects matching pool if i had confidence it would be ready for SP and would add value to the event experience

to know this path, i think wed have to do discoveery with the orgs of schelling point (or similar event) to see what kind of embodied cap allo they want to do. hackathons is def one use case.  there might be paritcipator budgeting experments we could do too.  eg vote for which speaker/charity/booth you think is most impactful

i did some light experiementation on some of this years ago https://www.youtube.com/watch?v=0WfCqM-M0_Q

-------------------------

wtfsayo | 2024-12-13 18:38:21 UTC | #9

Discussed above comments internally with the team!

We would love to do a high velocity build 2 months (~9-10 Weeks) targeting Schelling Point (2/27) Denver  with following milestones

1. **Milestone 1:** 
- Checkpoint at Week 4/5
- Frontend app is able to load round specific project cards at yollow.xyz/round-specific-url
- Project Cards are swipable
- Tapping on specific project card shows relevant details (similar to tinder/bumble)
- Demo Swipe Interactions are possible (No transactions yet)
- Low Polished UI
- Uses Regular `Connect Wallet` (recommended to used inside mobile wallet's browser)

2. **Milestone 2**
- Full Transaction Integration with Allo
- Simple Dollar Right Swipe or Zero Dollar Left Swipe
- Users are suggested to sign transaction in batch of $5/$10 multiple based on their appetite
- They can checkout at any point with flexibility of editing amount per project
- Post signing a transaction they can continue in discovery mode (no donation just like/bookmark)
- Users are able to see past donations/bookmarks
- More Polished and Testable UI
- No Farcaster Integration, Mobile Web First

Specifics to be changed as per discovery session proposed with Gitcoin/Allo team

Total Cost: 25000 USDC (misc between design, frontend, backend, QA)

-------------------------

Sov | 2024-12-21 03:38:24 UTC | #10

Chiming in here with my perspectives on this.  As a power user of our tools I could see where enabling mobile first experiences could help in various ways.

Given RaidGuild's strong track record and my experience working with them, I'm inclined to support this team - they don't take on projects without believing in their potential impact. However, while their proposal shows promise for improving mobile conversion, the $25k ask is steep against projected $5k donation volume.  Additionally, the timeline is only for three months.

Given our goals this year revolve around driving increased volumes through our platforms I would suggest that we consider a longer term roadmap from the team showing how they intend to scale the platform usage over 6-12 months.  Based on those estimates maybe we could look at an initial investment to get started and more incentivization via retrofunding over time if there is traction.

-------------------------

peth | 2024-12-23 08:46:59 UTC | #11

Love it!!

At this point, something like this is probably the only way we can get people to actually sift through so many grant programs and support more projects rather than just the ones they are already familiar with.

To those concerned about where will this be used, I‘d suggest integrating this as the official mobile UI for donating on Gitcoin. It could be A/B tested or users could be given choice between "Gitcoin Classic" & the swiping UX - then asked about which they enjoyed more.

It would also be a great way to encourage people to do a bit of donating whenever. No longer have to go through the whole process of scrolling, curating & making a cart. Instead, just open the app, do a few swipes for 5 min while drinking coffee in the morning :person_shrugging:

-------------------------

meglister | 2024-12-23 18:03:42 UTC | #12

Thanks for taking the feedback and revising! I'm in favor of this approach

-------------------------

ccerv1 | 2024-12-24 14:43:11 UTC | #13

This is the third proposal in recent weeks requesting funds to build something new for Gitcoin and/or Allo. For context, here are my responses on the other two recent ones: [Impact Passports and Impact QF](https://gov.gitcoin.co/t/citizen-grants-gcp-impact-passports-and-impact-quadratic-funding-impactqf/19712/5) and [Community Knowledge Base for LLM](https://gov.gitcoin.co/t/gcp-xxx-community-knowledge-base-for-llm/19523/6).

tl;dr - I like the ideas and the teams, but I don't like the principle of funding external teams to build prototypes that haven't undergone any initial user testing. I feel these proposals would be 10X more compelling if they had a working prototype or at least some wireframes. Call me crazy, but this should be a requirement for funding any team proposing something that hasn't shipped yet.

Given this is NOT how we currently do things, let me respond to the substance of the request.

I agree with the problem statements identified by the YOLLOW team, namely, that Gitcoin should be experimenting with new donation interfaces. I also appreciate the push to ship something before ETH Denver. Having skimmed the thread, I can also see that there's been a lot of feedback that the team has responded to wrt to budget and ROI from other stewards. I won't be a blocker, and am willing to vote in support of this proposal provided it maintains the support of Gitcoin's product leadership.

-------------------------

Prajjawalk | 2025-01-03 18:40:35 UTC | #14

@wtfsayo I have been working on quite a similar idea (check out https://donate.doogly.org), and it would be great if we could combine our strengths and collaborate rather than duplicate our efforts. I would be happy to discuss possible synergies.

-------------------------

owocki | 2025-01-06 00:51:08 UTC | #15

Is there a pilot identified for this product?  How big and for whom?  Id be more keen to vote yes if there is a pilot that will deliver some GMV/results in a real world scenario vs a build for a hypothetical end user.

-------------------------

wtfsayo | 2025-01-08 17:37:30 UTC | #16

Ideally want to do next Gitcoin round as target with the amendments last posted!

We have KPIs that are targets that we think would be called success in original prop

-------------------------

wtfsayo | 2025-01-08 17:38:06 UTC | #17

DM me on farcaster or telegram plz

@sayo on fc

-------------------------
