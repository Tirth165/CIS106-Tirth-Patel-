#Input Phase
def calculate_tuition(credit_hours, district_code):
    if district_code == "I":
        return credit_hours * 250
    elif district_code == "O":
        return credit_hours * 550
    else:
        return 0

student_data = []
total_tuition_owed = 0.0

#Process Phase 
while True:
    try:
        last_name = input("Enter student's last name (or press Ctrl+Z to stop): ")
        if not last_name:
            break 
        credit_hours = int(input("Enter the number of credit hours: "))
        district_code = input("Enter the district code (I for in-district, O for out-of-district): ").upper()

        tuition_owed = calculate_tuition(credit_hours, district_code)

        student_data.append((last_name, tuition_owed))
        total_tuition_owed += tuition_owed
    except (ValueError, ZeroDivisionError):
        print("Invalid input. Please enter valid credit hours and district code.")

# Output Phase 
print("\nStudent Information:")
for student in student_data:
    last_name, tuition_owed = student
    print(f"Last Name: {last_name}")
    print(f"Tuition Owed: ${tuition_owed:.2f}")
    print()

print(f"Total Tuition Owed for all students: ${total_tuition_owed:.2f}")
