import pandas as pd
 
df = pd.DataFrame(data=[[101, "The Alchemist", "Paulo Coelho", 1988, "Adventure"]], columns=['id', 'title', 'author', 'published', 'genre'])
 
df.to_csv('my_book.csv', index=False)