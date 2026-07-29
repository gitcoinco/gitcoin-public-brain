---
id: 11886
title: "Gitcoin starts and supports the OpenData Community"
slug: gitcoin-starts-and-supports-the-opendata-community
category: governancevision
url: https://gov.gitcoin.co/t/gitcoin-starts-and-supports-the-opendata-community/11886
created_at: 2022-11-09T02:21:54.296Z
last_posted_at: 2022-11-15T16:44:27.280Z
posts_count: 3
views: 2905
like_count: 8
---

# Gitcoin starts and supports the OpenData Community

<https://gov.gitcoin.co/t/gitcoin-starts-and-supports-the-opendata-community/11886>
epowell101 | 2022-11-09 02:21:54 UTC | #1

## Why an OpenData Community?

Gitcoin is evolving! Gitcoin has helped countless public goods projects to launch and scale but the time has come to further decentralize and scale Gitcoin itself. Instead of a public goods funder, Gitcoin will be a funding-factory. You can read much more about this transition in a recent blog post from the Gitcoin DAO here:
https://go.gitcoin.co/blog/introduction-to-grants-protocol

Decentralizing public goods funding means empowering individual communities to manage their own funding rounds. Gitcoin will provide the underlying protocols, related software, and expertise so that community-led public goods funding flourishes.

To achieve this, Gitcoin is deemphasizing its active involvement in the mechanics of grant funding, such as administration, grant reviewing, Sybil defense, and more and is instead leaning heavily into research and development with partners and open-source communities to develop and maintain protocols, tools, and useful data sets and infrastructure for community-led grant rounds. This is true both for the development of the grants protocols and the creation of algorithms and data analysis to protect and operate public goods funding.  

However - there is a risk that Gitcoin's vision of enabling communities to fund their shared needs will be undercut by *recentralization at the data layer*. The web3 data layer just above the blockchain is typically centralized in most stacks used by DAPPs and analysts, relying on proprietary interfaces, raising the risk of capture and censure. Even common tasks such as looking at transactions made by one's own wallet almost always are performed using centralized APIs. 

Moreover - many data practitioners including popular data analysis tool providers find themselves reinventing the wheel each time they set out to make sense out of the data; indices, schemas, transformations, and more of the data plumbing must be built and deployed before the real work of insight generation begins - all of which leads to more short cuts via the use of centralized services.      

The good news is that communities are the antidote to this creeping recentralization. Together we will prevent the tragedy of the commons by building a sustainable community that rewards open innovation.  

We are happy to announce the commitment of Gitcoin and the Fraud and Detection team to the emerging Open Data Community. The OpenData Community is where Gitcoin collaborates with the broader web3 community to increase the openness and usefulness of the web3 data stack. While we will particularly focus on protecting web3 and enabling the flourishing of public goods funding, in part by making the Open Data Community the home for our Anti-Sybil analysis and data engineering, we will also seek to solidify the data foundations of web3.    

## We had a Hackathon 

To help kick off this transition to more open collaboration, in October we held our first data hackathon. Nearly 200 participants joined and the spirit of collaboration on the public Discord was amazing to see. Stay tuned as we will be announcing the winners shortly and inviting them to join us in an upcoming Twitter space to learn more about them and their insights.   

We broke the hackathon into three guilds:
### Sybil slayers

Sybils disrupt quadratic funding of public goods by creating multiple user profiles that then vote in concert, greatly amplifying the influence of the attackers. Gitcoin's FDD team is at the forefront of anti-Sybil efforts and shared with contestants data and algorithms that contestants then attempted to improve. The mission for this guild was to interrogate the data to find new ways to *identify Sybils* from hidden signals in the data. 

Right now, Gitcoin implements a two-pronged approach to Sybil defense. There is a human-in-the-loop machine learning model that identifies users with Sybil-like behaviours and then retroactively "squelches" them (either eliminating them from the system or reducing their influence). At the same time, Gitcoin Passport aims to collect evidence of real personhood so that users can be confidently labelled "honest non-Sybil" at the outset. These two approaches have been developed largely independently but are becoming increasingly synergistic and integrated.

You can read much more about Gitcoin's efforts to counter Sybils [here](https://gov.gitcoin.co/tags/c/open-discussion/9/fdd-review). 
 
### Human hackers

Human reviewers complement automated analysis in public goods funding. Humans can become a bottleneck in the grant system because they are relatively slow and expensive. The Human hacker track of the hackathon aimed to find the right way to decentralize grant reviewing in ways that maintain quality and reliability without relying on a small pool of trusted reviewers. Contestants had access to a rich dataset showing the impact of different reviewer incentives on review quality and competed based on they insights they shared into optimal incentive design. 

You can read some of the background to the work FDD at Gitcoin does to study human incentives [here](https://gov.gitcoin.co/t/decentralizing-sybil-defense-using-gitcoin-data/11382/1). 

### Dune detectives

Monitoring and visualizing data is a powerful tool for exploring and understanding public goods funding rounds. Dune Detectives had access to all Gitcoin data and complete creative freedom to design novel dashboards that are useful for contributors to grants rounds and for grants round managers. A few competitors asked whether they could use Flipside Crypto and other alternatives to Dune to which we responded "heck yeah - serve it up" or words to that effect.  

The hackathon has been a success. In addition to gathering countless novel approaches we are now reviewing before sharing widely and proudly - we have also learned a lot about the design of data hackathons. We are working with others in the OpenData Community to plan the next data hackathons as well as the design of the OpenData Community itself.

## Join the OpenData Community!

Whether you are a data scientist, a community builder, a Discord degen, a project developer, or someone who wants to make sense out of web3 data with recommended solutions that support the decentralization ethos of Ethereum and web3 - please drop in and help build a more open data future.

There are at least a couple of ways to get involved with the OpenData Community:
* Join our Twitter Spaces on 16th November at 10am (Pacific time): https://twitter.com/i/spaces/1MnxnpbqmdkGO
* Please drop into our brand new Discord: https://discord.gg/KJ6PGH4cnK
* Or check out and add to our landscape and plan here: https://github.com/OpenDataforWeb3

You can also be one of the first to follow the community on Twitter:  
* https://twitter.com/OpenDataforWeb3

A special thanks to @j-cook for writing much of this post (the well-written parts) and to FDD and the broader DAO for making the initial OpenData hackathon a success.  We will be sharing many insights from the hackathon in the days to come.

-------------------------

shawn16400 | 2022-11-15 11:47:09 UTC | #2

I like this approach and that it was delivered to my door via Gitcoin.  And in web3 I am noticing a trend that goes something like "hey I have a great idea for a platform, how about you come join me" to which I see the response "I really really love that idea, but look at this platform I just created, how about you come join me??."   We in web3 seem to exacerbate this scenario with twitter-hero-worship which feeds the ego, a disease of the heart.

In the competition of ideas, these competing platforms lead to fertile grounds from which to harvest from, but blows a ton of time, energy, and money on platforms that will die (dotcombombanyone?).  Was there any research done to find existing platforms that are already addressing this need,  where we can amplify the hell out of someone else's great idea (former grants round winner?), or is this a novel approach that requires a new DAO, not just a new channel?

-------------------------

epowell101 | 2022-11-15 16:44:27 UTC | #3

Great question - yes we did some basic research and didn’t find any communities hitting these needs.  There are some landscapes for data tools in web3 that we will embrace and extend as opposed to reinventing the wheel for example.  In a community whose purpose in part is to help analysts to not have to reinvent the wheel - we need to make sure the OpenData Community itself also does not fall into that trap!

-------------------------
