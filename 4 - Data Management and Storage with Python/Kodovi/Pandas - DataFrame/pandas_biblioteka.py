from Book import Book
import pandas as pd
import os

books = []

if os.path.exists("pandas.csv"):
    df = pd.read_csv("pandas.csv")
    for index, row in df.iterrows():
        book = Book.create_from_dict(row)
        books.append(book)

if (len(books) > 0):
    print("\nAll books in the library:")
    for book in books:
        print(book)

command = input("Add new (Y/N)?")
 
while command == 'Y' or command == 'y':
 
    book_id = input("Book id:")
    book_id = int(book_id)
    book_title = input("Book title:")
    book_author = input("Book author:")
    book_published = input("Year of publishing:")
    book_published = int(book_published)
    book_genre = input("Book genre:")
 
    book = Book(book_id, book_title, book_author, book_published, book_genre)
 
    books.append(book)
    df = pd.DataFrame(book.__dict__ for book in books)
    df.to_csv("pandas.csv", index=False)
    print(f"You have added new book : {book_title}")
 
    command = input("Add new (Y/N)?")
 
print("\nGoodbye!")