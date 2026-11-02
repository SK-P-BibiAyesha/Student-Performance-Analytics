
# PROJECT DOCUMENTATION

# Student Performance Analytics System

## 1. Project Title

Student Performance Analytics System

## 2. Objective

The objective of this project is to develop a Python-based application that analyzes student academic records and generates meaningful insights.

The system helps identify student performance, calculate grades, analyze attendance, and determine students who may require academic support.

## 3. Technologies Used

- Python
- NumPy
- Pandas
- CSV files
- Visual Studio Code

## 4. Dataset Description

The project uses a CSV dataset containing 20 student records.

Dataset columns:

- Student_ID
- Name
- Department
- Python
- Mathematics
- DBMS
- Computer_Networks
- Attendance

Each subject has a maximum of 100 marks.

## 5. Implementation

### Step 1: Dataset Loading

Used Pandas read_csv() to load student records into a DataFrame.

### Step 2: Data Processing

Calculated total marks and average marks using Pandas and NumPy.

### Step 3: Grade Assignment

Assigned grades based on student average marks.

### Step 4: Pass/Fail Analysis

Identified students who scored at least 40 marks in every subject.

### Step 5: Performance Analysis

Calculated subject-wise and department-wise averages.

### Step 6: Attendance Analysis

Identified students with low attendance.

### Step 7: Data Validation

Checked missing values, duplicate IDs, invalid marks, and attendance values.

### Step 8: Exporting Results

Saved processed student information into analyzed_students.csv.

## 6. Key Features

- Total and average marks calculation.
- Grade assignment.
- Pass/fail statistics.
- Top three performers.
- Highest and lowest performers.
- Department-wise analysis.
- Subject-wise analysis.
- Grade distribution.
- Attendance risk identification.
- Data validation.

## 7. Results

Total Students: 20

Passed Students: 18

Failed Students: 2

Pass Percentage: 90%

Overall Class Average: 73.46

Highest Performer: Jyothi

Highest Average: 96.50

Lowest Performer: Rahul

Lowest Average: 35.75

Best Performing Subject: Computer Networks

Lowest Performing Subject: Python

## 8. Testing

The project was tested using valid and invalid datasets.

Validation tests included:

- Valid dataset.
- Duplicate student ID.
- Marks greater than 100.
- Missing student name.
- Invalid attendance.

All five validation tests passed.

## 9. Challenges and Learning

During this project, I learned how to:

- Read CSV files using Pandas.
- Perform numerical calculations using NumPy.
- Create reusable Python functions.
- Apply loops and conditional statements.
- Group and analyze student records.
- Validate datasets.
- Generate meaningful analytical results.

## 10. Final Outcome

The Student Performance Analytics System successfully processes student academic records and produces useful academic insights.

The project demonstrates the practical application of Python fundamentals, NumPy, Pandas, and data analysis techniques.

## 11. GitHub Repository

Add the GitHub repository URL here.
[https://github.com/SK-P-BibiAyesha/Student-Performance-Analytics.git]