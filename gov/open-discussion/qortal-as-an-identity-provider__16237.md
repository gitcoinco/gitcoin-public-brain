---
id: 16237
title: "Qortal as an Identity Provider"
slug: qortal-as-an-identity-provider
category: open-discussion
url: https://gov.gitcoin.co/t/qortal-as-an-identity-provider/16237
created_at: 2023-08-10T15:37:48.473Z
last_posted_at: 2023-11-01T18:38:55.090Z
posts_count: 9
views: 4333
like_count: 18
---

# Qortal as an Identity Provider

<https://gov.gitcoin.co/t/qortal-as-an-identity-provider/16237>
QuickMythril | 2023-08-10 15:37:48 UTC | #1

I am a supporter of both Idena, recently added to the Gitcoin Passport, as well as Qortal.  They are the only two blockchain projects I have found, aside from Neuralium which has been discontinued, which attempt to limit mass account farming, without requiring any sort of KYC.  Qortal requires new community members to get a "minting key" from an existing account, which is Level 5 or higher.  This is similar to how Idena validation first requires an "invite" from Verified/Human accounts.

I briefly mentioned this in the Gitcoin Discord, and seemed to get a positive response from @lucian but I figured it would be appropriate to share this with everyone before starting to work on an implementation.  I'm happy to answer any questions from the Gitcoin community, or hear any concerns or thoughts on this idea.  I will start with my reasoning for the benefits of this collaboration.

- For the Qortal community, an overview of the Gitcoin Passport:
The Gitcoin Passport is a system that can aggregate account info from various identity providers and other services.  The idea is to use a variety of metrics to determine how likely it is for any given account to be a unique person or not.  For example, I would be more likely to give someone a minting key if they were able to show me an address they control, with a relatively higher passport score.  I would like to add Qortal as one of the providers, which would allow higher level Qortal accounts to be worth a certain number of points on the passport.  While we cannot completely ensure that any one person has only one minting account, I think it still indicates a degree of uniqueness.  Here is a list of the other platforms that are included, and their scores and requirements, for comparison.
https://support.gitcoin.co/gitcoin-knowledge-base/gitcoin-passport/common-questions/how-is-gitcoin-passports-score-calculated

- For the Gitcoin community, an overview of Qortal:
Qortal is a blockchain based platform, focusing on complete decentralization, which includes private or group chat, peer-to-peer websites and apps hosting, multi-asset wallets with native cross-chain trades (no wrapped coins), and more.  It's fully open for anyone to build anything they want, without owners, KYC, or censorship.  Only you can control your content, and choose what you want to see or not see.  The chain is secured by a custom consensus protocol that differs from both PoW and PoS, to prevent those with more resources (mining hardware, or coins to stake) from gaining more influence over the network.  To take part in consensus, you need to have a node running, with a minting key.  Anyone level 5 or higher can create a key to share with others, and this is meant to help the network grow organically, in a sense like a trust network.  To reach Level 5, an account has to be online and minting for 244,000 blocks.  With a block time of about 1 minute, they would be supporting the network for over a year.  Here is a somewhat more technical explanation of how the minting and leveling systems work in detail.
https://wiki.qortal.org/doku.php?id=how_qortal_s_consensus_works
https://wiki.qortal.org/doku.php?id=leveling_system

(Copy of this discussion on the Gitcoin Passport GitHub repository)
https://github.com/gitcoinco/passport/discussions/1572

-------------------------

quaylawn | 2023-08-10 19:08:09 UTC | #2

Thanks for sharing this! As a non-techie, this is beyond my realm of expertise although I appreciate you posting

-------------------------

erich | 2023-08-11 09:58:38 UTC | #3

gm @QuickMythril, thank you for your detailed proposal and for sharing more about Qortal. We appreciate the effort you've put into explaining the potential benefits of integrating Qortal's leveling system with Gitcoin Passport. Before we proceed further, we'd like to gather some additional information to better understand the opportunity and ensure that any potential integration aligns with our goals, especially given the low dimensionality of our model.

1. **Understanding Qortal's Consensus Mechanism**:
  * In layman's terms, how does Qortal's consensus mechanism ensure that each account is unique and prevents mass account creation?
  * Could you briefly explain the role of "key distance" and "minter level" in the timestamping of a minted block in Qortal?
2. **Qortal's Leveling System**:
  * How does Qortal's leveling system encourage users to participate and stay committed over the long term?
  * What are the main benefits a user receives as they progress through Qortal's levels?
3. **Integration with Gitcoin Passport**:
  * How do you envision the integration of Qortal's leveling system with the scoring mechanism of Gitcoin Passport?
  * Given our aim to maintain a low-dimensional model for Gitcoin Passport, how would Qortal's multi-level system be accommodated?
4. **User Engagement and Growth**:
  * Could you share the current number of active minters on Qortal and a breakdown across the different levels?
  * What has been the growth trend of new minters joining Qortal in recent times?
5. **Use Cases and Applications**:
  * Are there specific platforms or applications currently leveraging Qortal's leveling system for identity verification or other functionalities?
  * Could you provide an example of a successful use case of Qortal's leveling system outside of the Qortal platform itself?
6. **Future Plans and Development**:
  * Are there upcoming features or modifications to Qortal's leveling system that we should be aware of?
  * How do you perceive the potential collaboration with Gitcoin Passport benefiting the broader Qortal community?
7. **Technical Aspects**:
  * From a technical perspective, how would the integration process unfold? Are there challenges or prerequisites we should consider?
  * Given Qortal's emphasis on minters being consistently online and synced, how would this factor be represented in the Gitcoin Passport score?

Your insights will be invaluable in helping us assess the feasibility and potential benefits of this integration. We aim to ensure that any additions to Gitcoin Passport are meaningful and align with our overarching objectives.

Thank you for your patience and understanding.

-------------------------

QuickMythril | 2023-08-23 23:06:45 UTC | #4

Hello, I have been meaning to respond to this for a while, but putting it off with various other things going on.  Was also talking with others in the Qortal community and wanted everyone to get a chance to give their feedback.

To answer some of your questions, I will make a slight comparison with Idena.  There are foundational similarities despite being very different platforms, and it's something that others involved with the Passport may be familiar with.  I have also seen some planning for Humanode integration with the Passport.  I'm not sure what data would be checked there, but they seem to have similar goals too.  Differences would be Humanode using biometrics, while Qortal is more of a trust network like BrightID, being used to allow mining/minting, like Idena without the captcha system.

**Understanding Qortal’s Consensus Mechanism:**
> In layman’s terms, how does Qortal’s consensus mechanism ensure that each account is unique and prevents mass account creation?

Trying to avoid PoW in order to allow anyone to participate without specialized hardware, has proven to be a challenge and as the project grows, there have been compromises made with that goal.  Minting uses MemPoW (memory hard proof of work) which prevents someone from running a large number of minting accounts on one machine.  This still requires some computer resources while allowing people to use lower powered devices to run a node.  There is no identifying information or KYC linked to a minting account, so there is not a guarantee they are unique.  The method of sharing minting keys within the community, from existing members to new ones, is a limiting factor on new account creation.  No one can just ask for 100 minting keys to start a farm.  The community would likely not support that, in addition to the fact that people can only create a few keys at a time.  The block consensus is weighted towards higher level accounts to some degree, which means even if someone had 100 minting accounts, they would not be able to influence the network too strongly.

> Could you briefly explain the role of “key distance” and “minter level” in the timestamping of a minted block in Qortal?

As each new block has a random hash, that is compared with the public minting key of any potential minters (both converted to numerical values).  This allows whoever comes closest to the random hash to be weighted towards a successful block.  Minter level is also factored in, with a higher level reducing that "distance" value.  Whichever block candidate has the best value would be the next block to be confirmed on the chain.  As for how that affects the timestamp directly, from what I understand, when the value is higher, it's less trusted and requires longer period of time to be allowed.  That's actually a bit beyond my technical understanding.  Looking at the code, it's not clear to me, but I will see if I can get a better answer from the devs.

**Qortal’s Leveling System:**
> How does Qortal’s leveling system encourage users to participate and stay committed over the long term?

As with most mining systems, people are rewarded for their contributions to maintain and secure the network by running a node.  The term "decentralized proof of stake" has been used for Qortal's system in the past, though it's more like staking time than coins.  In a sense, minting is "autopooled" so that everyone who is online gets a share, regardless of who actually signs the block.  Higher level accounts get a larger share, so there is incentive to support the network long term to earn more rewards.
> What are the main benefits a user receives as they progress through Qortal’s levels?

Aside from minting QORT rewards, the number of blocks minted (which corresponds to the levels) can be used for weighting any on-chain community decisions.  There is a polling system (similar to Idena oracles) which allows anyone to create a poll and take votes.  It's flexible like the Passport because whoever counts the vote can decide to use any metric they like.  For example, excluding Level 0 accounts so that people cannot spam the votes.  The development team is committed to using this system for feedback on major platform changes, which means people will have more influence on the direction of Qortal as they increase levels.

**Integration with Gitcoin Passport:**
> How do you envision the integration of Qortal’s leveling system with the scoring mechanism of Gitcoin Passport?

I think it would make sense to award a number of points on the Passport, based on someone's minter level.  Perhaps one point for levels 1-2, another for 3-4, and another for 5 and above.  There could be other indicators of natural human activity aside from levels as well, for example points for registering a name, making trades or other transactions, or publishing content to the network.

> Given our aim to maintain a low-dimensional model for Gitcoin Passport, how would Qortal’s multi-level system be accommodated?

If I understand what is meant by "low dimensional" it seems that this integration would align with that goal.  If minter level is what earns the Passport stamp, then the only metric being measured for that would be the amount of blocks minted, which just is dependent on running a node for longer time.

**User Engagement and Growth:**
> Could you share the current number of active minters on Qortal and a breakdown across the different levels?

It's not easy to determine exactly how many minting accounts are enabled and being used regularly, without some analysis of the chain over time, but it's possible to check the current info.  Right now I am seeing about 7000 minting accounts, with the following distribution:  Level 1: 1000, Level 2: 2000, Level 3: 1000, Level 4: 1500, Level 5: 1000, Level 6: 300, Level 7: 50.

This information can also be found using the following API call:
https://api.qortal.org/addresses/online/levels

> What has been the growth trend of new minters joining Qortal in recent times?

This is also hard for me to estimate accurately, but we have had steady growth over time, with more new people joining after new feature releases, or interviews with other communities.  Generally we have a wave of new accounts, with some getting more involved than others, and some staying longer term while some lose interest over time.  The platform is under constant development, and we're always looking to collaborate with other projects, so I expect to see more growth in the future as well.

**Use Cases and Applications:**
> Are there specific platforms or applications currently leveraging Qortal’s leveling system for identity verification or other functionalities?
> Could you provide an example of a successful use case of Qortal’s leveling system outside of the Qortal platform itself?

At this time there is no external platform or 3rd party services that integrate with Qortal to make use of the minter levels in that way.  I have not yet personally found anything beyond the Passport where that seems appropriate, but I am open to exploring that further.

**Future Plans and Development:**
> Are there upcoming features or modifications to Qortal’s leveling system that we should be aware of?

It's worth noting that Qortal cannot perfectly prevent sybil behaviour, though I think it does a good job of working towards that goal.  However, there have been patterns of activity which indicate some users creating multiple minting keys for themselves, against the intent of the system.  This caused the dev team to make a difficult decision to algorithmically apply a "blocks minted penalty" to any flagged accounts.  This was not without some controversy and much discussion in the community, but in the end it was supported as being good for the network.  If necessary, this could be applied again in the future, and that possibility may also deter that type of behaviour in first place.  Any other changes being considered so far, would be to increase decentralization, like giving the Founder accounts less influence.

> How do you perceive the potential collaboration with Gitcoin Passport benefiting the broader Qortal community?

I think it will give people recognition for supporting a decentralized network, as well as bring more awareness and growth to the project from those outside the existing community.  It will also be an opportunity for them to learn more about other Web3 projects, and potentially be motivated to donate to ones they want to support.  I would also hope that more collaboration will inspire developers to help build, for example to create a wrapped QORT on an EVM chain, which would allow more activity across different networks.

**Technical Aspects:**
> From a technical perspective, how would the integration process unfold? Are there challenges or prerequisites we should consider?

I would expect it to work similar to other blockchain based stamps, where the person would be required to sign a message in the Qortal network, to prove they control the address to be linked, then the info for this address could be checked using the API through a public node.  The main technical challege I see is how best to sign that tx in a way that's straightforward and simple for the end-users.  I am sure that it can be done, and should not be too complicated, but I have not spent much time on the technical side of that yet.

> Given Qortal’s emphasis on minters being consistently online and synced, how would this factor be represented in the Gitcoin Passport score?

It is not imperative that a minter stays online.  They simply won't increase their blocks minted while they are not active.  The minter's progress is always available in the blockchain data, so there should be no issue with this for the Passport score.

**I would also like to respond to another post I found that details some of the criteria for new stamp providers.**  (I cannot find the original post link to refer to at the moment.)

1. Strong human (vs sybil) signal
While not a perfect system, I think that Qortal does a good job to prevent mass account farming, without requiring any KYC.  As that is one of the goals of the project, I expect that it can also be adjusted and improved as the network grows, and we have more chain activity to review and consider.

2. Free (or very cheap)
There is no cost to run a Qortal node, aside from the usual electricity and bandwidth costs associated with any type of internet activities.

3. Ensuring that a user can quickly get set up and verified is important to the overall Passport and partner platform's success.
While it's intended that people have invested time to prove themselves to the community, the developers have worked to make the software as simple as possible, with install wizards that guide you through set up.  There is also a good amount of resources available online, and strong community support for those with technical issues.

4. Strong partnership
Having another project with similar goals would be beneficial to Qortal.  Any outside analysis or suggestion for improvement is always welcomed and taken seriously.  While I cannot speak for everyone, I think most in Qortal would be interested to work together, and implement changes when appropriate.

5. Sizable user base
There are estimated to be several thousand accounts, with hundreds of people who are actively using the platform for chat, trading, or sharing and browsing information, and a smaller group who are trying to build apps or move their content to Qortal.  Similar to any project, there are less people who are more active, but overall there is a strong sense of community and shared ideals.

Hopefully I was able to answer your questions well, but I am glad to elaborate or find more info if there is anything I missed.  I look forward to hearing everyone's thoughts, concerns, criticisms, etc.  Thank you very much for your patience and time, and I hope we can find a way to strengthen both communities with this potential collaboration.  :green_heart: :slight_smile: :blue_heart:

-------------------------

erich | 2023-08-24 12:38:18 UTC | #5

Thank you for sharing more details about Qortal, @QuickMythril! :)

I'd like to clarify a point regarding the term "low dimensional." In the context of Passport's scoring models, "low dimensional" refers to the challenge of balancing the complexity of our models with the amount and quality of data we have. Adding more dimensions or credentials, like Qortal minter level, could make our models more expressive but also risks overfitting if we don't have enough associated data points. This is a constant trade-off we have to consider.

Additionally, I'm curious about the experience of Qortal's verification process. Do you have a demo or walkthrough? We want to ensure that any verification process we consider integrating is as human-friendly as possible. Given Qortal's unique verification system, it would be helpful to understand how accessible and straightforward it would be for the broader Passport community.

Looking forward to your thoughts.

-------------------------

QuickMythril | 2023-08-24 14:49:54 UTC | #6

[quote="erich, post:5, topic:16237"]
Adding more dimensions or credentials, like Qortal minter level, could make our models more expressive but also risks overfitting if we don’t have enough associated data points.
[/quote]

I am trying to understand the terms and concepts here, but I think I am still missing the key takeaway.  After talking with ChatGPT, this is what it responded with:

> In the context of Passport's scoring models, "low-dimensional" means finding a balance between the complexity of the models used for verification and the available data points. Adding more dimensions, such as Qortal's minter levels, could enhance the expressiveness of the model but also carries the risk of overfitting if there isn't a sufficient amount of associated data to support these dimensions. In other words, if the data related to Qortal's minter levels is limited or not well-distributed across users, incorporating this dimension might lead to inaccurate or unfair scoring.

If that means across existing Qortal users, then I'd say the distribution is pretty evenly spread out.  If we are talking about Passport users, then of course I would expect many have not heard of Qortal before, but it's not very difficult to get started, for anyone who is interested to contribute to a decentralized network and be recognized for those efforts.

[quote="erich, post:5, topic:16237"]
Additionally, I’m curious about the experience of Qortal’s verification process. Do you have a demo or walkthrough? We want to ensure that any verification process we consider integrating is as human-friendly as possible. Given Qortal’s unique verification system, it would be helpful to understand how accessible and straightforward it would be for the broader Passport community.
[/quote]

Maybe I was mistaken to compare with Idena, as the process is only similar at first.  There is not a captcha like system in Qortal that requires regular activity to maintain identity status.  The process would be finding someone in the community who can provide you a minting key.  Idena has invites that are only given to Verified or Human status, usually one per person each epoch (every few weeks).  BrightID requires you to show up in a video call with already trusted members, and Proof of Humanity uses video submisisons reviewed by the existing community.  To me, these are like "trust networks" where the main way to prove yourself is by joining and participating with other users.

Sometimes it can be challenging when people are not sure what is expected of them.  In Idena there are a lot of people asking for invites, but not really learning about the platform.  Since invites are limited, usually just being active in the chat for a short while is enough to help you stand out from the rest.  I have seen good documentation in all of these projects:  Qortal, Idena, BrightID, PoH.  I think it explains well what is expected and how to get involved.  Some people are just not willing to put forth much effort, and so they don't get as much response from the community.

In Qortal, as well as the others, I see strong community support towards new members also.  Many people help to answer questions and point people in the right direction to get started.  I would say not only is it human-friendly, but it's human-oriented.  When people come in like "bots" saying "Please give code." it's not quite enough for most, and they will usually ask some questions and try to prompt more engagement.  For anyone who can take some time and communicate with other people on a direct level, it should be very accessible and straighforward.

-------------------------

QuickMythril | 2023-10-30 21:02:15 UTC | #7

Dodgers, who is involved in the Qortal community, has written an article that considers this proposed integration:

https://medium.com/@dodgersdesign/fostering-digital-trust-bridging-qortal-and-gitcoin-passport-028c3c06c6ce

-------------------------

allyouracid | 2023-11-01 00:52:01 UTC | #8

Hey there, friendly people over at Gitcoin! :wave:

I am a Qortal community member, and I just learned about the efforts being made here. I know, it's a bit late, but maybe it still helps. @QuickMythril mentioned that giving statements about the network growth is a bit hard, which is true due to the dynamic nature of the minting system.
However, being a "part time statistics guy in my spare time" (for the lack of a better term), I think I might be able to deliver some data, here, as I have started monitoring the Qortal network a while ago. The data sadly doesn't go back all the way to the beginning, but for one year, and I have created a couple charts, from a CSV file with ~2000 lines (they should be pretty much self explanatory; if not, I'm happy to explain). Oh, and don't mind the ~4-5 "holes" in the graph... had a few server outages which went unnoticed for some time. :sweat_smile: 

1. Development of all nodes across all levels:
...after going through quite some hassle and making the charts for all levels and writing this post, upon sending it, I learned that I cannot embed media. :sweat_smile: However, I'm glad the page here just passed on that info without a page reload, leading to a loss of my overall post...

Here are the images on an external hoster where you can view the network's development over the last year. It contains graphs for all levels as a stacked area chart, then a distribution chart for all levels and then charts for every (occupied) single level, for better visibility:

EDIT3: what, I also can't include links??
@QuickMythril I'll drop you a DM with the links, please feel free to add them. :slight_smile: 


Oh, and a couple words on the Level 10 development (8+9 have yet to be reached): level 10 are founder accounts which occupy the levels which don't have any minters, generating funds which are used to advance the network, i.e. paying our wonderful developers, bounties and other means to help the project thrive… as the higher levels gain minters over time, the founder accounts become less relevant in terms of minting rewards.

Ok, that's it from my side, for now. I hope this could shed some light on @erich 's question, although a bit late, but I thought it might contribute a bit.

*Fun anecdote (feel free to stop reading here, it's of literally no significance for the topic at hand, but after having spent quite some time before doing the obvious thing (using a free image hoster), it just feels wrong to not mention it: initially, I spun up a "quick" gitlab pages instance in order to dump my pics there, but then, pages didn't work correctly, I had certificate issues and on my way to fixing them, I botched my overall Gitlab instance (you gotta love it, lol), and I was in for a configuration marathon I'll spare you guys the details about. ^^*
*Now, Gitlab itself is working, again, with the correct certificates. But pages doesn't; it shows an error about the connection not being secure, which you can, of course, click away, but I don't feel good linking to something I made, which doesn't work properly and the thing that isn't working properly is what I would consider a red flag... honestly, I'd stay away in that case. :smile: well, the image hoster solved that for me.*

-------------------------

QuickMythril | 2023-11-01 18:44:04 UTC | #9

![](upload://s2Svaucdu4QLjJB6uVHxOCCuWCi.png)
![](upload://itvZT1jlRT3yQNGsLwggzeINI9V.png)
![](upload://430UPxHegSdupURfRsXPVnHScZf.png)
![](upload://a2Ys9XrjhZBDQTc0TZmmVQ8o4Za.png)
![](upload://5RVT0UILJP7B14fjVk2hIEqnj4H.png)
![](upload://xrtplV5P8DkKPHFH7DSbS3isQn3.png)
![](upload://ocZ0R3Tdqn1X7NfT4kz4kZVA6hZ.png)
![](upload://AcSO28j9GIocsmLGJ1fJfSDjQi.png)
![](upload://azPDPEW1jxaj5HVq7fZnvNTWIgo.png)
![](upload://mawdtXkmEQBANKRFu77Fe10y9WT.png)

-------------------------
