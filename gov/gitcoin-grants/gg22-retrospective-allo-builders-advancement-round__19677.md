---
id: 19677
title: "[GG22 Retrospective] - Allo Builders Advancement Round"
slug: gg22-retrospective-allo-builders-advancement-round
category: gitcoin-grants
url: https://gov.gitcoin.co/t/gg22-retrospective-allo-builders-advancement-round/19677
created_at: 2024-11-22T22:29:26.456Z
last_posted_at: 2025-11-03T07:28:01.916Z
posts_count: 5
views: 2698
like_count: 5
---

# [GG22 Retrospective] - Allo Builders Advancement Round

<https://gov.gitcoin.co/t/gg22-retrospective-allo-builders-advancement-round/19677>
cauetomaz | 2024-11-22 23:37:12 UTC | #1

## GM Builders! 

The **GG22 Allo Builders Advancement Round** has concluded, and we’re excited to share the outcomes, insights, and lessons learned. This round not only distributed funding to outstanding projects but also furthered our mission to enhance grant infrastructure and enable equitable resource allocation in the Allo ecosystem.
    [![Captura-de-tela-de-2024-11-22-05-18-07.png](upload://hWSZIpaDrDy9wfkPJeV233wK9L2.png)](https://postimg.cc/YLpDKhHp)

---

## **Round Overview**

### **Key Metrics**
- **Total Donations:** $5,273.06  
- **Matching Funds Available:** $25,000 USDGLO  
- **Unique Contributors:** 333  
- **Number of Contributions:** 934  
- **Participating Projects:** 17  
- **Average Contribution:** $15.84  

---

### **Passport Usage**
- **100%** of contributor addresses were scored using the **Passport Model-Based Detection System**.  
- **110 Users (33.0%)** received **full matching** (passport model score over 50).  
- **21 Users (6.3%)** received **partial matching** (passport model score between 25 and 50).  
  -  **Full Matching:** Contributions matched at 100% of the calculated amount.  
  - **Partial Matching:** Contributions matched between 50-100% based on the score.  

This system effectively incentivized legitimate users to strengthen their digital identities, ensuring fairer distribution while protecting matching funds from Sybil attacks and airdrop farmers.

---

Explore the full results in detail:  
[https://qf-calculator.fly.dev/?round_id=636&chain_id=42161](https://qf-calculator.fly.dev/?round_id=636&chain_id=42161)



---

## **COCM: Improving Fairness in Matching**

### **COCM vs. QF**
The adoption of **COCM** over traditional **Quadratic Funding (QF)** highlighted the value of filtering connections and weighting contributions based on relationships, leading to more equitable outcomes for ecosystem grant programs. 

Balancing between mechanisms (e.g., COCM and QF) can provide flexibility for future rounds depending on goals. 


[![Captura-de-tela-de-2024-11-21-17-31-06.png](upload://s20Nq11AlmsajkjhDnL5lhIXo3V.png)](https://postimg.cc/2bQVzcQm)

### Key Takeaways from COCM Results
**1.** Balancing Over-Concentrated Networks: Amplifying contributions from high-context donors and mitigating bot-like behavior on grants for, the COCM model mitigated the influence of isolated wallets and ensured fair matching allocations.

**2.** Projects like Giveth and VoiceDeck saw reduced matching under COCM compared to QF due to contributions coming from wallets that donated to just one project. This reduction highlights COCM's ability to discourage over-concentrated support and encourage a more diverse backing.

**3.** Projects such as Open Source Observer, 1Hive Gardens, and Karma GAP received significant boosts in matching through COCM due to their support coming from wallets with a diversity of connections.

## **Matching Models Breakdown**

The **COCM model** was used to calculate matching funds. Below are the top 10 projects based on COCM results:

| Project Name                                                                          | Matching Amount (COCM) | Matching Amount (QF) | Δ Match  |
|--------------------------------------------------------------------------------------|------------------------:|----------------------:|---------:|
| viaPrize Gitcoin Fiat Integration                                                     |               $4,438.77 |            $3,500.45  |  $938.32 |
| Atlantis                                                                              |               $3,694.93 |            $3,373.39  |  $321.54 |
| VoiceDeck: A Marketplace for Impact Certificates                                      |               $3,138.43 |            $5,000.00  | -$1,861.57 |
| Open Source Observer                                                                  |               $2,447.41 |              $871.77  | $1,575.64 |
| Giveth                                                                                |               $2,077.76 |            $4,109.78  | -$2,032.02 |
| 1Hive Gardens                                                                         |               $2,061.28 |              $946.32  | $1,114.96 |
| Karma GAP - Funding Map on Allo                                                       |               $2,059.52 |              $993.49  | $1,066.03 |
| Flow State (Streaming Quadratic Funding)                                              |               $1,223.86 |              $758.18  |   $465.68 |
| DAOIP-5 Grants Standard by DAOstar - Improving the web3 grants ecosystem for everyone |                $761.56  |              $341.96  |   $419.60 |
| Allo Hacker Abode                                                                     |                $612.28  |            $1,722.62  | -$1,110.34 |

These results reflect how matching was distributed, with the COCM model ensuring contributions from high-context donors were prioritized while managing coordination effects.


This approach resulted in a more equitable distribution of funds, aligned with the ethos of decentralized public goods funding.

---



## **Key Round Insights**

### **1. Enhanced Sybil Resistance**
- **Gitcoin Passport Integration:**  
   - 100% of contributor addresses were verified using Gitcoin Passport, ensuring credibility and reducing fraudulent activity.


### **2. Improving Matching Mechanism**

- **COCM vs. Quadratic Funding:**  
   - COCM outperformed traditional QF by focusing on meaningful relationships between wallets, aligning resources with high-context donors who provided stronger signaling.
      - further prioritized wallets backed by diversified connections, amplifying contributions impact  and mitigating bot-like behavior.
      
- **Matching Cap:**  
    We could have achieved even greater equity within the round with a Matching Cap set at 18% instead of 20%. Since none of the projects reached this value, and only 3 projects received over 10% of the funds, while 4 projects secured between 5% and 10%, and 9 projects received between 0% and 5%.
   
[![fundsfrompool.png](upload://vYdcmKuiVmsSoib7QlalsDbg6bO.png)](https://postimg.cc/VJ4M3qMd)

[![allo-percentages.png](upload://18ubF3kbxZuebFIYor7Ywp7N8kc.png)](https://postimg.cc/N2hr1phP)

### **3. Community Engagement**
- The round attracted a diverse set of projects and contributors, emphasizing the ecosystem’s growing vibrancy.  
- **17 Participating Projects:** Spanning a range of impact areas, from fiat integrations to reputation systems and impact tracking tools.

---

## **User Experience Enhancements**

The updated **Grantstack Dashboard** simplified round management and transparency:
- Provided clear visualizations of wallet connections, donor behaviors, and matching allocations.
- Enabled quick comparisons between COCM and QF models for informed decision-making.
- Streamlined payout processes with integrated features like member addition and fund distribution.

---

## **Lessons Learned**

### **1. Matching Mechanisms Matter**
- COCM proved effective for this grant type, but balancing between mechanisms (e.g., COCM and QF) can provide flexibility for future rounds depending on goals.

### **2. Transparency is Key**
- The dashboard visualizations and Passport integration demonstrated the importance of clear, accessible data in fostering trust and fairness.

### **3. Future Opportunities**
- Continue scaling the matching cap to maintain balance across larger matching pools.
- Explore ways to onboard more diverse contributors and projects into the ecosystem.

---

## **Next Steps**

### **1. Grant Tracking**
- Track how the matching funds are creating impact, using milestones on https://gap.karmahq.xyz

### **2. Expand Engagement**
- We aim to enhance education and outreach to onboard more projects and contributors for future rounds.

### **3. Build on Success**
- Use insights from this round to refine matching mechanisms and grow the Allo ecosystem with innovative, impactful projects.

---

## **Thank You, Builders!**

A massive thank you to everyone who participated, contributed, or supported this round. Together, we are shaping the future of decentralized funding and public goods. Your work inspires us to keep pushing the boundaries of what’s possible.

For questions, feedback, or ideas for future rounds, feel free to reach out. Let’s keep building!

Stay awesome,  
**The Allo Builders Team**

-------------------------

tomislavmamic | 2024-11-26 14:41:44 UTC | #2

What do the differences between COCM matching and QF matching in projects tell us?

-------------------------

cauetomaz | 2024-11-27 16:04:13 UTC | #3

Hey @tomislavmamic thx for your question. 

In few words, the difference between COCM matching and QF matching is, 
- COCM recognizes the diversity of contributors connections, giving higher matching to projects supported by independent contributors (who usually donate to a lot of projects). While QF treats all contributions equally, regardless of context. 

So in my opinion COCM ensures a more balanced and equitable distribution for rounds aiming to amplify genuine web3 community-driven support, while QF could have better use for rounds where we can expect to have a bunch of wallet onboardings and newly contributions, like on citzens rounds.

-------------------------

tomislavmamic | 2024-11-30 09:39:45 UTC | #4

Thanks @cauetomaz .

I should have been more specific about my question. In your graphic that you created (and which is awesome!) I can see that projects are positioned at different distance from the center. The center has donors that donate to multiple projects, and projects that are closer to the center have higher % of their donors also from the center. Then there are some "outliers" like giveth which have many outside donors that donate just to them.
![CleanShot 2024-11-30 at 10.36.04@2x|567x500](upload://6VZKIBAAAM3f6jJNJrU1FXDKCfO.jpeg)

Obviously, COCM decreased the multiplier for these voters, but I wonder did it do enough? Maybe I am misled by this graphic, how can I see the individual multipliers for donors or clusters?

-------------------------

webx3456 | 2025-11-03 07:28:01 UTC | #5

I would like to know after the funding, how the organisation go with the distribution

-------------------------
