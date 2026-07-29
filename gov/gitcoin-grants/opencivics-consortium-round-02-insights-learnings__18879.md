---
id: 18879
title: "OpenCivics Consortium Round 02 Insights & Learnings"
slug: opencivics-consortium-round-02-insights-learnings
category: gitcoin-grants
url: https://gov.gitcoin.co/t/opencivics-consortium-round-02-insights-learnings/18879
created_at: 2024-05-28T21:24:19.049Z
last_posted_at: 2024-06-06T23:30:15.644Z
posts_count: 4
views: 3112
like_count: 9
---

# OpenCivics Consortium Round 02 Insights & Learnings

<https://gov.gitcoin.co/t/opencivics-consortium-round-02-insights-learnings/18879>
omniharmonic | 2024-05-28 21:24:19 UTC | #1

The OpenCivics Consortium Round 02 was a massive success. We grew the matching pool from $15,000 USD to $66,000 USD and were able to provide sizable grants to 16 incredible projects. We learned a tremendous amount from running the round and look forward to continuing our efforts to provide coordination and funding infrastructure to our members. To date, we’ve now distributed over $100,000 USD to OpenCivics members!

We’re building upon the success of the grants program thus far to explore building a prototype for Streaming Quadratic Funding that will provide our members with ongoing financial support for their critical social impact work, leveraging the collective intelligence of the Consortium to allocate funds outside of one-off grant rounds. We’ll have more to share about that prototype experimentation soon!

In the mean time, continue reading to see what we learned from #GG20!

# Results Overview

OpenCivics Consortium Round 02 distributed **$66,000 USDC** in matching funds to **16 projects**. The round raised **$10,309.37 in crowdfunding** from community donations, **totaling $76,309.37** in funds distributed. A total of **492 donors** generated **1,090 donations**, averaging **$9.45 per donation**. Overall, donors generated a **7.4X multiplier** of their donations in matching funds.

Compared with our last round, the second iteration of OpenCivics Grants was the most successful round we’ve run so far with **40% more donors**, **20% more crowdfunding donations**, and **200% larger matching grants** for the top grantees.

[Click here to view the automatically generated Gitcoin Report Card for the round.](https://reportcards.gitcoin.co/42161/31)

**For a detailed data analysis of the grant round results, check out [Consortium Grant Round 02 Analytics](https://www.notion.so/Consortium-Grant-Round-02-Analytics-9f206f580d93462d80a55c3132a7c829?pvs=21) on our wiki.**

![Screenshot 2024-05-28 at 2.49.58 PM|511x499](upload://2jCKprPC5rBsExEx4I3zcKOHRd6.png)


# Overall Data Insights

1. **Significant Matching Contributions**
    - **Ethereal Forest**, **Urbánika's bus**, and **Metagov** received substantial matching funds. This indicates that these projects were able to leverage their donor base effectively to secure matching contributions. It suggests a high confidence level from matching funders in these projects' potential impact.
2. **Top Fundraisers**
    - **Ethereal Forest** stands out with the highest total amount received ($14,227.02). This project not only received the most substantial total funds but also had the highest number of donations (165), reflecting both broad and deep support. The high number of donations and matching funds indicates effective fundraising strategies and strong donor engagement.
3. **Potential for Increased Engagement**
    - Projects like **Mycelial Civic Knowledge Networks** and **Exploring Post-Capitalist Crypto Pathways** have moderate total funds and a relatively high number of donations. These projects could potentially increase their total funds by focusing on increasing the size of individual donations.
4. **Low Engagement with High Potential**
    - **VoiceDeck: A Marketplace for Journalism Impact Certificates** and **Moos: A Berlin hub for reimagining our cities** received substantial total funds but have relatively low ratios of donations to total funds. This suggests that these projects received significant donations from fewer contributors. They may benefit from strategies aimed at broadening their donor base to enhance sustainability.
5. **Diverse Fundraising Success**
    - The diversity in donation patterns and matching fund success across projects indicates varied effectiveness in fundraising strategies. Projects with lower total amounts but high donation counts might explore methods to increase individual donation amounts. Conversely, projects with high total amounts but fewer donations could focus on broadening their engagement strategies.

# Round Operator Insights

Overall, we learned that Quadratic Funding is unpredictable and, even by constraining some variables, the outcomes are very hard to sculpt or shape. We failed in our goal of ensuring each project walked away from the round with at least $3,000 - $5,000 USD, a goal driven by our first hand experience as grantees of extremely low returns of grant funding when compared with the time it takes grantees to promote their grants.

## Limiting Grantees Hypothesis

This round, we were experimenting with the hypothesis that reducing the total number of projects while increasing the matching pool would ensure that the minimum grant allocation would be large enough for all projects to create meaningful, documentable impacts created through the grant funding. We calculated the range of matching pool distributions based on our Genesis Round which reflected a 2-3x spread between the smallest matching amount and the largest. To achieve our goal of significant funding for each project, we chose to restrict the total number of projects to 16, a number derived from our analysis of the previous round’s outcomes and the volume of matching funds available for our second round.

Our insights from this aspect of the round were twofold. First, the matching distribution for this round was far more extreme than anticipated. The range from the lowest matching amount to the highest amount was closer to 10x, a significant increase from our previous round. In one sense, this is a positive discovery because it shows that the Quadratic Funding mechanism is successfully allocating funds based on the preferences of the collective intelligence of donors. On the other hand, it means that the hypothesis we were testing failed to achieve our desired goals. Rather than seeing this as a failure, we see it as a learning opportunity that reveals the high variability of matching amounts and the impossibility of using the variables that *are* within our control to influence the outcome, even if our desired influence on the outcome is holistically considered and well intentioned. This feeds into the second insight from this aspect of the round. As round operators, we struggled to limit participation in the round to only 16 projects. There were many deserving projects who submitted applications whom we rejected simply based on the premise that we had an obligation to test our hypothesis that a smaller number of projects would yield significant funding for each project. Filling the final spots in the round was a painful process that required over a week of deliberation, weighing a number of variables like use of funds, project history and track record, and available grant size vs scope of the project.

Based on the feedback and data generated by this round, we are unlikely to limit the number of projects in future rounds in the same way. This doesn’t solve the issue of unpredictable results and the potential for grantees to spend 10s or 100s of hours on project promotion only to receive a few hundred or a thousand dollars in matching funds, but it does embrace the philosophy of quadratic funding which places the entire allocation process in the hands of donors. Accepting and acknowledging this as a fundamental limitation and benefit of Quadratic Funding, we will encourage grantees to consider allocating only the number of hours they are willing to lose (without a guarantee of earning the value of that time back in donations) for their grant promotion.

## Updates To Gitcoin Passport

For those not familiar, Gitcoin Passport is a sybil resistance mechanism for Quadratic Funding rounds that attempts to ensure donors are unique human individuals and not bots or scammers attempting to rig the system for their benefit. Prior to this round, the Gitcoin Passport was based on Stamps, attestations of identity that included a number of different identity verification mechanisms like Google and GitHub accounts. This round, Gitcoin introduced Cluster Matching, an AI-enabled system that autonomously reviewed the on-chain transaction history of each donor to verify their “proof of humanity.”

Comparing the Gitcoin Passport Stamp-based matching results with the newly created Cluster Matching-based results, we were pleased to discover that the new Cluster Matching approach generated a more equitable and holistic distribution of funds. We believe this occurred because the Stamps system was an unwieldy user experience that took tremendous time and effort to reach a “passport score” that made a user eligible for matching funds. Even as web3 experts, it took us extensive time and energy to achieve a passing score and we imagine that the user experience was so challenging for most ordinary donors that they were discouraged from completing their passport or perhaps even donating to projects. Cluster matching reduces friction for donors and empowers non-web3 savvy individuals to make donations that qualify for matching funds.

## Arbitrum x Gitcoin User Experience

This was also our first round using Arbitrum, having run our previous round on a more obscure Layer 2 blockchain, the Public Goods Network. Overall, this was an incredibly positive experience. While the user interface for program managers is almost entirely the same other than a slightly different process for bridging and adding funds to the smart contract, as a donor, the experience of donating across multiple rounds on the same chain was incredibly streamlined and supported the cross-promotion of projects with grants in multiple rounds. Gas fees on Arbitrum are incredibly low which was another massive benefit for our grantees, donors and the round overall.

With that said, many of our donors still expressed challenges with bridging funds from Ethereum mainnet to a Layer 2 blockchain. We look forward to a future in which the donor experience on Gitcoin can include fiat donations as well as some kind of inter-chain mechanism that makes it irrelevant to the front end donors which chain the rounds themselves choose to operate. These challenges are persistent across the web3 ecosystem and are not unique to Arbitrum or Gitcoin, but we look forward to collaborating with both teams to co-develop the underlying infrastructures that help Quadratic Funding enter the mainstream, a path that serves the entire public goods ecosystem.

# Looking Forward

We’re excited to continue offering Gitcoin Grants rounds as a service to our members. We are well positioned to advocate on behalf of the entire Consortium of civic innovators we serve to raise matching funds and provide the support structures for funding rounds. We are currently exploring a large grant from ThankArb to develop a new funding mechanism for our members that distributes drips of funding to each project on an ongoing basis. This method, Streaming Quadratic Funding, will be developed by a new initiative called *Flow State* and we’re excited to collaborate with them to explore adding specific functionality that is custom-made for the OpenCivics Consortium. The platform will offer a token-gated environment where OpenCivics members can use Quadratic Voting to express their preferences on where the continuous drips of grant funding are allocated. This mechanism breaks fund allocation out of the time-locked grant round context into an ongoing stream of funding that supports the sustainability of projects over time.

Additionally, we forged lasting bonds with the other community grant round operators who all expressed an interest in co-hosting a collaborative round in the future. As ever, Gitcoin is all about relationships and this round deeply strengthened the relationships between community round operators. There seemed to be a universal sentiment that the entire public goods funding space could benefit from a funding round tailored to synergistic collaboration between different impact sectors, working together as ephemeral DAOs to generate outputs based on the unique contributions of multiple projects. We’re excited to explore this possibility and to work with other community round operators to continue serving our grantees in innovative ways.

# Conclusion

We believe Quadratic Funding for public goods funding allocations is one of the most promising and useful contributions of web3 infrastructure to the social impact space. This round taught us an immense amount about the limitations and benefits of Quadratic Funding related to ways we can improve the donor experience, grantee experience, and overall impact of the grants themselves. We are currently engaging our grantees in a participatory process to identify and report on the milestones they achieve with the funds they’ve received from our Consortium Round 02 which we will share with you here in a few months. Our grantees have already started to identify pathways to synergize their project efforts within the context of emerging collaborative initiatives within the Consortium and we can’t wait to see what we’re able to create together.

Thank you to all our donors, grantees, and members for supporting public goods and for funding the critical work of civic innovation.

In Us We Trust,

OpenCivics Stewards

-------------------------

gulliverz | 2024-05-29 13:32:11 UTC | #2

[quote="omniharmonic, post:1, topic:18879"]
Gitcoin introduced Cluster Matching, an AI-enabled system that autonomously reviewed the on-chain transaction history of each donor to verify their “proof of humanity.”
[/quote]

A person might have less tx history, due to many circumstances, it doesn't verify sybil to my eyes. Or,  he/she might be a newbie, just started exploring with gitcoin projects, and might have bare transactions.

-------------------------

metahands | 2024-06-03 02:01:24 UTC | #3

Awesome to get these insights, thanks for the write-up Benjamin, and all the good work you're doing for the ecosystem.

-------------------------

Sov | 2024-06-06 23:30:15 UTC | #4

Thanks for the thoughtful retrospective and for the ongoing partnership!

Great feedback on the UX.  While this is a common issue across Web3 we will continue to do what we can to improve and lessen barriers to entry.

Always a pleasure to work with you and the team at OpenCivics!

-------------------------
