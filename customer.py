from shopping_cart import ShoppingCart

class Customer:
    def __init__(self, name):
        self.shopping_cart = ShoppingCart()
        self.name = name
       
    def add_product_to_cart(self, product_to_add):
        self.shopping_cart.add_product(product_to_add)

    def display_cart(self):
        for items in self.shopping_cart:
            print(items)