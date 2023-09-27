#Input phase
ItemQuantity = float(input("Enter Item Quantity")) 
QuantityUnitPrice = float(input("Enter the quantity Unit Price"))
Tax = float(input("Enter Tax Percent"))

#Process phase
ExtendedPrice = ItemQuantity * QuantityUnitPrice 
Total = ExtendedPrice + Tax 


#Output phase 
print("ItemQuantity", ItemQuantity) 
print("QuantiyUnitPrice", QuantityUnitPrice) 
print(" ExtendedPrice", ExtendedPrice)
print("Tax", Tax)
print("Total", Total)