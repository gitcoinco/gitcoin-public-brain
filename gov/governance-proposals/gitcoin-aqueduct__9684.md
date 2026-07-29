---
id: 9684
title: "Gitcoin Aqueduct"
slug: gitcoin-aqueduct
category: governance-proposals
url: https://gov.gitcoin.co/t/gitcoin-aqueduct/9684
created_at: 2022-01-12T23:15:21.893Z
last_posted_at: 2022-01-19T20:27:41.976Z
posts_count: 17
views: 10820
like_count: 66
---

# Gitcoin Aqueduct

<https://gov.gitcoin.co/t/gitcoin-aqueduct/9684>
paradave | 2022-01-12 23:15:22 UTC | #1

## Authors

[Dave White](https://twitter.com/_dave__white_), [Kevin Owocki](https://twitter.com/owocki)

## Summary

This paper introduces **Gitcoin Aqueduct**, a tool that incentivizes ecosystem development for your project with a single line of Solidity.

Aqueduct helps unbundle the work of protocol creation from the work of supporting an ecosystem, and helps protocols grow in a truly decentralized way.

To fill your Aqueduct, you transfer in some of your project’s revenue or inflation.

In the beginning, your Aqueduct will distribute these tokens to developers on your ecosystem automatically, creating and running [quadratic funding](https://vitalik.ca/general/2019/12/07/quadratic.html) rounds with no human intervention.

As your project grows and more assets flow into its Aqueduct, GitcoinDAO will begin to provide more and more high-touch ecosystem development services.

## Narrative

### Problem

Alice is developing a new NFT project, NFTP. She is a talented coder and artist and believes in what she is making.

Alice also knows that if her project is to be successful long-term, it will need an ecosystem, with other developers contributing, a team managing the Discord, and so on.

However, Alice is a builder, not a manager. She is also committed to decentralization.

As a result, she doesn't want to personally coordinate an ecosystem long-term, and she doesn't want to set up an organization or hire somebody to do it for her.

### Solution

By design, NFTP receives ongoing revenue from secondary sales of its NFTs.

Alice redirects 10% of this revenue to NFTP’s Aqueduct.

If NFTP were intended as a pure public good, it might send 100% of revenue to its Aqueduct.

### Result

After a sufficient amount of tokens accrue in the Aqueduct, Gitcoin automatically holds a [quadratic funding](https://vitalik.ca/general/2019/12/07/quadratic.html) round for NFTP using those tokens: developers propose projects that will benefit the NFTP ecosystem, and members of the NFTP community allocate the Aqueduct’s funds to those projects using the quadratic funding mechanism. 

GitcoinDAO supports this process both by providing the infrastructure for funding and by promoting the round on Twitter and other channels (including, perhaps, a list of Discords to which a GitcoinDAO bot has been invited). Critically, none of this requires any significant expense or human time.

Furthermore, it requires no further interaction from Alice or NFTP, which doesn’t even need to have governance.

As NFTP grows, aided by Aqueduct-funded development, the amount of revenue allocated to the Aqueduct will grow as well, eventually reaching a point where human involvement is both prudent and economical.

Accordingly, at certain pre-defined revenue tiers, the level of service provided by GitcoinDAO will increase.

For example, a $100K Aqueduct might come with automated human-in-the-loop anti-fraud support, while a $1M Aqueduct might come with a part-time community manager, and a $10M Aqueduct might come with a full-time ecosystem management team.

GitcoinDAO would be compensated with a percentage fee for providing these services.

## Mechanism Notes

### Side Round Protection

The main challenge with this design is how to ensure that funds in the NFTP side-round are actually spent on NFTP ecosystem projects.

At sufficient levels of Aqueduct funding, a fee to GitcoinDAO could easily pay for humans to help ensure grants are appropriate.

For smaller rounds, or even to ensure alignment in larger rounds, specific protection mechanisms might help. For example, in order to match a donation of 1 ETH, Aqueduct might require the donor to stake at least 5 ETH worth of NFTP NFTs for some time period.

Or, it might require the person posting a new grant to post a bond that can be slashed if they are found to have submitted a project that isn't for the benefit of NFTP, with the bond amount sufficient to incentivize both reporting and adjudication.

### Alternatives to Quadratic Funding

Today, quadratic funding is the leading system for permissionless ecosystem development.

Over time, other methods like [Retroactive Public Goods Funding](https://medium.com/ethereum-optimism/retroactive-public-goods-funding-33c9b7d00f0c) might prove to be more effective.

Any such method can easily integrate with Aqueduct.

## Conclusion

Gitcoin Aqueduct unbundles the work of designing and implementing a protocol from the work of scaling it and managing its community.

By doing so, it reduces the friction involved with starting a protocol while providing opportunities for developers to make a living contributing to open source.

This is only a rough design sketch, and there are likely many problems to be solved before it can become a reality.

We’re excited to hear your feedback and work on improving it together.

## Acknowledgements

[Dan Robinson](https://twitter.com/danrobinson), [llllvvuu](https://twitter.com/llllvvuu), [Allan Niemerg](https://twitter.com/niemerg), [Jordan Lazaro](https://twitter.com/jordanlzg), [Greg Fodor](https://twitter.com/gfodor)

-------------------------

umarkhaneth | 2022-01-12 23:58:38 UTC | #2

This is awesome.

I can imagine Public Goods projects using some sort of funding curve where as the amount of proceeds they generate increase, the amount going to Aqueduct increases too. This would allow Founders to support themselves in early days and then let the funds flow to the ecosystem in later days. 

Let's make up an example for illustration: If NFTP has a wallet which has received less than 100k then maybe 10% flow into the aqueduct. If the project has received more than 1 million then maybe 50% flow into the aqueduct. If the project has received more than 10 million then 90%+ should flow into the aqueduct.

-------------------------

owocki | 2022-01-13 01:53:47 UTC | #3

if people have questions, or would like to discuss the design, pls comment below.

or you can pls contact aqueduct@gitcoin.co if you'd like to set up a Gitcoin Aqueduct.

![is-this-a-pigeon (5)|690x414](upload://vhDA7d1gm6ssISxCOowJ17U47qs.png)

-------------------------

0xjim | 2022-01-13 04:20:04 UTC | #4

Really cool idea! This reminds me of an automated version of Metis' "ecosystem mining" program they announced last week.

Nitpick on the value prop: in the illustrative example, you mentioned that Alice is a builder and doesn't want to deal with growing an ecosystem. However, Aqueduct only automates the BD/grants/dev relations part of running a project, and doesn't touch the marketing side -- which will still need to be done by Alice's team.

-------------------------

owocki | 2022-01-13 05:22:35 UTC | #5

> Metis’ “ecosystem mining” program they announced last week.

will check that out!

[edit: found it!](https://twitter.com/MetisDAO/status/1478872569394700296)

[quote="0xjim, post:4, topic:9684"]
However, Aqueduct only automates the BD/grants/dev relations part of running a project, and doesn’t touch the marketing side – which will still need to be done by Alice’s team.
[/quote]

why is that?  

AFAIK - there are plenty of marketing teams funded by QF in recent grants rounds.

-------------------------

leeyy777 | 2022-01-13 10:04:20 UTC | #6

真的很酷的想法我可以想象公共产品项目使用某种资金曲线，随着它们产生的收益量增加，进入Aqueduct的金额也会增加。这将使创始人能够在早期支持自己，然后在以后的日子里让资金流向生态系统

-------------------------

Sirlupinwatson | 2022-01-13 16:23:21 UTC | #7

Interesting, can you expand how does this work or it's still a work-in-progress, do you guys have an architecture model for the solidity line of code that represent what it actually do, is this an addon over an existing contract that bridge both?

I'm really curious about that and understand the process of funds distribution from that !code 

[quote="paradave, post:1, topic:9684"]
Furthermore, it requires no further interaction from Alice or NFTP, which doesn’t even need to have governance.
[/quote]

Looking really great!

-------------------------

0xjim | 2022-01-13 16:27:31 UTC | #8

Ah I see - so the Aqueduct can also fund marketing contributors

-------------------------

simplemachine92 | 2022-01-13 17:33:47 UTC | #9

Hey Dave, Kevin,

Read through the notion after Kevin sent me the draft, and as a solo-maintainer / dev of a public goods supporting project (Mars-Shot Bots), I really see the niche for this.

What if we think of this as a permission-less system, where we can identify "Cartels"? We could enable anyone to contribute to "Moonshot", "Mars-Shot", "LARP" cartels, simply by including an ID in their contract. When funding, or x amount is received from a contract, we can call a view function to retrieve their ID, and associate them with their cartel for a funding round.

Anyway, really interested in helping y'all get this off the ground.

-------------------------

DisruptionJoe | 2022-01-13 17:52:45 UTC | #10

This is a game changer. Love the idea. Looking forward to see how people use it.

-------------------------

annika | 2022-01-13 18:02:40 UTC | #11

I love this idea and am excited to collaborate in bringing it to life.

In case it's helpful to others as we ideate on what this might look like, I [jotted down some thoughts](https://docs.google.com/document/d/1RqXqSxJz2b6XYgYKAppx4P0yyZricaBkDSipWYIpZjk/edit) on my interpretation of the write-up and the potential solution sets & customer sets that I gleaned from it.

-------------------------

joshuavial | 2022-01-13 22:00:00 UTC | #12

Best proposal I have seen in a long time. Love it.

-------------------------

seedphrase | 2022-01-14 10:28:58 UTC | #13

Oh wow! This is an awesome concept.

-------------------------

Jordan | 2022-01-14 19:00:43 UTC | #14

This is a game changer for the whole ecosystem, love to see the community reaction. 

Already seeing a possible improvement : 

[quote="paradave, post:1, topic:9684"]
bond that can be slashed
[/quote]

This would make sense only if bonds can be community sponsored.

Indeed if all proposals must have bond then we run into a problem where proposers without any "cash" cant add value to the projects and we might end up money gating contribution.


A potential solutions would be to have proposers submit the proposal “off chain” and anyone from the community could stake on their behalf to support the aforementionned proposal, once the staking thresehold is met, the proposal becomes on-chain code and enter the aqueduct voting system.

We can call this the Dropshafts, those are safety mechanism in aqueduct architecture.

Happy to hear feedback on this to make the aqueduct even more efficient.

-------------------------

rahul-kothari | 2022-01-15 19:10:25 UTC | #15

Love this idea! Esp that Alice can now grow and reward the ecosystem without having to do grants or be ever present on discord.

1. How do you determine who in the ecosystem would be rewarded? Is it an automatic or manual process?

2. What are the biggest technical problems do you see rn for implementing this?

3. Stupid question that I might have missed -> will the contributions to Aqueduct be strictly in GTC or their token or a mix?

-------------------------

DisruptionJoe | 2022-01-19 11:51:24 UTC | #16

Jordan, that is a cool consideration! Thanks for posting. I see this is your first post on the forum. Are you in the Discord already?

-------------------------

frankchen07 | 2022-01-19 20:27:41 UTC | #17

This may come out as we experiment with the first initial groups in the Aqueduct, but do you think it's a risk that this fundamentally separates handling possible protocol development and the community that supports the protocol?

The positive case is that this would be a good separation between protocol building and the Aqueduct funding spawned off projects themselves in the community that eventually become public goods.

In the example for the NFTP ecosystem, what are the guidelines for the proposals that developers give? I can see in the case of a protocol, there can be projects that spawn off of it, but if it's already a set NFT project, are Aqueduct funds used to develop a community, or develop additional projects on top of NFTP? Is this distinction even important?

-------------------------
