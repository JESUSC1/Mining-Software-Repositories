File: Collect_Issue_Data.py

Description:
This code allows you to mine data from GitHub repositories using the GitHub API. Specifically, it retrieves information on issues for the repositories specified in the repos dictionary, which contains the names and owners of the repositories.

Requirements:
The code requires the following Python modules:

os
csv
requests

Usage:
1. Make sure you have a GitHub API token. If you don't have one, you can create one here.

2. Set the TOKEN variable to your GitHub API token.

3. Specify the repositories you want to mine data from in the repos dictionary.

4.Set the csv_save_path and txt_save_path variables to the paths where you want to save the CSV files and text files containing the data.

5. Run the code.

Output:
The code outputs a CSV file and a text file for each repository specified in the repos dictionary. The CSV file contains information on each issue, including the issue ID, state, labels, assignees, number of comments, created date, closed date, and locked status. The text file contains the comments for each issue.

Author:
This script was created by Jesus Cantu. Feel free to contact me with any questions or feedback.


