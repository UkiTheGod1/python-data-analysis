import pandas as pd

df = pd.read_csv("books.csv")
print(df.iloc[0].to_string())    # df.iloc se koristi za pristup indexima
print(" ")
print(df.iloc[2:4].to_string())  # prikazivanje vise redova (od 2 do 4 bez 4 - znaci 2. i 3. red)
print(df.iloc[4:7].to_string())  # od pete do sedme