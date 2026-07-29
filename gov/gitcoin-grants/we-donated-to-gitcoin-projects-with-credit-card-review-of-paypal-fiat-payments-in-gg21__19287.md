---
id: 19287
title: "We Donated to Gitcoin Projects with Credit Card! - Review of PayPal Fiat Payments in GG21"
slug: we-donated-to-gitcoin-projects-with-credit-card-review-of-paypal-fiat-payments-in-gg21
category: gitcoin-grants
url: https://gov.gitcoin.co/t/we-donated-to-gitcoin-projects-with-credit-card-review-of-paypal-fiat-payments-in-gg21/19287
created_at: 2024-08-27T16:40:07.112Z
last_posted_at: 2024-09-18T12:59:13.890Z
posts_count: 5
views: 3398
like_count: 7
---

# We Donated to Gitcoin Projects with Credit Card! - Review of PayPal Fiat Payments in GG21

<https://gov.gitcoin.co/t/we-donated-to-gitcoin-projects-with-credit-card-review-of-paypal-fiat-payments-in-gg21/19287>
noahchonlee | 2024-08-27 16:47:15 UTC | #1

**Overview**

We put credit card payments on-chain!!! 
PEW PEW PEW PEW (As @M0nkeyFl0wer would say) :raised_hands: :partying_face: :tada:

See how the viaPrize.org team built that for our platform here - https://youtu.be/19LFDAIDsB0

We are a full-time team of 5 with our only funding as of now by Gitcoin donations from >2,000 people and a couple thousand dollars in revenue (See our gratitude post and story here - https://gov.gitcoin.co/t/gitcoin-appreciations-thread/18332)

So once we built this, we asked how we could build this for the Gitcoin community and you can see this thread as we request a grant for this: [https://gov.gitcoin.co/t/10-000-donated-to-gitcoin-zuzalu-round-with-credit-card-pilot-project-proposal/18827](https://gov.gitcoin.co/t/10-000-donated-to-gitcoin-zuzalu-round-with-credit-card-pilot-project-proposal/18827) 

**Demo**
So yeah, we built fiat donations to Gitcoin projects! See the demo here - [https://x.com/viaprize/status/1825566773820723566](https://x.com/viaprize/status/1825566773820723566)

**How it works**
1. User sends funds to viaPrize
2. We send equivalent USDC (in future perhaps USDGLO) from our crypto reserve to a wallet associated with that user
3. Then from the wallet associated with that user to the Gitcoin project. 

Before the round, we send a round operator a URL where people can donate with fiat such as: [https://viaprize.org/qf/opencivics/explore](https://viaprize.org/qf/opencivics/explore) 

At the end of the round, we give the round operator a list of wallets to whitelist to receive matching. 
@umarkhaneth built this out for us and this is all possible thanks to his beautiful magical wizardry :mage:

**Proof of Personhood**
In this round, we used PayPal for proof of personhood because we can see a confirmed address associated with someone's credit card, we can see whether an account is verified based on if they have a bank account linked to it (only one bank account can be linked to one PayPal account), PayPal often puts payments "on hold" if someone recently changed their name or it's a new account and they haven't completed CIP/KYC with a gov ID. 

For a **future proof of personhood**, we're asking @azeem for help with a connection to Visa and MasterCard to receive their Payment Account Validation API access so we can check if someone is using their real legal name when making a payment. If anyone else has connections there, please let us know with a DM to @viaprize on Twitter.

**OpenCivics PayPal Round Review**
To start out, our first partner was the OpenCivics community. We received interest from several other round operators, but didn't have the funds for it so we ended up only onboarding CollabTech partway through.

Here is the data for PayPal donations to the OpenCivics round (emails and some other data removed, and payments from Noah and from Patricia were mostly for testing): 
![Screenshot 2024-08-24 at 8.44.46 AM|690x277](upload://GNAUzVxUMv5Nway9kmB6YrOzCM.jpeg)

Looking at this info, the round operators can now decide what they want to receive matching:
1. All accounts get matching
2. Exclude unverified accounts (no bank account attached)
3. Exclude pending transactions (often happens if it's brand new account that hasn't done KYC or if it just changed its name)
4. Exclude both pending and unverified

CollabTech has responded they are picking 4, which excluded 2/9 donors due to being unverified accounts (no bank account attached.) OpenCivics is deciding. 

Then they just mark which wallet addresses out of these to white-list and those will receive matching.

If a round operator prefers, we can also just take care of it for them and send them the final CSV to upload that determines matching. 

**Financial Sustainability (Hint: It's not yet!)**

Feedback we received from various people including @rohit , Henry, and Umar of Gitcoin and @omniharmonic and 6 other OpenCivics community members is that they find it fair to build this then charge a fee and continue applying for various grants. So that's what we're pursuing, shoutout to @Clinamenic and Ben West for helping us search for these. 

We received $400.70 through PayPal (about $100 of that was us testing), took a 5% cut (which is taken out of the post-PayPal fee balance. PayPal fees = min $0.35 per tx and 4.5% usually to 9.5% with currency conversions) so in the end made about $13ish in revenue. If anyone knows grant programs to support this, please let us know :pleading_face:

**NEXT STEPS**

GG22, perhaps apply as a community round supporting kids' shelters and at-risk kids projects. (I support a kids' shelter in Ecuador and my evil plan is in particular fund that one: [https://x.com/noahchonlee/status/1793862664961286413](https://x.com/noahchonlee/status/1793862664961286413))

Potentially have 3 options for proof of personhood ready in time:
1. Model based detection and donate with crypto on that chain (the usual as of now)
2. Donate with card and we get your real legal name with Visa and MasterCard API for that, PayPal is OK but kinda meh
3. Multi-chain
Some sorta KYC that gives us a donor's legal name (maybe with Visa API) and then you can donate with whatever including BTC, Sol, etc and then we send some equivalent USDGLO from our own crypto reserve through a wallet associated with that user to the Gitcoin project

IF ANYONE HAS A CONTACT AT VISA AND/OR MASTERCARD TO GIVE US PAYMENT ACCOUNT VALIDATION API ACCESS PLEASE LET US KNOW. This is the most important thing we could use help with. @kyle would you have any contacts there?

Feel free to contact us [viaPrize](https://x.com/viaprize) on socials and let us know of best options to fund this initiative!

-------------------------

thedevanshmehta | 2024-09-06 18:05:53 UTC | #2

Really interesting pilot! I love the solution of using bank account as proof of personhood or sybil resistance, definitely the right way to go. @owocki had done some work earlier on credit card based QF , curious to hear his thoughts and whether its worth integrating viaprize across all GG22 rounds by default.

Something i didn't fully understand was

1. supporting multiple projects
2. supporting multiple transactions

If i put many projects in a basket and pay with credit card, does viaprize simulate the transaction with the embedded wallet?

And if i donate on day 1, and then again on day 7, is the same wallet used?

Does viaprize have control of the wallet that is doing the donating? which service did you end up using for embedded wallets?

-------------------------

noahchonlee | 2024-09-06 19:42:49 UTC | #3

Thank you Devansh! Always happy to hear from you and been encouraged in our chats :slight_smile: 
Yes, viaPrize simulates the transaction with the embedded wallet.
Yes, same wallet is used on different days. It was 1 wallet per PayPal account. 
Yes, we ended up using custodial wallets for this because Gitcoin smart contracts has a quirk where it recognizes what wallet paid for the gas.
So if we wanted to do non-custodial, we would need the user to do an extra step signing an erc-20 sending permission and then we would send the crypto from their wallet for them and pay for gas from a different wallet. The "from" field in etherscan for erc-20 transactions would show the user wallet, but the "from" for normal transactions (where the gas came from) would show the platform wallet and that messes with the Gitcoin smart contract, which if they were to change that, we could adjust it. 
With custodial wallets however we can pay for the gas from the "user's" wallet itself
Happy to hear from people which is preferred.

-------------------------

Sov | 2024-09-17 19:20:38 UTC | #4

Thanks for the work that you put into this.  It's great to see the progress of community members like yourselves in pushing forward with these kinds of initiatives.

I want to ask if there is a process or template that could be shared with other round operators on how to activate this integration for their rounds.  

Making this available to others with GG22 on the horizon would be a huge unlock to continue to prove out the model.

-------------------------

noahchonlee | 2024-09-18 12:59:13 UTC | #5

Great point! Looking forward to chatting about it in our call :)

-------------------------
