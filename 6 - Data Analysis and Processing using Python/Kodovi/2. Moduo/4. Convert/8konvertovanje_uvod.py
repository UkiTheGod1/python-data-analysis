import pandas as pd
data = {
    'id': [1, 2, 3, 4],
    'value': ['10', '20', '30', '40']
}
df = pd.DataFrame(data)
df['value'] = df['value'].astype(int)
print(df.dtypes)

# Koristi df.info !