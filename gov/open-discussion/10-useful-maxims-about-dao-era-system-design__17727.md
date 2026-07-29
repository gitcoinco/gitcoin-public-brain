---
id: 17727
title: "10 Useful Maxims about DAO-Era System Design 📜"
slug: 10-useful-maxims-about-dao-era-system-design
category: open-discussion
url: https://gov.gitcoin.co/t/10-useful-maxims-about-dao-era-system-design/17727
created_at: 2024-02-12T00:39:18.999Z
last_posted_at: 2024-07-26T03:45:07.322Z
posts_count: 10
views: 4388
like_count: 29
---

# 10 Useful Maxims about DAO-Era System Design 📜

<https://gov.gitcoin.co/t/10-useful-maxims-about-dao-era-system-design/17727>
owocki | 2024-02-19 18:59:34 UTC | #1

# TLDR

1. **Gall’s Law** states that a complex system that works is invariably found to have evolved from a simple system that worked.
1. **The Pareto Principle**, or the 80/20 Rule, posits that for many outcomes, roughly 80% of consequences come from 20% of the causes.
1. **Parkinson’s Law** states that “work expands so as to fill the time or budget available for its completion.”.
1. **Goodhart’s Law** states that when a measure becomes a target, it ceases to be a good measure. 
1. **Brooks’ Law:** From Fred Brooks’ book “The Mythical Man-Month,” it states that “adding manpower to a late software project makes it later.” .
1. **Moore’s Law** is the observation made in 1965 by Gordon Moore, co-founder of Intel, that the number of transistors on a microchip doubles approximately every two years, though the cost of computers is halved.
1. **Metcalfe’s Law** posits that the value of a telecommunications network is proportional to the square of the number of connected users of the system (n^2).
1. **Dunbar’s Number** suggests that there is a cognitive limit to the number of people with whom one can maintain stable social relationships.
1. **The Unix Philosophy** is (1) Make each program do one thing well, (2) Expect the output of every program to become the input to another, as yet unknown, program, (3) Write programs to work together.
1. **Conway’s Law** posits that organizations design systems that mirror their own communication structure.

# 10 Useful Maxims about DAO-Era System Design

I've had two conversations with Gitcoin'ers in which I was  espousing a few different maxims I live by (Metcalfe's Law, Galls Law, Parkinsons Law, Unix Philosophy, etc).  

In these convos, the Gitcoiner's asked me what each of these maxims were and why the were important to me. In order to scale up the answering of that question, I'm writing up this gov post.

First, a couple caveats:
1. **The map is not the territory** = these maxims are representations of reality.  
   - They are not are not the reality itself but simplified abstractions that cannot capture all the complexities and nuances of the actual world. 
2. You can think of these maxims as the compression of hundreds of years of learnings about the evolution of human social systems (or sometimes, other complex systems) into simplified maxims (sometimes oversimplified).   These maxims are a combination of both:
    - **Empirical knowledge** - derived from sensory experience and observation, relying on evidence and experimentation. 
    - **A priori knowledge** - obtained independently of sensory experience, through reasoning or logical deduction.   

**Why is this useful?**  As the DAO goes through its evolution and re-organization towards its essential intents, these maxims can help us reason about the dynamics at play.  They can also help us to fall through predictable traps in organizational design.

Also, I just find them to be fun mental floss and hope that anyone else in web3 who pursues the practice of Intellectual Curiosity will agree!

![Screenshot 2024-02-11 at 5.28.59 PM|554x398, 50%](upload://9Ag0tccHriwO4wAiOWP2vu9BDRO.png)


# 1. Galls Law

**Gall's Law** states that a complex system that works is invariably found to have evolved from a simple system that worked. The law further asserts that a complex system designed from scratch never works and cannot be patched up to make it work. You have to start over with a working simple system. 

This principle is particularly relevant in the context of systems design and development, emphasizing the importance of starting with simple, manageable projects that can grow in complexity over time through incremental improvements.

**Owocki comment**:  This is one of the principles that I think is really important to practice in pre-product market fit products.  And I hope to put this principle to work as we build [Lean Startups](https://gov.gitcoin.co/t/lessons-about-the-book-lean-startup/17691) and [Rapidly Prototyping](https://gov.gitcoin.co/t/temp-check-rapid-prototyping-gitcoin/17419). 

Galls law reminds me of this image about how to do agile software development :slight_smile::
 
![download|273x184](upload://8vxDRGolaysiKk9Q4jyHmkKBuII.png)


# 2. The Pareto Principle

**The Pareto Principle**, or the 80/20 Rule, posits that for many outcomes, roughly 80% of consequences come from 20% of the causes. Organizations often apply this principle in productivity and performance analysis, resource allocation, and strategic planning to identify and focus on the most significant factors driving results.

![1_z8AsP_J0_JSZNCiwbaYZhA|627x500, 50%](upload://2XbNbj4De3zlwl0Q8tSWSMOGw5H.jpeg)


**Owocki comment**:   This is another really important one for a startup that is pre-product market fit or pre-revenue.  Getting 80% of outcomes for 20% of the cost is huge in [Lean Startups](https://gov.gitcoin.co/t/lessons-about-the-book-lean-startup/17691) and [Rapidly Prototyping](https://gov.gitcoin.co/t/temp-check-rapid-prototyping-gitcoin/17419).  

# 3. Parkinson's Law

**Parkinson's Law**: Articulated by Cyril Northcote Parkinson, it states that "work expands so as to fill the time or budget available for its completion." It highlights the inefficiency and time management issues within organizations that make budgets or timeframes expand far beyond market standards.

**Owocki comment**:  I wish we had paid more attention to this law during the launch of GitcoinDAO in May 2021.  Perhaps if we had, had smaller budgets that increased over time as workstreams proved success (galls law), and we wouldnt had so many governance challenges that led to us spending $1m/mo (parkinsons law) as we mostly failed to ship Grants 2.0 and lost our market leadership position (2021-2023).

# 4. Goodhart's Law

**Goodhart's Law** states that when a measure becomes a target, it ceases to be a good measure. In organizational contexts, this can refer to the phenomenon where employees and systems optimize for the metrics they are evaluated on, often at the expense of broader organizational goals or unintended negative consequences.

A correlary law to Goodhart's law is Campbell's Law.  Campbell's law suggests when a measure becomes a target for social or economic policy, it is likely to become corrupted or produce misleading results. It highlights the unintended consequences of overemphasizing and misusing metrics for decision-making.

![calltime|600x214](upload://1hCHA44ezY6gTH4cSjkCb6bCUrB.png)


**Owocki comment**:  I think this is of particular relevance in 
1. **Sybil Resistance** - We can characterize the Sybil Resistance Problem as an Infinite Evolutionary Game ([watch my talk on this here](https://archive.devcon.org/archive/watch/6/1-human-1-vote-money-legos-more-democratic-daos/?tab=YouTube)).  Because of Goodhart's law, the definition of cost of forgery must continually evolve because as cost of forgery for time t becomes a measure, it ceases to be a good measure, and so much evolve to Cost of Forgery for time t + 1.
2. **Public Goods Funding** - As soon as any public goods funding mechanism starts to proliferate and drop a lot of $$$, people will begin to game it.  We've already seen this in QF and RetroPGF (collusion attacks or bribery attacks).  So we will witness a similar infinite evolutionary game around Public Goods Funding in order for it to provide public goods but without being gamed.  (One way I think we can solve for this is by having a diversity of plural PGF mechanisms.. If each mechanism does 1 thing and does it well and only drives 20% of incentives, then it becomes harder to game all of them at once!)
3. **OKR planning** - We should be mindful of the limits imposed by Campbells/Goodharts law when measuring workstreams by the KPIs the define.

# 5. Brook's Law

**Brooks' Law**: From Fred Brooks' book "The Mythical Man-Month," it states that "adding manpower to a late software project makes it later." This law addresses the complexities and diminishing returns of scaling teams on software projects.

![mmm-communication|600x468, 75%](upload://yrrcOkJJMkU7a2dO2Wm3o2CX0fv.png)
![realistic|500x500, 75%](upload://3zKZThUAIKROtQW1Qb3NxnuUJrB.png)


**Owocki comment**:  This is another good one to remember as we evolve our ability to develop world class Software at Gitcoin :) 


# 6. Moore's Law

**Moore's Law** is the observation made in 1965 by Gordon Moore, co-founder of Intel, that the number of transistors on a microchip doubles approximately every two years, though the cost of computers is halved. 

This prediction has guided the semiconductor industry, leading to the exponential increase in computing power and efficiency over time. Although originally about transistor density and cost, Moore's Law has broadly come to represent the rapid and continual pace of technological and computational advancement.

![oin_tutorial.f3|548x500, 75%](upload://iZx6NT09H8XeCh3vOvqj2kfUk55.jpeg)


**Owocki comment**:  The entire technology industry, for the last 30 years, is built upon this law.  We are standing on the shoulders of giants!

# 7. Metcalfe's Law

**Metcalfe's Law** posits that the value of a telecommunications network is proportional to the square of the number of connected users of the system (n^2). 

Originally formulated by Robert Metcalfe in the context of ethernet and telecommunications networks, this principle has been widely applied to understand the increasing value of social networks, the internet, and other networked systems as they grow. 

Essentially, Metcalfe's Law suggests that the more people or devices that can interact within a network, the more valuable that network becomes, because the number of potential connections and interactions increases exponentially with each additional user.

![Screenshot 2024-02-11 at 6.07.45 PM|690x281](upload://usKcwEKPspm84Cgn4uFZFbUhD26.png)


**Owocki comment**:  Our entire "Network Effects" essential intent for 2024 is built upon Metcalfe's law, so we'd best internalize it :)

# 8. Dunbar's Law

**Dunbar's Number** suggests that there is a cognitive limit to the number of people with whom one can maintain stable social relationships. 

This concept has implications for organizational structure, suggesting that beyond this number, it becomes increasingly difficult to maintain direct social connections and cohesion within a group.

![Dunbars-number-300x300|300x300](upload://ikjNxjXK1bUGO0YX4RORmqFWxdj.png)


**Owocki comment**:  IMO this is an important thing to understand as the DAO evolves.  

One thing I would have done differently at the start of the DAO if I could would have been to keep teams below the size of 5-7 0 no more than two pizza team size (eg no more people than could eat two pizzas).,    **Why?**
1. Having smaller working groups is better because groups can contain context and relationships within themselves.  
2. It prevents fiefdom building behaviour.
3. It also prevents falling into [the meta trap](https://gov.gitcoin.co/t/the-meta-trap/10666).  
4. Working groups should look more like [Orca style pods](https://metropolis.mirror.xyz/_MT98bEtBoEULyOy8LHC3pbAguEZz3GOcB7y1yndox4) than 2021-2023 era Gitcoin maximum bloat workstreams. 
5. Then every pod should have a defined service layer that other DAOs can use (eg Innovation Collective has a project intake process. As does marketing. As does Citizens RFPs. As does X where X = every pod. KPIs can be built upon this service layer to measure quantity/quality of output).
6. [It's worked well elsewhere.](https://blog.crisp.se/wp-content/uploads/2012/11/SpotifyScaling.pdf)

# 9. Unix Philosophy

The top three principles of the Unix philosophy, distilled from the broader set of guidelines, focus on simplicity, modularity, and reusability. They are:

1. **Make each program do one thing well:** This principle encourages developers to focus on designing programs that perform a single task effectively. The idea is that doing one thing well leads to simpler and more reliable software. This approach facilitates easier debugging, testing, and maintenance, as each component has a clear, dedicated purpose.

2. **Expect the output of every program to become the input to another, as yet unknown, program:** This underscores the importance of designing programs to work together in a pipeline, where the output of one program can seamlessly become the input to another. This principle advocates for interoperability and flexibility, encouraging the use of standardized data formats (like text streams) that make it easy to chain programs together to perform complex tasks.

3. **Write programs to work together:** Related to the second principle, this guideline emphasizes building software components that can easily integrate with one another. By ensuring that programs can communicate and work together, developers can create more complex and versatile applications by combining simpler tools. This approach leverages the power of composition, where small, specialized programs are combined to solve larger problems, promoting code reuse and efficiency.

These three principles together form the core of the Unix philosophy, promoting a development culture that values simplicity, clarity, modularity, and the power of composition. They have profoundly influenced software design and development practices far beyond the Unix operating system itself.

### Unix architecture visualization:
![2222-5|657x500, 75%](upload://3LEet7Ic0UpAFjHRqPBds2b722K.png)


**Owocki comment**:  This philosophy is very similar to the design of modular blockchain systems.  Because Gitcoin's products are built on top of modular blockchains, we inherit a lot of these philosophies and we should extend them into our products.

Where as Gitcoin 1.0 was monolithic, Gitcoin 2.0 is modular.  Meaning it respects these 3 principles.  Take for example, these 3 tools that work together despite being differnet modules.
1. Gitcoin Grants Stack
2. reportcards.gitcoin.co
3. AlloScan

I also think that there is a possiblity to leverage the principlpes of the unix philosophy in organizational design.  These maxims, as applied to organizational design, would look like this:
1. Make each pod do one thing and do it well.
2. Make each pod have a process to intake work from other groups.
3. Pods can work together to form larger working groups as needed, and emergently.

# 10. Conway's Law

**Conway's Law** posits that organizations design systems that mirror their own communication structure. 

It was formulated by Melvin EConway in 1967 and implies that the technical architecture of a system will reflect the social boundaries of the organization that produces it, for example, the divisions between teams or departments. 

This law highlights the influence of organizational structure on the design and functionality of systems and suggests that to create desired systems, one might need to consider or even alter the organization's structure.

![Screenshot 2024-02-11 at 6.08.36 PM|582x500, 75%](upload://wzBZsbvDLRWRfq628aweUc3vSod.png)


**Owocki comment**:  
One thing I think is interesting about Gitcoin is that design products that we ourselves use to allocate capital to ourselves..

So that leads me to wonder if we could leverage conways law in new and interesting ways.

I wonder if we could design grants/allo strategies for funding working units at gitcoin and/or funding GCPs/the community at gitcoin.

This would prove allo market fit, dogfood allo internally, create grants expertise, and build confidence in it that will spill over into selling it to other daos. So much velocity can be built by dogfooding, using our own products would be huge for confidence and empathy.  And using our products to design our organization would be leet . 

It’s like inverse conways law- Gitcoin designs Allo, and then Allo designs GItcoin.  It would create an upward spiral of momentum and positive output.

![Screenshot 2024-02-11 at 5.23.54 PM|690x432, 75%](upload://tq8MqhvCXGyg2dGVPSFCRPopyWE.png)

 
# Conclusion.

I hope you found these maxims to be interesting mental floss.  As the DAO continues to evolve, I hope that these terms becoming common knowledge helps us to avoid landmines that we would have detected with these laws.

If there are other laws, principles, or maxims you think are useful to Gitcoin or the regen ecosystem, feel free to comment below.

-------------------------

rohit | 2024-02-12 17:13:31 UTC | #2

It will take a few reading cycles to internalize it all :sweat_smile: - thanks for compiling this!!!

Another one I see a lot of DAO-Era Systems lack was put forth by Ross Ashby.

**Ashby's Law:** A system must be able to have the same level of variety as its environment in order to survive.

"When the environment changes from one state to another, the system must be able to change in turn; the system must be able to match the variety in the environment. The way systems achieve this variety and adaptability is through their parts having a high level of autonomy to act as they see fit in their own particular part or niche of the environment. This is the core characteristic that Walter had identified as being common to both cybernetics and anarchism. If systems are too rigid and don’t have this capacity for change and variety, they become overwhelmed and break down."
(Reference - [Anarchist Cybernetics](https://theanarchistlibrary.org/library/thomas-swann-anarchist-cybernetics))

-------------------------

owocki | 2024-02-12 17:55:26 UTC | #3

Thanks rohit, thats a useful one.  Especially as the ecosystem evolves more mechanisms for public goods funding (direct grants in 2017, then QF in 2019-2021, now retropgf/protocol guild in 2023-2024).

-------------------------

owocki | 2024-02-16 00:33:40 UTC | #4

https://words.jonhillis.com/supper-place-village-city-state/

This piece from @jonhillis of Cabin does a nice job of interweaving the concepts of Matcalfe's law + Galls law into a DAO go to market strategy!

-------------------------

thedevanshmehta | 2024-02-16 13:10:41 UTC | #5

What a brilliant piece ! It'll also do really well as a twitter thread esp with all the images, you should do it if you haven't already or else I'll be happy to (with due credit to you ofc)

Another one I like on the context of DAOs is cunninghams law : best way to get an answer on the internet is not asking a question but posting the wrong answer

-------------------------

Kronosapiens | 2024-02-16 17:01:25 UTC | #6

Every time someone brings up the Unix philosphy, it's worth resurfacing [this gem](https://www.youtube.com/watch?v=tc4ROCJYbm0&t=9s).

-------------------------

owocki | 2024-02-19 19:08:00 UTC | #7

[quote="thedevanshmehta, post:5, topic:17727"]
What a brilliant piece ! It’ll also do really well as a twitter thread esp with all the images, you should do it if you haven’t already or else I’ll be happy to (with due credit to you ofc)
[/quote]

ask and yee shall receive! https://twitter.com/owocki/status/1759655703269069127

-------------------------

DarylEdwards | 2024-02-21 16:45:40 UTC | #8

I love this. If we all took a moment to think about how to integrate these ideas into day-to-day decision-making, Gitcoin would definitely accelerate forward!

I've found that actually applying mental models well is often a challenge for many people though, since they're often quite theoretical. Creating a meme-able tangible example really helps to drive the point home. 

For example on #2 The Pareto Principle, I like to talk about *hammers:*

**1.** **Maslow's Hammer:** "To a person with a hammer, everything looks like a nail." When you have a tool (say, Allo protocol, or Passport), you start looking for all the things you can do with it (Effort), and find out that only 20% of them matter. But how do you know which 20%?
![image|659x500, 75%](upload://iyviElk4pcCqfFKWvwluflMiW4k.jpeg)
**2.** "People don't buy *hammers*, they buy *ambiance*." Hammers and nails enable them to hang pictures, and improve the vibe in their space. If we get clear on what users/customers want (eg the vibe), then we can prioritize the 20% of the effort (things you can do with a hammer and nail) that get them their results.
![image|500x500, 75%](upload://w16sJeXuQSXx62k36Adn2RfjQVX.jpeg)


This is imho also an important contributor to Goodhart's law, since it's generally way easier to define targets on "hammers and nails" (internal stuff directly in your control) than on "beautified rooms" (external stuff that's often subjective). "Hammer and nail" targets then start to diverge from the actual desired results.

I'm curious about what everyone thinks:

What are some examples of applying these principles in the Gitcoin community?

What are some examples of where else we could apply these principles? 

What are some examples where the principles seem to apply, but what they tell us is really unexpected?

-------------------------

EventHorizonDAO | 2024-02-21 05:55:55 UTC | #9

Wonderful collection of principles a lot of us could benefit from keeping in mind going forward, thanks!

-------------------------

Decentralizedceo | 2024-07-26 03:45:07 UTC | #10

This is very useful! This collection can actually save a lot of time. Thanks again!

-------------------------
