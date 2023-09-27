#Input Phase
NameOfAppliance = input("enter Name of Appliance") 
CostOfAppliance = float(input("Enter Cost Of Appliance"))
CostOfWarrantee = float(input("Enter Cost Of Warrantee"))

#Process Phase
CostOfWarrantee = 1000 * .10 
Total = CostOfAppliance + CostOfWarrantee 

#OutPut Phase
print("Total" , Total)
print("CostOfWarrantee" , CostOfWarrantee)