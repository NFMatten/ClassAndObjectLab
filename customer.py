from shopping_cart import ShoppingCart

class Customer:
    def __init__(self, name):
        shopping_cart = ShoppingCart()
        self.name = name
        self.shopping_cart = shopping_cart

    def add_product_to_cart(self, name, price, category):
        ShoppingCart.add_product(name, price, category)

    def display_cart(self):
        for items in self.shopping_cart:
            print(items[0])