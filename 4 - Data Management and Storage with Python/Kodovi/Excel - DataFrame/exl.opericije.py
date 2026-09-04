import pandas as pd
 
df = pd.read_excel('user_rentals.xlsx')
 
# sum = df["total_rentals"].sum() - Ne radi jer se kolona smatra kao object
# print(sum)

# print(df.dtypes) - Provera koji tip podataka je koja kolona

# df["total_rentals"] = df["total_rentals"].astype('int') - Ne moze jer ima praznih polja koji ne mogu biti integer

# df["total_rentals"] = df["total_rentals"].astype('float') - Ne moze jer verovatno postoji slovo "o" umesto broja 0

df["total_rentals"] = pd.to_numeric(df["total_rentals"], errors="coerce")
print(df.dtypes) # Uspesno smo promeneli

print(df['total_rentals'].sum())
print(df["total_rentals"])