# python-log-parser

A modular Python application that parses raw system logs into structured records, validates input data, and stores processed information in a relational SQLite database.

Project Overview
This project demonstrates Python programming, regular expressions, data validation, SQL database management, memory-efficient file processing, and automated testing.

The application processes Apache-style server access logs line by line, extracts important information, validates records, and stores valid entries in SQLite.

Features
Log Parsing: Extracts IP addresses, timestamps, HTTP methods, endpoints, status codes, and request metadata.
Memory-Efficient Processing: Processes large log files line by line without loading the entire file into memory.
Data Validation: Validates IP addresses, timestamps, required fields, and HTTP status codes.
SQLite Integration: Stores structured log records in a relational database.
SQL Queries: Supports filtering by IP address and HTTP status code, retrieving records, and summarizing HTTP responses.
Error Handling: Skips malformed log entries while tracking invalid records.
Automated Testing: Uses pytest to test parsing, validation, and database functionality.
Technologies Used
Python 3
SQLite
SQL
Regular Expressions
Pytest
Git and GitHub
Installation
Clone the repository:


bash
git clone https://github.com/YOUR_USERNAME/python-log-parser.git
cd python-log-parser
Create a virtual environment:


bash
python -m venv venv
Activate it:

Windows:


bash
venv\Scripts\activate
Mac/Linux:


bash
source venv/bin/activate
Install dependencies:


bash
pip install -r requirements.txt
Running the Application
Run the parser using the sample log file:


bash
python main.py sample_logs/access.log
Specify a custom database:


bash
python main.py sample_logs/access.log --database logs.db
Running Tests
Execute the automated test suite:


bash
pytest -v
Database Structure
The SQLite database contains a logs table with the following fields:


Column	Description
id	Unique record identifier
ip_address	Client IP address
timestamp	Request timestamp
method	HTTP request method
endpoint	Requested resource
protocol	HTTP protocol
status_code	HTTP response status
response_size	Response size in bytes
referer	Referring URL
user_agent	Client browser information
event_details	Parsed event description
Example Output

text
Starting log processing...

Processing completed!
-------------------------
Valid records: 5
Invalid records: 1
Total processed: 6

HTTP Status Summary
-------------------------
Status 200: 2 requests
Status 401: 1 requests
Status 403: 1 requests
Status 404: 1 requests

Total database records: 5
Future Improvements
Add support for additional log formats.
Implement date-range filtering.
Add CSV and JSON export functionality.
Introduce structured logging for application errors.
Add performance benchmarks for large log files.
Author
Developed as a Python programming and data engineering project.
