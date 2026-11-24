product_count = int(input("Number of products: "))
names = []
system_stock = []
physical_stock = []

for i in range(product_count):
    print(f"\nProduct {i + 1}")
    names.append(input("Name: ").strip())
    system_stock.append(int(input("System stock: ")))
    physical_stock.append(int(input("Physical stock: ")))

print("\nWAREHOUSE RECONCILIATION")
for i in range(product_count):
    difference = physical_stock[i] - system_stock[i]
    status = []
    if abs(difference) > 5:
        status.append("DISCREPANCY")
    if physical_stock[i] < 20:
        status.append("REORDER")
    print(f"{names[i]:<15} System={system_stock[i]:>3} Physical={physical_stock[i]:>3} "
          f"Difference={difference:>4}  {', '.join(status) if status else 'OK'}")
