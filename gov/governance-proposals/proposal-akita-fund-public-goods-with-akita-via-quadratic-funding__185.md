---
id: 185
title: "[Proposal - Akita] Fund public goods with AKITA via Quadratic Funding"
slug: proposal-akita-fund-public-goods-with-akita-via-quadratic-funding
category: governance-proposals
url: https://gov.gitcoin.co/t/proposal-akita-fund-public-goods-with-akita-via-quadratic-funding/185
created_at: 2021-05-21T03:46:55.681Z
last_posted_at: 2021-06-01T13:41:45.797Z
posts_count: 2
views: 3572
like_count: 13
---

# [Proposal - Akita] Fund public goods with AKITA via Quadratic Funding

<https://gov.gitcoin.co/t/proposal-akita-fund-public-goods-with-akita-via-quadratic-funding/185>
castall | 2021-05-27 16:35:15 UTC | #1

## Background
@ceresstation suggested in [this topic](https://gov.gitcoin.co/t/discussion-what-should-the-gitcoin-community-multisig-do-with-the-donated-akita/67/101) that we split our discussion on how to use @vbuterin's Akita donation into distinct proposals.

I proposed using the Akita to fund public goods, asked some open questions a week ago to help with details, and got some inspiration from [this post](https://gov.gitcoin.co/t/discussion-what-should-the-gitcoin-community-multisig-do-with-the-donated-akita/67/126) by @vbuterin .

# Proposal
## Summary
Unlock the donated Akita over the course of 10 years and put it into matching pools for [quadratic funding](https://wtfisqf.com) of public goods. Half of the funds will be for public goods in the Akita ecosystem, and half will be for public goods in general that can benefit from receiving Akita tokens.

## Abstract
Put the Akita into a [Sablier](https://sablier.finance/) contract to stream it over 10 years into a multisig. The multisig will use the same [Trust Architecture](https://gitcoin.co/grants/12/gitcoin-grants-official-matching-pool-fund) that other matching pools use. The matching amounts per round will be proposed by Gitcoin as usual. A smart contract for distributing Akita will be funded at the end of a round once the multisig owners approve of the contract's particulars.

Gitcoin users can claim any token, including Akita.

When showing match estimates, the Gitcoin UI should not show Akita matching, unless the grant belongs to the "Akita" category. (See "Specification," below.)

## Motivation
A donation to Gitcoin is a donation to the matching pools of future quadratic funding rounds. Many public goods, including [Gitcoin itself](https://gitcoin.co/grants/86/gitcoin-grants-round-9-dev-fund) can be funded this way.

Indeed, @vbuterin asked @owocki where a donation should be sent "for future matching pools."

## Specification
Put the Akita into a [Sablier](https://sablier.finance/) contract to stream it over 10 years into a multisig. 

The multisig will be a 3/5 multisig managed by Ethereum community members David Hoffman, Anthony Sassal, Eric Coner, Kevin Owocki, and Hudson Jameson. It's the responsibility of the multisig managers to replace themselves for the Akita matching management roles as needed while maintaining a 3/5 structure.

The multisig will use the same [Trust Architecture](https://gitcoin.co/grants/12/gitcoin-grants-official-matching-pool-fund) used by the "official" matching pool with regard to validating a round, approving the distribution contract, and moving Akita into it.

The start date of the Sablier stream will be shortly after the creation of the multisig to receive the stream, but it will take a while to build up funds, so the next grants round (round 10) will not feature Akita matching--only rounds 11 and later. This will give the Akita community time to create grants for their own ecosystem matching pool. The end date for the stream will be 10 years from the start date.

On a technical note, the caller of the [`createStream()` function](https://docs.sablier.finance/streams#create-stream) (probably a smart contract) should remove its ability to make a later call to [`cancelStream()`](https://docs.sablier.finance/streams#cancel-stream) once the stream has been set up correctly. 

50% of the Akita received will go to a per-round Akita matching pool for supporting public goods in the Akita ecosystem. Grants may choose "Akita" as their category to be eligible to receive matching from this pool.

The remaining 50% will be divided (using [quadratic matching](https://wtfisqf.com)) among public goods grants in all other categories that can receive ERC-20 tokens as matching. (This may exclude categories for non-Ethereum platforms.)

The multisig managers may choose not to claim all funds available from the Sablier stream if they prefer to save them for future rounds.

When showing match estimates, the Gitcoin UI should not show Akita matching, unless the grant belongs to the “Akita” category.  This way, Akita (which is not a stable coin) can be distributed without expectation about its value.

Claiming Akita is possible using the claiming UI for Gitcoin grants recipients after the distribution contract for the round has been approved by the multisig managers.

## Benefits
Other communities might decide to follow suit by donating community tokens to Gitcoin and using Gitcoin to fund public goods within their ecosystems.

## Drawbacks
Creating new matching pools and new funding categories adds complexity to Gitcoin. Gitcoin has already been dealing with this, however.

## Voting
Voting "yes" means the Akita currently held in the community multisig will be distributed as specified above.  Voting "no" will require a different proposal to determine their distribution.

-------------------------

lefterisjp | 2021-06-01 13:41:45 UTC | #2

My understanding of this proposal is that the funds here are to be used to fund via a matching pool AKITA projects.

As Gitcoin's mission is to fund all opensource projects and not specifically AKITA ones I don't think this is a good proposal.

Also if we were to use the matching for all grants that would also be a very bad idea, since very few grants would want to accept matching in an illiquid memecoin and create taxable events on it.

So I personally disagree with this approach.

-------------------------
