import pandas as pd

df = pd.read_csv('books.csv')

 
print(df['language'].unique()) # Prikaz unikatnih vrednosti
print(df['language'].value_counts()) # Prikaz koliko puta se pojavljuje vrednost


mapping = {
    'eng': 'en',
    'En': 'en',
    "pt-BR": "br",
    "zh-CN": "cn"
}
 
df['language'] = df['language'].astype(object).replace(mapping).astype("category")
# Promena u object jer je category i lakse je manipulisati objektima, replace-ujemo i vracamo type na category

print(df['language'].value_counts())