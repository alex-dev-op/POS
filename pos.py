class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append((product, quantity))

    def remove_item(self, product):
        self.items.remove(product)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[0].price * item[1]
        return total

class POS:
    def __init__(self):
        self.cart = Cart()

    def scan_product(self, product, quantity=1):
        self.cart.add_item(product, quantity)

    def remove_product(self, product):
        self.cart.remove_item(product)

    def checkout(self):
        total = self.cart.calculate_total()
        print(f'Total: ${total}')
        # ResetCart
        self.cart = Cart()

