import csv
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

    def filter_by_category(self, category):
        """Zwraca listę produktów z danej kategorii."""
        return [p for p in self.products if p.category == category]

    def save_to_csv(self, filename):
        """Eksportuje zawartość koszyka do pliku CSV."""
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Name', 'Category', 'Price'])
            for p in self.products:
                writer.writerow([p.name, p.category, p.price])

    def __getitem__(self, index):
        """Umożliwia dostęp do produktów po indeksie."""
        return self.products[index]

    def __len__(self):
        return len(self.products)

    def __contains__(self, product):
        return product in self.products

    def __str__(self):
        if not self.products:
            return "Koszyk jest pusty."
        
        items_str = "\n".join([f"- {str(p)}" for p in self.products])
        return f"Zawartość koszyka ({len(self)} szt.):\n{items_str}\nSuma: {self.total_price()} PLN"
