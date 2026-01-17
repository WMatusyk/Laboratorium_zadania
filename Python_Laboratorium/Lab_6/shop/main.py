from models.product import Product
from logic.cart import Cart

def main():
    # Utwórz co najmniej trzy obiekty produktów
    p1 = Product("Laptop", 3500.0, "Elektronika")
    p2 = Product("Jabłko", 2.5, "Spożywcze")
    p3 = Product("Myszka", 150.0, "Elektronika")
    p4 = Product("Jabłko", 3.0, "Spożywcze") # Inna cena, ta sama nazwa i kategoria

    print("--- Testy produktów ---")
    print(f"Produkt 1: {p1}")
    print(f"Produkt 2: {p2}")
    print(f"Produkt 3: {p3}")
    
    # Testy logiczne: Porównanie produktów (==)
    print(f"\nCzy p2 (Jabłko, 2.5) == p4 (Jabłko, 3.0)? {p2 == p4} (Oczekiwane: True, bo nazwa i kategoria te same)")
    print(f"Czy p1 == p3? {p1 == p3} (Oczekiwane: False)")

    # Testy logiczne: Porównanie produktów (<)
    print(f"\nCzy p2 < p1? {p2 < p1} (Oczekiwane: True, 2.5 < 3500.0)")
    
    # Sortowanie
    products_list = [p1, p2, p3]
    print(f"\nPrzed sortowaniem: {[p.name for p in products_list]}")
    products_list.sort()
    print(f"Po sortowaniu (wg ceny): {[p.name for p in products_list]}")

    # Testy len() na produkcie
    print(f"\nDługość nazwy '{p1.name}': {len(p1)}")

    print("\n--- Testy koszyka ---")
    cart = Cart()
    cart.add_product(p1)
    cart.add_product(p2)
    cart.add_product(p3)

    # Wypisz liczbę produktów w koszyku używając len()
    print(f"Liczba produktów w koszyku: {len(cart)}")

    # Sprawdź obecność konkretnego produktu w koszyku za pomocą operatora in
    print(f"Czy '{p1.name}' jest w koszyku? {p1 in cart}")
    fake_product = Product("Chleb", 5.0, "Spożywcze")
    print(f"Czy 'Chleb' jest w koszyku? {fake_product in cart}")

    # Wyświetl sumaryczną cenę oraz pełną listę zakupów
    print("\nPełna lista zakupów:")
    print(cart)

    # --- Testy Rozszerzeń ---
    print("\n--- Testy Rozszerzeń (Step 5) ---")
    
    # 1. Test __getitem__
    print(f"Pierwszy produkt w koszyku (indeks 0): {cart[0]}")

    # 2. Test filtrowania
    elektronika = cart.filter_by_category("Elektronika")
    print(f"\nProdukty z kategorii 'Elektronika': {[p.name for p in elektronika]}")
    
    # 3. Test zapisu do CSV
    csv_filename = "koszyk.csv"
    cart.save_to_csv(csv_filename)
    print(f"\nZapisano koszyk do pliku '{csv_filename}'.")

    # 4. Test rabatów
    from logic.discounts import Discount
    discount = Discount("Black Friday", 20) # 20% zniżki
    total = cart.total_price()
    discounted_total = discount.apply(total)
    print(f"\nCałkowita wartość: {total} PLN")
    print(f"Zastosowano {discount}: Nowa kwota: {discounted_total} PLN")


if __name__ == "__main__":
    main()
