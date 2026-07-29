---
id: 17174
title: "Shape Rotators Guide to Funding What Matters"
slug: shape-rotators-guide-to-funding-what-matters
category: open-discussion
url: https://gov.gitcoin.co/t/shape-rotators-guide-to-funding-what-matters/17174
created_at: 2023-11-23T14:20:26.848Z
last_posted_at: 2023-12-07T12:54:45.815Z
posts_count: 7
views: 5875
like_count: 23
---

# Shape Rotators Guide to Funding What Matters

<https://gov.gitcoin.co/t/shape-rotators-guide-to-funding-what-matters/17174>
owocki | 2023-11-28 23:52:16 UTC | #1

*(this post is a 10 min read, and is targeted at leaders following Gitcoin's evolution in the regen web3 space.  if you want to get up to speed,  [start with this post first](https://gov.gitcoin.co/t/systematic-exploration-of-the-coordination-mechanism-design-space/12616) and [this post](https://gov.gitcoin.co/t/how-might-we-scale-gitcoins-impact-from-50mm-gmv-to-500m-gmv/16697) next, and [this post](https://gov.gitcoin.co/t/3-transitions-from-gitcoin-1-0-gitcoin-2-0/16736) last)*

# TLDR

This post discusses the evolution of funding mechanisms in the context of Gitcoin's mission to "Fund What Matters".

We use both empirical knowledge, a priori reasoning, and a few educated guesses, to explore the evolving landscape of funding mechanisms in web3.

The post examines how different design criteria have shaped various funding experiments.

We then explore the potential future of the design space, considering additional design criteria like project maturity, retroactive funding, dependance on impact attestations, or mobile first experiments.

We then make some educated guesses about how the design space might evolve, informing where to place bets over the next 5-10 years.

# Shape Rotators Guide to Funding What Matters

As a [shape rotator](https://www.urbandictionary.com/define.php?term=shape%20rotator), I love cartography. Cartography (the study and practice of making and using maps) allows for visual understanding of what’s around us. A picture is worth a thousand words, which means that by visualizing abstract concepts, more of us can get on the same page faster & at higher fidelity than we would otherwise.

The objective of this post is to cartography the design space in & around Gitcoin’s mission (To Fund What Matters).

![|624x256](upload://pMBATMdE4VyyOUK9Eir7K2wn3aO.png)

Empirical knowledge is gained through experience or observation, relying on the senses or experiments to understand the world. A priori knowledge, on the other hand, is knowledge that is known independently of experience, based on reason or logical deduction.

In this post, I will try to leverage both types of reasoning to cut through the “fog of war” of the design space. "Fog of war" metaphorically describes the ambiguity and lack of clarity in understanding and making decisions within complex systems.

![|264x200](upload://kpce7Q3vhffsJ9php9U80020N2Z.jpeg)

# The design space

By reflecting on the growth of the internet empirically, and by reasoning about the a priori parallels between web1 and web3, we can reason about how web3 might play out..

![Screen Shot 2021-12-24 at 9.26.45 AM|624x153](upload://p1T5DJxwcgb3D1rRUJSDxGt1R5e.png)

Just as email, IMs, twitter and tik tok, and LLMs changed how we transfer information… The internet of money could change how we transfer money. How we Fund What Matters.

We have Massively Multiplayer Online Role Playing Games (MMORPGs). Now that we’ve got web3, will we have Massively Multiplayer Online Funding Games (MMOFPs)? Can large networks of people coordinating resources be more powerful than large corporations/governments/billionaires?

I have an instinct that peer to peer funding games may be the biggest wedge we have. There is a greenfield opportunity to explore the design space around Gitcoin’s mission, to “Fund What Matters”.

# The mission

Gitcoin’s mission, "Fund What Matters", is a directive emphasizing the importance of investing in or financially supporting causes, projects, or initiatives that hold significant value or impact. It suggests prioritizing spending in areas that make a meaningful difference, whether socially, environmentally, culturally, or economically.

This phrase often encourages individuals or organizations to think critically about where their money can have the greatest positive effect. It's a call to action for responsible and purpose-driven allocation of resources, aligning financial decisions with core values and priorities.

# The mission x the design space

By leveraging blockchain technology, the attributes of it that make it powerful (transparency, corruption resistance, global, open source, programmable), and the wave of innovation surrounding the EVM, we can help evolve how people “Fund what matters” to them.

Just as the internet accelerated the flow of information, web3 can accelerate the flow of capital. We can ride this wave to build and scale new funding experiments.

# The past

In 2019, the bear market had just hit. And projects in the Ethereum ecosystem needed funding.. At the time, the major forces in Eth public goods funding were the Ethereum Community Fund, the Ethereum Foundation, and Consensys. The EF/ECF had grants programs or you could get hired at Consensys.

Gitcoin discovered [Quadratic Funding](https://wtfisqf.com/) in late 2018 and launched Gitcoin Grants in January 2019. We were differentiated from the existing players by the decentralized decision making introduced by quadratic funding.

I think the design space kind of looked like this.

|criteria|comment|
| --- | --- |
|technocratic = small group of decision makers|At the ECF/EF, you had to go through a grantmaking process where a small commitee would decide if you got funding. At Consensys, you had to be hired by Joe Lubin or his disciples.|
|democratic = larger more permissionless group of decision makers|At Gitcoin, anyone can help allocate the funding due to Quadratic Funding. This scales because 1000s of projects can get funded at once.|

Here it is visualized as a 2 dimensional spectrum:

![|238x99](upload://lKHlT8BzhPMYlfZksM9K5As8KGs.png)

Of course, this doesn't tell the full story. If you were to add a 2nd axis showing the amount of funding being deployed, the design space would look something like this.

![|245x194](upload://idvxfpq0y1sTanXgBwwD7qodaGt.png)

# The present

Over the course of 2022, more players entered the space and we began to see the rise of [retroactive public goods funding experiments](https://gov.gitcoin.co/t/devconnect-zuzalu-istanbul-takeaways-for-gitcoin/17159#h-2-new-market-leaders-7) like Optimism RPGF and very simple but effective mechanisms like the Protocol Guild’s self curating registry.

Trying to further map the design space, adding another 3rd dimension…. Looks like this:

![|295x194](upload://sxCUzUVyeGOPgnkXyNePyqildF7.png)

If we were to make the 3rd dimension “simplicity”, then it would kind of look like this:

![|219x142](upload://bi4W71QJh6zFHQ3HvshtShCLpR5.png)

Each of these experiments evolved the design space forward in important ways.

1. [Retroactive public goods funding](https://vitalik.ca/general/2021/11/16/retro1.html) is based off the idea that it is easier to fund projects based on the impact they’ve already had. As opposed to speculating on the impact they might have in the future. After retroPGF is established, we can then bet that projects could receive proactive funding based on future retroactive rewards.
2. [Protocol Guild](https://protocol-guild.readthedocs.io/en/latest/) built a very simple mechanism, a self curating registry. This registry allowed projects to easily contribute to protocol development.

Lets get weird. Lets look at what this new design space looks like all together. If we combine the two 3d cubes, we get a tesseract (4 dimensional cube) showing us the new design space.

![|624x379](upload://aKnJRNpBub1tnDd53HuTVZw1jGf.png)

Since us humans have evolved to understand 3d images, this 4d visualization is a bit hard to grok visually. That said, once you spend some time staring at it, you will can internalize that we’ve found a way to conceptualize the entire design space across all 4 dimensions:

1. Technocratic vs democratic
2. Amount of funding
3. Proactive vs retroactive
4. Simple vs complex

As a [shape rotator](https://www.urbandictionary.com/define.php?term=shape%20rotator) is where things get interesting to me. As people begin launching projects that are empirically effective at funding what matters to them, we can start to build a 1, 2, 3 dimensional ….. Up to n-dimensional space of what the design space looks like.

[![|624x193](upload://taeZp0viy00AdxuWuAlRSm8TsFQ.png)](https://www.figma.com/file/G40n68I2Qyi07WgQqMTjdV/Fund-What-Matters---Cartography'ing-the-design-space.?type=design&node-id=0%3A1&mode=design&t=lW4WMLuhJ55pxpzu-1)

# The future

Now we are really starting to cartography the design space. By creating visualizations of how these mechanisms relate to each other, and extracting the criteria that makes them different, we’re starting to get a visual of the design space!! We’ve started to beat back the fog of war of the possibilities.

Here, again are the criteria (dimensions) that the market has begun to segment itself upon:

|criteria|comment|
| --- | --- |
|Technocratic vs Democratic|Is the # of decision makers larger or small?|
|Amount of Funding in $$$|Is the amount of $$ at stake larger or small?|
|Retroactive vs proactive|Is the funding criteria based on value in the past, future, present, or a combo of both.|
|Simple vs complicated|How much complexity is within the capital allocation mechanism.|

What opportunities to do something cool and innovative, building on this criteria, are there? Some examples:

* What if we built self curating registries (like Protocol Guild) into Allo and deployed them to adjacent public goods spaces (eg other than protocol developers)? How big is the TAM (total addressable market) for this?
* What if we built retroactive public goods funding into Gitcoin Grants? How big is this TAM?
* What if we built more technocratic/expert-led decision making into Gitcoin Grants? How big is thisTAM?

What if there are more criteria (dimensions) that matter? What if there is a higher dimensionality to the design space?

[![|508x206](upload://pkHMZpV8C5ErlK5cb4Dtt1oIXLX.png)](https://www.figma.com/file/G40n68I2Qyi07WgQqMTjdV/Fund-What-Matters---Cartography'ing-the-design-space.?type=design&node-id=0%3A1&mode=design&t=lW4WMLuhJ55pxpzu-1)

What dimensions would we even care to splice the design space by? And would each dimension justify the complexity of thinking in higher dimensional thinking? Since it’s hard to think in higher than 3 dimensions, maybe we’d be better off focusing on design spaces 3 dimensions or less.

That said, there might be value in exploring what dimensions to even look at.

We can make some educated guesses here. Here are all of the additional dimensions I can think would ever matter within the design space of “how do you build a mechanism that helps people fund what matters?

|Criteria (cont’d)|Comment (cont’d)|
| --- | --- |
|Mature projects vs seed projects|Is the mechanism more for mature projects or seed stage projects?|
|web2 vs web3 ux|Is the ux usable for web2 natives??|
|Effective or not.|Is the mechanism actually effective at whatever its goal is (in Gitcoin’s case building an ecosystem)? How big is the TAM?|
|Return expected vs not|Is a return expected as part of the fundraise? Or not?|
|Virality vs not|Is virality a big part of the mechanism? Like for Quadratic Funding, where people tend to share their grants on social media.|
|Does it depend on Impact Attestations?|Does the mechanism depend on impact attestations? Do we have a reliable proof-of-impact?|
|Oracle-limited or not?|If the mechanism depends on some external data source, is it limited by having reliable oracles or not? Eg if you were trying to fund a project to stop deforestation, what is the data-trail between the forest + the blockchain?|
|Credibly neutral vs not|Does the mechanism's constituents care that its credibly neutral, or does it allow for rent-seeking intermediaries?|
|Desktop vs mobile|Is the mechanism experience desktop first (okcupid, match.com), or mobile-first? (like tinder)|
|Built into social media? (emergent)|Is the mechanism a standalone website, or is it built onto a web3 social network like farcaster/lens protocol?|
|Massively multiplayer?|Will the mechanism work at scale? Will it enable Massively Multiplayer Online Funding Games (MMOFPs)?|
|Are assets fungible or not?|Do the primary assets in the mechanism resemble fungible things like ERC-20s? Or are they more based on ERC-721 like assets?|
|Can it be built on top of Allo?|This is a germane question for Gitcoin. Can it be built upon allo? Does allo help make it easier to bring to market?|
|Can it be built on top of Passport?|Does the mechanism benefit from sybil resistance? If so, does Passport newly enable it?|
|Is the funding continuous/recurring? Is it based off dependably [economically exothermic](https://twitter.com/owocki/status/1722234106954838355) funding sources?|Does the mechanism depend on fickle things like people donating? Or does it depend on continuous sources of funding (like sequencer fees or yield)?|

# Open Questions

Which combinations of these criteria have billion$$$ potential to ‘Fund What Matters’?? Where is the TAM very large now, and what design spaces have billion $$$ potential next cycle? Which will only be enabled by new ux breakthroughs (like PWAs, gasless apps, account abstraction)?

Would we be served well by building/researching many of these tools internally, or enabling 1000s of devs to build in these design spaces, on top of Allo? And perhaps taking upside in each.

It may be worth defining criteria for when it makes sense to double down on existing families of mechanisms we know are working (QF, retro PGF), vs go broad and exploring new mechanisms. Are the two mutually exclusive, or can we design a network that, like a[ slime mold](https://twitter.com/owocki/status/1456368527347044355), can both search + harvest at the same time?

Here are some of the things I am interested in doing

1. Map out spectrum of public goods funding from cradle-to-grave (or cradle-to-unicorn) for each project.
2. How does retroactive public goods funding create new opportunities?
3. How does sybil resistance from things like Gitcoin Passport create new opportunities?
4. What opportunities are there to build mechanisms into web3 social networks like Lens/Farcaster?
5. What are the mobile-first possibilities?
6. What would Gitcoin Grants but for private goods look like? Eg you get gov tokens when you donate? Would it detract from Gitcoin’s mission or be a valuable extension of Allo/Grants Stack?
7. What is the design space of Allo v2? What are the highest opportunities within them?
8. How would making the ux of Gitcoin feel more web2 native affect the market size oppy?

# Next Steps

First, I’d love to validate that this way of thinking about the design space is valuable to others. If it is (or is not), feel free to comment below, DM me, or [join this telegram group](https://t.me/+SISOI8-cs3c0NjM5).

![Screenshot 2023-11-24 at 8.55.57 AM|690x391](upload://oGUIsnGnIi3wymaSRiouwVfDajT.jpeg)


I will be putting together a working group to work through these questions above. If this sounds like you, [Join the telegram group!](https://t.me/+SISOI8-cs3c0NjM5)

# Conclusion

In this post, we reasoned empirically and a priori about how the design space for Funding What Matters has evolved so far. We then visualized it.

From there, we made some educated guesses about what other types of experiments for Funding What Matters may exist in the future. Then we identified some next steps we could take for Gitcoin (and the broader regen web3 ecosystem) to advance the mission.

-------------------------

harryeastham | 2023-11-24 14:59:38 UTC | #2

gm, interesting thoughts here! just continuing this chat from the dm's

my initial reaction is that the multi-dimension *maps* could be overly complex and the complexity could actually be obscuring the 'thing' that's trying to be found/plotted/discovered.

if a real map contained every possible factor all at the same time while you were trying to navigate, would that map still be useful? running with the cartography/navigation concept, sometimes I only care about altitude if I'm walking but not driving.. sometimes I care about directness if i'm driving but not going for a stroll. So the multi-dimension map at some point is potentially no longer useful, and what may be more useful is pairing relevant criteria together - it may be that value lies not at the intersection between 5 dimensions, but actually inbetween the 2 or 3 dimensions that haven't been connected or put next to each other before

i wonder what would come from combining 2x or 3x criteria and looking at what the extremes of those combinations look like. No idea how to properly do this but would be cool to plot those orgs (and others in the space!) on 2/3 axis based even on the criteria you provided. 

**Have just generated the below on chatgpt as an example** ([chat here](https://chat.openai.com/share/f0522664-8567-452b-b507-9873168a6e4c))

| Criteria | Point 1 (Lowest) | Point 2 | Point 3 | Point 4 (Highest) |
| --- | --- | --- | --- | --- |
| Mature projects vs seed projects | Seed Projects | Early Stage | Growth Stage | Mature Projects |
| Effective or not | Ineffective | Somewhat Effective | Effective | Highly Effective |
| Return expected vs not | No Return | Possible Return | Expected Return | High Return |
| Virality vs not | Non-viral | Slightly Viral | Viral | Highly Viral |
| Impact Attestations Dependency | Not Dependent | Slightly Dependent | Dependent | Fully Dependent |
| Oracle-limited or not? | Not Oracle-limited | Somewhat Limited | Limited | Fully Limited |
| Credibly neutral vs not | Not Neutral | Somewhat Neutral | Neutral | Fully Neutral |
| Desktop vs mobile | Desktop-Only | Desktop-Preferred | Mobile-Preferred | Mobile-Only |
| Built into social media? (emergent) | Standalone | Slightly Integrated | Integrated | Fully Integrated |
| Massively multiplayer? | Not Scalable | Slightly Scalable | Scalable | Highly Scalable |
| Assets fungibility | Non-Fungible | Mostly Non-Fungible | Mostly Fungible | Fungible |
| Can it be built on top of Allo? | Not Applicable | Possible | Applicable | Fully Integrated |
| Can it be built on top of Passport? | No Benefit | Slight Benefit | Beneficial | Highly Beneficial |
| Funding: Continuous/recurring vs fickle | Fickle | Somewhat Stable | Stable | Highly Stable |

| Organizations / Groups | Mature Projects | Effective or Not | Return Expected | Virality | Impact Attestations Dependency | Oracle-limited | Credibly Neutral | Desktop vs Mobile | Built into Social Media | Massively Multiplayer | Assets Fungibility | Built on Allo | Built on Passport | Funding Stability |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ethereum Foundation | Mature Projects | Highly Effective | No Return | Non-viral | Not Dependent | Not Limited | Fully Neutral | Desktop-Preferred | Standalone | Highly Scalable | Fungible | Possible | Beneficial | Highly Stable |
| Ethereum Community Fund | Growth Stage | Effective | Possible Return | Viral | Dependent | Limited | Neutral | Desktop-Preferred | Slightly Integrated | Scalable | Mostly Fungible | Applicable | Highly Beneficial | Stable |
| Gitcoin | Early Stage | Highly Effective | No Return | Highly Viral | Fully Dependent | Limited | Fully Neutral | Mobile-Preferred | Fully Integrated | Highly Scalable | Non-Fungible | Fully Integrated | Highly Beneficial | Fickle |
| ConsenSys | Mature Projects | Highly Effective | High Return | Slightly Viral | Not Dependent | Not Limited | Somewhat Neutral | Desktop-Only | Standalone | Scalable | Fungible | Possible | Beneficial | Stable |



So you could see what happens and where orgs sit when you combine 'Credibly neutral' x 'massively multiplayer' or 'virality' x 'maturity' x 'assets fungibility'

-------------------------

owocki | 2023-11-24 15:31:54 UTC | #3

[quote="harryeastham, post:2, topic:17174"]
my initial reaction is that the multi-dimension *maps* could be overly complex and the complexity could actually be obscuring the ‘thing’ that’s trying to be found/plotted/discovered.
[/quote]

yeah thats definitely true.  its something @ccerv1 also mentioned.

I think when building market maps we should stick to 3d or less, but it’s useful to know higher dimensions are out there if we want to pop into them and re-index on other dimensions.

alternatively, another way of grokking the higher dimensional spaces could be star graphs.

here is one you and i have been jamming on in DMs
![Screenshot 2023-11-24 at 8.30.38 AM|672x500](upload://io8u4aRuLdFJZ9vAu9GRHcpheuL.jpeg)

-------------------------

owocki | 2023-11-24 15:49:20 UTC | #4

Responding to a few of my own prompts here:

[quote="owocki, post:1, topic:17174"]
* Map out spectrum of public goods funding from cradle-to-grave (or cradle-to-unicorn) for each project.
[/quote]

Here is the spectrum of cradle-to-grave funding for web3 projects:

![Screenshot 2023-11-24 at 8.39.55 AM|661x499, 40%](upload://xjR6KqazMqSoOgtwIBqYnqKsL4i.png)

(thanks @ccerv1 for stimulating these thoughts) There is maybe a trough of dissillusionment between 

-  pure prospective funding minimizes the risk of projects not getting off the ground due to lack of funding, but has high uncertainty when it comes to achieving impact (most startups die, etc)
- pure retro funding does the inverse

Some would say that this is what VC does, ie, inject different amounts of funding following the famous startup curve (peak of inflated expectations, trough of disillusionment, etc)

But I think there's some very interesting about experimenting on those dimensions, eg, Gitcoin could evolve to be perfect for projects in the trough of disillusionment phase.

There may also be an opportunity for projects to start issuing impact certificates and creating a web of trust that helps create data about which projects are ngmi vs wagmi.. and helps cross that cham too.

![Screenshot 2023-11-24 at 8.44.29 AM|690x406, 50%](upload://v3pQj3udkB8AeQYYZYEkWQ6sbui.png)


[quote="owocki, post:1, topic:17174"]
* What would Gitcoin Grants but for private goods look like? Eg you get gov tokens when you donate? Would it detract from Gitcoin’s mission or be a valuable extension of Allo/Grants Stack?
[/quote]

Perhaps another thing that could help more projects cross this chasm is making more people angel investors, in a more crypto native way...

![Screenshot 2023-11-24 at 8.45.04 AM|624x500, 50%](upload://47jzVdZ4a1HcX1R9X6o9n0Xud4Z.png)

-------------------------

owocki | 2023-11-28 22:19:36 UTC | #5

[quote="owocki, post:1, topic:17174"]
* Map out spectrum of public goods funding from cradle-to-grave (or cradle-to-unicorn) for each project.
[/quote]

[OP delivers!  ](https://gov.gitcoin.co/t/cradle-to-unicorn-public-goods-funding/17189)

-------------------------

sophia | 2023-12-07 02:34:19 UTC | #6

[quote="owocki, post:4, topic:17174"]
Perhaps another thing that could help more projects cross this chasm is making more people angel investors, in a more crypto native way…
[/quote]

Been thinking a lot about this, especially because of your twitter comment about pgf mechanisms becoming more active in economically exothermic areas. If we want real money to fund public goods, we can't rely solely on grants & donations forever... 

While the entire point of PGF infrastructure is that traditional venture models don't work here, those models also imply that acquisitions and IPOs are the main exit strategies. However, if retroPGF is a viable "exit" strategy, it can open a whole new pathway for early-stage and angel investors. Instead of donors, we could have investors actively speculating on the future impact of a project.

For this to happen, this assumes "impact equals profit." The main place (to my knowledge) where this is occurring is in Optimism retroPGF. But here, they have their own definitions for impact and governance structures that guide what gets funded. 

Perhaps, more tooling/research to figure out what type of impact metrics retroactive funders are willing to pay for could enable more marketplaces for retroactive funding projects/investments... ?

-------------------------

owocki | 2023-12-07 12:54:45 UTC | #7

[quote="sophia, post:6, topic:17174"]
Perhaps, more tooling/research to figure out what type of impact metrics retroactive funders are willing to pay for could enable more marketplaces for retroactive funding projects/investments… ?
[/quote]

im planning a whole greenpill season on this :) 5-7 episodes, recording next week.  hopefullly dropping by the new year.

-------------------------
