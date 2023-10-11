#InputPhase

count = 0
total_score = 0

#ProcessPhase 

while True:
    userresponse = input("Do you want to continue? (Enter 'Yes' to continue ")
    
    if userresponse.lower() != "yes":
        break
    
    lastname = input("Enter last name: ")
    examscore1 = float(input("Enter the first exam score: "))
    examscore2 = float(input("Enter the second exam score: "))
    
    average_score = (examscore1 + examscore2) / 2
    
    print(f"Last Name: {lastname}")
    print(f"Average Score: {average_score}")
    
    count += 1
    
    userresponse = input("Do you want to continue? (Enter 'Yes' to continue ")

  #Output Phase
    
print(f"Total number of students who entered data: {count}")

