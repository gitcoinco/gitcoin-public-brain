---
id: 17257
title: "Lessons from GreenPill Network's Hypercerts Impact Funding Experiment"
slug: lessons-from-greenpill-networks-hypercerts-impact-funding-experiment
category: open-discussion
url: https://gov.gitcoin.co/t/lessons-from-greenpill-networks-hypercerts-impact-funding-experiment/17257
created_at: 2023-12-12T09:05:54.237Z
last_posted_at: 2024-01-19T03:38:27.374Z
posts_count: 12
views: 4183
like_count: 44
---

# Lessons from GreenPill Network's Hypercerts Impact Funding Experiment

<https://gov.gitcoin.co/t/lessons-from-greenpill-networks-hypercerts-impact-funding-experiment/17257>
sejalrekhan | 2023-12-12 09:11:00 UTC | #1

Co-authors

@sejalrekhan , @lanzdingz and @bitbeckers 

Recap and reflection on Hypercerts Based Impact Funding experiment - The initiative was taken by GreenPill Network in collaboration with RaidGuild team.

The Raid Guild (RG) team forked the GrantsStack and helped us build a GPN-specific Hypercerts integrated tool which enabled chapters to mint GPN hypercerts for work done by the chapters, which was then meant to showcase their hypercert on the forked explorer page for GPN’s community round.

Hypercerts were minted on minter.greenpill.network.

![|624x193](upload://vp7DVHYZallK6wLnMaIxY42jsJa.jpeg)

The experiment was to see if having Hypercerts would have a correlation to the level of funding a project received.

Here is some of what we learnt:

1. Hypercerts were minted for the work done over a 6 month period,

* The short amount of time gave us no real data that will measure the impact to the community.
* There was not enough quality control as any chapter could mint on their own without having to meet certain criteria. This resulted in a mixture of impactful hypercerts and some highly frivolous ones.

An interesting next step is setting up an evaluation flow. For example, a chapter steward could approve minted hypercerts and these attestations would go on chain.

2. With this being a [forked version](https://explorer.greenpill.network/#/round/10/0x4727e3265706c59dbc31e7c518960f4f843bb4da), we ran into some glitches that had us in a start-stop space for a few weeks. This meant there was a lot of manual time spent both on GPNs side and RG’s side. We also ran into some issues with hypercert visibility in the backend when using the forked manager.greenpill page as a Round Operator. We had to reject half the applicants and have them reapply because not all the data was showing properly. This is normal when experimenting with something, so it was to be expected. As an improvement, we could take a more guided approach in the minting process to make sure the applications are correct. This could be either hands-on or more rigid checks in the application.

3. Not all chapters grasped why minting hypercerts was important and what impact this could have, which was a challenge and most likely is what affected the quality control aspect of it. Having hypercerts in your application was also a requirement for our internal GPN community round. This also meant people were minting as a step vs a thoughtful proof of impact - which also potentially affected quality control. The design is that hypercerts loop impact creators in a larger value flow, but this is something very abstract and we can improve on this by providing more education.

4. We believe that the average donor might not have understood the importance of hypercerts and therefore might not have taken that into consideration when donating. This is an assumption, but it’s based on how the quality/proof of impact of the hypercert didn’t seem to play a big factor in if a project got funding or not.

5. Overlap with GG19. The GPN round ran on a forked version while GG19 was happening and this caused confusion as you needed to apply to the GPN round on the forked Grants Stack in order to have your hypercert appear and some chapters applied from the normal builder.gitcoin program page. This meant that while all Chapters/grantees had a hypercert, not all of them showed up in the explorer page. From a Round Manager perspective there was no way for us to know where they were applying from and have them reapply from the proper greenpill.builder page. In comparison, RG ran an experiment connecting the Grants Stack with Lens which was widely announced during EthCC. Such a major announcement pull people into your app, while the GPN experiment was more on a friends-and-family scale for the network. Putting more attention on the fork, or finding support from GitCoin to run a ‘beta’ version, could generate more traffic into these kind of experiments.

6. Our hypothesis was the chapters with more hypercerts would get more funding. Our sample size wasn’t good enough for real data collection as all chapters had to have a hypercert to be accepted into the round. It also doesn’t seem that the quality of the hypercert was taken into account during the donation process. This could also be due to the fact that this was an internal GreenPill Chapter round, and therefore many donors might (this is an assumption) have just been donating to their own community and 1 other, as we saw 403 contributions from 172 unique contributors, which means the average contributor donated to 2.3 projects.

6. We believe that hypercerts can and will have a positive impact on how people make donations within the GreenPill ecosystem, we just need more structure around the hypercerts eligibility/ minting criteria, and have more education around why they are important - both for projects and for community members making donations. We also need to work out the technical glitches to make a smoother process for everyone.

7. Technically, it was relatively straightforward to adapt the grants stack to support hypercerts. Since rounds, project and application, all store their metadata on IPFS and only the CID pointer is stored on chain, RG was able to modify the metadata being stored to contain an array or related hypercert IDs. When reading the metadata, any hypercerts found were displayed in the application.

While our experiment didn’t turn out exactly as we had planned, we do believe that hypercerts and other impact tracking tools will be helpful in assisting people make decisions around what projects to donate to. GPN is also interested in ways to track impact so that we are better able to fund our own community projects.

-------------------------

thedevanshmehta | 2023-12-12 10:39:22 UTC | #2

Thanks for sharing this Sejal, really interesting pilot of integrating hypercerts with projects in their gitcoin round

I went through some of the projects and the hypercerts they minted, and I'm still unsure of their value add - what additional information or validity does the hypercert provide which is not already there in their project description?

Ideally it would have been good to have hard numbers against the hypercerts - this was our past impact and here's the cost we incurred in reaching it. Then we'd have an extra layer of accountability or information we can hold projects against and also compare with one another.

-------------------------

robioreefeco | 2023-12-12 15:18:27 UTC | #3

We are here early, hypercerts are awesome… 

Our task is to discover genuine onboarding mechanisms, creating on-chain value and meaningful impact.

Thanks for the experiment ✨💚
@sejalrekhan @lanzdingz @bitbeckers

-------------------------

FractalVisions | 2023-12-12 15:50:19 UTC | #4

Totally 💯 agree 👍… While hypercerts is still a work in progress there are a ton of things that need to be improved upon.

We for one can not get Hypercerts website to load properly & the tech team in the support channel of their discord gave up on helping us sort out the issues.

So our ability to mint any hypercerts has been taken away until their team provides us with a solution.

That being said anyone can create a hypercert to say anything they want which doesn’t necessarily mean the work was completed.

Who is going to hold projects accountable for their hypercerts ?

-------------------------

bitbeckers | 2023-12-12 21:25:30 UTC | #5

gm, sorry to hear you see it this way. Are you also in our Telegram? Feel free to reach out to me because I can't find any open issues related to you not being able to mint.

> Who is going to hold projects accountable for their hypercerts ?

This is a good question and high on the priority list for hypercert development. We want to support initiatives from organisations evaluation impact in a given domain. Gitcoinreviews / deresy is a good example -currently- or an application focussing on evaluating impact claims.

-------------------------

FractalVisions | 2023-12-12 22:08:03 UTC | #6

Yep 👍 we were directed to use the discord for our issue with minting from one ☝️ of the members in the TG chat that works for hypercerts.

Here is a link to the conversation where we were left hanging.

https://discord.com/channels/1075404472152494100/1169409394312757328

-------------------------

lanzdingz | 2023-12-15 19:02:33 UTC | #7

This is a great point, and something we also brought up internally - what constitutes 'impact' and how it is measurable/what are the metrics we use to measure it? @jon-spark-eco I know is diving into this with his project which we hope to use to help us answer these questions. 

On our end too we should have provided more structure for people minting hypercerts so that we could have had a better impact value captured.

-------------------------

lanzdingz | 2023-12-15 19:03:02 UTC | #8

thank you for participating in it with us

-------------------------

lanzdingz | 2023-12-15 19:04:53 UTC | #9

Yes, we also are looking into what systems are needed to 'verify' impact/that the work has been done. This was the first step in moving towards a more verifiable and measurable impact. We still have a long way to go but learned a lot from this first experiment.

-------------------------

krrisis | 2024-01-11 17:34:18 UTC | #10

Super interesting, thanks for sharing, also looking into this for the next Citizens Round. 

[quote="sejalrekhan, post:1, topic:17257"]
There was not enough quality control as any chapter could mint on their own without having to meet certain criteria. This resulted in a mixture of impactful hypercerts and some highly frivolous ones.
[/quote]

Wondering if what @mmurthy is building for [gathering of proof of work here with milestones](https://gap.karmahq.xyz/gitcoin/?categories=&status=all&sortBy=milestones), could be linked to the issuing of the hypercerts?

-------------------------

wasabi | 2024-01-11 22:10:32 UTC | #11

[quote="krrisis, post:10, topic:17257"]
Wondering if what @mmurthy is building for [gathering of proof of work here with milestones](https://gap.karmahq.xyz/gitcoin/?categories=&status=all&sortBy=milestones), could be linked to the issuing of the hypercerts?
[/quote]

Would be cool if we can mint Karma GAP milestones as Hypercerts on 1-click

-------------------------

owocki | 2024-01-19 03:38:27 UTC | #12

podcast about this experiment just dropped!

https://www.youtube.com/watch?v=yUybHaHKAHw

-------------------------
