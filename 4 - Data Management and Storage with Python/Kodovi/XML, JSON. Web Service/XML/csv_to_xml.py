import pandas as pd
df = pd.read_csv("books.csv")

df.to_xml('books.xml', parser='etree', root_name='library', row_name='book', index=False,  attr_cols=['id'], elem_cols=['title','author','published','genre'])