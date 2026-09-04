import pandas as pd

data = {
    'lista' : [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000],
    'lista2' : [1, 2, 3, 4, 5, 7, 7, 12, 12, 15, 17, 20]
    }
df = pd.DataFrame(data)

# Prva lista
print("Prosek prve liste:", df["lista"].mean())
print("Mediana prve liste:", df["lista"].median())
print("Mod prve liste:", (", ").join(df["lista"].mode().astype(str)))
print("STD prve liste:", df["lista"].std())

q1_lista = df["lista"].quantile(0.25)
q3_lista = df["lista"].quantile(0.75)
iqr = q3_lista - q1_lista
print("IQR prve liste:", iqr, "\n")

# Druga lista
print("Prosek druge liste:", df["lista2"].mean())
print("Mediana druge liste:", df["lista2"].median())

mode2 = df["lista2"].mode().astype(str) 
# Pretvaramo u string jer komanda ".join()" ocekuje string, a lista sadrzi brojeve (integer)
print("Mod druge liste:", (", ").join(mode2))
# Spajamo (join) u slucaju da ima vise vrednosti koje se pojavljuju najvise puta

print("STD druge liste:", df["lista2"].std())

q1_lista2 = df["lista2"].quantile(0.25)
q3_lista2 = df["lista2"].quantile(0.75)
iqr2 = q3_lista2 - q1_lista2
print("IQR prve liste:", iqr2)