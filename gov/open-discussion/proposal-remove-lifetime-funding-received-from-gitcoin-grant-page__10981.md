---
id: 10981
title: "[Proposal] Remove Lifetime funding received from gitcoin grant page"
slug: proposal-remove-lifetime-funding-received-from-gitcoin-grant-page
category: open-discussion
url: https://gov.gitcoin.co/t/proposal-remove-lifetime-funding-received-from-gitcoin-grant-page/10981
created_at: 2022-06-21T18:31:33.626Z
last_posted_at: 2022-08-14T04:02:18.976Z
posts_count: 25
views: 4971
like_count: 49
---

# [Proposal] Remove Lifetime funding received from gitcoin grant page

<https://gov.gitcoin.co/t/proposal-remove-lifetime-funding-received-from-gitcoin-grant-page/10981>
lefterisjp | 2022-07-28 16:00:38 UTC | #1

Hey all,

I would like to make a proposal for the gitcoin 1.0 page. Each grant has the " Lifetime funding received" which is a $ amount. I would like to propose to remove it from all grant pages. I would even go so far and ask to remove it with urgency.

My reasons follow below:

1. It's wrong and by a big margin. The calculation is simply off and I have pointed that out multiple times in the past but it was never fixed. There were improvements, then there were bugs again, regressions etc. We used to use the gitcoin API (where this number comes from) in the past in rotki. But since we are an accounting tool and financial accuracy is important for us and our users we had to stop using it and implement our own solution. With gitcoin 1.0 deprecated I understand it will never be fixed but having a wrong number there is harmful.
2. It gives the wrong idea since its supposed to be amount at the time received. Many grants were funded through multiple tokens, not only stables. Tokens which have lost their value by 50-90% since the time of funding and as such the amount is off.
3. Some grants are live since 2019, so the amount is going to be high~ish compared to other grants. The number does not take into account the duration the grant is active.

And you may ask why is it that bad? Let me tell you how it has harmed grants (including the one I am running -- rotki).

1. **It creates a tax liability**. This is the most important problem and why I am writing this here today though I wanted to let it slide. We at rotki are paying taxes as a Germany entity for all our revenue. And donations are also revenue so we owe taxes on them. We also are an accounting application and have our own way of calculating the per year income through grants which is accurate and tested thoroughly since it uses the actual on-chain data. Yet the real amount and the amount shown in the gitcoin page differ by so much that our accountant warned us we may get audited since the amount shown in the official gitcoin page should be correct and is what the tax authorities would look at.

2. Some grants were excluded from some ecosystem rounds due to having a high (>$50k) lifetime funding. While each ecosystem is free to manage their own round as they see fit, I believe that the number creates wrong expectations for all the 3 reasons I mentioned above ... most important of all that it's wrong by a very big margin.


----

I am not sure if this should be a DAO issue or a github issue for https://github.com/gitcoinco/web/ but I believe it should be here and discussed by the community as grants 1.0 is still the number 1 product of gitcoin.

----

Just one of the many issues we had and what lead us removing our integration with the gitcoin API: https://github.com/rotki/rotki/issues/3434

-------------------------

connor | 2022-06-22 17:49:43 UTC | #2

Hey thanks for the proposal Lefteris. Couple of questions - on point 1. Is the data definitely wrong? Are you considering it includes matching amounts? Is it wrong due to price fluctuations (point # 2) or wrong regardless of that? Do you have any concrete evidence or data you can share to help pinpoint this? If it is totally off we should definitely look into it.

2. Price fluctuations - I think trying to peg "lifetime funding" to the current price of tokens today would take a ton of work and constant recalculations, and I'm not sure it makes sense if we could. $ amounts of donations for matching calcs are always using the price at the time of donation, which they should be. If your concern is taxes/accounting, the price tokens were received at is what matters most, right? That's the cost basis for tracking any gains or losses when the tokens are eventually sold. Plus how is Gitcoin supposed to know whether a project held or sold non-stable tokens they received? Trying to make this value variable would cause more confusion and incorrect data IMO.

3. For Rotki specifically, if you received a lot of Eth in 2019/2020, wouldn't pegging to today's price actually make your grant look like it received even more $ than it shows now? I agree we could maybe showcase front and center a "grant created date" or "number of rounds participated in", but I don't see how the lifetime funding stat could objectively take into account a grant's age and be adjusted accordingly.

For the second part:

1. Tax liability - could you share the data you have from on chain that differs from whats shown on Gitcoin? This would help a lot. But to what I said earlier, pegging lifetime funding to today's price would actually make tax liability much more confusing and wrong since you owe taxes on the value at the time the transaction was made (I guess could differ in different jurisdictions though)

2. As you know in the ENS round, ENS said any grant who earned over $50k lifetime is not eligible for their round's matching, and I know Rotki was removed as a result. I get why this is upsetting, but that's ENS's call to make at the end of the day, and I do see why they want to focus on smaller/newer projects for their limited matching pool. But yeah it's not ideal for older/bigger grants :/

Last point, I do feel in some ways showcasing a grant's high lifetime funding amount helps build trust and reputation for new donors

-------------------------

lefterisjp | 2022-06-22 19:53:10 UTC | #3

1. The data is definitely wrong yes. I have had multiple issues reported both in github and via discord(mostly talked with thelostone-mc) and at this point I can't devote any more time on this. I just know that a wrong amount should not appear there. For example it turned out that the amount calculated at some point was using rounded up amount of tokens since this is what you had in the DB.

2. I am not asking to change this. Having this calculated with price at time of donation is indeed correct. It's just an unfair thing to think of when looking at the grant via a bear market lens and creates the wrong expectations for the grant.
3. Look into (2)

I am not making this post for ENS and this is not the point of the discussion. They can do whatever they want with their funds so I don't want to discuss it in here even though I am personally quite vexed by this decision for many reasons which I may go in more details elsewhere in the future.

The point of this post is to remove a value from the grants page that is wrong and also creates false expectations and may put us in serious accounting troubles as a project.

I know we are probably one of the few projects that actually also pay taxes on all donations so this may not bother others as much. In any case I will edit the grant description to specify that the "Lifetime funding" is simply wrong even if gitcoin decides to not remove it to at least have something shown in our grants page.

-------------------------

yabirgb | 2022-06-23 09:33:35 UTC | #4

Hello! In the past I started building the Gitcoin integration for rotki and we found several errors in the API starting by one critical error that affected in a bad way the total amount calculation. For reference we created `https://github.com/gitcoinco/web/issues/9222` . Also as @lefterisjp commented we found that the amounts were incorrect due to rounding of the tokens.

The worst case in the logic we found was `https://github.com/gitcoinco/web/issues/9256` and we can't say for sure if there are more errors or not since we decided to stop using the API.

As for the price calculation having it recalculated, as it has been commented, is not correct for tax purposes but we believe is better to avoid showing it or show some kind of warning next to it detailing how it was calculated and that might be inaccurate

-------------------------

the_greatest | 2022-06-27 18:47:33 UTC | #5

I think this total funding number is sometimes a useful metric to have when evaluating a grant but not always necessary. Perhaps having the current grant round's total (ie; GR14 here) and then the total all time funding is not shown automatically but can be toggled to display in the funding tab, under where the current round total is displayed.  That way the info is there if a user wants it but not automatically displayed.  

Just my 2 sats

-------------------------

lefterisjp | 2022-06-27 19:05:38 UTC | #6

[quote="the_greatest, post:5, topic:10981"]
total all time funding is not shown automatically but can be toggled to display in the funding tab,
[/quote]

That would be more useful during a round imo, yes.

But the point is also when there is no round running at all. Having a number that is not 100% accurate, to the cent there is misleading and can lead to financial trouble in some jurisdictions if your tax authority decides to audit you and see a number there adding up differently than what you reported.

-------------------------

tjayrush | 2022-07-19 16:08:59 UTC | #7

My thoughts:

1) The data absolutely must be accurate. That's obvious. If it can't be made accurate for some reason, other alternatives should be sought.

2) The mistaken number does not "create a tax liability." The tax liability is whatever the actually received grant amount is, which is (by your own claim) not the same as the amount shown on the interface. This can be easily remedied by adding text saying something like, "This number is not intended for any purpose public or private" or whatever "legalese" one would use to make it clear (even to dim-witted tax authorities), that this is not a "tax liability."

3) This number, especially being that it's at the very top of the display, is SUPER useful. Please don't remove it. It's the first number I look at when deciding whether or not to donate to a grant. If a grant has received a "decent" amount of money, I want to know that. If I'm trying to decide between two grants and one has $10,000-lifetime funding and another has 100,000-lifetime funding, that weighs heavily on my decision.

An alternative might be a "bar chart" or some other sort of graphical object with no numbers that indicates, "amount received" -- tall bars for a lot of lifetime funding, shorter bars or not at all for a small amount of funding. The important information is relative magnitude, not exact numbers. But, please don't remove this super-valuable clue to the a project's "needyness."

-------------------------

nategosselin | 2022-07-21 16:58:44 UTC | #8

Thanks for the proposal, Lefteris. I’m on the Grants product team and want to share how we’re thinking about this. 

While this feature predates my time at Gitcoin, I do know that many of the legacy platform features were experiments that were rapidly put into production. My hunch is that this feature falls into that category and that it was never intended to be a perfect representation of lifetime funding (despite displaying results to the dollar). I empathize with the challenges you’ve outlined, but as the discussion here shows there are still community members who find this indicator valuable — given that, we’re not comfortable removing this feature.

Another option presented here was developing a new calculation approach, but we’re faced with the challenge of prioritization — figuring out a new method is complex work and the cGrants platform is in maintenance mode while we are heads-down building Grants 2.0 to replace it. In fact, a key factor in deciding to fully replace the legacy platform with fresh Grants 2.0 code was the realization that the legacy platform couldn’t scale because of the sheer number of unsustainable experiment features like this still hanging around the codebase. 

Having said that, there might be an interim middle ground where we can just display a rounded number so it doesn’t give the illusion of accounting accuracy. I’ll look into whether we can accommodate that option ahead of GR15. 

Beyond that, I’d love to chat with you and the Rotki team about being an integration partner for Grants 2.0 if you’re interested. Our vision is for this funding data to live publicly and it would be great to get your team’s input on how to make that information valuable.

-------------------------

lefterisjp | 2022-07-22 22:51:27 UTC | #9

Hey @nategosselin , @tjayrush 

> The data absolutely must be accurate. That’s obvious. If it can’t be made accurate for some reason, other alternatives should be sought.

Agreed. The data is inaccurate by order of magnitude as both my team and I have showcased. There is multiple bugs that cause  this which we have reported. Most serious of which is the rounding up of each amount in the DB and most recently the matching amounts being calculated on difference price, than the price of the day of claiming.

> The mistaken number does not “create a tax liability.”

Are you a tax advisor licensed to operate in Germany?
I have had talks with my advisors and this number create a very serious problem for us. I have already had to spend close to 1k EUR in consulting fees to discuss this and try to figure out an interim solution. They see gitcoin as the platform and if its UI says a number this is the number they will take. Sure I can start arguing and show them this thread, but then the problems have already started and my bill are ramping up. Will you or gitcoin take this bill?

>  I empathize with the challenges you’ve outlined, but as the discussion here shows there are still community members who find this indicator valuable — given that, we’re not comfortable removing this feature.

@nategosselin 

This is unacceptable. I am showcasing with specific bugs that your product is broken. It has a mistaken number, **by orders of magnitude**,  that creates multiple problems. Problems with tax authorities, mistaken representation to the community that does not have the context in how long a period this funding has been earned in or what the budget that the project has for each quarter is. It's absolutely wrong and misleading.

> Another option presented here was developing a new calculation approach, but we’re faced with the challenge of prioritization — figuring out a new method is complex work and the cGrants platform is in maintenance mode while we are heads-down building Grants 2.0 to replace it. In fact, a key factor in deciding to fully replace the legacy platform with fresh Grants 2.0 code was the realization that the legacy platform couldn’t scale because of the sheer number of unsustainable experiment features like this still hanging around the codebase.

We just voted to give you guys $1,5m for 3 months. You can find some resources to fix a bug. (https://twitter.com/LefterisJP/status/1550051591801241601)

I am a developer. I find it **unacceptable** to have in my product something that is completely off. Either fix it, or remove it. There is no excuse to keep this.

> Having said that, there might be an interim middle ground where we can just display a rounded number so it doesn’t give the illusion of accounting accuracy. I’ll look into whether we can accommodate that option ahead of GR15.

Yes there is.

If the only reason you want to keep it is what @tjayrush said above, I sympathize. Let's then make it simple.

> An alternative might be a “bar chart” or some other sort of graphical object with no numbers that indicates, “amount received” – tall bars for a lot of lifetime funding, shorter bars or not at all for a small amount of funding. The important information is relative magnitude, not exact numbers. But, please don’t remove this super-valuable clue to the a project’s “needyness.”

I completely disagree on "neediness". There is no such thing. There is budgets per quarter. **Lifetime funding, without having a budget per quarter or how many months a lifetime constitutes for is completely misleading**

But we can have something that satisfies both approaches. How about this?

1. You say the old system is too broken to fix
2. You say you don't have the resources to fix it
3. You say an idea of how well funded (from a grants perspective) a project is, is a very useful metric and as such want to keep the number as it's "close enough".

So let's do the following.

1. Take the current broken lifetime amount and divide it by months the grant is active to get an average estimated funding per month.
2. Calculate this value for all grants.
3. Show this on the grant in a bar chart, or with tags like: "Highest percentile of avg. grant funding", "High percentile of average grant funding" , "Medium ..." etc.

Such an approach would:

1. Solve all the problems I have with the current approach.
2. Respect your resources. This is an assumption, but since you would not need to fix the bugs, just change the display method and average the calculation out, this should be easy to do.
3. Satisfy @tjayrush's concerns on showing which are the most well funded grants and which ones aren't so.

> Beyond that, I’d love to chat with you and the Rotki team about being an integration partner for Grants 2.0 if you’re interested. Our vision is for this funding data to live publicly and it would be great to get your team’s input on how to make that information valuable.

I don't know what that is but feels off-topic to the thread. Happy to take it via DMs in discord, twitter or email.

-------------------------

bobjiang | 2022-07-26 05:27:25 UTC | #10

[quote="lefterisjp, post:9, topic:10981"]
So let’s do the following.

1. Take the current broken lifetime amount and divide it by months the grant is active to get an average estimated funding per month.
2. Calculate this value for all grants.
3. Show this on the grant in a bar chart, or with tags like: “Highest percentile of avg. grant funding”, “High percentile of average grant funding” , “Medium …” etc.

Such an approach would:

1. Solve all the problems I have with the current approach.
2. Respect your resources. This is an assumption, but since you would not need to fix the bugs, just change the display method and average the calculation out, this should be easy to do.
3. Satisfy @tjayrush’s concerns on showing which are the most well funded grants and which ones aren’t so.
[/quote]

I can imagine if the issues are related with tax (in Germany) it should be very serious issue.
So I support @lefterisjp to insist to fix this issue.

Thanks a lot for your solution as well!

Only one question here, besides above solution you suggest, do we have other solutions?

-------------------------

connor | 2022-07-26 06:18:55 UTC | #11

[quote="lefterisjp, post:9, topic:10981"]
The data is inaccurate by order of magnitude as both my team and I have showcased
[/quote]

[quote="lefterisjp, post:9, topic:10981"]
It has a mistaken number, **by orders of magnitude**,
[/quote]

Can you share any examples or data of this number being off by orders of magnitude? Yes, I agree the number is not 100% accurate - but I believe it is ballpark correct. There may be some variance due to rounding, and/or conversion rate at the time of funding claim contract vs. rate at the time a user claims their match. But price volatility and when a user decides to claim is out of our control. Regardless, of the 10's of millions in matching funds that have been paid out, 95%+ have been in DAI, with only a fraction in other ERC-20's that may have this issue with conversion rates. I'd guess the number is accurate within a few percentage points, but if you can show grants that are orders of magnitude off, I'd be much more open to reworking or removing the stat.

Perhaps a band-aid fix here to address the tax concern would be adding "Approximately" before the number and rounding it? Surely any auditor would look at on-chain transaction data to calculate exact amounts and the price at the time of the transaction to figure out exact cost basis.

In any case, I really do believe this is a valuable metric to show for grantees and donors. Rather than a big number discouraging donations, I think it actually helps establish trust and reputation for a project.

-------------------------

lefterisjp | 2022-07-26 07:09:51 UTC | #12

[quote="connor, post:11, topic:10981"]
Can you share any examples or data of this number being off by orders of magnitude? Yes, I agree the number is not 100% accurate - but I believe it is ballpark correct.
[/quote]

Yes. At the time when rotki's total funding was at around $280k in gitcoin I got really suspicious as it looked off compared to what we actually had and since it was time to make the 2021 taxes I ran both rotki's accounting script but also custom scripts for zksync (with the help of their team) to get an amount. Back then polygon was not used.

The number we came up with agreed (almost) to the point with what we ended up having and was  about $190k. So almost off by $100k. That's not a ballpark.

As for the specific reasons this must be happening it's not hard to imagine. The gitcoin 1.0 product  is in a state of decay as it's abandoned for the newer 2.0. Please check what I wrote above and the issues I mentioned. We have opened multiple issues against the product and some of them are in a "Won't fix" state. For example: https://github.com/gitcoinco/web/issues/9213 each DB entry being up to 2 decimals so everything being rounded up.

Over thousands of mini contributions this goes off by a lot. Then I suppose differences between the price oracles you use and reality or most likely the timestamp you use for prices. Especially for prices of claiming grant matching non-stable tokens.

We have hit bugs at every corner when using gitcoin 1.0. And you yourselves said that it's an abandoned product. 

I proposed a solution here: https://gov.gitcoin.co/t/proposal-remove-lifetime-funding-received-from-gitcoin-grant-page/10981/9?u=lefterisjp

[quote="lefterisjp, post:9, topic:10981"]
So let’s do the following.

1. Take the current broken lifetime amount and divide it by months the grant is active to get an average estimated funding per month.
2. Calculate this value for all grants.
3. Show this on the grant in a bar chart, or with tags like: “Highest percentile of avg. grant funding”, “High percentile of average grant funding” , “Medium …” etc.

Such an approach would:

1. Solve all the problems I have with the current approach.
2. Respect your resources. This is an assumption, but since you would not need to fix the bugs, just change the display method and average the calculation out, this should be easy to do.
3. Satisfy @tjayrush’s concerns on showing which are the most well funded grants and which ones aren’t so.
[/quote]

Please let's just get this done.

-------------------------

yabirgb | 2022-07-26 16:51:19 UTC | #13

Just wanted to share that we found bugs like this one `https://github.com/gitcoinco/web/issues/9280` that makes me question whether the information can be partially or totally trusted and #9213 is also a concern. 

As @lefterisjp proposed some kind of aggregated data could be more insightful although if the data is wrong or partially wrong it could lead to useless conclusion. Definitely it would soft any possible errors caused by old bugs.

-------------------------

nategosselin | 2022-07-26 18:00:06 UTC | #14

Thank you for the suggestion @lefterisjp. We've decided to update the grant page to say "Estimated lifetime funding received", to display the amount rounded to the nearest thousand, and to include a "this number should not be used for accounting purposes" statement. Given the need to focus on Grants 2.0, this solution enables us to remove the illusion of accounting accuracy, keep a directional indicator for the users who desire it, and save us from implementing new calculations or tags per your proposal. We'll have this solution in place before GR15 kicks off.

We are planning to assist grants in migrating to Grants Hub once ready and will ensure that any data that is migrated is accurate and useful.

-------------------------

kevin.olsen | 2022-07-26 18:13:00 UTC | #15

Thanks @nategosselin, this is exactly the solution I was coming to as well.

@lefterisjp I think this should address the potential liability you identified for your situation in Germany. If there is any specific language your tax advisors would need to see to be fully confident this would not initiate an audit, please let us know what you'd need.

-------------------------

lefterisjp | 2022-07-26 18:37:04 UTC | #16

Hey @nategosselin and @kevin.olsen thank you for the response.

I think the "Estimated lifetime funding received" and a visible warning nearby that says: "this number should not be used for accounting purposes" would really help. Appreciate this.

For the number rounding I prefer the solution I proposed.

1. It should not be hard to implement
2. And should convey to everyone that grants like rotki's are among the top-funded by gitcoin grants without providing a number that is not accurate.

The idea to round to nearest thousand may be okay for grants that are in the tens of thousands raised, but for us since the error itself was in the tens of thousands,  this won't make any difference.

I would really prefer it if you could implement https://gov.gitcoin.co/t/proposal-remove-lifetime-funding-received-from-gitcoin-grant-page/10981/9?u=lefterisjp or at least explain why this is not possible. As this solution (which is actually what @tjayrush proposed) should check all boxes.

But still, if not that ... maybe then could you do what you suggest with the following addition: If the grant raised more than $100k according to your data, then start rounding at the nearest 25k? Rounding down (since the data you have seems to push the number up).

Also let's find a way to take into account:

1. Spending of a grant per quarter
2. Months/quarters/years the grant/project is active.

Without (1) and (2) any amount is not really put in perspective. A grant with 5 devs has more expenses than a grant with 1 dev which has more expenses that a guy writing some blogposts. Also there is a huge difference if the expenses have been only in the last month versus the last 3 years!!!!

I am not saying to do the above in grants 1.0. But let's get it right in 2.0.

-------------------------

nategosselin | 2022-07-26 18:43:36 UTC | #17

Thanks @lefterisjp

> I would really prefer it if you could implement [[Proposal] Remove Lifetime funding received from gitcoin grant page - #9 by lefterisjp](https://gov.gitcoin.co/t/proposal-remove-lifetime-funding-received-from-gitcoin-grant-page/10981/9) or at least explain why this is not possible.

I agree that this is not difficult, but it does require more time. The suggestion I laid out is a simple front-end code change: revised copy + rounding the number provided by the backend. The suggestion you laid out requires calculating a new number for all grants, storing that data, building a process to continually calculate / maintain that number, and coming up with a visual design or new tags to display it. Given the urgency to ship 2.0 I just don't think this is a prudent use of our resources.

> Also let’s find a way to take into account:
> 
> 1. Spending of a grant per quarter
> 2. Months/quarters/years the grant/project is active.
...
> I am not saying to do the above in grants 1.0. But let’s get it right in 2.0.

I definitely agree that grants 2.0 is an opportunity to rethink our approach to data and visualization. I'm looking forward to hearing more of your thoughts as we get closer to that stage of development.

-------------------------

lefterisjp | 2022-07-26 19:00:57 UTC | #18

[quote="nategosselin, post:17, topic:10981"]
The suggestion you laid out requires calculating a new number for all grants, storing that data, building a process to continually calculate / maintain that number, and coming up with a visual design or new tags to display it.
[/quote]

Yet this should also be easy for a well funded team like you. I am also a CTO of a very complicated project with thousands of users and I can do software estimates. You guys just got funded by us, the DAO, for the next 3 months to the amount of almost $1.5m. This is just for 3 months funding!!!!

[quote="lefterisjp, post:16, topic:10981"]
But still, if not that … maybe then could you do what you suggest with the following addition: If the grant raised more than $100k according to your data, then start rounding at the nearest 25k? Rounding down (since the data you have seems to push the number up).
[/quote]

you have not answered to that part of my question. Which would even be an easier change as it's just an algorithm adjustment.

-------------------------

tjayrush | 2022-07-26 19:07:10 UTC | #19

I'm going to come down on the side of Lefteris (in support of the idea I proposed). I don't think you have to store any data. Here's the purely front-end code:

```
If (the lifetime funding is big) {
    display A_Lot_Of_Funding.png

} else (if lifetime funding is medium sized) {
    display A_Medium_Amount_of_Funding.png

} else {
    display A_Small_Amount_of_Funding.png
}
```

I'm kind of joking, but I'm kind of not. It's not a lot of work.

-------------------------

yabirgb | 2022-07-26 19:14:11 UTC | #20

The problem with this approach is that as per what we have detected the calculation is off by a considerable amount (this can be reproduced) and rounding to the thousand in a number on the 100K+ will make no considerable change. For someone that wants to use this number as metric you could just leave the old number and would have the same effect.

Moreover I believe showing a metric that has been proven to be off with such a high error is also dangerous for other projects since, if you want to use it as metric to choose where to donate or not, could lead to decisions that are not aligned with the strategy choosen.

If the focus is in the v2 of the grants and no time can be alocated to properly handle a broken solution I believe is in the interest of the users to find an approach that is useful to as many users as possible, and showing erronous information clearly damages them.

Furthermore if v2 is realising soon it shouldn't be an issue to take a temporal solution like removing this number and properly handle it in v2.

I believe that for v2 the focus should be in detecting why this numbers are off by such big differences since from this thread I understand is something that has not been considered and looks like a critic metric in the system.

The changes proposed are not meaningful and the only considerable effort is to display a label saying that the amounts are incorrect... which feels like the worst solution for the ecosystem

-------------------------

tjayrush | 2022-07-26 19:22:26 UTC | #21

Assuming V2.0 comes relatively soon, and assuming that there's a strong commitment to retaining some method for end users to ascertain at least a relative amount of lifetime earnings, I suppose not wasting time fixing it is reasonable.

One comment on monthly average vs. overall. That hides useful information. Two projects, both with 1,000 monthly average, but one with one month's worth of lifetime earnings and another with 1,000,000 lifetime earnings are two completely different things.

In version 2.0, since we're going to this problem, perhaps both metrics can be retained.

-------------------------

nategosselin | 2022-07-26 19:38:22 UTC | #22

I appreciate all the feedback everyone. We're going to implement the solution I outlined above, and will keep this thread for reference when we begin working on this design space in Grants 2.0.

-------------------------

lthrift | 2022-07-26 19:42:33 UTC | #23

Thanks for your follow-up here, Nate! I'm glad we can address the most pressing concerns around tax liability with minimal effort and context switching.

I just wanted to echo what Nate's stated about our focus on Grants 2.0 and keeping the 1.0 platform in maintenance mode. We're making great progress on 2.0 and the more laser focus we can keep, the sooner we can move the entire program off of the 1.0 platform - every bit matters.

-------------------------

lefterisjp | 2022-07-27 23:24:10 UTC | #24

Since I spoke with Kevin Olsen a bit in private about this he asked me to clarify something that he at least did not understand from my posts above and he thought would make my argument stronger.

I believe I made it clear but perhaps that is not the case.

1. I agree with all of you that you should focus on grants 2.0 and only do maintenance stuff on cgrants.
2. **But** the current page of cgrants is the SOURCE of our problems and in our opinion should be fixed as part of maintaining cgrants. I mentioned that a number without any context does damage here: https://gov.gitcoin.co/t/proposal-remove-lifetime-funding-received-from-gitcoin-grant-page/10981/16?u=lefterisjp. I explained that you need the project's budget, the amount of months this funding is for etc. But I did not mention how this has damaged projects as I did not want to name specific cases. Kevin said it's okay and helps illustrate the problem so I will. Rotki and other grants (like otterscan from wmitsuda) got removed from the ENS ecosystem round exactly due to the funding amount being higher than a specific amount. 

> One comment on monthly average vs. overall. That hides useful information. Two projects, both with 1,000 monthly average, but one with one month’s worth of lifetime earnings and another with 1,000,000 lifetime earnings are two completely different things.

Absolutely.

----

But guys in general I feel like I am trying to get my point across over long forum posts and I see the members of the gitcoin team largely ignore what I am saying and saying you won't fix it and then nodding to each other for a job well done.

This makes me sad :frowning:

-------------------------

php | 2022-08-14 04:02:18 UTC | #25

if it is an accuracy issue, rounding to 3 categories - large, medium, small seems fine.

Shouldn't the tax authority use the actual wallet address? rather than a website number?
"Problems with tax authorities, mistaken representation to the community that?

-------------------------
