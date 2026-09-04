from Book import Book
 
my_favourite_book = Book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction")
 
text_file = open("output.txt", "a")
text_file.write(f"{my_favourite_book}\n")
text_file.close()