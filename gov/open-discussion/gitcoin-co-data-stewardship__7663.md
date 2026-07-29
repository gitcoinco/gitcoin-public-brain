---
id: 7663
title: "Gitcoin.co Data Stewardship"
slug: gitcoin-co-data-stewardship
category: open-discussion
url: https://gov.gitcoin.co/t/gitcoin-co-data-stewardship/7663
created_at: 2021-07-02T19:14:39.897Z
last_posted_at: 2021-07-04T06:55:08.042Z
posts_count: 3
views: 3293
like_count: 17
---

# Gitcoin.co Data Stewardship

<https://gov.gitcoin.co/t/gitcoin-co-data-stewardship/7663>
owocki | 2022-05-28 15:38:05 UTC | #1

Hi all,

I wanted to daylight something thats been keeping me up at night - data stewardship.

As you know we are focused on [decentralizing Gitcoin](https://gov.gitcoin.co/t/workstream-suggestion-decentralize-gitcoin/180) in the next several years.  When that is done, the Grants platform will be provably credibly neutral, permissionless, transparent, forkable, composable, and secure and -- on the subject of user data -- the user data will be self sovereign owned by the users that use the platform, perhaps in a 3box/DID type architecture.

Until then, I wanted to open up a discussion with the community about what responsible data stewardship on the existing Gitcoin.co marketplace looks like. 

Why do this now?  I am reminded of the [hippocratic oath](https://en.wikipedia.org/wiki/Hippocratic_Oath) which is basically 'first do no harm".  stated more bluntly.... until we decentralize Gitcoin, I'd love to make sure that we dont do anything awful -- like dox an end user or have a data leak of some sort.

So Id put this question to you all , the community - What does responsible data stewardship look like to you?  Both in the short, medium, and long term.

For reference, [Here is the current gitcoin.co data privacy policy for reference](https://gitcoin.co/terms/privacy)

-------------------------

octavioamu | 2021-07-02 22:01:04 UTC | #2

Thanks Owocki to open this topic, been already looking some alternatives and want to share my thinking and discoveries around it.

# Mastodont
Been reading about it for long time and seems a very nice way to decentralize an open source project.
How it works can be read here https://savjee.be/videos/simply-explained/mastodon-and-fediverse-explained/ but basically this runs under the [activityPub](https://www.w3.org/TR/activitypub/) protocol that make possible different instances communicate with each other. (if you want to see how that data looks like check this [real life example](https://mstdn.social/users/stux/statuses/106506229806664176/activity) of a twitter like data) 

Mastodont is a twitter like app but there are many diff apps like reedit like, youtube like, medium like [etc](https://fediverse.party/)... all built on activityPub, I only bring mastodont as one of the most successfully and popular apps using it.  

## In practice
Lets talk for example about bounties, what if someone want to run his own bounties instance? well will be just them going and run the repo on their own servers and then decide which others servers data want to share with. 

# Data
The other part of it is data owning  as you can actually see the data on others instances you actually can walk away with it. Lets say Polkadot folks decide to run his own bounties platform, some user original from Gitcoin can decide start only using polkadot instance instead, so even if gitcoin is turned off the user lives on the "[Fediverse](https://simple.wikipedia.org/wiki/Fediverse)"

# Innovation
Something I really feel could be explored and not aware nobody is doing, is mixing the best part of 2 worlds web3 and activitypub protocol. So going further seems there is a lot to be explored where we could be, for example, using decentralize DBs to store the data instead of instances DB. 

What are the wins? Well we could be providing good way to people run his own instances of "bounties" but at the same time using a well funded protocol like activitypub we provide a solid architecture foundation for makers, where someone could just grab the backend and rebuilt all the product with a diff UI, or even extend the functionality. 


# Today
As a core dev member this could be a nice way to start thinking a way to build and rebuild things on Gitcoin but in a way we are attached to a pattern that scales and is **open by default** so as our intention to be more REST like application under json data endpoints and deciding how to open that data from the time the feature / product is build and not something to figure out later, making it more secure. 

Im curious to know if there are some others already looking at it and share their ideas, opinions or anything.

-------------------------

hankthebldr | 2021-07-04 06:55:47 UTC | #3

The first rule about being a doctor, is that you're gonna have to touch some dead bodies. Most breaches are caused by human error, so ask yourself - how can you limit the human while still providing a service?

Data stewardship is a very critical question, who the is steering the ship  (outside of Gitcoin) now. Outside of education, the best way to keep users data safe is implementing a source based solution, where the transaction network plausibly would be separated from any PII or data that could assume a level decent criticality of risk.  Think about a bilateral service call, ie ack or etb that would set the parameters for the transactions on a multiplexed protocol i.e node peer status on one, however transactions on another 

For Gitcoin

First step is to acknowledge that its a asymmetric game, P2P will be dependent on some type of connection protocol whether its based in TCIP/FIPS/TLS/or other state-full/stateless connections there is always a risk of packet forensics, and data capture. Using UEM, ifconfig, sep, any derrivative from the pcap library you can build a forensic profile on the source to source, or per to per relationship of of anyone supporting a future distributed node. 

Also, you're going to have to accept the same responsibility any enterprise IT organization does, you're gonna have admin that will know all data but he'll be able to capture critical data in a KV store and use hashi/vault protect the data, and able to provide automated re-cription if bad node is recognized by the peer, hashi/vault 

Normally when large orgs are gong for PCI, SOX, HIPPA, HITRust Compliances a game of streaming the data to the coldest S3 bucket and checking a box. Decentralizing doesn't assume the same WAN/LAN dynamics that most organizations are health with --- meaning there can be a a replicated, hidden data repository on the host node. This would be similar to a netboot, where part of the disk is formatted in an away that unacceable to the core node it bloomed. i.e move and alias the file. 

Implement staff IAM/Least Privledge User and internal integrity checks. 
long story short 
1.identify and tag each type of data associated with a peer, and transaction state (create internal self generated handshake token to pass coin to wallet account in segregated volume)
2. Create local and global controls  1. use non traditional id signing or external keygen site thats Gitcoin managed 2. create separation layers between the data link and network transport that omits, or encrypts PII with tools like hashi vault etc, this might be done through some of the allied projects regarding identity ownership. 


I think that we've all realized that data is the one thing that is only becoming more abundant, but as a network operator that can provide services and public goods, ask yourself - do you worry about data stewardship when using cash? `I think that would be the ideal to strive for

Dont collect data than you need. Dont provide any data that would hurt you, set up robust automation if the shit hits the fan.

-------------------------
