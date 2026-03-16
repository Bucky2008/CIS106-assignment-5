#input phase
quantity = int(input("Enter quantity of widgets: "))

#process phase
if quantity > 10000:
    price = 10
elif quantity >=5000:
    price = 20
else:
    price = 30

extended_price = quantity * price
tax = extended_price * 0.07 
total = extended_price + tax

#output phase 
print("Price per widget", price)
print("Extended price:", extended_price)
print("Tax:", tax)
print("Total:,total")
