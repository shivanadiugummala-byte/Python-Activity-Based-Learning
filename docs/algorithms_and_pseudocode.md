# Algorithms and Pseudocode

## 1. Employee Payroll
Read name, basic pay, overtime hours, and incentive. Calculate allowances and gross pay, apply the tax slab and deductions, and print net salary.

```text
gross = basic + 0.20*basic + 0.10*basic + overtimeHours*500 + incentive
IF gross <= 50000 THEN tax = 0
ELSE IF gross <= 100000 THEN tax = gross*0.05
ELSE IF gross <= 150000 THEN tax = gross*0.10
ELSE tax = gross*0.15
net = gross - tax - basic*0.12 - 2000
```

## 2. Retail Billing
Read products and accumulate amounts and category taxes. Apply a 5% or 10% discount, cap it at 2000, and calculate payable amount.

## 3. Attendance Recovery
Calculate current percentage. Increment extra attended classes until projected attendance reaches 75%.

## 4. Warehouse Inventory
Compare each physical quantity with system quantity. Report discrepancies above five units and reorder quantities below twenty.

## 5. Student Performance
Store names and marks in parallel structures. Calculate student averages and weak-subject counts.

## 6. Timetable Conflicts
Store `(course, start, end)` tuples. For each pair, test `startA < endB AND startB < endA`.

## 7. Transaction Detection
Store `(transactionId, amount, merchant)` tuples. Compare pairs and report matching amount and merchant.

## 8. Calendar Generator
Validate month and year, determine month length and starting weekday, and print a nested week-column grid.

## 9. Marks Matrix
Traverse a nested matrix row-wise for totals and averages and column-wise for subject averages.

## 10. Smart Canteen
Store menu rows as `[name, price, stock]`. Validate orders, update stock, apply the above-Rs.200 discount, and audit low stock.
