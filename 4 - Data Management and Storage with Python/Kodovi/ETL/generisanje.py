import pandas as pd

df = pd.read_excel("user_rentals.xlsx")

# df['new_column'] = 0  Pravi se nova kolona i svim redovima se dodeljuje vrednost 0

# df['new_column'] = df['column1'] + df['column2'] Pravi se nova kolona i upisuje se zbir prve dve kolone

mask = (pd.Timestamp.today() - df['rental_date']) > pd.Timedelta(days=31)
new_df = df[mask]

new_df2 = new_df.sort_values(by='rental_date', ascending=True)

new_df2['overdue_days'] = (pd.Timestamp.today() - new_df2['rental_date']).dt.days - 31 
# .dt.days od razlike datuma pretvara sve u broj dana (bice obican broj) i odbijamo 31 dan jer tad je legalno imao knjige.

print(new_df2)