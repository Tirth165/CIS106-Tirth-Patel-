#InputPhase 

def calculate_mpg(miles, gallons):
  if gallons == 0:
      return 0.0
  return miles / gallons

trips = []
entry_count = 0

#ProcessPhase

while True:
  try:
      destination_city = input("Enter the destination city (or press Ctrl+Z to stop): ")
      if not destination_city:
          break
      miles = float(input("Enter the number of miles traveled: "))
      gallons = float(input("Enter the number of gallons used: "))

      mpg = calculate_mpg(miles, gallons)
      trips.append((destination_city, miles, mpg))
      entry_count += 1
  except (ValueError, ZeroDivisionError):
      print("Invalid input. Please enter valid numbers for miles and gallons.")

#Output Phase

print("\nTrip Information:")
for trip in trips:
  destination, miles, mpg = trip
  print(f"Destination City: {destination}")
  print(f"Miles Traveled: {miles} miles")
  print(f"Miles Per Gallon (MPG): {mpg:.2f} MPG")
  print()
print
