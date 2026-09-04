import pandas as pd
 
df = pd.read_csv('books.csv')  # read_csv je pandas funkcija, a df je DataFrame isto pandas 
print(df.to_string())          # Pretvorili u string iz gasa
print(df.shape)                # Pokazuje broj redova i kolona (df.shape[0] - redovi, df.shape[1] - kolone)