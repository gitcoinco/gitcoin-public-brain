---
id: 10125
title: "[Proposal] Grants Policy Update: Projects with Tokens"
slug: proposal-grants-policy-update-projects-with-tokens
category: governance-proposals
url: https://gov.gitcoin.co/t/proposal-grants-policy-update-projects-with-tokens/10125
created_at: 2022-03-18T21:52:28.313Z
last_posted_at: 2022-03-29T16:00:25.238Z
posts_count: 33
views: 6427
like_count: 63
---

# [Proposal] Grants Policy Update: Projects with Tokens

<https://gov.gitcoin.co/t/proposal-grants-policy-update-projects-with-tokens/10125>
annika | 2022-03-18 22:00:45 UTC | #1

## Abstract

This post is intended to provide context on, and guide the community to a decision around, grant eligibility criteria as it pertains to projects with tokens.

This post is a Part III follow-up & summary of existing discussions outlined in these two recent governance posts: [Novel Situation #1](https://gov.gitcoin.co/t/novel-situation-1-project-should-not-have-a-token-or-raised-vc-funding/10029), and [Proposed Revision to Grant Eligibility Criteria](https://gov.gitcoin.co/t/proposed-revision-to-grant-eligibility-criteria/10098).

We acknowledge this is a net new policy evaluation happening in the middle of a grants round, seeking to bring near-term resolution to a policy ambiguity, which is not ideal. In doing this evaluation, we have identified the need to craft a longer-term, more deliberate & community-involved process for grants policy definition that spans across workstreams.

## Context: Existing Policy

One of Gitcoin’s legacy eligibility criteria reads that, to be eligible for a grant on the Gitcoin platform, a project *“should not have its own token or have raised over $500k in VC funding”*.

This criteria was put into place in early 2021 before the DAO provided a strong governance model for Gitcoin Grants. The Web3 space has evolved substantially since then, and many early-stage projects now launch governance tokens at inception.

These tokens often have little-to-no economic value at the onset – and, as such, questions have been raised about whether this eligibility criteria should be revised to be more inclusive to these types of projects. Currently, FDD is declining all grant applications that have their own token of any sort.

This includes:

* Projects which currently have a token
* Projects which have any mention of an airdrop or sale on their grant page or any of the links on the grant page including their Twitter, Website, or github.

## Bright ID Case

BrightID grant #191 was flagged by a user during GR12 as having a token. This dispute was escalated to the review team which determined that they are ineligible because they do have a token. After GR12, an appeal was raised by the BrightID team on this topic. This appeal relates to [their existing grant](https://gitcoin.co/grants/191/brightid-universal-proof-of-uniqueness-panvala-le), which has raised over $150K in Gitcoin Grants funding in prior rounds.

The email outlining the appeal, which can be read in full [in this post](https://gov.gitcoin.co/t/novel-situation-1-project-should-not-have-a-token-or-raised-vc-funding/10029), served as a catalyst for revisiting & re-evaluating this eligibility criteria, as well as for more clearly defining the [FDD Appeals process](https://docs.google.com/document/d/1y9lFdlfgTf3GvATmgVbPUaK5WWMuQ44uICvBGuhaB6A/edit) as a whole (future post to come on this).

## Proposed Policy Amendment

After extensive cross-workstream dialogue, as well as public discourse in the comments on the posts mentioned above, PGF & FDD propose revising the criteria as follows:

*A project in the Main Round cannot:*

* *Have a token with a fully-diluted market cap of greater than $20 million*
* *Have raised over $500k in VC funding*

We recognize that these criteria are somewhat arbitrary, but we believe creating an objective starting-point threshold from which we can iterate, rather than maintaining the status quo of nebulous criteria, is a) more scalable for the program long-term, and b) much clearer to current & prospective grantees.

Finally, the verbiage “in the Main Round” was specifically included to give us the flexibility to de-couple Ecosystem & Cause Rounds from this logic in the future. Today, all QF-eligible projects on the Gitcoin Grants platform are in the main round – so this applies to all grants for the immediate term – but we may de-couple ecosystem/cause rounds in the future, such that the funding partners of those rounds can make their own decisions around eligibility for their pools.

## Grants Policy Definition Process (Longer-Term)

This discourse has led us to the realization that there is not clear accountability or process as to "who defines grants policy, and how?" – whether it’s PGF, FDD, the community-at-large, or a combination thereof, and how we collaborate and govern policy definition. We certainly want to make this a joint, community-heavy domain, and that is something we need to improve on as we continue to progressively decentralize the running of our grants programs.

As a next step, PGF & FDD will come back to the forum prior to Grants Round 14 with a proposed policy definition process for discussion.

## Snapshot Vote

In the interim, on the ‘Projects with Tokens’ policy, we propose moving to a Snapshot Vote with two options:

**1. Maintain “no token” status quo**

This would mean that we continue with the ambiguous policy (“a grant should not have its own token”), and leave case-by-case decisions in the hands of FDD.

In this case, the Bright ID decision would be handled centrally by that group and would not continue further through governance.

**2. Adopt new $20M market cap threshold**

This would mean that we would adopt the new policy to be implemented for all grants as of GR13. Grants previously denied in GR13 for having a token would have an option to either submit a new grant (preferred) or appeal their old grant’s denial.

In this case, the Bright ID decision would be made by this criteria. Given that BrightID’s FD market cap is $7.6M at the time of writing, and they confirm to have not raised VC funding, they would continue on as a grantee eligible for QF in GR13.

Allowing projects with tokens to not be immediately disqualified does not mean that ALL projects with tokens having a market cap under $20 million will qualify. These grants must still pass all other platform eligibility criteria.

**Wrap-Up**

Given that this post is a “Part III” follow-on post and that community discussions on this topic started [ten days ago](https://gov.gitcoin.co/t/novel-situation-1-project-should-not-have-a-token-or-raised-vc-funding/10029), we plan to move this to a Snapshot vote on Tuesday, March 22nd. This will allow us to have the decision ratified prior to the end of the GR13 dispute period.

Thanks to @DisruptionJoe, @David_Dyor, @connor, @seanmac, @M0nkeyFl0wer for your collaboration & input.

-------------------------

lefterisjp | 2022-03-20 16:20:52 UTC | #2

Thank you for this post Annika.

Indeed the "have a token" criteria may have been way too arbitrary.

But the marketcap proposal sounds equally arbitrary, doesn't it?

What if a developer team creates a token, gives all of it to the community and it has $100m marketcap? They would still have kept nothing for themselves, thus would have no funding at all from the token.

I would guess we would really have to do a case-by-case study, see how the token operates, how many tokens does the team have, and if it is the same team that requests the funding for the gitcoin grant.

Generally the idea is not to punish anybody here. It's just to not let greedy people take money from projects that have otherwise very small sources of funding.

For BrightID's case I have no idea how much they have raised from the token if there was a sale, how many tokens they kept etc. so I can't really give an informed opinion.

-------------------------

DisruptionJoe | 2022-03-20 19:54:18 UTC | #3

Lefteris,

I believe the "$20 million market cap" is a suggestion that puts some reasonable, though arbitrary guideline that helps us start fine tuning the logic. I also think it is important to say that **we are setting precedent on how we want the Gitcoin ecosystem's judicial system to work in the future**. 

The stewards could vote to switch this model in the future so I think both avenues are **safe to try**. 

**In practice, this vote will guide us on which judicial model the community prefers us to try first:**
* Option 1 - A separation of judicial and legislative branches where the judicial branch judges on a case by case basis setting precedents which the legislative branch can turn into policy in the future.
* Option 2 - A system where the policy is continually fine tuned by the votes of the community. In this model FDD uses a letter of law approach and an appeals system guides us to refine and redefine policy as we see the letter of law interpretations diverging from the community's interest. 

Ideally, we would build out a system which would move the functions executed by FDD now, to be executed by the community in a distributed and fair way in the near future. For the time being, FDD would have to both supply judgements AND build the system for the community to supply judgements.

## ANOTHER WAY TO FRAME THE VOTE

**OPTION 1 - MAINTAIN "NO TOKEN" STATUS QUO**

***How it would play out for BrightID***

BrightID appeal would most likely be upheld and they would be allowed to participate in GR13.
 
Unless there was significant objection, FDD is currently in favor of ruling to uphold their appeal for the following reasons.

FDD has already found through our Polis surveys that the community overwhelmingly wants us to fund public goods over following the letter of the law. In this case, BrightID is clearly building a public infrastructure needed for digital democracy. Their token was an opportunity to let the community drive it's governance. 

The token has not provided sufficient funding to allow BrightID to continue building. 

***How it would affect the Gitcoin Ecosystem moving forward***

This would set a precedent for many other appeals to be judged case by case by FDD which would act as the judicial branch of the system. 

Once a pattern was seen, then it would be appropriate for the legislative branch (Stewards) to create policy which would "hard code" the bottoms up norms created by the community.

I think it might help to say that option 1, letting FDD decide on a case by case basis is similar to English common law allowing the high courts to adjudicate on a case by case basis. The results of these cases comprise our legal canon which can all be used as relevant examples used to determine precedent.

FDD has continued to advance how decentralized and transparent our processes are. While not near perfect yet, we have come a long way from Kevin or Joe deciding. For GR13 & 14, FDD would be deciding most cases while building a system for the community to decide in the future.

In this scenario, I would push for FDD to create a tiered appeals system with the following characteristics
* Creation of oversight mechanisms at "appellate court" level
* Implementation of external appeals panel (Jury duty!)
* High quality documentation of cases and processes to make FDD appeals process "forkable"


**OPTION 2 - Adopt new $20m market cap threshold**

***How it would play out for BrightID***

BrightID would be eligible for GR13 as they would not be in violation of any policy. 

***How it would affect the Gitcoin Ecosystem moving forward***

Option 2 would fundamentally change how the policy for the Gitcoin platform (and currently the main ethereum round as well) is governed. 

In this system, an appeal to the current policy not matching the intended desires of the community would trigger a quick research and writing process wherein FDD & PGF would draft a policy update to be voted on by stewards. 

The FDD would then judge each grant application based on the letter of the law, removing an opportunity for bias. I believe this will actually help us build a scalable future. 

FDD is working to build tools that help the community validate whether grants match a criteria. In this type of system, the community members themselves would participate in judging whether grants met a specific criteria. FDD's role fundamentally changes from judge to builder of a trustless system which is less expensive to defend than attack. 

## In conclusion

My vote will be for option 2. I believe it is: 
* Less empowering (and stressful) to FDD
* More scalable
* Fixes some fundamental problems in the US legal system by being built on better communication and value rails.

-------------------------

lefterisjp | 2022-03-20 20:45:22 UTC | #4

I see you are trying to solve 2 different problems here in a misguided way.

**Problem 1**: BrightID not having sufficient funding from the token so they should still be eligible for gitcoin grants.

**Problem 2**: Figure out a way to judge which projects with tokens should be eligible for a gitcoin grant and which ones should not.


The proposed solution seems to try and address both which it should not. The 20m marketcap is arbitrary for the reason I explained [above](https://gov.gitcoin.co/t/proposal-grants-policy-update-projects-with-tokens/10125/2?u=lefterisjp). It does not really address problem 2.

The argument that we can change it later to make more sense does not sound like a sufficient reason to go ahead with this change.

From what I understand there is a pressure of time (?) in order to make BrightID still eligible for GR13 before ratification? Then let's just try to address **Problem 1** and think on **Problem 2** a bit longer.

The information we would need for this is how much funding does the brighID team itself has gotten from the token.

1. Was there a token sale? If yes how much was sold and what was received.
2. If it was just a token creation event how much of the token does the team own?

I think we all want the same thing in the end. Let's just go towards it the right way without rushing to create new rules without thinking them through first.

-------------------------

polarpunklabs | 2022-03-20 23:01:07 UTC | #5

I would just echo the above that Problem 2 is a quite complicated question involving the evolving nature of Gitcoin governance. It should be parked until after the round. 

A decision on BrightId is clearly more pressing. It seems Problem 1 is already answered in that 'the community overwhelmingly wants us to fund public goods over following the letter of the law.' Since BrightId is 'clearly building a public infrastructure needed for digital democracy' then the surveys tell us the token issue is not the deciding factor here. 

I don't think this particular case then needs to be binding for all other cases. 

Regarding Problem 2, I also wonder to what extent the community would be happy to see issues like this delegated to FDD. I'm not super closely involved in GitcoinDAO, just an observer from an academic perspective, but I actually think the degree of decentralisation currently present is quite a nice balance. While a desire to ever more decentralisation is commendable a quick survey on just how closely the community wants to be involved in refining policies around eligibility might be sensible.

-------------------------

annika | 2022-03-21 03:24:07 UTC | #6

[quote="lefterisjp, post:2, topic:10125"]
Indeed the “have a token” criteria may have been way too arbitrary.

But the marketcap proposal sounds equally arbitrary, doesn’t it?
[/quote]

Sure, it's equally arbitrary, but it at least begins to limit our scope to the subset of projects with tokens that actually need funding. If all projects with tokens are allowed, the aperture is super broad -- projects with multi-billion dollar gov token treasuries are technically eligible.

If I were a new grantee to Gitcoin trying to determine if I fit the bill, I think I'd appreciate at least directional clarity.

[quote="lefterisjp, post:2, topic:10125"]
What if a developer team creates a token, gives all of it to the community and it has $100m marketcap? They would still have kept nothing for themselves, thus would have no funding at all from the token.
[/quote]

This is an interesting corner case; I haven't heard of any projects that have given 100% to community - but we should certainly have a process that accounts for and reviews situations like this.

IMO, in order for the grants program to be scalable, this should be an *exceptions process* -- where projects like this one have the opportunity to raise their hand and make their case as to why they should be included, in spite of the $20M (or whatever dollar figure) cap -- rather than a standard "FDD-reviews-the-issuance-details-of-every-single-token" process. 

To give grantees proximate clarity, to have *something* to go off of --  and then to intentionally build in a process for the "we-gave-away-all-our-tokens" type exceptions to make their case.

Blank slate case-by-case review for every grantee is not sustainable.

[quote="lefterisjp, post:4, topic:10125"]
From what I understand there is a pressure of time (?) in order to make BrightID still eligible for GR13 before ratification? Then let’s just try to address **Problem 1** and think on **Problem 2** a bit longer.
[/quote]

Yes, this is correct. 

The BrightID decision needs to be finalized by the end of the GR13 disputes period, which I believe is March 28th.

My personal bias would be towards action and to try to come to community agreement on a more scalable starting policy that's directionally right, such that BrightID can be evaluated in that framework, rather than as a complete one-off. 

That said, I totally appreciate the concern around the timeline and I'm good with whatever the community decides.

-------------------------

bobjiang | 2022-03-21 05:04:56 UTC | #7

Hi @annika 

From my understanding, there should be 2 votes from this post:

1. Update grants policy
    - maintain "no token" status quo
    - adopt new $20m market cap threshold 
    - [my suggestion based on discussion] add a case-by-case option, not sure the name

2. brightid case decision
    - eligible for GR13
    - not eligible for GR13

sorry I have a small brain, cannot deal with much info at the same time.
so for the topic one, I would support `adopt new $20m market cap threshold `

and also we should have a machinism to update the grant policy.

-------------------------

thelostone-mc | 2022-03-21 06:47:56 UTC | #8

+1 of splitting this into  2 separate proposals/posts.
The 20m cap while sounds better than a blanket ban on if the project has token does sound more appealing but I do think it would have to be more detailed to cover out corner cases like the one [lefterisjp](https://gov.gitcoin.co/u/lefterisjp) mentioned. (there may be more as well)

Moving onto bright ID -> asking the team if they are open to sharing 
- Token sold
- % Owned by the team 

And using that information to decide if they can take part in GR13 / should step down to allow other projects to get more funds.

-------------------------

polarpunklabs | 2022-03-21 15:26:22 UTC | #9

I think the sense of being overwhelmed is what I was trying to get at. 

Vote 2 should happen soon. Vote 1 should be deferred until after the round as it seems unwise to adopt such a change in the middle of a round or just after.

-------------------------

annika | 2022-03-21 16:41:14 UTC | #10

Sounds good, thanks everyone for your feedback. 

What I am hearing pretty universally is that we should expedite the BrightID decision as a one-off and hold off on broader policy definition.

@DisruptionJoe - in light of the community comments here, I don't think we should move to a Snapshot vote tomorrow on the whole proposal, but rather move forward on BrightID alone.

Based on FDD's current process, how will that decision be handled? Is done in isolation by the policy squad, without community input, or does it go to a full Snapshot vote of its own? I assume others may not have clarity here either so I want to have this discussion on next steps in public :slightly_smiling_face:

-------------------------

David_Dyor | 2022-03-21 19:39:08 UTC | #11

The FDD has not needed Snapshot yet and has been able to use discussion, emoji-signalling, and polls to make group decisions.  I would guess this won't change anytime soon.

I appreciate your statement to delay the snapshot vote pending further discussion because it is sensitive to obtaining full participation.  But I am still in favor of voting on the change because I believe it is a positive change.  It will help both reviewers and grantees absorb both the letter & spirit of Gitcoin laws (briefings/policies/documentation).  

Joe and Annika have been foundational to getting this murky issue clarified.  Thanks so much you two!  I bias towards community-cohesion over independence.  If the community feels we should discuss this more before taking action than so be it.  I support the community vision...I just hope we can get quick results and not disappear into endless debates.

As a reminder, during the three part progression of this topic it became clear that the BrightID entity that created the grant actually doesn't have a token.  Thus a technicality would enable us to immediately reverse the BrightID grant denial.  The entity that created and manages the $BRIGHT token is legally separate from BrightID Dao.   This quickly resolves Q2 however it may not be the best way forward as even though the 2 bright organizations are not legally linked they are connected in theory through name and actions.

-------------------------

DisruptionJoe | 2022-03-21 20:08:52 UTC | #12

[quote="annika, post:10, topic:10125"]
Based on FDD’s current process, how will that decision be handled? Is done in isolation by the policy squad, without community input, or does it go to a full Snapshot vote of its own? I assume others may not have clarity here either so I want to have this discussion on next steps in public :slightly_smiling_face:
[/quote]

I believe I outlined what I think will happen if we decide not to do a snapshot vote here: 

[quote="DisruptionJoe, post:3, topic:10125"]
**OPTION 1 - MAINTAIN “NO TOKEN” STATUS QUO**

***How it would play out for BrightID***

BrightID appeal would most likely be upheld and they would be allowed to participate in GR13.

Unless there was significant objection, FDD is currently in favor of ruling to uphold their appeal for the following reasons.

FDD has already found through our Polis surveys that the community overwhelmingly wants us to fund public goods over following the letter of the law. In this case, BrightID is clearly building a public infrastructure needed for digital democracy. Their token was an opportunity to let the community drive it’s governance.

The token has not provided sufficient funding to allow BrightID to continue building.
[/quote]

I am ok with moving forward and having FDD make the call on the BrightID case without a snapshot vote. This is what has been done in the past. 

The reason this case is different is because we built out an appeals process and found a legitimate case where the appeal serves as guidance to future policy. (as opposed to being a reviewer error or poor interpretation of current policy)

[quote="lefterisjp, post:4, topic:10125"]
The proposed solution seems to try and address both which it should not. The 20m marketcap is arbitrary for the reason I explained [above](https://gov.gitcoin.co/t/proposal-grants-policy-update-projects-with-tokens/10125/2). It does not really address problem 2.
[/quote]

Because this situation is a "first" to make it this far in the appeals process FDD has built out to decentralize the decision making process, I do believe it is fair to judge both together. By saying we want FDD to make the decision or not, we establish a precedent which will be used for future appeals. 

I don't see how the decision here can not set a precedent, therefore there is no way to handle these separately.

However, because these types of calls (grant eligibility decisions) have always happened in FDD, the way forward that does not include a snapshot vote would be for FDD to make a call and write up the reasoning for it.

Then perhaps PGF could be responsible for updating policy in between rounds?

The token and funding info is all on the original post about the BrightID appeal: https://gov.gitcoin.co/t/novel-situation-1-project-should-not-have-a-token-or-raised-vc-funding/10029

-------------------------

lefterisjp | 2022-03-21 20:55:52 UTC | #13

I have to comment here that 2 different entities is not a reason to automatically reverse decisions.

In BrighID's case I don't have all the facts so can't speak from factual knowledge but my interactions with them have been very positive so I don't think they would appeal without a reason and try to cheat Gitcoin.

BUT, if for example I(Lefteris) have 2 different entities, both of which I have major control of. Say Rotki Germany and "Opensource software Cayman Islands", and the latter creates and sells a token, but the rotki Germany entity still wants to keep the grant matching ... I hope you would challenge me there.

What I am trying to say is that it's hard to have blanket rules and unfortunately I am afraid we would need case by case decisions after reviewing all the facts.

-------------------------

lefterisjp | 2022-03-21 20:57:46 UTC | #14

> The token and funding info is all on the original post about the BrightID appeal: [Novel Situation #1 - Project should not have a token or raised VC funding](https://gov.gitcoin.co/t/novel-situation-1-project-should-not-have-a-token-or-raised-vc-funding/10029)

I read that post and I still can't find out how much has the DAO/team kept for itself. What is their treasury situation?

-------------------------

DisruptionJoe | 2022-03-21 21:14:05 UTC | #15

I am comfortable making the case by case decisions in FDD as has been done in the past, but would like the process to be explicit because this is the first appeal to get to this level. 

Not deciding is a decision! We might call this **OPTION 0 - Maintain the status quo and DO NOT explicitly agree to FDDs authority in this domain and set clear boundaries**

If we maintain course, this is what the outcome might be:

1. FDD source council makes a decision and writes it up on the gov forum.
2. PGF & FDD Policy writes up policy recommendations based on the gov forum conversation
3. FDD Grant Reviewers & Approver follows these policy recommendations for initial approval of new grants
4. PGF writes up a policy update between rounds to be ratified (has the problem of bundling many policy decisions into one vote)

If we go with Option 1 or Option 2 via snapshot vote, then the decisions of FDD or the snapshot vote will have more legitimacy. (Option 1 & 2 as outlined here: https://gov.gitcoin.co/t/proposal-grants-policy-update-projects-with-tokens/10125/12?u=disruptionjoe)

I would like to see us start the appeals system in a legitimate way rather than leaving it as is. 

A snapshot would need to start tomorrow or Wednesday by the latest to be able to pass in time for this round. 

If we get positive approval from 5 stewards by Wednesday, I would advocate for us to put it up for a vote and not let our community be guided by inaction. 

I'd also like to refrain from thinking we can find the BEST ANSWER and instead think "Is the recommendation of the people closest to the work SAFE TO TRY" 

The complexity of the situation is high, therefore a sensing and responding methodology is practical.

-------------------------

DisruptionJoe | 2022-03-21 21:17:07 UTC | #16

[quote="lefterisjp, post:13, topic:10125"]
I have to comment here that 2 different entities is not a reason to automatically reverse decisions.
[/quote]

I also agree with your sentiment here, Lefteris. @David_Dyor is making sure the entire surface area of the problem is in view, but it seems to me that his interpretation is that he agrees with you that we should do a case by case analysis and is informing of the DOWNSIDE to pushing for a letter of the law interpretation. (Which you aren't pushing for, but some might)

-------------------------

DisruptionJoe | 2022-03-21 21:23:55 UTC | #17

@castall can you share the info @lefterisjp and @bobjiang requested here?

-------------------------

castall | 2022-03-22 01:40:25 UTC | #18

If we're talking about changing to rules to this,

[quote="annika, post:1, topic:10125"]
*A project in the Main Round cannot:*

* *Have a token with a fully-diluted market cap of greater than $20 million*
* *Have raised over $500k in VC funding*
[/quote]

Then, yes, BrightID would fit within those rules.

If we're thinking of including other rules about the value of tokens sold, or the value of tokens given to the team, and we want to look at BrightID as an example, no tokens were sold and no tokens were given to the team.  I think this is unusual for community token launches. I normally see around 15% reserved for the team.

Unfortunately, BrightID's token model is not likely to be used by other projects, so the decision isn't likely to be of much help.  I didn't think about this when we agreed to be a test case for a new appeal process in December.

-------------------------

connor | 2022-03-22 03:30:45 UTC | #19

I generally agree with the sentiment that many of these situations will be unique cases and it's hard to put a blanket policy down. I also feel that setting a policy like this going forward should take time and deliberation, and not be rushed for GR13 or to close a specific case (like BrightID). But I do feel the urgency to make a call on BrightID and I think I'd encourage FDD to make the final call for now.

Regarding the $20m threshold - I think we should focus on a project's treasury and not the market cap - what if the token is 100% owned by community members? This is naturally hard to measure and verify, so it's maybe not the best metric, but I struggle to think of something better.

It seems like these unique 1 off cases will continue to be raised, and it's likely not possible to set a policy across the board that is fair to all, but it's also not possible to scale governance votes for each and every dispute. So given that, I'd like to throw out the idea of setting a "loose" policy on funding/tokens for grants between GR13 and 14, with plenty of time to debate. And then maybe using governance to elect a "board" of decision-makers who have the final say, independent of FDD. Governance can then vote to tweak the general policy or board members in the future when they see fit.

-------------------------

kyle | 2022-03-22 04:12:46 UTC | #20

[quote="lefterisjp, post:4, topic:10125"]
I see you are trying to solve 2 different problems here in a misguided way.

**Problem 1** : BrightID not having sufficient funding from the token so they should still be eligible for gitcoin grants.

**Problem 2** : Figure out a way to judge which projects with tokens should be eligible for a gitcoin grant and which ones should not.

The proposed solution seems to try and address both which it should not.
[/quote]

This is so well stated. :raised_hands: I agree that we are conflating a few problems together and love that we are starting to tease them apart. Thank you Lefteris!

[quote="David_Dyor, post:11, topic:10125"]
The FDD has not needed Snapshot yet and has been able to use discussion, emoji-signalling, and polls to make group decisions
[/quote]

This makes me a bit weary. I will trust the intention of this comment, but for policy making, bringing these items to the community and not just leveraging emoji reactions would likely be more credible. Once again, I dont have the context here, just would caution making any larger decisions on this mechanism (ie, who is invited to emote, how much information and time do they have to decide, etc.)

[quote="David_Dyor, post:11, topic:10125"]
it became clear that the BrightID entity that created the grant actually doesn’t have a token
[/quote]

As Lefteris mentioned, this just isn't true in spirit and I don't feel like this would stand up in any real evaluation.

[quote="castall, post:18, topic:10125"]
no tokens were given to the team
[/quote]
I am really surprised to hear this. I assume the team participated in the fair launch? [Eligibility criteria here](https://brightid.gitbook.io/brightid/bright/getting-bright/fairdrop/eligibility) would likely favor the team doing development (rightfully so!). It feels dishonest to say the team was given no tokens though :thinking: 

-----
This may be the pessimist in me, but I feel like a token was launched, and was optimistically positioned as a way to fund development. Now that the markets have cooled and that is not sustainable as once hoped  the question becomes, should BrightID be allowed to receive matching  funds again. 

Interested in seeing the vote options as they come up :)

-------------------------

bobjiang | 2022-03-22 14:26:41 UTC | #21

Hi @castall 

From what you said, I can get following info (please correct me if I am wrong):

1. Brightid team reserved about 15% token.
2. 0 token sold from the team

so would you share the team multi-sig address? (not sure if it is sensitive to be public, if yes, please find a proper channel to share in Gitcoin discord).

-------------------------

David_Dyor | 2022-03-22 16:59:04 UTC | #22

[quote="kyle, post:20, topic:10125"]
isn’t true in spirit
[/quote]
I agree it is a weak argument and I explained why in my post.  I am simply trying to pull all information into this discussion and ensure nothing gets ignored.  

[quote="kyle, post:20, topic:10125"]
This makes me a bit weary
[/quote]
Yeah daos have a funny way of making me weary too.  Full empathy with you on this!  In all seriousness, I see the FDD decision making as a feature not a bug.  We are learning which types of decisions require various methods and info preservation.  The ability of the fdd to rapidly signal on simple matters has helped us adapt and pivot along the way.  And this is not the topic of this post.  We are discussing projects with tokens and somebody asked how the fdd would likely make the next decision.  My response was specifically to answer her question, not table fdd decision-making for inspection and critique.  

At risk of irritating y'all, I want to point out that it can be difficult and time-consuming to achieve Dao consensus.  We are so close to actually making a beneficial policy change derived from an appropriate process it would be sad and counter-productive to cancel it, in the hopes that maybe in some hypothetical future we will sit down to address the issue again.

Procrastination is the enemy and we have a great simple modification here that had been created by a PG/FDD co-lead process which involved ample public discussion.  Do we really think more pages of debate will create changes to the proposed changes?  I suggest it is unlikely and we move ahead with the suggested changes.  However, I will support the community majority position.

-------------------------

DisruptionJoe | 2022-03-22 20:56:53 UTC | #23

This needs to either go to a vote tomorrow or be left as is... which is a vote for option 0. 

[quote="DisruptionJoe, post:15, topic:10125"]
A snapshot would need to start tomorrow or Wednesday by the latest to be able to pass in time for this round.

If we get positive approval from 5 stewards by Wednesday, I would advocate for us to put it up for a vote and not let our community be guided by inaction.
[/quote]

Do we currently have comments from 5 or more stewards @Pop? What is the process for us moving this forward in the most legitimate way?

-------------------------

DisruptionJoe | 2022-03-23 16:17:50 UTC | #24

# Moving Forward with Input from this Thread

Based on the feedback from the community, and given we did not receive at least 5 steward comments in favor of moving this motion to a snapshot vote, FDD is moving forward with Option 0 for the BrightID appeal.

## FDD Judgement of BrightID Appeal

**After judging this case, FDD made the decision to uphold BrightID’s appeal, for two primary reasons:**

1. The changing nature of how web 3 is using tokens such as governance tokens creates a divergence between the intentions of the community and the policy as written today. “Cannot have a token”
2. BrightID clearly fits the definition of a public good as infrastructure which supports digital democracy. Our [Polis report](https://pol.is/report/r2dxjrdwef2ybx2w9n3ja) which received 138 responses from the community overwhelmingly shows that the community wants us to “fund public goods” before worrying about the semantics of policy. While their launch of a token hoped (and still does) hope to give them a sustainable funding model, they have not achieved this status yet.

**As a result of this decision, the BrightID grant will be included in GR13 and eligible for matching funds in the round.**

As discussed above, policy will be re-evaluated post-round, and we welcome input on that process.

Thank you to @annika @David_Dyor, the stewards & community members who took their time to weigh in, and @castall and the BrightID team for going through the experience of being the first appeal to go through the full Gitcoin appeals process. 

## Situational Context

1 - FDD source council voted as the "appellate court" to decide if the appeal had merit to be heard.

2 - FDD put it to the community on the governance forum saying "we would like this to be a vote to determine precedent on how we deal with appeals at this level because it is the first case to get to this level."

3 - Because it did not get enough positive steward attention to put it to a snapshot vote, Option 0 has been selected. 

4 - This post serves as communication of FDD's justification for it's decision to uphold BrightID's appeal, include them in GR13, and informs the community on potential next steps.

[quote="DisruptionJoe, post:15, topic:10125"]
Not deciding is a decision! We might call this **OPTION 0 - Maintain the status quo and DO NOT explicitly agree to FDDs authority in this domain and set clear boundaries**

If we maintain course, this is what the outcome might be:

1. FDD source council makes a decision and writes it up on the gov forum.
2. PGF & FDD Policy writes up policy recommendations based on the gov forum conversation
3. FDD Grant Reviewers & Approver follows these policy recommendations for initial approval of new grants
4. PGF writes up a policy update between rounds to be ratified (has the problem of bundling many policy decisions into one vote)
[/quote]

[quote="DisruptionJoe, post:3, topic:10125"]
***How it would affect the Gitcoin Ecosystem moving forward***

This would set a precedent for many other appeals to be judged case by case by FDD which would act as the judicial branch of the system.

Once a pattern was seen, then it would be appropriate for the legislative branch (Stewards) to create policy which would “hard code” the bottoms up norms created by the community.

I think it might help to say that option 1, letting FDD decide on a case by case basis is similar to English common law allowing the high courts to adjudicate on a case by case basis. The results of these cases comprise our legal canon which can all be used as relevant examples used to determine precedent.

FDD has continued to advance how decentralized and transparent our processes are. While not near perfect yet, we have come a long way from Kevin or Joe deciding. For GR13 & 14, FDD would be deciding most cases while building a system for the community to decide in the future.

In this scenario, I would push for FDD to create a tiered appeals system with the following characteristics

* Creation of oversight mechanisms at “appellate court” level
* Implementation of external appeals panel (Jury duty!)
* High quality documentation of cases and processes to make FDD appeals process “forkable”
[/quote]

-------------------------

David_Dyor | 2022-03-23 18:23:57 UTC | #25

I never get tired of watching you tie-together seemingly disparate concepts and individuals/groups.  Thank you Joe for bringing closure to this incredible 3 part process in a way that clearly describes what has happened as well as what is happening next in the world of grant appeals.  I am optimistic the lessons taken from running this actual appeal will make future appeals leaner and faster.  And thanks to all who contributed to these talks.  i think it is worth noting we came very close to moving to steward vote.  It is a bit murky but  I think I saw at least 3 supportive steward comments maybe 4.

-------------------------

castall | 2022-03-24 01:52:44 UTC | #26

[quote="bobjiang, post:21, topic:10125"]
Brightid team reserved about 15% token.
[/quote]

Sorry that's not correct.  I was just pointing out 15% as an example of a typical amount.

[quote="bobjiang, post:21, topic:10125"]
so would you share the team multi-sig address?
[/quote]

There is no team multisig.  The team didn't receive any tokens.

-------------------------

castall | 2022-03-24 02:34:29 UTC | #27

[quote="kyle, post:20, topic:10125"]
was optimistically positioned as a way to fund development. Now that the markets have cooled and that is not sustainable as once hoped
[/quote]

This isn't the right narrative. $Bright token is performing much better than we ever expected, but we never expected it to cover BrightID core development. If one day it could cover the costs, great, but we never anticipated that.  That would be very optimistic indeed.

Whether there is a possibility of a token or DAO treasury being used to fund core development at some future time (I hope it can, but we need other options, like Gitcoin grants) is different than saying the core team received tokens, which they didn't.

I'm not trying to paint us in a more positive light, I'm trying to dispel misinformation, so that if there's any use for this token launch to set a precedent, it can be done so accurately.

[quote="kyle, post:20, topic:10125"]
As Lefteris mentioned, this just isn’t true in spirit and I don’t feel like this would stand up in any real evaluation.
[/quote]

I think @lefterisjp was making the point that the same people can control multiple entities and pretend to not be related.  Very true, but not the case here.  United in purpose, but not the same people.  The $Bright token airdrop was meant to be much more spread out to avoid being just the same people.  The link you shared has the right information.

10 million $Bright went to the DAO treasury. That treasury could certainly be used to fund BrightID core, but it hasn't yet, and we need Gitcoin and other grants.

Most projects do take some tokens for the core team or dev team, so I'm sorry we can't be of more help setting a precedent for that with regard to Gitcoin grants.  My personal feeling is that should be OK if a project does that.

I don't know if these will factor in at all to the updating the token guidelines, but in case you all don't know there's another token (actually two tokens) that BrightID has had since before it first applied to Gitcoin Grants in round four.  These have been used to raise funds almost exclusively for the core team. Should a grants project be allowed to charge a fee for its services and sell rights to those services?--because that's what we've done.  You can read about [Sponsorships tokens](https://medium.com/brightid/brightid-sponsorships-5327a8d39f1e) and [Subscriptions tokens](https://medium.com/p/49b7602aa228).  Gitcoin has purchased sponsorships tokens to use in the trust bonus.

-------------------------

bobjiang | 2022-03-24 04:05:08 UTC | #28

sorry sir, I misunderstand you ;(

-------------------------

lefterisjp | 2022-03-24 08:56:35 UTC | #29

> 10 million $Bright went to the DAO treasury. That treasury could certainly be used to fund BrightID core, but it hasn’t yet, and we need Gitcoin and other grants.

At current prices that seems to be ~$3,057,240.

If the DAO's treasury is not used to fund development of the BrightID core then what is the purpose of the DAO and its treasury?

-------------------------

castall | 2022-03-24 19:27:07 UTC | #30

Good question. Since it launched in September, BrightDAO has funded the following initiatives:

1.  Build a [Soulbound NFT standard](https://github.com/BrightID/BrightID-Soulbound-NFT) and an example (free) soulbound NFT that was given away to 10,000 unique people.
2.  Translations of the documentation into Chinese and Spanish.
3.  Upgrades to [BrightID unique bot](https://github.com/ShenaniganDApp/brightid-discord-bot) which is used in 1300 discord servers.
4.  Funding ["meets" parties](https://meet.brightid.org/#/) and discord mods.
5.  [A Trivia event on 1hive TV](https://forum.1hive.org/t/1hive-crypto-trivia-game-update-season-1/4524/10)
6.  Integration of tip.cc so helpful people in the discord can be tipped in $Bright.
7.  Fund the ["coordination cluster"](https://forum.brightid.org/t/build-and-fund-a-dao-coordination-cluster/217/11) to share what's happening in BrightID within the different teams, and PR.
8.  [BrightID gatekeeper for Aragon permissions](https://forum.brightid.org/t/brightid-gatekeeper-for-aragon-permissions/131/9) (for Aragon and Gardens DAOs)

I consider this a great success based on the [mission of Bright DAO](https://dao.brightid.org/covenant) and I hope these kinds of grants will accelerate.

As I mentioned in the appeal, we're also trying to reduce the size and responsibility of the core team so that it doesn't need as much funding as it currently does (about $30k per month).  We could probably cut that down to $10k / month.  We've had a hiring freeze since last year and one dev has left the team.

[quote="lefterisjp, post:29, topic:10125"]
what is the purpose of the DAO and its treasury?
[/quote]

I encourage you to read this.  I hope I've been able to clear up some assumptions you may have had about the story behind Bright DAO and why BrightID core still asks for donations.

> The goal of BrightDAO is to broaden the community that supports BrightID.

https://brightid.gitbook.io/brightid/bright/bright-dao

-------------------------

bestape | 2022-03-25 23:43:10 UTC | #31

I'm purposefully posting this after the fact because my comments are about policy not the matter at hand. I learned a lot about DAO governance from reading this "case study." Thank you all for publishing your reasoning here. 

[quote="DisruptionJoe, post:3, topic:10125"]
* Option 1 - A separation of judicial and legislative branches where the judicial branch judges on a case by case basis setting precedents which the legislative branch can turn into policy in the future.
* Option 2 - A system where the policy is continually fine tuned by the votes of the community. In this model FDD uses a letter of law approach and an appeals system guides us to refine and redefine policy as we see the letter of law interpretations diverging from the community’s interest.
[/quote]

This is very good. You should think about applying for LEETH certification in LexDAO given your multidisciplinary abilities! :slightly_smiling_face:

I believe spirit of the law is much more important than letter of the law. Compare common law with equity. https://en.wikipedia.org/wiki/Court_of_Chancery and https://en.wikipedia.org/wiki/Estoppel#Promissory_estoppel_2 (especially regarding consideration and *quid pro quo*)

Is FDD appeals a tribunal or a court? What I mean by this is can appeals revisit facts established at trial or just application of the law? 

Importantly, letter of the law is wet code and not dry code so interpretations will most likely include some variation between interpreters. The community should contemplate how much variation is reasonable.

One if the issues that arises trying too much to avoid variation in interpretation of the law is policy cannot develop with sufficient complexity to handle matters. For instance, negligence has a ~6 element test: duty, breach of duty, cause, in fact, proximate cause, and harm.

Moreover, how much judicial activism is included in application of the law, understanding no judicial activism is dysfunctional because, among other reasons, Natural language is imprecise? https://en.wikipedia.org/wiki/Statutory_interpretation#Meaning 

Doesn't the "T" in NFT stand for token? if I make 20,000,001 "$1 bills" each with a unique generative art design, can I circumvent the under $20,000,000 policy's letter of the law? https://rarest.org/stuff/dollar-bills#:~:text=Solid%20serial%20numbers%20are%20extremely,than%20one%20with%20repeated%20twos 

I hope Gitcoin considers a final appeal that is conducted by arms-length parties outside of Gitcoin, for instance a reputable ODR service. Considering Gitcoin could be served without an agreement to arbitrate, it might be a smart move. Further, if the community perceives the impartiality of Gitcoin's Snapshot as relatively low now or in the future, ODR final appeal could help bolster confidence.

This is not legal advice.

-------------------------

DisruptionJoe | 2022-03-27 02:29:26 UTC | #32

Thank you for your choice in how and when to engage with this topic.

I'm digging in and learning more here, but overall I think our policy will need expert opinions to help guide the process. It must also be a joint effort between the all the teams which interact with Grants. 

I think we learned a lot and made great progress on our system overall. We now need to vet the processes and bring in subject matter experts to help us get to the next level. This will definitely be an outcome we shoot for before GR14.

-------------------------

David_Dyor | 2022-03-29 16:01:07 UTC | #33

[quote="bestape, post:31, topic:10125"]
Is FDD appeals a tribunal or a court? What I mean by this is can appeals revisit facts established at trial or just application of the law?
[/quote]

Great Q.

imo FDD Appeals is more like a tribunal.  We will revisit facts.  A common example relates to broken website links.  Eg:   When grantees apply the website is broken so the grant gets denied.  The grantee then fixes the website link and requests an appeal.  In these conditions the FDD Appeals absolutely revisits the 'fact' and upon finding a working website link recommends the appeal succeed.  Assuming no other eligibility criteria violations exist ofc.  

We are not so refined as to use and define ourselves by a single model.  Rather we are trying to be comprehensive, fair, and fast.  And do so in a manner approved/vetted by the Steward group & every workstream.

-------------------------
