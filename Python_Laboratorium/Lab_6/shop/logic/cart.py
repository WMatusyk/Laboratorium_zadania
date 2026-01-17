from models.product import Product

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)
        else:
            raise TypeError("Only Product instances can be added to the cart.")

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def total_price(self):
        return sum(product.price for product in self.products)

    def __len__(self):
        return len(self.products)

    def __contains__(self, product):
        return product in self.products

    def __str__(self):
        if not self.products:
            return "Koszyk jest pusty."
        
        items_str = "\n".join([f"- {str(p)}" for p in self.products])
        return f"Zawartość koszyka ({len(self)} szt.):\n{items_str}\nSuma: {self.total_price()} PLN"
