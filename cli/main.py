from library_manager.inventory import LibraryInventory
from library_manager.book import Book

def menu():
    inventory = LibraryInventory()
    while True:
        print("\n====== Library Inventory Manager ======")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            isbn = input("ISBN: ").strip()
            book = Book(title, author, isbn)
            inventory.add_book(book)
            print("Book added successfully.")
        elif choice == "2":
            isbn = input("Enter ISBN to issue: ").strip()
            book = inventory.search_by_isbn(isbn)
            if book and book.issue():
                inventory.save_books()
                print("Book issued.")
            else:
                print("Book unavailable or not found.")
        elif choice == "3":
            isbn = input("Enter ISBN to return: ").strip()
            book = inventory.search_by_isbn(isbn)
            if book and book.return_book():
                inventory.save_books()
                print("Book returned.")
            else:
                print("Invalid return attempt.")
        elif choice == "4":
            for b in inventory.display_all():
                print(b)
        elif choice == "5":
            title = input("Enter title to search: ").strip()
            results = inventory.search_by_title(title)
            for b in results:
                print(b)
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
