---
id: 16772
title: "Gitcoin WalletGuard 🛡️"
slug: gitcoin-walletguard
category: open-discussion
url: https://gov.gitcoin.co/t/gitcoin-walletguard/16772
created_at: 2023-10-17T15:32:09.550Z
last_posted_at: 2023-11-12T19:07:57.094Z
posts_count: 8
views: 3750
like_count: 29
---

# Gitcoin WalletGuard 🛡️

<https://gov.gitcoin.co/t/gitcoin-walletguard/16772>
owocki | 2023-11-08 20:42:27 UTC | #1

There was recently an [incident in which Treasury Funds were mistransfered from the Gitcoin TimeLock](https://gov.gitcoin.co/t/incident-regarding-mistransferred-treasury-funds/16683) (Treasury) to a dead address. As a result, 521.44K GTC was lost.

I propose a new scheme to avoid having such issues in the future.

## Gitcoin WalletGuard

Introducing the Gitcoin WalletGuard, a decentralized group of individuals who are responsible for making sure the code on Gitcoin Treasury proposals match the textual description of the proposal.

What is expected of a member of the Gitcoin WalletGuard?

1. Monitor https://www.tally.xyz/gov/gitcoin/proposals
2. For any new proposal, click to the ‘executable code’ tab, and verify that the code matches the intent of the proposer.
3. After you’ve verified this, post the SUCCESS TEXT (see below) on the gov.gitcoin.co post for the proposal.
4. If the code does not match the intent, then post the FAIL TEXT (see below) on the gov.gitcoin.co post for the proposal.

In return for this vigilance, the Gitcoin WalletGuard will be rewarded with a POAP. A new POAP will be issued every quarter.

It is POSSIBLE (but not guaranteed) that active membership in the Gitcoin WalletGuard will lead to future participation in Gitcoin Citizens rounds and/or other rewards.

I will monitor the number of people who participate, and will advise CSDO the gov forums if the level is healthy or not. In the future, this responsibility could be decentralized to someone else.

-----

## POAP

![|624x273](upload://5UNPvF94ENjVj6Xi0D685DGy8Ci.jpeg)

## SUCCESS TEXT

**(bolded text to be replaced with custom text from writer)**

I **(owocki.eth)** am a member of the [Gitcoin WalletGuard](https://gov.gitcoin.co/t/gitcoin-walletguard/16772). 🛡️🛡️🛡️

I’ve verified that the code on this proposal matches the intent of the proposal.

If you are interested in joining the Gitcoin WalletGuard [click here](https://gov.gitcoin.co/t/gitcoin-walletguard/16772).

## FAIL TEXT

**(bolded text to be replaced with custom text from writer)**

I **(owocki.eth)** am a member of the [Gitcoin WalletGuard](https://gov.gitcoin.co/t/gitcoin-walletguard/16772). 🛡️🛡️🛡️

The code on this proposal does not match the intent. **It will send tokens to a dead address** ❌❌❌

If you are interested in joining the Gitcoin WalletGuard [click here](https://gov.gitcoin.co/t/gitcoin-walletguard/16772).

-------------------------

QuickMythril | 2023-10-17 15:47:06 UTC | #2

seems like an interesting and positive idea.  i would probably be willing to help with this.  i do have some questions though.  how would the members of the guard be selected, just whoever volunteers?  isn't this something that the signers should all be doing before signing anyway?

-------------------------

owocki | 2023-10-17 18:43:09 UTC | #3

>  how would the members of the guard be selected, just whoever volunteers? 

just whoever volunteers for cohort 1.

>  isn’t this something that the signers should all be doing before signing anyway?

yes ideally the voters are also checking this.   we are following the philosophy of ethereum, whereas anyone with 32 eth can run a full validating node, constant vigilence is expected from many members of the community (even those without 32 eth) to validate/check blocks.

-------------------------

jaxcoder | 2023-10-17 18:56:09 UTC | #4

Happy to volunteer 👀 Let me know how I can help.

-------------------------

owocki | 2023-10-17 18:59:12 UTC | #5

the first step would be to validate any proposals (eg check the execution code matches the intent of the proposal, and then comment on the gov post for it) on tally for s20 budgets as they come in!

i will distribute the POAPs after budgeting season!

-------------------------

carlosjmelgar | 2023-10-19 20:23:56 UTC | #6

Cool way to gamify community participation and position participants for retro rewards. My only suggestion is to use NFTs on PGN instead of POAPs.

-------------------------

gravityblast | 2023-11-08 22:03:34 UTC | #7

[quote="owocki, post:1, topic:16772"]
Introducing the Gitcoin WalletGuard, a decentralized group of individuals who are responsible for making sure the code on Gitcoin Treasury proposals match the textual description of the proposal.
[/quote]

Great idea! 
I think we should automate part of the process, not only checking that the address is correct, but also that the keys used for those accounts/multisigs are still in use. 

For workstreams budgets proposals the recipient address will probably remain the same, so we can have a script with hardcoded addresses and automate the check. 

If the recipient is an EOA, we can have a webapp that let the proposer sign a random message with the recipient key to prove ownership of the account.

The same process can be used to prove you still have ownership of a key that is part of a multisig. 

And everything can be automatically posted here in the forum. I'm happy to help if anyone wants to do it.

-------------------------

jon-spark-eco | 2023-11-12 19:07:57 UTC | #8

Dig the idea. One possible issue: I got this when verifying my 3rd tally/gov post. 

![Screenshot 2023-11-12 at 2.06.00 PM|690x131](upload://3hmowOwm4JOsfwrtnajBe1D940O.png)

I will try again later.

-------------------------
