from library.repository import LibraryRepository
from library.services import LibraryService
from library.ui import LibraryUI
from utils.error_handler import handle_exceptions

@handle_exceptions
def main():
    repo = LibraryRepository()
    service = LibraryService(repo)
    ui = LibraryUI(service)

    while True:
        ui.display_menu()
        choice = ui.get_choice()

        if choice == '1':
            ui.add_book_flow()
        elif choice == '2':
            ui.search_book_flow()
        elif choice == '3':
            ui.issue_book_flow()
        elif choice == '4':
            ui.return_book_flow()
        elif choice == '5':
            ui.display_books_flow()
        elif choice == '6':
            print("\nThank you for using the Library Management System. Application is now closing. Have a great day!")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 6.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # User pressed Ctrl+C or interrupted program
        print("\nApplication interrupted by user. Closing gracefully.!")
    except Exception:
        # Catch-all for unexpected errors
        print("\nOops! Something went wrong. The application will now close. Please try again later or contact support.")
