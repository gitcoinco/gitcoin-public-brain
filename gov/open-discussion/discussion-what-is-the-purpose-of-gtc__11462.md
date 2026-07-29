---
id: 11462
title: "Discussion: What is the purpose of GTC?"
slug: discussion-what-is-the-purpose-of-gtc
category: open-discussion
url: https://gov.gitcoin.co/t/discussion-what-is-the-purpose-of-gtc/11462
created_at: 2022-09-08T12:43:09.377Z
last_posted_at: 2022-09-14T15:57:20.518Z
posts_count: 5
views: 4005
like_count: 16
---

# Discussion: What is the purpose of GTC?

<https://gov.gitcoin.co/t/discussion-what-is-the-purpose-of-gtc/11462>
nategosselin | 2022-09-08 12:43:09 UTC | #1

A frequent discussion topic within the DAO over the last several months has been creating utility for our token, GTC. From an existential standpoint, it’s crucial that we build utility for GTC so that it holds value and continues funding the DAO’s efforts towards our mission. We’ve dedicated [words](https://gov.gitcoin.co/t/circuits-a-modular-scalable-way-to-think-about-network-utility/11085) and [code](https://voting.gitcoin.co/) to experimenting with how we could make our token useful, but something that’s been missing (for me at least) is a shared understanding of what GTC should be useful *for.* [Utility is defined as “fitness for some purpose”](https://www.merriam-webster.com/dictionary/utility) — my goal with this post is to suggest a core purpose for GTC. 

**What is our MVI?**
Part of our challenge is that GTC was [originally conceived as a governance token](https://gitcoin.co/blog/introducing-gtc-gitcoins-governance-token/) — it wasn’t designed to have functionality beyond DAO decision-making, and we are now trying to retrofit a utility component for our fledgling protocol ecosystem. To help us navigate this design space, I’d like to introduce a [concept from Packy McCormick and Tina He](https://www.notboring.co/p/designing-token-economies) called **Most Valuable Interaction (MVI)**:

> When consulting with new DAOs or crypto projects contemplating the launch of a new token, Tina tends to start with a simple question: *What is the one most important reason why people are in your ecosystem?* This is the **Most Valuable Interaction (MVI)** of the network, and the **focus of the token design is to incentivize a sustainable feedback loop for such MVI**.
> 
Agreeing on an MVI enables us to navigate fundamental questions around functionality and drivers. 

So, what is the MVI of the Gitcoin network? One of the most common themes that has come up in product research for our protocols is the idea of **trusted reputations**. Our purpose is to *empower communities to fund their shared needs*, and our community members often highlight that there needs to be trust between parties in our ecosystem for that funding to be successful. Communities using quadratic allocation mechanisms need to *trust* that voters aren’t sybil attackers, round operators need to *trust* that grant recipients are legitimate projects, and projects need to *trust* that a given community will actually fund their work. We’re in the process of building protocols that enable our different participant archetypes to create the profiles that they will use to navigate our network (Passport for voters, Grant Hub for projects, etc) and I **propose we consider GTC a unit of trust** that enables network participants to enrich their reputation in our protocols. 

**Cool, so now what?** 
Aligning on GTC as a unit of trust allows us to think about [the token itself as a product](https://variant.fund/articles/tokens-are-products/) — meaning that we can frame utility discussions with questions like “what is our core user need?” or “what problem does our ownership experience solve?” (h/t Jesse Walden). Thankfully, much of our ideas for GTC utility already hint at trust as a purpose:

- Staking on trusted identities in Passport
- Staking on project legitimacy via the Curation Game
- and so on

With that intellectual foundation in place, we’re in a position to design sustainable feedback loops around our core interaction. As [this piece highlighted](https://cobie.substack.com/p/apecoin-and-the-death-of-staking), that will also require us to determine an effective balance of risk and reward in our utility systems. In order to sustain GTC’s value as a unit of trust, we will need to examine our utility ideas and make sure that they incentivize GTC holders to use it for this new purpose. My suggestion would be that the DAO aligns on this core function, then we discuss what we think appropriate risk and reward levers are for our system before jumping further into utility ideas.

Does this resonate with people? Would love your thoughts.

-------------------------

epowell101 | 2022-09-08 18:03:44 UTC | #2

Thank you for writing this!

What resonated w/ me:
- it **is** existential - the elephant in the room

- your perspective is informed by product goodness - like talking w/ users and the community (follow the persona!)

- scaling trust is all important even in a “trust less” decentralized focused ecosystem 

- definitely in the open data and data science world where I’m supporting FDD efforts there are many (incld me) that think that mechanism design including governance / meta governance might unlock or at least further communities to defend web3 from sybils for eg and I’d love to brainstorm about how GTC can help (in addition to hopefully being used in staking identity role as you mentioned)

I can see a few ways that GTC could be tied into grants 2.0 as well.

Who is currently responsible for GTC utility today?  I hear there are more experiments about GTC utility coming - so maybe part of the answer here is more visibility and thereby traction and contributors these efforts.

-------------------------

shawn16400 | 2022-09-10 00:27:32 UTC | #3

Hey @nategosselin - thanks for the post.  I appreciate new frameworks that can help us think differently about chronic issues - the MVI is an interesting take.   I also like your how you suggest value follows utility.  Previously I considered that DAOs using a governance token should focus on efficiency and engagement of the process - and with demonstrated good decisions, value would fend for itself.  I think I like your approach better than mine, but find both better than the "how can we make number go up" game. 

[quote="nategosselin, post:1, topic:11462"]
I **propose we consider GTC a unit of trust** that enables network participants to enrich their reputation in our protocols.
[/quote]

Ok, I kind of follow here - but I tend to ask a lot of questions so here goes:
1) how do I reconcile GTC as a unit if trust, if I can just go buy more GTC?  I can see it as a unit of trust if we use limit the "trust" component to sybil resistant delegation of GTC ([passport](https://passport.gitcoin.co/)  comes to mind) and count the delegation as a unit of trust.  But is the idea a pile GTC by itself is more trustworthy? 
2) Does Gitcoin decentralization fit into GTC as a unit of trust?  As a governance token, I see token value as a referendum on DAO performance (excluding macro market swings) which I think includes delivery of our purpose to **empower communities to fund their shared needs**.  If we deliver the purpose well, but in a hierarchically centralized way, does trust increase?  If we do a mediocre job of delivering the purpose but run all major decisions via a decentralizing mechanism does trust increase more? 
3) Do existing trust or reputation mechanisms fit into this model?  Here I am thinking [Karma](https://www.showkarma.xyz/) or [boardroom.io](https://boardroom.io/voter/0xc2E2B715d9e302947Ec7e312fd2384b5a1296099)  or Kudos?
4) Ok, some will groan at this - but how do we draw a line between trust and value? Or how can we measure the trust level achieved?  Potentially in relation to other governance tokens? 

and hey, don't take these as challenges - I like the concept, I am just trying to understand it.

-------------------------

nategosselin | 2022-09-12 18:25:40 UTC | #4

Thanks for the thoughts @shawn16400! I love these questions — please keep them coming.

I have some specific ideas below, but want to share some macro framing that I think might help first. Up until now, "governance utility" has been the only category of token utility available with GTC. IMO, much of our discussion about "adding token utility" across the DAO has actually been about adding "protocol utility" as another class alongside governance. In other words, how can GTC be used to enrich the experience of using our protocols? My goal with this post is to suggest a north star for this new category, so that it's clearer what type of systems we should be designing:

* **governance utility**: how should Gitcoin DAO spend its treasury? What should we focus on?
* **token utility**: how do we signal trust in our protocol ecosystem?

Here are some thoughts on your specific questions:
> how do I reconcile GTC as a unit if trust, if I can just go buy more GTC? I can see it as a unit of trust if we use limit the “trust” component to sybil resistant delegation of GTC ([passport](https://passport.gitcoin.co/) comes to mind) and count the delegation as a unit of trust. But is the idea a pile GTC by itself is more trustworthy?

Great point! If we go this route, I think we will need to design feedback loops that reinforce GTC as a unit of trust. We have the bones of an a supply system that supports this, in that GTC essentially enters the market from the Gitcoin community (via salaries, airdrops, etc). We'll need to look at designs that make it hard for one whale to tip the scales (sort of like what QF does...)

> Do existing trust or reputation mechanisms fit into this model? Here I am thinking [Karma](https://www.showkarma.xyz/) or [boardroom.io](https://boardroom.io/voter/0xc2E2B715d9e302947Ec7e312fd2384b5a1296099) or Kudos?

I think so! One idea that we've been talking about in GPC is the ability for different organizations to provide scores for projects or programs, so that other protocol users can see a community's perspective. For example, you could see the "Gitcoin trust score" for a project (as determined by GTC staking perhaps) alongside a Karma score, or something else.

Your other questions are heady, but I like them! Happy to chat through them directly if you want to :slight_smile:

-------------------------

epowell101 | 2022-09-14 15:57:20 UTC | #5

@nategosselin @shawn16400 is there a source for information on ongoing GTC utility experiments that could be shared here?  It would seem to be relevant to the conversation. 

I know there have been prior threads for eg… 

Given that afaik we have no means of extending our runway via traditional methods (like revenues) & the value of GTC has been volatile - again I’m appreciative of Nate raising the question again.  

I do wonder whether in addition to identity staking (one of those experiments afaik) we couldn’t look at other approaches such as using GTC to build relationships w grantees perhaps similar to the way JuiceBox is - even if done in a net neutral way this might both increase liquidity and invite more folks into the tent to participate in the DAO.

-------------------------
