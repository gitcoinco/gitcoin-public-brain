---
id: 8116
title: "Request for Proposal: Decentralize Gitcoin Profiles"
slug: request-for-proposal-decentralize-gitcoin-profiles
category: open-discussion
url: https://gov.gitcoin.co/t/request-for-proposal-decentralize-gitcoin-profiles/8116
created_at: 2021-08-02T19:34:35.831Z
last_posted_at: 2021-12-09T15:15:52.399Z
posts_count: 9
views: 3578
like_count: 11
---

# Request for Proposal: Decentralize Gitcoin Profiles

<https://gov.gitcoin.co/t/request-for-proposal-decentralize-gitcoin-profiles/8116>
owocki | 2022-05-28 15:38:06 UTC | #1

Hello DAOfrens, 

This is request for someone to come up with a new decentralized experience for managing gitcoin profiles.

This includes [The reputation information on Gitcoin profiles](https://gitcoin.co/owocki)


As we progressively decentralize Gitcoin, the Gitcoin Holdings company is interested in decentralizing the data that we host on each end-user.  

An ideal candidate would be have the following principles:
1. Simplicity - products that do ONE THING and do it WELL.
2. Antifragility - Well-documented Decentralized products that our community can run without the centralized company.
3. Modularity - products that easily unix-style interoperate with each other.

An ideal proposal would: 

0. leverage IPFS or ceramic network/IDX to store information, and would make it easily navigable in non-Gitcoin contexts. 
1. setup a simple way of migrating data from the centralized site to the decentralized storage area.
2. provide some way to view SOME of the data in a decentralized way
3. does not need to include ALL gitcoin information, but could progressively move all information over.

Please include

1. Who are you
2. What is your proposal to build this
3. What is your timeline to build this
4. What do you need (funding, etc)

Please submit your proposal as a comment on the gov forum thread.

-------------------------

iamzubin | 2021-08-07 06:59:33 UTC | #2

Hey,

I am Zubin, I've been working on bounties from gitcoin for some time, i would like to help build this project and contribute to gitcoin platform.

I do have a couple of things in mind that could work out for this project

ipfs - orbitdb

unique identifier - erc721 token (if preferred on chain, for easy transfer)

About migration i can also write a simple migration page for everyone to access and migrate the data

this would also go well with the decentralized kudos system.

if required will provide a well documented timeline.

requirements

1.75-2 ETH

1.5 - 2 month timeline (with deployment and testing )

thanks

-------------------------

aturx | 2021-08-09 09:55:53 UTC | #3

Hello, I am AturX. I have been following the development of Gitcoin bounty and Ceramic for a long time.When 3Box came out, I felt that this kind of decentralized basic information was necessary.So we can see information from different Dapps in the same place.It's a cool experience.I will try to build a basic Profile through the DID of Ceramic to associate the basic information of GitCoin with the user's Ethereum information.

-------------------------

RisingStar-Web | 2021-08-09 23:56:24 UTC | #4

Hello, I am Roy Chong.
This is my first time working on bounties from gitcoin, but still, I have great experience in IPFS(Filecoin), and also easy to migrate data from centralized to decentralized storage areas.
During my career, I have worked on several DeFi user profile management and this will be very helpful for you.
I can build the decentralized gitcoin profile within a month with 5 ETH
Please let me know if you need more information
Thanks
Roy

-------------------------

Miendy | 2021-08-14 07:39:47 UTC | #5

Hey,

I am Mehdi, I have been looking across git coin and found your Bounty.

I am thinking of some things for this project.

Here is my id for 
Ethereum: 0x58FE0302112F0C54729A42732de9b845342DAc5f
Bitcoin: bc1qg47wgu7pag3fuua93f6x56yllr6p9wl8gjpldn

-------------------------

Huxwell | 2021-10-06 01:19:19 UTC | #6

Hello friend,

Here is my proposal:

**Who ?**
Cali "Huxwell", Software Engineer (very familiar with Ceramic & IDX)
Contributor @GitcoinDAO & @MoonshotCollective
Giovanni "NoName", UX/UI designer and Front-end developer
Contributor @MoonshotCollective

**What ?**
**dProfiles**, a dApp with a super cool UI like the Quadratic Lands colors/identity where users can:
- Browse all the profiles (search, sort and filters)
- Apply to join the GitcoinDAO
- Edit their [basic profile](https://developers.ceramic.network/streamtypes/tile-document/schemas/basic-profile/)
- Edit their Gitcoin Profile (custom JSON schema to be defined based on the current Gitcoin profile data structure)
- Migrate their [legacy 3BOX](https://developers.ceramic.network/streamtypes/tile-document/schemas/basic-profile/) account by using the new 3ID Connect SDK (this might require a custom migration script if the default migration tool doesn't work)

**When ?**
I'd like to start simple with the bullet points listed above, that would be achievable in **one month and a half** (three sprints of 2 weeks with recurrent meetings to ease the migration process and make sure we're always on track).

**Needs?**
- The current Gitcoin profile data structure and some sample data (JSON if possible)
-  Funding: 4 ETH or 2k GTC

-------------------------

owocki | 2021-10-07 16:58:34 UTC | #7

this seems like it'd be interesting/worthwhile to me.   

here is the current profile structure => https://github.com/gitcoinco/web/blob/master/app/dashboard/models.py#L2808

you can generate sample data by getting your local dev environment up & running.

-------------------------

frankchen07 | 2021-10-15 17:24:27 UTC | #8

Curious how this is going. 

It came up in the team call today that if this is done well, it could be the "LinkedIn" for crypto/blockchain folks.

-------------------------

trent | 2021-12-09 15:15:52 UTC | #9

where can i find the latest updates on this?

-------------------------
