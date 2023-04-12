This Python script extracts commit data from a Git repository using the PyDriller library and stores it in a CSV file. The CSV file contains information about each commit, including the commit ID, message, author and committer information, file modifications, and various metrics such as the number of lines deleted, inserted, and net lines, the number of files modified, and delta maintainability model statistics.

Requirements
Python 3.x
PyDriller library

You can install PyDriller using pip:
pip install pydriller

Usage
1. Clone the repository (optional): git clone --mirror https://github.com/<USERNAME>/<REPO_NAME>.git

3. Navigate to the project directory and open the Jupyter notebook: Collect_Commit_Data.ipynb 

4. Set the repository path and CSV file path and header in the code.

5. Run the script.


Output
The script will create a CSV file named reponame_commit_data.csv in the project directory. The CSV file will contain a header row that describes the fields that will be extracted for each commit. These fields include commit ID, message, author and committer information, file modifications, and various metrics such as the number of lines deleted, inserted, and net lines, the number of files modified, and delta maintainability model statistics.

Author
This script was written by Jesus Cantu.






