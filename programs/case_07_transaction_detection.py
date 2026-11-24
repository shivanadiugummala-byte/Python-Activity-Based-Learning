count = int(input("Number of transactions: "))
transactions = []

for i in range(count):
    print(f"\nTransaction {i + 1}")
    tx_id = input("Transaction ID: ").strip()
    amount = float(input("Amount: "))
    merchant = input("Merchant: ").strip().lower()
    transactions.append((tx_id, amount, merchant))

print("\nSUSPICIOUS TRANSACTION REPORT")
suspicious = []
for i in range(count):
    tx_id_a, amount_a, merchant_a = transactions[i]
    for j in range(i + 1, count):
        tx_id_b, amount_b, merchant_b = transactions[j]
        if amount_a == amount_b and merchant_a == merchant_b:
            entry = (tx_id_a, tx_id_b, amount_a, merchant_a)
            suspicious.append(entry)

if not suspicious:
    print("No duplicate transactions found.")
else:
    for tx_id_a, tx_id_b, amount, merchant in suspicious:
        print(f"{tx_id_a} and {tx_id_b}: duplicate Rs. {amount:.2f} at {merchant}")
