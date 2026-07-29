---
id: 10316
title: "Ditch Quadratic Funding?"
slug: ditch-quadratic-funding
category: governancevision
url: https://gov.gitcoin.co/t/ditch-quadratic-funding/10316
created_at: 2022-04-06T21:10:47.079Z
last_posted_at: 2022-04-29T04:55:29.241Z
posts_count: 6
views: 4486
like_count: 13
---

# Ditch Quadratic Funding?

<https://gov.gitcoin.co/t/ditch-quadratic-funding/10316>
nollied | 2022-04-06 21:10:47 UTC | #1

This post assumes you have knowledge of [Quadratic Funding](https://wtfisqf.com/?grant=&grant=&grant=&grant=&match=1000), henceforth known as "QF".

**Warning! Hot take ahead.**

it seems like QF is a central part of the gitcoin identity. how hard-set of a constraint is this?

![Screen Shot 2022-04-06 at 1.54.36 PM|690x291](upload://vLUcjANrRdHPgAJWVAmhnQMVaaf.jpeg)

QF was assumed to have product-market fit [after some experimentation](https://gov.gitcoin.co/t/a-quadratic-funding-powered-social-network/9462). 

is this *really* because of the mathematical properties of QF being optimal? or *is it actually* because of the [immediate (inaccurate) promise of matching funds ridiculous amounts](https://twitter.com/LefterisJP/status/1505311006645526533)? My intuition is the latter.

In practice, using QF might not be worth the [consequences it has](https://medium.com/block-science/deterring-adversarial-behavior-at-scale-in-gitcoin-grants-a8a5cd7899ff). This is made apparent with all of the [modifications](https://gitcoin.co/blog/grants-round-12-matching-caps/) to [QF we have to make](https://ethresear.ch/t/pairwise-coordination-subsidies-a-new-quadratic-funding-design/5553) to keep it usable. 

[Sybil account](https://en.wikipedia.org/wiki/Sybil_attack) detection has been raising significant concerns of privacy-invasive machine learning practices of our users, and they should be taken very seriously.

In the spirit of [pluralism](https://gov.gitcoin.co/t/a-vision-for-a-pluralistic-civilizational-scale-infrastructure-for-funding-public-goods/9503), it makes sense for QF to exist in some capacity, especially with different modifications. However, It feels like we're jamming a square peg (QF, pun intended lmao) into a circular hole (gitcoin grants). 

This inevitably brings in [computational complexity](https://github.com/gitcoinco/web/blob/master/app/grants/clr.py), making smart contracts (if we ever continue dGrants development) for the QF mechanism potentially more vulnerable to attacks.

[The simplest answer is often the best.](https://en.wikipedia.org/wiki/Occam's_razor)

the question i would like to pose is: how married to QF is gitcoin? if a funding mechanism design totally different from QF emerged and had better in-practice capabilities, is this something we would be willing to adopt?

the optimality assumptions that the QF paper makes are rooted in theory, and as we've seen through pragmatism, it isn't optimal (at least not yet).

despite the pessimistic tone of this post, i'm still optimistic that more bullet proof identity systems can make QF more usable, but there are still problems that need fine-tuning to the community (as with everything). 

so my judgement is withheld, i'm moreso interested in what others' thoughts are and if they are having similar concerns. Btw, Glen Weyl the co-author of many QF white papers [does](https://gov.gitcoin.co/t/a-vision-for-a-pluralistic-civilizational-scale-infrastructure-for-funding-public-goods/9503/11?u=glenweyl).

-------------------------

owocki | 2022-04-06 23:07:38 UTC | #2

Hi nollied,  thanks for starting this discussion! I think its important to be willing to revisit & update our priors from time to time, so this conversation could serve as a nice discussion about "why QF".

IMO this post jumps into solutioning (ditch QF) a bit too early for me.  I think that it makes sense to explore the problem space a bit first.  In this reply I am to do so by articulating the 

1. **problems/cons of QF** - starting with the discrete problems with QF you noted as currently implemented on Gitcoin Grants & 
2.  **what QF provides/pros of QF** - what Gitcoin Grants gains from QF.  

Here goes:

## problems (cons)

In my opinion, the problems you noted are
1. inaccurate match estimates
2. privacy of sybil resistence
3. computational complexity

I would also add these problems which you did not note (but I think about a lot)
1. the necessity to keep raising matching pools
2. collusion attacks

## what QF provides (pros)

QF provides:
1. *(from the perspective of a contributor)* - an incentive to get over the free rider problem by providing a matching contribution to every crowd contribution
2. *(from the perspective of an ecosystem)* 
- an opportunity to measure the signal of what your ecosystem participants want to fund, 
- a way to push the power/responsibility of deciding what to fund away from a central grants team, 
- and an opportunity to double(ish) your matching pool money (because contributors will crowdfund + this often doubles the amount of money that goes to those projects)
3. *(for everyone)* - funding for projects supported by the poor/many instead of just the rich few

## pros vs cons

The DAO should make its own decision (this post is just my thoughts) about the pros vs cons.  

In my opinion, 
1. the juice QF provides is worth the squeeze,
2.  QF is a money lego for the space (similar to AMMs), 
3. but the approach Gitcoin Grants uses could be evolved.  

The core reason I think QF is worth the effort that goes into it is that it is an elegant & scalable way of getting over the free rider problem, which is a core problem to solve for Gitcoin's [mission](https://gitcoin.co/mission) to build/fund digital public goods.

A secondary reason is that I've seen the most energy & excitement around QF of anything I've seen that Gitcoin has done over the last 5 years. 

I also believe that the problems noted above have discrete solutions which could be explored:
1. inaccurate match estimates => updated matching estimate algorithms
2. privacy of sybil resistence => Proof of Personhood Passport, ZK tech, & MACI
3. computational complexity => MACI or off-chain computation verifiable on-chain
1. the necessity to keep raising matching pools => https://gov.gitcoin.co/t/gitcoin-aqueduct/9684 & https://gov.gitcoin.co/t/how-does-the-dao-prioritize-side-rounds/9827
2. collusion attacks => MACI / pairwise


but I welcome differing views!

## Grants 2.0

[quote="nollied, post:1, topic:10316"]
if we ever continue dGrants development
[/quote]

Have you seen this post? https://gov.gitcoin.co/t/gitcoin-grants-2-0/9981.  IMO Grants 2.0 is the successor to dGrants.

FWIW, Gitcoin Grants 2.0 has a Grants Registry at a base layer that does not have any opinions about what mechanisms should be built on top of it (see below diagram).  One could build pairwise QF, MACI QF, retroactive public goods funding, dominance assurance contracts, or [effective altruism](https://gov.gitcoin.co/t/quadratic-funding-x-effective-altruism/10016) on top of it.

![fLTzUgQ8zK5zC3vXgcp8STSz8GT2BfKgvPj2IVzHtdnyzaezrQCiFB38G71-UJgm0axtGWImIVWBMTIwXY0SYiXMM9MPiIP2HtNMBLFDLDhJheqxD_8mQbA_2xy7AsK9c6tIiJrv|690x323](upload://3ELRwiVb7hCoYGYccYia277rDUA.jpeg)

This is of course just my personal opinion + I welcome differing views !

Thanks again @nollied for starting the convo!

-------------------------

nollied | 2022-04-06 23:31:45 UTC | #3

[quote="owocki, post:2, topic:10316"]
again @nollied for starting the
[/quote]

Of course, thank you for taking the time to respond!

[quote="owocki, post:2, topic:10316"]
Have you seen this post? [Gitcoin Grants 2.0](https://gov.gitcoin.co/t/gitcoin-grants-2-0/9981). IMO Grants 2.0 is the successor to dGrants.
[/quote]

i have not seen this... but wow, it's incredible. it actually is super similar to a project i'm working on in FDD. i left a comment [here](https://gov.gitcoin.co/t/gitcoin-grants-2-0/9981/16?u=nollied).

-------------------------

nollied | 2022-04-07 10:29:17 UTC | #4

i can't stop thinking about this lol, i think we should wrestle a bit more.

[quote="owocki, post:2, topic:10316"]
1. *(from the perspective of a contributor)* - an incentive to get over the free rider problem by providing a matching contribution to every crowd contribution
2. *(from the perspective of an ecosystem)*

* an opportunity to measure the signal of what your ecosystem participants want to fund,
* a way to push the power/responsibility of deciding what to fund away from a central grants team,
* and an opportunity to double(ish) your matching pool money (because contributors will crowdfund + this often doubles the amount of money that goes to those projects)
[/quote]

none of these pros are specific to QF. in fact, any funding mechanism like 1d1v or 1p1v with a sufficient matching pool checks these boxes.

[quote="owocki, post:2, topic:10316"]
*(for everyone)* - funding for projects supported by the poor/many instead of just the rich few
[/quote]

1p1v with a bullet proof identity system would cover this. Is it more accurate to say that QF **balances** the poor/many with the rich/few?

so far, all of the pros you've mentioned **combined** would be fully supported by a 1p1v with a robust identity system and sufficiently large matching pool (approximately 2x the size of the expected total contributions).

[quote="owocki, post:2, topic:10316"]
A secondary reason is that I’ve seen the most energy & excitement around QF of anything I’ve seen that Gitcoin has done over the last 5 years.
[/quote]

why do you think that is? is it because they feel it captures the sentiment of the community effectively (dampening wealth) while also offering wicked matching ratios? Or are there other reasons (for example, very good game-ification/marketing)? 

note that in [GR3](https://vitalik.ca/general/2019/10/24/gitcoin.html) the total amount of grants received from donators exceeded the matching pool. (i'm sure this close to applies to other grant rounds also, but i haven't combed through them all)

[quote="owocki, post:2, topic:10316"]
and an opportunity to double(ish) your matching pool money (because contributors will crowdfund + this often doubles the amount of money that goes to those projects)
[/quote]

you can say the same thing about 1d1v with a 1:1 matching pool or 1p1v with a 1:N matching pool.

----

clearly QF taps into *something*, but what *exactly*?

----


in the case you've outlined, and from my own perspective, it appears that QF could be replaced if we could derive a new funding mechanism that has all of the following properties:
- immune to sybil accounts by design (for example, 1d1v)
- it also captures the sentiment of the community, without giving too much power to the rich
- marketability (it's gotta be at least as sexy as QF)

the other pros you mentioned seem to be covered by any non-negligible matching pool allocator.

what do you think? it might be tempting to say QF (and modifications thereof) is the only way, but i've got some ideas i want to explore. there's a low likelihood of my efforts bearing fruit, but it's fun and either way i will learn something!

-------------------------

bestape | 2022-04-17 19:48:19 UTC | #5

Are you in our CRL chat on Discord? Octopus and I both suggested ways to lower computational complexity. Let me know if you're not included and I'll try to add you.

-------------------------

nollied | 2022-04-29 04:55:29 UTC | #7

CRL? i don’t think im in there. my discord is nollied#6773 i’d love to join

i work closely with octopus though, he’s part of my catalyst squad in FDD

-------------------------
