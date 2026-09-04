class User:
    def __init__(self, name, age, balance):
        self.__name = name
        self.__age = age
        self.__balance = balance
    
    def get_age(self):
        return self.__age
    
    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print("Uneli ste pogresnu vrednost godina!")
    
    def add_balance(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Unesi ste pogresnu vrednost!")
    def withdraw_balance(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
        else:
            print("Nemoguce je podici vise novca nego sto imate.")
    def display_user_info(self):
        print(f'Korisnik {self.__name} ima {self.__age} godina i na racunu ima {self.__balance}$')

u1 = User("Marko", 18, 2000)

u1.set_age(19)
u1.display_user_info()

u1.add_balance(1000)
u1.display_user_info()
u1.withdraw_balance(1500)
u1.withdraw_balance(3000)
u1.display_user_info()




