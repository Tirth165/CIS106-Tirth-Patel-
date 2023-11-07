def calculate_discount(quantity, price, discount_rate):
  # Compute Discount Amount
  discount_amount = quantity * price * discount_rate

  # Compute Discounted Price
  discounted_price = price - discount_amount

  # Return both discount amount and discounted price
  return discount_amount, discounted_price

# Main function
if __name__ == "__main__":
  # Get input values from the user
  quantity = int(input("Enter the quantity: "))
  price = float(input("Enter the price: "))
  discount_rate = float(input("Enter the discount rate (in decimal): "))

  # Call the function to calculate discount amount and discounted price
  discount_amount, discounted_price = calculate_discount(quantity, price, discount_rate)

  # Display the results
  print(f"Quantity: {quantity}")
  print(f"Price: ${price:.2f}")
  print(f"Discount Amount: ${discount_amount:.2f}")
  print(f"Discounted Price: ${discounted_price:.2f}")
