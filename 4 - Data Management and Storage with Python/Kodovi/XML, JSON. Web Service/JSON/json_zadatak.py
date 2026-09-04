import json

with open("data.json") as file:
    data = json.load(file)
    courses = data['courses']
    print(courses)