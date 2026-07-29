---
id: 18415
title: "[Citizens Innovate GCP] Karma's On-Chain Grant Aggregator on Allo V2"
slug: citizens-innovate-gcp-karmas-on-chain-grant-aggregator-on-allo-v2
category: citizen-grants
url: https://gov.gitcoin.co/t/citizens-innovate-gcp-karmas-on-chain-grant-aggregator-on-allo-v2/18415
created_at: 2024-03-26T19:35:27.501Z
last_posted_at: 2024-07-25T11:48:55.634Z
posts_count: 18
views: 4627
like_count: 56
---

# [Citizens Innovate GCP] Karma's On-Chain Grant Aggregator on Allo V2

<https://gov.gitcoin.co/t/citizens-innovate-gcp-karmas-on-chain-grant-aggregator-on-allo-v2/18415>
mmurthy | 2024-03-27 21:12:59 UTC | #1

### **Summary (TL;DR):**

Karma proposes to develop an onchain grant program aggregator platform, leveraging the foundational work of the Grantee Accountability Protocol ([GAP](https://gap.karmahq.xyz)). This platform aims to build a registry atop Allo that will bring together details on the broad scope of grant programs within the EVM ecosystem, enabling grant program discovery and improving the application process for grantees and management for grantors while embodying Gitcoin's open-source ethos.

### **Abstract:**

This project is designed to establish a comprehensive and accessible registry of EVM-compatible grant programs, capitalizing on the strengths of the Grantee Accountability Protocol (GAP).

By developing an on-chain platform built atop Allo Protocol, we aim to streamline the discovery and management of grant programs, making it simpler for grantees to find relevant opportunities and for grantors to maintain up-to-date program information. The initiative focuses on delivering a user-centric interface for exploring grant listings integrated directly with GAP to ensure a seamless, transparent, and efficient process for all stakeholders.

We are excited to collaborate with @Sov for this project. Sov has vast experience collaborating with various grant programs and has managed grants program data in the past. His expertise will be crucial in driving the success of this project.

### **Benefits & Motivation:**

Grants are crucial for ecosystem development, offering essential funding for projects and initiatives. However, the current grant landscape needs to be more cohesive and clear, which poses challenges. This platform addresses these by simplifying discovery, application, and management processes, fostering ecosystem growth, enhancing transparency, and encouraging community participation.

### **Scope:**

- An onchain registry of EVM-aligned grant programs built on top of Allo Protocol

- Integration with Karma GAP.

- Open-source development and community collaboration.

### **Strategic Fit:**

The opportunity presented by this project is multifaceted and deeply aligned with Gitcoin's overarching goals. Here's a breakdown of the "why" behind its potential impact and value:

**Aligns with Open-Source Development Goals**

Gitcoin has long championed open-source development, recognizing it as a cornerstone of progress within Web3. The platform's open-source nature ensures that the community can continuously improve, audit, and extend it, fostering a collective development and learning culture.

**Enhances Transparency Across EVM Ecosystem**

The project's core objective is to create a transparent overview of EVM-aligned grant programs. In the current landscape, finding and applying to these programs can be opaque, with information scattered and processes varying significantly between programs. This platform centralizes and clarifies the available opportunities, making it easier for potential grantees to find relevant programs and for grantors to attract suitable applicants. Such transparency is crucial in building trust and accountability within the ecosystem, encouraging more participation and engagement.

**Facilitates Accessibility and Management**

Grantors are empowered to keep their information up-to-date and reflect current opportunities and requirements by enabling the claiming and proactive management of program profiles on the platform. This feature benefits the grantors by ensuring that programs are represented and aids grantees in accessing the most relevant and current opportunities. The ease of access and the ability to directly manage these profiles democratize the grant application process, making it more inclusive and efficient for all parties involved.

**Leverages the Allo Protocol**

Allo's design for facilitating on-chain actions and interactions makes it an ideal foundation for this aggregator platform. It offers scalability, security, and integration capabilities with existing Web3 infrastructure. This alignment with Allo harnesses its technical strengths and signifies a strategic collaboration within the Gitcoin ecosystem.

**Presents Broad EVM Ecosystem Benefits**

While the immediate benefits to Gitcoin and its community are clear, this project also presents significant opportunities for the broader EVM ecosystem. By streamlining access to grant programs, the platform can stimulate more active participation across different projects, leading to increased innovation, collaboration, and growth. It catalyzes ecosystem-wide development, supporting projects at various stages and fostering a more interconnected and supportive Web3 community.

### Risk Assessment

The primary risks involve adoption by grant programs and applicants and the technical challenges of integration. To address these, we will leverage the relationships already built with existing programs along with our in-house development expertise. The work we have already done with Karma GAP demonstrates our ability to execute in both of these areas.

### Budget

The projected budget for developing and implementing Karma's On-Chain Grant Aggregator platform is $40,000. This budget encompasses work across seven key phases, ranging from website design to automating program data aggregation. A high-level breakdown of the phases and estimated LOE is as follows:

|Scope|Task|Resource|Level of Effort|
| --- | --- | --- | --- |
|1|Website Design|Design|40|
|2|Design Data Model|Developer|12|
|3|Frontend Implementation + Allo Registry Integration|Developer|50|
|4|Indexer|Developer|24|
|5|Backend Work|Developer|40|
|6|Populate Registry|Analyst|40|
|7|Jobs to Auto Pull Programs|Developer|24|
||Total||230|

## Project breakdown

### High-Level Architecture

![|624x436](upload://2K0btGVJzTid7GQnI2s90ndLkv7.png)

### Website Design

- **Objective:** Create intuitive, user-friendly Figma designs for the GrantHub website, enabling users to efficiently browse, navigate, and interact with grant program listings. Build a program manager interface to manage their grant program information.

### Design Data Model

- **Objective:** Identify all grant program data and design a schema to store it in the Allo registry. Also, design the data models for offchain storage of data.

### Frontend Implementation + Allo Registry Integration

- **Objective:** Construct the frontend application based on the Figma designs and seamlessly integrate it with the Allo registry smart contract. This integration will enable program managers to manage their grant programs on-chain effectively. A specific program manager interface will be implemented to facilitate these on-chain management activities. The frontend will be developed as an extension of the existing GAP front end, utilizing React/NestJS frameworks.

This integration aims to maintain consistency with the Allo registry by using the same identifiers for projects as found in the registry, ensuring a unified source of truth across the platform.

In addition to leveraging data directly from the Allo v2 registry, the platform is designed to import and incorporate project data from sources outside of Allo v2. Projects ingested from external sources will be integrated into the Allo v2 registry, providing a comprehensive view of grant programs across the ecosystem.

Recognizing the multi-chain nature of projects within the Web3 space, our platform supports the management of program data across multiple chains. Program managers can select a preferred chain for maintaining their program data, accommodating grant programs' diverse operational needs. This approach ensures that the GAP architecture includes the multi-chain landscape, offering program managers a tailored and efficient management experience.

### Indexer

- **Objective:** Develop dynamic scripts and services designed to continuously monitor and respond to blockchain events associated with grant programs. This includes capturing essential actions such as program creation, updates, and other modifications. The goal is to ensure the Allo registry is always current and the definitive source of truth. Indexed data will be systematically stored, facilitating efficient retrieval and allowing for real-time adjustments to the registry entries (e.g., adding, editing, or removing entries) to maintain their accuracy and relevance.

### Backend Work

- **Objective:** Develop a robust backend infrastructure to support frontend operations, data management, and integrations. Design and implement RESTful APIs to serve data to the front end, including lists of grant programs, detailed program information, and submission endpoints.

### Populate Registry

- **Objective:** Leverage an existing database containing information on EVM-compatible grant programs as the foundational dataset for creating the new on-chain registry. This process involves extracting and transferring relevant data from Airtable to populate the registry, ensuring an extensive and accurate listing.

### Jobs to Auto Pull Programs

- **Objective:** After initial import, we will develop a continuous automation process for aggregating grant program data from various platforms to ensure the registry remains comprehensive and up-to-date. This will facilitate the integration of new grant programs into the Allo registry via an ongoing job that extracts data from diverse platforms and consolidates it within Allo. The process is designed to leverage both on-chain data directly from the blockchain and off-chain data through our sophisticated Indexer, ensuring a thorough and dynamic update mechanism for the registry.

### Ongoing Analytics and Reporting

- **Objective:** Integrate analytics tools for tracking user interactions and engagement, providing insights for continuous improvement.

For the **Acceptance Criteria** and **Relevant Metrics**, expanding them can help ensure a comprehensive assessment of the platform's success and impact. Here are some ideas:

## Milestones

**Milestone 1**: MVP website with read only program data
**Details**: We will build a basic program registry page that will let anyone browse programs. This will be a barebones website without any bells and whistles like filtering, sorting etc. 
**Timeline**: 2 weeks (will update this to exact date if/when proposal passes)
**Budget**: $10k

**Milestone 2**: Implement Program manager functionality
**Details**: Upon completion of this milestone, program manager will be able to login to the website, fill in program details and write to the Allo registry. The program data will be displayed in the registry page to the public.
**Timeline**: 1 weeks (we'll update this to exact date if/when proposal passes)
**Budget**: $10k

**Milestone 3**: Aggregate and load program data to registry
**Details**: Work with analyst to aggregate program data from across the EVM ecosystem and load it into the registry. Come up with a clean process to easily upload program data to the registry. Anyone will be able to view all program info on the website once this milestone is complete.
**Timeline**: 1 weeks  (we'll update this to exact date if/when proposal passes)
**Budget**: $5k

**Milestone 4**: Launch fully featured registry with program data
**Details**: Launch the registry feature with atleast 25 programs listed in the registry. Upon completion of this milestone, anyone will be able to visit the registry page, browse the programs and find all the program details. Program managers will be able to login and add their program details.
**Timeline**: 2 weeks  (we'll update this to exact date if/when proposal passes)
**Budget**: $15k

## Acceptance Criteria

- **Successful Integration with Karma GAP and Allo v2:** The platform must seamlessly integrate the Grantee Accountability Protocol (GAP) functionalities and leverage Allo v2's capabilities.

- **User-friendly Interface for Grantees and Grantors:** The platform should have an intuitive, easy-to-navigate interface that simplifies finding, applying, and managing grants.

- ** Listing Accuracy:** The information about each grant program must be accurate and up-to-date.

## Relevant Metrics

- **Number of Grant Programs Listed (target 100+):** Track the total number of grant programs available on the platform to ensure a broad and diverse range of opportunities for grantees.
- **Number of Profiles Claimed in First Month (target 10+):** Monitor grant programs' engagement with the platform, as indicated by the number of programs that claim and manage their profiles. For the initial version (v1), we will implement a manual process for profile claiming. This will involve a simple form on the platform where grant programs can submit requests to claim ownership. Once a claim is verified, the Allo contract's ownership transfer feature will manually assign ownership. This approach allows us to carefully verify each claim to ensure legitimacy before considering automation for future iterations. We will develop a structured verification process to confirm the authenticity of claims, learning from these interactions to streamline and automate this process in subsequent versions.

- **User Engagement Rate:** Measure the frequency and duration of user interactions with the platform to gauge its attractiveness and usefulness to the community.

- Interaction with each program page

- No. of program filter and search interactions

- No. of redirects to the program site

## Team

We are team of developers who have been building [contributor reputation tools](https://www.karmahq.xyz) for the past two years. We have been long time contributors of Gitcoin. We currently maintain the [Gitcoin Steward Dashboard](https://delegate.gitcoin.co/) that displays all the stewards and their governance activity. Our grantee protocol [GAP](https://gap.karmahq.xyz/gitcoin) is used by many Gitcoin grantees to build reputation and show their project progress to the funders. GAP has also been integrated into Grants Stack making it easy to the funders to view updates from grantees. 

## Conclusion

We are excited about this project's potential to streamline the discovery of grant programs within the broader EVM ecosystem. This project represents another step forward for Karma in our ongoing efforts to enhance transparency, accessibility, and efficiency for both grantors and grantees.

We welcome your feedback, questions, and suggestions. Your input is invaluable in ensuring the project meets the community's needs and expectations.

-------------------------

meglister | 2024-03-26 19:41:08 UTC | #2

I'm super supportive of this proposal. It's a great use case for the Allo registry and provides sustained value back to the protocol (rich data and reputation building) and Karma GAP (increased surface area for impact measurement).

-------------------------

Sov | 2024-03-27 00:13:46 UTC | #3

Super excited to work on this.  

As @mmurthy mentions, I have been collecting data on these programs for some time, and I can't wait to bring this all on-chain with Allo for all the reasons mentioned in this proposal.

-------------------------

rohit | 2024-03-27 08:18:20 UTC | #4

@mmurthy, thanks for the detailed proposal. I am excited about the possibilities here for broader use cases on top of this foundation for streamlining workflows for grant programs and builders, especially for reducing friction grantees have today in finding appropriate grants in a timely manner and saving the effort involved in submitting similar information multiple times across grant programs.

A couple of quick suggestions:
- Besides the high-level tasks, could you propose 3 to 5 milestones with relevant outcomes and associated budget for each? This will aid in tracking progress and managing the budget effectively. 
- If relevant, also include any support or resources you might need from the Gitcoin team so that the project's needs are met effectively and in a timely manner.

As a next step, once the 5-day window for reviewing and feedback on the proposal is completed, the Grant Council will decide on it as part of the monthly funding decisions for Citizens Innovate.

-------------------------

webx1610 | 2024-03-27 12:43:16 UTC | #5

super to participate actively and hope that I will get there, and there I need to know how and when I will be to be part of the application

-------------------------

mmurthy | 2024-03-27 21:16:07 UTC | #6

@rohit Thanks for the feedback! I added new milestone section with details you requested. 

Regarding support/resources - we have been in constant communication with product and tech teams and all our questions have been addressed. So I didn't add anything. Let me know if you see anything else missing. Thanks!

-------------------------

Viriya | 2024-03-28 19:15:08 UTC | #7

Really excited about this proposal and the value add it specifically around impact measurement (which is something that is very much on all of our minds!) but also bullish on how this will enable us to improve builder UX for Grants Stack :slight_smile:

-------------------------

rohit | 2024-03-29 12:38:45 UTC | #8

Awesome, that's perfect. And thanks for the breakdown!

-------------------------

deltajuliet | 2024-04-08 10:19:13 UTC | #9

Really excited about this proposal and the approach to tackling EVM ecosystem challenges. It’s a solid move towards reducing friction for projects seeking support, which could significantly speed up their development.

Enhancing discoverability and simplifying the application process will likely draw a broader range of projects and contributors to our ecosystem. Engaging with the community to pinpoint and tackle potential challenges early is crucial. Also, are we considering ways to encourage more participation and collaboration/feedback? Curious about any strategies on that front, @mmurthy.

-------------------------

ccerv1 | 2024-04-12 17:23:58 UTC | #10

Very cool initiative! I am supportive. Where it makes sense, please capture the project's GitHub org so we (at [OSO](https://docs.opensource.observer/docs/contribute/project-data)) can compose with it. Would also be keen to connect the registry to [our dataset](https://docs.opensource.observer/docs/contribute/connect-data) when it makes sense. I imagine there will be a decent amount of overlap especially when it comes to OSS grantees.

-------------------------

mmurthy | 2024-04-16 03:32:09 UTC | #11

Thanks @deltajuliet. We feel the best way to encourage more participation is by driving high quality builders to these grant programs. We are going to build in that direction. We plan to run workshops, post on various forums and onboard programs one at a time for first few to learn and get feedback and iterate on the product.

-------------------------

mmurthy | 2024-04-16 03:35:37 UTC | #12

We will capture github org and also look into connecting the registry with your dataset!

-------------------------

webx1610 | 2024-04-26 07:27:25 UTC | #13

That is correct, I m already part of the application

-------------------------

mmurthy | 2024-05-02 12:43:34 UTC | #14

I created the grant on GAP and added all the milestones. I will continue to post updates on our progress there :pray:

https://gap.karmahq.xyz/project/karma---gap/grants?grantId=0x3f3037ea95b224fe360479e5f8547653f869579d8503235de579f797e760c875&tab=overview

-------------------------

KMLLC | 2024-06-19 23:09:30 UTC | #15

I am in support of this. Very necessary for startups, founders, and orgs to be able to find available funding sources easily. Shifting the paradigm from traditional fundraising to Web3 fundraising, the onus on founders should not to be in a debt creation position, rather who can I find that is willing to support us based on our mission, vision, focus, and ability to execute without cause or prejudice to repayment schedules.

The majority of startups don't make it past the first 3 years without adequate funding sources. As a Web3 advocate for creating more responsible solutions, we can act more fair, equitable, and inclusive.

-------------------------

mmurthy | 2024-07-23 18:34:47 UTC | #16

Hello! I wanted to provide an update on grant registry project.

We recently launched the registry! You can find the registry with all the grant programs here: https://gap.karmahq.xyz/funding-map. There are just under 300 grant programs listed, all onchain, on allo registry and more being added. Anyone can submit a grant program. We will review and approve them to go onchain. We also have started indexing all the Gitcoin rounds, they will be automatically displayed.

Announcement tweet: https://x.com/karmahq_/status/1808512070083838011

@Sov and I went on greenpill podcast to talk about it: https://x.com/greenpillnet/status/1814336232610312346

There is now an active community [cartographer syndicate](https://sovs.notion.site/Cartographer-Syndicate-a574b48ae162451cb73c17326f471b6a) who has been contributing to the research, growth and development of the registry.

Shoutout to @rohit for helping through the entire process and making the grant experience seamless!

We are actively working on adding more features to the registry. If anyone has suggestions to improve the registry or general feedback, please let me know.

-------------------------

KMLLC | 2024-07-23 22:19:18 UTC | #17

Have you reached out to CharmVerse as they have grants available on their platform. One of the most significant is the current Polygon Community Grants Program?

More info here: https://app.charmverse.io/grants-tracker/web3-grants-hq-5501690381350384

-------------------------

rohit | 2024-07-25 11:48:55 UTC | #18

Congrats, @mmurthy @Sov and the Karma team on the launch. I have validated the functionality for all milestones (grant registry portal with program data and program manager functionality to add/edit program details) and attested it onchain using the "verify" functionality for the project on Karma GAP (a neat feature for decentralized verification!).

Here's a quick update on the Citizen Grants payment: On May 7th, $10K was disbursed for the first MVP milestone. I will now initiate the transaction for consolidated payments for all remaining milestones.

Looking forward to future updates on the registry!

-------------------------
