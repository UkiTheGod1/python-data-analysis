employees = [
    {'name': 'Peter', 'salary': 50000},
    {'name': 'Mila', 'salary': 60000},
    {'name': 'Nemanja', 'salary': 55000}
]
 
employees_with_increased_salaries = list(map(lambda x: {'name': x['name'], 'salary': x['salary'] * 1.05}, employees))
for e in employees_with_increased_salaries:
    print(f"{e['name']} has a new salary: {e['salary']} dinars")



# map funkcija prolazi kroz listu i zamenjuje sve elemente (sve ono iza "lamba x:" ce zameniti trenutni element)