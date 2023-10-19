#InputPhase 

def calculate_pay_rate(job_code):
    if job_code == "L":
        return 25.0
    elif job_code == "A":
        return 30.0
    elif job_code == "J":
        return 50.0
    else:
        return 0.0

def calculate_gross_pay(hours_worked, pay_rate):
    if hours_worked <= 40:
        return hours_worked * pay_rate
    else:
        regular_hours = 40
        overtime_hours = hours_worked - 40
        return (regular_hours * pay_rate) + (overtime_hours * (pay_rate * 1.5))

employee_data = []
total_gross_pay = 0.0

#Process Phase 

while True:
    try:
        last_name = input("Enter employee's last name (or press Ctrl+Z to stop): ")
        if not last_name:
            break 
        job_code = input("Enter the job code (L, A, or J): ").upper()
        hours_worked = float(input("Enter the number of hours worked: "))

        pay_rate = calculate_pay_rate(job_code)
        gross_pay = calculate_gross_pay(hours_worked, pay_rate)

        employee_data.append((last_name, gross_pay))
        total_gross_pay += gross_pay
    except (ValueError, ZeroDivisionError):
        print("Invalid input. Please enter valid job code and hours worked.")

# Output Phase
for employee in employee_data:
    last_name, gross_pay = employee
    print(f"Last Name: {last_name}")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print()

print(f"Total Gross Pay for all employees: ${total_gross_pay:.2f}")
