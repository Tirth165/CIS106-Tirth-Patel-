# InputPhase
principle = float(input("Enter the principle amount of the CD: "))
yearstomaturity = int(input("Enter the years to maturity of the CD: "))

# ProcessPhase
if principle > 100000 and yearstomaturity == 5:
    interest_rate = 0.06
elif 50000 <= principle <= 100000 and yearstomaturity == 10:
    interest_rate = 0.05
elif 50000 <= principle <= 100000 and yearstomaturity == 5:
    interest_rate = 0.04
else:
    interest_rate = 0.02

first_year_interest = principle * interest_rate

# OutPut Phase
print(f"Principle Amount: ${principle}")
print(f"Interest Rate: {interest_rate * 100}%")
print(f"Interest Amount for the First Year: ${first_year_interest}")
