# python-log-parser

A modular Python application that parses raw system logs into structured records, validates input data, and stores processed information in a relational SQLite database.

Project Overview
This project demonstrates Python programming, regular expressions, data validation, SQL database management, memory-efficient file processing, and automated testing.

The application processes Apache-style server access logs line by line, extracts important information, validates records, and stores valid entries in SQLite.

Features:

Log Parsing: Extracts IP addresses, timestamps, HTTP methods, endpoints, status codes, and request metadata.

Memory-Efficient Processing: Processes large log files line by line without loading the entire file into memory.

Data Validation: Validates IP addresses, timestamps, required fields, and HTTP status codes.

SQLite Integration: Stores structured log records in a relational database.

SQL Queries: Supports filtering by IP address and HTTP status code, retrieving records, and summarizing HTTP responses.

Error Handling: Skips malformed log entries while tracking invalid records.

Automated Testing: Uses pytest to test parsing, validation, and database functionality.

Technologies Used:

Python 3

SQLite

SQL

Regular Expressions

Pytest

Git and GitHub

