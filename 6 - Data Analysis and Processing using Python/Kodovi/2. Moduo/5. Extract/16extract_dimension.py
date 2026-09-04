import pandas as pd
 
df = pd.read_csv('books.csv')
 
df[['dimensions_width', 'dimensions_thickness', 'dimensions_height']] = df['dimensions'].str.replace("inches", "").str.replace(" ", "").str.split('x', expand=True).astype(float)
# Parsirali i ekstrahovali numeričke podatke iz kolone dimensions, tako što smo:
# Uklonili reč inches,
# Uklonili razmake,
# Podelili tekst po karakteru x;
# Spakovali ekstrahovanu širinu, debljinu i visinu u nove kolone (parametar expand, postavljen na True);

df.drop('dimensions', axis=1, inplace=True)
# Uklonili staru kolonu dimensions

print(df.head(30))


