import json

# Iz python u json
data = {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "published": 1960,
    "genre": "Fiction"
}

json_string = json.dumps(data)
print(json_string)


# Iz json u python
json_string = '{"title": "To Kill a Mockingbird", "author": "Harper Lee", "published": 1960, "genre": "Fiction"}'
 
data = json.loads(json_string)
 
print(data["title"])
print(data["author"])
print(data["published"])
print(data["genre"])