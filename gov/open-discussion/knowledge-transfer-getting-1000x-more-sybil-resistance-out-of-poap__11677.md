---
id: 11677
title: "Knowledge Transfer: Getting 1000x more sybil resistance out of POAP"
slug: knowledge-transfer-getting-1000x-more-sybil-resistance-out-of-poap
category: open-discussion
url: https://gov.gitcoin.co/t/knowledge-transfer-getting-1000x-more-sybil-resistance-out-of-poap/11677
created_at: 2022-10-18T14:57:03.181Z
last_posted_at: 2023-05-05T03:54:35.848Z
posts_count: 17
views: 4177
like_count: 29
---

# Knowledge Transfer: Getting 1000x more sybil resistance out of POAP

<https://gov.gitcoin.co/t/knowledge-transfer-getting-1000x-more-sybil-resistance-out-of-poap/11677>
owocki | 2022-10-18 14:57:03 UTC | #1

# Post TLDR

1. there is 1000x more sybil resistance available from POAP than the Gitcoin Passport is currently consuming.
2. there is a data intelligence problem of "how much is each POAP worth?".
3. there may be decentralized ways to solve the problem.

# Post Body

Gitcoin Passport uses (among other things) [POAP](https://poap.xyz/) for sybil resistance.  This is what the stamp looks like:

![Screen Shot 2022-10-18 at 8.14.57 AM|417x500, 75%](upload://qamJKLOsoxxQga3f1UAo1aKk0iB.png)

As you can see, you get the POAP stamp if you "Connect an account to a PoAP owned for over 15 days."

I was having a conversation with Patricio Worthalter about the stamp at Devcon, and we both agreed there was 1000x more sybil resistance that could be gotten out of POAP than what Passport currently does.   

I've actually had this same conversation with a few different Gitcoiners over the last several months, and so I'm writing up this post to detail it.

The objective of this post is to detail the diversity of POAPs and to talk about how the sybil resistance from that diversity of POAPs might be tapped.

There are 10000s of different POAPs out there.   This screencap from https://poap.delivery/ shows the diversity of the POAPS out there.

![Screen Shot 2022-10-18 at 8.23.56 AM|491x500](upload://hTlDjvQTBlvuPq3Slt263J5IWq2.jpeg)

Each of these POAPs can have between 0 and 1000s of collectors.  
Each of these POAPs can be a sybil resistance signal on Passport, though some may be stronger than others.  For example a publicly available POAP likely only creates a sybil resistance of about $0.01 (because the cost of forgery is low), whereas a "I met owocki.eth at Devcon 2022" POAP is likely worth much more in terms of sybil resistance (because the cost of forgery is high).

What would have to be true for Passport to process the diversity and plurality of POAPs out there + to reward sybil resistance of each of these POAPs, instead of just one small criteria of "owned a POAP for more than 15 days"?

GitcoinDAO would need to categorize the POAPS + figure out the sybil resistance each POAP confers, and then find a way of loading all of that sybil resistance into the passport.  This is a huge data + governance challenge (and perhaps a UI challenge too) .

A naive way of solving this problem might be to hire someone to catalogue all of the POAPs + reward them with sybil resistance scores.  But that person would surely have a very large backlog to work through, and there would be a non-negligible cost to keeping that person on staff.  And one person only has a limited vantage point on the problem.

A more decentralized and scalable way of solving this problem might be to push the problem out to the edges of the network.  What if there was a dapp that allowed people to do [conviction voting](https://gov.gitcoin.co/t/gtc-conviction-voting-dapp-network-utility/10523) on the POAPs.  eg when someone stakes GTC on a POAP, then that increases the sybil resistence that that POAP grants to the system.  Then this problem of "how does the DAO categorize the POAPs?" becomes a giant collective intelligence problem which the market can solve.

Thanks for reading to the end.  If you made it this far, you now see see that 
1. there is 1000x more sybil resistance available from POAP than the Gitcoin Passport is currently consuming.
2. there is a data intelligence problem of "how much is each POAP worth?".
3. there may be decentralized ways to solve the problem.

Thanks for reading this knowledge transfer post.

-------------------------

Anthony | 2022-10-18 20:23:37 UTC | #2

Hey Owocki, 

I completely agree that POAP's can be great for sybil resistance but there is an open problem of quantifying how much weight each POAP holds.

**Short Term Fun, Unscalable**

An interesting short term solution would be to fund a small bounty(s) for someone to gather a ~top 100 list of Sybil resistant POAPs. It could be anchored around a few data points (collector base, size, historical significance, etc) but focusing on the quality of distribution is the most important.

Examples of POAPs that could be included may be:
- You Met Me POAPs from Patricio
- Schelling Point POAPs
- rAAVE POAPs
- ETHGlobal Builder POAPs (distributed to builders at events)
- Ethereum Foundation POAPs (DevConnect)
- and the entire gambit of Ethereum core events (ETH Denver, DappCon, ETH Berlin, ETH CC, etc)

There are random goodies that exist that are not known to most but a good analyst can find, like the [AAVE V2 Pioneers POAP.](https://poap.gallery/event/566)

The POAP Community Call has a small treasury and I would assume they would be willing to throw into this bounty as well.

**Mid Term Solution, More Scalable**

Zooming out, it's easy to see that this isn't very scalable and feels more like a fun POC for learnings. 

I like your idea of having some sort of stake-weighted-voting mechanism to measure conviction, there could be interesting dynamics as well if not only GTC could be staked but some of those "top 100" POAPs as well. One may assume that those collectors may be more philosophically aligned with what we are trying to achieve here and may have quality input into the conviction voting system.

-------------------------

dghelm | 2022-10-18 20:42:52 UTC | #3

This is a really interesting idea. A minor concern I have is about how trivial it is to transfer a POAP. Most of the other passport mechanisms aren't easy to spread across multiple accounts, and I'd expect we could see a market created around bad actors paying for POAPs if their sybil resistance signal was weighted too heavily.

Perhaps one mechanism would be to diminish the value of a POAP that has been transferred from its initial owner.

-------------------------

zeroknowledge | 2022-10-19 09:30:39 UTC | #4

I think if POAP differentiates IRL POAPs(e.g: İ met worthalter at devcon) vs POAPs distributed online, we could have a solid foundation for sybil resistance. IRL POAPs could also be made non-transferrable so they keep their anti-sybil properties. 

A good starting point for online POAPs would be imo either verified communities (e.g: Rocketpool, POAP) and whitelists submitted by community leaders attesting to users or the fair distribution of POAPs.

Another idea is having a dedicated forum and voting process with verified POAP holders and community members attesting to the legitimacy and anti-sybil properties of new POAPs.

-------------------------

owocki | 2022-10-19 13:45:05 UTC | #5

[quote="dghelm, post:3, topic:11677"]
. A minor concern I have is about how trivial it is to transfer a POAP.
[/quote]

This is a great point.  Perhaps only a POAP that hasn't been transfered and remains at its "origin" should count towards a personhood score.

-------------------------

whiskey | 2022-10-19 19:50:18 UTC | #6

AGREED , I think GitPOAPs (decentralized reputation platform that represents off-chain accomplishments and contributions on chain as POAPs ) are great choice to assign high weight sybil resistant points . Protocols and dapps distribute this kind of POAPs with extra care (as @Anthony  mentioned the quality of distribution is the most important ), so they are farmed way less .

-------------------------

1chioku | 2022-10-20 09:28:42 UTC | #7

I had had an extensive discussion with other data analysts at Berlin in September on POAPs, and yes fundamentally the metadata they contain can be used to build a better identity, especially for anons who collect POAPs but are allergic to centralised KYC like gitcoin passport.

However the current weakness of POAPs is on the technical implementation: they use a QR code or an NFC to open a URL which from a malicious point of view can be used to create artificial identities, i.e I could be in a group that shares POAP urls from events and keep accumulating those on sybil wallets.

POAPs can only become 100% reliable if there is a physical device with geolocation signing capabilities that only issues the POAP  to the POAP seeker that has the private key is physically near the POAP issuing machine.

It's Pokemon Go all over.

-------------------------

owocki | 2022-10-20 13:39:30 UTC | #8

[quote="1chioku, post:7, topic:11677"]
centralised KYC like gitcoin passport.
[/quote]

passport is decentralized and doesnt use KYC.  

if you are interested in doing a little research => docs.passport.gitcoin.co

-------------------------

1chioku | 2022-10-20 14:59:59 UTC | #9

My bad, went through too many SSOs :sweat_smile:

-------------------------

neo | 2022-10-20 18:39:59 UTC | #10

This idea is interesting and attractive and I agree with this idea and support it. We see the events of Sybil every day. It is a good thing with this move.

-------------------------

torlak78 | 2022-10-20 18:40:07 UTC | #11

Hello owocki
I agree with most of what you wrote. Yes, the poap criterion set for sybil is very ordinary. More serious steps can be taken. First of all, I would like to express some of my concerns.
1) Scoring a particular group of poap increases that poap's floor price in the market.
2) Not everyone has a chance to participate in events like Devcon. There is inequality here.
3) Certain projects have their poap mint their poap in return for paying a certain fee. If the score of this type and similar projects is high, the prices requested from us will increase. Many projects that see this will switch to similar practice. Also, the poap team does not approve of poap's trade and says it is against the spirit of poap, I agree. However, the fact that the projects make poap mint at a certain price will unfortunately bring the poap trade to the legal ground. This is a big risk.
4) Not everyone can afford to pay for the poap, which may lead to unfair competition.
5) Every poap's lover is different. Some are programmers, hackhatlon collects poap, some art lovers collect art poap. Therefore, how will the poap scores be determined here?
My suggestion
1) Poaps should be classified (such as art-software-entertainment-defi-culture). Each title can be rated in itself.
2) Ens requirement can be introduced for one-time or subsequent poap mints. An application like Devcon. (Having a person's ens domain name on the poap can be considered a condition for sybil. Also, I think that type of poaps will not be traded.
3)Poap period may be spread over a long period of time such as 3-6 months, not 15 days.
4) Minimum poap requirement may be introduced.
5) Like the requirement to participate in a minimum of 5 events of any project (5 poaps)

Thank you

-------------------------

omahs | 2022-10-21 11:02:28 UTC | #12

Hey everyone,

That's an interesting topic, I'm looking forward to seeing POAPs being used for sybil resistance.

Here are a few things that could be used in a scoring algorithm:

**Frequency:** Less chances of sybil accounts if user attended POAPs events over a long period of time 

**Uniqueness:** Let's say someone owns 100 POAPs and those were not bought. There could be a *POAPs-in-common* comparison. If the closest match is 50 POAPs in common, that user would have an extremely high chance of being unique. If 5000 other accounts own the same set of POAPs it has more chances of being a sybil.

**Old POAPs:** In my opinion POAP farming wasn't very common before summer 2021, old POAPs could have a bonus

Other things:

POAPs have an ID, number indicating which one was claimed first for a specific event. From my observation, POAP #1/670 has a much higher chance of being a unique account than #652/670. Usually #1 and other low numbers are claimed by the event organiser and other people very involved. POAP #652 might be someone who shared a secret word somewhere.

Most farmed and heavily traded POAPs are speculation about future airdrops (Metamask, Zksync…)

It would be interesting to see how many POAPs are actually transferred after being claimed. I believe it's a minority.

I agree with @torlak78 about the downside of choosing only POAPs related to real-life ETH events. The scope of POAP events is very large and it would be good to be inclusive.

-------------------------

torlak78 | 2022-10-21 11:46:52 UTC | #13

If the ceramic API problem is fixed it will be awesome :roll_eyes:

-------------------------

PaigeDAO | 2022-10-22 11:27:30 UTC | #14

Good point. And good reply. 
Raises the question of could SBTs be used like you are talking about POAPs?
If not instead of, then in addition to?

-------------------------

PaigeDAO | 2022-10-22 11:29:24 UTC | #15

Also, what about GR past participation POAPs that have remained in original claimant's wallet?  Could this act as a 'gold standard' POAP? :dizzy:

-------------------------

SkyDAO | 2022-10-25 19:48:48 UTC | #16

[quote="omahs, post:12, topic:11677"]
It would be interesting to see how many POAPs are actually transferred after being claimed. I believe it’s a minority.
[/quote]

a quick look:

600k have been transferred on top of the claimed txns out of 5.7m POAPs, so ~10%...a minority but more than you might have guessed!

Won't let me embed a picture or URL!

Not a URL: https:// gnosisscan .io /token/0x22c1f6050e56d2876009903609a2cc3fef83b415

-------------------------

Rahul123458 | 2023-05-05 03:54:35 UTC | #17

This ia a good idea beacuse you need to badge🥳🥳🥳

-------------------------
