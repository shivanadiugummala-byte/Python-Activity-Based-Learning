course_count = int(input("Number of courses: "))
courses = []

for i in range(course_count):
    print(f"\nCourse {i + 1}")
    name = input("Course name: ").strip()
    start = float(input("Start time (24-hour, e.g. 9.5): "))
    end = float(input("End time (24-hour): "))
    courses.append((name, start, end))

print("\nTIMETABLE CONFLICTS")
conflict_count = 0
for i in range(course_count):
    for j in range(i + 1, course_count):
        name_a, start_a, end_a = courses[i]
        name_b, start_b, end_b = courses[j]
        if start_a < end_b and start_b < end_a:
            conflict_count += 1
            print(f"{name_a} overlaps {name_b}")
if conflict_count == 0:
    print("No conflicts found.")
