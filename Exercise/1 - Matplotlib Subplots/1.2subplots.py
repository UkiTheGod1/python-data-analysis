import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Datum': ['2025-01-01', '2025-01-01', '2025-01-02', '2025-01-02', '2025-01-03', '2025-01-03', '2025-01-04', '2025-01-04', '2025-01-05', '2025-01-05'],
    'Grad': ['Beograd', 'Novi Sad', 'Beograd', 'Niš', 'Novi Sad', 'Beograd', 'Niš', 'Novi Sad', 'Beograd', 'Niš'],
    'Prodaja_RSD': [120000, 95000, 150000, 45000, 110000, 800000, 48000, 105000, 140000, 52000],
    'Broj_Kupaca': [45, 38, 52, 20, 40, 5, 22, 41, 48, 25],
    'Kategorija': ['Elektronika', 'Elektronika', 'Nameštaj', 'Elektronika', 'Nameštaj', 'Elektronika', 'Nameštaj', 'Elektronika', 'Nameštaj', 'Nameštaj']
}

df = pd.DataFrame(data)

# 1. Pocetak - provera

print(df) # Cisto da vidimo kako izgleda dataframe
print(df.dtypes) # Provera tipova, da vidimo da li je sve kako treba - Nije: Datum, Grad i Kategoriju mozemo pretvoriti da nisu object

# 2. Konvertovanje

df["Datum"] = pd.to_datetime(df["Datum"], errors="coerce")
df["Grad"] = df["Grad"].astype("string")
df["Kategorija"] = df["Kategorija"].astype("category")
print(df.dtypes) # Grad i Kategorija je bilo suvisno pretvarati, ali hajde da vezbamo :D

# 3. Duplikati i nepoznate vrednosti
print(df.duplicated().sum()) # Nema duplikata
print(df.notna()) # Nema NA vrednosti

# 4. Spremanje podataka za vizualizaciju

# 4.1 Ukupna prodaja po gradovima
df_UPpG = df.groupby("Grad").agg(
    Prodaja = ("Prodaja_RSD", "sum")).reset_index().sort_values(by="Prodaja", ascending=False)

# 4.2 Efikastnost
df_EF = df.sort_values(by="Broj_Kupaca", ascending=False)

# 4.3 Distribucija - nepotrebno je formirati podatke

# 5. Vizualizacija

fig, axs = plt.subplots(2, 2, figsize=(16,8))

sns.barplot(df_UPpG, x = "Prodaja", y = "Grad", hue = "Grad", ax = axs[0,0])
axs[0,0].set_title("Ukupna prodaja po gradu")

sns.scatterplot(df_EF, x = "Broj_Kupaca", y = "Prodaja_RSD", hue = "Kategorija", style="Grad", s=200, ax=axs[0,1])
axs[0,1].set_title("Odnos prodaje i broja kupaca")

sns.boxplot(df, x = "Prodaja_RSD", y = "Grad", hue = "Grad", showfliers=False, ax=axs[1,0])
axs[1,0].set_title("Raspon prodaje po gradovima")

axs[1,1].set_title("Najrizicniji grad je ???")

plt.tight_layout()
plt.show()

# 1. Nismo imali grafik sa kategorijama da znam koja kategorija je napravila anomaliju
# 2. Vidimo da je ta cifra od 800.000 dosla od jednog kupca



