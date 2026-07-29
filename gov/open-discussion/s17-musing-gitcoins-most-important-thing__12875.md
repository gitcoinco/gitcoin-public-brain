---
id: 12875
title: "S17 Musing - Gitcoin's \"Most important Thing\""
slug: s17-musing-gitcoins-most-important-thing
category: open-discussion
url: https://gov.gitcoin.co/t/s17-musing-gitcoins-most-important-thing/12875
created_at: 2023-02-10T13:45:32.449Z
last_posted_at: 2023-03-07T21:05:53.319Z
posts_count: 7
views: 3977
like_count: 36
---

# S17 Musing - Gitcoin's "Most important Thing"

<https://gov.gitcoin.co/t/s17-musing-gitcoins-most-important-thing/12875>
kyle | 2023-02-10 13:45:32 UTC | #1

Years ago now, Gitcoin partnered with Paradigm to ensure continued operations and success. It was during that time that @owocki and I were often asked "what's the most important thing?" and then we would be probed on why we weren't doubling down on it, tripling down on it... cutting everything else to focus on it. 

That feedback worked. It helped us shape and determine that our "most important thing" was the Grants protocol and finding ways to fund public goods in perpetuity through that protocol.

Today, when I ask that question to each workstream leader (whats the most important thing), I get a different answer or perhaps just variations around the same thing. I want to share what I believe is the most important thing, and get feedback to make sure our community agrees.
![Screenshot 2023-02-10 at 8.13.55 AM|690x499](upload://ifejZf5qj0sfrCo0KmzwybAXsW7.png)

In this scenario - the most important thing for Gitcoin is building and launching Gitcoin Allo. The second most important thing is our Grants program (not us running rounds for other communities, but maintaining the *soul* of Gitcoin around funding what matters most to our community with our Matching Pool) and continuing to be a beacon for open source software. Finally the third most important thing is Gitcoin Passport - creating an identity and reputation aggregator that enables communities to connect in genuine and consensual ways while protecting us from Sybil attacks.

What this means is... all the other stuff we are doing should probably stop (heck, a case could be made for stopping Passport work, but I still believe that's the wrong outcome).

All the other stuff that matters likely needs to live somewhere with "the most important thing" or it should be evaluated for the value it brings.

What do you all think though? How would you describe the "most important thing" for Gitcoin right now?

-------------------------

CoachJonathan | 2023-02-10 17:18:38 UTC | #2

I just finished participating in a CSDO chat about exactly this topic. We landed on almost the same image that is presented here with some welcome nuances from our group.

That said, I'm pretty much 100% aligned to these 3 priorities and creates *way way way* more clarity for me and, ultimately, the MMM workstream on what we should be working on over the next several months.

I think there is still much to discuss, though I'm happy to see these ideas surface and would welcome exercises like this on a seasonal basis (maybe ahead of budget season so that we can align to it?).

-------------------------

DisruptionJoe | 2023-02-12 18:55:35 UTC | #3

[quote="kyle, post:1, topic:12875"]
Finally the third most important thing is Gitcoin Passport - creating an identity and reputation aggregator that enables communities to connect in genuine and consensual ways while protecting us from Sybil attacks.
[/quote]

I might agree on this if Passport broadened its scope to being a protocol or primitive applicable to projects & programs as well as donors/voters. See my comment here:

[quote="DisruptionJoe, post:18, topic:12727"]
Here are a few things that might surprise people. I think the passports system of reputation attestation, gating, and a shared ETL layer for transparent algorithmic policy decisions is needed for Projects and for Programs.
[/quote]

Passport is a protocol for using DIDs to:
* Scoring reputation for gating access in a transparent and auditable way
* Scoring behavioral interactions for retroactively discounting unwanted behavior in a transparent and auditable way. 

If it was a comprehensive solution needed for all of our components, I would agree it is the third most important. 

If not, then I think "***empowering the community to participate in building alongside us***" is #3. 

This would include:

* Improving documentation to empower developers to build on our protocols
* Improving open data access to empower data scientists to conduct research and guide a community driven R&D cycle
* Development of educational materials and runbooks for Program Managers - maybe even training classes
* Defining ENGAGEMENT LOOP metrics for each of these constituencies to not only acquire their interest, but to make their participation "sticky" (The old 10 friends on facebook thing)


How might we have more of the community weigh in to see if we don't change our minds before EthDenver in person sessions?

-------------------------

tigress | 2023-02-13 11:28:13 UTC | #4

[quote="kyle, post:1, topic:12875"]
How would you describe the “most important thing” for Gitcoin right now?
[/quote]

Studying **Token Engineering** I learned the following: There are (at least) two perspectives how one can look at blockchain projects and their way of trying to make a living and become thriving ecosystems (= secure the network, increase token value, generate network revenue, become self-sustaining)

**1) The Web3 Sustainability Loop**
![image|690x326](upload://l36tt6yh0GiqCUR6XicqEjOAaxT.jpeg)

The **Web3 Sustainability Loop** focuses on (a) token dynamics such that token value goes up as volume goes up (top right); and (b) using Network Revenue to do work to grow volume further. As a bonus, some tokens get burned as function of volume, which drives token value further yet (bottom left). This model directly links usage to value, and is amenable to valuation approaches like Net Present Value.

**2) The Network Flywheel**
![image|690x395](upload://lWKOEWBCi6QohXM0svSBZabylsP.jpeg)


In the **Network Flywheel**, “Token Value” has two inputs: (a) Investors who “provide financial capital” to founders to “build the protocol and bootstrap some initial token value”, and (b) Vision + Protocol: “the stronger the vision for the token value is, the more the value in the broader market” as the loop goes. **This model relies more on investor sentiment, without strong connection between usage and token value.**

Source and learn more here: https://blog.oceanprotocol.com/the-web3-sustainability-loop-b2a4097a36e or take the [Token Engineering Academy Module 1 Training](https://tokenengineering.net/course/tefundamentals-module1/) (it is academic, be warned, but I feel it was worth my time and effort).

*Here is my reflection:* 

I have not yet seen much in-depth thinking, designing, architecting and engineering a Web3 Sustainability Loop for Gitcoin. 

👉 As a protocol DAO with an impact arm, shouldn't we look more at how the relationships between the 3 most important things outlined above are intended to develop: Which incentives drive which behaviours and how the protocols interact in order to enable a thriving ecosystem?

And then... there is something else that shows up for me...  Aren't we stuck at the point in the Network Flywheel where Miners and Validators come in? Miners and validators are the ones who, in exchange for a reward from the protocol, contribute the production capital—i.e. computational resources—that give the network its functionality and security.

👉 There is no incentive yet (no reward from the protocol(s)) for the ones who give the Gitcoin network its security!

**To sum up: YES, and!  Yes to your most important things listed here and the relationships (the "whitespace") between them!**

-------------------------

epowell101 | 2023-02-20 00:11:32 UTC | #5

It’s a great discipline to ask - and to get engagement around the subject.  

Somehow I missed it - until the steward council prereading.

I guess my question would be how did we decide what the elements on the menu were?  

Coming out of essential intents and our capabilities and positioning - I would argue the most important thing is that we see a proliferation of successful users of the grants protocol.  That would then tend to lead to the development of the grants protocol being the top priority - as stated here.  

However starting at that higher level might lead us to also write down what we think it takes for our personas (I think grants operators of various types) to succeed.  Some of that we could also influence even if beyond the scope of code we write.

My bias of course is that I am somewhat of a Open Data Community and anti Sybil maxi.  I really believe that without passport & data science to protect the credibility of funding rounds - our users will not succeed and word of mouth will turn against us and especially against quadratic voting.  

Similarly if we define the most important thing as our personas succeeding in grants & public goods funding - then for a certain class of users like UNICEF we might find that our ability to prime the pump of a community / to provide some QV voting via MMM & community might be important as well.

Or not 😇😅.  Alternatively we might decide that “just devrel” (itself a major undertaking as we know) will be sufficient to allow for user success.  The rest - preventing and responding to Sybils, driving demand to help a grants protocol user get initial critical mass, might be secondary.  

What I don’t want us to do is fall into the trap of thinking that “just” the code will lead to success for our persona.  IMO it’s necessary but typically wd be insufficient.  

Product ideally might own mapping the needs of the personas - taking a total product perspective and thinking about current users and prospects (early adopters) vs those we hope to adopt in 12-24 months (more corporate perhaps?)

-------------------------

shawn16400 | 2023-02-22 13:36:42 UTC | #6

[quote="kyle, post:1, topic:12875"]
n this scenario - the most important thing for Gitcoin is building and launching Gitcoin Allo. The second most important thing is our Grants program (not us running rounds for other communities, but maintaining the *soul* of Gitcoin around funding what matters most to our community with our Matching Pool) and continuing to be a beacon for open source software. Finally the third most important thing is Gitcoin Passport - creating an identity and reputation aggregator that enables communities to connect in genuine and consensual ways while protecting us from Sybil attacks.
[/quote]

Kyle thanks for giving us a space to react. 
Here are my reactions:
1) The DAO needed focus, and this can help us - to a point.  I suspect that refocus might mean cutting scope within the remaining workstreams to make room for new work that is coming in.
2) This view is helpful, but we do need a longer view.  We need to think about life after stabilization so that any design choices made now can be informed by a reasonably worked out plan of where we are going. Failing to do this will likely result in suboptimal choices being made now/ rework in the future. 
3) I wonder if we are losing ground with community and we are taking them for granted.  I know that one tweet from Vitalik might be worth 5K raving fans, but if we have 5K pissed off fans, the probability for one a Vitalik tweet drops.   I think subjugating community to fourth place is not the right choice.
4) I think we need to think long and hard before "stopping" brand marketing, community, events, governance, operations, people support, hiring and tooling.  The reality is that some of that work is necessary and at a certain size, the work will not really stop, there will be an outage and someone will have to drop in to solve the issue and some kind of support structure will evolve.  
5) Finance seems to be missing from the picture. With our budget and with the flow through protocol, we really should have some kind of outside/inside professional help. 


My suggestions: 
1. Find a dedicated group to get input and refine 12-36 month roadmap 
2. Clarify a plan, or a "reengagement" plan for community
3. Lets be diligent on what stops, and what continues.

-------------------------

kyle | 2023-03-07 21:05:53 UTC | #7

[quote="epowell101, post:5, topic:12875"]
What I don’t want us to do is fall into the trap of thinking that “just” the code will lead to success for our persona. IMO it’s necessary but typically wd be insufficient.
[/quote]

I appreciate the thoughts and generally agreed with much of your sentiment. As a CSDO team, we aligned on the tech being the foundation for our success. And then ensure adoption, and the growth of Grants program as the "next most important" thing. 

as you also mentioned, Grants Stack needs a Sybil solution. Passport happens to be that solution for now, but it might be the only solution in the future. We don't want to put the cart before the horse in declaring protection for a thing that isn't yet live and thriving is the most important thing.

[quote="shawn16400, post:6, topic:12875"]
but we do need a longer view.
[/quote]

We have our Purpose and Essential Intents now, and folks mentioned they were "too long term" or "too abstract given the time horizon" so we narrowed things down more. Do you think the Essential Intents can continue to serve that medium term time horizon north star?

[quote="shawn16400, post:6, topic:12875"]
My suggestions:

1. Find a dedicated group to get input and refine 12-36 month roadmap
2. Clarify a plan, or a “reengagement” plan for community
3. Lets be diligent on what stops, and what continues.
[/quote]
I love these suggestions. I am inclined (just personally) to let the dust setttle on the new 6mo goals, the 6-24mo goals, and then expand the 24+ mo goals before diving too deeply back into the roadmap details, but open to feedback if others disagree with that approach.

Community engagement has a few things in the works via GCPs. I am excited for folks to share more as they develop their thinking.

Being diligent on what stops is important. I think we are still sense making on that front given teh way the budgeting process has evolved this season.

-------------------------
