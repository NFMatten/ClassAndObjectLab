from product import Product

class ShoppingCart:
    def __init__(self):
        self.product_list = [] # list of objects (products)

    def calc_total_of_cart(self):
        pass

    def add_product(self, product_to_add):
        self.product_list.append(product_to_add)
      
    def clear_cart(self):
        self.product_list = []

    def display_shopping_cart(self):
        print(f'Shopping cart {self.product_list}')