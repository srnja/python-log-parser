Python Log Parser & Data Validation

A Python application that parses Apache-style server logs, validates records, and stores structured data in a SQLite database.

Features
Parses raw server logs using regular expressions.
Validates IP addresses, timestamps, and HTTP status codes.
Stores processed records in SQLite.
Supports SQL queries and HTTP status summaries.
Handles malformed log entries.
Includes automated tests using pytest.
Technologies
Python
SQLite
SQL
Regular Expressions
Pytest
How to Run
Clone the repository.
Install dependencies:

pip install -r requirements.txt

Run the application:

python main.py sample_logs/access.log

Run Tests

pytest -v

Project Purpose

Built to demonstrate Python programming, data validation, database management, file processing, and software testing.
