Website Log Data Cleaning and Sessionization
Project Overview

This project focuses on cleaning raw website server log data and converting it into structured, sessionized user activity data. The objective is to parse unstructured Apache web logs, remove bot traffic, identify user sessions using a time-based rule, and prepare clean data for further analysis.

Technologies Used

Python

Pandas

Jupyter Notebook

MySQL (optional)

Dataset

Apache web server access logs (apache_logs.txt)

The dataset contains raw HTTP request logs including IP address, timestamp, URL, status code, referrer, and user-agent information.

Project Workflow
1. Data Ingestion

Imported raw Apache log file into Python using file handling.

Stored log lines in a Pandas DataFrame for processing.

2. Data Parsing & Standardization

Used regular expressions to extract:

IP address

Timestamp

Requested URL

User-Agent

Converted timestamps into standard datetime format for time-based analysis.

3. Bot and Crawler Removal

Identified bot traffic using common user-agent keywords such as:

bot, crawler, spider, feed, archive

Removed automated traffic to retain genuine user behavior.

4. Sessionization Logic

Grouped requests by IP address.

Sorted logs by timestamp.

Created a new session when the time gap between consecutive requests exceeded 30 minutes.

Assigned unique session IDs for each user session.

5. Data Output

Generated a clean, sessionized dataset.

Exported the final table as a CSV file.

Optionally stored the data in a MySQL database for further querying.

Sessionization Rule

A session is defined as a sequence of user requests with no more than 30 minutes of inactivity.

If the inactivity exceeds 30 minutes, a new session is created.

Deliverables

cleaned_sessionized_logs.csv – Cleaned and sessionized log data

Jupyter Notebook containing code and explanations

This README documentation

Final Outcome

The project converts unstructured web server logs into structured, analysis-ready session data. This enables understanding user behavior, session duration, and navigation patterns, which are essential for web analytics and business decision-making.

Author

Abhishek Shukla
BCA – Big Data Analytics