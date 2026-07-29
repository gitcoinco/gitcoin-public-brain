---
id: 7705
title: "Gitcoin Disputes"
slug: gitcoin-disputes
category: open-discussion
url: https://gov.gitcoin.co/t/gitcoin-disputes/7705
created_at: 2021-07-04T12:59:32.474Z
last_posted_at: 2021-07-12T20:48:30.546Z
posts_count: 17
views: 3058
like_count: 29
---

# Gitcoin Disputes

<https://gov.gitcoin.co/t/gitcoin-disputes/7705>
tjayrush | 2021-07-04 12:59:32 UTC | #1

I truly don't want to be critical, so please take these comments in the spirit they are intended, but does anyone else find the whole "GitCoin Disputes" mechanism seriously flawed?

I was reviewing a few of the disputes and I have a few comments:

1) There are way too many for anyone to be able to spend time making informed decisions,
2) Making an informed decision is almost totally impossible,
3) There are no clear guidelines for decision making,
4) I fear that by making a public comment in support of identifying a grant as malicious or illegitimate, I am opening myself to harassment from the grantee -- especially given that I would have no confidence in my opinion -- so I simply choose not to remark unless it's a clear case of mistaken dispute -- in other words, I can vouch.
5) It's not at all clear who makes the actual final decision or how,

Sorry if this has been covered or discussed elsewhere. If that's the case, perhaps some kind soul would point me to such information.

Just thinking out loud and hoping to elicit discussion...

-------------------------

Sirlupinwatson | 2021-07-04 17:46:30 UTC | #2

Hi @tjayrush, I hope you are doing well!

Everyone can have his own opinion here or comment a thread as long as it stay a friendly discussion. 

Can you point out to a dispute in particular (I dont think this has been covered before) since most of the proposition here are voted for example, just to make sure that you are not speaking about proposals in general or a about dispute happening here in the forum from a specific thread?

-------------------------

bobjiang | 2021-07-05 00:44:27 UTC | #3

Hi @tjayrush 
Actually you're right, there is no clear rule for now to identify the disputes grant. And the rule is emerging from the community, e.g I know one rule is 

- no token sale or vc fund (if the grant owner has issued token sale or got vc funded, supposed they have enough budget now, )

if you think any grant should not be in disputes, please raise it. 
thanks for your post ;)

-------------------------

AwakeNing_Tong | 2021-07-05 04:44:42 UTC | #4


I think that most people do not have effective thinking and the phenomenon of feedback is objective. You can frame the response format in the question under discussion. Which angles are there for this question? When giving feedback, give feedback on each of these angles.  If the respondent has his own opinion, he can add it. Such measures will bring statistical pressure, and many people are required to participate in counting everyone's ideas.

The above is my opinion,I don’t know if there is a better way, please express your opinion.

-------------------------

tjayrush | 2021-07-05 13:27:31 UTC | #6

Oh. Sorry. I meant the disputes here: https://twitter.com/GitcoinDisputes

-------------------------

tjayrush | 2021-07-05 13:29:50 UTC | #7

Where should I 'raise it'? In the public twitter? That's kind of the point I'm making. It seems that being so public means that if I 'engage' I'm sort of opening myself up to more trouble than it's worth. Especially if I agree with a dispute (in other words, I think the grant should be penalized).

-------------------------

Yalor | 2021-07-05 14:47:42 UTC | #8

I agree there should be a better mechanism for flagging and solving disputes, I think the team has mentioned many times that what we currently have is not ideal, but also Gitcoin staff doesn't have the time or desire to be the judge/jury on each of these disputes. 

It needs to be something that emerges from the community, empowering individuals who have a high trust score to solve disputes as they come up and claim a reward for doing so would be more along the lines of something that could scale. Do you have any suggestions for a good Dispute Resolution System you might like to suggest @tjayrush ?

-------------------------

tjayrush | 2021-07-05 15:05:27 UTC | #9

I'm kind of serious when I say this. I literally thought that's what Quadratic funding was supposed to solve. By funding certain projects and not others the system naturally weeds out shit (because those projects die on the vine).

Has there been any discussion about figuring out exactly how much of this supposed 'abuse' is costing the system as a whole? If the 'abuse' is 30% of the system, that's one thing. If it's 1/10 of 1% that's an entirely different thing. In the later case, I might consider not even trying to solve the 'problem'. (Although, of course, there are dragons there...)

I would want to have those sort of metrics first before I even try to design a solution to what may be a non-issue (compared to the whole pie).

-------------------------

Sirlupinwatson | 2021-07-05 20:29:12 UTC | #10

If there is anything I am willing to help with the dispute resolution. Even for free...

-------------------------

auryn | 2021-07-07 18:51:46 UTC | #11

[quote="tjayrush, post:9, topic:7705"]
I literally thought that’s what Quadratic funding was supposed to solve. By funding certain projects and not others the system naturally weeds out shit (because those projects die on the vine).
[/quote]

This is a common misconception about quadratic funding. It reflects how the contributors collectively value the recipients, not the eligibility of recipients.

For quadratic funding to work as intended, it is critical that the system prevents malicious recipients from being added to the round. Otherwise this is an attack vector similar to a Sybil attack from a malicious contributor.
i.e. if an attacker can add multiple malicious projects to the round, they can spread their vote weight (contributions) among each of their malicious projects and earn a disproportionate portion of the matching pool.

For clr.fund, we initially used [Kleros Curate](https://curate.kleros.io/) for this, but have switched to a [custom built registry](https://github.com/clrfund/monorepo/blob/develop/contracts/contracts/recipientRegistry/OptimisticRecipientRegistry.sol) for the last few rounds as Curate was not yet available on xDai and gas prices were cost prohibitive on mainnet.

The key to any registry option is well defined acceptance and removal criteria, you can check out clr.fund's acceptance criteria [here](https://ipfs.io/ipfs/QmeygKjvrpidJeFHv6ywjUrj718nwtFQgCCPPR4r5nL87R).

I'd recommend that the Gitcoin community come up with a similar set of documents for Gitcoin Grants.

-------------------------

tjayrush | 2021-07-08 10:33:34 UTC | #12

Thanks Auryn.

Does the size of the malicious group matter? If it's 1/10 of one %, that's one thing. If the malicious set is 10-20% that seems to be a different thing. Do we have any measure for the size of the malicious set is and at what point it becomes a problem?

I'm asking if we're solving a problem with the dispute resolution mechanism that actually exists and has a measurable effect or if we're down a theoretical rabbit hole.

There were 10s? of disputes and 1000s? of grants, so that feels like less than 1%. How much of the total grant pool was taken by identified malicious participants? (Sorry if this data is available elsewhere.)

Your point is interesting though. So your registry is sort of solving disputes before the round. Is that one way to look at it?

-------------------------

auryn | 2021-07-12 15:29:52 UTC | #13

[quote="tjayrush, post:12, topic:7705"]
I’m asking if we’re solving a problem with the dispute resolution mechanism that actually exists and has a measurable effect or if we’re down a theoretical rabbit hole.
[/quote]

I the case of Gitcoin, I'm honestly not sure. @owocki or @ceresstation might have more insight on the actual numbers. I'd guess that your your estimate is in the right ballpark.

[quote="tjayrush, post:12, topic:7705"]
Your point is interesting though. So your registry is sort of solving disputes before the round. Is that one way to look at it?
[/quote]

It just formalizes the acceptance and remove criteria and process in a way that Gitcoin currently does not. Projects could be added or removed at any point before, after, or during the round.

-------------------------

owocki | 2021-07-12 16:41:53 UTC | #14

@DisruptionJoe might be able to comment on the http://twitter.com/gitcoindisputes process and the QF dispute resolution process.

-------------------------

DisruptionJoe | 2021-07-12 19:32:08 UTC | #15

@tjayrush I agree with you about the rules not being clear. It is definitely a complicated discussion. 

The issues @auryn brought up are totally valid and part of our consideration.

Another issue is the separation of the Gitcoin platform (all grants) vs an ecosystem (ethereum). As we look to decentralize grants, there will be many ecosystems. Potentially any new funding pool.

Issue 3 would be that if sybil was solved* the mechanism would still be susceptible to outside indirect bribery. You might think of this as the allocation of funds because of the potential for receiving airdrops rather than support for public goods. (I think of the different ecosystems somewhat like forks of the mechanism which can independently decide what is in and out in terms of grants)

Issue 4 is a practical "this is how it has been done" with the gitcoin team having the control. Centralization debt that needs to be paid down. The public oversight is a first big step. Building a mechanism, or using one that is out there as Auryn suggests, could be a way to bypass the gitcoin team having their hand on the controls. 

However, depending how the decentralized grants gets built, it might make sense to wait to do this. (This spec is being worked on with 2 proposals in the decentralize grants workstream) 

The reason I bring this up is there are two broad was to look at this 

Curation via governance -  Lets come up with policy and enforcement

Governance via curation - Let the participants in each collective group curate users & grants that match their requirements. Many experiments make this a self organizing & adapting model

Without knowing which it is, it is hard for Gitcoin to come up with even a starter set of guidelines for ecosystem involvement. 


As far as your not wanting to comment due to retaliation, some of our commenters on the public notion page are using alias accounts. I wouldn't optimize for this in the future, but it is a known issue which we are looking for better solutions which also fit into the larger picture.

-------------------------

DisruptionJoe | 2021-07-12 19:35:41 UTC | #16

I do think that if there were no defensive measures, the system would be corrupted and eventually die. 

Disputes are especially interesting, because they are generally about ecosystem rules, not platform rules. We don't yet have a clear mechanism for deciding who is a participant and how much voice they have at the ecosystem level. 

Additionally we haven't yet used GTC to really clarify this at a platform level yet. Hopefully we can get that clarified soon.

-------------------------

tjayrush | 2021-07-12 19:56:35 UTC | #17

Thanks for your careful reply. You make a good point about using an alias account. Hadn't thought of that.

-------------------------

DisruptionJoe | 2021-07-12 20:48:30 UTC | #18

Forcing the use of an alias is not a great long term solution, but could be solved via some form of MACI or potentially new design in a decentralized solution.

-------------------------
