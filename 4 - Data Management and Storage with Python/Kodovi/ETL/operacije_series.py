import pandas as pd

data = pd.Series([10,20,30,40,50], name='values')

data2 = pd.Series([1,2,3,4,5], name="multipliers")

result = data * data2
print(result)