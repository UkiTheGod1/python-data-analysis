import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
sd = df['times_borrowed'].std()
q1 = df['times_borrowed'].quantile(0.25)
q3 = df['times_borrowed'].quantile(0.75)
iqr = q3 - q1
 
print(f"Standard deviation: {sd:.2f}")
print(f"IQR (Q3 - Q1): {iqr:.2f}")

# Ako je standardna devijacija veća od interkvartilnog raspona: 
# postoje ekstremne vrednosti;
# raspodela je razvučena.
 
# Ako su standardna devijacija i interkvartilni raspon približno jednaki:
# nema drastičnih ekstremnih vrednosti;
# raspodela nije mnogo razvučena;
# raspodela je blago asimetrična ili sabijena.

# Ako je interkvartilni raspon približno 1,35 standardne devijacije (IQR ≈ 1,35 × SD):
# nema izraženih ekstremnih vrednosti;
# raspodela je simetrična.