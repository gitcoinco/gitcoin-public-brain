---
id: 22949
title: "[PROPOSAL] Withdrawing remaining fees from PGN back to the Gitcoin Foundation Q2 2026 (Original Q4 2025)"
slug: proposal-withdrawing-remaining-fees-from-pgn-back-to-the-gitcoin-foundation-q2-2026-original-q4-2025
category: pgn
url: https://gov.gitcoin.co/t/proposal-withdrawing-remaining-fees-from-pgn-back-to-the-gitcoin-foundation-q2-2026-original-q4-2025/22949
created_at: 2025-08-14T02:37:09.071Z
last_posted_at: 2026-04-26T16:58:22.510Z
posts_count: 15
views: 2063
like_count: 15
---

# [PROPOSAL] Withdrawing remaining fees from PGN back to the Gitcoin Foundation Q2 2026 (Original Q4 2025)

<https://gov.gitcoin.co/t/proposal-withdrawing-remaining-fees-from-pgn-back-to-the-gitcoin-foundation-q2-2026-original-q4-2025/22949>
deltajuliet | 2026-04-16 22:58:15 UTC | #1

## TL;DR

[PGN completed its shutdown in October 2024](https://gov.gitcoin.co/t/pgn-shutdown-a-recap/18794) and [the BalanceClaimer contract](https://gov.gitcoin.co/t/updating-pgns-contract-to-make-funds-easier-to-claim/19569) is working as intended. With the network fully wound down, I am proposing to withdraw the remaining unclaimed funds back to the Gitcoin Foundation treasury in November 2025 (and splitting 50/50 with the Gitcoin Treasury). I'm hoping this post may prompt users that hadn’t claimed to execute, which is great - and I’d love to see the remaining funds refunded back to Gitcoin as one of the final tasks upon my exit. 


## Current situation

When we shut down PGN in October 2024, we implemented the BalanceClaimer contract to handle user funds recovery. This process remains active and will continue - users can still claim their remaining assets without any deadline pressure as it stands today and will remain as such until we ratify this proposal (or another like it). 

The network currently holds approximately $900K from accumulated sequencer fees due to ETH’s current trajectory. With PGN's operational phase complete, these funds are now sitting idle on the shut down network. Further data [here](https://l2beat.com/scaling/projects/publicgoodsnetwork). 


## What I'm proposing

Withdraw the remaining funds from PGN in November 2025 return them to the Gitcoin Foundation treasury that originally funded the network.  **I also suggest splitting the difference and sending 50% of this back to the Gitcoin Timelock*. While it wouldn't put the Foundation in profit for it's funding to create the L2, it would cover the legal, administrative and operational costs for the Foundation (which are minimal) for another few years - I've currently been able to extend the runway from the OG funding request from 2 years to nearly 5 more and I'm kinda happy the Foundation has been able to mitigate some of our legal and operational challenges without requesting further funds. 

This ensures the capital from PGN's experiment gets put back to work funding public goods rather than remaining unused on a discontinued network. The Foundation took the risk on PGN, and these fees should flow back to support ongoing public goods initiatives, given the skeleton crew of the Foundation and the massively fantastic work from @kyle @enidavis, @sophia and @lebraat that worked on making this initiative happen. Thanks y'all, again. 


## Next steps

If this temp check shows community support, we can turn it into a formal proposal for the community to ratify w/ a Snapshot vote. 

Thoughts? Shall we claim the funds back from PGN back to the Foundation and send 50% back to the Gitcoin Treasury? How can we ethically support the legacy of PGN while also giving back to the organization that funded it and make these funds a boon for PG?

-------------------------

owocki | 2025-08-14 02:43:51 UTC | #2

What kind of efforts have been made to reach out to users who could claim via the BalancerClaimer to notify them they can get those funds? 

-----

FYI I asked chatgpt "how long do funds have to sit somewhere before they are considered abandoned, legally, ethically, and morally?" and this is what it said:

-----
**Legal:**

* **Bank accounts (U.S.)** – Usually deemed abandoned after **3–5 years** of no activity.
* **Custodial crypto accounts** – No uniform law; depends on the platform’s terms. Many mirror bank rules (1–5 years of inactivity).

**Ethical:**

* Make reasonable efforts to contact the owner before treating funds as abandoned.

**Moral:**

* Act as a steward: return if possible; if not, use for good rather than let it sit idle.

-------------------------

kyle | 2025-08-14 20:28:01 UTC | #3

@deltajuliet - How much is still remaining, do you know? And is this something anyone can do (ie a specific contract call open to public), or only an approved wallet address?

@owocki - Perhaps we expend too much energy contacting people, we figure out how much it is and if the juice is worth the squeeze.

-------------------------

deltajuliet | 2025-08-17 21:38:43 UTC | #4

@owocki Messaging was sent out via Socials (X), Telegram and via email once we established the bridge for users to claim back in Fall 2024. I would suggest a cooldown period where we do the same again if this proposal pushes through. Including amping up this post so the community has time and visibility to react. 

@kyle I buried the lede a bit in the paragraph above w/ the link to L2 Beat. There is ~$900K still sitting on on the network. Nearly double the USD amount w/ ETHs current pricing and excluding operational costs, PGN was ~220 ETH in fees over the course of it's existence. https://l2beat.com/scaling/projects/publicgoodsnetwork

![Screenshot 2025-08-17 at 15.28.51|690x244](upload://u0nvVnJkMw5hugCE6pMcizIBSkw.png)


Gitcoin has the deployer address - and will be able to claim back via the contract with some light support from our partners. 

Looking forward to hearing pushback, suggestions and feedback!

-------------------------

owocki | 2025-08-17 22:55:02 UTC | #5

do we think there is any brand risk here?  do we think we are doing right by people here?  one thing i've found about web3 is you can be really thoughtful, persistent, try to do right by people, and they still accuse you of rugging them without even checking the gov forum to see why we did what we did and how thoughtfully we did it.  it feels like we've diluted the meaning of that word to just mean "something i dont like".  but then again, i cant help but wonder what we could do to protect the brand and do right by people here.

-------------------------

thedevanshmehta | 2025-08-18 02:05:11 UTC | #6

So Aragon faced a similar issue, after they decided to withdraw their token. In their case, over $20 million was left unclaimed and under Swiss law they could only allow claims for 1 year.

AFAIK, they decided to move the funds to a separate foundation. Worth looking at them as a case study for guidance on how to tackle the situation

-------------------------

deltajuliet | 2025-08-20 00:54:08 UTC | #7

Thanks all, 

@owocki I get that no matter how much care or communication we put into this, someone will be upset. That’s the nature of the space—we conflate “doing something I didn’t like” with “being malicious.”

@thedevanshmehta great point but from a legal standpoint there isn't much to relate back to Gitcoin's jurisdiction including but not limited to the structure of how the funds were raised for both orgs (appreciate it though!). 


Either way it's pretty straightforward: the network is shut down, the claim contract is still live, and we’ve communicated consistently. These funds are sitting idle. We’re proposing a final step to close the loop and put the capital back to work for public goods. @owocki we can throw out a couple more comms in the meantime. 

We’ll keep being clear about what we’re doing, why we’re doing it, and then we’ll do it. That’s about the only lever we have against the inevitable noise and I think that's a strong case for giving the funds to funding public goods.

-------------------------

griff | 2025-11-10 20:24:52 UTC | #8

I'm confused... is the $900k Sequencer Fees? Or is it from users?

Do we have a list of addresses with balances on the network?

Can people still claim? Does the RPC even work?

I think it's fine to clawback the funds, but we should at least publish a list of addresses with funds somewhere so people can claim.... The UX of claiming was really hard if I recall.. it was like make a tx, come back later, make another tx, come back 7 days later... then come back and make another tx! A lot of people would get lost in that.

I am doing this right now with "Graceful Exits" for tokens from q/acc that want to get rid of their token, but there is a lot of collateral in Bonding Curves that can be claimed... we are only giving 21 days... but its VERY easy to see who can claim cause everyone has tokens, and I dm everyone I know so they can try to get their money back.... If there was a list then this would be pretty trivial... put the list out, give a week or 2 and call it good.

I'm going to vote no, mostly so the message is read, if a list of users with funds is put out publicly, and a little bit of extra time is given to claim then I'd support the claw back :-D

-------------------------

deltajuliet | 2025-11-11 01:00:40 UTC | #9

Thanks, @griff! 

These are user funds still on the network. Users have always been able to claim - more information on how to do it is [here](https://docs.publicgoods.network/using-pgn/claiming-old-funds) and within the documentation is the list of addresses. Also linked [here](https://docs.publicgoods.network/funds-proofs.txt). 

The previous claiming process has been updated to make it easier to claim directly from the contract, as outlined in the documentation linked above. 

OG post on EOL of PGN was published June 2024 and [I published a recap in November 2024](https://gov.gitcoin.co/t/pgn-shutdown-a-recap/18794). :) 

@owocki Maybe with your socials you can post this thread again?

-------------------------

owocki | 2025-11-11 20:53:26 UTC | #10

[quote="deltajuliet, post:9, topic:22949"]
@owocki Maybe with your socials you can post this thread again?
[/quote]

tweeted about it [here](https://x.com/owocki/status/1985896168233320652)! 

not sure if this is optimised for conversion rate tho.

-------------------------

owocki | 2025-11-11 20:54:14 UTC | #11

[quote="owocki, post:2, topic:22949"]
* Make reasonable efforts to contact the owner before treating funds as abandoned.
[/quote]

worth thinking about what else we could do to contact the owners of these addresses to get them to pull their funds... since theres no real onchain messaging standard its hard to know what that would be.

-------------------------

MathildaDV | 2025-11-12 12:56:12 UTC | #12

I would recommend another communication rollout plan for this and letting users know that by they have a final chance until X date to withdraw. I've learned that once has to communicate multiple times to make sure nothing gets lost. I can work on this with the team to roll out after Devconnect

-------------------------

deltajuliet | 2026-04-16 23:00:28 UTC | #13

Proposal is live on Snapshot: https://snapshot.box/#/s:gitcoindao.eth/proposal/0xac01be13caef126ab758c160f91a7a0c616f94d15a3890872d485966d3869e56

-------------------------

owocki | 2026-04-17 14:30:52 UTC | #14

[quote="owocki, post:11, topic:22949"]
[quote="owocki, post:2, topic:22949"]
* Make reasonable efforts to contact the owner before treating funds as abandoned.

[/quote]

[/quote]

i will be voting for this proposal, mainly to close out this era of gitcoin history, and bc i have seen plenty of efforts to contact anyone who has funds leftover.

-------------------------

narcov_eth | 2026-04-26 16:58:22 UTC | #15

I support this proposal and agree with @owocki.

At this point, closing out the PGN chapter and putting the remaining funds back to work for Gitcoin feels reasonable, as long as the final communication remains clear and visible.

-------------------------
