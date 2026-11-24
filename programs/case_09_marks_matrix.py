student_count = int(input("Number of students: "))
subject_count = int(input("Number of subjects: "))
names = []
matrix = []

for i in range(student_count):
    names.append(input(f"\nStudent {i + 1} name: ").strip())
    row = []
    for j in range(subject_count):
        row.append(float(input(f"Subject {j + 1} mark: ")))
    matrix.append(row)

print("\nSTUDENT MARKS MATRIX")
top_name = names[0]
top_average = -1
for i in range(student_count):
    total = sum(matrix[i])
    average = total / subject_count
    if average > top_average:
        top_average = average
        top_name = names[i]
    print(f"{names[i]:<15} Total={total:>7.2f} Average={average:>6.2f}")

print("\nSUBJECT-WISE AVERAGES")
best_subject = 1
best_average = -1
for j in range(subject_count):
    subject_total = 0
    for i in range(student_count):
        subject_total += matrix[i][j]
    average = subject_total / student_count
    print(f"Subject {j + 1}: {average:.2f}")
    if average > best_average:
        best_average = average
        best_subject = j + 1

print(f"Top student: {top_name}")
print(f"Best subject: Subject {best_subject}")
