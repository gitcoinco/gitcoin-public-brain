---
id: 12679
title: "Refactoring Gitcoin DAO: What's in a name?"
slug: refactoring-gitcoin-dao-whats-in-a-name
category: open-discussion
url: https://gov.gitcoin.co/t/refactoring-gitcoin-dao-whats-in-a-name/12679
created_at: 2023-01-26T12:41:39.105Z
last_posted_at: 2023-01-27T02:11:52.370Z
posts_count: 4
views: 2138
like_count: 7
---

# Refactoring Gitcoin DAO: What's in a name?

<https://gov.gitcoin.co/t/refactoring-gitcoin-dao-whats-in-a-name/12679>
kevin.olsen | 2023-01-26 12:41:39 UTC | #1

*In my attempts to bring the "DAO insider" work that I'm apart of into more public spaces, I felt it would help to step back and offer up a post on how I think about problems. I hope it's of value to someone.*

## Background 

So, a bit of context on my background and my approach to solving issues, what I mean by refactoring, and how I see **names** as the high-value place to start addressing change in our DAO.

In the arc of my career, I've spent a lot of time in and around code, but not just coding or programming specifically, but software design and software engineering. There are some concepts from these disciplines that I have internalized deeply enough that it's hard sometimes to tell where those beliefs come from. This pops up in funny non-coding places for me these days, namely: names. 

I hate things that are named wrong. I find acronyms or names that force you to translate their meaning every time you use them not just irritating but alarming. Like literally, when I hear a badly named thing, an alarm goes off in my head. *This is not a subtweet at the branding work. I think that process stands and brands are a bit of a different animal*. 

But this alarm has been useful, and I've tried to pay attention to it. It comes from the years I've spent trying to organize software and systems, and I want to try and explain the importance of names in the hope that my recommendations to rename things can be seen for what they are: an attempt at good systems design.

## Does all code crumble?

I'm going to walk this back to the beginning.

At first, every programmer starts out just learning to code. Just building stuff that works is the hard thing. 
 
But at some point, you encounter the next hard problem: codebases get big, they begin to get buggy, they're hard to work in, and eventually, they start to crumble. It feels like a fact of nature: code slowly rots. 

It's in encountering this "fact" that a fine distinction between just coding and something else emerges.

This next thing is software engineering. I think the Xooglers that wrote the book Software Engineering at Google own the best definition in the section Programming Over Time: 
>We propose that 'software engineering' encompasses not just the act of writing code, but all of the tools and processes an organization uses to build and maintain that code over time [...] Software engineering can be thought of as programming integrated over time.” https://abseil.io/resources/swe-book/html/pr01.html#programming_over_time
 
And now, as someone thinking about coding in terms of software engineering (including the processes and tooling), you see there are some projects where this "fact" you saw early in your career doesn't hold up - there are cleaner, healthier codebases that don't slowly crumble. 
 
You start wanting to build lasting things, things that scale, things that don't break down slowly over time. And in this part of your journey, you'll encounter a number of techniques: automated testing,  test driven design, clean code, CI/CD, domain driven design, etc. Each of these contributes tools to let you build maintainable systems, not just at a code level, **but at a human-to-human level, at a level where the organization of your work supports the maintainability of the systems you build**. 

 
Let's zoom in on two turning points where naming things emerged as clear benefits to building maintainable systems

## Cleaner Code

> “Any fool can write code that a computer can understand. Good programmers write code that humans can understand” — __Martin fowler__

Clean code was something I encountered fairly early on, and it's a bit too big to get into, but one of the core parts of this is to write your code in a way that lowers the cognitive load of those that have to read it, or extend it later.
 
Clean Code - Reveal your intent:
>`var d: Int // elapsed time in days`
>a name that requires a comment does not reveal it’s intent
>           
>`var elapsedTimeInDays: Int`
>the name of a variable should tell us the significance of what that variable contains
>https://bpoplauschi.github.io/2021/01/30/Clean-Code-Naming-by-Uncle-Bob-part-3.html

Kevin, hold it, why do I care. I don't code. 

You don't need to code, relax. What this example shows is that the code itself now captures the meaning that the programmer was trying to express with the comment. When that `var d` gets used later on, potentially dozens of lines of code later it won't have that comment next to it, and the semantic meaning is lost. The programmer will just be seeing that `d` in some new context and have to remember, 'oh yeah, that means elapsed time in days'. The clean code approach is to give that `d` a meaning, reveal the intent of that variable by naming it `elapsedTimeInDays` so when the programmer encounters it many lines later, away from any comment or explanation of what that variable is, they can reason about it in line, no mental lookup or translation necessary.

So really good names in your code is great and we should all do it. Glad we all agree. Moving ON!

## Building a Ubiquitous Language

Now that your code is clean and intention-revealing, you'll notice that you are still doing these mental lookups and translations in conversations with colleagues and in meetings with stakeholders. You'll realize you're constantly translating concepts from your non-engineering colleagues (business, design, product) into concepts in your codebase. If you inherit a legacy codebase or stick around a project long enough, these concepts can drift very far apart!

This higher-order problem is core to Eric Evan's [Domain Driven Design: Tackling Complexity in the Heart of Software](https://a.co/d/1JXcj1b )  (great title) in a concept he repeats (ad nauseam) called Ubiquitous Language.

Ubiquitous Language is the creation and maintenance of a shared vocabulary end to end - from the customer to the codebase. 

For those that were in the event storm as we kicked off the build-out of the Grants Stack / Allo protocol, this ubiquitous language was part of what @lthrift and I were trying to establish.

**But** this is also meant to be a living practice:
> _Domain experts should object to terms or structures that are awkward or inadequate to convey domain understanding; developers should watch for ambiguity or inconsistency that will trip up design.__
>  __-- Eric Evans__

Framed in the negative, Evans‘s ideas on what we should avoid:
> - The lack of a common language, generating “translations”, which is bad for the __Domain Model__, and causes the creation of wrong __Domain Models__.
> - Team members using terms differently without realizing it, for lack of a common language.
> - Communication without using __Ubiquitous Language__, even if it exists.
> - Creation of abstraction by the technical team for the construction of the __Domain Model__, which is not understood by domain experts.
> - Technical team disregarding the participation of domain experts in the __Domain Model__, considering it too abstract for domain experts. But it is necessary that domain experts participate, because who can validate the __Domain Model__ that was built?
> - https://thedomaindrivendesign.io/developing-the-ubiquitous-language/
 
Got it, so we all use the same vocabulary to describe our system and we're all good! 

Yes. **AND** we make this a continuous process to check that our vocabulary matches reality and that we update our vocabulary every time our model, our strategy, and our macro context change. Everytime our Domain changes. 
 
## Refactoring the DAO

> In computer programming and software design, code refactoring is the process of restructuring existing computer code—changing the factoring—without changing its external behavior. Refactoring is intended to improve the design, structure, and/or implementation of the software (its non-functional attributes), while preserving its functionality. **Potential advantages of refactoring may include improved [...] readability and reduced complexity; these can improve [..] maintainability and create a simpler, cleaner, or more expressive internal architecture or object model to improve extensibility**. - https://en.wikipedia.org/wiki/Code_refactoring

At the point I'm at in my software engineering journey, I see how software, codebases, teams, and organizations are all helped tremendously by good naming.
 
As I think about and suggest refactorings to the DAO, naming is the low-hanging fruit. Because naming our work badly manifests in the accumulating friction from many repeated low-level translations, mistranslations, and misuse we incur when mapping other team's concepts onto our work. It is a tax we all pay daily to get things done: as we onboard new contributors, as stewards and workstream leads struggle to understand each other's budgets, in the anxiety our DAO Community expresses on the forum.

**We need to reduce this mental burden.**
 
This is at the core of my recommendations: How can we reveal intent in a name that everyone can use as they navigate the complex and abstract structures of these human and software systems we are building? 

I see the solution in clean names mapping the work being done to the budgets we are funding.  **These are the slim workstreams as I see them**. It's my belief the fear of a sprawling and unmaintainable DAO would largely be solved with clear, intent revealing workstream names.
 
I've formed this belief about the importance of naming over the years from my experiences with software engineering (in the broadest possible definition), and I'm basing quite a lot of my recommendations on these beliefs. 

I hope this post helps elucidate at least some of my process and may even help to introduce a tool into the systems design work we do here in organizing and running our DAO.

-------------------------

owocki | 2023-01-26 15:26:33 UTC | #2

Thanks for the post and the background context/why behind it.

[quote="kevin.olsen, post:1, topic:12679"]
I see the solution in clean names mapping the work being done to the budgets we are funding. **These are the slim workstreams as I see them**. It’s my belief the fear of a sprawling and unmaintainable DAO would largely be solved with clear, intent revealing workstream names.
[/quote]

Is there any work scheduled to define the work at Gitcoin in this way?  Has anyone taken a stab at naming workstreams in this way?

-------------------------

kevin.olsen | 2023-01-26 15:30:47 UTC | #3

Thanks man.

This was definitely present in my support of the GPC's decision to split up into Passport and Allo Protocol.

That said, I don't think there's been a holistic effort yet to map all the work done in the DAO to the right names.

-------------------------

birdsoar | 2023-01-27 02:11:52 UTC | #4

Thank you for writing this, it's been awhile since I considered the principles of code. Good to be reacquainted.

[quote="kevin.olsen, post:1, topic:12679"]
*This is not a subtweet at the branding work. I think that process stands and brands are a bit of a different animal*.
[/quote]

Thank you for calling this out!! My first thought was, "Oh no, he hates the name Allo." :) 

In a general sense, I'm in agreement that naming things as they are is the best approach. One of my first suggestions when joining Gitcoin was to rename workstreams in a way that describes our respective intents more clearly. 

I could also seeing this being of benefit to people in the workstreams. Beyond the social energy that comes with (thoughtful) new names, updating our names could be an opportunity to inspire a renewed sense of purpose.

Looking forward to seeing this conversation develop.

-------------------------
