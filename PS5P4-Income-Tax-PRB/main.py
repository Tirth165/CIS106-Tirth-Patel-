#Input Phase 

Lastname = input("Last Name")
NumberOfDependents = float(input("Enter Number Of Dependents")) 
GrossIncome = float(input("Input gross income"))

#Process Phase
AdjustedGrossIncome = GrossIncome - NumberOfDependents * 12000 
IncomeTaxRate = 50000 * .20 
IncomeTax = 100 

#Output Phase
print ("IncomeTaxRate", IncomeTaxRate) 