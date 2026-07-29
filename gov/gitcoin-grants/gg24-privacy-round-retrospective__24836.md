---
id: 24836
title: "GG24 Privacy Round Retrospective"
slug: gg24-privacy-round-retrospective
category: gitcoin-grants
url: https://gov.gitcoin.co/t/gg24-privacy-round-retrospective/24836
created_at: 2025-11-14T23:12:59.644Z
last_posted_at: 2025-12-20T16:46:10.666Z
posts_count: 2
views: 745
like_count: 5
---

# GG24 Privacy Round Retrospective

<https://gov.gitcoin.co/t/gg24-privacy-round-retrospective/24836>
johnguilding | 2025-11-14 23:12:59 UTC | #1

### Context & Objectives

Privacy projects face obstacles in securing sustainable funding. Traditional venture capital models can often align poorly with privacy-focused development, and recent regulator insinuations 4 have caused additional chilling effects on funding. Some privacy projects are public goods without revenue sources, so have little upside for investors. And while it is possible to attract funding, many privacy endeavours can be viewed as risky, as they carry regulatory risk and uncertainty. The recent privacy market report 3 by Web3Privacy Now states that “the post-Tornado Cash investment climate in privacy remains mild”. According to their research, in Q1 and Q2 2025, about $161.6 million was invested in privacy, with B2B decentralised privacy projects attracting the most funding. When compared with broader crypto funding, this is tiny, leaving privacy builders fighting over a smaller slice of the funding pie.

As a pioneer in quadratic funding for public goods, Gitcoin is in a unique position to help fund privacy projects, and doing so in a privacy-preserving manner using private voting protocols. With this privacy round, Gitcoin addressed one of the core contradictions in the privacy space: privacy tools need funding, but traditional funding mechanisms compromise privacy.

The Privacy Domain in this Gitcoin round was set up to help discover promising privacy projects and accelerate the funding for these projects.

We set the following specific metrics in the [Privacy Domain proposal](https://gov.gitcoin.co/t/the-case-for-privacy-gg24-maci-allo-capital/22491) to measure success in this particular domain:

* Participation
* Funds received by projects part of the round(s)
* Feedback by donors/voters

Long-term success means creating a funding environment where privacy developers can focus on building rather than constantly seeking funding, ultimately strengthening the broader Ethereum ecosystem. We haven’t got there this time round, but we hope that this round can serve as a strong foundation for the continued funding of privacy projects.

### Round Design & Mechanism

#### Voting model

Quadratic Funding (QF) is a fair distribution model for community funding rounds like GG24 because it helps spread the voting power along multiple projects. QF has been used for public goods funding in the past, and we wanted to continue experimenting with this promising mechanism. We saw a diverse project pool being funded ranging from established and well-known teams to promising new projects.

#### Eligibility criteria

The Privacy Domain conducted two selection processes. One process was performed internally with the round operators and partners in order to filter out projects that did not meet the eligibility requirements stated in the [round page](https://pse-team.notion.site/gg24-privacy-round):

* Privacy R&D
* Privacy dApps
* Privacy infrastructure
* Privacy education

We just found a few projects that were not aligned with the privacy domain and we recommend them to submit their application to the appropriate Gitcoin round domain. We also discarded a few projects that were not completely ready to apply (lack of prototype, lack of documentation, lack of whitepaper or research paper, no information on their landing page, etc).

#### Partners

We ran the privacy domain successfully with the help of amazing partners in the different areas of the round. We are grateful to have such incredible and supportive teams working towards making privacy succeed in the Ethereum ecosystem.

Donors

* Community donations
* Celo PG
* Self
* PSE
* Gitcoin

Round operations

* Privote
* Web3Privacy Now
* MACI team

#### Design choices

* WETH as funding asset: we selected WETH as our only funding asset because we needed an accessible token that donors would own. Our smart contract that handles funds distribution can also only support a single funding asset.

* MACI as our voting protocol: We wanted to experiment with a private voting model in order to elicit more truthful voting patterns and avoid the vote being turned into a popularity contest where the winning projects get the most votes. Private voting prevents bandwagon effects and individuals have to think carefully about what projects they want to vote for. All votes were private and receipt-free which would make it impossible for bribers to verify with 100% certainty that their bought vote was tallied. Coercion was not a concern here, but it is a feature bundled with MACI.

* Human Passport as our gatekeeper: securing private voting rounds is challenging. There are different gatekeeping mechanisms implemented in the MACI protocol to filter users and only allow authorized voters to submit their vote. In the Privacy Domain case we wanted all humans to be able to vote so we decided to implement the Human Passport technology as a gatekeeping mechanism. This way we would be sure that all voters were humans and not sybils or bots.

### Participation Snapshot

We were happy with the outreach we were able to do on social media. This effort was assisted by the campaigning effort from Web3Privacy Now. Here are a couple of quantitative metrics we gathered:

* Number of applications: 121
* Number of accepted projects: 93
* Total QF votes: 7427
* Community donations: ~$13,000
* Total raised: 35.41 WETH
* Project that received the most: dev3pack got 6.4368 WETH
* Project that received the least: WoCo got 0.0016 WETH

### Funding Distribution & Thematic Insights

The Privacy Domain of Gitcoin Grants Round 24 had strong participation and community support from privacy projects. It consisted of 4 categories that we considered important for the privacy space A project could mark itself as multiple properties. In the following sections we describe each category in detail and what insights we got from the round. Each category can be divided into subcategories.

dApps (59 projects marked as dapps)

dApps were the main category in the privacy domain due to the amount of projects that applied. This is expected as privacy should be a main feature in apps. We divided it into subcategories:

* Private transfers
* Private voting apps
* Wallets
* Social apps
* AI apps
* Journaling apps
* User-facing apps
* Private communication apps
* Health-related apps
* Private wallet recovery

It is interesting to see a couple of subcategories arise, particularly private wallet recovery and health-related apps. The former involves methods to recover smart accounts or to backup accounts in a privacy-preserving way. The latter are focused on providing privacy to individuals' health data.

Infrastructure (60 projects marked as infra)

Infrastructure encompasses solutions that provide a specific feature/service for developers and dApps to use in order to build a user-facing application. We divided the projects into the following different subcategories:

* Identity
* Networking
* Browsing
* Public Goods
* Co-processors (FHE, Garbled Circuits, UTXO-based)
* Private compute
* DNS
* Operating system
* Reputation

We mainly saw teams working on identity technology like zk-passport or anonymous reputation systems. Co-processors for FHE (Fully Homomorphic Encryption), Garbled Circuits and even private UTXO-based models were presented.

It is important to mention that we had [Tor](https://gitcoin.privote.live/rounds/0/0x088ea854a714df5af2b482665f0bcb688615c2cb0933cf648b0783f233edf343) in the dApps and Infrastructure categories. This project is a famous private browser not natively related to the web3 ecosystem. This project gets special mention as it is a well-known and established non-web3 privacy project.

Education (29 projects marked as education)

Education includes individuals or organizations that have been actively involved in teaching about technologies, implications,benefits, tradeoffs, use cases and more topics related to privacy. The education projects can be subcategorized into:

1. Courses: educational material that people can use to understand topics related to privacy. Examples include: courses, workshops and learning resources.
2. Content: communication material that describes a specific topic or use case. Examples include: newsletters, blogposts, podcasts, etc.
3. Events: real-life and online events focused on privacy topics. Examples include:

Research (37 projects marked as research)

In the round application form, multiple projects that applied to the dApps and infrastructure categories also selected research. It is more than evident that multiple projects in the privacy space are actively working on research and development of cryptographic techniques that would make privacy use cases practical. We recognize that most of these projects (if not all) have a strong research component involved.

We considered research as an additional category with the aim to get researchers, cryptographers and mathematicians to apply because of their research results and advancements. We got lots of projects that did research, but we interestingly only got a single project that was exclusively research. So for future rounds it might be important to communicate that pure research projects/endeavors could apply.

### Impact To Watch Out For

The Privacy Domain of the GG24 round was based on a retroactive funding mechanism which implies giving funds to projects that already have some advancements, prototypes or developed features. We would love to see how these projects keep progressing in the future and how far the privacy space on the Ethereum ecosystem advances.

#### dApps

We saw dApps mainly focused on voting, private transfers and private communication. As the Ethereum ecosystem evolves, we will see more user-facing dApps with privacy as their main feature. We hope to see improvements, new developments and new approaches from the round participants to tackle end user challenges regarding privacy. The project used for the frontend, Privote, got a good chunk of funding. These donations will fund their continued work in making onchain private voting effective and easy to use on Ethereum.

#### Infrastructure

Privacy infrastructure is the cornerstone for developers to build privacy-focused applications and solutions. We saw infrastructure projects focused on identity, networking, browsing and co-processing. One notable example is the Worm team getting a good amount of funding. We view this as a very interesting and promising project. This funding will aid their development and hopefully help burnt eth become a successful privacy preserving mechanism.

#### Education

Education and awareness about privacy is important to push the space towards a fair and secure environment. We recognize the immense work that education projects have been doing on the privacy space. From spreading new technological approaches to forming new privacy-focus developers, education projects are doing a huge impact in space. We hope to continue seeing the education category in the privacy domain to grow. One notable example is the Dev3pack team being the first winner in the general leaderboard. We hope they continue to invest resources into educational resources to prepare the next generation of privacy-focus developers.

#### Research

Research is key for the development of new technologies like the ones we are seeing in the privacy domain. We did not get many pure research projects, so this is potentially an area to focus on more in the future to find the right participants.

### Learning & Reflections

Running the Privacy Domain of the Gitcoin Grants Round 24 was an interesting challenge that we had to face in order to keep pushing the privacy development in the Ethereum ecosystem. The following section will describe in more detail what worked, what didn’t and process insights for future round operators.

#### What worked

1. Multiple projects applications: we had a large number of applications given the short time notice.

2. Broad range of applications: the Privacy Domain had applicants from different categories across the privacy space. We got projects ranging from private health solutions to networking infrastructure.

3. Novel voting mechanisms: we got to see how MACI, a private voting protocol, can be used in a quadratic funding round. While coercion was not a concern, the private vote forced voters to come to independent conclusions about what they voted for without relying on the votes of others.

4. Sybil resistant authentication: We tried out an open and public vote where anyone could take part as long as they were human. This enabled anyone from the community to get involved. One issue with open participation over a selection of experts is that projects with larger communities can galvanise members to vote for them during the funding round. So while bots are prevented, large and coordinated communities could swing the vote. We are unsure if this happened, but it is a possibility.

#### What did not work

1. Not enough matching funding given the topic and the momentum: privacy has been a main talking point in 2025 and a lot of organizations have stated its importance on the Ethereum ecosystem. We could have funded more organizations and donors for this domain.

2. Issues with deployment flow: MACI platform is an end-to-end funding mechanism solution using MACI as its private voting protocol. We had some issues with the contract deployment and verification which caused us to redeploy the contracts at the last minute. We waited until the last deployment to publicly announce the round opening but some projects had already been submitting applications. This caused 5 projects to reapply again into the new deployed contract.

3. Application editing: our application interface did not allow applicants to modify their information after submission. This caused difficulties to projects that wanted to add new information into their public project page.

#### Process insights for future operators

The Privacy Domain in the GG24 round gave us multiple insights and improvements for future operators focusing specifically on the privacy space of the Ethereum ecosystem.

1. Early organization: operators should start organizing their privacy domain round as soon as possible in order to talk to possible donors, publicly communicate projects about criteria and market themselves with the opportunities of participating at a Gitcoin round.

2. Clear gatekeeping instructions: bot prevention is always an issue in on-chain voting protocols. In this GG24 round we used the Human Passport solution to only allow humans to submit votes. For future rounds, the gatekeeping mechanism and instructions should be clearer so users can participate in the round effortlessly.

3. Better fundraising: operator’s team should include a fundraising specialist that would present the Gitcoin round to donors, explain to them their benefits from sponsoring the round and getting a considerable amount of matching funds. The privacy space is growing fast and there are multiple stakeholders interested in getting onboard.

4. Improve initial review process: A Gitcoin Grant round usually involves users voting for selected projects but as round operators, it is important to filter projects that do not need the round criteria or are not relevant to the domain topic. This process requires time and therefore it should be considered in the round timeline as an important item.

### Community Voice

#### Projects

* > “i was accepted into @gitcoin #GG24's privacy round — where @zkMACI & @Privoteweb3 are being used to coordinate funding *privately* SO. COOL. Ethereum engineers 21st century democracy🚀” http://x.com/haochizzle/status/1981394595734077788
* > “We’re excited to share that we won 🥈 2nd place in Gitcoin’s GG24 Privacy Round! Massive thanks to our amazing supporters who made this possible!
  >
  > Also huge thanks to @Privoteweb3 @zkMACI @web3privacy 🫡 Privacy is wormal🪱“ https://x.com/EIP7503/status/1984494888985972927

* > “Gitcoin's privacy funding round has ended. I made it to spot #69 out of 93 projects ! This achievement got me $22 in WETH.” https://x.com/LauriPelto/status/1985605440122552441

#### Voters

* > “Spent the last few hours reading all the privacy projects in the round. Never am I more excited for the future of privacy. 2026 is shaping up to be a very exciting year.” https://x.com/Savio_Sou_/status/1981836611475132728

* > “Honestly, this has been the worst Gitcoin round I’ve experienced so far. I’ve tried several times, but I’m still not sure whether my votes or donations were processed successfully.
  >
  > I successfully submitted my vote in the GG24 Privacy round through @privoteweb3! 🚀 Even though it's on-chain, no one can see how I voted. True privacy. ANY HUMAN CAN VOTE. Don't miss your chance to shape the future of privacy!” https://x.com/brucexu_eth/status/1982986136084787558

* > “... And I found out about all sorts of other, interesting, privacy projects.” https://x.com/LauriPelto/status/1985605440122552441

### Ecosystem Gaps & Emerging Opportunities

The round was useful for projects in the education and research categories, as those areas do not normally get public goods funding. We did not get many pure research applications. This could mean a few things: that research already has good funding, that projects are funding their research through other work (e.g. most research applications also fall under the infra or dapps categories), or that we aren’t reaching the right people. Reaching out to academics somehow could be a good improvement for next time.

We got an application from the Tor project. There are many other privacy projects that are not in the web3 space. We would love to see more non-web3 projects apply for funding on Ethereum more generally. This could be a good opportunity for all funding rounds to pursue in the future. It is unclear if now is the right time for public goods funding to branch out of the web3 space, but we should be mindful that building capital allocation mechanisms and distributing public goods funding needs to break out of the web3 ecosystem eventually.

### Recommendations & Next Steps

* **Organise the round much sooner**, the privacy round was only announced a few weeks before it took place. This gives projects more time to apply and gives the round organisers more time to campaign and fundraise.
* **Engage in fundraising more effectively and sooner.** We would like a future privacy round to get significantly more funding.
* **Use the latest Privote frontend using MACI V3.** We used an older version of MACI and an old MACI UI modified specially for the round. The new Privote frontend and MACI version would solve many of the UX hurdles raised during the round.
* **Explore a better proof of personhood flow.** We had a few issues with the Passport integration. People were slightly confused by it, we didn’t include full instructions about what chain to mint the passport on, and users had to leave the site to mint their passport. Next time, we could use a Human Passport feature where you can mint the passport in the end-users app itself, provide better messaging about minting the passport the correct chain from the start, and possibly explore additional proof of personhood tools such as ZKPassport.

-------------------------

ivanmolto | 2025-12-20 16:46:10 UTC | #2

Hey @johnguilding  thanks for sharing your GG24 Privacy Round retrospective — really enjoyed it.

I’m wrapping up some notes based on it and was wondering where I could find detailed data on each grantee, such as total funding received, community donations, etc to generate stats like max, min, and average/median grantee donations. Thanks!

-------------------------
