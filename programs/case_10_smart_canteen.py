menu = [
    ["Rice Meal", 60, 20],
    ["Dosa", 30, 15],
    ["Tea", 15, 30],
    ["Water", 10, 50]
]

print("SMART CANTEEN")
for i in range(len(menu)):
    name, price, stock = menu[i]
    print(f"{i + 1}. {name:<12} Rs.{price:<4} Stock={stock}")

order_count = int(input("Number of menu items to order: "))
subtotal = 0
print("\nORDER BILL")

for i in range(order_count):
    item_index = int(input("Menu item number: ")) - 1
    quantity = int(input("Quantity: "))
    if item_index < 0 or item_index >= len(menu):
        print("Invalid menu item.")
        continue
    name, price, stock = menu[item_index]
    if quantity <= 0:
        print("Invalid quantity.")
    elif quantity > stock:
        print(f"Only {stock} {name} available.")
    else:
        amount = quantity * price
        subtotal += amount
        menu[item_index][2] -= quantity
        print(f"{name:<12} {quantity:>3} x {price:>4} = Rs. {amount:.2f}")

discount = subtotal * 0.10 if subtotal > 200 else 0
payable = subtotal - discount
print(f"Subtotal: Rs. {subtotal:.2f}")
print(f"Bulk discount: Rs. {discount:.2f}")
print(f"Payable: Rs. {payable:.2f}")

print("\nLOW-STOCK AUDIT")
low_stock_found = False
for name, price, stock in menu:
    if stock < 5:
        low_stock_found = True
        print(f"{name}: {stock}")
if not low_stock_found:
    print("No low-stock items.")
