# Define the bonus rate chart
bonus_rates = {
    50000: 0.1,
    60000: 0.15,
    70000: 0.2,
    # Add more salary thresholds and bonus rates as needed
}

# Initialize variables
total_bonus = 0

# InputPhase
with open("employee_data.txt", "r") as file:
    for line in file:
        data = line.split()
        if len(data) == 2:
            lastname, salary = data[0], float(data[1])

            bonus_rate = 0
            for threshold_salary, rate in bonus_rates.items():
                if salary <= threshold_salary:
                    bonus_rate = rate
                    break

            #ProcessPhase
            bonus = salary * bonus_rate

            #OutputPhase 
            print(f"Last Name: {lastname}, Salary: ${salary:.2f}, Bonus: ${bonus:.2f}")
          
            total_bonus += bonus

print(f"Total Bonuses Paid Out: ${total_bonus:.2f}")
