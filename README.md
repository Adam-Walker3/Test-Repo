# Adam-Test-Repo
[![Python package](https://github.com/cdk-global/Adam-Test-Repo/actions/workflows/pythonCICD.yml/badge.svg)](https://github.com/cdk-global/Adam-Test-Repo/actions/workflows/pythonCICD.yml)

## Notes
- Find pros and cons of Bamboo and Github Actions
- Bamboo build plans are exported as Java Specs
- Bamboo can use yaml build plans if manually created and stored in linked repo
- Github Actions only supports yaml config files 


## Github Actions
#### Pros: 
- Ease of editing build configurations (Configuration as Code)
- Can specify multiple versions of languages and operating systems for compatibility
- Download artifact from seperate workflow
- Lots of templates for different projects, and create your own
- Github hosted runners

#### Cons:
- Does not support Java specs
- 

#### Limitations:
- 100 workflows run per 10 seconds
- Jobs can run up to 6 hours, terminated after
- Workflows limited to 72 hours
- Bamboo - Unlimtied local agents and jobs. Cost based on number of remote agents

## Bamboo
#### Pros:
- One overall dashboard showing all build statuses
- Java specs are more versatile
- Hosts wide tech stack with any language
- Automatically applies build config to new branches

#### Cons:
- Mainly supports Java specs
- Overall pricing is more than Github (per Srinibas)


## Commonalities
- Add and run scripts through workflow
- Save job output for job input
- Store sensitive data as environment variables
- Integrate JIRA with marketplace app in Github, Already integrated in Bamboo
- Ability to use JFrog Artifactory on both platforms

#### Sources
https://docs.github.com/en/actions/learn-github-actions/essential-features-of-github-actions
Discussion in 2018 regarding converting Java specs to YAML: https://community.atlassian.com/t5/Bamboo-questions/Tools-to-convert-bamboo-java-specs-to-bamboo-yaml-specs/qaq-p/746539