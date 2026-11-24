student_count = int(input("Number of students: "))
subject_count = int(input("Number of subjects: "))
students = []

for i in range(student_count):
    name = input(f"\nStudent {i + 1} name: ").strip()
    marks = []
    for j in range(subject_count):
        marks.append(float(input(f"Subject {j + 1} marks: ")))
    students.append((name, marks))

print("\nSTUDENT PERFORMANCE")
for name, marks in students:
    average = sum(marks) / subject_count
    if average >= 80:
        grade = "Excellent"
    elif average >= 60:
        grade = "Good"
    elif average >= 40:
        grade = "Average"
    else:
        grade = "Poor"
    consistently_weak = 0
    for mark in marks:
        if mark < 40:
            consistently_weak += 1
    print(f"{name:<15} Average={average:>6.2f}  {grade:<9}  Weak subjects={consistently_weak}")
