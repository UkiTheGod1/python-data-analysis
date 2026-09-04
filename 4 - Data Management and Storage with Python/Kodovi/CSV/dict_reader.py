import csv
 
with open("books.csv", mode="r") as file:
    fieldnames = ["title", "author", "published", "genre"]
    csv_reader = csv.DictReader(file, fieldnames=fieldnames)
    for row in csv_reader:
        print(row["title"])