def calculate_out_the_door_price(msrp, make, model, electric_vehicle_code):
  percent_off_msrp = 0.05  # Default percent off MSRP for other vehicles

  if make == "Honda" and model == "Accord":
      percent_off_msrp = 0.10
  elif make == "Toyota" and model == "Rav4":
      percent_off_msrp = 0.15
  elif electric_vehicle_code == "Y":
      percent_off_msrp = 0.30

  discount = msrp * percent_off_msrp
  new_msrp = msrp - discount
  total = new_msrp * 1.07  # Adding 7% sales tax

  return total

total_msrp = 0
total_sales_price = 0

while True:
  response = input("Do you want to calculate the out-the-door price for an automobile? (Yes/No): ").strip().lower()
  if response != "yes":
      break

  make = input("Enter the make of the automobile: ")
  model = input("Enter the model of the automobile: ")
  electric_vehicle_code = input("Is it an electric vehicle? (Y/N): ").strip().upper()
  msrp = float(input("Enter the MSRP (sticker price) of the automobile: $")

  total_price = calculate_out_the_door_price(msrp, make, model, electric_vehicle_code)
  total_msrp += msrp
  total_sales_price += total_price

  print(f"The out-the-door price for the {make} {model} is: ${total_price:.2f}\n")

print(f"Total MSRP of all cars: ${total_msrp:.2f}")
print(f"Total sales price of all cars: ${total_sales_price:.2f}")
