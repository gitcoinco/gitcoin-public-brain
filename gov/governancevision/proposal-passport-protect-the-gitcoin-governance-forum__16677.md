---
id: 16677
title: "[Proposal] - Passport-protect the Gitcoin governance forum"
slug: proposal-passport-protect-the-gitcoin-governance-forum
category: governancevision
url: https://gov.gitcoin.co/t/proposal-passport-protect-the-gitcoin-governance-forum/16677
created_at: 2023-10-04T20:37:39.763Z
last_posted_at: 2023-11-06T21:54:52.722Z
posts_count: 18
views: 4670
like_count: 40
---

# [Proposal] - Passport-protect the Gitcoin governance forum

<https://gov.gitcoin.co/t/proposal-passport-protect-the-gitcoin-governance-forum/16677>
lebraat | 2023-10-05 16:14:34 UTC | #1

## Summary

In S19, we partnered with ENS and a developer shop to create a Discourse plugin that enables web3 organizations to Passport-protect their forums from Sybils and bots.

We would like to implement this functionality on the Gitcoin governance forum to take advantage of these protections, to promote the functionality, and to dogfood the plugin.

## Abstract

As also stated in recent [Metaforo proposals](https://gov.optimism.io/t/proposal-move-optimisms-forum-from-discourse-to-a-web3-native-forum-platform-to-prevent-sybil-attacks-metaforo/6032), the web3 forum is a critical piece of community infrastructure where members brainstorm ideas, draft proposals, give feedback on each other’s ideas, and generally coordinate to get things done. In many cases, these community forums are hosted using Discourse, a web2 tool that has some additional plugins that make it work well with web3 tools.

While there are fantastic web3 forum solutions out there (some of which have Passport built in), not all companies have the resources to or interest in migrating. Because of this, we’ve partnered with ENS and 3rd party developers to create a Gitcoin Passport plugin that allows you to protect your forum from Sybil attacks.

This proposal outlines the functionality made available using this plugin, and suggests how we should integrate it into the Gitcoin forums.

## Motivations

Discourse is highly susceptible to Sybil attacks, where community proposals, feedback, and coordination can be manipulated. We would like to ensure that we are only allowing verified humans to contribute to the conversation and governance of our DAO.

## Specification

### All available protections

For this proposal, we are recommending using the following plugin: [Dappy.Lol’s Gitcoin Passport Plugin](https://meta.discourse.org/t/gitcoin-passport-plugin/273532)

The following features are available:

* Require a score over a certain threshold to create an account
* Require a score over a certain threshold to reply to topics
  * User-level – Score required to reply to any topics for specific user
  * Category-level – Score required to reply to specific topic
  * Forum-level – Score required to reply to any topic for all users
* Require a score over a certain threshold to create topic
* Scheduled date where score will be required

### Recommended implementation

We would like to implement the new Discourse x Passport plugin to protect the following forum functionality:

* Topic protection: Require users to have a score of 20 to create a new topic in any category
* Reply protection: Require users to have a score of 20 to reply to any topic in any category
* Implementation date: Start to require these new score levels on November 1st, 2023

Every 3 months, we will collect feedback and review the integration to make sure it continues to have the desired effect.

## Benefits

* The forum will be protected against sybil attacks.
* We will be able to prove out the sybil-protection that Gitcoin Passport provides, and use it as a use case to encourage others to take advantage of it.

## Drawbacks

* Participants will need to create a Passport and generate a score of 20.
* There is some maintenance required to reverify your Passport’s credentials every 90 days, and the score can change as our scoring models adapt to changes in Sybil behavior.

## Vote

A “Yes” vote means that you would like to add the Sybil protection to the governance forums for at least a period of 3 months. We will continue to monitor how effective this is every 3-6 months after that to ensure it is continuing to have the desired effect.

A “No” vote means that you do not approve of this proposal in its current form. This does not mean that you disapprove of the overall concept of adding Sybil protection. It might just mean that we need to adjust the integration details based on your feedback.

—

### Alternative solutions considered

The team has also discussed the following solution for this same problem, but ultimately recommend we move forward with just the Passport protection at this time.

We are happy to review your feedback on this solution as well in the comments of this proposal.

**Alternative solution**

Require individuals wishing to participate to have at least 1 GTC staked.

**Identified issues with this solution:**

Regardless of the low token price, this may exclude some who cannot afford to stake 1 GTC

**Potential Solution:**

Establish a program to delegate the necessary 1 GTC to participate to those who need it

* New Steward onboarding call quarterly (we should do this anyway)
* To minimize gas fees, we’ll do a multi-batch transaction for all of those who have applied & been accepted
* Delegates must maintain a score of X (aka be active) over 180 day period to maintain their delegation
* Each quarter we will do a sweep of inactive stewards and revoke the delegation

-------------------------

quaylawn | 2023-10-05 11:58:31 UTC | #2

Hey thanks so much for posting this :slight_smile: I'm tagging @garysheng to get the right set of eyes on this!

-------------------------

Jeremy | 2023-10-05 17:57:41 UTC | #3

Thanks for raising this and driving the use of Passport to help protect our forum. I think this will be a great experiment where we can determine if a score of 20 is too high for replies (e.g. will it exclude too many people) and the impact it has on preventing spam.

Big yes from me!

-------------------------

CoachJonathan | 2023-10-05 18:17:27 UTC | #4

I think this is a great step in terms of not just protecting our governance forum, but also dogfooding our products. I'm a yes to this proposal.

-------------------------

jengajojo | 2023-10-06 09:31:08 UTC | #5

Great to see that this updated is finally shipped! I'm in favor of this proposal

-------------------------

thedevanshmehta | 2023-10-06 14:59:52 UTC | #6

Hi there i wanted to know whether this is a solution for an existing problem the forum faces or for a hypothetical future one.

Is the forum under attack by bots that it needs to be passport protected in the first place?

I'd be against creating boundaries to participation, its hard enough to get engagement without creating additional hoops to jump through for posting a single comment

-------------------------

CoachJonathan | 2023-10-07 13:36:01 UTC | #7

This is a great point and something I'd want to continuously keep in mind as we continue with governance experiments. I also don't think the number of bot attacks is alarming at this point, but a good metric to keep looking at. 

That said, one reason I'm keen to proceed with this is that we are, straight up, dogfooding our products. If we don't find this feature useful, I'm not sure why we would build them/have them or why others would use them. 

To address your more specific concern, I also want to work with the team to ensure that the score needed to participate is relatively low, and that there are avenues to connect with us if a failing score is preventing someone from participating.

-------------------------

thedevanshmehta | 2023-10-08 10:32:58 UTC | #8

[quote="CoachJonathan, post:7, topic:16677"]
I also don’t think the number of bot attacks is alarming at this point
[/quote]

In that case passport protecting our forum does look alarmingly like a solution in search of a problem

[quote="CoachJonathan, post:7, topic:16677"]
If we don’t find this feature useful, I’m not sure why we would build them/have them
[/quote]

From my vantage point it looks like we've incurred the sunk cost of building passport gating for discourse forums and are now looking for a problem to apply it towards as its already been built

[quote="CoachJonathan, post:7, topic:16677"]
also want to work with the team to ensure that the score needed to participate is relatively low, and that there are avenues to connect with us if a failing score is preventing someone from participating.
[/quote]

Amazon's research is pretty conclusive that a % of users drop away at each point of friction (hence their emphasis on 3 click checkout). 

So the tradeoff is looking like passport gating solves the non-existent problem of bot attacks on discourse forums at the cost of a non-zero number of users choosing to disengage rather than go through the hassle of extra steps to participate

-------------------------

FractalVisions | 2023-10-08 18:33:09 UTC | #9

I’m curious as to why the forums can’t have a dashboard that is easy for newcomers to understand & join the governance with a web3 token gate like charmverse offers…

This seems like a simple solution to give role based permissions for forum discussions.

Are we really still relying on old web2 legacy systems to try and come up with a solution for something that is supposed to be decentralized?

To me the suggestion to integrate passport with discourse in order to gate the forums seems to be heading in the opposite direction of further decentralized governance for the Gitcoin ecosystem.

-------------------------

CoachJonathan | 2023-10-09 10:51:53 UTC | #10

There seems to be some great points being brought up as to whether or not this is something we want to integrate. I like the way Devansh put it of:

[quote="thedevanshmehta, post:8, topic:16677"]
like a solution in search of a problem
[/quote]

I'm going to set up a quick poll as a pulse check here to see how others are feeling about it based on the conversation we've been having so far.

[poll type=multiple results=always min=1 max=2 chartType=pie]
# Should Gitcoin Passport-gate its governance forum?
* Yes
* No
* Not sure/need more info
[/poll]

-------------------------

lebraat | 2023-10-09 15:52:38 UTC | #11

[quote="thedevanshmehta, post:8, topic:16677"]
From my vantage point it looks like we’ve incurred the sunk cost of building passport gating for discourse forums and are now looking for a problem to apply it towards as its already been built
[/quote]

Wanted to quickly point out that this integration was built for any Discourse forum provider to utilize, not just for us. ENS partnered with us to fund a bounty to build out this functionality and they have already integrated it into their forum. 

Sybil-resistance was just one of the benefits of this proposal... Dogfooding the plugin was another, but I agree that it would add some friction to the governance of the DAO.

-------------------------

DistributedDoge | 2023-10-09 20:28:39 UTC | #12

I don't think putting additional barriers to participation in Gitcoin forums is a good thing. I would rather see forums remain open to attract quality contributors and discussion. 

There are many situations when some external actor pops up, offers valuable perspective and leaves - asking them to spend 20 minutes messing with Passport before they write a single post is a bit much.

I would support a test that is limited in scope to a single forum category (Proposals?) but I would also suggest lowering score treshold considerably (20 is a pain to get).

-------------------------

garysheng | 2023-10-10 15:36:43 UTC | #13

[quote="DistributedDoge, post:12, topic:16677"]
I would support a test that is limited in scope to a single forum category (Proposals?) but I would also suggest lowering score treshold considerably (20 is a pain to get).
[/quote]

This make sense to me, with exception of 20 being a pain to get. This is what the Passport team has through research learned is a substantial gate for Sybils.

-------------------------

meglister | 2023-10-10 21:54:40 UTC | #14

I love Passport and the idea of using it to gate parts of our engagement processes where we incur high volumes of spam or want to set a high bar for legitimate actors to participate. I haven't personally seen high volumes of spam on the forum, but `1` I might be missing something and `2` I wonder if there are other areas where Passport gating could have a beneficial impact. Maybe GCP gating for the Allo test that's proposed here? https://gov.gitcoin.co/t/temp-check-managing-s20-gcps-on-allo-v2-repost/16726/3

As it stands I voted no in the temp check, since we've been optimizing so heavily for forum-based conversation in the wake of some controversial GG18 topics. Happy to be outvoted and participate in this experiment though! I'd also likely vote yes to a lowered score threshold.

-------------------------

flowscience | 2023-10-11 23:02:50 UTC | #15

Big agree @thedevanshmehta - this feels like solving a problem that doesn't exist and putting up barriers to participation.

If there's concern over temp check voting being compromised here. It would be very persuasive to show a specific example for those of us who participate less frequently. Further, if the concern is about protecting the integrity of voting, then I'd be more in favor of this initiative if the implementation was restricted to voting (instead of creating accounts, making a first post, and replying).

-------------------------

gaoa97 | 2023-10-14 02:47:14 UTC | #16

Great idea! I support this proposal.

-------------------------

CoachJonathan | 2023-10-24 07:16:48 UTC | #17

I appreciate everyone's comments on this post. After reading back and forth, I am going to change my position and would vote toward "no" for implementing this at this time.

Until gov forum attacks become a more serious problem, I think dogfood > participation is not the right heuristic for us.

I'm also keen to work with the Passport team (and maybe the Discourse team?) to create more experiments around "roles" within our gov forum so that those who have more at stake (aka more GTC) have access to more actions (creating proposals, commenting on certain proposals, etc.).

-------------------------

lebraat | 2023-11-06 21:54:52 UTC | #18

Wanted to close this out. 

We will not be gating our governance forum with Passport for the time being. We have a few other partners testing integrations, so dogfooding the process is not as important. 

If we identify in the future that we are experiencing a sybil problem, or if we make Passport onboarding more simple, we will revisit this and potentially make some adjustments. 

Thank you all for your input!

-------------------------
