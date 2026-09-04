import pandas as pd
 
# Otvaramo excel i pravimo praznu listu
df = pd.read_excel('user_rentals.xlsx')
rows = []

# Definisemo danasnji datum
today = pd.Timestamp.today()
 
# Iteriramo kroz svaki red i izbiramo celiju "rental_date" iz reda i oduzimamo ga od danasnjeg datuma
# Ako je ta razlika veca od Timedelta(days=31) to jest 31 dana onda se dodaje u listu rows
for index, row in df.iterrows():
    interval = today - row['rental_date']
    if(interval > pd.Timedelta(days=31)):
        rows.append(row)

# Upisujemo i printujemo
new_df = pd.DataFrame(data=rows, columns=df.columns)
print(new_df)


# Drugi nacin
mask = (pd.Timestamp.today() - df['rental_date']) > pd.Timedelta(days=31)
new_df = df[mask]
print(new_df)