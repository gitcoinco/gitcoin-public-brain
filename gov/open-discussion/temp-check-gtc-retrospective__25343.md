---
id: 25343
title: "[temp check] gtc retrospective"
slug: temp-check-gtc-retrospective
category: open-discussion
url: https://gov.gitcoin.co/t/temp-check-gtc-retrospective/25343
created_at: 2026-07-14T21:19:54.673Z
last_posted_at: 2026-07-17T14:04:51.438Z
posts_count: 10
views: 74
like_count: 13
---

# [temp check] gtc retrospective

<https://gov.gitcoin.co/t/temp-check-gtc-retrospective/25343>
owocki | 2026-07-15 22:00:26 UTC | #1

*a one pager for the [transitionary stewards cohort](https://gov.gitcoin.co/t/temp-check-transitionary-stewards-cohort/25342). first agenda item, first call.*

---

i want to open this cohort with a retrospective of the past gtc era.  (this post is sourced from my [listening tour](https://gov.gitcoin.co/t/gitcoin-listening-tour-learning-from-1-0-2-0-3-0/23350) last year.)

## launch video promises made, promises kept

in 2021 we shipped a launch video and made some promises.

* fund public goods with quadratic funding.
* hand the keys to the community.
* get to the quadratic lands.

watch it again before our first call ([i re-shared it in 2024](https://x.com/owocki/status/1788303295003427129) with my own scorecard attached; feel free to grade differently)

[![Screenshot 2026-07-15 at 1.01.26 PM|365x499](upload://xSjciBhkMMQXGOYfBjkoBF9J1qB.jpeg)](https://x.com/owocki/status/1788303295003427129)

here’s what we said gtc would do in the launch video, scored promise by promise:

* ✅ **gtc used for governing the treasury.** the dao has voted real capital in and out for years: [gcp-001 deployed treasury into gtceth](https://gov.gitcoin.co/t/gcp-001-passed-funding-indexcoop-gtceth-offering/13013), [gcp-002 into rocketpool](https://gov.gitcoin.co/t/gcp-002-passed-rocketpool-odao-participation/13044), plus every seasonal workstream budget since 2021
* ✅ **gtc used to settle disputes.** the akita saga (what to do with a memecoin dumped on the multisig) was [argued and settled by gtc vote](https://gov.gitcoin.co/t/akita-sale-stream-implementation-make-it-a-scheduled-liquidity-pool/4717), with a follow-up vote as recently as may 2026
* ✅ **gtc used to create policy.** governance created its own rules by vote: [the post-vote reconsideration process (gcp-003)](https://gov.gitcoin.co/t/gcp-003-passed-post-vote-reconsider-process/13165), the [governance process itself, versioned and amended](https://gov.gitcoin.co/t/gitcoin-dao-governance-process-v2-updated/7860)
* ✅ **gtc used to ratify grants rounds.** round structures and eligibility went to the token: the [cgrants-to-protocol transition passed snapshot at 99.98%](https://gov.gitcoin.co/t/discussion-feedback-request-grants-protocol-alpha-round-eligibility/11873), the [citizens round (gcp-004)](https://gov.gitcoin.co/t/gcp-004-passed-gitcoin-citizens-round/13462)
* ✅ **gtc used to surface community collections.** shipped in gg24: co-funded domains, with the allocation across domains [decided by gtc-weighted vote on snapshot](https://gov.gitcoin.co/t/temp-check-capital-allocation-governance-research-for-gg24/24202)
* ✅ **gtc used to mitigate sybil attacks.** we pioneered qf sybil resistance as a discipline: gitcoin passport for identity, gtc [identity staking feeding the “price of forgery” score](https://gov.gitcoin.co/t/the-utility-of-gtc/10071), and cocm (cluster-matching qf) making collusion structurally harder
* ✅ **(bonus, unpromised) gtc used to govern allo protocol.** the protocol era put contract upgrades under the token too ([gcp-009](https://gov.gitcoin.co/t/gcp-009-upgrading-gitcoin-s-governance-contracts/14010))

7 for 7 on the letter of it. partial credit on the spirit: some of these didn’t scale, and they weren’t enough to stop people from leaving us for dead.

and beneath the token promises, the receipts of the mission itself:

* feb 2019: the first qf round on gitcoin. $25k matching pool, 200 donors, $38k total to open source ([source](https://gov.gitcoin.co/t/discussion-feedback-request-grants-protocol-alpha-round-eligibility/11873))
* by gr15: $72m facilitated for oss and public goods across 15 rounds ([source](https://gov.gitcoin.co/t/discussion-feedback-request-grants-protocol-alpha-round-eligibility/11873))
* quadratic funding went from a 2018 paper to a mechanism the whole ecosystem runs. octant, giveth, and artizen all fund public goods today with qf or adjacent mechanisms. the idea outgrew the org that shipped it
* the dao formed, decentralized, and still holds a meaningful treasury: over $20m across associated treasuries as of dec 2025 ([source](https://gov.gitcoin.co/t/2026-strategy-from-reset-to-upward-spiral/24967)); see the [q2 2026 budget report](https://gov.gitcoin.co/t/gitcoin-dao-q2-2026-budget-report/25335) for current numbers

the core contract (quadratic funding for public goods, alive in the world, beyond us) held.

## we got out of consensys

a second victory that’s easy to forget. december 2018: eth at $80, consensys laying off staff, gitcoin assigned a “spinout shepherd” and told we had 3 months of capital left. january 2021: we spun out as an independent company. may 2021 (only 3 months later): we launched gtc and handed the thing to its community.

most projects born inside a corporate parent die inside it. this one walked out and became community-owned.

the dao arrangement that followed didn’t work the way any of us hoped, and there’s no blame in that sentence. the independence was real, and that was the plan.

in retrospective we were hopelessly naive about how to make a DAO that actually worked.  if we could have just set the DAO on a better foundation from the start, and with more regulatory clarity, we could have avoided some of the 2021-2025 era pain.

## the pain, the chaos, the strife

honesty is the price of declaring victory

**the dao years hurt.**

civil wars over budgets, workstreams, and direction. [my 2022 disaffiliation.](https://gov.gitcoin.co/t/passing-the-torch/10971) the wind-down of gitcoin 1.0, then 2.0.  the $1.2million/mo spend that turned into (what exactly??). reorgs and layoffs that cost us people we loved. fissures between old friends that haven’t fully healed. years where “governance” consumed energy that should have gone to shipping.

**the hardest part for me:** we lost the lead in a market we created, and we didn’t ship the software we wanted to ship. that one still stings.

and yet. [we created a category big enough](https://x.com/owocki/status/1996972702687797580) that artizen, octant, giveth, and clrfund can fill it. signal ran its own qf round, kickstarter laucnhed a protocol.  dozens of gitcoin copycats launched. [my ted talk](https://x.com/owocki/status/1840769813347483745) carried the funding-public-goods story to a mainstream audience (340k+ views). the ideas won even where our product didn’t. i’m proud of that, and i hold both at once.

we mourn it, name it in the retro, and carry the lessons forward. the dao was an experiment run at full scale with real money and real people. some of it worked. some of it burned.

**on forgiveness.** a retro that only scores the ledger leaves the wounds open. forgiveness is a practice, and it’s how communities heal: name the hurt specifically, separate the person from the moment (most people were doing their best inside a system on fire), say the words (to them if possible, to yourself if it’s too raw), and release the debt. forgiveness doesn’t mean the call was right or the cost wasn’t real. it means you stop reliving the trauma of it. [let go.](https://www.amazon.com/dp/1401945015?lv=shuf&channelId=500&plpRedirect=mhFallback)

*i’m deliberately keeping forgiveness out of the ask section below. it isn’t an enforceable ask, and a gov post can’t assign it as homework. putting it on the agenda would point the room at blame, which is the opposite of the point. it’s an open invitation. take it or leave it, privately, on your own time.*

**on the market:**  the market for public goods funding /crowdfunding tools (and really anything that wasnt DEFI) completely evaporated over the last few years as ETHUSD stagnated and all the risk capital went to AI.  the category is on life support.  we were in some ways on land that was sliding into the sea.

## gtc: down only in vibes

let’s say the quiet part out loud. gtc launched in may 2021 as [a governance token with no economic value](https://gov.gitcoin.co/t/tldr-what-is-gitcoin-aug-2022/8694), a valueless public goods coin, minted to govern a mechanism rather than to make anyone rich. then the bull market swept it up, handed it a valuation far beyond anything it claimed for itself, and the chart has gone one direction since.

so yes: vibes were down only. but a token that promised nothing and governed something was only ever down in vibes. the substance it was minted for (tens of millions to public goods, a community-owned protocol, an independent dao) delivered. if you held expecting number go up, that pain is real and i’m not dismissing it. but i’m also holding that “number go up” was never what was promised (nor was it part of the story). it was an expectation, never an agreement. judged against what it said on the tin at launch, gtc kept its word.

## unforced error: gitcoin media youtube deletion

I wish that whomever was in charge at the time hadn’t deleted Gitcoin Media and all the amazing videos wed painstakingly created/accumulated of our mission and movement from 2017-2026. Talks and research and educational stuff that we did is all just gone. Zooming out, it was an example of the lack of good stewardship that existed in that era.  There was many unforced errors, but this is one that stings a lot to me.

## what’s next

the social contract from the launch video is fulfilled. what it promised now exists in the world, and not all of it was built by us. that counts as winning.

we go boldly forward. the frontier moved from funding open source on ethereum to funding real life, locally. bringing humanity to quadratic lands, or adjacent. gitcoin’s next form points at localism: local funding experiments, starting with node zero this october. your charter as stewards is to transition gitcoin from what it is to what it could be, and to keep us honest while we do it.

## the ask, on this call

1. react to this retro. is the victory earned? what’s missing from the ledger, on both sides?
2. help shape the public version: promises made and promises kept, wins and losses, what’s next.
3. your first act: refer people who would add legitimacy to this process, and tell us how to make the process itself legitimate.

owocki

---

*Disclaimer: This post is for informative purposes only and is not financial advice.*  *This post reflects my personal views ahead of the stewards’ review, not a decision or commitment by Gitcoin governance. Forward-looking items in it, like the october node zero timing, are targets, not commitments.* *The information in these posts is subject to change as we continue learning. This post may contain estimates, may contain errors, and is provided on a best-effort basis. DYOR, do not make any financial decisions based on these posts.*

-------------------------

ashh | 2026-07-15 00:04:09 UTC | #2

I would offer that something about “down only in vibes” feels unfair to what Gitcoin truly built. GTC might be down in certain definitions of value, but those definitions were never the point. Decentralized governance was the point; funding what matters was the point. Gitcoin delivered on both.

I don’t have the internal experience much of this cohort does, but I’ve been an audience member since launch – and what I can share from that perspective, from the outside looking in, is that Gitcoin’s a beloved brand specifically because of the vibes it exported. Good, meaningful, collectively empowering vibes: identity, culture, community – a sense that funding for the people, by the people was something the people could belong to.

I understand the lived internal experience was tumultuous, and I won’t pretend to know what that was like. But that tumultuousness was certainly in no small part a result of building in the early stages of not only an emerging market but, objectively, a paradigm shift. To this day, if you zoom out even slightly, Ethereum is still the wild west. And against the headwinds inherent to that kind of nearly impossible chaos, Gitcoin still built something that endures – in Giveth, Octant, Artizen, Clr.fund: more equitable funding mechanisms that put power back in the hands of the people.

That’s a legacy to be proud of. And if putting power back in the hands of the people isn’t vibes, then I’m not sure what is 💚

-------------------------

MathildaDV | 2026-07-15 16:42:37 UTC | #3

Having been around for 4 of these years, I've been in the middle of most of these changes, reorgs, the high successes and the so-called failures. I agree with @ashh: not all is bad or "down."

Yes, there have absolutely been missteps and it was very difficult for many involved, but we have to remember the legacy that we have built: distributing $70M+ to public goods, and making a lasting impact on the Ethereum ecosystem. We seeded projects that now sit at the backbone of the Ethereum ecosystem, and through every bear market kept showing up to fund what mattered most at that time. Look at who has followed in our footsteps and who now runs QF rounds of their own. The category we created outgrew us, and that's something to be very, very proud of. I hope we never lose sight of it.

On what I'd add to the ledger: the ecosystem itself has shifted dramatically in the past year. PGF is basically DED, projects and platforms are shutting down, and many high-value people and teams have moved away from the instability. Gitcoin has always been held by the ecosystem, and vice versa. Any honest retro has to name that some of what reads as our failure is at least in part category collapse, not all execution.

On forgiveness: my instinct is that we heal by building, not by re-litigating. Taking accountability where needed is very important of course (and we shouldn't shy away from it), but rehashing every mistake before we move forward? Probably not necessary.

We're rebuilding inside an era that has been unforgiving to many. We won't succeed in this new era without making difficult calls about what to sunset and what to double down on, and I'd rather spend the majority of the cohort's energy there than on the wreckage behind us. 

*(dropping more detailed thoughts on the stewardship cohort on that post separately)*

-------------------------

ccerv1 | 2026-07-15 21:49:51 UTC | #4

One thing I would add to the ledger: GTC was a special attractor of people, talent, and ideas. It created a uniquely big tent.

I remember saying something like this to Kevin around 2022 and he said “Nah, that’s just Ethereum.” In retrospect, I think that was too humble. If you randomly sampled different pockets of Ethereum during those years, there really was something differentiated about GTC holders.

Gitcoin was also one of the few things in crypto that you could explain fairly easily to normies. It onboarded a lot of people into the space. It nerd-sniped a lot of nerds. Even when people eventually went elsewhere, they took Gitcoin memes and values with them.

The other side of that story was high turnover. I think that made it very hard to sustain momentum and compound knowledge. For a while, the only thing you could count on was that some kind of Gitcoin Grants round would happen each quarter. The software, contracts, matching funders, chains, sybil resistance, org structures, etc were constantly changing.

That instability was not only a product problem. A lot of talented and committed people crashed out. The human cost of the GTC experiment belongs in the retro somewhere alongside the capital deployed and mechanisms created.

Anyway, Mathilda said it best:

> We heal by building, not by re-litigating.

-------------------------

owocki | 2026-07-15 22:03:38 UTC | #5

[quote="ccerv1, post:4, topic:25343"]
I remember saying something like this to Kevin around 2022 and he said “Nah, that’s just Ethereum.”

[/quote]

> [![Screenshot 2026-07-15 at 4.01.29 PM|690x269](upload://vLw1AAli1yxEA67xlth57fPkn0B.png)](https://x.com/owocki/status/1460374660139270151)

i still believe it.  for all its faults, ethereum is a beacon for hope for the world.

gitcoin can be too (again).  just needs the right config.

[quote="ccerv1, post:4, topic:25343"]
The human cost of the GTC experiment

[/quote]

im supportive of hearing learnings to the extent we keep chatham house rules (eg Chatham House Rule: use the ideas, not the names. Participants may share what was said, but not who said it.).  and with the intent to learn/sensemake!

-------------------------

skilesare | 2026-07-15 23:18:06 UTC | #6

I’ll add another perspective to the retrospective.

First, a little solidarity: nearly everyone in the broader crypto ecosystem is getting battered right now. I share the following mostly as context and an alternative perspective. During periods of extreme volatility, it can help to know that you are not the only person looking back at what might have been.

Our paths diverged after your *You’ve Got ETH* days at the Dappathon. I was super impressed with your approach to things, way of working, etc. You leaned further into the Ethereum ethos and built Gitcoin. I thought I could pursue a different theory: if you want to change established institutions, sometimes you have to make them believe you are joining them.

For a while, that path seemed promising. We came close to bringing decentralized technology into several major institutions and industries. A combination of corporate politics, geopolitical events, layoffs, and terrible timing repeatedly got in the way. At one point, I thought I was exceptionally well positioned. In hindsight, I underestimated how much organizational dysfunction, ego, incentives, and plain bad luck shape the outcome of even technically strong ideas.

When Ethereum moved away from execution sharding and toward a rollup-centric scaling roadmap, I became convinced that DFINITY’s sharding approach would eventually prove compelling. I imagined Ethereum might return to something similar, or that the two ecosystems might find a way to converge.

That was naive. I did not have visibility into what was happening inside DFINITY, and I did not fully appreciate the financial incentives driving the emerging L1 and L2 landscape. Technical merit alone was never going to determine the winner. I still believe DFINITY made some excellent technical choices, but being technically right is not enough when the surrounding incentives, culture, developer experience, and ecosystem strategy are misaligned.

I was often jealous that I had not stayed as close to the metal as Gitcoin did. I remained a cheerleader from the sidelines and eventually tried to raise funding for ICDevs.org through several Gitcoin Grants rounds. We even raised money to explore bringing an EVM environment to the DFINITY ecosystem.

That experience also showed me some of the limitations of ecosystem-based funding mechanisms. Because many of our supporters were not regular Ethereum participants, the matching algorithms did not recognize our donor community particularly well. It felt as though we were being penalized for trying to build a bridge from outside the existing network.

I was stunned when ICP launched with so little meaningful Ethereum integration or interoperability. To me, it was one of the clearest opportunities available. Had the network launched in 2021 as an accessible, push-button environment for deploying EVM applications, whether positioned as an L1, L2, or complementary execution platform, I believe its trajectory could have been very different.

Instead, once the importance of the EVM opportunity became obvious, the work was left to a small team without the resources or institutional support needed to succeed. The effort faded just as it was beginning to become usable, and my recurring dream of bringing parts of the Gitcoin stack to DFINITY was postponed again.

I remember sitting at Schelling Point in Colombia, listening to Fabian Vogelsteller describe the vision for LUKSO and thinking, “The Internet Computer already does that.”

What I failed to add was: “But it is not EVM-compatible, so most of this audience has no reason to care.”

And those were the good times.

On DAOs, I learned a great deal from Gitcoin and the projects around it. *GreenPill* gave me a huge number of ideas. Sov provided a thoughtful interview for my DAO book project, which came out around the same time as yours.

But some of my most powerful lessons came from watching the DFINITY ecosystem struggle with governance, particularly through the launch of the SNS framework. Gitcoin appeared to be wrestling seriously with the human, cultural, and institutional questions behind decentralized governance. DFINITY’s approach often felt more like a technically complete mechanism in search of a community and a soul.

Unsurprisingly, many of the resulting DAOs struggled. Some failed for reasons similar to the problems you identify in the GTC era. Others failed far more dramatically.

That broader context is why I would encourage everyone involved with Gitcoin to hold their heads up, identify the pieces that genuinely worked, and keep building from them.

Perspective is difficult when things are painful.

The thought I keep returning to(probably unhelpfully, given the dangers of dwelling on spilled milk) is: what could we have done with those resources if we had also possessed today’s AI capabilities?

Over the past few months, I was finally able to build the damn EVM implementation for DFINITY’s “Internet Computer” that another effort had spent years and millions of dollars pursuing(and to understand why they probably failed). That achievement arrived at a strange moment, when the ecosystem it was intended to serve was already transforming into something very different from what many of us once imagined and shedding community at an alarming rate.

But perhaps that is also the opportunity.

For anyone looking to refocus on the application layer, it is difficult to imagine a more powerful time to be alive. Small teams can now attempt projects that previously required years of funding and large organizations.

The hardest lesson for me has been accepting that it was never only about the technology, no matter how much I wanted it to be.

Metcalfe’s law is made of people. It always was.

Gitcoin attracted a remarkable collection of builders, thinkers, idealists, and community members. Perhaps it did not retain every person or assemble every ingredient required to achieve all of its hopes. But many of those dreams were lived. Real mechanisms were tested, real public goods were funded, real communities formed, and ideas escaped into the wider world.

That is worth celebrating.

Congratulations on what Gitcoin and the GTC community accomplished. I’m here for the fourth iteration.

-------------------------

owocki | 2026-07-16 02:58:36 UTC | #7

thanks for stopping by austin. its been interesting to follow your journey as well.

[quote="skilesare, post:6, topic:25343"]
First, a little solidarity: nearly everyone in the broader crypto ecosystem is getting battered right now. I share the following mostly as context and an alternative perspective. During periods of extreme volatility, it can help to know that you are not the only person looking back at what might have been.

[/quote]

from wikitionary:

> Solidarity is a bond of unity and mutual support among individuals or groups who share common interests, goals, or struggles. It turns the feeling of shared humanity or shared responsibility into active, concrete assistance, ensuring that no one has to face difficulties alone.

i think that the solidary bit is interesting and important because it helps me (and if you think like me, us) to feel like were in it together, that prosocial web3 (or even prosocial contemporary society) is even possible. that interdependence can be really powerful if it is stoked skillfully. 

sometimes it feels like the fabric of that solidary is torn when number not go up, if we suffer setbacks, if we dont show up in our most skillful/mindful/authentic selves to each other.  i have found that, through many landmines, it is possible to work through many things (but not all things). lets try and hold this solidarity through the next cycle (or whatever replaces cycles going forward :stuck_out_tongue: ), and to the degree that we can do so skillfully/authentically, moving forward.


i am reminded here of the famous Elon Musk quote “a start-up is like chewing glass and staring into the abyss. after a while, you stop staring, but the glass chewing never ends”.  that feeling peaked for me in the 2019 bear, the 2025 bear, hard.  we used to call our management meetings at the end of Grants Lab/Grants Stack era “staring into the void” lol.  as a way of coping with the pain of the glass chewing together in solidarity.

one thing i can say is i hope i personally have gotten a lot of practice in glass chewing + void staring, which could mayhaps, over time, help learn to prefigure culture that can hold solidarity (within whatever constrains i was given) more skillfullly/mindfullly/authentically over time.  and also achieve great things.  as they say, if you want to go fast go alone, if you want to go far go together.  i think the 2017-2022 era (right up until disaffiliation) was my “go fast alone” era, now i hope my 2025 (my reaffilliation with gitcoin) is my “go far together” era.

*Disclaimer: This post is for informative purposes only and is not financial advice.* *This post reflects my personal views ahead of the stewards’ review, not a decision or commitment by Gitcoin governance. Forward-looking items in it, like the october node zero timing, are targets, not commitments.* *The information in these posts is subject to change as we continue learning. This post may contain estimates, may contain errors, and is provided on a best-effort basis. DYOR, do not make any financial decisions based on these posts.*

-------------------------

MconnectDAO | 2026-07-17 03:49:51 UTC | #8

Thanks for this honest retrospective, owocki.

The 7/7 scorecard on GTC’s functional promises is well-documented and worth acknowledging. But as stewards evaluating this ledger, I think there are critical data gaps that need to be filled before we can call this retro complete:

1. Token holder impact  The post frames GTC’s price decline as “vibes only,” but thousands of community members held GTC based on ecosystem faith. Where’s the data on holder demographics, average holding loss, and how this affected contributor retention?

2. Treasury spend accountability  $1.2M/month is named but not broken down. Which workstreams consumed what, and what did each deliver? A retro without spend-to-output mapping leaves the hardest question unanswered.

3. Allo Protocol adoption metrics  GTC governed the protocol. What did the protocol actually achieve? TVL, integrations, active rounds run on Allo would give this retro credibility beyond narrative.

4. Gitcoin Passport numbers Sybil resistance was a flagship use case. Real numbers (verified wallets, attack reduction %) would show whether this was a win or just infrastructure.

5. Node Zero / Localism plan  “October” is a target, not a plan. What’s the funding model, success metric, and governance structure for this next phase?

The honesty in this post is appreciated. But a complete retro needs data where there are currently only stories. Happy to help compile any of these if the forum can point to existing reports.

-------------------------

owocki | 2026-07-17 13:42:21 UTC | #9

i would support having someone who has data skills pulling together some data (especialy allo, grants stack, passport adoption numbers!)

-------------------------

MconnectDAO | 2026-07-17 14:04:51 UTC | #10

Appreciate the willingness to support someone pulling the Allo / Grants Stack / Passport data. To make this retro actionable for stewards, we probably need:
 A rough owner  timeline for compiling these numbers
 Clarity on whether treasury spend breakdown  token holder impact analysis are also in scope
If there’s an internal analytics/reporting person I can collaborate with, I’m happy to help structure the data needs from the governance side.

-------------------------
