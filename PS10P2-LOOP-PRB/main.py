#Input Phase 

def calculate_square_footage(length, width, height):
  floor_ceiling_area = 2 * length * width
  wall1_area = 2 * length * height
  wall2_area = 2 * width * height
  total_square_footage = floor_ceiling_area + wall1_area + wall2_area
  return total_square_footage

while True:
  response = input("Do you want to calculate the number of gallons needed to paint a room? (Yes/No): ").strip().lower()
  if response != "yes":
      break

#Process Phase
  
  length = float(input("Enter the length of the room in feet: "))
  width = float(input("Enter the width of the room in feet: "))
  height = float(input("Enter the height of the room in feet: "))

  square_footage = calculate_square_footage(length, width, height)
  gallons_needed = square_footage / 50  # 50 square feet per gallon of paint

#Output Phase 
  
  print(f"To paint the room, you'll need {gallons_needed:.2f} gallons of paint.\n")
