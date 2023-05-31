# MiningSoftwareRepositories
Project for COMP 370/470: Software Quality &amp; Testing 

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/JESUSC1/MiningSoftwareRepositories.git/HEAD)

Project: 
-
    Build an automated data pipeline to mine information from software repositories hosted on GitHub. 
    Complete instructions can be found under 'COMP 370_470_Week 9.pdf' (Pages 14-15). 

Project Stages: 
-
    Stage 1: Pull all issues (open and closed) for the given owner (user or org) and repo, 
             Request parameters (e.g., state = all, page, per page),
             Identify attributes of interest (e.g., state, labels, assignees, etc.) and 
             Visualize and analyze data in various ways 
    
    Stage 2: Pull all commits for the given owner and repo,
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

			
>>>>>>> d09a1317813e1b29440038254ad532364b0ea61d
