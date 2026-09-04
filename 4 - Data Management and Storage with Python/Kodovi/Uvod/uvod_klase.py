class Book:
    def __init__ (self, name, author, date, genre):
        self.name = name
        self.author = author
        self.date = date
        self.genre = genre

first_book = Book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction")
second_book = Book("1984", "George Orwell", 1949, "Dystopian")
third_book = Book("Moby Dick", "Herman Melville", 1851, "Adventure")
fourth_book = Book("War and Peace", "Leo Tolstoy", 1869, "Historical")
fifth_book = Book("The Catcher in the Rye", "J.D. Salinger", 1951, "Coming-of-Age")