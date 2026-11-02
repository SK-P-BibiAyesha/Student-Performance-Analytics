
# Student Performance Analytics System

## Project Overview

The Student Performance Analytics System is a Python-based data analysis application that processes student academic records and generates meaningful performance insights.

It uses Python, NumPy, and Pandas to calculate student marks, averages, grades, pass/fail results, department performance, subject-wise statistics, and attendance risk.

## Objectives

- Analyze student academic performance.
- Calculate total and average marks.
- Assign grades based on average marks.
- Identify passed and failed students.
- Find top and low-performing students.
- Perform department-wise analysis.
- Analyze subject-wise performance.
- Identify students requiring academic support.
- Validate student data before processing.

## Technologies Used

- Python
- NumPy
- Pandas
- CSV

## Project Structure

```text
Student-Performance-Analytics/
│
├── data/
│   ├── students.csv
│   └── analyzed_students.csv
│
├── screenshots/
├── main.py
├── functions.py
├── test_validation.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate into the project:

```bash
cd Student-Performance-Analytics
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python main.py
```

## Run Validation Tests

```bash
python test_validation.py
```

## Key Features

1. Student dataset loading using Pandas.
2. Total and average marks calculation.
3. Grade assignment.
4. Pass/fail identification.
5. Highest and lowest performer identification.
6. Subject-wise performance analysis.
7. Department-wise performance analysis.
8. Grade distribution.
9. Attendance risk analysis.
10. Dataset validation.
11. Export analyzed results to CSV.

## Technologies and Concepts

- Python functions
- Loops and conditional statements
- NumPy numerical calculations
- Pandas DataFrames
- Data filtering and grouping
- CSV file handling
- Data validation

## Sample Results

- Total students: 20
- Passed students: 18
- Failed students: 2
- Pass percentage: 90%
- Overall class average: 73.46
- Highest performer: Jyothi
- Highest average: 96.50

## Output

The processed student information is saved in:

`data/analyzed_students.csv`

## Author

Student Performance Analytics – Python with AI Mini Project
