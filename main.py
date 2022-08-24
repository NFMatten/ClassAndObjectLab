from customer import Customer
# Task 2: Shopping Cart

customer_1 = Customer("John")

# End goal:
# print customer's name
print(customer_1.name)
#call the customers add product (x3) adding 3 objects
customer_1.add_product_to_cart("apple", 1, "fruit")
customer_1.add_product_to_cart("carrot", 1, "veggie")
customer_1.add_product_to_cart("steak", 5, "meat")
#call customers view products method
customer_1.display_cart
#call customers shopping cart get cart total method. Capture the total the method returns in a variable and print
#call the customers shopping carts empty cart method
#check if cart is empty