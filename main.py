from customer import Customer
from product import Product
# Task 2: Shopping Cart

customer_1 = Customer("John")

# End goal:
# print customer's name
print(customer_1.name)

#call the customers add product (x3) adding 3 objects
# apple = Product("Apple", 1, "fruit")
# customer_one.add_product_to_cart(apple)
apple = Product("Apple", 1, "fruit")
steak = Product("Steak", 5, "meat")
carrot = Product("Carrot", 1, "veggie")
customer_1.add_product_to_cart(apple)
customer_1.add_product_to_cart(steak)
customer_1.add_product_to_cart(carrot)

#call customers view products method
print(customer_1.display_cart)


#call customers shopping cart get cart total method. Capture the total the method returns in a variable and print
#call the customers shopping carts empty cart method
#check if cart is empty