---
id: 14010
title: "[GCP-009] - Upgrading Gitcoin’s Governance Contracts"
slug: gcp-009-upgrading-gitcoin-s-governance-contracts
category: governance-proposals
url: https://gov.gitcoin.co/t/gcp-009-upgrading-gitcoin-s-governance-contracts/14010
created_at: 2023-04-17T15:48:13.185Z
last_posted_at: 2023-09-06T15:30:13.099Z
posts_count: 50
views: 7474
like_count: 86
---

# [GCP-009] - Upgrading Gitcoin’s Governance Contracts

<https://gov.gitcoin.co/t/gcp-009-upgrading-gitcoin-s-governance-contracts/14010>
kyle | 2023-05-03 03:06:58 UTC | #1

## Summary

Gitcoin has been working with [ScopeLift](https://scopelift.co) for a number of months to develop, test and now implement new onchain governance contracts for the Gitcoin DAO. These new contracts are built on [tested Open Zeppelin](https://blog.openzeppelin.com/compound-governor-bravo-audit/) contracts that bring [Governor Bravo](https://blog.tally.xyz/understanding-governor-bravo-69b06f1875da) functionality to our DAO’s governance. These new contracts also have the [Flexible Voting](https://www.scopelift.co/blog/how-scopelift-built-a-flex-voting-atoken-on-aave) extension which has been [audited](https://blog.openzeppelin.com/scopelift-flexible-voting-audit/). Flexible Voting provides a permissionless interface for integration and experimentation via voting contracts, enabling a host of new use cases to eventually be built (layer 2 voting, shielded voting, new delegation schemes, etc..). It is our goal to have the DAO review and approve the upgrade to these new contracts, and then for us to migrate our governor contracts.

## Abstract

The Gitcoin DAO was launched nearly two years ago, in May of 2021 using our iconic [Quadratic Lands website](https://quadraticlands.com). The initial governance contracts used were the only “battle tested” contracts available at the time (though Governor Bravo was just emerging as an option). As a result, when deploying the DAO, the selection of Governor Alpha contracts were used to ensure stability and safety.

Fast forward two years and we have seen an explosion of new governance mechanisms (Nouns, NFTs, token voting, Gnosis voting, etc.). Gitcoin has explored a number of options to encourage more voter participation (like our Quadratic Votes on Snapshot, Signaling on our governance forums, etc.), but remains deeply tied to our governance token and the onchain mechanisms that it affords. We would like to upgrade the existing contract (technically replace) with new contracts to expand our onchain governance capabilities.

ScopeLift is a team that has been building and developing smart contracts with Gitcoin for years. They built the first bulk checkout experience and our zkSync checkout flow on the cGrants Platform, contributed to the first version of the Trust Bonus which became Passport, were integral in a large revamp of cGrants at GR9, and also shared their wisdom on how to construct dGrants.

## Motivation

The Alpha contracts we have work and are reliable, but we feel they are restrictive in our ability to explore, and upgrade components of our governance process. We would like to give the community the ability to decide the proposal threshold, voting delay, voting duration, and also introduce novel mechanisms via Flexible Voting strategies.

It has been flagged multiple times that we want more capabilities in governance voting. Even just giving voters an abstain option for on chain votes is not possible right now with the existing governor contracts.

## Specification

The new Governor contract and associated tests, simulations, and scripts are available in a [GitHub repository](https://github.com/gitcoinco/Alpha-Governor-Upgrade). The [Governor](https://github.com/gitcoinco/Alpha-Governor-Upgrade/blob/main/src/GitcoinGovernor.sol) was assembled from OpenZeppelin’s widely used, audited, and battle tested implementation of the Governor. It is compatible with Governo Bravo and with the existing GTC token contract and governance Timelock contract, which will remain in place.

The Governor contract also inherits ScopeLift’s Flexible Voting extension, which is backwards compatible with the existing Governor interface. It provides a new point for integrations. It is also fully [audited](https://blog.openzeppelin.com/scopelift-flexible-voting-audit/).

The repository contains an [extensive suite of tests](https://github.com/gitcoinco/Alpha-Governor-Upgrade/blob/main/test/GitcoinGovernor.t.sol). These tests simulate the upgrade to the new Governor, from deployment, proposal, Governance vote, and future votes by the DAO. The tests run on a “forked” state from mainnet to simulate the closest possible production state. They exercise all scenarios before and after the upgrade, and ensure Governance will still function properly after it is completed.

The repository contains [scripts](https://github.com/gitcoinco/Alpha-Governor-Upgrade/tree/main/script) for deploying the new Governor and for submitting a proposal for the upgrade to the existing Governor. The scripts are exercised by the tests. The deployment script was used to [deploy](https://etherscan.io/address/0x1a84384e1f1b12d53e60c8c528178dc87767b488) a candidate Governor contract. If the DAO chooses to move this to an onchain vote, the proposal script will be used by a delegate with sufficient weight to submit the proposal.

If an onchain vote on the proposal fails, the existing Governor will retain its Governance privileges and can continue to be used. This scenario has also been fully tested.

If an onchain vote on the proposal is successful, the old Governor will be left without a privileged role, while the new candidate Governor will be given control of the treasury and other Governance functions. Votes on future proposals will proceed through the new Governor. We are coordinating with Tally to ensure the change is reflected immediately in the Governance frontend should it succeed.

No proposals should be queued behind the upgrade proposal, as it will not be possible for them to execute if the upgrade succeeds. Any such proposal could still be resubmitted to the new Governor.

## Benefits

Upgrading (aka replacing) the existing Governor Contracts will offer the following benefits:

* Ongoing Customization of key voting criteria (proposal threshold, voting delays, voting period)
* Introduction of Flexible Voting to enable new use cases, such as GTC locked in various locations (Uniswap, Maker, Compound) to still be used for voting, Layer 2 voting, shielded voting, etc…
* Extensibility to explore additional customizations in delegation, such as expiring delegation, overridable delegation, chained delegation, quadratic delegation, and more

## Drawbacks

The cost of this work has been funded by the Gitcoin Foundation and is not something DAO will incur. The largest drawback to this proposal is execution risk. If there were a serious bug, we could lock the treasury. Said differently, without an operational governor contract, the treasury would be inaccessible. This is why all contracts have been audited and why ScopeLift has spent extensive time testing and simulating the upgrade.

## Vote

I propose three options:

1 - Vote Yes to upgrade the Governor Contract to the contracts ScopeLift has deployed [here](https://etherscan.io/address/0x1a84384e1f1b12d53e60c8c528178dc87767b488).

2 - Vote No and do not upgrade

3 - Abstain

-------------------------

bendi | 2023-04-18 15:49:36 UTC | #2

I'm excited to have this upgrade before the community for consideration. If anyone has any questions on the engineering here, feel free to tag me or reach out privately. Thanks!

-------------------------

DisruptionJoe | 2023-04-18 16:09:36 UTC | #3

We've been looking for this for a while! I'm glad to see it is finally ready. Fully in support.

-------------------------

jengajojo | 2023-04-21 07:43:03 UTC | #4

Absolutely in favor! 1 - Vote Yes to upgrade the Governor Contract. I like the fact that the DAO will be able to experiment with flexible voting and perform granular customisations in on-chain governance. 

I suggest predefining protocols to mitigate any crisis In case a bug were ever detected and the treasury becomes inaccessible.

-------------------------

ale.k | 2023-04-23 02:54:57 UTC | #5

I am excited for the benefits this upgrade brings, but I do not think that we've done a full exploration to mitigate risk. I'm a no until this can be addressed.

+1 as @jengajojo suggests, we could underwrite a fall-back protocol method and I believe this is the industry standard.

While this is an audit of another ScopeLift product, and not the flexible voting product, I would echo concerns of the 3rd party dependency which was surfaced here: https://leastauthority.com/static/publications/LeastAuthority_ScopeLift_Umbra-js_Final_Audit_Report.pdf

I appreciate OpenZeppelin as an industry leader in testing, but would like to further know that we can depend on thorough auditing for not only the core solidity technology, but also all dependencies and subdependencies, so as to mitigate issues in the future. @bendi can you speak more to how we can avoid exploits that might implicate ScopeLift indirectly, and whether there are procedures in place to "roll-back" should a new version be found insufficient?

-------------------------

QuadraticLander | 2023-04-23 13:13:49 UTC | #6

[quote="kyle, post:1, topic:14010"]
The largest drawback to this proposal is execution risk. If there were a serious bug, we could lock the treasury. Said differently, without an operational governor contract, the treasury would be inaccessible
[/quote]

This is a big drawback.  Can we be 100% sure this will not happen?

-------------------------

zcf | 2023-04-24 00:06:02 UTC | #7

Pretty excited to see Gitcoin go through with this governance upgrade. I think it'll enable a suite of new features that will really improve the governance experience.  I think this is great for both the DAO and the Gitcoin ecosystem.

@bendi and the team are also one of the best in the space. So I believe the execution risk is very minimal as they have a strong track record.

-------------------------

bendi | 2023-04-24 16:04:56 UTC | #8

Hey @ale.k, appreciate your thoughts. It's 100% valid to be concerned because obviously locking the treasury would be a serious problem. I'm glad folks are considering this carefully!

[quote="ale.k, post:5, topic:14010"]
+1 as @jengajojo suggests, we could underwrite a fall-back protocol method and I believe this is the industry standard.
[/quote]

Can you expand a bit on what you mean here? From a technical perspective, I don't believe there's any real opportunity to provide a "fall-back method", outside of the extensive testing and simulation we've done, along with the conservative approach toward the upgrade we've taken (leaving the timelock in place, etc...).

[quote="ale.k, post:5, topic:14010"]
While this is an audit of another ScopeLift product, and not the flexible voting product, I would echo concerns of the 3rd party dependency which was surfaced here: [https://leastauthority.com/static/publications/LeastAuthority_ScopeLift_Umbra-js_Final_Audit_Report.pdf ](https://leastauthority.com/static/publications/LeastAuthority_ScopeLift_Umbra-js_Final_Audit_Report.pdf)
[/quote]

The only dependency of Flexible Voting (which has been audited) is the OpenZeppelin Governor contracts, which—in addition to being audited themselves—are widely used in the ecosystem by many DAOs, including those like ENS and others that have quite a large amount at stake. The OZ contracts do not have any sub-dependencies.

[quote="ale.k, post:5, topic:14010"]
@bendi can you speak more to how we can avoid exploits that might implicate ScopeLift indirectly, and whether there are procedures in place to “roll-back” should a new version be found insufficient?
[/quote]

ScopeLift doesn't have any special control over the contracts being deployed. They're autonomous and we don't have any kind of permissions or admin rights. The contracts are [open source](https://github.com/gitcoinco/Alpha-Governor-Upgrade) and can be reviewed and verified by anyone technical. I'd strongly encourage technical folks in the DAO to take a look.

Unfortunately there is no way to enable a rollback method. For such a method to be possible, the existing Governance contracts would have to support it, which they don't. This is part and parcel with living in the world of immutable smart contracts.

It should be noted that a number of large DAOs have successfully upgraded Governance in the past, including Compound, Uniswap, Nouns and others. We've reviewed the processes used by those DAOs and carefully incorporated learnings from them into the work we've done.

It's also worth noting that the Gitcoin DAO will certainly have to upgrade at some point—there's just no way the DAO could survive on the Alpha contracts forever without stagnating.

One of the big advantages of both the Bravo compatible Governors, and Flexible Voting is that both allow for certain future changes to occur without impacting the core Governance system. This should mean this upgrade can get the DAO pretty far into the future before having to worry about this again.

If I've misunderstood any of your questions, or would like me to expand on anything further, please don't hesitate to follow up!

-------------------------

ale.k | 2023-04-24 19:20:39 UTC | #9

Hey @bendi - thanks for the thoughtful follow-ups and all the extra info!

Rereading @jengajojo's note I think maybe what they had in mind was more of an incident process, now - but what I'm curious about would be if we could use some sort of fail-safe logic to keep the contract from locking. I.e. if no funds/votes/actions have been taken for x period of time (2 years, for example), all funds will be sent to a new multisig for which we have key Foundation members in place. An "escape" route if you'd like, in case of catastrophe. 

I understand that the likelihood is low, and I agree that your team seems to have done all the necessary due diligence. Given some very high profile contract snaffus, though, just wondering if there is any way to encode further safety meaures here...

-------------------------

shawn16400 | 2023-04-25 12:15:10 UTC | #10

Hey @kyle 
I want to support this as I am a proponent of governance innovation.  But I have reservations and perhaps I just need a bit more context on the priority of the work.

1. How much did this cost the Gitcoin Foundation? 
2. How did the foundation decide this was the priority governance innovation to fund?
3. What immediate Gitcoin problems / priorities / strategies will this change address?

Thanks, 
Shawn

-------------------------

bendi | 2023-04-25 15:41:58 UTC | #11

Thanks for clarifying @ale.k. Unfortunately, no, there is no way to add such an "escape" route as you've described it. To have such an escape route, it would have to have been added to the *existing* Governance contracts that were deployed when the DAO launched, and which we're currently migrating away from. As it is, we're limited by what the existing contracts permit us to do.

As for incident response, in the unlikely event that the funds were locked, the appropriate response would probably be a social migration to a freshly deployed token and governance system with a contract that allowed GTC holders to exchange one to one. Having this plan in mind is useful, but I don't think it's a good use of time to actually build such a system ahead of time because, again, the likelihood of it playing out is exceptionally low.

Obviously the ScopeLift team will be monitoring the upgrade closely as it rolls out, and would be immediately available to the community were anything to come up.

-------------------------

kyle | 2023-04-26 19:17:55 UTC | #12

This work was initially [discussed](https://gov.gitcoin.co/t/should-we-increase-quorum/13031) and scoped (at CSDO) by the DAO over a year ago (and revived again [here](https://gov.gitcoin.co/t/upgrading-the-gitcoin-governance-contracts/10721)). It stalled among our process without a clear/motivated owner. I decided to take on the DRI role and pick this up and ensure it was completed.

Some of the immediate problems and priorities have been outlined in past posts (linked in my reply and in the initial thread). We are interested in adding customization to some configurations when the DAO is ready to make those changes and then also introduce flexible voting to ensure token holders have more ability to leverage their GTC that might not be in their wallet, but in other places on the Ethereum network.

-------------------------

borisdyakov | 2023-04-27 14:58:15 UTC | #13

As a new contributor to the DAO (PGF, as of nearly 3 months ago)  I was actually very surprised to hear that flexible voting was not already implemented. It's awesome to hear that this upgrade is moving forward. Kudos to everyone involved!

I'm very excited to explore new ways of letting GTC holders get utility out of their tokens while still being able to participate in governance (or delegating to a steward).

-------------------------

jengajojo | 2023-04-28 07:14:40 UTC | #14

Thanks for the explanation @bendi 

Is it possible to estimate the monetary cost of such an incident response? This ofcourse excludes any costs related to time or PR suffered by the DAO and its contributors. I would suggest keeping funds (+ some buffer) required to execute such an incident response in a separate multi-sig for additional redundancy.

-------------------------

bendi | 2023-04-28 14:36:04 UTC | #15

Interesting question and idea @jengajojo.  Very roughly you'd need:

* New Governor contract (out of the box Open Zeppelin probably good enough)
* New ERC20Votes contract with minting for GTC functionality (out of the box OZ with minor modifications probably good enough)
* A few scripts to deploy and configure the new system
* A frontend to allow for claiming

Putting the social coordination aside (no small thing), the engineering effort here isn't enormous. At typical rates for web3 work I'd say on the order of low six figures. It'd probably take 3-6 weeks for a team to pull it together, maybe less if they're completely focused on it, but you also wouldn't want to rush and botch it, which would compound your problems.

-------------------------

ccerv1 | 2023-04-29 15:13:40 UTC | #16

Thank you @kyle for flagging that this upgrade is not without risk. Nonetheless, I believe it is time for this to proceed and will be voting **YES.**

-------------------------

shawn16400 | 2023-05-01 14:47:57 UTC | #17

@kyle This proposal has met the minimum requirements to move to snapshot for a vote. 

* **5 day posting period:** met
* **Steward comments:** met (5 of 5) (DisruptionJoe, jengajojo, ale.k, shawn16400, ccerv1)

-------------------------

epowell101 | 2023-05-01 16:32:20 UTC | #18

Also fwiw voting YES - great conversation above btw.

-------------------------

azeem | 2023-05-01 17:40:24 UTC | #19

Definitely in favor of option 1 here.

-------------------------

kyle | 2023-05-04 14:15:23 UTC | #20

Hey all - I want to share some of the testing plan and details that @bendi shared with me.

> Testing & Simulation
>
> The tests are where the majority of the engineering effort for this upgrade took place. There are approximately [1,500 lines](https://github.com/gitcoinco/Alpha-Governor-Upgrade/blob/main/test/GitcoinGovernor.t.sol) of tests written in Solidity using Foundry’s testing framework.
>
> The tests run on “local fork” of Mainnet, meaning the test environment pulls its state and contract code from Mainnet as the tests interact with it. Effectively, the tests run in a simulated environment that mimics the real environment where the contracts will execute as closely as possible.
> 
> The tests exercise the Deploy script and the Propose script in order to hew as closely as possible to the scenario that will occur in production. Additionally, the tests are architected to be executed in different scenarios. One such scenario deploys the Governor scripts on the local test network.
> 
> The second scenario was added after the candidate Governor was deployed. It uses the actual deployed contract code that now exists on mainnet directly. This, again, allows the test suite to be simulated as closely as possible to the production environment.
> 
> After the proposal is submitted to the Alpha Governor, a third scenario will be added which will simulate the relevant tests against the actual proposal data that will—at that point—be onchain. When the simulations complete successfully after this update, we can be further assured the upgrade will work exactly as expected, and that no bugs were somehow introduced in the proposal phase.
> 
> The test suite itself simulates dozens of different individual scenarios related to the Governor upgrade and to its usage by the DAO before and after the upgrade occurs. These include:
> 
> * Successful deployment of the updated Governor with parameters that match the existing Governor
> * Successful submission of the upgrade proposal to the existing Governor
> * Rejection of the upgrade proposal if the vote fails
> * Continued successful operation of the existing Governor contracts if the upgrade proposal vote fails
> * Successful execution of the upgrade after a passing vote
> * Ability of the new Governor to queue and vote on new proposals after the upgrade, including:
>   * Proposals that succeed and are executed
>   * Proposals that fail and do not execute
> * Ability of the new Governor to move treasury funds after a successful upgrade, including individual tests for Ether, for each token held by Governance, and for combinations thereof
> * Ability of the new Governor to queue and execute proposals which modify its own Governance parameters, with individual tests for the voting delay, voting period, and proposal threshold
> * Ability of the new Governor to exercise Flexible Voting capabilities and pass various proposals wherein some or all voters leverage Flexible Voting
> * Validation that the *old* Governor no longer has the ability to execute proposals after the upgrade, including validation that it has no provenance over the treasury funds
> 
> Wherever possible within the test suite, parameters used by the tests are “fuzzed.” This means that instead of hardcoding values, random parameter values are injected each time the test suite runs. The suite has been run thousands of times, thereby exercising millions of individual permutations and validating that all test expectations hold regardless of the input.


You can read the full details here in the [HackMD here](https://hackmd.io/@scopelift/S1iO1llVh).

-------------------------

rajeev4321 | 2023-05-04 14:24:01 UTC | #21

 😀 New Governor contract (out of the box Open Zeppelin probably good enough)
New ERC20Votes contract with minting for GTC functionality (out of the box OZ with minor modifications probably good enough)

-------------------------

jengajojo | 2023-05-05 06:48:03 UTC | #23

Thanks for sharing. I understand that a new token contract can be deployed using these steps, but that will not recover non-native tokens from the treasury (stables/eth etc..). I'd suggest moving non-native tokens sufficient to cover these costs and some buffer into a separate multi-sig

-------------------------

kyle | 2023-05-08 00:17:17 UTC | #28

[quote="jengajojo, post:23, topic:14010"]
I’d suggest moving non-native tokens sufficient to cover these costs and some buffer into a separate multi-sig
[/quote]

Say more here? Why would we need to move these from the treasury?

-------------------------

jengajojo | 2023-05-08 06:53:47 UTC | #29

The downside of this upgrade has been flagged as a bottleneck by me and a few others such as @ale.k @QuadraticLander 

Since there is no way to install an 'escape hatch' incase of 

[quote="kyle, post:1, topic:14010"]
a serious bug, we could lock the treasury.
[/quote]
and the suggested solution

[quote="bendi, post:11, topic:14010"]
incident response, in the unlikely event that the funds were locked, the appropriate response would probably be a social migration to a freshly deployed token and governance system with a contract that allowed GTC holders to exchange one to one
[/quote]

Afaik, this cannot be done for nonGTC tokens. If this means that 35% of the treasury value will be inaccessible/permanently lost, then funds on a backup address will help reducing the damage.

-------------------------

bendi | 2023-05-08 15:30:56 UTC | #31

I think your proposal is worth a discussion @jengajojo, but something to remember is that moving the tokens is not a risk free proposition either. Where do they get moved to? Who has the ability to send them back. And all of that has to be done without error as well.

-------------------------

jengajojo | 2023-05-09 11:03:16 UTC | #32

I agree with your comments. Maybe a multi-sig with one member each from CSDO, Steward Council, foundation and yourself could be a starting point before diving deeper into governance around the backup address. As long as members on that multi-sig can be trusted, those backup funds are relatively safer in case the main treasury becomes inaccessible.

-------------------------

kyle | 2023-05-09 15:01:22 UTC | #33

hmm... this seems like a slippery slope. Why not just empty the treasury to that gnosis safe, then move it back after the upgrade? Im not sure where we draw the line.

-------------------------

bendi | 2023-05-19 13:58:02 UTC | #34

If the DAO is interested in moving some or all of the non-GTC funds out of the treasury before the update, we can facilitate this as part of the upgrade itself.

Onchain proposals can contain multiple actions that execute in sequence. We can add actions to the upgrade proposal which transfer any amount of any tokens to the desired address *before* upgrading the Governor.

In the very unlikely event the upgrade breaks governance, the tokens will still be available. This change can be made in the proposal script and we can add simulations to test it as well.

If the DAO would like to go this route, there are two questions which will have to be answered:

1. How much of the USDC and RAD tokens held by the [timelock](https://etherscan.io/address/0x57a8865cfB1eCEf7253c27da6B4BC3dAEE5Be518#code) should be moved.
2. Where should the tokens be moved to, e.g. a multisig held by DAO leaders, etc...

If the community would be more comfortable with the upgrade given these changes we are happy to facilitate them. I'm curious to hear what folks like @kyle, @shawn16400, @jengajojo, and others in the community think about this option. Thanks!

-------------------------

shawn16400 | 2023-05-23 11:59:20 UTC | #35

@bendi 
In a past life, we would do a risk assessment with each project that would list out realistic risks associated to a project.  This would be risks to the project, and risk because of the project (unintended consequences).  
Each risk is then weighted according to the vectors of "likelihood" and "consequences".  In this example the likelihood might be considered rare, unlikely, or even unknown.  However the consequence of bricking the treasury would rank up there with major/catastrophic.  

![image|690x401](upload://eykCQ4wyPX8b4GYbL4NX944SIcg.jpeg)

If Gitcoin followed this methodology, we have to put in a risk mitigation plan in place to protect against the occurrence.  Typically I would have done this via phasing in the changes to lower risk components (move change to a sub-treasury), building emergency inventory (moving tokens to a back up wallet), or building a back-up site (new & functional copy of our existing treasury) that is ready  for execution.   

Net - we really should put a plan in place.

-------------------------

bendi | 2023-05-23 16:32:53 UTC | #36

Hey Shawn, I love this framework for thinking about the risks and agree with where you've benchmarked it. *Very* unlikely/rare, but very negative consequences were it to happen.

I'm curious what concrete plan you think ought to be in place beyond moving some of the tokens out of the treasury before the upgrade? I.e. can you flesh out what you mean here, and how what's suggested is different than simply moving the tokens?

> Typically I would have done this via phasing in the changes to lower risk components (move change to a sub-treasury), building emergency inventory (moving tokens to a back up wallet), or building a back-up site (new & functional copy of our existing treasury) that is ready for execution


As I mentioned, I think moving the tokens is a reasonable step to consider, and it can be done (without additional risk) as part of the upgrade proposal itself. We're happy to execute on this, we just need to decide how much of the tokens to move and where to send them. If you have concrete additional suggestions for risk mitigation we're also happy to discuss!

-------------------------

shawn16400 | 2023-05-25 13:59:48 UTC | #37

@bendi thanks for all you and @ScopeLift have done to upgrade governance for the network.  During Tally Delegation Week I heard Scopelift mentioned in two different twitterspaces so these changes are indeed anticipated.  And to note, that once one or two protocols successfully perform this move without incident, I think migration becomes easier.

In the old world (if I did not have a QA environment), for a change with this potential impact I would have taken one of two approaches:
1) Upgrade a stand alone (back-up) system which has the same configuration as the target system.  This means move the changes to a mirror copy and (depending on interfaces), run a suite of business cases against the back up to ensure nothing broke.  If nothing breaks after testing, move the changes into the target system.
2) Move the entire upgrade to a new environment and migrate "business" over to the new environment.  Basically do step 1, but instead of moving the changes over to the old system after testing the backup, bring the treasury over to the new system in series of increasing stages based on demonstrated use.

Now part of the reason DAOs ~~run like crap~~ are sometimes slow is because people with little knowledge get to weigh in on things they may not know all that much about. Sometimes the outside perspective helps, and sometimes it just gums things up.  Not sure which case this is, but if it looks like help to you, I am happy to jump on a call and work through it. :)

-------------------------

jengajojo | 2023-05-26 06:49:28 UTC | #38

Thanks @bendi 

kyle brings a good point here
[quote="kyle, post:33, topic:14010"]
Why not just empty the treasury to that gnosis safe, then move it back after the upgrade?
[/quote]

if this is indeed a 
[quote="shawn16400, post:35, topic:14010"]
major/catastrophic.
[/quote]
 risk, then @kyle 's line of thinking doesn't sound so bad. I would like to hear what the other members of the stewards council have to say in this matter.

-------------------------

bendi | 2023-05-26 14:00:18 UTC | #40

Hey Shawn, no worries at all. These are good things to talk through to make sure they're clear. If I understand what you're saying correctly, it basically sounds like what you're recommending is that the upgrade be done in incremental steps instead of all at once. Is that basically right? 

Unfortunately, because of the way the existing contracts are designed, you can't put one system in place and slowly migrate over to it. Here's why, in (somewhat) more technical detail:

The treasury is held by a contract called a [Timelock](https://etherscan.io/address/0x57a8865cfB1eCEf7253c27da6B4BC3dAEE5Be518#code), which executes the onchain proposals after a delay. The Timelock has an administrator that can queue the transactions to execute through it. The [Governor](https://etherscan.io/address/0xDbD27635A534A3d3169Ef0498beB56Fb9c937489) contract is the administrator of the Timelock. There can only be one administrator at a time. Only the existing administrator can update it.

This means there must be a proposal where the existing Governor transfers the Timelock's administrator role over to the [new Governor](https://etherscan.io/address/0x1a84384e1f1b12d53e60c8c528178dc87767b488). It must be done in one step. And in the unlikely event that something went wrong with that step, such that the new Governor could not properly queue transactions to the Timelock, the funds there would be locked.

That's why we wrote all the tests as part of this process. These tests effectively simulate the upgrade process in an environment that mimics the network state of mainnet.

[quote="jengajojo, post:38, topic:14010"]
@kyle 's line of thinking doesn’t sound so bad. I would like to hear what the other members of the stewards council have to say in this matter.
[/quote]

I'll let @kyle comment, but I think he meant this as an example of how we could go too far in attempting mitigations.

As I said, I do think moving some proportion of the funds out of the treasury and into some other wallet is a reasonable disaster mitigation plan. We can incorporate this into the proposal itself and test the transfer out.

That said, it's important to remember that the mitigation itself is not risk free, may actually be riskier than the upgrade. What is more likely: the carefully planned and extensively tested/simulated upgrade process fails? Or a well intentioned multi-sig member fat-fingering the address in the Safe UI when they go to transfer the funds back?

This is why my personal recommendation would be to only move some percentage of the funds out. I think you'd want to transfer enough to allow the DAO to continue to function and recover in the very unlikely event that something went wrong, but also an amount small enough that the DAO could afford to lose it should something go wrong moving the funds back.

-------------------------

bendi | 2023-06-16 21:56:07 UTC | #41

Hey all, I wanted to share that we just [disclosed](https://www.scopelift.co/blog/flexible-voting-bugfix-and-adoption-update) and [patched](https://github.com/ScopeLift/flexible-voting/releases/tag/v1.1.0) a bug with Flexible Voting. The bug was found during an audit of Frax Finance's governance contracts, which use Flexible Voting. PoolTogether has also [funded](https://www.tally.xyz/gov/pooltogether/proposal/73) ScopeLift to execute their upgrade to an Flexible Voting Governor.

It's important to note that this bug was an edge case, would *not* have put treasury funds at risk, and would not have impacted Gitcoin directly, as signature based voting is not (currently) leveraged by the DAO.

All that said, the fact this bug was discovered *does* emphasize the very valid concerns the community has had around security and safety of funds.

Next week, we will deploy a new candidate Governor—with the fix included—for Gitcoin to consider, and update the repository to reflect this change. We hope the community can come to some consensus soon on a path forward, in particular on:

* How much of the treasury funds to move out before executing the upgrade and...
* Where to move the backup funds to

-------------------------

kyle | 2023-06-20 17:16:34 UTC | #42

Thanks, Ben for the update!

When are the the PoolTogether contract upgrades going live?

-------------------------

jengajojo | 2023-06-21 06:30:19 UTC | #43

Thanks for the update @bendi 

[quote="bendi, post:41, topic:14010"]
How much of the treasury funds to move out before executing the upgrade
[/quote]
Considering the fact that bugs are being found on an ongoing basis, I suggest we move all non-native tokens to another address. The reason being that non-native tokens cannot be recovered but a new contract can be deployed for native tokens

[quote="bendi, post:41, topic:14010"]
Where to move the backup funds to
[/quote]
Assuming that these responsibilities still hold true for CSDO https://gov.gitcoin.co/t/csdo-charter-v1/12490 I suggest them to make a separate address to hold these funds. Alternatively a time dependant contract can escrow but I am not sure if it's worth the operational effort for you all.

In either case, I am happy to add my feedback on the draft proposal if you want. Thanks once again @bendi

-------------------------

bendi | 2023-06-26 15:54:39 UTC | #44

Hey Kyle, we're working on the engineering side of this now. Realistically I think a proposal for PoolTogether could be live in 4-5 weeks.

[quote="jengajojo, post:43, topic:14010"]
Considering the fact that bugs are being found on an ongoing basis, I suggest we move all non-native tokens to another address. The reason being that non-native tokens cannot be recovered but a new contract can be deployed for native tokens
[/quote]

I understand this reaction, and if the Gitcoin community decides to move 100% of non-native funds, we are happy to support it. I just want to reiterate a few facts:

1. The bug in question would not have resulted in lost or locked funds
2. The contracts have now gone through two in-depth audits
3. Moving of the funds is not a risk free endeavor, as they have to be sent back to the DAO by the entity that holds them, such as the CSDO as you are suggesting, and errors can happen in that process as well.

With regards to the CSDO as a suggested entity to custody the funds, I have a couple of quick practical questions: 

1. How many people are on the CSDO
2. Does the CSDO currently have a multisig it operates on mainnet, and how is that multisig configured if so? What is its address?

Thanks for the suggestion! Hoping we can move this forward and come to a consensus soon :slight_smile:

-------------------------

kyle | 2023-07-26 11:54:08 UTC | #45

Hey all - I want to bump this thread again for everyone.

We recently withdrew $3MM USDC from the treasury to support the workstreams and moved that into the gnosis safe. 

I wold love to revive these conversations and move this to a vote on snapshot. If the snapshot vote passes, I will work with ben to ensure we test this together a few times prior to que`ing up the Tally vote.

Hopefully folks are interested in supporting the upgrade!

-------------------------

bendi | 2023-07-26 14:08:42 UTC | #46

Thanks for moving this forward Kyle. As always, happy to answer any questions anyone might have!

-------------------------

bendi | 2023-07-31 17:07:20 UTC | #47

We're gratified to see the snapshot vote on the upgrade is going well. As promised, the updated candidate Governor has been deployed: 
https://etherscan.io/address/0x9d4c63565d5618310271bf3f3c01b2954c1d1639

-------------------------

dcictalireza | 2023-08-01 22:58:23 UTC | #48

Vote Yes to upgrade the Governor Contract to the contracts ScopeLift has deployed

-------------------------

bendi | 2023-08-11 17:21:42 UTC | #49

The upgrade proposal is now live onchain. We have done two additional security/safety checks since the proposal was put onchain by @kyle.

First, we updated our tests & simulations to run with actual deployed proposal data, to ensure no errors were introduced when the proposal was put onchain. See results [here](https://github.com/gitcoinco/Alpha-Governor-Upgrade/pull/27).

Secondly, we modified [Seatbelt](https://github.com/Uniswap/governance-seatbelt) to simulate the proposal and analyze its effects. You can see the report [here](https://gist.github.com/mds1/ce7b65b02c257dab1569fac081e3aa94).

Both checks indicate that the proposal will behave as expected, that Gitcoin's Governor will be properly upgraded, and that the DAO's onchain governance will continue to function as expected afterwards.

Given all this, we encourage DAO Delegates to vote in favor of the proposal. https://www.tally.xyz/gov/gitcoin/proposal/65

Thanks again to the Gitcoin community for entrusting ScopeLift with this sensitive work. We look forward to seeing the upgrade completed and what will get built on top of it afterwards.

As always, I'm happy to answer any additional questions anyone has.

-------------------------

garm | 2023-08-15 11:58:14 UTC | #50

Excited to see the proposal going live @bendi ! Appreciate I'm late to the party, but I was wondering if you could share the links to the audits of the GitcoinGovernor contracts? I'm probably overlooking something obvious, but can't find them myself :sweat_smile:

-------------------------

bendi | 2023-08-16 13:00:56 UTC | #51

Hey @garm, thanks! And no worries at all for the late question.

The final Gitcoin Governor contract is assembled from fully audited components, namely: ScopeLift's Flexible Voting extension and the battle tested OpenZeppelin Governor implementation.

Flexible Voting was audited twice, but only one of the audits was made public, which you can see [here](https://blog.openzeppelin.com/scopelift-flexible-voting-audit). The code was audited a second time by Trail of Bits as part of that projects Governance system audit. We have seen the final report but it has not (yet?) been published. 

As you can see by looking at the [Gitcoin Governor](https://github.com/gitcoinco/Alpha-Governor-Upgrade/blob/main/src/GitcoinGovernor.sol), there is no new code—only the inheriting of audited contracts and the configuration of parameters as appropriate for Gitcoin.

Most of the work for the upgrade actually comes from the [tests/simulations](https://github.com/gitcoinco/Alpha-Governor-Upgrade/blob/main/test/GitcoinGovernor.t.sol) we wrote to ensure the upgrade would execute properly and that the new Governor contract we put in place would function as expected afterwards.

Please let me know if you have any further questions! We are also excited to see this upgrade coming to fruition.

-------------------------

bendi | 2023-08-24 12:58:42 UTC | #52

Hi all, as most of you have no doubt seen, the upgrade has now executed successfully. The new Governor is available on Tally and one new proposal has already been submitted to it. I again reiterate my thanks to the Gitcoin community for trusting ScopeLift with this work. We're excited to see what comes next, and eager for the opportunity for continued collaboration. Congrats to Gitcoin!

-------------------------

owocki | 2023-08-24 13:33:10 UTC | #53

Kudos on the successful upgrade. (err seemingly successful?  Does the new Tally proposal have to pass and successfully execute to 100% prove it works?)

[quote="kyle, post:1, topic:14010"]
Flexible Voting provides a permissionless interface for integration and experimentation via voting contracts, enabling a host of new use cases to eventually be built (layer 2 voting, shielded voting, new delegation schemes, etc…).
[/quote]

Looking forward to seeing what kind of things are built here.  I'd love to wrap my mind around the possibilities enabled.

[quote="kyle, post:1, topic:14010"]
The Alpha contracts we have work and are reliable, but we feel they are restrictive in our ability to explore, and upgrade components of our governance process. We would like to give the community the ability to decide the proposal threshold, voting delay, voting duration, and also introduce novel mechanisms via Flexible Voting strategies.
[/quote]

Kyle teased some possibilities here.

-------------------------

bendi | 2023-08-25 13:19:05 UTC | #54

[quote="owocki, post:53, topic:14010"]
Does the new Tally proposal have to pass and successfully execute to 100% prove it works?
[/quote]

Hey Kevin, good question. We can say with high confidence that the Governor is working based on the execution of the proposal and the queuing of a new one. But you're right. We'll be able to say with **total** confidence that it worked only after the first proposal clears through it!

-------------------------

bendi | 2023-09-05 13:21:59 UTC | #55

Excited to say that [one proposal](https://www.tally.xyz/gov/gitcoin/proposal/49342153689828217040461764921799237826821432521798787433997318257313751977548) has now executed through the new Governor, with several others lined up to do so soon. It is now possible to say with full confidence that the upgrade has gone as expected. Once more, thanks to the Gitcoin community for entrusting us with this work!

-------------------------

kyle | 2023-09-06 13:49:30 UTC | #56

As Ben mentioned, the Upgrade has been successful!

We are going to spend a bit of time outlining where there are opportunities to introduce novel voting schemes in the future. 

Just a heads up, Tally will continue to show the details for the old governor, and now also the new governor. All voting and on-chain interaction will happen using the new page and new governor.

Let us know if you have any questions :slight_smile:

-------------------------

owocki | 2023-09-06 15:30:13 UTC | #57

Kudos to everyone who worked on this on a successful upgrade.

-------------------------
