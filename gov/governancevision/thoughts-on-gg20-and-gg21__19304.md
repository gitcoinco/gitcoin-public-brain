---
id: 19304
title: "Thoughts on GG20 and GG21"
slug: thoughts-on-gg20-and-gg21
category: governancevision
url: https://gov.gitcoin.co/t/thoughts-on-gg20-and-gg21/19304
created_at: 2024-09-01T13:16:43.739Z
last_posted_at: 2024-09-01T13:16:43.812Z
posts_count: 1
views: 2608
like_count: 2
---

# Thoughts on GG20 and GG21

<https://gov.gitcoin.co/t/thoughts-on-gg20-and-gg21/19304>
Daniel | 2024-09-01 13:16:43 UTC | #1

Jumping into Gitcoin Grants Round 21 (GG21) as a first-time participant, and a second-time observant was definitely an eye-opener. Gitcoin is known for its transparency and community-focused approach, but as someone new to the process, I found myself wondering about a few things… below is a critical review of the experience.

**Observations on Gitcoin’s Processes**

1.	Segregation of Duties (SoD): During my time in GG21, I often heard people say that it’s “the same crypto bros in rotation” handling different parts of the grant process. This made me wonder how well Gitcoin is implementing Segregation of Duties. Ideally, SoD should ensure that no single group or individual has too much control over the entire process. However, if it’s just the same folks rotating through, it might be worth considering how to diversify these roles to bring in fresh perspectives and ensure fair decision-making. From the outside, it isn’t clear how these things operate internally at Gitcoin, and this may in fact be well thought out and implemented, yet I could not find anything that points to this.

2.	SOX-Type Controls: Beyond SoD, other controls like audit trails, regular reconciliation, and independent reviews are essential for maintaining trust in any system that manages significant funds. Gitcoin has made some strides here, but I think there’s still room to grow. For example, bringing in more external audits could help ensure everything aligns with best practices, and formalizing whistleblower protections would encourage people to speak up if something doesn’t seem right. Some of these controls may even entice bigger investors to join in… ISO standards may also help.

3.	The Regen.tips mechanisms: they create a strong incentive for individuals to donate from multiple accounts simply to accumulate more points, which can be exchanged for rewards (later on?) or recognition within the platform, acting as an engagement farming tool for partners like Celo and USDGLO. This practice may facilitate Sybil attacks on Gitcoin by allowing these multiple, often fake, identities to falsely boost the visibility and perceived support of certain projects. Surprise!, because it’s in a decentralized system, it can’t even be proven with ease. When these Sybil identities coordinate their donations, they manipulate Gitcoin's Quadratic Funding (QF) system, leading to an unfair distribution of funds. Instead of fostering genuine community-driven impact, this shifts the focus towards gaming the system for personal gain. The result is a distorted funding landscape where authentic projects are overshadowed by those artificially inflated through such exploitative tactics, ultimately harming the integrity of the platform and disadvantaging legitimate participants…

**Rethinking Quadratic Funding (QF)**

In the paper “A Flexible Design for Funding Public Goods” by Buterin, Hitzig, and Weyl, quadratic funding (QF) is largely described as a mechanism that aims to achieve near-optimal public goods provision by subsidizing smaller contributions more heavily than larger ones, thereby encouraging a broad base of contributors.

However, if the mechanism disproportionately favours projects with founders that have established networks, it would fail to allocate resources efficiently across all potential public goods based on potential impact in start-up cases, and scalable impact for established ones.

This leads to suboptimal outcomes where only the most established or popular projects receive adequate funding, while potentially valuable but lesser-known or new initiatives remain underfunded. Thus, defeating the stated purpose of QF – near-optimal funding allocation.  

Startups are typically looking for initial funding to prove their concept, while established projects are focused on scaling. Since these two groups have such different goals, it doesn’t seem fair to review them using the same criteria.

Quadratic Funding (QF) is a big part of how Gitcoin distributes funds, aiming to make the process more democratic by boosting smaller contributions. But after seeing it in action thrice, I couldn’t shake the feeling that it actually ends up being more of a “self-congratulatory circle-jerk” (pardon my bluntness!). The focus seems to shift from making a real impact to a sort of inward praise among participants, which doesn’t always foster true innovation.

**A Friendly Suggestion**

QF should perhaps be limited to no more than a third of the weight in the final allocation, with the rest being decided by multiple groups:
1.	Peer Review Group: This group would consist of project leaders who are asked to distribute points (say, 100 points) across other projects based on their perceived impact. They wouldn’t be allowed to vote for their own projects. To encourage thoughtful participation, there could be penalties for not distributing points fairly, such as reducing their grant by 20%. Conversely, those who take the time to distribute their points across multiple projects could be rewarded. This would promote a more honest and impactful assessment from peers.

2.	Specialized Expert Group: This group could include experts who focus on evaluating the potential impact of startups and the scalable impact of established projects. By applying criteria tailored to each project’s stage, this group could ensure that funding goes to those with the highest potential for real-world impact.

3.	Community Advisory Group: This could be a group of community members or stakeholders who have a vested interest in the outcomes of the projects but are not directly involved in them. Their role would be to offer perspectives on how projects align with broader community needs and values. Because this group would not require deep technical expertise, it could be a low-cost but high-impact way to incorporate diverse views into the decision-making process.

4.	Low-Cost Review Panels: Gitcoin could also introduce low-cost review panels, made up of volunteers or part-time reviewers from within the community. These panels would focus on specific aspects such as ethical considerations, environmental impact, or inclusivity. By decentralizing this aspect of the review, Gitcoin can tap into a wider pool of knowledge without significantly increasing costs.

5.	Pitch Panels: Another idea could be a panel where each project pitches their ideas, similar to how athletes are scored in the Olympics. Each project would present its case for why it deserves funding, and the panel would score them based on factors like innovation, potential impact, and scalability. This not only makes the review process more interactive but also ensures that projects are evaluated based on a comprehensive understanding of their value.

One additional benefit of giving QF a lower weight in the final allocation is that it would make the system less attractive for Sybil attacks and other types of gaming. When QF determines a smaller portion of the overall funding, it becomes less worthwhile for bad actors to try and manipulate the system. This would help make the grant rounds more equitable, as fewer resources would be needed for defending against these types of attacks, allowing more funds to be directed toward creating diverse and effective review groups that enhance the overall decision-making process.

**Making Everything Public and Transparent**

Since QF is public and you can see who votes for which project, it makes sense that the decisions of these other groups should also be made public. Transparency should be a core value across the board, ensuring that every aspect of the grant process is open for review.

1. Specialized Expert Groups: These groups could publish reports detailing the rationale behind their votes. By explaining why they supported certain projects, they could help the community understand the thought process behind the funding decisions, making the whole process more transparent.

2. Community Advisory Groups: Similarly, these groups could share their decision-making process with the public. They could explain how they assessed the alignment of projects with community values and broader societal needs, helping to build trust in the system.

3. Low-Cost Review Panels: Even though these panels might be composed of volunteers or part-time reviewers, they could still post their findings and decisions. By making their evaluations public, they would contribute to the overall transparency and fairness of the process.

4. Pitch Panels: For the pitch panels, the process could be even more interactive. Hosting these pitches on platforms like Twitter Spaces or other live-streaming services would allow the community to listen in and see how projects are being scored in real-time. A one-minute pitch format could be used, where the jury votes based on the pitch's clarity, innovation, and potential impact. This would make the process not only transparent but also engaging for the wider community.

**Learning from Public Tenders**

There’s a lot that Gitcoin could learn from how public tenders are conducted, especially when it comes to transparency and fairness:

1.	Open Submission and Review Processes: In public tenders, all submissions are reviewed publicly, and the criteria for selection are clearly defined beforehand. Gitcoin could adopt this model by ensuring that every project submission is visible to the community and that the criteria used by different review panels are shared upfront. This transparency would help avoid any perception of bias or favoritism.

2.	Detailed Evaluation Reports: Just as public tenders often require detailed evaluation reports that explain why certain bids were successful, Gitcoin could ensure that all review groups publish comprehensive reports that detail the reasoning behind their decisions. These reports would be invaluable for projects that were not selected, providing them with the feedback needed to improve and succeed in future rounds.

3.	Public Feedback Loops: Public tenders often include a feedback loop where participants can ask for clarifications or contest decisions. Gitcoin could implement a similar process, allowing project teams to receive constructive feedback and, if necessary, request further explanation of the decisions. This would enhance transparency and promote a more collaborative environment where projects can grow and evolve.

4.	Clear Conflict of Interest Policies: Public tenders typically have strict rules to prevent conflicts of interest. Gitcoin could further strengthen its processes by implementing and enforcing clear conflict-of-interest policies for all review groups. Ensuring that reviewers do not have a vested interest in the projects they evaluate would help maintain the integrity of the grant process.

Additionally, tools like the ReFi Scorecard could be useful in structuring this assessment, and it can serve as a point of reference. The tool illustrates how different criteria should be applied depending on a project's stage of development. Startups and established projects can't be reviewed under the same lens because they are at different stages and have different objectives. Startups should be evaluated based on their potential impact, aiming to prove their concept and gain initial traction, while established projects should be assessed based on their scalable impact, focusing on how they can grow and sustain their influence.

https://anuinitiative.org/refiscorecard/

-------------------------
