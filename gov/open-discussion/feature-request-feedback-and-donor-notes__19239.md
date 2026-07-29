---
id: 19239
title: "Feature Request: Feedback and Donor Notes"
slug: feature-request-feedback-and-donor-notes
category: open-discussion
url: https://gov.gitcoin.co/t/feature-request-feedback-and-donor-notes/19239
created_at: 2024-08-08T15:59:05.273Z
last_posted_at: 2024-08-14T00:26:55.588Z
posts_count: 6
views: 2657
like_count: 14
---

# Feature Request: Feedback and Donor Notes

<https://gov.gitcoin.co/t/feature-request-feedback-and-donor-notes/19239>
cauetomaz | 2024-08-08 15:59:05 UTC | #1

### Context:
During a recent discussion with @MontyMerlin , a concern was raised regarding the lack of feedback mechanisms for grant applicants and the potential value of allowing donors to include notes with their donations. This suggestion aims to address these points by proposing new features for the Gitcoin platform.

### Proposed Features:

1. **Feedback Mechanism for Grant Applicants**

   **As a grant applicant, I would like to:**
   - Have a dedicated section where I can view feedback and considerations around the decisions made on my application.
   - Understand the reasons behind the acceptance or rejection of my application to improve future submissions.

   **Benefits:**
   - Provides transparency in the grant decision-making process.
   - Helps applicants learn and grow from constructive feedback.
   - Enhances the overall experience and trust in the Gitcoin platform.

2. **Donor Notes**

   **As a donor, I would like to:**
   - Have the option to add notes when making a donation.
   - Provide specific feedback, encouragement, or suggestions to the grant recipients.

   **Benefits:**
   - Creates a more interactive and engaging donation experience.
   - Allows for better communication and signaling between donors and projects.
   - Helps grant recipients understand donor motivations and preferences.

### Implementation Suggestions:
- **Feedback Mechanism:**
  - Integrate a feedback section in the applicant’s dashboard where they can see detailed feedback from reviewers.
  - Ensure the feedback is structured, clear, and constructive.

- **Donor Notes:**
  - Add a text box in the donation process where donors can write notes.
  - Display these notes to grant recipients in their funding overview section.

### Conclusion:
Implementing these features will enhance the Gitcoin platform by fostering transparency, improving the applicant experience, and encouraging more meaningful interactions between donors and grant recipients.

-------------------------

Sov | 2024-08-08 17:34:58 UTC | #2

Thanks for surfacing this.  I agree it would be good to have a place to share this information as a round operator, grantee, and donor.  We have built some of this functionality into secondary tools, like Checker, but it is not integrated into the core Grants Stack product.

I will share this feedback internally with product and see if we can add this to our list of things to address as we continue to improve.

-------------------------

mars | 2024-08-09 09:21:45 UTC | #3

This is a great suggestion.

A related tool is called Karma GAP (grantee accountability protocol) and it is a requirement to use in CCN (climate coordination network)

CCN round: https://gap.karmahq.xyz/climate-coordination-network

![image|690x351](upload://5BeAvDjm05wFCDLpkUZKss80LIr.png)

Example project: https://gap.karmahq.xyz/project/treegens-3/grants?tab=milestones-and-updates&grantId=0xd8bbf22b3f669d687d22c259d728116318265607180cd6a13d3b0e0a9228ff2f

![image|690x184](upload://pPFcSAMLu9PTOER6G4bNpttxinN.png)

Might be easier to integrate / implement some of the features than to build from scratch?

I encourage you @cauetomaz to check Karma GAP and evaluate how close it is to your requirement / suggestion.

-------------------------

cauetomaz | 2024-08-12 14:54:03 UTC | #4

Hey @Sov , tks for the reply. This was my first contribution on the forum, and im still not sure if is the right place to bring this up, so if you know a better space to discuss this kind of feedback or request i would love to learn how to. 
I'm already aware of gitcoin checker, it's a great tool to research about past grantees, but im not sure about the feedback for projects when rejected. Besides that, thank you and the team for considering my humble suggestions. 

Hey @mars tks for replying, i hope you're having a great day. I know Karma Gap, we're using to make greenpill brasil accountability. Besides that im not sure how can i receive feedback when rejected on rounds from there, or even receive a clear signal from donors, besides the endorsement feature.

Could you give more specific details about how to use karma gap in a way that help with my requests?

-------------------------

mars | 2024-08-13 22:06:57 UTC | #5

[quote="cauetomaz, post:4, topic:19239"]
Could you give more specific details about how to use karma gap in a way that help with my requests?
[/quote]

No. My comment was mostly *“here is a related project in the space, check it out, maybe it it matches your requirements, maybe it is close enough, maybe that’s a good integration / collaboration opportunity”*

I admit I did not interpret your requirements strictly, I was operating in *“maybe close enough check it out”* framework of the conversation. I also wasn’t aware that you know about Karma GAP already.

******

Philosophical comment: collaboration is good. Competition and free market is good. Just like Gitcoin has Giveth / CLR.fund / Octant as entities operating in the space, what are other entities in the Karma GAP space?

_(feedback, updates, suggestions, comments, accountability, milestones, roadmap, donor notes)_

I’m also wondering if there is enough money / scale / demand to hire specialist entities focused specifically of fact-checking, verification, assessments? Think in terms: “project verified by XYZ” acting as seal of approval, something to ensure the project is legit.

_(and the entire rabbit hole of trusted 3rd parties, who is verifying the verifiers, who is evaluating the evaluators, I personally like these 🧠 debates and if you are like me join the chat at [**t.me/ImpactEval**](https://t.me/ImpactEval))_

**EDIT / UPDATE:**

You've inspired me to do "seal of approval" not by XYZ but IEF: [**t.me/ImpactEval/876**](https://t.me/ImpactEval/876)
![image|690x455](upload://2kCcIe5R1A88UIoJtsNHcyXxS6K.jpeg)

Need to figure out a suitable timing. And probably better to spread out across 2 weeks to have some notetaking / publishing / social media / grow time.

We are building in public, and we issued "request for comments" about impact evalution *(cobenefits, externalities)*, join our chat at [**t.me/ImpactEval**](https://t.me/ImpactEval)🌱

https://docs.google.com/document/d/11dmAfVj3dwbQ0LQ6BPTN-dVJI7qR5wjfOhC3FV38cfQ/edit?usp=sharing
![image|688x500](upload://7BgQ8P7Mv2rS3Mhi7ag67cKXGJV.png)
[Link](https://t.me/karmahq/1/486)

![image|690x262](upload://4DoywmcslAd9M80Mt9XckVHV7FK.png)
[Link](https://t.me/karmahq/322/489)

[quote="mars, post:5, topic:19239"]
Philosophical comment: collaboration is good. Competition and free market is good.
[/quote]

Public goods + network effect + [Metcalfe's law](https://en.wikipedia.org/wiki/Metcalfe%27s_law) + anti fragile = easier to feature request a new feature than to build from scratch, especially when you have historical data.
[quote="mars, post:3, topic:19239"]
Might be easier to integrate / implement some of the features than to build from scratch?
[/quote]

Yes. I agree with this sentiment. What do you think? Would you agree as well?

-------------------------

cauetomaz | 2024-08-14 00:26:55 UTC | #6

Hello @mars tks for the details. Sorry for not selecting better words when writing, sometimes the language make the communication harder for me. 
Tks for bringing this discussion, i agree with you that sometimes its better to integrate than building from scratch and im not sure yet about any other tool working in the same scope of gap.karmahq.xyz. 

I already joined the tg group and will be waiting for our evaluation meeting. 🌟

-------------------------
