class User:
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email
    
    def display_info(self):
        print(f'User: {self.name} {self.surname}, email: {self.email}')
    
u1 = User("Uros", "Djordjic", "uki.burek@gmail.com")
u2 = User("Damjan", "Lazic", "travica00@gmail.com")

u1.display_info()
u2.display_info()