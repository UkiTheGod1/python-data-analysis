import pandas as pd

df = pd.read_csv("books.csv")
print(df.iloc[4, 2])          # Priv broj red, drugi broj kolona

print(df.loc[4, "author"])     # iloc je za indexe, loc je za tekstove

 #df = pd.read_csv('books.csv', index_col="id")  dodavajuce index_col="id" napravili smo tu kolonu da bude ID kolona
 #print(df.loc[103, "title"])                    i preko nje mozemo da pristupimo odredjenoj celiji ako joj znamo ID

 # Postoje 3 nacina dakle, ti izaberi koji ti je najlaksi