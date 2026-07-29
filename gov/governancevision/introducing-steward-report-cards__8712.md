---
id: 8712
title: "Introducing Steward Report Cards"
slug: introducing-steward-report-cards
category: governancevision
url: https://gov.gitcoin.co/t/introducing-steward-report-cards/8712
created_at: 2021-09-30T21:54:35.548Z
last_posted_at: 2022-05-25T18:21:04.398Z
posts_count: 24
views: 7524
like_count: 64
---

# Introducing Steward Report Cards

<https://gov.gitcoin.co/t/introducing-steward-report-cards/8712>
Fred | 2022-02-05 12:27:40 UTC | #1

The [MMM-Workstream](https://gov.gitcoin.co/t/proposal-merch-memes-marketing-workstream-budget-request/8562) are proud to present *Steward Report Cards*, live via both [DNS](https://www.daostewards.xyz/) and [ENS](https://stewards.eth.limo/)!

![|602x331](upload://h4RrPkWPoRs7vOlxyKZkQ6PNRga.png)

The stewards of Gitcoin DAO play a vital role in driving the Gitcoin ecosystem forward through their work in governance and in workstreams. Previously there hasn’t been an easy way to gauge their level of engagement within the DAO. The Steward Report Cards aims to solve this problem by providing the most valuable metrics of each steward and improve the transparency and accountability of their work. The cards may function as a tool to assist delegators making informed decisions and to allow stewards to compare their involvement relative to their peers.

Public data of each stewards involvement in discourse, workstreams and governance participation are presented and combined to calculate an overall health-score. The titles on the card are clickable and will respectfully route the user to the data source with more info.


**A quick walk through of the cards**

* **Steward since:** This is the date that the Steward introduced themselves on the [governance forum](https://gov.gitcoin.co/t/introducing-stewards-governance/41). The earliest date is the [launch of Gitcoin DAO](https://gitcoin.co/blog/introducing-gtc-gitcoins-governance-token/), 25th of may 2021. Link goes to the Stewards introduction post on the forum.

 * **Forum posts:** The number of comments and threads started on the governance forum. 
Link goes to the Stewards profile on the forum.

* **Workstream:** Involvement in any of the Workstreams of Gitcoin DAO according to the public information of the governance forum and on [Notion](https://www.gitcoindao.com). 
Link goes to gitcoindao.com

* **Voting weight:** The percentage of governance tokens delegated to the Steward in relation to the total number of tokens. 
Link goes to the stewards GitcoinDAO-profile on Tally.

* **Vote participation:** This value displays the percentage of proposals [Snapshot](https://snapshot.org/#/gitcoindao.eth) the Steward has participated in. Non-serious proposals on Snapshot are not taken into consideration. As of writing this post, participation in 20 out of 25 proposals are required to achieve a 100% score. On-chain voting on proposals via [Tally](https://www.withtally.com/governance/gitcoin) are not displayed on the cards but are taken into consideration in the health-score calculation, more on this below.
Link goes to the GitcoinDAO-page on Snapshot.

* **Health:** The metrics described above are combined into an overall health-score, displayed in the top right corner of the card. The current formula for calculating the health of a Steward is based on three sub-scores; Forum-score (F), Voting-score (V) and Workstream-score (W):

  * F = 1.75 * Posts/Weeks as Steward
(the maximum forum score is set to 1.5)

  * V = (2.2 * S + 1.5 * T) / 2
  where;
  S = Snapshot participation
  T = Tally participation

  * W = Lead Stewards of a Workstream gives 5 points. Workstream contributor gives 3 points.

  These are combined to achieve an over-all health-score:
   * Health = F * V + W

  *(We are exploring additional ways to represent Steward involvement in Workstreams and DAO-wide initiatives.)*

* **[Statement]:** Link to the stewards introduction post on the forum.

* **[Delegate]:** Link to the stewards GitcoinDAO-profile on Tally with an option to delegate GTC.


The search field at the top of the site allows the user to quickly find a specific steward or group of stewards. It is also possible to link to a specific card, or a group of cards, by utilizing the search function. As you search the URL-bar auto-updates with the shareable link. For example:  `https://www.daostewards.xyz/#search=public`
will display all stewards in the Public Goods Funding-workstream.

We are continuously working on improving the cards are looking forward to receive feedback!

Signed,
@Fred, @seedphrase and the rest of the [MMM-Workstream](https://gov.gitcoin.co/t/proposal-merch-memes-marketing-workstream-budget-request/8562) ✨

-------------------------

tjayrush | 2021-10-01 03:12:56 UTC | #2

Very cool. Nice job. You'all should allow users to sort by engagement percentage as, at least to me, this would be the most important consideration as to whom I would delegate. Also, overall weight of vote (which you already sort by) and also number of forum posts, as this is also an indication of involvement.

-------------------------

ntnsndr | 2021-10-01 04:08:49 UTC | #3

This is fantastic—as a steward who has had trouble getting engaged, I can attest that this helps nudge me toward changing that—or, perhaps, stepping back from the role.

In a next phase, I think it is important to get more data on *how* people have participated. Some potential data points:

- Create a poll with some basic principle-based questions that users can fill out, as well as stewards, and the app can match users with stewards that match their general philosophy
- Evaluate how often the steward votes with the majority in Snapshot votes
- Track not only the number of forum posts, but the steward's reputation on the forum based on likes and replies

-------------------------

ntnsndr | 2021-10-01 04:12:28 UTC | #4

One other thing: I have initially found it hard to know when votes are coming up. I've just changed my notification settings in the forum on proposal posts. But is there another way that we should be getting notified about when and how to participate?

-------------------------

seedphrase | 2021-10-01 12:03:46 UTC | #5

Hi! Thanks! Totally agree, a way of sorting the cards based on any of the metrics is high on our todo-list of improvements and we're looking into adding additional metrics to give a better overview of the engagement of each Steward

-------------------------

seedphrase | 2021-10-01 12:10:46 UTC | #6

These are great suggestions. I really like the idea of the principle-based questions.

*"One other thing: I have initially found it hard to know when votes are coming up. I’ve just changed my notification settings in the forum on proposal posts. But is there another way that we should be getting notified about when and how to participate?"*

This is something I struggle with myself, so I'm going to do some digging on how we can be better informed.

-------------------------

Sirlupinwatson | 2021-10-01 15:46:31 UTC | #7

Looking great! Amazing work @Fred :grinning:

-------------------------

krrisis | 2021-10-01 16:04:13 UTC | #8

Yes! We will be sending out a DAO Newsletter very soon, which will gather all the open discussions & proposals, so you can easily review all of them at once and vote, comment etc.

-------------------------

krrisis | 2021-10-01 16:07:10 UTC | #9

Awesome, very big fan of the proposal that was made in the stewards chat, to use the bot data to also cover the activity in the discord.

Next to this I'm just very surprised that even the 'top stewards' don't have more than 1% of GTC delegated to them. Hurray for decentralization but in order to have some impact we need more people to delegate. We'll have to work on a multitude of programs to incentivize people to delegate their votes asap. But these cards are a great start to keep us wide awake! thx for this, so happy this is out

-------------------------

Fred | 2021-10-02 13:43:01 UTC | #10

Absolutely, we are looking into adding more public metrics to give an even better representation of the involvement and engagement of each Steward in the DAO! Examples are attendance to calls, and potentially Discord and Telegram-activity, if we are comfortable we can do this in a fair way.

In terms of the Voting weight-metric we use the same terminology as [Tally](https://www.withtally.com/governance/gitcoin) to eliminate confusion. Voting weight is calculated as the percentage of tokens delegated in relation to the *total amount of tokens*, as opposed to the amount of tokens in governance.

With 15.59% of tokens currently being delegated towards governance we get:
1% Voting weight equals ~6% influence in GitcoinDAO governance.

-------------------------

linda | 2021-10-03 03:08:37 UTC | #11

Love this initiative, thank you for starting it!

-------------------------

iyunkz86 | 2021-10-03 10:12:41 UTC | #12

Nice info brother,.......,.........................very cool

-------------------------

Pop | 2021-10-04 16:13:50 UTC | #13

Agree here! I am also wondering whether in time, we could also link to social (read Twitter) discussions re Gitcoin DAO/gov...

-------------------------

kelsien | 2021-10-19 12:03:57 UTC | #14

Hello GitcoinDAO!

 I’m concerned about how these metrics on volume of activity and attention map to quality of governance? It seems like more activity (noise), rather than greater effectiveness (signal). 

Also, tracking all activities risks creating a surveillance state on what is a voluntary, participatory organisation. This paper on surveillance in DAOs may be of relevance: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3907693#

My hope is that this offers a constructive perspective

-------------------------

tjayrush | 2021-11-01 13:53:48 UTC | #15

Thanks for sharing this. I'm also concerned with these issues both. Especially the surveillance issue. It's kind of unbelievable how deeply one can see not only into the activity of the DAO itself but the historical activity of each individual participant as well.

-------------------------

owocki | 2021-12-08 16:14:10 UTC | #16

hi all,  i just rebalanced some of my delegations from people who were inactive to those who were active and i found https://www.daostewards.xyz/ to be a really useful tool in doing so.  

it's really important that the people who have delegated governance are active & engaged.  thanks for helping to make that possible!

-------------------------

wkarshat | 2022-01-06 19:01:01 UTC | #17

Great tool, solid and bold initiative, thanks!

Any further explanation or modeling of the coefficients in the Health metric, please? Follow-up plans for the UI or supports for deriving insights, perhaps a time component?

All the folks commenting on usability and finding the presentation of information useful [or not].  Could you take the time to unpack your thinking, to help with further improvements and tuning of this system, please.

It can become very significant and impactful, once the DAO effort gets to the phase when the votes become more controversial or contentions.

-------------------------

seedphrase | 2022-02-07 15:45:18 UTC | #18

Hey! Thanks for the feedback!

We've tested out a bunch of different ways of calculating the health-metric of the Stewards. After some iterations we ended up with the formula presented in the OP. This formula takes into account all of the currently tracked metrics and the results it produces are aligned with how we understand Steward participation so far. 

We are finalizing the specifications for v2.0 which we aim to ship this quarter with added features and metrics developed alongside the new [Steward Council initiative](https://gov.gitcoin.co/t/introducing-the-steward-council/9485). An important aspect of the new version is to make sure the site does not turn into a dystopian surveillance tool like @kelsien touched upon above by only showing relevant metrics i.e. score per season/quarter or similar. We also don’t want to penalize a Steward or hinder their health score forever due to periods of low engagement whether it be other obligations, health reasons or similar.  We're looking into how Stewards can potentially own their cards and personalize them with social media links and other customization options.

-------------------------

owocki | 2022-02-10 17:18:50 UTC | #19

posting this for transparency reasons, i just delegated away from more ppl who were inactive in governance this cycle (away from shreyas, avsa) using the steward report cards (and the comments on the gov forum) as a source of truth for who is active/whos not.  no judgement towards ppl who are inactive (i know ppl get busy), i just think its important that my delegations go to ppl who are most active.

-------------------------

owocki | 2022-07-06 18:15:44 UTC | #20

again posting for transparency reasons.    similar to my https://gov.gitcoin.co/t/s14-voter-guide-template/10488 i hope that this post inspires others to share who they delegated to and why.

here are my current delegations along with comments per delegatee.

![Screen Shot 2022-07-06 at 12.15.12 PM|690x493](upload://2srT1SgEIlrRrvL6eHr51X1myPk.jpeg)

next season, i would like to delegate away from this current group + more broadly to people who:
1. have deep context.
2. good judgement.
3. are damage dealers.
4. help [bring the fire around the fire]([rive](https://gov.gitcoin.co/t/where-is-the-fire-around-this-fire/10664))
4. have good pulse on Grants 2.0.
5. want to help push governance/resource allocation at GitcoinDAO forward to be more effective.
4. will stick around to see through the DAO survive the bear market + into the next market cycle.

please DM me on discord (Owocki#1337) if you want to nominate someone for delegation next season!  to consider delegating to them i'd want to know
1. what their ETH address is
2. why you think they should be given more governance power

-------------------------

seanmac | 2022-05-22 19:31:54 UTC | #21

Thank you for sharing this... it's really helpful to know who you're delegating to and why. IMO this transparency is a key part of making the whole system function.

-------------------------

owocki | 2022-05-23 00:03:03 UTC | #22

[quote="seanmac, post:21, topic:8712"]
IMO this transparency is a key part of making the whole system function.
[/quote]

I think so too.  I'd encourage other large holders of tokens to publish similar reports too.

Maybe in leiu of that, someone would be able to issue a report on who is delegating to who using on-chain metrics?

I'd like to treating this initial delegation as an invitation for conversation.  If you think I'm delegating to someone too much or too little, or would like to nominate someone pls DM me (Owocki#1337) on discord.

-------------------------

tjayrush | 2022-05-25 17:49:17 UTC | #23

I always thought APIs were supposed to be designed to be painful to use, so I think you did a really good job there. :-)

-------------------------

owocki | 2022-05-25 18:21:04 UTC | #24

i wish this section of thte tally delegate report card worked better, it'd be nice to see the ENS names of the ppl who delegated, and be able to sort by the largest delegations (not just the latest)

![Screen Shot 2022-05-25 at 12.20.06 PM|690x271](upload://mufj3C3tlZSvCKDub2h99mfi1Ht.png)


https://www.tally.xyz/voter/profile/L4PZWY

im happy to be transparent, but a systemic level of transparency would be better design IMHO

-------------------------
