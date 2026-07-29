---
id: 6874
title: "How might we decentralize Gitcoin Grants Discovery?"
slug: how-might-we-decentralize-gitcoin-grants-discovery
category: open-discussion
url: https://gov.gitcoin.co/t/how-might-we-decentralize-gitcoin-grants-discovery/6874
created_at: 2021-06-18T19:44:52.646Z
last_posted_at: 2021-06-27T00:05:57.143Z
posts_count: 7
views: 4011
like_count: 14
---

# How might we decentralize Gitcoin Grants Discovery?

<https://gov.gitcoin.co/t/how-might-we-decentralize-gitcoin-grants-discovery/6874>
owocki | 2022-05-28 15:38:05 UTC | #1

hey all,

we [recently discovered](https://twitter.com/owocki/status/1405512789444071428) that the projects that are more highly visible on gitcoin grants are more likely to be funded.

because of that, im trying to figure out how to enable more discoverability on gitcoin grants for great projects. 

# what we are doing so far.

## sorting algorithms

right now the [grants explorer](https://gitcoin.co/grants/explorer/)  has the following sort options: 
![Screen Shot 2021-06-18 at 1.39.15 PM|370x500](upload://tyzocc6ta017lOYag6xrSksuyfc.png)

## collections

and we've also launched [collections](https://gitcoin.co/grants/explorer/collections) which are basically a way for anyone to sort their favorite projects + enable easy browsing of them

![Screen Shot 2021-06-18 at 1.40.42 PM|690x470](upload://dMqr1PCNVreXx4O67zmkvm6Wmxb.jpeg)

# what could we do in the future?

in the future, it is envisioned that gitcoin grants [will be completely decentralized](https://gov.gitcoin.co/t/workstream-suggestion-decentralize-gitcoin/180) and as part of that @ [phutchins](https://gov.gitcoin.co/u/phutchins) @ceresstation and others are considering what type of ways we can solicit community input on which grants should be highly visible on the site.

i've started a [twitter thread](https://twitter.com/owocki/status/1405512789444071428) to facilitate discussion on these ideas, but I wanted to open up a post about this on the governance forums so that we can design together.  

open to suggestions.  if you have an idea, post it below!

-------------------------

owocki | 2021-06-18 19:46:04 UTC | #2

one way we might do this without building any new product (eg in GR10) is if you all tell me which COLLECTIONS of grant should be featured.  

this is something the core team has historically (eg before the DAO launched) done, and i truly think the stewards should have the privilege of doing it from here on out

(these are the collections https://gitcoin.co/grants/explorer/collections/? )

if you are a steward, and feel strongly that a specific collection should be featured pls LMK.

-------------------------

martz | 2021-06-22 05:50:05 UTC | #4

https://gitcoin.co/grants/explorer/collections?collection_id=1218

-------------------------

Spugpow | 2021-06-22 07:49:22 UTC | #7

I mentioned it in the Twitter thread, but I'll post here for visibility: I think it would be good to see what collections a project is part of on the project page itself, ordered by the collections' popularity. That way a user can see that a decentralized ID is part of a collection with other IDs for example, and they can click through to the collection to find other projects they might be interested in. Basically, make collections discoverable from grants as much as grants are discoverable from collections.

It would also be nice if projects could self-organize by adding tags to categorize themselves. Then users could click on the tags to see what other projects had put themselves in the same category, or find similar projects by putting tags in the search bar.

-------------------------

Spugpow | 2021-06-22 08:16:32 UTC | #8

It would be cool to adopt [this](https://gov.gitcoin.co/t/proposal-gitcoin-round-10-matching-pool-allocations/4988/6?u=spugpow) suggestion, and make collections themselves the recipients of quadratic matching. Then you could surface collections using the same algorithms you use for projects.

-------------------------

markop | 2021-06-24 16:58:54 UTC | #9

Looking from the user perspective I believe that Gitcoin offers plenty of ways for them to search, filter, and find the grants they want to fund. I agree that a lot of times great grants get buried down the list but whatever we do to bring them up we are the ones enforcing that, thus making other grants come into their place (there's always gonna be someone at the bottom). 

This is a usability and UX research topic and something that need to be worked on deeply understanding existing user profiles and their interactions on the site in order to provide simple solutions targeting their specific needs and solving the bigger problem. 

Personally, I just take an hour or two and simply go throug  **e v e r y   s i n g l e    g r a n t**  and decide which ones to add to cart. But my path, intentions and motivations are not the same as to others. Therefore, I suggest doing more research and tracking site metrics, looking for dropoffs, and finding ways maybe through browsing the site to encourage further discovery (suggestions, similar grants, people who viewed also viewed etc. / just thinking out loud).

I didn't offer an explicit solution but hope this helped a bit.

-------------------------

Alunara | 2021-06-27 09:19:49 UTC | #10

As a developer I like the sorting algorithms, but they're a bit nerdy and I suspect >95% of the users don't see them or don't care too much about them. Even if people do see and use them they might not know what is best and they'll probably try different ones at random.

The collections are also a great idea, but one of the downsides to them is that if I for example have a grant I'm basically begging the popular folks to include my grant in their collection. You'll be highly dependent on your existing social networking skills, and as a developer that is not to great at pitching himself it's extremely difficult to get a proper footing.

This is also why I started out with [Grandiose](https://gov.gitcoin.co/t/grandiose-a-gitcoin-grant-discovery-and-exploration-tool/149), where my goal is to make finding grants fun without relying too much on social networking skills or possible biased algorithms. Instead, I'd prefer to explore grants while doing fun little games that don't rely on different ordering or networking.

I'm currently taking a small break playing World of Warcraft, and this game also makes the most mundane and borings tasks fun. With Grandiose I aim to do the same, by making exploration fun and non-biased without the user having to think about anything at all. I've started out with a Tinder like system of swiping and aim to re-implement collections as I think there's much more to them than simply being shared with others. Other things we could try to 'gamify' exploration is by introducing mini-games such as memory or other games that allow grants the opportunity to be seen without some kind of ranking or sorting algorithm. Another venture would be multiplayer kind of games with leaderboards, but we'll have to be wary that it doesn't simply become a popularity contest again but with extra steps.

-------------------------
