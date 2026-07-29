---
id: 11505
title: "Fileverse Grant Deactivation"
slug: fileverse-grant-deactivation
category: gitcoin-grants
url: https://gov.gitcoin.co/t/fileverse-grant-deactivation/11505
created_at: 2022-09-13T18:14:32.024Z
last_posted_at: 2022-09-26T16:31:42.903Z
posts_count: 9
views: 4688
like_count: 22
---

# Fileverse Grant Deactivation

<https://gov.gitcoin.co/t/fileverse-grant-deactivation/11505>
DisruptionJoe | 2022-09-13 19:33:32 UTC | #1

On Friday, Sept 9th, the [Fileverse grant](https://gitcoin.co/grants/4846/fileverseio-file-sharing-between-blockchain-addre) was deactivated by a Fraud Detection & Defense workstream reviewer. It remained inactive for less than 24 hours. The issue was escalated and processed resulting in the grant being reactivated.

The team at Fileverse was very upset about the situation because the donations at the beginning of a grant round can have an outsized effect on the overall earnings the grant receives. Additionally, they are concerned about reputational damage from being deemed as bad actors by the Gitcoin community.

[GR15 Dispute Page](https://gitcoin.notion.site/https-gitcoin-co-grants-4846-fileverseio-file-sharing-between-blockchain-addre-9d967e46b920418c9367d3fbac88bce6)

## TL;DR

* Why was the grant initially deactivated?
  * The reviewer saw what they believed was sufficient evidence (listed at the bottom of the doc) to deactivate the grant. This was done in service of their goal of protecting the community.
* Was the proper process followed?
  * The reviewer believed that their decision was correct and was seconded by a member of the PGF Grant Operations team. Afterwards, a more senior person in FDD overturned the decision. The decision to overturn was based on the fact that a further investigation would still have time to avoid illegitimate matching fund allocation.
* What were the findings of the follow up investigation?
  * The behavior that has been identified is likely a newly identified attack vector which allows the attacker a “free shot” at the attack. We believe that the sybil attack is NOT an anomaly and IS a direct attack on the matching funding available.
* What should happen to the grant considering the evidence?
  * Considering the overwhelming found, FDD will deactivate the grant in 72 hours provided Fileverse cannot introduce sufficient evidence of another cause for the attack.

The rest of this post will examine the findings of our investigation.

## Why was the grant initially deactivated?

***The reviewer saw what they believed was sufficient evidence to deactivate the grant. This was done in service of their goal of protecting the community.***

Fileverse grant has a product and would normally be unquestionably eligible for the Main round as well as multiple side rounds. The reviewer responsible for shutting down the grant is a senior reviewer and approver with FDD.

Our reviewer had a heightened suspicion level because this grant has routinely been the receiver of sybil donations. You can see the disputes from [GR14 here](https://gitcoin.notion.site/https-gitcoin-co-grants-4846-fileverseio-file-sharing-between-blockchain-addre-a25dd283f41842d8ba2cb83ca3d95025) & from [GR13 here](https://gitcoin.notion.site/https-gitcoin-co-grants-4846-fileverseio-file-sharing-between-blockchain-addre-ec924298da2e49b8a2cdf86820caea46). This in addition to an anonymous investigator reaching out via Gitcoin Discord support put the reviewer on high alert.

Fileverse has been reported for receiving sybil donations multiple times. It has been flagged in previous rounds, but it was not found ineligible (guilty) due to the fact that some sybil donors are [farming for airdrops](https://gov.gitcoin.co/t/airdrop-farming/10938) and not solicited by the grant in any way. It would be inappropriate to deactivate the grant without further evidence.

The reviewer then found further evidence!

The owner of the fileverse grant made a donation at almost the exact same time as a set of sybil accounts. These accounts were easy to identify sharing attributes open to review by our steward council.

Below, you can see that the user [MoMo @momonosukke](https://gitcoin.co/momonosukke) donated at the same time as user [Cici @cici0910](https://gitcoin.co/cici0910)

![|436x245](upload://jHmFco0GWcWM3Q2Ik25aCna4f2X.png)

An analyst did a quick review and found that there was sufficient evidence.

![|624x33](upload://9FwSwOxX22Fd6XtxCkpLiGTygE0.jpeg)

Another analyst said “Great Work!” and agreed.

A few more pieces of evidence, which are discussed below, combined with this to make the reviewer confident in their decision.

## Was the proper process followed and what was the result?

***The reviewer believed that their decision was correct and was seconded by a member of the PGF Grant Operations team. Afterwards, a more senior person in FDD overturned the decision. The decision to overturn was based on the fact that a further investigation would still have time to avoid illegitimate matching fund allocation.***

A senior reviewer must have some flexibility to identify issues and solve them in real time. The reviewer of this grant felt that there was indeed overwhelming evidence of fraudulent behavior and made the call to shut down the grant immediately.

This evidence included that described above plus the fact that these sybil accounts only donated to Fileverse. In the past, we have seen airdrop farming accounts normally donate to 5-10 if not more grants which are likely to have an airdrop in the future.

There still wasn’t a link to the team itself being responsible. After a call with the fileverse team, which was requesting help on Twitter, an FDD lead (Disruption Joe) decided to turn the grant back to active.

As long as the grant is sanctioned before the final calculations, the community will avoid any misdirected matching allocations, but is susceptible to sending p2p donations that they would not have otherwise set. Therefore, it is important that illegitimate grants are made inactive as soon as sufficient evidence is available.

In talking with the fileverse team, they pointed out that the reviewer believed their grant had no progress from the last round after reviewing their [Github](https://github.com/fileverse). However, they commented that they post exactly what they have completed between rounds on the [grant itself](https://gitcoin.co/grants/4846/fileverseio-file-sharing-between-blockchain-addre).

![|484x241](upload://wtxBHPZ10aMYnfoZfAfjmHgW4m.jpeg)

It is common for a grant to post updates, but there is no way for Gitcoin reviewers or donors to know if they are honest without checking the Github. In this case, the reviewer saw a lack of activity and decided that the best bet for protecting the community was to deactivate the grant. This was a decision made in combination with all the above evidence.

## What were the findings of the follow up investigation?

***The behavior that has been identified is likely a newly identified attack vector which allows the attacker a “free shot” at the attack. We believe that the sybil attack is NOT an anomaly and IS a direct attack on the matching funding available.***

![|624x44](upload://sMkfXgB9S91UxaOWZQbE34cLJdu.jpeg)

We hope the Fileverse team, whose cofounder studied sybil attacks in the past and offered to help, will either admit to the actions or provide new evidence that can overturn our current opinion that the presented evidence is overwhelming.

The issue here is that Fileverse may have exploited a unique sybil attack method previously not seen by FDD. The attack skews the normal profitability equation for a sybil attack by taking advantage of the gitcoin discoverability formula and a greater user incentive created by the early donations showing donors that the matching available for their donation is much more than if they were to donate to an alternative grant.

Here is the previously assumed sybil attacker profitability equation:

![|624x213](upload://eMzXJfeiFBf8IBBSllYLs96SvhX.jpeg)

Here is how this attack changes the equation:

![|624x235](upload://1KHXT4syEWk9wa3v140fDcPPg9Z.jpeg)

The Fileverse grant is currently eligible for over $47k in matching on approximately $2.5k in donations. This total will change as FDD squelches the sybil accounts, but the number of donations gained via the newly added profitability parameters may offer a free attack.

On the call with the Fileverse team, they suggested that we should “squelch” the sybil accounts. This is fine considering the attack because it allows them to look like the good guys saying “deactivate them, we don’t know them”. However, if the amount they gain from the other donations coming from legitimate community members based on their higher discoverability and larger UX incentive is greater than their cost of generating sybils, then the attack is successful.

Additionally, if FDD does not catch and squelch ALL of their sybil accounts, then they receive a “free” sybil attack!

This new equation potentially offers attackers a price of conducting a sybil attack. If they can gain more legit donors and illegitimate matching funds than what they spent on creating sybils, they are literally incentivized to create more sybil accounts.

Remember, they aren’t counting on the sybils diverting matching funds. They want some sybils caught, and will even suggest we catch them, because their goal is not to have the sybil donations directly affect the matching pool allocation.

This is similar to when banks like HBSC get a $200 million fine on laundering $8 billion. It is not a deterrent. It is a cost of doing business.

## What should happen to the grant considering the evidence?

***Considering the overwhelming new evidence found, FDD will deactivate the grant in 72 hours provided Fileverse cannot introduce sufficient evidence of another cause for the attack.***

Because this attack is normally not linked to the grant itself, we must have a threshold for deactivating grants within a reasonable suspicion level. We haven’t identified that level at this time, but feel confident that the Fileverse sybil actions would exceed that threshold.

Here is the full list of evidence including the initial evidence and the following investigation.

### Initial Evidence for Deactivation

* Donation by owner at the same time as sybil accounts
* Confirmed sybils only donated to Fileverse
* Multiple flags in past rounds

### Follow Up Evidence

* Nearly 70% of previous donations have been from sybil accounts
  * Without seeing the new equation, there was no alarm to look into this
* The second highest percentage of sybil donors in past rounds even without being a likely future airdrop grant
* Over 10% of handles that donated during GR15 donated over 10 times during
  * This is the highest percentage by far!
* Over 16% of past donations came from Squelched users
  * This is THE MOST PAST SYBIL DONATIONS of any grant in GR15
* Fileswap is in 22nd place for most donations under $2 when looking at all active grants previous donations
* There are 4 more items which are available for steward council review if requested

![|624x237](upload://6lDa3b7fQs0u6kV5EJjSC2wnk5i.jpeg)

-------------------------

vijaykrishnavanshi | 2022-09-14 17:00:28 UTC | #2

Hi Everyone,

**This first post** is an honest reflection on this whole saga and an attempt to provide a productive way forward. It’s our personal take, it is a call for you to acknowledge the asymmetry of power in this dynamic. It’s a plea that you do not execute an unjust sanction that will kill our project and publicly portray us as crooks.

Fileverse is a small team that got together ~9 months ago and is now fighting to protect their main source of funding. Gitcoin is the ONLY recurrent source of funding for Fileverse. The deal for us is much bigger than for you and we do not intend to get kicked out without giving it our all to rectify the injustice. The stakes are way too big for us to just say “we can’t fight back, they control the system, the narrative, and our funds”.

**The second post** is a point-by-point response to your analysis and defamatory accusations. It provides counterpoints, counter-evidence, and a breakdown of what we believe to be an erroneous statistical analysis you made. This second post tries to be as clear as humanly possible, despite our anger, to make the case for our innocence.

To be clear, the burden of proof should never be on a victim of an uncontrollable external event they were harmed by: but unfortunately, we are past this point already. We implore you to read it carefully, with an open mind, and not punish us for trying our best to build a useful public good.

First post –

First of all, who we are, what we do, and why we do it.

About the two grant owners:

* Vijay is a senior software engineer (github[.]com/vijaykrishnavanshi) that quit his job at the end of GR13, and took a huge leap of faith because of the success the grant had and the hope it gave us that we can actually be full-time free-open-source software developers with a decent source of recurrent funding. Building the public good we call Fileverse is now everything to him.

* MoMo is a PhD student in the UK that has put his work on pause these past few months to focus more on Fileverse. Focusing on public goods is a long commitment of his. He has been donating on Gitcoin since 2019. He received a reward by the GitcoinDAO last year for his proposal for a “new kind of public good” called the algorithmic resistance cookbook (go[.]gitcoin[.]co/blog/seeking-a-new-kind-of-public-good-honorable-mentions). His academic work is on social good  (nature[.]com/articles/s42256-021-00296-0), ethics (link[.]springer[.]com/article/10.1007/s00146-021-01154-8#ref-CR33) and the climate crisis and artificial intelligence (link[.]springer[.]com/article/10.1007/s00146-021-01294-x).

We both passed KYC on Gitcoin, you have our whole details and identities.

We both have a lot of admiration for the people that are building Ethereum because we think it's a new technological primitive, a community computer, that enables people from anywhere in the world to collaborate and solve global coordination problems.

If you look at our history of donations you will see we have been supporting the Ethereum infrastructure builders since 2019, also supporting some projects we consider role models for the whole industry, that includes Rotki app. In fact, we wanted to build our DApp following their example. When we met their team at EthBarcelona and EthCC, we were like little fanboys. We talked about how long we have been following them, we talked about grants and Gitcoin, we talked about how to experiment surviving without taking any VC money, and how to create a sustainable future for our project while remaining open source and while having our code stolen by others who just slap a token onto it and make a ridiculous amount of money.

Gitcoin gave us the best opportunity we could have ever dreamed of. It allowed us to build something we loved and believed in while not compromising on our values. So we built Fileverse. Fileverse is open source, it’s free, it’s useful to a wide range of people, it was built to accommodate both web3 users and people wanting to get into web3 for non-financial/speculative reasons. We see crypto wallets and blockchains as a rebirth of public key cryptography and wanted to show the world how useful it is to have control over your own key pair via your wallet and to leverage the computational integrity that community computers like Ethereum offer. So we built a tool to facilitate, in a web3 way, one of the more important and popular activities on the web: file sharing.

The grant’s early success is because of the nature of our free DApp, because it's easy to use by anyone and requires no money, because it replicates in the web3 world one of the most popular activities on the web, because it just works and doesn't require much knowledge or skills, because of a smiley, shiny logo and because of the Twitter grind of its founders. Additionally, GitcoinDAO is not the only group that has done due diligence on us, every funder that received our Ecosystem and Cause Round Eligibility Application and decided to add us to their side-round, namely, ENS, Polygon, a16z, and Web3Social, saw that we are a serious, deserving public good.

By any stretch of imagination, getting around $40K from Gitcoin donations and QF every three months pales in comparison to what either of us two grant owners could make just working a job we have the qualifications for. So when we are told that we are not victims of a sybil attack and instead that we are evil masterminds that are trying to make around $40k every three months by launching a sybil attack on the platform while risking the death of our project, we feel **disgusted and feel immense disappointment.**

Our whole tech team has 4 members other than us:

2 Full Stack Developers (Sumit, Joshua)

1 Backend Developer (Aakash)

1 Designer (Mohit)

We built a public good, we improve on it every day, have shipped countless features already, we employ 4 people, and do not take a salary for ourselves yet (three founders). The space is filled with opportunities to make a lot of money by taking advantage of people’s greed and hopes. And you decided that we look like those people. That our whole DApp is a front, an elaborate facade to a get-a-bit-of-money-slowly scheme. A scheme based on the theft of funds that would otherwise go to many of our friends and people we admire and have supported in the past, building public goods thanks to Gitcoin QF.

**The impact:**

We don’t want the impact that these slanderous accusations are having on us to be taken lightly. Based on a wrong, unjust and badly argued analysis (which we break-down and counter in the next post) you are:

* Effectively killing our project’s main source of funding.

* Killing the project’s public image.

* Publicly portraying us, our team, individuals that gave their soul to this project, as crooks. As thieves.

* You are asking us to prove our innocence, like it is easy to prove that something does not exist.

All that BASED ON ASSUMPTIONS. Based on the fact that we are the closest sanctionable entity to the Sybil attackers and so it must be assumed we are the attackers themselves.

Victims are ALWAYS close to the facts of the harm, that is why they are victims. Yet you use that fact, twist it, add to it a flawed statistical analysis and make it fit in a logically fallacious argument that presents us as the actual attackers.

Because of the way the Gitcoin platform works and blockchains work, good people can be sprayed by malicious actors, like being sent Tornado Cash dust and being sanctioned for it. What is the logical continuation of your approach? Next Fileverse-like victim gets banned as well. And the one after that? Banned as well. And so on. Because it is too hard to take care of the attackers, because sybil resistance is a game of cat and mouse, you decide that the victims are good proxies for you to focus on. Until you change your mind when you realise that this approach is wrong, and by then, you will have destroyed and alienated honest actors like us.

A productive way forward:

* We implore you to not deactivate our grant. We will not recover from it.

* We are ready to invite you to our Github organisation account for you to see all the extra work happening to ship a huge new feature (Squad / Subdomains).

* We ask that you consider our next post, counter-analysis, and evidence honestly and with an open mind.

* We ask that you put 1 and 1 together and understand that it simply does not make sense for people with our skill sets to become publicly exposed thieves, using a super risky fraud scheme to get ~$40k every three months.

* We are ready to show you bank statements of development costs, of employment payments, EVEN proof of end-of-year tax payments on the donations since we are incorporated in the UK and pay taxes. Anything you might be able to think of to help you put your suspicions to rest.

* We are ready to discuss it on a call, on a Twitter space, anything.

* We would like to suggest ways for you to ensure this never happens again to honest actors, us, and others.

> Give grant owners the ability to mute contributors. That means that grant owners would be able to stop an account from giving any more donations if they feel like it is likely a sybil attacker. You think that grant owners do not look at donations and donors when grant rounds start? Think again. For projects like ours, this is our bread and butter. We are the best front line you have, given the appropriate tools, to create a sybil resistant Gitcoin Platform.

> Give grant owners the ability to reject specific donations’ matching. Because donations come directly to grant addresses, what grant owners can at least do is identify malicious actors and put them in a category of “not to be counted for QF matching”. This is useful on many levels. First, it allows GitcoinDAO to see that a grant being targeted is actively fighting off the attackers. Second, it creates a quick response mechanism that leads to faster identification of attackers and a safer, fairer round. Third, it allows for corroboration to occur. For example, you will be able to see that of the top 10 grants’ owners, 7 of them have reported at least 60% of the same accounts.

* Do not deactivate grants before a public post has been made. I can’t tell you how stressful and overwhelming it is to be the grant owner. To have waited a long time for a grant round to start and see your grant has been deactivated and that there is no information on why, that an opaque decision-making process led to it, and that you have no recourse over. Please don’t turn Gitcoin into GoFundMe.

* This is maybe an overkill suggestion but, we are pretty big fans of ZachXBT. If all the evidence and arguments we provided still do not convince you, would you be willing to co-fund a grant to Zachxbt with us and ask them if they would be willing to investigate the sybil attackers that targeted us? ZachXBT’s work is mainly about uncovering scammers and exposing them publicly, maybe they would be interested in an opportunity to prove people’s innocence this time…

* Give us suggestions on what kind of information we could provide to satisfy your suspicions. You are both the prosecutor and the judge in this trial. Would you please, for the love of god, tell us how we convince you that something did not happen? We are desperately trying to think of every possible way we can prove our innocence to you. But since you are the judge, maybe you have a good idea of what it would take.

Finally, thank you Joe (DisruptionJoe) for taking the time to chat with us after the premature punishment and deactivation of our grant, which was done without proper explanations and without any notice (i.e. without being flagged at first). This is a human mistake, this can happen to anyone. And we want to make sure that you and your colleagues know that we mean no offence to you for having come up with a hypothesis in trying to protect the platform you love. We are not attacking your abilities or intelligence. However, because you are using this hypothesis to accuse our project and team of being the evil masterminds behind sybil attacks we want to make it publicly clear here and on other forums that we will not accept **(a)** the accusations that portray us as *crooks* and **(b)** your discovery of sybil attacks and us being victims of them as **evidence of wrongdoing by us.** Please do not die on the hill of “these guys are *crooks*” just because your analysis of sybil attacks and discovery of a new attack vector was tied to us by some twisted turn of events.

Once again, we implore you to read all this carefully and give it the consideration it deserves. You have our livelihood and hopes in your hands, please do not punish us for being victims of sybil attacks.

Fileverse Team

-------------------------

vijaykrishnavanshi | 2022-09-15 06:33:19 UTC | #4

Hi everyone,

This is post two, responding point-by-point to the post made by Joe and the FDD team.

## #1 “Why was the grant initially deactivated? → The reviewer then found further evidence!”

We honestly do not understand why MoMo making a small ~15$ to our own grant is evidence of collusion with sock puppet accounts spamming our grant since before GR15 had even started.

At the start of every Gitcoin Round MoMo makes a list of projects, funds them and shares the list on Twitter to get people to donate to them as well. The list includes Fileverse to add some visibility when he shares the list around on Twitter. Is this evidence of malicious behaviour? Clearly not.

Now, a counterpoint: you explain that MoMo donated at the same time as one of the sybil attackers gitcoin[.]co/cici0910

In fact, Tx made by MoMo was at 9:14
Tx made by cici0910 was at 9:46
Correct timestamp: docs[.]google[.]com/document/d/18dpqNdFv1dOYQpDwrOlbKePzRokawXoUsIC11BMLWbg/edit

ALSO, if you look at cici0910 account you will notice that it has been spam donating to our grant almost everyday for FOUR WEEKS.

To summarize, you suggest that MoMo making a donation at the the beginning of GR15 and that donation being done 30 minutes prior to a sybil account donation that day is evidence of a relationship. You also do not mention the fact that this account has been donating almost every day for the past 4 weeks (!!). Instead you just claim that one of those 4 weeks of donations is evidence of a relationship between us and them. We say it is a grave mistake which may be due to the reviewer not having had the time to look at the history of behaviour of that clearly fraudulent account. We sincerely hope you can consider the new evidence we just presented.

## #2 “Was the proper process followed and what was the result? → This evidence included that described above plus the fact that these sybil accounts only donated to Fileverse. In the past, we have seen airdrop farming accounts normally donate to 5-10 if not more grants which are likely to have an airdrop in the future.”

When our grant was deactivated and we were informed that our grant was getting sybil attacked, there had been ~30 donors to our grant. We looked at the donations to understand which accounts were exhibiting this behavior. We found that cici0910 and wanghaha02 and wanghaha03 had been spamming ONLY to our grant for weeks, way before GR15 started. You also point out in your analysis that they all belong to the same IP, if I understood correctly.

These are clearly malicious actors that have targeted us. Are there more such accounts that ONLY donated to us or only those listed above? We ask because after the grant was reactivated we were on high alert and started looking at the profiles of our contributors. We found some odd accounts that, like you say, donate small amounts to us + 5 to 10 other grants and seem to be farming airdrops. But in those cases we are not the only target, it is a widespread issue. So going back to my question, are there more than just the three aforementioned accounts that have been donating ONLY to us? If so, could you please list them so we can help you find some connection between them and absolve us once and for all from suspicion?

Regarding more general farming accounts that donate to us AND others, we would also like to point out that a famous Crypto Twitter account by the name of @Olimpiocrypto posted a thread (twitter[.]com/OlimpioCrypto/status/1568728742494875648)  on projects currently with a grant on Gitcoin, that might have an airdrop in the future. The post went super viral by crypto standards (1626 likes and 559 retweets) and probably is the reason there was an explosion of new donations after our grant was reactivated. Note also that we never mentioned doing an airdrop in the history of our project, anywhere, not on our grants (GR13-15), nor on Twitter.

## #3: “It is common for a grant to post updates, but there is no way for Gitcoin reviewers or donors to know if they are honest without checking the Github. In this case, the reviewer saw a lack of activity and decided that the best bet for protecting the community was to deactivate the grant. This was a decision made in combination with all the above evidence.”

This point made by the reviewer in the initial justification (www[.]notion[.]so/https-gitcoin-co-grants-4846-fileverseio-file-sharing-between-blockchain-addre-9d967e46b920418c9367d3fbac88bce6) for deactivating our grant is that we have provided “no updates on their progress”.

This is easily disproved and we hope you can acknowledge the below evidence.

Since GR13, when we started our project, we have provided a roadmap with multiple bullet points of what we aim to achieve with the funds. GR13 allowed us to ship our Beta and keep it free ever since. On GR14 we provided a comprehensive, point-by-point update on every one of the 10+ bullet points on the roadmap that was presented in GR13. The progress was huge. The beta DApp looked completely different from what it did just after GR13 and came with many new features. Again, all free.

We also provided an updated roadmap “looking forward” to GR15. Then a few days before GR15, we updated our grant description to provide a new update on the roadmap and point-by-point summary of progress - you can see it on our result of grant 14 section of grant page: gitcoin[.]co/grants/4846/fileverseio-file-sharing-between-blockchain-addre.

The reviewer could have gone to our actual DApp and seen the progress that has happened since the previous grant round. Assuming someone actually has looked at our DApp. The progress, as we explain in the description, was quite significant.

All this continuous progress is also viewable on github[.]com/fileverse

For the brief period of inactivity on the backend repo: it is due to the fact that most of what we had promised in GR14 was achieved and pushed to prod. We are working on Fileverse Co-op / Subdomain for some time now which will be open source once it’s in proper shape and form. For verification and transparency purposes we are willing to add anyone from your team to our github organization so that you can see what work has been going on behind the scenes and that the work is in advanced state on Fileverse subdomain / co-op. This should relieve you of your suspicions once and for all.

## #4 What were the findings of the follow up investigation? → The behavior that has been identified is likely a newly identified attack vector which allows the attacker a “free shot” at the attack. We believe that the sybil attack is NOT an anomaly and IS a direct attack on the matching funding available. → The issue here is that Fileverse may have exploited a unique sybil attack method previously not seen by FDD. The attack skews the normal profitability equation for a sybil attack by taking advantage of the gitcoin discoverability formula and a greater user incentive created by the early donations showing donors that the matching available for their donation is much more than if they were to donate to an alternative grant.

This is an even more difficult point to accept by any reasonable measure. Before I start explaining why it is flawed and logically fallacious, allow me to repeat that, I mean no offense to the individuals that came up with the above hypothesis. I am not attacking their abilities or intelligence. However, because they are using these to accuse our project and team of being the evil masterminds behind sybil attacks, I need to be clear about the problems in their current reasoning and conclusions.

The “Free Shot Attack” you describe is a clear description of a possible type of attack on the Gitcoin platform’s algorithms:

Bad actor uses sybil attack → hope to either not get caught or get caught and not be punished → get caught and get away with it (big “if” for the attacker) → still benefit from the artificial popularity that the non-sanctioned attack granted them → makes more money from the matching than lost in doing the attack.

This makes sense.

What is deeply flawed and unjust is that this theory emerged and was linked to us (worse even, it was used to describe us) based on an assumption which itself was based on another assumption. In other words, because the end theory (of the attack vector) makes sense, you have decided to validate the antecedent assumptions that led to the theory. This is not the way you construct an argument, not one that would be accepted in court at least. Why? Because the departing assumption is not substantiated by valid evidence. Start any argument with an arbitrary assumption, and that argument will be valid insofar as the first assumption is accepted and not challenged.

Allow me to explain further.

The first assumption you make is that we are the originators of the sybil accounts. This assumption is vicious in effect because it disregards the presumption of innocence on the basis that events that are completely beyond our control have created an inevitable connection between us and malicious actors. The victims are by definition the closest entity to the attackers.

Then you add a another assumption, that, assuming the first is right, the second assumption states that we would have anticipated our sybil attack to “successfully fail” and place us in this sweet spot where our grant is reapproved and the gamble we took to make our grant super popular at the risk of killing the project, is rewarded by the lack of sanction and the gain in artificial popularity on the platform.

The problem is that this second assumption only exists as a patch, a fix to the first, flawed assumption. You saw that we were outraged by the accusation and we provided arguments to disprove it and reverse the sanction, and because we were successful and the sanction was reversed you decided to add a second assumption that our defence “was actually part of the plan all along”. That second assumption exists solely because our response was made. In other words, we can continue this game forever, where even our current post on this forum can then be used to “substantiate” a new, third assumption about how we expected this issue to escalate to the forum and planned to make a big fuss in the community and THUS gain even more donations and visibility! It never ends. That is why it's fallacious.

That is akin to saying:

Your partner died due to a truck hitting your car → I discovered the “evidence” that you had a married couple’s life insurance → I assume that it is you who arranged for the truck to hit your car → because if you were lucky enough to survive the crash and only your partner died in it → you would gain an immense amount of insurance money which would far exceed the cost of your car and starting your life anew with another partner → the risk/reward could make sense so I conclude that my original assumption that you arranged for the crash to happen is correct.

Another way of explaining why you are wrong in creating this vile connection between our intentions and the inevitable plight that we were victims of is by using a counterfactual. Or the opposite assumption if you will. One that you haven’t even shown us the courtesy of entertaining in this post: that we are honest people busting our asses to build a useful public good.

So, let’s reverse your assumption for a second and see how the arguments develop from that reverse assumption - based on the presumption of innocence:

You discover that our grant is targeted by sybil attackers → you assume that we are innocent, honest people that were victims of their own success and fell on the radar of malicious actors (farmers or competitors, NOT inimaginable in the crypto space…) → you defend the assumption that we are innocent based on the fact that even a project with the best intentions is technologically incapable of stopping outside people from conducting these targeted attacks. The way blockchains work, it is impossible to stop a bad actor from sending you Tornado Cash dust to your account or spammy donations, for example → also you don't find a clear link between the grantee and these multiple old and new sybil attacks, the only thing you are certain of is that attacks are happening and Fileverse is a juicy target to attackers → So you rightly decide that the burden of proof should not be on those good actors, because, by any stretch of imagination, there was nothing they could have possibly done to prevent attackers from targeting them → You decide to come up with ways to attack the attackers, and work on a better sybil resistance technique with the victims so that you can learn from their experience and prevent future injustices and the common pool from being drained from deserving public goods.

Instead, you publicly stripped us from the presumption of innocence that we deserve and presented arguments based on text book logical fallacies.

To conclude, the biggest problem I have with your argument is: what happens after Fileverse? Ok today you banish the favorite victim of a group of malicious attackers, but what happens when inevitably there is another Fileverse-type victim? You banish that victim as well for not being able to prove their innocence. And then, with the next favorite victim of malicious actors? Well you banish them as well, and so on, forever, hoping the attacks stop at some point if you remove enough juicy victims. All that because you decided to not take care of the attacker but instead to focus your attention on the closest sanctionable entity (which happens to be the victim) for being preferred by the malicious actor. GG WP, until next time.

## #5 What should happen to the grant considering the evidence? →

### #5.1: Nearly 70% of previous donations have been from sybil accounts → Without seeing the new equation, there was no alarm to look into this

Do you have this analysis for all the grants per round, please? This metric tells a completely different story when it is compared with other successful grants.

We are one of the top grants for the past two rounds, we started in GR13. If you take that fact alone it would explain this data. If we were a bottom 100 project in those past rounds this would indeed be a problem.

What you are essentially saying is that a top project is a good proxy indicator for the percentage of sybil accounts and/or airdrop farming activity since they are getting the bulk of all donations.

Note that during GR13 we got ~43% of ALL donations made on the platform during that round.

### #5.2: The second highest percentage of sybil donors in past rounds even without being a likely future airdrop grant

Yes, and? We are to be stripped of our legitimacy in public because we are victims of our own success? Why is this evidence of our intentions exactly?

Is it our fault that we are not doing an airdrop or are you saying that we are not doing an airdrop to keep the gitcoin farm spirit alive?

Again, we are one of the top grants for the past two rounds, we started in GR13. If you take that fact alone it would explain this data. If we were a bottom 100 project in those past rounds this would indeed be a problem. What you are essentially saying is that a top project is a good proxy indicator for the percentage of sybil accounts and/or airdrop farming activity since they are getting the bulk of all donations.

Can you put a similar analysis for all the famous grants per round? So we see how our “second highest percentage” compares with others in the, say, top 30 projects.

Also, we would also like to point out again that a famous Crypto Twitter account by the name of @Olimpiocrypto posted a thread (twitter[.]com/OlimpioCrypto/status/1568728742494875648) on projects currently with a grant on Gitcoin, that might have an airdrop in the future. The post went super viral by crypto standards (1626 likes and 559 retweets) and probably is the reason there was an explosion of new donations after our grant was reactivated. This happens a lot and affects every point you make in this list. What it should not affect is the presumption of innocence.

### #5.3: Over 10% of handles that donated during GR15 donated over 10 times during →  This is the highest percentage by far!

Apologies, but this is a statistics 101 mistake you made to support your point. Let me explain why:

You are making a percentage based comparison without mentioning the difference in absolute numbers. Thank you for sharing the sheet though, this helps in building a constructive feedback.

While computing the stats you use to claim “highest percentage by far!” we only had 31 contributors + 71 donations, so you got this statistic. The other projects on your sheet, which you are using to make a comparison that makes us look bad, have a much higher number of contributions. JediSwap, Umbra, Tally-ho, and the matching pool fund are the other victims of the same targeting we were, which you use to say “highest percentage by far”. So let’s compare properly to see why your statistic is misleading:

- JediSwap had a higher number of contributors to us by a factor of 25!!
- Umbra had a higher number of contributors to us by a factor of 13!
- Tally-Ho had a higher number of contributors to us by a factor of 21!
- Gitcoin matching pool had a higher number of contributors to us by a factor of 95!

And yet, you decided that our 31 contributors were enough data points to determine a percentage that is a) Sufficient indication of fraud and b) Appropriate to compare with other projects that had at a minimum over 13 times the amount of contributors.

Since when do statisticians only take the percentage without mentioning the absolute number to give context? How is that percentage relevant to an absolute number of 31 contributors when the projects compared to it have hundreds more contributors diluting the relative percentage?

I’ll give the benefit of the doubt to the person who ran those numbers, but I insist that you correct the record please.

### #5.4: Over 16% of past donations came from Squelched users →  This is THE MOST PAST SYBIL DONATIONS of any grant in GR15

This is the same issue as the above point. It’s a point that stands only because you don’t mention the absolute number.

This is based on the first hours of our GR15 where Filverse had less than ~70 donations in total and 31 contributors. If you replicate this now, is the number 16%? How much smaller is it? This is important for a statistical analysis that will negatively impact our whole project.

This argument is basically implying that to kill any grant on Gitcoin from now on, one malicious actor only needs to reach a 16% or higher by making a super obvious sybil attack very early on on a grant. In other words:

I hate project Y → within the first 2 hours of GR16 I make sure I attack it with enough very obvious sybil accounts → because its the first 2 hours the project doesn’t have many donations yet so my sybil accounts become a big percentage of the total contributors and donations → that project grant is deactivated → GG, easiest attack vector ever for competitors and malicious actors looking to kill a project.

### #5.5: Fileverse is in 22nd place for most donations under $2 when looking at all active grants previous donations

To repeat, please note that during GR13 we got ~43% of ALL donations made on the platform during that round. During the post GR13 assessment live on youtube, you mentioned that we were in the top 5 projects if there was no cap on matching. Why are you surprised that a top project is a good statistical proxy to the highest amount of sybil donations and/or airdrop farming activity?

We have built something useful here, that also is free and open source. That anyone with or without blockchain experience can use. That is non-financial/speculative and appeals to a different, less money oriented crowd. So you are saying it's bad to be popular? Or is it bad that people like our product / grant? Is it bad that Bernie Sanders got the most amount of low donations in the history of the USA elections by a huge margin because he was appealing to a different class of new voters?

One final, super important point, that relates to this and every point you make above.
What you are facing here, and failing to acknowledge despite the harm and distress you are causing us, is a chicken and egg problem:

What came first, the grant’s success or the sybil? Is the sybil there because of the success of the grant or is the success there because of the sybil?

The grant’s early success is because of the nature of our free DApp, because it's easy to use by anyone and requires no money, because it replicates in the web3 world one of the most popular activities on the web (file sharing), because of a smiley, shiny logo and because of the twitter grind of its founders. Additionally, GitcoinDAO is not the only group that has done due diligence on us, every funder that received our Ecosystem and Cause Round Eligibility Application and decided to add us to our side-round, namely, ENS, Polygon, a16z, and Web3Social, saw that we are a serious, deserving public good.

Because of that early success, our grant became the perfect target. Sybil attackers came flocking to us like vultures on a carcass, and did so so strongly and early that you are not capable of distinguishing our success from their manipulations. And you decide, with no evidence, that the sybil came first, that we are at fault, that we are taking the risk to kill our own project, a public good we have been working on with passion since day one, that by any measure is useful to a lot of people, in order to maybe gain the benefit of a bit of grant matching money.

If we were half the evil geniuses you describe, I can assure you there would be better ways for us to make money in crypto. We would already have a token by now, we would have already rugged, we would be like so many other crypto scammers that made it by exploiting people’s greed. Not building a self-evident, working, free, open source, DApp that keeps improving every day.

### #5.6: There are 4 more items which are available for steward council review if requested

Please share them in public as well. Would like this to be transparent to the community and since you are painting us as malicious actors.

The only way to fight this injustice, beyond having 3 founders drafting these answers instead of working on the product, is to openly invite all accounts we admire, or think are relevant for the situation you are putting us in, to invoke their knowledge and experience and help us solve this.

Fileverse team

-------------------------

Momonosukke | 2022-09-16 12:01:45 UTC | #5

Hi all,

So in the **first post** we tried to show you that we are honest actors on which the accusations really don’t fit, on which the profile of thieves doesn’t fit.

In the **second post**, we tried to show that your analysis had plain flaws because of the narrow focus and bad statistical comparison. That you generalised based on insufficient data and constructed logically problematic connection between limited incriminating data to a theory of the new attack vector and our intentions as grant owners / project founders.

What we did **this time** is try to understand the on-chain activity to find patterns that would prove to you that it was a targeted attack against **us rather** than just a sybil attack that unfortunately put us under a bad light.

We were not planning on doing a third post but were not able to sleep after being told that one of us was the culprit, so we did some dark forest investigation. It doesn't show definitive proof of the attackers identity, but it gives evidence that there is **one person** behind all the sybil accounts that were **explicitly set-up to do us harm** rather than just “help the grant get donations”.It gives you information linking all the addresses targeting us and others + us exclusively.

The reason it is crucial is because it invalidates your hypothesis that one of our team members tried to do good to our grant. If one of us wanted to help the grant through sybil accounts, the effort would have been focused on making good sybil accounts with low visibility if possible and game the QF + discoverability.

Instead what happened is a form of sybil that is **designed to be discovered** and discovered **very early** in order to make the DFF team focus on the most **incriminating early data** possible.


**Let’s start:**
As we can all agree that your analysis was done in the first few hours of the grant when it had 31 contributors and ~70 donations. If the analysis is done on the current numbers behind our grant, the “signal” would be completely different and the story that we are the attackers would not have been credible. 

Since it was obvious from past rounds that we are popular and victims of sybil attacks that target other popular grants too, the attacker knew that just doing a sybil attack that affects many grants would not be enough to get you to sanction us only and get us deplatformed.

So the attack needed to **start early** and be **reported early** (maybe even through the attacker themselves tipping your team) in order to inflict maximum damage on us, and get the DFF team to focus on us using the most incriminating data possible (where it shows high % of fraudulent activity tied to our grant because the absolute number is very small). 

What we essentially show now is that there is a pattern here where the most maliciously coordinated addresses, those that made the whole “**start the obvious attack early and report it early**” are **all linked together**. 

We can probably all agree that the most problematic evidence of attack are the accounts that only donated to Fileverse grant early on and that donated many times to it (>10). So they are ground 0 of our investigation.

Because the donations had very little money in them and were spammed almost every day for over four weeks in some cases, it makes sense that the attackers would use a cheap chain. We started looking for those donation patterns on Polygon and ZkSync.

Because we don’t have access to your backend we did the next best thing and tried to identify donations made to us (our zksync address) using these parameter: 
- Username and Timestamp from Txn confirmation message on gitcoin
- Committed Timestamp in the Txn on ZK Sync
- Amount donated to fileverse account

**This is what we discovered:**

1. Link between wanghaha and cici and other connected addresses.
2. All the sybil accounts using multiple similar services (bridge/mixer and centralised services -OKx and FTX) in the same timeframe. 
3. Similar pattern of changing the public key only on the zksync and not the main account all together. AND to attack us before GR15 and very early on during GR15 to become a majority of donations on our grant.

(1) We found addresses corresponding to cici0910 and wanghaha02’s activities (the sybil accounts made for targeted attacks on us) on ZkSync. To help our investigation further and retrace their activities and links to other addresses that may reveal their identities we bought a subscription to Breadcrumbs.

Here you will find the txs hashes, links to breadcrumb graph reports on each address, names of centralised exchanges they used, and even mixers they used to obfuscate the links: https:// docs.google[.]com/spreadsheets/d/1ZVAgT9SGL633NQVTstCKhrqIlUtK5gzW38r-Gxn2qjo/edit#gid=0 

You will see that cici and wanghaha made transactions to each other on zksync.

(2) We found that cici and wanghaha are connected to each other and funded by the same entities. In looking into the txs graph of those accounts we discovered two more addresses. When looking into them we saw they were also donating to us but with a different pattern of recurrence and with a different public key on zksync and using the same services to get funds.

When we compared these two new addresses to the list of addresses that were donating to us (which grant owners can see on gitcoin) we saw that they were not there, confirming the public key change theory. So we did the next best thing and looked at which accounts donating to us had made donations similar to the addresses we had found on Zksync.

After a while we found them, they are probably: yaya0910  (Note that @yaya0908 - @yaya0905 were donating before the grant round had started). 

All of them are using the same mixers, and the same exchanges.

There might also be a connection with 123456dao.eth but we are not sure of that. It’s just something that seemed connected looking at breadcrumb’s graph.

(3) That all those connected addresses made sure to attack us before GR15 and very early on during GR15 in such a way that would make them a **significant %** of our total contributors and a **majority of our contributions** (because of >10 donations).

The good news is that now we know for sure that it is one scummy attacker that is behind all this and wants to harm us. 
 

**A potential suggestion to nail this:**
The other part which may have potential for good news is that we know attackers used OKx and FTX for the initial funding. So we suggest that your team and ours fill a report to those exchanges and ask that they either provide some identity for the attackers (which is unlikely because we would likely need to contact law enforcement first) OR ask them to provided just a confirmation that the account behind those sybil attackers are not us (by KYC’ing us basically). With the second option, these exchanges wouldnt dox their user but would be able to give harmless information about us not being the attackers. 

Another important correction we would like to submit to your analysis is about the new Sybil Attack Equation you suggested. We made one addition that we really want you to add as well because it’s crucial to the costs you are considering and changes the whole attack dynamic. You can find it here:
https:// drive.google[.]com/file/d/1Jm2mUn6aC6eklcsL_pIiY2mKnbi7NowZ/view?usp=sharing

Voila. This is what we could do with our limited resources. With access to some of your backend info and dataset of known sybil accounts with their primary addresses, we think that an experienced investigator would be able to find some more proof of identity of the attackers. So maybe we can co-fund that investigator?

-------------------------

DisruptionJoe | 2022-09-16 21:05:30 UTC | #6

[quote="Momonosukke, post:5, topic:11505"]
So in the **first post** we tried to show you that we are honest actors on which the accusations really don’t fit, on which the profile of thieves doesn’t fit.
[/quote]

I agree that your team seems like great people. 

[quote="Momonosukke, post:5, topic:11505"]
In the **second post**, we tried to show that your analysis had plain flaws because of the narrow focus and bad statistical comparison. That you generalised based on insufficient data and constructed logically problematic connection between limited incriminating data to a theory of the
[/quote]

There is much more analysis done than simply what you have sited. We didn't only look at the 31 donors so far in GR15, but also each round before and a cumulative view. I am however challenging our analysts to clarify the arguments here and make the result visually accessible. 

[quote="Momonosukke, post:5, topic:11505"]
(3) That all those connected addresses made sure to attack us before GR15 and very early on during GR15 in such a way that would make them a **significant %** of our total contributors and a **majority of our contributions** (because of >10 donations).

The good news is that now we know for sure that it is one scummy attacker that is behind all this and wants to harm us.
[/quote]

The most difficult thing to reckon is that an attacker wanting you deactivated would use this strategy because we never deactivated a grant for this before. Additionally, it happened in GR13 and 14 too. This means that the attacker must have doubled down on an unsuccessful strategy. 

Our analyst got pulled off this today and yesterday so we will leave the grant active in good faith. The dispute is still open and we will be trying to find something that is more convincing. Unfortunately, the arguments you presented in post three would be valid for either hypothesis and do not narrow down the potential reasons. 

Please take the weekend as our team will be putting in extra hours and we aren't going to deactivate or disqualify until we have gone deeper on the analysis here.

-------------------------

Momonosukke | 2022-09-19 18:05:02 UTC | #7

[quote="DisruptionJoe, post:6, topic:11505"]
Unfortunately, the arguments you presented in post three would be valid for either hypothesis and do not narrow down the potential reasons.
[/quote]

Hi all,

This is our fourth post. You suggested that we rest during the weekend while you continue your investigation but the stakes are simply too high for us to just stand by and wait. We hope you can understand that.

This post presents an extensive on-chain analysis of the sybil accounts targeting our grant, and describes the custom open source tool we’ve built for establishing patterns of attack in sybil networks targeting the Gitcoin platform and individual grants like ours.

One of the main arguments you use in your original post is that there was an alarming, **exclusive focus on our grant** by the sybil accounts you flagged which made you hypothesise that it must be because we are behind them. This is the one outstanding point that our previous posts may not have challenged enough, simply because it required that we spend hours and hours on-chain to prove that something else was up.

Our analysis below shows this has been happening on other grants too, where there are networks of sybil accounts donating to individual grants and using the same on-chain transactions pattern you can observe in the flagged sybil accounts donating to Fileverse.

**TL;DR:**

* We analysed the on-chain activity of the donor accounts that you (correctly) flagged as suspicious and (incorrectly) used as evidence that we are gaming the platform.

* We followed the trail and found that these donors are part of a large network of sybil addresses attacking the Gitcoin platform as a whole.

* We found that other popular grants on Gitcoin are receiving identical sybil attacks to the ones we received. Where you can see sybil addresses in that large network donating exclusively to their grants.

* The evidence we use to connect sybil accounts donating only to our grant with sybil accounts donating only to other popular grants is the discovery of a specific script being used across a large network of sybil addresses making donations via zksync.

* The fact that other grants are being targeted by a network of sybil addresses donating exclusively to them using the same script that sybil accounts used to donate exclusively to us disproves the allegation that we orchestrated a new attack vector to benefit our grant.

* We describe the script in the below analysis.

Our hope is that by publicising our analysis and open sourcing the custom tool we built for it, we will help the Gitcoin DFF team find overwhelming evidence and squash the sybil attack problem of the platform once and for all so that honest actors never have to experience the distress that our team had to experience in the past week.

**The analysis:**

We spent the weekend building a tool that aggregates metadata associated with donors on different chains (zksync, polygon and ethereum) and analyses their transaction pattern and connections.

We analysed all donations made to our grant and found that the addresses associated with potential sybil accounts were all donating to us by following the same pattern of transactions which we describe below:

* Retrieve money from the same bridge (0x80c67432656d59144ceff962e8faf8926599bcf8)
or from an address that retrieved money from the same bridge and then followed the below pattern.

* Do the similar type of transactions prior to the donation (do some token swaps and/or mint some NFT).
* Donate on low nonce, below nonce 15.
* Donate to our grant only.
* Return the rest of the money back into the bridge.
* Stop all activity once nonce 15 is reached or before.

As you understand, this was already a big find for us. It showed us that these attackers were very likely using a script and then discarding the addresses used for donating before nonce 15 or when they reached nonce 15.

Our next step was to find evidence that this script was being used by other addresses on zksync and see if those addresses were donating exclusively to other popular grants.

Because we didn’t have access to the dataset of donations of other popular grants, we analysed every address that interacted with the same bridge (0x80c67432656d59144ceff962e8faf8926599bcf8) our attackers used. Because the list would have been too long for us to analyse with our resources, we narrowed it down to every address that interacted with that bridge and had nonce 11 or 9. Why 11 and 9? Because we knew that the attack range occurs below nonce 15 and because we saw in our manual review that these two nonces were quite recurrent.

Our analysis of the bridge was done during the timeframe: 7 - 12 Sept.

This gave us a list of 198 addresses. Of these 198 addresses, we found that a whopping 87 of them were using the exact same script to exclusively attack individual grants on Gitcoin!

In this spreadsheet, we show these 87 different addresses we discovered on zksync and which grants they donated exclusively to:

https:// docs.google[.]com/spreadsheets/d/1WKACqtXCaVsFmak7AUwrzrKDO3OaK7s32NZQqH7TF1E/edit#gid=1646267492

So in a random sample of addresses using that bridge with nonce 11 or 9 you see that they all:

* Retrieve money from the same bridge.

* Do the similar type of transactions prior to the donation (do some token swaps and/or mint some NFT).
* Donate on low nonce, below nonce 15.
* Donate to one grant only.
* Return the rest of the money back into the bridge.
* Stop all activity once nonce 15 is reached or before.

In this list of addresses we used, we found that they are donating exclusively to **Fileverse** or exclusively to **Syncswap** or exclusively to **Pyme** or exclusively to **JediSwap** or exclusively to **other grants** we could not identify in our analysis.

—------------------------------

**Side note:**

Another part of our efforts, which is less important but gives you a bit of context on how we ended up discovering that important bridge (0x80c67432656d59144ceff962e8faf8926599bcf8), is that **cici** and **wanghaha**, which are the two accounts we focus on in our previous post, led us to its discovery. These two accounts followed a different pattern (beginning their activity on Arbitrum) and making weeks worth of donations to our grant prior to GR15 even, but ended up using the same bridge (0x80c67432656d59144ceff962e8faf8926599bcf8) on multiple occasions.

This document describes in detail the trail we followed for them in order to arrive at the discovery of the bridge, our analysis of it and finally the discovery of the network of sybil addresses that donate exclusively to certain Gitcoin grants: https:// docs.google[.]com/document/d/1U_7bancvXPhIWV_10s1tspQJPiO-_eck35avH5rOEQs/edit

—------------------------------

We were able to connect these important dots despite not being pros in on-chain investigations and despite having limited data at our disposal.

Two things can be done to help nail this even further:

* First, to ask other grant owners if they would be willing to use our tool to make a similar analysis over a longer period of time. We are confident that if we were able to find so many connections with the limited data and resources we had, these connections will be even clearer using a larger dataset and by crowdsourcing the analysis.

* Second, we took the liberty of getting in touch with different on-chain investigators with whom we will share our findings and who have accepted to look into these sybil networks. We will be putting a bounty up on Gitcoin or publicly on Twitter for them to receive when they have uncovered connections between our attackers (sybil donors targeting us exclusively) and other attackers on the platform / on other grants (sybil donors targeting them exclusively). And an even higher bounty for whomever discovers the real identity of the originators of these sybil donor networks.

We believe that crowdsourcing this investigation is the only way forward to create a sybil resistant Gitcoin platform and we hope that our analysis, tool and bounties can contribute to this and help you in your work.

We paused all our work on our DApp to focus on your unjust allegations and request to “prove” our own non-involvement with this attack. To do so we had to do a deep dive in the available data and scavenge on-chain for evidence. It took a big mental (and resource) toll on us. But because of what is at stake for Fileverse and our whole team, we did it. With this fourth post we clearly invalidate the original assumptions you made. With this fourth post we are proving that what was missing was an in depth on-chain analysis of donations to gitcoin grants and a comparison between them. Something that is very hard because of the lack of tools existing to aggregate and analyse transactions on zksync. With this fourth post we also open source the tool that builders on Gitcoin will need to protect their grant if ever they find themselves in the unfair situation Filverse was put in.

We hope that with all the information and evidence shared with you now, you will realise that we did not game the platform and that we are not behind these sybil networks attacking us and many grants on the Gitcoin platform.

**Tool Repo**: https:// github[.]com/fileverse/sybil-analysis

-------------------------

DisruptionJoe | 2022-09-21 23:14:49 UTC | #8

Our analysis shows sufficient evidence of a unique Sybil attack targeted on this grant, which began promptly at the start of the round and stopped abruptly several days into the round. 

Because this is a new attack vector and we cannot directly link the owners of the grant to this activity, we have decided not to deactivate the grant. We will, however, continue to take the usual action of disqualifying all Sybil donations from the quadratic funding allocation. 

Furthermore, we believe that the brief period for which the grant was deactivated served as a counterbalance for the early momentum the grant received as result of the Sybil attack. 

We believe this incident provides an important lesson for our community. If this type of attack becomes more prevalent in the future, then we reserve the right to deactivate such grants. We urge any grant that believes it is the target of a Sybil attack to alert us immediately, rather than wait for us to detect the activity.

-------------------------

Momonosukke | 2022-09-24 00:15:10 UTC | #9

Hi Joe,

Thank you for your ongoing efforts on this.

We are really relieved that you are not deactivating our grant and choosing to target fraudulent contributors rather than their victim, Fileverse.

I will be honest, we were hoping you would also correct the record and admit that your allegations were unjustly harmful to us. But I guess that is not how you want to go about it.

You are right in saying that you cannot link the owners of the grant to this fraudulent activity, that is because they are not linked. We wish that you had recognised that from the start instead of first assuming guilt and requiring our small team to cease all development activity on our DApp to do on-chain investigations to prove our own innocence.

**We had to fight this uphill battle on our own and it really had a big toll on us.**

Our last analysis (post 4) showed that the network of sybil accounts targeting our grants were directly linked to other big networks that were automating attacks on other popular grants as well. We hope this is being investigated further by your team so that **GR16** can begin with a healthier foundation. We also hope that the Sybil Analysis tool we built and open sourced will help your team do more in-depth analysis of attacks.

As you suggested, we also want to immediately flag the following account, that, **after GR15 ended**, spammed 48 (!!) micro-donations to the Fileverse grant: https:// gitcoin[.]co/bravewallets

This is the type of accounts that are just net negatives for everyone on Gitcoin. They seem to only serve to raise suspicion about certain grants, distract the DFF team and ultimately poison the platform as a whole.

Finally, we also decided that if we want to rely on Gitcoin in the future, we would need to actively contribute to its improvement. Hence,

* (1) we are presenting a list of recommendations and tools in our next forum post, which we hope we can discuss with you to make Gitcoin fairer and more robust.
* (2) we will be continuing the discussion with known on-chain investigators that took an interest in this unjust situation we were put in; in the same vain, we will also propose in our next post to co-fund with Gitcoin a bounty to build on the research and evidence we shared in post 4.

-------------------------

ccerv1 | 2022-09-26 16:31:42 UTC | #10

[quote="Momonosukke, post:9, topic:11505"]
Finally, we also decided that if we want to rely on Gitcoin in the future, we would need to actively contribute to its improvement
[/quote]

Yes! As the DAO moves to further decentralize Sybil detection, it seems inevitable that communities who rely on grants as an important source of funding will need to be more proactive in identifying attack vectors and quid pro quo arrangements. Every grantee in a community/round should take a strong interest in preventing Sybil attacks because successful attacks undermine the credibility of the QF mechanism. Thank you for leading the way here :pray: 

The hard part is that it's virtually impossible to establish the motive of a Sybil attacker and to "prove" they have no affiliation with a grant that's in an active round. As there will rarely if ever be a smoking gun, we need to build collective intelligence and mechanisms that align all grantees with the incentive to defend the system rather than attack it.

-------------------------
