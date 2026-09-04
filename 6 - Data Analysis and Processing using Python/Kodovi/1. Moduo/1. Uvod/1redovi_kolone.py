import pandas as pd
df = pd.read_csv('books.csv')
print(df.shape) # (broj redova, broj kolona) (KOLONE USPRAVNO - REDOVI HORIZONTALNO)

rows, columns = df.shape

print("Broj redova je",rows) # Samo broj redova
print("Broj kolona je",columns) # Samo broj kolona

column_names = df.columns.tolist() # Stavlja imena kolone u listu
print("Imena kolona:", column_names)

print(df.head(20)) # Prikaz prvih 20 redova
print(df.tail(20)) # Prikaz poslednjih 20 redova
 
print(df.sample(n=5, random_state=42, replace=False))   
# n - broj nasumicnih redova ili frac - procenat svih redova
# random_state - iste vrednosti će uvek da proizvedu identične nasumične vrednosti
# replace - ne ponavljaju se redovi

print(df.iloc[0]) # Pokazuje jedan ceo red
print(df.loc[0, "title"]) # Pokazuje celiju prvog reda u koloni "title"
print(df.at[0, "title"]) # Isto kao loc

# print(df.to_string(columns=['title', 'page_count'])) # Prikazuje sve redove kolona "title" i "page_count"
# print(df.head(30).to_string(columns=['title', 'page_count'])) # Ogranicavamo broj na prvih 30
print(df.head(30).to_string(columns=['title','page_count'], float_format="{:.0f}".format)) # Formatiramo da su brojevi stranica celi brojevi

print(df.sample(n=30, replace=False).to_string(columns=['title', 'price', 'rating'], float_format="{:.0f}".format))

print(df.nunique()) # Prikazuje unikatne redove po kolonama
print(df['section'].value_counts()) # Prikazuje broj unikatnih vrednosti po koloni