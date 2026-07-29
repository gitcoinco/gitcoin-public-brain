---
id: 16683
title: "Incident Regarding Mistransferred Treasury Funds"
slug: incident-regarding-mistransferred-treasury-funds
category: newscommunity
url: https://gov.gitcoin.co/t/incident-regarding-mistransferred-treasury-funds/16683
created_at: 2023-10-05T18:37:15.209Z
last_posted_at: 2023-10-19T15:07:27.758Z
posts_count: 30
views: 9930
like_count: 96
---

# Incident Regarding Mistransferred Treasury Funds

<https://gov.gitcoin.co/t/incident-regarding-mistransferred-treasury-funds/16683>
CoachJonathan | 2023-10-05 18:37:15 UTC | #1

This post is to inform the Gitcoin ecosystem about an incident of misdirected funds in relation to this Tally proposal: https://www.tally.xyz/gov/gitcoin/proposal/108857091257155353415608123635307134327397364492395330571315789161941080916144

The transfer intended for the MMM’s S19 budget did not land in its multisig, and instead was sent to a GTC token contract. This has rendered the funds stuck in the contract, with no way of recovering them.

Below I outline all the facts about what happened, the timeline of events and steps we are putting in place to ensure that a mistake like this does not happen again.

## Relevant Data

* Total amount transferred: 521.44K GTC
* Sent to GTC token contract: 0xde30da39c46104798bb5aa3fe8b9e0e1f348163f
* Proposal was created by Laura (MMM Workstream Lead)
* Large token holders who signed off on the proposal include:
  * Kyle (ED of the Foundation)
  * Meg (Grants Stack WS Lead)
  * Jeremy (Passport WS Lead)
  * Carl (Steward Council member)
  * Myself (MMM co-lead)

## Timeline

* Tuesday Sept 19 17:16 - Proposal published onchain
* Thursday Sept 21 13:24 - Voting period started
  * Sept 22 - Carl, CoachJ, Jeremy votes
  * Sept 25 - Laura and Kyle vote (quorum is now met)
  * Sept 27 - Meg votes
* Wednesday Sept 27 04:54 - Voting period ended
* Saturday Sept 30 00:16 - Proposal executed
* Sunday Oct 1 evening CET - CoachJ informed that funds have not yet landed in MMM’s multisig
* Monday Oct 2 morning CET - CoachJ connects with Aditya (core dev on Allo) to explore whether the contract has a withdraw function and/or is upgradable
  * Aditya says no, and to double check with the contract owner to make sure
* Monday Oct 2 6pm CET - CoachJ connects with Kyle to explain the situation and see if the funds are recoverable
  * Kyle says it is unlikely, but will do some digging to see if it is possible
* Thursday Oct 5 - CoachJ confirms with Kyle that the funds are not recoverable
* Thursday Oct 5 - CoachJ informs CSDO of the incident

## Next steps

The intention of these steps are to:

1. Create safeguards to ensure something like this never happens again
2. Create clearer accountability if there is an incident like this again

Action items:

* All proposals in Snapshot moving forward should have wallet addresses listed if there will be any transfers of funds
* All proposals in Tally moving forward should have wallet addresses listed if there will be any transfers of funds
  * It is up to the Tally proposal creator to ensure that the funds are being transferred to the correct address based on the Snapshot description
  * It is up to Tally voters to ensure that the funds are being transferred to the correct address based on the Tally description
* CSDO is going to explore the possibility of implementing a DAO Guardians program
  * DAO Guardians would be individuals contracted to review proposals and ensure their accuracy, particularly around proposals and large transactions
* We’ve been in contact with the team at Tally who have graciously accepted some feedback requests that they will look to include in their roadmaps, including:
  * If the destination address is not a DAO multisig within our DAO admin address book, a warning will come up and confirm they still want to use the address
  * If an admin has an address labeled, then everyone can see that label (not just the admin) - this way anyone voting will have a better visual cue

*Note: Though the Tally team was very receptive to our feedback and is keen to work with us in the future to prevent something like this from happening again, it is important to note that the root cause of this incident was due to human error, not issues with the Tally platform.*

## Conclusion

It is unfortunate that this incident occurred and I want to apologize on behalf of myself and others involved in this having happened. I am also confident that the steps being put into place will create more safeguards and clear accountability should a situation like this happen again.

Large token holders and multisig signers have a responsibility to be extra diligent when it comes to handling funds that do not belong to them (myself included). Unfortunate as this incident was, I hope it can serve as (yet another) lesson for many of us.

If you have any feedback, concerns or suggestions on other safeguards we can put in place, please leave a comment below.

-------------------------

essemharris | 2023-10-05 18:59:37 UTC | #2

Just for clarification's sake, this post is meant to inform that roughly $464K USD from the Gitcoin treasury was lost and is unrecoverable?

-------------------------

CoachJonathan | 2023-10-05 21:01:44 UTC | #3

Yes @essemharris that is correct.

-------------------------

umarkhaneth | 2023-10-05 22:42:46 UTC | #4

[quote="essemharris, post:2, topic:16683, full:true"]
Just for clarification’s sake, this post is meant to inform that roughly $464K USD from the Gitcoin treasury was lost and is unrecoverable?
[/quote]

IMO bc the gitcoin treasury is the largest holder of GTC this is more likely to be a permanent reduction in the supply of available GTC than a loss of the DAO's $USD. Already, we have to be careful with the rate at which we convert GTC into USD because of the downward price pressure. If we are ever in a situation where we have to turn our last 500k GTC into USD then that would be the real issue. 

The process improvements that can be made from learning from this incident are so important.

-------------------------

owocki | 2023-10-09 01:56:42 UTC | #5

obviously saddened this happened, but thankful its only a small portion of funds relative to the total treasury. i hope we learn something from this.

> IMO bc the gitcoin treasury is the largest holder of GTC this is more likely to be a permanent reduction in the supply of available GTC than a loss of the DAO’s $USD.

ill be curious if this narrative of "its actually GTC burned" is seen as legitimate.

>  If we are ever in a situation where we have to turn our last 500k GTC into USD then that would be the real issue.

FYI the token supply is 100m GTC right now, but CAN be inflated UP TO 2% per year by the governance process calling the [mint()](https://etherscan.io/address/0xde30da39c46104798bb5aa3fe8b9e0e1f348163f#writeContract) function of the GTC smart contract.  (But the DAO has never done this)  Nor am I advocating for that at this time, I'm only noting it is an option baked into the GTC smart contract.

-------------------------

connor | 2023-10-06 00:58:38 UTC | #6

Thank you for the transparency here. I am extremely sorry for all parties directly affected at no fault of their own. This is a shitty situation all around :( 

[quote="CoachJonathan, post:1, topic:16683"]
All proposals in Tally moving forward should have wallet addresses listed if there will be any transfers of funds

* It is up to the Tally proposal creator to ensure that the funds are being transferred to the correct address based on the Snapshot description
* It is up to Tally voters to ensure that the **funds are being transferred to the correct address based on the Tally description**
[/quote]

I agree it should be made extremely clear and redundant where transfers are going. But as laid out, this action item could be even more dangerous. The transaction details and destination address are already laid out front and center, even before the actual description:
![Screenshot 2023-10-05 at 5.49.43 PM|690x473](upload://7XoISRlF6j9pCdlvehpf5kNk2D.jpeg)
Asking voters to verify the address in the description opens the possibility for a malicious actor to put the correct address in the description while the on chain action sends somewhere else (not saying this is likely just thinking out loud).

[quote="CoachJonathan, post:1, topic:16683"]
CSDO is going to explore the possibility of implementing a DAO Guardians program

* DAO Guardians would be individuals contracted to review proposals and ensure their accuracy, particularly around proposals and large transactions
[/quote]

All large delegates and Tally voters should be DAO Guardians, we don't need a new special program or to contract anyone for this imo. Obviously, we all screwed up here to let this slip though, but hopefully that's a huge wake up call to all delegates that they should be a DAO Guardian and need to do light due diligence on what they vote on.

[quote="owocki, post:5, topic:16683"]
ill be curious if this narrative of “its actually GTC burned” is seen as legitimate.
[/quote]
This is certainly not a net positive situation for the DAO, but I think objectively these 500k GTC (.8% of the circulating supply) are stuck forever and burned.

-------------------------

DistributedDoge | 2023-10-06 03:50:59 UTC | #7

To see organization waste funds in such reckless manner is disappointing.

I don't care much for "burned/locked" narrative but I am concerned how multiple high-profile DAO individuals misallocated 450k which could have been avoided if even a single person exercised *baseline level of due diligence*.

I think a short checklist could help Tally voters to follow the motions of validating common budgets proposals without omitting steps or having to think too much about the process. At the minimum:

- confirm recipient address is known & labeled
- confirm correct token is being sent
- check token amount 
- check `executable code` matches written `description`

Then you can go in more detail like "Confirm I am NOT sending token DIRECTLY to BRIDGE/TOKENADDRESS where it will get STUCK (again)"

-------------------------

jengajojo | 2023-10-06 09:29:00 UTC | #8

Sorry to hear about this and thank you for the transparency. @Viriya will MMM be able to function as budgeted given this development?

-------------------------

CoachJonathan | 2023-10-06 09:50:12 UTC | #9

In short @jengajojo, no.

These funds were supposed to provide the MMM workstream with funding for August, September and October.

MMM was able to use funds from S18 (May-July) to pay all its contributors and opex in August. However, MMM has insufficient funds to pay contributors and opex costs for September and October.

We will be re-requesting budget for the two months (a reduced amount, not for the original request of around $500k).

I just posted the new request to Tally here: https://www.tally.xyz/gov/gitcoin/proposal/83370444265186051506036240751499191729551923064564972278212022875236597720544

-------------------------

pinakion | 2023-10-06 18:30:27 UTC | #10

Should have used Kleros! Maybe next time? :wink:

-------------------------

rsolari | 2023-10-07 01:42:20 UTC | #11

Hi, Raf from Tally here. I'm really sorry to hear that this happened.

We know that proposals have high stakes, so we're adding more safety checks for both proposal creators and voters. We're talking with some of the leads and stewards about how we can help prevent this kind of thing from happening in the future. They've already suggested some great ideas as part of the post-mortem for this incident.

Today, we added a warning to the Create Proposal tool when sending funds to a token contract. "This is a token address, and in most cases is not recommended. Please make sure this is the intended address"

Proposal safety is a key pillar of our product, so we'll be rolling out more improvements to proposal drafts, simulations and safety checks over the next few months. I'm especially keen for feedback from you all. My goal is to make sure that creating and voting on these high-stakes proposals is both easy and safe!

Feel free to reach out if you have suggestions or would like to preview some of our UX ideas.

-------------------------

lefterisjp | 2023-10-07 12:43:54 UTC | #12

I am really sad to see this happen. Signers/voters should triple check arguments and try to simulate all transactions to see they do what they were intended to do.

Safe's UI is integrating Tenderly simulations for exactly this reason. Could it be that this can also be integrated in the voting process with Tally?

But really sending to own token contract is really easy to spot even in Tally's interface. I just looked at the UI.

![2023-10-07_10-41|690x427](upload://3zYJ621Qaj6uo2cFhFkCBAVTKHY.png)


Edit: To be clear, I am not taking the shitty view that I would have seen this if I was still participating in governance. I can very well imagine situations where it's late, you are confused or tired and just press sign/vote.

Just sad to see that not one person noticed it before it was too late. I mean come on guys 136 people made an on-chain transaction spending their own ETH in gas to vote for such a mistake without even bothering to check what it is they are spending the ETH for.

![2023-10-07_14-43|292x151](upload://wklikxSJV0WPu1890DyTCX0biI.png)

-------------------------

ccerv1 | 2023-10-07 12:58:55 UTC | #13

Extremely sorry to learn about this incident. And, as a delegate who voted on the proposal, I'm especially disappointed and frustrated. 

IMO, I don't think delegates have the mindset that they should be checking executable code. I also don't think they have the mindset that they should confirm other particulars, eg, that the transfer amounts match the original budget proposals, that the Snapshot vote was approved with quorum, etc.

While it's great that any delegate or interested member from the community can easily check these things on Tally, we should also have a checklist that someone other than the proposer can use to verify the proposal. For example:

* Proposer is in good standing with the DAO / address has not been hacked
* Proposal has been approved on Snapshot
* Amount of tokens and exchange rate is correct
* Recipient address is correct

I'm happy to see Tally responding quickly with a UI improvement. I could also imagine Tally giving DAOs an address whitelisting / labeling feature to give users more confidence that the address the proposal is interacting with is the correct one.

That said, I would also like to see the DAO implement its own "social ware" upgrade in light of this event.

-------------------------

lefterisjp | 2023-10-07 13:11:49 UTC | #14

Absolutely. A checklist and people checking that the advertised function is what the actual call data do is a must.

In my opinion we should educate governance voters that they are in essence multisig signers for such transactions. It's their responsibility to check the call data. Perhaps this is not widely understood and needs to be explained.

On a more personal note this is not an individual failure, but a collective governance failure. Don't feel bad about this. **Neither you nor the other votes or the proposer are solely responsible for what happened.**

Individual people can and do make mistakes. The collective as a whole should check for them and mitigate them. This is what failed and did not happen here.

-------------------------

thedevanshmehta | 2023-10-08 10:43:03 UTC | #17

[quote="owocki, post:5, topic:16683"]
ill be curious if this narrative of “its actually GTC burned” is seen as legitimate.
[/quote]

i did post this on twitter and there were some sympathetic views towards this perspective.

![Screenshot 2023-10-08 at 4.08.03 PM|690x190](upload://8fqlFfZDArb5YduEqdUszCr2U80.png)

Really drives home the importance of paying workstreams in your native token! this mishap would have been much much worse had it been in stables or eth

[quote="CoachJonathan, post:9, topic:16683"]
We will be re-requesting budget for the two months (a reduced amount, not for the original request of around $500k).
[/quote]

Will the reduced amount negatively affect the workstream ? I wouldn't want them penalized for no fault of theirs. 

[quote="CoachJonathan, post:9, topic:16683"]
I just posted the new request to Tally here
[/quote]

Ideally it would have been nice to have a snapshot vote before the tally vote, with the options of keeping the same budget, increasing it or reducing it  (with the multi-sig signers involved abstaining from the vote)

-------------------------

FractalVisions | 2023-10-08 18:49:14 UTC | #18

Still trying to grok how this much funding was fumbled after all the years of experience between the members who were involved with the transfer.

Even if a test transaction was sent separately from a personal wallet with funds out of their own pockets it could have prevented this from happening.

I see that a test transaction is not the best way to approach voting 🗳️ mechanisms but still think that the method to send a small test transaction of $1 would be helpful regardless.

Perhaps there is a way to implement this into the procedure because a small transaction of this nature could have easily saved a half a million dollars. I am imagining the community is at a loss of words as we were until now. 

The potential that this funding could have brought to the grant ecosystem is now lost for those who have been grinding day in and out to improve the Gitcoin platform. A major setback in the world of public goods. 

To those who were involved with the transaction make sure to keep your chin up!

We are all rooting for you & hope that this learning lesson will improve the quality control happening during a transfer for a large sum of capital.

-------------------------

carlosjmelgar | 2023-10-08 19:36:57 UTC | #19

It's unfortunate to see a workstream's budget disappear this way. I'm relieved that the community and contributors are being so forgiving in light of this incident. 

The Tally team are the heroes we don't deserve in all of this. They [delivered a great update](https://twitter.com/tallyxyz/status/1710696489297617067) as a response to this mishap. It's great seeing team's react so swiftly to community reports. 

**Where's the learning opportunity here?**
Should we be incentivizing/ rewarding delegate participation? Instead of creating another internally appointed mini workstream? 

[quote="CoachJonathan, post:1, topic:16683"]
CSDO is going to explore the possibility of implementing a DAO Guardians program

* DAO Guardians would be individuals contracted to review proposals and ensure their accuracy, particularly around proposals and large transactions
[/quote]
I'd love to explore delegate rewards, which could encourage more community participation and create an opportunity for them to earn GTC for their work in governance. Creating an internal DAO Guardians Program sounds like the DAO appointing more insiders and paying them for work we should have all been already been doing more of as contributors. Interested in governerds like @jengajojo @FractalVisions @CryptoReuMD @lefterisjp to offer their insights on this.

-------------------------

FractalVisions | 2023-10-08 21:58:25 UTC | #20

I like the idea of creating an attestation dashboard for the checks & balances to sign on chain prior to sending the main Tx from the vote. 🗳️ 

Anyone could participate in these attestation check in events to get the full community participation of GTC holders or stakers to further decentralize the process.

Even a token of appreciation like the Kudos was a nice touch at the end of an educational quest on Gitcoin. The learning aspect of the platform was something that I was heavily drawn to in the past. That is one thing that would be really amazing to see implemented into the UI somehow down the road. 
Maybe 🤔 even refurbished kudos on PGN or other L2 options that align with the ecosystem such as Optimism.

I will just use what was mentioned above ⬆️ from @DistributedDoge ! 🐕

[quote="DistributedDoge, post:7, topic:16683"]
I think a short checklist could help Tally voters to follow the motions of validating common budgets proposals without omitting steps or having to think too much about the process. At the minimum:

* confirm recipient address is known & labeled
* confirm correct token is being sent
* check token amount
* check `executable code` matches written `description`
[/quote]

-------------------------

jengajojo | 2023-10-09 08:32:08 UTC | #21

[quote="carlosjmelgar, post:19, topic:16683"]
I’d love to explore delegate rewards, which could encourage more community participation and create an opportunity for them to earn GTC for their work in governance.
[/quote]
I second this and is absolutely necessary from a decentralisation pov! For the actual implementation, while I have designed and delivered many delegates programs myself, for gitcoin we can perhaps start with a 'Delegates QF Round' each quarter or so and iterate from there? What do you think @CoachJonathan ?

-------------------------

CoachJonathan | 2023-10-09 10:45:01 UTC | #22

I'd love to see this. I'm adding this to the roadmap, hoping we can tackle this in S20 (starting next month) or S21 at the latest.

-------------------------

Jimi | 2023-10-09 18:32:05 UTC | #23

Sorry to hear about this!

How do you all feel about doing test transactions for anything above a certain amount? 

Obviously it's a balance between this not slowing down ops too much & securely avoiding situations like this. 

What do you think the number would be that enables a nice balance between those things? 50K? 100K?

-------------------------

CryptoReuMD | 2023-10-10 14:16:48 UTC | #24

Yes my friend. I'm fully engaged with the team that it's been growing for the good of the community. With a very aligned and ethical responsabilities as far as i can say and i know from all the tagged ones in this post. 
I'd love to work with an internal workforce could be great, and a big opportunity to learn and discuss about what it's the best for the different communities. As we can see in L2Beat for the pie that its being very popular we can have a spider web graphic with eight different values and align the projects inside.

-------------------------

connor | 2023-10-11 10:00:36 UTC | #25

[quote="CoachJonathan, post:9, topic:16683"]
I just posted the new request to Tally here: [Tally | Gitcoin Proposal ](https://www.tally.xyz/gov/gitcoin/proposal/83370444265186051506036240751499191729551923064564972278212022875236597720544)
[/quote]

This may not be the ideal place to share this but I'm not aware of discussion on this vote happening anywhere else, so posting here. I voted "Against" on this proposal - some people have reached out privately to learn why, so to be transparent I'll also post in public.

First off, let me say I absolutely think we need to find a way to keep the MMM team compensated for both past and future work, I don't want to see the workstream stuck with $0 for the season, and regardless of my vote I'm confident the proposal will pass given it's basically at quorum already.

But I voted against it for a few reasons:
- There hasn't really been any actual discussion (in public or that I've seen) about the issue, how to resolve it (financially) and the next steps, it was "hey this big mistake happened" and then "Here's a new budget request". The proposal says MMM "will be staggering their budget request from the rest of Gitcoin" going forward - what are the financial and operational implications of this?
- I don't feel like any real ownership has been taken over the mistake (and I don't think it's Tally's fault) 
- I am still a bit unsettled about the $100k+ sent from the CSDO multisig to MMM of which there still hasn't been any acknowledgment of it, unclear whether that was free gift or if it's supposed to be paid back by this budget, if that will happen again, etc
- IMO some key stakeholders should probably abstain from voting on this

But **most importantly** with so little discussion or debate, does this go and set the precedent that any time in the future funds are lost, workstreams can just turn around and request more and expect to get it?

I hesitated to vote no outright because i knew it would ruffle some feathers, but frankly, it looks pretty clear this is going to pass regardless so it's more of an ideological pushback. I <3 the MMM team and want the DAO to support you all but I also would like more transparency, accountability, and to establish clear processes.

[quote="thedevanshmehta, post:17, topic:16683"]
Will the reduced amount negatively affect the workstream ? I wouldn’t want them penalized for no fault of theirs.
[/quote]
+1 need more info on workstream impact, new budget items, other funding sources in the interim (csdo) etc

[quote="thedevanshmehta, post:17, topic:16683"]
Ideally it would have been nice to have a snapshot vote before the tally vote, with the options of keeping the same budget, increasing it or reducing it (with the multi-sig signers involved abstaining from the vote)
[/quote]
+100

-------------------------

CoachJonathan | 2023-10-11 11:16:17 UTC | #26

[quote="thedevanshmehta, post:17, topic:16683"]
Will the reduced amount negatively affect the workstream ? I wouldn’t want them penalized for no fault of theirs.
[/quote]

No, this should not negatively impact the workstream. Because of how MMM operates, MMM often ends up with a large surplus at the end of each season. Looking ahead, it is fairly easy to estimate that MMM will come under the amount that they've requested, hence the lower budget request.

[quote="thedevanshmehta, post:17, topic:16683"]
Ideally it would have been nice to have a snapshot vote before the tally vote, with the options of keeping the same budget, increasing it or reducing it (with the multi-sig signers involved abstaining from the vote)
[/quote]

I think this is worth a larger discussion on how to treat situations like this. Technically [a Snapshot vote was done to guarantee these funds,](https://snapshot.org/#/gitcoindao.eth/proposal/0xc8cea5df7b14e71ec91aa307837e1e86f7cd285a5037a517daac29e45e34bb2d) and now we had this situation + MMM is requesting a reduced amount that still will get them to the end of the season.

Maybe to move this conversation forward - what do you think are the pros/cons of running another Snapshot vote? What is the intention of doing that and what outcome are we hoping to achieve? Maybe let's start there and we can get to the bottom of some sort of procedure we can put in place (and [codified in our governance manual](https://gitcoin-1.gitbook.io/gitcoin-governance-manual/) that I shared in a separate post).

-------------------------

CoachJonathan | 2023-10-11 11:25:49 UTC | #27

Appreciate the thoughtful post, Connor. Would love to address a few of your comments and use your post to springboard the discussion that you're seeing has been missing.

[quote="connor, post:25, topic:16683"]
There hasn’t really been any actual discussion (in public or that I’ve seen) about the issue, how to resolve it (financially) and the next steps, it was “hey this big mistake happened” and then “Here’s a new budget request”. The proposal says MMM “will be staggering their budget request from the rest of Gitcoin” going forward - what are the financial and operational implications of this?
[/quote]

I think what would be helpful here is an actual discussion starter, maybe:
- Some questions to get us started pondering how to handle future situations like this
- A strawman for others to comment on and eventually arrive at a satisfactory conclusion

This would be super helpful to advancing the conversation.

[quote="connor, post:25, topic:16683"]
The proposal says MMM “will be staggering their budget request from the rest of Gitcoin” going forward
[/quote]
I wouldn't worry too much about this comment - this is almost a sidebar convo and Laura will be posting about this in the coming days to explain why MMM's budget is not going up at the same time as everyone else's.

[quote="connor, post:25, topic:16683"]
* I don’t feel like any real ownership has been taken over the mistake (and I don’t think it’s Tally’s fault)
[/quote]
What would have you feel like "real ownership" has been taken? Are there any specific actions you'd like to see?

[quote="connor, post:25, topic:16683"]
I am still a bit unsettled about the $100k+ sent from the CSDO multisig to MMM of which there still hasn’t been any acknowledgment of it, unclear whether that was free gift or if it’s supposed to be paid back by this budget, if that will happen again, etc
[/quote]
Apologies for not acknowledging this in the gov forum and only discussing this in CSDO channels. Funds were borrowed from the CSDO multisig in order to be able to pay contributors at the end of the month. 

As soon as MMM receives funds for work completed in September, the full amount will be sent back to the CSDO multisig. @Sov had already flagged this and we will be creating new procedures around the use of the CSDO multisig moving forward to ensure transparency (that will ultimately be documented in the [Governance Manual](https://gitcoin-1.gitbook.io/gitcoin-governance-manual/).

[quote="connor, post:25, topic:16683"]
But **most importantly** with so little discussion or debate, does this go and set the precedent that any time in the future funds are lost, workstreams can just turn around and request more and expect to get it?
[/quote]
Would love your support on leading this discussion! If you have a place for us to start that would be super helpful and consider me your partner in driving this conversation and documenting its outcome for future implementation.

-------------------------

carlosjmelgar | 2023-10-11 17:43:16 UTC | #28

I voted "Abstain" because my self delegated tokens wont make an impact on the decision and would be more visible in grey than in red. 

Connor raises many valid concerns. 

[quote="connor, post:25, topic:16683"]
I don’t feel like any real ownership has been taken over the mistake (and I don’t think it’s Tally’s fault)
[/quote]
I thought these severance payments bundled with Devconnect expenses was a result of the mistake, but it is unclear. These could have been separated in sub bullet points for clarity.  
![severance pay|690x100](upload://zUeLqtO11UuM2UYpkg5CtYAW9xb.png)

[quote="connor, post:25, topic:16683"]
I am still a bit unsettled about the $100k+ sent from the CSDO multisig to MMM of which there still hasn’t been any acknowledgment of it, unclear whether that was free gift or if it’s supposed to be paid back by this budget, if that will happen again, etc
[/quote]

+1 - With more clarity on the use of these funds, this vote does seem rushed and prevents proper procedures to be put in place through DAO participation. The idea of a DAO Guardians sounds redundant now that the DAO Infra Workstream (?) [proposal](https://gov.gitcoin.co/t/proposal-dao-infra-workstream/16732) (?) went up. 

[quote="jengajojo, post:21, topic:16683"]
I second this and is absolutely necessary from a decentralisation pov! For the actual implementation, while I have designed and delivered many delegates programs myself, for gitcoin we can perhaps start with a ‘Delegates QF Round’ each quarter or so and iterate from there?
[/quote]

Bullish on this idea. Leaning in favor of this being a community led initiative (as it aligns with new EIs), rather than this being caked into another workstream's roadmap.

-------------------------

CryptoReuMD | 2023-10-11 18:07:49 UTC | #29

[quote="jengajojo, post:21, topic:16683"]
I second this and is absolutely necessary from a decentralisation pov! For the actual implementation, while I have designed and delivered many delegates programs myself, for gitcoin we can perhaps start with a ‘Delegates QF Round’ each quarter or so and iterate from there? What do you think
[/quote]

Up to. I think that self delegation sometimes it's indifferent for the protocol but if we raise hands in the same way it's more visible and valuable.

-------------------------

thedevanshmehta | 2023-10-14 18:05:53 UTC | #30

[quote="CoachJonathan, post:26, topic:16683"]
Looking ahead, it is fairly easy to estimate that MMM will come under the amount that they’ve requested, hence the lower budget request.
[/quote]

Thanks for the clarification, i was under the mistaken impression that gitcoin management reduced MMM's budget for no fault of theirs and it would adversely impact their functioning.

[quote="CoachJonathan, post:26, topic:16683"]
Technically [a Snapshot vote was done to guarantee these funds,](https://snapshot.org/#/gitcoindao.eth/proposal/0xc8cea5df7b14e71ec91aa307837e1e86f7cd285a5037a517daac29e45e34bb2d) and now we had this situation + MMM is requesting a reduced amount that still will get them to the end of the season.
[/quote]

Yes my thinking was that the snapshot vote was for allocating a certain amount X. Changing that to another amount Y requires a fresh vote as there are budgetary implications.

-------------------------

owocki | 2023-10-17 15:33:29 UTC | #31

gm all,

here is my proposal to prevent an incident like this from happening in the future: https://gov.gitcoin.co/t/gitcoin-walletguard/16772

-------------------------

CoachJonathan | 2023-10-19 15:07:27 UTC | #32

Hey everyone, [I started a new thread](https://gov.gitcoin.co/t/proposal-process-procedure-for-handling-funds/16808?u=coachjonathan) to discuss governance we can put in place to create more clarity around how to handle situations like this moving forward.

-------------------------
