---
id: 10077
title: "How Soulbound Tokens Can Make Gitcoin Grants More Pluralistic"
slug: how-soulbound-tokens-can-make-gitcoin-grants-more-pluralistic
category: open-discussion
url: https://gov.gitcoin.co/t/how-soulbound-tokens-can-make-gitcoin-grants-more-pluralistic/10077
created_at: 2022-03-15T09:51:09.869Z
last_posted_at: 2023-02-08T20:39:33.917Z
posts_count: 18
views: 15186
like_count: 74
---

# How Soulbound Tokens Can Make Gitcoin Grants More Pluralistic

<https://gov.gitcoin.co/t/how-soulbound-tokens-can-make-gitcoin-grants-more-pluralistic/10077>
erich | 2022-08-22 21:20:19 UTC | #1

There has been [lots of work](https://gitcoin.co/blog/a-community-based-roadmap-for-sybil-detection-across-web-3/) happening around Sybil resistance in Gitcoin. By way of background, creating multiple accounts by a single person is an apparent danger to [Gitcoin Grants](https://gitcoin.co/grants/explorer/) and [quadratic funding](https://www.radicalxchange.org/concepts/quadratic-funding/). For example, a [Sybil attacker](https://en.wikipedia.org/wiki/Sybil_attack?wprov=sfti1) could set up numerous profiles in the quadratic funding program. Then, split their funds between them to make many small contributions instead of one enormous contribution to the grants in their favor. Voilà, this is how they might get a disproportionately high reward from the quadratic matching fund. Indeed, to maintain the quadratic funding grants program, we need to detect and defend against fraud like this.

# ⚠️ More Complicated Potential Dangers

We also need to consider [more complex cases](https://gov.gitcoin.co/t/a-vision-for-a-pluralistic-civilizational-scale-infrastructure-for-funding-public-goods/9503/11?u=leone) that might be dangerous for the overall utility of quadratic funding programs. **We should build social technologies for [Plurality](https://www.radicalxchange.org/media/blog/why-i-am-a-pluralist/) — technologies that acknowledge the beauty and richness of our diversely shared lives.** Social Plurality is about recognizing and fostering cooperation between various socio-cultural ecosystems. @GlenWeyl's [talk at the Schelling Point conference](https://youtu.be/MsMsL5v2-Ls) inspired the idea of applying the Plurality paradigm to quadratic funding and Gitcoin Grants.

Assume that these Plurality principles are critical. Then, we need to consider the role of these more complicated dangers to Gitcoin Grants, i.e., homogenous and highly cooperative groups within quadratic funding ecosystems. Consider families and friends, co-workers, neighbors, fellow citizens, for example. Naturally, our identities are nested within rich social graphs of relationships. Different people care about and cooperate with a unique set of people and organizations in their network. Should quadratic funding and Gitcoin Grants significantly reward and amplify cooperation between family members, co-workers, and friendly neighbors? Technically, a couple, a company, or a geographic community might be able to claim infinite amounts of matching funds through cooperation in Gitcoin Grants.

![image|500x500](upload://A1pFLI7VLDVm8iDTpkQacPrFzh5.jpeg)

One of the early steps that Gitcoin took to cope with this reality was the adoption of [pairwise quadratic funding](https://ethresear.ch/t/pairwise-coordination-subsidies-a-new-quadratic-funding-design/5553) computations. The key feature of this method is that it allows quadratic funding administrators to adjust the matching weights between any pair of contributors. In the spirit of Plurality, administrators can base these adjustments on recognitions about how much the contributors already cooperate. So, for example, two highly-cooperative agents would get a lower matching weight than two agents with very different social backgrounds. **Yay: A formal mechanism for cooperation across differences!** As far as I know, up until this point, the only evidence for collaboration between contributors that Gitcoin Grants captured is their contribution behavior in the current grants round, however. Unfortunately, it does not seem like this evidence sufficiently recognizes the complexity of the cooperative realities of contributors.

# 📔 Soulbound Token Journals

Here are some thoughts on formalizing richer evidence for pairwise cooperation in an accountable and value-aligned manner. First, imagine that contributors would maintain personal journals with all sorts of [soulbound](https://vitalik.ca/general/2022/01/26/soulbound.html) attestations about themselves. So, for example, you’d get attestations for the grant rounds you participate in, the projects you contribute to, the GitHub organizations you work with, your Twitter followings, et cetera.

[details="Rightfully so, the cyberpunks among us might be wondering at this point: What about privacy? Fortunately, we have a variety of applicable privacy solutions at our disposal."]

For example, we can zip the journals with cryptography. Moreover, we can assess an account's possessed attestations without identifying account information. Check out Vitalik Buterin's [post introducing the soulbound concept](https://vitalik.ca/general/2022/01/26/soulbound.html), where he details some of these privacy-related technicalities.

[/details]

On the other hand, some people might even like to present specific attestations publicly. For example, many people in the Web3 community have profile picture NFTs and affiliate with the organizations they work with within their Twitter bios. Similarly, they might want to highlight some soulbound attestations in public.

Now, remarkably, administrators of quadratic funding programs like Gitcoin could query these soulbound journals to quantify the cooperation between contributors. Here is how a simple version of this could work by comparing the intersecting attestations in the journals of each pair of cooperating agents.

[![\\ \text{Cooperative Multiplier}_{\text{Alice, Bob}}=\frac{\text{Shared Attestations}_{\text{Alice, Bob}}}{\text{Mean of Total Attestations}_{\text{Alice, Bob}}}](https://latex.codecogs.com/svg.latex?%5C%5C%20%5Ctext%7BCooperative%20Multiplier%7D_%7B%5Ctext%7BAlice%2C%20Bob%7D%7D%3D%5Cfrac%7B%5Ctext%7BShared%20Attestations%7D_%7B%5Ctext%7BAlice%2C%20Bob%7D%7D%7D%7B%5Ctext%7BMean%20of%20Total%20Attestations%7D_%7B%5Ctext%7BAlice%2C%20Bob%7D%7D%7D)](#_)

Suppose a pair of contributors, Alice and Bob, share two attestations relevant to the quadratic funding administrators. Further, suppose both have five relevant attestations in total. In that case, the quadratic funding administrators could quantify their cooperative multiplier as ⅖.

[![\\ \text{Matching Weight}_{\text{Alice, Bob}}=1-\text{Cooperative Multiplier}_{\text{Alice, Bob}}](https://latex.codecogs.com/svg.latex?%5C%5C%20%5Ctext%7BMatching%20Weight%7D_%7B%5Ctext%7BAlice%2C%20Bob%7D%7D%3D1-%5Ctext%7BCooperative%20Multiplier%7D_%7B%5Ctext%7BAlice%2C%20Bob%7D%7D)](#_)

Next, feeding that result back into the pairwise quadratic funding computations, the matching weight for Alice and Bob could be approximated as ⅗, i.e., one minus their cooperative multiplier of ⅖. If the cooperation between two contributors would be super high, say a cooperative multiplier of one, this way (one minus one), their matching weight would be zero. In turn, if two contributors come from very different social ecosystems and don’t share any attestations, their matching weight could be 100%.

**The above cooperative multiplier resulting from simple divisions of binary attestations is merely a kludge for a first start and not set in stone.** One day, there might be a whole industry for further innovation dedicated to researching formal models to quantify the social distance of people. Ecosystems will need to keep iterating on the Plurality algorithms they apply as context and possibilities evolve. For the Gitcoin ecosystem specifically, I could see the [Fraud Detection and Defense](https://gitcoin.notion.site/Fraud-Detection-Defense-2bde13c0b8e74fda81435d94e49e2703) (FDD) workstream or a dedicated Plurality working group taking the lead here.

# 🤝 Cooperation Across Differences

**In any case, with soulbound journals and tokens as more coherent evidence for pairwise cooperative relationships within the Gitcoin Grants ecosystems, we can significantly increase the Plurality of Gitcoin Grants. To the point, we’d gradually increase cooperation across differences and mute contributions between homogeneous and more highly cooperative groups.** The whole execution of this process would be possible without manual surveillance as currently practiced by the human evaluators in the FDD workstream.

![|602x439](upload://nPYV9VLg7bOsXv9dQgoqi77E1rX.png)

There are various possible mechanisms around the distribution of soulbound attestations. Attestations might be

* Free to claim or purchasable,
* Required for participation in, e.g., a grant round, or to contribute to a particular grant,
* Combinations of the above,
* Much more.

In any case, attestations might, on the one hand, represent a right to partake in governance and, on the other hand, might mean a liability when it comes to the matching weight calculations. Complex tradeoffs would determine the supply and demand for specific attestations. People would carry all sorts of attestations in their vaults. The value of their attestations would lie in the connections between them.

# 💫 Scaling Plural Technologies

Zooming out, we need to acknowledge that there won't be a one-size-fits-all model to measure and apply social graphs to Plurality. So instead, let's build a world where a Plurality of social institutions can query soulbound journals based on custom algorithms to assess and distribute rights and responsibilities to their people. The process might become a vital foundation for plural mechanism design across social organizations and mechanisms, including democracies, markets, the data economy, the commons, and identity. **Research and development of identity and policy modules for Plurality might become a whole new business model for Gitcoin.** For example, we might work with diverse ecosystems on grant rounds and, beyond quadratic funding, provide Plurality infrastructure for democratic, self-organizing communities more generally.

Notably, for example, as the infrastructure scales, it might help solve even some of the most significant technical issues of our time: e.g., Sybil-resistance, digital authentication, and more. Check out this piece on [intersectional social data](https://www.radicalxchange.org/media/blog/2019-10-24-uh78r5/) to learn more about some of these possible applications.

# 🛣 Time to Build

In the meantime, some concrete next steps for Gitcoin might be the following:

* Model pairwise grants round matching based on “artificial” soulbound journals with the information we already have: e.g., IP addresses as attestations about location; grants round behavior; GitHub data; [Twitter data](https://quadratictrust.com/); POAPs; [DAO memberships](https://public.flourish.studio/visualisation/8894796/); et cetera. Maybe the FDD workstream would be the best driver for these experiments. How about comparing different model results of plural funding with the actual GR13 results? @DisruptionJoe
* In working out the [Grants 2.0 roadmap](https://gov.gitcoin.co/t/gitcoin-grants-2-0/9981?u=leone), we need to ensure the identity and policy modules are interoperable with these Plurality mechanisms and technologies. @kevin.olsen @lthrift
* Prototype and standardize soulbound journals. Maybe fork [Gitcoin Kudos](https://gitcoin.co/kudos/marketplace) towards soulbound attestations? What [mintkudos.xyz](https://mintkudos.xyz/) is up to [related to soulbound Gitcoin Kudos](https://gov.gitcoin.co/t/request-for-proposal-decentralize-gitcoin-kudos/8115/4?u=leone) seems highly relevant here. @keikumata
* Finally, we need to help Gitcoin and other social organizations to adopt soulbound journals and plural technologies for diverse cooperation. This work will require highly-interdisciplinary collaboration between researchers, engineers, educators, community builders and institutions, and more.

To learn more about the ideas described in this post, check out the [presentation](https://youtu.be/RM7UFpSemjA) @GlenWeyl and I gave at a recent event organized by Protocol Labs.

I am super excited about the possibilities at the intersection of Gitcoin Grants, pairwise quadratic funding, and soulbound tokens. I hope we can work them out together. So join the discussion below, and let's build [a world where many worlds may fit](https://pluriverse.world/).

___

*I am deeply indebted to @GlenWeyl for his research and support, which guided the work on this post. My thanks are also due to @DisruptionJoe, @Fred, @kevin.olsen, @owocki, and Puja Ohlhaver for their suggestions and encouragement.*

-------------------------

cwarny | 2022-03-15 14:58:14 UTC | #2

I like this. I just have two quick comments: (1) I remember someone calling this "eigenvoting" (can't remember where I heard that) because your voting power is a function of how unique ("orthogonal") the vector representing you is, which is a rough linear algebra metaphor I guess; (2) have you looked into decentralized identifiers (DIDs) and Verifiable Credentials (VCs) (I would include links but as a first-time poster, looks like I'm not allowed)? These are two recently-finalized W3C standards that are akin to soulbound tokens. The main difference is that the data can be private (unlike POAPs afaik). "Verifiable credential", besides being a less sexy term than "soulbound token", is also a slight misnomer--a better term would be "verifiable container" for claims data about a person. A credential is issued by someone who asserts claims about an entity (identified by a DID) in a cryptographically-secure and tamper-evident fashion. Instead of a credential's claims data being written publicly forever on a decentralized ledger, it is held privately by the subject of the credential in a digital wallet, and presented by its holder on an as-needed basis (eg, to prove age in order to buy alcohol at a liquor store, or to prove uniqueness for participating in a Gitcoin grant vote). VCs could be used to prove uniqueness while preserving the privacy of whatever PII they contain. The verifier (in this case, Gitcoin) could ask the presenter (VC holder) for a variety of proofs of uniqueness, whether that is proving you hold a government-issued ID in the form of a VC without revealing the contents of that ID, using zero-knowledge proofs, or by proving a unique pattern of geolocated VC over time, for instance.

-------------------------

erich | 2022-03-15 22:53:29 UTC | #3

Thanks for sharing your thoughts, Cedric -- this seems super helpful in figuring out how we might implement plural quadratic funding. Indeed, I highly consider the work in the decentralized identifier (DID) and verifiable credential (VC) ecosystems, and @kevin.olsen also directed me to it in this context.

Here, the "soulbound" term is primarily meant to be a better meme for non-transferable attestations/credentials. It's not meant to commit plural quadratic funding to a particular technology substrate. 

The real contribution is the social incentive design, combining non-transferable attestations and pairwise quadratic funding to increase Plurality.

So absolutely, DID + VC might be the proper technical infrastructure for identities in plural quadratic funding. In any case, I hope we can tie the Plurality paradigm into the ongoing DID and VC discourses.

A bit more related context for everybody: https://decentralized-id.com/web-standards/w3c/wg/vc/verifiable-credentials/

-------------------------

george | 2022-03-16 07:37:37 UTC | #4

One question I've always had: does gitcoin understand what the motivation is for participating in donations? Last year I was involved in selecting a grants program for a group of investors and tried to create one myself, from which I learned that almost all of the donors' purpose is to airdrop, which is precisely contradictory to gitcoin's core logic.

-------------------------

kevin.olsen | 2022-03-18 15:16:36 UTC | #5

Thanks for posting this up, and yah, the exact mechanism is less important than the need for systems like QF to have this richness of data to work with. Interoperable and ubiquitous self sovereign identity feels right around the corner with folks like Spruce and Disco.xyz and even our dPopp project. Building out this even richer self and community attested data to allow for the community mapping you discuss in the post seems like the next evolution to ensuring systems that rely on one person one vote can flourish.

Establishing personhood to allow cooperation in systems like ours is the goal, soulbound is the meme not the mechanism.

-------------------------

castall | 2022-03-21 17:30:35 UTC | #6

Have you thought about how to make the Soulbound credentials non-transferable? In [BrightID Soulbound](https://github.com/BrightID/BrightID-Soulbound-NFT), we have the concept of a rescue operation, which allows you to rescue your Soulbound NFT from a wallet that has been compromised or that you no longer control.

To give an example, let's say you're bribed to give your credential to someone else.  You can accept the bribe, give them control of the wallet, then rescue your NFT to a new wallet

This Soulbound ownership is backed by [BrightID's social recovery](https://brightid.gitbook.io/brightid/setting-up-social-recovery).

-------------------------

castall | 2022-03-21 17:54:29 UTC | #7

[quote="erich, post:1, topic:10077"]
Prototype and standardize soulbound journals.
[/quote]

I watched your presentation, and it seems in governing plural goods, you want to consider the intersection (or perhaps the union) of a person's communities, but then at the very end, you say that you think we should use ZKP to allow the person to choose what to reveal. You also seem to give an example that a person might qualify for participation in Gitcoin grants by proving membership in the Ethereum ecosystem, but then for pairwise collusion computations, we should consider all of their memberships.

In the specific example of maximizing the matching funds going to projects I care about, it seems to benefit me to share enough to qualify me to participate, but not more.

How will ZKP help if I should share everything at once (the union of my memberships)? Is it just to protect privacy in cases where one's journal is tied to a demand for unnecessary personal information--like a registry that demands a self-submitted video, first and last name, and bio--or did you have in mind that ZKP allows for selective sharing, i.e. some but not all of my memberships?  In that case, how we can get the full benefit of understanding someone's union, while balancing that with the privacy implications of an [anonymity set](https://privacypatterns.org/patterns/Anonymity-set) that tends toward |1|?

-------------------------

Fishbiscuit | 2022-03-23 05:38:50 UTC | #8

**Initial Thoughts**
The post addresses two separate things and suggests one potential way that could help both things. Namely soulbound tokens being a way to identify important behaviour, characteristics, or contributions people have been in. The first challenge being preventing sybil behaviour > unique attestations prevent voting multiple times. Second challenge being acknowledging the dynamic nature of human existence and putting it 'on-chain' so that we can better encourage pluralistic behaviour.

**Contribution/Critique**
1. Sybil attacks - probably taking a leaf from consensus mechanisms might help too? Making it expensive to sybil attack would work. A simple way would be to create a lock-up/bond/stake for donors that will be returned after a challenge period. (now that would be such a pain and deter donating but let's ignore this first). But rather than lock-up/bond/stake we could give a soulbound NFT through a specific soul-binding ritual (like how proof of humanity or BrightID verifies) and these folks get a much higher trust score. Negative soulbound tokens might also work where identified sybil attackers get stuck with such a token and the entire ecosystem can shun them? The cost of creating new accounts is 0 though and it costs gas to make tokens so that might not work... so rather than penalising, incentivising might be a better approach.

2. Pluralism - I'd like some examples of plurality in action to get a better sense of how this might work out. But I think having some sort of soulbound attested address rather than just faceless addresses would be an important stepping stone to building plural institutions as it allows us to study decision-making from an ethno/anthro perspective.

**To do?**
What is the smallest experiment that we can run with soulbound attestations that can prove this? If we can prototype with just an excel sheet and a bunch of volunteers that would give us a sense of what we're actually building here

-------------------------

erich | 2022-03-29 07:22:56 UTC | #9

[quote="castall, post:7, topic:10077"]
we should use ZKP to allow the person to choose what to reveal
[/quote]

Ideally, people could programmatically select what type of data they want to reveal to a computer. However, in so doing, the counterparty should be able to verify that the data is complete. E.g., verify that the communicated data represents all relevant POAPs and past Gitcoin Grants behavior they have. 

Then, it might be required to reveal, e.g., your EthEvent POAPs and past Gitcoin Grants behavior to the quadratic funding program to participate in it. 

You can't get rights (e.g., matching weight) without responsibilities (e.g., revealing some of your attestations); this is a prevalent social dynamic. You don't get paid by a company if you don't work. You don't get full-service support from a nation-state if you don't follow its rules.
[quote="castall, post:7, topic:10077"]
for pairwise collusion computations, we should consider all of their memberships
[/quote]

[quote="castall, post:7, topic:10077"]
how we can get the full benefit of understanding someone’s union, while balancing that with the privacy implications of an [anonymity set](https://privacypatterns.org/patterns/Anonymity-set) that tends toward |1|?
[/quote]

I don't think any specific measure for pre-existing cooperation between people will be universally applicable. Depending on the local context, the algorithms will need to be adjusted. E.g., in a grants program for musicians, contributors' music tastes might be highly relevant. On the other hand, this seems significantly less proper for grants programs for software or energy production facilities.

[quote="castall, post:7, topic:10077"]
How will ZKP help if I should share everything at once (the union of my memberships)?
[/quote]

Suppose that the personal identity registries and the quadratic funding computations (considering contributions and contributor registries) would be zipped in cryptography. Things like the [Minimum Anti-Collusion Infrastructure](https://appliedzkp.github.io/maci/) might be one of the avenues enabling us to execute all the algorithms in a verifiable black box. So, after all, the only locally available/verifiable information would be the size of the contributions you made and the matching you received.

-------------------------

erich | 2022-03-29 08:59:46 UTC | #10

[quote="Fishbiscuit, post:8, topic:10077"]
Sybil attacks
[/quote]

Check out this essay on [Intersectional Social Data](https://www.radicalxchange.org/media/blog/2019-10-24-uh78r5/) and specifically the section on "Verifying Humanity of a Unique Participant." In fact, the personal registries might become highly secure Sybil defense tools, more accessible and valuable than the individualist personhood proofs around today.

We can combine the Plurality algorithms with the [Gitcoin trust verification scores](https://gitcoin.co/blog/trust-bonus) and more conventional personhood verifiers until the registries in themselves yield sufficient personhood proofs.

[quote="Fishbiscuit, post:8, topic:10077"]
I’d like some examples of plurality in action to get a better sense of how this might work out.
[/quote]

Here is a powerful example among other plural institutions in action that @GlenWeyl highlighted in his [Plurality essay](https://www.radicalxchange.org/media/blog/why-i-am-a-pluralist/).

> Let me close by imagining, hoping that ... Plurality might be feasible.
> 
> If so, we have a far brighter future ahead of us than the past few decades have given us reason to imagine. We can harness digital technologies to transform, improve and proliferate our social institutions even more than those technologies have corroded and undermined them to date. With three orders of magnitude less investment than has been poured into Web 3 and AI, Taiwan has in the space of a few short years [harnessed its initial foray in this direction](https://consilienceproject.org/taiwans-digital-democracy/) to develop arguably the world’s most technologically sophisticated and vibrantly democratic society, with widely shared growth even through a pandemic that cost its population of 22 million less than a thousand souls.

[quote="Fishbiscuit, post:8, topic:10077"]
What is the smallest experiment that we can run with soulbound attestations that can prove this? If we can prototype with just an excel sheet and a bunch of volunteers that would give us a sense of what we’re actually building here
[/quote]

Suppose we started to apply Plurality algorithms based on when (e.g., GR14, GR15) people contributed to what grants (e.g., Dark Forest, Rotki) and ecosystems (e.g., Ethereum, Polygon). In that case, I think we might already see more emerging diversely supported grants bubbling up to the top matching weight ranking. I also hope this might give us a legitimate reason to reduce the number of semi-arbitrary mechanism tweaks like the matching caps.

So for early experimentation, imagine that you'd need to claim corresponding time-stamped grants and ecosystems attestations to make a matching-eligible contribution to a project.

Since Gitcoin has that data (and more) in a centralized database, FDD (copying @DisruptionJoe) might be a good spearhead for some data modeling, as you describe. The models might definitely help set expectations and increase imagination around these ideas in the meantime.

-------------------------

DisruptionJoe | 2022-03-29 11:18:27 UTC | #11

One example for testing this could be to do it in a DAO workstream. You could send a soulbound token for:

* Each start date a contributor has (Workstream/Initiative/Squad)
* Each time a contributor gets paid
* Attending events (DAO Vibes/Gathering Hour/Weekly Update)

-------------------------

erich | 2022-03-29 12:59:24 UTC | #12

Interesting, Joe -- how'd you apply the tokens? DAO-internal quadratic funding?

-------------------------

nollied | 2022-03-29 18:15:33 UTC | #13

[quote="erich, post:1, topic:10077"]
[pairwise quadratic funding ](https://ethresear.ch/t/pairwise-coordination-subsidies-a-new-quadratic-funding-design/5553) computations
[/quote]

the problem with pairwise subsidies and other modifications to QF is that they move further from what QF saught to do. pairwise subsidies pushes the allocation of funds closer to uniformity, and most of the others like the [grant matching cap used in GR12](https://gitcoin.co/blog/grants-round-12-matching-caps/) do as well.

i love the way you formulate the problem of cooperation within communities as needing to be addressed with acknowledgement in the meme you shared:

[quote="erich, post:1, topic:10077"]
![image|500x500](upload://A1pFLI7VLDVm8iDTpkQacPrFzh5)
[/quote]

although, i'm skeptical of pairwise subsidies being the way to do this, it appears to be suppressive of said groups. i think the most commendable step towards this is actually side-rounds (ie. the [ukraine](https://pixel.ag/index.php/2022/03/18/gitcoin-grants-have-raised-1-2-million-in-ethereum-for-ukraine/) and environmental impact matching pools).

they act as an encapsulation that mitigates their impact for bleed-over between the cultures. the main round allows for a shared value to be captured and rewarded as well AND it serves as an explicit acknowledgement of their existence.

[quote="erich, post:1, topic:10077"]
For example, we can zip the journals with cryptography
[/quote]

and validate them with [zero-knowledge proofs](https://en.wikipedia.org/wiki/Zero_knowledge).

[quote="erich, post:1, topic:10077"]
their matching weight would be zero
[/quote]

i'm skeptical of punishing coordinated behavior, implicitly this rewards exploratory behavior, which *can be* great, but [it can also lead to unforeseen circumstances](https://www.manifold.ai/exploration-vs-exploitation-in-reinforcement-learning). this is well known in the reinfocement learning space as the exploration vs exploitation tradeoff.

we should tread very carefully. the problem we're seeing right now is sybil accounts with high coordination (which is fairly easy to detect), however if we bias towards pluralism too much, you might see the behavior being indistinguishable from randomness (this is the extreme of the exploration side of the tradeoff). it is much easier for sybil accounts to hide in entropy.

> It is difficult because *random exploration* in such scenarios can rarely discover successful states or obtain meaningful feedback. [[source](https://lilianweng.github.io/posts/2020-06-07-exploration-drl/)]

souldbounded NFTs won't fix this. they might make the problem easier to detect in retrospective analysis, but not without a lot of human intuition.

[quote="erich, post:1, topic:10077"]
The value of their attestations would lie in the connections between them.
[/quote]

i love the idea of staking as a consensus mechanism for decentralized identity.

[quote="erich, post:1, topic:10077"]
Model pairwise grants round matching based on “artificial” soulbound journals with the information we already have: e.g., IP addresses as attestations about location; grants round behavior; GitHub data; [Twitter data](https://quadratictrust.com/); POAPs; [DAO memberships](https://public.flourish.studio/visualisation/8894796/); et cetera. Maybe the FDD workstream would be the best driver for these experiments. How about comparing different model results of plural funding with the actual GR13 results? @DisruptionJoe
[/quote]

we're doing something similar to this in "The Matrix" squad i lead. we're exploring behavioral emergence and how models may react when the components of the system change (ie. pairwise subsidies).

[quote="erich, post:1, topic:10077"]
Prototype and standardize soulbound journals. Maybe fork [Gitcoin Kudos](https://gitcoin.co/kudos/marketplace) towards soulbound attestations? What [mintkudos.xyz](https://mintkudos.xyz/) is up to [related to soulbound Gitcoin Kudos ](https://gov.gitcoin.co/t/request-for-proposal-decentralize-gitcoin-kudos/8115/4) seems highly relevant here. @keikumata
[/quote]

please be more careful with how you use the word soulbound. it seems to have become a buzzword in the community and soulboundedness to me implies perfection. i like the idea of calling it "robust decentralized identity".

one of the simplest exploits that a soulbounded system should be impervious to: sell your private keys to your twin brother.

-------------------------

DisruptionJoe | 2022-05-13 16:52:09 UTC | #14

[quote="erich, post:1, topic:10077"]
For the Gitcoin ecosystem specifically, I could see the [Fraud Detection and Defense ](https://gitcoin.notion.site/Fraud-Detection-Defense-2bde13c0b8e74fda81435d94e49e2703) (FDD) workstream or a dedicated Plurality working group taking the lead here.
[/quote]

This is exactly where I see FDD going. Launching a bunch of services in this pluralistic future. Gitcoin would hold massive upside in them. And most would be digital public infrastructure to protect communities from being taken advantage of.

-------------------------

llllvvuu | 2022-08-23 17:47:05 UTC | #15

I like this research direction - it represents the broader research area of social distance inference, which is useful not just for Gitcoin Grants but for almost every social application - e.g. declaring conflicts of interest is a big thing in academic journals, and practice in law, medicine, finance, government, etc.

One extension which might make the research especially challenging/interesting is *incentive-compatible inference*. If you use self-declared relationships for anything meaningful, there is an incentive to lie and hide relationships. My sense is that usually we have penalty of perjury to deal with this.

-------------------------

tkgshn | 2022-11-13 01:30:55 UTC | #16

I wrote about related topic
https://gov.gitcoin.co/t/decentralized-social-graph-as-an-oracle-powered-by-the-wisdom-of-the-crowd-for-the-era-of-plurality/11927

-------------------------

erich | 2023-02-08 22:29:18 UTC | #17

Hello all,

Please allow me to follow up on this thread I started about a year ago regarding making Gitcoin Grants more pluralistic through [soulbound](https://vitalik.ca/general/2022/01/26/soulbound.html) tokens. There have been exciting developments in this field with the emergence of more advanced pluralistic QF models [1] [2].

Gitcoin Allo can source the necessary social information for these models through existing Gitcoin Passport stamps and new integrations. Diverse pluralistic QF formulas are specified and analyzed in writing and code in the papers [1] and [2], and another whitepaper [3] rigorously tackles the technical and computational aspects of the required identity solutions.

Why have these opportunities yet to be considered to find their place on Gitcoin's roadmap? Indeed, a more pluralistic QF model could drive significant improvements in grant round matching results (without relying on hackneyed tweaks like matching caps), even if based on one or two dimensions of sociality to start. So start somewhere: Define some Passport stamps (i.e., which the Gitcoin Allo communities want to bridge by matching across them) and gradually adjust the QF models to incorporate them.

What limitations or concerns need to be addressed before proceeding in this direction? Would love your thoughts on these ideas and their intersections with Gitcoin Allo and Passport, @kevin.olsen @kyle @michelle_ma @nategosselin.


[1]
Weyl, Eric Glen and Ohlhaver, Puja and Buterin, Vitalik, Decentralized Society: Finding Web3's Soul (May 10, 2022). Available at SSRN: https://ssrn.com/abstract=4105763 or [http://dx.doi.org/10.2139/ssrn.4105763](https://dx.doi.org/10.2139/ssrn.4105763)

[2]
Miller, Joel and Weyl, Eric Glen and Erichsen, Leon, Beyond Collusion Resistance: Leveraging Social Information for Plural Funding and Voting (December 24, 2022). Available at SSRN: https://ssrn.com/abstract=4311507 or [http://dx.doi.org/10.2139/ssrn.4311507](https://dx.doi.org/10.2139/ssrn.4311507)

[3]
Jain, Shrey and Erichsen, Leon and Weyl, Eric Glen, A Plural Decentralized Identity Frontier: Abstraction v. Composability Tradeoffs in Web3 (August 24, 2022). Available at arXiv at https://arxiv.org/abs/2208.11443 or [https://doi.org/10.48550/arXiv.2208.11443](https://doi.org/10.48550/arXiv.2208.11443)

-------------------------

kevin.olsen | 2023-02-08 20:39:33 UTC | #18

I couldn't be more excited to see the progress being made here and throw my full support behind getting Gitcoin to experiment with, and adopt these new approaches to QF. 

We owe our current mechanism to these thinkers. And as they've continued their work, they have found new and novel mechanisms that add dimensionality to our problem space and may let us step over some of the complex problems (airdrop farmers, sybils, etc.) that drain resources and distort the signals from our community. I'm very bullish on the potential of these next-generation allocation mechanisms.

Importantly, I see this as an incredible opportunity to re-establish our position as vanguards by returning to our roots as the living laboratory for these ideas. And as our best forward path to ensuring the communities that adopt our protocols become the egalitarian, pluralistic spaces we aspire to create.

-------------------------
