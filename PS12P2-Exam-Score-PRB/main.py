# Function to display names and exam scores
def display_data(names, scores):
    print("Names and Exam Scores:")
    for i in range(len(names)):
        print(f"{names[i]} - Exam Score: {scores[i]}")

# Function to display names and exam scores in reverse order
def display_data_reverse(names, scores):
    print("Names and Exam Scores in Reverse Order:")
    for i in reversed(range(len(names))):
        print(f"{names[i]} - Exam Score: {scores[i]}")

# Arrays for last names and exam scores
last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
exam_scores = [85, 90, 78, 92, 88, 76, 95, 89, 84, 91]

# Display names and exam scores
display_data(last_names, exam_scores)

# Display names and exam scores in reverse order
display_data_reverse(last_names, exam_scores)
