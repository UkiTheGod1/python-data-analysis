from product import Product
from employee import Employee
from user import User

Smartphone = Product("Smartphone", 1000, 10, "Mobile device")
Monitor = Product("Monitor", 300, 15, "PC peripheral - visual")
Mouse = Product("Mouse", 50, 20, "PC peripheral - interactive")
Headphones = Product("Headphones", 100, 5, "PC pheripheral - audio")
TV = Product("TV", 700, 10, "Living room visuals")

Marko = Employee("Marko", "marko.employee@gmail.com", 1500, "21 Jump Street")
Mirko = Employee("Marko", "marko.employee@gmail.com", 1500, "21 Jump Street")

Ana = User("Ana", "anabanana33", "0645533065", "47 Sesame Street")
Bojana = User("Bojana", "bojana_pvz", "0612516777", "90 Boulevard Street")
Dejan = User("Dejan", "dekimajstor21", "0645936560", "Partisa Lulumbe 26")

products = [Smartphone, Monitor, Mouse, Headphones, TV]
employees = [Marko, Mirko]
users = [Ana, Bojana, Dejan]

# Provera metode check_quantity
for p in products:
    print(f'Product {p.name} has quantity over 10: {p.check_quantity()}')

# Provera metode check_email
for e in employees:
    print(f'Employee {e.name} has a valid email: {e.check_email()}')

# Provera metode increase_salary
for e in employees:
    e.increase_salary(10)
    print(f'Employee {e.name}\'s salary has been raised by 10 percent. New salary: {e.salary}$')

# Provera metode add_product
Ana.add_product(Smartphone)
Ana.add_product(TV)
Bojana.add_product(Mouse)
Bojana.add_product(TV)
Dejan.add_product(Monitor)
Dejan.add_product(Headphones)

# Provera metode total_spent
Ana.total_spent()
Bojana.total_spent()
Dejan.total_spent()
