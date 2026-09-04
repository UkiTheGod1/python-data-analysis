# 1. Naš zadatak je da joj pomognemo da kreira Python program koji:

# pita korisnika za ime prvog kupca i broj njegovih kupovina;
# pita korisnika za ime drugog kupca i broj njegovih kupovina;
# izračunava ukupan broj kupovina;
# prikazuje personalizovanu poruku, npr.: „Kupci Alex i Max su zajedno ostvarili 50 kupovina.”

first_customer = input("Enter the name of first customer: ")
first_purchase = int(input("Enter the number of first customer's purchases: "))

second_customer = input("Enter the name of second customer: ")
second_purchase = int(input("Enter the number of second customer's purchases: "))

total_purchases = first_purchase + second_purchase
print(f"Customers {first_customer} and {second_customer} bought a total of {total_purchases} items!")
