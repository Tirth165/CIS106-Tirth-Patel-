#Input Phase 
accumulated_interest = 0

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (as a decimal): "))

#Process Phase 
for year in range(1, 6):
    annual_interest = principal * rate
    ending_balance = principal + annual_interest
  
    print(f"Year {year}:")
    print(f"Beginning Balance: ${principal:.2f}")
    print(f"Ending Balance: ${ending_balance:.2f}")
    print(f"Annual Interest: ${annual_interest:.2f}")
    print()

    accumulated_interest += annual_interest

    principal = ending_balance

#Output Phase 
print(f"Accumulated Interest over 5 years: ${accumulated_interest:.2f}")
