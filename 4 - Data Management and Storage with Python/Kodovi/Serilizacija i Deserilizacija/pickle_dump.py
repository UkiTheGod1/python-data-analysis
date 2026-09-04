import pickle
from Book import Book
 
my_favourite_book = Book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction")  
 
with open('my_book.pkl', 'wb') as file:
    pickle.dump(my_favourite_book, file)