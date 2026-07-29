---
id: 16423
title: "Grants Stack Product Reflections: GG18"
slug: grants-stack-product-reflections-gg18
category: product
url: https://gov.gitcoin.co/t/grants-stack-product-reflections-gg18/16423
created_at: 2023-08-31T19:28:53.440Z
last_posted_at: 2023-09-06T15:07:36.369Z
posts_count: 8
views: 1845
like_count: 35
---

# Grants Stack Product Reflections: GG18

<https://gov.gitcoin.co/t/grants-stack-product-reflections-gg18/16423>
meglister | 2023-08-31 19:28:53 UTC | #1

Hi all -- I recently posted a twitter thread about Grants Stack product during GG18 that I wanted to capture on the forum as well!

Setting the stage: I joined Gitcoin ~3 months ago to lead product for Grants Stack. Grants Stack launched publicly in May as a new dApp for grants managers that Gitcoin's PGF team also used to run GG18.

**TL;DR**: lots of work to do and things to build, but I feel pretty good about Grants Stack during GG18!

Why?
- Number of donations almost 3x beta round & 2x alpha
- Team addressed top 3 pieces of feedback from beta
- Big increase in product performance/stability from beta

**Improvements from Beta Round**
We addressed the top pieces of feedback we got during the beta round: gas fees, checkout UX, and donation history. We built features/workflows to address each of these. 

We dramatically improved product stability and decreased the number of high-impact bugs (~10 -> 3)!

We also strengthened our internal support processes with clear escalation guidelines, communication channels, and a bug priority matrix that helped our teams be more efficient in resolving bugs and better communicate with users who were impacted by them.

**Feedback from GG18**
We received some great feedback during GG18 & I’m SO grateful to the people who took the time to engage and share. Thank you all!!

On the grantee side, we heard two primary frustrations: an inability to edit applications after submission, as well as lack of visibility into rejection rationale.

Making applications un-editable was purposeful to reduce fraud, but ultimately not the right decision! it's caused too much friction and we plan to change. The timeline is still TBD because there's some contract work to read from the project registry directly instead of capturing a snapshot.

On rejection rationale, we've been discussing two paths forward...
`1` Continue review process as-is & provide comments or criteria fields for rejection transparency
`2` Move reviews process to "filter out spam only" and require applicants to stake GTC (which is then slashed if found to be spam/fraud)
*Would love to hear what you would do in our shoes!*

Donor feedback primarily centered around better discovery and browsing. We hear you :) We're already working on a redesign and looking forward to your feedback as we roll it out. We're planning to start with branding updates, search, sort/filter, and ability to browse all projects (vs select round first). We're also considering how we might use ML to auto-tag or categorize grants since we have a relatively rich text library to build on. If you're interesting in contributing to this project, please let us know!

Finally, we also heard frustration with the Passport experience -- which the awesome Passport team is constantly digesting and adjusting to solve for! In Grants Stack, we're exploring changing the default score or evolving to a sliding scale vs binary passing threshold.

**Finally...**
I'd be remiss not to note, again, how grateful I am to our community for engaging, supporting, and giving feedback during this round! I'm attaching a screenshot from an internal tool (Productboard) where we tag and categorize all of the feedback we receive. It's one of our greatest assets as a product/dev squad!
![F44dslmaMAAGyfY|481x500](upload://x8HRzU8PsfzGQrSNnDm95uOOslh.jpeg)


We know we have a lot to build and improve, but we're committed to continually improving the product so that communities can invest in what matters to them. Public goods are good :revolving_hearts:

-------------------------

jengajojo | 2023-09-01 07:55:01 UTC | #2

Thanks for all your hardwork @meglister 

[quote="meglister, post:1, topic:16423"]
Move reviews process to “filter out spam only” and require applicants to stake GTC (which is then slashed if found to be spam/fraud)
[/quote]

this approach is great at aligning incentives and reducing the overhead for reviews as compared to option 1

-------------------------

owocki | 2023-09-01 13:34:41 UTC | #3


[quote="meglister, post:1, topic:16423"]
I’m attaching a screenshot from an internal tool (Productboard) where we tag and categorize all of the feedback we receive. It’s one of our greatest assets as a product/dev squad!
[/quote]

wow, very decisive data  to see that discoverability is far and away the winning item!

[quote="meglister, post:1, topic:16423"]
. We’re planning to start with branding updates, search, sort/filter, and ability to browse all projects (vs select round first)
[/quote]

I think these changes would be a huge win for discoverability.   

Of course I'd also like to be able to share collections of grants that I recommend to my friends.

I'd be interested in helping the community build tools for discoverability that aren't in grants stack that help with this.  Apps like funding.social that provide new ways of discovering grants.   I bet there is a bunch of different innovative ways we could help people navigate the grants registry.

[quote="meglister, post:1, topic:16423"]
On rejection rationale, we’ve been discussing two paths forward…
[/quote]

It seems like the primary feedback from the community is "the rejection decisions seem arbitrary or qualitative".  I think that both path forwards seem like a good step forward, but I tend to lean towards the second.

[quote="meglister, post:1, topic:16423"]
I’d be remiss not to note, again, how grateful I am to our community for engaging, supporting, and giving feedback during this round!
[/quote]

I heard from many people that they really appreciated hearing directly from you on twitter (where the conversation lives) about their feedback. There were a number of situations where someone posted a frustration with Gitcoin and you calmy, empathetically, and rationally dug into it and defused thte situation.  I think it was great "work in public" style leadership, kudos.

-------------------------

wasabi | 2023-09-01 14:17:44 UTC | #4

[quote="meglister, post:1, topic:16423"]
Finally, we also heard frustration with the Passport experience – which the awesome Passport team is constantly digesting and adjusting to solve for! In Grants Stack, we’re exploring changing the default score or evolving to a sliding scale vs binary passing threshold.
[/quote]

Yes!!! Dynamic Matching is coming! 

Higher passport score = higher matching until it reaches the Matching Cap.

-------------------------

meglister | 2023-09-04 22:22:33 UTC | #5

Thanks for the kind words @owocki and @jengajojo !

I'm personally leaning towards the 2nd (create transparent decision criteria) vs staking. Grantees are worried about the friction that staking creates, plus I'm mindful that we're trying to support and grow direct grants that have a clear precedent for decision matrixes (and not a strong use case for staking.)

Will keep you posted, roadmap is always publicly available: https://docs.google.com/spreadsheets/d/1ckMnZWXeJzMfrg8C1g305OE1cRFWaULnu2rpKhnbTdE/edit#gid=0

-------------------------

Viriya | 2023-09-05 15:27:55 UTC | #6

This is super helpful info @meglister. Pulled some key CTAs and bits of info to communicate on Twitter from this so thanks for that. 

Super interested to further understand how grantee staking might work. Would love to involve grantees from the global south in that design process as I think they'll probably be the hardest hit by the move (even if necessary :slight_smile: )

+1 on discoverability functions. Lists were incredibly useful on cgrants for marketing purposes.

-------------------------

FractalVisions | 2023-09-06 15:29:55 UTC | #7

[quote="meglister, post:1, topic:16423"]
On rejection rationale, we’ve been discussing two paths forward…
`1` Continue review process as-is & provide comments or criteria fields for rejection transparency
`2` Move reviews process to “filter out spam only” and require applicants to stake GTC (which is then slashed if found to be spam/fraud)
*Would love to hear what you would do in our shoes!*
[/quote]

Hello 👋 Meg..!

1. The process of applying for a grant comes with a lack of understanding about the category that one may or may not fall into.

For ourselves we found it difficult to decide whether to choose Open Source Software due to the fact that we have no intention to share our product prior to deployment.

2. There is also a lack of transparency within the grant application process from the decision made by the elected grant council.

In order to provide a fair and unbiased review for grantees it is crucial to rotate review council members during the intake process. 

This will prevent any outside coordination efforts to eliminate certain groups or individuals from participating in the grant cycle with ill intent.

It is also important to note 📝 who the review committee is when a grant is reviewed. That way the transparency of who was involved with the process is not hidden from the public. It will also assist the grantees in determining who they need to speak with to provide additional information if a denial decision has been made.

This also prevents a council member from making biased judgments over and over again. 
Which could be detrimental to the overall health and growth of the ecosystem.

3. A scoring rubric will allow grantees who received a denial from Gitcoin the opportunity to view their strengths & weaknesses for the next grant application opportunity. 

I have included a link to the Scoring Rubric from the Optimism Grants ecosystem to provide an example for Gitcoin. 

This type of information is crucial to the development growth of a team especially when an applicant is denied & required to increase their score in order to qualify for the next proposal application.

https://docs.google.com/spreadsheets/d/1ozeet5kgLOOXZZp9GJ2HOfUr1BjSJ3_FXzo3LTdmCek/edit

4. Allowing a review phase with additional feedback from the review council to help determine whether or not a project should be considered will improve the overall experience of the applicants.

Being able to work through the bumps or kinks of an application with guidance from the review committee ensures that participants are well aware of the guidelines they must follow when applying for a grant. 

This type of transparency increases the trust of community members and builds a stronger alignment of the vision & mission that Gitcoin has provided in order to help fuel the movement of public goods funding.

That’s my two cents for the morning..!

Have a great day Gitcoin family.

-------------------------

meglister | 2023-09-06 15:07:36 UTC | #8

Thanks, @FractalVisions ! Appreciate the thorough response. Since your feedback is centered on how the PGF team (acting as a grants manager who uses Grants Stack) configures rounds, so I'm tagging PGF leads @connor and @M0nkeyFl0wer so they can review!

-------------------------
