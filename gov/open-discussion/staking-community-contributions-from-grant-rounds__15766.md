---
id: 15766
title: "Staking community contributions from grant rounds"
slug: staking-community-contributions-from-grant-rounds
category: open-discussion
url: https://gov.gitcoin.co/t/staking-community-contributions-from-grant-rounds/15766
created_at: 2023-07-11T14:30:50.630Z
last_posted_at: 2023-07-28T14:15:17.809Z
posts_count: 5
views: 2275
like_count: 12
---

# Staking community contributions from grant rounds

<https://gov.gitcoin.co/t/staking-community-contributions-from-grant-rounds/15766>
thedevanshmehta | 2023-07-11 14:33:59 UTC | #1

I've been thinking for some time on how public goods projects can have perpetual funding streams. An idea I've been mulling around is letting projects allocate community contributions received during a gitcoin grant round into a staking pool. 

Project expenditure = matching funds received + staking rewards earned on community contributions

in traditional philanthropy, ensuring perpetuity of a project is done most famously by universities, through the endowment model. Basically, raise so much money that the interest earned is enough to let your institution survive. If over many rounds the rewards from staked community contributions are enough to pay a basic sustenance for the founding team, it could allow them to unleash their full potential.

Some open Qs:

1. What would it take for gitcoin to give projects the option of putting all community contributions they receive into a staking pool, from where they can receive a monthly stream of rewards? 

Having one entity like gitcoin create the pool (rather than each project doing so individually) would enable higher rewards due to increased volume.

2. Would it be ethical to inform prospective voters that in the event of a project winding up, funds can from the staking pool would be returned to them?

3. Should we let voters decide whether their contribution goes to the project or into a staking pool that perpetually supports the project? Or should projects have the sole discretion of making this call?

Would be curious to know of similar models that are there in web3 and whether this is an interesting avenue for gitcoin to pursue, possibly in collaboration with Aave, Lido & other staking services.

EDIT: Mandatory locking of community contributions into a staked pool supporting a project can greatly improve Sybil defense. Since it locks up funds while the project is active, wash trading becomes more difficult

-------------------------

koday | 2023-07-11 21:20:52 UTC | #2

Thanks for sharing your ideas! I'm particularly interested in this:

[quote="thedevanshmehta, post:1, topic:15766"]
Mandatory locking of community contributions into a staked pool supporting a project can greatly improve Sybil defense. Since it locks up funds while the project is active, wash trading becomes more difficult
[/quote]

On the surface, I think this is a fantastic idea that's worth exploring more. I don't think we could require this for all donations, as there are a significant number of projects who rely on our grants rounds to keep their projects going and need relatively quick access to the funds they've earned. 

However, this could get interesting if we were to reward the projects who commit to locking up the funds for a certain amount of time. It doesn't have to be a huge reward it would be interesting to see how many grants would commit to locking up their funds for X amount of time if we promise them a Y% higher matching funds payout. I do think this could work as a tool for Sybil defense considering projects are much less likely to use their own funds for spoofing donations or spin up/fund multiple wallets if it means they will lose access to those funds for a certain amount of time.

Anyway, this definitely got me thinking and I think there are some ideas here that are worth brainstorming on further.

-------------------------

thedevanshmehta | 2023-07-12 03:16:36 UTC | #3

Super interesting approach of using the carrot of a matching fund boost for enticing projects to stake their community contributions! I also appreciate the feedback on how its more useful as sybil defence than as a continuous revenue stream for projects.

This could potentially address a major pain point in Sybil defence, that there is no * cost * to launching a sybil attack. At the worst you lose gas fees (& your reputation if its something you value) but your capital remains intact. While the effort to identify sybil attacks is expensive for round managers. This would somewhat correct that imbalance by penalizing egregious sybil attackers both through cancelling matching fund payouts & also locking up a % of their capital for a period of time without the corresponding reward that fair play participants receive.

If we had to draw up a go-to-market strategy for the staking feature, what are the main questions to be addressed? Here are some i can think of;

1. Should there be a mandatory minimum (say 5%) of all community contributions that need to be entered into the staking pool? What is the % beyond which there is no additional matching boost for staking more contributions (maybe 50%?) 

2. How would projects (& donors) interact with the staking feature? Would they need to enter the % of community contributions that will go into the staking pool before the round starts or after the round ends? How would this be displayed to donors?

3. What should be the lock-up period for staked funds (maybe 9-12 months?) Can projects increase the staking period for additional matching fund boost? How would the staked funds (& interest earned on them) be returned to projects after the lock-up period is over?

I'm glad this has prompted some thinking, excited to see where it leads !

-------------------------

owocki | 2023-07-12 05:21:21 UTC | #4

[quote="thedevanshmehta, post:1, topic:15766"]
staking rewards earned on community contributions
[/quote]

Checkout what Octant is doing.  For Octant Phase 0, they have 100k ETH staked with the APR going to 10 diff public goods (gitcoin is one of them)   Its pretty similar:

https://www.youtube.com/watch?v=cdDmWEW3ElY

-------------------------

thedevanshmehta | 2023-07-28 14:15:17 UTC | #5

Thanks Kevin! I got to chat with the Octant team in depth during FTC and SP. It seems their 100k staked eth gives 400 ETH every 90 days, which is a hefty amount indeed towards continuous public good funding.

I do see some possible collaboration with Octant (joint staking pool?), while still keeping in mind our separate goals with community staking - improving sybil defense and providing a constant drip for projects to perpetually sustain themselves in low power mode.

-------------------------
