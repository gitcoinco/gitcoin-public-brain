---
id: 13011
title: "Lessons Learned: A Look at Gitcoin Allo Alpha Rounds and the Path Forward with Gitcoin Passport"
slug: lessons-learned-a-look-at-gitcoin-allo-alpha-rounds-and-the-path-forward-with-gitcoin-passport
category: gitcoin-grants
url: https://gov.gitcoin.co/t/lessons-learned-a-look-at-gitcoin-allo-alpha-rounds-and-the-path-forward-with-gitcoin-passport/13011
created_at: 2023-02-20T14:22:23.178Z
last_posted_at: 2023-04-26T17:57:05.918Z
posts_count: 15
views: 4064
like_count: 39
---

# Lessons Learned: A Look at Gitcoin Allo Alpha Rounds and the Path Forward with Gitcoin Passport

<https://gov.gitcoin.co/t/lessons-learned-a-look-at-gitcoin-allo-alpha-rounds-and-the-path-forward-with-gitcoin-passport/13011>
erich | 2023-02-20 14:27:34 UTC | #1

The purpose of this post-mortem is to document the experience with Gitcoin Passport during Gitcoin Allo Alpha Rounds. The goal is to understand what went well, wrong, and what can be improved to prevent similar issues from happening in the future.

# Summary of the Experience

During the Gitcoin Allo Alpha Rounds, donors were unable to verify their unique identity for most of the program due to infrastructure instability with Gitcoin Passport. This resulted in a significant number of donors being unable to meaningfully participate in the program because they would not be able to verify themselves for matching funding for their donations.

When the infrastructure was accessible, we heard that Stamps were reset, and Passports often needed to be “re-anchored.” In the event users were able to verify stamps, they could then have their Passports scored to determine eligibility. 

# Background

Gitcoin Allo Alpha Rounds were pilot grant programs hosted by GitcoinDAO on the Gitcoin Allo Protocol, which is a new and more decentralized version of the grants product. The program was aimed at supporting innovative projects in the blockchain, open-source, and regen space, with a focus on increasing the impact and reach of such projects.

To ensure the fairness and transparency of the program, Gitcoin Grants operates on a democratic matching funding mechanism called Quadratic Funding. Based on previous experience, the grants programs may be manipulated by participants who create multiple accounts/wallets to influence the matching funding results. To address this issue, Gitcoin Passport was introduced as a decentralized identity verification tool that allows participants to prove their unique humanity through various identity providers.

During the round, Gitcoin Passport worked by linking a participant's digital identity to their Ethereum wallet address on the Ceramic Network, and then verifying their identity through trusted identity providers. This ensured that each participant can only have one account, and that their vote and donation are tied to their unique identity.

# Timeline of Experience

* 2023/01/18: Users reported issues with Ceramic Network, with a CORS policy blocking requests and 504 Gateway timeout error. The team attempted to debug, restarted IPFS, and waited for feedback from Ceramic.
* 2023/01/19: Users experienced issues with Passports and verification process. The team advised users to be patient and were compiling an issues log. Kyle reported a few steps in place to resolve the issue.
* 2023/01/20: A user reported difficulty with Twitter, Discord, and ENS verification stamps. Kyle asked for an update and Gerald mentioned they were close to a fix.
* 2023/01/21: Ceramic network became unhealthy causing an outage and issues with the Gitcoin Passport App. Gerald worked on fixing the problem and deployed a fix for the error pop-up.
* 2023/01/22: The team deployed a fix for the Ceramic Network Error and moved the Passport App to AWS Amplify in an effort to resolve the server side errors we were seeing. Some web2 stamps didn't work due to the domain, but they would be fixed with a domain change. Gerald identified a bug in the reset flow causing an infinite loop error.
* 2023/01/23: The issue of chunks not loading persisted, with a high rate of 4xx errors in Amplify. Gerald sought assistance from Kammerdiener for the issue, which only affected the Passport App.
* 2023/01/24: Two separate issues were discussed regarding the Ceramic Network Error, one for the Grant Explorer page and one for the Gitcoin passport page. The team tried to improve the situation by increasing the number of worker threads.
* 2023/01/25: Some users reported slow performance and issues with loading their passport. Gitcoin pushed an upgrade for the Ceramic node. Another user reported that stamps could not be verified with "too many open files" error.
* 2023/01/26: The team attempted to resolve issues with Passport Stamps and timeouts by restarting IPFS and Ceramic nodes and considered a caching layer.
* 2023/01/27: Passport connections continued to time out on the Gitcoin platform. Gerald restarted the nodes and considered scripting a restart every 3 hours. Kammerdiener suggested using AWS commands for a redeploy. Product and engineering teams start considering and exploring a hotfix to the issues by migrating Passport data over from Ceramic to a centralized “cache”database.
* 2023/01/28: Passport app still not working, despite servers being restarted every 2 hours. The team attempted to resolve the issue by restarting nodes but with no success.
* 2023/01/29: Many errors are reported by the Passport app and in Datadog. The team tried restarting the Ceramic node but with no success. The idea of using a second Ceramic node is discussed, but it will result in a delay as the node has to sync. Good progress has been made on cache, but the challenge remains in migrating to a new data strategy. Passport app still not working for some team members.
* 2023/01/30: Team works on fixing Passport app and Ceramic Network Error. They try various methods including changing ENS stamps. Joel from Ceramic suggests turning off pub-sub could solve the issue. New build deployed and team monitors logs, but couldn't find any issues. Some team members succeed in removing/adding stamps, while others face trouble. The team tweets they're working on the issue, but node is not functioning properly again by the end of day. Team notices a wave pattern of requests trending downwards and erroring out, then spiking back up.
* 2023/01/31: Ceramic returns to problematic state. The team decides to switch to its own database for Passport instead of relying on Ceramic. The community is informed of the change and development begins to migrate Passport away from Ceramic as the primary database.

# The Triggering Event or Root Cause of the Incident

![|624x183](upload://ilxhuHAM9CKyAsZ4NpgJzu2aqaV.png)

Gitcoin Passport requests on Ceramic in Gitcoin Grants Round 15, Source: Ceramic team

The incidents that occurred during the recent Passport app were a result of increased load on the Ceramic node. Although the total number of participating donors was lower in this round compared to Grants Round 15, the number of write requests to the Ceramic node was higher due to the fact that a solid Passport score (derived through verifying various stamps) was mandatory in order to receive matching, while in GR15 it was just a boost.

![|624x351.63442150809897](upload://lFQu3lNvNpJDUCteWyEMYhZSUiO.png)

Gitcoin Passport requests on Ceramic in Gitcoin Allo Alpha Rounds, Source: Ceramic team

Despite efforts to resolve the issue by restarting the Ceramic node and its underlying IPFS nodes, the problem persisted. The Ceramic and Passport teams observed a wave pattern of failing requests trending downward and then spiking back up, but were unable to identify the root cause of the issue and corresponding fix during the round.

# Customer Impact

The incident had a significant impact on Gitcoin's brand, with many users expressing frustration on platforms like Twitter and the Gitcoin Discord. The user impact of the incident was that the Passport app was not working and loading properly, causing inconvenience for the users, especially for those participating in the Gitcoin Allo Alpha Rounds. The team worked to resolve the issue and communicate with the community about the changes being made.

![|624x372](upload://mEA3w8VW720sa9ZkBjKDD0fj3WP.jpeg)

Source: https://twitter.com/EnormousRage/status/1618922283829178369?s=20

# Direct Outcomes

As a result of the ongoing issues with the Ceramic infrastructure, the team decided to migrate Passport to its own database instead of relying on Ceramic as the primary database. This change in plans allows users to verify their participation after the round ended within a grace period.

In other words, we have taken steps to migrate the Passport app and Scorer so that they read from and write to our centrally hosted database instead of Ceramic. We plan to work on migrating Passports to Ceramic in the background.

# Preventive Measures in Future Rounds

To prevent similar issues from occurring in future rounds, we have identified the need for rigorous load testing to be conducted prior to a round to reveal potential issues with Passport. We are taking the following preventive measures:

* Relying on a new PostgreSQL instance for the Gitcoin Passport as the primary cache database.
* Exploring on-chain solutions for Passport to benefit from the reliable uptime and data availability on blockchains.
* The Ceramic team acknowledges the experienced instability and supports a primary cache database mitigation proposed as an intermediate solution. Meanwhile, Ceramic is committed to conducting rigorous load testing and making improvements to ensure the stability of the Ceramic system for future rounds. Ceramic is dedicated to the Gitcoin Passport mission and is determined to make Gitcoin Passport reliably composable across web3.

# Risk and Mitigation Strategies

1. Improve communication and attention to issues:

  * Increase transparency by providing more frequent updates to the community about the status of Gitcoin Passport and any issues that arise.
  * Enhance the monitoring and alert systems to quickly identify and address any potential issues.
  * Implement a protocol for reviewing and addressing community feedback to improve Gitcoin Passport

2. Ensure reliability and scalability of centrally hosted Gitcoin Passport database:

  * Conduct regular audits and testing of the database to identify potential issues and ensure that it is functioning properly.
  * Implement redundancy and backup measures (i.e., via Ceramic, on-chain solutions, and more) to minimize the risk of data loss.
  * Evaluate the need for additional infrastructure and capacity to support future growth.

3. Enhance collaboration with Ceramic team:

  * Establish clear lines of communication and collaboration with the Ceramic team to prevent similar issues from occurring in the future.
  * Regularly review and assess Gitcoin Passport’s architecture and infrastructure to ensure compatibility and reliability with the Ceramic network.
  * Foster an ongoing dialogue with the Ceramic team to identify potential risks and vulnerabilities and develop appropriate mitigation strategies.

-------------------------

Maxwell | 2023-02-21 18:21:48 UTC | #2

This is amazing! Thank you so much for taking the time to write this up, Erich. Lots of learnings, and excited for Gitcoin to continue to grow, develop, and deliver outstanding products. 

Thanks again for the honest, vulnerable, and detailed reflection here.

-------------------------

tjayrush | 2023-02-22 00:42:11 UTC | #3

[quote="erich, post:1, topic:13011"]
relying on Ceramic as the primary database.
[/quote]

This is an excellent article. Thanks so much for posting. I wanted to highlight the above quote. That's the root of the problem.

**...writer steps up on soapbox**

IPFS, Ceramic, Ethereum are peer-to-peer. By funneling all users through a website, you're taking a many-to-many relationship and forcing it through a many-to-one-one-to-many relationship. You've eliminated a massive amount of connections. 

Plus, you've removed the fact that in a true peer-to-peer network each participant brings some of their own resources to the party (in the form of storage and/or compute).

It's not surprising that you had to add a SQL database. SQL databases are designed (very well) to serve as the `to-one-one-to` in the above relationship.

The trouble isn't that Ceramic is not a good database, nor is the solution that Ceramic needs to become a better database. The trouble is that your app isn't peer-to-peer.

That's where your efforts should be spent.

**...writer steps down**

-------------------------

kyle | 2023-02-22 01:43:43 UTC | #4

[quote="tjayrush, post:3, topic:13011"]
The trouble is that your app isn’t peer-to-peer.
[/quote]

I appreciate this! I want to confirm I am understanding the feedback here. I suspect that by posting these details on chain, might help resolve this? I would love your thoguhts on what making Passport "peer to peer" means to you. :pray:

-------------------------

tjayrush | 2023-02-22 04:01:51 UTC | #5

It's very complicated, I think. And it requires the "peers" to be *actual* "peers." By that, I quite explicitly mean, that the normal, web 2.0 "client-provider" model has to be upset.

It's a radical position, I know, but I think that as long as "developers" build "systems" using web 2.0 APIs that "serve services to humans" you will never create a true peer-to-peer system.

The word "peer" means something. I think it means "equal peer." In a provider-client relationship the "peers" are not equal. The "provider" sets the rules of the game. The "provider" determines what happens to the data -- because the data is physically on the "provider's" hardware. The "provider" pays for the hardware.

In a true peer-to-peer system, every peer provides resources (compute, hard drive space, etc.) and carries their fair share of the burden. This massively lowers the cost of the system for the provider. That's important. If the provider is able to massively lower their costs, they're not so heavily pressured to monetize the user. If a user is being monetized, she's not a true peer.

As I said above, it's very complicated. But, I think, if we never start the process and continue to build on top of what I call "an old-fashioned web 2.0 tech stack," we'll never solve the problems we're trying to solve.

A really amazing place to start thinking about this stuff is in this document: https://www.inkandswitch.com/local-first/. It's one of the things that lit my mind on fire five years ago.

By the way -- I did indicate above that I was on a soapbox. I know what I'm saying is a bit radical and that it's not easy, so there's that.

-------------------------

DisruptionJoe | 2023-02-22 14:31:02 UTC | #6

I think we can start by running our own node with Trueblocks indexing. Then, we can realize the efficiency and performance gains along with the cost reduction of the decentralized storage for data. Then perhaps we begin acquiring peers on the network.

Every program manager with more than say $100k has a pretty strong incentive to run a peer if we can package the image properly to make it as easy as possible.

-------------------------

pcfreak30 | 2023-02-26 00:26:30 UTC | #7

Ironically my project (Lume Web, lumeweb.com), which is also a Gitcoin project grantee, is innovating development on true web3 infrastructure as I see the same problems. We call everything web3, but it's really just web2 + blockchain (even AWS was used here). I, however, cannot say anything I'm engineering would have solved these issues, though my tribe is a decentralized storage network :stuck_out_tongue: .

I find this writeup interesting as it exposes bottlenecks in Ceramic at scale that force the need for a web2 centralized system that just talks to a crypto/web3 database to get information.

Broadly speaking the more decentralized something is, the more inefficient it is by definition. So I might call the passport a `self-hosted identity system that uses web3 technology`.

-------------------------

tjayrush | 2023-02-27 02:18:00 UTC | #8

[quote="pcfreak30, post:7, topic:13011"]
Broadly speaking the more decentralized something is, the more inefficient it is by definition.
[/quote]

I don't agree with this. I would slightly modify it to say, "If one tries to force a decentralized system through centralized pipelines, then this will be more inefficient that both pipelines."

If a truly decentralized system is working in a truly decentralized way, it's significantly more efficient than a centralized system. In both cost (per participant) and speed (if well designed) and especially resiliency and censorship resistance. It depends what you're optimizing for.

-------------------------

pcfreak30 | 2023-02-27 02:45:05 UTC | #9

[quote="tjayrush, post:8, topic:13011"]
It depends what you’re optimizing for.
[/quote]

It depends on what you are targeting, but I view this more from a blockchain POV. The more centralized leadership that exists, the faster you innovate. But the more decentralized (BTC) the harder it is to agree on the time of day and thus no leadership at all.

-------------------------

DisruptionJoe | 2023-03-10 15:34:35 UTC | #10

Is there a good way for us to estimate the minimum viable decentralization needed for something like Ceramic or Trueblocks to operate efficiently for our use case? 

For example, could we use math/engineering to know that "if we had 5 or more nodes, we wouldn't have run into passport issues on ceramic until > 60,000 donors accessing it)

Also, how does a truly decentralized system handle ddos attacks? Is it simply resiliant because of the increased needs to ddos *all* of the nodes?

-------------------------

tjayrush | 2023-03-10 21:16:15 UTC | #11

It's very hard for me to express these ideas, so you'll bear with me as I stumble through...

1) I'm not sure add more "trueblocks" nodes would ever help the situation. TrueBlocks is local first and intended to support a single user. In that case, it's very fast because it's not rate limited or shared.

2) If you're hoping to support many "data scientists' or many 'users,' then perhaps a local-first, single-user-focused tool is not quite right.

3) Web 2.0 SQL databases are excellent at serving data to many clients and many users.

4) Blocks only appear once every 12 seconds, so there's tons of time to process data.

I've been thinking lately that TrueBlocks should not be seen as an API server. It's not that. It's a data extraction tool.

One of the tools we're working on is called 'monitoring' whereby TrueBlocks watches the end of the chain, extracts any needed data at each new block and puts it somewhere, and then goes to sleep waiting for the next block.

"Putting it somewhere" currently means writing the data to a `.csv` file on disc, but it could be modified to push the data into a regular web 2.0 SQL database.

In that way, you can use TrueBlocks to extract deep data and not use it for something it's not good at (serving data to many users). You can use regular, old-fashioned SQL API server to serve as many users as you like.

As far as decentralization, SQL (of course) doesn't help there at all, but there could be some sort of post processing done (on the SQL database) to create any sort of structures one might like. TrueBlocks itself already decentralizes the index of addresses, so simply by running it as a `monitoring` tool, it would decentralize the index by creating, pinning and publishing the IPFS hashes.

As I said, bear with me as I try to learn how to articulate the ideas behind TrueBlocks. They're subtle and they don't work the way we might expect.

-------------------------

griff | 2023-03-16 11:12:06 UTC | #12

[quote="erich, post:1, topic:13011"]
To prevent similar issues from occurring in future rounds, we have identified the need for rigorous load testing to be conducted prior to a round to reveal potential issues with Passport.
[/quote]

I think that is the big one... basically a dress rehearsal before launch will find all the catastrophic issues... and lots of the minor ones too.

Overall though, if you look passed this glaring issue there were a lot of wins with passport this round, I am VERY bullish on Passport, and know several groups excited to build on and fork. Don't let one oversight cloud the incredible leap in meta-identity that you all are making.

-------------------------

skilesare | 2023-04-26 13:28:39 UTC | #13

Was this resolved for the Beta round?  Is a passport being used?  We need a solution for Proof of Humanity over on the IC and with tECDSA coming online I'd like to explore if we could plug into Passport easily or not.

-------------------------

kyle | 2023-04-26 15:08:47 UTC | #14

It has been! We would love your feedback as you start to use the updated Passport experience.

-------------------------

ale.k | 2023-04-26 17:58:16 UTC | #15

I'm late on the uptake here- but finding this now and finding it beautifully expressed.

Yes- our plan is to use best-in-class web2 solutions to surface on-chain data as it is available to us.  Doing this in duplicate (or even triplicate) is our contribution to general chain stability and trust-but-verify methods for treating stamp providers.

When the web3 solutions that can serve data pipelines for near-live data and anomaly detection exist - I hope we'll be the first to jump... But right now we are committed to independently verifying on-chain data (with TrueBlocks+Erigon suite) and providing transparency in our usage of on-chain data (i.e. through relational db, neo4j environment, bigquery dump, etc - we will get the data to the interested parties.)

-------------------------
