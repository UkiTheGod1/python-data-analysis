import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("prodaja_2025.csv")

print(df.dtypes) 

# 0. Promena kolone Datum u datetime

df["Datum"] = pd.to_datetime(df["Datum"], errors="coerce")
print(df["Datum"].head())

# 1.1 Nova kolona "Zarada" (Cena_RSD * Količina)

df["Zarada"] = df["Cena_RSD"] * df["Količina"]

# 1.2 Top 3 proizvoda po kolicini

top_3_proizvoda = df.groupby("Proizvod")["Količina"].sum()
print(top_3_proizvoda.sort_values(ascending=False).head(3))

# 1.3 Filtriranje - Novi DataFrame sa proizvodima koji imaju zaradu preko 200.000RSD

df_visoka_zarada = df[df["Zarada"] >= 200000]
print(df_visoka_zarada.shape[0]) # 626 proizvoda (374 prozivoda su imala zaradu manju od 200.000RSD)

# region Duzi nacin rada

# 2.1 Zarada po gradu 
# zarada_po_gradu = df.groupby("Grad").agg(
   # suma = ("Zarada", "sum")).reset_index().sort_values(by="suma", ascending=False)

# 2.2 Grad koji po proseku prodaje najskuplje proizvode
# najskuplji_prosecan_grad = df.groupby("Grad").agg(
   # prosek = ("Cena_RSD", "mean")).reset_index().sort_values(by="prosek", ascending=False)

# najskuplji_prosecan_grad["prosek"] = najskuplji_prosecan_grad["prosek"].round(2)


# 2.3 Bonus - grad koji po proseku ima najvecu kolicinu prozivoda i najvecu zaradu
# prosecna_kolicina_grada = df.groupby("Grad").agg(
   # kolicina = ("Količina", "mean")).reset_index().sort_values(by="kolicina", ascending=False)

# prosecna_kolicina_grada["kolicina"] = prosecna_kolicina_grada["kolicina"].round(2)


# prosecna_zarada_grada = df.groupby("Grad").agg(
   # zarada = ("Zarada", "mean")).reset_index().sort_values(by="zarada", ascending=False)

# prosecna_zarada_grada["zarada"] = prosecna_zarada_grada["zarada"].round(2)
# endregion

# 2. Kraci nacin 

grad_podaci = df.groupby("Grad").agg(
    suma = ("Zarada", "sum"),
    prosek = ("Cena_RSD", "mean"),
    kolicina = ("Količina", "mean"),
    zarada = ("Zarada", "mean")).reset_index()

grad_podaci["prosek"] = grad_podaci["prosek"].round(2)
grad_podaci["kolicina"] = grad_podaci["kolicina"].round(2)
grad_podaci["zarada"] = grad_podaci["zarada"].round(2)

print(grad_podaci)

# 3. Vizualizacija - Boxplot (cena po gradu) i barplot (Zarada po proizvodu)

fig, axs = plt.subplots(1, 2, figsize=(15,6))

sns.boxplot(df, x = "Cena_RSD", y = "Grad", hue="Grad", showfliers=False, ax = axs[0])
axs[0].set_title("Cene po gradovima", fontsize=15, color="navy")
axs[0].set_xlabel("Cena u dinarima", fontsize=12, color="navy")
axs[0].set_ylabel("Grad", fontsize=12, color="navy")

df_bar = df.groupby("Proizvod").agg(
    zarada = ("Zarada", "sum")).reset_index().sort_values(by="zarada", ascending=False)

sns.barplot(df_bar, x = "Proizvod", y = "zarada", hue="Proizvod", palette="magma", ax = axs[1])
axs[1].set_title("Ukupna zarada po proizvodu", fontsize=15, color="maroon")
axs[1].set_xlabel("Proizvod", fontsize=12, color="maroon")
axs[1].set_ylabel("Zarada", fontsize=12, color="maroon")
# axs[1].ticklabel_format(style='plain', axis='y') - Sklanja ovo e+107
axs[1].grid(axis="y", linestyle="--", alpha=0.5)

plt.show()


