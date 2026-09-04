import pandas as pd
df = pd.read_csv('books.csv')
df.sort_values(by="title", inplace=True)
print(df.head(30).to_string(columns=['title', 'author'])) # Preko inplace=True (preko originalnog skupa)

sorted_df = df.sort_values(by='year_published') # ascending=False) suprotan smer prikazivanja (logicno)
print(sorted_df.head(30).to_string(columns=['title', 'year_published'])) # Pravi se novi skup "sorted_df"

print(df.loc[0]) #Printovace prvi red u originalno NESORTIRANOM skupu
print(df.iloc[0]) #Printovace prvi red u novom SORTIRANOM skupu
df.reset_index(drop=True, inplace=True) # Resetuje indexe tako da je nebitno da li koristimo LOC ili ILOC

df.sort_values(by=["title", 'author'], inplace=True, ascending=[False, True]) # Sortiranje vise kolona