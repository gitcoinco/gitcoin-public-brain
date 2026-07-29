---
id: 3640
title: "Weekly Update: Decentralize Gitcoin"
slug: weekly-update-decentralize-gitcoin
category: open-discussion
url: https://gov.gitcoin.co/t/weekly-update-decentralize-gitcoin/3640
created_at: 2021-05-28T15:54:14.092Z
last_posted_at: 2021-08-16T16:00:21.199Z
posts_count: 6
views: 4200
like_count: 24
---

# Weekly Update: Decentralize Gitcoin

<https://gov.gitcoin.co/t/weekly-update-decentralize-gitcoin/3640>
phutchins | 2022-05-28 15:38:05 UTC | #1

Hey Gitcoin Community,
I'm pumped to have kicked off the Decentralize Gitcoin Workstream last week along side the announcement of the release of the GTC token. Seeing all of the positive feedback from the community gets me excited to push this forward. 

The mission of this workstream is to decentralize Gitcoin and empower the community that it serves. The first step toward accomplishing our mission is to increase transparency and open the lines of communication with the community.

I will start by providing regular updates on our progress beginning today!

**Community Status & Updates**
    - [Published Workstream Suggestion post](https://gov.gitcoin.co/t/workstream-suggestion-decentralize-gitcoin/180)
    - [Published Steward post](https://gov.gitcoin.co/t/introducing-stewards-governance/41/41)

**Decentralization Architecture Proposal Creation Status**
    - Aiming to propose multiple solutions for each area which requires decentralization recommending one with background on why
    - Goal is to focus on solutions that provide same or better UX/Performance
    - Proposal focus is currently overall but will move to prioritizing decentralized storage/retrieval initially

**Research**
    - Researched [Gnosis SafeSnap](https://blog.gnosis.pm/introducing-safesnap-the-first-in-a-decentralized-governance-tool-suite-for-the-gnosis-safe-ea67eb95c34f#:~:text=We%20see%20the%20Gnosis%20Safe,execution%20of%20off%2Dchain%20votes.)
    - Digging into [MACI](https://github.com/appliedzkp/maci)
    - Better understand types of attacks on Gitcoin grants to date
    - Will dig into [The Graph and Indexers](https://thegraph.com/docs/network#overview) (initial high level research done, will test implementation)
    - Got caught up on background of Hackathons and details (with Connor)
    - Meeting with Aditya to understand current codebase / GitHub

**Next Steps**
    - Will post a bounty to have API documentation built in Swagger

-------------------------

mortan | 2021-06-02 20:47:45 UTC | #2

Thanks for the update!  Looking forward to the traction this gets.

[quote="phutchins, post:1, topic:3640"]
Will post a bounty to have API documentation built in Swagger
[/quote]
Has that bounty been posted yet?  Would love to help where I can.  

If you find a good resource on some of the attacks on Gitcoin grants I would love to dive-in and do some research.  Finding where the community has been exploited in the past is a great place to start, and I'd love to read about it or get in touch with people who can explain a bit of it.

I know it's a fresh workstream, but is there anything specific you would like help with, either from the community or an individual?

Thanks for the great work!  So excited to see the community in action.

-------------------------

phutchins | 2021-06-15 16:23:16 UTC | #9

Hey @mortan, the bounty has not been posted yet. I can share a link in this forum when it has been posted however!

Regarding attacks on Gitcoin grants, [this article](https://medium.com/block-science/deterring-adversarial-behavior-at-scale-in-gitcoin-grants-a8a5cd7899ff) is a great place to start. Also check out the [Grants round 9 governance brief](https://gitcoin.co/blog/gitcoin-grants-round-9-governance-brief/).

We are almost to the point in the timeline where we could begin accepting help as I'd like for us to take an organized approach which will be possible once we have a better idea of where we are headed and all of the moving pieces involved.

In the mean time, it would be great to hear ideas around how we can get the community more involved while keeping the progress moving quickly.

-------------------------

phutchins | 2021-06-21 18:00:06 UTC | #10

It has been a couple of weeks since our last update. I was out of office two weeks ago so little progress was made during that time. Over the last week we've made some great progress on the Architecture Proposal and are nearing completion of the initial draft. Most of the big pieces are getting clearer and are falling into place.

We realize that we have a huge resource here in our community and we are working hard to get to a place where we can accept all of the generous offers for help and contribution. Once we have a clear draft of the Architecture Proposal that is laid out in conceptual pieces, or building blocks if you will, we will be much better positioned to start more specific conversations around each of those areas and begin to give clear direction for those that would like to contribute their time, brain power, and experience.

**Gitcoin Community, we appreciate you!**

**Community Status & Updates**
    - We have created a channel on discord (#decentralize-gitcoin) specifically for discussion around decentralizing Gitcoin
    - [Created a grant](https://gitcoin.co/grants/2929/decentralize-gitcoin-grants) for funding the [Decentralize Gitcoin Grants project](https://github.com/gitcoinco/dgrants) (repo is currently empty awaiting the initial draft of the Architecture Proposal)

**Decentralization Architecture Proposal Creation Status**
    - Initial draft of Architecture proposal is nearly complete

**Research**
    - We are currently focused on areas like curation, and payout and matching calculation which are more difficult to decentralize and keep costs down

**Proof of Concept**
    - I have begun building a Grant Registry and Grant Rounds contract which will be open sourced in the coming weeks
    - Next will be building a very simple UI (Dapp), Integrating Metadata, and implementing Graph Protocol

**Next Steps**
    - Preparing to schedule initial community update call
    - Progress on API documentation has been halted as we have discovered a parallel initiative that is moving forward with something similar to this
    - Wrap up Architecture Proposal draft and post to the [DGrants Github](https://github.com/gitcoinco/dgrants) for feedback
    - Continue work on POC and move to [DGrants Github](https://github.com/gitcoinco/dgrants)

P.S. I'd love to here thoughts around how I post these updates moving forward...
[poll type=regular results=always chartType=bar]
* Future updates should be posted in this thread.
* Future updates should be posted in a new thread each time.
[/poll]

-------------------------

ceresstation | 2021-06-22 18:41:45 UTC | #13



-------------------------

phutchins | 2021-08-16 16:00:21 UTC | #16

For future weekly updates, please check the Meta-Governance category which is where we collectively post all workstream updates. Threads titled "Week in Governance Eddition #X" are what you should be looking for.

The most recent update can be seen [here](https://gov.gitcoin.co/t/gitcoin-dao-week-in-governance-edition-7/8229)!

-------------------------
