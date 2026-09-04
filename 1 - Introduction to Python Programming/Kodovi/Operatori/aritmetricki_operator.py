broj_kupaca_jan = 1200
broj_kupaca_feb = 950

ukupno_kupaca = broj_kupaca_jan + broj_kupaca_feb

print("Ukupni broj kupaca je: ", ukupno_kupaca)

vrednost_jan = 4500
broj_dana = 31

dnevni_prihod_jan = vrednost_jan / broj_dana
print(type(dnevni_prihod_jan))
print("Prosecna vrednost po danu za januar je :", dnevni_prihod_jan)

items_no = 100
employee_no = 35

items_per_employee = items_no // employee_no
print(type(items_per_employee))
print("Svaki zaposleni ce dobiti po",items_per_employee, "poklona")

leftover_items = items_no % employee_no
print(type(leftover_items))
print("Ostalo je",leftover_items, "poklona")