import requests

title = 'To Kill a Mockingbird'
author = 'Harper Lee'
url = f'https://openlibrary.org/search.json?title={title}&author={author}'
response = requests.get(url)
print(response.url) # Umesto razmaka pise %20

url = "https://openlibrary.org/search.json"
params = {"title": title, "author": author}
response = requests.get(url=url, params=params)
print(response.url) # Umesto razmaka pise +