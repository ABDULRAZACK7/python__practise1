
def analyze_marks(marks):
    total = sum(marks)
    average = total / len(marks)

    grades = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

    for mark in marks:
        if mark >= 90:
            grade = "A"
        elif mark >= 80:
            grade = "B"
        elif mark >= 70:
            grade = "C"
        else:
            grade = "D"

        grades[grade] += 1

    return {
        "total": total,
        "average": average,
        "highest": max(marks),
        "lowest": min(marks),
        "count": len(marks),
        "grades": grades
    }


if __name__ == "__main__":
    marks = [85, 90, 72, 96, 78]
    result = analyze_marks(marks)

    print("Total marks:", result["total"])
    print("Average marks:", result["average"])
    print("Highest mark:", result["highest"])
    print("Lowest mark:", result["lowest"])
    print("Number of students:", result["count"])

    for mark in marks:
        if mark >= 90:
            grade = "A"
        elif mark >= 80:
            grade = "B"
        elif mark >= 70:
            grade = "C"
        else:
            grade = "D"
        print(mark, "-> Grade:", grade)

    print("Student analysis completed.")

    for grade, count in result["grades"].items():
        print(f"{grade}:{count} students")
