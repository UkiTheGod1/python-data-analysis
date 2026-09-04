import csv
 
with open('my_book.csv', 'w', newline='') as file:
    fieldnames = ["title", "author", "published", "genre"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
 
    writer.writeheader()
    writer.writerow({'title': 'The Alchemist', 'author': 'Paulo Coelho', 'published': 1988, 'genre': 'Adventure'})
    # Unutar writerow mozemo iskoristiti naziv klase (my_favourite_book = Book(....)) i dodati .__dict__ i automatski ce dodati vrednosti.