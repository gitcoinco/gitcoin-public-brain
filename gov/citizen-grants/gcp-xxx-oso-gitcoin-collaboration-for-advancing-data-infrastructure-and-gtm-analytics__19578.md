---
id: 19578
title: "[GCP - XXX] OSO-Gitcoin Collaboration for Advancing Data Infrastructure and GTM Analytics"
slug: gcp-xxx-oso-gitcoin-collaboration-for-advancing-data-infrastructure-and-gtm-analytics
category: citizen-grants
url: https://gov.gitcoin.co/t/gcp-xxx-oso-gitcoin-collaboration-for-advancing-data-infrastructure-and-gtm-analytics/19578
created_at: 2024-11-04T06:32:10.072Z
last_posted_at: 2025-01-17T08:22:50.522Z
posts_count: 13
views: 3747
like_count: 38
---

# [GCP - XXX] OSO-Gitcoin Collaboration for Advancing Data Infrastructure and GTM Analytics

<https://gov.gitcoin.co/t/gcp-xxx-oso-gitcoin-collaboration-for-advancing-data-infrastructure-and-gtm-analytics/19578>
rohit | 2024-11-04 06:32:10 UTC | #1

## Summary

This GCP proposes to fund tighter integration and ongoing use of analytics from [Open Source Observer (OSO)](https://www.opensource.observer/) to track cohorts of grantees before, during, and after they receive funding from grant programs on Grants Stack. We aim to enhance data infrastructure and develop advanced metrics to improve the grants experience and Gitcoin’s go-to-market strategy.

For this, we are requesting a total of $15K GTC from the Gitcoin treasury, equivalent to $2500/mo over 6 months.

## Abstract

Open Source Observer (OSO) analytics provides critical insights into grantee impact by capturing data on open source developer activity. This integration will enable more objective impact scoring, efficient fund tracking, and granular post-funding analysis of grantee performance.

There are two primary components:

* **Infrastructure:** Tighter integration and collaboration on improving grants data. Gitcoin would benefit from stronger data infrastructure, but should also keep its team lean and focused on growing GMV. OSO’s model of maintaining [public datasets](https://docs.opensource.observer/docs/integrate/overview/) and [public ETL infrastructure](https://docs.opensource.observer/docs/how-oso-works/architecture) can reduce Gitcoin’s maintenance burden while opening up additional pathways for the analyst / data science community to work on top of Gitcoin data.

* **Data-driven GTM:** Development of more advanced metrics to improve the grants experience and go-to-market. In addition to using more data to screen projects and provide impact metrics on Grants Explorer, there is a backlog of data science work the two organizations would like to pursue together. This includes co-developing new measures of builder quality, project momentum, and round success. Gitcoin wants to use data to improve its GTM strategy, help Round Operators configure their grants programs, and show ROI to funders.

## Motivation

The Gitcoin ecosystem requires transparent, data-driven insights into funded projects' impact. Current challenges include:

* Maintenance of ETL infrastructure
* Lack of automated data collection for grantee performance
* Difficulting joining Gitcoin data on other relevant datasets
* Need for more objective impact metrics, especially back to funders
* Limited visibility into post-funding outcomes
* Difficulty in demonstrating ROI and effectiveness of different allocation strategies

Previously, OSO data demonstrated the [impact of Gitcoin Grants](https://docs.opensource.observer/blog/tags/gitcoin/) on open source developer activity. Snapshots of OSO data have been integrated into the application sign-up and screening. Gitcoin also uses OSO’s free API to surface “impact stats” for OSS projects on Grants Explorer. At the same time, Gitcoin and OSO have worked closely in a variety of other contexts, including the Cartographers Syndicate, Optimism Retro Funding, and the Sunny Awards. OSO also maintains raw and indexed Gitcoin data in its public data warehouse.

By expanding this collaboration, we can provide high-resolution analytics for grant operators and program managers using Gitcoin Grants Stack, improving accountability and attracting new ecosystems to the platform.

This collaboration will result in:

* A single source of truth for Gitcoin project data that’s easy to join on other datasets
* More automated tracking of developer activity
* Standardized impact metrics across the grants lifecycle
* Continuous monitoring of funded projects and cohort-based analysis
* Data-driven insights for program and GTM optimization

## Specifications

### Work Components

#### Infrastructure

Existing Infrastructure:

* Allo Indexer and RegenData.xyz as ETL and data warehouse for Gitcoin data
* Regular updates to OSO’s [OSS Directory](https://github.com/opensource-observer/oss-directory) of projects in each Gitcoin grants round
* Gitcoin’s existing backend infrastructure for serving grant and funder data to users
* OSO’s project-artifact registration and mapping system, and events indexer for monitoring code contributions and blockchain transactions related to projects
* OSO’s free API and BigQuery access to metrics (plus easy integration with other public datasets)

New Development:

1. Alignment on ETL standards

  * Identify the critical data marts to serve business needs
  * Ingest and warehouse the necessary (raw) source data, e.g., from Allo Indexer
  * Implement schemas for processing and normalizing the data

2. Tighter integration and single (public) source of truth for grants data

  * Implement consistent project, round, and donor namespacing
  * Create automated updates for projects from Grants Stack applications
  * Ensure data synchronization and latency requirements are met

#### Data-driven GTM

3. Develop advanced analytics and GTM

  * Design v1 “builder quality” and momentum metrics
  * Create cohort analysis models for different rounds and categories of projects
  * Use metrics to power public dashboards and internal tools, addressing key questions like:
    1. How has grantee impact evolved before and after receiving funding?
    2. How do impacts compare across different rounds?
    3. Predict future impact using historical data to identify high-potential grantees.
    4. Analyze trends across rounds to refine future funding strategies.
  * Collaborate on GTM value proposition and round success metrics

### Milestones & Timeline

|Phase|Task|Date|
| --- | --- | --- |
|Phase I|Alignment on ETL standards|Month 1|
|Phase II|Tighter integration and single (public) source of truth for grants data|Month 2-3|
|Phase III|Develop advanced analytics and GTM|Month 4-6|

### Budget Breakdown

Total Request: $15K GTC ($2500/month for 6 months).

This effectively covers a portion of time spent by the OSO data & engineering teams. It does not cover any of the infrastructure costs, which will continue to be borne by each organization on its own. There is strong potential for a win-win here, so this GCP provides a springboard for additional work between Gitcoin and OSO in the future.

Note: There may be additional data requirements around metrics and reporting that come from partners and will be budgeted & scoped directly with those partners.

### Success Measures

1. Infrastructure

  * Source data is cleaned up and harmonized
  * All active OSS projects are indexed; relevant metrics available on Gitcoin
  * Ongoing data coverage and latency requirements are met

2. Analytics implementation

  * Release of v1 of builder quality and momentum models
  * Builder metrics integrated at the application stage and on grants explorer
  * Longitudinal analysis of grant cohorts by round and type of project

3. Adoption

  * Number of round operators using the analytics
  * User engagement with dashboards on Gitcoin website
  * Use of raw data in data warehouse and via the OSO API

### Benefits

1. Reduced data infra burden for Gitcoin
2. Enhanced decision making for round operators and donors
3. Improved transparency and accountability to funders
4. High quality and up-and-coming projects receive more funding
5. Ecosystem growth and better ROI

### Drawbacks & Considerations

1. Legacy data migration (eg, from cGrants, Allo v1)
2. Integration complexity with existing systems
3. Standardization / “hardening” of schemas
4. Data quality maintenance and pipeline upkeep
5. Finding robust metrics that are resistant to gamification

### Out of Scope

The following items are not included in this proposal:

* Impact metrics beyond open source developer activity
* Custom visualizations for specific grant programs
* Data entry for onboarding new ecosystems
* Deep dives / additional data science work

-------------------------

umarkhaneth | 2024-11-04 16:16:27 UTC | #2

Bullish. OSO has done amazing work pushing forward the grants and impact measurement space. I'm excited to have your expertise more available to us at Gitcoin and to work with familiar faces like @rohit and @ccerv1

-------------------------

Sov | 2024-11-04 18:18:47 UTC | #3

I’m in favor of this proposal as I believe this investment will enhance our data infrastructure and metrics capabilities. The team at OSO are proven and longtime partners to Gitcoin.

LFG!

-------------------------

ccerv1 | 2024-11-04 19:17:51 UTC | #4

I have a COI so will be abstaining from this GCP, but obviously think there is a huge win-win here. Happy to help clarify anything from the original post too.

-------------------------

meglister | 2024-11-06 21:48:00 UTC | #5

I'm in favor of this proposal and am grateful for the collaboration with the OSO team!

-------------------------

Joel_m | 2024-11-08 17:09:47 UTC | #6

I support this proposal. I can't speak to the finer points of the proposed infrastructure changes, but in general I'm very excited to see what we can do with easier access to data about impact.

-------------------------

owocki | 2024-11-18 15:52:15 UTC | #7

I support this proposal.  Seems like a big value add!

-------------------------

MathildaDV | 2024-11-19 09:46:05 UTC | #8

In massive support of this proposal! Love seeing this work coming to life.

-------------------------

MathildaDV | 2024-11-19 09:56:18 UTC | #9

And just as an FYI, GCP's are now bucketed under the Citizens Grants program. You can find out more about the new process here: https://gov.gitcoin.co/t/citizen-grants-program-updated-strategy/19203/12

I will also be updating everyone on next steps once a decision is made.

-------------------------

deltajuliet | 2024-11-19 10:14:25 UTC | #10

Support this proposal, thanks for thinking through the details. Excited to see this data come to life.

-------------------------

MathildaDV | 2024-11-21 05:17:41 UTC | #11

This proposal has passed by a majority vote through our internal GCP council. I will be in touch with this team directly for next steps!

-------------------------

disruptionjoe1 | 2024-12-24 19:05:25 UTC | #12

Highly in favor. I'm seeing a strong need for the alignment of data standards for the ETL portion of this. We are even seeing this with attempts to do it using attestations. There is budding fragmentation that Gitcoin could potentially head off for the betterment of the web 3 ecosystem as a whole.

-------------------------

rohit | 2025-01-17 08:28:01 UTC | #13

### Milestone 1 Update:
This post summarizes the outcomes of Milestone 1: Alignment on ETL Standards, highlighting how standardized queries and integrated pipelines effectively link funding data, development activity, and coding metrics for Gitcoin grantees. By creating a unified approach to normalizing and processing disparate data sources, the milestone ensures harmonized data outputs, enhances dataset usability, and lays a strong foundation for advanced analytics within Gitcoin’s Grants Stack.

The following queries show how you can use OSO to:

* Find and explore Gitcoin grantee (OSS) information in OSO's repository
* Evaluate coding activity, contributions, and productivity to assess project momentum and engagement
* Track funding patterns across rounds, review top-funded projects, and correlate funding with developer activity
* Identify similar grantees with comparable development profiles 
* Discover additional funders supporting Gitcoin grantees

Open Source Observer is a public good built with the community. We aim to make this data as widely available and easy-to-use as possible. We welcome you to explore the clean, normalized data to generate visualizations and insights, connect to your favorite data tools, and integrate into your existing applications.

You can execute these queries on the OSO Data Lake in BigQuery by following the instructions [here](https://docs.opensource.observer/docs/integrate/query-data) or setting up a local [Jupyter Notebook environment](https://docs.opensource.observer/docs/guides/notebooks/jupyter/) and using the tutorial Notebook available [here](https://github.com/opensource-observer/insights/blob/main/community/notebooks/oso_gitcoin_tutorial.ipynb).


### Query 1: Find a Gitcoin Grantee in OSO

You can search if an OSS Gitcoin Grantee's data is available in OSO by using their name as follows:
```
query = """
select project_id, project_name, display_name
from `oso_production.projects_v1`
where lower(display_name) like lower('%open%source%')
"""
results = client.query(query)
results.to_dataframe()
```
The matching records are displayed as follows. You can utilize the field project_name, say “opensource-observer”, for additional information on the grantee, as shown in the following queries.

![|624x145](upload://qTualQwgziQQzUoRtH1XFSvIWpD.png)

OSO manages a repository of open source projects, including OSS grantees in Gitcoin, called the [oss-directory](https://github.com/opensource-observer/oss-directory). This repository serves as the foundation of the OSO data pipeline. By running indexers on every artifact linked to projects in the directory, OSO generates metrics that power its API and dashboards, providing valuable insights into project performance and impact.

### Query 2: Query the latest coding metrics for a project

> Evaluating the latest coding metrics for a project provides critical insights into its development activity, community contributions, and overall momentum in the open source ecosystem.

After identifying the project in OSO, you can quickly evaluate its recent performance by reviewing its coding metrics for the past six months with the following query:
```
query = """
select
project_name,
display_name,
star_count,
fork_count,
commit_count_6_months,
contributor_count_6_months
from `oso_production.code_metrics_by_project_v1`
where project_name = 'opensource-observer'
"""
results = client.query(query)
results.to_dataframe()
```

![|624x48](upload://19748jcmACk1GmcGL6Ppb9b4NGN.png)

Besides the above metrics, the dataset also allows for analyzing trends in code contributions, issue resolution, community engagement, and project releases. These insights collectively offer a comprehensive view of a project's health and momentum, enabling data-driven evaluations for funding decisions. It’s important to note that developer activity is an input metric rather than the desired impact outcome; however, it offers valuable context for understanding engagement and sustainability.

### Query 3: Track Project Funding Across Gitcoin Grant Rounds

> Tracking project funding across Gitcoin Grant rounds offers a clear view of a project's growth trajectory, funding patterns, and its appeal to the community over time.

This query aggregates the total funding received by the project in each Gitcoin Grant round.
```
query = """
SELECT
grant_pool_name,
sum(amount) grant
FROM `oso_production.oss_funding_v0`
WHERE to_project_name = 'opensource-observer'
and from_project_name = 'gitcoin'
group by grant_pool_name
"""
results = client.query(query)
results.to_dataframe()
```

![|624x263](upload://o5QhzGkKzt02k7FHsTozBkkDOXZ.png)

OSO maintains the [oss-funding](https://github.com/opensource-observer/oss-funding) repository, which houses Gitcoin funding data alongside a curated registry of grants and other funding sources for open source software (OSS) projects. This directory is free to use and distribute as a public good, aiming to support researchers, developers, foundations, and others in gaining deeper insights into the OSS ecosystem.

### Query 4: Explore the Latest Coding Metrics for Top-Funded Projects in a Round
> Understanding how top-funded projects perform provides valuable insights into their sustainability, community engagement, and potential for long-term impact.

In this example, you can discover the top 20 funded projects from the GG22 Developer Tooling and Libraries round and gain insights into their development activity. View key metrics such as active developers, commits, issues opened, stars, and forks over the past six months, alongside their total funding in the round.

```
query = """
WITH project_funding AS (
SELECT
to_project_name,
SUM(amount) AS total_funding,
COUNT(DISTINCT event_source) AS funding_sources
FROM `oso_production.oss_funding_v0`
WHERE grant_pool_name = 'GG-22 - 609'
GROUP BY to_project_name
ORDER BY total_funding DESC
LIMIT 20
)
SELECT
f.to_project_name,
f.total_funding,
f.funding_sources,
m.active_developer_count_6_months,
m.commit_count_6_months,
m.opened_issue_count_6_months,
m.star_count,
m.fork_count
FROM project_funding f
JOIN `oso_production.code_metrics_by_project_v1` m
ON f.to_project_name = m.project_name
ORDER BY f.total_funding DESC;
"""
results = client.query(query)
results.to_dataframe()
```

![|624x361](upload://3dUMYSgQHixHwPII5cHCWzndgbk.jpeg)

### Query 5: Normalized Funding Productivity: Commits per Developer vs. Total Funding
> Understanding how funding correlates with developer activity helps assess funded projects' engagement and resource utilization.

Continuing the analysis from the prior example, the following example inspects how funding translates into developer activity for the top 20 projects.

```
import plotly.express as px
results_df = results.to_dataframe()

# Calculate the ratio of commit_count_6_months to active_developer_count_6_months
results_df['commit_ratio'] = results_df['commit_count_6_months'] / results_df['active_developer_count_6_months']

# Create the scatter plot using Plotly with bubble size
fig = px.scatter(
results_df,
x='total_funding',
y='commit_ratio',
size='active_developer_count_6_months', # Bubble size
size_max=50,
text='to_project_name',
hover_data=['to_project_name'],
labels={
'total_funding': 'Total Funding ($)',
'commit_ratio': 'Commits per Active Developer',
'active_developer_count_6_months': 'Active Developers'
},
title='Commit Ratio vs Total Funding for Top 20 Projects in GG-22 - 609',
log_x=True, # Logarithmic X-axis
log_y=True # Logarithmic Y-axis
)

# Update layout for better visualization
fig.update_layout(
xaxis_title='Total Funding ($)',
yaxis_title='Commits per Active Developer',
height=1000,
width=1000
)

# Show the scatter plot
fig.show()
```

This scatter plot visualizes total funding against the normalized ratio of commits per active developer, with bubble sizes representing the number of active developers. It offers insights into how efficiently teams utilize funding relative to their developer engagement.

![|624x624](upload://3OOQuFZlCkiq6xUJGtfWlsoudCE.png)

### Query 6: Discover grantees with the most similar coding metrics to another project
> Identifying projects with similar development profiles can uncover potential collaborators, reveal benchmarking opportunities, and highlight successful patterns in the open-source ecosystem.

This query compares metrics such as active developers, commits per developer, and contributors per developer to find the top 10 projects most similar to Open Source Observer.

```
query = """
WITH reference_metrics AS (
SELECT
active_developer_count_6_months AS reference_active_developers,
commit_count_6_months / active_developer_count_6_months AS reference_commit_per_developer,
contributor_count_6_months / active_developer_count_6_months AS reference_contributor_per_developer
FROM `oso_production.code_metrics_by_project_v1`
WHERE project_name = 'opensource-observer'
)

SELECT
project_name,
active_developer_count_6_months,
commit_count_6_months / active_developer_count_6_months AS commit_per_developer,
contributor_count_6_months / active_developer_count_6_months AS contributor_per_developer,
SQRT(
POWER((commit_count_6_months / active_developer_count_6_months - reference_commit_per_developer), 2) +
POWER((contributor_count_6_months / active_developer_count_6_months - reference_contributor_per_developer), 2) +
POWER((active_developer_count_6_months - reference_active_developers), 2)
) AS similarity_score
FROM `oso_production.code_metrics_by_project_v1`, reference_metrics
WHERE project_name != 'opensource-observer'
and active_developer_count_6_months > 0
ORDER BY similarity_score ASC
LIMIT 10;
"""
results = client.query(query)
results.to_dataframe()
```

![|624x236](upload://dQ7h3B0VSnmh8IquaVlbJ2YqBqC.jpeg)

### Query 7: Find other funders of the top Gitcoin Grants recipients

> Understanding the funding relationships for top-supported projects reveals key contributing funders, highlights funding patterns, and provides insights into collaborative networks within the ecosystem.

This query identifies the top 50 Gitcoin-funded projects and aggregates their funding amounts, breaking down contributions by funders to showcase the most influential backers and their impact.

```
query = """
WITH top_projects AS (
-- Select the top 50 projects funded by Gitcoin
SELECT
to_project_name,
SUM(amount) AS total_funding
FROM
`oso_production.oss_funding_v0`
WHERE
from_project_name = 'gitcoin'
GROUP BY
to_project_name
ORDER BY
total_funding DESC
LIMIT 50
)
SELECT
o.to_project_name AS project,
o.from_project_name AS funder,
SUM(o.amount) AS funding_amount
FROM
`oso_production.oss_funding_v0` o
JOIN
top_projects t
ON
o.to_project_name = t.to_project_name
GROUP BY
o.from_project_name, o.to_project_name
ORDER BY
project, funding_amount DESC;
"""
results = client.query(query)
results.to_dataframe()
```

Here's a Sankey diagram created using the outputs of the above query showing the flow of funds for top Gitcoin grantees from other ecosystems, using linked nodes and proportional flow widths to highlight relationships and the magnitude of transfers.

![|624x447](upload://39O9xjimhICrBHK6x3Cq1lWaN8V.png)

### What's upcoming?
The next phase of the grant focuses on automating project updates, ensuring data synchronization, and developing advanced analytics further to enhance Gitcoin’s grant management and go-to-market strategy.

-------------------------
