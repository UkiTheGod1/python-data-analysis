import requests
 
# Define input data
title = 'To Kill a Mockingbird'
author = 'Harper Lee'
 
# Create search URL
url = f'https://openlibrary.org/search.json?title={title}&author={author}'
 
# Send request and get response data
response = requests.get(url)
data = response.text
print(data)