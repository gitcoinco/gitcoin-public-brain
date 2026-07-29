---
id: 16875
title: "Reportcards.gitcoin.co"
slug: reportcards-gitcoin-co
category: open-discussion
url: https://gov.gitcoin.co/t/reportcards-gitcoin-co/16875
created_at: 2023-10-25T20:32:41.494Z
last_posted_at: 2023-10-30T16:44:28.373Z
posts_count: 8
views: 3451
like_count: 23
---

# Reportcards.gitcoin.co

<https://gov.gitcoin.co/t/reportcards-gitcoin-co/16875>
owocki | 2023-10-25 20:40:46 UTC | #1

a few months ago, i set out to build a tool that generates a pdf/html infographic summary of a grants stack/allo QF round.

the idea was to create something glossy that says “it got x contributions from y contributors, it was a z% success.  here are the winners, here are some testimonials.”

the thought was that this would be useful for me to have something like this in the greenpill community (well, actually, each of the communities i’ve run a round for) to market the round as a success to my peers other members of the community.  that would then increase the social support for doing further rounds in the future.

by enabling the round operator to present the results of a round back to a community that was served, there is an opportunity to 

0. make the round operator look cool
1. shape how that community perceives the round
2. gather feedback on the round
3. set up the next quarter for another round well-ahead of time

i assembled a team to make it happen (@lare.cristina @octaviaan @umarkhaneth ), and i am now happy a few months later to show it to you!

say hello to https://reportcards.gitcoin.co/ !

let me show you what the tool does.  you can view the screenshots below or click [here](https://reportcards.gitcoin.co/10/0x21Fe7B098A69F59e3483E260b76798fE32D815ce) to see a live version.

at the top of the page you can select a network & a round (the system should know how to find most recent rounds).  

you can also pull the round direclty by going to https://reportcards.gitcoin.co/NETWORKID/ROUND_ADDRESS (replace the NETWORKID and ROUND_ADDRESS with your information)

![Screenshot 2023-10-25 at 2.26.09 PM|644x500, 50%](upload://GDLkH8ScJ0IDb2K7vau9HGWzWz.png)

at the top of the report card for a specific round (in this screencap were looking at the PDX DAO round, the round I recently ran for Portland community), you will see
1. the title of the round
2. top level stats
3. how the matching pool was distributed

(this information is loaded straight from Allo Protocol - and can only be pulled after a round is finalized)

![Screenshot 2023-10-25 at 2.24.39 PM|409x500](upload://kLYhseQ4C3z5FigIDG2j1FVej7S.png)

below that, you will see a note from the round operator.   only the round operator can set this by connecting their wallet + typing it in.

![Screenshot 2023-10-25 at 2.28.16 PM|690x419, 75%](upload://oR050qlLCFyCVx1Fb4DdJvHHrjg.png)

below that you will see a leaderboard for the round, and also the stats of each grant.

![Screenshot 2023-10-25 at 2.29.13 PM|690x402](upload://qINvSx8Z9MOe5OAklsBMnXkdv0p.png)

# feedback welcome

if you are a round operator, id love to hear your feedback.  does this help you market your work?  why or why not?

post feedback below or in the telegram for this proejct: https://t.me/+bwzgltpGi2g0ODBh

thanks again, especially to @lare.cristina @octaviaan @umarkhaneth & co.

-------------------------

kyle | 2023-10-27 13:28:28 UTC | #2

This is pretty cool! I get assked often - "where can I see the round results for the last ABC round?"

This looks to have most of the data folks would want to review to understand which projects received the most funding, etc.

A couple of thoughts:
- Is there a way to filter out the test / spam rounds?
- Can I get a view that shows the inverse (ie, a project view that shows all the rounds they participated in and how much they have earned).. perhaps I can click on a project from a round and then see the rounds they received more than $10 in or something

How do we see this fitting into the other tools we have to visualize the rounds? ie, the data dashboard, etc. It would be great if we had a single source of truth for all round data with lots of view available. I would hate to fragment the experience and leave lots of orphaned tools on various subdomains.

-------------------------

M0nkeyFl0wer | 2023-10-27 14:52:47 UTC | #3

this is doooooope. Looking forward to playing with this and seeing what is possible with it.

-------------------------

owocki | 2023-10-27 17:07:13 UTC | #4

[quote="kyle, post:2, topic:16875"]
* Is there a way to filter out the test / spam rounds?
[/quote]

try now, cristina just pushed an update

[quote="kyle, post:2, topic:16875"]
* Can I get a view that shows the inverse (ie, a project view that shows all the rounds they participated in and how much they have earned)… perhaps I can click on a project from a round and then see the rounds they received more than $10 in or something
[/quote]

this is a good idea!  but not something i think will be built into this tool.  perahps another module woul do it? (i wonder if this should be a tab on the project profile?)

[quote="kyle, post:2, topic:16875"]
How do we see this fitting into the other tools we have to visualize the rounds? ie, the data dashboard, etc. It would be great if we had a single source of truth for all round data with lots of view available. I would hate to fragment the experience and leave lots of orphaned tools on various subdomains.
[/quote]

So far as far as I've gotten is just listening the tools all on https://ecosystem.gitcoin.co/ 

i think it would make sense to have a cleanup process that every 6 months or so looks at the tools that have been built in/around the ecosystem and starts to think about what a common nav looks like or how to stitch them together

-------------------------

umarkhaneth | 2023-10-27 20:09:30 UTC | #5

[quote="kyle, post:2, topic:16875"]
Can I get a view that shows the inverse (ie, a project view that shows all the rounds they participated in and how much they have earned)… perhaps I can click on a project from a round and then see the rounds they received more than $10 in or something
[/quote]

Harry, @Sov, and I are building something for this! It's currently called 'Grants Archive' and will allow anyone to look back and view the history of the Gitcoin Grants Program by round, project, and/or cause. 

[quote="kyle, post:2, topic:16875"]
How do we see this fitting into the other tools we have to visualize the rounds? ie, the data dashboard, etc. It would be great if we had a single source of truth for all round data with lots of view available. I would hate to fragment the experience and leave lots of orphaned tools on various subdomains.
[/quote]

I also worry about the fragmentation and many tools each doing a slightly different thing. 

I think grants-archive and my grants-data dashboard may merge somewhere along the lines but reportcard kind of feels like it's best as a separate tool for round operators to build marketing collateral rather than as a data-viewer. 

Right now it feels like we're in a 'building more data tools' phase and that we'll likely need to combine them + reduce them in the future to provide better UX.

[quote="owocki, post:4, topic:16875"]
So far as far as I’ve gotten is just listening the tools all on https://ecosystem.gitcoin.co/
[/quote]

thanks for putting that together!

-------------------------

0xKurt | 2023-10-28 07:11:17 UTC | #6

That's a nice tool! I love it.
Also I love the ecosystem list!

-------------------------

meglister | 2023-10-30 16:11:21 UTC | #7

This is really cool -- thank you for building and posting it! I'm interested to see how it's used in GG19. We talk a lot about both the power of Grants Stack building in an open source environment and it's cool to see how the product can be permissionlessly extended like this by relying on our indexer data. It might be cool to point to particular GS repos that are used on ecosystem.gitcoin.co so others can fork the forks!

If it's used by round managers I'd love to figure out how to integrate it into the manager workflow so that it's more easily discoverable.

-------------------------

FractalVisions | 2023-10-30 16:44:28 UTC | #8

Amazing!!! 🤩 

Beyond each round it’s always a bit of a puzzle 🧩 to dig up old links trying to find information ℹ️ regarding what occurred in regards to each project. This is something we will definitely 💯 utilize!

It would also be very useful if the report card linked to the old proposal of each project somewhere. That way  folks could view previous renditions of the projects grant proposals and better understand how the team or product came into existence.

-------------------------
