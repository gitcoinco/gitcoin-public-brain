---
id: 8782
title: "[Proposal] Redistribute GTC to Individuals Who Could Not Claim Due to Error"
slug: proposal-redistribute-gtc-to-individuals-who-could-not-claim-due-to-error
category: governance-proposals
url: https://gov.gitcoin.co/t/proposal-redistribute-gtc-to-individuals-who-could-not-claim-due-to-error/8782
created_at: 2021-10-11T17:44:56.254Z
last_posted_at: 2022-07-25T18:57:22.273Z
posts_count: 32
views: 6640
like_count: 50
---

# [Proposal] Redistribute GTC to Individuals Who Could Not Claim Due to Error

<https://gov.gitcoin.co/t/proposal-redistribute-gtc-to-individuals-who-could-not-claim-due-to-error/8782>
Tardigrade | 2021-10-11 21:40:05 UTC | #1

**I. Overview**
The GTC airdrop earlier this year was a great step towards the decentralization of the Gitcoin ecosystem. Unfortunately, there are several users who were eligible for the drop because they funded the project [Force DAO](https://gitcoin.co/grants/1987/delta-prize) before the date of the airdrop, however, an error in the transaction validator ingesting their transactions meant that these users were unable to claim their tokens. Specifically, when these users went to claim their tokens within the 30-day airdrop window, they were not allocated a percent of GTC tokens for their donations to [Force DAO](https://gitcoin.co/grants/1987/delta-prize). This proposal is looking to retroactively compensate the users who were not able to claim their GTC due to the error.


**II. Proposal Details**
Since understanding this error involves many fine details and retroactive date tracing, we will look at one user’s experience ([@haj199](https://gitcoin.co/haj199)) in order to show how everything unfolded:

- *February 14th 2021:* [@haj199](https://gitcoin.co/haj199) donated a grant (Figure 1) to the project Delta Prize.

- *~ March 4th 2021:* The project’s name changes on the Gitcoin website from “Delta Prize” to “Force DAO”.

- *~March 10th 2021:* The Gitcoin bot drops (Figure 1)  [haj199’s](https://gitcoin.co/haj199) original transaction to Delta Prize / Force DAO from his Gitcoin account. We examined the Gitcoin code base and did not find a clear reason for this.

- *May 1st 2021:* Cutoff date for transactions factoring into the GTC airdrop. Unfortunately for [@haj199](https://gitcoin.co/haj199), his transaction no longer meets the cut off date because the Gitcoin Bot had already dropped it.

- *May 25th 2021:* The 1-month window for the airdrop opens.

- *~June 7th 2021:* [@haj199](https://gitcoin.co/haj199) attempts to claim GTC tokens, but is not able to claim the allocated percent of GTC tokens from his donation to Delta Prize / Force DAO. [@haj199](https://gitcoin.co/haj199) lets Gitcoin know by filling out [this form](https://gitcoin.co/grants/add-missing-contributions). Gitcoin recognizes that his original transaction before the cut-off date was valid and reposts it (Figure 1) on [@haj199’s](https://gitcoin.co/haj199) account. Due to the posting of the transaction occurring after the cut-off date (but not that transaction itself), [@haj199](https://gitcoin.co/haj199) is still unable to claim his GTC reward. 

*This proposal is asking for a rolling period of 4 weeks for “affected individuals” like [@haj199](https://gitcoin.co/haj199) to resolve inconsistencies with activity shown on their Gitcoin profiles by providing “valid proof” to their eligibility claim. During this 4-week period, users would receive GTC from the DAO treasury upon proving their eligibility.*


**III. Qualifications and Criteria**
*Qualifications for “Affected Individuals”:*
- Donated to Delta Prize / Force DAO before April 1st 2021 - the cutoff date for the original airdrop.
- Was not compensated by GTC for those donations.
- Attempted to claim GTC within the 1-month airdrop window starting on May 25th 2021.

*Criteria for “Valid Proof”:*
- Etherscan receipt for transactions before the airdrop cutoff date showing:
a. Transaction hash
b. Interaction with the [Gitcoin: Bulk Checkout](https://etherscan.io/address/0x7d655c57f71464b6f83811c55d84009cd9f5221c) smart contract
c. Amount sent
d. To address (0xe5b5514e0618f4b55736c0c0c78ccd6f8ac14631)
e. From address
- Proof of Wallet ID matching Gitcoin Account
a. Our workstream will ask the Gitcoin Core team to look into their database to verify that the wallet ID that made the original donation matches back to the Gitcoin user claiming they are an affected user.
b. We are assuming that having a transaction re-added during the 1-month airdrop period is proof that the individual attempted to claim GTC within the window. This is because individuals who re-added their transactions were ones who reached out to Gitcoin [via the form](https://gitcoin.co/grants/add-missing-contributions), thereby interacting with the Gitcoin website at the time.


**IV. Distribution**
After proving that an individual is an “affected user” and has shown “valid proof” for their GTC claim, we will use the same formula used to calculate their new GTC allocation as was used in the [original airdrop](https://bits.owocki.com/7KuEqyxo):

*Formula:* GMV per user / GMV Total (in USD, $22,000,000) * GMV Allocation Percent (10,080,000) (see Figure 2 and 3)

After calculating the GTC allocations, the process of distributing the actual GTC tokens from the Gitcoin DAO treasury to the “affected users” is a straightforward one, and would be done using [Whaler DAO’s AstroDrop application](https://whalerdao.github.io/astrodrop/create). To learn more about Whaler DAO and their reliability, feel free to check out their [grants page](https://gitcoin.co/grants/1297/whalerdao).


**V. Motivation and Benefits**
By implementing the proposed solution, we uphold the integrity of the Gitcoin ecosystem, ensure equity for all members, and set a positive precedent moving forward. Gitcoin prides itself in empowering participants and emphasizing collaborative behavior. As shown above, it is evident that certain members have not received GTC during the airdrop period despite meeting all requirements and attempting to claim GTC, while other users received their allocation successfully. This proposal aims to retroactively support those members by giving them the GTC they were eligible to originally receive. This allows Gitcoin to stay true to its founding principles while also ensuring all participants are being valued. Finally, this will also set a positive precedent moving forward as it shows that the Gitcoin community through its governance is willing to accommodate and adapt when needed, prioritizing equality and fairness. 


**VI. Drawbacks**
A potential drawback that might prevent people from voting “yes” on this proposal is that it is asking for GTC tokens to be withdrawn from the DAO Treasury, thereby increasing the circulation of GTC in governance. However, as explained above, these tokens should have been distributed to the users from the treasury earlier during the original airdrop as they were eligible. Another drawback in this proposal is that it does not address what the original bug was that caused the original transactions to be dropped by the Gitcoin bot. However, as proven above, it is clear that regardless of what the error was, it’s explanation is not necessarily needed for remedying the solution, as proof of eligibility can be determined without it. It would be useful to eventually find the root cause and identify the bug to prevent future occurrence of this problem, but it is not needed for this proposal. 


**VII. Voting**
*Yes:* Open up a 4 week-rolling period for “affected users” to resolve inconsistencies with their GTC claims mentioned above. If an affected user is able to prove that they were in fact eligible for a GTC allocation from their donation to Force Dao (using the proof criteria above) and did not receive it, then send them their GTC from the DAO treasury. Voting yes only covers the above use case. It does not cover cases for users who forgot to claim their GTC within the original 1-month airdrop. 

*No:* No 4-week rolling period of GTC drops for affected users who should have received an allocation but did not due to the error in the transaction validator. 

[poll name=poll2 type=regular results=always chartType=bar]
* Yes
* No
[/poll]



**VIII. Figures**
*Figure 1 (taken October 8th, 2021):*
![1|690x396](upload://h4Hf3yphBEClEYTEZZ8uxxSvIh7.png)

*Figure 2 (taken October 8th, 2021):*
![2|690x381](upload://rbbwUA5PZkahCw1ho0yJd5tqnzm.jpeg)

*Figure 3 (taken October 8th, 2021):*
![3|690x106](upload://y1jZgL0D6cWBq8MmQqzBKiCsFrZ.png)

-------------------------

haj199 | 2021-10-11 21:53:45 UTC | #2

Thanks for creating this post. In my case, here is an etherscan receipt showing proof that I donated before the cut off date, as well a screenshot verifying that the wallet id traces back to my gitcoin account.
https://etherscan.io/tx/0xca84e1d9e21cca9cefa532ccadacc2cd62de14fde673e4ce4209cfd01c89622d
![telegram-cloud-photo-size-1-5127796575098218842-y|690x322](upload://jfd9ltsXTXA0f6hU9zh98tS5Z4w.jpeg)

-------------------------

McGroovyJ | 2021-10-11 23:38:52 UTC | #3

Yes, my situation is quite similar. I had a back and forth communication with both Conner and Kyle which helped me understand the situation a bit better. Thanks for such a detailed summary of the issue.

-------------------------

tjayrush | 2021-10-14 13:09:33 UTC | #4

I would vote yes for this on its surface. A few questions:

1. Is there any chance of getting an estimate of how many people are affected? It mentions only Force DAO, but does anyone know if this happened with other donations?
2. Is there an estimate of how many "affected users" who can provide a "valid proof" there are? If there's 10, that's one thing. If there's 100,000 that's quite a different thing.
3. Is there an estimate of how many potential tokens we're talking about and (importantly) what percentage of the total treasury this might represent? Again -- 1/10 of one percent is one thing - 10% is another.
4. Is there a plan for making it clear that this is a one-time only correction? One concern is that by doing this you're establishing a precedent and other (equally justified examples) will come with further claims. Solving this problem once and for all would seem better than opening up a continuing stream of similar claims.
5. Related to 4, is there a plan to broadly announce that this policy is being enacted? If not, then how are you to know that all potential claimants (with similar but different claims) have come forward?

-------------------------

Tardigrade | 2021-10-16 01:16:15 UTC | #5

Hey - thanks for the input!

I would like to preface this by saying that I am not part of the Gitcoin team, so much of the information obtained had to be acquired by scurrying the website, the forums, discord, etc. As outbound workers on this project, we do not have access to the internal database and had to rely on the Gitcoin core team helping us on a few occasions by providing us with information from their database. That being said, even as outbound workers, we were able to acquire enough proof to show that some individuals would have been eligible for the airdrop, but never received their allocation specific to FORCE DAO.

To answer your first 3 questions, we went through the FORCE DAO donation list and were able to identify the list below as all users who had their transactions dropped at the same time by the same error. This is not a big list, as it is specific to the project mentioned above. However, not all the users listed had their transaction re-added during the airdrop window, therefore, using our outbound method of proving attempt to claim GTC, not the entire list might have proof to show that they attempted to claim the GTC during the 1-month window. Therefore, since some individuals from this list can't even prove attempt to claim during the 1-month window, they would not be eligible for the compensation as they missed the airdrop window entirely. This proposal does not address users who missed the airdrop window entirely. Regardless of who on this list ends up being compensated based on the proof supplied during the rolling window, if you look at the list size and the total amounts donated, we will only need a very tiny portion of the treasury to compensate the individuals affected. 

1. [@sitnyaga](https://gitcoin.co/profile/sitnyaga) 7.00 ETH 6 months, 3 weeks ago
2. [@drmtaha](https://gitcoin.co/profile/drmtaha) 0.200 ETH 6 months, 3 weeks ago
3. [@jindevilfruits](https://gitcoin.co/profile/jindevilfruits) 3.000 ETH 6 months, 3 weeks ago
4. [@kumotaro](https://gitcoin.co/kumotaro) 2700 USDC 6 months, 3 weeks ago
5. [@haj199](https://gitcoin.co/profile/haj199) 50000 USDT 6 months, 3 weeks ago
6. [@andmilj](https://gitcoin.co/profile/andmilj) 0.70 ETH 6 months, 3 weeks ago
7. [@dekutree1314](https://gitcoin.co/profile/dekutree1314) 0.50 ETH 6 months, 3 weeks ago
8. [@angelom777](https://gitcoin.co/profile/angelom777) 1.50 ETH 6 months, 3 weeks ago
9. [@fdanso](https://gitcoin.co/profile/fdanso) 0.60 ETH 6 months, 3 weeks ago
10. [@zombiehobbes](https://gitcoin.co/profile/zombiehobbes) 1.0 ETH 6 months, 3 weeks ago
11. [@fruktozamin](https://gitcoin.co/profile/fruktozamin) 26000 DAI 6 months, 3 weeks ago

To answer your 4th question, I agree and think solving this problem once and for all for all cases of individuals affected, even across other projects, is a smart decision. However, I also think making an all-encompassing proposal will be harder to get a vote to pass on right now, as a decision that big might appear risky to many voters as it will involve more GTC being distributed. I think that starting small by taking on this project first, seeing how it goes, and then using it as a guide to structure a future all-encompassing proposal would be a wiser decision. Especially considering that the informal workstream we have for this proposal right now consists of mostly outbound workers. For a more encompassing proposal, I think we would need more members from the Gitcoin core team on the workstream, and right now based on my understanding, most of the team is busy with others matters. If an all encompassing proposal ends up happening in the future, I would also be happy to help lead that as I think solving this problem and helping the affected users is a worthy cause.

To answer your final question, I think the way to announce this policy would be to directly reach out to the users affected. Since we have narrowed in on a very specific problem within a specific project, we were able to identify the exact people who are affected. I also think making the window for this policy enactment be rolling for 4 weeks, will also give people more than enough time to come forward. Furthermore, we can also announce this policy on the relevant Discord channels pertaining to GTC to let people know about it.

-------------------------

bobjiang | 2021-10-18 04:20:41 UTC | #6

I would vote this proposal yes. and I have suggestion , 

1. integrate with data from blockscience

as Gitcoin has collaborated with blockscience to build the anti-sybil model, and there are some data there we could borrow, and then we could filter out some sybil users for this proposal.

2. identify active users

we could identify the users are active or not. (I know some users are banned from github and then they could not login gitcoin) So we won't include the inactive users in this proposal.

3. Opt in by users.

I suggest we could invite the impacted users to opt in, e.g they could input the info required to claim. (tx, gitcoin handle, etc)

Last, I am sure it is low priority for Gitcoin core team for this proposal, so I am happy to see you could lead this.

-------------------------

Tardigrade | 2021-10-22 20:11:52 UTC | #7

Thanks for the insights. I agree with a lot of what you mentioned and think your suggestions will improve the proposal.

To address your first point, I think filtering out sybil users would have been a great idea. However, as you mentioned to me on Discord, and for everyone here to also get in the loop, Blockscience does not have an API right now that we can use for the anti-sybil model. Since they plan to release it much later in the year, we won't be able to use it for the anti-sybil model. Would definitely be open to any alternative ways to address potential sybil users. However, if we are not able to find a way to do this, I do not think it would be detrimental to the strength of the proposal. Since we are working with a very small list size as seen above, I don't think this will be a major problem for us.

I think your second and third points are closely linked to one another. We will not include users that are banned from github as affected users for this proposal. I also think inviting users to opt in by inputting their info (like tx, gitcoin handle, etc.) will filter out for inactive users as well, so we can definitely make it an interactive process. I believe we can do this by sending out a form for the users to fill out.

-------------------------

David_Dyor | 2021-10-23 22:47:45 UTC | #8

I will support this proposal but I always feel mixed about changing results linked to blockchains due to the whole immutable-piece.  But the way I see it, someday it could be me asking for a redo.

-------------------------

JTraversa | 2021-10-27 03:13:48 UTC | #9

My thought on this is that of course it would be good to compensate early users that were not rewarded tokens due to some error on gitcoins side. 

This should also be especially easy to do given there are enough tokens left unclaimed (IIRC) from the initial distribution to cover these impacted donators.

However the response also establishes a bit of a precedent for similar errors in the future and this should be kept in mind.

That said, I think it should be imperative to identify the core cause of the error instead of just fixing the result for the loudest party.

> We examined the Gitcoin code base and did not find a clear reason for this.

It might be reasonable to designate some minimal workstream funds to throw together an "official"/public resource allowing the community to audit the issue (really just an official pdf that says it happened, with tx logs for public investigation, links to reviewed code).

This would help the community identify other affected parties/grants and ensure that the topic isnt brought up multiple times, as well as add to the public legitimacy of any new distributions.

-------------------------

Tardigrade | 2021-10-27 17:21:13 UTC | #10

@David_Dyor 
Thank you for your positive support towards the proposal.

@JTraversa 
Really appreciate your feedback here. You touch on a really important point: the bug that is the core cause leading to this error for many users. I think finding a permanent solution to prevent an error like this from happening in the future would be the optimal last stage step towards putting this issue to bed. However, we are currently facing a few obstacles preventing us:

1) The current team tackling this proposal is very limited in size.
2) The team already spent extensive time and effort trying to identify the bug without clear-cut success.
3) The team does not contain any Gitcoin core members / individuals who were part of the group that wrote the original code.
4) Those members are already jammed up with work and have other things on their plates right now.

Since it is possible to prove failure to claim without identification of the bug, we can, and I personally believe we should take the necessary steps to remedy the situation, hence the proposal. That being said, I think your suggestion of creating a public resource sharing all the ground we've covered so far with regards to identifying the bug is a smart supplementary idea. We will put that together if this proposal passes. Hopefully, with the help of more people within the community we can identify this bug once and for all.

I also agree that a proposal like this will set a precedent, but I do not think that it will be a bad one. I think having the community, without any monetary incentive to do so, come together and show support to retroactively help those who were unfortunate victims of an error in the system will demonstrate strength in integrity. 

Although there might be other parties with similar problems, I think creating an all-encompassing proposal for everyone is the ideal scenario. However, I also think that getting a proposal like that to pass, given the team size we have right now and how much money we would need from the treasury, will not be feasible and probably won't pass right out the bat. That is why I still think that starting small by passing this proposal first, and then gaging its response might be the safer and wiser approach to structure a future all-encompassing proposal with more hands on deck.

-------------------------

auryn | 2021-11-03 15:15:50 UTC | #11

I haven't had a chance to dive deeply into this, but on the surface it seems like a reasonable proposal.

-------------------------

ceresstation | 2021-11-17 00:46:29 UTC | #12

I don't feel super strongly here, and this might sound harsh, but I'm personally against this for a few reasons:

1) I would argue Force DAO (which the largest amounts in this proposal cover) was an anomaly: transactions to this grant occurred outside of a grants round and largely as a "pass through" for the creation of the DAO itself. In addition, some of the largest single distributions already went through to the creators of this DAO but they have not been active or meaningful participants in its success (which was in many ways the meta-goal of distribution).

2) This proposal risks opening up a larger pandoras box that will likely distract stewards or other participants for more pressing issues around how we push forward our mission to grow and sustain public goods. I should also stress that it would be incumbent on the DAO to operationally execute on this from start to finish as the core team would not be allowed to assist in the way they did to set up the initial claim.

3) In many cases, the amounts of funding we're talking about could be attained by joining a workstream for less than 1 quarter, I would argue the fact that we are talking about very small amounts is in fact as much of a reason to not spend time here as it is to move forward.

Again please don't take this the wrong way, I think the claim experience could have been executed better, but I think we're chasing a zero-sum versus positive-sum game here.

-------------------------

owocki | 2021-11-17 02:33:55 UTC | #13

>  I should also stress that it would be incumbent on the DAO to operationally execute on this from start to finish as the core team would not be allowed to assist in the way they did to set up the initial claim.

I wanted to briefly comment on this point made by @ceresstation .

One way to solve for this would be for the proposals authors to amend the proposal with the addresses of whomever they think has proved their valid claim for an airdrop, and to distribute the tokens themselves, say through a multisig or something like [this tool](https://multisender.app/) or [this one](https://whalerdao.github.io/astrodrop/).

-------------------------

Tardigrade | 2021-11-17 18:33:21 UTC | #14

Hey Scott - thanks for your input here. I spoke to a few of the community members and we understand where you are coming from, and as such I would like to clarify a few things in regards to the points you bring up.

I don’t think the first point presents a strong enough case to argue against the passing of this proposal. Although transactions to Force DAO were outside of the grants round, they still technically occurred before the cut-off date, and the original GTC drop did cover Force DAO contributors when the tokens were being distributed. The fact that some Force DAO donators received their share of GTC while others did not due to the error demonstrates that Force DAO contributions are in fact eligible contributions. As such, I believe all the evidence points towards them still being eligible. While some of these users have not been very active participants, I don’t think it diminishes their eligibility claim. I personally think it’s harsh to expect reciprocated contribution to the community from their end when they felt left out of the community by not being included in the drop. And I don’t mean to point fingers when I say this, I am just trying to make sure their voices are also heard in this discussion. What happened with the error happened in the past and is nobody's fault, but I think it’s the steps we take moving forward which are more important. I think compensating these eligible individuals is a positive gesture Gitcoin can make to reintegrate these marginalized individuals back into the community. After working with them on this proposal, I can tell you that many of them are fantastic individuals with great minds and ideas who can be a real asset to this community. 

To address the second point taking Kevin’s input into consideration, we will ensure that the implementation of this proposal will require minimal assistance from the DAO’s part. I will work with the rest of my team on generating a final list of individuals (and their addresses) who have demonstrated valid proof of eligibility, so that we can present this information, and with the approval of the community, distribute the GTC ourselves. We have been working on this proposal for weeks and have covered most of the ground work ourselves already, and I am confident we can bring this past the the end-line ourselves as well. I think if this proposal passes, it reinforces the already strong notion that Gitcoin is truly a decentralized entity. 

To address your third and final point, I do not think the suggestion that working elsewhere to earn tokens they were already eligible for is convincing enough. I think it’a a matter of principle rather than token amount here. Regardless of how big or how small X’s contribution was, if X is eligible for GTC from the drop, I do not think X should be told to work elsewhere to receive the amount they were eligible for from the drop. It just seems like disincentivizing ask in my opinion. The time and effort being spent here is time and effort spent by these affected individuals which could pave the way for the re-forming of a strong relationship between themselves and Gitcoin moving forward. Furthermore, some of these contributions are way larger than any amount that could be earned in a quarter, and especially for these individuals, it seems harsh to suggest joining a work stream for a quarter.

I tried my best to avoid coming off as hostile the points you bring up, so my sincerest apologies if I do seem antagonizing - that was not my intention. I think the points you bring up are strong rebuttals to the proposal. That being said, I ultimately do not believe that these counter-arguments are enough to justify the failing of this proposal.

-------------------------

fruktozamin | 2021-11-27 00:01:10 UTC | #15

I am one of the affected users,donate from two different adresses

-------------------------

JosephClarkClayton | 2021-11-29 20:40:44 UTC | #16

Heres my opinion on the govence system. 
What about all the members who were, have been, or still are, too busy with working on this community's vision, (and the ones who dedicate themselfs in the future) to have time to be socialy active on forum, in the last 6 months. And, in turn, now, are not givin the Choice to help govern, what direction our community goes now. 

If a person commits to something one believes in and works hard, giving pieces of ones life up for it, Respect and Admiration is what is created for the person. NOW, if it's a something that you share working on. Then give the respect and graditude that you and I would expect to receive. as long as someone has and is showing decication to the vision, EVERYONE should always have a right to help govern the vision when they have dedicated there life to it selflessly, Our Honor and Integrity Demands it.

Please, tell me your opinions on this, am I missing something here??

-------------------------

Tardigrade | 2021-12-09 23:39:09 UTC | #18

**Final Amendments**

Thank you to everyone for your feedback on the proposal. We will now transition into the Snapshot vote. Here are the final amendments based on your feedback:

1. Rather than open a 1-month window for allowing users to supply proof as qualifying for the “affected user” category, we will now only compensate the users listed below. All these users have demonstrated the necessary proof to be eligible for the airdrop and were responsive throughout the proposal process. We have obtained this list by doing the following steps:a) Reaching out to all members who had dropped transactions from FORCE DAO donations. This was done through discord and/or posting on their gitcoin page.b) For those that responded, we ensured proof of the original donation (through an etherscan receipt) and attempted a claim during the original airdrop period.

*Given that this proposal has been posted for 1-month+ we will no longer be adding any new users. We have personally reached out to all affected users on the Gitcoin website and on the Gitcoin discord. Thus, unfortunately it does not make sense to add more users given the original airdrop period was only 1-month long and we have given all affected users at least that long to get back to us.

**Total GTC Allocation from treasury: 32,390.06** *(rounded each user to nearest tenth)*

https://drive.google.com/file/d/1p5botoxZ4vd5XpVbZzusyiqxZGfB8SaU/view

-------------------------

Tardigrade | 2021-12-10 15:48:25 UTC | #19

Proposal is live on Snapshot, here is a link:

https://snapshot.org/#/gitcoindao.eth/proposal/0x3fdc2452ce289ea193413b3f169577f4dea05373fb6c503d982f4c3b1b892bb0

-------------------------

krrisis | 2021-12-13 14:39:53 UTC | #20

I will probably vote no here for the same reasons, because this is indeed very much a box of pandora, and there is so much we need to focus on for Gitcoin. If I vote yes here I would need to vote yes also for the many, many people who did not get the full amounts they deserved bcs of certain anomalies. (I'm one of those people myself)
I just hope future airdrops of other projects can learn from this detailed use case and will optimize their airdrops based on exceptions as described here and in other places.

-------------------------

Tardigrade | 2021-12-14 02:44:23 UTC | #21

Thanks for your input Kris. I understand where you are coming from, but personally, I'm not sure if I ultimately agree that the opening of a Pandora's box of future requests justifies not compensating eligible users. For the other potential voters on here, I would like to explain why I think so.

I think it's fair to say that most of us here are on the same page about the fact that these users have demonstrated that they are in fact eligible. The main worry is this potentially shifting focus away from other matters. I do not think this will be an extra burden on the community, especially the Gitcoin Core team. As demonstrated by this proposal, the proof of eligibility can be arrived at without the need to trouble the core team, and the carrying out of this redistribution can be done using tools that do not require much extra work from the team's part. WhalerDAO's Astrodrop tool is such an example. The people actually putting in the work to build a proposal like this one are mostly affected users who want to to do some little bit of work because they are personally affected by the matter. The biggest ask we are making from the team's part is simply voting on Snapshot or Tally.

If you look at these requests on a case by case basis, for users who have proven eligibility, I don't see how an option that chooses not to compensate them aligns with Gitcoin's core mission. If the aim is to empower a whole community of builders and individuals, then letting a few cases of misfortune slip by the cracks hinders us from fulfilling that mission to its truest nature. That is why I think voting yes on this proposal is important: it shows that the larger community can come together to support a smaller subset of that community. If that is not inclusive community empowerment, I don't know what is.   

Again, thanks for your input and taking the time to read the proposal, Kris. I hope other people are able to see this proposal from the different light I have just mentioned.

-------------------------

Pop | 2021-12-15 14:37:32 UTC | #22

I think my concern having spoken to the anti sybil workstream is that ForceDAO created a grant and then did their entire raise through grants (which again, we know did not happen during a grants round). Is there an instance where the “donors” were in effect purchasing their share in ForceDAO? 

Is there a record of the accounts who donated actually using or being active contributors to ForceDAO? I think this is my primary reason as it is a considerable allocation of GTC and I am weary of its impact on the treasury (while we wait for a dashboard to be build showing a real time health of the treasury which I am trying to push forward). I also cannot see, and please let me know if I have missed it, any indication that the GTC will not be offloaded immediately.

I understand your points, Tardigrade and on the surface I was definitely going to vote yes because I do believe in fair distribution - but digging into it a little bit, I have a few concerns that I am unable to resolve from the info available/in the proposal. Hence my vote - I know you reached out to me on Sunday to go through the proposal and my apologies for missing a reply over the weekend.

-------------------------

philh | 2021-12-15 14:48:19 UTC | #23

Makes sense. I already voted yes, but knowing about this would have me freezing indeed.

As I mentioned on [Twitter](https://twitter.com/phil_h/status/1471090360818487302), I don't care about precedents as long as proposals are legitimate, which is what your comment is questioning. It's too late for my vote, but I look forward to reading @Tardigrade's reply anyway :)

-------------------------

DisruptionJoe | 2021-12-15 22:25:32 UTC | #24

Exactly. Look at user [https://gitcoin.co/haj199](https://gitcoin.co/haj199) for example. This user has done one thing on Gitcoin's platform ever. One $50 "donation" to ForceDAO. These weren't donations to a project in grants. It wasnt even during a grants round!

... and look at how well ForceDAO is doing! [https://www.coingecko.com/en/coins/force-dao](https://www.coingecko.com/en/coins/force-dao)

Was it created just to game the airdrop? I don't know....

-------------------------

Tardigrade | 2021-12-16 00:04:00 UTC | #25

Wow, that’s a lot of information all at once! I appreciate you raising these points, Simona. I think they are healthy in bringing us closer to fully understanding the nature of the problem. I spent a lot of time the last few hours researching more about this project and speaking to the affected users. I also tried reaching out to the Force team to get a better idea of the situation. Here are some of the things I was able to uncover to address your concerns:

“Is there an instance where the “donors” were in effect purchasing their share in ForceDAO?”

The research I found shows that Force and Gitcoin partnered together to host the Force prize which was an ongoing competition scheduled to take place every 6 months in the form of Gitcoin Hackathons. The grant was set up at the time to fund an operation/org to build yield strategies, and never a membership in a DAO. Based on the different sources, this appears to have always been a grant, and the team set it up in conjunction with Gitcoin. There was no portrayal of any equity compensation when it happened, contrary to speculation.

“Is there a record of the accounts who donated actually using or being active contributors to ForceDAO?”

I spoke to some of the eligible members to ask about their contributions to Force, and the two users who make up the largest share of this proposal’s GTC pool (haj199 and sitnyaga) have both been active members to Force DAO. Although Force turned out unsuccessful, both these users played a part in the project. Members of the Force team who I was able to get in contact with confirmed this, noting how Haj199 was consistently active in advisory and strategy assistance, while Sytnyaga is actively assisting with the project’s recent pivot to a new direction following its past difficulties.

At the end of the day, I’d prefer not place words in other people’s mouths by making claims about what they will or will not do, but if my word as the creator of this proposal counts for anything, here’s what I think: I personally do not believe these users will offload the GTC upon claim if this proposal passes.

There is no way to guarantee this and I say this based purely on gut instinct. As an optimist, I always try to see the truth and good in people’s words. Based on their past behavior contributing to Force and based on my interactions with them over the last few months, I think these users truly want to be active in helping govern Gitcoin.

I know I said this before, but having worked with some of these users for months on this proposal, and after listening to their great ideas and plans to contribute to Gitcoin, I think the community will benefit from their future involvement. These users are great workers and I am very grateful to have met them and learned from them in this time period. I understand there is some headwind against the proposal right now, and this saddens me. I have dedicated much time and effort to this proposal because I truly believe in it, and I tried my absolute best to get people to share my enthusiasm towards it as well. It’s been a tremendous journey working on this project for so long and learning so much about how Gitcoin operates during this time period, and I can’t wait to undertake new projects moving forward as well.

I just ask for those of you who voted against this proposal, to reevaluate your vote based on my findings above. And if there are still those who disagree or have any other new information that I haven’t been made aware of to add to the discussion, I gladly welcome it and ask that you please leave a comment. The more angles we cover, the clearer I believe a decision to vote can be made.

-------------------------

haj199 | 2021-12-16 23:54:24 UTC | #26

Fwiw, I firstly want to thank everyone for their efforts here. It's incredible to see the discussion here and the community Gitcoin has built over the last months. Seeing that the majority of votes on the snapshot voted yes, however a minority with sizable GTC allocation have flipped the vote, I feel obliged to chime in as I am a major benefactor here. Responding to @Pop's concern about the GTC being offloaded immediately, I will pledge to lock-up 50% of my GTC for a period of 12months and pledge the other 50% to be donated to future Gitcoin Round grants. Hopefully that also addresses @DisruptionJoe's concern about my activity and benefit to the network. I would also like to say that I worked pretty closely with ForceDAO in the early days after the donation, and though the project has failed, I do not take that as a reason for this proposal to be penalized here. Performance of projects that took part in the Gitcoin Grants was never a metric that was ever used when the original airdrop was put in place to begin with. Hope this addresses some issues and hopefully the community can come through! ❤️

-------------------------

DisruptionJoe | 2021-12-17 14:33:54 UTC | #27

You are not interpreting this correctly. Those aren't whales who flipped the vote. They are stewards who have been delegated votes by users who believe that the steward will more actively pay attention and participate in the governance.

-------------------------

fruktozamin | 2021-12-18 11:22:02 UTC | #28

I am an active GG donator and cant claim my well earned Gtc from a mistake of the Sc.Very disappointed when looking the proposal results.Well done guys💩💩.Planning the spent at least half of my unclaimeable gtc’s in the upcoming GG rounds but i never thought the majorty of community gonna  vote “no” for this proposal and also thanks to wisdom of these Stewards u are gonna change the world🤣🤣🤣

-------------------------

Pop | 2021-12-21 09:20:29 UTC | #29

Thanks for this @haj199 - would love to get some other stewards opinion on this pledge re lock-up and grant allocation. I feel it's a genuinely productive resolution to the questions I brought up and indeed grants spec does not include the expectancy of success for grantees - it's something we absolutely hope for but nowhere was there a specification around it being a condition in the allocation.

-------------------------

bestape | 2021-12-26 02:02:27 UTC | #30

I find this decision to not be generous when given the choice very disheartening and it is highly persuasive evidence that Gitcoin is talking the talk but not walking the walk. 

I have given quite a bit of my time to Gitcoin the past few months and was looking forward to giving much more of my time throughout 2022. But, because of this extremely unfortunate decision to hoard when given the choice, I am questioning whether that is the correct decision (after my Schelling Point obligations conclude of course.) 

Maybe I wouldn't be so perturbed if we weren't building the Green Pill and other regen concepts in this DAO, but we are doing that, and that's why I'm here in the first place. In other words, I'm a bleeding heart here for the hope WAGMIT provides to all members of the community. 

I don't want my good name and honourable reputation that I've sacrificed a lot to maintain over the years attached to a degen community pretending to be regen, a community of good rhetoric but not good substance; that's worse than a degen community being honest about being degen.

Moloch won this round hands down!

Merry Coal Pill Christmas y'all.

Sincerely,
bestape

-------------------------

Tardigrade | 2022-03-23 22:37:35 UTC | #31

Hello,

It's been a while, but I've got some good news for all the users who were deemed eligible for the proposal above. Alberto Cevallos, the founder of the project recently announced that the project will be unwinding their operations, and will be redistributing their possession of GTC to users who were disproportionately impacted by the project's failures, and users who were mentioned in this proposal are included in that list. I am in contact with Alberto and he asked me to compile a list of eligible users.

To preserve confidentiality, if you are one of the users mentioned in the above proposal and would like to be reimbursed, please find me on the Gitcoin discord channel send me a private message with the address you wish to receive your allocation in. I will personally reach out to all of you on discord as well, but I am just bumping this message here in case you don't see my message on there. 

For more information about this redistribution process, feel free to check out the link below. A massive thank you is owed to Alberto and the Force DAO team for going out of their way to make things right for the users on here who were victims of an error in the redistribution process. Awesome work!
https://forcedao.medium.com/winding-down-and-redistribution-8ed28220101b

Hope this news provides some sense of closure.

Best wishes,

-------------------------

bobjiang | 2022-03-30 06:26:12 UTC | #32

Thank you for your efforts and continuous updates here.
Publish this link in #gtc-support Discord channel.

-------------------------

bestape | 2022-07-25 18:57:22 UTC | #33

I just caught the outcome. Deeply inspirational generosity @Tardigrade :pray: . And was well in time for Easter!!

Thank you for holding space for me during that rough patch in my life back in December; sorry my personal issues amplified my response here to an absurd degree.

For what it's worth, I'm very glad this community exists and I'm happy my reputation is somewhat entangled with y'all. :heart: 

ReFi Summer :slightly_smiling_face: .

-------------------------
