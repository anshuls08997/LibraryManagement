from .services import LibraryService

class LibraryUI:
    def __init__(self, service: LibraryService):
        self.service = service

    def display_menu(self):
        print("\n------ Library Management System ------")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Display All Books")
        print("6. Exit")

    def get_choice(self):
        return input("Enter your choice (1-6): ").strip()

    def add_book_flow(self):
        book_id = input("Enter book ID (numeric): ")
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        success, message = self.service.add_book(book_id, title, author)
        print(message)

    def search_book_flow(self):
        book_id = input("Enter book ID to search: ")
        success, message = self.service.get_book_info(book_id)
        print(message)

    def issue_book_flow(self):
        book_id = input("Enter book ID to issue: ")
        user_name = input("Enter your name: ")
        success, message = self.service.issue_book(book_id, user_name)
        print(message)

    def return_book_flow(self):
        book_id = input("Enter book ID to return: ")
        success, message = self.service.return_book(book_id)
        print(message)

    def display_books_flow(self):
        print(self.service.list_all_books())
