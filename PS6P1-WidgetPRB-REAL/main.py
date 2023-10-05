# InputPhase:
def calculateprice(quantity):
    if quantity > 10000:
        return 10
    elif 5000 <= quantity <= 10000:
        return 20
    else:
        return 30

# ProcessPhase:
def calculatetotals(quantity):
    priceperwidget = calculateprice(quantity)
    extendedprice = quantity * priceperwidget
    taxrate = 0.07
    taxamount = extendedprice * taxrate
    total = extendedprice + taxamount
    return extendedprice, taxamount, total

quantity = int(input("Enter the quantity of widgets: "))

# OutPutPhase: 
extendedprice, taxamount, total = calculatetotals(quantity)
print(f"Extended Price: {extendedprice:.2f}")
print(f"Tax Amount: {taxamount:.2f}")
print(f"Total: {total:.2f}")
