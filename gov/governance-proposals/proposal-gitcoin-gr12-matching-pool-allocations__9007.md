---
id: 9007
title: "[Proposal] Gitcoin GR12 Matching Pool Allocations"
slug: proposal-gitcoin-gr12-matching-pool-allocations
category: governance-proposals
url: https://gov.gitcoin.co/t/proposal-gitcoin-gr12-matching-pool-allocations/9007
created_at: 2021-11-11T16:07:57.052Z
last_posted_at: 2021-11-29T14:40:38.596Z
posts_count: 26
views: 9256
like_count: 55
---

# [Proposal] Gitcoin GR12 Matching Pool Allocations

<https://gov.gitcoin.co/t/proposal-gitcoin-gr12-matching-pool-allocations/9007>
annika | 2021-11-11 16:07:57 UTC | #1

# Summary

This proposal looks to discuss and finalize how funding allocations for the Gitcoin Grants Round 12 Matching Pool are distributed and how to use categories (if at all). After previous successful Grants Rounds, this proposal aims to continue community-owned decision making.

# Abstract

Previously, the distribution of the Matching Pool to different Grants categories had been handled by the Gitcoin Core team (rounds 1-5), and later in consultation with the Funders League (rounds 6-9). Round 10 & 11’s distribution was based on GTC governance and we look to continue this with Grants Round 12 (GR12) to continue to reinforce the mission of decentralization.

This is also the first round where operations and execution of the round will happen by a DAO workstream - the Public Goods Funding workstream (with Gitcoin’s core team supporting).

During the discussion of [Grants Round 11](https://gov.gitcoin.co/t/gitcoin-round-11-matching-pool-allocations/8386) (GR11), we saw feedback that some folks [don’t like](https://gov.gitcoin.co/t/gitcoin-round-11-matching-pool-allocations/8386/10) regional rounds, while others feel we [should continue](https://gov.gitcoin.co/t/gitcoin-round-11-matching-pool-allocations/8386/12) to have them, but instead [have only a single region](https://gov.gitcoin.co/t/gitcoin-round-11-matching-pool-allocations/8386/13) and focus on highlighting those grants. It was also noted that having a grant receive ~65% of the matching contribution amount for a category round was [not good](https://gov.gitcoin.co/t/gitcoin-round-11-matching-pool-allocations/8386/15), and some folks were hoping to see an environment category [get created](https://gov.gitcoin.co/t/gitcoin-round-11-matching-pool-allocations/8386/20).

*Disclaimer: Much of this feedback was primarily based on individual community members’ sentiment, and there has not yet been deep analysis on the impact of making these changes.*

# Proposal

Gitcoin has historically utilized categories, based on Grant types, to determine matching pool allocations based on a percentage of the overall matching pool fund during Grant Rounds. During the GR11 Finale Event this overall strategy was questioned by Vitalik Buterin, the argument being Quadratic Funding should be just as effective during Grant Rounds using no categories*.

In GR11, the $800k “main” matching pool was allocated as follows across 7 category pools:

* Infrastructure: 25%
* Dapp Tech: 25%
* Community: 20%
* NFT Tech: 10%
* dGov: 7.5%
* Africa: 7.5%
* Latin America: 5%

Gitcoin Holdings also worked with three other communities to introduce ecosystem rounds (“side rounds”) to GR11 which featured Uniswap Grants Program, OpenGSN (funding public goods retroactively), and Gitcoin building Gitcoin, which collectively brought another $150k matching to eligible grants. Finally, CommonStack donated another $15k to the Latin America category during the round bringing the total matching available to Grants Round 11 to $965k.

During GR12, the Public Goods Funding workstream wants to test Vitalik’s theory that Quadratic Funding should be as effective at allocating funds as allocation via categories. By doing away with specific grant categories and having all grants listed together, we hope to simplify and decentralize matching. This is a radical change in how we’ve historically set matching funds for grants’ matching pools, but a challenge we believe will help to better understand how to best implement Quadratic Funding.

Furthermore, Gitcoin Holdings will be publishing a deep-analysis comparing our historic category-driven grant round over the non-category GR12 results to see how these two approaches differ and if there are any inherent benefits/drawbacks.

**Assuming there is a cap on the amount a single Grant can receive in matching, relative to the matching pool total (see GR12 Main Pool section below)*

There are two ways we might implement this: Option 1 being a single pool experiment, and Option 2 being having the Stewards & community propose an alternative.

## Option 1: Single Pool Experiment

Though tags will still function as per usual on the Gitcoin front-end when navigating and searching for grants on the website, there will no longer be specific categories for matching pool allocation.

The “main” matching pool would be distributed based on the following breakdown. These allocations are proposed by the Public Goods Funding workstream and are based on the [observed results](https://gitcoin.co/blog/gitcoin-grants-round-11-governance-brief/) in GR11.

#### Grants Round 12 Main Pool

The GR12 main pool will be a single matching pool fund/distribution of $1,000,000 in matching for the round. No individual grant’s matching contribution amount shall exceed 2.5% of the overall matching pool fund (i.e., $25k).

#### Thematic Rounds

In addition to the main pool, Gitcoin DAO will leverage the multisig as a pass-through for thematic rounds, funded by external sponsors for clear sets of global public goods. As part of our work with [Other Internet](https://otherinter.net/research/positive-sum-worlds/), we received a wide range of submissions about [new](https://gitcoin.co/blog/seeking-a-new-kind-of-public-good-closing-the-loop/) [types](https://gitcoin.co/blog/seeking-a-new-kind-of-public-good-honorable-mentions/) of public goods we should consider funding beyond just web3. In GR12, we will be experimenting with rounds on climate change, tech advocacy, and longevity with *net new* funds.

#### Ecosystem Rounds

Finally, the DAO will operate ecosystem rounds for groups like Forefront, Polygon, and Uniswap, as they have continued to do in the past. These funds will *not* interact with the multisig.

In summary, the goal of the single “main” matching pool experiment is to:

* Continue to follow the pace of our community’s contributions in determining matching pool allocation amount. (GR11 brought $1.5M in contributions from the community, we would advocate we should raise the matching pool to $1M from $800k to better follow the community's lead).
* Gather real-world data to learn whether multiple sub-categories or a single category provides better fund allocation as it relates to Quadratic Funding to grant owners.
* Provide an in-depth post-analysis comparing these two approaches for future CLR/QF mechanisms.

## Option 2: Alternative Community-led Proposal

Gitcoin Stewards and the wider community decide on a new matching breakdown and propose such. We encourage any Steward or community member to submit their own matching pool breakdown if there are concerns on the single pool experiment!

Please submit your proposal to the forum this week so that the community has sufficient time to vote before the round begins!

# Vote

Once we have feedback on both this and other proposals, the Public Goods Funding workstream will gather all formal proposals and submit a Snapshot vote to decide which to move forward with.

Please do not submit a snapshot vote for your proposal specifically! This just adds confusion and makes it harder for the community’s voice to be heard effectively.

-------------------------

lefterisjp | 2021-11-12 16:23:02 UTC | #2

Hey @annika,

Thank you for the proposal. I have a very fundamental concern with the single pool approach. Won't that really skew the result towards the most popular grants of all categories? In the past the categories at least allowed lesser known grants in a category to get some matching. With this approach it sounds as if that will no longer be possible.

> No individual grant’s matching contribution amount shall exceed 2.5% of the overall matching pool fund (i.e., $25k).

That would probably help, but still not really solve the concern I have above. Also why not discuss here what the max matching for a grant should be? 2.5% sounds okay~ish but perhaps we can discuss/tweak the parameters if someone else in the community has any useful insight.

With 2.5%, in the worst case scenario we would have ~40 top/most popular grants take the most matching funds.

-------------------------

socal434 | 2021-11-12 17:39:39 UTC | #3

@lefterisjp  Please correct me if I am wrong but isn't the whole mechanism of quadratic matching going to ensure that less popular grants will get some matching funds? The way I thought it works is that the as a grant gets more and more donations the ratio of matching funds is decreased for the later grants relative to the early grants. For example, the first grant gets 100% matching but the 1000th grant only gets 1% matching. Maybe I am misunderstanding the concept though.

-------------------------

tjayrush | 2021-11-12 17:47:48 UTC | #4

I think Lefteris is almost certainly right that not having categories will skew the results to the most popular grants (and those with the largest communities), but this is the whole purpose of quadratic funding.

One of the outcomes of this, I hope, is that we may realize that instead of dumping all the grant types into a single round, we have staggard rounds.

So there might be a round just for infrastructure, just for media, just for frontend. You get the best of both worlds - no categorization but yes categorization. You would probably also get different matching contributors interested in different rounds. Some would want to fund matches for media, some would want to fund matches for infrastructure. Having a single overarching round disallows matching funders from deciding what's important to them as the entire decision making is in the hands of the donors.

-------------------------

unvetica.eth | 2021-11-12 18:49:52 UTC | #5

@lefterisjp This is a very valid concern.

> Won’t that really skew the result towards the most popular grants of all categories?

This is a problem that's difficult to solve for even without category-based matching pools. For example even when we *did* have category-based matching pools we would still see a 'rich get richer' funding pattern where Grants with large communities or popular Grants take a larger percentage of the Matching Pool. 

That being said I do want to be clear and drive this specific point: From a UI/UX perspective nothing is changing. If for example you're browsing through grants under the "community" category, grants still have the same probability of being funded as before. 

The only difference here is instead of potentially having matching fund of ~$100K within the "Community" category, a grant is now eligible for matching funds among the full $800K matching pool. 

Also, to provide further context if we really breakdown "runaway" grants from previous rounds that take a large sum of the matching pool - we're really only talking about <5 grants in GR11. And this was without the 2.5% cap. So in theory by introducing the 2.5% cap we *should* see more grants get funded.

In terms of individual grants having more or less exposure on the site - it's all the same. An individual grants success really boils down to the ability to galvanize their communities, and broadcast that their grant exists.

-------------------------

lefterisjp | 2021-11-12 19:07:54 UTC | #6

If popularity contest is the whole point of quadratic funding then it's a deeply flawed concept.

Additionally another **very important** point of categorization is that the funding league, or whoever, who wants to provide funding for a certain kind of app gets to decide where their funds go.

Having all funds in one huge melting pot of community/infra/apps/regional donation/help covid/save envionments/save the kitties is terrible for the people who donate their funds.

If I wanted to donate to opensource I would not donate to such a pot. As I may end up helping comms projects, or save kids in Uganda. Both of which may be very noble causes but not what I wanted to fund.

Without categorization and category specific rounds the incentives for a certain kind of donator (I would argue the majority of donators) is gone.

-------------------------

unvetica.eth | 2021-11-12 19:25:29 UTC | #7

[quote="lefterisjp, post:6, topic:9007"]
Having all funds in one huge melting pot of community/infra/apps/regional donation/help covid/save envionments/save the kitties is terrible for the people who donate their funds.

If I wanted to donate to opensource I would not donate to such a pot. As I may end up helping comms projects, or save kids in Uganda. Both of which may be very noble causes but not what I wanted to fund.
[/quote]

This is a great observation, in fact this is exactly why we've created "Side Rounds". We have two types of Side Rounds going into GR12: **Ecosystem Rounds & Thematic Rounds.** 

**Ecosystem Rounds** allow companies like Uniswap to host their own matching round funded by Uniswap themselves, the goal being to fund grants specific to their ecosystem. We have multiple big-name companies that will be announced soon that will be doing exactly this. 

**Thematic Rounds** will be used during GR12, specifically there will be three categories: Longevity, Tech Advocacy, and Climate Change. These grants will help fund and advocate for very specific causes outside of the "Main" matching pool.

-------------------------

ebpwt02 | 2021-11-12 19:44:57 UTC | #8

I think the point of quadratic funding is balancing between popularity contests and buying elections with one large vote, and I think that will still happen with this round if the proposal passes.  

On the funding league side, I don't think the matching funds should discriminate by groups. I think the point of Gitcoin governance is to effectively run the platform and let contributors decide what to fund. Having the GTC holders, or whoever, allocate matching amounts of different sizes to different groups biases the assets towards their individual goals. 

I do agree it may deter some funder's league donors looking to support specific causes, but those donors should do matching grants for their specific causes then. A donation to the matching funds is a vote of confidence in the community to allocate donations correctly. At some point we have to put trust in the community that they will fund open source projects because they are important, not just because we think they are.

-------------------------

David_Dyor | 2021-11-12 19:48:26 UTC | #9

I wonder what the difference is between the Longevity theme and the Climate theme?  These sound somewhat similar, unless longevity refers to human lifespan.  Lots of research going on there (see HEX coin sheesh).

I just want to thank the Annika for drafting and posting this well laid-out post.  It is producing great discussions.  I support experimentation and I like wild idea of trying a single pool.  2.5% seems a bit high to me.  I'd rather see less...maybe 1.5%.   The ecosystem rounds should be enough to enable segregating the largest popular projects and the low 1.5% ensures many projects can get funded.

I am no economist expert!

-------------------------

unvetica.eth | 2021-11-12 19:53:40 UTC | #10

[quote="David_Dyor, post:9, topic:9007"]
I wonder what the difference is between the Longevity theme and the Climate theme? These sound somewhat similar, unless longevity refers to human lifespan.
[/quote]

That is exactly correct. 

The Longevity Round will be for initiatives like VitaDAO which look to extend human lifespan by researching, financing, and commercializing longevity therapeutics in an open and democratic manner.

The Climate Change round would be for initiatives like NORI who's goal is to create scalable carbon removal with crypto.

-------------------------

lefterisjp | 2021-11-12 19:57:38 UTC | #11

I never suggested that GTC holders should allocate the funds. GTC holders/votes never had a say here. It's not the GTC holders who gave the funds to the matching pool. It's the funder's league. Individuals and organizations.

Say Kraken for example as can be seen here: https://blog.kraken.com/post/7001/kraken-150000-grants-ethereum-gitcoin/

"Fund open source projects"

If those funds end up getting used to fight the climate crisis that's a mis-use of donated funds. And If I was Kraken I would never donate again. What's more everyone else who is sitting on the sidelines thinking, should I donate, sees such a mis-allocation of donated funds will have their answer.

-------------------------

ebpwt02 | 2021-11-12 20:06:05 UTC | #12

Gotcha, I understood the below to mean GTC voters determined the allocation

> Round 10 & 11’s distribution was based on GTC governance and we look to continue this with Grants Round 12 (GR12) to continue to reinforce the mission of decentralization

I buy the argument that groups that donated when they were able to determine a category should still see their funds used towards that category, but I still think it is better going forward to have one matching pool and let the community fully decide through their donations where it goes. Perhaps we should continue category grants for a round or two more to drawdown those specific matching donations while only taking in new donations to a main pool. Then we could go forward with the new pool without misappropriating any funds. Full disclosure, I am not an expert in this at all so I don't know how feasible that is. I actually delegate my votes to @lefterisjp for this reason.

-------------------------

lefterisjp | 2021-11-12 20:10:21 UTC | #13

Thanks Elliot!

So I am also not sure. Simply voicing my concerns. And as I said above I still think the system is quite skewed towards popular projects so the categories, so far at least, seemed to have helped.

I totally get the view that we can experiment for a round with a global pot to see how the system works in its purest most unrestricted form (okay maybe with limits on the max match per grant).

But as you said maybe let's do this gradually?

@annika I would like to propose if this goes to a vote to have 2 more options.

Option 2: Do GR12 with the same categories as GR11 (without any regional ones).
Option 3: Do a 50/50. So 50% of the matching pot in a global category, and 50% category based.

Point of Option 3 would be to go gradually and maybe even have data to compare the two approaches through actions of the same round.

-------------------------

okeaguugochukwu | 2021-11-12 22:16:09 UTC | #14

 I think it's ok to do away with regional grant

-------------------------

annika | 2021-11-12 23:19:50 UTC | #15

Thanks everyone for the great discussion - some excellent questions and pushback.

(And thanks @David_Dyor for the shoutout - I do want to call out that there are many others behind this write-up to whom all the credit is due!)

This is definitely an experiment and the plan is to iterate. @lefterisjp, I like the suggestion of the 50/50 on principle, with the ethos of making this more truly 'experimental' - but I'm not sure it's desirable for two reasons:

(1) From a UX perspective, having both in the same round poses the risk of being very confusing for both funders and grantees 

(2) From a data collection perspective, having a stand-alone round where we can get untainted insights from just the one pool is probably safer than trying to do both at once - I'm not sure we'd feel as confident in our takeaways/conclusions if both existed in parallel at once. There's also the question of operational lift - would be more onerous to execute.

-------------------------

lefterisjp | 2021-11-12 23:47:12 UTC | #16

Hey thanks for the response!

> From a UX perspective, having both in the same round poses the risk of being very confusing for both funders and grantees

Why? UX of whom? According to what @unvetica.eth wrote [here](https://gov.gitcoin.co/t/proposal-gitcoin-gr12-matching-pool-allocations/9007/5?u=lefterisjp) there is no UX difference for people who donate and neither will be for grant owners. Their grant will still be in the same category as before and will get matching from multiple pools.

This already happened last round with some grants being in the uniswap round and the GR11 round.

> From a data collection perspective, having a stand-alone round where we can get untainted insights from just the one pool is probably safer than trying to do both at once - I’m not sure we’d feel as confident in our takeaways/conclusions if both existed in parallel at once. There’s also the question of operational lift - would be more onerous to execute.

Operational lift aside, why do you think the insights would be tainted? You would clearly see how 50% of the pot is allocated (one standalone round) and how the other 50% is (app rounds as before) across all participating grants.

---

For operation lift, please don't take this the wrong way but I am going to be blunt. If this post is about telling us what you are going to do and just want us to do a snapshot vote to ratify it then starting a discussion 15 days before the round start may be okay. It's barely enough time to do a vote (7 days discussion + 7 days vote) by the time the round starts.

But I hope that we can get the community and the stewards more involved in the whole process and not just ask for a last minute snapshot ratification. Otherwise what's the point of the DAO?Which means this discussion should have began month/s ago.

Which is why in any upcoming snapshot vote I need to see more options and the ones I personally suggest are the ones in my previous post. Would love to hear other ideas/options too.

-------------------------

lee0007 | 2021-11-13 01:57:08 UTC | #17

[quote="tjayrush, post:4, topic:9007"]
Some would want to fund matches for media, some would want to fund matches for infrastructure. Having a single overarching round disallows matching funders from deciding what’s important to them as the entire decision making is in the hands of the donors.
[/quote]

[quote="lefterisjp, post:6, topic:9007"]
Having all funds in one huge melting pot of community/infra/apps/regional donation/help covid/save envionments/save the kitties is terrible for the people who donate their funds.
[/quote]

I also suspect removing categories could deter matching donations. Personally, I am very selective about donations and while I think all causes are worthy I simply (and maybe selfishly) have my own preferences, which are not indicated in the current thematic side rounds.

However, I look forward to learning whether multiple sub-categories or a single category provides better fund allocation and I am for the proposal due to the promise of an

> in-depth post-analysis comparing these two approaches for future CLR/QF mechanisms.

-------------------------

tjayrush | 2021-11-13 23:19:10 UTC | #18

[quote="lefterisjp, post:16, topic:9007"]
But I hope that we can get the community and the stewards more involved in the whole process and not just ask for a last minute snapshot ratification. Otherwise what’s the point of the DAO?Which means this discussion should have began month/s ago.
[/quote]

I agree with this while recognizing that everyone is doing their best work and everything is being invented as we go. Perhaps one things that may need to be invented is more of a process. Alternatively, less (or smaller, more focused) rounds per year with more planning.

-------------------------

annika | 2021-11-14 21:33:10 UTC | #19

[quote="lefterisjp, post:16, topic:9007"]
Why? UX of whom? According to what @unvetica.eth wrote [here](https://gov.gitcoin.co/t/proposal-gitcoin-gr12-matching-pool-allocations/9007/5) there is no UX difference for people who donate and neither will be for grant owners. Their grant will still be in the same category as before and will get matching from multiple pools.
[/quote]

Correct, as @unvetica.eth described, there isn't a UX issue if we move from categories to *just* the one pool - I’m suggesting there are issues that arise if we have *both in tandem*. Also, to specify, my concerns are more from a general confusion / grantee & funder experience perspective, not so much UI.

E.g., with a 50/50 split, we would need some mechanism to decide which grants are getting funded from the main pool vs. which are getting funded from the category pool. If a grant clearly falls into a specific category, does it by default just get funds from the category match? Does it also get funds from the main pool match? If yes, how are those allocated? If not, how do we decide which grants go to the main pool vs. category pools?

If I’m a grantee trying to understand my matching, it adds complexity. I'm not convinced the tradeoff of taking on this complexity is worth the benefit of iterating a bit more gradually - but very open to debate & ideas here.

[quote="lefterisjp, post:16, topic:9007"]
Operational lift aside, why do you think the insights would be tainted?
[/quote]

Part of the motivation of the experiment is to have a stark contrast between the two approaches. 

The main challenge I foresee goes back to the above question of how matching is handled across the two pools - if some grants are treated differently than others, and/or if funders now have the option to donate to the main pool or the 50/50 pool, we can't really reliably compare that data vs. previous rounds. 


[quote="lefterisjp, post:16, topic:9007"]
But I hope that we can get the community and the stewards more involved in the whole process and not just ask for a last minute snapshot ratification. Otherwise what’s the point of the DAO?
[/quote]

Totally hear your concerns and feedback around timing, and agree that doing this two weeks before the round isn’t ideal. I appreciate the bluntness, and we’ll try to do better. We’re going to start building out more structure and processes for the rounds, which we will be involving the community & stewards in, and we hope that will help.

-------------------------

kyle | 2021-11-16 03:20:16 UTC | #20

I love seeing the discussion here. 

I see one of the largest motivations for proposing something like this is to experiment with QF approach to measure the impact in different forms. I personally also share lots of the concerns that projects like Rotki may not be able to compete with other projects with larger communities. Frankly, we (Gitcoin Holdings) have dismissed this idea (single round) for multiple rounds given this concern. This experiment likely would not have been proposed had it not been for Vitalik asking to see something like this for multiple rounds now - I am not saying this should be a reason for executive decision making, merely the fact that I respect Vitalik's curiosity and desire to see the experiment unfold.

A few points to the concerns listed:
0 - Grants Round 12 is the first round we (Gitcoin Holdings) are working to decentralize operations of. As such, there will be great learnings as we proceed -- timing on this discussion has always been shorter than we want (GR11 was even shorter!) :confused:.
 
1 - There are no funds currently remaining in the matching pool (that I am aware of), that have been ear marked to a specific category. Keep in mind, Vitalik donated lots of dog tokens to fund public goods without an earmark for how those are used, and given the round size is now up to $1MM, the $150K from Kraken are long distributed.

2 - The QF mechanism has long tried to optimize for the many over the rich and few. This may be interpreted as a popularity contest, but it is also an incentivization mechanism for individuals with small amounts of money to have an outsize impact on the round. The true opportunity (IMO) is for increased curation mechanisms on the thousands of Grants we now have on platform. Going one step further, I am really excited to see the community ratify (hopefully soon) a policy on what criteria a Grant must adhere to to be eligible for matching funds. This is pretty loose right now (ie, no longer is it just digital public goods that are showing up on platform).

3 - As @lefterisjp mentioned, we have had Grants spanning multiple matching pools. ie the Uniswap Grants round and the Dapp Category round. I expect this to continue, and as such Gitcoin Holdings is working on optimizing the UX to make this more clear (for both funders and Grant owners).

All and all, I am supportive of the proposal under the condition that there will be an analysis after the round. This ensures there is documented learning, and continued conversations based on actual results, as opposed to just conjecture.

-------------------------

lefterisjp | 2021-11-17 17:56:59 UTC | #22

In case it was not obvious from my previous comments, when you move this to snapshot please add the two options I mentioned above.

https://gov.gitcoin.co/t/proposal-gitcoin-gr12-matching-pool-allocations/9007/13?u=lefterisjp

Don't just make a snapshot saying: "Yes we all agree with what the gitcoin team says" or "No".

And again please please please use the stewards and the community more in planning and feedback. This round, like the previous one feels a lot more like the gitcoin team telling us what we will do, rather than the DAO deciding.

-------------------------

annika | 2021-11-20 01:05:08 UTC | #23

Thanks everyone for the thoughtful dialogue. We plan to move this to a Snapshot vote on Monday.

Yes, @lefterisjp, I'll definitely include the two options you mentioned above. 

So, to summarize, there will be three options proposed to the community:

Option 1: Single Pool Experiment
Option 2: No Experiment - run GR12 with the same categories as GR11
Option 3: Do a 50/50. 50% of the matching pot as a single pool experiment, and 50% being category-based.

We'll include some context on each one in the post.

-------------------------

lefterisjp | 2021-11-20 10:30:17 UTC | #24

Thanks a lot Annika. And thank you all for the thoughtful back and forth. Really appreciate the insight and different perspective.

-------------------------

thelostone-mc | 2021-11-25 09:10:54 UTC | #25

@annika This discussion has come out with good possibilities on how this round should run.
I do have a suggestion as being one of the folks who's building stuff out for grants round.

Going forward could we have proposal for changes such as this one done (voting included) much ahead of time.
The reason I say this is cause we set code complete + testing plan setup based on our what we believe helps us improve the product.   

Changes from proposal like having 2.5% cap while def makes sense experimenting , having this pass just before the round starts, puts us in a tight spot as it makes it harder to meet our deadline.

Having this ironed out beforehand, would enable to grants team account for this during planning and ensure we have the right things built out

-------------------------

glocalVR | 2021-11-25 16:14:31 UTC | #26

and besides the last minute dev challenges @thelostone-mc , there´s one meta perspective of this one pool experimentation proposal that should be consider too ( with 50/50 dynamics or not) :  the potential increase of interaction/interface between grants or /and between collections ! and why I´m highlighting this ? because with categorization the projects tend to concentrate their " community action " within the borders of the category , which means very little widespread pollination effect occurs in terms of the micro funding that one can do regardless of the existing funding in the matchfunding round .... that said, it would be nice to count with features where even team members of each project feels compelled to browse between all the grants proposals to micro-invest time or/and crypto ..... that could potentially culturally deconstruct the " popularity contest " dynamics because the goal becomes enhance the web3/DAO culture as a whole ! and hey, that´s my 02 cents for now folks =)

-------------------------

trent | 2021-11-29 14:42:47 UTC | #27

Reading through the discussion here, appreciate everyone's perspectives. Agree with Lefteris that this discussion should take place earlier ideally.

I do agree that it seems like a bit of focus has been lost by the expansion into different categories. I'm supportive of their being a single large pool - though the 2.5% cap seems like a similar departure from "pure" Quadratic Funding, albeit a smaller impact. 

I will be voting for the "Single Pool Experiment" instead of the "50/50" split because it will be a cleaner data set to analyze.

-------------------------
