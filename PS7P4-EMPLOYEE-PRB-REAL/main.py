#InputPhase 

total_gross_pay = 0
employee_count = 0

continueprogram = input("Do you want to continue?) Enter 'Yes' to continue, any other response to stop")

while continueprogram.lower() == "yes":
    lastname = input("Enter employee last name: ")
    hoursworked = float(input("Enter hours worked: "))
    rateofpay = float(input("Enter rate of pay: "))

    #ProcessPhase 
    if hoursworked <= 40:
        gross_pay = hoursworked * rateofpay
    else:
        regular_pay = 40 * rateofpay
        overtime_pay = (hoursworked - 40) * (rateofpay * 1.5)
        gross_pay = regular_pay + overtime_pay


  #Output Phase 
  
    print(f"Employee: {lastname}")
    print(f"Gross Pay: ${gross_pay:.2f}")
  
    total_gross_pay += gross_pay
    employee_count += 1

