from klase import Employee, User, Product

# Iskoristio sam liste iz proslog task-a, da ne gubim vreme radeci potpuno isti zadatak

Smartphone = Product("Smartphone", 1000, 10, "Mobile device")
Monitor = Product("Monitor", 300, 15, "PC peripheral - visual")
Mouse = Product("Mouse", 50, 20, "PC peripheral - interactive")
Headphones = Product("Headphones", 100, 5, "PC pheripheral - audio")
TV = Product("TV", 700, 10, "Living room visuals")

Marko = Employee("Marko", "marko.employee@gmail.com", "21 Jump Street", 1500)
Mirko = Employee("Marko", "marko.employee@gmail.com", "21 Jump Street", 1500)

Ana = User("Ana", "47 Sesame Street", "anabanana33", "0645533065")
Bojana = User("Bojana", "90 Boulevard Street", "bojana_pvz", "0612516777")
Dejan = User("Dejan", "Partisa Lulumbe 26", "dekimajstor21", "0645936560")

products = [Smartphone, Monitor, Mouse, Headphones, TV]
employees = [Marko, Mirko]
users = [Ana, Bojana, Dejan]

# Dodavanje proizvoda u shopping_history
Ana.add_product(Smartphone)
Ana.add_product(TV)
Bojana.add_product(Mouse)
Bojana.add_product(TV)
Dejan.add_product(Monitor)
Dejan.add_product(Headphones)

# Prikazivanje ukupno potrosenog iznosa
print("\nUsers:")
for u in users:
    u.display_info()
    u.total_spent()

print("\nEmployees:")
for e in employees:
    e.display_info()
    