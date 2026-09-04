person = {
    "name": "John",
    "age": 27
}

print(person["name"])

person["occupation"] = "barista"
print(person)

person["age"] = 21
print(person)

josh = person.copy()
josh["name"] = "Josh"
print(josh)

del person["age"]
print(person)