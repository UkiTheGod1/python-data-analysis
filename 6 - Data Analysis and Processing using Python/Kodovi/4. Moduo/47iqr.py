import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
import pandas as pd
 
q1 = df['times_borrowed'].quantile(0.25)
q3 = df['times_borrowed'].quantile(0.75)
 
iqr = q3 - q1
print(iqr)