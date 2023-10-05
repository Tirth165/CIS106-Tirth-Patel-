# InputPhase
numtickets = int(input("Enter the number of concert tickets:"))

# ProcessPhae
if numtickets >= 25:
    priceperticket = 50
elif numtickets >= 10:
    priceperticket = 60
elif numtickets >= 5:
    priceperticket = 70
else:
    priceperticket = 75

totalcost = numtickets * priceperticket

# OutPutPhase
print(f"Number of tickets: {numtickets}")
print(f"Price per ticket: {priceperticket})
print(f"Total cost: ${totalcost}")
