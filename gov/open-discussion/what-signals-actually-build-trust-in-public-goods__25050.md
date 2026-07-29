---
id: 25050
title: "What Signals Actually Build Trust in Public Goods?"
slug: what-signals-actually-build-trust-in-public-goods
category: open-discussion
url: https://gov.gitcoin.co/t/what-signals-actually-build-trust-in-public-goods/25050
created_at: 2026-01-12T22:04:25.862Z
last_posted_at: 2026-03-14T11:54:29.075Z
posts_count: 9
views: 161
like_count: 10
---

# What Signals Actually Build Trust in Public Goods?

<https://gov.gitcoin.co/t/what-signals-actually-build-trust-in-public-goods/25050>
Petition.io | 2026-01-12 22:04:25 UTC | #1

Trust plays a central role in how public goods work, especially in decentralized ecosystems where participants may never meet, and where impact can be hard to quantify.

Within Gitcoin, trust seems to emerge from many different signals: past grant history, open-source contributions, community endorsements, transparency in communication, on-chain activity, or even long-term presence in the ecosystem. Different participants may weigh these signals very differently depending on whether they’re builders, donors, reviewers, or stewards.

From our perspective at **Petition.io**, thinking about trust has been unavoidable. As we build tools that rely on broad participation and public confidence, we’re constantly reflecting on what makes a project feel credible without relying on centralized verification or traditional institutional backing.

I’m interested to know how do newer projects earn trust without an established track record?

-------------------------

nya-elimuai | 2026-01-29 13:27:41 UTC | #2

@Petition.io I suppose trust can be built into a project by enforcing donated funds to flow through a transparent system.

In our case, we are using a *Drip List* so that donors can easily see what type of work is funded, and who the end recipients are: https://www.drips.network/app/drip-lists/41305178594442616889778610143373288091511468151140966646158126636698

With this setup, a donor doesn’t have to worry about funds being mismanaged/wasted since everything is transparent and 0% goes to admin overhead.

I believe this is how the most efficient non-profits will operate in the future.

-------------------------

Petition.io | 2026-01-30 19:22:25 UTC | #3

Thanks for sharing this, I agree that building transparency directly into how funds move is a strong way to establish trust early on. Making the recipients and funded work visible by default removes a lot of uncertainty.

From our side at Petition.io, this is something we think about a lot as well, especially how transparency fits alongside other trust signals over time, like consistency, follow-through, and community feedback.

-------------------------

Pablo | 2026-02-27 00:59:17 UTC | #4

From my experience building in African markets, trust signals look different than in Western crypto contexts. On-chain history matters, but what actually moves communities is demonstrated presence showing up at local hackathons, being known in local developer communities, and having people vouch for you face to face. The interesting challenge is how to translate that off-chain social trust into something Gitcoin's quadratic funding can actually read and amplify. That gap feels like an opportunity for a signal layer that's community-attestation based, not just contribution history.

-------------------------

Petition.io | 2026-02-27 21:56:47 UTC | #5

This really resonates. Reputation is relational, being present, known, and vouched for carries weight. The challenge you pointed out is powerful, how do we translate that off-chain social capital into something funding mechanisms like quadratic funding can recognize? That gap definitely feels like an opportunity for community-driven attestation models.

We are open to hear more contributions on this topic.

-------------------------

Pablo | 2026-03-03 21:04:39 UTC | #6

Glad it resonates. To push it further  a community-attestation layer could work as a trust primitive that sits alongside contribution history, not replace it. The idea: local nodes (developer communities, hackathon organizers, DAOs operating on the ground) issue attestations for builders they've directly interacted with. Not just "this person contributed code" but "this person showed up, taught others, shipped under real constraints."

In  Africa specifically, some of the strongest builders I've seen have no GitHub trail worth mentioning, but they've won hackathons, trained 50 students, and kept communities alive through infrastructure blackouts. That signal is real. It just has no current path into a QF mechanism.

The gap isn't just technical — it's about who gets to define what credibility looks like. If Gitcoin's signal layer is built only around on-chain and open-source activity, it will keep systematically underweighting builders from ecosystems where those aren't the primary modes of participation.

A starting point could be EAS (Ethereum Attestation Service) — local community leads issuing structured attestations that can be aggregated and weighted in Gitcoin's matching logic. The trust chain is: community knows builder → community is trusted by the protocol → attestation carries weight.

Happy to explore what this could look like in practice, especially for emerging market contexts.

-------------------------

Petition.io | 2026-03-05 20:54:33 UTC | #7

I like the framing of community attestations as a trust primitive alongside contribution history. That feels like a more complete way to capture credibility.

EAS also is a practical starting point for experimenting with this kind of signal layer.                                                                                             
Curious how you think those attestations should be weighted or verified so the system remains credible at scale.

-------------------------

Pablo | 2026-03-12 18:53:22 UTC | #8

A few principles I'd suggest:

First, attestations should decay. A voucher from 2 years ago that was never renewed shouldn't carry the same weight as one refreshed this quarter. Trust is maintained, not minted once. Time-weighted attestations prevent stale credibility from accumulating.

Second, the credibility of the attester matters more than the volume of attestations. One attestation from a community node that has itself been attested by multiple other nodes should outweigh 20 attestations from unknown wallets. This is where you get a trust graph, not just a list. The weighting logic could borrow from eigenvector-style ranking -- your attestation carries weight proportional to how much trust is placed in you.

Third, verification at scale probably means accepting that not all attestations are equal and being transparent about it. You could tier them: self-declared (lowest weight), peer-attested (medium), and institutionally attested by a recognized community node (highest). The system doesn't need to verify every claim -- it needs to make the cost of faking credibility higher than the cost of earning it legitimately.

The attack vector to watch is attestation rings – groups of wallets vouching for each other with no real activity behind it. Countermeasures could include requiring attesters to stake reputation (their own attestation score drops if their vouched builders don't follow through) and cross-referencing attestation claims against minimal on-chain or off-chain activity signals.

None of this needs to be perfect at launch. A pilot with 5-10 community nodes in different regions issuing EAS attestations, with Gitcoin weighting them experimentally in one round, would generate more useful data than trying to design the full system upfront.

-------------------------

Archie-Ray | 2026-03-14 11:54:29 UTC | #9

New projects can build trust through transparency, clear goals, early community engagement and showing real contributions, even without a long track record.

-------------------------
