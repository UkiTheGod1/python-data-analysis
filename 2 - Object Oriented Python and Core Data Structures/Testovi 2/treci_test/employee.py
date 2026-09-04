class Employee:
    def __init__(self, name, email, salary, address):
        self.name = name
        self.email = email
        self.salary = salary
        self.address = address

    def check_email(self):
        if "@" in self.email:
            return True
        else:
            return False
        
    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage / 100)