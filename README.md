# Mining-Software-Repositories

<img src="github-logo.jpeg" alt="GitHub Image" width="450">

The objective of this project is to develop an automated data pipeline to mine information from software repositories hosted on GitHub. Complete guidelines for this endeavor are provided in `COMP 370_470_Week 9.pdf` (Pages 14-15).

## Data Source
The primary data source for this project is GitHub, an extensive platform that hosts software repositories. By utilizing GitHub's API, this project mines data from specified repositories to gather insights on issues, commits, and code structure.

## Project Stages

### Stage 1: Issues Data Mining
- Pull all issues (both open and closed) for the specified owner (user or organization) and repository.
- Utilize request parameters like `state=all`, `page`, and `per page`.
- Identify attributes of interest such as state, labels, assignees, etc.
- Engage in diverse visualization and data analysis methodologies.

### Stage 2: Commits Data Mining
- Retrieve all commits for the given owner and repository.
- Employ request parameters such as `page` and `per page`.
- Pinpoint attributes of interest like date, commit, committer, tree, URL, etc.
- Undertake various visualization and analytical approaches.

### Stage 3: Git Tree Data Extraction
- For the specified repository, extract each commit’s git tree based on the commit URLs.
- Leverage request parameters like `recursive=true`.
- Identify attributes of interest including tree, size, path, etc.
- Aggregate over size to compute the code `size` for a particular commit.
- Engage in a wide range of visualization and data analysis techniques.

### Stage 4: Data Synthesis and Analysis
- Integrate the issue data from Stage 1 with the code size data.
- Delve deep into diverse visualization and data analysis methods.

## Libraries Used
The analysis utilizes the following Python libraries and packages:
- `Seaborn`: Data visualization library based on Matplotlib.
- `Scipy`: Library used for high-level computations.
- `Matplotlib`: 2D plotting library.
- `OS`: Module for interacting with the operating system.
- `CSV`: Module for reading from and writing to comma-separated value (CSV) files.
- `Pandas`: Data manipulation and analysis.
- `Numpy`: Library for numerical operations.
- `PdfPages (from Matplotlib)`: Utility for saving multiple figures to a single PDF.
- `Warnings`: Module to handle warning messages.

## Analysis
The project employs a systematic approach, starting from data collection to detailed analysis. Each stage focuses on specific data types, such as issues or commits, and leverages various analytical techniques to uncover patterns, trends, and insights. The visualizations aid in understanding the evolution of repositories over time and highlight key attributes of interest.

## Key Achievements
- Successfully established an automated data pipeline to mine and analyze GitHub repositories.
- Uncovered intricate patterns in issues and commits, providing a holistic view of repository evolution.
- Integrated diverse data sources, facilitating comprehensive analysis and visualizations.

## Conclusion
The "Mining-Software-Repositories" project showcases the potential of data mining in understanding the intricacies of software development. Through methodical stages of data extraction, processing, and analysis, this project offers valuable insights into the dynamics of software repositories.

## Future Work
- Enhance the granularity of data extraction to capture finer details of repositories.
- Implement machine learning algorithms to predict trends in repository activity.
- Expand the scope to include more repositories and achieve broader insights.

## Author
Jesus Cantu Jr.

## Last Updated 
April 3, 2023

