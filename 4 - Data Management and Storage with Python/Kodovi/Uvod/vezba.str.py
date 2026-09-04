class Book:
    def __init__(self, title, author, published, genre):
        self.title = title
        self.author = author
        self.published = published
        self.genre = genre
 
    def __str__(self):
        return f'{self.title}, {self.author}, {self.published}, {self.genre}'

books = []
 
command = input("Add new (Y/N)?")
 
while command == 'Y' or command == 'y':
 
    book_title = input("Book title:")
    book_author = input("Book author:")
    book_published = input("Year of publishing:")
    book_published = int(book_published)
    book_genre = input("Book genre:")
 
    book = Book(book_title, book_author, book_published, book_genre)
 
    books.append(book)
 
    print(f"You have added new book : {book.title}")
 
    command = input("Add new (Y/N)?")
 
print("\nAll books in the library:")
for book in books:
    print(book)
 
print("\nGoodbye!")