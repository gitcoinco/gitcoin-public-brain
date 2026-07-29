---
id: 17292
title: "Introducing: Checker"
slug: introducing-checker
category: open-discussion
url: https://gov.gitcoin.co/t/introducing-checker/17292
created_at: 2023-12-18T11:35:52.032Z
last_posted_at: 2024-03-29T14:53:25.931Z
posts_count: 5
views: 4175
like_count: 15
---

# Introducing: Checker

<https://gov.gitcoin.co/t/introducing-checker/17292>
Sov | 2023-12-18 11:35:52 UTC | #1

Initially envisioned in the [GG19 - Outline and Strategy](https://gov.gitcoin.co/t/gg19-outline-and-strategy/16682/1#open-source-software-oss-22) and in development since Checker is a tool developed by the GPT Team to improve the process of grantee evaluation and application reviews. Checker is poised to revolutionize our grant review process in several ways:

* **Automated Review**: Checker automates the evaluation of grant applications at scale, ensuring a more efficient and consistent review.
* **Enhanced Transparency**: Utilizing AI/LLM technology, Checker allows for a transparent review process where community members and applicants can better understand how evaluations are conducted.
* **Dynamic Application System**: With Checker, we're moving towards a system where grantees can self-service their reviews, breaking free from the constraints of predefined application windows.

@giliomeejg has been leading the development, with feedback from the rest of the GPT Workstream, including @sejalrekhan , @M0nkeyFl0wer , @jon-spark-eco , @umarkhaneth , and myself. The goal is to use Checker and actively contribute to its evolution and growth.

@giliomeejg created a video to show a sneak preview of the tool. You can check that out [here](https://www.youtube.com/watch?v=Mf-wj1FKSY8).

# Futures

In addition to the current work on Checker, we have a larger vision that includes the following:

* **Integrations**: Checker could integrate with platforms like GitHub to analyze project metrics, offering a deeper insight into each project's development activity and community engagement.
* **Enhanced Customization**: Checker will allow round organizers to customize evaluation criteria to suit the specific goals of different funding rounds.
* **Integration with Other Gitcoin Tools**: Checker is being designed to integrate with other Gitcoin tools like Grants Stack, enhancing its functionality and user experience.

# Conclusion

Checker is not just a tool; it's a vision for a more efficient, objective, and transparent future in grant application reviews. As we test and refine Checker internally, we are excited about its possibilities for our community and the broader ecosystem of grantees we support.

We invite your feedback, suggestions, and collaborations to ensure Checker evolves in a direction that aligns with our collective needs and aspirations.

-------------------------

CoachJonathan | 2023-12-18 12:08:43 UTC | #2

[quote="Sov, post:1, topic:17292"]
Checker is poised to revolutionize our grant review process in several ways:
[/quote]

I'm very excited about this tool and to test out its potential for the Gitcoin ecosystem and eventually the web3 ecosystem as a whole. Kudos to everyone who helped create this (esp. @giliomeejg for all the time and effort!).

I think the one thing that I heard flagged (and was probably already discussed but maybe I missed it) was the idea of malicious actors getting access to the tool and using it in order to game the review process. Any ideas on how to mitigate this behaviour? Or maybe that is a v2 issue we'll address in the future?

-------------------------

Sov | 2023-12-18 12:40:52 UTC | #3

Thanks for the comment and show of support.  

Maybe I should have been more clear that Checker is just a tool that helps humans make decisions and is not intended to replace human actors in decision making.  Ultimately it will still be members of the GPT Team for our program rounds (or anyone using Grants Stack once enabled) that will allow grantees to enter rounds.

-------------------------

giliomeejg | 2024-01-03 06:38:57 UTC | #4

Currently only the internal Gitcoin team has access to use the tool to assist with evaluating round applications, however if we do roll this out to give near real-time feedback for users that create projects, e.g. via builder.gitcoin.co, we might open up possibilities for malicious actors, e.g. I create a malicious project which is initially rejected, but I get told which parts of my project need attention, so fixing these would lead to a greater probability of my project being included.

One potential way around this when we cross that bridge, is to have distinctly different GPT responses for round operators vs. the general public, so if I'm a round operator, I get a high level of detail on how a project scores against all the eligibility criteria, but if I'm a member of the public, I get a toned down version of this.  An example might be instead of "no active Github commits in the past 3 months" for the round operator, the public response might be "no recent meaningful Github activity".

-------------------------

machuche1 | 2024-03-29 14:53:25 UTC | #5

Excited for this! Especially for the GitHub analyzing of project metrics. Would it be open tp customization of different languages?

-------------------------
