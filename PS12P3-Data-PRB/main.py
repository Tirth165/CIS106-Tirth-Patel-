# Function to display names and exam scores
def display_data(names, scores):
    print("Names and Exam Scores:")
    for i in range(len(names)):
        print(f"{names[i]} - Exam Score: {scores[i]}")

# Function to find and display the highest and lowest scores along with last names
def display_highest_and_lowest(names, scores):
    high_var = 0
    low_var = 999
    high_index = 0
    low_index = 0

    for i in range(len(scores)):
        # Check for highest score
        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i

        # Check for lowest score
        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i

    print(f"Highest Score: {names[high_index]} - {high_var}")
    print(f"Lowest Score: {names[low_index]} - {low_var}")

# Read data from a file
def read_data_from_file(file_path):
    names = []
    scores = []

    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            names.append(data[0])
            scores.append(int(data[1]))

    return names, scores

# File path to your data file (replace 'data.txt' with your actual file name)
file_path = 'data.txt'

# Read data from file
last_names, exam_scores = read_data_from_file(file_path
