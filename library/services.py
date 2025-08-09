from .models import Book
from .repository import LibraryRepository

class LibraryService:
    def __init__(self, repo: LibraryRepository):
        self.repo = repo

    def add_book(self, book_id: str, title: str, author: str) -> (bool, str):
        if not book_id.isdigit():
            return False, "Book ID must be numeric."
        book_id_int = int(book_id)
        if not title or not author:
            return False, "Title and author cannot be empty."
        new_book = Book(book_id=book_id_int, title=title.strip(), author=author.strip())
        result = self.repo.add_book(new_book)
        if not result:
            return False, "Book ID already exists. Try updating the book instead."
        return True, f'Book "{title}" added successfully.'

    def get_book_info(self, book_id: str) -> (bool, str):
        if not book_id.isdigit():
            return False, "Book ID must be numeric."
        book_id_int = int(book_id)
        book = self.repo.get_book(book_id_int)
        if not book:
            return False, "Sorry, that book ID does not exist."
        status = "Issued" if book.issued else "Available"
        info = f'Book ID: {book.book_id}\nTitle: {book.title}\nAuthor: {book.author}\nStatus: {status}'
        return True, info

    def issue_book(self, book_id: str, user_name: str) -> (bool, str):
        if not book_id.isdigit():
            return False, "Book ID must be numeric."
        if not user_name.strip():
            return False, "User name cannot be empty."
        book_id_int = int(book_id)
        book = self.repo.get_book(book_id_int)
        if not book:
            return False, "Sorry, that book ID does not exist."
        if book.issued:
            return False, "This book is already issued to someone else."
        self.repo.issue_book(book_id_int, user_name.strip())
        return True, f'Book "{book.title}" issued to {user_name}.'

    def return_book(self, book_id: str) -> (bool, str):
        if not book_id.isdigit():
            return False, "Book ID must be numeric."
        book_id_int = int(book_id)
        book = self.repo.get_book(book_id_int)
        if not book:
            return False, "Sorry, that book ID does not exist."
        if not book.issued:
            return False, "This book is not currently issued."
        user_name = self.repo.issued_books.get(book_id_int, "Unknown User")
        self.repo.return_book(book_id_int)
        return True, f'Book "{book.title}" returned by {user_name}. Thank you!'

    def list_all_books(self):
        books = self.repo.list_books()
        if not books:
            return "Library is empty."
        lines = [f"\n{'ID':<6}{'Title':<20}{'Author':<20}{'Status':<10}"]
        lines.append("-" * 60)
        for book in books:
            status = "Issued" if book.issued else "Available"
            lines.append(f"{book.book_id:<6}{book.title[:19]:<20}{book.author[:19]:<20}{status:<10}")
        return "\n".join(lines)
