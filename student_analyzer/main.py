marks = [85, 90, 72, 96, 78]

total = sum(marks)
average = total / len(marks)

print("Total marks:", total)
print("Average marks:", average)
print("Highest mark:", max(marks))

print("Lowest mark:",min(marks))
print("Number of students:",len(marks))

grades={'A':0,'B':0,'C':0,'D':0}

for mark in marks:

    if mark >= 90:
        grade = "A"
        grades[grade] += 1

    elif mark >= 80:
        grade = "B"
        grades[grade] += 1
    elif mark >= 70:
        grade = "C"
        grades[grade] += 1
    else:
        grade = "D"
        grades[grade] += 1

    print(mark, "-> Grade:", grade)
print("Student analysis completed.")  

for grade, count in grades.items():
    print(f"{grade}:{count} students")