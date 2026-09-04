class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email
     
    def send_email(self, subject, message):
        print(f"Sending email to {self.email}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")

class SalesManager(Employee): # U zagradi stavljamo klasu iz koje vadimo podatke
    def __init__(self, name, email, sales_target):
        super().__init__(name, email) # super().__init__ koristimo da bismo importovali objekte iz pozvane klase
        self.sales_target = sales_target
     
    def track_sales(self):
        print(f"{self.name} is tracking sales towards the target of {self.sales_target}")

class DataAnalyst(Employee):
    def __init__(self, name, email, analysis_tool):
        super().__init__(name, email)
        self.analysis_tool = analysis_tool
     
    def analyze_data(self):
        print(f"{self.name} is analyzing data using {self.analysis_tool}")
 
class Intern(Employee):
    def __init__(self, name, email, project_assigned):
        super().__init__(name, email)
        self.project_assigned = project_assigned
     
    def work_on_project(self):
        print(f"{self.name} is working on {self.project_assigned}")

# Koju god da pozovemo, mozemo koristiti komandu send_email jer se sve pozivaju na Employee i sve imaju isti objekat "email"

# super().send_email - pozivanje funkcija