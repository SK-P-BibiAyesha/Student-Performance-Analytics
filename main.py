
import pandas as pd

from functions import (
    generate_performance,
    highest_performer,
    lowest_performer,
    subject_analysis,
    attendance_analysis,
    top_performers
)

from functions import (
    generate_performance,
    highest_performer,
    lowest_performer,
    subject_analysis,
    attendance_analysis,
    top_performers,
    department_analysis,
    grade_distribution,
    subject_performance,
    academic_support,
    attendance_risk
)

from functions import validate_dataset

# 1. Load dataset
students = pd.read_csv("data/students.csv")

print("\n==========================================")
print("       STUDENT PERFORMANCE ANALYTICS")
print("==========================================")

# 2. Generate student performance
students = generate_performance(students)


# 3. Display complete student results
print("\n========== STUDENT PERFORMANCE ==========")

print(
    students[
        [
            "Student_ID",
            "Name",
            "Total_Marks",
            "Average_Marks",
            "Grade",
            "Result"
        ]
    ].to_string(index=False)
)


# 4. Pass and fail statistics
print("\n========== PASS / FAIL ANALYSIS ==========")

passed = (students["Result"] == "Pass").sum()
failed = (students["Result"] == "Fail").sum()

total_students = len(students)

print("Total Students:", total_students)
print("Passed Students:", passed)
print("Failed Students:", failed)

pass_percentage = (passed / total_students) * 100

print(f"Pass Percentage: {pass_percentage:.2f}%")


# 5. Overall class average
class_average = students["Average_Marks"].mean()

print(f"\nOverall Class Average: {class_average:.2f}")


# 6. Highest performer
highest = highest_performer(students)

print("\n========== HIGHEST PERFORMER ==========")

print("Name:", highest["Name"])
print("Average:", highest["Average_Marks"])
print("Grade:", highest["Grade"])


# 7. Lowest performer
lowest = lowest_performer(students)

print("\n========== LOWEST PERFORMER ==========")

print("Name:", lowest["Name"])
print("Average:", lowest["Average_Marks"])
print("Grade:", lowest["Grade"])


# 8. Subject-wise analysis
subject_analysis(students)


# 9. Attendance analysis
attendance_analysis(students)


# 10. Top three performers
top_performers(students)


# 12. Department-wise analysis
department_analysis(students)

# 13. Grade distribution
grade_distribution(students)

# 14. Subject performance
subject_performance(students)

# 15. Academic support identification
academic_support(students)

# 16. Attendance risk
attendance_risk(students)



# 11. Save analyzed data
students.to_csv(
    "data/analyzed_students.csv",
    index=False
)

print("\n==========================================")
print("Analysis completed successfully!")
print("Results saved to data/analyzed_students.csv")
print("==========================================")


students = pd.read_csv("data/students.csv")

# Validate dataset before analysis
validate_dataset(students)