import pandas as pd
import difflib
import numpy as np

df = pd.read_csv("online_store_data.csv")

# 1. Konverzija tipa podataka
print(df.dtypes) # Vidimo da su "quantity_sold" i "num_of_ratings" vec float64, ne moramo koristiti .to_numeric()

df["quantity_sold"] = df["quantity_sold"].astype("Int32") # Pretvorili u Int32
df["num_of_ratings"] = df["num_of_ratings"].astype("Int32") # Pretvorili u Int32

# "quantity_in_stock" je tipa object, tako da njega moramo prvo pretvoriti u numeric (float64) pa cemo onda u integer
df["quantity_in_stock"] = pd.to_numeric(df["quantity_in_stock"], errors="coerce") 
df["quantity_in_stock"] = df["quantity_in_stock"].astype("Int32")

# Isto to radimo i sa "date_added" samo sto njega pretvaramo u datetime
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

print(df.dtypes) # Proveramo da li smo sve ispravno konvertovali (nije obavezno)


# 2. Ekstrakcija numeričkih vrednosti iz kolone rating

print(df.sample(n=30, replace=False).to_string(columns=['rating']))
print(df['rating'].unique())
# Vidimo sablon (x out of 10) gde nam je potreban samo taj x, vidimo i "no value" sto moramo transformisati u NaN
def parse_rating(text):
    if pd.isna(text) or str(text).strip().lower() == "no value":
        return np.nan

    parts = str(text).split() # Napravili listu od jednog reda, npr. ('9.25', 'out', 'of', '10') i potreban nam je prvi clan liste

    try:
        return float(parts[0]) # Rejting je uglavnom decimalan, zato float
    except ValueError: # Ako se desi neki error da isto vrati NaN
        return np.nan

df['rating'] = df["rating"].apply(parse_rating)
print(df.sample(n=30, replace=False).to_string(columns=['rating'])) # Provera (nije obavezno)


# 3. Uklanjanje redova sa nedostajućim vrednostima

df.dropna(axis=0, subset=["product_name"], inplace=True)
print(df['product_name'].isna().sum()) # Provera, output je 0 znaci nema vise nedostajucih vrednosti
 
columns = df.shape[1] # Dodajemo logiku za broj kolona
df.dropna(axis=0, thresh=(columns-4), inplace=True) # Brisemo sve redove koji imaju vise od 4 NaN vrednosti


# 4. Uklanjanje duplikata

print(df[df.duplicated(keep=False)]) # Imamo samo jedan duplikat (keep=False da nam pokaze i "original" - nije neophodno)
df.drop_duplicates(keep="first", inplace=True, ignore_index=False) # Indexi nepromenjeni


# 5. Inženjering karakteristika
df['revenue'] = df['quantity_sold'] * df['price'] 


# 6. Pronalazak 10 tastatura sa najboljim i 10 televizora sa najlošijim prihodom
filter_keyboards = df[df['category'] == 'Keyboards'] # Filtriramo samo tastature
sorted_keyboards = filter_keyboards.sort_values(by='revenue', ascending=False) # Sortiramo po "revenue" da vrednost opada
top_10_keyboards = sorted_keyboards.filter(items=['product_name', 'revenue']).head(10) # Biramo da ispisuje prvih 10 redova ove 2 kolone
print(top_10_keyboards)

filter_tvs = df[df['category'] == "TVs"]
sorted_tvs = filter_tvs.sort_values(by='revenue') # Ne treba nam ascending jer se podrazumeva True vrednost
bottom_10_tvs = sorted_tvs.filter(items=['product_name', 'revenue']).head(10)
print(bottom_10_tvs)
