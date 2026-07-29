---
id: 18827
title: "$10,000 Donated to Gitcoin Zuzalu Round with Credit Card Pilot Project Proposal"
slug: 10-000-donated-to-gitcoin-zuzalu-round-with-credit-card-pilot-project-proposal
category: open-discussion
url: https://gov.gitcoin.co/t/10-000-donated-to-gitcoin-zuzalu-round-with-credit-card-pilot-project-proposal/18827
created_at: 2024-05-17T10:08:00.903Z
last_posted_at: 2024-08-09T09:14:35.064Z
posts_count: 20
views: 4586
like_count: 35
---

# $10,000 Donated to Gitcoin Zuzalu Round with Credit Card Pilot Project Proposal

<https://gov.gitcoin.co/t/10-000-donated-to-gitcoin-zuzalu-round-with-credit-card-pilot-project-proposal/18827>
noahchonlee | 2024-05-17 10:20:19 UTC | #1

What if users could donate with credit card to Gitcoin campaigns?

This would more than 100x the reach from EVM L2 users to all credit card users (billions of people.)

**How it would work**

A user creates an account on the viaPrize.org platform and adds Gitcoin projects to their cart to fund. In essence, we would test this out with our front-end just being one more way to access Gitcoin projects so Gitcoin doesn't need to make any big changes before seeing results. (To create an account, we use Privy which creates a wallet for a user with account abstraction with simply an OTC sent to an email, so web2 people can easily do this.) Then...

1. The user types in how much they are donating
2. They sign permission for us to send that amount of an ERC-20 stablecoin from their wallet 
3. They are taken to a Stripe credit card checkout page which has that amount they are donating pre-filled so they just click send
(From the user's perspective, they are done. Here's what happens next internally...)
4. The fiat funds show up in our Stripe account, and we turn it into USDC for example with Circle mint
5. We send the USDC into the user's wallet, and since we already have their permission to send that amount out of their wallet, we immediately send it to the projects they are donating to. 

In this way, the user has on-chain history of their donations even though they donated with credit card. 

**Why do this instead of an onramp?** 
Check out this ad from Onramper on my LinkedIn feed from when I and the viaPrize team were testing several onramps: 
![photo1715874807|230x500](upload://wH4yqjnMfQsjfTfW2ote7uy1Uz9.jpeg)
A 52% increase of fiat-to-crypto transactions succeeding from 22% equals... 33%? If I did that math right, then still **2/3 of all attempts to onramp fail** through Onramper which is an aggregator offering many onramps (btw Onramper is hard to work with and we honestly feel kinda scammed into spending money on them. Shoutout to Guardarian/ChangeNow for working well so far)
And that's if the user is even willing to sit through the process of doing KYC if this is their first time buying crypto. 

Compare that with the proposal to: have users send fiat, then we convert that into crypto for them with a trusted solution that works consistently. 

**Background**

At Zuzalu last year, I started testing out crowdfunded prizes as a concept with an MVP for viaPrize. (Details here: https://gov.gitcoin.co/t/gitcoin-appreciations-thread/18332?u=noahchonlee)
Since then, a team of five has come together with 100% of our funding so far coming from Gitcoin donations. 

We made a tiny bit of revenue in January with some paying users, but to be honest have been slowed down since then spending months talking about how to make web3 easier to use. We think we may finally have found a strategy that addresses this (we already built USDC based contracts so it is a familiar currency, gasless transactions, and ability to send funds to usernames instead of public keys, full roadmap here: https://docs.google.com/document/d/1lwtuuvofkaK1c-zHEgaplcOzVgg_TXCiPeLL-Bwg488/edit?usp=sharing )

It is thanks to Gitcoin that we exist, and we would love to build something that gives back to the community and pioneers a way for many web3 platforms to be easier for web2 users to interact with. 

**Pilot Project**

For this system to work immediately, we need a "buffer reserve" of funds (see "deep dive into issues" below for an explanation.)

We are suggesting a pool of $10,000 be available in the upcoming Zuzalu Gitcoin round so that users may be able to donate up to $10,000 total to projects in that round with credit card.

If this works well, we can expand this to more rounds, and perhaps viaPrize even creates vpfinance - a b2b saas consultancy that works with web3 platforms to make them easier for web2 users to interact with. 

**Deep Dive into Issues (For Nerds Like Me)**

To send fiat from Stripe to a minting service, a wire transfer will take around 3 business days. We are looking into sending from Stripe to a bank account (which adds a different few days wait unless we pay 1% fee for instant stripe withdrawal) then manually buying crypto in an exchange (there's no APIs to automate this) or use CBIT transfers or Hong Kong's special real time gross settlement (which would require opening a Hong Kong company.) 

But if those fall through, basically we need to have a "buffer reserve" so we can immediately send the crypto upon receiving the fiat, and that buffer is replenished once the fiat we received has finished turning into crypto. 

There are many more considerations, some of which we have simplified in this blog post: https://www.noahchonlee.com/post/how-to-bring-credit-card-payments-to-web3-crowdfunding-platforms

The most important tradeoff is that we COULD use dev-controlled wallets and do everything on behalf of the user at the cost of the user giving up sovereignty of their wallet (this would remove the need for users to click "sign" with a wallet pop up which might confuse people unfamiliar with web3.) 
We would still keep the option for people to use their own self-sovereign/non-custodial wallet, but if someone just wants things to work easier they could select "normal account" instead of a "web3 account" when creating their profile. 

**Funding for This Project**

We see 3 ways this could be funded:
1. A proposal and DAO vote to make a prize for someone to build in credit card payments to donate to Gitcoin campaigns (which we anticipate winning, but at least it's an open invitation then and it is a results based reward system, and there's another prize on our platform :stuck_out_tongue_winking_eye:)
2. The community appreciates our work and donates more to us during GG rounds (and maybe in the citizens round?)
3. We make revenue through a platform fee (we are thinking 5% flat fee, 2.9% of which goes to the credit card fees and potentially 1% goes to Stripe instant payout fee which leaves 2.1%-1.1% for us)

We would prefer all three, and would love feedback from the community on what they think is reasonable. 

**Conclusion**

Gitcoin is making big changes!

Congrats to the switch to the new cluster based matching and model based detection strategy that removes the need for Gitcoin passport stamps!
See @umarkhaneth great article on that and cheers to him encouraging me to write this: https://gov.gitcoin.co/t/our-sybil-resistance-strategy-for-gg20/18524

This change combined with credit card payments may make it orders of magnitude easier to donate and receive matching. 

This could be the start of an even brighter era for Gitcoin, QF, and web3 crowdfunding at large.

What do *you* think? :thinking:

-------------------------

thedevanshmehta | 2024-05-17 11:36:29 UTC | #2

The Gitcoin Citizens Active program might be a good place to apply for grant funding. I do know that @meglister is already thinking about credit card integrations so she would be the person to talk to about this!

-------------------------

noahchonlee | 2024-05-17 12:22:24 UTC | #3

Nice! I just messaged with Meg who set us up with a call with a devrel tonight to help us understand the Gitcoin stack.
Why do you think a citizens forward proposal instead of a Gitcoin Community Proposal? It's unclear to me when to do one or the other

-------------------------

thedevanshmehta | 2024-05-17 12:25:50 UTC | #4

From what I understand, the citizens forward or citizens innovate is a more streamlined version of a GCP

Where a GCP requires the entire DAO to vote, a citizens proposal only requires approval by a committee of 5.  The citizens program budget was approved via GCP, so those seem to be reserved for more higher end frameworks rather than individual proposals

-------------------------

mars | 2024-05-17 13:46:13 UTC | #5

[quote="noahchonlee, post:1, topic:18827"]
What if users could donate with credit card to Gitcoin campaigns?

This would more than 100x the reach from EVM L2 users to all credit card users (billions of people.)
[/quote]

### I 💯 support this idea, it makes so much sense...

I've literally suggested (talk is cheap, show me the code) it some time ago and I'm so happy that you have the code up and running.


[quote="mars, post:6, topic:16668"]
Potentially an :bulb: to **expand beyond Web3** - checkout with payment card as a vote - create a custodial / non-custodial / account abstractions wallet on the backend - that would be pretty neat onboarding into Web3.
[/quote]

### Sybil resistance

Note that long-term using a payment card is good as **unique data point** for normies without on-chain history and without connecting loads of social accounts.

[quote="noahchonlee, post:1, topic:18827"]
me to write this: [Our Sybil Resistance Strategy for GG20](https://gov.gitcoin.co/t/our-sybil-resistance-strategy-for-gg20/18524)
[/quote]
[quote="noahchonlee, post:14, topic:18524"]
If they choose the wallet we control, they can log in with just an email OTP for account abstraction and make a username and they don’t need to worry about keys or wallet addresses or anything
[/quote]

### Payment provider / onramp

> Onramper is hard to work
> Shoutout to Guardarian/ChangeNow for working well so far
> users send fiat, then we convert that into crypto for them with a trusted solution that works consistently.

* Does Stripe supports that?
* Do you have legal entity?
* Do you have money transmitting / brokering licenses?

About the Web2 to Web3 onramp, recently they were in the press - https://transak.com/ - announcing profitability for crypto company? Rare in this space, with such an ability to execute they are here to stay:

![image|687x500](upload://4GLCqvJua1KeXgK1t8Ima4zHp3t.png)

-------------------------

noahchonlee | 2024-05-17 14:59:22 UTC | #6

Ah I see! Do you know what the max is for citizens program budget? Could we do a proposal for $10k? Also Im curious about how voting works, which 5 are eligible, how rejection votes factor in, if there's any write up explaining that I'm curious. Thank you for info!!

-------------------------

noahchonlee | 2024-05-17 15:02:23 UTC | #7

Thank you Mars! Glad to see others are thinking about this, too and down to call or jam if you want to collab on this. Stripe has a beta program that we applied to for crypto payouts but we haven't been added to it, they say it will be more widely available over summer. We are a Delaware C corp for legal entity. We don't have that license and would love intros to lawyers to discuss this more.
We talked with some people at Transak as well and seems like they are a growing onramp solution!

-------------------------

rohit | 2024-05-20 07:14:21 UTC | #8

Hey @noahchonlee - thanks for booking time for the Citizen Grants office hours. I am looking forward to working with you on this proposal. For more context on the direct grants available for Gitcoin Citizens, you can check out more details [here](https://gitcoin.co/citizens).

-------------------------

noahchonlee | 2024-05-21 13:05:19 UTC | #9

Thank you for the help through the call!! Really appreciate the guidance and I'm writing up the Citizens Innovate template now. Curious about how the Gitcoin idea board could become prizes that could be crowdfunded and funders collectively choose the winners :thinking:

-------------------------

rohit | 2024-05-23 07:35:05 UTC | #10

[quote="noahchonlee, post:9, topic:18827"]
Curious about how the Gitcoin idea board could become prizes that could be crowdfunded and funders collectively choose the winners :thinking:
[/quote]

That's a great idea—I'm open to experimenting with it. As it stands now, most of the topics on the [idea board](https://gitcoin.notion.site/Gitcoin-Idea-Board-3d839ea2b299495d9e4a6268cf1e0f9e) are the DAO's wishlist to nudge citizens to either opt into existing ideas or submit new ones. It would be great to curate some of these where the chances of having other funders interested are highest. I will DM for a deeper dive.

-------------------------

PaigeDAO | 2024-05-27 11:23:19 UTC | #11

Really like the gist of this. And agree that cc payment functionality will be the key to more, broader engagement. 

Looking forward to hearing more about how this potentially syncs with Meg's/ Gitcoin Product Team's in-progress plans. 

Keep up the good work! 

Also, your tool looks like it could be very useful to many of the Gitcoin Round participants. Where can I find a more general overview of your product? the website doesn't seem to illustrate any use cases, at least not on the home page? 

Thank you for all your good work.

-------------------------

noahchonlee | 2024-05-27 11:51:09 UTC | #12

Hi Paige, thank you! We are currently working on a full website front-end redesign, a blog, and newsletter hopefully all those help :slight_smile: 
There's a bit more info about how prizes work here: https://www.viaprize.org/prize/about
Basically there's...
Proposer - Adds the prize idea
Funders - Adds funds to the prize and can vote on the winner
Contestants - Wins prizes

There's also this blog post with more info - https://www.noahchonlee.com/post/prizes-as-the-missing-middle-road-in-public-goods-funding

-------------------------

noahchonlee | 2024-06-02 05:39:10 UTC | #13

GCP update:
Immensely grateful to @rohit and Henry Wilson for our calls helping draft up a Citizens Innovate GCP. They suggested viaPrize provides the buffer funds and then Gitcoin reward us after achieving certain milestones, so now we are thinking viaPrize would take on the risk of providing 5000 USDC. The full proposal should be posted soon.

Tech Update and Proof of Personhood Challenges:
Even in COCM as the new sybil resistance, a new wallet without various on-chain history will not receive matching. Thus, we need a proof of personhood for these new people coming in with credit card.

Solutions: We do proof of personhood through a person's legal name

The following payment methods allow us to obtain that info:
Visa
Amex
PayPal
Bank transfer (this is slower so if we include this option we would need to remove it near the end of the round) 

If a donor has a unique name, they get matching. (Perhaps we can also store these with ZK in the future. There's also the possibility to add Holonym NFC e-passport and if anyone shows their name through that, then they can donate with any method and get matching.)

Issue: This means someone could donate with fiat and receive matching with that wallet, then donate again with another wallet that has sufficient on-chain history and get matching on a 2nd wallet. This could be thought of as a 2x Sybil, or we could say that each donation could get you 50%(ish) of your total possible matching. 

2 interesting benefits of this is that:
For non-crypto people, this incentivizes individuals to onboard to web3 and get more on-chain history so they can get more matching.
As Henry pointed out, many crypto people will donate the minimum amount to get matching and if they can donate 2x to get more matching, maybe this increases the total amount donated. 

Are these trade-offs worth giving access to billions of non-crypto people? We would love some community input.

-------------------------

rohit | 2024-06-03 17:36:06 UTC | #14

Hey @noahchonlee, I'm sharing notes from our discussion here. Thanks for your patience in working through the proposal. At this stage of the pilot, we will be unable to offer a proactive direct grant.

We appreciate the thoroughness and innovative approach outlined in this post and the supporting research you and the team have done on factoring user experience, Sybil, and other technical tradeoffs.

The problem you're tackling is highly relevant and holds immense potential for broadening participation in decentralized web3 grant funding. By integrating fiat payments into the quadratic funding (QF) mechanism for Gitcoin Grants, you're opening up an opportunity to significantly expand the number of donors, thereby democratizing access and support. 

However, to justify an upfront investment, we would love to see a more scalable approach readily applied across multiple rounds, focusing on the volume of users opting for fiat donations. The following  factors will help reconsider the funding decisions in the future:

1. **Projected Impact:** Based on the Zuzalu rounds in Q1, the projected number of users for fiat donations for the Zuzalu round is likely low, given the crypto-native nature of the community. This makes it challenging to make an upfront investment pending a clear indication of broader adoption and impact. 

2. **Integration Scope / Scalability:** The current approach involves driving credit card donations through the viaPrize platform. While this keeps the process clean, it also limits the initiative's visibility and impact (e.g., having a CTA for fiat contributions as part of the donors' existing workflow on Grants Stack). A deeper integration into Explorer could potentially drive more users.

We strongly encourage you to proceed with the pilot and refine your approach based on your findings for a revised proposal to address the above topics. We would also love the team to continue engaging with the community here to gather feedback on topics like handling Sybils, revenue models, and the integration approach. Also, note that the individuals on the team contributing to research and development can opt into the next Citizens Retro round for additional funding based on the impact of this experiment. As always, feel free to utilize the [office hours](https://calendar.app.google/YY1Pnt7i4oMka9sX9) for any follow-up and I look forward to the pilot.

-------------------------

noahchonlee | 2024-06-04 07:59:45 UTC | #15

Thank you Rohit! As mentioned in the call you have been awesome to work with and super fast and responsive. 

Just responding as did in the call for the community: All good! For this pilot in our minds the main value is knowing if this system can work so that way we could scale it in the future to more rounds, and the amount of new users from this particular activation is not a focus. 

Also when I asked if it matters more to drive more donations through Allo or more users to grants stack, I'm now operating according to the response that the main goal for Gitcoin is to have more donations through Allo and it is welcome to have more front-ends and platforms which is the intention of making this a protocol. That's more important for us to understand if we are doing things that fit the community goals long-term than upfront funds right now and I appreciate all the feedback helping us to understand this.

Sidenote Rohit mentioned: Citizens retro would be awesome, though since only one individual can apply and this was very much a group effort (Myself, Dipanshu, Nithin, Swaraj, and Aryan, plus support from Rohit Umar and Henry) we would have to as individuals quantify the ways we have been researching this together

-------------------------

mars | 2024-08-07 10:51:12 UTC | #16

Well done ser! I've seen a demo video posted in the OpenCivics chat: 

https://youtu.be/Hp47z9_bqVo 

Gitcoin stewards, crew, community: Please make sure donations via cards are accounted in QF matching! :)

I think that unique credit card is a good sybil-resistant signal, unless someone creates disposable on the fly.

-------------------------

noahchonlee | 2024-08-07 15:07:43 UTC | #17

Hi Mars! The sybil resistance is not based on unique credit card, it's based on someone's legal name. We built it so people can use multiple credit cards and it'll go through the same single wallet associated with their name :)

-------------------------

mars | 2024-08-07 17:22:03 UTC | #18

[quote="noahchonlee, post:17, topic:18827"]
based on someone’s legal name
[/quote]

In my country, when you pay with card online, there is usually a question about billing address. But it is not checked. You could put Mickey Mouse as the name or Buckingham Palace as the address.

My assumption is that there is no government issued ID KYC in viaPrize. Or maybe there is? Where is the legal name coming from?

Is the signal from viaPrize integrated with QF results on Gitcoin?

I hope the experiment will be successful and cards will be natively supported.

Once again congrats for shipping and I’m hoping that my questions / suggestions are on point.

-------------------------

noahchonlee | 2024-08-07 18:45:47 UTC | #19

Thank you! Yes with standard credit card payments they often only check the zip code and the rest can be fake. We tested paying as Batman. 

However, with PayPal specifically we get donors' legal name

We are also in contact with Visa requesting API access for checking legal name as well for the future

-------------------------

mars | 2024-08-09 20:25:15 UTC | #20

[quote="noahchonlee, post:19, topic:18827"]
they often only check the zip code
[/quote]

That is likely to be the case in the US.

In the EU there is 2FA requirement: https://en.wikipedia.org/wiki/Strong_customer_authentication

> The requirement ensures that electronic payments are performed with [multi-factor authentication](https://en.wikipedia.org/wiki/Multi-factor_authentication), to increase the security of electronic payments.

*(and because of the 2FA, the validation of ZIP code / name / address does not happen, using Mickey Mouse or Batman works fine)*

**RELATED.** Yet another way to GROWnate: [x.com/jimicohen/status/1821551869728018751](https://x.com/jimicohen/status/1821551869728018751)

![image|684x500](upload://x0ShWy66BFNUxCXPFRhY2ESSSM2.jpeg)

https://www.ggframe.xyz/

@MathildaDV *(and the rest of the Gitcoin crew)* take note of viaPrize and GG Frame and all the others ways in final calculation of the matching!

-------------------------
