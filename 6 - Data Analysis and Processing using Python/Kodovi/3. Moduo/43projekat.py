import pandas as pd
from preprocessing import prepare_data
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
inventory_gap = df.groupby('section').agg({
    'title': 'count',
    'times_borrowed': 'sum'
})
 
inventory_gap['titles_to_borrow_ratio'] = inventory_gap['times_borrowed'] / inventory_gap['title'] 
 
print(inventory_gap.sort_values(by=['titles_to_borrow_ratio'], ascending=False))


best_authors = df.groupby("author").agg(
    titles = ('title', 'count'),
    borrowings = ('times_borrowed', 'sum')
)

best_authors['titles_to_borrow_ratio'] = best_authors['borrowings'] / best_authors['titles']
print(best_authors.sort_values(by=['titles_to_borrow_ratio'], ascending=False))