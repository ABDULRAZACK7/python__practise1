marks = [85, 90, 72, 96, 78]

total = sum(marks)
average = total / len(marks)

print("Total marks:", total)
print("Average marks:", average)
print("Highest mark:", max(marks))

print("Lowest mark:",min(marks))
print("Number of students:",len(marks))

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