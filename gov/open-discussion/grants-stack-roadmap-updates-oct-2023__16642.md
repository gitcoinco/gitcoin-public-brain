---
id: 16642
title: "Grants Stack Roadmap Updates (Oct 2023)"
slug: grants-stack-roadmap-updates-oct-2023
category: open-discussion
url: https://gov.gitcoin.co/t/grants-stack-roadmap-updates-oct-2023/16642
created_at: 2023-10-02T13:14:39.037Z
last_posted_at: 2023-10-03T17:32:47.050Z
posts_count: 6
views: 4082
like_count: 25
---

# Grants Stack Roadmap Updates (Oct 2023)

<https://gov.gitcoin.co/t/grants-stack-roadmap-updates-oct-2023/16642>
meglister | 2023-10-02 13:19:50 UTC | #1

Hi all – I recently posted an update to our roadmap based on GG18 feedback. You can see that GG18 feedback here on the forum (https://gov.gitcoin.co/t/grants-stack-product-reflections-gg18/16423) and on Twitter (https://twitter.com/MegLister/status/1697326744544616602). The Twitter thread to accompany this post is here: https://twitter.com/MegLister/status/1708832178333970532 :) 

First, a few things we’ve been up to since GG18!

1. We've been supporting community-led rounds by launching Grants Stack on Polygon, Arbitrum, and Avalanche. Arbitrum is just wrapping up 4 Quadratic Funding rounds on Grants Stack, and Polygon and Avalanche have plans to launch QF rounds within the next month!
2. We launched Direct Grants, a new feature that allows grants managers to allocate funds directly to projects. You can view a demo of that feature here: https://www.loom.com/share/91aca72b1ff94145863d5010fe7501af?sid=6a60a051-e188-4834-8005-f9eba70a003f
3. We resolved some persistent bugs in our build process and upgraded our front-end deployment system from Fleek to Vercel, enabling us to ship faster
4. In the coming days, you can expect to see us ship Matching Estimates – a favorite feature from the old platform that estimates how much matching power individual donations might have!

![|624x401](upload://61uoHY9bEaRgJIKPiV8CzpF87nN.png)

To address GG18-specific feedback, we summarized all of the pain points and loosely ideated features we could build to address those. We then prioritized those features by impact, feasibility and readiness.

* Impact: will this accelerate Grants Stack adoption?
* Feasibility: level of effort + do we have all of the tools and skills we need to do this?
* Readiness: are we confident in the viability of our product solution?

As you can see, Passport and Explorer features rose to the top!

![|624x185](upload://2lKGw94ZJRYP5gA3YNjFRIqsC8x.png)

This week we'll kick off creating a sliding scale for Passport, so that donations that don't reach >20 can still be eligible for some matching funds. Wou can also expect to see Explorer homepage redesigns rolled out for GG19. We're particularly excited about new sort/filter options and community-curated collections!

Preview of those designs:
![Screenshot 2023-10-02 at 9.11.31 AM|294x500](upload://xCc2kC0kXlaTf0U5ygW0T3tcgtI.jpeg)


Unfortunately, we're not going to be able to fix the edit application flow or in-product accept/reject rationale for GG19. I know that the edit application flow is particularly painful and sucks!! We will fix it in the future, but we need more time and thought behind the architecture.

Luckily, our awesome PGF team is working on some automated accept/reject rationale messaging outside of the product that should hopefully ease pain around timeliness and transparency of those decisions.

As always, our roadmap is public, my DMs are open, and would love to hear thoughts/feedback/etc!

https://docs.google.com/spreadsheets/d/1ckMnZWXeJzMfrg8C1g305OE1cRFWaULnu2rpKhnbTdE/edit#gid=0

-------------------------

owocki | 2023-10-02 14:22:43 UTC | #2

[quote="meglister, post:1, topic:16642"]
Luckily, our awesome PGF team is working on some automated accept/reject rationale messaging outside of the product that should hopefully ease pain around timeliness and transparency of those decisions.
[/quote]

one stopgap thing we could do is just make sure the accept/reject emails are sent well before that info is shown on the product.  this would prevent ppl looking at their grant on day 1 and being like "wtf it was rejected but idk why".  cc ppl on PGF who are closer to this @monkeyflower @jon-spark-eco @connor @Sov

-------------------------

meglister | 2023-10-02 15:00:23 UTC | #3

The solution the team is working on (with Absolute Labs) will actually trigger emails based on contract status changes -- so the notification should happen simultaneously with the product update!

-------------------------

FractalVisions | 2023-10-03 15:02:30 UTC | #4

[quote="meglister, post:1, topic:16642"]
This week we’ll kick off creating a sliding scale for Passport, so that donations that don’t reach >20 can still be eligible for some matching funds.
[/quote]

I assume that participation amongst donors will dramatically increase with this ability to get a matching score with less than 20 points. 
We have been preparing our community by telling them to obtain 20 GTC passport points since GG18 so they will be prepared to get matching funds.
Very nice updates here it seems like the team has been grinding nonstop since the last round ended in order to prepare for GG19.

-------------------------

ZER8 | 2023-10-03 16:41:39 UTC | #5

Great to see all the updates and the Direct Grants-this is really interesting. I'm dreaming of a future in which we can have a mix of funding methods in a single grant program :smiley: (maybe it's even possible atm..idk)

[quote="meglister, post:1, topic:16642"]
Arbitrum is just wrapping up 4 Quadratic Funding rounds on Grants Stack, and Polygon and Avalanche have plans to launch QF rounds within the next month!
[/quote]

FYI. The Arbitrum program just ended and the results are great. I can testify to the support received during the Arbitrum grant programs, the team has been extremely responsive and fast to action.

PS. Can't w8 for the matching estimates, people just lov'em!

-------------------------

meglister | 2023-10-03 17:32:47 UTC | #6

Thrilled to hear this! We are so happy to be able to partner with the Arbitrum team -- looking forward to many future collabs :saluting_face:

-------------------------
