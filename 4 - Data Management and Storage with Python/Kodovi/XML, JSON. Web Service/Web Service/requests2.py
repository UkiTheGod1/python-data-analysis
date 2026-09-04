import requests
 
# Define input data
title = 'To Kill a Mockingbird'
author = 'Harper Lee'
 
# Create search URL
url = f'https://openlibrary.org/search.json?title={title}&author={author}'
 
# Send request and get response data
response = requests.get(url)
data = response.json()

first_book = data["docs"][0]

print(first_book["first_sentence"])
print(first_book["subject"])
print(first_book["place"])
print(first_book["time"]) 
# Ne znam zasto ne radi