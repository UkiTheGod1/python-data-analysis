from Book import Book
import pickle
import os

books = []

if os.path.exists("library.pkl"):
    with open("library.pkl", "rb") as file:
        books = pickle.load(file)

if (len(books) > 0):
    print("\nAll books in the library:")
    for book in books:
        print(book)

command = input("Add new (Y/N)?")
 
while command == 'Y' or command == 'y':
 
    book_title = input("Book title:")
    book_author = input("Book author:")
    book_published = input("Year of publishing:")
    book_published = int(book_published)
    book_genre = input("Book genre:")
 
    book = Book(book_title, book_author, book_published, book_genre)
 
    books.append(book)
    with open("library.pkl", "wb") as file:
        pickle.dump(books, file)
 
    print(f"You have added new book : {book_title}")
 
    command = input("Add new (Y/N)?")
 
print("\nGoodbye!")