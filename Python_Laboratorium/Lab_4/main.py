from library import Book, Library


def main():
    # 1. Tworzymy bibliotekę
    library = Library()

    # 2. Dodajemy kilka książek na start (opcjonalne, ale wygodne do testów)
    library.add_book(Book("Wiedźmin", "Andrzej Sapkowski", 1993))
    library.add_book(Book("Lalka", "Bolesław Prus", 1890))

    # 3. Główna pętla programu
    while True:
        print("\n--- MENU BIBLIOTEKI ---")
        print("1. Dodaj książkę")
        print("2. Wypożycz książkę")
        print("3. Zwróć książkę")
        print("4. Pokaż wszystkie książki")
        print("5. Wyjście")

        wybor = input("Wybierz opcję (1-5): ")

        # Obsługa wyborów użytkownika
        if wybor == '1':
            title = input("Podaj tytuł: ")
            author = input("Podaj autora: ")
            year = input("Podaj rok wydania: ")
            # Tworzymy nową książkę i dodajemy do biblioteki
            new_book = Book(title, author, year)
            print(library.add_book(new_book))

        elif wybor == '2':
            title = input("Podaj tytuł książki do wypożyczenia: ")
            print(library.borrow_book(title))

        elif wybor == '3':
            title = input("Podaj tytuł książki do zwrotu: ")
            print(library.return_book(title))

        elif wybor == '4':
            print("\n--- Lista książek ---")
            library.list_books()

        elif wybor == '5':
            print("Zamykanie systemu...")
            break  # Przerywa pętlę i kończy program

        else:
            print("Niepoprawny wybór, spróbuj ponownie.")


# Uruchomienie programu
if __name__ == "__main__":
    main()