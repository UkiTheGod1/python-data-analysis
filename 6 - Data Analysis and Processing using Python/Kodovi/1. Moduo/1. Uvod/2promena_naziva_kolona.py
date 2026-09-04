import pandas as pd
df = pd.read_csv('books.csv')

df.columns = ['catalog_position', 'title', 'author', 'year_published', 'genre', 'section', 'total_copies', 'times_borrowed', 'last_borrowed_date', 'rating', 'ratings_count', 'price', 'language', 'page_count', 'isbn', 'subjects', 'dimensions', 'thumbnail']
df.columns = [col.lower().replace(' ', '_').replace('-', '_') for col in df.columns]

print(df.columns.tolist())

df.to_csv("books.csv", index=False, encoding="utf-8-sig")