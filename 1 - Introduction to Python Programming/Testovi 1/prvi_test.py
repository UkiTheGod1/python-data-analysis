mon_cus = int(input("Unesi broj kupaca za ponedeljak: "))
tue_cus = int(input("Unesi broj kupaca za utorak: "))
wed_cus = int(input("Unesi broj kupaca za sredu: "))
thu_cus = int(input("Unesi broj kupaca za cetvrtak: "))
fri_cus = int(input("Unesi broj kupaca za petak: "))
sat_cus = int(input("Unesi broj kupaca za subotu: "))
sun_cus = int(input("Unesi broj kupaca za nedelju: "))

total_cus = mon_cus + tue_cus + wed_cus + thu_cus + fri_cus + sat_cus + sun_cus
total_cus_weekend = sat_cus + sun_cus
total_cus_weekday = total_cus - total_cus_weekend
print(f"Ukupan broj kupaca za celu nedelju je {total_cus}")
print(f"Ukupan broj kupaca za radne dane je {total_cus_weekday}")
print(f"Ukupan broj kupaca za vikend je {total_cus_weekend}")

print("Da li je u nedelju bilo vise kupaca nego u subotu? -", sun_cus > sat_cus)

print("Da li je za 5 radnih dana bilo vise kupaca nego za 2 dana vikenda? -", \
      total_cus_weekday > total_cus_weekend)

print("Da li je te nedelje bilo vise od 1000 kupaca ili je za vikend bilo vise od 500 kupaca? -", \
      total_cus > 1000 or total_cus_weekend > 500)

input("Press ENTER to exit")