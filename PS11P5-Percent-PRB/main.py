# Define global variables
total = 0
tax = 0

def calculate_total_and_tax(quantity, unit_price):
    global total, tax  # Declare global variables

    # Compute Total
    total = quantity * unit_price

    # Compute Tax (7% of Total)
    tax = 0.07 * total

# Main function
if __name__ == "__main__":
    # Get input values from the user
    quantity = int(input("Enter the quantity of the item: "))
    unit_price = float(input("Enter the unit price of the item: "))

    # Call the function to calculate total and tax
    calculate_total_and_tax(quantity, unit_price)

    # Display the results using global variables
    print(f"Total: ${total:.2f}")
    print(f"Tax (7% of Total): ${tax:.2f}")
