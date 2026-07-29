---
id: 16201
title: "Org-Wide Roundup, August 8 2023"
slug: org-wide-roundup-august-8-2023
category: newscommunity
url: https://gov.gitcoin.co/t/org-wide-roundup-august-8-2023/16201
created_at: 2023-08-08T19:21:57.444Z
last_posted_at: 2023-08-09T16:25:04.574Z
posts_count: 8
views: 2358
like_count: 37
---

# Org-Wide Roundup, August 8 2023

<https://gov.gitcoin.co/t/org-wide-roundup-august-8-2023/16201>
quaylawn | 2023-08-08 19:37:29 UTC | #1

## Org-Wide Roundup ([Check out the full overview here](https://docs.google.com/presentation/d/1WJseBI_raaBPhZFxTD-ProPvb9e9Ay-6vzWSERKmgmY/edit#slide=id.g22c82fc12dd_3_0))

Hey Gitcoin gang, as you’ll know we are experimenting with a new format in lieu of our weekly catch-up today.

### 🗣Weekly Gitcoin Updates 🗣

### Kudos 🙌

* Shout out to @Sor03 from @rena  – “All the spreadsheet love to Sorana for helping get the DAO budget ready for me to present to the Foundation on Friday.”
* Shout out to @MathildaDV  from @Viriya  – “Appreciate Mathilda for her leadership and partnership on all things Grants.”

### Ecosystem Headlines 📰

**A Million Journeys, One Destination:** Celebrating major milestones in Passport user growth and GTC staking.

**Uniting Continents and Elevating Impact Together:** Funding, building, and protecting what matters with GG18 – refresh your stamps before August 15!

**Putting Users First and Seeding the Ecosystem:** In a strategy to amaze, Allo & Grants Stack coalesce in cultivating 3 highly specialized grants management apps during S19.

**Learning and Perseverance Continues:** Grants Stack serviced 15 QF rounds to date, Direct Grants fit for launch, GG18 multi-round checkout confirmed, and smiling at the future of self-serve.

### Community Call 💚

Join @jon-spark-eco & @carlosjmelgar on Twitter spaces w/ @austingriffith, @ricmoo, @RevokeCash, @Sablier, @futurealisha, @realMaskNetwork to discuss Gitcoin Grants’ Builder impact.


*Set your reminder [here](https://twitter.com/i/spaces/1RDxlalWAOOKL)

## Further Updates ✍️

### PGN 🟢

* We have an updated Bridge Dune Dashboard – details are [here](https://dune.com/cerv1/pgn-bridge)
  * 1700 accounts
  * 41Eth
  * Focused on GG18, Bridge offramp, and governance conversations
  * Support items coming up related to PGN off-boarding (i.e. request funds to be moved to L1, state roots get published, 30 minutes later the proof can be “proved” and then 7 days after that, the funds can be requested to be moved back to L1).

### Foundation Updates 💼

**DAO Economics and Operations:**
  * Focused on building a DAO wide P&L to ensure we are tracking to the projections we built ahead of the DAO reduction in spending.
  * Continuing to revise how to coordinate in the DAO (changing cadence of weekly team sync, CSDO meeting cadence, etc.)

**Token Utility:**
  * August is the last month we will be engaging Mechanism Institute
  * The financial model for Passport is nearing completion and the templates will be shared soon (so others may use them to evaluate opportunities).
  * Kicking off financial modeling work for Allo and curation mechanisms to better understand quantities of GTC that may be put to use.

**Misc Updates:**
  * Legacy site of cGrants has been shut down 🎉 Read about its final voyage
  * CSDO is planning a virtual “offsite” for September to step through strategic planning (post S19)
  * Governance considerations

## Q&A - Let’s talk!

* Add your comments and questions below
* What do you want to hear about in our next weekly call?

-------------------------

owocki | 2023-08-08 19:59:48 UTC | #2

I'd love to learn why "see estimated matching at checkout time " was deprioritized on the Grants Stack team and if a community vendor (like supermodular) could build it instead.

IIRC [in Gitcoin Grants round 3](https://twitter.com/owocki/status/1252807337238126593), we saw a 50% - 70% conversion rate increase on crowdfund contributions simply by showing the user that their $1 could have $10, $100, or even $1000 worth of impact (as we know, the number depends on the number of contributors) without them having to do the math.

This is how the UI has looked in the past:

![slider|690x355, 50%](upload://yWikoR98YmjUHCp50w3WaZ9fnx0.gif)

Of course, just because the old centralized platform saw this conversion rate increase from having the matching estimates in the UI, doesnt guarantee that Grants Stack will.  But it seems like a worthy thing to try from my perspective as an outsider.

My 002 wei.

-------------------------

quaylawn | 2023-08-09 11:39:52 UTC | #3

Thanks for flagging this! @meglister looping you in here :slight_smile: 

**Edit: I checked out Discord for a rationale behind the deprioritization and it looks like there are significant integrations happening -- it would be best if we could keep a lid on some of this for PR purposes ;)

-------------------------

meglister | 2023-08-09 12:39:48 UTC | #4

Hey @owocki thanks for the question. We had originally prioritized matching estimates for GG18 as we responded to top pieces of user feedback from the beta round. It was the 3rd-ranked piece of user feedback so third in the sequence of what we built for the round (1: gas fees --> PGN support, 2: checkout fragmentation --> multiround checkout.) Unfortunately, our work on PGN support and multiround checkout has run over the estimated time to complete, so we don't have the capacity to also build matching estimates before GG18 donations kick off next week. 

*NB: Why did our estimates run over? 1: We've significantly changed team capacity over the last 6 weeks through parental leave/RIF/performance-related layoff, 2: multi-round checkout and PGN both required substantial coordination with other teams 3: multi-round checkout is a massive project that we likely underscoped -- retro forthcoming :slight_smile:* 

We've dropped it from the roadmap entirely instead of delivering after GG18 because we want to focus on delivering features that help us hit our self-serve QF + direct grants goals. We've already knocked Gitcoin Grants Round QF goals out of the park! ([Link to budget post for updates on those goals](https://gov.gitcoin.co/t/s19-proposal-amended-grants-stack/16188).) Matching estimates are not applicable to direct grants, and feedback so far around self-serve adoption indicates our feature efforts would be better focused on the Grants Manager experience vs the donor experience.

Re: could supermodular or another 3rd party build this. We've tried two projects with external teams building on the Grants Stack front end (Supermodular- collections, Bootnode- direct grants) and didn't find that either of them were effective. The Supermodular project was a great 0 -> almost 1 but wasn't able to incorporate styling and UX improvements and never shipped. The Bootnode project required really heavy coordination with our internal teams and the amount of adaptations and merge conflicts from that project were very substantial.

Hope this helps, always happy to discuss further!

-------------------------

meglister | 2023-08-09 13:38:26 UTC | #5

Also, FWIW... I expect multi-round checkout to have a MUCH higher impact on checkout conversion rates than matching estimates would! We saw checkout conversion rates of 4% in the beta round and 20% in the citizens round where only one round was running -- thus checkout fragmentation not an issue. We are aiming for 10% in GG18 (20% likely unsustainable with a larger, more diffuse audience) which would be a 125% increase over beta round. :)

-------------------------

owocki | 2023-08-09 15:24:43 UTC | #6

Thanks for the context. 

I agree multi-round checkout will probably increase conversion rates.  I hypothesize that multi-round checkout AND match estimates (if/when they are built) will have the highest conversion rate.  But we will let the data decide.  Whats the old trope? "If we have data, let's look at data. If all we have are opinions, let's go with mine." :P

Good to know about the experience with the collections PR, I was not aware that was where it fell over.  I know there are some active convos between us about how to evolve collaborations between GS <> outside contributors like Supermodular.  

The latest thinking is
1. building some easy/lightweight tooling to auto-generate web interfaces for different Allo v2 strategies.  This would be an investment in making it easy to not only write new strategies but also to put them in front of users.
2.  what we're loosely calling *Grants Stack Frontier* (an experimental fork of Grants Stack by Raid Guild, which can build experimental features at its own leisure but could also be PR'd back to Grants Stack proper according to criteria we negotiate later, and only IFF the experimental feature is important enough to warrant the effort).  

For those who are curious, the first GS Frontier fork is going to be this: We are going to be building a UI that displays a Grants HyperCerts into Grants Stack (running an experiment to see if showing users which Hypercerts are attributed to a Grant changes the contribution behaviour, which could be important in RPGF rounds where the explicit objective is to reward impact retroactively).

![Screenshot_2023-08-08_at_9.18.43_AM|690x403](upload://8rEYZa1rpdZxuNFgRjTg5xjTa3U.jpeg)

-------------------------

meglister | 2023-08-09 15:35:54 UTC | #7

[quote="owocki, post:6, topic:16201"]
I agree multi-round checkout will probably increase conversion rates. I hypothesize that multi-round checkout AND match estimates (if/when they are built) will have the highest conversion rate
[/quote]

Data, opinions, etc considered, you're probably right! And, I think my larger point is that increasing conversion rates will have a smaller impact on Grants Stack adoption than other efforts geared towards Grants Managers that solve their pain points and increase self-serve adoption. Would love to chat if you disagree -- I generally find that stakeholder convos that center on goals vs features provide much more value to the product team!


[quote="owocki, post:6, topic:16201"]
1. what we’re loosely calling *Grants Stack Frontier* (an experimental fork of Grants Stack by Raid Guild, which can build experimental features at its own leisure but could also be PR’d back to Grants Stack proper according to criteria we negotiate later, and only IFF the experimental feature is important enough to warrant the effort).
[/quote]

Would be remiss not to note that I'm excited about this and building more collaboration with the GS team :)

-------------------------

owocki | 2023-08-09 16:25:04 UTC | #8

[quote="meglister, post:7, topic:16201"]
And, I think my larger point is that increasing conversion rates will have a smaller impact on Grants Stack adoption than other efforts geared towards Grants Managers that solve their pain points and increase self-serve adoption.
[/quote]

My trail of thinking is that increased end-contributor conversion rates => more community funding => solves customer pain point (wanting to fund what matters in your DAO/ecosystem).

I'll name that having to make these types of priority tradeoffs is foreign to me.  With the 0 to 1 builds that I work on with Carl, Raid Guild, or I do myself, it takes a couple days to do a steel thread of a feature like this.  With QuadraticLenster, Raid Guild put the match estimates into the UI + it took roughly a day to do from conception to implementation.  Our work isn't perfect, but it gets us to *data* about what affects the customer UX very fast.  There are probably trade-offs to taking the approach I just articulated that I'm not fully articulating also (maybe our code is less maintainable over time, documentation is lacking, 80/20 work isnt possible/desirable/responsible in some cases, etc), so please don't interpret this is "you should do it our way".  I'm just naming that when you're doing dev work in a more 0 to 1 way, you just dont have to make these kinds of priority trade offs because you've got an abundance of resources (time/dev cycles/design spaces) fitting multi day projects into a quarter, instead of a scarcity of resources because you're trying to fit multi week projects into a quarter.

I've not seen the prioritized list of customer pain points nor the thinking about self-serve adoption (though I have dogfooded the product and [my dogfooding accounts](https://gov.gitcoin.co/t/s19-proposal-amended-grants-stack/16188#h-8-self-serve-qf-rounds-5) for half of the self serve adoption so far), you are closer to the data/customer/GS team these days, and my advocating for this feature has always been consider feedback, so while I'm disappointed to see the feature deprioritized because it feels like an easy/obvious win to me, I trust your judgement to prioritize Grants Stack work as you see fit.

-------------------------
