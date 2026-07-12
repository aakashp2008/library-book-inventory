def add_book():
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    file = open("books.txt", "a")
    file.write(f"Title: {title}, Author: {author}\n")
    file.close()

    print("Book added successfully!")

def view_books():
    try:
        file = open("books.txt", "r")
        print("\n=== Library Books ===")
        print(file.read())
        file.close()
    except FileNotFoundError:
        print("No books found.")

while True:
    print("\n=== Library Book Inventory ===")
    print("1. Add Book")
    print("2. View Books")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        print("Thank you for using Library Book Inventory!")
        break

    else:
        print("Invalid choice. Please try again.")
