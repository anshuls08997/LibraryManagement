from .models import Book

class LibraryRepository:
    def __init__(self):
        self.books = {}  # book_id -> Book instance
        self.issued_books = {}  # book_id -> user name

    def add_book(self, book: Book) -> bool:
        if book.book_id in self.books:
            return False  # Book ID already exists
        self.books[book.book_id] = book
        return True

    def get_book(self, book_id: int):
        return self.books.get(book_id)

    def update_book(self, book: Book):
        self.books[book.book_id] = book

    def issue_book(self, book_id: int, user_name: str) -> bool:
        book = self.books.get(book_id)
        if not book or book.issued:
            return False
        book.issued = True
        self.issued_books[book_id] = user_name
        self.update_book(book)
        return True

    def return_book(self, book_id: int) -> bool:
        book = self.books.get(book_id)
        if not book or not book.issued:
            return False
        book.issued = False
        self.issued_books.pop(book_id, None)
        self.update_book(book)
        return True

    def list_books(self):
        return list(self.books.values())
