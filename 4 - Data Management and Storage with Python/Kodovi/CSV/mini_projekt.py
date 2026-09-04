import os
import csv
from classes import Book

books = []

if os.path.exists('books.csv'):
    with open('books.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            books.append(Book.create_from_dict(row))

if(len(books) > 0):
    print("\nAll books in the library:")
    for book in books:
        print(book)

command = input("Add new (Y/N)?")

while command == 'Y' or command == 'y':

    book_id = input("Book ID:")
    book_id = int(book_id)
    book_title = input("Book title:")
    book_author = input("Book author:")
    book_published = input("Year of publishing:")
    book_published = int(book_published)
    book_genre = input("Book genre:")

    book = Book(book_id, book_title, book_author, book_published, book_genre)

    books.append(book)
    with open('books.csv', 'w', newline="") as file:
        fieldnames = ['id', 'title', 'author', 'published', 'genre']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        for book in books:
            writer.writerow(book.__dict__)

    print(f"You have added new book : {book.title}")

    command = input("Add new (Y/N)?")

print("\nGoodbye!")

