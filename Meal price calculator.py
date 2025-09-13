"""
author:Nabukenya Phiona
Description:price_1 is  the price of achild's meal and price_2 is the price of an adult's meal
num_children means number of children
num_adults means number of adults

"""
child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))

price_1 = num_children * child_meal_price
price_2 = num_adults * adult_meal_price

subtotal = price_1 + price_2
print()
print(f"Subtotal: {subtotal:.2f}")
print()