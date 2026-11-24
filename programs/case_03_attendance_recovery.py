total_held = int(input("Total classes held: "))
attended = int(input("Classes attended: "))
threshold = 75

current = attended * 100 / total_held
print(f"Current attendance: {current:.2f}%")

extra = 0
if current >= threshold:
    print("Eligibility status: ELIGIBLE")
else:
    while (attended + extra) * 100 / (total_held + extra) < threshold:
        extra += 1
    projected = (attended + extra) * 100 / (total_held + extra)
    print(f"Minimum consecutive classes required: {extra}")
    print(f"Projected attendance: {projected:.2f}%")
