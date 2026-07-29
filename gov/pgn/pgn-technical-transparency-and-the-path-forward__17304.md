---
id: 17304
title: "PGN Technical Transparency and the Path Forward"
slug: pgn-technical-transparency-and-the-path-forward
category: pgn
url: https://gov.gitcoin.co/t/pgn-technical-transparency-and-the-path-forward/17304
created_at: 2023-12-19T02:37:40.084Z
last_posted_at: 2023-12-21T22:47:03.510Z
posts_count: 11
views: 4370
like_count: 51
---

# PGN Technical Transparency and the Path Forward

<https://gov.gitcoin.co/t/pgn-technical-transparency-and-the-path-forward/17304>
sophia | 2023-12-19 02:37:40 UTC | #1

# **TLDR**

- Initial technical hurdles impacted PGN’s early growth
- PGN is part of the Optimism Superchain, a network of L2s working together
- Our alliance with OP Labs provides vital technical support and resource that can accelerate our technical development

---

PGN launched 6 months ago with an innovative and ambitious goal of creating durable and recurring funding for public goods. As one of the first small players to launch an L2 on the OP Stack, we have admittedly encountered technical challenges due to the inherent novelty and complexity involved in operationalizing decentralized compute environments. While these technical challenges have hindered our ability to grow at the pace and scale we envisioned, our commitment to the original goal remains steadfast.

We also feel it is worthwhile and productive to share more transparently on what it really takes to launch an L2. We are confident that as L2 technology matures, and as our ecosystem grows, the original vision of growing the pie of available public goods funding is still possible.

# **Technical Hurdles**

It is easy to take for granted how well developed the Ethereum ecosystem is, with new platforms and improvements being added regularly. Today’s Ethereum is a very functional place for a crypto native person, with multiple wallet, exchange, block explorer and security solutions available. When building an L2 from scratch, each of these technical integrations must be identified and built independently, based on the focus of that specific L2.

### **Integrating technical dependencies**

The process for integrating with various technical dependency providers can be broken down into three main approaches:

1. **Decentralized Providers:** This usually involves drafting a detailed proposal on their forum that highlights the advantages of integrating PGN. Then, we rally community support and gather votes to ensure our network gets added.
1. **Traditional Teams:** The focus here is on building relationships. This typically involves communicating directly with providers to explain PGN's advantages and offering technical support for integration.
1. **Self-integration:** In some instances, we can directly add our network and submit a pull request. However, more often than not, getting our pull request merged hinges on the integration partner’s willingness to include our network. This also doesn’t guarantee that our network will be incorporated into the frontend UI.

Understandably, providers often want to see evidence of significant activity on our network to justify the effort required for integration. Some may request upfront capital to cover deployment and maintenance costs.

### **Limited resources**

PGN has no external (venture) funding pumping our network activity.

As a public good itself, this was an intentional part of PGN’s strategy. We prioritize allocating sequencer fees towards public goods instead of venture capitalists. However, bootstrapping an L2 with a small team and a limited budget is challenging. This constraint has limited our ability to integrate with various service providers as we have to strategize which technical dependencies we prioritize.

### **L2s flywheel problem**

Initially, we underestimated the extent of technical dependencies and integrations needed for an **ecosystem-ready** L2 network. This resulted in technical obstacles, most notably the lack of a Safe UI, which significantly slowed down our deployment with ecosystem partners. Without the necessary technical dependencies in place, the pace of our ecosystem growth was delayed.

Once we overcome these initial technical hurdles and achieve ecosystem readiness, we can confidently move forward with the next phase of PGN's development. At a high level, we aim to focus on expanding alliance partnerships, integrating dApps, and growing transaction volume. (More details on this to come in future discussion posts).

We launched in a state where PGN was not fully ecosystem-ready. We lost momentum in the process. So, the big question still remains… When will we get the flywheel moving?!

# **The OP Superchain**

Despite our initial challenges, being part of Optimism’s Superchain ecosystem provides us with a vital lifeline. **We’re not a siloed L2.** PGN is still in its infancy but being one of the early adopters in the Superchain ecosystem gives us a unique advantage; we get to work directly with OP Labs, Base, Test in Prod, and other Optimism core contributors, shaping the future of how these chains can effectively interact and function together.

### **What does this mean?**

Since meeting in person at DevConnect, we’ve gone deep in our relationship with extremely helpful individuals on the OP Labs team and across the Optimism Collective. We have been closely working with them to overcome these technical barriers and develop our overall strategy. This includes weekly meetings where we discuss and address broader L2 strategy and identify areas where we need technical support. We have received valuable feedback regarding bridging, stablecoins, and areas within our ecosystem that require further attention. Additionally, they are helping to support the development of crucial components of our technical dependencies, such as the Safe UI, which was a major obstacle for our partners before they could build on our network. (More details on that to come soon!)

### **Why are they doing this?**

PGN’s success advances the success of the Superchain ecosystem. The grander vision is a network of chains, each with an individual market and value prop, that share bridging, decentralized governance, upgrades, a communication layer and more—all built on the OP Stack.

The ultimate goal is to merge OP Mainnet and other L2s built on the OP Stack (such as Base, Zora, PGN, and others into a single unified network of chains. Learn more about it [here](https://stack.optimism.io/docs/understand/explainer/). This paves the way for a more scalable and decentralized web.

### **A shared vision**

In a truly decentralized web, more players should be able to create an L2 and benefit from sequencer fees, with governance over their allocation within their ecosystem. Not just players that have a lot of upfront venture capital where fees benefit early investors.

Yes, bootstrapping an L2 in the current ecosystem is incredibly challenging. However, creating this opportunity is crucial for the overall L2 and Superchain ecosystem, which itself is vital to a thriving on chain future. PGN's experiences and transparency as a public good itself serve as valuable learning opportunities for the Optimism Collective, allowing them to design better support mechanisms for the L2 Superchain ecosystem.

We will explore the Optimism Superchain and PGN's role within this broader narrative and movement in a future post. Stay tuned!

## **Looking ahead**

The Superchain ecosystem is still early. Many of the anticipated benefits, such as interchain interoperability and standardization, are yet to be fully realized.

For example, Grant Stack is exploring multi-chain checkout solutions. In a future where Superchain interoperability tooling is more abundant, multichain checkout across PGN, Base, and OP Mainnet would be effortless, offering dApps a plug-and-play solution.

Another example is span batches, a technique developed for the OP Stack specificallyto efficiently aggregate and compress transaction data, significantly reducing data size and lowering costs for PGN. Research from Test in Prod indicates that, during the GG18 event, the use of span batches could have slashed PGN's L1 costs by 50% to 90%. This is planned to be implemented as part of the Optimism Delta hard fork if it passes a governance vote scheduled for January - in which case it would be rolled out around mid to late February. You can read more about it here [https://x.com/testinprod_io/status/1723367847483646175?s=20] and I'll continue to update as I learn more.

# **The Bigger Picture**

Though PGN is still in its initial development stage, with technical hurdles still to tackle, we are part of a larger movement. PGN is not a siloed L2; we are deeply integrated within the Optimism ecosystem and supported by its powerful network.

Our mission is important. The future is leaning towards a world with multiple L2s, and PGN is not an outlier in this trend. While the current landscape is crowded with L2s, leading to fractured UX challenges, the need for horizontal scalability requires multiple chains. The current user experience pain points surrounding L2s primarily stem from the incomplete development of interoperability solutions - but these challenges are being actively addressed, and acceleration toward solutions will only come from a willing commitment to engage in the challenges.

***It’s important that we lay down the groundwork. By building the necessary infrastructure now, more communities can create and support their own L2 ecosystems, ensuring that sequencer fee control isn’t just in the hands of those with the most resources.***

PGN is an ambitious experiment. We acknowledge that bootstrapping an L2 is a challenging task, and PGN's struggles highlight the need for improved support. While we faced many blockers, it’s an important problem to try and solve. We are learning and sharing valuable lessons along the way and contributing to a future where public goods receive the sustainable funding they deserve.

## **Our call to action**
**If you believe in our mission, the most helpful thing you can do is contribute to and advocate for the development of core infrastructure on PGN.**

Here’s how:

- [Join our Telegram](https://t.me/pgn_eth) and shape the technical roadmap through feedback and support.
- [Join the Alliance](mailto:pgn@gitcoin.co) and contribute to public goods funding by filling blockspace.
- [Deploy your project onto PGN](https://docs.publicgoods.network/) and [join the biweekly Builders Calls](https://docs.publicgoods.network/) to grow the ecosystem.

-------------------------

Jimi | 2023-12-19 12:27:56 UTC | #2

Thank you for sharing all of these aspects of PGN, Sophia. 

Talk about building in public! :clap:

Questions for you:
1) Since PGN is apart of Optimism's Superchain ecosystem, does that mean startups that launch on PGN will still qualify for Optimism Retro PGF?
2) Since limited resources is challenge, why not launch a token or NFT that could crowdfund for PGN?

Let's GROW

-------------------------

ccerv1 | 2023-12-19 13:56:50 UTC | #3

Great post!

It's worth considering what could be done to encourage more public goods projects to build their community on PGN first and foremost, eg, layering use cases across Zora, Guild, Jokerace, etc. These are much more social than financial use cases.

I'd also love to see more identity primitives take root on PGN. For instance, it would be great to see a protocol like EAS deploy on PGN.

-------------------------

owocki | 2023-12-19 18:04:16 UTC | #4

Thanks for the detailed post Sophia.

Reading between the lines, the launch of PGN has been lackluster so far.  Other than Gitcoin Grants, there is not any other dApps consuming block space on PGN.  According to the dune dashboards [here](https://dune.com/oplabspbc/op-stack-chains-l1-activity) and [here](https://dune.com/kouei/pgn-bridge-overview) it’s not being used much outside of Gitcoin Grants.

I say this not to be needlessly critical, but because I think we should look at this soberly if we are to turn it around.

It's not clear to me what the Unique Selling Proposition of PGN is, nor where the deep well of market demand is realistically going to come from.   "How do we get developers to deploy their dApps on PGN?" feels like a very germane question.

If PGN is going to continue operations, I'd love to see the PGN team have more of a bias towards creating momentum on PGN.   Momentum begets momentum   PGN is basically a mini pre product market fit startup + most startups die because of a lack of momentum. -  If PGN is going to continue, I want to see more volatile energy coming out of the PGN team ( https://randsinrepose.com/archives/stables-and-volatiles/ ) creating momentum.

-----

[quote="sophia, post:1, topic:17304"]
PGN has no external (venture) funding
[/quote]

Gitcoin was funded by Consensys/Paradigm.  And has a fairly large treasury relative to it's humble beginnings.  It [spends $10k-100k/mo (depending on whether there is a Gitcoin Grants round that month)](https://vxtwitter.com/0xkofi/status/1735796630769512526?s=46&t=X0oQ26a3ezptVAZLp1QFaw) on keeping PGN alive.

Between 2018-2021 Gitcoin spent less than $130k/mo on all of Gitcoin (at the time, this meant Grants, Bounties, and KERNEL business lines).  

I feel like PGN has got a scarcity mindset here when we need not have one.  

Maybe if/when batch txns go live, ya'll can save some $$$ on gas fees + reroute that to marketing and adoption rewards.

Here's one thing we could do to bootstrap demand with only a few thousand $$$/mo.  Implement [Contract Secured Revenue](https://eips.ethereum.org/EIPS/eip-6968) with a lean no-code approach:

1. i can get u a list of addresses by the amount of blockspace they consumed
2. we airdrop $5k of rewards to them
3. we market that PGN rewards developers of public goods.
4. repeat every month + increase funding as more becomes available.

thats 0 to 1 on PGN CSR that we can do in a few hours.

-----


[quote="sophia, post:1, topic:17304"]
 We are confident that as L2 technology matures, and as our ecosystem grows, the original vision of growing the pie of available public goods funding is still possible.
[/quote]

What would have to be true for the original vision of growing the pie of available public goods funding **to be on track** (not just possible)?.

---

Given that PGN was launched out of the Gitcoin Foundation + not through DAO governance, I do not have much more to say on the gov forums other than to say that I hope this situation is resolved well before the Foundation needs to come to the DAO for more funding.   The Foundation does critical support work for the DAO, and I don't want to see that complicated, or put at risk, by the Foundation burning too much of its $$$ on a skunkworks project. (i'm not saying that has already happened, i'm saying its a potential future scenario that should be avoided)

I have authored a brief [here](https://docs.google.com/document/d/1TaIdypMcXyjn_d4m3Y6SWfbkYNJCmy4NfES_s4PLxno/edit) in which I propose an increase in momentum for PGN.   I am looking forward to discussing together with PGN leaders in the coming months.

-------------------------

CryptoReuMD | 2023-12-20 18:53:48 UTC | #5

[quote="owocki, post:4, topic:17304"]
Reading between the lines, the launch of PGN has been lackluster so far. Other than Gitcoin Grants, there is not any other dApps consuming block space on PGN. According to the dune dashboards [here](https://dune.com/oplabspbc/op-stack-chains-l1-activity) and [here](https://dune.com/kouei/pgn-bridge-overview) it’s not being used much outside of Gitcoin Grants.
[/quote]

Interestingly, several people within the DeFi universe are keeping track of this. No other use can be found.
Areas for improvement:
1.- We could start using chain governance and start by voting on a tool like Tally that signs on PGN.
2.- Make more use of the terms and conditions in PGN, as we often have to bridge to Ethereum to make decisions.
3.- Launch a stable coin ecosystem or in due time a DeFi place to be able to make exchanges within PGN. 
4.- The introduction of hyper-certs in PGN, not only in optimism.
5.- The Gitcoin passport, the atm station is done in Optimism. We could mine it in PGN. 
In the end, the intention is to use more PGN chain, not only for rounds. 
Best

-------------------------

sophia | 2023-12-21 01:26:12 UTC | #6

[quote="Jimi, post:2, topic:17304"]
Since PGN is apart of Optimism’s Superchain ecosystem, does that mean startups that launch on PGN will still qualify for Optimism Retro PGF?
[/quote]

Yes! This is something we definitely need to publicize more.

-------------------------

sophia | 2023-12-21 01:42:49 UTC | #7

Ooo great thinking!

PGN is already an active network on jokerace and zora, so that'd be an easy lift. 

Some feedback we received from OP Labs is to identify **how** we expect users to engage on our network and build for that. Previously, we were targetting other public good funding dApps but the defi infra on our network is not the strongest. 

Perhaps the social use case is strong enough for PGN to be self sufficient. (With our current financial models and transaction volume, we are about half way there). This is something I'd definitely like to explore more in the new year.

-------------------------

sophia | 2023-12-21 04:45:59 UTC | #8

Thanks for the detailed response - I fully agree. We need to be candid about what's happening at PGN if we want to see things change.

I joined the team last month with a specific focus on integrating new technical dependencies, so might be lacking some context. But here are my thoughts based off of my understanding so far:

[quote="owocki, post:4, topic:17304"]
It’s not clear to me what the Unique Selling Proposition of PGN is, nor where the deep well of market demand is realistically going to come from.
[/quote]

Officially, our USP is that net sequencer fees go to public good projects. While, that doesn't mean much in our current state, exploring sustainable funding methods is crucial for the public good ecosystem. Yet, a compelling mission alone isn't enough. 

I believe a well designed sequencer fee allocation plan would strengthen our USP. PGN plans to announce more information on the governance strategy in January. I haven't been directly involved in these discussions, but as you know, I personally would like to see us implement contract secured revenue. The main issue isn't getting dApps to deploy on our network, its incentivizing them to consume block space. I'd like to see PGN leverage CSR as a mutually beneficial unique selling point to mitigate this. 

[quote="owocki, post:4, topic:17304"]
Other than Gitcoin Grants, there is not any other dApps consuming block space on PGN.
[/quote]

True. While getting developers to deploy dApps on PGN hasn't been seamless (because of some technical hurdles), we're still an added network on [other high traffic dApps](https://publicgoods.network/) besides just Gitcoin Grants. Yet, they aren't consuming nearly enough block space - probably due to our weak USP and mediocre tech. 

As outlined above, we have a strategy to fix our mediocre tech. And, I'd like to test if bootstrapping CSR can fix our weak USP.

The scalability vision of the [Superchain](https://docs.optimism.io/stack/explainer) is that most big dApps will [eventually have their own app chain.](https://x.com/Th3Optimist/status/1735042164780880246?s=20) If that is the direction we're going in, public good dApps might as well use PGN. It's already built out, values aligned, part of the superchain, and (if CSR is implemented) creates a new source of direct funding. Win win!!

[quote="owocki, post:4, topic:17304"]
If PGN is going to continue, I want to see more volatile energy coming out of the PGN team
[/quote]

Admittedly, we've been playing it safe. I like your bootstrap suggestions for some experiments we can run. There's a lot more we can do to be creative, cut corners, and get this flywheel moving. Hopefully, we can test that out in the new year. 

[quote="owocki, post:4, topic:17304"]
Gitcoin was funded by Consensys/Paradigm.
[/quote]
oops didn't know that. I still don't think we plan to allocate any sequencer fees back to them though. No shade to other L2s, but my understanding of other L2 funding models is that they typically start with a significant amount of capital that pumps network activity to generate sequencer fees and be profitable.

But, like you said, there are other creative ways to pump network activity that don't require significant capital.

[quote="owocki, post:4, topic:17304"]
It [spends $10k-100k/mo (depending on whether there is a Gitcoin Grants round that month) ](https://vxtwitter.com/0xkofi/status/1735796630769512526?s=46&t=X0oQ26a3ezptVAZLp1QFaw) on keeping PGN alive.
[/quote]

The link you added is referencing what we spent on posting data to Ethereum. What is not shown is that that same month our total revenue from gas fees was 38.78 ETH (numbers from Conduit our rollup provider). So our data cost was the difference (around 10 ETH). 

Besides getting more tx volume, we can also increase gas fees so that we break even. Of course, increasing gas fees might upset users, so the key here is strengthening our USP. 

[quote="owocki, post:4, topic:17304"]
Here’s one thing we could do to bootstrap demand with only a few thousand $$$/mo. Implement [Contract Secured Revenue](https://eips.ethereum.org/EIPS/eip-6968) with a lean no-code approach:
[/quote]

Love this! I wanted to run some adoption reward experiments but need to get the green light from budgeting first... I don't have full understanding for how finances work, but pretty sure we have to get every financial cost (from tech dependencies to experiments) approved by the foundation. And asking the foundation for money is a bit sensitive. (Would like to re-emphasize I don't get how this stuff works so I could be totally wrong here. Don't mean to speak for anyone or throw people under the bus). 

[quote="owocki, post:4, topic:17304"]
What would have to be true for the original vision of growing the pie of available public goods funding **to be on track** (not just possible)?.
[/quote]

1. Better tech (more superchain interoperability tooling, funding to pay for key tech dependencies, etc.) 
2. A stronger USP
3. More capital to experiment with adoption rewards

Would enable:
1. More dApps deploying on PGN
2. dApps incentivized to add us as their default network and consume blockspace

[quote="owocki, post:4, topic:17304"]
I have authored a brief [here ](https://docs.google.com/document/d/1TaIdypMcXyjn_d4m3Y6SWfbkYNJCmy4NfES_s4PLxno/edit) in which I propose an increase in momentum for PGN. I am looking forward to discussing together with PGN leaders in the coming months.
[/quote]

Same here! We have a challenging road ahead but an important one.

The L2 ecosystem is not slowing down. As this ecosystem continues to evolve, it's likely that mature dApps will start considering creating their own L2s. While being early created a lot of technical hurdles and killed our momentum, it also means we are well positioned for a multi-chain future.

-------------------------

thedevanshmehta | 2023-12-21 13:28:42 UTC | #9

As someone closely following PGN since inception, the lack of momentum has caused me to reconsider plans of launching my dapp on it.

Firstly, I can't see enough differentiation from Optimism in the comms as both claim a public goods allocation from sequencer fees. OP Mainnet has the advantage of a much more well developed ecosystem

Secondly many of the protocols i want to build on, such as hypercerts, are not on PGN with no plans of launching there either

Thirdly, PGN itself seems too much like a Gitcoin Foundation initiative with not enough buy-in from its Alliance partners Giveth, Octant, Hypercerts or even Gitcoin DAO. A true alliance would do cost-sharing and support more than what we have witnessed so far.

I do not mean to be needlessly critical or harsh, I like the vision of PGN ! What needs more clarification is how different alliance members show buy-in of the chain and also how the mission is substantively different from Optimism

-------------------------

sophia | 2023-12-21 19:05:54 UTC | #10

[quote="thedevanshmehta, post:9, topic:17304"]
As someone closely following PGN since inception, the lack of momentum has caused me to reconsider plans of launching my dapp on it.
[/quote]

PGN doesn't have to be the default network. Can I ask why it can't be an added network? As we move into a multi-chain future, I envision most dapps will be on many networks.

[quote="thedevanshmehta, post:9, topic:17304"]
Firstly, I can’t see enough differentiation from Optimism in the comms as both claim a public goods allocation from sequencer fees. OP Mainnet has the advantage of a much more well developed ecosystem
[/quote]

Optimism allocates to network public goods. We don't just support public goods on our network, but any public goods at large. 

In general, having more systems supporting and funding public goods is good. Optimism will have their own governance method of retropgf and PGN will have their own governance method as well. We love Optimism and think their well developed sequencer fee allocation methods are great! But, one big player deciding how fees are allocated creates centralization. If we value the ethos of web3, it's crucial to also decentralize sequencer fee allocation control. 

[quote="thedevanshmehta, post:9, topic:17304"]
Secondly many of the protocols i want to build on, such as hypercerts, are not on PGN with no plans of launching there either
[/quote]
We're adding Hypercerts. What other protocols/tech dependencies aren't available? 

I'd encourage you to join our telegram channel and participate in our builder calls. That way, we can communicate and assess if we're on track to provide the necessary technical dependencies for your dApp. We have a roadmap detailing our future tech integrations, which is flexible and evolves based on the needs of our builders. Would love to get your involvement in these conversations :)

As mentioned in this forum post, integrating with new tech dependencies as a smaller L2 hasn't been seamless. But, we are in the process of working alongside other L2s in the Superchain ecosystem to "unionize" our efforts.

-------------------------

owocki | 2023-12-21 22:47:03 UTC | #11

Thanks for the engagement and earnest answers @sophia !  

[quote="thedevanshmehta, post:9, topic:17304"]
I do not mean to be needlessly critical or harsh, I like the vision of PGN !
[/quote]

Like Devansh, I do not mean to be needlessly critical or harsh, and like the vision of PGN.

But I do think that the state of PGN does warrant some necessary questions about it's future.

[quote="thedevanshmehta, post:9, topic:17304"]
As someone closely following PGN since inception, the lack of momentum has caused me to reconsider plans of launching my dapp on it.
[/quote]

Unfortunately for PGN, a lot of crypto is reflexive.  Momentum begets momentum.  And a lack of momentum begets more lack of momentum.

This can work in the favor of product rollouts where the team behind them engineer (and with the benefit of a bit of luck + tailwinds) engineer momentum!  Look at BASE, which caught fire over onchain summer.  Or Zora, with a similar order of magnitude of resources as Gitcoin, has [consumed a lot of blockspace with Zora chain](https://dune.com/queries/2453515/4755478).


[quote="sophia, post:8, topic:17304"]
The link you added is referencing what we spent on posting data to Ethereum. What is not shown is that that same month our total revenue from gas fees was 38.78 ETH (numbers from Conduit our rollup provider). So our data cost was the difference (around 10 ETH).
[/quote]

So for 1 month per quarter (the month that Gitcoin Grants runs), PGN loses 10 ETH.  And the other 2 months, it loses ~50 ETH/month?  By my math, PGN costs the Gitcoin Foundation roughly 110 ETH($220k)/quarter  - Though I assume this varies quarter over quarter depending on gas costs + amount of block space Gitcoin Grants can consume.

This leads me to a few questions:
1. Do you know when these operational costs will reduce (either via danksharding or batch txns, or perhaps PGN should become a L3?)?  
2. When will the confidence of the market be restored? (to me this means a clearly articulated path to success + a credible resource commitment to make it happen, but I cannot speak for other builders)  
3. Or when will we call it quits and recap our learning experiences?  I personally think learning from experiments should be celebrated, and [there are a lot of early Gitcoin ventures that didn't work out](https://twitter.com/owocki/status/1736831846439076250) that I'm still proud to have given a shot. 

It pains me to be losing this $$$ much on a product that lacks the confidence of the market.

[quote="sophia, post:8, topic:17304"]
Officially, our USP is that net sequencer fees go to public good projects.
[/quote]

I feel like this USP suffers from two significant drawbacks right now.
1. There are no net-postive sequencer fees rn.
2. There is nothing in it for the builder to choose PGN.  Only a vague promise of future ecosystem benefit.

It seems like until PGN solves its [cold start problem](https://www.nfx.com/post/network-effects-bible#Chicken-or-Egg-Problem-(Cold-Start-Problem)), it lacks a compelling USP that will get dApps and users to consume block space on it.

[quote="sophia, post:8, topic:17304"]
Admittedly, we’ve been playing it safe.
[/quote]

PGN is [default dead](http://paulgraham.com/aord.html) until it hits profitability, so I'd love to see the team behind it playing it less safe + making more decisive moves towards success.
[quote="sophia, post:8, topic:17304"]
I joined the team last month with a specific focus on integrating new technical dependencies, so might be lacking some context.
[/quote]

I'm sorry to hear that you've been put in this position.  

I hope that something or someone emerges to restore confidence in PGN soon.  Or that we move on and pursue other ventures to fund public goods.

-------------------------
