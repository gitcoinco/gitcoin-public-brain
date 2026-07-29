---
id: 16672
title: "Gitcoin.ai - An AI Chatbot that knows about Gitcoin (in alpha now)"
slug: gitcoin-ai-an-ai-chatbot-that-knows-about-gitcoin-in-alpha-now
category: open-discussion
url: https://gov.gitcoin.co/t/gitcoin-ai-an-ai-chatbot-that-knows-about-gitcoin-in-alpha-now/16672
created_at: 2023-10-04T17:38:52.183Z
last_posted_at: 2024-02-20T15:11:56.151Z
posts_count: 4
views: 3745
like_count: 12
---

# Gitcoin.ai - An AI Chatbot that knows about Gitcoin (in alpha now)

<https://gov.gitcoin.co/t/gitcoin-ai-an-ai-chatbot-that-knows-about-gitcoin-in-alpha-now/16672>
owocki | 2023-10-04 17:40:29 UTC | #1

DAOs require a lot of context to be governed well. 

Gitcoin has done an extraordinary job of making sure that any material information about the governance Gitcoin is public (whether on the gov forum, notions, youtube channel, or on-chain), but this has resulted in a flood of information that governors need to consume in order to be prepared for governing Gitcoin.

This can mean that DAOs begin to be governed by insiders (people who are employed by the DAO and can spend 40 hours/week gathering context from public information) as opposed to outside governors (who may have a better view on the org outside in, but only can spend a few hours a quarter consuming information about the DAO).

I am interested in closing the gap between insiders and outsiders, and that's why I've been experimenting with a new tool called http://gitcoin.ai

http://gitcoin.ai is a LLM chatbot powered by ChatGPT4 that is trained on gitcoin.co, gov.gitcoin.co, the gitcoin notion, endgame.gitcoin.co, impact.gitcoin.co, support.gitcoin.co, and information in the Gitcoin google drive.

In the future, 
1. I think it'd be cool to extend this chatbot with historical data/analytics about past GG rounds.  If this vision is successful of having to write a dune query for Gitcoin info, people could just ask the chatbot.
2. I'd love to add developer docs to this site, to make it easy to know how to do dev stuff on allo/gs/passport.
3.  Any data source that [Docsbot](https://docsbot.ai/documentation) supports can be added to the training material.  Please give me suggestions of what to train it on!
4. I'll have to iterate this chatbot forward (or kill it) based on community feedback.

Ideally this chatbot can be a tool that you can ask anything about Gitcoin to, and receive an answer, without having to comb through the mountain of context.  Feel free to give it a spin ( http://gitcoin.ai ) and let me know what you think.

Disclaimers:
1. THIS BOT IS IN ALPHA.  BE EXTRA CAREFUL ABOUT TRUSTING WHAT IT SAYS TO YOU.
2. This bot does not give financial or tax advice. This content is strictly educational and is not investment advice or a solicitation to buy or sell any assets or to make any financial decisions. This resource is not tax advice. Talk to your accountant. Do your own research.

-------------------------

rohit | 2023-10-05 18:17:11 UTC | #2

This is a great start (love the ability to see linked sources)! I have a strongly held belief that information silos create cultural silos, and LLMs can play a huge role in reducing that asymmetry. A few very very early findings are below across three categories of questions. 
- Works best when the potential number of sources that might have answers are few
- Questions where recency is critical have mixed results
- Even when the response might not be the most accurate, the links to sources offer enough direction for a deeper dive

#### 1 - Questions that need to provide the most recent answer from the data
Worked:
- What is the Passport Score requirement for Gitcoin Grants?
- Who can I reach out to for a question about my application?

Does not contain information:
- How much funds were raised in the Beta Round?
- How much funds were raised in GG18?

Not the most current answer:
- Who is part of the steward council at Gitcoin?
- How many workstreams does Gitcoin have?

#### 2 - High-level questions
Worked:
- How do I explain what is Gitcoin Passport to someone who is new to web3?
- ELI5 what is quadratic funding?
- How are Allo and Grants Stack different from each other?
- What is Gitcoin Citizens Round?
- Tell about collaboration between Gitcoin and UNICEF

Not the most current answer:
- What products does Gitcoin build? 
- ELI5 What is Gitcoin all about? 

#### 3 - Subjective questions
(Worth debatable if this should be in scope)

Does not contain information:
- What are the top 3 areas of improvement for Gitcoin?
- Is Gitcoin a DAO?
- What's the most complex case study involving Gitcoin Passport?

Not the most current answer:
- How easy is it to become a contributor for Gitcoin?

-------------------------

owocki | 2024-02-19 17:14:40 UTC | #3

I have decided to deprecate gitcoin.ai for now due to lack of use.

Learnings
1. This is a promising research area, and I think that LLMs will become the default way people interface with support/knowledge base info in the future.
2. But I found the software that powered gitcoin.ai to be too clunky to ingest info into, and that even w GPT4 it would miss stuff that was clearly in the source material.
3. I would consider other LLMs/LLM wrappers in the future.
4. I'd love if a community member took this forward. Id be happy to lend the gitcoin.ai domain to someone who does a credible job of indexing Gitcoin info.  And i would fund such a project in the citizens round.

-------------------------

krrisis | 2024-02-20 15:11:56 UTC | #4

All the work @rohit has done on https://grantsscope.xyz/ as a Gitcoin Citizen should definitely be continued, maybe it's ready to take on that url? 

You can play around with this applet for GG19: [https://all-about-gg19.streamlit.app](https://t.co/33BoZGdaP9)

All linked on that page, but here's also [a link to a thread with more examples](https://twitter.com/RohitMalekar/status/1727055572686782631).

-------------------------
