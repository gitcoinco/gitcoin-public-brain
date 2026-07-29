---
id: 5404
title: "Resolving Snapshot Votes Without Quorum"
slug: resolving-snapshot-votes-without-quorum
category: governancevision
url: https://gov.gitcoin.co/t/resolving-snapshot-votes-without-quorum/5404
created_at: 2021-06-07T20:18:23.947Z
last_posted_at: 2021-06-11T18:56:54.811Z
posts_count: 5
views: 2689
like_count: 14
---

# Resolving Snapshot Votes Without Quorum

<https://gov.gitcoin.co/t/resolving-snapshot-votes-without-quorum/5404>
ceresstation | 2021-06-07 20:18:24 UTC | #1

So given that we're still releasing treasury funds, hitting quorum is still relatively hard to do in many cases. For example, this vote was overwhelmingly positive with about 99% of turnout voting yes:

https://gov.gitcoin.co/t/rfc-transfer-sacks-lp-position-to-gitcoin-governance-timelock/3262/7

Even if 1m votes came in against and quorum was reached this would have passed. In these scenarios, given we're early on in governance and that even with quorum it would have passed, should we simply count these kinds of votes as ratified?

cc @monet-supply @Yalor @HelloShreyas and others who participated in the initial thread!

-------------------------

HelloShreyas | 2021-06-07 21:44:21 UTC | #2

I like the idea of using a soft quorum, but could we have a standard policy in place? We could use one of these options or something else:

* Temporarily change quorum from 2.5 million to something lower (e.g. 1.5 million)
* Temporarily change quorum from 2.5 million to something lower (e.g. 1.5 million) **and** require that the proposal should have passed even if all votes to get to 2.5 million voted against the proposal.
* Require 2.5 million quorum on critical decisions (call it "hard quorum") but lower quorum on other decisions (call it "soft quorum")

-------------------------

cupOjoseph | 2021-06-08 01:45:34 UTC | #3

[quote="ceresstation, post:1, topic:5404"]
should we simply count these kinds of votes as ratified?
[/quote]

Yes, we will not get anything done if we dismiss largely popular things that miss quorum by a small margin.

-------------------------

monet-supply | 2021-06-10 02:46:11 UTC | #4

I think quorum thresholds are somewhat less important for Snapshot votes because they don't directly execute any transfer - a clearly malicious proposal that makes it through with low participation can always be rejected by multisig signers. 

That being said, it definitely helps give governance a greater sense of legitimacy to make formal procedures/standards for this - Index Coop stands out as a protocol with well specified processes around snapshot voting. 

A low quorum threshold for snapshot votes should work fine (maybe anywhere from 100k-500k GTC) considering the low security concerns. Maintaining the existing 2.5% quorum requirement for on chain governance is probably best for now, as this has direct control over funds in the treasury.

-------------------------

imfredmi | 2021-06-11 18:56:54 UTC | #5

i can't agree with you any more :100: :100: :100:

-------------------------
