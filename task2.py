import json   # to work with json files

FILENAME = "library.json"   # file where books are stored


# ---------- Helper Functions ----------
def load_books():
    try:
        with open(FILENAME, "r") as file:
            data = file.read().strip()
            if not data:
                return []   # empty file to return empty list
            return json.loads(data)   # json to Python list
    except FileNotFoundError:
        return []


def save_books(books):
    with open(FILENAME, "w") as file:
        json.dump(books, file, indent=4)   # Python list to json


# ---------- Features ----------
def add_book():
    books = load_books()
    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    quantity = int(input("Enter Quantity: "))

    books.append({   # each book is a dictionary
        "book_id": book_id,
        "title": title,
        "author": author,
        "quantity": quantity
    })

    save_books(books)
    print(f"Book '{title}' added successfully!")


def view_books():
    books = load_books()
    if not books:
        print("No books available.")
    else:
        for book in books:
            print(
                f"{book['book_id']} - {book['title']} by {book['author']} (Qty: {book['quantity']})")


def borrow_book():
    books = load_books()
    book_id = input("Enter Book ID to borrow: ")

    for book in books:
        if book["book_id"] == book_id:
            if book["quantity"] > 0:
                book["quantity"] -= 1   # decrease when borrowed
                save_books(books)
                print(f"You borrowed '{book['title']}'.")
                return
            else:
                print("Not available right now.")
                return
    print("Book ID not found.")


def return_book():
    books = load_books()
    book_id = input("Enter Book ID to return: ")

    for book in books:
        if book["book_id"] == book_id:
            book["quantity"] += 1   # increase when returned
            save_books(books)
            print(f"You returned '{book['title']}'.")
            return
    print("Book ID not found.")


# ---------- Menu ----------
def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            break   # exit the loop


if __name__ == "__main__":   # run main only if script is executed directly
    main()
