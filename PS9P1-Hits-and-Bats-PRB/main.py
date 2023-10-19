#InputPhase

def calculate_batting_average(hits, at_bats):
  if at_bats == 0:
      return 0.0
  return float(hits) / at_bats

players = []
count = 0

#ProcessPhase 


while True:
  try:
      last_name = input("Enter player's last name (or press Ctrl+Z to stop): ")
      if last_name == "":
          break
      hits = int(input("Enter the number of hits: "))
      at_bats = int(input("Enter the number of at-bats: "))

      batting_avg = calculate_batting_average(hits, at_bats)
      players.append((last_name, batting_avg))
      count += 1
  except (ValueError, ZeroDivisionError):
      print("Invalid input. Please enter valid numbers for hits and at-bats.")


#Output Phase

print("\nBatting Averages:")
for player in players:
  last_name, batting_avg = player
  print(f"{last_name}: {batting_avg:.3f}")
print(f"Number of players entered: {count}")
