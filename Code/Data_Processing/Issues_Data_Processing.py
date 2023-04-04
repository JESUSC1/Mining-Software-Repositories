"""
This code reads CSV files from an input directory, processes them by creating new columns based on datetime information, and writes the resulting dataframes to CSV files in an output directory. The code checks the output directory to only process new files that have not already been processed.
"""
# Import required libraries 
import os
import pandas as pd

# File Path
file_path = "file_path" # ~/MiningSoftwareRepositories/Raw_Data/Issues

# Get list of files in directory containing data for a GitHub Repository's Issues 
print("Files in directory containing data for a GitHub Repository's Issues:")
for files in os.listdir(file_path):
    if files.endswith(".csv"):
        # Prints only text file present in My Folder
        print(files)

# Set input and output paths
input_path = 'file_path' # ~/MiningSoftwareRepositories/Raw_Data/Issues
output_path = 'file_path' # ~/MiningSoftwareRepositories/Generated_Data/Issues

# Get list of CSV files in input directory
input_files = [f for f in os.listdir(input_path) if f.endswith('.csv')]

# Get list of CSV files already processed in output directory
output_files = [f for f in os.listdir(output_path) if f.endswith('_processed.csv')]

# Filter input files to only include new CSV files
new_files = [f for f in input_files if f not in [out_file[:-13] + ".csv" for out_file in output_files]]

# Loop through new CSV files and process them
for filename in new_files:
    print(f"Processing {filename}...")
    
    # Check if the file has already been processed
    if filename[:-4] + "_processed.csv" in output_files:
        print(f"File {filename} has already been processed.")
        continue
    
    # Read CSV file into DataFrame
    issues_df = pd.read_csv(os.path.join(input_path, filename))
    
    # Convert 'Created At' column to datetime format
    issues_df['created_at'] = pd.to_datetime(issues_df['created_at'])

    # Create columns from 'Created At' for day, week, month, year, time, and hour
    issues_df['day_created'] = issues_df['created_at'].dt.day
    issues_df['week_created'] = issues_df['created_at'].dt.isocalendar().week
    issues_df['month_created'] = issues_df['created_at'].dt.month
    issues_df['year_created'] = issues_df['created_at'].dt.year
    issues_df['time_created'] = issues_df['created_at'].dt.time
    issues_df['hour_created'] = issues_df['created_at'].dt.hour

    # Convert 'Closed At' column to datetime format
    issues_df['closed_at'] = pd.to_datetime(issues_df['closed_at'])

    # Create columns from 'Closed At' for day, week, month, year, time, and hour
    issues_df['day_closed'] = issues_df['closed_at'].dt.day
    issues_df['week_closed'] = issues_df['closed_at'].dt.isocalendar().week
    issues_df['month_closed'] = issues_df['closed_at'].dt.month
    issues_df['year_closed'] = issues_df['closed_at'].dt.year
    issues_df['time_closed'] = issues_df['closed_at'].dt.time
    issues_df['hour_closed'] = issues_df['closed_at'].dt.hour

    # Note that the Week column uses the isocalendar() method to get the week number,
    # since the standard week method can return inconsistent results depending on the specific calendar used.
    
    # Write DataFrame to new CSV file in output directory
    output_filename = f"{filename.split('.')[0]}_issues_processed.csv"
    issues_df.to_csv(os.path.join(output_path, output_filename), index=False)
    
    print(f"Finished processing {filename}. Output saved to {output_filename}.")
