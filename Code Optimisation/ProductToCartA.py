class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, product_name, quantity, price):
        if not product_name or quantity <= 0 or price <= 0:
            return False
        item = {'name': product_name, 'quantity': quantity, 'price': price}
        self.items.append(item)
        return True
