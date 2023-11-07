def calculate_scores_with_handicap(last_name, score1, score2, score3, handicap):
  # Compute Average Score
  average_score = (score1 + score2 + score3) / 3

  # Compute Average Score with Handicap
  average_score_with_handicap = average_score + handicap

  # Return both average score and average score with handicap
  return average_score, average_score_with_handicap

# Main function
if __name__ == "__main__":
  # Get input values from the user
  last_name = input("Enter the bowler's last name: ")
  score1 = float(input("Enter Game Score 1: "))
  score2 = float(input("Enter Game Score 2: "))
  score3 = float(input("Enter Game Score 3: "))
  handicap = float(input("Enter Handicap: "))

  # Call the function to calculate average score and average score with handicap
  average_score, average_score_with_handicap = calculate_scores_with_handicap(last_name, score1, score2, score3, handicap)

  # Display the results
  print(f"Bowler's Last Name: {last_name}")
  print(f"Average Score: {average_score:.2f}")
  print(f"Average Score with Handicap: {average_score_with_handicap:.2f}")
