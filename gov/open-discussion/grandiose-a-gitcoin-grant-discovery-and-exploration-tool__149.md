---
id: 149
title: "Grandiose - A Gitcoin grant discovery and exploration tool"
slug: grandiose-a-gitcoin-grant-discovery-and-exploration-tool
category: open-discussion
url: https://gov.gitcoin.co/t/grandiose-a-gitcoin-grant-discovery-and-exploration-tool/149
created_at: 2021-05-18T21:48:27.596Z
last_posted_at: 2021-06-08T19:09:34.328Z
posts_count: 14
views: 4858
like_count: 39
---

# Grandiose - A Gitcoin grant discovery and exploration tool

<https://gov.gitcoin.co/t/grandiose-a-gitcoin-grant-discovery-and-exploration-tool/149>
Alunara | 2022-05-28 15:40:52 UTC | #1

Grandiose is a Gitcoin grant discovery and exploration tool, aiding users in their quest to find and donate to grants and give an insight to what is present in the grants ecosystem. This is done by experimenting with novel ways to gamify the search for new grants.

The app can be found over at https://grandiose.app.
The project's focus is currently on delivering a minimal viable product.

The following features are currently live:
* An overview of all grants (using a test subset at the moment)
* A like / dislike matching algorithm
* Leaderboards
* Grant of the Day
* Some cute KPIs / stats

Core features that are not yet done but are considered a requirement for the MVP:
* Shopping cart with support for zkSync. There's no use in using Grandiose if you still have to leave the app and go to the Gitcoin website where you manually have to find your grants again.
* Collections. A great feature present in the current version of Gitcoin. People want to share what they like.
* Flash grants. Yeeted the idea from the flash deals you can find in some online game stores. You get shown 4 different grants, and every 6 hours one of the 4 grants gets (randomly?) replaced by a different one.
* Other leaderboard types / KPIs. Not a hard requirement though.

With these features I feel like the app would be ready to offer users a proper and satisfying first experience. There's no possible way this can be completed by GR10, meaning I'll have until GR11 which should give some extra time. This is a side-project I work on after my normal working hours, so that extra time is a nice boon.

**Why?**
There's two reasons why I've decided to create this app.

The *first* reason is that whenever a new funding round kicks off, people are presented and overwhelmed with an enormous collection of grants they might contribute to. You can search by terms and tags, but you still have to manually browse through a big list, which isn't very fun. What usually happens is that people ask around, seeking grant recommendations from people they know and trust. This leads to funding becoming a popularity contest where a lot of hidden gems might not get the attention they deserve. The goal of this app is to introduce gamifications that not only should make exploration fun, but also provide a better experience overall where projects will get the attention they so rightfully deserve.

The *second* reason is that Gitcoin wants to be a credibly neutral platform and focus on solving the problem of public goods (funding), not necessarily showcasing users what grants should be to their likings. Such algorithms could also be accused of being biased in some way or another, damaging Gitcoin's legitimacy. This app could relieve Gitcoin from that duty.

**Will it be open source?**
Naturally. I'm planning to release the source together with the MVP when it is deemed ready. For those interested, the front-end is made with Vue + Typescript. The back-end is written in C# with .NET 5.

-------------------------

ceresstation | 2021-05-20 17:45:09 UTC | #2

This is actually so cool, you should check out @austingriffith's prototyping workstream if you haven't already:

https://gov.gitcoin.co/t/workstream-suggestion-public-goods-prototyping/130

-------------------------

Alunara | 2021-05-20 19:54:03 UTC | #3

I've given it a peek, and it sure looks cool!

I'm happily working on this project in my spare time however, and don't necessarily need any funding (that's what I think the workstream is for?), given I don't really have a way to put that funding to use. The app is 'just' a website with a small back-end that runs fine for now on a $5/mo VPS. Scaling is not a problem yet. The app's also living on the very outskirts of Ethereum so it doesn't really interact with the blockchain at all, aside from the shopping cart I'm working on right now using zkSync. In the future I also might use somebody's Metamask to store personal settings but that's about it. I was planning on just dogfeeding the project by having a grant up on Gitcoin itself.

Of course I'd be happy to connect with other people if they have any ideas, suggestions or need help in general!

-------------------------

phutchins | 2021-05-21 13:14:59 UTC | #4

This is awesome. I’m excited to see it progress. Along the way it would be great to collect feedback from you around your experiences. 

One of the areas that we plan to put work into in the Decentralize Gitcoin Workstream is documentation of the current API as well as improving and decentralizing the API.

Keep that in mind while you build and we should connect in a few weeks.

Keep up the great work!

-------------------------

ngovanloi | 2021-05-26 17:09:33 UTC | #5

nice ! thank you so much for infomation !

-------------------------

DreadKnight | 2021-05-28 10:36:00 UTC | #6

This seems like an awesome project. A tinder for grants <3 but so much more actually. Good job!

I really need to find ways to raise some money for a possibly world changing project that I've been poking at for 2 decades now https://gitcoin.co/grants/916/ancient-beast - so if this can help with that by bringing more exposure and donors, then Grandiose ftw, because garbage copycat projects like Pepemon that blatantly infriges a well known franchise is raising a lot of money via multiple gitcoin grant campaigns, which is a very sarcastic and depressing thing while I'm starving.

-------------------------

K1du | 2021-05-28 11:14:15 UTC | #7

When is the release date more or less?

-------------------------

Cashmoneyind | 2021-05-28 13:26:32 UTC | #8

This project sounds so great! I’m loving this community more and more!

-------------------------

Alunara | 2021-05-29 19:19:38 UTC | #9

Hey, took me a moment but I finally recognized you! I remember your project from literally 10 years ago in the #reddit-gamedev channel on FreeNode. Nice to see that you're still working on that! But you got it right, the first iteration is a "tinder for grants". Not very original, but I have a couple of other ideas I want to implement afterwards.

-------------------------

Alunara | 2021-05-29 19:22:33 UTC | #10

I wouldn't worry too much about a release date. I'm working on the three main features (shopping cart / collections / flash grants) right now, and will probably release it as open-source as this MVP is done. I believe there's a new Gitcoin Grants round coming up soon and I definitely won't be able to get this all done before that. This should give me ample time in order to prepare a usable app before the grants round after that. Still a side-project so I'm working on this in my after hours.

-------------------------

DreadKnight | 2021-05-29 20:04:58 UTC | #11

Yeah, I used to hang around there a bit as well back in the day. Good memory you have :D
I keep grinding, but wish would have received a bit more support instead of TONS of promises.
Quite close to releasing a major version that finally has online multiplayer, though bumped into some showstopper bugs for now. But once those are squished, hopefully things will improve a lot.

-------------------------

Alunara | 2021-06-07 22:47:41 UTC | #12

Small update: I'm taking a short break at the moment, recharging myself a bit so I can later work on the project in the hopes that it's ready for GR11. In the meantime I thought it would be nice to open-source the project so that others can have a peek if they want. You can find the project over at https://github.com/0xAlunara/Grandiose.

For the moment the software is licensed under GNU GPLv3, in spirit of public goods. If this is too permissive at a later stage this could be changed. I think it should suffice for now.

-------------------------

bobjiang | 2021-06-08 02:38:51 UTC | #13

[quote="Alunara, post:12, topic:149"]
GitHub - 0xAlunara/Grandiose: Gitcoin grant exploration app
[/quote]

This is definitely awesome tool, I have the same painpoints for your first reason. love it.

-------------------------

mlnck | 2021-06-08 19:09:34 UTC | #14

LOVE the idea!
Great execution so far - Staying tuned :+1:

-------------------------
