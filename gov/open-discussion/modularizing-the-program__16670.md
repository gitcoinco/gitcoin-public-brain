---
id: 16670
title: "Modularizing the Program"
slug: modularizing-the-program
category: open-discussion
url: https://gov.gitcoin.co/t/modularizing-the-program/16670
created_at: 2023-10-04T03:09:26.475Z
last_posted_at: 2023-10-21T04:18:13.956Z
posts_count: 10
views: 4964
like_count: 52
---

# Modularizing the Program

<https://gov.gitcoin.co/t/modularizing-the-program/16670>
owocki | 2023-10-04 03:23:10 UTC | #1

# tldr

the gitcoin grants program (or "the program" for short) = the quarterly gitcoin grants rounds (as opposed to the self-service rounds run by other communities)

in this post, i propose that we further modularize gitcoin by building (1) subbrands for each program & (2) creating always-on matching pools for each round/program.

why do this?
1. to make it clear which parts of the network are credibly neutral vs not.
2. to allow different programs/subbrands to have different (and sometimes incongruent) messaging
3. to create more ownership and accountability around each program.
4. to create more targeted/niche campaigns for different audiences.

# post body

the controversies of the last grants rounds (DEI/shell) did a lot of damage to gitcoin's legitimacy in the eyes of ethereum communities.  

i would like to propose a solution to this problem that is one part optical and one part foundational.

i think the programs should be treated more modularly, namely that means that:
1. we should have separate matching pools for each round we run a la climate.gitcoin.eth, eth_infra.gitcoin.eth, eth_oss.gitcoin.eth, eth_community.gitcoin.eth, etc..
2. we should extend our current house of brands + have seperate brands for each program we run.
3. each program should have a clear DRI (directly responsible individual) + KPIs measuring their success.

why have separate matching pools for each round?
1. allow donations to a specific round, instead of pooling donations only to the main pool
2. start to build aqueducts of long term sustainable funding into specific pools.
3. start to catch up to other public goods funding projects that have more of a narrow focus with programs that also have their own narrow focus. 

why have separate brands for each program?  

0. put the internally bootstrapped programs on similar footing with external programs (like [@arbitrumgrants](https://twitter.com/arbitrumgrants))
1. modularize ownership over a program's identity/values/comms/execution to the people who run that program.
2. educate our community on what the different parts of gitcoin are, earning value towards a common understanding outside-in of what gitcoin looks like when it's fully decentralized 
3. build more targeted/niche marketing campaigns for different audiences.
4. separate out credibly neutral parts of the gitcoin ecosystem (grants stack, allo protocol, passport) from the non credibly neutral parts of the ecosystem (climate program, eth public goods program).

*(here is a map of gitcoin's products and their place on the credibly neutral spectrum, thanks @Harryeastham ! )*
![Frame 1000002359|690x388](upload://niJ6GzwOW63hdRZdwr7k9DWLnBl.png)


beyond these specific benefits, modularization has broad benefits as an architecture.

by architecting gitcoin around modularity, we follow the ethereum architecture of modularity.  [i believe that protocols built on top of ethereum should inherit ethereum values.](https://twitter.com/owocki/status/1699910032568226127).  it's good for comprehension, good for recruitment, and just generally good vibes.

by architecting the [topology of gitcoin](https://gov.gitcoin.co/t/gitcoin-dao-topology/16668) in the style of the unix philosophy of small groups that do one thing and do them well but can interface with other groups, we create a scalable, repeatable, and accountable structure for longer term success.  

these delineated identities/modular sets of accountability's would be a break from the past where there has been these giant workstreams with million $$ budgets and unclear accountabilites.  these large monolithic groups have traditionally made it hard for ppl to know whos responsible for what / to be responsible for outcomes.

> you can have as many modules as you have true leaders in the organization. give them small contained scoped. - ele from radicle, when i asked him about modular team architectures.

a priori, we know that public goods are relative to the values of the communities they serve. emperically, we know that the internet is super tribal. it follows that there WILL be another shell/DEI style blow up if we don't modularize the protocols now. its not a matter of if, its a matter of when. we have no choice but to untangle the main gitcoin brand from the program, other than risking the main brand unnecessarily.  **we should do this before GG19.**

we have lost out on tens of millions of $$$ in donations in market to projects like other eth public goods projects that have built strong brands around funding of specific causes (like eth protocol devlopment) and a better/simpler mechanism for distributing those funds.  don't get me wrong, i'm very happy for the protocol devs that are benefitting from this, but i'm sad gitcoin isn't a player here anymore. in a counterfactual world in which we were investing back in our roots/in oss with basic setup like a separate multisig/brand/fundraising/messaging for the eth infra program, that may not have happened.

gitcoin is investing hundreds of thousands of $$$ into the programs from a staffing perspective, and we've seen millions$$$ of brand damage to the gitcoin brand in the last two seasons due to the missteps on the programs. the overhead of architecting the brands/communications right is not that high relative to the costs of doing it wrong.

i believe that the sooner we begin to build separate brands for the programs the better.  it will take 6-9 months to inflate these brands followings to a place where they are substantial, but we can bootstrap them with my twitter account, the main gitcoin twitter account, and the twitter accounts of our partners.

(thanks to @MathildaDV @krrisis @M0nkeyFl0wer @Sov @alexalombardo for feedback on many of these ideas)

-------------------------

quaylawn | 2023-10-04 16:33:22 UTC | #2

I think modular team architectures sound good and I do think it would be valuable to the brand, I'm just not sure it is the right time. From a holistic comms perspective, this is not how I would recommend managing brand equity or reputation in the long term.

Gitcoin is already super modular ( :wink: ) and becoming even more modular through sub-brands ahead of GG19 feels more like fragmentation than decentralization. This is before we take into account the resourcing demands of managing another account, communicating that to our people effectively, and keeping all of the other many balls in the air.

What I would prefer is if we could action the aggregated feedback received from the community with regard to the recent controversies and gradually move towards your suggestion @owocki. I don't think it is a bad idea at all, and I'd love to get behind it at some stage, I just think there are more steps that we need to take as a unified brand before we further modularize.

-------------------------

owocki | 2023-10-04 17:26:18 UTC | #3

theres been millions$$$ of brand damage done by the shell/dei controversies. so i have a hard time understanding the push back to spending a few hundred dollars here and there to manage a seperate twitter account.

i'm curious to see if anyone will present an alternative plan for how to deal with the inevitable next shell/dei style controversy.   we can't be caught flat footed again, the gitcoin brand is one of the primary assets we still have.

-------------------------

connor | 2023-10-05 06:08:49 UTC | #4

I think this general direction is good - we should move towards more decentralization, increase community engagement, and divest from central points of failure. However, I do think as proposed it may be too hard a correction made too quickly, which could ultimately lead to the failure (either slowly or abruptly) of the Gitcoin Grants Program everyone has grown accustomed to over the last 4.5 years. 

I do think a lot of core community members and Gitcoin OGs rely on recurring grant funding round over round for their projects. And I do think it's valuable to engage the community through governance to help decide on the rounds we run, how they are funded and structured, what eligibility looks like, etc. I also think there's something special about having some recurring event where many workstreams come together and collaborate on to make happen (ie. Allo shipping new features to experiment with, Passport testing different scoring metrics, PGF fundraising and operating, marketing preparing long term promotional plans + iterating each time, community rallying to both apply with grants and to donate, etc etc). There's power in the network effects and it brings the DAO together in a lot of ways

I still think there's a lot of overlap between the 3 core rounds. For example, if we hold onto the rule of a grant only being allowed in 1 of the 3, we need to communicate and compare. Having 3 unique teams doing the same work but in a silo could end up redundant and a waste of resources. They're certainly easier and more effective to market together (imo). I don't really see the need to brand each one uniquely. Does each round's team need to hire their own marketing team, designers, and support personnel?

> 1. allow donations to a specific round, instead of pooling donations only to the main pool

We do already do this (although they do share a multisig, funds are earmarked for specific rounds)

> 2. start to build aqueducts of long term sustainable funding into specific pools.

We do already *try to do this, when there is demand

> 3. start to catch up to other public goods funding projects that have more of a narrow focus with programs that also have their own narrow focus.

We definitely can do much better here. But I think it's sort of a separate (but parallel) issue, with it's own causes, that may or may not be addresses by this proposal

> theres been millions$$$ of brand damage done by the shell/dei controversies

I've seen you say this in a few places now - I would not be surprised at all if it's true, but I'm curious as to how you're coming to that conclusion / what data you're looking at

Overall I do want each of our rounds to grow, prosper, further decentralize, have more community involvement, etc. But I'm not sure that making each round have its own Twitter account ,write its own blog posts, and exist in its own vacuum is the way to achieve that. I am open to experimenting and agree we really need to avoid or at least minimize the polarizing controversies of prior rounds going forward. But I do still believe the Gitcoin Grant Program that has evolved from GR1 to today is a core Pillar of the project and our community, and dogfooding our own new tech to learn/show by doing, is extremely powerful

-------------------------

owocki | 2023-10-05 13:51:29 UTC | #5



[quote="connor, post:4, topic:16670"]
I still think there’s a lot of overlap between the 3 core rounds.
[/quote]

IIRC we agreed to stop calling them core rounds and instead decided to call them program rounds, no?


[quote="connor, post:4, topic:16670"]
I’ve seen you say this in a few places now - I would not be surprised at all if it’s true, but I’m curious as to how you’re coming to that conclusion / what data you’re looking at
[/quote]

This is admittedly a hard to quantify exercise, but where's where I'd start: Look at the impression counts of the tweets complaining about us, the news coverage of it, the decrease in donations to the matching pools in the last couple rounds, and the drop in Gitcoin's treasury value during the controversies.

[quote="connor, post:4, topic:16670"]
We do already do this (although they do share a multisig, funds are earmarked for specific rounds)
[/quote]

So people have to trust that someone is tracking it correctly?  Socialware only goes so far (especially when there is poor or opaque record keeping)  Seems like a more trustware based approached where one could see on chain the funds going to the correct places is more inline with ecosystem values.

[quote="connor, post:4, topic:16670"]
I am open to experimenting and agree we really need to avoid or at least minimize the polarizing controversies of prior rounds going forward
[/quote]

[quote="connor, post:4, topic:16670"]
I don’t really see the need to brand each one uniquely
[/quote]

I think the controversies are inevitable, as the world is polarized and public goods are relative to the communities they serve.  Just like an experienced skiier doesnt focus so much on not falling, but on bouncing back after a fall...  We should focus on bouncing back from the controversies when they happen, and on limiting damage to the main brand.   Modularizing the ecosystem and building up subbrands accomplishes this bc it educates the community on the diff between the credibly neutral protocols, gitcoin (which is an ecosystem now), and the opinionated programs that occur within/around that ecosystem.

[quote="connor, post:4, topic:16670"]
Having 3 unique teams doing the same work but in a silo could end up redundant and a waste of resources
[/quote]

I don't think this is proposed anywhere in my OP.

[quote="connor, post:4, topic:16670"]
Does each round’s team need to hire their own marketing team, designers, and support personnel?
[/quote]

IMO this line of questioning just shows how bloated Gitcoin workstreams have gotten.  We're just assuming giant monolithic teams, and that it should cost $1m in net-new staffing to run a round, when it's just not true.  You can run a team self-service for 10x, 100x, or 1000x less.  We've invested tens of millions of $$ in making a product that can be more self-service and less resource intensive, let's start adopting that mindset.

Yes, the program contains major rounds, and bc each is larger than the median round, it will cost more than the median round.   So to directly answer your question, each program can rely on shared resources.  The point of [Unix-philosophy style modularity](https://twitter.com/owocki/status/1709274077360214111) is that  each team does one thing and does it well, and is made to be interoperable with other teams..  To say that teams work in silos just bc they have seperate brands is to misinterpret modularity.

[quote="connor, post:4, topic:16670"]
> 2. start to build aqueducts of long term sustainable funding into specific pools.

We do already *try to do this, when there is demand
[/quote]

Given protocol guild's ability to raise tens of millions of $$$ for eth infra public goods funding, I think there is clearly demand here.  I'm happy for protocol guild's impact on eth core infra, but I'm saddened that it seems to me that our offering is not as competitive anymore.

-------------------------

raybankless | 2023-10-13 13:20:32 UTC | #6

Thank you Kevin, i am not so familiar with Gitcoin team structure but what you are proposing here offers a good modular approach that ties together i think. 

The teams that are operating rounds can start their own QF models, either rounds or may be ultimately streams. 

[quote="owocki, post:1, topic:16670"]
the controversies of the last grants rounds (DEI/shell) did a lot of damage to gitcoin’s legitimacy in the eyes of ethereum communities.
[/quote]
I saw that as a win for greenpilling a corp. Seems like there is less people than i thought, that thinks in the same way.

for that reason, a separation of the Gitcoin brand from any other brand would help with the problem. And gives Gitcoin the freedom to choose which names to come together with and when.

[quote="owocki, post:1, topic:16670"]
(2) creating always-on matching pools for each round/program.
[/quote]
WEN? just WEN? Thinking of the two local chapters i'm involved in, getting into list of the teams for an AO-Matching pool would be a good goal to work towards.

-------------------------

krrisis | 2023-10-20 18:17:11 UTC | #7

I waited some time to respond here, hope this is still relevant/useful. 

No strong opinions on the separate matching pools, this definitely sounds like a great idea, might be good to formalize and make this externally visible as you suggest!

Overall, I deeply agree that we need and can avoid future controversies like Shell & DEI, but I don't think  different social presences for all rounds are the solution, although I do support this gradual move for the community rounds. 

Imo the main issue here for both of these PR tragedies is - more than anything else - how tough it it is to organize **streamlined coordination within a DAO**. Wrt to Shell there is 6 months of internal history and buildup here - it would take me a few hours to write down what I personally saw as influential factors, noting I've only seen a tiny part of this puzzle. :slight_smile: 
In any case to me these internal failures were at the root of all this, leading to external symptoms of opacity and inconsistent communication. A lot of work in progress here, beautiful to see all the strategic documents on this forum. 

When it comes to communication strategy - what this post is about - I agree we need more credible neutrality, I just believe there's other paths to achieve this. 

Imo we have not been leveraging enough (yet), what the differentiation is **between the program rounds (managed by gitcoin) and the community rounds (managed independently, run on grants stack)**. To me this is key, rather than to distance the brand from **all** the rounds, whether they are run by Gitcoin or not. [Having clear terms now](https://gov.gitcoin.co/t/vocabulary-gitcoin-grants-programs-rounds-etc/16773) to differentiate **gitcoin-run vs community** will definitely help a lot, so thank you for driving this. 

This is actually already quite the step, small but crucial and impactful. People in general are barely aware that this distinction exists, to them rounds on Gitcoin = Gitcoin, and this needs to change.

This is already in progress and quite the task but a beautiful opportunity to win back hearts and market share.

[quote="owocki, post:3, topic:16670"]
i’m curious to see if anyone will present an alternative plan for how to deal with the inevitable next shell/dei style controversy.
[/quote]

My plan would be 

1) **continue to improve internal coordination** (too much happening to list here, but things are looking well, including [the updated essential intents](https://gov.gitcoin.co/t/update-gitcoin-s-ratified-essential-intents-2023-2024-and-a-recap-of-our-successes/16818) as a northstar.) 

2) **associate the Gitcoin main twitter account even more with the program rounds**, rather than take away what defines it (as @connor goes into a bit). If we are serious about community being one of the essential intents, it feels inconsistent and strategically unwise to make our main account with 200K followers into a soulless and neutral voice that only retweets other accounts which are starting from scratch. On top of it, having separate accounts, at least for Gitcoin-run programs, will dilute the impact and connection with our community (aka existing user base). 

3) support community round operators (strategically and financially) to build a social media presence for their **community rounds**, I think this can be done gradually, would echo much of what @quaylawn wrote. I would only do this once a continuous social media presence with a dedicated team can be guaranteed.

4) focus the existing (limited) resources on building out the presence of our key **product accounts**. Grants Stack (our platform) and Passport (our identity solution) being the underlying (mostly) neutral solutions Gitcoin (the DAO) offers to its user base. Gitcoin's credible neutrality is reinforced on this level. We emphasize we have a platform (Grants Stack) and a protocol (Allo) that can be used independently by our community.  
*(Note: I would discontinue the Allo Protocol twitter account, as it dilutes resources, Grants Stack can mention the protocol when relevant)*

--

As mentioned in a comment on @Sov's GG19 [strategy outline](https://gov.gitcoin.co/t/gg19-outline-and-strategy/16682) draft I believe Gitcoin can avoid future controversies by following the above strategy and show the world through its main account that it is the 

1) the umbrella brand
2) owner of the program rounds
3) supporter of community rounds

Next to original tweets on the program rounds, both product & community accounts get retweeted often by Gitcoin's main account, which emphasize this positioning. 

--

**What else can we do to explicitly avoid future damage to our brand**? 

1) **Linking key beliefs/values to our program**. 

This should not be too difficult: we already talk about these very often and they return (to some extent) in the updated essential intents: the importance of transparency, to build **open source**, to support public goods and key **infrastructure**, importance of **education**, honoring the will of our **community**. 

This will help to undo the damage which happened during the preceding rounds or at least create a consistent tone of voice. 

2) **Crisis communication and isolation of potential controversy.** 

Random example, Amazon runs a community round on Grants Stack to support individuals who are breaking up unions. 

If such a controversial round pops up and part of our 'existing user base' is not happy, Gitcoin (the DAO) can make the decision this is a community round which Gitcoin (the Twitter account) should not retweet or endorse. This also makes sense as we honor the will of our community. (values/beliefs)

If controversy erupts and communication is necessary, the Grants Stack Twitter account will release a statement, which Gitcoin the main account will then retweet, with additional context if needed, helping to emphasize the distinction to our user base that 
1) Grants Stack is our permissionless platform and 
2) Gitcoin is and remains the overarching umbrella brand, which communicates in times of crisis.

Happy to chat more!

-------------------------

quaylawn | 2023-10-20 20:49:35 UTC | #8

[quote="krrisis, post:7, topic:16670"]
2. **Crisis communication and isolation of potential controversy.**

Random example, Amazon runs a community round on Grants Stack to support individuals who are breaking up unions.

If such a controversial round pops up and part of our ‘existing user base’ is not happy, Gitcoin (the DAO) can make the decision this is a community round which Gitcoin (the Twitter account) should not retweet or endorse. This also makes sense as we honor the will of our community. (values/beliefs)

If controversy erupts and communication is necessary, the Grants Stack Twitter account will release a statement, which Gitcoin the main account will then retweet, with additional context if needed, helping to emphasize the distinction to our user base that

1. Grants Stack is our permissionless platform and
2. Gitcoin is and remains the overarching umbrella brand, which communicates in times of crisis.
[/quote]

Thank you for sharing this :slight_smile:

-------------------------

owocki | 2023-10-21 03:59:23 UTC | #9

Thanks for the thoughtful thread Kris.

I agree with a lot of you said and I think you are right in a lot of places.  I with the tangible steps you recommend taking are directionally correct.   Highlighting a few places where I see daylight between us that maybe we can work out next time we chat live!

[quote="krrisis, post:7, topic:16670"]
but I don’t think different social presences for all rounds are the solution
[/quote]

Just for clarity - I don't either.  I think that templatizing & modularizing the programs (of which there being different social presences is 1 of many downstream effects) is the solution.

[quote="krrisis, post:7, topic:16670"]
Imo the main issue here for both of these PR tragedies is - more than anything else - how tough it it is to organize **streamlined coordination within a DAO**.
[/quote]

I just dont think that some mythic "streamlined coordinated" state will ever happen.  I've been at half a dozen startups in my 15 years in the game and everyone always points at it but it never seems to happen.  It's just this perfect state that is infinitely on the horizon in our dreams but we never achieve it because humans are imperfect and as soon as the retrospective is done we all have 99 other priorities to think about besides our little perfect coordination fantasy. 

That's not to say that we shouldnt try to incrementally improve our coordination.   We should. I'm just saying lets not hold on to this perfect fantasy + lets do other stuff in the meantime to solve the problems too.  I guess I just think we should be protopian (gets better every quarter) as opposed to utopian (will be perfect in some eternally future state) in our approach.

-------------------------

owocki | 2023-10-23 16:00:21 UTC | #10

[quote="krrisis, post:7, topic:16670"]
**What else can we do to explicitly avoid future damage to our brand**?
[/quote]

[quote="krrisis, post:7, topic:16670"]
My plan would be
[/quote]


I think these are all great steps to take.

But I also think that many of those proposed actions are defensive in posture.  Or internal.  IMO we need to start going on offense externally.  

One thing I want to add to the top of this list of what to do is **Start Winning in Market**

I think that one reason Shell hit Gitcoin's psyche so hard was that times were tough at Gitcoin.  We're in between what used to make Gitcoin legitimate last cycle + what's going to make Gitcoin legitimate in the future.  The burn is high according to some measures and future financial longevity is a worry.  Vitaliks 2020 endorsements of Gitcoin are fading from memory + cGrants momentum 2019-2021 is disipating.   The new Gitcoin products have early traction, but have not yet hit growth scale yet.  We're kind of in the messy middle still.  I probably didn't help and I just made things worse (sorry about that).

The reason I want to modularize the programs is partially defensive yes.  But a big reason I want to modularize the programs is offensive.

The old PGF was giant + expensive + monolithic.  It had to use a complicated unmaintainable product to run Gitcoin Grants Program.  It had a lot of turnover in it's leadership and didn't have good accounting.  It invested a lot of $$ into things that didnt go anywhere or didnt provide a ROI (like pgDAO).  It lost in market to Optimism/Protocol Guild.  We couldnt grow + win in market if we wanted to.  (Nor was it really a priority for the PGF team while it was a bull market + the product was still being rebuilt from ground up)

The new PGF is using a new product that is relatively simple + has self serve capabilities.  So now we can focus more on teaching people to fish than fishing ourselves.    

When the programs are modular, simple, and templatized, we have strong accountability.  We can scale Gitcoin's adoption in market by adding strong leaders. We will be able to scale from 1 program to 100s of programs by just combining 1 great leader to operate as round manager to 1 funding source, rinse and repeat.  

These leaders could be held accountable to KPIS (how much $$ did they raise? how many contributions did they drive?  whats their community NPS?).  These leaders would then use social media to drive results not *"idk, because Owocki said so??? i dont really get it either"*, but because they are doing it to reach their goals

I think that getting really good at creating/managing/scaling the modular programs are how Gitcoin Grants Stack starts to scale it's impact in market.  Thats an offensive play.  

Momentum begets momentum.  I am hoping that this is one area there could be a groundswell of momentum created.

Then when the next Shell/Iran Grant Shutdown/AKITA/Chris Blec tweet/DEI Round controversy/whatever is next comes around, it won't get to us as much cause we'll be crushing it in market.

-------------------------
