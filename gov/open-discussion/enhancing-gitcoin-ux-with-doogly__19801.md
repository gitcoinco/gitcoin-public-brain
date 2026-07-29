---
id: 19801
title: "Enhancing Gitcoin UX with Doogly"
slug: enhancing-gitcoin-ux-with-doogly
category: open-discussion
url: https://gov.gitcoin.co/t/enhancing-gitcoin-ux-with-doogly/19801
created_at: 2024-12-27T10:51:50.449Z
last_posted_at: 2025-01-25T15:26:25.166Z
posts_count: 9
views: 2323
like_count: 6
---

# Enhancing Gitcoin UX with Doogly

<https://gov.gitcoin.co/t/enhancing-gitcoin-ux-with-doogly/19801>
Prajjawalk | 2025-01-01 06:34:07 UTC | #1

# Introducing Doogly

## Summary

Doogly is the mobile-first Allo client and donation platform. It is built on top of Allo protocol where the donors can swipe through the projects, donate cross-chain using any ERC20 token they have, and get hypercerts which will accrue impact attestations as their donated project creates some impact to the ecosystem.

The aim is to create the best possible mobile-UX for the participants of gitcoin quadratic funding mechanisms to actively engage, donate and vote for the projects.

The MVP is already live, checkout - https://donate.doogly.org

## Problem

The participant’s attention becomes really valuable when the quadratic funding mechanism requires human-in-loop and creating the better UX maximises the efficiency with which the attention span is utilised hence impacting the overall outcome.

Whenever the donor tries to participate in the quadratic funding round to support projects they have to encounter certain friction points -

1. Cherry-picking the right projects from the pool of 1000+ projects is much of an hassle especially when it involves impact evaluation

![problem_1|690x417](upload://2XiTKPSATK3tprv2vl3CM41myq8.jpeg)

2. Even after the user manage to successfully curate the right projects there is no easy way to donate to the projects when they don’t have the required tokens on the required chain
![problem_2|690x363](upload://8GIRgJKyR8ZfGfNI3KOyLEOmk8A.jpeg)

## Solution

In order to make the donor’s life a bit easier we have built Doogly. Features -

1. The project discovery is powered by a recommendation algorithm that recommends the right projects to the donors that they can swipe left and right.
![project_page_1|690x376](upload://kjeTKwNntQdp018EHVMkQaGWLi5.jpeg)

2. The user can check the project details, endorse them, and we present the project impact metrics in the format understandable to them
![project_page_2|690x381](upload://1AOncmgpPYYi51KVISwvHUJX3aU.jpeg)

3. On clicking the endorse button the user can provide rating, endorsements and additional feedback to the projects in the form of on-chain attestations
![endorsement_page|690x375](upload://svQOzas6xkCmkwOyN42BV2Soc3q.jpeg)

4. User can also view detailed description of the project that also includes the impact details. All of this combined will help the users make an informed decision regarding which projects to support.
![details_page|690x373](upload://fv7eEPflMztMAVdrNq9zTmxrwi2.jpeg)

5. Once the users clicks the donate button, they can visit the checkout page by clicking the bag icon at bottom right. The users can then select the desired chain and token and click donate. Doogly will perform all the swapping and bridging in order to ensure the receivers get the right token on their correct destination chain.
![checkout_page|690x383](upload://rVOr3SF4z8zEage7Z0n2H64tUJc.jpeg)

6. Upon successful contribution the donors will get hypercerts (https://hypercerts.org) as a token of impact
![hypercerts_page|690x383](upload://4vt0hMxy886bjnGFm9bfvd5dO1N.jpeg)

### Why Doogly?

* It’s good to have multiple clients on top of Allo protocol providing flexibility for the users to choose from many and it also promotes decentralization
* Having the mobile-first UX with added gamification + social layer will drive more engagements to Allo protocol

Doogly is still at its experimentation phase and initial aim is to have users test out this product, get quick community feedback so we can iterate faster while we are still figuring out pmf.

### Roadmap -

1. Current progress -

  - MVP completed with swipe left and right feature, checkout - https://donate.doogly.org
  - Privy integration for frictionless user onboarding
  - Users can donate to the projects cross-chain using any of the supported ERC20 token (powered by Squid router)
- Since there is no ongoing Gitcoin round, direct donations are supported now.

2. Milestone 1 (1 - 1.5 month) -

  - Project recommendation algorithm
  - Feature integration - QR scan -> get project details -> vote/donate
  - Additional feature enhancements based on requirements of Schelling Point, Denver

3. Milestone 2 (1 month)

  - Project endorsements + KarmaGAP integration for project impact metrics
  - Hypercerts integration

4. Milestone 3 (1 month)

  - User feedback -> product iteration cycle
  - Social engagements + gamification through Commit protocol integration (https://www.commit.wtf/)

### Success Metrics and KPI

* Maximization for the funding of high impact project rather than popular ones
* Increase in the total Gitcoin donation volume by >5%
* 100+ unique donors per GG round

### Team - 
Prajjawal Khandelwal -
Twitter - https://x.com/prajjawalkh
Github - https://github.com/Prajjawalk

### Call to action -

1. User - Do try out Doogly and donate to projects using this link - https://donate.doogly.org and your feedback would be highly beneficial to make this product even better - https://forms.gle/jrWfCY9btdp8vDUQ7

2. Projects - Share me your project id to get your project whitelisted, DM (https://t.me/prajjawal003)

3. Funder - Anybody wishing to fund the development of Doogly, please donate to prajjawal.eth

4. Cheerleader - Please follow Doogly on twitter - https://x.com/dooglyy and join the community - https://t.me/+tK5zI5ohunI2Mjhl

-------------------------

masterhw | 2025-01-06 19:32:54 UTC | #2

Hey Prajjawal, happy to see [donate.doogly.org](https://donate.doogly.org/) live :slight_smile:
As devrel it brings me joy that others are able to come in and successfully build/integrate without needing support or permission first.

[quote="Prajjawalk, post:1, topic:19801"]
3. Funder - Anybody wishing to fund the development of Doogly, please donate to prajjawal.eth
[/quote]

I would encourage you to launch Doogly as a project that can be supported using Doogly!
I also appreciate your commenting on the Yollow proposal - your apps are clearly very aligned and I believe there is strong possibility for a better-together collab.

Look forward to the next iteration with the recommendation algorithm. If there is any way I can be of help, feel free to reach out :saluting_face:

-------------------------

owocki | 2025-01-06 21:17:02 UTC | #3

> As devrel it brings me joy that others are able to come in and successfully build/integrate without needing support or permission first.

same!

im wondering if any pilot customers / pilot campaigns have been identified for doogly? or is it built to bolt onto grants stack and be used in GG rouhnds?  itd be interesting to see this hit the market and see how it performs in the wild

-------------------------

Prajjawalk | 2025-01-07 06:39:20 UTC | #4

Yes, it is intended to be directly integrated with the grants stack and used with GG rounds. I will pilot this project with GG23 and Citizen Retro which will run alongside GG23, and let's see how it performs.

-------------------------

Prajjawalk | 2025-01-07 18:57:49 UTC | #5

Thanks a lot @masterhw, much appreciated, I will definitely reach out for help in case.

-------------------------

owocki | 2025-01-07 14:33:34 UTC | #6

[quote="Prajjawalk, post:4, topic:19801, full:true"]
Yes, it is intended to be directly integrated with the grants stack and used with GG rounds. I will pilot this project with GG23 and Citizen Retro which will run alongside GG23, and let’s see how it performs.
[/quote]

got it; then id love to know from @meglister and @katalunia whether they plan to embrace a tool like this.  what would have to be true to route this proposal to the most value?

-------------------------

Sixty | 2025-01-07 14:52:09 UTC | #7

[quote="Prajjawalk, post:1, topic:19801"]
Whenever the donor tries to participate in the quadratic funding round to support projects they have to encounter certain friction points
[/quote]

hey @Prajjawalk, as someone who would love to participate more in the Gitcoin ecosystem, the friction points you mention ring very true in my case. Super excited to see more efforts to improve UX like Doogly coming up

-------------------------

Sirlupinwatson | 2025-01-23 09:50:40 UTC | #8

Looking great, would love to coordinate with you and talk about your project and mine and I believe we could do a sort of merge or shared code, would you be interested?

-------------------------

Prajjawalk | 2025-01-25 15:26:25 UTC | #9

Sure, lets connect over tg - [Telegram: Contact @prajjawal003](https://t.me/prajjawal003)

-------------------------
