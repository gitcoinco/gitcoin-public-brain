---
id: 14174
title: "[GCP-010] Evolving Gitcoin Grants: The Q.E.D. (Quadratic Experimentation and Development) Program"
slug: gcp-010-evolving-gitcoin-grants-the-q-e-d-quadratic-experimentation-and-development-program
category: governance-proposals
url: https://gov.gitcoin.co/t/gcp-010-evolving-gitcoin-grants-the-q-e-d-quadratic-experimentation-and-development-program/14174
created_at: 2023-04-26T17:47:02.994Z
last_posted_at: 2023-06-22T16:55:42.772Z
posts_count: 20
views: 6389
like_count: 103
---

# [GCP-010] Evolving Gitcoin Grants: The Q.E.D. (Quadratic Experimentation and Development) Program

<https://gov.gitcoin.co/t/gcp-010-evolving-gitcoin-grants-the-q-e-d-quadratic-experimentation-and-development-program/14174>
Joel_m | 2023-05-08 10:59:46 UTC | #1

*How can Gitcoin leverage the lessons learned from its past experiments to address the limitations of the current Quadratic Funding model and refine it for future applications?*

*Given the multiple cohorts which exist and commit extractive and exploitative attacks on Gitcoin Grants and our Web3 partners, what novel solutions can Gitcoin explore to enhance the security and fairness of the Quadratic Funding model?*

*In the pursuit of next-generation allocation mechanisms, how can Gitcoin ensure a more representative and pluralistic environment for its Grants Programs and QV governance models?*

We present the Q.E.D. (Quadratic Experimentation and Development) program, which aims to answer those questions through the development and implementation of collusion-resistant Quadratic Funding mechanisms for Gitcoin Grants. The project lead for Q.E.D. has [developed state-of-the-art collusion-resistant QF mechanisms](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4311507) in collaboration with [leaders in the field](https://www.microsoft.com/en-us/research/people/glenweyl/), and brings to the table an ability to rigorously understand the unique needs of Allo Protocol. Q.E.D.'s aim is to create a more inclusive and democratic funding model that addresses collusion and improves the efficiency and fairness of the funding process, as well as to educate our prospective and current partners about the trade-offs that can be made in their own Allo use-cases.

# Proposal

We propose to deliver the following:

1. A tailored mathematical framework for understanding QF within Gitcoin’s context.
2. Empirical analysis of collusion-resistant mechanisms using Gitcoin Grants data.
3. Product roadmap with recommendations for data collection practices and Gitcoin Allo/ Passport feature analysis.
4. Series of articles for marketing, educational, and onboarding purposes.
5. Bi-weekly updates to the Gitcoin community.

# Personnel and Funding

The Q.E.D. project will be led by Joel Miller (that's me!), a Computer Science PhD student at the University of Illinois, Chicago, who brings a wealth of expertise in algorithmic game theory/mechanism design, algorithmic fairness, and the socio-political aspects of technology. Joel has previously collaborated with Erich and Glen Weyl, the inventor of QF, as the lead author of a [paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4311507) on collusion-resistant QF. This paper established a flexible framework for understanding collusion in QF and presented a new collusion-resistant mechanism currently utilized in the RadicalxChange [web app](https://pluralvote.radicalxchange.org/).

Erich (@erich) has been involved in community-building, research, and tooling efforts related to Quadratic Voting and Funding since 2019 and currently works as a product manager with the Gitcoin Passport workstream. Collaborating closely with Joel, Erich's contributions will help drive towards actionable product outcomes of the Q.E.D.

Alex (@ale.k) from Public Goods Funding will contribute her expertise as a data analyst with experience in on-chain identity analysis and unique insights into product experimentation design. Alex will offer invaluable support to the Q.E.D. team.

Furthermore, Kevin Olsen (@kevin.olsen), Gitcoin's VP of Engineering, will serve as the partnership champion to ensure that the Q.E.D. program is executed with academic rigor and technical excellence. Kevin's extensive experience within Gitcoin's engineering team will be instrumental in facilitating a strong partnership and enabling seamless integration of proposed changes into Gitcoin's products. By fostering open communication and collaboration between the Q.E.D. team and Gitcoin's product and engineering leaders, Kevin's involvement will help address potential challenges and roadblocks during the implementation process.

The entirety of the budget will go to staffing funding ($9,080 a month for three months, or $27,240 total), which will be allocated to Joel, who will play a crucial role in developing and implementing the collusion-resistant QF mechanisms. $9,080 a month is the exact amount they earned working on the same problem last summer with Glen Weyl. All other costs (e.g. software licenses) will be covered out-of-pocket.

# Technical Specification

Here's a detailed account of our planned methodology. Our goals can be broken into three interrelated components:

1. Custom-tailored Mathematical Framework: The Q.E.D. program will develop a micro-economic model describing the QF process (including agent behavior and funding outcomes) and a well-defined set of desiderata for measuring collusion resistance relative to that model. Unlike previous research, which either presented under-specified or general models/definitions of collusion resistance, we aim to create a framework specifically designed to capture Gitcoin's unique needs and circumstances. This will allow us to reason about QF with clarity and better predict the outcomes of various mechanisms (such as those listed [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4311507) and [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763)).
2. Empirical Analysis: The program will conduct an empirical analysis of collusion-resistant QF mechanisms using real-world Gitcoin Grants data. This analysis will help us understand how these mechanisms behave in the GitCoin ecosystem and develop new techniques for evaluating them. We plan to explore techniques inspired by work on [counterfactual fairness](https://arxiv.org/pdf/1703.06856.pdf), which will allow us to reason about outcomes even in the absence of ground-truth data about coordinated attempts to manipulate results. No additional PII will be kept or maintained through this program and all potentially identifying information will be subject to a 64-bit hash prior to ingestion/transmission.
3. Implementing and Developing Collusion-Resistant Measures: Based on the mathematical framework and empirical analysis, the Q.E.D. program will provide practical recommendations for implementing collusion-resistant measures in Gitcoin's QF product. This includes suggestions for data collection practices, Gitcoin Passport operation, and the actual QF mechanism, ensuring a more robust and secure funding process. Currently, the most promising collusion-resistant mechanism is Connection-Oriented Cluster Match, developed by Joel and Glen Weyl (see section 3.2 [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4311507) for details). The technical work outlined above will help us adapt that mechanism for the Gitcoin ecosystem. Our work will also explore the development of new mechanisms in addition to this promising initial direction..

# Benefits

Funding the initial trial period of the Q.E.D. program offers several key benefits that will positively impact Gitcoin’s community and reinforce its position as a leader in public goods funding. These core benefits include:

1. Improved Collusion and Sybil-resistance: By developing and implementing collusion-resistant QF mechanisms, the Q.E.D. program will make the funding process more robust, secure, and resistant to manipulation, ensuring a fair distribution of resources to the projects who show the most grass-roots support among diverse communities.
2. Enhanced Trust and Adoption: The introduction of a more equitable and transparent funding model will instill trust among the Gitcoin community members, funders, and stakeholders. This increased trust will lead to greater adoption of the Gitcoin platform and attract more participants to contribute to public goods projects.
3. Inclusive and Democratic Funding Model: The Q.E.D. program promotes a more pluralistic QF mechanism that incentivizes cooperation across social differences. This fosters a more inclusive and democratic funding model, resulting in a diverse and vibrant Gitcoin ecosystem that supports a wide array of projects and initiatives.
4. Driving Innovation: By allocating resources more effectively and fairly, the Q.E.D. program will help drive innovation within the web3 ecosystem, fueling the development of groundbreaking projects and technologies that contribute to the greater good.
5. Collaboration with Researchers and Practitioners: Joel and Erich have close ties to other leading experts in the field of Plurality. While we can’t promise anything from those not directly involved in the Q.E.D. program, these connections will likely allow us to leverage outside expertise to create a more effective and equitable QF mechanism, while also encouraging a culture of open collaboration and intellectual curiosity within the Gitcoin and web3 communities.

Through these benefits, the Q.E.D. program aims to create a more resilient, fair, and economically optimal funding model for Gitcoin Grants. This comprehensive approach will not only address the existing limitations of the QF model but also contribute to the long-term growth and sustainability of the Gitcoin ecosystem.

# Drawbacks

While the Q.E.D. program offers several significant benefits, it is essential to consider some drawbacks and challenges that may arise from its implementation:

1. Cost Factors: Implementing the Q.E.D. program requires funding to cover staffing costs, which amount to $27,240 in USDC. These costs must be weighed against the potential benefits and long-term impact of the program.
2. Data Privacy Concerns: Developing collusion-resistant QF mechanisms may require collecting additional user data, potentially raising privacy concerns among Gitcoin community members. It is crucial to balance the need for data collection with maintaining user privacy and ensuring compliance with relevant regulations. As stated above, no additional PII will be kept or maintained through this program and all potentially identifying information will be subject to a 64-bit hash prior to ingestion/transmission.
3. Complexity and Integration Challenges: The Q.E.D. program entails the development of new mathematical frameworks and empirical analyses, which may increase the complexity of Gitcoin's existing systems. Integrating these new components into the platform may present challenges and require close collaboration with product and engineering leaders. Additionally, barring technical challenges, the choice of whether to integrate our proposal will be left to a future decision.
4. Execution Risk: As with any project that involves research and development, there is a risk that the proposed collusion-resistant mechanisms may not deliver the expected results or face unforeseen challenges during the implementation phase. It is essential to monitor progress closely and adjust the approach as needed to ensure the program's success which is why we will give bi-weekly progress updates to the GitCoin community.

# Vote

We invite the Gitcoin community to vote on the implementation of the Q.E.D. program to develop and integrate collusion-resistant QF mechanisms into the Gitcoin Grants platform. Your vote is important to determine the direction and priorities of the Gitcoin ecosystem.

*To be clear: a "yes" vote for this project is not a vote to change Gitcoin's core QF algorithm. It's a vote to fund R&D aimed at giving Gitcoin a button it could press to change the core QF algorithm.*

Voting "Yes": By voting "yes," you support the implementation of the Q.E.D. program. This includes allocating the necessary funds for staffing costs ($27,240 in USDC), as well as the commitment to collaborate with leading experts in the field to ensure the program's success.

Voting "No": By voting "no," you indicate that you do not support the implementation of the Q.E.D. program at this time, either due to concerns about costs, potential drawbacks, or other factors. This would mean that the core logic of the current QF mechanism would remain unchanged, and the resources allocated for this proposal would not be utilized for the Q.E.D. program.

To cast your vote and share your opinion, please visit Snapshot (link pending responses from Stewards).

-------------------------

ale.k | 2023-04-26 18:03:44 UTC | #2

Very excited for the scope of this research to create anti-collusive systems.

As a product of @Joel_m's work, we are very hopeful for the modifications to core Allo Protocol which will result from a thorough examination of the existing QF/QV techniques.

-------------------------

kevin.olsen | 2023-04-27 09:03:28 UTC | #3

This is a very exciting proposal, and it has my full support. 

Beyond the explicit outputs laid out in this proposal, I'm additionally excited as this proposal demonstrates the Gitcoin DAO's shift to directly funding research and investing in the exploration of the frontiers of our core Quadratic Funding mechanism.

Great work. LFG.

-------------------------

erich | 2023-04-27 09:27:10 UTC | #4

I had the pleasure of collaborating with @Joel_m last year on the [collusion-resistant QF paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4311507) with Microsoft Research and the [corresponding RxC prototype](https://pluralvote.radicalxchange.org/) with RadiclaxChange Foundation. Joel is a remarkable collaborator and an excellent choice to lead this program, given his contributions to the [Plurality](https://www.radicalxchange.org/media/blog/why-i-am-a-pluralist/) paradigm. I believe that QF applications must reflect the vibrant dynamics and interconnectedness of communities, rather than relying on assumptions about isolated and rational agents. I fully support Joel's proposal and wish him all the best. :-)

-------------------------

DisruptionJoe | 2023-04-27 16:54:22 UTC | #5

I'm very excited to see this move forward! Thanks for a well thought out proposal targeting a critical need.

-------------------------

schultztimothy | 2023-04-27 16:55:57 UTC | #6

This is super exciting! I'm especially bullish on increasing educational efforts around QF

-------------------------

OffroadStudios | 2023-04-28 00:47:12 UTC | #7

full support, great proposal !!!!

-------------------------

azeem | 2023-04-29 03:19:35 UTC | #8

Fundamentally believe QF is going to be one of the major ways forward for Gitcoin even as we work on other things, so I'm definitely in favor of seeing this exciting research move forward.

-------------------------

owocki | 2023-04-29 14:53:22 UTC | #9

[quote="Joel_m, post:1, topic:14174"]
Currently, the most promising collusion-resistant mechanism is Connection-Oriented Cluster Match, developed by Joel and Glen Weyl (see section 3.2 [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4311507) for details).
[/quote]

Joel just appeared on the GreenPill podcast to talk about this work. In case it’s helpful, here is the episode https://youtu.be/ueQDnq-J2mY

-------------------------

ccerv1 | 2023-05-01 15:36:37 UTC | #10

I had the pleasure of speaking with Joel last month and am very enthusiastic about this work. I will be voting **YES**.

Some comments on a few of the deliverables:

[quote="Joel_m, post:1, topic:14174"]
Series of articles for marketing, educational, and onboarding purposes.
[/quote]

I'd love to see a one sentence / one paragraph / one thousand word summary of interesting findings.

[quote="Joel_m, post:1, topic:14174"]
Empirical analysis of collusion-resistant mechanisms using Gitcoin Grants data.
[/quote]

I'd love to see a repo or instructions for replicating your experiments and analysis. 

I hope this proceeds -- and best of luck Joel! :rocket:

-------------------------

epowell101 | 2023-05-01 16:56:39 UTC | #11

Just a shout out to see if the OpenData Community possibly can be helpful - maybe a future hackathon challenge or something a sandbox software project could embrace

The current hackathon for eg has data scientists looking at weights for stamps and also working at on chain stamp creation for eg.  Hopefully we will get some great responses and so have yet more educated and experienced “Regen Rangers” available to assist if useful

-------------------------

PaigeDAO | 2023-05-01 19:58:19 UTC | #12

Listened to this Green Pill episode over the weekend.  I appreciated @Joel_m  explanation of collusion vs. collaboration.  I especially appreciated how he and @owocki pulled at the threads of recognizing that humans naturally cluster (have friends, relationships and aligned interests) and that this isn't necessarily a Sybil attack. And that this exploration of QED appears to be able to set up mechanisms that deter (negate any benefit derived) from true Sybil attacks. Anyway, the podcast made it easier to understand for me.  

On that note, I agree with @ccerv1 suggestion above to provide a TL;DR written for the non-mathematical/QF layperson.  

Very interesting work! Thank you for this.

-------------------------

J9leger | 2023-05-01 21:29:09 UTC | #13

Really appreciate this proposal and idea. I'd like us to invest more in pushing the bounds of quadratic funding mechanisms. 

This is super exciting to see and it has my full support.

-------------------------

0xZakk | 2023-05-02 02:06:38 UTC | #14

Hey y'all, very curious about this proposal!

My first question is one about process and commitment - Erich, Alex, and Kevin Olsen are all full-time with Gitcoin through one of our work streams, but are listed here as members of the personnel. It sounds like, from your description, they wont be drawing from the allocation here. Is that accurate? Similarly, how much time are these three expecting to allocate to this proposal? I'm not per se against contributors receiving compensation from or contributing time to GCPs, but both of these aren't very clear from this proposal.

Second, in reading this, I don't feel like I have a lot of clarity on what the *result* or *output* of the proposal is, nor what specific problem it's solving. My biggest question is actually, "why should we do this?" What are we going to do with a Custom-tailored Mathematical Framework? And is there a specific issue that we can point to that we're experiencing that this framework will solve? Have we tried general, non-custom frameworks already?

-------------------------

ale.k | 2023-05-02 04:28:32 UTC | #15

[quote="Joel_m, post:1, topic:14174"]
The entirety of the budget will go to staffing funding ($9,080 a month for three months, or $27,240 total), which will be allocated to Joel, who will play a crucial role in developing and implementing the collusion-resistant QF mechanisms.
[/quote]

I think this may answer your first question.

As to the allocation of time - since anti-collusion is a piece of ensuring the core goals of trust and reputation for our grants program (my role), as well as an opportunity to advance Passport + Allo mechanisms for community clustering (a large part of Erich + Olsen's roles to determine feasibility of new features and scope problems solved by our products), this particular GCP fits well within current strategic goals for this group.  Much of the assistance and oversight provided will go into providing context for Gitcoin's ecosystem, so that Joel's ongoing QF/QV work can be directly impactful for our use-cases.

I hope this helps answer your first question on personnel. As to the second of results and output, we plan to measure our success in terms of traction built with community chatter around the project.  Joel will be delivering both high-level, technical research frameworks and also (in collaboration with myself and Erich) some more entry-point materials to explain and refresh conversations about QF as an option for funds allocation.  Anti-collusive systems, of course, have ramifications for governance and problems faced by the larger web3, web2, and non-web world, however - so part of the scope of this project is to invite a larger audience into our work at Gitcoin and highlight the practical problems solved by our products.

If there are specific metrics of success or methods that you've used in measuring the impact  of messaging and thought leadership in DevRel @0xZakk, would love to hear!

-------------------------

shawn16400 | 2023-05-08 11:09:37 UTC | #16

This proposal has been moved to snapshot for vote - find the link below and please cast your decision. 

https://snapshot.org/#/gitcoindao.eth/proposal/0x8b8e0ed4ec6ef5031b407d4abbc41a604c2f14528a12ec87e21aa5f9e04cabc7

**End date** May 15, 2023, 7:06 AM EST

-------------------------

tkgshn | 2023-05-08 15:14:35 UTC | #17

awesome! I'm building a social graph oracle that analyzes from GR Data to Plural QF's cluster set. Let's do it together!!


![image|551x500](upload://96AZysqP4Bmb2QYu8YxpIOdMpIj.jpeg)
![image|626x499](upload://tcqlhzA77fTNqLAgR3SeXsWhQeV.jpeg)
![image|690x133](upload://9X4aaUmxQqjVlvR3QzLM22apYNz.png)

project:
https://drive.google.com/file/d/1Q-OTIH_dBJ9a8gxJWsQm9qCHxd9_MolQ/view?usp=sharing
Code:
https://github.com/tkgshn/plural-qf/blob/main/decartography-pluralqf.py

Full Video:
https://i.gyazo.com/6fbeb55d161ff7a84b670efe4bfdad16.mp4

-------------------------

bobjiang | 2023-05-09 04:21:22 UTC | #18

I would support this Q.E.D experiment for anti-sybil. For Gitcoin (no matter Passport or Allo), this is a valuable try. move forward!

-------------------------

nategosselin | 2023-05-11 20:33:16 UTC | #19

I'm supportive of this proposal and will be voting YES — we haven't had a team dedicated to iterating on the underlying calculation mechanics and I'm excited to see what comes out of this. 

To @0xZakk's point about deliverables, from the Allo Protocol perspective it would be really helpful to see outputs that document any new calculation mechanism(s) and their relative tradeoffs. Perhaps expanding [on this format from our initial Linear QF mechanism](https://github.com/gitcoinco/grants-stack/blob/main/packages/api/docs/linearQF.md). 

The things that would be useful to see are:
- the actual calculation math
- explanations of the different customization levers and their impacts
- overviews of how distributions with new mechanisms compare to a distribution generated with old mechanisms

Happy to jam on what a useful output would look like to the protocol team — excited to see more from this group!

-------------------------

atris | 2023-06-22 16:55:42 UTC | #20

Full support from me. As an aside, a super well-written proposal too.

-------------------------
