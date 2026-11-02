
import pandas as pd
import numpy as np

# Subjects included in the analysis
SUBJECTS = [
    "Python",
    "Mathematics",
    "DBMS",
    "Computer_Networks"
]


# 1. Calculate total marks
def calculate_total(data):
    data["Total_Marks"] = data[SUBJECTS].sum(axis=1)
    return data


# 2. Calculate average marks using NumPy
def calculate_average(data):
    marks = data[SUBJECTS].to_numpy()
    data["Average_Marks"] = np.mean(marks, axis=1)
    return data


# 3. Assign grades based on average marks
def assign_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# 4. Identify pass or fail
def check_result(row):
    for subject in SUBJECTS:
        if row[subject] < 40:
            return "Fail"

    return "Pass"


# 5. Generate student performance
def generate_performance(data):

    data = calculate_total(data)
    data = calculate_average(data)

    data["Grade"] = data["Average_Marks"].apply(assign_grade)

    data["Result"] = data.apply(check_result, axis=1)

    return data


# 6. Find highest performer
def highest_performer(data):
    index = data["Average_Marks"].idxmax()
    return data.loc[index]


# 7. Find lowest performer
def lowest_performer(data):
    index = data["Average_Marks"].idxmin()
    return data.loc[index]


# 8. Calculate subject-wise averages
def subject_analysis(data):

    print("\n========== SUBJECT-WISE ANALYSIS ==========")

    for subject in SUBJECTS:
        average = data[subject].mean()

        print(f"{subject}: {average:.2f}")


# 9. Attendance analysis
def attendance_analysis(data):

    print("\n========== ATTENDANCE ANALYSIS ==========")

    average_attendance = np.mean(data["Attendance"])

    low_attendance = data[data["Attendance"] < 75]

    print(f"Average Attendance: {average_attendance:.2f}%")

    print("Students below 75% attendance:")

    if low_attendance.empty:
        print("No students")
    else:
        print(
            low_attendance[["Student_ID", "Name", "Attendance"]]
            .to_string(index=False)
        )


# 10. Display top performers
def top_performers(data, count=3):

    print("\n========== TOP PERFORMERS ==========")

    top_students = data.sort_values(
        by="Average_Marks",
        ascending=False
    ).head(count)

    print(
        top_students[
            ["Student_ID", "Name", "Average_Marks", "Grade"]
        ].to_string(index=False)
    )



# 11. Department-wise performance analysis
def department_analysis(data):

    print("\n========== DEPARTMENT-WISE ANALYSIS ==========")

    result = data.groupby("Department").agg(
        Total_Students=("Student_ID", "count"),
        Average_Marks=("Average_Marks", "mean"),
        Average_Attendance=("Attendance", "mean")
    )

    print(result.round(2))


# 12. Grade distribution
def grade_distribution(data):

    print("\n========== GRADE DISTRIBUTION ==========")

    grades = data["Grade"].value_counts().sort_index()

    for grade, count in grades.items():
        print(f"Grade {grade}: {count} students")


# 13. Highest and lowest performing subjects
def subject_performance(data):

    print("\n========== SUBJECT PERFORMANCE ==========")

    averages = data[SUBJECTS].mean()

    highest_subject = averages.idxmax()
    lowest_subject = averages.idxmin()

    print("\nSubject Averages:")
    print(averages.round(2))

    print(
        f"\nBest Performing Subject: {highest_subject} "
        f"({averages[highest_subject]:.2f})"
    )

    print(
        f"Lowest Performing Subject: {lowest_subject} "
        f"({averages[lowest_subject]:.2f})"
    )


# 14. Identify students needing academic support
def academic_support(data):

    print("\n========== STUDENTS NEEDING SUPPORT ==========")

    support_students = data[
        (data["Average_Marks"] < 50) |
        (data["Result"] == "Fail")
    ]

    if support_students.empty:
        print("No students currently require academic support.")
    else:
        print(
            support_students[
                ["Student_ID", "Name", "Average_Marks", "Grade", "Result"]
            ].to_string(index=False)
        )


# 15. Attendance risk analysis
def attendance_risk(data):

    print("\n========== ATTENDANCE RISK ANALYSIS ==========")

    high_risk = data[data["Attendance"] < 75]

    moderate_risk = data[
        (data["Attendance"] >= 75) &
        (data["Attendance"] < 85)
    ]

    print("High Attendance Risk:", len(high_risk))
    print("Moderate Attendance Risk:", len(moderate_risk))
    print("Good Attendance:", len(data[data["Attendance"] >= 85]))



# 17. Validate student dataset
def validate_dataset(data):

    print("\n========== DATA VALIDATION ==========")

    required_columns = [
        "Student_ID",
        "Name",
        "Department",
        "Python",
        "Mathematics",
        "DBMS",
        "Computer_Networks",
        "Attendance"
    ]

    # Check required columns
    missing_columns = [
        column for column in required_columns
        if column not in data.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    if data.empty:
        raise ValueError("Dataset is empty.")

    # Check missing values
    if data[required_columns].isnull().any().any():
        raise ValueError(
            "Dataset contains missing values."
        )

    # Check duplicate student IDs
    if data["Student_ID"].duplicated().any():
        raise ValueError(
            "Duplicate Student IDs found."
        )

    # Check empty names and departments
    for column in ["Name", "Department"]:
        if data[column].astype(str).str.strip().eq("").any():
            raise ValueError(
                f"Empty values found in {column}."
            )

    # Validate numerical columns
    numeric_columns = [
        "Student_ID",
        "Python",
        "Mathematics",
        "DBMS",
        "Computer_Networks",
        "Attendance"
    ]

    for column in numeric_columns:
        data[column] = pd.to_numeric(
            data[column],
            errors="coerce"
        )

    if data[numeric_columns].isnull().any().any():
        raise ValueError(
            "Invalid numerical values found."
        )

    # Validate marks
    for subject in SUBJECTS:
        if not data[subject].between(0, 100).all():
            raise ValueError(
                f"Invalid marks found in {subject}."
            )

    # Validate attendance
    if not data["Attendance"].between(0, 100).all():
        raise ValueError(
            "Attendance must be between 0 and 100."
        )

    print("All validation checks passed!")

    return True
