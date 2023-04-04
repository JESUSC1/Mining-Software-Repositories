# MiningSoftwareRepositories
Project for COMP 470: Software Quality &amp; Testing 

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/JESUSC1/MiningSoftwareRepositories.git/Master)

Project: 
-
    Build an automated data pipeline to mine information from software repositories hosted on GitHub. 
    Instructions can be found under 'COMP 370_470_Week 9.pdf' (Pages 14-15). 

Project Stages: 
-
    Stage 1: Pull all issues (open and closed) for the given owner (user or org) and repo, 
             Request parameters (e.g., state = all, page, per page),
             Identify attributes of interest (e.g., state, labels, assignees, etc.) and 
             Visualize and analyze data in various ways 
    
    Stage 2: Pull all commits for the given owner and repo=,
             Request parameters (e.g., page, per page),
             Identify attributes of interest (e.g., date, commit, commiter, tree, url, etc.) and 
             Visualize and analyze data in various ways 
    
    Stage 3: For the given repo, pull each commit’s git tree based on the commit URLs,
             Request parameters (e.g., recursive = true),
             Identify attributes of interest (e.g., tree, size, path etc.),
             Use aggregation over size to compute the code size for this commit and 
             Visualize and analyze data in various ways 
   
   Stage 4: Combine the issue data from step 1 with the code size data and 
            Visualize and analyze data in various ways


Team Members:
-
     Cantu, Jesus
     Ali, Faisel
     Hafner, Trevor
     Tesillos, Angel 
     
Team Members Contributions:
-
          Cantu, Jesus: Created repository, wrote scripts to: collect issues/commits, process the data (e.g., create new columns based on datetime information), and  analyze issue data (e.g., correlation analysis, time-series plots)
