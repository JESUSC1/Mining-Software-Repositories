This repository contains CSV files that contains commit data extracted from a Git repositories using PyDriller. Each CSV file has a header row that describes the fields that will be extracted for each commit. Below is a description of each variable (i.e, column) and how it was calculated:

commit_id: The unique identifier for the commit.
message: The commit message.
author_name: The name of the author who committed the code.
author_email: The email of the author who committed the code.
author_date: The date and time when the author committed the code.
author_tz: The timezone of the author who committed the code.
committer_name: The name of the committer who committed the code.
committer_email: The email of the committer who committed the code.
committer_date: The date and time when the committer committed the code.
committer_tz: The timezone of the committer who committed the code.
in_main: A boolean indicating whether the commit was made on the main branch or not.
is_merge: A boolean indicating whether the commit is a merge commit or not.
num_deletes: The number of lines deleted in the commit.
num_inserts: The number of lines added in the commit.
net_lines: The net change in the number of lines (insertions - deletions) in the commit.
num_files: The number of files modified in the commit.
branches: A comma-separated list of branches the commit is found in.
files: A comma-separated list of files modified in the commit.
parents: A comma-separated list of parent commits.
dmm_unit_size: The delta maintainability model unit size for the commit.
dmm_unit_complexity: The delta maintainability model unit complexity for the commit.
dmm_unit_interfacing: The delta maintainability model unit interfacing for the commit.

These variables were calculated using PyDriller's Commit class, which provides access to various metadata about each commit, including author and committer information, file modifications, and various metrics such as the delta maintainability model. 