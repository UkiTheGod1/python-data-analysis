from Book import Book
 
text_file = open("output.txt", "r")
my_favourite_book_data = text_file.read()
text_file.close()
 
def from_string_to_book(string_book):
    attributes = string_book.split(',')
 
    for i in range(len(attributes)):
        attributes[i] = attributes[i].strip()
 
    return Book(attributes[0], attributes[1], attributes[2], attributes[3])
 
my_favourite_book = from_string_to_book(my_favourite_book_data)
 
print(my_favourite_book.name)
print(my_favourite_book.author)
print(my_favourite_book.date)
print(my_favourite_book.genre)