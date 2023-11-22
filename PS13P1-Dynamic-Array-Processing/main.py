# Prompt the user for the number of items in the list
num_items = int(input("Enter the number of items in the list: "))

# Initialize an empty list
my_list = []

# Use a for loop to add integers to the list
for _ in range(num_items):
    user_input = int(input("Enter an integer: "))
    my_list.append(user_input)

# Display the list
print("Original List:", my_list)

# Insert the score of 99 at position 1 within the list
my_list.insert(0, 99)
print("List after inserting 99 at position 1:", my_list)

# Replace the value of 99 with the value 100
my_list[my_list.index(99)] = 100
print("List after replacing 99 with 100:", my_list)

# Create a second list
second_list = [500, 600, 700, 800, 900]
print("Second List:", second_list)

# Extend the first list with the second list
my_list.extend(second_list)
print("First List after extending with the second list:", my_list)

# Remove the value 800 from the first list
my_list.remove(800)
print("First List after removing 800:", my_list)

# Remove the third item from the first list
del my_list[2]
print("First List after removing the third item:", my_list)

# Create a list of grades
grades = ["A", "B", "C", "A", "A", "C"]

# Display the count of the number of A grades
print("Number of A grades:", grades.count("A"))

# Display the index of the first B grade
print("Index of the first B grade:", grades.index("B"))

# Look for grade of F in the grades list
if "F" not in grades:
    print("F is not in the list.")

# Clear the second list of integers
second_list.clear()
print("Cleared Second List:", second_list)

# Delete the second list
del second_list

# Try to display the second list (should get an error)
try:
    print("Second List:", second_list)
except NameError:
    print("Second List no longer exists.")

# Create a list of players
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]

# Sort the list of players
players.sort()
print("Sorted List of Players:", players)

# Make a copy of the list of players called players2
players2 = players.copy()
print("Copy of the List of Players (players2):", players2)

# Reverse the order of players2
players2.reverse()
print("Reversed players2:", players2)
