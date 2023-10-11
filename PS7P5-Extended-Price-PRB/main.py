# InputPhase 
totaldiscount = 0

while input("Do you want to continue? (Yes/No): ").lower() == "yes":
    quantity = int(input("Enter the quantity of the item: "))
    price = float(input("Enter the price of the item: "))

  
  #ProcessPhase 
  
    extendedprice = quantity * price
    if extendedprice > 10000.00:
      discountpercent = 0.25 
    else:
      discountpercent = 0.10 


    discountamount = extendedprice * discountpercent
    total = extendedprice - discountamount

  #Output Phase
  
    print(f"Extended Price: ${extendedprice:.2f}")
