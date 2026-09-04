import csv
 
with open('books.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["The Alchemist", "Paulo Coelho", 1988, 'Adventure'])

# Svaki put kad pokrenemo program on ce da upise ovaj red u books.csv 