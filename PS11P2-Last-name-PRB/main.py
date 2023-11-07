def calculate_scores(last_name, score1, score2, score3):
  # Compute Total Points
  total_points = score1 + score2 + score3

  # Compute Average Exam Score
  average_score = total_points / 3

  # Return both total points and average score
  return total_points, average_score

# Main function
if __name__ == "__main__":
  # Get input values from the user
  last_name = input("Enter the student's last name: ")
  score1 = float(input("Enter Exam Score 1: "))
  score2 = float(input("Enter Exam Score 2: "))
  score3 = float(input("Enter Exam Score 3: "))

  # Call the function to calculate total points and average score
  total_points, average_score = calculate_scores(last_name, score1, score2, score3)

  # Display the results
  print(f"Student's Last Name: {last_name}")
  print(f"Total Points: {total_points}")
  print(f"Average Exam Score: {average_score:.2f}")
