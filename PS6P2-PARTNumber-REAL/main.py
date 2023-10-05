# InputPhase
part_costs = {
    10: 1.00,
    55: 1.00,
    99: 2.00,
    80: 3.00,
    70: 3.00,
}

# ProcessPhase
part_number = input("Enter a part number: ")
quantity = int(input("Enter the quantity: "))

if part_number.isdigit():
    part_number = int(part_number)

if part_number in part_costs:
  unit_cost = part_costs[part_number]
else:
  unit_cost = 5.00

total_cost = quantity * unit_cost

# OutputPhase
print("Part Number:", part_number)
print("Cost per Unit:", unit_cost)
print("Total Cost:", total_cost)

