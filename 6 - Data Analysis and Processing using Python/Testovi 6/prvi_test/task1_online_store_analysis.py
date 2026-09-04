import pandas as pd
df = pd.read_csv('online_store_data.csv')

# 1. Koliko proizvoda postoji u datasetu?

print("Broj redova:", df.shape[0]) # df.shape nam prikazuje broj redova i broj kolona, ako postavimo index 0, prikazace samo broj redova

# 2. Koji je najprodavaniji proizvod u celoj online trgovini

print("\nNajprodavaniji prozivod:\n", df.sort_values(by='quantity_sold', ascending = False).iloc[0].to_string(float_format="{:.0f}".format)) 
# to_string() zbog preglednosti, ascending = False da bi krenuo od najvise ka najmanje, float_format da pretvorimo quantity sold iz floata u celi broj.

# 3. Koja su 5 najprodavanijih mobilnih telefona?

mask = df['category'] == 'Smartphones'
filtered_df = df[mask]
sorted_df = filtered_df.sort_values(by='quantity_sold', ascending=False)
print("\nTop 5 najprodavanijih mobilnih telefona:\n", sorted_df.head(5))
# Filtrirani po kategoriji sa "mask", sortirani pomocu "sort_values" (ascending=False da krene od najvece vrednosti), float_format nije preko potreban
# Printujemo ".head(5)" da se prikazu prvih 5

# 4. Kolika je cena najskupljeg, a kolika najjeftinijeg laptopa

mask2 = df['category'] == 'Laptops'
filtered_laptops = df[mask2]
most_expensive = filtered_laptops.sort_values(by='price', ascending=False).iloc[0]
least_expensive = filtered_laptops.sort_values(by='price').iloc[0]
print("\nNajskuplji laptop je:\n", most_expensive, "\nNajjeftiniji laptop je:\n", least_expensive)
# Dodat index2 kod mask da ne menjamo prvi (originalni) mask. ascending=True nije iskoriscen jer se podrazumeva
# Izbacivanje NaN vrednosti nisam znao da uradim, medjutim nisu prisutne u resenju.

print(filtered_laptops['price'].max)