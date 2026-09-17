Item = "Clippers"
Price = 380
Quanity = 5

# Bill values
subtotal = Price * Quanity
tax = subtotal * 0.05
total = subtotal + tax

# 3 Bill Line

print(f"subtotal: ${subtotal: .2f}")
print(f"tax: ${tax: .2f}")
print(f"total: ${total: .2f}")
