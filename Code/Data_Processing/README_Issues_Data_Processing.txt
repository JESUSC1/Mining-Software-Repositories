File: Issues_Data_Processing.py
This Python script processes CSV files containing issue data, adding columns with information about when the issue was created and closed.

Requirements
The script requires Python 3 and the Pandas library.

Usage
Set the input and output paths in the script. By default, the input path is /Users/jesuscantu/Desktop/Workspace/MiningSoftwareRepositories/Raw_Data/Issues and the output path is /Users/jesuscantu/Desktop/Workspace/MiningSoftwareRepositories/Generated_Data/Issues.
Save the script and run it in a Python environment.
The script will look for new CSV files in the input path, process them, and save the output CSV files in the output path. The script will skip files that have already been processed.
Output
The script adds the following columns to the CSV files:

day_created: day of the month when the issue was created
week_created: week of the year when the issue was created
month_created: month of the year when the issue was created
year_created: year when the issue was created
time_created: time of day when the issue was created
hour_created: hour of the day when the issue was created
day_closed: day of the month when the issue was closed
week_closed: week of the year when the issue was closed
month_closed: month of the year when the issue was closed
year_closed: year when the issue was closed
time_closed: time of day when the issue was closed
hour_closed: hour of the day when the issue was closed
The output CSV files are saved in the output path with the suffix _processed.csv.

Author
This script was created by Jesus Cantu. Feel free to contact me with any questions or feedback.