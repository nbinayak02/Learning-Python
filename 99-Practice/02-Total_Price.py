# Store the price of 3 items and print the total bill

# Method 1

item1 = 20
item2 = 83
item3 = 25

totalPrice = item1 + item2 + item3

print(totalPrice)

# Method 2

item_prices = [13, 45, 146]

totalPrice = 0
for price in item_prices:
    totalPrice += price 
print(totalPrice)    