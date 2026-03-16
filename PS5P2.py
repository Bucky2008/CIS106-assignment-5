#input phase
part = int(input("Enter part number:"))
quantity = int(input("Enter quantity:"))

#process phase
if part == 10 or part == 55:
    cost = 1.00
elif part == 99:
    cost = 2.00
elif part == 80 or part == 70:
    cost = 3.00
else:
    cost = 5.00
  
total_cost = quantity * cost 

#output phase
print("Part number:",part)
print("Unit cost",cost)
print("Total cost:", total_cost)