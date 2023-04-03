from github import Github
import requests
import csv
from requests.exceptions import Timeout

# Authenticate with a personal access token
g = Github("github_token")

# Define the repos
repos = ["owner/repo"]

# Iterate over the repos
for repo_name in repos:
    print(f"Processing repository {repo_name}...")
    
    # Get the repository
    repo = g.get_repo(repo_name)

    # Initialize an empty list for commit data
    commit_data = []

    # Iterate over all commits
    for commit in repo.get_commits():
        # Get the commit URL and tree URL
        commit_url = commit.url
        tree_url = commit.commit.tree.url

        try:
            # Get the commit data
            commit_data_request = requests.get(commit_url, timeout=5)
            commit_data_json = commit_data_request.json()
        except Timeout:
            print(f"Timed out while fetching data for commit {commit.sha} in repository {repo_name}. Skipping...")
            continue

        # Check if the "commit" key is present in the JSON response
        if "commit" not in commit_data_json:
            continue

        committer = commit_data_json["commit"]["committer"]["name"]
        date = commit_data_json["commit"]["committer"]["date"]

        # Get the tree data
        try:
            tree_data_request = requests.get(tree_url, timeout=5)
            tree_data_json = tree_data_request.json()
        except Timeout:
            print(f"Timed out while fetching tree data for commit {commit.sha} in repository {repo_name}. Skipping...")
            continue

        if "tree" in tree_data_json:
            code_size = sum([file["size"] for file in tree_data_json["tree"] if file["type"] == "blob"])
        else:
            code_size = 0

        # Append commit data to the list
        commit_data.append([committer, date, tree_url, code_size])

    # Save the commit data as a CSV file
    with open(f"{repo_name.replace('/', '_')}_commit_data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Committer", "Date", "Tree URL", "Code Size"])
        writer.writerows(commit_data)
        
    print(f"Finished processing repository {repo_name}.")
