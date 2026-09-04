import csv
 
with open('books.csv', 'r') as file:
    reader = csv.reader(file)
 
    for row in reader: 
        print(row)      # Printuje ceo red
        print(row[0])   # Printuje ime (prvi clan reda)
