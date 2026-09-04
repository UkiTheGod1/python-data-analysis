import abc
class Person(abc.ABC):
    def __init__(self, name, email, address):
        self.name = name
        self._email = email
        self._address = address
    
    def get_email(self):
        return self._email
    
    def set_email(self, email):
        self._email = email
        print(f"The email was set to: {self._email}")

    def get_address(self):
        return self._address
    
    def set_address(self, address):
        self._address = address
        print(f"The address was set to: {self._address}")
    
    def check_email(self):
        if "@" in self._email:
            return True
        else:
            return False
        
    @abc.abstractmethod
    def display_info(self):
        pass


class Employee(Person):
    def __init__(self, name, email, address, salary):
        super().__init__(name, email, address)
        self.__salary = salary

    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        self.__salary = salary
    
    def increase_salary(self, percentage):
        self.__salary += self.__salary * (percentage / 100)
    
    def display_info(self):
        print(f"Name: {self.name}, email: {self._email}, address: {self._address}, salary: {self.__salary}")

class User(Person):
    def __init__(self, name, address, username, phone):
        super().__init__(name, "", address) # Koristimo prazno polje jer nam ne treba "email" iz klase Person
        self.phone = phone
        self.username = username
        self.shopping_history = []

    def get_phone(self):
        return self.phone
    
    def set_phone(self, phone):
        self.phone = phone

    def add_product(self, product):
        self.shopping_history.append(product)
        print(f"Product {product.name} has been added to shopping history list.")

    def total_spent(self):
        total = sum(product.get_price() for product in self.shopping_history)
        print(f"Total spent amount: {total}$")
    
    def display_info(self):
        print(f"Name: {self.name}, username: {self.username}, address: {self._address}, phone: {self.phone}")

class Product:
    def __init__(self, name, price, quantity, description):
        self.name = name
        self.__price = price
        self.quantity = quantity
        self._description = description
    
    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print(f'Price cannot be negative')
    
    def get_description(self):
        return self._description
    
    def set_description(self, description):
        self._description = description

    def check_quantity(self):
        if self.quantity >= 10:
            return True
        elif self.quantity < 0:
            print(f"Quantity cannot be negative! Change immediately! - Product: {self.name}")
        else:
            return False
