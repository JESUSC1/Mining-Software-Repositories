"""
This code fetches data for a repository from the GitHub API and saves it to a CSV file 
and a text file. The CSV file contains information about the repository's issues, 
such as the issue ID, state, labels, assignees, number of comments, created and closed dates, 
and whether the issue is locked. The text file contains the comments for each issue.

Script Author: Jesus Cantu
"""

# Import required libraries 
import os
import csv
import requests

# GitHub API token
TOKEN = "GitHub_Token"

# Repository names and their owners, e.g., "repo1": "owner1"
repos = {"repo1": "owner1", "repo2": "owner2", "repo3": "owner3"}

# Columns for CSV
columns = ["owner", "repo_name", "issue_id", "state", "labels", "assignees", "number_of_comments", "created_at", "closed_at", "locked"]

# Save paths
csv_save_path = "file_path" # Path ~/MiningSoftwareRepositories/Raw_Data/Issues
txt_save_path = "file_path" # Path to ~/MiningSoftwareRepositories/Raw_Data/Issues/comments

# Loop through repositories
for repo, owner in repos.items():
    # Print message for starting
    print(f"Fetching data for {repo}...")
    
    # GitHub API URL
    url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=all&per_page=100"

    # Create CSV file
    csv_file_path = os.path.join(csv_save_path, f"{repo}_issues.csv")
    with open(csv_file_path, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=columns)
        writer.writeheader()

        # Create text file for comments
        txt_file_path = os.path.join(txt_save_path, f"{repo}_issues_comments.txt")
        txt_file = open(txt_file_path, "w")

        # Get issues from GitHub API
        try:
            page = 1
            while True:
                response = requests.get(url+f"&page={page}", headers={"Authorization": f"Bearer {TOKEN}"}, timeout=25)
                issues = response.json()
                if not issues:
                    print(f"No issues found for {repo}")
                    break

                # Loop through issues and write to CSV every issue
                for issue in issues:
                    # Write to CSV file
                    writer.writerow({
                        "owner": owner,
                        "repo_name": repo,
                        "issue_id": issue["number"],
                        "state": issue["state"],
                        "labels": ", ".join([label["name"] for label in issue["labels"]]),
                        "assignees": ", ".join([assignee["login"] for assignee in issue["assignees"]]),
                     #  "comments": issue["body"],
                        "number_of_comments": issue["comments"], 
                        "created_at": issue["created_at"],
                        "closed_at": issue["closed_at"],
                        "locked": issue["locked"]
                    })

                    # Write comments to text file
                    txt_file.write(f"Issue {issue['number']} - Author: {issue['user']['login']}\n")
                    txt_file.write(f"{issue['body']}\n\n")

                # Check if there are more pages
                if 'next' not in response.links:
                    break
                page += 1
        except requests.exceptions.Timeout:
            print(f"Skipping data for {repo} due to timeout.")

        # Close text file
        txt_file.close()

    # Print message for finishing
    print(f"Data for {repo} saved to {csv_file_path} and comments saved to {txt_file_path}.")
