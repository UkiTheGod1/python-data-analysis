import pandas as pd
 
df = pd.read_excel('user_rentals.xlsx')
 
month = df.loc[1, 'rental_date'].month
# print(month)

today = pd.Timestamp.today()
# print(today)

diff = today - df.loc[1, 'rental_date']  # Razlika izmedju danasnjeg datuma i datuma u odredjenoj celiji
# print(diff)

if diff.days > 31:
    print(f"Nije predao na vreme: {diff.days} dana")
else:
    print(f"Korisnik je i dalje u roku: {diff.days} dana")


# print(diff > pd.Timedelta(days=31)) # Izbacuje True jer je razlika veca od 31 dana
