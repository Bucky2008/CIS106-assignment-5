#input phase
quantity = int(input("Enter number of concert tickets:"))

#process phase
if quantity >= 25:
   price = 50
elif quantity >= 10:
   price = 60
elif quantity >= 5:
   price = 70
else:
  price = 75

total_cost = quantity * price

#output phase
print("Number of tickets:", quantity)
print("Price per ticket:", price)
print("Total cost:", total_cost)