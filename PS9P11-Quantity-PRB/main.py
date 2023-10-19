#InputPhase

def calculateextendedprice(quantity, price):
  total = quantity * price
  if total > 10000:
      total *= 0.9  # Apply a 10% discount if the total is over $10,000
  return total

extendedpricesum = 0.0

# ProcessPhase
while True:
  try:
      quantity = int(input("Enter the quantity (or press Ctrl+Z to stop): "))
      price = float(input("Enter the price: $"))

      total = calculateextendedprice(quantity, price)

      print(f"Quantity: {quantity}")
      print(f"Price: ${price:.2f}")
      print(f"Total: ${total:.2f}\n")

      extendedpricesum += total
  except (ValueError, ZeroDivisionError):
      print("Invalid input. Please enter valid quantity and price.")

# Output Phase 
print(f"Total Extended Price: ${extended_price_sum:.2f}")
