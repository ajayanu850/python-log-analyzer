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
