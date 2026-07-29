---
id: 10418
title: "Introducing Steward Health Cards 2.0"
slug: introducing-steward-health-cards-2-0
category: governancevision
url: https://gov.gitcoin.co/t/introducing-steward-health-cards-2-0/10418
created_at: 2022-04-26T08:48:45.966Z
last_posted_at: 2023-01-04T01:07:55.988Z
posts_count: 20
views: 5903
like_count: 40
---

# Introducing Steward Health Cards 2.0

<https://gov.gitcoin.co/t/introducing-steward-health-cards-2-0/10418>
sidcode | 2022-07-28 16:02:28 UTC | #1

Authored by @fred @sidcode

## Summary
The MMM-Workstream have released an update to the Steward Health Cards, live via both [DNS ](https://www.daostewards.xyz/)and [ENS](https://stewards.eth.limo/). The first version of the project was [launched in Q3 2021](https://gov.gitcoin.co/t/introducing-steward-report-cards/8712) and has been discussed further in the context of the [Steward Council](https://gov.gitcoin.co/t/introducing-the-steward-council/9485) spearheaded @Pop.

This thread summarizes our newest update with features that make the cards even more comprehensive and powerful. We invite the community to continue to share feedback and help us improve this public good further!

## Improvements
Even though the look and feel of the site has stayed close to the original design, the backend and data infrastructure has been completely rewritten. The site is now able to deliver greater granularity of metrics and much improved automation. This has been possible due to our partnership with [Karma](https://www.showkarma.xyz/), a reputation system for DAO contributors. Both Stewards Health Cards and Karma share a common goal of aggregating information and engagement of DAO contributors to increase transparency and accountability. As a result of us being able to grab richer data the overall health calculation should provide an improved representation of each Steward’s engagement in GitcoinDAO.

The way we calculate Stewards' health has also been adjusted based on feedback received from the community. Previously, all activity on the forum had the same weightage in the health calculation. With the new release, we are now differentiating between forum threads and forum posts with different weights. We are also differentiating between activities in the “[Proposal discussion](https://gov.gitcoin.co/c/governance-proposals/5)” section of the forum versus other sections. Activity in the Proposal discussion has a higher weight due to the higher level of conversation often found within this category.

**Variables**:

**`V`** = &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Vote participation on Snapshot (only proposals with >0.5M GTC are counted)
**`F_t`** =&nbsp;&nbsp;&nbsp;&nbsp; Forum Topics initiated (excluding the “Proposal Discussion” category)
**`F_t_p`** = Forum Topics initiated in the “Proposal Discussion” category
**`F_p`** = &nbsp;&nbsp;&nbsp;&nbsp;Forum posts (excluding the “Proposal Discussion” category)
**`F_p_p`** = Forum posts in the “Proposal Discussion” category
**`W`** = &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Workstream involvement. Lead role adds 5p and contributor adds 3p to health.

Visitors of the site can now choose to display metrics and health for either Lifetime or the Last 30 days. The new health score calculations are as follows:

**Lifetime health** : &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `V*0.7 + F_t*1.1 + F_t_p*1.5 + F_p*0.6 + F_p_p*0.7 + W`

**Last 30-days health** : &nbsp;&nbsp;&nbsp;`V*0.7 + F_t*1.1 + F_t_p*1.5 + F_p*0.7 + F_p_p*1 + W`

[Tally participation](https://www.tally.xyz/governance/eip155:1:0xDbD27635A534A3d3169Ef0498beB56Fb9c937489) was previously used in the health calculation but has now been removed. Proposals that reach Tally have already passed GitcoinDAO governance on the forum and Snapshot. The on-chain nature of Tally voting results in gas costs. Therefore, Stewards might not vote after the quorum has been reached which makes it an unsuitable data point to use in this context.

Please note that these formulas are our best attempt at fairly representing Steward engagement with the data available to us. We appreciate feedback and invite you all to help us improve further!

## Looking ahead

The vision of the Steward Health Cards has always been to provide the most valuable metrics for each Steward with the goal of improving the transparency and accountability of their work. The cards may function as a tool to assist delegators making informed decisions and to allow Stewards to compare their involvement relative to their peers. Steward Health Cards have been completely built in public and can be forked without permission by any community with a similar governance structure.

We are continuously working on improving the site with new features and improvements. A couple of features we have in the pipeline for the upcoming season include:

* Web3 login for Stewards to have control of their card and-
   -  Change their picture
   -  Add addresses
   -  Add link to Twitter & Github
   -  Ability to add additional Stewards to their Workstream
   - Ability to opt-out and remove their card
  
* Introduction of Workstream cards
* Minting “End of Season”-cards and allow users to scroll through Seasons
* Introducing additional metrics to capture other types of engagement such as on-chain compensation, attendance to monthly Steward calls and involvement in working groups not tied to any specific Workstream

We look forward to continuing working together with the community to map our collective health and make it available to the broader ecosystem as a public good!

-------------------------

seedphrase | 2022-04-27 11:46:05 UTC | #2

Kudos to yall and the Karma team! I know alot of work has gone into making this update happen.   Really looking forward to the new features that will be added in the next version. I love the minting of an "end of season" card-maybe we can tie this to some special token-gated merch in the schwag store? :smile:

-------------------------

linda | 2022-04-27 13:17:09 UTC | #3

Thank you for your work on this!

-------------------------

Pop | 2022-05-01 10:09:58 UTC | #4

SO excited to see this evolve and finally becoming an important, living DAO tool. As mentioned in all my conversations with @Fred and others in the DAO, building objective and dynamic engagement flows are key to evolving governance and making it sustainable. 

When discussing the variables and metrics involved, it was very important to me to capture FAR more than votes for a more complete and complex view into participation. It enabled me to determine the formation of the Steward Council and I hope it will enable a more fluid governance structure. Being able to undelegate from a steward who may have dropped in engagement to another who is in line with one's values AND has a high engagement score is much more in line with the ebbs and flows or activity and daily life. 

My idea of expanding this model to workstreams and treasury health is in line with creating tooling that easily measures and quickly provides the context needed for informed, complete and  objective decision making.

-------------------------

owocki | 2022-05-09 18:08:42 UTC | #5

Right now I'm sorting the data by "Last 30 days".  Is that the last 30 days as of right now, or as of 13 days ago when this gov post was created?

Would it be possible to make that more clear?

Is there a way to expose the raw data behind the steward report cards?

-------------------------

krrisis | 2022-05-10 14:00:18 UTC | #6

Will hopefully find the time to respond in more detail at a later point, but very happy that this exists and continues to evolve. 

Quick question for now, [could you fix the preview image,](https://twitter.com/krrisis/status/1524026020373962754?s=20&t=31PMJYasnA0LMlXyNinXpQ) so that it's easily shareable on the socials?

-------------------------

Fred | 2022-05-11 15:39:21 UTC | #7

"Last 30 days" display metrics and health based on the last 30 days.

The daily update-script did lag for a couple of days but should now be up and running again.
An indicator that display how many hours ago the data was last updated will be added to the site as well.
Potentially we can also add information of the start- and end-dates when looking at “Last 30 days”. That indicator would for example today read: "April 11th - May 11th".

Raw data for the Stewards can be found in [this json](https://github.com/mmmgtc/stewards/blob/main/assets/json/stewards_data.json).

@krrisis: We are looking into why the Twitter card has stopped working. Thanks for the heads up!

We have a lot of ideas on how to improve the site further and are actively working on new features and optimizations. Looking forward to hear more feedback!

-------------------------

owocki | 2022-05-11 19:24:04 UTC | #8

[quote="Fred, post:7, topic:10418"]
An indicator that display how many hours ago the data was last updated will be added to the site as well.
[/quote]

nice; this would solve for my questions.

[quote="Fred, post:7, topic:10418"]
Raw data for the Stewards can be found in [this json](https://github.com/mmmgtc/stewards/blob/main/assets/json/stewards_data.json).
[/quote]

thanks!

-------------------------

mmurthy | 2022-05-12 18:26:12 UTC | #9

[quote="owocki, post:5, topic:10418"]
Is there a way to expose the raw data behind the steward report cards?
[/quote]
If you are interested in more raw granular data that went into some of these calculations, you can find it [here](https://api.showkarma.xyz/api/dao/delegates?name=gitcoin&pageSize=100&offset=0&workstreamId=4,6,3,7,1,2,5)

-------------------------

krrisis | 2022-07-07 18:04:51 UTC | #10

hey Fred & @sidcode I see the 30 days has disappeared now, only lifetime is in there. Is that as planned?

-------------------------

David_Dyor | 2022-07-08 16:34:06 UTC | #11

I am having technical difficulty with my Steward Health card.  Made over 90 forum posts but I show 0.  Same with vote participation, did many but none show up.  Any suggestions about how to fix this?

-------------------------

Fred | 2022-07-09 08:44:23 UTC | #12

Hey, yes unfortunately we ran into some issues with the 30days metrics.

We pulled it down as we are working on a fix. Will be back up shortly!

-------------------------

Fred | 2022-07-12 15:46:02 UTC | #13

Sorry about that, it seems like we had an issue with your forum handle in the backend. Will get this fixed asap. Thanks for flagging!

-------------------------

David_Dyor | 2022-07-14 15:34:51 UTC | #14

Considering some aspects of the Steward Health Cards 2.0 are under repair, can we not take any snapshots or base any elections until the cards are confirmed as correct?  For example my score changed from 3/10 to 10/10 over the last day.  It is possible others are also misrepresented.  I don't want to see any active stewards excluded from any opportunities because of a glitch.  I thought I read recently the next Steward Council will be created soon.  No council elections, which require a minimum health score, should proceed until we confirm the cards are displaying accurate data.  (imho)

Huge thanks to Fred for being on-top of this!

-------------------------

Fred | 2022-07-24 10:47:23 UTC | #15

The site is functioning as intended with correct metrics for each Steward. We're in close collaboration with Karma to make sure metrics are always correct and up to date.

We’re also dedicated to make sure it straightforward to audit the metrics, both through the links on the card and through the repository.

Your card was an edge case due to you changing your Discourse username from blazingthirdeye to David_Dyor. Your previous message in the Steward intro-thread also got removed due to the name change which resulted in the card displaying empty stats.

This all resultet in your card having 0/10 health, but your role as Contributor to FDD gave you +3 which resulted in 3/10 overall health.

I was not aware of the name change previous to you flagging it, we’ve pushed a fix to correct the name and your card is now correct. No other cards were affected.

It’s incredibly important for us to make sure metrics on the site are up to date and correct. 
When we realized some cards were displaying empty stats for 30 days we immediately removed that option until we had a fix deployed.

-------------------------

epowell101 | 2022-08-16 20:32:08 UTC | #16

Hi @Fred @sidcode erstwhile steward here.  Wondering when I might be listed on health cards?  

For ease of access, profile here:  https://gov.gitcoin.co/u/epowell101/summary

Please LMK if I'm missing something.  Gamification FTW!

-------------------------

chaselb | 2022-12-31 20:05:32 UTC | #17

Is the stewards health card site open source? If so, can someone link it?

-------------------------

shawn16400 | 2023-01-02 13:26:41 UTC | #18

Hey Chase - yes this is [daostewards.xyz](https://www.daostewards.xyz/).  But to note, the site has a number of issues and omissions and we are unit testing a new site now with help from @mmurthy and the team at [ showkarma.xyz](https://www.showkarma.xyz/).  We will relaunch this new site in Jan and a list of planned improvements.

-------------------------

chaselb | 2023-01-02 20:41:00 UTC | #19

I meant to say is the site open to forking/contribution. Like is it maintained openly on github or something similar? Or is it being worked on closed-source? Excited for the new site. Thanks shawn.

-------------------------

mmurthy | 2023-01-04 01:07:55 UTC | #20

Chase - The frontend is open source, you can find the code here https://github.com/show-karma/dao-delegates-app. The data comes from our backend where we index all the contributions and aggregate it.

-------------------------
