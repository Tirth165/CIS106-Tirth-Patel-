# InputPhase
lastname = input("Enter employee last name: ")
salary = float(input("Enter employee salary: "))
joblevel = int(input("Enter employee job level: "))

# ProcessPhase
if joblevel >= 10:
    bonusrate = 0.25
elif joblevel >= 5:
    bonusrate = 0.20
else:
    bonusrate = 0.10

bonus = salary * bonusrate

# Output Phase
print(f"Employee last name: {lastname}")
print(f"Bonus: {bonus:.2f}")
