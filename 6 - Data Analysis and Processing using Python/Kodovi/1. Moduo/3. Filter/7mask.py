import pandas as pd
df = pd.read_csv('books.csv')
mask = (df['genre'] == 'Drama') & (df['times_borrowed'] < 5) # U mask stavljamo kad imamo vise uslova
filtered_books = df[mask] # Definisemo filter kao df[mask] tj. df[uslovi]
print(filtered_books.filter(items=['title', 'author', 'times_borrowed']).sort_values(by='times_borrowed').head(30))