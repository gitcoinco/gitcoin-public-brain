---
id: 10711
title: "The Grants 2.0 Flywheel ♻️"
slug: the-grants-2-0-flywheel
category: gitcoin-grants
url: https://gov.gitcoin.co/t/the-grants-2-0-flywheel/10711
created_at: 2022-05-25T23:51:56.558Z
last_posted_at: 2022-06-06T00:24:15.292Z
posts_count: 3
views: 4300
like_count: 14
---

# The Grants 2.0 Flywheel ♻️

<https://gov.gitcoin.co/t/the-grants-2-0-flywheel/10711>
owocki | 2022-06-06 15:52:14 UTC | #1

# Grants 1.0 flywheel

I think that Gitcoin Grants is a triple sided marketplace.

![Screen Shot 2022-05-25 at 5.19.23 PM|582x500](upload://zb6PplBdYzvvxoYnjetCOlnr5a4.png)

1. We enable **Community/Ecosystem builders** to get their JTBD (Build their ecosystem/community) done.
1. The way we do that is we enable **Grant Owners** to get their JTBD (raise $$$) done.
2. The way we do that is we enable **Contributors** to get their JTBD (find great projects, support them) done.

This is a virtous flywheel here where each side of the market contributes to the network effect of the entire market.

[![a0ce63f7-2a5e-4155-a040-1426497419d6|661x500](upload://4x7tOb0JKcxruXdbUfA06lLlmBd.gif)](https://ncase.me/loopy/v1.1/?data=[[[1,484,194,0.5,%22more%2520contributions%22,4],[2,571,336,0.5,%22more%2520grants%22,4],[4,726,210,0.5,%22more%2520ecosystems%22,4]],[[2,1,70,1,0],[1,2,60,1,0],[4,2,-35,1,0],[2,4,-58,1,0]],[[626,134,%22Grants%25201.0%2520Flywheel%22]],7%5D)

Said another way:  

- More contributions creates more grants creates more ecosystems => (repeat)
- More ecosystems creates more grants creates more contributions => (repeat)

Because each marginal new user creates more value for each grant owner, and visa versa, the network is subject to power law growth in it's utility.  This law of network value is called [Metcalfe's law](https://www.techopedia.com/definition/29066/metcalfes-law#:~:text=Metcalfe's%20Law%20is%20a%20concept,100%20(10%20*%2010).):
![Screen Shot 2022-05-25 at 6.50.47 PM|690x368](upload://5vCd3oxg7EVrlatnpRUV59GOSLt.jpeg)


It gets better. We can build this triple sided market by choosing the leverage point on any of the 3 sides of the marketplace.
1. Focus on getting more ecosystems (via sales)
2. Focus on getting more grants (via marketing)
2. Focus on getting more contributions (via marketing).

This triple sided marketplace (and Metcalfe's law) is how Gitcoin has grown to help **78,070** funders reach an audience of **318,218** earners. Gitcoin has facilitated **2,069,421** complete transactions to **10,457** unique earners.

# Grants 2.0 flywheel

I think that Grants 2.0 builds on the momentum of Grants 1.0 in a really important way.

In the second half of this post I aim to articualte how.

Grants 1.0 was a monolithic app, but Grants 2.0 will be made up of a suite of modular money legos that are all interoperable with each other (and replacable)

![Screen Shot 2022-05-25 at 5.27.38 PM|690x318](upload://iaivLh3U2dxl3xmjQmlfx1iTmng.png)

1. At the base of the system is a deeply liquid grants registry (which in the spirit of [Practical Pluralism](https://gov.gitcoin.co/t/practical-pluralism-essay-draft/10462), is interoperable with other grants programs).
2. Built on that is an ecosystem of mechanisms that all help create more contributions on the platform.  
   - In Grants 1.0, we leveraged [Pairwise QF](https://ethresear.ch/t/pairwise-coordination-subsidies-a-new-quadratic-funding-design/5553) and were stuck with it because of the monolithic architecture.  But in Grants 2.0, we could build many pluralistic mechanisms (MACI QF, [DeSoc QF](https://gov.gitcoin.co/t/how-soulbound-tokens-can-make-gitcoin-grants-more-pluralistic/10077), Retroactive Public Goods Funding, Dominance Assurance Contracts, etc) on top, or integrate other mechanisms (like Optimism's RetroPGF or CLRFunds Maci QF).  
   - This allows for more modular choice among ecosystems about how they want to coordinate their ecosystem.
    - It also allows mechanism designers to quickly traverse the design space of possible mechanisms to get real emperical feedback & data.
3. We can supercharge this ecosystem by adding Governance to any part of the system that needs it.
   - For example, the DAO could build useful components that (1) offer Mutual Grants to Grant owners, (2) enhance the sybil resistence of the system, (3) help curate Grants, (4) set the round rules.

I really cant emphasize enough how much this modular & composable architecture matters to building on the EVM.  

https://twitter.com/deaneigenmann/status/1524746298074697732

What is really exciting to me is how this modular architecture enhances the existing  Grants 1.0 flywheel.

[![a9643b9b-88c6-459b-ba74-e43cb74ba356|690x392](upload://35SqjkSp2hXqM4h4XqMo98tEuLn.gif)](https://ncase.me/loopy/v1.1/?data=[[[1,563,241,0.5,%22more%2520contributions%22,4],[2,650,383,0.5,%22more%2520grants%22,4],[4,805,257,0.5,%22more%2520ecosystems%22,4],[5,466,91,0.5,%22more%2520gtc%2520utility%22,5],[6,387,257,0.5,%22more%252C%2520better%252C%2520mechanisms%22,5],[7,428,410,0.5,%22more%2520registry%2520integrations%22,5],[8,214,311,0.5,%22more%2520developers%22,5]],[[2,1,70,1,0],[1,2,60,1,0],[4,2,-35,1,0],[2,4,-58,1,0],[7,2,-30,1,0],[6,1,-29,1,0],[1,6,-42,1,0],[2,7,-26,1,0],[8,7,-19,1,0],[8,6,13,1,0],[6,5,-23,1,0],[5,6,-39,1,0],[1,5,-16,1,0],[5,1,-15,1,0]],[[716,192,%22Grants%25201.0%2520Flywheel%22],[216,179,%22Grants%25202.0%2520Flywheel%22]],8%5D)

In Grants 2.0, we can enhance the Grants 1.0 flywheel by giving our ecosystem participants more leverage points to create network effects.  The levers that become available to them in Grants 2.0:
1. Building more better mechanisms into the platform.
2. Building more registry integrations into the platform.
2. Building more governance utility into the platform.

It is important to note that this modular open source architecture presupposes that each module will have good documentation + there will be a solid developer relations campaign to build out this ecosystem .  Having these things will create a thriving developer ecosystem + marketplace of mechanisms to fund these grants.  *(We could jumpstart this with Gitcoin Hackathons + Moonshot Collective)*
![Screen Shot 2022-05-25 at 5.36.34 PM|690x378](upload://oy9amwFriTFsMY0cObHfry7jn08.png)

By creating this thriving ecosystem of modules,  we can speed run the search space of possible coordination mechanisms, which speeds our ability to reach our shared mission.

If you think of Gitcoin as being on search for better coordination mechanisms that help us meet our purpose (help communities build & fund their shared needs), then you can visualize the search as follows:

We are in a [hill climbing problem](https://cdixon.org/2009/09/19/climbing-the-wrong-hill) where the heuristic (how high or low each point in the hill climbing problem is), is defined by the heuristic of "how much does it help communities meet their shared needs".

Within this hill climbing problem, we are looking for the global maxima.  The mechanism that helps us find the global maximum utility this heuristic (again, the heuristic is "how much does it help communities meet their shared needs?")

![Screen Shot 2022-05-25 at 5.34.23 PM|690x384](upload://zhhiNvA0jfxjJuFTe3HMirorx9Q.png)

We can speedrun the traversal of that mechanism design space by creating a thriving ecosystem of developers who are building different flavors of QF in parallel with each other.   

By creating & designing new modular plugins that do a better job of coordinating ecosystems + deploying them to our ecosystem partners, we find the ultimate coordination mechanisms for helping communities build & fund their shared needs.

Here is the same diagram, but laid out with multiple mechanisms (many of which are on our roadmap) on it.

![Screen Shot 2022-05-25 at 5.34.09 PM|690x390](upload://akKtcFxK5k4h848dZxHtE1JU8Pb.png)

Feedback welcome.

-------------------------

owocki | 2022-05-25 23:56:09 UTC | #2

Oh, one other Grants 1.0 flywheel effect I think is really powerful (but not really documented above):

The community that serves (1) ENS can also be the community that (2) Gitcoin serves can also be the community that (3) Ethereum serves. 

Visualized below, each ecosystem that does a QF round is a circle in a series of circles that sometimes overlap and sometimes do not.  

![Screen Shot 2021-12-14 at 1.00.53 PM|690x383](upload://lD4SzC3BmVE6TOadxafzgTEmxU1.png)

Whats exciting to me is the intersection of these overlapping circles + the opportunity to force multiply projects that serve multiple ecosystems.  

e.g. if Project X₁ is in QF Matching Round Y₁, the matching multiple of that is Z₁. And if you add Project X₁ to Y₂Y₃...Yₙ, then the matching multiple of it becomes Z₁*Z₂*Z₃*...Zₙ.  essentially if each QF round for each public is a fan, then all-together they stack to be a jet engine.

This in fact did happen for [Coin Center](https://gitcoin.co/grants/1668/coin-center-is-educating-policy-makers-about-publ) during GR12 ($1 contribution == $1000 in matching).  The matching multiple was so good that the [twitterati](https://twitter.com/NeerajKA/status/1466416228084457497) though it was too good to be true. :laughing: 

This is an extremely powerful primitive!  If each QF matching pool is like a fan, then the combination of several matching pools together is like a jet engine!

-------------------------

owocki | 2022-06-06 00:24:15 UTC | #3

[quote="owocki, post:1, topic:10711"]
1. We enable **Community/Ecosystem builders** to get their JTBD (Build their ecosystem/community) done.
2. The way we do that is we enable **Grant Owners** to get their JTBD (raise $$$) done.
3. The way we do that is we enable **Contributors** to get their JTBD (find great projects, support them) done.
[/quote]

I would like to augment this graph to represent the following feedback loop (denoted in blue)..

![Screen Shot 2022-06-05 at 6.22.00 PM|587x500](upload://vUQ1hnfPF73dIhcCGW8y5KtTBTK.png)


1. We enable **Community/Ecosystem builders** to get their JTBD (Build their ecosystem/community) done **(and get feedback about which parts their community is worth funding)**.
2. The way we do that is we enable **Grant Owners** to get their JTBD (raise $$$) done. **(and get feedback about which things their community thinks is worth funding)**
3. The way we do that is we enable **Contributors** to get their JTBD (find great projects, support them) done.  **(and give feedback about which things they think is worth funding)**

-------------------------
