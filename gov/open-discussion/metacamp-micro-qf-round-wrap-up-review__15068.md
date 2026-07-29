---
id: 15068
title: "Metacamp Micro-QF Round Wrap-Up/Review 🌊"
slug: metacamp-micro-qf-round-wrap-up-review
category: open-discussion
url: https://gov.gitcoin.co/t/metacamp-micro-qf-round-wrap-up-review/15068
created_at: 2023-05-17T14:14:05.544Z
last_posted_at: 2023-12-10T06:38:31.963Z
posts_count: 13
views: 5591
like_count: 43
---

# Metacamp Micro-QF Round Wrap-Up/Review 🌊

<https://gov.gitcoin.co/t/metacamp-micro-qf-round-wrap-up-review/15068>
owocki | 2023-05-19 05:14:51 UTC | #1

![5qr7Drg|690x303](upload://qeEQctYUG1umn7fIiMvXKjpVadj.jpeg)

A couple weeks ago I attended [MetaCamp](https://mirror.xyz/yalor.eth/dDiyLhld5PDfhSHoI30mVRUvSE7QQMm8g6DH9UjJX6g) - MetaCamp is “an unconference event organized by members of MetaCartel key players of the DAO ecosystem, hosted in Costa Rica..”

The event was an opportunity to chill out in the beauty of natural Costa Rica and also to nerd out on mechanism design and DAOs while we were doing it. In typical unconference style, the ~40 members of the community self-organized around what it wanted to do. This meant hiking, surfing, yoga, a boat trip, trips to the beach, and unconference sessions - but also more mundane activities like running to the local town to pick up supplies, supporting the food/drink of the event, logistics, etc.

The event was a fantastic opportunity to reconnect with the beauty of nature and also an opportunity to connect with a lot of cerebral ideas. “Coordination” is a buzzword with this group; so I know I had found my people. :)

I decided to take the opportunity to test out Gitcoin’s new Grants [round manager](https://round-manager.gitcoin.co/). What would it look like to run a small [quadratic funding](http://wtfisqf.com) (QF) round for ppl to support the people who made the event great?  So far, Gitcoin Grants has been used to support projects that create public good, could it be deployed on a micro-scale to support *people* who created public good for a small unconference?

This felt like an opportunity to reward the people who contributed to the vibes( eerr.. the public goods) of the event.

Another result of the round would be a mapping of the web of trust of the metacamp community. By seeing who in the community had contributed the most to the public good of metacamp, we could reinforce that behavior.

![Screenshot 2023-05-17 at 8.04.22 AM|438x400](upload://1pOrGIW26VBs2jjCMKx0TL1JM4L.png)

Of course, QF is not a perfect mechanism - nor the only mechanism we could have used. QF can sometimes be a Keynesian beauty contest (a mechanism that selects for the most visible/popular ppl, instead of those who contributed to the public goods).. Running this experiment would be an opportunity to find out what types of behavior ppl would fund.

Maybe next year, if there are more voting strategy/payout strategies in Gitcoin stack, we can experiment with other mechanisms for supporting public goods - things like Quadratic Voting, gift circles, NFTs, or other mechanisms for measuring and funding what matters.

This round was also an opportunity to take Gitcoin’s tech stack for a spin on the L2. The most recent main Gitcoin round, the [Beta Round](https://www.gitcoin.co/blog/announcing-the-gitcoin-grants-beta-round) was run on a L1 and had very high gas fees. What would contributions look like on a L2?

I used https://round-manager.gitcoin.co/ to spin up a Metacamp Program and a Metacamp Round. A program has a one-to-many relationship with a round. E.g, I could reuse the Metacamp Program again in 2024 and create a Metacamp 2024 round if I chose to.

One hiccup we ran into is that the Gitcoin UI on round-manager forces two date ranges,

1. Application date - when Grants can apply to the round
2. Round (which maybe should be named ‘Crowdfund’) - when ppl can fund those grants.

The UI will only allow the crowdfund to begin after the applications end. This forced us to try and decide who could be in the round before the crowdfund started… when we would have preferred to have some overlap between the two periods.

![Screenshot 2023-05-17 at 8.04.55 AM|690x197](upload://hfp9yUerWtAc3nnVw2uZpcOVQeK.png)

Another wrinkle was that we did not feel like an “application period” was the right fit for an unconference style social community like Metacamp at all.

1. People were busy surfing and hiking, they were not checking telegram often. So they could not be relied upon to submit a grant.
2. While most people would feel fine receiving funding for contributing to the public goods of the event, people would likely not want to be seen seeking funding for it.

For this reason, we figured that if we accepted applications for the round, we would have had about ¼ of the participation as if we just loaded all of the attendees into the round (100% participation).

But what were the privacy implications of loading everyone into the round? The event itself was ticketed via NFTs, so everyone's information was on chain already. But we felt that we could not proceed without allowing attendees the opportunity to opt out.

After giving attendees the opportunity to opt out, we proceeded to ingest the attendee database into the granting system. But we hit another wrinkle, Gitcoin’s system expected everyone to submit their own grant application. And there is no bulk uploader for a round manager to simply create the grants on behalf of their attendees.

We worked around this by assembling a crack team of DAO nerds that was in charge of ingesting all of the grants into the system and then transferring the grants to the users themselves. This ride or ride crew took about 45 minutes to clean and ingest the 40 participants to the event (plus 4 locals who were helping out) into the Grants system.

In addition to the attendees, we also decided to include locals who helped out with the event into the QF round. The babysitters who watched the children, a woman who taught us a cooking class, and the staff from the hotel we stayed at, were all included. For those locals who were not crypto native, we decided that we would use addresses that one of us controlled for each of their grants, and that we’d settle up with the locals in cash after the round. This goal was to minimize the complexity of onboarding the locals to using crypto. In my opinion, more projects should be focused on providing value to people first and then onboarding them to crypto second - not the other way around. I’m sure they’ll be more interested in crypto if we [give first](https://www.techstars.com/the-line/podcasts/what-is-give-first). Lets not confuse the means (crypto) with the end (reward people who contribute to public goods).

At this point, the QF round had momentum within the social commons of the group. I put 3 ETH in myself, and was happy to see that I was matched with 3 ETH from [Metacartel’s Ethos project](https://www.metacartel.org/ethos), and .26 ETH from other participants, bringing the total pool of funding to 6.26 ETH.

Did I mention that this was on a L2? It cost about $4 to launch the round, $2 to apply to the round, and each contribution cost about $.50 in gas fees.

Over the next few days, contributions to the round began to roll in.

The contributor experience was similar to the typical Gitcoin Grants contribution experience.

1. Go to the round explorer.
2. Add grants to cart.
3. Checkout

I even printed out these fun little promotional fliers for the round using the hotels printer.
![IMAGE 2023-05-18 23:10:43|666x500](upload://gmF1c3iS5gTxnKbXGCE1sqPqAuV.jpeg)

After all was said and done, the round stats looked like this:

* 4 ETH in crowdfund contributions
* 6.28 ETH in matching funds
* Total funding: 10.28 ETH
* 41 grants
* Average earnings per grant: 0.25 ETH.
* 31 ppl contributed to the round
* 529 contributions were created
* An average of 17 contributions per person.

This is what the social structure of the round looked like. Each gray circle is a “grant”, and each blue/red contribution is a contribution to the grant.

![Screenshot 2023-05-17 at 8.05.51 AM|502x500](upload://hnEC95WeSjbYpipwvASvvNLU63R.jpeg)


All in all, I’m proud of the experiment that we ran. Especially the fact that the hotel staff, babysitters, and organizers are all going to get $300+ bonuses each from the round (some will receive over $1000).

Next time around, I’d be interested to explore a different funding mechanism (like Quadratic Voting, a giving circle, etc) for the round… And I’d like to be able to accept applications to the round during the round because theres a few organizers/locals we forgot to add the first time around.

I don’t think people realized that the new Gitcoin Grants tooling can be used in this way (or even that anyone can self-serve create a round at all). So I was happy to take the new tooling off the beaten path a little bit and experiment with a new form of social coordination.

Pura Vida 🌊🌈

—-----------------------------------—-----------------------------------—-----------------------------------—--------

Some assorted feedback I got during the round:

> Would be really nice to see who made the most donations or how many each person made but not on the receiving side.

> never seen a private qf round that turned out to be an observation for emerging connections and contributions from a group (or a past event), this was a really cool new use case for the mechanism, thank you for setting this up!

> I noticed the random sorting on refresh or page load as well. It would be great to either have a static loading or sorting options selected by the user. Alphabetical, most interest/signaling, etc. This randomness may have been their way of not giving priority to a single project, etc. however it is a bit distracting/interrupting to the end user experience.

> the page navigation is really weird on this site. Everytime I click into a grant and "Add to my cart" it should take me back to the section I was browsing before, but it appears that all the grants are shuffled at random instead ?

> I think it went really well for yolo test case of a new platform, education is key for this kind of thing to work and we can get ahead of it early for the next one ☝🏼

> i did it yesterday it's super easy, i like the shopping cart method

It was hard to explain how Quadratic Funding works to people in a concise way. We did lean on https://wtfisqf.com/ but it was still hard.

A handful of people were wondering how much match they were getttng for a contribution and tried to do the math. It would have been nice if the UI showed the answer so ppl dont have to do the match.

I turned off Gitcoin Passport in the round manager UI for the round, but during the contribution experience, the UI still prompted people to sign up for passport or their contributions wouldnt be matched. I think if Passport is off for the round, then the contributors should not get that prompt.

It’d be nice to have other sybil defense mechanisms available. I this case, I had the addresses of everyone who could participate. Rather than using Passport or nothing, the round manager could have allowed me to upload everyones address (into a merkle tree for gas efficiency of course) and just use that for anti-sybil.

A few folks had trouble finding their funds for the round and needed to be reminded to switch their wallets to optimism. (and this was a pretty crypto-native crew).

There is no way to see who you contributed to or who contributed to you without sleuthing on Etherscan, which is kind of clunky.

There were a few small UX issues during the round (eg you cant input .1 into the amount field on the checkout page, only 0.1…. On metamask mobile the ‘amount’ page doesnt accept decimals at all. The dates/times in the UI are all UTC instead of localized to our timezone, which means ppl were confused about the start/end dates, etc)

—-----------------------------------—-----------------------------------—-----------------------------------—--------

Disclaimers:

* I cofounded gitcoin but I have been disaffiliated from leadership of the DAO for about a year.
* The DAO is now in charge 100 pct.
* I am passing along "consider" feedback.  None of the feedback is directing any work in the DAO.
* I hold GTC.
* All of the information about Gitcoin in this post is public information.
* Nothing in this post is financial advice.

-------------------------

ccerv1 | 2023-05-17 15:32:28 UTC | #2

Very cool!

> Did I mention that this was on a L2? It cost about $4 to launch the round, $2 to apply to the round, and each contribution cost about $.50 in gas fees.

In the future, would love to see a round manager be able to offer gasless applications + voting/contributions on a L2 with strict passport eligibility requirements and/or allowlisting to prevent attacks

-------------------------

meglister | 2023-05-17 16:31:26 UTC | #4

thanks @owocki -- great feedback! putting it into product board :rocket: 

as a newbie to the Quadratic Lands, I have to say it makes me feel "less dumb" that you still have trouble explaining QF. :) that said, points to a bigger opportunity to reframe QF using values-oriented language, perhaps something like Nike talking about NFTs: https://twitter.com/patrickxrivera/status/1658511903382204417

-------------------------

koday | 2023-05-18 13:34:04 UTC | #5

Great experiment and writeup - as far as I know, you're the first one to spin up and complete a fully self-serve QF round on Grants Stack which seems fitting :grinning:


[quote="owocki, post:1, topic:15068"]
After giving attendees the opportunity to opt out, we proceeded to ingest the attendee database into the granting system. But we hit another wrinkle, Gitcoin’s system expected everyone to submit their own grant application. And there is no bulk uploader for a round manager to simply create the grants on behalf of their attendees.
[/quote]

Also, I found this super interesting - the need for something like this has never crossed my mind but as we try to onboard more non-Web3-native users to the ecosystem I definitely see the value in it. I'm also curious how much it would save in gas (moreso for mainnet rounds) to collect applications off-chain and submit them in a batch through a single transaction. Would love to hear some more thoughts around this from product and ops folks as Grants Stack development continues.

-------------------------

owocki | 2023-05-18 15:06:51 UTC | #6

[quote="koday, post:5, topic:15068"]
Also, I found this super interesting - the need for something like this has never crossed my mind but as we try to onboard more non-Web3-native users to the ecosystem I definitely see the value in it. I’m also curious how much it would save in gas (moreso for mainnet rounds) to collect applications off-chain and submit them in a batch through a single transaction. Would love to hear some more thoughts around this from product and ops folks as Grants Stack development continues.
[/quote]

One of the hackers in the supermodular ecosystem has been working on a batch grant upload tool.  [Here is a demo.](https://www.loom.com/share/89e75de8c54f49e3bf23b392e14b9238).

This tool is more for the convenience of uploading a batch of participants vs saving gas (gas was p cheap on optimism) tho.

Permissionless protocols ftw!

-------------------------

llllvvuu | 2023-05-20 21:12:41 UTC | #7

[quote="owocki, post:1, topic:15068"]
A handful of people were wondering how much match they were getttng for a contribution and tried to do the math. It would have been nice if the UI showed the answer so ppl dont have to do the match.
[/quote]

IMO this should be configurable by the round owner. The use case is clear, but there is also a use case for hiding this information and even hiding all current stats (how many people have donated so far etc) so as not to bias or add undue momentum to the results. Whether a project is looking hot at the time of the user logging in and voting is not necessarily an accurate indicator of anything and can be manipulated.

[quote="owocki, post:1, topic:15068"]
I noticed the random sorting on refresh or page load as well. It would be great to either have a static loading or sorting options selected by the user. Alphabetical, most interest/signaling, etc.
[/quote]
I'm a fan of alphabetical provided that the list is short enough to scroll through to the end. Trending may encourage users to stop browsing early. But of course it would be great to implement all the things (or even roll a custom feed plugin system like Bluesky) and let operators set defaults/recommendations and users choose.

[quote="owocki, post:1, topic:15068"]
It was hard to explain how Quadratic Funding works to people in a concise way. We did lean on [https://wtfisqf.com/ ](https://wtfisqf.com/) but it was still hard.
[/quote]
I wonder if people care that it's QF behind the scenes, or that it's sqrt and square, versus something more handwavy like - your match is multiplied by roughly the number of people who donated, in order to emphasize applicants with a broad/public impact.

-------------------------

kevin.olsen | 2023-05-25 11:27:58 UTC | #8

+1 to considering sorting a design choice of the round operator. Having a round configuration amplifying trending grants isn't necessarily bad. Popularity is a great signal and creates certain kinds of results. But it could drive sub-optimal outcomes in other contexts.

Love the plugin idea. Also easy to start out by having a variety of sort mechanisms that round operators can select from in the explorer view for their round.

-------------------------

ccerv1 | 2023-05-26 18:29:26 UTC | #9

Personally, I think sorting / shuffling are fine, the problem is when you are in a session, if you click a grant link to view it, and then go back to the explorer, you lose your bearings.

-------------------------

Supreme | 2023-05-30 06:56:23 UTC | #10

Hi @owocki I have a few questions:

[quote="owocki, post:1, topic:15068"]
For those locals who were not crypto native, we decided that we would use addresses that one of us controlled for each of their grants, and that we’d settle up with the locals in cash after the round.
[/quote]

There are so many thing I find concerning with this statement and questions that  I have - 
Looking at the [round eligibility](https://docs.google.com/document/d/1YUvoAMFs69g-AL7WCfiKvhgwPcOXnbNIBdlmr3MJS7g/edit#):
1) Using an address that you control for someone else - seems to be falsification/fraud/impersonation
2) Why not choose to take this opportunity to educate the non-crypto natives?
3) What did  you "settle up" on, and why in cash?  

[quote="owocki, post:1, topic:15068"]
the babysitters who watched the children, a woman who taught us a cooking class, and the staff from the hotel we stayed at, were all included.
[/quote] 
4.)  It sounds like "participants" were given a vacation and a babysitter for their    donation -   would you consider this to fall in the scope of bribery?

[quote="owocki, post:1, topic:15068"]
In my opinion, more projects should be focused on providing value to people first
[/quote]
5) What value did this Metacamp provide?

[quote="owocki, post:1, topic:15068"]
I put 3 ETH in myself, and was happy to see that I was matched with 3 ETH from [Metacartel’s Ethos project ](https://www.metacartel.org/ethos), and .26 ETH from other participants, bringing the total pool of funding to 6.26 ETH.
[/quote]

6. Are there tx hash's for these donations?

[quote="owocki, post:1, topic:15068"]
assembling a crack team of DAO nerds that was in charge of ingesting all of the grants into the system and then transferring the grants to the users themselves. This ride or ride crew took about 45 minutes to clean and ingest the 40 participants to the event (plus 4 locals who were helping out) into the Grants system.
[/quote]
7.) Were those that gave their information aware that someone else would have access to their info?
8.) Do you vote with the GTC that you hold?

-------------------------

owocki | 2023-07-26 17:09:44 UTC | #11

Just wanted to circle back and share this testimonial that @Yalor shared (with permission) with the group:

![Screenshot 2023-07-26 at 11.09.15 AM|224x500](upload://mWXln6qCMFwkGidNFAVWtGvHctK.jpeg)

![Screenshot 2023-07-26 at 11.08.04 AM|624x422, 50%](upload://qS6hSHuZuTZd6vrnQztO6WyehvF.png)

-------------------------

KarlaGod | 2023-12-06 13:08:06 UTC | #12

This is so insightful, I'd like to replicate what you've done in my community, so first I'm going to read the Green Pill book, and then I'm going to listen to all the content on the podcast, and I'm going to come up with a strategy to Green Pill my community.

Will post my updates as I progress :smiley:

-------------------------

FractalVisions | 2023-12-09 01:03:37 UTC | #13

[quote="owocki, post:1, topic:15068"]
The UI will only allow the crowdfund to begin after the applications end. This forced us to try and decide who could be in the round before the crowdfund started… when we would have preferred to have some overlap between the two periods.
[/quote]

We ran into similar issues when trying to set up our own formula for a mini grants round.

For instance, the crowd fund that we are currently running as our pilot program had to be set up as a quadratic funding module instead of the direct grants… Which actually do not function the way that we intended them to after setting up a round with the direct grants option because we wanted the perpetual cycle to last throughout the future in case we wanted to run future round on the same program… Little did we know the direct grants was for capital that was already allocated upfront and not for crowd sourcing direct grant donations.

This caused us to also shift to the quadratic funding model and have to close the cycle for crowdfunding halfway through the first quadratic funding round in order to deposit the funds into the QF matching pool. I’m not certain if there’s a way to distribute funds from a QF matching pool in portions and keep the direct donations coming in after the fact. It was not clear according to the UI.

Alternatively this method allows us to reiterate and improve upon the pilot program in subsequent rounds quarter to quarter. 
We made it work!


[quote="owocki, post:1, topic:15068"]
But what were the privacy implications of loading everyone into the round? The event itself was ticketed via NFTs, so everyone’s information was on chain already. But we felt that we could not proceed without allowing attendees the opportunity to opt out.
[/quote]

This is great that you took the time to let folks decide how they wanted to be included. Perhaps in the future off chain attestations could be provided to help verify human identification with account abstraction.

[quote="owocki, post:1, topic:15068"]
I even printed out these fun little promotional fliers for the round using the hotels printer.
[/quote]

This is wonderful. Please let us know if you would like us to provide some printing services in the future for anything along these lines. Of course some proper prior planning would be needed for us to produce the materials.

[quote="owocki, post:1, topic:15068"]
I don’t think people realized that the new Gitcoin Grants tooling can be used in this way (or even that anyone can self-serve create a round at all). So I was happy to take the new tooling off the beaten path a little bit and experiment with a new form of social coordination.
[/quote]

We have been a part of many events and festivals before and think this is a great way to incentivize the folks who set up the grounds prior to and after the event.

Another role I have served at a concert before is something called a “illuminator” for a musician on tour who would incentivize the core members of their fan group to work during certain shows over the course the tour. I would get a free ticket but in order to do so I would have to put down a deposit when I would show up for my role. 
Then, after the show everyone that was serving these duties would have to show up and serve a sobriety test to receive their deposit back for the work they did. 

The duties of these members included walking around and giving people water, snacks, and free merchandise or art. You are also encouraged to help people if you saw that they were intoxicated just to check on them, and if there was a medical emergency or you saw somebody that needed assistance you became the first line of communication to medics arriving in the middle of a crowd.

Kudos to you for giving us a great case of study here.

[quote="owocki, post:1, topic:15068"]
It was hard to explain how Quadratic Funding works to people in a concise way. We did lean on [https://wtfisqf.com/ ](https://wtfisqf.com/) but it was still hard.
[/quote]

This is always a difficult term to explain. Something that comes to mind is that a small replica of quadratic funding with a finite amount of funds could be used to display quadratic funding with an app that’s shared on a screen live for people by having presets and models that show funds being redistributed back-and-forth to the same addresses, along with a gasless transaction mechanism to keep the funds available in the app for example. Maybe then they could see how it works with a visual representation in real time onchain.


[quote="owocki, post:1, topic:15068"]
I turned off Gitcoin Passport in the round manager UI for the round, but during the contribution experience, the UI still prompted people to sign up for passport or their contributions wouldnt be matched. I think if Passport is off for the round, then the contributors should not get that prompt.
[/quote]

This is something we also were aware of when setting up our crowd funding round. We shut off the passport for that aspect. 
When we set up the quadratic funding round that is crowdfunded we set up a completely separate round so that way we could implement the passport when people are contributing to each project.

The crowdfunding round actually goes all the way up halfway through the quadratic funding round so it serves as a funnel for direct donations to the quadratic funding without having to choose any project and allows an alternate source for folks to direct people to contribute towards besides their own grant in the round. Creating a synergy of crowdfunding through the participants of the round themselves.

-------------------------

sophia | 2023-12-10 06:38:31 UTC | #14

[quote="owocki, post:1, topic:15068"]
Would be really nice to see who made the most donations or how many each person made but not on the receiving side.
[/quote]

Hypercerts ran something similar to this for Zuzalu. Think it would've been really interesting to build upon Gitcoin Grants rather than building the whole marketplace from scratch. 

One nice thing about using Hypercerts is the ability to clearly see who made the most donations for the entire collection of grants or for each individual grant in a digital billboard UI -  like [this].(http://bafybeic7ewuxfegbqjyh7thgitkppbboc7dvgwawutcejqm4gly6rjwa2i.ipfs.localhost:8080/app/zuzalu/billboard/)

A quick flow could be:
1. Hypercerts automatically created for each grantee
2. As people donate they automatically get a fraction of that specific Hypercert correlated to their donation amount

What this enables:
* the ability to easily see who made the most donations for a specific hypercert or across an entire collection of hypercerts
* grantees can make collections of all the Hypercerts they've ever gotten (say the babysitter got a Hypercert at Metacamp and then later on for some other impact at another event - they can make a collection representing all the impact they've done to make a visual representation of their impact, reputation, social graph of people who've donated to them)
* starts building out the data layer for retroactive rewards (say someone reads this post and wants to allocate even more tips to the grantees and maybe even gift those who donated with a nice lil tip too - they can now do that)
* new incentives for donating (right now there's social pressure and other intrinsic incentives to donate. but the potential for retroactive rewards because you were an early donors might open up a whole new range of new incentives that incentivize people to donate even more...)

Would love to hear your thoughts on this

-------------------------
