---
id: 8114
title: "Request for Proposal: GitcoinDAO.com website"
slug: request-for-proposal-gitcoindao-com-website
category: open-discussion
url: https://gov.gitcoin.co/t/request-for-proposal-gitcoindao-com-website/8114
created_at: 2021-08-02T19:17:24.947Z
last_posted_at: 2021-08-30T19:44:45.316Z
posts_count: 21
views: 4765
like_count: 22
---

# Request for Proposal: GitcoinDAO.com website

<https://gov.gitcoin.co/t/request-for-proposal-gitcoindao-com-website/8114>
owocki | 2022-05-28 15:38:06 UTC | #1

Hello DAOfrens,

This is a request for someone to come up with a homepage for GitcoinDAO.com 

An ideal candidate would be 
- aesthetically pleasing and [on brand](http://gitcoin.co/press) for Gitcoin
- would help a newcomer navigate GitcoinDAO, including the Gitcoin mission, how to get involved in governance, how to earn/use GTC, etc.
- be decentralized in such a way that governance (or someone with delegated legitimacy from governance) could control the content.

As we progressively decentralize Gitcoin, and as Gitcoin Holdings takes a back seat, I imagine that this content will become increasingly important for the GitcoinDAO/ecosystem.

Would any of you be interested in developing a GitcoinDAO homepage?  If so please submit a proposal by September 15th 2021.

Please include

1. Who are you
2. What is your proposal to build this
3. What is your timeline to build this
4. What do you need (funding, etc)

Please submit your proposal as a comment on the gov forum thread.

-------------------------

DisruptionJoe | 2021-08-03 21:00:48 UTC | #2

The basics of what would need to be on the page are [here on this Notion](https://www.notion.so/gitcoin/GitcoinDAO-be541eac15354fdc94655965aa7fbc39).

-------------------------

ceresstation | 2021-08-05 17:06:59 UTC | #3

What if we started iterating on the quadratic lands site? It feels like that's the closest place beyond the forum that has relevant information about the DAO + most stewards are already listed there.

-------------------------

owocki | 2021-08-05 17:31:42 UTC | #4

the main issue is that gitcoin (the company) hosts it.  for this to be truly decentralized it should not be hosted by gitcion (the company) but should be owned/maintained by governance

if someone wants to leverage any of the code/art from quadraticlands.com site that is fine by me.  i think that its a good start.

-------------------------

Developer-piyush | 2021-08-06 15:26:13 UTC | #5

I think Hosting gitcoin DAO website on Akash Network (Decentralized cloud) one of the sponsor of GR10 would be great idea..

-------------------------

Developer-piyush | 2021-08-06 15:32:27 UTC | #6

I think Hosting gitcoin DAO website on Akash Network (Decentralized cloud) one of the sponsor of GR10 would be great idea… If you all agree then i could talk with the CEO of akash network and he will surely agree on that.

@owocki  Sir can i have some more details like what gitcoindao is for, this will help me to plan what needs to be done!

I saw notion website, its just a simple page where some updates about events and gitcoin governance details listed! Do we need to just make a website where one can have update about events and all the links to resources of gitcoin??

Thank you

-------------------------

owocki | 2021-08-09 14:22:27 UTC | #8

> Sir can i have some more details like what gitcoindao is for

https://gitcoin.co/blog/introducing-gtc-gitcoins-governance-token/
http://quadraticlands.com/
https://gov.gitcoin.co/t/ecosystem-mapping-discussion/8123

or just browse the forum

-------------------------

owocki | 2021-08-09 14:23:04 UTC | #9

> **GitcoinDao for climate change:**

You you submit this as a seperate topic?  Seems worthwhile but unrelated to current thread.

-------------------------

Developer-piyush | 2021-08-09 15:02:12 UTC | #10

Yes sir i submitted this as a separate topic on gov.gitcoin.co
By mistake i replied to this thread!

For this thread i will update my proposal soon before deadline.
Thank you

-------------------------

owocki | 2021-08-16 15:44:12 UTC | #11

[quote="ceresstation, post:3, topic:8114, full:true"]
What if we started iterating on the quadratic lands site? It feels like that’s the closest place beyond the forum that has relevant information about the DAO + most stewards are already listed there.
[/quote]

After conferring with Scott a bit on the team call today, I think this would be a direction we'd be interested in funding.  Its easy to know what the site looks like (1:1 transfer of assets over) which should hopefully reduce discussion of what the content is.

@Developer-piyush would you be interested in porting gitcoin.co/quadraticlands to a decentralized location?

-------------------------

Developer-piyush | 2021-08-16 16:35:43 UTC | #12

Thank you so much sir, i am very much interested in porting this to a decentralized location!
In my experience this would be great to port this to Akash, I will discuss this with the akash team and will update here soon!

Can i please have reference to code of quadraticlands so that i can check what exact tech stack is being used behind the scene, this will help me to structurize the containers accordingly and port this to akash!

Thank you

-------------------------

owocki | 2021-08-16 16:44:45 UTC | #13

sure its https://github.com/gitcoinco/web/tree/master/app/quadraticlands

most of the frontend code is here https://github.com/gitcoinco/web/tree/master/app/quadraticlands/templates/quadraticlands

this is whats served at http://quadraticlands.com/

-------------------------

anthonyrosa | 2021-08-18 00:27:34 UTC | #14

Super cool project, will take a look at this and consider a proposal.

-------------------------

gavin | 2021-08-18 02:59:42 UTC | #15

Hi, I'm a community dev lead from Crust Network. We are very interested in building a homepage for GitcoinDAO, hosting and continuously deploying it in a completely decentralized way.

Some well-know DAPPs like uniswap-interface or ipfs-docs are already hosted on Crust Network, like by using crust-pin-job in the repository's github workflow. Similarly but further, we can provide a more decentralized solution for GitcoinDAO portal in following ways:

1. (Development) Build the portal in a way that can be exported as static HTML website

2. (Hosting) Host the portal in Crust Network, as we did for uniswap-interface. This can be done by using Github Action and crustio/ipfs-crust-action

3. (Domain Name) Use ENS (Ethereum Name Service) to always point to latest website release. Or, if ENS solution is not feasible or preferred, using dnslink and ipfs gateway with a traditional DNS domain. Dnslink/IpfsGateway/Clouldflare is a preferred solution from our point of view, as we are more experienced with it.

In fact, besides GitcoinDAO portal, we'd like to contribute to the whole decentralization work of Gitcoin, to decentralizedly store various kinds of data of Gitcoin. But GitcoinDAO portal would be a good starting point.

Pls let me know if you are intrested in our proposed solution. Thanks.

-------------------------

Developer-piyush | 2021-08-18 06:13:20 UTC | #16

Update: Sir i have already started working on porting frontend to decentralized location! 
After that if backend is required to be integrated then i will be needing some help from gitcoin development team.

Thank you
PIYUSH CHOUDHARY

-------------------------

Developer-piyush | 2021-08-18 16:56:11 UTC | #17

**Progress:** Sir, i have successfully deployed the webapp to decentralized location i.e Akash network

Still some work left but i  thought to  give you an update about the progress here!

**App link:** [Click here](http://857tp1qb31bkh1ncp6f3vsbb0s.ingress.provider-0.prod.ams1.akash.pub/)

**Github:** [Click here](https://github.com/Developer-piyush/Gitquad)

Sir, let me know what do you think about this.
Thank you

-------------------------

owocki | 2021-08-18 18:21:42 UTC | #18

Seems like a promising prototype.  What would have to be true to migrate all the pages over?

-------------------------

Developer-piyush | 2021-08-18 18:34:15 UTC | #19

Sir, I have migrated most of the pages, working on rest: i think only mission part left!

But will soon migrate 100% pages!

Thank you

-------------------------

Developer-piyush | 2021-08-19 18:10:29 UTC | #20

Good evening sir, just to give you an update, task is **completed**, please have a look.

**App link:** [Click here](http://857tp1qb31bkh1ncp6f3vsbb0s.ingress.provider-0.prod.ams1.akash.pub/)

**Github link:** [Click here](https://github.com/Developer-piyush/Gitquad)

-------------------------

owocki | 2021-08-30 19:44:42 UTC | #21

Hey all, closing this thread.

Please feel free to post to thread here if ur interested to building this: 

https://gov.gitcoin.co/t/pre-proposal-call-for-discussion-what-should-we-do-with-dropped-tokens/7359/15
https://gov.gitcoin.co/t/request-for-proposal-decentralize-gitcoin-quests/8120/6

-------------------------

owocki | 2021-08-30 19:44:45 UTC | #22



-------------------------
