class Discount:
    def __init__(self, name, value_percent):
        self.name = name
        self.value_percent = value_percent

    def apply(self, price):
        """Zwraca cenę po obniżce."""
        if price < 0:
            raise ValueError("Cena nie może być ujemna")
        return price * (1 - self.value_percent / 100.0)

    def __str__(self):
        return f"Rabata '{self.name}': -{self.value_percent}%"
