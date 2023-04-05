# MiningSoftwareRepositories
Project for COMP 370/470: Software Quality &amp; Testing 

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/JESUSC1/MiningSoftwareRepositories.git/HEAD)

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


Team Members:
-
     Cantu, Jesus (GitHub Username: JESUSC)
     Ali, Faisel
     Hafner, Trevor
     Tesillos, Angel 
     
Team Members Contributions:
-
          Cantu, Jesus: Created repository, wrote scripts in Python to:
                        Collect issues/commits along attributes of interest for specific repos, 
                        Process the data (e.g., create new columns based on datetime information) and
                        Analyze/Visualize issue data for Stage 1 (e.g., correlation analysis, time-series plots)
	Hafner, Trevor: Made some small edits to the README file.
			Commenced on the work for the Stage 4 comparison between the number of open issues and the code size.
