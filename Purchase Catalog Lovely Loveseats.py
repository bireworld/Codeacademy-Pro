#PROJECT: Create Purchasing Information and Receipts for Lovely Loveseats


#CATALOG
lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches
high x 40 inches wide x 30 inches deep. Red or white.
"""
lovely_loveseat_price = 254.00

stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""
stylish_settee_price = 180.50

luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""
luxurious_lamp_price = 52.15

#SALES TAX
sales_tax = .088

#FIRST CUSTOMER
customer_one_total = 0
customer_one_itemization = ""

#customer one purchases loveseat
customer_one_total += lovely_loveseat_price
customer_one_itemization = lovely_loveseat_description

#customer one adds lamp to purchase
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

#customer one is ready to check out
customer_one_tax = customer_one_total*sales_tax
customer_one_total += customer_one_tax

print("Customer One Items:" + str(customer_one_itemization))
print("Customer One Total: " + "$" + str(round(customer_one_total, 2)) + "\n" + "**********")


#SECOND CUSTOMER
customer_two_total = 0
customer_two_itemization = ""

#customer two purchases settee
customer_two_total = stylish_settee_price
customer_two_itemization = stylish_settee_description

#customer two adds lamp to purchase
customer_two_total += luxurious_lamp_price
customer_two_itemization += luxurious_lamp_description

#customer two is ready to check out
customer_two_tax = customer_two_total * sales_tax
customer_two_total += customer_two_tax

print("Customer Two Items:" + str(customer_two_itemization))
print("Customer Two Total: " + "$" + str(round(customer_two_total, 2)) + "\n" + "**********")





