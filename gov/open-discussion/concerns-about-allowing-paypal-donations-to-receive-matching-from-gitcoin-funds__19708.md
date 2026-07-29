---
id: 19708
title: "Concerns about allowing Paypal donations to receive matching from Gitcoin funds"
slug: concerns-about-allowing-paypal-donations-to-receive-matching-from-gitcoin-funds
category: open-discussion
url: https://gov.gitcoin.co/t/concerns-about-allowing-paypal-donations-to-receive-matching-from-gitcoin-funds/19708
created_at: 2024-12-05T03:58:47.700Z
last_posted_at: 2024-12-09T00:46:17.955Z
posts_count: 3
views: 1921
like_count: 9
---

# Concerns about allowing Paypal donations to receive matching from Gitcoin funds

<https://gov.gitcoin.co/t/concerns-about-allowing-paypal-donations-to-receive-matching-from-gitcoin-funds/19708>
Diogo | 2024-12-05 04:02:29 UTC | #1

Gm. I would like to share a personal feedback about allowing fiat donations to match funds from the Gitcoin Community.  In the recent round reports I saw many operators praising the benefits of having more fiat donations, and not so many criticizing it so I felt the need to play devil's advocate for once, in the spirit of collective learning. 

There were 2 specific points that made me concerned and I would like to hear your perceptions about them.

1. **Security Risks**: It seems that fiat donations are not transparent enough to flag bad behavior like collusion or other attack vectors. If I make a fiat deposit in your bank account so you can donate it back to me there's no way to detect it. Therefore all the hard work of folks building the security features of Gitcoin Passport and COCM becomes of no use, or applied only upon web3 donors.

2. **Inequality:** There's a clear inequality in accessibility to allow digital transfers from only one private company, in this case PayPal. In India people do digital transactions using UPI, in Brazil it's PIX and so on. If the goal is to be more "democratic" then should consider all the many digital payment options, or stick with the one that can be used by anyone such as web3. According to the website [worldpopulationreview](https://worldpopulationreview.com/country-rankings/paypal-users-by-country), the **United States** has the most PayPal users with 38.87%. This is followed by **Germany**, which has 19.25%, and the **United Kingdom** with 7.85%. Bringing up the top five is **France** 2.87% and **Italy** with 3.06%. 

So we can always expect the matching to favor projects based or with strong ties with these countries, like happened in the Land Regenerators Round. A suggestion would be to add a QR code for fiat donations of any company in the project application, or a link to a gofundme site, but to allow these donations to get matched is quite risky imo. If one invested one thousand to bribe people to support him and got 10 thousand as match in return COCM wouldn't even notice it. 

I hope this feedback can be of any use for the Gitcoin Community to continue building the best allocation tool that exists. For a more in depth discussion on the flaws of using Paypal please refer to the most recent comments in the Viaprize topic [here](https://gov.gitcoin.co/t/gcp-017-updated-proposal-for-fiat-donations-in-grants-stack/19446/51).

Thank you,
Diogo Jorge

-------------------------

umarkhaneth | 2024-12-06 07:35:41 UTC | #2

Thanks for sharing your concerns! 

> Therefore all the hard work of folks building the security features of Gitcoin Passport and COCM becomes of no use, or applied only upon web3 donors.

To clarify, COCM works on donation choices therefore it applies equally to both Paypal and regular donors. Collusion still gets treated even if you donate via Fiat. 

Passport works on transaction behavior to filter out bot accounts so you're right that this part does not apply to Paypal donors. However, when donating through Paypal, viaPrize only accepts donations from verified donors. Paypal verification and passport therefore each provide security against bots. 

> If I make a fiat deposit in your bank account so you can donate it back to me there’s no way to detect it.

This is also possible onchain using CEXs. Our goal with sybil defense is similar to the goal of most cybersecurity systems: you can't make a system unhackable you can only increase the cost to attack it beyond what attackers can pay. 

> There’s a clear inequality in accessibility to allow digital transfers from only one private company, in this case PayPal.

I also agree that PayPal might not be the best long-term onramp yet it's sufficient for us to run a test to see what the demand for fiat onramping is. As a lean experiment it let us gather data that @noahchonlee shared amounted to 48% of donations in the GG22 rounds it was used in. That doesn't mean it's always going to be PayPal tho!

-------------------------

Diogo | 2024-12-09 00:46:43 UTC | #3

Hi Umar, thanks for taking the time to address my concerns regarding security risks.  Here are my 2 last additions to this debate:

[quote="umarkhaneth, post:2, topic:19708"]
This is also possible onchain using CEXs. Our goal with sybil defense is similar to the goal of most cybersecurity systems: you can’t make a system unhackable you can only increase the cost to attack it beyond what attackers can pay.
[/quote]

In theory this kind of attack could be made using CEX, that's right. But imo, the cost of attacking it using CEX is a lot higher than using Paypal, because of the learning curve it demands, which adds a new layer of difficulty to commit crimes (create CEX account, create personal wallet, transfer, donate)... It can be done, but it seems to be much harder for the attacker than just using their favorite digital payment systems. 

[quote="umarkhaneth, post:2, topic:19708"]
I also agree that PayPal might not be the best long-term onramp yet it’s sufficient for us to run a test to see what the demand for fiat onramping is. As a lean experiment it let us gather data that @noahchonlee shared amounted to 48% of donations in the GG22 rounds it was used in. That doesn’t mean it’s always going to be PayPal tho!
[/quote]

I imagine you say this because of the inherent inequality in picking one specific digital payment company. I wonder if this 48% increase in donations makes it worth using it despite the inequality. Also, wonder if this 48% increase led to a more concentrated allocation of funds to few projects or kept a similar allocation ratio as seen in previous rounds.

I praise the experiment and hope it contributes to continue improving the allocation mechanism. Thank you for all the work you put into this.

-------------------------
