---
id: 20899
title: "What's happening with the Grants stack indexer?"
slug: whats-happening-with-the-grants-stack-indexer
category: gitcoin-grants
url: https://gov.gitcoin.co/t/whats-happening-with-the-grants-stack-indexer/20899
created_at: 2025-06-12T15:35:51.985Z
last_posted_at: 2025-09-23T17:56:49.975Z
posts_count: 17
views: 2698
like_count: 43
---

# What's happening with the Grants stack indexer?

<https://gov.gitcoin.co/t/whats-happening-with-the-grants-stack-indexer/20899>
divine-comedian | 2025-06-12 15:35:52 UTC | #1

Hello folks, 

I have been loosely following the deprecation of Grants Lab and related services. 

As a result it seems the graphQL API used to fetch gitcoin projects appears to be shut down (along with all of the explorer links and project pages. 

https://grants-stack-indexer-v2.gitcoin.co/graphql

We were using this API to integrate Gitcoin projects into [DeVouch](https://devouch.xyz/). We'd love to keep offering this to all ecosystem users since we are also integrated with Human/Gitcoin passport.  Following the conversations of [Gitcoin 3.0: The Road to GG24](https://gov.gitcoin.co/t/gitcoin-3-0-the-road-to-gg24/20723) it seems there is a plan to have another GG round. I assume you will need some way to fetch and display projects to your users.

Do you plan to spin up another service for fetching Gitcoin projects via API?

-------------------------

deltajuliet | 2025-06-12 15:48:52 UTC | #2

Hi there @divine-comedian 

You can find more info on the sunset [here](https://gov.gitcoin.co/t/focusing-gitcoins-future-sunsetting-grants-stack-eol-may-2025/20333/7) and direct access to the data via our partner (OSO) [here](https://docs.opensource.observer/docs/integrate/datasets/#gitcoin).

The indexer is no longer being maintained, which I know isn't ideal. However the cost to do so outweighed the alternatives. As we move forward with GG24 - and creating a modular arena of funding mechanisms for our community - we'll have more info on data access, but for now this is the best place to pull from.

-------------------------

owocki | 2025-06-13 22:11:37 UTC | #3

hey @paul2 is there any chance the gardens allo builders round would fund someone who keeps the indexer running?

-------------------------

paul2 | 2025-06-13 23:24:14 UTC | #4

There's $1k left in the Builder's Fund: https://app.gardens.fund/gardens/10/0x1eba7a6a72c894026cd654ac5cdcf83a46445b08/0xd3345828914b740fddd1b8ae4f4d2ce03d1e0960/123

Definitely seems like a good use of those funds to me, if that's enough to keep it online for a bit.

-------------------------

deltajuliet | 2025-06-14 04:28:23 UTC | #5

It's public if anyone wants to review: https://github.com/gitcoinco/grants-stack-indexer-v2

If the community wants to pick it up to maintain, absolutely supportive! I would more than likely vote yes on any proposal that is interested in picking it up. Think it's a great path towards a UBI for our community + the path the GG (and beyond).

-------------------------

divine-comedian | 2025-06-15 16:32:54 UTC | #6

That would be amazing to have those services back up and running! Let us know if there's anything our team can do to help.

-------------------------

troopdegen | 2025-06-16 18:33:25 UTC | #7

regm everyone

At regen.tips we also noticed this service down. I checked the repo, I don't have the bandwidth to take maintain the project, but it's indeed unfortunate that this data will no longer be available if we can't keep it up.

What would be the major requirements/maintenance needs? We could do a community effort to find someone who can help with this.

-------------------------

owocki | 2025-06-16 19:32:37 UTC | #8

a group of us are coordinating a solution (or attempting to) here https://t.me/+g86YKl3tgFYyZDYx

-------------------------

abitrolly | 2025-06-19 02:13:57 UTC | #9

Is GraphQL calls really required? Ot it can be static data?

-------------------------

divine-comedian | 2025-07-09 08:26:42 UTC | #10

Hey everyone providing an update on this initiative. Giveth will take on the work for bringing the service back online. We are requesting 750 USDGLO to pay for development costs from the [Gitcoin Grants Garden](https://app.gardens.fund/gardens/10/0x1eba7a6a72c894026cd654ac5cdcf83a46445b08/0xd3345828914b740fddd1b8ae4f4d2ce03d1e0960)

The Giveth DevOps team will:

* Adapt the existing [allo-v2 repo](https://github.com/gitcoinco/grants-stack-indexer-v2/) deployment steps to align with Giveth’s DevOps tooling.
* Redeploy the Allo v2 indexer at the original endpoint: https://grants-stack-indexer-v2.gitcoin.co/graphql
* Maintain the service and cover all associated infrastructure costs.

We need to reach a certain voting threshold in order to pass the vote and receive the funding. If anyone has the **[Allo Patron NFT holders](https://www.allo.capital/patron)**, Giveth would love your support to bring the Allo v2 Indexer back online. 


### Vote Here :point_down: 
https://app.gardens.fund/gardens/10/0x1eba7a6a72c894026cd654ac5cdcf83a46445b08/0xd3345828914b740fddd1b8ae4f4d2ce03d1e0960/123/0x4ceda4f34d3512900cc03c813e7eff4619ce5cfa-18

-------------------------

LuukDAO | 2025-07-09 10:33:22 UTC | #11

Love the proactive action and collab here.

Having the indexer back up is essential. In favor!

-------------------------

thelostone-mc | 2025-07-12 11:30:41 UTC | #12

Just happened to see this ! 
@divine-comedian it might be worth exploring using the DB snapshot that was taken before we had retired the indexer. You could potentially just throw it behind a graphql endpoint and use it as is
If the goal is to also capture the future events emitted from Allo v2.1 , then you're on the right track IMO cause you'd have to stand up the service and get it up and running 

PS: this dashboard might make maintaining easier 
https://github.com/gitcoinco/indexer-dashboard

-------------------------

divine-comedian | 2025-08-26 13:52:48 UTC | #13

Hey everyone! Providing an update on our working bringing back the Indexer. Great News! 

We have brought back the grants stack indexer graphql endpoint and it can be used to query historical data of previous gitcoin grants data, including data for individual projects. 

The endpoint can be found here:

```
https://indexer.grantsstack.giveth.io/v1/graphql
```

We decided to only provide it with the necessary config to handle historical data. In order to allow it to process new data we would need some additional service API keys such as a Coingecko paid API and Envio API, which would exponentially increase the running costs of the service. I'm not sure if there is real demand for using the grants stack indexer for adding new data

If you need extra services from the indexer and are willing to chip in for these paid API keys or already have keys you'd like to donate, then reach out and we'd be happy to plug them in to upgrade the service. 

Great work team! We made it happen. 

Special shout out to [geleeroyale](https://x.com/krassvs) and @thelostone-mc for making it happen!

-------------------------

divine-comedian | 2025-08-29 16:22:05 UTC | #14

Hey friends, I just want to reiterate.. the Grants stack indexer is an *expensive* service to run, much more than we estimated. We're glad to be providing this to the community, however Giveth's finances are exceptionally tight. 

If you find value in this service and would like to contribute it turns out we have this pretty awesome [donation platform](https://giveth.io) where you can donate. 

You can contribute to the running of this service by making a donation or even setting up a recurring donation on Base or Optimism directly to Giveth. 

Here is the link directly to our donation page: 
https://giveth.io/donate/the-giveth-community-of-makers

-------------------------

krrisis | 2025-09-23 12:47:32 UTC | #15

Hey Mitch, so great that you guys did this.
Hope both Giveth & Gitcoin could tweet about this, totally missed it. 
 
However, it seems to be offline again now though, is this just a glitch or because of financial reasons?

-------------------------

divine-comedian | 2025-09-23 16:44:54 UTC | #16

It seems to be working on my end - are you using the graphQL endpoint? 

https://indexer.grantsstack.giveth.io/v1/graphql

ATM it seems to be working for me 
![image|690x405](upload://tt9Xrs2fPcuFSRiRqzQ8btnADhK.png)

We also did do a post here:
https://x.com/Giveth/status/1965421386975072644

But probably got lost in the noise of CT

-------------------------

krrisis | 2025-09-23 17:56:49 UTC | #17

ah no my mistake, it works!

and thanks for the post as well!

-------------------------
