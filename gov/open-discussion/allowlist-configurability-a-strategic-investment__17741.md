---
id: 17741
title: "Allowlist Configurability - A strategic investment"
slug: allowlist-configurability-a-strategic-investment
category: open-discussion
url: https://gov.gitcoin.co/t/allowlist-configurability-a-strategic-investment/17741
created_at: 2024-02-12T18:47:18.591Z
last_posted_at: 2024-04-16T16:30:06.915Z
posts_count: 6
views: 3502
like_count: 10
---

# Allowlist Configurability - A strategic investment

<https://gov.gitcoin.co/t/allowlist-configurability-a-strategic-investment/17741>
owocki | 2024-02-12 18:47:18 UTC | #1

Thanks to Feems and @DisruptionJoe from ThankARB for pointing this out to me!  Thanks to @meglister and @renaobrien for reviewing this doc before publishing!

# Allowlist Configurability - A strategic investment

Right now, Gitcoin Grants Stack has a limitation in utility for grants round operators because a key configuration variable (who gets to vote?) is not very tunable.

To do a QF Round on Grants stack I must decide whose votes count in allocating the matching pool. In doing so I must choose between

1. No Sybil Resistance
2. Passport > 20

Because there are only 2 options, that means that round managers cannot really tune their capital allocation. If I want to just upload a simple list of Badgeholders, like Optimism does, I can’t do that. If I want to give a specific Hats role in my DAO the ability to do a vote, I can’t do that.

# Strategic Investment

We should make this parameter more tunable.

I should be able to configure this very important parameter.

As @meglister pointed out to me, JokeRace does a great job of providing a UX. eg you can upload a lsit of addresses, tokens, criteria like "you have held token for x amount of time", etc and then those people can vote on the JokeRace.  We could perhaps take some inspiration from that.

Some options that seem like no brainers to me:
1. Configure passport. What if I want to use a non-Gitcoin scorer, or specific set of stamps? What if I want the threshold < 20?
2. Other options:
   1. Easiest - CSV Upload of addresses I want to be able to vote.
   2. More advanced stuff
      1. Hats role.
       2. Owner of SAFE Multisig
       3. People who have more than x amount of y token (I should be able to vote with these tokens, either with the number of votes being the number of tokens, 1 per account, or other formulas in between).
       4. EAS Attestations
       5. Guild roles
3. Use other sources for sybil resistance.
    1. Worldcoin or brightid or zupass

# Conclusion

Giving round managers the ability to be able to tune these parameters would give them the ability to sculpt very specific capital allocation requirements into their rounds. It would allow Gitcoin Grants Stack to be more configurable to capture not just QF, but RPGF, or other novel use cases.

# Open Questions

1. What 1-3 allowlist options are the most important ?
2. How do we make sure we are continuously keeping up with the markets needs?
3. Is this an Allo build or Grants Stack build?

-------------------------

Sov | 2024-02-13 01:41:07 UTC | #2

I believe this would be worth pursuing.  To answer your questions:

1. I think we can start simple and enable allowlisting via 1) simple delegation (i.e. who is an admin versus a reviewer, etc.) 2) .csv upload of allowlist (the badgeholder example you share) and 3) integration with best of breed partners like Hats Protocol.

1. Develop partnerships with others in the space who are specializing in this domain and keep our internal functionality (simple delegation/.csv upload) limited.  We should also be actively looking to fund integration partners that are best of breed versus internalizing effort ongoing.

1. IMO simple integration (the delagation example and .csv uploads) could be Grants Stack with more advanced/partner integrations being an Allo build that eventually can make its' way upstream to Grants Stack if feasible.

-------------------------

thelostone-mc | 2024-04-16 04:17:10 UTC | #3

This would be an Allo Build at the strategy level.

This is what we currently have.
![image|507x499](upload://yPQVosSwZ39zlG0evRu0juvNG9F.png)

Given how allo is built, we can evolve it to 
![image|690x409](upload://iSARKxyezJopJ4FCo9AZ8iGwaU4.png)


We built out something along those lines in MicroGrants
https://github.com/allo-protocol/allo-v2/blob/main/contracts/strategies/_poc/micro-grants/MicroGrantsHatsStrategy.sol#L74

We could just throw this into it's beforeAllocate util function and create mixes of all of these gating strategies. 

Advantages:
- We create optional dependencies with other protocol which means if allo choses to launch in a chain without passport or hats, it could still do so. If it does -> then the strategies using these hooks can be deployed/used as well 
- If we make a library of utils hooks like these, others can use them and we have gating hooks available to all strategies and all you have to do is write afew lines of code to import the file and call the function

-------------------------

owocki | 2024-04-15 21:46:16 UTC | #4

[quote="thelostone-mc, post:3, topic:17741"]
* If we make a library of utils hooks like these, others can use them and we have gating hooks available to all strategies and all you have to do is write afew lines of code to import the file and call the function
[/quote]

i think this is a very exciting direction to me!  having these functions in a well organized library would make it easy to drop in diff allowlists to diff strategies as they are built out.

would it be possible to configure the allowlist at round creation time, such that a round manager can select between allowlist type upon round creation?

-------------------------

thelostone-mc | 2024-04-16 04:26:29 UTC | #5

[quote="owocki, post:4, topic:17741"]
would it be possible to configure the allowlist at round creation time, such that a round manager can select between allowlist type upon round creation?
[/quote]

Yes. 
**OPTION 1**
We would simply create a QFGating.sol contract which imports QF contract and we'd have to override 
- init function : to set what type of gating is needed 
- implement the beforeAllocate to gate based on the type of gating  (all gating logic is stored in 1 contract)

**OPTION 2 (RECOMMENDED)**
Another option is to keep the contract logic simpler. We just have multiple contracts instead of one QFGating contract. We'd have QFNFTGating.sol, QFPassportGating.sol or QFHatsGating.sol and all these contracts would 
- override init function
- implement the beforeAllocate to gate based on the type of gating 

=======

Both are good options but option 2 might be smarted cause that way we have gating contact specifc to a protocol and we can control where this is deployed (For example: if we deploy QFGating.sol aka option 1 on a chain where passport and hats isn't deployed -> it's a pointless deploy ) but option 2 ensures we can deploy the specific gating contract where that gating protocol is present 

Both options have the same level of effort in terms of coding / integrating into grants-stack as the sdk would handle which contract to create based on the gating option selected

Sidnote: We could honestly do both options cause it's that simple

-------------------------

carlb | 2024-04-16 16:30:06 UTC | #6

I have written some suggestions in my allo sketch doc on gating that might be interesting.
It's basically just a small contract with a modifier:

```solidity
contract GatedRound is Round, EASGate, NFTGate {
  function init(bytes config) {
    __EASGate_init(attester);
    __NFTGate_init(nftAddress);
  }
  // Only allow projects with an EAS Attestation
  function register(address recipient) onlyAttestation(recipient, attester, schemaId) {}

  // Only funders with an NFT can allocate
  function allocate(address recipient, uint256 amount) onlyNFT(recipient) {}

  // Or with 10 GTC
  function allocate(address recipient, uint256 amount) onlyERC20(gtcAddress, 10e18) {}
```

That way they can be composed with other types of round, not just QF.

-------------------------
