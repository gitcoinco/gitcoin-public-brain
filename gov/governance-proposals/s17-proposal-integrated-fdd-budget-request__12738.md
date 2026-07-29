---
id: 12738
title: "[S17 Proposal] INTEGRATED FDD Budget Request"
slug: s17-proposal-integrated-fdd-budget-request
category: governance-proposals
url: https://gov.gitcoin.co/t/s17-proposal-integrated-fdd-budget-request/12738
created_at: 2023-01-31T19:51:08.371Z
last_posted_at: 2023-04-01T15:12:53.119Z
posts_count: 52
views: 7727
like_count: 135
---

# [S17 Proposal] INTEGRATED FDD Budget Request

<https://gov.gitcoin.co/t/s17-proposal-integrated-fdd-budget-request/12738>
tigress | 2023-02-14 19:45:13 UTC | #1

<br><br>
# TL;DR

**FDD as a workstream is dissolving after Season 17, but the need for fraud detection and prevention services is far from done.** 

* S17 Budget is almost $10k lower than Season 16
* FDD is not requesting any reserves as this is the last season for us as a workstream
* The Contributor Transition process has already started partially with an intention for clear transfer roles after EthDenver
* Embedding fraud & data analyst/science knowledge and expertise across the workstreams will help the DAO realize the value of trust & risk management as well as increase awareness for fast-paced, data-driven “build-measure-learn” culture
* Open Data Community continues data infrastructure innovation with hackathons and provides data transparency, provenance, and reproducibility for algorithmic policy decisions

**3 key themes this season:**
  * 1️⃣ **Continued Trust in Gitcoin’s Ability to Prevent Fraud**
  * 2️⃣ **Empowering the DAO with Open Data Infrastructure & Processes**
  * 3️⃣ **FDD Workstream Dissolution Success**

<br><br>
# Amount

FDD is requesting **$123,694** from the treasury to complete a budget of $340,314 for S17. A breakdown of the budget can be found at the end of this document.


|Gitcoin Season|Season 15|Season 16|Season 17|
|---|---|---|---|
|Season Budget|$349,500|$349,500|$340,314
|Season Reserves| $233,000|$172,615|$216,620 1*|
|Unspent Reserves %|100%|100%|100%|
|Treasury Request USD|$362,500| $409,885| **$123,694** 2**


1*) *FDD received $233,000 in reserves which were requested at a GTC price of $1.65 in S15. These were received in January at a GTC price of $1.37 making the received total of $193,461. 60% was converted to stables ($116,077) leaving a 40% exposure of GTC to upward price movement from $1.37 to $1.78 ($77,384 to $100,543) leaving a total of $216,620 in unspent reserves*

2**) *Since FDD intends to dissolve as a workstream, **we will request the full season budget less 100% rolled over reserves from S16**. The amount of GTC requested and the value of the reserves will be adjusted based on the current market value at the time this proposal is moved to Tally using the lower of the current price or the 20 day moving average, whichever is lower.*



<br><br>
# Milestone Report S16

Season 16 has been a very dynamic and the most unusual season for us. We set out with likely projects ([S16 budget request]([https:/](https://gov.gitcoin.co/t/s16-proposal-integrated-fdd-budget-request/11890)/)) and needed to respond to the changing circumstances of the DAO during the season. The changes include the decision not to host GR16 in December, to deprecate the cGrants product, the decision by GPC/PGF that sybil defense services wouldn’t be needed during UNICEF/Fantom/Alpha rounds, and subsequent findings that these did indeed need services. 

Our assessment on what we completed and why can be found here: https://miro.com/app/board/uXjVP0ptO3k=/

|Objectives Past Season|Initiative / Outcome|Key Result|
|---|---|---|
|Continuous analysis & validation of passport scores made available for round owners & technical users in partnership with the Passport team.|🟢 Everything the Passport team asked for was delivered on time and extra work was done |<br>* Created 4 scores including the one in use for Alpha rounds and Passport Scoring as a Service <br>* Built a passport scoring application mvp<br>* Delivered stamp topology research and stamp prioritization requests|
|Build reliable composable, open source software tools for round owners to prevent fraud.|🟡 Documentation and understanding were massively improved, but actual building was slower than expected. Results of hackathon could make this green. |<br>* Designed a user interface for legos to be used by an fdd fraud consultant & eventually a round owner<br>* 5 Packages wallet legos in FDD github<br>* Created documentation for the person of a fraud consultant or round operator<br>* Created & updated readme files for all legos and applications and general getting started<br>* Created FAQ for Open Data Community to build and interact with legos<br>* Posted 3 articles discussing Sybil Scoring Legos<br>* Building custom aura implementation for gitcoin grants and an gitcoin/fdd team to participate|
|To empower a regen data community with infrastructure, tools, and shared learnings which provides 50% of impactful insights into optimal capital allocation using Gitcoin grants.|🟢 Community growth and participation were a huge success with non-gitcoin community members driving many efforts.|<br>* Enabled the community led curation of data sources for quality and usefulness.<br>* Collaboratively authored the landscape of useful tools and guides for Open Data Community.<br>* Catalyzed & lead creation of a platform to host the open data community including collaboration about tools, data sources and methodologies especially non-gitcoin participation documentation & bounties to create new analysis and turn validated analysis into legos<br>* Over 100 in Discord with 6 active (non-fdd)  contributors on Github<br>* Built a public facing data & research hub with all past grant round datasets with FDD|
|Find a sustainable strategy to engage ODC members and contributors to service decentralized grants rounds & maintain quality processes.|🟡 While we lowered the % of ODC costs which Gitcoin pays, we did not establish governance to run a grants round yet. This is partly because the protocol wasn’t ready this season. |<br>* Doubled prize total from $19k to $40k while Gitcoin/FDD is only paying 39% of it! (paid 100% last round)<br>* Added 6 sponsor orgs<br>* Contests hosted for unicef, fantom, and gitcoin alpha<br>* One previous hackathon participant was funded and returned as a Sponsor to the 2nd hackathon - They also provided services to the Fantom round outside of the hackathon.|
|Continuously iterate, test & innovate on algorithmic solution quality and availability.|🟢 We deprioritized much of the grant eligibility work due to the decision to have closed alpha rounds, but had multiple useful outputs from FDD research.|<br>* Bankless & Snapshot Analysis leading to 6 new legos<br>* Created a topology of stamps with recommendations<br>* Designed Cost of Forgery stamp weighting model<br>* Trial use of rhaphorty open source graphdb for graph analysis<br>* Building custom aura implementation for gitcoin grants and an gitcoin/fdd team to participate<br>* cadCAD round simulator - can be used to find optimality gap analysis and optimal red team strategies<br>* Design workflow pipelines for legos from ideation or behavioral observation through building|
|The right work gets done and the tools and access needed to do it is in order. We build plans for the future|🟡 The lego process was more difficult to scope and start but now since it is going it is moving well, we worked through many models for the future, but ended up needing the last week of the season to realize dissolution was the best answer. |<br>* Created a custom moloch DAO (on testnet) for a multisig allowing for true decentralization and potential spin out capability while separating Gitcoin funds to NOT be accessible by a ragequit<br>* Analyzed at all past FDD contributors pay, membership status, and contribution weeks to design a share splitting model<br>* Received a grant for sybil study of Aave onchain activity which overlaps with needs for Gitcoin<br>* Posted 5 FDD review articles<br>* Taught and/or transferred responsibility to Tigress treasury management and how to pay contributors|



**Legend**
🟢 Success
🟡 Incomplete, will hit goal or priority change
🔴 Incomplete, will not hit goal
⚫ Canceled - out of workstream's control


<br><br>
# Moving to a Protocol Future
The launch of the Allo Protocol will shift the needs of the Gitcoin community away from the historic goals of the Fraud Detection and Defense workstream. 

> *In pivoting into a new structure, FDD is preparing to support the break out into smaller and more end-to-end accountable workstreams, **without sacrificing the unified intention of the FDD: fraud defense, risk mitigation, and trust building.*** 

These smaller functional units eliminate any “I have 2 bosses” conflicts of interest. Individuals safe-guarding risk and trust priorities are embedded in end-to-end accountable working groups.

The core promise of the Fraud Detection & Defense workstream has been providing legitimacy & trust to the outcomes of Gitcoin’s quadratic funding rounds. This has been done by keeping quadratic funding rounds free from stolen and misallocated funds caused by sybil attacks and illegitimate grants. The continued improvement of our ability for clients using Passport & Allo protocols the ability to access and share this trust with their communities belongs **as a function** that is accountable with the program, product or engineering teams providing the trust. 

These functions of the current “centralized” organizational FDD structure will have moved over to other end-to-end accountable workstreams by the course of Season 17 to better reflect the future structure desired by stewards & Gitcoin leadership. We anticipate beginning to make these operational changes gradually with clear accountability shifts only happening after EthDenver, concurrently with the GPC workstream splitting into Passport & Allo streams. These changes are being made with the prior consent and partnership of the other workstreams involved. 

**This last season FDD has 3 key themes:**

**1️⃣ Continued Trust in Gitcoin’s Ability to Prevent Fraud**: Data informed recommendations to mitigate fraud are made continuously available.

* Fantom & Gitcoin Alpha Round Recommendations
* A Scalable Mitigation Sybil Solution Exists
* Sybil Defense Innovation & Insights Continue after FDD
* Passport has Analysis & Data Science Support
* Recommendations to Correct Web2 Vulnerabilities are Followed Through

**2️⃣ Empowering the DAO with Open Data, Infrastructure, & Processes**: Data processes & pipelines are reliably available & maintained.

* An On-chain Data Extraction Solutions that Meets the Needs of Real-Time Anomaly Detection
* Open and Decentralized Data Repository for the Community
* Gitcoin Analytic DB & Query Interface

**3️⃣ FDD Workstream Dissolution Success**: FDD contributors and work is smoothly transitioned and/or shut down.

* Successful Transition of Contributors
* Clearly Documented Closing of Accounts & Obligations
* A Proposal for a Ratified Process to Spin-Out “Investible Workstreams”

# List of S17 Outcomes
## 1️⃣ Continued Trust in Gitcoin’s Ability to Prevent Fraud

|Outcome Description|Essential Intent Connection|Likely Projects/Tasks|
|---|---|---|
|“What outcome or impact will we see?”|“How does this align with our most important work?”|“What will the work likely look like?”|
|Final recommendations are provided to the Fantom & Gitcoin Alpha rounds|Programs<br><br>Growth|Data extraction & cleaning<br><br>Computation of all sybil scoring legos available<br><br>Analysis of potential fraudulent behavior is drafted<br><br>Final recommendations for retroactive Sybil discounting|
|The tools & processes for a scalable sybil mitigation solution is available for program managers during the beta rounds.|Programs<br><br>Growth|Conduct historical analysis<br><br>Design dashboard essentials & highest impact visualizations<br><br>Finish building a round dashboard MVP<br><br>Earn consensus on policy shifts as needed<br><br>Collect user feedback on round dashboards<br><br>“Trusted Vendor” process solidified<br><br>Monitor April rounds and define opportunities for improvement|
|A flywheel of insight and innovation in sybil defense brings continued innovation & insights from the Open Data Community which reduces sybil behavior and improves Program Manager feedback.|Financial Sustainability|Insights are documented and included in fraud runbooks<br><br>Analyze ODC 2nd Hackathon submissions (e.g. www.grantlooker.xyz) and use potentially good submissions as inspiration for the further development<br><br>Builds are documented in Github for future use<br><br>Lowercost of iterative innovation for data infrastructure & innovation from the FDD workstream budget to bounties & membership costs.<br><br>ODC synthesizes learnings from the first three hackathons and provides documentation towards data standards and good practices in ongoing resource updates, useful to Gitcoin and the entire web3 community. <br><br>Freshly built legos get tested and applied to beta rounds<br><br>Testing reports including metrics on fraud tax are written in co-creation (ODC, Gitcoin Fraud Analyst) and shared with Gitcoin’s product & engineering teams.|
|Passport is supported with analysis & data science needs as they work to hire a new data analyst/scientist.|Protocols<br><br>Passport|Assistance in hiring and training of a data scientist to join the GPC workstream in S18<br><br>Updated score is provided<br><br>Retraining schedule is created for PSaaS<br><br>Update & adjust weighting before next season<br><br>Testing reports including metrics on fraud tax are written in co-creation (ODC, Gitcoin Fraud Analyst) and shared with Gitcoin’s product & engineering teams. <br><br>In case of success, stakeholders discuss how and when to implement legos.|
|Recommendations to correct web 2 vulnerabilities are made to respective product units.|Protocols|Define Opportunities & additional data pull needs<br><br>Monitor Google Analytics events during alpha round & analysis<br><br>Get feedback on recommendations<br><br>Correct web 2 vulnerabilities<br><br>Monitor core metrics for change with implementation|

## 2️⃣ Empowering the DAO with Open Fraud Data, Infrastructure & Processes

|Outcome Description|Essential Intent Connection|Likely Projects/Tasks|
|---|---|---|
|“What outcome or impact will we see?”|“How does this align with our most important work?”|“What will the work likely look like?”|
|An on-chain data extraction solution is developed providing speed, transparency, reliability, cost efficiency, and auditability gains.|Programs|Settle on tech stack<br><br>Erigon archival node for ethereum chain data<br><br>Trueblocks node with custom Chifra Server<br><br>Define core heuristics<br><br>Share with partners for testing<br><br>Define contract/protocol anomalies<br><br>Set up a Service Leasing Agreement (SLA) with Open Data Community to run the Gitcoin Open Data Stack<br><br>Begin serving up chain data via Rounds Dashboard & GitcoinDB|
|An open & decentralized data repository with all round data is consistently updated for the entire Gitcoin community.|Programs<br><br>Growth|Discovering scope of repository project in co-creation with Gitcoin<br><br>Builds an MVP similar to the fddhub.io but hosted by the open data community and updated with new round data<br><br>To ensure continued support and availability a service agreement for continued data infrastructure support is defined and agreed upon between Open Data Community and Gitcoin.|
|A Gitcoin Analytic DB & query environment empowers analysts across all of GitcoinDAO to become more data driven||DB design discovery - Tech stack / tooling research<br><br>Continue build in progress<br><br>Metric discovery in partnership with all workstreams<br><br>Financial Dashboards w/ DAOops<br><br>Partnership health w/ PGF Partnerships<br><br>Product Goals w/ Allo & Passport<br><br>DevRel Goals w/ DevRel<br><br>User Activity w/ MMM<br><br>Modeling for GTC utility to design a more costly to attack than defend system<br><br>Solve hosting questions - gain home for SaaS charges<br><br>Begin surfacing key on-chain signals in query environment|

## 3️⃣ FDD Workstream Dissolution Success

|Outcome Description|Essential Intent Connection|Likely Projects/Tasks|
|---|---|---|
|“What outcome or impact will we see?”|“How does this align with our most important work?”|“What will the work likely look like?”|
|Successful transition of contributors with offered and accepted roles to other workstreams allows the completion of FDD work and the smooth assimilation to new roles.|DAO Organization|Transfers are communicated with other workstream leads, introductions are made, and formal transition dates & compensation agreements are set.<br><br>Data Analyst > Allo<br><br>Fraud Analyst > Program Readiness (PGF)<br><br>Data Analyst hiring support > Passport<br><br>Other TBD = Data Engineering, Technical Writer, Financial Analyst<br><br>Successful handover: FDD work is either completed or transitioned to new workstreams|
|Clearly documented accounting winddown of all FDD wallets and financial obligations.|DAO Organization|All FDD multisig wallets are closed<br><br>Severance is paid where necessary<br><br>Exit interviews are conducted in partnership with DAOops<br><br>Transparent budget is available for review w/ audit|
|Proposal to create a CSDO-ratified process for spinning out “investable workstreams” exists to help Gitcoin avoid the “services trap”.|Financial Sustainability|In cooperation with DAOops create a positive sum model / process for de-risked, legally viable, and minimally disruptive investible spinout of workstreams.<br><br>Discovery around unanswered or uncertain aspects of workstream dissolution is conducted leading to ratified solutions which are safe to try.<br><br>Recommend a “spinout architecture” including literature research on legal wrappers and tech solutions<br><br>Craft a “spinout process” to transfer ownership and funds|





<br><br>
# Budget Breakdown
The FDD Season 17 budget is almost $10k lower than Season 16. Additionally we will not be requesting reserves for S17.

|Budget Category|Description|Amount USD|
|---|---|---|
|7 Core Contributors|**WS Leads**<br>Product / Strategy (Joe)<br>Operations (Tigress)<br>**Full Time Contributors**<br>Data Scientist (Omni)<br>Sr. Fraud Detection Analyst (Alex)<br>Data/DevOps Engineer (Zen)<br>Data Analyst (Bella)<br>OpenData Community Project Lead (EPowell) |$241,639|
|3 Trusted Contributors|FDD Review & Science SME (J-Cook)<br>Data Analyst (Adebola)<br>Analyst (Sorana)|$27,300|
|2 Regular Contributors|Software Engineers (Eric & Yogeesh)|$24,375|
|Open Data Hackathon|Bounties / Prizes|$30,000|
|SaaS, Fees, etc.||$3,000|
|Travel & other expenses*)||$14,000|
|Other Bounties||$0|
|**Total**||**$340,314**|

*) *Includes Gitcoin Retreat, EthDenver or similar events & travel reimbursements.*

<br><br>
# Footnotes in Conclusion and Looking Forward

With the DAO Data-related outcomes described above, we intend to provide data insights for protocol-based and transparent DAO operations. We have the skills and the opportunity to codify certain best practices. We also believe past learnings from best-in-class sybil defense have led to several key opportunities for automation, tooling, and experimentation.  

> *As we prepare to better utilize data for FDD aims, we see a necessity of building out the data capacities of the whole DAO alongside us, and it no longer seems efficient for FDD’s data resources to operate in silo.*

Can Gitcoin be the new, more secure, and more trusted GoFundMe?  Can we correct the issues inherent in early web2 projects like Kickstarter & co?  We believe so.  But to be ready for the new challenges which come from a wider audience, we have to invest in tooling and the necessary infrastructure now in order to carry out the promise inherent in an on-chain, trustless grants system.

It is, of course, the case that Gitcoin is not alone in these essential needs to secure our protocol and protect our governance practices.  We have heard repeatedly from our partners – new and long-standing – that it is necessary for other DAOs in the ecosystem to have the tools and the knowledge available to protect their own environments. Because of the growing demand for such services, it is thought to be well-validated that the DAOs Growth unit can spinout and begin seeking payment for more generalized “trust-as-a-service” as an a la carte consulting product, as well as providing this service which can be added to the most vulnerable grants rounds ad hoc.



---

***Authors of this Document***
|Section|Author(s)|
|---|---|
|Milestone Report|Joe|
|TL;DR|Joe|
|FDD Outcomes|Joe in collaboration with Stewards and FDD contributors|
|Amount, Budget Breakdown|Tigress with support from Joe|
|Footnotes in Conclusion and Looking Forward|Alex|

-------------------------

shawn16400 | 2023-02-01 10:13:23 UTC | #2

Thanks @tigress for posting this - your reviewers to this proposal are @kevin.olsen @drnicka @eugyal  @farque65 @llllvvuu  @ccerv1 @lthrift

-------------------------

ccerv1 | 2023-02-03 19:48:39 UTC | #3

First off, let me say that I deeply admire this team's intention to work itself out of a job this season and to distribute itself across the DAO and the broader ecosystem. This is admirable and a clear sign of true mission-alignment.

Second, given the intention to dissolve, I am highly supportive of a transition season that not only enables the services provided by FDD to be refactored / relocated but also gives the people reasonable time to find their footing elsewhere in the DAO or the broader ecosystem.

**For these reasons, I am supportive *at a high level* of both the proposed outcomes and the amount of budget requested by FDD for S17.** 

That said, I have some more specific feedback that I would like to see incorporated in the final request, which I will share below.

#### 1. The three themes read as goals for FDD contributors, not the DAO. 

The current themes are: 
1. Contributor Transition Success
2. Dissolution Governance Success
3. ODC Project Value to Gitcoin

I would prefer to see a clear statement of where the DAO should head and how this team will contribute to getting it there.

For instance, this is a great first theme to anchor on: 
[quote="tigress, post:1, topic:12738"]
building out the data capacities of the whole DAO
[/quote]

Another theme, not explicitly mentioned, might be: "ensure Sybil attacks do not detract from the QF experience for round managers and grants" 

A third theme could be "bootstrap a community outside Gitcoin to contribute to Sybil defense on the protocol".

#### 2. The outcomes feel arbitrary and inward-looking

This may sound overly harsh, so let me provide some examples:
> 5 or more legos discovered or built during the 2nd ODC hackathon are used during the beta round fraud analysis

If I'm a round manager, I don't care how many legos it takes or where they came from. I care about Sybil attacks manipulating my matching pool. I care about projects feeling unhappy about the allocation. I care about honest users complaining on Twitter that they couldn't donate or their votes were squelched.

(aside: I believe there is a HUGE role for data analysis and new legos / algorithms to play in improving the round manager experience, but those are the means to an end, not the ends.)

Similarly, all of the **Contribution Transition Success** outcomes in the form "transitioning [..] from FDD to [...] team" do not feel demand-driven. Again, I strongly believe there are highly valuable skills among FDD members that should be absorbed elsewhere in the DAO! But a successful outcome should be framed from the perspective of the DAO and its partners accomplishing something, not a contributor finding a new home.

#### 3. ODC activities / outcomes don't make sense here

As per my earlier point, I am very supportive of a theme along the lines of "bootstrap a community outside Gitcoin to contribute to Sybil defense on the protocol". I am also supportive of budget going to outsource or bounty work through ODC.

But it feels disorienting to have a DAO goal be, in effect, to prove that another DAO is valuable to Gitcoin.

***

# tl;dr 
I am supportive of the overall budget. I share the goal of ending this season with every current member of FDD finding a new home within a Gitcoin workstream, in ODC, or in some other entity that is highly complimentary to Gitcoin. But I would like to see some crisp, more measurable outcomes to this transition season that are framed from the DAO's perspective.

-------------------------

griff | 2023-02-08 07:46:09 UTC | #4

Wow, a graceful exit. Thank you for recognizing the market conditions and the fact that this is not the right timing to invest in the epic research that the FDD is known for. 

Thank you for your work in the previous seasons, i don't think Grants would have the legitimacy it has without your work.

I'm in general supportive of this proposal, but I want to ask every work stream... what would happen if this proposal didn't pass? 

Not fear mongering, just a practical reality. What would "No" look like?

-------------------------

lefterisjp | 2023-02-08 11:06:38 UTC | #5

To everybody else I would vote abstain or No. But for this since it's an exit of FDD as a workstream with a nicely laid out plan I am inclined to vote FOR.

-------------------------

kevin.olsen | 2023-02-08 12:21:13 UTC | #6

The response from Carl regarding framing was spot on, and in particular, I resonated very strongly with:

[quote="ccerv1, post:3, topic:12738"]
Again, I strongly believe there are highly valuable skills among FDD members that should be absorbed elsewhere in the DAO! But a successful outcome should be framed from the perspective of the DAO and its partners accomplishing something, not a contributor finding a new home.
[/quote]

It would be very helpful to know what a successful transition looks like, what the timeline for transition looks like, and what would a successful end state look like.

Regarding the proposal for a data workstream:
[quote="tigress, post:1, topic:12738"]
A proposal for a “thin” project based DAO data workstream is ready for Season 18 budget reviews.
[/quote]

I'm not supportive of this line item and feel it's heading in the wrong direction. This is a purely functional workstream vs. an end-to-end accountable workstream. I would prefer to see budgeted work embedded in the workstreams, but encourage non-budgeted organizational structures that span workstreams (i.e. guilds, or communities of practice).


### Given our budgets don't come with a BATNA, I would want to quickly explore that here: 

Given the FDD has reserves for 2/3 of the next season, this budget is really just a request for the final 1/3 of the season. 

If this budget wasn't passed, what would happen?

For Contributor Transition, given the current needs in the DAO for the analysis work to happen across Growth/Allo/Passport I think any workstream that is planning to absorb FDD'ers could support the contributors joining in S18 out of reserves. I see little impact if 2 mo or 3 mo of budget is available to support this transition.

For ODC I'm unclear what 2 mo vs 3 mo of further incubation in the DAO would yield.

For the Dissolution Governance requests I'm unclear what would not be delivered in 2 mo vs 3 mo.

To help Stewards make this choice. I think it would be helpful to clarify what the choice is between (2 mo vs 3 mo) and what would change in the S17 FDD output given either of those outcomes.

-------------------------

ale.k | 2023-02-08 19:42:26 UTC | #7

[quote="kevin.olsen, post:6, topic:12738"]
It would be very helpful to know what a successful transition looks like, what the timeline for transition looks like, and what would a successful end state look like.
[/quote]

This is helpful! And thanks, as always @ccerv1 for high level direction - 

@disruptionjoe @tigress I think it sounds like we can definitely incorporate better the key deliverables (with clear value props) for the DAO will be in place; 30-60-90 - to help parse this decision.

Top of mind for the longer term projects in flight: 
1) Best in class on-chain analysis tools so that Gitcoin can not only provide elegant protections against sybils, but also serve our greater needs of grantee transparency and reputation-assessment long-term.
2) Dashboards, core metric design + results of user research from our alpha partners: How do they want to do sybil defense? What are they willing (and unwilling) to do internally- and where does sybil defense rank in their priorities? 

Both of these are currently underway - and can be accelerated if we accept certain trade-offs - but given that there are lead-time contingencies which are outside of FDD control (e.g. the time to sync an archival node is ~3 weeks) - let's be really clear about the time commitments we need to do an excellent job - and also honest about when analyst + data eng attention can fully be focused on the new initiatives of the workstreams they're absorbed into.  I think we should articulate where we are now and what key milestones will have been achieved throughout the season.

(renewing my lucidchart trial now :sweat_smile:)

-------------------------

DisruptionJoe | 2023-02-09 20:12:43 UTC | #8

# Update

We will be updating to a revised version incorporating feedback on Friday, 2/10.

-------------------------

kyle | 2023-02-10 17:03:46 UTC | #9

I just want to chime in that I really appreciate the consideration and direction FDD is proposing. I am supportive of the general path and look forward to revised budget version coming out soon :)

-------------------------

ccerv1 | 2023-02-12 00:15:53 UTC | #10

I'm in support of the **updated** budget and proposal that @tigress and @DisruptionJoe have posted at the top of this page. Thank you for incorporating feedback from me and other stewards.

(For readers, ICYMI, the original budget post has now been updated to a new one ... so note that all the comments above this comment were in reference to the original budget, not the updated one.)

And ... I do think @kevin.olsen raised a good point that's worth addressing in the comments about the incremental value of a 2 vs 3 mo transition. It's not a sticking point for me, but may be helpful for other stewards to consider.

-------------------------

DisruptionJoe | 2023-02-13 13:06:44 UTC | #11

On one hand, it seems at first like we are talking about 2 months vs 3 months of funding. In reality, we are talking about a much bigger difference. I will try to break it down here.

### Fund the budget
* Finish ongoing work which is needed to successfully set the infrastructure which will support the analysts that move into the other workstreams.
* The people in FDD have the time to transition whether they are continuing in another workstream or moving on.
* We collectively celebrate a governance success as FDD completes work and smoothly transitions.
* Will cost the DAO $125k

### Don't fund the budget
* Confused contributors unsure about their transition will make finishing work unlikely or difficult to predict.
* Some would likely qualify for a severence and would need to end their work immediately for us to fund it.
* Loss of trust of contributors in other workstreams to see that Gitcoin has their best interest in mind. 
* Unknown losses in knowledge transfer to newer FDD members. 
* Will save the DAO $125k

Going into the Unicef, Fantom, and Alpha rounds we were told they would not need fraud analysis for these rounds. We were prepared anyway and have been working directly with Fantom to make sure they have all the knowledge to make choices that build trust with their community. 

This work required FDD contributor experience and skills to gather the data. This data gathering process even helped us to troubleshoot protocol issues with GPC as we learned how the protocol was setup. We found issues such as the need for timestamps with contributions. These weren't originally on the subgraph, but they are necessary for fraud analysis. We had the ability to scrape the ceramic nodes when product was way to busy fixing issues. We did this to better understand Passport effectiveness. We are currently doing data operations work for the Alpha round and the analysis will follow. This data operations/engineering example is only one that illustrates this issue. 

At this time, FDD works as a team with specialist strengths boosting the abilities of the others. To successfully transition, we need to move from this working culture to one where more generalist capable analysts are embedded in the workstreams. We are lucky that much of FDD's past work is at a point where we can finish building systems that will 10x the output & accuracy of the analysts who continue the fraud detection & defense work for Gitcoin. 

***Without clear transitions for the contributors, it is unclear which necessary skills we might lose.*** 

### A look at context and dependencies

We have some work that is ongoing which has context and dependencies which I don't think would be easy to manage through an abrupt transfer. 

This 30-60-90 milestone diagram shows a few of the deliverables listed above which have high context & dependencies. This work is the most likely work to be disrupted. It is also the work that will best set up the DAO for a data informed future with the analysts in each workstream empowered by having the right tools and processes. 

![Image 2023-02-10 at 10.35.30 AM|690x471](upload://bPX3TYS7DINkKhWkfaLnSPyAqFd.jpeg)

### My personal opinion & bias

As an FDD workstream lead, you can see there is obvious bias likely to be present in my opinion. However, if you consider that I am the one putting forth the idea to dissolve FDD for the better of the DAO, then perhaps my motivation is pure. Especially when you consider that I am one of the FDD contributors without a clear transition. There are currently 3/9 who have fairly certain transition plans, and 5/9 who I believe have clear and obvious paths forward. 

I personally want to see Gitcoin succeed. I am a stakeholder not only as a contributor, steward, and user, but also with substantial personal "skin in the game". My honest advice to the stewards would be to approve this budget. 

FDD has protected the community from $3 million in fraudulent allocation of funds over the last year and a half. This move to dissolve FDD is not because fraud detection & defense is no longer needed. It's exactly the opposite. ***We have the opportunity to setup the infrastructure, processes, and tools needed to empower the analysts working with the end to end accountable workstreams. This effort might not happen if this transition is not managed well.*** 

To me this is not a question of 2 or 3 months of work. It is 3 months of work with smooth transitions for both those staying with Gitcoin and those moving on OR confusion and difficulty rallying the team to do their best and complete the work that sets up  future protocol and program success. The work we do this season IS part of Gitcoin's most important work. I encourage stewards to provide us the opportunity to show the entire web 3 ecosystem that
* Gitcoin governance is working 
* The next 100 grants program managers can be absolutely sure that using Gitcoin gives them trust, legitimacy, and credible neutrality in funding what matters.

-------------------------

ccerv1 | 2023-02-14 00:31:08 UTC | #12

Agree. From my perspective, three months is a reasonable transition period. Mitigating the downside in terms of morale / unintended skills loss is more important than a once-off cost savings. Furthermore, I respect that FDD went straight to proposing a transition season (as opposed to, say, proposing a normal S17 and pushing the dissolution question further on down the road). 

I'll state it again: this budget proposal has my support.

-------------------------

JR-OKX | 2023-02-13 20:51:34 UTC | #13

I really like the two longer term projects you mentioned, and we are already in conversation on how we can help re: the on-chain data analytics project. Three quick questions on this initiative with consideration to the dissolution context of FDD, which might be in many people's heads as well

1. How would on-chain analytics help other work streams? Any potential synergy between this part of FDD and Gitcoin passport (has web2 credentials)?
2. Once certain on-chain analytics tool is employed (assuming quite some work and follow-ups and maintenance are needed), who/which party would be held responsible to generate insights and crystallize into action items if FDD members are spread out across work streams? 
3. A follow up question would be are there going to be occasionally check-ins as a team to align on the shared topic? How would this look different to the working style prior to dissolution?

On high level, this proposal has my support. Thank you for all your hard work in previous seasons and working on legitimacy of Grants. 3 months of work also seem justified to me considering the work and commitments leading up to Eth Denver in about a month.

-------------------------

kyle | 2023-02-14 02:59:56 UTC | #14

Thanks for the updates. 

I am still likely to support this budget, but I am slightly confused at the continued build out and support with 7 FT contributors. I don't know what **actually** lives on for those analysts that are embedding in the teams. 

Regardless, I do trust the team to suss out what they need, and hopefully @ale.k and others are pushing for things they can leverage and maintain on-going.

-------------------------

DisruptionJoe | 2023-02-14 03:15:50 UTC | #15

We have strategically setup an FDD edition of the community call this Wednesday at 12pm EST / 5pm UTC. This call is open to all DAO Citizens in the Discord. Here we will be showing the Open Data Community's 2nd hackathon results and discussing the future of protocol based fraud defense. 

Here are some of the topics we will likely cover:

* Growth of the Open Data Community (ODC)
* How Ongoing Goals of the ODC Will Help Gitcoin
* Showing Off the Best Submissions
* Discussing Open Data Infrastructure
* How the New Data Infrastructure Benefits All Workstreams
* Q&A 

I'll let @ale.k chime in as to how the work of Season 17 will live on an benefit the analysts which transition.

-------------------------

tigress | 2023-02-14 19:48:40 UTC | #16

Proposal updated to INTEGRATED status.

Thank you! 🙏

-------------------------

ale.k | 2023-02-15 01:14:52 UTC | #17

Hey @JR-OKX - thanks for the thoughtful follow-up!  We really foresee enterprise-level data abilities to be a huge need for multiple initiatives around the DAO - certainly going well outside of fraud-fighting and systems design for risk mitigation, as you call-out.

> 1. How would on-chain analytics help other work streams? Any potential synergy between this part of FDD and Gitcoin passport (has web2 credentials)?

Yes to synergy, to be sure! Passport use and roll-out by our partners definitely presents a rich opportunity to see the success (and the failure) of various stamps in safeguarding many communities with diverse needs. We have already been asked for recommendations from early partners in this capacity, and we see the work FDD has done in creating scores and training models to be something where there will be an ongoing need. An example of this is the good initial results in predictive nature of a model that maps stamp-attainment to average donor spend.

Outside of the Passport product team, we also see several mission-critical initiatives to be reliant on on-chain data and a final-state permissionless postgres solution. Examples of this include one of the top things we heard from donors during alpha rounds: They want to see their own donation history.  Another example where data infra is pivotal to our success would be in providing indicators of Grantee reputation and tracing grant-awarded funds over time. We are building in a way which will make this kind of data not only available internally, but available for public audit at any time.

> 2. Once certain on-chain analytics tool is employed (assuming quite some work and follow-ups and maintenance are needed), who/which party would be held responsible to generate insights and crystallize into action items if FDD members are spread out across work streams?

I think I addressed this a bit above in terms of ownership of future insights, and how these initiatives may live within product teams as needed.

As far as the ongoing maintenance need - on-chain data will actually be by far our lowest-lift on an ongoing basis, and node maintenance the smallest fee (less than 20 USD/monthly currently scoped).  Through the peer-to-peer sharing method pioneered by the OpenSource indexing project TrueBlocks, our on-chain data will only improve with more users.

More generally, we do see the full-time Data Engineer (@zengatsu) serving a role which will be billed similarly to how DevOps has been billed of throughout the DAO: each workstream who depends on such services absorbs part of the salary and SAAS costs.

> 3. A follow up question would be are there going to be occasionally check-ins as a team to align on the shared topic? How would this look different to the working style prior to dissolution?

Excellent question and I think we're all curious how this is going to shape up in practice :sweat_smile:  We welcome any ideas or best practices in terms of "guilds" and similar formations where we might have formal specialties imbedded in product teams...

-------------------------

shawn16400 | 2023-02-15 10:51:26 UTC | #18

In case you missed it - this proposal is now posted on Snapshot for vote.  The vote closes on Tuesday Feb 21 so be sure you vote before then. 

https://snapshot.org/#/gitcoindao.eth/proposal/0xf185198f0b0b7dacfcfd0e25d6129ed2b8a2fa40e5f527c38e966ebad0417284

if you have any issues voting, please ping shawn16400#5507 in discord for assistance.

-------------------------

linda | 2023-02-16 23:25:34 UTC | #19

I voted yes on this proposal given the assigned steward reviews and that it’s reasonable to have a transition period/budget.

-------------------------

lefterisjp | 2023-02-19 23:02:53 UTC | #20

I also voted yes as per my previous comment. I like the way you guys are handling this and the transitional budget is reasonable.

-------------------------

kyle | 2023-02-22 01:32:20 UTC | #21

[quote="tigress, post:1, topic:12738"]
|**Total**||**$340,314**
[/quote]

Hey @DisruptionJoe - I wanted to confirm this is the amount in total FDD needs to operate for this season?

I see that based on currently market values, FDD has two gnosis safes:
1 - [Gitcoin Fraud Detection & Defense (Main)](https://www.tally.xyz/safe/eip155:1:0xD4567069C5a1c1fc8261d8Ff5C0B1d98f069Cf47) starting with (0xD45) and has a balance of 361.72K USD
2 - [Fraud Detection & Defense (ops)](https://www.tally.xyz/safe/eip155:1:0xbc4C3D4c6cCA25d5704b6d6841BA75882b8F061B) starting with (0xbc4) and has 83.16K USD

The total seems to be in excess of the $340k requested for the season (and offer a healthy reserve). Does this mean you don't need to request any funds this season?

-------------------------

shawn16400 | 2023-02-22 08:23:19 UTC | #22

This snapshot vote has passed with ~93% approval rate.
Metrics:
1171 unique votes
~13M GTC tokens cast.
@kevin.olsen @drnicka @farque65 @llllvvuu @ccerv1 @lthrift and @kyle thanks to all of you for agreeing to do a deep dive review and provide feedback.  
https://snapshot.org/#/gitcoindao.eth/proposal/0xf185198f0b0b7dacfcfd0e25d6129ed2b8a2fa40e5f527c38e966ebad0417284

-------------------------

DisruptionJoe | 2023-02-22 14:03:13 UTC | #23

That is not correct. The vote was to fund the season 17 budget less the 100% of reserves which are being rolled over. 

If there is a governance agreement about a workstream acquiring extra funds, please point me to it.

-------------------------

kyle | 2023-02-24 19:47:55 UTC | #24

[quote="DisruptionJoe, post:23, topic:12738"]
about a workstream acquiring extra funds
[/quote]

What do you mean by this?

I am just trying to figure out if you all actually need funding given the amount you hold across the two multisigs?

Is some of that Grant money from Aave that should be excluded here?

-------------------------

DisruptionJoe | 2023-02-25 14:00:26 UTC | #25

Yes, and over the course of the last year and a half, FDD has made good treasury decisions. We accurately report our seasonal reserves to roll over and request the difference. This request is to fund our S17 budget of $340k. 

In the past we have used these "gray funds" sparingly. For example, last season we had great breakthroughs with time-series graph database analysis with a payment to Pometry for setup and example uses of their open source Raphorty DB. This was not on our original budget. 

The gray funds have been a way for us to maintain some autonomy in getting things done when needed. At the end of this season, we will wind down the workstream entirely. We believe we should have autonomy in using those funds. They will first pay for severence for those who are put out of work by the dissolution and secondly be put to use further advancing our sybil defense capabilities. 

We want to push innovation forward, not just for our mandate, but for the DAO which desperately needs some innovative governance experiments which aren't choked off by top delegated stewards not having the bandwidth to decide how to manage them. Because we believe these funds are separate from the quarterly budget request, we believe we have the autonomy to choose how they are spent. 

Our current plan is to setup a Quadratic Vote for stewards to decide how much is allocated to 1) sending back to treasury  2) conduct a jokedao contest for sybil innovations  3) grant to Open Data Community as Founding Member to a subDAO structure   4) Fund FDD as a MolochDAO for ongoing independent services. Maybe there are other options. We would then follow through the execution of the results. This would happen after EthDenver and before 4/28, the end of Season 17. 

Here are a few other reasons why we think ensuring FDD gets this budget is both a legitimate and smart decision. 

1) The treasury decisions weren't primarily gains in the last quarter. 

2) Saying no after the vote is shady. We did not hide our current holdings this season as we dissolve. We reported accurately and consistently as we always have. 

3) The secondary effect of taking workstreams autonomy to do as they will with funds they acquire will demotivate them from being creative in becoming sustainable. Why would a workstream do any treasury management? Why would they attempt to get outside grants?

4) CSDO discussed sending funds back to the treasury. However, that is CSDO which is an opt in council representing how workstreams will work together. All of the workstreams have opted out of CSDO recommendations in the past, so why is FDD opting out of this one different.  The entire point of CSDO is that it IS NOT governance sanctioned by token holders. It should only make OPT-IN decisions that require the decisions about workstream collaboration to not be enforceable. This means the decisions have to be good enough to opt in. Saying that a CSDO decision has the same value as a token vote would upend the entire structure of CSDO, its purpose, and its intended outcomes. It would also directly violate the foundation agreement for token governance as the decision making power. Of course workstreams can make decisions within their workstream or between workstreams if it doesn't break any steward voted policies or require their releasing funds. CSDO is bottom's up, soft power. 

## Conclusion

It seems like there are 2 choices:

1) Follow through with the vote. Maintain integrity and consistency. FDD finishes the season working hard and gets the rest of the DAO inspired with some governance innovation and the gray funds going to continuing our mission. 

2) Cancel or overturn the vote. Lose integrity. FDD members not moving forward likely have to stop working on 4/1 (or earlier) so we can pay severance. FDD is able to return a minimal amount of what's left < $20k. No extra governance innovation. No funds being jointly allocated by stewards and FDD for continued sybil innovation after dissolution.

-------------------------

griff | 2023-02-25 22:58:59 UTC | #26

Love ya Joe, but i don't get it. 

The plan is to end the workstream.

You outlined a budget to do that.

Turns out there was an accounting oversight and you have more then enough money to do the proposed budget.

Why should the DAO send an extra 123k to a workstream that is ending, when you are holding an excess of 100k already to complete your stated objectives?

[quote="DisruptionJoe, post:25, topic:12738"]
Saying no after the vote is shady. We did not hide our current holdings this season as we dissolve. We reported accurately and consistently as we always have.
[/quote]

![Screen Shot 2023-02-25 at 3.44.47 PM|690x230](upload://wcIWRjC0EpWGk67upWX8Ra078k8.png)

It says the season reserves are $216k.... but....

[quote="kyle, post:21, topic:12738"]
I see that based on currently market values, FDD has two gnosis safes:
1 - [Gitcoin Fraud Detection & Defense (Main)](https://www.tally.xyz/safe/eip155:1:0xD4567069C5a1c1fc8261d8Ff5C0B1d98f069Cf47) starting with (0xD45) and has a balance of 361.72K USD
2 - [Fraud Detection & Defense (ops)](https://www.tally.xyz/safe/eip155:1:0xbc4C3D4c6cCA25d5704b6d6841BA75882b8F061B) starting with (0xbc4) and has 83.16K USD
[/quote]

This shows you have $444.88k.

Maybe you weren't hiding it but it seems like inaccurate reporting. It's fine to have an accounting error, but it is very pertinent to this request and **IMO it invalidates the vote,** as the vote was for money needed to complete tasks outline here, which you have more than enough money to do... So now you are now requesting funds you don't need.  


[quote="DisruptionJoe, post:25, topic:12738"]
Cancel or overturn the vote. Lose integrity. FDD members not moving forward likely have to stop working on 4/1 (or earlier) so we can pay severance. FDD is able to return a minimal amount of what’s left < $20k. No extra governance innovation. No funds being jointly allocated by stewards and FDD for continued sybil innovation after dissolution.
[/quote]

This doesn't make any sense man, you have the funds to complete the proposed plan without the $123k injection.  Please do right by Gitcoin DAO and use the funds in the workstream for their intended purpose and don't follow thru with a push to request this funding. You have 100k more then you outlined you need to complete your stated work... why do you need another $123k on top of that? 

IMO the workstream is funded and Gitcoin DAO needs to conserve its resources. 

We should probably revote given the new information.

-------------------------

J9leger | 2023-02-26 18:12:04 UTC | #27

Going through this conversation and overall I'm confused about a couple things:

> The gray funds have been a way for us to maintain some autonomy in getting things done when needed. At the end of this season, we will wind down the workstream entirely. We believe we should have autonomy in using those funds. They will first pay for severence for those who are put out of work by the dissolution and secondly be put to use further advancing our sybil defense capabilities.

No other workstream has gray funds and this is something we've never heard about before. Could we have full transparency about these gray funds?

The workstream has funds already to do all the things that are mapped in the budget. Revoting makes sense to me and not fund anything beyond that makes sense to me.

-------------------------

chaselb | 2023-02-26 22:44:35 UTC | #28

Here's what I *think* is going on (hopefully Joe can clarify further):

Through smart treasury management and other means independent of the work of Gitcoin, the FDD workstream was able to amass some funds extra to that given to them by the GitcoinDAO. I believe Joe is arguing that these "gray funds" should be used at the discretion of the FDD Workstream, and should not be included as pertinent information in FDD's budget request from GitcoinDAO.

Whether or not one agrees with Joe on this is a function of how they view the workstream-DAO relationship (which is currently ill-defined, and is something we should try to define better in the future to prevent problems like these).

For example, if the "Workstream" is an autonomous unit that GitcoinDAO grants money in exchange for some future work, then Joe's point is valid. We should not expect the "Workstream" to do work on behalf of GitcoinDAO with funds that were not given by GitcoinDAO. In the context of this budget, under this assumption of a "Workstream," then FDD should receive DAO funds because they are doing DAO work. If they do not receive DAO Funds, then we should only expect from them work that can be compensated by the DAO Funds they have in reserve (NOT their "gray funds").

However, if the "Workstream" is bound to GitcoinDAO in the way a corporate division is bound to the larger corporation, then Joe's point is invalid. All funds made by a corporate division belongs to the corporation itself, and is relevant to all funding decisions of that corporation. To be honest, I don't think anyone in GitcoinDAO thinks of a workstream like this.

Another possibility (and perhaps the most likely) is that the "Workstream" is somewhere in-between, without a clear precedent. However, even if we do not explicitly state it, we are defining this precedent by choosing to revote or not.

Another important precedent we are setting is that of revotes. What constitutes a revote and what doesn't? There do not seem to be clear guidelines for this, which is unfortunate considering that our voting process is largely social (no automatic execution on snapshot, and automatic execution on-chain has to be pushed through by large delegates willing to pay the gas cost).

TL;DR:
We are setting two important precedents through the decision to revote and not fund FDD's treasury request:
1. What is the Workstream-GitcoinDAO relationship and expectation?
2. What constitutes grounds for a revote?

All stewards should carefully think about their answer to these questions before making a decision.

-------------------------

disruptionjoe1 | 2023-02-27 00:09:53 UTC | #29

Sorry for the short phone reply, but I want to clarify the WHY here. It is important. 

I do believe that Chase 2 questions are spot on. I am doing this because I believe there is an insecure gap in our governance. We need to be in challenging governance situations to learn if there is a delta between how secure we think we are, and what the onchain portion of the governance plays out. 

There is soft power that can say “I believe we should revote”. 

I’m saying “show me how governance actually enforces whatever it decides here”

AND “whichever way this goes, let’s see if the DAO governance we have today leads us to a smart decision for tomorrow.”

I do believe my claim is legitimate. Others don’t. Ok Governance, what happens next. Do people with soft power get to say we must revote. How does our governance today decide this in a fair way?

I led the grants reviews for 5 or 6 seasons. These are the type of questions that come up in grant disputes and appeals. Our next 100 ALLO program managers will need to help their communities solve this problem.  Not the specific law, but how does governance handle the process.  

1. Let’s look up the current state of our agreements. 2. Let’s have a thoughtful, careful debate on how and why this decision should go each way
3. Let’s make sure we get a great outcome (like we did with the Akita Balancer pool - A governance mega-win that was super inspirational)
4. Share the learnings of our practical governance problems in how WE allocate funds across our DAO and the ecosystem to help them fund what matters.

All I’m asking is how do we find a legitimate outcome? 

I do believe that my understanding is both legitimate, and the better decision for the DAO long term. 

Either way it turns out the funds will be spent in a way that pushes forward the DAO goals. My word and reputation is behind that. This isn’t that large of a sum. This low stakes way of testing governance seems like a good idea for us to learn our weaknesses. 

Worst case scenario, I wasted some time pushing the subject. Best case scenario, we truly learn if we have weaknesses in our current system and if we can learn from our experience about how to solve a problem that EVERY grant round has!

-------------------------

linda | 2023-02-27 05:18:01 UTC | #30

Echoing this sentiment. I think it's important to have full transparency around the workstream finances so all stewards are able to make an informed vote. A major difference in understanding the financial situation seems reasonable to me to have a revote (applies to any workstream, not just this situation).

-------------------------

disruptionjoe1 | 2023-02-27 05:54:53 UTC | #31

I appreciate your engaging. I do agree with your assessment. Then, I think who has a right to call a revote in the future? Do we have a legitimate process for determining if a revote request is valid? Could someone DDoS our governance by requesting a devote on everything? 

A clear and legitimate appeal process is a need of every grants round. I’d love for the conversation to be in good faith that we have two different positions presented that both might be legitimate. Who act as an appellate court in our system? Hopefully it’s not the person presenting the other side of the argument. Maybe it’s the steward council, with the people who are presenting each side committed to abstain. 

I was approached by multiple people saying there was some “heat” on the forum. 

It would be nice to have this conversation in the light-hearted fun way our leadership described governance could be at our retreat. It would be nice to hear “Great job, Joe. We have this money that wouldn’t have existed without your pushing boundaries and innovating in a responsible way. AND we are glad it is you and not someone actually testing our governance structure for malicious reasons.”

Really happy you chimed in here Linda. 

How might you suggest we make the decision whether a recite is acceptable or not?

Did you know that this is a pain point for program managers every single round since I have been a part of Gitcoin?

These program managers are coming to us and literally requesting to use the protocol the way Gitcoin does because we get trusted results. I have been the person that handled these appeal situations since round 8. 

Can our process here be something that doesn’t open the door to more problems AND is a step towards solving one of the primary problems our round managers have?

-------------------------

shawn16400 | 2023-02-27 14:58:50 UTC | #32

This is an interesting case which I think our current structure does not address.  What happens when a proposal has legitimately passed, but new information surfaces and voters no longer feel the information was symmetric?

We have to be careful here.  Good governance is about protecting against bad actions, but any incremental governance process is always at risk of increasing bloat, bureaucracy, and unintended consequences.   Unintended consequence I see popping up here is creating an appeal process that can be manipulated by actors who are simply unhappy with legitimate votes.  We must avoid this. 

This case is important, but I think it is more important to get the response right.  My sense is FDD does not need the funding right away, and I would propose we take a couple days to draft a process (based on a bit of research), bring it to the Steward Council for a quick review, and we trial the process with this case.  If the process proves to be just, we adopt it as part of our governance structure.  

I am happy to coordinate and welcome any and all contributors to the process in an active, passive, or observational sense.  I have created a thread in discord under "Cross Stream Pods" > "DAO success"  where we can hash it out.

-------------------------

chaselb | 2023-02-27 18:23:14 UTC | #33

[quote="shawn16400, post:32, topic:12738"]
I am happy to coordinate and welcome any and all contributors to the process in an active, passive, or observational sense. I have created a thread in discord under “Cross Stream Pods” > “DAO success” where we can hash it out.
[/quote]

Is this channel only open to contributors?

-------------------------

ccerv1 | 2023-02-28 14:37:27 UTC | #34

Just catching up on things here, but want to share several reactions.

As a steward, I am primarily focused on the question: "is this budget proposal a good use of DAO resources". 

I have not been concerned with the question "where will the funding coming from". To me, that feels like more of an implementation detail. It was my impression (perhaps incorrectly) that funding could be moved around across different multisigs if it needed to be.

Coming to @chaselb's two questions:

[quote="chaselb, post:28, topic:12738"]
* What is the Workstream-GitcoinDAO relationship and expectation?
* What constitutes grounds for a revote?
[/quote]

**1. What is the Workstream-GitcoinDAO relationship and expectation?**

I have viewed each workstream as a pod within the DAO that's granted a multisig and the autonomy to figure out how best to get things done. I have not viewed workstreams as service providers to the DAO. Personally, I don't like the idea of each workstream having its own P&L or the ability to accumulate a surplus that is then controlled by ... who? the workstream lead? current contributors? 

This could also create an incentive for workstreams to overestimate what they request from the treasury so they can build up their own reserves. That does not feel like something we should be messing with at a time when neither the DAO nor any of its workstreams has a revenue model.

Others may feel differently about this issue and I respect that.

**2. What constitutes grounds for a revote?**

We should revote if we feel we were not given an accurate picture of what's at stake in the original proposal. Proposal-generation and Snapshot voting are social coordination mechanisms. I don't see a reason to be rigid on this issue, but if revotes start happening regularly, it will definitely erode confidence in the DAO.

Judging from the comments here, a number of people appear in favor of a revote. 

Personally, I'm in favor of a revote because the $123K treasury request was presented as a requirement to meet the S17 budget of $340K. Had I known that the workstream already had $445K and was therefore projected to dissolve in three months with a net balance $228K [$445 + $123 - $340], then I would have voted differently.

***

Finally, let's not conflate the issues. It's important to articulate the intended financial relationship between workstreams and the DAO. It's also important to determine if / when a revote is on the table.

To Shawn's question:

[quote="shawn16400, post:32, topic:12738"]
What happens when a proposal has legitimately passed, but new information surfaces and voters no longer feel the information was symmetric?
[/quote]

We revote. Regardless of the explanation for why the information was presented a certain way the first time. And we vow to do better so it hopefully doesn't happen again.

-------------------------

DisruptionJoe | 2023-03-02 15:03:57 UTC | #35

# Let's Revote

First, I am seeing broader sentiment that requests the revote. I'm quite disappointed that there isn't more enthusiasm around finding a legitimate way to determine if a revote will happen. We have an opportunity to find a more legitimate solution - ***a solution EVERY ALLO PROGRAM MANGER NEEDS***.

We could direct power for revote to the steward council. For example, a Snapshot vote with the following options:
1. Revote 
2.  Have steward council decide if a revote should happen and set precedent for how revotes are made legitimate
3.  Keep the results of the first vote

I believe that either 1 or 2 would end up with the same results for this budget, however, 2 would be the better decision for the DAO. 

# Clarifications

### Regarding my Intent to deceive

[quote="kyle, post:21, topic:12738"]
Hey @DisruptionJoe - I wanted to confirm this is the amount in total FDD needs to operate for this season?

I see that based on currently market values, FDD has two gnosis safes:
1 - [Gitcoin Fraud Detection & Defense (Main)](https://www.tally.xyz/safe/eip155:1:0xD4567069C5a1c1fc8261d8Ff5C0B1d98f069Cf47) starting with (0xD45) and has a balance of 361.72K USD
2 - [Fraud Detection & Defense (ops) ](https://www.tally.xyz/safe/eip155:1:0xbc4C3D4c6cCA25d5704b6d6841BA75882b8F061B) starting with (0xbc4) and has 83.16K USD
[/quote]

This felt misleading to me. I had a specific one on one session with @kyle in December where we discussed that FDD has these funds AND that we were applying for an Aave grant. I suggested we should think about the Governance issues that would come up when we dissolved FDD. At the time, we both thought it wouldn't happen this soon, but it was explicitly discussed. 

Additionally, I did bring this up at a recent Stewards call and a Steward Council call. Yes, I didn't put this as material info on the budget request, however, no other workstream puts that info on their budgets nor is there an established norm across most DAOs. In fact, the norm is that everyone knows the info is public and proposers never put up how much they are currently holding. 

[quote="J9leger, post:27, topic:12738"]
No other workstream has gray funds and this is something we’ve never heard about before. Could we have full transparency about these gray funds?
[/quote]

Is this implying that I have been lying by omission? I don't know why you don't know about them. 
I have spoken about them at both CSDO and steward meetings in the past. Not only have I brought it up, I've called it out as a potential issue and that we should be prepared. 

[quote="ccerv1, post:34, topic:12738"]
Personally, I’m in favor of a revote because the $123K treasury request was presented as a requirement to meet the S17 budget of $340K.
[/quote]

As I understand, the budget request was only presented as a request for the DAO to fully fund our Season 17. 

If one believes that the DAO should control how the $228k in gray funds (That wouldn't have existed) are spent, then it is reasonable for them to think we should have reported them. 

If you believe those funds should be autonomously spent by the workstream (In line with the workstream's mandate), then you might not consider it as relevant to a seasonal budget request. 

Whichever of these opinions are right is up to the DAO. Hopefully, this helps clarify that this wasn't a deceitful thing to do on our part. 

I'm also quite surprised you didn't have previous knowledge that FDD had these funds. We do speak pretty freely about them in FDD and always have! 

### Legitimacy of workstream autonomy

In August 2021, I put up the first FDD proposal. It involved personal risk as I left the company and had little clarity on what the future would hold. The message from Gitcoin to the public at the launch of the DAO was that workstreams would be autonomous (DAO of DAOs). I was even told that it was 100% up to me if we incorporated, but they recommended we did. We pushed back, hired legal help, and defined FDD as an unincorporated non-profit association and designed contributor agreements. 

We've discussed workstream treasury management many times with the CSDO group. It was necessary! I remember @annika asking what she would do if the price of GTC dropped and PGF couldn't follow through on dollar based commitments to pay contributors. ***WE WERE EXPECTED TO DO OUR OWN TREASURY MANAGEMENT!***

Some of our workstreams had leadership that was hired by Gitcoin Holdings and paid to create proposals and create a workstream. GPC was transferred from the company to the DAO less than a year ago. I understand that many people would view our workstreams as departments in a corporation. I'm not here to say that they are wrong. 

***I am here to say that it shouldn't be unreasonable to consider my viewpoint legitimate considering the early risk I took and the experience I had.*** 

If it is a legitimate viewpoint, then our governance should have a process to solve the issue in which those with both viewpoints would consider legitimate - even if the result isn't in their favor. 


# Suggestion for next steps

***I could post the vote suggested at the top.*** This might be more legitimate than someone else posting it, but I don't feel too strongly about that detail. 

Mostly, I'd like every Gitcoin Stakeholder to know that we were proud to bring extra value to the DAO. This seems like a great decision to have to make!

If we moved forward without a revote, we were excited to do governance experimentation dogfooding the protocol and/or testing other allocation mechanisms to spend the last of the funds we would have had. Specifically, ideas like a QV round, a JokeRace, or Moloch implementations where the DAO would have ragequit capabilities if it didn't like the decisions made. 

It could help fund things like:
* Decartography PoC - Using DeSoc collusion dampening
* BrightID Aura Implementation
* Open Data Community Sandbox Sponsorship - Another node pinning relevant data from trueblocks 
* Sybil detection legos built using our findings from this last season with Pometry and their Raphorty open source time-series graph database.
* And many other great ideas! 

Rather than push for this vote to go the way I think it should, I'm pushing for it to be handled in the best way possible for the future of the DAO, even if it is against my personal opinion. 

I'd love to see people establish the steward council as having the power to call for a revote, followed by voting their fully informed present opinion on the topic. 

Perhaps, we could compromise by writing a new GCP for us to do the planned innovation experiments if the DAO were to give us the explicit approval?

-------------------------

chaselb | 2023-03-02 02:21:32 UTC | #36

I'm putting my support behind Joe on this one. I both agree with the need to create a governance process for these situations, as well as the argument that FDD has full autonomy and discretion over the funds they acquired outside of GitcoinDAO's involvement. I do not believe these funds are material information, and I do not believe we should conduct a revote. I DO believe, in the absence of a formal process for deciding whether or not to revote, we should create some temporary mechanism for doing so (such as pushing it to the Steward Council), and then workshop a more thoughtful mechanism for deciding whether or not to revote.

-------------------------

epowell101 | 2023-03-02 04:28:49 UTC | #37

Thank you Chase and everyone for your insights here.

I've been on the sidelines (for once!) in this discussion because I have a clear conflict of interest as I am very active as a founder of the OpenData Community which itself will likely be requesting resources from the DAO in the future and, more importantly, was started with the support and inspiration from FDD and from Joe specifically. 

That said - I would just like to state for the record that I think Joe has acted in good faith and that I have been in a number of conversations in which he freely shared that FDD has generated additional funds.

-------------------------

ZER8 | 2023-03-02 12:22:30 UTC | #38

I would like to start by manifesting deep appreciation for all the people that worked to build Gitcoin into what it is today. I deeply appreciate the work of  @kyle @J9leger @DisruptionJoe @connor @kevin.olsen @griff and others... without them Gitcoin would not be what be what it is today and I have so say I can't wait to see what it evolves into :robot: :evergreen_tree:

I would like to share my honest thought around the "issue" discussed in the last 20 or so comments and hope that by this I can provide additional clarity for those who seek it.  At first sight this appears to be a complicated subject because the more far away a Steward/Key decision maker is from the actual "action zone" the more inclined it would be to believe that Joe has omitted the existence of the "gray funds" , but this is a false premise because:

-as a formed team lead in the FDD I have always been informed of the existence of these funds, also every FDD member was aware of the existence of these funds, more so at certain points we were included and informed in all the decision making around them
-I have been in numerous public meetings(with other WS) in which Joe has proudly talked about them and the way that FDD managed to be very wise via good treasury management decision making
-**if he didn't care about the DAO and Gitcoin's mission so much he wouldn't have made the effort to protect funds via wise treasury management**

I respect that a lot of the Stewards have a limited amount of time(because they are doing valuable  work for all of web3) and it's hard for them to understand what's actually going on. The past two years have been filled with experimentation for the common-good, decentralization at almost every decision making level and also empowerment with the goal of growing the Gitcoin DAO. As the bull market ended, the macro has changed and it resulted in a relatively accelerated shift toward a more sustainable future for the DAO, it's is understandable, because ofc the biggest vulnerability a DAO  is...surprize..."human nature" :smiley: , but this should not create dissonance between all the great people working towards our collective PG future.

IMO the concrete fair way forward would be to continue to fund the FDD as indented because the information was not hidden and people voted yes to the budget, but unfortunately seeing how the conversation here took place and what the current state of affairs is I am worried that this would lead to dissonance between stewards and this is not the point, so  +1 to @chaselb viewpoint: 

[quote="chaselb, post:36, topic:12738"]
do not believe these funds are material information, and I do not believe we should conduct a revote. I DO believe, in the absence of a formal process for deciding whether or not to revote, we should create some temporary mechanism for doing so (such as pushing it to the Steward Council), and then workshop a more thoughtful mechanism for deciding whether or not to revote.
[/quote]

As in life these challenges appear and can lead to an even stronger DAO, it will be very interesting to see how Gitcoin DAO handles this particular one as it seems to be quite complex and provoking at first :robot:

I also know for a fact that the last 2 years have not been easy for all the Gitcoin WS leads, more so for the ones that always pushed forward and maintained their position as Joe did. I also know for a fact that Joes intentions are always positive towards GitcoinDAO and its future.  He is one of the most value aligned persons I've met in web3 and worked with in web3.  If someone doubts that he can just search DisruptionJoe in Gitcoins Discord and will be amazed by the level of engagement and value addition most of his messages lead 2.

I really hope the situation is handled in the best way possible for all the parties involved, but I would add that a certain level of kudos should be awarded to the FDD leadership, who managed to be one of the WS who protected funds and generated profits via great treasury decision making.

-------------------------

octopus | 2023-03-03 00:18:46 UTC | #39

I'm sad to see FDD go. I enjoyed my brief time working there and am proud of the contributions I was able to make. I regret that I wasn't able to stick around to finish getting the simulation results from the Agent-Based Model. In the end, I had too many commitments to do them all well. 

FDD saved a quantifiable chunk of GitCoin's funds from sybils (many of whom had developed really smart strategies to game Quadratic Funding). In addition, FDD proactively prevented both new attacks and repeat attacks by people who would have come back. I thank you @DisruptionJoe for being the person who could lead this difficult effort through crucial times. There's no doubt in my mind that your work and the work of FDD literally saved GitCoin from becoming a scammer's paradise.

-------------------------

annika | 2023-03-03 16:57:29 UTC | #40

I am catching up on this conversation and, while it is certainly a challenging & uncomfortable situation, my overarching sentiment is that there is so much to learn from this and a great opportunity for the DAO to really build more clarity & specificity in budget request templates looking ahead. 

I am in favour of a revote. I strongly echo @ccerv1 's sentiment:

> Personally, I’m in favor of a revote because the $123K treasury request was presented as a requirement to meet the S17 budget of $340K. Had I known that the workstream already had $445K and was therefore projected to dissolve in three months with a net balance $228K [$445 + $123 - $340], then I would have voted differently.

I think getting caught up in the "what constitutes a re-vote?" discourse is unnecessarily distracting. Yes, that is 100% something that should be outlined and agreed-upon in the aftermath of all this, but I think having a huge debate & discussion around that just stifles progress in getting to an outcome here.

To me it's directionally pretty clear that this is a re-vote situation, and then the re-vote specifics on guidelines/process can be figured out post-mortem.

I also selfishly would *love* to see a TLDR recap of all this after the fact either in Steward Council or on a monthly steward call -- what happened, what we learned, what we'll change in the future as a result. If resolved effectively, I think this moment might end up being a big milestone we look back on in productively moving forward governance processes.

-------------------------

octopus | 2023-03-03 18:42:37 UTC | #41

I want to request clarification on some key points. Is it correct that:

1. The existence of the "surplus" FDD funds was made publicly known in a public and recorded Stewards council meeting.
2. Many Stewards voted on FDD funding without doing due diligence and information-gathering, i.e. attending the meeting or reading the transcript.
3. An unprecedented revote is being enacted on sentiment analysis of the basis of about ten forum posts, absent any provision in any existing GitCoin governance document.

If these are the facts, then my personal view is that a revote is completely illegitimate and sets a terrible precedent regarding the ability of individuals to simply assert decisions through personal will. It borders on the Tyranny of Structurelessness.

Is there a clear model of the desired information flow in GitCoin governance, and of who bears what responsibility for that flow?

Specifically, what are the official records that Stewards are expected to be familiar with before voting? Are Stewards expected to know what has occurred in meetings relevant to their votes? 

I understand that some Stewards have expressed that they have little bandwidth. But, I don't understand how this is possible: all human beings are equal in the fact that we all have 24 hours of bandwidth per day. 

I think ultimately that there need to be clear standards and expectations regarding what constitutes effective disclosure of relevant information, so that we can determine whether a standard of clear information availability has been met. 

Additionally, I'm not sure if I have standing to raise points in this discussion, since I sold my all of my GitCoin this week. But, as a DAO and mechanism researcher,  I am still interested in the answers to the above questions, and clarity regarding the situation.

-------------------------

shawn16400 | 2023-03-04 19:33:41 UTC | #42

As described above, this case illustrates a gap in our governance processes.  Finding such gaps are not uncommon and this will not be the last time we find new challenges to deal with.  
Using existing tools, and leaning heavily on Robert's Rules of Order NR, I built a reconsideration process that can help Gitcoin navigate cases like this.

I do not presume my proposed path is perfect for this and all future circumstances, but it could give us a framework from which to start.  I welcome any and all input in on that draft post so that we can find an equitable and non-acrimonious solution to this and future cases. 

https://gov.gitcoin.co/t/gitcoin-community-proposal-post-vote-appeal-process-aka-to-reconsider-a-vote/13165

-------------------------

octopus | 2023-03-04 22:33:16 UTC | #43

Really appreciate your writing this. I appreciate that you posted it on Twitter. 

This is more than a single issue. It sets a precedent for the GitCoin DAO. that will likely influence other DAOs in the future. 

I would encourage that the discussion be publicized widely, at least within GitCoin DAO. My guess is that relatively few people realize a major governance question is emerging in a forum discussion on a vote that was already settled.

-------------------------

DisruptionJoe | 2023-03-05 17:27:44 UTC | #44

This is really great work. One suggestion: CSDO doesn't have any legitimacy in this context. The steward council would serve as a better appellate court because their legitimacy comes from the token holders.

I would like for us to take the time to do this right. The nature of the problem also allows us to take time without immediate financial worries for FDD. 

I'd echo Octopus sentiment. Our governance says that a snapshot vote is final. If you look at Uniswap, 100% of their snapshot votes are enacted on Tally. Do we want to be the ones to change this precedent for the ecosystem based on a few posts on the forum rather than a legitimate process? How do we remain leaders in legitimacy after that?

-------------------------

shawn16400 | 2023-03-06 15:25:36 UTC | #45

[quote="DisruptionJoe, post:44, topic:12738"]
CSDO doesn’t have any legitimacy in this context.
[/quote]

Hey Joe, thanks for the comment.  With everyone I am in touch with regarding this situation, I try to draw a line between this example, and the proposed process to deal with this example.  I find doing that places a layer of abstraction between contention and good governance design.  This being the case, I moved responses to this to the proposal thread. 

https://gov.gitcoin.co/t/gitcoin-community-proposal-post-vote-appeal-process-aka-to-reconsider-a-vote/13165/3

-------------------------

ccerv1 | 2023-03-09 15:59:29 UTC | #46

Just want to come back to this (after reading comments) and provide a bit more context regarding my position:

- I have full confidence in Joe's integrity, that he has been acting in good faith, and that he is deeply committed to serving Gitcoin DAO and its community. I hope no one see this process as a referendum on one person's intentions.

- I have deep respect for the work FDD has provided to the DAO over the years and the impact it has had on Sybil defense (both practically, by preventing attacks during rounds, and through its thought leadership / experimentation) and in the data community. I also hope no one sees this as a referendum on the value or legitimacy of FDD's work.

- It is normal for organizations to refactor / reorg. Given the market conditions PLUS the fact that the DAO is transitioning from cGrants to a protocol stack, it makes sense to examine the role of "service" workstreams like FDD and question whether the current structure is optimal. As a Steward looking in, my impression is that this could have been communicated / executed better. However, since learning of the plan to dissolve FDD after S17, my position has been to advocate for an orderly  and full season-long transition.

[quote="ccerv1, post:3, topic:12738"]
First off, let me say that I deeply admire this team’s intention to work itself out of a job this season and to distribute itself across the DAO and the broader ecosystem. This is admirable and a clear sign of true mission-alignment.

Second, given the intention to dissolve, I am highly supportive of a transition season that not only enables the services provided by FDD to be refactored / relocated but also gives the people reasonable time to find their footing elsewhere in the DAO or the broader ecosystem.
[/quote]

- I don't have a strong opinion (yet) on whether workstreams *should* have "gray funds" or what happens to those funds in the event of a workstream dissolving. It appears the DAO is divided on this issue. As Joe and others have said, this should be clarified and made more explicit. That work feels urgent. But I wouldn't make a decision and then try to apply it retroactively to FDD's case. From my perspective, FDD can do what it wants to with those funds -- but they should be exhausted or at least fully earmarked by the end of S17.

- I do believe the presence of those funds was material information to Stewards. Sure, the funds were not hidden, but the salient issue is that they were not mentioned as a source FDD could draw upon for completing its S17 budget. In effect, FDD had the choice of funding a full S17 by tapping its gray fund OR requesting an allocation from the treasury and preserving the gray fund so it could be used for something else at the end of the season (eg, a Joke Race).

- Finally, on the question of the revote, I am happy to see that this is moving towards a resolution [here](https://gov.gitcoin.co/t/gitcoin-community-proposal-post-vote-appeal-process-aka-to-reconsider-a-vote/13165). Hopefully there are important communication and governance lessons we all gain from this. I would hate to see revotes become a common thing or a new layer of bureaucracy added to decision-making.

I hope people find my comments constructive. I appreciate all of the commentary in this thread and hope this ends up being a net positive in the long run for GTC governance.

-------------------------

lefterisjp | 2023-03-14 20:30:23 UTC | #47

I will keep it short. I also was not aware of the extra funds when voting in favour of this, and since the workgroup is dissolving and has enough funds to dissolve I don't understand why more was needed.

Questions about Intent to deceive and pages and pages of drama is not something I am going to go in.

-------------------------

shawn16400 | 2023-03-21 13:42:14 UTC | #48

On 3.20 this proposal was referred to the Steward Council for a reconsideration by @kevin.olsen, a member of CSDO.  Following the newly defined process, it will be reviewed in the next Steward Council meeting for consideration.  I will post the outcome of that discussion in this thread. 

https://gov.gitcoin.co/t/gcp-003-passed-post-vote-reconsider-process/13165

-------------------------

shawn16400 | 2023-03-28 12:42:26 UTC | #49

Quick update:
The steward council met on 3.27 and voted to reconsider the vote on the S17 FDD budget.  This effectively means the snapshot vote for the  S17 FDD budget is **null and void**.  FDD budget owner @DisruptionJoe does comment on his intentions moving forward and you can see the discussion in the recording below (starting at about 3:13.

you can see a recording of the meeting `[here](https://www.youtube.com/live/zwrQpyzc5pM?feature=share )
And you can see the notes of the meeting [here](https://www.notion.so/gitcoin/Steward-Council-Mar-2-92aa72f9fe064dd8b26f966d0bb31d5e?pvs=4)

Thank you to the Gitcoin Steward council members who were present, and cast their vote.  

![image|690x205](upload://YUUZiuWepK1m5Fb5oveec9zxvF.png)

-------------------------

DisruptionJoe | 2023-03-28 15:24:41 UTC | #50

Thank you for all your hard work to make this happen. While I still disagree with the outcome, I do feel that the process for making the decision was fair and legitimate. 

I will not be posting the budget again as FDD does have the funds to finish the season and we are already well down that path.

-------------------------

kyle | 2023-04-01 12:51:55 UTC | #51

[quote="DisruptionJoe, post:50, topic:12738"]
I will not be posting the budget again as **FDD does have the funds to finish the season** and we are already well down that path.
[/quote]

Hey Joe - Do whats does this actually mean? I think we discovered FDD does have "grey funds" and those cold be used to finish out the season (not saying they have to be, but want to get a bit of context)?

Where do those "grey funds" go once FDD dissolves? 

IIRC, dCompass kept their excess funds after spinning down as a workstream as they were working to finish up the product they were building and felt they may still have a go to market path without additional WS funds. What are you thinking for FDD's case?

-------------------------

DisruptionJoe | 2023-04-01 17:06:08 UTC | #52

I delayed posting a FAQ about this as I was trying to gather all the details. You beat me to it! My intention is to get it up this Monday. 

TL;DR

* We are planning to execute on almost everything in the Season 17 budget as [posted](https://share.getcloudapp.com/YEueP80r).  It seemed that we had alignment on the work to be done, just not if FDD should be given more funds to do it. 
* We have $30-60k left which FDD will vote on how to use to further its mission. These will likely be used dogfooding Allo protocol. 
* 5/10 have transfer plans which will be outlined on the FAQ - Most of these are paid by FDD through 4/28 although they transfer accountability on 4/3 - Its a hand held process
* Those who aren't moving on had final dates set according to work they are responsible for and severence based on time/postition with Gitcoin. 
* ODC will still conduct the hackathon 4/25-5/30! Checkout Evan post here: https://gov.gitcoin.co/t/gitcoin-founded-opendata-community-regen-rangers-hackathon-is-approaching/13421
* We do hope for other opportunities for individuals to participate in the ecosystem through GCPs and building some of the first service orgs on the protocol! More details TBD.

-------------------------
