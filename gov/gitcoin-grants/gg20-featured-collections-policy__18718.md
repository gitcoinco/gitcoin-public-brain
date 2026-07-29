---
id: 18718
title: "GG20 Featured Collections Policy"
slug: gg20-featured-collections-policy
category: gitcoin-grants
url: https://gov.gitcoin.co/t/gg20-featured-collections-policy/18718
created_at: 2024-05-02T15:50:50.906Z
last_posted_at: 2024-06-17T13:01:31.597Z
posts_count: 14
views: 3010
like_count: 27
---

# GG20 Featured Collections Policy

<https://gov.gitcoin.co/t/gg20-featured-collections-policy/18718>
MathildaDV | 2024-05-02 15:50:50 UTC | #1

gm! 

ICYMI, collections are back! Anyone can now create a collection from their cart in Grants Stack. [Check out this post](https://x.com/grantsstack/status/1782885164244173283) for a full walkthrough if you haven't already! 

The team is also featuring collections on the GS homepage for GG20. Right now, we will add all collections that are submitted to us [through this form](https://forms.gle/Fx9pxfQWHKEjhw2J7) unless we deem them as scam. Here's the [PR for getting the collections up.](https://github.com/gitcoinco/grants-stack/pull/3407)

For future rounds, what do you think the policy should be on the collections we feature on the homepage? Feedback welcome!

-------------------------

owocki | 2024-05-02 16:00:30 UTC | #2

[quote="MathildaDV, post:1, topic:18718"]
The team is also featuring collections on the GS homepage for GG20. Right now, we will add all collections that are submitted to us [through this form](https://forms.gle/Fx9pxfQWHKEjhw2J7) unless we deem them as scam
[/quote]

The intent behind this policy is to allow people to create and discovery collections, and to do so in a credibly neutral way.  Credible neutrality is important because the more discoverable projects may get funded more often.


[quote="MathildaDV, post:1, topic:18718"]
For future rounds, what do you think the policy should be on the collections we feature on the homepage? Feedback welcome!
[/quote]

A couple experiments Id be interested in in for gg21 + beyond:
1. storing the collections on IPFS or smart contracts (which would mean we dont have to update the code as new collections come in)... but that will create an issue with ppl spamming the form with their collections.. so we will still need some ability to curate the collections list.
2. building on (1), perhaps we can create some sort of community group that curates the best collections, in order to decentralize the governance of collections.
3. another thing we could do is allow people to create a marketplace for collections.  some things to try
   1.  stake GTC or ETH on their collections, which would then get slashed if they spam the collections list.  
   2. why bother to stake your hard earned tokens on collections?  perhaps there could even be a reflink added to a collection wherein those who add grants in the collection to cart can do an optional donation back to the collection creator, effectively creating an economy for the best curators.

feedback welcome

oh and another thing. @gravityblast right now collections are specific to a round right?  imo in the future we should have collections that live past a round.

-------------------------

M0nkeyFl0wer | 2024-05-02 16:44:25 UTC | #3

Somewhat related topic: what are the implications of collections as it relates to pluralistic QF? It will be interesting to track the donation patterns of people and if we now see more clusters as a result of people adding all the same people to their cart. Sucessfull collections that generate a lot of donation may actually be punished in a sense. 

Im a big big fan of this feature, don't get me wrong. ;) 

Just curious to see how that plays out.

-------------------------

M0nkeyFl0wer | 2024-05-02 16:46:23 UTC | #4

[quote="owocki, post:2, topic:18718"]
storing the collections on IPFS or smart contracts
[/quote]

This is a dope idea. Would also love to see data viz of how people are interacting with collections. Where are the nodes in the network. Who is being added to the most collections etc.

-------------------------

owocki | 2024-05-02 16:46:40 UTC | #5

[quote="M0nkeyFl0wer, post:3, topic:18718"]
Somewhat related topic: what are the implications of collections as it relates to pluralistic QF? I
[/quote]

one way to answer this question in a data centric way might be to take a look at whether there are clusters of contributions around projects on collections.  or stated more broadly: where are the clusters of contributoins and what drives them?

-------------------------

M0nkeyFl0wer | 2024-05-02 16:49:15 UTC | #6

[quote="owocki, post:2, topic:18718"]
stake GTC or ETH on their collections, which would then get slashed if they spam the collections list.
[/quote]

This is interesting too. Maybe up and down votes of some kind could be explored... Hmmm. 

Also curious how we could tie collections to attestations. It's basically a form of endorsement. Maybe if people were actually attesting to a set of projects that they believe meet a certain standard and were will to stake tokens on it we could capture that as a hypercert or something? Could be useful in a variety of ways. 

Bonus points if we could integrate that directly into the eligibility review process and make that data widely available for anyone running rounds on grants stack. 

Hmmmm

-------------------------

jaxcoder | 2024-05-03 16:51:34 UTC | #7

[quote="owocki, post:5, topic:18718"]
one way to answer this question in a data centric way might be to take a look at whether there are
[/quote]

I like the idea of a collection not having the "round" lifetime and existing in perpetuity.

-------------------------

meglister | 2024-05-03 17:34:19 UTC | #8

I like this too, could drive donations outside a round -- which you've also been exploring!

-------------------------

jaxcoder | 2024-05-03 17:41:40 UTC | #9

I can also see a collection being used to spin up a Direct Grants round with the projects of the collection being the applicants of the Direct Grant being created. 

With the addition of attestations, we can also start to prove some reputation behind the projects - the question here to me is should the reputation exist at the project level as well and not just the collection level? I would like to see the project as being part of a/many collections would be able to have these positive outcomes within their profile and provable.

How can these collections be used with other protocols?

-------------------------

owocki | 2024-05-03 18:46:42 UTC | #10

[quote="meglister, post:8, topic:18718, full:true"]
I like this too, could drive donations outside a round – which you’ve also been exploring!
[/quote]

primary benefit i was hoping for having collections outside of a round, is that i wouldnt have to ask my influential friends to recreate their collections each round :).  less friction => more active collections => better discvoerability

-------------------------

gravityblast | 2024-05-03 18:53:37 UTC | #11

[quote="owocki, post:2, topic:18718"]
oh and another thing. @gravityblast right now collections are specific to a round right? imo in the future we should have collections that live past a round.
[/quote]

Yes exactly, they are round applications for now. It definitely makes sense to change them to be lists of projects as soon as we have projects pages (outside of a round) in explorer.

-------------------------

thedevanshmehta | 2024-05-07 07:20:59 UTC | #12

[quote="owocki, post:2, topic:18718"]
but that will create an issue with ppl spamming the form with their collections
[/quote]

I think the incentive should be around donation amounts, if they have contributed X  in the gitcoin round only then does their profile unlock the ability to make collections for that round.

[quote="owocki, post:2, topic:18718"]
those who add grants in the collection to cart can do an optional donation back to the collection creator
[/quote]

[quote="MathildaDV, post:1, topic:18718"]
For future rounds, what do you think the policy should be on the collections we feature on the homepage? Feedback welcome!
[/quote]

Love this idea! We can also then use amount donated to the creator as an ordering mechanism for displaying collections on the homepage.

-------------------------

owocki | 2024-05-10 16:37:25 UTC | #13

Another thing to put on the table as we talk about curating collections.

In the original Gitcoin DAO launch video, we talked about using GTC to surface community collections [[timestampped video]](https://www.youtube.com/watch?feature=shared&t=103&v=mTU6J4WTPtk).  It'd be interesting to experiment with GTC-oriented mechanisms for deciding what collections to feature.

-------------------------

M0nkeyFl0wer | 2024-06-17 13:01:31 UTC | #14

Could that be done with quadratic voting so that whales don't have all the decision making power?

-------------------------
