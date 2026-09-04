import csv

with open('my_book.csv', 'a', newline='') as file:
    fieldnames = ['title', 'author', 'published', 'genre']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writerow({'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'published': 1813, 'genre': 'Romance'})