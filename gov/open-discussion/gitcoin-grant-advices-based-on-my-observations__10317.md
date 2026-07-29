---
id: 10317
title: "Gitcoin grant advices based on my observations"
slug: gitcoin-grant-advices-based-on-my-observations
category: open-discussion
url: https://gov.gitcoin.co/t/gitcoin-grant-advices-based-on-my-observations/10317
created_at: 2022-04-07T01:53:02.313Z
last_posted_at: 2022-04-08T21:33:55.617Z
posts_count: 2
views: 2558
like_count: 1
---

# Gitcoin grant advices based on my observations

<https://gov.gitcoin.co/t/gitcoin-grant-advices-based-on-my-observations/10317>
bobjiang | 2022-05-28 15:39:02 UTC | #1

# What questions the Gitcoin users have
There are some FAQs from Gitcoin users for the grant, you can find them from [Gitcoin support knowledge base](https://support.gitcoin.co/gitcoin-grants/grantee-questions).

-  **Some Grant issues examples**
		- in the beginning of GR13, some grantees didn't know why their grants are inactive.
		- some grants are not in matching round grants
		- for the denied grants, the grantees didn't know next steps clearly.
		- for the appealed grants, the grantees didn't know the status.
		- removing tags, the grantees didn't get notifications for the reasons.

## Grants status

Based on above issues we can see, there are several statuses for the grants, and I would introduce a bit here (please correct me if I am wrong, I am not the grant guru):

- **new** - This is a “virtual” status, without mapping a real status in the database. The new grants are inactive and invisible from web UI.
- **inactive** - The grant is inactive after being created by default. Once the grant is approved, it should be changed to be active. The grant could be set to inactive by the review team after reported and confirmed.
- **opt in for clr** - Eligible to get matching funds from the matching pool. By default the grant is in clr status after approval, but the grantees could de-select clr matching by themselves.
- **cancel (removed)** - The grant will be canceled (removed) from the database.

## Advices for grant status
Firstly it is very confused with the inactive status for the grantees, I would like to re-design the grant status like:

- **new** This is a “virtual” status, without mapping a real status in the database. The new grants are inactive and invisible from web UI.
- **review** The grant is in review phase, it may move to `need more info` or `denied` or `approved`
- **need more info** If the review team cannot make decisions with existing information, the grant could be required to provide more info.
- **denied** The grant is denied by review team
- **approved (active)** The grant is approved and shown on Gitcoin web.
- **dispute** The grant is flagged by the community and in dispute phase.
- **appeal** The grant is in appeal phase (after denied, the grantee could appeal for the result.)
- **cancel (removed)** The grant will be canceled (removed) from the database.

So the happy path should be `new -> review -> approved`.

The major changes are for `inactive` status, which has more meanings for now. Once the grant is in review or dispute or appeal phase, it could be inactive.

Just make the status more clear and meaningful.
I would not describe the details for grant process here, but would like to have deep talk with grant ops team.

**grant tags**

For the grant tags changes, we need a clear process interacting with the users. 

## Grant policies

For now the grant policies are emerging, and we need the clear current policies for the users. According new knowledge base (support) is live, the latest policies are here https://support.gitcoin.co/gitcoin-policy/policy

But for appeal and dispute processes, we need to refine them. For example, there are still 2 stages for appeal process, and stake $15 (https://support.gitcoin.co/gitcoin-policy/policy/appeals/appeal-process-stage-1)

-------------------------

David_Dyor | 2022-04-08 21:33:55 UTC | #2

Some good ideas here Bob.  Thanks for sharing your thoughts.

[quote="bobjiang, post:1, topic:10317"]
But for appeal and dispute processes, we need to refine them. For example, there are still 2 stages for appeal process, and stake $15 ([Appeal Process - Stage 1 - Gitcoin support ](https://support.gitcoin.co/gitcoin-policy/policy/appeals/appeal-process-stage-1))
[/quote]

I updated the appeal and dispute process in the Knowledge Base as a result of the extensive discussions in gr13, but the update is not showing up in the link you provided.  I suspect this is because I am updating a version of the KB that is not propagating to the KB available on Gitcoin.co.  

Here is the link I use to access the KB, and which reflects the appeal process changes recently made (no more deposit required, much simpler, typeform to trigger appeal)
https://discovery-1.gitbook.io/gitcoin-knowledge-base/-MjC5KnuB6HdGrn7Kh8T/gitcoin-policy/policy/appeals/appeal-process-stage-1

I am a bit confused by the fact there are 2 KBs showing up when I log into Gitbook.  One has multiple language translations and one has just two, English and Chinese.  Both are within 'Discovery.'  I took steps to verify the proper version but clearly revising the multi-language version KB was not enough if the old un-revised appeal process is still publicly available.  I will repeat all the updates into the second version today just to be safe.  This is what I see when I log into Gitbook:

![image|235x500](upload://b9CIi2Sau5R47eBQ2xRLGoG9UwU.png)

I think this is related to dCompass and maybe I am updating a KB that never got approved for Gitcoin.co publication.  Not really sure...I am puzzled by this.  It would be helpful to know why two KBs are showing in Gitbook, or equally helpful, if I understood where the content you say is on the Support KB is coming from.   

Thanks again for point that out!

-------------------------
