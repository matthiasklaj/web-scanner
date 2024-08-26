# Multi-Function Web Scanner

## Overview

Multi-Function Web Scanner is a Python-based tool designed to detect common web application vulnerabilities. This tool is intended for educational purposes and should only be used on websites for which you have explicit permission to test.

## Features

- **SQL Injection Detection**: Identifies SQL injection vulnerabilities using a set of common payloads.
- **XSS (Cross-Site Scripting) Detection**: Detects XSS vulnerabilities by injecting typical JavaScript payloads.
- **Directory Traversal Detection**: Finds directory traversal vulnerabilities by attempting to access sensitive files.

## Installation
**pip install requests **from command line , if not installed , install pip .
1. **Clone the Repository**:
   git clone https://github.com/matthiasklaj/web-scanner.git
   cd web-scanner
Run the Scanner:
example = python scanner.py

Follow the Prompts:

Enter the Target URL: Provide the base URL of the web application you want to test (e.g., http://example.com/index.php?param=).

Select Scan Type: Choose the type of scan you want to perform:

1 for SQL Injection

2 for XSS

3 for Directory Traversal

Review the Results: The tool will output the results of the scan to the console, indicating whether vulnerabilities were found and providing details.
