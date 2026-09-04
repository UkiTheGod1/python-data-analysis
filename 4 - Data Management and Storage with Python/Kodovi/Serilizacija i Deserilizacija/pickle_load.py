import pickle
 
with open('my_book.pkl', 'rb') as file:
    my_favourite_book = pickle.load(file)
 
print(my_favourite_book)