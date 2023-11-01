#Input Phase

def calculate_ticket_price(miles_from_downtown):
    if miles_from_downtown >= 30:
        ticket_price = 12
    elif 20 <= miles_from_downtown <= 29:
        ticket_price = 10
    elif 10 <= miles_from_downtown <= 19:
        ticket_price = 8
    else:
        ticket_price = 5

    return ticket_price

total_ticket_price = 0

# Process Phase

while True:
    response = input("Do you want to calculate the train ticket price? (Yes/No): ").strip().lower()
    if response != "yes":
        break

    last_name = input("Enter your last name: ")
    miles_from_downtown = int(input("Enter the number of miles from downtown Chicago: "))

    ticket_price = calculate_ticket_price(miles_from_downtown)
    total_ticket_price += ticket_price

#Output Phase 
  
    print(f"Hello, {last_name}! The ticket price for {miles_from_downtown} miles is: ${ticket_price}\n")

print(f"Total price of all tickets: ${total_ticket_price}")
