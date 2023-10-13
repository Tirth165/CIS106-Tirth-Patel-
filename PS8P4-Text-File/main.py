# InputPhase
total_extended_price = 0
order_count = 0

# ProcessPhase 
with open('orders.txt', 'r') as file:
    # Iterate through each line in the file
    for line in file:
        # Split the line into item, quantity, and price
        item, quantity, price = line.strip().split(', ')

        # Convert quantity and price to float
        quantity = int(quantity)
        price = float(price)

        # Calculate the extended price
        extended_price = quantity * price

        # Display item, quantity, price, and extended price
        print(f"Item: {item}, Quantity: {quantity}, Price: {price}, Extended Price: {extended_price}")

        # Add the extended price to the total
        total_extended_price += extended_price

        # Increment the order count
        order_count += 1


average_order = total_extended_price / order_count if order_count > 0 else 0

# Output Phase 
print(f"Sum of Extended Prices: {total_extended_price}")
print(f"Number of Orders: {order_count}")
print(f"Average Order: {average_order}")
