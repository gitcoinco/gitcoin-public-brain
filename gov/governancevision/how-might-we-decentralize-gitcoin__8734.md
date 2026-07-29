---
id: 8734
title: "How might we Decentralize Gitcoin?"
slug: how-might-we-decentralize-gitcoin
category: governancevision
url: https://gov.gitcoin.co/t/how-might-we-decentralize-gitcoin/8734
created_at: 2021-10-04T21:54:30.463Z
last_posted_at: 2021-10-05T02:29:43.275Z
posts_count: 2
views: 4278
like_count: 12
---

# How might we Decentralize Gitcoin?

<https://gov.gitcoin.co/t/how-might-we-decentralize-gitcoin/8734>
owocki | 2021-10-04 21:54:30 UTC | #1

![Screen Shot 2021-10-04 at 3.36.54 PM|690x383](upload://pZX90wr9QmPVi7t1fXUSDamKsBb.jpeg)

Hey everyone,

Wanted to take a moment to lay out a high level view of *how we might decentralize Gitcoin* from a platform into a series of protocols.  

This post contains much of the same information as my recent [Edcon talk Decentralizing Gitcoin Grants](https://www.youtube.com/watch?v=ucaA3sh3SRA).

# Disclaimers

The information in this post is not a promise; it is a high level view of how we might decentralize Gitcoin IFF the DAO continues to grow + the company elects to progressively move more of it's functions into a DAO.  Of course, there is a lot of unknowns in this path, and we would only take any actions if there was a regulatory compliant way to them -- so please don't take this post as gospel, only a high level sketch of a direction.

This post is strictly educational and is not investment advice or a solicitation to buy or sell any assets or to make any financial decisions. This post is not tax advice or financial advice. Talk to your accountant. Do your own research.

This post is merely one persons opinion, and is not meant to represent everyone in the company or the DAO.  This is not an official statement of intent, it is merely a thoughtful exploration of the design space.  If you are a member of the DAO and you think another path should be taken, you are welcome to author a post that articulates a competing vision!

# Why

Why would we decentralize Gitcoin?

1. Because it's a better way to fulfill our [mission](https://gitcoin.co/mission) of building & funding digital public goods.  Digital public goods are inherently a global phenomenon, and a company domiciled in a specific jurisdiction and focused on a specific citizens court system is not well equipped to take on such a global mission.

2. Because a DAO is a fundamentally less fragile vessel for our mission, inso far as it's not oriented around any specific group of actors.

3. A DAO can do more things better/faster than a company can.    By leveraging a global workforce,  a DAO can draw talent from anywhere.  In a networked age, a DAO is a better/faster/vessel for human organization than a hierarchical company.  By creating common protocols that anyone can permissionlessly build on, a DAO enables innovation that was not previously possible.

For more on why it's time to decentralize Gitcoin, [checkout this post of the same name](https://gitcoin.co/blog/its-time-to-decentralize-gitcoin/).

# What

When we talk about decentralizing Gitcoin, the following are four pillars in scope:

1. Governance
2. Computation
3. Development
4. Economic

In general, a rubric that can be applied to decentralizing each of these things is "As the DAO grows in size, scale, competence, and ability, the transfer of more core functions to the DAO becomes possible.

I will breakdown some of the way I think about these things below.

## Governance

GitcoinDAO is governed by GTC - the governance token that powers the Gitcoin network.  

GTC is a fork of COMP, and allows delegation of voting power from everyday members of the DAO to a group of [Stewards](https://gov.gitcoin.co/t/introducing-stewards-governance/41/28) - basically highly involved and active members of the DAO who've agreed to be involved in governance.  This is whats commonly called [Liquid Democracy](https://en.wikipedia.org/wiki/Liquid_democracy).  [Here](https://twitter.com/owocki/status/1398282868741214215) is what the GitcoinDAO stewards looked like upon launch in May 2021:

![E2ey1M8UUAYFRpR|648x500, 75%](upload://AmeLK4Unf9wujB5QpMqBamGc2Tx.jpeg)

Why build GitcoinDAO with delegation at the base layer of the DAO?  Well, most governance tokens are not used except for by whales.  We wanted to make sure that common Gitcoin users had a say in the governance of the system..  After all -  A system's legitimacy & moral right to use political power is only justified & lawful when consented to by the people over which that political power is exercised.

The decentralization of Gitcoin's governance took another step with the release of the Steward Health cards - https://stewards.eth.limo/  - by the mmm workstream.  As I understand it, the idea is to provide information to Gitcoin token holders so that they understand who the most active/engaged stewards are.

A further step that has been discussed in decentralizing Gitcoin governance is to [move beyond coin voting](https://vitalik.ca/general/2021/08/16/voting3.html) into something that looks more like Quadratic Voting.  While no proposals have been made on this front, it has been an active point of discussion and tools like [Quadratic Diplomacy](https://quadraticdiplomacy.com/) and https://quadraticvote.co/ continue to provide low-risk experimentation on this vector.

## Development

The development of the software used to host Gitcoin's services is something that the DAO has been been experimenting with:

1. The open RFPs to decentralize [Gitcoin Quests](https://gov.gitcoin.co/t/request-for-proposal-decentralize-gitcoin-quests/8120) and [Gitcoin Kudos](https://gov.gitcoin.co/t/request-for-proposal-decentralize-gitcoin-kudos/8115/3).  We've also posted [RFPs to decentralize how Gitcoin profile information is stored](https://gov.gitcoin.co/t/request-for-proposal-decentralize-gitcoin-profiles/8116/4).
2. The [launch of the decentralize Gitcoin Workstream](https://gov.gitcoin.co/t/workstream-decentralize-gitcoin/180) in May 2021, and more recently, the launch of a MVP of dGrants - a completely decentralized version of Gitcoin Grants.
3. The launch of [Moonshot Collective Workstream](https://moonshotcollective.space/) - the DAO's rapid prototyping workstream, and several DAO-era products such as tip.party and Quadratic Diplomacy.

Over time, the GPG (Gitcoin Product Group) hopes to become more integrated with the DAO and to  itself begin working more as a workstream.  The gestalt of the cultural, technical, product (and probably other) layers of this stack working together will be important IFF the products are to survive & thrive in a DAO-era world.
 
## Computation

The [version of Gitcoin that was developed between 2017 - 2020](https://github.com/gitcoinco/web) is open source, but Gitcoin Holdings runs the website itself.  This version of Gitcoin is available at https://gitcoin.co is hosted on AWS.

Over time, we hope to see the Decentralize Gitcoin workstream build decentralized versions of the products in Gitcoin.co, such that the products in the product suite can be moved over to a more [credibly neutral](https://nakamoto.com/credible-neutrality/) architecture.  

There are a few special considerations that come along with decentralizing the computation of the network.
1. We must protect PII at all costs.
2. We are unsure how to decentralize the email portions of the architecture, as they (1) drive a lot of visits (2) are not easy to make public due to data privacy concerns.
3. The Cross-chain integrations built into gitcoin.co are not easy to decentralize due to the lack of an EVM-compatible smart contract layer on some of the chains we serve.  (While we are thankful to the Ethereum ecosystem for giving us our start, keep in mind that we are [open source maximalists](https://gitcoin.co/mission), not Ethereum maximalists)
4. Considerable functionality has been built into the legacy product over 4 years, and the 4 months of the DAO's software being live has been impressive but it has not yet reached feature parity with the DAO.
5. The legacy product is built as a centralized monolith ( https://github.com/gitcoinco/web ).  In retrospect, this was a mistake. In the future, the DAO workstreams are focused on building software that is simple, modular, and antifragile.

It is possible that for these reasons, we will not be able to fully rewrite all of the technology stack.  In such a case, there are 2 possible alternatives

1. Retire products that have lesser impact.
2. Build a [federated Mastadon-style architecture](https://en.wikipedia.org/wiki/Mastodon_(software)) into the legacy product suite which provides interoperability of data between different installations of the Gitcoin site.   From there the DAO could encourage community members to "run their own GitcoinDAO node", creating a decentralized network of Gitcoin.co-like services.

## Economic

GTC is a governance token and has no economic rights imbued within it.   As such, there is nothing much to write here at this time.

## Brand

The Gitcoin design team has been hard at work thinking about what decentralizing the Gitcoin brand would mean.  Here is an early exploration of what the mark could look like if it is decentralized:

![screen_shot_2021-09-29_at_9.28.01_am|595x500](upload://Aaoa0KEbf4jYJtI62dHoN2wOHDp.png)

For now, Gitcoin Holdings runs https://twitter.com/gitcoin and the [DAO mmm workstream](https://gov.gitcoin.co/t/workstream-suggestion-mmm-merch-memes-marketing-for-public-goods-gitcoin-gitcoindao/7066) runs https://twitter.com/gitcoindao  - Over time, it is possible that these brands may be merged into one visual mark and one [headless](https://otherinter.net/research/headless-brands/) brand identity.

# Conclusion

Thanks for reading my post.  We are in the early days of this discussion, but I hope that this post provided some mental floss for those out there who are considering helping out or are simply following along at home.

If you'd like to help us decentralize Gitcoin or to learn more, please sign up for the DAO at http://gitcoindao.com/ or join the conversation at https://gitcoin.co/discord .

![Screen Shot 2021-10-04 at 3.53.43 PM|690x277](upload://7x5OBAZkRiPCU1jYjX46LPCNHVq.png)

-------------------------

griff | 2021-10-05 02:29:43 UTC | #2

[quote="owocki, post:1, topic:8734"]
We are unsure how to decentralize the email portions of the architecture, as they (1) drive a lot of visits (2) are not easy to make public due to data privacy concerns.
[/quote]

For email services and other things, that don't make sense to be open and transparent, the DAO can hire "Service Providers" to manage these things... I don't think it makes it less decentralized, per say, just like any other work stream, some people are appointed to take on a certain role, and this role would entail securing private info... If you want redundancy, then hire 2 or 3 service providers to collect, share and secure that data. 

The harder thing / impossible thing is transferring the PII that you have already collected to another org... as I assume you want to eventually sunset the current Gitcoin org, and it's not really ok to send that data to the new org that would take over that roll. If thats the case, then the DAO will take a hit and lose some data... if not, then the old Gitcoin org and act as a service provider and there are no problems :-D.

We have the same issue with Commons Stack's Trusted Seed and the Token Engineering Commons... 2 very much overlapping communities but different legal entities so we can't share PII... The TEC had to build its list from scratch but Commons Stack supported them by sending emails giving people on our list the opportunity to opt in to sharing their PII... it's annoying, it won't get everyone, but with time the TEC collects more and more emails.... 

It's not the end of the world.

PS - I had to google this, so I assume others will as well:
PII = Personal Identifiable Information

-------------------------
