class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, product_name, quantity, price):
        if product_name == '' or quantity <= 0 or price <= 0:
            return False
        item = {'name': product_name, 'quantity': quantity, 'price': price}
        try:
            self.items.append(item)
            return True
        except:
            return False
