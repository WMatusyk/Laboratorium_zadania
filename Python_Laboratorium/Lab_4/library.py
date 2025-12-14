class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            return f"{self.title} wypożyczona"
        return f"{self.title} jest już wypożyczona."

    def return_book(self):
        self.is_available = True
        return f"{self.title} zwrócona."

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return "Dodano książkę do biblioteki."

    def list_books(self):
        for book in self.books:
            print(f"{book.title}, {book.author}, {book.year}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                return book.borrow_book()
        return "Nie ma takiej książki w bibliotece."

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                return book.return_book()
        return "Nie wypożyczono takiej książki"



