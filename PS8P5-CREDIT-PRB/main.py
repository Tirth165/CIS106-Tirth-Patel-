# InputPhase
total_tuition_owed = 0
student_count = 0

#ProcessPhase 
with open('students.txt', 'r') as file:
    for line in file:
        last_name, district_code, credits = line.strip().split(', ')

        credits = int(credits)

        if district_code == 'I':
            cost_per_credit = 250.00
        elif district_code == 'O':
            cost_per_credit = 500.00
        else:

#OutputPhase 
            print(f"Invalid district code for student {last_name}. Skipping.")
            continue

       
        tuition_owed = credits * cost_per_credit
      
        print(f"Last Name: {last_name}, Credits Taken: {credits}, Tuition Owed: {tuition_owed:.2f}")

