import pandas as pd
df = pd.read_csv('books.csv')
filtered_df1 = df.filter(items=['title', 'author'])
print(filtered_df1.head(50)) # Dobijamo 50 redova kolona title i author

filtered_df2 = df.filter(items=[0, 1, 2, 3], axis=0) # 0 - redovi, 1 - kolone
print(filtered_df2) # Dobijamo prva 4 reda (sve kolone)

df = df.set_index('catalog_position') # Stavljamo da je catalog_position index
filtered_df3 = df.filter(like="A1-B1", axis=0) # Dobijamo redove cije je catalog_position A1-B1
print(filtered_df3)

filtered_df4 = df.filter(like="A1-B1", axis=0).filter(items=['title', 'author'])
print(filtered_df4.to_string()) # to_string() pokazuje sve (nema tri tacke) i nadovezujemo filter da bi prikazao samo title i author kolone
                                # Spojili smo filtered_df1 i filtered_df3

filtered_df5 = df[df['author'] == 'Mark Twain'] # Filter bez filtera, trazimo gde je polje author jednako sa Mark Twain
print(filtered_df5)

