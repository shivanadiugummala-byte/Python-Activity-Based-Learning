# Test Cases

| Case | Test | Expected Result |
|---|---|---|
| Employee Payroll | Basic 75000, overtime 10, incentive 5000 | Gross 107500, tax 10750, net 85750 |
| Retail Billing | 7600 subtotal | Discount 380, payable 8313 |
| Retail Billing | Subtotal above 10000 | 10% discount capped at 2000 |
| Attendance Recovery | 60 held, 38 attended | 28 classes; projected 75.00% |
| Attendance Recovery | 32/40 attended | Eligible with no extra classes |
| Warehouse Inventory | Difference 6 units | Discrepancy |
| Warehouse Inventory | Physical stock 19 | Reorder |
| Student Performance | Marks 80, 85, 90 | Excellent |
| Timetable | 9-11 and 10-12 | Conflict |
| Timetable | 9-10 and 10-11 | No conflict |
| Transactions | Same amount and merchant | Suspicious pair |
| Calendar | July 2025 | 31 days; July 1 on Tuesday |
| Calendar | February 2024 | 29 days |
| Marks Matrix | 4x4 marks | Correct row and column averages |
| Canteen | Quantity above stock | Order rejected |
