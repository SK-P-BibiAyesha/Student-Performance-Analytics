
import pandas as pd

from functions import validate_dataset


# Load original dataset
students = pd.read_csv("data/students.csv")

# Test 1: Valid dataset
print("\nTEST 1: Valid Dataset")

print(validate_dataset(students.copy()))


# Test 2: Duplicate student ID
print("\nTEST 2: Duplicate Student ID")

duplicate_data = students.copy()
duplicate_data.loc[1, "Student_ID"] = 101

try:
    validate_dataset(duplicate_data)
except ValueError as error:
    print("Successfully detected:", error)


# Test 3: Invalid marks
print("\nTEST 3: Marks Greater Than 100")

invalid_marks = students.copy()
invalid_marks.loc[0, "Python"] = 150

try:
    validate_dataset(invalid_marks)
except ValueError as error:
    print("Successfully detected:", error)


# Test 4: Missing student name
print("\nTEST 4: Missing Student Name")

missing_name = students.copy()
missing_name.loc[0, "Name"] = None

try:
    validate_dataset(missing_name)
except ValueError as error:
    print("Successfully detected:", error)


# Test 5: Invalid attendance
print("\nTEST 5: Invalid Attendance")

invalid_attendance = students.copy()
invalid_attendance.loc[0, "Attendance"] = 120

try:
    validate_dataset(invalid_attendance)
except ValueError as error:
    print("Successfully detected:", error)


print("\nAll validation tests completed!")
