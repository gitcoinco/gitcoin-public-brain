---
id: 8122
title: "Fraud Detection & Defense Working Group Mapping"
slug: fraud-detection-defense-working-group-mapping
category: open-discussion
url: https://gov.gitcoin.co/t/fraud-detection-defense-working-group-mapping/8122
created_at: 2021-08-02T21:28:32.174Z
last_posted_at: 2021-08-02T21:28:32.308Z
posts_count: 1
views: 4384
like_count: 9
---

# Fraud Detection & Defense Working Group Mapping

<https://gov.gitcoin.co/t/fraud-detection-defense-working-group-mapping/8122>
JessicaZartler | 2022-05-28 15:34:43 UTC | #1

*The goal of this post is to provide a preliminary mapping of the Fraud Detection & Defense Working Group of the Gitcoin DAO, explaining its purpose and the interplays between the various stakeholders and the functions that must be fulfilled. In order for that purpose to be reliably fulfilled, the Gitcoin DAO and its stakeholders must understand not only the functions, but the effort, skills and resources - including but not limited to human, financial, access & permission, technical infrastructure - required to maintain Fraud Detection & Defense for the Gitcoin Grants ecosystem.*

*Following a similar exercise at the [ecosystem level](https://gov.gitcoin.co/t/ecosystem-mapping-discussion/8123), this map, fashioned in the spirit of [this Computer-Aided Governance Map & Process,](https://blockscience.github.io/cag-map/map/) serves many purposes:* *i) A focal point and tool for further coordination and iteration of this working group and its associated processes ii) Transparent communications to the Gitcoin DAO iii) Onboarding and orientation tool for the Fraud Detection & Defense Working Group.*

# **Fraud Detection & Defense Working Group Mapping**

The Fraud Detection & Defense working group (FDD-WG for short; formerly known as Anti-Fraud & Collusion, Anti-Sybil workstream) is analyzing Gitcoin data and exploring mechanism, process and policy design solutions for sybil-resistance with the stated goal of identifying and defending against economic attacks such as collusion strategies by bots and fraudulent accounts. *(For context on the aims of the group, see [here](https://gitcoin.co/grants/3130/gitcoin-dao-anti-fraud-workstream-round-10).)*

The FDD-WG uses the data from Grant rounds and a machine learning pipeline to [define, detect, evaluate, and sanction](https://medium.com/block-science/deterring-adversarial-behavior-at-scale-in-gitcoin-grants-a8a5cd7899ff) fraud and other attacks on the Gitcoin platform, and also to scale the monitoring capabilities of human reviewers.

![|591x225.52487736510162](upload://adpgJA0UtdAgPph2hWmfgmeqU49.png)

## Computer-Aided Sybil Defense: Human / Machine Learning Pipeline

The working group has come a long way since its tasking: It began with two workstreams (tech and education) to catalyse the working group. Those working on the FDD-WG quickly realized the functions and workstreams of the group needed to be expanded to match a complex web of stakeholders and functions.

This required, and requires, [institutional design](https://www.researchgate.net/publication/220007310_Institutional_Design) work - the choice of rules for collective decision making (which will be iterative and ongoing) - to fulfill the plans of Gitcoin Holdings and Gitcoin DAO to “progressively decentralize” the Fraud Detection and Defense work of the Gitcoin platform.

## Workstream (sub working group) Functions within FDD

At the highest level, the FDD-WG is split into five main workstreams at this point in time:

![|512x202](upload://avM6skmXlDy1t6YddW2EnsDysf2.png)
*Figure 1.1: FDD Working Group by Workstream (BlockScience: Emmett, Zartler)*

### Admin, Ops & Education Workstream

This workstream is responsible for the administrative and operational functions of the working group, along with communications and educational responsibilities both within the workstream and with external stakeholders. Some main tasks include, but are not limited to:

* Working group operations and coordination, ensuring efficient functioning
* Internal & external communications, documentation and repository management
* Maintenance and mapping of communications channels i.e. Discord, Notion
* Transparency and monitoring operations i.e. note taking, recording and uploading call recordings
* Orientation to the group and onboarding contributors
* Community management & education
* Initiating and maintaining fundraising, reward and incentive systems and payments to contributors and/or contracted subject matter experts
* Supporting other workstreams with admin, operational, communications and educational work

### Grant Verification Workstream

This workstream is responsible for reviewing and accepting or rejecting incoming grant submission for the Gitcoin platform and is also responsible for creating processes and transparent documentation for those processes.

It also interfaces with Gitcoin DAO governance bodies on policy creation, iteration and implementation in regards to Grant Verification. This workstream group also interacts quite heavily with the Appeals & Sanctions workstream to ensure quality control processes are being met.

Major tasks of FDD-WG include, but are not limited to:

* Reviewing and verifying grant submissions, and documenting actions
* Ensuring adequate resources and staffing for review input
* Onboarding and training contributors for tasks specifically related to Grant Verification work
* Enforcing terms and conditions e.g. removing grants from the platform that do not meet community standards, or marking grants as ineligible for matching
* Communicating outcomes to internal & external stakeholders i.e. Stewards, wider DAO community
* Maintenance and documentation of communications channels i.e. Discord, Notion
* Creating, documenting, iterating and maintaining FD processes
* Technical, product and UI/UX development where necessary
* Supporting and enforcing PII standards and access control
* Ongoing research and development to improve the FD function and ourselves as a working group.

### ML Sybil Detection

The ML Sybil Detection workstream is in charge of building and maintaining the sybil detection machine learning algorithm. This group coordinates closely with platform operations to operationalize the ML pipeline in each Gitcoin round, providing data, reports and advice in support of real-time intervention or other requests to FDD, and coordinates in between rounds for any necessary process improvements. Major tasks include but are not limited to:

* Feature engineering within the data pipeline, model and metaparameter selection, loss function selection & maintaining human labeled training sets cross validation
* Conducting testing to improve the accuracy of the algorithm in fraud detection
* ML model upgrades
* Ongoing data science R&D
* Upholding Personally Identifiable Information (PII) standards, access control and policies created and maintained by the Platform Operations Working Group
  * Balancing transparency with privacy (e.g. keep PII private while providing transparency about the process and any trade off decisions)

* Builds on data operations infrastructure and documents processes, code, data, microservices, and any other infrastructure required in order to reliably fulfill this function to report and file with *Platform Operations/Data Operations *(see below "Additional Working Groups Needed")*
* Onboarding and training contributors for tasks specifically related to ML Sybil Detection stream work.

### Flag Evaluation

This workstream is the human part of the sybil defense pipeline and is responsible for the *Define* & *Evaluation* sections of the pipeline. This group supports in continuing to refine definitions of sybil patterns, and participates in evaluating the actions flagged by the machine learning algorithm to match patterns deemed fraudulent.

The evaluations by this group are also used by the ML Sybil Detection group to further tune the algorithm. The Flag Evaluation workstream also provides suggestions, data, reports and advice surrounding processes and further actions or improvements necessary in policymaking via communications with the other FDD workstreams.

* Onboarding and training contributors for tasks specifically related to evaluation work
* Evaluate flagging outputs to confirm accuracy of the machine learning algorithm
* Report to appropriate stakeholders
* Ongoing research and development

### Appeals & Sanctions

The Appeals & Sanctions group is responsible for making sure community feedback is heard and integrated in developing, enforcing, and iterating policies surrounding the appeals and sanctions processes within FDD and the [wider Gitcoin ecosystem](https://gov.gitcoin.co/t/ecosystem-mapping-discussion/8123) in meeting the terms and conditions of the platform. Responsibilities can be expanded but include the following:

* Develop, iterate and maintain appeals and sanctions policy processes, documentation and implementation
* Liaise with appropriate stakeholder groups and Gitcoin DAO governance bodies regarding policymaking and implementation
* Explore Restorative/Transformative Justice and other measures via R&D to inform and improve policymaking and community well being and growth
* Supporting and enforcing Personally Identifiable Information standards and access control.

## Participant Groups, Recommended Responsibilities & Funding

To this point, the FDD Working Group has been made up of Gitcoin Holdings (Gitcoin’s core team), [BlockScience](https://block.science/) as paid contractor/subject matter expert/advisor, and unpaid volunteers from the Gitcoin community, [Token Engineering community](https://tokenengineeringcommunity.github.io/website/), and other ecosystem volunteers.

Going forward and to meet the goals of progressive decentralization, it is important to understand the current roles fulfilled, and the other that must be taken on by paid and/or volunteer contributors, coordinators and/or stewards. The following is a map of current resources and recommendations for roles and tasks to be fulfilled:

![|610x352](upload://ghtliCXlZORBsgl25vLoloR46nF.png)
*Figure 1.2: FDD Working Group Participant Groups (BlockScience: Zartler)*


For now, we are identifying three main categories of participants:

**Coordinators**
  * Can be anyone who has been elevated to the “role” of steward within the gitcoin DAO *(see [this introductory Forum post](https://gov.gitcoin.co/t/introducing-stewards-governance/41))* - or community members

     *Coordinators can serve in multiple workstreams as needed, until workloads expand.*

**SMEs (subject matter experts)**
  * Domain experts in areas including but not limited to advising, strategy, scientific documentation, process engineering and technical development (as appropriate)

**Contributors**
  * Anyone contributing work or participating in the FDD Working Group
  * Can be community members or stewards

Participants in all categories can be compensated or volunteer. Currently, there is no rewards system in place for this working group. Until this point, Gitcoin Holdings has been contracting the functioning of this group and there was a [Gitcoin Grant submitted](https://gitcoin.co/grants/3130/gitcoin-dao-anti-fraud-workstream-round-10) to fund the previous Gitcoin Round (Round 10) only. Going forward, that grant could be revived to support contributors, but more sustainable funding is required from GitcoinDAO to fund key operational functions of this working group and/or recruit volunteers in order to decentralize responsibilities. Work is underway by some participants of the FDD-WG to submit proposals to the DAO to fund FDD-WG operations *(see the [FDD-WG forum thread](https://gitcoin.co/grants/3130/gitcoin-dao-anti-fraud-workstream-round-10) for updates)*.

Currently there are no rules or policies around onboarding contributors, decisions around participation, proposals and requests for participants to engage at the working group level. There is also no tracking system for those processes or funding systems. Participation and contributor processes need further institutional design. Many DAOs operate under models of [do-ocracy](https://communitywiki.org/wiki/DoOcracy). Discussion at the DAO level on governance and metagovernance are happening on the [Gitcoin DAO forum](https://gov.gitcoin.co/) under the [MetaGovernance](https://gov.gitcoin.co/c/governance-meta/6) and [Proposal Discussion](https://gov.gitcoin.co/c/governance-proposals/5) threads. Any participant can submit a proposal to the DAO via those threads.

The following is a recommendation for tasks and responsibilities by participant group:

## Workstream Roles and Responsibility Recommendations

**Coordinators (paid/volunteer):** Community and contributor management, organizing and setting calls/calendar invites, making sure communications are flowing inside of the workstream with the community, SMEs, advisors and DAO.

**SMEs/Domain Experts (paid):** Advising, strategy, scientific documentation, process engineering, technical development (as appropriate)

**Contributors (paid):** Supporting grant verification, appeals & sanctions, evaluation panel flag judging, process mapping, governance policy making, data science for ML workstream, workstream operations, payroll management and contributor rewards tracking.

**Contributors (volunteer/education through participation):** Supporting admin such as note taking, recording calls, uploading videos, community communications (forum/Discord comms), orientation/onboarding to the group.

***NOTE ABOUT DAO FUNDING & REWARDS SYSTEMS:*** Funding proposal and incentive/rewards systems for DAOs are nascent, relatively underdeveloped and require further research and development. One example of a functioning funding proposal system is [Conviction Voting](https://twitter.com/commonsstack/status/1309211776425365510). Some examples of reward and incentive systems being explored in multiple DAOs includes [SourceCred](https://sourcecred.io/), [Coordinape](https://coordinape.com/), [Praise]((https://wiki.commonsstack.org/contributors-guide)) and UBI (Universal Basic Income) models, but ongoing work is nascent and exploratory. Yet another model to handle rewards and incentives is a Proposal Inverter, read more about in [this research article](https://medium.com/primedao/exploring-dao2dao-collaboration-mechanisms-c37218a17a21). Feel free to post/discuss other systems in the [MetaGovernance section](https://gov.gitcoin.co/c/governance-meta/6) of the GitcoinDAO forum.

## FDD Functions & Interdependencies with External Stakeholders & Working Groups

The FDD Working Group has several interdependencies in order to carry out its best work in defending the Gitcoin platform from Sybil attacks, collusion, and fraudulent actions. In order to protect ecosystem funding and ensure grants are distributed to legitimate projects contributing to Ethereum public goods, it requires coordination with many external stakeholders and working groups:

![|624x408](upload://2ErSsMKCxe6cJcuHKN9QSQzygEp.jpeg)
*Figure 2: FDD Interactions Map (BlockScience: Zargham, Emmett, Zartler)*

## Interactions with other Gitcoin DAO working groups
*(see [ecosystem map](https://gov.gitcoin.co/t/ecosystem-mapping-discussion/8123) for further detail of working groups mentioned below)*

Interdependencies and coordination needs include, but are not limited to, the following:

**Platform Operations**
  * Initiates calls for service to FDD and the ML Sybil Detection sub working group for operational needs regarding flags and intervention
  * Requests ad hoc analysis to various FDD workstreams and updates/reports on research and development
  * Coordinates with FDD to ensure platform data and API needs are being met and code/database repos are being maintained, along with access and version control and PII requirements

**Communication & Community Management**
  * Supports the flow of communications and community feedback to and from the FDD Working Group with other working groups, stewards and stakeholders
  * Supports contributor and community management with FDD needs and requests
  * Support research communications, documentation and publications in FDD

**Treasury Management**
  * Supports rewards/incentives and funding proposal management needed for FDD Working Group
  * Supports contracts/payments for SMEs and organization level proposals
  * Coordinates with FDD Working Group regarding grant matching totals and calculations i.e. Fraud Tax data

**Governance**
  * Coordinates with FDD in policymaking for Grant Verification, Evaluation and Appeals & Sanctions processes
  * Supports the flow of communication to and from FDD regarding community and stakeholder feedback in policymaking
  * Supports documentation and maintenance of policy repo and communication to the community about rules, processes and corresponding communication channels

**Meta Governance**
  * Coordination with FDD for continuing institutional design and analysis regarding FDD functions and operations
  * Support in FDD process engineering, refinement and updating documentation
  * Supports in ensuring stakeholder representation within FDD, and managing policymaking involving FDD functions at the ecosystem level

### Recommendations for Additional Working Groups / Functions Needed for FDD-WG and the Gitcoin DAO:

The FDD-WG is privy to privileged data on behaviours of people who use the Gitcoin platform, as well as some private materials available only to group members, and is under [PIIs](https://digitalguardian.com/blog/how-secure-personally-identifiable-information-against-loss-or-compromise) as such through Gitcoin.co’s existing [data privacy policy](https://gitcoin.co/terms/privacy). In order to manage and balance any liability or privacy issues with transparent operations, it is critical the Gitcoin DAO maintain spaces and permissioned access levels specific to this working group.

This mapping exercise has surfaced the following functional needs which are not currently met and remain unclear in the emerging Gitcoin DAO structure:

**Data & Technical Infrastructure Operations**
  * Consists of data engineers, development operations experts and data analysts
  * Building, maintaining and operating data warehouse i.e. data collection, cleaning, curation, analytics and staging (maintained by data engineers to assure data consistency and availability for various use cases)
  * Maintains data infrastructure and operations, corresponding standards, policies and data privacy access & control standards to meet legal requirements
  * Supports FDD-WG in upholding and enforcing PII standards, policies and compliance

*This working group could be a workstream of Platform Operations, or its own stand alone working group.*

**Legal & Advisory Support**
  * Advising on liability and legal requirements and considerations for DAO operations and stakeholders
  * For Platform Ops/Data Ops & FDD-WG: Guidance on PII requirements, considerations for Appeals & Sanctions and other needs as they arise

***NOTE**:* There has been some discussion around PII, in [this Gitcoin DAO forum post](https://gov.gitcoin.co/t/gitcoin-co-data-stewardship/7663/2).

While access to some materials is limited, membership in the working group is still open to qualified volunteers.

## In Closing

As mentioned, FDD-WG is at a complex cross section of stakeholders and organizations in the journey to “progressively decentralize” the working group functions. It is challenging to pass responsibility to GitcoinDAO and the community without first understanding the landscape and functions of Fraud Detection and Defense, setting up funding and rewards mechanisms, and a minimum viable institutional shell to which can be passed said responsibilities.

We hope this map will serve as a compass for further development of FDD and the Gitcoin DAO and look forward to continuing to serve as SME participants. I invite you to participate in the mapping exercise as a (continuously) ongoing process and participate in the Fraud Detection & Defense of the Gitcoin platform.


*🙏Thank you to everyone who contributed ideas and feedback to this mapping exercise: @Zargham, @jeffemmett, @kelsien, Danilo Lessa Bernardineli, burrrata, @DisruptionJoe and @ceresstation 🙏*
#

----
#
***Disclosure:*** I am a paid contractor of BlockScience for subject matter expertise in the Fraud Detection and Defense Working Group and have been volunteering in the role of FDD co-coordinator along with my colleague Jeff Emmett and Disruption Joe of Gitcoin core team, although we are actively seeking new coordinators for the aforementioned workstreams. We’ve been working with Dr. Michael Zargham, Danilo Lessa Bernardineli, Jesse Tao, Jiajia H, Kyle Weiss, Scott Moore, Kevin Owocki, Dr. Andrew Penland, David Moss, Varun Bhargava, Dong Data, William Xuan, Kelsie Nabben and others to bootstrap this functional unit.

There is a lot more work to be done to establish a self-sufficient working group, but we’ve been thankful for the contributions of named (and some unnamed) participants in this group. We would also like to thank volunteers of the Token Engineering community who have stepped up to provide their data science expertise and expand the work of this group to serve the wider Gitcoin community and open source, public goods ecosystems. We would also like to thank Commons Stack, Token Engineering Commons, 1Hive, MetaGov, Token Engineering Academy, Prime DAO, Curve Labs, NEAR Protocol and other pioneers in supporting continued research and development in the DAO and Commons space.

-------------------------
