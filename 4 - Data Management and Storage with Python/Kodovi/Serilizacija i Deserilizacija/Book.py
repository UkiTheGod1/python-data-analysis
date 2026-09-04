class Book:
    def __init__ (self, name, author, date, genre):
        self.name = name
        self.author = author
        self.date = date
        self.genre = genre

    def __str__(self):
        return f'{self.name}, {self.author}, {self.date}, {self.genre}'