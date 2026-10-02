# Python Log Analyzer

A Python automation tool that analyzes server log files, filters records by transaction ID, counts INFO/WARNING/ERROR messages, extracts error details, and generates a summary report automatically.

## Problem

Server log files can contain thousands of entries, making it difficult to manually find issues related to a specific transaction or request ID.

## Solution

This tool automates the process by:

- Searching logs using transaction ID
- Counting INFO messages
- Counting WARNING messages
- Counting ERROR messages
- Extracting error details
- Handling missing log files
- Handling transaction IDs with no matching records
- Generating a text report automatically

## Technologies Used

- Python
- File Handling
- Exception Handling
- String Processing
- Git
- GitHub

## Project Structure

```text
python-log-analyzer/
│
├── README.md
├── log_analyzer.py
├── sample.log
│
└── output/
    └── report_1001.txt

## 📸 Project Screenshot

Below is an example of the Log Analyzer successfully processing transaction ID `1001` and generating a report.

<img width="1556" height="919" alt="image" src="https://github.com/user-attachments/assets/c83f693f-08c2-4d15-9176-fe381eeeed03" />

<img width="1556" height="919" alt="image" src="https://github.com/user-attachments/assets/643c87b5-f06f-4c30-9dc9-61bcadf09f8a" />


