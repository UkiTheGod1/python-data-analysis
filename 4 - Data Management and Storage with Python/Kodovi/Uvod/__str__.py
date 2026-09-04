class Book:
    def __init__ (self, name, author, date, genre):
        self.name = name
        self.author = author
        self.date = date
        self.genre = genre

    def __str__(self):
        return f'{self.name}, {self.author}, {self.date}, {self.genre}'

my_favorite_books = [
    Book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    Book("1984", "George Orwell", 1949, "Dystopian"),
    Book("Moby Dick", "Herman Melville", 1851, "Adventure"),
    Book("War and Peace", "Leo Tolstoy", 1869, "Historical"),
    Book("The Catcher in the Rye", "J.D. Salinger", 1951, "Coming-of-Age")
]

for book in my_favorite_books:
    print(book)