name = input("Employee name: ").strip()
basic = float(input("Basic pay: "))
overtime_hours = float(input("Overtime hours: "))
incentive = float(input("Incentive: "))

hra = basic * 0.20
da = basic * 0.10
overtime_pay = overtime_hours * 500
gross = basic + hra + da + overtime_pay + incentive

if gross <= 50000:
    tax = 0
elif gross <= 100000:
    tax = gross * 0.05
elif gross <= 150000:
    tax = gross * 0.10
else:
    tax = gross * 0.15

pf = basic * 0.12
other_deductions = 2000
net = gross - tax - pf - other_deductions

print("\nEMPLOYEE PAYROLL STATEMENT")
print(f"Name: {name}")
print(f"Gross salary: Rs. {gross:.2f}")
print(f"Tax: Rs. {tax:.2f}")
print(f"PF: Rs. {pf:.2f}")
print(f"Other deductions: Rs. {other_deductions:.2f}")
print(f"Net salary: Rs. {net:.2f}")
