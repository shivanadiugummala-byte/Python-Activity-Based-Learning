product_count = int(input("Number of products: "))
subtotal = 0
total_tax = 0
items = []

for i in range(product_count):
    print(f"\nProduct {i + 1}")
    name = input("Name: ").strip()
    quantity = int(input("Quantity: "))
    price = float(input("Unit price: "))
    category = input("Category (grocery/electronics/luxury): ").strip().lower()
    line_amount = quantity * price
    subtotal += line_amount
    if category == "grocery":
        tax_rate = 0.05
    elif category == "electronics":
        tax_rate = 0.12
    else:
        tax_rate = 0.18
    tax = line_amount * tax_rate
    total_tax += tax
    items.append((name, quantity, price, line_amount, tax))

if subtotal > 10000:
    discount = subtotal * 0.10
elif subtotal > 5000:
    discount = subtotal * 0.05
else:
    discount = 0
discount = min(discount, 2000)
payable = subtotal - discount + total_tax

print("\nRETAIL INVOICE")
for name, quantity, price, line_amount, tax in items:
    print(f"{name:<15} {quantity:>3} x {price:>8.2f}  Amount={line_amount:>9.2f}  Tax={tax:>7.2f}")
print(f"Subtotal: Rs. {subtotal:.2f}")
print(f"Discount: Rs. {discount:.2f}")
print(f"Tax: Rs. {total_tax:.2f}")
print(f"Payable: Rs. {payable:.2f}")
