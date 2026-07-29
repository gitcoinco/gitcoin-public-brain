---
id: 10777
title: "Prepping cGrants for its Final Voyage"
slug: prepping-cgrants-for-its-final-voyage
category: gitcoin-grants
url: https://gov.gitcoin.co/t/prepping-cgrants-for-its-final-voyage/10777
created_at: 2022-06-01T18:12:25.305Z
last_posted_at: 2022-06-02T11:56:24.359Z
posts_count: 3
views: 2632
like_count: 13
---

# Prepping cGrants for its Final Voyage

<https://gov.gitcoin.co/t/prepping-cgrants-for-its-final-voyage/10777>
nategosselin | 2022-06-02 11:57:06 UTC | #1

The Gitcoin team has iteratively built up the centralized Grants platform (aka cGrants) over the last 13 seasons of Grants Rounds. We’ve run countless experiments on the platform, enabled millions in grant funding, and helped launch core projects in the Ethereum ecosystem. However, the major investment in [Grants 2.0 is a realization](https://gov.gitcoin.co/t/grants-2-0-is-how-we-scale-our-impact/10015) that cGrants has reached its ceiling and that we need to pour all we’ve learned over its lifespan into a new foundation if we’re going to fully realize our organizational vision. Before our shiny new protocol is ready to take over the load though, we’ll need the venerable cGrants platform to power a couple more grants rounds.

In order to get cGrants ready for its swan song, the Gitcoin Product Collective [spent a chunk of its time](https://www.notion.so/gitcoin/Prep-cGrants-for-autopilot-afbf413eb5f7414b87e9604f7aedbc57) over the last couple months patching holes and getting the platform into the best possible shape. This work included:

[**Checkout TLC**](https://www.notion.so/gitcoin/Improve-Checkout-Contribution-UX-238660cc500746fe889727bf5824de45) — the “checkout” experience arguably sees the heaviest use on the platform, and its wiring is complex given the number of chain, wallet, and token options we’ve built into the flow. We [audited the checkout experience](https://www.notion.so/gitcoin/Checkout-Research-Findings-April-2022-69480850163a48999f5b59a58fff7118) and identified the most common combinations, then heavily tested and tweaked the top flows where needed. While an aspect of checkout will always be dependent on components outside of our control (i.e. chains and wallets), we have put this version of checkout in the best possible position to handle the largest potential swath of traffic during a grants round.

**Coinbase Wallet support** — also on the checkout front, we’ve updated our options to include support for the Coinbase Wallet extension. We know this is a popular wallet, and users who prefer this implementation will now be able to use it on cGrants.

![|624x321](upload://5GKEnTEzlUekgYsp0ztMCTAHrc7.jpeg)

**Short URLs** — we know that a big part of a grants round is the community sharing and discussing their opinions. To help this discourse, we’ve enabled short, easily-shareable URLs for each round within GR14 and added a share button so that community members can promote the causes they care about.
![image|690x197](upload://lQlTKUNSJPT2CVsdbAuG94eBgpl.jpeg)


[**Search improvements**](https://www.notion.so/gitcoin/Search-as-expected-db788196d46740618fb57b7cad03d99c) — we’ve made significant investments into our global search and grant explorer search UX to remove some common navigation issues we’ve heard from the community. Search should now return more relevant results and in less time.

[**Ops Workflow updates**](https://www.notion.so/gitcoin/S14-Ops-workflow-improvements-757e4b5177f14fe1b49b06f4ee6785a9) — there’s a highly dedicated team of Gitcoiners who ensure that the service side of a Grants Round runs smoothly, and there are some key points in their workflow that have become painful as we’ve scaled. While the future Round Manager dApp is the long-term solution for these workflows, we’ve provided a few quick fixes ahead of GR14 to help make everyones’ lives easier.

[**Copy Cleanup**](https://www.notion.so/gitcoin/Copy-clean-up-05269476ff854ed0a481d84dc2137a2b) — grants rounds have evolved a lot over the past 13 seasons and we know that some of our language doesn’t always make sense. We dug deep into the site to clean up copy where we could, and identified key concepts that we will further clarify as part of Grants 2.0.

![|624x643](upload://wsoCq1E72ksag3EUSy2jsiuGuAq.jpeg)

Taken together, we hope that these updates will help us continue to successfully fund grants while we build out the next chapter of our protocol. The Grants team has now turned its full attention to the Grants 2.0 roadmap and getting it out into the world as quickly as possible. Even though we’ve cleaned up the old platform as much as we can, we know that bugs will occasionally arise and will have 1 engineer and 1 product manager on call each week for cGrants. We won’t be introducing new features to the platform but we will be available to help with issues that pop up. In the meantime, we’d love for you to follow along with our [weekly](https://gov.gitcoin.co/t/weekly-grants-2-0-update-2022-5-30/10760) [updates](https://gov.gitcoin.co/t/weekly-grants-2-0-update-2022-5-16/10625) on Grants 2.0.

-------------------------

connor | 2022-06-02 08:33:46 UTC | #2

Thank you for your hard work and support! Onward and upward :slight_smile:

-------------------------

puncar | 2022-06-02 11:56:24 UTC | #3

Great to see so much improvement, and also a very comprehensive approach to defining and implementing those improvements. 
Thank you for making our flagship product better and GitcoinDAO stronger!

-------------------------
