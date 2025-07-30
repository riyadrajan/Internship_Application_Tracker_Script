# Co-Op Job Application Tracker (Python Script)

This is my first Python script, built to automate the tracking of job applications during my Co-Op term search.

## Summary

This script reads a directory structure where job applications are organized by company and job ID, then generates a continuously updated Excel tracker. It ensures previously recorded applications are preserved and new entries are appended without duplication.

## Features

- Reads a base folder (`Co-Op`) that stores job applications in a structured format:
  - First-level subfolders represent **companies**
  - Each company contains subfolders named by **job ID**
- Extracts:
  - `Company Name` from the folder name
  - `Application` (Job ID) from subfolder names
- Uses `pandas` to generate a DataFrame
- Writes the DataFrame to an Excel file (`.xlsx`)
- Appends new applications without overwriting existing entries
- Scheduled daily execution using `cron`

## Folder Structure Example

Co-Op/  
├── Ciena/  
│ ├── 2025-0001/  
│ └── 2025-0002/  
├── IBM/  
│ └── 2025-0021/  


Each `Company/Job ID` pair becomes a unique entry in the Excel tracker.

## Technologies Used

- Python 3
- pandas
- cron (macOS/Linux job scheduler)

## Automation (Cron)

The script is set to run daily at 9:00 AM using `cron`. Example cron entry:  
`0 9 * * * /usr/bin/python3 /Users/riyadrajan/Desktop/coopScript.py`
