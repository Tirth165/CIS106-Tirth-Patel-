# Function to display player names and batting averages
def display_data(names, averages):
    print("Player Names and Batting Averages:")
    for i in range(len(names)):
        print(f"{names[i]} - Batting Average: {averages[i]}")

# Function to search for a last name in the arrays and display the result
def search_player(name, names, averages):
    for i in range(len(names)):
        if names[i].lower() == name.lower():
            print(f"Player Found - {names[i]}: Batting Average - {averages[i]}")
            return

    print(f"Player with last name '{name}' not found.")

# Read data from a file
def read_data_from_file(file_path):
    names = []
    averages = []

    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            names.append(data[0])
            averages.append(float(data[1]))

    return names, averages

# File path to your data file (replace 'player_data.txt' with your actual file name)
file_path = 'player_data.txt'

# Read data from file
player_names, batting_averages = read_data_from_file(file_path)

# Display player names and batting averages
display_data(player_names, batting_averages)

# Use a while loop to repeatedly ask the user for a last name
while True:
    search_name = input("Enter a last name to search (or 'exit' to quit): ")

    if search_name.lower() == 'exit':
        break

    # Search for the last name in the arrays and display the result
    search_player(search_name, player_names, batting_averages)
