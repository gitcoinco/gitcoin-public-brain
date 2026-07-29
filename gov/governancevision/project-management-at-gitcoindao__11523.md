---
id: 11523
title: "Project Management at GitcoinDAO"
slug: project-management-at-gitcoindao
category: governancevision
url: https://gov.gitcoin.co/t/project-management-at-gitcoindao/11523
created_at: 2022-09-17T00:13:32.831Z
last_posted_at: 2022-09-27T19:47:14.025Z
posts_count: 11
views: 3629
like_count: 29
---

# Project Management at GitcoinDAO

<https://gov.gitcoin.co/t/project-management-at-gitcoindao/11523>
puncar | 2022-09-17 00:19:07 UTC | #1

# Intro

@tigress , @june , and @puncar-dev would like to present our suggestions for the standardization of our project/task management process within GitcoinDAO. We genuinely believe that flexibility within workstreams and initiatives is essential, but we should all speak the same language. Here we’ll focus only on core principles and keep space for specific workstream needs.

**This initial proposal is a request for comments – we would appreciate your view on this so we can prepare a final recommendation for the DAO (CSDO).**

# Problem statement

The Action Items DB (Notion Database ([Link](https://www.notion.so/gitcoin/b349e7d525064335b4f8f6ae34b2cd6c?v=58412819cbbc4d89bc31c963d53c5866))) is the centerpiece of all our project and/or task management activities at GitcoinDAO.

This database should contain all the tasks and projects we are executing on. For this reason, this database must be in good shape and well maintained in terms of structure and content. Currently, every workstream uses it slightly differently, increasing the database's complexity and making it harder to set up individual instances.

Therefore, we need to find an alignment between workstreams to use the database similarly and ensure consistency in the naming (the same word should mean the same across the workstreams), but keep the flexibility to ensure that the database works well for each workstream.

From the DAOops perspective, all initiatives need to be able to record their tasks and projects on their board and then report on successful project completion on weekly DAOops calls. But MMM might need something slightly different; thus, we must find a flexible solution for everyone.

# Project Management Structure

Through analyzing the project management systems at DAOops, FDD, and MMM, we have concluded that there are two general workflows: the execution workflow, and the reporting workflow. The execution workflow refers to actions for completing work, and the reporting workflow refers to how the completed work relates to achieving objectives and key results.

We suggest using the Action Items DB and the Initiatives DB (Notion Database ([Link](https://www.notion.so/gitcoin/c797e0f0cf43404fb9770e59e3dfae50?v=e9f5014af06241fda400226da70e64b1))) to manage these two workflows. Below is the overall structure:

![|624x765](upload://oXd9xVbmZTd55LfRwr4rAPSgdXR.jpeg)

The Action Items DB will contain tasks, projects, and key results. The Initiatives DB will contain initiatives and their related objectives, and are also directly linked to projects and key results from the Action Items DB.

It’s up to each workstream to decide how many steps they want to have in their project management process, and if they want to introduce a new tag or subcategory. However, it is vital to keep alignment on the basic structure.

## Action Items DB

### Action Item

An Action Item is the centerpiece of the Action Items DB. This field can be used to represent tasks, projects, or both – this distinction will vary across workstreams.

If used to represent a project, the field can still be used to incorporate tasks as another level of granularity. Using this field for both projects and tasks is possible by making use of filters and establishing clear relations between tasks and projects.

Or, the Action Item field can be used mainly as tasks, and bundled together into projects.

Alternatively Action Items can also directly relate to an Initiative. There is a lot of flexibility for WorkStreams but its important to keep the same flow:

1. Key Results - represents what Initiatives promised to accomplish for the budget they have been given, usually a seasonal initiative
2. Project - break down of key results to a smaller initiatives that takes couple of weeks to complete
3. Task - smallest piece of work that doesnt take more than couple days to complete

### Templates

The templates we have created will represent the various ways that Action Items can be used in the Action Items DB. Currently, there are three templates that can be used when creating an Action Item:

![|222x107](upload://yFL5qkfREFavqECKLHksMF7ydxG.png)

1. Project Template

A project is an Action Item within the Action Items DB that represents a multiple-week effort to be achieved. A project can contribute to successfully completing a Key Result of an Initiative. Additionally, some projects may also stand on their own (e.g. research projects), thus enabling autonomy within workstreams.

Projects may contain multiple tasks; therefore, the project template enables seamless task creation from within it.

![|624x119](upload://5QezEwoYJDLBAPZTY3JkDA8QNjv.png)

2. Task Template

A Task functions like a Project, but is used as an additional level of granularity. A Task can roll up and relate to a separate, larger Action Item. This can be done by marking Tasks as dependencies on a Project or Key Result.

A task can be created from a project’s Notion page or separately in the Action Items DB and then tagged to a project.

![|624x125](upload://cnoJbsaOzvoe2IPvViJIycgqnm8.png)

3. Key Results Template

A Key Result is the third type besides Tasks and Projects for which the Action Items DB can be used. The set of Key Results represents what Initiatives promised to accomplish for the budget they have been given and always relates to an objective. It's important to keep that in mind when executing on projects or tasks. Majority projects should contribute partially or fully to accomplishing those key results.

All initiative leads should create the key results at the beginning of the season and then they can track all projects and tasks there on top of there.

![|624x363](upload://61Ua8pZhRUIaJsQvGlls0E0L7ZZ.jpeg)

## Initiatives DB

### Initiatives

An Initiative is a structure in the Initiatives DB. It represents a grouping element to gather a group of people (=squad or team) around a specific objective and set of key results. An initiative has a "lead person" which is the Initiative Owner, and others are contributors. Large initiatives are executed as a set of projects to achieve key results. Smaller initiatives might not use projects to bundle tasks and instead directly execute tasks to achieve the key results.

Below, you can see an example of an initiative wide view divided by projects.

![|624x239](upload://yfhPtAlejuUDFL5KChG6T9aKQZy.jpeg)

### Objective

An objective is a precise sentence describing what we intend to achieve by the end of the season for a given Initiative(s), and the overarching goal for an initiative. To realize and deliver option the objective a set of key results is defined.

### Gitcoin Essential Intent (EI)

The Gitcoin EI is situated at DAO level and represents long term “30 year” objectives. The EI outlineswhat we are all trying to accomplish together as a DAO, and all our activities should directly or indirectly contribute to that.

# Recommendation for project & task workflow

Every project or task can be in various stages, and to align on naming conventions, June and the MMM team have prepared this great workflow. FDD also uses this workflow.

It is highly recommended to use these same statuses when dealing with projects and tasks, even though you might not use all of them. Creating additional statuses for a single initiative or project can create confusion in the DAO and add up to increase complexity of the Notion databases, which is to be refrained from!

### Happy Path![|624x188](upload://sth0yATLcd5x7nb4RquNvjiqSfJ.png)

### Unhappy Path

![|624x351](upload://hRSZvlcB7mKKcvUOl9P6HnYOG15.png)

|Status|Description|
| --- | --- |
|Future|Backlog for all projects or tasks related to the initiative(s)|
|Next up|Prioritized projects/tasks to be started within the next two weeks|
|In progress|Projects/Tasks that are actively being worked on|
|In review|Projects/Tasks being reviewed (optional, only if project requires review)|
|Blocked|Projects/Tasks that are currently blocked|
|On hold|Deprioritized Projects/Tasks before they get back to “future” or dropped to “won’t do”|
|Done|Completed Projects/Tasks (woo!)|
|Won’t do|Dropped Projects/Tasks|

**We would leave this proposal up whole next week for discussion and then propose a final version in about 2 weeks from now to CSDO. If ratified we would like to work with workstreams during October to incorporate those standards.**

**Please let us know if there is anything unclear from this proposal or if you would suggest any modifications.**

-------------------------

DisruptionJoe | 2022-09-18 16:34:03 UTC | #2

This is a great start. You have my consider suggestions on the original doc. I do think it is impactful to point out that you formatted this in a way that workstream reps in CSDO can set STRATEGY level objectives and initiatives together, but the workstreams would be empowered to solve what the best opportunities, features, user stories, projects, and tasks would be in a bottom up way if preferred.

-------------------------

tigress | 2022-09-19 10:57:25 UTC | #3

Yes, and what I am seeing also is that the level of freedom and autonomy of workstreams and contributors is not yet made visible in this document. 

For example, I personally believe that not 100% of all the work must be aligned and traceable to a strategic element. Workstreams should have the authority of e.g. running their own research projects. The Pareto Principle of 80% working towards achieving Initiatives and 20% explorative, emergent work seems to be feasible to me.

-------------------------

safder | 2022-09-19 23:34:27 UTC | #4

Really happy to see this conversation started! Would love to arrive at a consistent understanding of how things are done in the DAO - @CoachJonathan led a great discussion on the importance of documenting "how we work" in addition to just "what we work on", and I'm convinced that better processes and documentation in that realm will prevent balls from being dropped and reduce coordination failures. 

I'd love to hear why this way of documenting and managing tasks is being suggested - in other words, what's the "Why" for each of the elements of this model? Personally, I've tried and struggled with using Notion for task management, and have created my own personal workflow that works for me (currently using a combination of Asana + Sunsama). With all process adoption proposals within a self-managing organization, I think there needs to be a strong "why" for people to switch from tools/structures/processes they are currently using. Fortunately there's a ton of research on this topic so I think we can come up with something that has been demonstrated to lead to better team and individual contributor health.

-------------------------

tigress | 2022-09-20 17:14:05 UTC | #5

[quote="safder, post:4, topic:11523"]
what’s the “Why”
[/quote]

The bigger WHY behind the proposed approach has several answers to it. 

TLDR: it's all about coordination ;-)


@puncar's take is: if you need to track your todo only for yourself, you can and probably should track it in the tool of your choice. But when we need to cooperate or share information with each other, we need to speak the same language, otherwise, we are creating friction or we just won't understand each other. 

And that's why we are creating those standards, to try to establish the common language, but also to not restrict individual flexibility

@june agrees with that and adds: we're striving for easier and better collaboration & it gets that much harder to do if we're not creating the same level of transparency & using the same tools/process

we're def not trying to restrict individual and even workstream flexibility - just setting the foundations for each workstream to expand upon

And **my stance** is: our ideas are borrowed from basic Kanban as a methodology to manage work in progress and enable transparency. of course there is a whole lot more which can be done with Kanban. we are touching the tip of the iceberg.

and we reuse the tools, such as Notion, which are already in place and adopted by the DAO

Hope I am not embarrassing you - the WHY is not that spectacular :-D

-------------------------

shawn16400 | 2022-09-22 00:37:18 UTC | #6

Team, This is great work and if implemented, can make results reporting and budgeting much more simple.  The project framework makes sense: an Initiative may hold several projects which may hold many tasks.  Yes there can be projects / tasks which do not ladder up to an initiative, but those should be the exception. 
I had to diagram it out - starting with the budget proposal to see if it made sense.  Initially the relationships between key results, objectives, and Initiatives felt a bit clunky, but it seems to work in my relatively simple domain.   
![image|690x420](upload://uKwiDifKqTg4pUsEgKGsUCQVeVG.png)

Looking forward - how do you see an executive level board review using the database(s)? Would there be a view that can be shown to illustrate the overall health of the season?

-------------------------

puncar | 2022-09-25 19:32:45 UTC | #7



[quote="shawn16400, post:6, topic:11523"]
Looking forward - how do you see an executive level board review using the database(s)? Would there be a view that can be shown to illustrate the overall health of the season?
[/quote]

Hey Shawn, yes that's a great point, and yes it will be possible as all data will live in the same database in the same structure, it will be a dream for any data analyst to run reports on it.  We have not planned reporting dashboards as part of this project, but its definitely a feature of this concept.

-------------------------

krrisis | 2022-09-26 18:06:11 UTC | #8

Great overview, thanks for all your hard work on this Puncar!

Only thing I wonder is if we need 'objectives' in the initiatives database, this might be an unnecessary layer, but maybe I'm missing something here? 

If each initiative has one objective (which seems to be the case reading your description), what's the use of adding this layer here? It might be enough to just directly link to the key results per initiative?

-------------------------

bobjiang | 2022-09-27 06:48:56 UTC | #9

Thanks a lot, @puncar and your team for this initiative!

one comment is in the area `template` - https://gov.gitcoin.co/t/project-management-at-gitcoindao/11523#templates-6

I didn't get it clear for Project Template and Task Template with the screenshots. (e.g in project template, the screenshot says "task 5". Is it task or project? In task template, nothing shows it is a task but some details and key dates and documents)

The last comment is whether you could have demo or good practice for how to use this guide (once it is approved).

-------------------------

puncar | 2022-09-27 19:44:08 UTC | #10

Great point Bob and I admit those partial screenshots might not give the best sense of how the templates will look, let me repost it here in full. 

### Innitiative page
It will display all project and its task on the board
![Screen Shot 2022-09-27 at 3.34.55 PM|690x303](upload://9gjRyzGhhpGhZeBQ5zC3DnSdiiN.jpeg)

### Project page (template)
That will show a description of the project, any additional details, and all the tasks that belong to that project

![Screen Shot 2022-09-27 at 3.35.53 PM|690x242](upload://vQ5pbJmhIXLTUL4iEFWtozYfuf6.png)

### Task page (template) 
Similar to the project page (template), but does not have subtasks, instead shows the project to which this task belongs and additional details of the project itself. 
![Screen Shot 2022-09-27 at 3.37.48 PM|690x258](upload://c0EjO1YD2QFK4S6somOxucMGOgl.png)

Hope this makes it more clear, and we will provide support to anyone who would be struggling with the setup.

-------------------------

puncar | 2022-09-27 19:47:14 UTC | #11

Good point Kris, I think we should have an objective as a guiding NorthStar for every initiative, but I agree that it doesn't necessarily need to be within the initiative database.

-------------------------
