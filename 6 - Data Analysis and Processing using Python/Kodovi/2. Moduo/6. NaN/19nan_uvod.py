import pandas as pd

 
df = pd.read_csv('books.csv')
 

 
print(df.isnull()) # Ne dobijamo neko resenje sa ovim

print(df.isnull().sum()) # Ovo je vec bolje (pokazuje koliko koja kolona ima null (nedostajuca vrednost) celija)


# Brisemo ove kolone jer su nebitne, imaju preko 1700 nepopunjenih celija od ukupno 2000 tkd ono