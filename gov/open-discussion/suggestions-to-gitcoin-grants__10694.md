---
id: 10694
title: "Suggestions to Gitcoin Grants"
slug: suggestions-to-gitcoin-grants
category: open-discussion
url: https://gov.gitcoin.co/t/suggestions-to-gitcoin-grants/10694
created_at: 2022-05-24T11:44:27.689Z
last_posted_at: 2022-05-26T20:33:46.595Z
posts_count: 2
views: 3031
like_count: 5
---

# Suggestions to Gitcoin Grants

<https://gov.gitcoin.co/t/suggestions-to-gitcoin-grants/10694>
Raphina | 2022-06-01 17:42:20 UTC | #1

Hey Gitcoin team,
I am Raphina from Primitives Lane. As an early user of Gitcoin, both myself and Primitives lane have witnessed your tremendous growth. We are very grateful for your dedication to the public good.
However, in order to better fight for Moloch, we do have some suggestions :grinning:

:heavy_heart_exclamation:**Statistics**

:thinking:**1. Incorrect statistics** :face_with_thermometer:

* a. We requested the grant statistics for analysis and received from Gitcoin after GR13. When we were checking the data, we found that one donor donate 1 ETH to us (txid: sync-tx:2acec8d4d31123ccc58c491989fadb6134667743c313d6d0d451b476fe2545ca), but we actually didn’t receive it, so we checked out on zkSync and found the donor only donate 1 DAI(https://zkscan.io/explorer/transactions/0x2acec8d4d31123ccc58c491989fadb6134667743c313d6d0d451b476fe2545ca) while the donor’s gitcoin profile page shows the 1 ETH transaction failed.
**We still didn’t understand why the data was wrong and is there any other mistake that we didn’t find in the exported data form? Any possibility to help us figure out why?**


**![|602x95](upload://tGBMJRVRdgZZYiX3b2WOGkJpUkA.jpeg)**

* b. **There’s no donation status (success/failure) through the exported data form**, it is really confusing that the donation amount we calculated from the data form is not the same as what we actually received on gitcoin (since some transactions on the form actually failed.)

:slightly_smiling_face:2. Traffic tacking:

*  a. The creator can't see what collections the grant has been included in, and therefore can't analyze the related traffic sources. It would be better if owners of grants can get notifications when grants are added to collections.

* b. There’s no notification of being included in the official list, so it is impossible to analyze the traffic sources related to the list. It would be great if owners of grants can get notifications when grants are included in the official list.

* c. The creator can’t see the source of home page visits. If there is a traffic-related data analysis function, grants can better optimise the promotion methods and achieve better fundraising results.

3. We are also interested in the cumulative amount of donations made by individual users and donation amount range distribution

4. It would be great if there are richer and more refined data analysis dimensions, e.g, a,filter the donation data by Grants Round (rather than date)


:heavy_heart_exclamation:**User Experience**
1. The banner at the top of the grant's homepage uses the logo uploaded by grant creator, and the thumbnail of the homepage sharing link only displays the middle square part of the banner, so for any banners that are not square, it will be cut rather than kept the full logo. Here is an example:
**![|602x193](upload://Alr9QossKCCWgNLOARywtAQBVtG.png)**
We suggest setting separate options for the logo（square like 500x500） and banner, meanwhile, using the logo for the thumbnail in the sharing link.

2. According to [Fundraising Principles and Practice](https://onlinelibrary.wiley.com/doi/book/10.1002/9781119228974) written by Co-Director of the Institute for Sustainable Philanthropy[ Adrian Sargeant](https://www.linkedin.com/in/adriansargeant/?originalSubdomain=uk), **donors tend to donate in reference to other donors' amounts.** So it would be better to set suggestions for donation amounts, perhaps by displaying objective donation data, or by setting a few recommended donation amounts for the grants by creators themselves. There are also some best practices like on Patreon and Wechat Official Account, people can donate easily by just clicking the suggestion amount button.
**![|602x547](upload://haxBkmthbw0phOGNr1qzpK25MQg.jpeg)**

3. For now, it seems that the exported data on donations is according to users. What if someone has multiple accounts?



**Not sure which category the thread should be posted in, please let me know if this is not the correct sub-category and I would move it to the correct one, thanks!*

-------------------------

nategosselin | 2022-05-26 20:33:46 UTC | #2

Hey Raphina, thanks for taking the time to provide such detailed feedback! I'm on the product team for Grants and wanted to share some thoughts back.

**Re: the incorrect statistics** for that specific transaction, I'm not entirely sure what happened — and I'm sorry for the confusion! I'm going to look into this, but do you mind dropping an email to support@gitcoin.co so we have your email and can work through it with you directly?

**Re: the rest of your suggestions**, this is all incredibly helpful feedback. We're in the process of revamping our Grants software product through the [Grants 2.0 protocol](https://gov.gitcoin.co/t/gitcoin-grants-2-0/9981), which @owocki also [wrote about this week](https://gov.gitcoin.co/t/the-grants-2-0-flywheel/10711). A big design consideration for this initiative is data availability, and your suggestions are super useful inputs to that work. Right now the teams are working on laying the foundation of the protocol (you can see weekly progress on the gov forum — [here's this week's](https://gov.gitcoin.co/t/weekly-grants-2-0-update-2022-5-23/10679)) but as we get further into development this summer we'll start to turn our attention to things like this.

Thanks again, and feel free to reach out with any questions!

-------------------------
