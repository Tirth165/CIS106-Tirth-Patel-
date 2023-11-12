# Function to display names
def display_names(names):
    print("Names:")
    for name in names:
        print(name)

# Function to display names in reverse order
def display_names_reverse(names):
    print("Names in Reverse Order:")
    for name in reversed(names):
        print(name)

# Assign 10 last names to an array
last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]

# Display names
display_names(last_names)

# Display names in reverse order
display_names_reverse(last_names)
