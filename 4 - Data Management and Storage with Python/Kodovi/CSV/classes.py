class Book:
    def __init__(self, id, title, author, published, genre):
        self.id = id
        self.title = title
        self.author = author
        self.published = published
        self.genre = genre


    def __str__(self):
        return f'{self.id}, {self.title}, {self.author}, {self.published}, {self.genre}'
    
    def create_from_dict(row):
        return Book(row['id'], row['title'], row['author'], row['published'], row['genre'])