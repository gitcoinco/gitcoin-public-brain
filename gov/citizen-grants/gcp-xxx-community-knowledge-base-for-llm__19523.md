---
id: 19523
title: "[GCP - XXX] Community Knowledge Base for LLM"
slug: gcp-xxx-community-knowledge-base-for-llm
category: citizen-grants
url: https://gov.gitcoin.co/t/gcp-xxx-community-knowledge-base-for-llm/19523
created_at: 2024-10-14T16:41:18.389Z
last_posted_at: 2024-10-25T08:53:54.919Z
posts_count: 13
views: 4012
like_count: 18
---

# [GCP - XXX] Community Knowledge Base for LLM

<https://gov.gitcoin.co/t/gcp-xxx-community-knowledge-base-for-llm/19523>
Conor | 2024-10-29 16:57:43 UTC | #1

# **a3na GCP**

Enhancing Gitcoin's Knowledge Base and Citizen Engagement

# Summary

[a3na](https://www.a3na.com/) (Consensys) proposes to unlock funds for Gitcoin Citizens to be rewarded for content that they contribute by leveraging a developing protocol named a3na. We also wish to work closely with Gitcoin to ensure that what we are building is for communities like Gitcoin, helping us to make informed decisions along the way about our application design, architecture decisions, smart contract design, and tech stack in order to ensure that Gitcoin’s knowledge base and community contributions are best positioned for scalable growth and usefulness.

# Abstract

a3na is a new concept by the team behind the community support product [VillageDAO](https://www.villagedao.com/) (Consensys) which looks to reward content contributors for their contributions to a shared, community knowledge base. Our research has found that communities find it difficult to keep their knowledge bases up-to-date, which results in gaps. Additionally, individual community member’s knowledge is not optimally utilised inside of a given community. The recent development of LLMs means that knowledge bases have become more valuable, as LLMs are able to deliver community knowledge to individuals at scale.

Inside of Consensys, we built a proof-of-concept, an LLM bot which references a specific knowledge base only (when answers do not reside in the KB, the LLM responds to say there is no answer available). Once one (or more) articles are referenced, a token is passed to the wallet of the contributor(s). Through this method, members of a community can be incentivized to contribute knowledge to a community knowledge base.

By expanding on and further developing this proof-of-concept we aim to revitalise the Gitcoin knowledge base (support.gitcoin.co) and provide a system for ensuring its sustainable long-term growth and management. We are excited to work with @Sov on this project given his expertise and familiarity with the Gitcoin ecosystem landscape and knowledge base.

# ![|624x351](upload://2xjh3l4zG1YBMRDONlHXytuSqU8.gif)

Demo of the proof of concept built during the hackathon.

# Benefits & Motivation

Maintaining a repository of knowledge for individuals to reference and use is a key component to enabling the successful growth of an ecosystem. However, it can come at a high cost in terms of time and effort when it is owned by only a select few. This proposal addresses this cost by providing a means for the community to contribute its collective knowledge for the benefit of the community, fostering ecosystem knowledge in a scalable way, and incentivising community efforts in return.

The benefits are multiple fold;

* Gitcoin will now have a way to catalogue and access all of the knowledge in the community. Which can include support use cases and beyond.

* Many of the conversations happening in support can be automated.

* We wish to create a legal framework for the content contributor (Gitcoin Citizen) owning their own content, which means that they will put more effort into the content which results in better content being added

* Any content that a Gitcoin Citizen publishes which is applicable to other ecosystems can be bootstrapped in those other communities, if they use this solution.

* Which also means that any content referencing Gitcoin, can be propagated in those communities too, which is good for Gitcoin’s exposure.

* Humanity will benefit, as this is a model for paying people for their knowledge, as opposed to [training LLMs with stolen content](https://www.axios.com/2024/02/22/copyleaks-openai-chatgpt-plagiarism).

# Project Scope

The proposed scope of the application and solution is planned to encompass the three experiences described below:

* Support seeking user experience

In the first instance we plan to implement the service as an API that could be integrated with tools such as Intercom. The result shown to the user is an answer from the LLM with references to any articles, and their authors. Ideally the references will be links to the full article.

* Content contributor user experience

The content contributor will be able to log into an a3na application (connect wallet) where they can publish content they believe to be useful and subsequently rewarded for it.

* Content curator user experience

The content curator will have the ability to select individuals (wallets) and/or specific content and associate them to specific topics of a knowledge base, so they can own a domain or “library”. Additionally, by leveraging keywords generated from the content submitted, we can expose gaps in coverage of the content being leveraged.

In the first instance, the end user (Support seeker) experience will be delivered as an API, planned for Intercom integration or other similar tools. After developing this initial concept, we plan to consider a more robust user experience for querying an LLM and browsing content which is indexed.

# Project Breakdown

Below is a high level overview of how the system will function for contributing and using content provided by the community:

![|624x137](upload://uxqwrGVwxbj4tvcLQGxBRFSpJu7.png)

**Content Contributor experience eg Gitcoin Citizen**

We are striving to design and implement a user-friendly experience for uploading and submitting content for community members. This will ensure that community members can provide useful information to answer the questions of other community members by providing a display of their submitted content and the rewards earned towards each piece of content contributed.

**Content Curator experience eg Gitcoin Community Manager**

The goal of the curator experience will be to provide a simple and clean means of browsing contributed community content to select and build out a robust set of libraries or collections of content that are targeted towards answering and/or documenting specific domains. Additionally, we want to explore leveraging generated keywords from the contributed content to provide a breakdown of areas that are under/overrepresented in the content being curated.

**Content usage**

Once the content has been curated, we intend on providing it via an API that will process the data and deliver it in a consumable manner for tools such as Intercom, LLMs, and, ideally in the near future, an embeddable search that can be plugged into various experiences.

**File/content storage**

We are investigating onchain as well as offchain file storage solutions and will need to consider cost. We can likely allow for intermittent onchain file publishing or some combination of solutions between key data onchain and more costly data offchain.

**LLM design**

We have previously used OpenAI service to build a proof of concept, but wish to explore more web3 aligned LLM services in our tech stack, such as the Venice.ai API, for privacy and censorship resistance. These services are pretty simple to swap out too.

**Token/Rewards design**

We are considering a two token model, where a citation token or attestation is sent to a content contributor each time their content is cited. This is then used as a calculation for payment (which can happen in a communities own token, on that communities chain, in this case $GTC on Allo).

# Risks

We have identified three potential risks to the success of this project in detail below:

* Usage and adoption
This can be mitigated by ensuring easy integration with the existing experience.

* Content moderation
This will be mitigated by the Content Curator role who will serve as the moderator and filter for content being selected for usage. In the future we would like to explore more automated means of filtering content contributed to a3na.

* Sybil resistance/spam attacks
There are a number of methods that can be employed (see below).

One note on sybil resistance / spam attacks, is that we can use many different ways to determine whether a user is a bot or genuine. These methods range from bot detection (e.g. cloudflare in use on perplexity.ai, or discord bots to detect real users ) to even the possibility of a kind of “connect wallet to ask the LLM experience”. Different clients of the protocol will have different appetites to prevent bot attacks from earning citation tokens. However, we will be cautious and monitor the activity, and act accordingly.

Also, we can plan the rewards such that they reward better behaviour, e.g. the possibility of future rewards will be removed from bad actors, separation of citation and rewards (i.e. payment for citation).

Additionally, we have prevented any sybil attacks inside of VillageDAO clients due to recruiting trusted community members.

# Budget

[Below from the RFP]

The recommended total budget for the enablement of usage and adoption of this platform is 20,000 GTC. The recommended breakdown of monthly allocations is as follows.

### Monthly Allocation

1,666.67 GTC per month (20,000 GTC / 12 months)

### Breakdown

1. Content Contributor Compensation: 15,000 GTC

  * Allocated for community members contributing high-quality content
  * Distributed based on contribution quality and usage metrics
  * Monthly pool: 1,250 GTC

2. Technical Development and Maintenance: 3,000 GTC

  * For ongoing development, updates, and technical maintenance of the knowledge base platform
  * Monthly allocation: 250 GTC

3. Community Engagement and Moderation: 1,200 GTC

  * To support community managers and moderators overseeing the knowledge base
  * Monthly allocation: 100 GTC

4. Incentives and Rewards Pool: 800 GTC

  * For special initiatives, contests, or bonus rewards to drive engagement
  * Can be distributed as needed throughout the year

### Additional Considerations

* LLM Usage Costs: To be billed separately based on actual usage
  * Recommend setting aside a separate budget for this, not included in the 20,000 GTC
* Flexibility: The allocations above can be adjusted based on actual needs and performance throughout the year, ensuring optimal use of the budget.
* Reporting: Monthly reports will track GTC distribution, content creation metrics, and overall knowledge base performance to ensure the budget is used effectively.

# Milestones

We present below an outline of the four major milestones we are planning to hit in order to achieve the initial version of this project and their descriptions. Currently, we estimate achieving these milestones over a time period of six months.

## Milestone 0: Design and Content Review

Description: We will work closely with Gitcoin to map out the existing content library, and understand a framework for closing the gap between the missing, and outdated content, and adding new content. Content is a living thing! As a result, the system which keeps the content up to date with the workings of Gitcoin will be important. Through a3na (rewards and citations) we hope to enable a living knowledge base for Gitcoin. Something which many LLM systems struggle with, is how to keep the references up to date.

## Milestone 1: View Content Library

Description: We will build a system for storing and retrieving contributed content to a3na that will ensure content ownership is verifiable and lay the groundwork for the rewards and citation system.

## Milestone 2: Content Contributor Experience

Description: Completion of this milestone will enable Gitcoin Citizens to begin contributing content to a3na for usage by Content Curators, building the body of community knowledge.

## Milestone 3: Content Curator Experience

Description: With the foundation in place for community sourced content, achievement of this milestone will mean that Gitcoin Content Curators will be able to browse and select contributed content for use in their knowledge base via API, enabling integrations into existing systems (e.g. Intercom) and LLM usage.

## Milestone 4: Content Usage Rewards

Description: A smart contract, which, when implemented, means each time a content contributor’s (Gitcoin Citizen) content is referenced, rewards are calculated for distribution.

# Acceptance Criteria

* Knowledge Base review and gap analysis: As part of the initial review of the current state of the Gitcoin knowledge base, the gaps in information will need to be surfaced and communicated.

* Interface for Contributors and Curators: The platform should have an intuitive interface for community members to contribute content and for Gitcoin to browse and curate which content is relevant for the knowledge base based on needs and quality.

* Content usage mechanism and rewards: The platform should enable Gitcoin to be able to reference and leverage the curated content by means of a permissioned API that can be integrated into existing tools.

* Onboarding and training materials: To ensure smooth migration and adoption of the platform, onboarding and training materials should be published and provided to the community.

# Relevant Metrics

* Number of content contributed: Track the total amount of articles contributed to the platform to assess level of engagement and variety of content provided by the community.

* Number of content referenced: Track the total number of times individual articles are referenced (through distributed citation tokens) when providing users solutions to their questions/requests for information to ascertain the level of usage.

* Number of rewards earned: Track the total amount of rewards being earned for the usage of community content to ensure appropriate amounts of rewards are being distributed for the community’s efforts.

* Content gaps identified: Published information that highlights the domains where knowledge is out of date and/or lacking so that it can be proactively addressed.

# Team

We are a team situated within the Customer Success department at Consensys who have been building web3 support tools to improve the overall user experience in the ecosystem for the past two years. Our current products include [0xplain](https://www.0xplain.info/), a tool designed to improve the readability of transactions and relevant content for users. We also built [activity.metamask.io](http://activity.metamask.io) (which leverages 0xplain API) and [VillageDAO](https://www.villagedao.com/), a platform that enables communities to reward their members for solving user problems.

# Conclusion

We are very excited about this project and the opportunity to enable the Gitcoin community to own and expand their collective knowledge. This project represents a continuation of our efforts to create a web3 suite of tools that fully enable communities to empower themselves and create a more sustainable, transparent and open ecosystem for all to engage with.

We welcome any feedback, questions, and suggestions. The input provided by Gitcoin is key to guarantee that the project appropriately addresses the needs of the community and meets expectations. All of this proposal is up for discussion, if there is any part that does not fit with your needs, we would love to know and iterate!

# FAQ

* What is the model for a3na to charge money?

Currently, we are looking to take a % of the token rewards which flow through the system, about 7% to begin with. But we will work with you, and hopefully more communities, to understand how this price discovery works best for everyone.

* Do Intercom have a similar feature?

Intercom have Fin, an AI chatbot which can provide an LLM service. However, the Intercom model assumes that there is a centralised entity maintaining a knowledge base of answers for the bot to draw upon. The a3na concept is a way for a community of individual contributors to earn rewards for their contributions to a collective knowledge base, and see their citations onchain. Also, we will build an integration with an LLM service in order to consume the knowledge base.

-------------------------

deltajuliet | 2024-10-14 22:05:22 UTC | #2

Thanks @Conor - please re-post this GCP using [the full template](https://gov.gitcoin.co/t/gitcoin-community-proposal-gcp-template/134) and including all relevant information (amount requested, timeline and milestones, work being completed, etc).

-------------------------

MathildaDV | 2024-10-15 09:21:05 UTC | #3

I echo what is being outlined and asked of here. Please repost with the full proposal so that we can review and comment on it more productively.

-------------------------

Conor | 2024-10-15 11:12:22 UTC | #4

thank you Mathilda and deltajuliet! I have a proposal in the correct template ready to go. I need permissions in order to add to the "Proposals" category. Currently it says *You are not allowed to create topics in this category*. Can you please allow for me to add persmissions?

-------------------------

Conor | 2024-10-15 12:08:38 UTC | #5

upon Sov's request I updated the post to be the entirety of the proposal in the correct template so that we can hopefully move it to the Proposal section :)

-------------------------

ccerv1 | 2024-10-18 15:54:29 UTC | #6

This is an interesting idea, but I have some major concerns:

1. This is completely unproven beyond there being a PoC at Consensys. That means there's risk it never ships. This is true of any new project. 
2. Assuming it ships, we also don't know if the content created will be valuable to Gitcoin community members and widely adopted. It's not responding to an existing pain point (that I know of) around content creation.
3. The proposed future take rate of 7% is very high. If Gitcoin moves $1M in GMV, thats $70K. You could get 40 premium Intercom accounts for that amount.

In summary, I don't like the idea of Gitcoin paying a team to build something that neither a workstream nor the community asked for. FWIW, this feels like a good candidate for retro funding (after its shipped and impact is more evident). I'm not pooh-poohing the idea, just the request for 20K GTC.

-------------------------

deltajuliet | 2024-10-19 00:18:32 UTC | #7

I'm going to echo @ccerv1 concerns and add some notes. 

FWIW the Grants Lab team struggles to maintain the KB so I think it would be great to overhaul and make this useful - especially as we grow our builder community. 

20K GTC makes sense to do the initial work, it's valuable to have relevant/up to date docs - but 7% is a high ask and there isn't any evaluative criteria. @Conor how would you measure this? 

@Sov may have some insights here to refine further. I think having the Gitcoin team weigh in on why/if this is valuable could help and further modeling on the take from the a3na team could be beneficial. 

fwiw @Conor this also needs a voting criteria. If we are to use funds from the Citizen's Grants Program (cc @MathildaDV) we need to move this to snapshot. You can find those in the template as well.

-------------------------

Sirlupinwatson | 2024-10-21 22:00:04 UTC | #8

HI all! 

My opinion about this project: 

For 20K GTC for which is about 15k USDC at the moment, you could effectively build 100's of those LLM's, custom, to fit any needs or particular process and who can fit in almost any context, Discord, Twitter rollup, Telegram channel.

I can effectively build one overnight, that will contain any knowledge base that will be required in order to be fully functional, then you can share it for free to any community or frens. And all this, for free... I can also introduce LLM's that are open-source, with ease, finesse and elegance. 

There is definitely no need for such LLM's, even more at this price since we can get them for free, and build them for free... 

Also, I'd like to point out at this specific part where: 

[quote="Conor, post:1, topic:19523"]
Humanity will benefit, as this is a model for paying people for their knowledge, as opposed to [training LLMs with stolen content ](https://www.axios.com/2024/02/22/copyleaks-openai-chatgpt-plagiarism).
[/quote]
How can you claim that you are not using stolen content... Since it's for the community? For me, it's the same. Frens are actually giving away their "knowledge", on a free will similar as using the MIT open-source license, right? On the other side, you market this solution, grow the effective and relational market associated with it at the same time (the token), and distribute a fraction to the original contributors... Where is the difference?

To resume, there is no need for this.


Update: 
I was thinking overnight how this was non-sense and here is a few other points: 

1- You claim that a fraction of the benefits will be redirected to a user, fine... How do you manage the distribution of that said "knowledge" when the same user will be rewarded over and over for the same question, are you telling me that, each user will be "forced" to contribute to your ($%^&*) LLM to be rewarded?
2- Bias, bias and more bias... First let's imagine you release this LLM to any community, who will update and maintain it? Who will maintain the data that reside in this LLM, who will decide which part is or require censuring about specific subjects... 
3- How much is the cost to maintain this LLM, how much cost the infrastructure, how much cost the database and the host...
4- Think about it, each time a question in triggered, an answer will follow, right? The knowledge that reside in the database will be attributed to a specific user, and thus will be rewarded at the same time... If there is something that has bias, it's clearly this... 

So, again, I believe no one will have any objection that, if this proposal move forward, that I'll build the same tool, for half the price... So, no stewards will object, right?

Let's talk about it, unless you want to avoid this conversation... @Sov

-------------------------

Sov | 2024-10-21 12:58:56 UTC | #9

Thanks @ccerv1 for context this is a platform that I have been working with the team on.  I can add some comments to your points below:

1) yes this is true of any product.  The team has a working platform and can provide those details here.
2) I believe our current KB setup could use some help as we have siloed KB instances and a good amount of the documentation needs to be updated.  This is an existing pain point for me personally in working with partners and grantees for support and operations.
3) the take rate only refers to the amount given out from the platform not GMV as a whole.  I can work with the team to update the language.  Also keep in mind that Gitcoin sets the amount of allocations available from the platform so we have control in that respect.

-------------------------

meglister | 2024-10-22 00:41:25 UTC | #10

Thanks @Conor for the proposal -- cool to see the innovation coming out of Consensys! 

I share the concerns flagged here. While we certainly should do a better job of keeping the KB up to date, I'd rather just work with a set of known community members to do so with the tools we already have. There are switching costs for every project and the fact that this is unknown and may not be maintained in the future doesn't make it palatable to switch for little gain.

-------------------------

Conor | 2024-10-22 14:15:18 UTC | #11

Thank you all very much for considering the proposal, and your detailed feedback! The reason why we are considering proposals at such an early stage in our product development was to ensure that we were building with communities such as Gitcoin in mind. To address the issues raised in the replies:
* To clarify, the original outline of the 20k GTC was for incentives for the Gitcoin Citizens to write articles for the knowledge base. We suggested protocol fee of 7%. Perhaps a protocol fee is too blunt a pricing mechanism, a flat fee might be more appropriate. This is great feedback, ty!
* The objective of the proposal was to create an incentive mechanism for Gitcoin to fund articles to go to the knowledge base. We've gotten some insight that the knowledge base articles may not be up to date, and are potentially in disparate places. The proposal was also to provide an LLM solution in order to consume articles from this knowledge base. 
* The concern around switching costs and delivery are certainly valid, and perhaps could be mitigated if we were to move to a more retro funding model. 

How would folks feel if we were to move to a retro funding model instead? We may all be more aligned with that.

-------------------------

Sirlupinwatson | 2024-10-22 21:24:21 UTC | #12

Even, this does not advice or explicitly arose about any of the points I have mentioned... Still, LLM's are "Free", org are splitting themselves in order for "you" to use their algorithm where you can have them for free, use a custom integration of GPT, Gemini, LIama2...

So, to write up a "knowledge base" that have been written multiple times already, we could in fact, use a much smaller amount of user, pay them even a fraction of this price, and do a much better job with user-interaction. 
- Last time, we created an AI bot, for free, we built it overnight, and we had an AI chatbot, that could in fact answer any of those question in real-time for the user-support or the knowledge base at GitcoinDAO... This in fact, require lest maintenance, it's almost a no-cost infrastructure to setup, and any rookie could do it...

If you want, I can lay out the pros and cons, about those 2, and we'll weight which is best for the DAO at this point.

-------------------------

ccerv1 | 2024-10-25 08:53:54 UTC | #13

Hi Conor
Thanks for the clarifications, especially about the use of the incentives and protocol fee. Personally, I would love to see some traction behind this *first* before funding it.

-------------------------
