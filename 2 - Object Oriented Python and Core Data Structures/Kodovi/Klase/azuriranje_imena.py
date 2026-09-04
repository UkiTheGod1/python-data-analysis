class Employee:
    company_name = "TechCorp"  # Static field
 
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    @staticmethod
    def set_company_name(new_name):
        Employee.company_name = new_name
        print(f'New name is {Employee.company_name}')

Employee.set_company_name("KidareCOO")