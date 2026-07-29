---
id: 9023
title: "Discussion: dGrant solution"
slug: discussion-dgrant-solution
category: open-discussion
url: https://gov.gitcoin.co/t/discussion-dgrant-solution/9023
created_at: 2021-11-13T05:31:12.178Z
last_posted_at: 2022-05-01T08:42:42.742Z
posts_count: 19
views: 3281
like_count: 30
---

# Discussion: dGrant solution

<https://gov.gitcoin.co/t/discussion-dgrant-solution/9023>
lanlan3322 | 2022-05-28 15:38:06 UTC | #1

**Decentralized Grants Verification**
***Challenges we are facing now:***
- Grants review manually is becoming unrealistic by a small team
- Community is not encouraged to be involved in the grants verification process

***Decentralising Grants Verification:***
- Grants legality is governed by the whole community 
- Community is incentivized with GTC to be involved in the grants verification process

***Possible process:***
- Community members are promoted to "Watcher" once they have any of DID verified (POH, POAP, BrightID and so on)
- Any "Watcher" has the right to "Flag" a suspicious grant submission with X*GTC deposit and detailed reasons
- The challenge details are sent to "Gitcoin Grant Court" in Kleros (decentralized dispute resolution) to get the challenge result
- If "Watcher" is flagging a malicious grant submission successfully he will get the deposit back and Y*GTC rewards
- If "Watcher" is flagging a legit grant submission as suspicious he will lose the staked X*GTC
- The grant will be removed if it is successfully identified by "Watcher"

***The effects we get from this solution:***
- Grants are governed by the whole community in realtime globally
- Community is incentivized with Y*GTC each time flagging malicious grants submission
- It is an effective deterrent security protection from spam/scam grants submission

***Future expansion:***
- It could be applied to dBounty as well
- It could be expanded to any modules of GitcoinDAO which requires monitoring and curation

***Support needed from GitcoinDAO:***
- Detailed grants policy documents 
- GTC funds to be rewarded to successful "Watcher" and to be sent to "Gitcoin Grant Court" as arbitration fees
- GitcoinDAO members tier implementation for "Watcher"

***Possible difficulties:***
- Gas fee keeps high on Mainnet 
- Often adjustment of X*GTC and Y*GTC if the price of GTC is changing too much

-------------------------

bobjiang | 2021-11-15 01:44:11 UTC | #2

I love this proposal, although the name should be changed bc dGrant is used for decentralized grant in workstream. 

Maybe we could integrate this proposal in Decentralized Gitcoin stream, so @phutchins and @DisruptionJoe what are your thoughts?

I heard that Gitcoin Core team has collaborated with PoH team before, while in this proposal we could use GTC as staking and incentive for GitcoinDAO users (community members). 
@owocki any insight for this proposal?

-------------------------

DisruptionJoe | 2021-11-16 20:07:08 UTC | #3

The FDD workstream is currently managing the policy and evaluation of grants for approval to different rounds. The dGrants product needs to be integrated to our current process as well as these forward looking solutions. 

There are multiple options for how we prioritize. Let's connect with @phutchins and @Sirlupinwatson around how to move this forward.

-------------------------

DisruptionJoe | 2021-11-16 20:08:25 UTC | #4

Can you ping me on discord Ianian ?

-------------------------

Sirlupinwatson | 2021-11-16 20:11:27 UTC | #5

Hi @lanlan3322! 

Thanks for your feedback, highly valuable!


[quote="lanlan3322, post:1, topic:9023"]
Grants review manually is becoming unrealistic by a small team
[/quote]

Right now we have 2 separate decentralized squads working on to review each grants under 24/48 hours delay. We had the first "Splitting Squad" on the first of November I think.

[quote="lanlan3322, post:1, topic:9023"]
Community is not encouraged to be involved in the grants verification process
[/quote]

I think the community is highly encouraged to be involved in the grants verification process, we are actively getting more user and contributors involved in that part only.

[quote="lanlan3322, post:1, topic:9023"]
Any “Watcher” has the right to “Flag” a suspicious grant submission with X*GTC deposit and detailed reasons
[/quote]

This is already possible to "Flag" a grant, once a grant has been "Flagged" we will carefully review it. Any member of the community can "Flag" a grant. @David_Dyor can tell you more about that process since he's building up the policy's.

We are also planning on creating an interface UX-UI to review these grants, either on dGrants or on Gitcoin. Feel free to jump in the conversation on Discord or we can keep this post up.

-------------------------

tjayrush | 2021-11-17 14:40:43 UTC | #6

Unless Y is very significantly larger than X, I for one would not participate due to a natural human tendency to prefer pain avoidance over reward.

A slightly different way to state this so that it's very clear would be to change Y to 3 * X and change the amount lost due to an incorrect identification to .1 * X.

Summary "Watcher stakes X GTC and, if correct, receives 3 * X reward. If incorrect the Watcher forfeits .1 * X and received .9 * X refund."

This sounds simultaneously more rewarding on correct identification and less punishing on incorrect identification.

-------------------------

David_Dyor | 2021-11-18 04:28:49 UTC | #7

I agree this general direction is desirable.   There is some progress already and I look forward to continuing the discussion.  We (the Fdd) have been talking to a project already (Celeste) but the goal is to have a modular system where a variety of court-like systems can fit in.  As for policy, all docs are migrating to Gitbook where current versions will be accessible to everyone.

The FDD also developed an appeals procedure intended to be used with the future iteration of the grants program.  I can see being used after the 'marking' process you describe.  In the legacy version of grants what you call marking was called flagging.

Would like to see a short gamified training quest for the 'Markers' much like the Grant Evaluation Squads receive a small amount of training.  In the legacy system anybody had the ability to mark/flag a grant.  Even members of the public.  Sometimes industry folks like to squeal on each other.  I would like to see that preserved somehow.  Lots to discuss and I look forward to meeting you.

-------------------------

lanlan3322 | 2021-11-19 03:15:40 UTC | #8

Thanks for your detailed clarifications. 
We are perfectly ok right now but if we see the future when there are 100+ or even 1000+ submissions (who knows it is not happening?! :slight_smile:  ) the review pressure will be hard to handle by dedicated members. Instead, it will be easier to hand over to all members in the system.

For now, the community is basically involved by "Goodwill" and there could be a more sustainable way to keep encouraging members to join the mission with a proper incentives system established.

The present "Flag" function is easily attacked without any protection. Malicious actors would do irresponsible flagging to overload our review teams. 

To align with GitcoinDAO concept we could build these small DAO components which will eventually stack up a whole DAO system.

:slight_smile:

-------------------------

lanlan3322 | 2021-11-19 03:21:28 UTC | #9

Exactly, totally agree with you.
We need to work out a better way and put the managing factors in DAO process which could be discussed and then applied via smart contract forcefully without human interaction.

-------------------------

lanlan3322 | 2021-11-19 03:29:28 UTC | #10

Thanks, I am looking forward to working out a gamified module on this. FDD is the first perfect place to realize this DAO-like component. Internet of jobs should be incentivized based on valuable contributions and there should be certain penalization on hostile actions.

-------------------------

lanlan3322 | 2021-11-22 02:17:47 UTC | #11

In order to keep the discussion record I copied Joe's comments from discord here:

//Start of msg from discord
So we have a manual review process now, but it needs to be better than that. 

There was a curation interface made for this which could be lightly adjusted. 

I’m not sure if all these steps are necessary, but I think they are at first glance 

1) update and plug in the curation game interface but only so whitelisted reviewers and leave reviews

2) Open up to anyone to review (maybe staking) and compare results of whitelist to the open one

3) add in functionality to better create thresholds for participation and test them. 

4) connect the outcome of reviews to directly activating ir shutting off grants match eligibility for rounds. (Previously done manually based on reviews done in the game)

//End of msg from discord

Thanks @DisruptionJoe

-------------------------

lanlan3322 | 2021-11-22 02:29:57 UTC | #12

Thanks, which channel should i join for dGrant discussion?

-------------------------

David_Dyor | 2021-11-22 18:37:13 UTC | #13

I propose we use the dgrants-feedback channel.  https://discord.gg/xuZxzvfn

Started a discussion there.  Note we are planning to use Celeste for the external conflict resolution step, not Kleros, however the goal is to enable any similar project to be used.  Aragon Court is another possibility.

-------------------------

lanlan3322 | 2021-11-23 01:07:13 UTC | #14

Thanks, but I don't have access to dGrant-feedback channel.
yap, More options provide more resilience for the system, just like uniswap provides options for users to choose which token list to show.

-------------------------

lanlan3322 | 2021-11-25 03:47:47 UTC | #15

Just had a quick check on Celeste and it is using Aragon Court actually:
https://1hive.gitbook.io/celeste/developers/documentation

https://github.com/1Hive/celeste-backend

-------------------------

willjgriff | 2021-11-25 14:09:17 UTC | #16

That's correct. If between us we build an interface for the Gitcoin DAO proposal process with Celeste, it should interface fairly easily with Aragon Court too. However, note that Celeste lives on xDai and soon Polygon and Arbitrum, where as Aragon Court lives on the Ethereum mainnet so depending on where the Gitcoin DAO proposal process lives (I believe it is on Ethereum mainnet), there may also be bridging infrastructure necessary.

For reference I work at 1Hive and on the Celeste Smart Contracts fork from Aragon Court.

-------------------------

lanlan3322 | 2021-11-28 07:50:02 UTC | #17

Thanks @willjgriff , I am glad to join this task if there are any needs. I think independent dispute resolution is more logical in DAO. The guardians of the constitution are not affected by governing voting power.

-------------------------

wkarshat | 2022-03-04 06:45:21 UTC | #18

The ratio of the reward and punishment needs to be compared to the prevalent rates of false negatives [faulty grant application getting approved].

For example, you propose a ratio of 30:1, and if the rate of false negatives is 5%, it may pay to simply flag every grant.

Unfortunately we may not have very precise empirical numbers for false negatives, and not only because the criteria are somewhat vague, given the entire range of grant applicant and subject matter possibilities, and the judgements are inherently subjective.

With various grant subtypes and a range of possible failing criteria, somewhat unevenly distributed over time, it is not immediate how to map any set of secondary evaluations to the entire population of the grant applications.

-------------------------

shahid1956 | 2022-05-01 08:42:42 UTC | #19

Well thought proposal. Involving   Gitcoin community in verification is a good idea.

-------------------------
