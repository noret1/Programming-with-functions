"""
Author:Nabukenya Phiona
Description:price_1 is the price of achild's meal and price_2 is the price of an adult's meal
num_children means number of children
num_adults means number of adults
#i added atip calculator that asks the user for atip percentage and include it in the final total
#tip rate is apercentage of the meal total that acustomer voluntarily adds as areward for agood us
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
sales_tax_rate = float(input("what is the sales tax rate? "))
sales_tax = subtotal * (sales_tax_rate / 100)
total = subtotal + sales_tax
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")
print()
payment = float(input("\nWhat is the payment amount? "))
change = payment - total
print(f"Change: ${change:.2f}")
print()
tip_rate = float(input("Enter tip percentage ( 15 for 15%): "))
tip_amount = total * (tip_rate / 100)
grand_total = total + tip_amount
print()
print(f"Tip: ${tip_amount:.2f}")
print(f"Grand Total (with tip): ${grand_total:.2f}")


