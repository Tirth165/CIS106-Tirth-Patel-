def calculate_commission_and_target(last_name, sales):
  # Compute Commission
  if sales > 100000:
      commission = 0.10 * sales
  else:
      commission = 0.05 * sales

  # Compute Next Year's Target
  target = 0.05 * sales

  # Return both commission and next year's target
  return commission, target

# Main function
if __name__ == "__main__":
  # Get input values from the user
  last_name = input("Enter the salesperson's last name: ")
  sales = float(input("Enter the sales amount: "))

  # Call the function to calculate commission and next year's target
  commission, target = calculate_commission_and_target(last_name, sales)

  # Display the results
  print(f"Salesperson's Last Name: {last_name}")
  print(f"Commission: ${commission:.2f}")
  print(f"Next Year's Target: ${target:.2f}")
