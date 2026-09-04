import pandas as pd
import numpy as np

df = pd.read_csv("D:/Python/libraries/smart_home_prodaja_2025_raw.csv")

# 1. Proveravanje svega

print(df.sample(10, random_state=40)) # Random state da bi iste (ali nasumicne) podatke uvek izbacivao tokom printa

print(df.dtypes) # Datum treba menjati, Proizvod i Grad nek ostanu object, Cena, Zarada i Kolicina nek ostanu float

# 2. Pretvaranje tipova kolona

df["Datum"] = pd.to_datetime(df["Datum"], errors="coerce")

# 3. Izbacivanje NaN vrednosti - Odluceno je da se izbacuju umesto da se popunjavaju sa prosecnim vrednostima

print(df.shape[0]) # Gledamo koliko redova imamo pre dropovanja (515)
print(df.isna().sum()) # Gledamo koliko ima nedostajucih vrednosti i u kojoj to koloni

df.dropna(axis=0, how="any", inplace=True) # Brisemo NaN i NaT vrednosti
df.reset_index(drop=True, inplace=True) # Resetujemo indexe da krecu od 0 i dropujemo kolonu "index"

print(df.shape[0]) # Gledamo koliko redova imamo posle dropovanja (463 - uklonili smo 52 reda)
print(df.isna().sum()) # Proveravamo da li smo sve nedostajuce vrednosti izbacili 

# 4. Duplikati

print(df.duplicated().sum()) # 11 duplikata
print(df[df.duplicated]) # Gledamo kojih tacno 11
df.drop_duplicates(keep="first", inplace=True, ignore_index=True)
print(df.duplicated().sum()) # 0 duplikata

# 5. Opet cemo izracunati ukupnu zaradu bez duplikata i NaN vrednosti

df_filter = df[df["Ukupna_Zarada"] == 0]
print(df_filter.to_string())

# Cudno je sto kada sam pokusao da mi ispise sve redove gde proizvod cene i kolicine nije jednak ukupnoj zaradi, dobio sam 42 reda
# Medjutim gledajuci sam fajl shvatio sam da umesto resenja od 100, u koloni pise 100.0000001 i zato nije tacno

df["Ukupna_Zarada"] = df["Cena_EUR"] * df["Količina"]
df["Ukupna_Zarada"] = df["Ukupna_Zarada"].round(2)

df_filter2 = df[(df["Cena_EUR"] * df["Količina"]).round(2) != df["Ukupna_Zarada"]]
print(df_filter2.to_string()) # Empty DataFrame :3

# 6. Export

# df.to_csv("smart_home_prodaja_2025.csv", index=False)

print(df.dtypes)


