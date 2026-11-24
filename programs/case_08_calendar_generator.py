month = int(input("Month number (1-12): "))
year = int(input("Year: "))
month_names = ["", "January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

if month < 1 or month > 12:
    print("Invalid month")
else:
    if month == 2:
        leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
        days = 29 if leap else 28
    elif month in (4, 6, 9, 11):
        days = 30
    else:
        days = 31

    offset = year - (1 if month < 3 else 0)
    weekday = (offset + offset // 4 - offset // 100 + offset // 400 +
                (14 if month < 3 else 0) + month) % 7
    # Convert formula result to Monday-first layout.
    month_starts = (weekday - 1) % 7

    print(f"\n{month_names[month]} {year}")
    print("Mo Tu We Th Fr Sa Su")
    print("   " * month_starts, end="")
    current = 1
    while current <= days:
        column = (month_starts + current - 1) % 7
        print(f"{current:2}", end=" ")
        if column == 6:
            print()
        current += 1
    print()
