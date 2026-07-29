---
id: 16192
title: "GG18 Grantee Discovery Using LLM-Enabled Conversations"
slug: gg18-grantee-discovery-using-llm-enabled-conversations
category: open-discussion
url: https://gov.gitcoin.co/t/gg18-grantee-discovery-using-llm-enabled-conversations/16192
created_at: 2023-08-08T08:14:06.640Z
last_posted_at: 2023-08-23T18:40:45.759Z
posts_count: 10
views: 2081
like_count: 21
---

# GG18 Grantee Discovery Using LLM-Enabled Conversations

<https://gov.gitcoin.co/t/gg18-grantee-discovery-using-llm-enabled-conversations/16192>
rohit | 2023-08-23 18:03:09 UTC | #1

**UPDATE 23-AUG-2023**: The application is live [here](https://gg18-llm.streamlit.app/). For now, it includes grantees in the Climate Round only and will be updated for other core rounds shortly. If you take it for a spin, please share inline feedback in the app (using :+1: or :-1:). As we understand the patterns of queries where there is room for improvement, we can get it to respond better over time.

**tl;dr** This is a brainstorming post to help iterate on an existing [LLM-based prototype](https://gitcoin-citizens-round.streamlit.app/) for GG18. It was originially built as a (personal) side-project and deployed for donors as [Citizens GPT](https://twitter.com/GitcoinCitizens/status/1671617848551112706?s=20) for grantee discovery during the Gitcoin Citizens Round. *This project is undertaken in a personal capacity and does not involve any asks for resources or funding from Gitcoin.*

### What?
A conversational experience for GG18 donors to discover value and impact-aligned grantees.

### Why? 
An experience that matches the user's style and pace to discover content is more effective than relying solely on pre-defined information hierarchies. 

### How?
Prospective GG18 donors can ask more information about grantees they are aware of using this utility. Alternatively, users can share the description of work they are interested in funding to discover additional grantees. Additionally, users can ask questions about the round itself in case they need help with any aspect of participating in GG18.

### What already exists?
A [proof-of-concept](https://gitcoin-citizens-round.streamlit.app/) deployed during the Gitcoin Citizens Round for donors to ask questions about the grantees and the round. For example:

![FzK8cVTWcAA5iT_|690x297, 100%](upload://kPZaDhtg8y7tZLeTZC2CURYf9FB.jpeg)


### Features currently in development:
- Add memory to facilitate conversations like ChatGPT
- Re-direct user to single sources of truth (Gitcoin Explorer, Gitcoin Documentation, etc.) as appropriate for more information
- Capture user feedback on relevancy of responses
- Analytics and logging to inform content planning for future rounds
- Code refactoring for granular control on the underlying abstractions to improve quality of responses (porting from GPT Index to Langchain)

### What the product should NOT be able to do:
- Pass algorithmic biases to influence donor for one grantee over another
- Respond to any line of questioning that requires it to filter, sort or rank grantees
- Utilize any information outside of what grantee has submitted in its responses
![Screenshot 2023-08-08 at 1.30.48 PM|690x142](upload://68WlXpbbe8Yfr9iDDxhdAHuHcd8.jpeg)

### Timeline:
The chatbot will be available 24 hours after the start of GG18 i.e. August 16th and will be online through the end of the round

### ASK: As a potential donor for GG18, what additional features would you find desirable in a "Gitcoin Grants GPT"?

-------------------------

jengajojo | 2023-08-08 09:34:40 UTC | #2

Thanks @rohit This is definitely a helpful upgrade to the donor experience. 
- It would be great to have a few FAQs I can click on when the chat box opens
- Is it too much to ask the bot to go online and cross reference the facts stated in the application with links/resources avaliable online?
- can the bot be multi-lingual?

-------------------------

essemharris | 2023-08-08 16:09:10 UTC | #3

This is a really interesting idea, and thanks for putting it together. How will we audit the questions and responses to know whether the product is doing / is not doing what it should?

-------------------------

koday | 2023-08-08 22:36:03 UTC | #4

Thanks for sharing @rohit, this is awesome!

I'll play around with this tool once the round goes live and try to give more feedback/ideas at that point. 

For now, the first thing that came to mind is using this for grouping grants in a given round by the technology they're using/building. I.e. I would ask "Provide a list of all grants in the Web3 OSS round who are building on Optimism" or "Provide a list of all grants in the Climate Solutions round who are working with solar technology", or something along those lines. I think this type of feature could be incredibly useful, especially for the larger rounds with 100+ grantees.

-------------------------

rohit | 2023-08-09 11:16:02 UTC | #5

[quote="jengajojo, post:2, topic:16192"]
It would be great to have a few FAQs I can click on when the chat box opens
[/quote]
This is a great suggestion. I might need to pick up some more frontend skills :sweat_smile: but I will give this a shot.

[quote="jengajojo, post:2, topic:16192"]
Is it too much to ask the bot to go online and cross reference the facts stated in the application with links/resources avaliable online?
[/quote]
The short answer is yes. The current architecture is set up such that the responses are based on curated and gated content only i.e. project details as part of the grant application and not from anything else Open AI might have already scraped or other online information. However, if the project details submitted by the grantee include links and external references, the relevant responses will offer the same links inline in the response to the user to explore further.

[quote="jengajojo, post:2, topic:16192"]
can the bot be multi-lingual?
[/quote]
Mostly, yes. Behind the scenes, the product uses Open AI APIs for a semantic search for the user inquiries. The underlying models likely generate [good results](https://help.openai.com/en/articles/6742369-how-do-i-use-the-openai-api-in-different-languages) out of the box for a variety of languages. Will test this out more. Here's an example in Spanish on the data set for Citizens Round. 

![Screenshot 2023-08-09 at 4.43.06 PM|690x259](upload://omu791rlPxNGik3mH23BQtN6nwx.png)

Thanks for all your suggestions!

-------------------------

rohit | 2023-08-09 11:42:02 UTC | #6

That's a great question and the #1 risk from my standpoint from the time this was deployed for the Citizens Round. I classify this risk into two categories: (a) the need for accuracy and (b) avoiding response bias. Here are some proactive and reactive measures. This doesn't guarantee 100% success but will help narrow down undesirable experiences. 

Proactive steps:
- The underlying architecture to respond to user queries is essentially a search (versus fine-tuning an AI  model) over curated and gated content (single sources of truth about Gitcoin products, round information, project details, etc.) The restricted content prevents the responses from being affected by information broadly available on the Internet.
- Predefined prompt templates that safeguard the neutrality of responses are embedded in the code before calls to the Open AI APIs. This will restrict the product from answering questions like, "Sort the grantees in climate round based on impact" or "Which project has the highest chances of succeeding in the long term?"


Reactive steps:
- All responses will be logged to understand patterns in user questions and utilize it in informing changes, if any, needed in communications for future rounds by MMM team. This logging mechanism will also allow catching scenarios that haven't been handled.
- There will be an opportunity for the user to provide feedback on every response to escalate any inappropriate responses.

LLMs are an evolving technology and I anticipate this will be an iterative process over a few rounds to determine if this will be a useful utility for donors. If you anticipate any additional risks or concerns, please do share.

-------------------------

rohit | 2023-08-09 11:54:15 UTC | #7

Thanks @koday ! Looking forward to your feedback!

If the project detail submitted by the grantee has information about the attribute of interest (e.g. technology, domain, geography, partnerships, etc.), then the existing code should be able to respond to the type of questions you have shared. I will test this out before the code gets deployed once the grantee information is public. Here's a preview based on the data from Citizens Round (it ain't perfect, but close enough to the line of inquiry). 

![Screenshot 2023-08-09 at 5.19.03 PM|690x213](upload://zMSiKZpZei9nF76O1JM5gQeQiI9.png)

-------------------------

garm | 2023-08-15 12:21:51 UTC | #8

This is awesome! 

I look forward to crafting prompts to achieve a jailbreak of what the product should NOT be able to do. 

On that note, I do have some questions: 
1. are you going to go through great lengths to try to prevent jailbreaks, or do you accept that if people _really want_ to get an LLM ranked list, that's fine? 
2. arguably being able to ask the LLM to filter, sort and rank specific grantees based on things I care about might actually be the painpoint I'm trying to solve? A prompt like "Give me all climate related initiatives with a focus on animal welfare, ranked by the amount of positive impact they expect to generate per $ donated" may actually save me a _lot_ of time!

-------------------------

rohit | 2023-08-23 18:22:46 UTC | #9

The application is live [here](https://gg18-llm.streamlit.app/). For now, it includes grantees in the Climate Round only and will be updated for other core rounds shortly. 

[quote="jengajojo, post:2, topic:16192"]
It would be great to have a few FAQs I can click on when the chat box opens
[/quote]

@jengajojo It isn't as seamless as a click, but I have added a few queries that can be copied as a prompt.

![Screenshot 2023-08-23 at 11.35.12 PM|690x381, 75%](upload://ubNzvlrQN6L4w4r4V9KrpHuJQnc.png)

[quote="jengajojo, post:2, topic:16192"]
can the bot be multi-lingual?
[/quote]

It seems to be doing okay out-of-the-box, but I would love it if you could try a language you could offer feedback on (the question in Spanish was, "What projects are working to improve the health of the oceans?", subject to Google Translare's accuracy ... haha!)

![Screenshot 2023-08-23 at 11.40.25 PM|449x500](upload://92s7ZvtL1fBWlBfZH14C9g4G190.png)

[quote="koday, post:4, topic:16192"]
For now, the first thing that came to mind is using this for grouping grants in a given round by the technology they’re using/building.
[/quote]

@koday This is a work in progress, and I am not content with the quality of responses yet (missing breadth). It requires the ability to accurately pick the right chunks of information across all the grantee data sets and still be able to fit in the limited context window for an LLM. Possibly, will have a better design for GG19. But with what I could do so far, here's a response to the question you had:

![Screenshot 2023-08-23 at 11.47.37 PM|648x499](upload://r4ildxsD3RlRDAp7z2HjmTTMPP3.png)

-------------------------

rohit | 2023-08-23 18:40:45 UTC | #10

[quote="garm, post:8, topic:16192"]
I look forward to crafting prompts to achieve a jailbreak of what the product should NOT be able to do.
[/quote]

Awesome, do let me know what you find. I look forward to learning.

[quote="garm, post:8, topic:16192"]
are you going to go through great lengths to try to prevent jailbreaks, or do you accept that if people *really want* to get an LLM ranked list, that’s fine?
[/quote]

I see the problem space has two different challenges - information discovery and recommendation engine. Right now, I am actively trying to constrain the scope to information discovery alone. Here are a few reasons I am wary of jumping to solve for the recommendations feature for now:
- I am using the out-of-the-box Open AI models for performing a semantic search on curated content (i.e. grantee project details page). Any inherent biases in the base model will likely port over in responding to questions like ranking. Probably, fine-tuning a model might be able to address this.
- There is information asymmetry in the data ingested that will likely add noise to the AI recommendation. Grantee project details page with multimedia (images) and external references to richer data are ignored by LLM. A human interpreting this information manually will likely have more data points than LLM to derive inferences.

[quote="garm, post:8, topic:16192"]
A prompt like “Give me all climate related initiatives with a focus on animal welfare, ranked by the amount of positive impact they expect to generate per $ donated” may actually save me a *lot* of time!
[/quote]
I agree! I am out of depth on the precision in data modeling required to ingest this information for high-quality inferences. "all climate related initiatives with a focus on animal welfare" is essentially a semantic search, and the app does that (it could be better). "positive impact they expect to generate" is an inference that will likely require domain-specific fine-tuning for accurate results. I will keep this in mind as I continue my explorations beyond what I have been able to code so far!

-------------------------
